---
title: Asistente financiero con IA
summary: Un prompt iterado durante seis meses que convierte a un LLM en registro de gastos y consejero de presupuesto.
year: 2026
status: en uso
role: autor del prompt
stack: [LLMs, prompt engineering, Gemini]
order: 5
---

## La idea

Registrar cada gasto conversando con un modelo de lenguaje, que mantiene
las cuentas del mes y de vez en cuando sugiere mejoras en el manejo del
dinero. El prompt va en su quinta iteración y lo comparto completo en
[Saving Money](https://blog.jath.cl/posts/es/saving-money).

## Flujo

1. Hago un gasto en el mundo real.
2. Lo registro en el chat: monto, descripción y categoría.
3. El modelo actualiza el estado de mis finanzas.
4. Al cierre de mes le pido resúmenes y recomendaciones.

Funciona con modelos de pago y open source por igual; la capa gratuita de
Gemini ha sido la más constante. Su punto débil es el *drift* en
conversaciones largas, que hay que re-encauzar de vez en cuando.
