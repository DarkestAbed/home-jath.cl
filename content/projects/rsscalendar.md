---
title: RSSCalendar
summary: Combina varios calendarios ICS, públicos o protegidos, en un único feed RSS. Self-hosted y dockerizado.
year: 2026
status: activo
role: autor
stack: [Python, Docker, ICS, RSS, GHCR]
repo: https://github.com/DarkestAbed/rsscalendar
order: 5
---

## Qué hace

- Administra una lista de URLs ICS, cada una opcionalmente con autenticación
  HTTP básica.
- Las descarga y procesa periódicamente, expandiendo eventos recurrentes.
- Expone **un solo feed RSS** en `/feed.xml` con los próximos 30 días.
- Interfaz web oscura para agregar fuentes y previsualizar eventos.

La imagen multi-arquitectura se publica en GitHub Container Registry:

```bash
docker run -p 8000:8000 -v "$PWD/data:/app/data" \
  -e BASE_URL=http://localhost:8000 \
  ghcr.io/darkestabed/rsscalendar:latest
```
