---
kicker: "~/jath.cl $ whoami"
title: Javier Thompson
tagline: desarrollador · tecnólogo · ingeniero de datos
lead: >-
  Construyo software y plataformas de datos, lidero equipos técnicos y
  escribo sobre lo que aprendo en el camino: infraestructura, Python,
  self-hosting y el oficio de hacer software con otras personas.
ctas:
  - label: Ver proyectos
    href: /proyectos
  - label: Leer el blog ↗
    href: https://blog.jath.cl
    ghost: true
terminal_title: jath.py
focus:
  - title: Software y backend
    text: >-
      Python de punta a punta: APIs, herramientas de línea de comandos y
      sitios renderizados en el servidor, sin más JavaScript del necesario.
  - title: Datos e infraestructura
    text: >-
      Pipelines con Spark, data warehouses columnares, contenedores y
      Kubernetes. Del laptop al clúster, y de vuelta al home lab.
  - title: Equipos y procesos
    text: >-
      Formación en procesos de negocio, experiencia como líder técnico y
      mánager de ingeniería. Co-construir antes que imponer.
cta:
  title: ¿Conversamos?
  text: Proyectos, ideas, consultas o simplemente buena conversación técnica.
---

```python
from dataclasses import dataclass

STACK = ("python", "fasthtml", "spark",
         "clickhouse", "docker", "kubernetes")

@dataclass
class Javier:
    rol: str = "desarrollador & tecnólogo"
    base: str = "Chile"
    stack: tuple[str, ...] = STACK

    def escribir(self) -> str:
        return "https://blog.jath.cl"

print(Javier().escribir())
```
