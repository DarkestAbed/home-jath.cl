"""Reusable page blocks. Class names follow the blog's custom.css where a
matching component exists (post-card, tag, read-more, page-header...)."""

from datetime import date

from fasthtml.common import A, Article, Div, H1, H2, Li, NotStr, P, Section, Span, Ul

from .config import SITE
from .content import Doc, render
from .layout import ext_link

MONTHS = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
          "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def fecha(d: date) -> str:
    """6 de mayo de 2026 — same format as the blog."""
    return f"{d.day} de {MONTHS[d.month - 1]} de {d.year}"


def page_header(title, subtitle=None):
    return Div(H1(title), P(subtitle, cls="page-subtitle") if subtitle else None,
               cls="page-header")


def prose(doc: Doc, cls="about-body"):
    return Div(NotStr(doc.html), cls=cls)


def section(title, *content, more=None, cls=""):
    """Home-page section with an optional `(label, href)` link in the header."""
    head = Div(H2(title), ext_link(more[0], href=more[1], cls="read-more") if more else None,
               cls="section-head")
    return Section(head, *content, cls=f"section {cls}".strip())


def tags(names, href=None):
    """Tag chips. With `href`, each links to href.format(tag)."""
    def chip(t):
        return A(t, href=href.format(t), cls="tag") if href else Span(t, cls="tag")
    return Div(*[chip(t) for t in names], cls="post-tags") if names else None


def meta_line(*parts):
    parts = [p for p in parts if p]
    items = []
    for i, p in enumerate(parts):
        if i:
            items.append(Span(" · "))
        items.append(Span(p))
    return P(*items, cls="post-meta")


def button(label, href, ghost=False):
    return ext_link(label, href=href, cls="btn btn-ghost" if ghost else "btn")


# ── Projects ──

def project_card(p: Doc):
    return Article(
        H2(A(p.title, href=f"/proyectos/{p.slug}")),
        meta_line(str(p.get("year", "")), p.get("status")),
        P(p.summary, cls="post-description"),
        tags(p.get("stack", [])),
        A("Ver proyecto →", href=f"/proyectos/{p.slug}", cls="read-more"),
        cls="post-card",
    )


# ── Blog digest ──

def blog_tag_url():
    return SITE["blog_url"] + "/tags/{}"


def digest_card(post: dict, with_notes=True):
    """One entry of the `posts` list in content/pages/blog.md."""
    notes = post.get("notes") if with_notes else None
    return Article(
        H2(ext_link(post["title"], href=post["url"])),
        meta_line(fecha(post["date"]), f"{post['reading_time']} min de lectura"),
        P(post["summary"], cls="post-description"),
        Div(NotStr(render("\n".join(f"- {n}" for n in notes))), cls="digest-notes")
        if notes else None,
        tags(post.get("tags", []), href=blog_tag_url()),
        ext_link("Leer en el blog ↗", href=post["url"], cls="read-more"),
        cls="post-card",
    )


# ── Contact ──

def channel_card(c: dict):
    return Li(ext_link(
        Span(c["label"], cls="channel-label"),
        Span(c["value"], cls="channel-value"),
        Span(c.get("note", ""), cls="channel-note") if c.get("note") else None,
        href=c["href"], cls="channel",
    ))


def channel_list(channels):
    return Ul(*[channel_card(c) for c in channels], cls="channel-list")
