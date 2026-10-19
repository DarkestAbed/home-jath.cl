# jath.cl

Personal landing site for Javier Thompson — developer and technologist.
Served at <https://jath.cl> and <https://www.jath.cl>; the blog lives at
<https://blog.jath.cl>.

## Stack

- [FastHTML](https://fastht.ml) for pages and routing
- Markdown + YAML front matter for all copy (`content/`)
- Pygments for code highlighting
- The blog's design system: Pico classless + `custom.css` (layout) +
  `theme.css` (tokens), extended by `static/site.css`

## Run

```bash
uv sync
uv run python main.py      # http://localhost:5001
uv run pytest              # smoke tests
```

## Layout

```
main.py            app entry point
jath/config.py     site identity, navigation
jath/content.py    Markdown loader + Pygments highlighting
jath/layout.py     <head>, navbar, footer
jath/routes.py     pages
content/pages/     one Markdown file per page (blog.md holds the blog digest)
content/projects/  one Markdown file per project
static/            CSS, fonts, favicon
```

## Design system

`static/custom.css`, `static/theme.css`, `static/pygments.css`, the fonts and
`static/vendor/pico.classless.min.css` are copied verbatim from
blog.jath.cl. Re-sync them from there rather than editing them here; put
site-only rules in `static/site.css`, using the theme tokens only.
