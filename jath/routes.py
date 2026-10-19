"""URL routes. Each page pulls its copy from a Markdown file in content/."""

from fasthtml.common import Div, H1, NotStr, P

from .content import load
from .layout import page


async def not_found(request, exc):
    return page("404", Div(H1("404"), P("Esta página no existe."), cls="not-found"),
                path=request.url.path)


def register(rt):
    @rt("/")
    def home():
        doc = load("pages/home")
        return page(
            "",
            Div(H1(doc.title), P(doc.tagline, cls="page-subtitle"), cls="page-header"),
            Div(NotStr(doc.html), cls="about-body"),
        )
