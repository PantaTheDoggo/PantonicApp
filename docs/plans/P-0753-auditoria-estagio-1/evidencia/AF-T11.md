# Evidência de revisão — P-0753 AF-T11

## Diff (`git diff --stat`)
```
.claude/agents/pantonic-consultant.md              |  2 ++
 .claude/skills/scrum-master/SKILL.md               |  7 +++++
 docs/DIARIO_DE_OBRAS.md                            |  4 +--
 docs/plans/P-0753-auditoria-estagio-1/estado.tsv   |  2 +-
 .../evidencia/P-0753-AF-T11-medida.json            | 36 ++++++++++++++++++++++
 docs/telemetria.tsv                                |  1 +
 6 files changed, 49 insertions(+), 3 deletions(-)
```

## Arquivos tocados
- `.claude/agents/pantonic-consultant.md` — atribuição: da entrega; estado git: ` M`
- `.claude/skills/scrum-master/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0753-auditoria-estagio-1/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T11-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `17e0ae840f322e4268ad45737bd1627488e8bdd5`
- Arquivos-alvo declarados: `.claude/agents/pantonic-consultant.md`, `.claude/skills/scrum-master/SKILL.md`
- Arquivos tocados: `.claude/agents/pantonic-consultant.md`, `.claude/skills/scrum-master/SKILL.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T11-medida.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T11-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/agents/pantonic-consultant.md`
```
diff --git a/.claude/agents/pantonic-consultant.md b/.claude/agents/pantonic-consultant.md
index 65c706e..596bf9d 100644
--- a/.claude/agents/pantonic-consultant.md
+++ b/.claude/agents/pantonic-consultant.md
@@ -21,10 +21,12 @@ cenário fica **num arquivo só**, persistido, e cada acionamento nasce lendo o
 ## O que você faz
 
 1. **Lê o cenário, não o plano.** A cada acionamento você lê `docs/plans/P-<n>-<slug>/cenario.md` (plano legado: `_CENARIO-<plano>.md` em `docs/plans/`) — decisões vivas, fila, achados abertos, matéria inconclusiva, no máximo 15k tokens — e o card em causa; do plano, só o trecho que o cenário aponta. Ao sair, reescreve no cenário o que a sua decisão mudou: o que você não escrever ali, o próximo acionamento não sabe. Cenário acima de 15k tokens: mova a matéria fechada para `## 9` do plano, com ponteiro, e registre isso na coluna `inconclusivo` da sua linha de estatística.
+   **Lê só as três entradas.** O despacho traz três entradas — o caminho do cenário, o id do card e a evidência (a linha de retorno do executor, a pendência do laudo ou o stderr do instrumento) —, e você lê só elas e, da doutrina, só a seção que o cenário aponta: relatório de auditoria, diário, RDO de outra tarefa e plano inteiro ficam fora, e fato que só eles teriam vai ao cenário como matéria inconclusiva. Caso medido (2026-09-27): o acionamento que leu o relatório de auditoria fora do cenário custou 131,2k tokens; o seguinte, com a instrução de não ler fora dele, 67,4k.
 2. **Tria toda parada de executor.** Quando um card volta `blocked` — motivo `premissa`, `dependencia` ou `ferramenta` —, quando um laudo traz pendência substantiva ou quando um instrumento do loop recusa o fechamento, o loop manda o caso a você. O motivo é evidência, não rota. A primeira linha do seu retorno é `rota=<resolve|modelador|planejador>`; a segunda, só quando o impedimento é estratégico — muda escopo ou objetivo do plano, ou revoga decisão do dono —, é `estrategico=<uma frase>`, e com ela o loop **para** em qualquer rota sem executar a ação da rota: o reparo já gravado fica no plano, e a frase, a rota e o dossiê de emenda, se houver, vão ao relatório de encerramento (`DCS-27`, `DCS-28`). Depois vêm a decisão e o reparo — nunca opções:
    - `rota=resolve` — a questão é operacional, técnica ou tática: você a fecha sozinho, e o dono não valida (ato do dono de 2026-09-22: *"Eu não vou validar a decisão dele para questões técnicas e táticas."*). Um dos desfechos é **recusar o impedimento como improcedente** — o executor parou sem razão e o card é executável como está (`DCS-35` do `P-0747`), com três amarras: você declara a improcedência com a razão, que vai à coluna `motivo` da estatística; devolve o card a `ready` com **ao menos uma linha nova** — a contingência ou o fato que responde à dúvida do executor —, porque recusar sem tocar o card só reproduz a parada num executor frio; e o redespacho **não consome a retentativa**.
    - `rota=modelador` — a resolução altera objeto, operação ou estado final da `## 1`: é drift do modelo, a sua guarda. Devolva o dossiê `Ato de modelo` de `emenda` junto com o reparo do card; o loop despacha o modelador sem parar a janela, a versão pendente coexiste com a vigente até o marco, e é lá que o pedido de validar ou recusar o drift sobe ao dono (`GOVERNANCA.md` §3.2) — recusado, o caso volta a você para resolver preservando o modelo.
    - `rota=planejador` — emenda já aceita cria ou remove operação, ou a premissa do plano caiu por inteiro.
