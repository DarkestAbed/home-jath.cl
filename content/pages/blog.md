---
title: Del blog
subtitle: Resumen de lo publicado en blog.jath.cl
updated: 2026-10-19
# Newest first. Add an entry here when a new post goes live.
posts:
- title: Self hosting
  date: 2026-05-06
  url: https://blog.jath.cl/posts/es/self-hosting
  reading_time: 5
  tags:
  - self-hosted
  - home-lab
  summary: Primer post de una probable serie sobre autogestionar software en un laboratorio
    local, partiendo por las lecciones aprendidas.
  notes:
  - 'Poder hostear no significa que debas hostear: el stack debe responder a cómo trabajas.'
  - Gestiona tus contenedores y, sobre todo, respáldalos.
  - Identifica tus servicios vitales y mantenlos siempre arriba.
  - Si nada cumple tus expectativas, puedes construirlo tú.
- title: Saving Money
  date: 2026-05-03
  url: https://blog.jath.cl/posts/es/saving-money
  reading_time: 4
  tags:
  - genai
  - budget
  - prompt
  summary: Un prompt probado durante seis meses para usar IA generativa como asistente de
    finanzas personales.
  notes:
  - 'El flujo: gastar, registrar el gasto en el chat y dejar que el modelo lleve las cuentas.'
  - Funciona igual con modelos gratuitos y de pago; la capa gratis de Gemini rindió muy bien.
  - Hay que avisarle al modelo los cierres de mes y vigilar el *drift* de contexto.
- title: Cómo Kubernetes decide dónde ejecutar un Pod
  date: 2026-03-15
  url: https://blog.jath.cl/posts/es/kubernetes-scheduling
  reading_time: 4
  tags:
  - kubernetes
  - infraestructura
  - devops
  summary: Un recorrido por el pipeline del kube-scheduler, primera parte de la serie kubernetes-internals.
  notes:
  - 'El scheduler solo decide el `spec.nodeName`: filtra nodos, los puntúa y hace el *binding*.'
  - El filtrado usa *requests* (no *limits*), selectores, afinidad, *taints* y *topology spread*.
  - Cuando no hay espacio, la *preemption* puede desalojar Pods de menor prioridad.
- title: Bienvenido a jath.cl
  date: 2026-03-01
  url: https://blog.jath.cl/posts/es/bienvenida
  reading_time: 2
  tags:
  - meta
  - fasthtml
  - python
  summary: El primer artículo del blog técnico. Qué esperar, por qué existe y cómo está construido.
  notes:
  - Escribir como la forma más honesta de verificar que entiendes algo.
  - En español, en extenso y como conversación, no optimizado para SEO.
  - 'Stack: Python, FastHTML, PicoCSS, Mistune y Pygments; sin CMS, sin base de datos y sin
    framework de JavaScript.'
- title: CodeOps (o cómo estamos empujando ventas a través de marcos metodológicos)
  date: 2024-09-03
  url: https://blog.jath.cl/posts/es/equis-as-a-service
  reading_time: 2
  tags:
  - software
  - ventas
  - desarrollo
  - xaas
  summary: Crear conocimiento es difícil y vale la pena. ¿Vale también cuando es con fines
    comerciales?
  notes:
  - 'CodeOps: construir productos rápido con código propietario y reutilizable.'
  - Una mirada crítica a la proliferación de marcos *XOps* desde DevOps en 2009.
  - 'La pregunta de fondo: cómo los asistentes de código se convierten en productos *as a
    Service*.'
- title: Ser jefe. Una mirada des-romantizada
  date: 2024-05-16
  url: https://blog.jath.cl/posts/es/un-buen-jefe
  reading_time: 4
  tags:
  - liderazgo
  - experiencias
  - trabajo
  summary: Ser jefe, o líder, en esta época es una labor compleja. Reflexiones desde la experiencia
    como mánager y líder de equipos.
  notes:
  - Nadie nace sabiendo ser jefe; se aprende sobre la marcha.
  - 'No existe un estilo de liderazgo correcto: cada uno tiene su contexto.'
  - Las herramientas se usan en su contexto, y también se reemplazan después.
- title: Profesionales efectivos
  date: 2023-07-18
  url: https://blog.jath.cl/posts/es/profesionales-efectivos
  reading_time: 7
  tags:
  - liderazgo
  - cultura
  summary: Cómo navegar la delgada línea entre el desacuerdo y la co-construcción.
  notes:
  - La orientación a procesos da una visión integral del valor que entregan nuestras decisiones.
  - Encontrar desacuerdos y fricciones temprano es una buena noticia.
  - '*Win-win-win*, *disagree and commit* y co-construcción positiva frente al relacionamiento
    defensivo.'
- title: Data warehousing en Clickhouse en 15 minutos
  date: 2021-02-13
  url: https://blog.jath.cl/posts/es/data-warehousing-clickhouse
  reading_time: 5
  tags:
  - clickhouse
  - data-warehousing
  summary: Un breve acercamiento a crear data warehouses en Clickhouse, a partir de un desafío
    real de ingeniería de datos.
  notes:
  - Llevar datos procesados en Spark a Clickhouse, todo dockerizado.
  - 'Clickhouse: base analítica columnar, open source, con compresión y múltiples motores.'
  - Un entorno cliente/servidor efímero con dos comandos de Docker. (Artículo en inglés).
---

En [blog.jath.cl](https://blog.jath.cl) escribo en extenso sobre
infraestructura, datos, Python y el oficio de hacer software. Esta página
es un resumen estático, escrito a mano, de los artículos publicados: la idea
central de cada uno y sus puntos clave. Para leerlos completos, sigue el
enlace a cada artículo.
