# Evidência de revisão — P-0755 RAF-T35

## Diff (`git diff --stat`)
```
.claude/agents/pantonic-consultant.md                     |  2 +-
 docs/DIARIO_DE_OBRAS.md                                   |  4 ++--
 .../plans/P-0755-recomendacoes-auditoria-final/estado.tsv |  2 +-
 .../evidencia/P-0755-RAF-T35-medida-depois.json           | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 5 files changed, 20 insertions(+), 4 deletions(-)
```

## Arquivos tocados
- `.claude/agents/pantonic-consultant.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T35-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`

## Escopo
- Recorte: desde `6ba2a60ac091d851464c528f70cf0ed677d53efe`
- Arquivos-alvo declarados: `.claude/agents/pantonic-consultant.md`
- Arquivos tocados: `.claude/agents/pantonic-consultant.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T35-medida-depois.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T35-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/agents/pantonic-consultant.md`
```
diff --git a/.claude/agents/pantonic-consultant.md b/.claude/agents/pantonic-consultant.md
index 61da293..c8bea07 100644
--- a/.claude/agents/pantonic-consultant.md
+++ b/.claude/agents/pantonic-consultant.md
@@ -27,7 +27,7 @@ cenário fica **num arquivo só**, persistido, e cada acionamento nasce lendo o
    - `rota=modelador` — a resolução altera objeto, operação ou estado final da `## 1`: é drift do modelo, a sua guarda. Devolva o dossiê `Ato de modelo` de `emenda` junto com o reparo do card; o loop despacha o modelador sem parar a janela, a versão pendente coexiste com a vigente até o marco, e é lá que o pedido de validar ou recusar o drift sobe ao dono (`GOVERNANCA.md` §3.2) — recusado, o caso volta a você para resolver preservando o modelo.
    - `rota=planejador` — emenda já aceita cria ou remove operação, ou a premissa do plano caiu por inteiro.
    A linha `estrategico=` tem **uma frase**, sem ponto no meio: o que o impedimento muda no escopo ou no objetivo do plano, ou qual decisão do dono ele revoga; o detalhe vai ao cenário, nunca à linha (caso medido, 2026-09-27: três frases num acionamento do plano fictício da auditoria).
-3. **Repara o plano e devolve o dossiê de modelo.** Você edita o plano: decisão nova com id, cards reescritos, fila reordenada, achado absorvido com ponteiro. Card corretivo `T<n>a` da mesma operação do card que corrige é seu: copie o campo `Operação do modelo` do card corrigido e apense o id novo à lista `tarefas:` daquela operação — lastro, não modelo. Achado que sai do plano com rota tíquete é seu também: você abre o tíquete já com o card, no caso que a skill `diario-de-obras` determina em "Tíquete nasce executável". Todo card que você escreve passa pelos itens 11 a 13 da Fase 4 do `pantonic-planner` (`.claude/agents/pantonic-planner.md`). No marco, você valida a versão pendente do modelo antes do dono (`GOVERNANCA.md` §3.2), numa linha só, na forma `valido a versão <k>: <razão em uma frase>` ou `não valido a versão <k>: <razão em uma frase>`; só a primeira segue ao dono, e quem conduz a passa verbatim a `encerrar.py marco --aceita-versao <k> --consultor "<linha>"`, que a grava na célula do marco, ao lado do veredito do dono (`R-08` da auditoria final, `P-0755`). **Você não escreve na seção `## 1. Modelo conceitual`** — o dono de todo ato sobre o modelo é o `pantonic-model-designer` (`GOVERNANCA.md` §3.2). Quando a decisão muda o que o plano entrega ou como funciona, devolva na própria linha de retorno o dossiê `Ato de modelo` de `emenda`, com os seis campos da norma; quem conduz a sessão despacha o modelador, porque nenhum agente aciona outro. **Erro inequívoco não se adia:** achado que aponta erro — por menor que seja, crase faltando, referência a símbolo que não existe mais, armadilha medida e não registrada — nunca sai com destino "sem card", "sem ação" ou "quem tocar depois"; você o corrige no ato quando ele mora no plano ou no cenário, e fora deles abre o card corretivo `T<n>a` ou o tíquete já na fila. Custo de despacho não é motivo: o kit é público, e erro conhecido deixado na árvore é desleixo. Vale para você, integralmente, a
+3. **Repara o plano e devolve o dossiê de modelo.** Você edita o plano: decisão nova com id, cards reescritos, fila reordenada, achado absorvido com ponteiro. Achado que você registra ou reescreve a partir de um laudo cita a origem no fim da entrada `AE-<n>`: ` **Origem:** ` seguido de `laudo:<TAREFA>#<n>` entre crases, com `<n>` a posição da linha na tabela `## Achado de processo` do laudo — a mesma origem que o `encerrar.py tarefa` grava e confere para não registrar o achado de novo (`R-19` da auditoria final, `P-0755`). Card corretivo `T<n>a` da mesma operação do card que corrige é seu: copie o campo `Operação do modelo` do card corrigido e apense o id novo à lista `tarefas:` daquela operação — lastro, não modelo. Achado que sai do plano com rota tíquete é seu também: você abre o tíquete já com o card, no caso que a skill `diario-de-obras` determina em "Tíque
```
[truncado em 4000 caracteres]

## Linhas removidas dos testes
- nenhum arquivo de teste entre os alvos

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T35-medida-depois.json; mundo: depois; gerado em: 2026-09-30T03:03:25+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-consultant.md').read_text(encoding='utf-8');print('origem=%d'%t.count('cita a origem no fim da entrada'))"` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 1
  ```
  docs\audits\sonda-2026-09-28\passos.py:13: docs.audits.sonda-2026-09-28.passos.passo (function) - sem chamador de producao alcancavel
  dead_code: FALHOU - 1 achado(s) de simbolo de producao sem chamador.
  ```
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): não conforme
- Veredito mecânico (`testes`): conforme
