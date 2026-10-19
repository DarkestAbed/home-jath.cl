---
title: FridAI
summary: Plataforma de tareas y pendientes con backend FastAPI, frontend FastHTML instalable como PWA y un worker de tareas programadas.
year: 2025
status: experimental
role: autor
stack: [Python, FastAPI, FastHTML, SQLAlchemy, SQLite, Docker]
repo: https://github.com/DarkestAbed/fridai
order: 7
---

## Arquitectura

Un monorepo con tres piezas:

- **Backend**: FastAPI con SQLite (SQLAlchemy 2.0 asíncrono) y routers
  modulares por dominio: tareas, categorías, etiquetas, adjuntos, vistas y
  notificaciones.
- **Frontend**: FastHTML + Sakura CSS, interacciones estilo HTMX, PWA.
- **Worker**: ejecuta el scheduler llamando a los endpoints cron del backend.

Las notificaciones salen por [Apprise](https://github.com/caronc/apprise),
y el CI publica imágenes en GHCR. Incluye tests unitarios, de integración,
de rendimiento y de estrés.
