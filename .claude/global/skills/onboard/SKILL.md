---
name: onboard
description: Onboarding econômico em um projeto — coleta o estado inicial pelo caminho mais barato (índices e mapas antes de arquivos). Usar no início de qualquer tarefa em projeto com docs/ extenso, ou quando o usuário pedir para "se situar" no projeto.
---

# onboard — porta de entrada econômica em qualquer projeto

Ler tudo (docs inteiros, `git log` completo, listagem recursiva) para "se situar" num projeto
gasta o contexto antes do trabalho real começar. Esta skill prioriza índices e ponteiros baratos
sobre leituras integrais — a mesma lógica de progressive disclosure usada por [[doc-map]] e
[[memory-diet]].

## Passos

1. **Docs.** `CLAUDE.md` do projeto já está carregado (não reler). Verificar se existe
   `docs/DOC_MAP.md`:
   - Se existir, usá-lo como porta de entrada — Grep pela âncora relevante, Read com
     `offset`/`limit` só na faixa encontrada.
   - Se não existir e houver doc(s) > 500 linhas em `docs/`, **não varrer** — sugerir gerar o mapa
     via skill [[doc-map]] antes de ler qualquer doc grande integralmente.

2. **Estado do repo.** `git status --short` + `git log --oneline -10` — nunca as formas completas
   (`git status`, `git log` sem `--oneline`/limite).

3. **Planejamento.** Procurar, nesta ordem, o primeiro que existir: `docs/PLANNING_ACTIVE.md`,
   `TODO.md`, issues do tracker do projeto. Ler apenas o primeiro encontrado — não os três.

4. **Estrutura.** `Glob` com padrões dirigidos (ex.: `*/manifest.json`, `pyproject.toml`,
   `src/**/*.config.*`) em vez de listagem recursiva; excluir sempre `build/`, `dist/`, `.venv/`,
   `__pycache__/`, `node_modules/`.

5. **Arquivos > 500 linhas.** Grep para localizar o trecho relevante + Read com `offset`/`limit`.
   Read integral é proibido nessa faixa de tamanho.

6. **Varreduras amplas.** Quando só a conclusão importa (muitos arquivos, busca exploratória sem
   alvo certo) — delegar ao subagente `context-scout` (roda em Haiku; critérios de corte na skill
   [[context-prep]]) em vez de ler tudo no contexto principal.

## Aceitação

- Nenhum doc > 500 linhas foi lido integralmente durante o onboarding.
- `git status`/`git log` só nas formas resumidas.
- Se `docs/DOC_MAP.md` não existia e havia doc grande, a skill [[doc-map]] foi sugerida em vez de
  uma varredura manual.

## Quando rodar de novo

No início de qualquer tarefa nova neste projeto — o onboarding não fica "feito" de uma vez, é o
primeiro passo padrão de cada tarefa que exige contexto do repo.
