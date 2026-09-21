# Evidência de revisão — P-0743 DOM-T8a

## Diff (`git diff --stat`)
```
.claude/README.md                          |   3 +-
 .claude/agents/pantonic-consultant.md      |   5 +-
 .claude/agents/pantonic-planner.md         |  52 +-
 .claude/agents/pantonic-reviewer.md        |  28 +-
 .claude/skills/diario-de-obras/SKILL.md    |  37 +-
 .claude/skills/passagem-de-bastao/SKILL.md |   6 +-
 .claude/skills/scrum-master/SKILL.md       |  52 +-
 .claude/tools/rdo.py                       |   8 +-
 GOVERNANCA.md                              |  93 +++-
 README.md                                  |  18 +-
 docs/DIARIO_DE_OBRAS.md                    | 121 ++++-
 docs/RDO/INDEX.md                          |  18 +
 docs/RUBRICA_DE_REVISAO.md                 |   7 +-
 docs/plans/P-0741-modelo-conceitual.md     | 842 ++++++++++++++++++++++++++---
 docs/plans/_INBOX.md                       |   3 +-
 docs/plans/_INBOX_HISTORICO.md             |   2 +
 docs/telemetria.tsv                        |  58 ++
 tests/test_rdo.py                          |  19 +
 18 files changed, 1253 insertions(+), 119 deletions(-)
```

