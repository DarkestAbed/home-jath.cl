---
title: jath.cl
summary: Este sitio. Landing personal en FastHTML que se alimenta de Markdown y comparte el sistema de diseño del blog.
year: 2026
status: en desarrollo
role: diseño y desarrollo
stack: [Python, FastHTML, Markdown, Pygments, PicoCSS]
url: https://jath.cl
featured: true
order: 1
---

## Qué es

La puerta de entrada a todo lo demás: quién soy, qué hago, en qué estoy
trabajando y dónde encontrarme. Comparte tipografías, paleta y componentes
con [blog.jath.cl](https://blog.jath.cl), así que pasar de uno a otro se
siente como el mismo lugar.

## Cómo está hecho

- **FastHTML** genera el HTML en el servidor, directo desde Python.
- Todo el contenido vive en archivos **Markdown** con *front matter* YAML.
- **Pygments** resalta el código al renderizar, sin JavaScript en el cliente.
- El tema claro/oscuro usa la misma cookie que el blog, compartida en `*.jath.cl`.

Los bloques de código del Markdown se extraen antes de renderizar y se
reemplazan por HTML resaltado:

```python
def render(text: str) -> str:
    blocks: list[str] = []

    def stash(m: re.Match) -> str:
        blocks.append(highlight_code(m["code"], m["lang"]))
        return "\n\n" + PLACEHOLDER.format(len(blocks) - 1) + "\n\n"

    html = markdown.markdown(FENCE.sub(stash, text), extensions=MD_EXTENSIONS)
    for i, block in enumerate(blocks):
        html = html.replace(f"<p>{PLACEHOLDER.format(i)}</p>", block)
    return html
```
