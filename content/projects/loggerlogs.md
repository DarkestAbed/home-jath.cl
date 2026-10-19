---
title: loggerLogs
summary: Implementación a medida sobre la librería logging de Python, con salida a consola y archivo configurable y niveles según el entorno.
year: 2024
status: estable
role: autor
stack: [Python, logging, setuptools]
repo: https://github.com/DarkestAbed/loggerLogs
order: 9
---

## Qué es

Un envoltorio sobre el módulo `logging` de la librería estándar para dejar
de reconfigurar handlers y formatos en cada proyecto. `CustomLogger` arma
el logger con salida a consola y, opcionalmente, a archivo, cada una con su
propio nivel.

## Detalles

- El nivel por defecto depende del entorno: `DEBUG` si `ENVIRON=dev`, `INFO`
  en cualquier otro caso.
- Un formato de log detallado: archivo, módulo, función, línea y proceso.
- Incluye una metaclase `Singleton` propia para compartir una sola
  instancia en toda la aplicación.

```python
from loggerLogs import CustomLogger

logger = CustomLogger(
    console_log=True,
    file_log=True,
    file_log_path="logs/",
)
```