## Arquivos tocados
- `.claude/README.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-consultant.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-model-designer.md` — atribuição: alheio; estado git: `??`
- `.claude/agents/pantonic-planner.md` — atribuição: da entrega; estado git: ` M`
- `.claude/agents/pantonic-reviewer.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/diario-de-obras/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/skills/passagem-de-bastao/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/scrum-master/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/tools/modelo.py` — atribuição: alheio; estado git: `??`
- `.claude/tools/rdo.py` — atribuição: alheio; estado git: ` M`
- `GOVERNANCA.md` — atribuição: da entrega; estado git: ` M`
- `README.md` — atribuição: alheio; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/OPERACOES_AS_IS.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/INDEX.md` — atribuição: alheio; estado git: ` M`
- `docs/RDO/P-0741-MC-T1-a-norma-e-a-gramatica-do-modelo-publicadas-nas-residencias-u.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0741-MC-T2-modelo-py-check-e-show-e-o-alvo-modelo-no-gerador-de-laudo.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0741-MC-T2a-o-campo-sem-consumidor-sai-da-dataclass-do-instrumento.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0741-MC-T2b-a-cadeia-sem-consumidor-sai-inteira-do-instrumento.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0741-MC-T3-os-tres-papeis-que-escrevem-o-modelo-planejador-revisor-e-co.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0741-MC-T4-o-loop-le-confere-e-mostra-o-modelo-scrum-master-e-passagem.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0741-MC-T4a-o-gate-do-modelo-no-fechamento-para-de-criar-o-vermelho-que.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T1-a-norma-do-modelo-de-dominio-e-o-papel-que-a-executa.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T2-a-gramatica-que-a-maquina-le.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T3-o-instrumento-le-a-forma-nova.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T3a-o-que-o-instrumento-e-a-gramatica-dizem-de-si-mesmos.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T3b-a-referencia-cruzada-do-docstring.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T4-o-modelador.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T5-os-papeis-diante-do-modelador.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T5a-a-costura-do-retorno-do-revisor.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T5b-a-cadeia-do-retorno-do-emissor-ao-consumidor.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T7-a-norma-da-forma-nova-propriedades-estado-e-versao.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T8-a-gramatica-da-forma-nova.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0741-MC-T1.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0741-MC-T2.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0741-MC-T2a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0741-MC-T2b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0741-MC-T3.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0741-MC-T4.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0741-MC-T4a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0741-MC-T5.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T1.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T2.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T3.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T3a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T3b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T4.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T5.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T5a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T5b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T7.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T8.md` — atribuição: alheio; estado git: `??`
- `docs/RUBRICA_DE_REVISAO.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0741-modelo-conceitual.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0743-modelo-de-dominio.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0744-spec-do-planejador.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_INBOX.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/_INBOX_HISTORICO.md` — atribuição: alheio; estado git: ` M`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/fixtures/modelo/fluxo-concluido.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/fluxo-valido.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-forma-anterior.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-invalido-2.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-invalido.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-sem-cabecalho.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-sem-modelo.md` — atribuição: alheio; estado git: `??`
- `tests/test_modelo.py` — atribuição: alheio; estado git: `??`
- `tests/test_rdo.py` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `e0efcf6b1a5aae9ec176f906a28384385d710a7f`
- Arquivos-alvo declarados: `GOVERNANCA.md`, `.claude/agents/pantonic-planner.md`, `.claude/skills/diario-de-obras/SKILL.md`
- Literais não reconhecidos como caminho (11): `I-5`, `| **Modelagem** |`, `| modelador |`, `### 3.2`, `I-5`, `## 1. Modelo conceitual`, `**O modelo antes das tarefas.**`, `I-5`, `## Gramática legível por máquina`, `### Modelo de domínio (seção do plano)`, `DOM-T8`
- Arquivos tocados: `.claude/README.md`, `.claude/agents/pantonic-consultant.md`, `.claude/agents/pantonic-model-designer.md`, `.claude/agents/pantonic-planner.md`, `.claude/agents/pantonic-reviewer.md`, `.claude/skills/diario-de-obras/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/modelo.py`, `.claude/tools/rdo.py`, `GOVERNANCA.md`, `README.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/OPERACOES_AS_IS.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0741-MC-T1-a-norma-e-a-gramatica-do-modelo-publicadas-nas-residencias-u.md`, `docs/RDO/P-0741-MC-T2-modelo-py-check-e-show-e-o-alvo-modelo-no-gerador-de-laudo.md`, `docs/RDO/P-0741-MC-T2a-o-campo-sem-consumidor-sai-da-dataclass-do-instrumento.md`, `docs/RDO/P-0741-MC-T2b-a-cadeia-sem-consumidor-sai-inteira-do-instrumento.md`, `docs/RDO/P-0741-MC-T3-os-tres-papeis-que-escrevem-o-modelo-planejador-revisor-e-co.md`, `docs/RDO/P-0741-MC-T4-o-loop-le-confere-e-mostra-o-modelo-scrum-master-e-passagem.md`, `docs/RDO/P-0741-MC-T4a-o-gate-do-modelo-no-fechamento-para-de-criar-o-vermelho-que.md`, `docs/RDO/P-0743-DOM-T1-a-norma-do-modelo-de-dominio-e-o-papel-que-a-executa.md`, `docs/RDO/P-0743-DOM-T2-a-gramatica-que-a-maquina-le.md`, `docs/RDO/P-0743-DOM-T3-o-instrumento-le-a-forma-nova.md`, `docs/RDO/P-0743-DOM-T3a-o-que-o-instrumento-e-a-gramatica-dizem-de-si-mesmos.md`, `docs/RDO/P-0743-DOM-T3b-a-referencia-cruzada-do-docstring.md`, `docs/RDO/P-0743-DOM-T4-o-modelador.md`, `docs/RDO/P-0743-DOM-T5-os-papeis-diante-do-modelador.md`, `docs/RDO/P-0743-DOM-T5a-a-costura-do-retorno-do-revisor.md`, `docs/RDO/P-0743-DOM-T5b-a-cadeia-do-retorno-do-emissor-ao-consumidor.md`, `docs/RDO/P-0743-DOM-T7-a-norma-da-forma-nova-propriedades-estado-e-versao.md`, `docs/RDO/P-0743-DOM-T8-a-gramatica-da-forma-nova.md`, `docs/RDO/evidencia/P-0741-MC-T1.md`, `docs/RDO/evidencia/P-0741-MC-T2.md`, `docs/RDO/evidencia/P-0741-MC-T2a.md`, `docs/RDO/evidencia/P-0741-MC-T2b.md`, `docs/RDO/evidencia/P-0741-MC-T3.md`, `docs/RDO/evidencia/P-0741-MC-T4.md`, `docs/RDO/evidencia/P-0741-MC-T4a.md`, `docs/RDO/evidencia/P-0741-MC-T5.md`, `docs/RDO/evidencia/P-0743-DOM-T1.md`, `docs/RDO/evidencia/P-0743-DOM-T2.md`, `docs/RDO/evidencia/P-0743-DOM-T3.md`, `docs/RDO/evidencia/P-0743-DOM-T3a.md`, `docs/RDO/evidencia/P-0743-DOM-T3b.md`, `docs/RDO/evidencia/P-0743-DOM-T4.md`, `docs/RDO/evidencia/P-0743-DOM-T5.md`, `docs/RDO/evidencia/P-0743-DOM-T5a.md`, `docs/RDO/evidencia/P-0743-DOM-T5b.md`, `docs/RDO/evidencia/P-0743-DOM-T7.md`, `docs/RDO/evidencia/P-0743-DOM-T8.md`, `docs/RUBRICA_DE_REVISAO.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0743-modelo-de-dominio.md`, `docs/plans/P-0744-spec-do-planejador.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/telemetria.tsv`, `tests/fixtures/modelo/fluxo-concluido.md`, `tests/fixtures/modelo/fluxo-valido.md`, `tests/fixtures/modelo/plano-forma-anterior.md`, `tests/fixtures/modelo/plano-invalido-2.md`, `tests/fixtures/modelo/plano-invalido.md`, `tests/fixtures/modelo/plano-sem-cabecalho.md`, `tests/fixtures/modelo/plano-sem-modelo.md`, `tests/test_modelo.py`, `tests/test_rdo.py`
- Atribuídos a outra tarefa do mesmo plano: `.claude/README.md` → `DOM-T4`, `.claude/agents/pantonic-consultant.md` → `DOM-T5`, `.claude/agents/pantonic-model-designer.md` → `DOM-T4`, `.claude/agents/pantonic-reviewer.md` → `DOM-T5`, `.claude/skills/scrum-master/SKILL.md` → `DOM-T5`, `.claude/tools/modelo.py` → `DOM-T3`, `README.md` → `DOM-T4`, `docs/RUBRICA_DE_REVISAO.md` → `DOM-T1`, `docs/plans/P-0743-modelo-de-dominio.md` → `DOM-T10`, `tests/fixtures/modelo/fluxo-concluido.md` → `DOM-T3`, `tests/fixtures/modelo/fluxo-valido.md` → `DOM-T3`, `tests/fixtures/modelo/plano-forma-anterior.md` → `DOM-T9`, `tests/fixtures/modelo/plano-invalido-2.md` → `DOM-T9`, `tests/fixtures/modelo/plano-invalido.md` → `DOM-T3`, `tests/fixtures/modelo/plano-sem-cabecalho.md` → `DOM-T3`, `tests/fixtures/modelo/plano-sem-modelo.md` → `DOM-T3`, `tests/test_modelo.py` → `DOM-T3`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0741-MC-T1-a-norma-e-a-gramatica-do-modelo-publicadas-nas-residencias-u.md`, `docs/RDO/P-0741-MC-T2-modelo-py-check-e-show-e-o-alvo-modelo-no-gerador-de-laudo.md`, `docs/RDO/P-0741-MC-T2a-o-campo-sem-consumidor-sai-da-dataclass-do-instrumento.md`, `docs/RDO/P-0741-MC-T2b-a-cadeia-sem-consumidor-sai-inteira-do-instrumento.md`, `docs/RDO/P-0741-MC-T3-os-tres-papeis-que-escrevem-o-modelo-planejador-revisor-e-co.md`, `docs/RDO/P-0741-MC-T4-o-loop-le-confere-e-mostra-o-modelo-scrum-master-e-passagem.md`, `docs/RDO/P-0741-MC-T4a-o-gate-do-modelo-no-fechamento-para-de-criar-o-vermelho-que.md`, `docs/RDO/P-0743-DOM-T1-a-norma-do-modelo-de-dominio-e-o-papel-que-a-executa.md`, `docs/RDO/P-0743-DOM-T2-a-gramatica-que-a-maquina-le.md`, `docs/RDO/P-0743-DOM-T3-o-instrumento-le-a-forma-nova.md`, `docs/RDO/P-0743-DOM-T3a-o-que-o-instrumento-e-a-gramatica-dizem-de-si-mesmos.md`, `docs/RDO/P-0743-DOM-T3b-a-referencia-cruzada-do-docstring.md`, `docs/RDO/P-0743-DOM-T4-o-modelador.md`, `docs/RDO/P-0743-DOM-T5-os-papeis-diante-do-modelador.md`, `docs/RDO/P-0743-DOM-T5a-a-costura-do-retorno-do-revisor.md`, `docs/RDO/P-0743-DOM-T5b-a-cadeia-do-retorno-do-emissor-ao-consumidor.md`, `docs/RDO/P-0743-DOM-T7-a-norma-da-forma-nova-propriedades-estado-e-versao.md`, `docs/RDO/P-0743-DOM-T8-a-gramatica-da-forma-nova.md`, `docs/RDO/evidencia/P-0741-MC-T1.md`, `docs/RDO/evidencia/P-0741-MC-T2.md`, `docs/RDO/evidencia/P-0741-MC-T2a.md`, `docs/RDO/evidencia/P-0741-MC-T2b.md`, `docs/RDO/evidencia/P-0741-MC-T3.md`, `docs/RDO/evidencia/P-0741-MC-T4.md`, `docs/RDO/evidencia/P-0741-MC-T4a.md`, `docs/RDO/evidencia/P-0741-MC-T5.md`, `docs/RDO/evidencia/P-0743-DOM-T1.md`, `docs/RDO/evidencia/P-0743-DOM-T2.md`, `docs/RDO/evidencia/P-0743-DOM-T3.md`, `docs/RDO/evidencia/P-0743-DOM-T3a.md`, `docs/RDO/evidencia/P-0743-DOM-T3b.md`, `docs/RDO/evidencia/P-0743-DOM-T4.md`, `docs/RDO/evidencia/P-0743-DOM-T5.md`, `docs/RDO/evidencia/P-0743-DOM-T5a.md`, `docs/RDO/evidencia/P-0743-DOM-T5b.md`, `docs/RDO/evidencia/P-0743-DOM-T7.md`, `docs/RDO/evidencia/P-0743-DOM-T8.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0744-spec-do-planejador.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/telemetria.tsv`
- Fato: 4 arquivo(s) fora dos alvos e sem atribuição: `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/tools/rdo.py`, `docs/OPERACOES_AS_IS.md`, `tests/test_rdo.py`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `GOVERNANCA.md`
```
diff --git a/GOVERNANCA.md b/GOVERNANCA.md
index 5526ecc..8d1e39a 100644
--- a/GOVERNANCA.md
+++ b/GOVERNANCA.md
@@ -88,10 +88,11 @@ adequado ao seu custo — a coluna *Modelo* é a tabela vinculante do **modelo p
 | Papel | Modelo | Responde por | Não faz |
 |---|---|---|---|
 | **Dono / gerente** | humano | Última instância e **fonte da doutrina de produto**: decide o quê e o porquê, ratifica decisões (`DR-`/`DP-`), valida cada sprint (§4.5), aceita release, autoriza saída do piso de regressão (§4.4) e comando destrutivo (§7 item 13) | Não desempata, no meio de uma execução, o que o plano deveria ter decidido — a pergunta que chega até ele em execução é sintoma de plano não-pronto (§7 itens 11 e 12) |
