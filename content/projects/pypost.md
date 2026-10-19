---
title: pypost
summary: Motor de blog limpio y desplegable con Python, FastHTML y Markdown. Es lo que corre detrás de blog.jath.cl.
year: 2026
status: en producción
role: autor
stack: [Python, FastHTML, Mistune, Pygments, PicoCSS, Copier]
url: https://blog.jath.cl
featured: true
order: 2
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
- Etiquetas, paginación, feed RSS y metadatos Open Graph.
- Separación entre `custom.css` (del motor) y `theme.css` (de cada instancia).

```yaml
---
title: Cómo Kubernetes decide dónde ejecutar un Pod
date: 2026-03-15
tags: [kubernetes, infraestructura, devops]
series: kubernetes-internals
---
```
