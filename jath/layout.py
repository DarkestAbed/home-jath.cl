"""Page shell: <head>, navbar and footer, mirroring blog.jath.cl markup."""

from datetime import date

from fasthtml.common import (
    A, Body, Button, Div, Footer, Head, Html, Li, Link, Main, Meta, Nav, NotStr,
    P, Script, Span, Title, Ul,
)

from .config import NAV, SITE

# Same theme handling as the blog. The cookie is written for the parent
# domain when served from *.jath.cl, so the choice carries across sites.
THEME_INIT = """
(function(){
  var m = document.cookie.match(/(?:^|;\\s*)theme=([^;]+)/);
  var t = m ? m[1] : (matchMedia('(prefers-color-scheme: light)').matches ? 'light' : null);
  if (t) document.documentElement.setAttribute('data-theme', t);
})();
"""

SITE_JS = """
function toggleTheme() {
  var h = document.documentElement, n = h.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
  h.setAttribute('data-theme', n);
  var c = 'theme=' + n + ';path=/;max-age=31536000;samesite=lax';
  if (location.protocol === 'https:') c += ';secure';
  if (/(^|\\.)jath\\.cl$/.test(location.hostname)) c += ';domain=jath.cl';
  document.cookie = c;
}
function toggleNav(btn) {
  var nav = btn.closest('.site-nav'), open = nav.toggleAttribute('data-open');
  btn.setAttribute('aria-expanded', open);
}
function copyCode(btn) {
  var block = btn.closest('.code-block').querySelector('.highlight pre');
  var text = block ? block.innerText : '';
  navigator.clipboard.writeText(text).then(function() {
    btn.textContent = 'copied!';
    setTimeout(function(){ btn.textContent = 'copy'; }, 1500);
  });
}
"""

STYLESHEETS = ["vendor/pico.classless.min.css", "pygments.css", "custom.css", "theme.css", "site.css"]


def is_external(href: str) -> bool:
    return href.startswith(("http://", "https://", "mailto:"))


def ext_link(*children, href: str, **kw):
    """Anchor that opens off-site links in a new tab."""
    if is_external(href) and not href.startswith("mailto:"):
        kw |= {"target": "_blank", "rel": "noopener"}
    return A(*children, href=href, **kw)


def site_nav(path: str):
    def item(label, href):
        current = not is_external(href) and (path == href or path.startswith(href + "/"))
        return Li(ext_link(label, href=href, aria_current="page" if current else None))

    return Nav(
        Div(
            A(Span(SITE["name"], cls="brand-full"), Span(SITE["short"], cls="brand-short"),
              href="/", cls="nav-brand", aria_label=SITE["name"]),
            Ul(*[item(l, h) for l, h in NAV], cls="nav-links", id="nav-links"),
            Div(Button("menú", cls="nav-toggle", onclick="toggleNav(this)",
                       aria_expanded="false", aria_controls="nav-links"),
                Button("☀ / ☾", cls="theme-btn", onclick="toggleTheme()",
                       aria_label="Cambiar tema claro/oscuro"),
                cls="nav-controls"),
            cls="nav-inner",
        ),
        cls="site-nav",
    )


def site_footer():
    return Footer(
        P(f"© {date.today().year} {SITE['author']} · ",
          A(SITE["short"], href="/"), " · ",
          ext_link("blog.jath.cl", href=SITE["blog_url"])),
        cls="site-footer",
    )


def page(title: str, *content, path: str = "/", description: str | None = None):
    """Full HTML document. `title=None`-ish empty string gives the bare site name."""
    full_title = f"{title} | {SITE['name']}" if title else SITE["name"]
    desc = description or SITE["description"]
    url = SITE["url"] + path
    return Html(
        Head(
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1, viewport-fit=cover"),
            Title(full_title),
            Meta(name="description", content=desc),
            Meta(property="og:site_name", content=SITE["name"]),
            Meta(property="og:type", content="website"),
            Meta(property="og:title", content=full_title),
            Meta(property="og:description", content=desc),
            Meta(property="og:url", content=url),
            Meta(name="twitter:card", content="summary"),
            Link(rel="canonical", href=url),
            Link(rel="icon", href="/static/favicon.svg", type="image/svg+xml"),
            Script(NotStr(THEME_INIT)),
            *[Link(rel="stylesheet", href=f"/static/{s}") for s in STYLESHEETS],
            Script(NotStr(SITE_JS)),
        ),
        Body(site_nav(path), Main(*content, cls="container"), site_footer()),
        data_theme="dark",
        lang=SITE["lang"],
    )