-| **Planejamento** | O mais poderoso disponível (Opus; Fable só sob solicitação explícita do dono) | PRD, arquitetura, specs, decisões de rota e decomposição em checklists de **tarefas atômicas fechadas** (G-PLANREADY, §7 item 11), cada uma com objetivo, arquivos-alvo, verificação e critério de pronto; **o dimensionamento de cada tarefa** sob a *Diretriz de dimensionamento de tarefa* desta seção — coesão, autossuficiência em contexto e ocupação estimada, exercidas no recorte, não publicadas no card; **a revisão de plano, com exclusividade** — indício de que o plano precisa mudar chega aqui e só aqui, e o planejador decide por si o que for **técnico ou tático**, escalando ao dono o que for **estratégico ou alterar escopo**; **a revisão do README ao encerrar cada sprint** — tarefa nomeada do próprio plano, com o guarda executável como instrumento e o veredito do dono como aceite (G-README dever 2, §7 item 14); sprint planejada sem essa tarefa é plano incompleto; **o risco de interrupção de cada card** — plano em que um executor frio pararia por dúvida sem contingência fechada não se libera (G-NOASK, §7 item 18) | Não executa: não implementa, não fecha tarefa, não transforma dúvida própria em pergunta ao executor |
-| **Orquestração** | Melhor custo-benefício (Sonnet); o loop roda no contexto principal, onde o dono interrompe sem derrubar a sessão, e **para para pedir `/model`** quando a fase exige outro modelo | Conduzir um plano do começo ao fim: despachar cada tarefa ao papel competente com o dossiê fechado, rotear a linha de retorno do executor e o laudo do `reviewer` (aprovado segue, reprovado volta ao mesmo escopo, escalado sobe ao dono), registrar a telemetria medida e arquivar o resultado | Não implementa, não julga a entrega — o veredito é da revisão — e não decide arquitetura: obstáculo à rota e dossiê não fechado sobem ao **planejamento** (G-REPLAN e G-NOASK, §7 itens 17 e 18), nunca viram improviso do loop nem pergunta ao dono no meio da janela — ao dono chega, no relatório de encerramento, só o que o planejador classificar como estratégico. **Não revisa plano** — roteia a escalada ao planejamento, não replaneja |
+| **Planejamento** | O mais poderoso disponível (Opus; Fable só sob solicitação explícita do dono) | PRD, arquitetura, specs, decisões de rota e decomposição em checklists de **tarefas atômicas fechadas** (G-PLANREADY, §7 item 11), cada uma com objetivo, arquivos-alvo, verificação e critério de pronto; **o dimensionamento de cada tarefa** sob a *Diretriz de dimensionamento de tarefa* desta seção — coesão, autossuficiência em contexto e ocupação estimada, exercidas no recorte, não publicadas no card; **a revisão de plano, com exclusividade** — indício de que o plano precisa mudar chega aqui e só aqui, e o planejador decide por si o que for **técnico ou tático**, escalando ao dono o que for **estratégico ou alterar escopo**; **a revisão do README ao encerrar cada sprint** — tarefa nomeada do próprio plano, com o guarda executável como instrumento e o veredito do dono como aceite (G-README dever 2, §7 item 14); sprint planejada sem essa tarefa é plano incompleto; **o risco de interrupção de cada card** — plano em que um executor frio pararia por dúvida sem contingência fechada não se libera (G-NOASK, §7 item 18);
```
[truncado em 4000 caracteres]

### `.claude/agents/pantonic-planner.md`
```
diff --git a/.claude/agents/pantonic-planner.md b/.claude/agents/pantonic-planner.md
index b067486..d75a2a0 100644
--- a/.claude/agents/pantonic-planner.md
+++ b/.claude/agents/pantonic-planner.md
@@ -133,6 +133,19 @@ fora. Classifique cada uma pela escada de `GOVERNANCA.md` §3:
   anterior ou do próprio pedido; (c) o dono ainda não a respondeu nesta conversa. Falhou em um →
   não é pergunta: é decisão sua com default registrado.
 