+   A linha `estrategico=` tem **uma frase**, sem ponto no meio: o que o impedimento muda no escopo ou no objetivo do plano, ou qual decisão do dono ele revoga; o detalhe vai ao cenário, nunca à linha (caso medido, 2026-09-27: três frases num acionamento do plano fictício da auditoria).
 3. **Repara o plano e devolve o dossiê de modelo.** Você edita o plano: decisão nova com id, cards reescritos, fila reordenada, achado absorvido com ponteiro. Card corretivo `T<n>a` da mesma operação do card
```
[truncado em 4000 caracteres]

### `.claude/skills/scrum-master/SKILL.md`
```
diff --git a/.claude/skills/scrum-master/SKILL.md b/.claude/skills/scrum-master/SKILL.md
index 4bf9d88..8634bd3 100644
--- a/.claude/skills/scrum-master/SKILL.md
+++ b/.claude/skills/scrum-master/SKILL.md
@@ -319,6 +319,13 @@ fronteira do ponto do dono", e não se redecide aqui.
 
 Forma **efêmera com cenário persistido**, em piloto (`docs/plans/P-0747-consultor-de-plano.md` `DCS-6`, `DCS-7`). O consultor não fica de prontidão: a cada escalonamento das regras `A3a`, `A3b`, `A3c`, `A6a`, `A7` e `B1` e do gate do modelo do passo 9, o loop despacha **uma instância nova** do `pantonic-consultant`, com três entradas — o caminho do cenário do plano, `docs/plans/P-<n>-<slug>/cenario.md` (plano legado: `_CENARIO-<plano>.md` em `docs/plans/`); o identificador do card em causa; e a evidência (a linha de retorno do executor, a pendência do laudo ou o stderr do instrumento). A instância lê o cenário e o card, decide, reescreve o cenário com `Edit` mínimo, apensa a linha dela a `docs/ACIONAMENTOS_CONSULTOR.tsv` e devolve `rota=<resolve|modelador|planejador>` — e, só quando classifica o impedimento como estratégico, a linha `estrategico=<uma frase>` logo abaixo (`DCS-27`) —, que o loop roteia pelo passo 8. Nenhuma instância é retomada por `SendMessage` e nenhuma é reprovisionada por limite: o cenário **é** o handover, e a instância que cai se descarta — a `A1` despacha outra, com as mesmas três entradas, sobre o cenário como ficou. Sem o arquivo de cenário na árvore, o primeiro acionamento do plano o cria, com as decisões vivas, a fila, os achados abertos e a matéria inconclusiva, em no máximo 15k tokens. A linha de telemetria de cada instância é gravada pelo hook `SubagentStop`, com a tarefa `<ID>-consultor-<n>`.
 
+Molde do despacho — as três entradas, e nada além delas:
+
+    cenario=docs/plans/P-<n>-<slug>/cenario.md
+    card=<ID>
+    evidencia=<a linha de retorno do executor, a pendência do laudo ou o stderr do instrumento, verbatim>
+    Leia só o cenário, o card e a evidência acima e, da doutrina, só o que o cenário aponta.
+
 ## Relatório de encerramento
 
 Uma vez por janela, na parada. Abre com a saída integral de `python

```

## Medida do executor
- Arquivo: docs\plans\P-0753-auditoria-estagio-1\evidencia\P-0753-AF-T11-medida.json; mundo: depois; gerado em: 2026-09-27T15:02:55+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;c=chr(96);t=Path('.claude/agents/pantonic-consultant.md').read_text(encoding='utf-8');print(t.count('Lê só as três entradas.'),t.count('A linha '+c+'estrategico='+c+' tem **uma frase**'))"` | 0 | true |
| 2 | `python -c "from pathlib import Path;print(Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8').count('cenario=docs/plans/P-<n>-<slug>/cenario.md'))"` | 0 | true |
| 3 | `python -m pytest -q` | 0 | true |
| 4 | `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
