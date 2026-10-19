"""URL routes. Each page pulls its copy from a Markdown file in content/."""

from fasthtml.common import A, Article, Div, H1, H2, Li, NotStr, P, Section, Span, Ul
from starlette.exceptions import HTTPException

from .components import (
    button, channel_list, digest_card, fecha, meta_line, page_header,
    project_card, prose, section, tags,
)
from .config import SITE
from .content import collection, load
from .layout import ext_link, page


async def not_found(request, exc):
    return page("404", Div(H1("404"), P("Esta página no existe."),
                           A("← Volver al inicio", href="/", cls="back-link"),
                           cls="not-found"),
                path=request.url.path)


def hero(doc):
    return Section(
        Div(
            P(doc.kicker, cls="hero-kicker"),
            H1(doc.title),
            P(doc.tagline, cls="hero-tagline"),
            P(doc.lead, cls="hero-lead"),
            Div(*[button(c["label"], c["href"], c.get("ghost", False)) for c in doc.ctas],
                cls="hero-actions"),
            cls="hero-copy",
        ),
        Div(
            Div(Span(cls="dot"), Span(cls="dot"), Span(cls="dot"),
                Span(doc.get("terminal_title", ""), cls="terminal-title"),
                cls="terminal-bar", aria_hidden="true"),
            NotStr(doc.html),
            cls="hero-terminal",
        ),
        cls="hero",
    )


def focus_grid(items):
    return Ul(*[Li(Span(f"{i:02d}", cls="focus-index"), H2(f["title"]), P(f["text"]))
                for i, f in enumerate(items, 1)],
              cls="focus-grid")


def register(rt):
    @rt("/")
    def home():
        doc = load("pages/home")
        featured = [p for p in collection("projects") if p.get("featured")]
        posts = load("pages/blog").posts[:3]
        return page(
            "",
            hero(doc),
            section("Lo que hago", focus_grid(doc.focus)),
            section("Proyectos destacados",
                    Div(*[project_card(p) for p in featured], cls="card-grid card-grid-4"),
                    more=("Todos los proyectos →", "/proyectos")),
            section("Últimas del blog",
                    Div(*[digest_card(p, with_notes=False) for p in posts], cls="card-grid"),
                    more=("Resumen del blog →", "/blog")),
            Section(
                Div(H2(doc.cta["title"]), P(doc.cta["text"])),
                Div(button("Contacto", "/contacto"),
                    button("blog.jath.cl ↗", SITE["blog_url"], ghost=True),
                    cls="hero-actions"),
                cls="cta-band",
            ),
        )

    @rt("/sobre-mi")
    def about():
        doc = load("pages/about")
        return page(doc.title, page_header(doc.title, doc.subtitle), prose(doc),
                    path="/sobre-mi", description=doc.subtitle)

    @rt("/skills")
    def skills():
        doc = load("pages/skills")
        groups = [
            Article(H2(g["name"]), P(g["text"], cls="post-description"), tags(g["items"]),
                    cls="skill-group")
            for g in doc.groups
        ]
        return page(doc.title, page_header(doc.title, doc.subtitle),
                    Div(*groups, cls="skill-grid"), prose(doc),
                    path="/skills", description=doc.subtitle)

    @rt("/proyectos")
    def projects():
        doc = load("pages/projects")
        return page(doc.title, page_header(doc.title, doc.subtitle), prose(doc),
                    Div(*[project_card(p) for p in collection("projects")], cls="card-grid"),
                    path="/proyectos", description=doc.subtitle)

    @rt("/proyectos/{slug}")
    def project(slug: str):
        p = {d.slug: d for d in collection("projects")}.get(slug)
        if p is None:
            raise HTTPException(404)
        links = [ext_link(label, href=href, cls="read-more")
                 for label, href in (("Repositorio ↗", p.get("repo")), ("Sitio ↗", p.get("url")))
                 if href]
        return page(
            p.title,
            Div(
                Span("Proyecto", cls="series-label"),
                H1(p.title),
                meta_line(str(p.get("year", "")), p.get("status"), p.get("role")),
                P(p.summary, cls="post-description"),
                tags(p.get("stack", [])),
                Div(*links, cls="project-links") if links else None,
                cls="post-header",
            ),
            prose(p, cls="about-body post-body"),
            Div(A("← Todos los proyectos", href="/proyectos", cls="back-link"), cls="post-footer"),
            path=f"/proyectos/{slug}", description=p.summary,
        )

    @rt("/blog")
    def blog():
        doc = load("pages/blog")
        return page(
            doc.title,
            page_header(doc.title, f"{doc.subtitle} · actualizado el {fecha(doc.updated)}"),
            prose(doc),
            Div(*[digest_card(p) for p in doc.posts], cls="post-list"),
            Div(button("Ir a blog.jath.cl ↗", SITE["blog_url"]), cls="blog-more"),
            path="/blog", description=doc.subtitle,
        )

    @rt("/contacto")
    def contact():
        doc = load("pages/contact")
        return page(doc.title, page_header(doc.title, doc.subtitle),
                    channel_list(doc.channels), prose(doc),
                    path="/contacto", description=doc.subtitle)
