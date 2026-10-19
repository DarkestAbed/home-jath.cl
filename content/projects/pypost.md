---
title: pypost
summary: Motor de blog minimalista y bilingüe. Sin build, sin base de datos, sin frameworks de JavaScript; solo Markdown y una app Python. Corre detrás de blog.jath.cl.
year: 2026
status: en producción
role: autor
stack: [Python, FastHTML, Mistune, Pygments, PicoCSS, Copier]
repo: https://github.com/DarkestAbed/pypost
url: https://blog.jath.cl
featured: true
order: 1
---

## Qué es

Un framework de blog sin CMS ni base de datos: los posts son archivos de
texto plano que se parsean al compilar, y el sitio se distribuye como
plantilla de [Copier](https://copier.readthedocs.io) para crear nuevas
instancias y actualizarlas.

## Características

- Resaltado de sintaxis en el servidor con Pygments.
- Índice de contenidos y navegación entre artículos de una serie.
- Tema claro/oscuro con paleta inspirada en SynthWave '84.
- Bilingüe: español, inglés o ambos.
- Etiquetas, paginación, feed RSS y metadatos Open Graph.
- Separación entre `custom.css` (del motor) y `theme.css` (de cada instancia).

Crear un blog nuevo es un solo comando; Copier pregunta nombre, autor,
idiomas y URL, y entrega un repo listo, con tests pasando. Las mejoras del
motor se traen después con `uvx copier update --trust`.

```bash
uvx copier copy --trust gh:darkestabed/pypost my-blog
cd my-blog && uv run python main.py
```

Y cada post es Markdown con *front matter*:

```yaml
---
title: Cómo Kubernetes decide dónde ejecutar un Pod
date: 2026-03-15
tags: [kubernetes, infraestructura, devops]
series: kubernetes-internals
---
```
