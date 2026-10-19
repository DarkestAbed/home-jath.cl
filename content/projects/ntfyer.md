---
title: ntfyer
summary: Pequeño wrapper de línea de comandos para enviar notificaciones a cualquier servidor ntfy, incluso instancias privadas.
year: 2025
status: estable
role: autor
stack: [Python, CLI, ntfy, pipx]
repo: https://github.com/DarkestAbed/ntfyer
order: 8
---

## Para qué

Avisarte desde la terminal cuando algo termina: un backup, un build, un
script largo. Se configura una vez con tu servidor y tópico de
[ntfy](https://ntfy.sh), y se integra en cualquier flujo de Linux.

```bash
pipx install git+https://github.com/DarkestAbed/ntfyer
ntfyer config get
./backup.sh && ntfyer send "backup listo"
```
