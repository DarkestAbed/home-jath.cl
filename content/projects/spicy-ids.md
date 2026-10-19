---
title: spicy ids
summary: Módulo Python para generar identificadores con prefijo de tipo, al estilo de los IDs de Stripe.
year: 2024
status: estable
role: autor
stack: [Python, packaging]
repo: https://github.com/DarkestAbed/python-spicyids
featured: true
order: 3
---

## La idea

Inspirado en [django-spicy-id](https://github.com/mik3y/django-spicy-id):
identificadores no referenciales que dicen qué son y no revelan cuántos
registros existen, a diferencia de los IDs autoincrementales.

```text
<identificador_objeto>_<cadena aleatoria>[-<timestamp enmascarado>]
```

Por ejemplo, `rec_` para registros o `row_` para filas, seguido de una
cadena aleatoria única.
