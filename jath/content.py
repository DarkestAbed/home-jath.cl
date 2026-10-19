"""Markdown documents with YAML front matter, rendered to HTML.

Fenced code blocks are highlighted with Pygments and wrapped in the same
`.code-block` markup the blog uses, so its stylesheet applies as-is.
"""

import re
from dataclasses import dataclass, field
from datetime import date
from functools import lru_cache
from pathlib import Path

import markdown
import yaml
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import TextLexer, get_lexer_by_name
from pygments.util import ClassNotFound

from .config import CONTENT_DIR

FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.S)
FENCE = re.compile(
    r"^(?P<fence>```|~~~)[ \t]*(?P<lang>[\w+#.-]*)[^\n]*\n(?P<code>.*?)\n(?P=fence)[ \t]*$",
    re.M | re.S,
)
PLACEHOLDER = "JATHCODEBLOCK{}"
FORMATTER = HtmlFormatter(cssclass="highlight")
MD_EXTENSIONS = ["tables", "toc", "attr_list", "sane_lists", "smarty"]


@dataclass
class Doc:
    slug: str
    meta: dict = field(default_factory=dict)
    html: str = ""

    def __getattr__(self, key):
        # Front matter keys read as attributes: doc.title, doc.summary, ...
        try:
            return self.__dict__["meta"][key]
        except KeyError:
            raise AttributeError(key) from None

    def get(self, key, default=None):
        return self.meta.get(key, default)


def highlight_code(code: str, lang: str = "") -> str:
    try:
        lexer = get_lexer_by_name(lang) if lang else TextLexer()
    except ClassNotFound:
        lexer = TextLexer()
    label = f'<span class="code-lang">{lang}</span>' if lang else ""
    return (
        f'<div class="code-block">{label}'
        '<button class="copy-btn" onclick="copyCode(this)">copy</button>'
        f"{highlight(code, lexer, FORMATTER)}</div>"
    )


def render(text: str) -> str:
    """Markdown → HTML, with fenced code highlighted by Pygments."""
    blocks: list[str] = []

    def stash(m: re.Match) -> str:
        blocks.append(highlight_code(m["code"], m["lang"]))
        return "\n\n" + PLACEHOLDER.format(len(blocks) - 1) + "\n\n"

    html = markdown.markdown(FENCE.sub(stash, text), extensions=MD_EXTENSIONS)
    for i, block in enumerate(blocks):
        html = html.replace(f"<p>{PLACEHOLDER.format(i)}</p>", block)
    return html


def parse(text: str, slug: str = "") -> Doc:
    meta, body = {}, text
    if m := FRONT_MATTER.match(text):
        meta = yaml.safe_load(m[1]) or {}
        body = text[m.end():]
    return Doc(slug=slug, meta=meta, html=render(body))


@lru_cache
def load(path: str) -> Doc:
    """Load `content/<path>.md`, e.g. load("pages/home")."""
    file = CONTENT_DIR / f"{path}.md"
    return parse(file.read_text(encoding="utf-8"), slug=file.stem)


def _sort_key(doc: Doc):
    # Explicit `order` first, then newest `date` first.
    d = doc.get("date") or date.min
    return (doc.get("order", 999), -d.toordinal() if isinstance(d, date) else 0)


@lru_cache
def collection(folder: str) -> list[Doc]:
    """All documents in `content/<folder>/`, sorted by order then date."""
    files = sorted(Path(CONTENT_DIR / folder).glob("*.md"))
    docs = [load(f"{folder}/{f.stem}") for f in files if not f.stem.startswith("_")]
    return sorted(docs, key=_sort_key)
