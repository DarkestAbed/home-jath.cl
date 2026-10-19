import pytest
from starlette.testclient import TestClient

from jath.config import NAV
from jath.content import collection, load, render
from main import app

client = TestClient(app)


@pytest.mark.parametrize("path", ["/", *[h for _, h in NAV]])
def test_pages_render(path):
    r = client.get(path)
    assert r.status_code == 200
    assert 'class="site-nav"' in r.text
    assert 'class="site-footer"' in r.text
    assert "©" in r.text


def test_every_project_has_a_page():
    for p in collection("projects"):
        assert client.get(f"/proyectos/{p.slug}").status_code == 200


@pytest.mark.parametrize("path", ["/no-existe", "/proyectos/no-existe", "/proyectos/../pyproject"])
def test_not_found(path):
    r = client.get(path)
    assert r.status_code == 404
    assert "not-found" in r.text


def test_static_assets():
    for f in ["custom.css", "theme.css", "site.css", "pygments.css", "fonts/inter-var.woff2"]:
        assert client.get(f"/static/{f}").status_code == 200


def test_blog_digest_links_to_blog():
    html = client.get("/blog").text
    posts = load("pages/blog").posts
    assert posts
    for post in posts:
        assert post["url"].startswith("https://blog.jath.cl/")
        assert post["url"] in html


def test_code_blocks_are_highlighted():
    html = render("```python\nx = 1\n```")
    assert 'class="code-block"' in html
    assert '<span class="code-lang">python</span>' in html
    assert 'class="highlight"' in html