+**Forma de artefato que o dono lê é decisão dele, não sua.** Quando o produto do plano é a
+**interface de leitura do dono** — um relatório, uma seção que ele valida, a saída de um
+instrumento que substitui a leitura de um documento —, a **forma** dessa interface passa no teste
+de legitimidade e é pergunta, não decisão técnica: duas formas levam a planos materialmente
+diferentes, e quando a interface não existe ainda não há default a derivar de doutrina nenhuma. Ela
+sobe na rodada de decisões como **worked example** — a leitura pronta, preenchida com dado do
+próprio plano, em ≤ 15 linhas, com a alternativa ao lado —, nunca como prosa normativa descrevendo
+a forma. Prosa normativa sobre forma de leitura não é julgável pelo dono antes de existir o
+primeiro artefato. Caso medido: o `P-0741` prescreveu orações independentes com estado por frase,
+entregou os cinco estratos, 20 orações confirmadas e três guardas verdes, e levou `no-go` **de
+forma** no Marco 2 — o dono queria objetos e operações encadeadas, com estado como posição no
+fluxo (2026-09-20, `RP-1` do `P-0741`).
+
 Sobrou pergunta legítima → **SAÍDA 2 — Rodada de decisões**: **uma** mensagem, todas as questões
 juntas, cada uma com contexto em ≤ 2 linhas, opções, **sua recomendação** e a consequência de cada
 opção sobre o plano. Toda questão de rota lista também a opção **registrar e não agir** (adiar,
@@ -149,17 +162,35 @@ Esqueleto fixo do plano, nesta ordem e sem seção de questões abertas:
 ```
 # P-NNNN — <título>            (cabeçalho: data de origem, iniciativa, plano de origem se derivado)
 ## 0. O problema, verbatim
-## 1. Fatos estabelecidos        (cada fato com a fonte: dossiê, doc §, decisão anterior)
-## 2. Decisões                   (tabela id → valor → razão; toda decisão consumida por ≥ 1 tarefa)
-## 3. Invariantes de execução    (regras que valem para todas as tarefas — e que cada card repete
+## 1. Modelo conceitual          (GOVERNANCA.md §3.2 — escrito pelo pantonic-model-designer ANTES
+                                  de decompor: objetos com propriedades, fluxo de operações OP-<n>
+                                  que as alteram, estado inicial e final, registro de versões;
+                                  nada carrega andamento; é o que o dono lê no Marco 1 e dá go/no-go)
+## 2. Fatos estabelecidos        (cada fato com a fonte: dossiê, doc §, decisão anterior)
+## 3. Decisões                   (tabela id → valor → razão; toda decisão consumida por ≥ 1 tarefa)
+## 4. Invariantes de execução    (regras que valem para todas as tarefas — e que cada card repete
                                   na parte que o vincula: o executor não é obrigado a ler esta seção)
-## 4. Tarefas                    (cards, anatomia abaixo; ordem = ordem de dependência)
-## 5. Ordem de execução          (grafo explícito: quem depende de quem; o que roda em paralelo)
-## 6. Fora de escopo (explícito) (o que este plano não faz e onde isso mora, se mora)
-## 7. Riscos                     (cada risco com resposta pré-decidida: o que o executor faz se ocorrer)
-## 8. Achados da execução        (vazio; apensado por quem executa/orquestra)
+## 5. Tarefas                    (cards, anatomia abaixo; ordem = ordem de dependência)
+## 6. Ordem de execução          (grafo explícito: quem depende de quem; o que roda em paralelo)
+## 7. Fora de escopo (explícito) (o que este plano não faz e onde isso mora, se mora)
+## 8. Riscos                     (cada risco com resposta pré-decidida: o que o executor faz se ocorrer)
+## 9. Achados da execuç
```
[truncado em 4000 caracteres]

### `.claude/skills/diario-de-obras/SKILL.md`
```
diff --git a/.claude/skills/diario-de-obras/SKILL.md b/.claude/skills/diario-de-obras/SKILL.md
index fd525c0..264e3a8 100644
--- a/.claude/skills/diario-de-obras/SKILL.md
+++ b/.claude/skills/diario-de-obras/SKILL.md
@@ -131,7 +131,9 @@ objeto:
 
 Transcrição normativa de `docs/plans/P-0739-backlog-instrumento.md` §2.1–§2.4 e §2.7 — é a
 gramática que `.claude/tools/backlog.py` (§3 do mesmo plano) lê e escreve. Esta seção é a
-residência única do texto; o plano de origem não a recopia depois da transcrição.
+residência única do texto; o plano de origem não a recopia depois da transcrição. A subseção
+"Modelo de domínio (seção do plano)" transcreve `docs/plans/P-0743-modelo-de-dominio.md` §5 e §15 —
+onde as duas divergem, governa a §15 — e é lida por `.claude/tools/modelo.py`.
 
 ### Item e residência
 
@@ -170,11 +172,36 @@ Linha viva: começa com `- ` e contém um caminho `docs/plans/P-NNNN-<slug>.md`
 Drenada: prefixada `- [drenado AAAA-MM-DD] ` e movida **verbatim** para `_INBOX_HISTORICO.md`.
 Contador: `**Próximo id de plano: P-NNNN.**` — `drain` o recalcula como `max(id visto) + 1`.
 
-### Máquina de transições (forma para o instrumento)
+### Modelo de domínio (seção do plano)
 
-Tabela da residência única acima ("Status — residência única" → "Máquina de transições") transcrita
-para `_TRANSICOES: dict[tuple[str, str], ...]`; `blocked` exige `--razao`; `done`/`cancelled` são
-terminais; `superseded` só para plano. Transição fora da tabela → exit 1 sem escrever nada.
+Seção `## 1. Modelo conceitual` do plano (`GOVERNANCA.md` §3.2), delimitada pelo próximo heading de
+nível 2. Dentro dela, nesta ordem:
+
+| elemento | forma | regra |
+|---|---|---|
+| cabeçalho | `**Estado do modelo:** versão <n> · AAAA-MM-DD · autor: <papel> · <k> operações · <p> propriedades · situação: <vigente \| pendente>` | linha única; obrigatória (`V13`); `<n>` monotônico e `situação` é `vigente` na seção `## 1` |
+| objetos | `### 1.1 Objetos` + tabela `\| objeto \| o que é \| propriedades \| contrato \| origem \|`; `<objeto>` é um nome em linguagem corrente, único na tabela; `<propriedades>` é uma lista separada por vírgula, em linguagem corrente, não vazia; `<origem>` é `externo` ou `OP-<n>` | obrigatória (`V13`); objeto sem propriedade é violação (`V15`); `<origem>` `OP-<n>` existe no fluxo (`V7`); objeto de origem `externo` é citado por alguma operação (`V6`) |
+| operações | `### 1.2 Fluxo de operações`; cada operação é o par de linhas: `- **OP-<n>** — <texto>` e, na linha seguinte, `  - \`precisa de: <objeto>[, <objeto>]\` · \`altera: <objeto>.<propriedade>[, <objeto>.<propriedade>]\` · \`tarefas: <ID>[, <ID>]\`` | numeração `1..k` na ordem do encadeamento, sem salto (`V8`); `<n>` único (`V11`); `<texto>` sem crase e sem `/` (`V12`); todo `<objeto>` existe na tabela de objetos (`V5`); todo par `<objeto>.<propriedade>` de `altera:` existe na tabela de objetos (`V16`); toda `<ID>` existe como `### <ID> — …` no plano (`V3`); lista de tarefas não vazia (`V1`); operação com `<n>` maior que 1 cita ao menos um objeto de origem `OP-<m>` (`V9`), e esse `<m>` é menor que `<n>` (`V10`). Subtítulos `**A. …**` entre operações são livres e ignorados |
+| estado | `### 1.3 Estado inicial e estado final` + tabela `\| propriedade \| estado inicial \| estado final \|`; a célula `propriedade` é `<objeto>.<propriedade>`; `estado inicial` é o retrato antes da implementação; `estado final` é o desejo do dono, quantificável ou qualificável | obrigatória (`V13`); toda propriedade da tabela de objetos tem exatamente uma linha aqui (`V17`) |
+| versões | `### 1.4 Registro de versões` + tabela `\| versão \| data \| situação \| por \|`; `situação` é `vigente`, `pendente` ou `obsoleta`; a linha `obsoleta` registra por aceite de qual versão ela caiu, e o conteúdo dela não fica no plano | obrigatória (`V13`); exatamente uma linha `vigente` (`V19`) |
+| campo do card | `- **Operação do modelo:** \`OP-<a>\`[, \`OP-<b>\`]` como campo de todo `### <ID> — …` do plano, seguido, 
```
[truncado em 4000 caracteres]

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
