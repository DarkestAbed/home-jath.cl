---
title: Data warehouse en Clickhouse
summary: Solución dockerizada que entrega datos procesados en Spark a un data warehouse columnar en Clickhouse.
year: 2021
status: archivado
role: ingeniero de datos
stack: [Apache Spark, Clickhouse, Docker, Python, SQL]
repo: https://github.com/jtapiath-cl/docker_training
order: 4
---

## El desafío

Entregar datos transformados en Spark a un data warehouse en Clickhouse,
una base de datos analítica y orientada a columnas que no conocía, y
además dockerizar la solución completa, con la comunicación de red y las
APIs que eso implica. La experiencia quedó escrita en
[Data warehousing en Clickhouse en 15 minutos](https://blog.jath.cl/posts/es/data-warehousing-clickhouse).

## Aprendizajes

- Clickhouse se levanta en contenedores en minutos, sin instalar nada local.
- Los motores de tabla y la compresión hacen una diferencia enorme en
  cargas analíticas.
- Modelar pensando en columnas cambia cómo se diseñan las tablas de hechos.

```sql
-- Ejemplo ilustrativo de tabla de hechos
CREATE TABLE ventas
(
    fecha      Date,
    tienda_id  UInt32,
    producto   LowCardinality(String),
    monto      Decimal(12, 2)
)
ENGINE = MergeTree
ORDER BY (fecha, tienda_id);
```
