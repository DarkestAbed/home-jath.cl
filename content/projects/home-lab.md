---
title: Home lab
summary: Laboratorio local para autogestionar los servicios que uso a diario, con contenedores, monitoreo y respaldos.
year: 2026
status: en curso
role: operador único
stack: [Docker, Portainer, Coolify, Linux, Beszel]
featured: true
order: 3
---

## Por qué

Hace unos meses empecé el camino del *self-hosting* para dejar de depender
de servicios que usaba y pagaba: streaming, libros, un IDE propio y algunos
más. Lo cuento en [Self hosting](https://blog.jath.cl/posts/es/self-hosting).

## Lecciones hasta ahora

1. **Poder hostear no significa que debas hostear.** El stack tiene que
   responder a la forma real de trabajar.
2. Gestionar los contenedores con herramientas como Portainer o Coolify, y
   **respaldarlos**.
3. Identificar los servicios vitales y mantenerlos siempre arriba.
4. Si no existe el servicio que necesitas, puedes construirlo.

```yaml
# Ejemplo ilustrativo: un servicio con política de reinicio y volumen respaldable
services:
  calibre-web:
    image: lscr.io/linuxserver/calibre-web:latest
    restart: unless-stopped
    volumes:
      - ./data/calibre:/config
    ports:
      - "8083:8083"
```
