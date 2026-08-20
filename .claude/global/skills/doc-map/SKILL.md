---
name: doc-map
description: Gera ou atualiza docs/DOC_MAP.md — índice de navegação (âncoras de seção + padrão Grep de acesso) para documentos > 500 linhas. Usar ao criar docs grandes, quando o DOC_MAP existente desatualizar, ou no bootstrap de um projeto novo com documentação extensa.
---

# doc-map — mapa de navegação para docs grandes

Documentos de referência grandes (arquitetura, estado vigente, lições aprendidas) custam dezenas
de milhares de tokens se lidos inteiros. Esta skill gera um índice barato — propósito + âncoras de
seção + padrão Grep — para que qualquer agente vá direto à faixa relevante em vez de fazer Read
integral.

## Passos

1. **Localizar candidatos.** `Glob docs/**/*.md` (ou a raiz do projeto, se não houver `docs/`).
   Medir cada arquivo (`wc -l` via Bash, ou `(Get-Content arquivo | Measure-Object -Line).Lines`
   via PowerShell) e selecionar os que passam de **500 linhas**. Arquivos menores não precisam de
   entrada no mapa (mencionar em 1 linha que estão abaixo do limite é suficiente).

2. **Para cada documento grande:**
   - Extrair os cabeçalhos reais com `Grep pattern:"^#{1,3} " path:<arquivo> -n` — nunca adivinhar
     um cabeçalho ou número de seção; toda âncora no mapa deve vir de um Grep executado de fato.
   - Escrever **propósito** em 1 frase e **quando consultar** (que tipo de tarefa leva um agente a
     abrir este doc).
   - Escrever um **sumário de seções**: 1 linha por seção/cabeçalho, ancorado no texto do cabeçalho
     ou marcador (`§N`, `## Título`) — **nunca em número de linha**, pois desatualiza a cada edição.
   - Anotar o **padrão de acesso**: o comando Grep que localiza a seção (ex.:
     `Grep pattern:"^## §7" path:docs/AS-IS.md -n`), a ser seguido de Read com `offset`/`limit` na
     faixa encontrada.

3. **Prefixar o mapa com a regra de ouro** (idêntica em todo projeto):

   > Nunca Read integral em doc > 500 linhas. Sempre: DOC_MAP → Grep pela âncora → Read com
   > `offset`/`limit` na faixa encontrada. Âncoras são cabeçalhos/marcadores, nunca números de
   > linha — eles desatualizam.

4. **Meta de tamanho:** `docs/DOC_MAP.md` ≤ 2k tokens (~8000 chars, a ~4 chars/token). Medir com
   `wc -c` (Bash) ou `(Get-Item arquivo).Length` (PowerShell) antes de considerar concluído; se
   passar do alvo, condensar prosa e células de tabela — nunca remover uma âncora sem substituí-la.

5. **Registrar propostas fora de escopo.** Se, ao mapear, surgir uma necessidade de mudança maior
   num doc canônico (ex.: separar um doc em ATIVO + HISTÓRICO), **não executar** — registrar como
   ticket no tracker de pendências do projeto (`docs/PLANNING_ACTIVE.md` ou equivalente) para
   decisão do dono, e seguir com o mapeamento.

6. **Apontar o CLAUDE.md do projeto para o mapa.** Se o `CLAUDE.md` do projeto ainda não menciona
   `docs/DOC_MAP.md`, acrescentar 2-3 linhas na seção de planejamento/docs declarando-o porta de
   entrada obrigatória antes de qualquer Read integral em doc grande.

## Aceitação

- Todo documento > 500 linhas do projeto tem uma entrada no mapa.
- Toda âncora listada foi validada por Grep contra o arquivo real (não adivinhada).
- `docs/DOC_MAP.md` ≤ 2k tokens.
- `CLAUDE.md` do projeto referencia o DOC_MAP como entrada obrigatória.

## Quando rodar de novo

Quando um documento novo passar de 500 linhas, ou quando um Grep listado no mapa deixar de bater
(cabeçalho renomeado/removido) — reexecutar apenas a seção afetada, não o mapa inteiro.
