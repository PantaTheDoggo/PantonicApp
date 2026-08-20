---
name: memory-diet
description: Compacta o MEMORY.md do projeto atual quando ele passa de ~4k chars ou ~40 linhas: consolida entradas históricas em project-history.md, extrai pendências vivas para project-pending.md (ou aponta para o tracker canônico de pendências do projeto, se houver) e reduz o índice a hooks de 1 linha. Usar quando o índice de memória crescer demais, ou quando o usuário pedir para "fazer dieta na memória" / "limpar o MEMORY.md".
---

# memory-diet — higiene periódica do índice de auto-memória

`MEMORY.md` é carregado inteiro em toda sessão. Quando ele vira um changelog — muitas entradas
"Sprint X complete" com o conteúdo embutido na linha em vez de um ponteiro — o custo fixo de
onboarding cresce sem necessidade. Esta skill compacta o índice sem perder informação.

## Localização

O diretório de memória do projeto atual: `C:\Users\panta\.claude\projects\<slug-do-projeto>\memory\`
(o mesmo diretório onde já vivem `MEMORY.md` e os arquivos `*.md` individuais).

## Passos

1. **Ler `MEMORY.md`** e classificar cada entrada em:
   - **Histórica** (sprint/tarefa concluída, sem pendência viva) — a maioria.
   - **Histórica com pendência viva** (menciona algo tipo ".exe pending", "manual smoke pending",
     "revisar depois") — extrair a pendência **antes** de arquivar a linha.
   - **Viva** (feedback do usuário, preferências, setup, referências externas) — manter como está.

2. **Verificar se existe um tracker de pendências canônico no próprio projeto**
   (ex.: `docs/PLANNING_ACTIVE.md`, `TODO.md`, issues) — procurar no `CLAUDE.md` do projeto por
   frases como "single source of truth for open tickets". Se existir e já cobrir as pendências
   encontradas no passo 1, **não duplicá-las**: `project-pending.md` deve ser um ponteiro fino para
   esse tracker, não uma segunda lista que pode ficar desatualizada. Só liste pendências vivas
   diretamente em `project-pending.md` se nenhum tracker canônico as cobrir.

3. **Criar/atualizar `project-history.md`** (frontmatter `metadata.type: project`) consolidando as
   entradas históricas em uma linha compacta cada (nome do sprint/tarefa, resultado em 1 frase,
   métrica relevante — nº de testes, versão de doc/contrato). Link para o arquivo `project_*.md`
   original em cada linha. **Nunca apagar os arquivos individuais** — permanecem recuperáveis sob
   demanda.

4. **Criar/atualizar `project-pending.md`** (frontmatter `metadata.type: project`) com o resultado
   do passo 2: ou a lista viva de pendências (cada uma com o sprint/tarefa de origem), ou o
   ponteiro fino para o tracker canônico com uma nota explicando por que o arquivo fica enxuto.

5. **Reescrever `MEMORY.md`** para conter apenas:
   - 1 linha → `project-history.md`
   - 1 linha → `project-pending.md`
   - 1 linha por memória viva (feedback/setup/referência), hook ≤120 chars cada.

6. **Meta de tamanho:** `MEMORY.md` ≤ 4k chars (~1k tokens). Verificar com
   `wc -c MEMORY.md` (Bash) ou `(Get-Item MEMORY.md).Length` (PowerShell).

## Aceitação

- Nenhuma informação perdida: tudo que saiu do índice está em `project-history.md`,
  `project-pending.md`, ou permanece recuperável nos arquivos individuais.
- `MEMORY.md` ≤ 4k chars.

## Risco e mitigação

Risco: perder uma pendência viva embutida numa linha histórica. Mitigação: o passo 1 é uma
triagem explícita antes de qualquer reescrita — nunca compactar direto sem classificar primeiro.

## Quando rodar de novo

Quando `MEMORY.md` ultrapassar de novo ~40 linhas ou ~4k chars — memórias novas vão se acumulando
entre execuções desta skill.
