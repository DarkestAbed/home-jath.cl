---
title: EigenMemory
summary: Capa de memoria persistente y compartida entre herramientas para asistentes de código con LLM, expuesta vía MCP.
year: 2026
status: v0.1.10
role: autor
stack: [Go, MCP, SQLite FTS5, Markdown]
repo: https://github.com/DarkestAbed/eigenmemory
featured: true
order: 2
---

## Qué es

Una memoria para agentes de programación que sobrevive entre sesiones y
entre herramientas. Mantiene una única **LLM Wiki** en Markdown como fuente
de verdad, siguiendo el patrón *LLM Wiki* de Andrej Karpathy, y la expone a
Claude Code, Zed, Codex CLI, Antigravity y cualquier cliente MCP mediante un
servidor local por stdio.

## Cómo funciona

- Los archivos de memoria propios de cada herramienta son **proyecciones**
  de la wiki, no fuentes independientes.
- `wiki_remember` guarda hechos durables como páginas tipadas (decisión,
  preferencia, referencia) con fuentes y etiquetas.
- `wiki_query` / `wiki_recall` buscan con FTS5 y expanden un salto por los
  `[[wikilinks]]`, así aparecen páginas relacionadas aunque no calcen con la
  búsqueda.
- Todo vive en Markdown legible y editable; SQLite es solo el índice.

```json
{
  "mcpServers": {
    "eigenmemory": {
      "type": "stdio",
      "command": "eigenmemory",
      "args": ["serve", "--mcp"]
    }
  }
}
```
