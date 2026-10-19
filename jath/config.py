"""Site-wide settings: identity, paths and navigation."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"
STATIC_DIR = ROOT / "static"

SITE = {
    "name": "Javier Thompson punto Ce Ele",
    "short": "jath.cl",
    "author": "Javier Thompson",
    "url": "https://jath.cl",
    "blog_url": "https://blog.jath.cl",
    "lang": "es",
    "description": "Javier Thompson — desarrollador y tecnólogo.",
}

# (label, href). Local paths get `aria-current` when active.
NAV = [
    ("Sobre mí", "/sobre-mi"),
    ("Skills", "/skills"),
    ("Proyectos", "/proyectos"),
    ("Blog", "/blog"),
    ("Contacto", "/contacto"),
]
