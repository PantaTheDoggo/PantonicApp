# Evidência de revisão — P-0743 DOM-T5b

## Diff (`git diff --stat`)
```
.claude/README.md                          |   3 +-
 .claude/agents/pantonic-consultant.md      |   5 +-
 .claude/agents/pantonic-planner.md         |  51 +-
 .claude/agents/pantonic-reviewer.md        |  28 +-
 .claude/skills/diario-de-obras/SKILL.md    |  28 +-
 .claude/skills/passagem-de-bastao/SKILL.md |   6 +-
 .claude/skills/scrum-master/SKILL.md       |  52 +-
 .claude/tools/rdo.py                       |   8 +-
 GOVERNANCA.md                              |  61 ++-
 README.md                                  |  18 +-
 docs/DIARIO_DE_OBRAS.md                    |  57 +-
 docs/RDO/INDEX.md                          |  15 +
 docs/RUBRICA_DE_REVISAO.md                 |   7 +-
 docs/plans/P-0741-modelo-conceitual.md     | 842 ++++++++++++++++++++++++++---
 docs/plans/_INBOX.md                       |   3 +-
 docs/plans/_INBOX_HISTORICO.md             |   2 +
 docs/telemetria.tsv                        |  47 ++
 tests/test_rdo.py                          |  19 +
 18 files changed, 1133 insertions(+), 119 deletions(-)
```

## Arquivos tocados
- `.claude/README.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-consultant.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-model-designer.md` — atribuição: alheio; estado git: `??`
- `.claude/agents/pantonic-planner.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-reviewer.md` — atribuição: da entrega; estado git: ` M`
- `.claude/skills/diario-de-obras/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/passagem-de-bastao/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/scrum-master/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/tools/modelo.py` — atribuição: alheio; estado git: `??`
- `.claude/tools/rdo.py` — atribuição: alheio; estado git: ` M`
- `GOVERNANCA.md` — atribuição: alheio; estado git: ` M`
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
- Recorte: desde `e0efcf6`
- Arquivos-alvo declarados: `.claude/skills/scrum-master/SKILL.md`, `.claude/agents/pantonic-reviewer.md`
- Literais não reconhecidos como caminho (2): `I-5`, `- Saída:`
- Arquivos tocados: `.claude/README.md`, `.claude/agents/pantonic-consultant.md`, `.claude/agents/pantonic-model-designer.md`, `.claude/agents/pantonic-planner.md`, `.claude/agents/pantonic-reviewer.md`, `.claude/skills/diario-de-obras/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/modelo.py`, `.claude/tools/rdo.py`, `GOVERNANCA.md`, `README.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/OPERACOES_AS_IS.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0741-MC-T1-a-norma-e-a-gramatica-do-modelo-publicadas-nas-residencias-u.md`, `docs/RDO/P-0741-MC-T2-modelo-py-check-e-show-e-o-alvo-modelo-no-gerador-de-laudo.md`, `docs/RDO/P-0741-MC-T2a-o-campo-sem-consumidor-sai-da-dataclass-do-instrumento.md`, `docs/RDO/P-0741-MC-T2b-a-cadeia-sem-consumidor-sai-inteira-do-instrumento.md`, `docs/RDO/P-0741-MC-T3-os-tres-papeis-que-escrevem-o-modelo-planejador-revisor-e-co.md`, `docs/RDO/P-0741-MC-T4-o-loop-le-confere-e-mostra-o-modelo-scrum-master-e-passagem.md`, `docs/RDO/P-0741-MC-T4a-o-gate-do-modelo-no-fechamento-para-de-criar-o-vermelho-que.md`, `docs/RDO/P-0743-DOM-T1-a-norma-do-modelo-de-dominio-e-o-papel-que-a-executa.md`, `docs/RDO/P-0743-DOM-T2-a-gramatica-que-a-maquina-le.md`, `docs/RDO/P-0743-DOM-T3-o-instrumento-le-a-forma-nova.md`, `docs/RDO/P-0743-DOM-T3a-o-que-o-instrumento-e-a-gramatica-dizem-de-si-mesmos.md`, `docs/RDO/P-0743-DOM-T3b-a-referencia-cruzada-do-docstring.md`, `docs/RDO/P-0743-DOM-T4-o-modelador.md`, `docs/RDO/P-0743-DOM-T5-os-papeis-diante-do-modelador.md`, `docs/RDO/P-0743-DOM-T5a-a-costura-do-retorno-do-revisor.md`, `docs/RDO/evidencia/P-0741-MC-T1.md`, `docs/RDO/evidencia/P-0741-MC-T2.md`, `docs/RDO/evidencia/P-0741-MC-T2a.md`, `docs/RDO/evidencia/P-0741-MC-T2b.md`, `docs/RDO/evidencia/P-0741-MC-T3.md`, `docs/RDO/evidencia/P-0741-MC-T4.md`, `docs/RDO/evidencia/P-0741-MC-T4a.md`, `docs/RDO/evidencia/P-0741-MC-T5.md`, `docs/RDO/evidencia/P-0743-DOM-T1.md`, `docs/RDO/evidencia/P-0743-DOM-T2.md`, `docs/RDO/evidencia/P-0743-DOM-T3.md`, `docs/RDO/evidencia/P-0743-DOM-T3a.md`, `docs/RDO/evidencia/P-0743-DOM-T3b.md`, `docs/RDO/evidencia/P-0743-DOM-T4.md`, `docs/RDO/evidencia/P-0743-DOM-T5.md`, `docs/RDO/evidencia/P-0743-DOM-T5a.md`, `docs/RUBRICA_DE_REVISAO.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0743-modelo-de-dominio.md`, `docs/plans/P-0744-spec-do-planejador.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/telemetria.tsv`, `tests/fixtures/modelo/fluxo-concluido.md`, `tests/fixtures/modelo/fluxo-valido.md`, `tests/fixtures/modelo/plano-forma-anterior.md`, `tests/fixtures/modelo/plano-invalido-2.md`, `tests/fixtures/modelo/plano-invalido.md`, `tests/fixtures/modelo/plano-sem-cabecalho.md`, `tests/fixtures/modelo/plano-sem-modelo.md`, `tests/test_modelo.py`, `tests/test_rdo.py`
- Atribuídos a outra tarefa do mesmo plano: `.claude/README.md` → `DOM-T4`, `.claude/agents/pantonic-consultant.md` → `DOM-T5`, `.claude/agents/pantonic-model-designer.md` → `DOM-T4`, `.claude/agents/pantonic-planner.md` → `DOM-T5`, `.claude/skills/diario-de-obras/SKILL.md` → `DOM-T2`, `.claude/tools/modelo.py` → `DOM-T3`, `GOVERNANCA.md` → `DOM-T1`, `README.md` → `DOM-T4`, `docs/RUBRICA_DE_REVISAO.md` → `DOM-T1`, `tests/fixtures/modelo/fluxo-concluido.md` → `DOM-T3`, `tests/fixtures/modelo/fluxo-valido.md` → `DOM-T3`, `tests/fixtures/modelo/plano-invalido.md` → `DOM-T3`, `tests/fixtures/modelo/plano-sem-cabecalho.md` → `DOM-T3`, `tests/fixtures/modelo/plano-sem-modelo.md` → `DOM-T3`, `tests/test_modelo.py` → `DOM-T3`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0741-MC-T1-a-norma-e-a-gramatica-do-modelo-publicadas-nas-residencias-u.md`, `docs/RDO/P-0741-MC-T2-modelo-py-check-e-show-e-o-alvo-modelo-no-gerador-de-laudo.md`, `docs/RDO/P-0741-MC-T2a-o-campo-sem-consumidor-sai-da-dataclass-do-instrumento.md`, `docs/RDO/P-0741-MC-T2b-a-cadeia-sem-consumidor-sai-inteira-do-instrumento.md`, `docs/RDO/P-0741-MC-T3-os-tres-papeis-que-escrevem-o-modelo-planejador-revisor-e-co.md`, `docs/RDO/P-0741-MC-T4-o-loop-le-confere-e-mostra-o-modelo-scrum-master-e-passagem.md`, `docs/RDO/P-0741-MC-T4a-o-gate-do-modelo-no-fechamento-para-de-criar-o-vermelho-que.md`, `docs/RDO/P-0743-DOM-T1-a-norma-do-modelo-de-dominio-e-o-papel-que-a-executa.md`, `docs/RDO/P-0743-DOM-T2-a-gramatica-que-a-maquina-le.md`, `docs/RDO/P-0743-DOM-T3-o-instrumento-le-a-forma-nova.md`, `docs/RDO/P-0743-DOM-T3a-o-que-o-instrumento-e-a-gramatica-dizem-de-si-mesmos.md`, `docs/RDO/P-0743-DOM-T3b-a-referencia-cruzada-do-docstring.md`, `docs/RDO/P-0743-DOM-T4-o-modelador.md`, `docs/RDO/P-0743-DOM-T5-os-papeis-diante-do-modelador.md`, `docs/RDO/P-0743-DOM-T5a-a-costura-do-retorno-do-revisor.md`, `docs/RDO/evidencia/P-0741-MC-T1.md`, `docs/RDO/evidencia/P-0741-MC-T2.md`, `docs/RDO/evidencia/P-0741-MC-T2a.md`, `docs/RDO/evidencia/P-0741-MC-T2b.md`, `docs/RDO/evidencia/P-0741-MC-T3.md`, `docs/RDO/evidencia/P-0741-MC-T4.md`, `docs/RDO/evidencia/P-0741-MC-T4a.md`, `docs/RDO/evidencia/P-0741-MC-T5.md`, `docs/RDO/evidencia/P-0743-DOM-T1.md`, `docs/RDO/evidencia/P-0743-DOM-T2.md`, `docs/RDO/evidencia/P-0743-DOM-T3.md`, `docs/RDO/evidencia/P-0743-DOM-T3a.md`, `docs/RDO/evidencia/P-0743-DOM-T3b.md`, `docs/RDO/evidencia/P-0743-DOM-T4.md`, `docs/RDO/evidencia/P-0743-DOM-T5.md`, `docs/RDO/evidencia/P-0743-DOM-T5a.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0743-modelo-de-dominio.md`, `docs/plans/P-0744-spec-do-planejador.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/telemetria.tsv`
- Fato: 6 arquivo(s) fora dos alvos e sem atribuição: `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/tools/rdo.py`, `docs/OPERACOES_AS_IS.md`, `tests/fixtures/modelo/plano-forma-anterior.md`, `tests/fixtures/modelo/plano-invalido-2.md`, `tests/test_rdo.py`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/skills/scrum-master/SKILL.md`
```
diff --git a/.claude/skills/scrum-master/SKILL.md b/.claude/skills/scrum-master/SKILL.md
index d126db8..8cd7d64 100644
--- a/.claude/skills/scrum-master/SKILL.md
+++ b/.claude/skills/scrum-master/SKILL.md
@@ -57,7 +57,12 @@ Dez passos, nesta ordem.
   (`.claude/skills/passagem-de-bastao/SKILL.md`, seção "Gate de delegação", sete itens), sem
   recopiar o texto de nenhum dos dois. Recusa de qualquer um: **não delega** — vai ao passo 10 por `B3`.
 
-  Aprovados os dois, e **antes** de delegar, materializar `ready` → `in-progress` no kanban
+  Terceiro gate, mecânico: `python .claude/tools/modelo.py check --plano <plano>`
+  (`GOVERNANCA.md` §3.2). Exit `1`: **não delega** — o stderr vai à razão e a tarefa cai em
+  `B3`. Exit `2`: plano anterior à doutrina do modelo; segue, com a nota "sem modelo" no
+  relatório. Exit `0`: segue.
+
+  Aprovados os três, e **antes** de delegar, materializar `ready` → `in-progress` no kanban
   (`DP-G` item 1, consequência 3) — ato exclusivo do `scrum-master`.
 - **Saída:** tarefa materializada em `in-progress` e liberada para despacho, ou parada com o que
   falta fechar.
@@ -103,7 +108,12 @@ Dez passos, nesta ordem.
 ### Passo 6 — Despacho do `reviewer`
 
 - **Gatilho:** **gatilho 1** da `DP-E` — a tarefa entrou em `review`. Tarefa `blocked` **não** passa
-  por aqui (`DP-G` item 4): não há entregável a julgar.
+  por aqui (`DP-G` item 4): não há entregável a julgar. **Confira, antes de invocar, que o status materializado da tarefa no plano é mesmo
+  `review`** — é o estado em que o reviewer julga, e materializá-lo é ato do passo 5. O
+  reviewer **não escreve** no modelo de domínio do plano: o andamento é derivado das tarefas e
+  nenhum papel o grava (`GOVERNANCA.md` §3.2), então não há gravação de revisor a conferir
+  aqui. Status diferente de `review` é defeito de condução do passo 5, não do revisor:
+  materialize e só então invoque.
 - **Entrada:** o **mesmo dossiê** que o executor recebeu; plano e identificador da tarefa. Nenhum
   caminho de RDO é repassado.
 - **Ação:** gerar o dossiê de evidência mecânica, exigido pelo `reviewer`:
@@ -115,20 +125,25 @@ Dez passos, nesta ordem.
   ```
 
   Redirecionar a saída padrão do comando. Em seguida invocar `pantonic-reviewer` com o dossiê da
-  tarefa e o caminho do dossiê de evidência, instrução de devolver só as duas linhas de veredito.
-- **Saída:** duas linhas do `reviewer`.
+  tarefa e o caminho do dossiê de evidência. **Não limite o retorno dele às duas linhas.**
+  A forma do retorno é a que a definição do papel fixa: as duas linhas de veredito e, quando o
+  passo `5a` apurar divergência, o dossiê `Ato de modelo` de `conflito` anexo abaixo delas
+  (`GOVERNANCA.md` §3.2). É esse dossiê que o passo 8 consome para despachar o modelador.
+- **Saída:** as duas linhas do `reviewer` e, quando houver, o dossiê `Ato de modelo` anexo.
 
 ### Passo 7 — Leitura do veredito
 
 - **Gatilho:** retorno do `reviewer`.
-- **Entrada:** as duas linhas fixas:
+- **Entrada:** as duas linhas fixas e, quando houver, o dossiê anexo abaixo delas:
   `<tarefa> <veredito> <percentual> bloqueante=<dimensão|nenhuma>`
   `laudo=<caminho>`
+  Dossiê presente: são os seis campos do `Ato de modelo` (`GOVERNANCA.md` §3.2). O loop não o
+  reescreve, não o resume e não o interpreta — passa-o inteiro ao passo 8.
 - **Ação:** ler `veredito` ∈ {`aprovado`, `ressalva`, `reprovado`}, `bloqueante` e o caminho do
   laudo — calculados pelo gerador, não recalculados pelo loop. Colher a `recomendação` **do
   laudo**, campo fechado (`seguir`, `seguir com ressalva`, `refazer`, `escalar`), lido por `A6`,
   `A6a`, `A8a`, `A8`, `A9` e `B1`.
-- **Saída:** tripla (`veredito`, `bloqueante`, `recomendação`) para o roteamento.
+- **Saída:** tripla (`veredito`, `bloqueante`, `recomendação`) para o roteamento, mais o dossiê `Ato de modelo` quando ele veio no retorno.
 
 ### Passo 8 — Roteamento, bloco A
 
@@ -136,7 +151,11 @@ Dez passos, nesta ordem.
 - **Entrada:** `status`, `veredito`,
```
[truncado em 4000 caracteres]

### `.claude/agents/pantonic-reviewer.md`
```
diff --git a/.claude/agents/pantonic-reviewer.md b/.claude/agents/pantonic-reviewer.md
index 6ca738e..fb8248a 100644
--- a/.claude/agents/pantonic-reviewer.md
+++ b/.claude/agents/pantonic-reviewer.md
@@ -25,8 +25,8 @@ das faixas. Abra a régua durante a revisão; marcação feita de memória é ma
   travado no dossiê de evidência, e marcar `conforme` contra um vermelho declarado é recusado
   pelo gerador. O juízo opera nas dimensões de fonte de juízo e nas faixas que a evidência
   mecânica deixa em aberto.
-- Achado de processo (`docs/RUBRICA_DE_REVISAO.md` §6) tem campo próprio e três alvos possíveis —
-  `dossiê`, `doutrina`, `rubrica`. Ele nunca rebaixa dimensão de entrega e sempre sai com rota.
+- Achado de processo (`docs/RUBRICA_DE_REVISAO.md` §6) tem campo próprio e quatro alvos possíveis —
+  `dossiê`, `doutrina`, `rubrica`, `modelo`. Ele nunca rebaixa dimensão de entrega e sempre sai com rota.
 - **Decisão tomada pela entrega que o card não fechou** (nome, rota, valor, teste inventado) e
   **parada por dúvida que o card não previu** são a mesma classe: defeito do dossiê, não da
   execução (G-NOASK, `GOVERNANCA.md` §7 item 18). Saem como achado de processo de alvo `dossiê`,
@@ -44,7 +44,12 @@ das faixas. Abra a régua durante a revisão; marcação feita de memória é ma
 
   O instrumento se executa; abrir o fonte para entender a chamada é sinal de documentação
   insuficiente, não caminho normal.
-- Saída: duas linhas de veredito ao chamador e o laudo em documento próprio, gravado pelo gerador
+- **Você não escreve no modelo de domínio do plano** (`GOVERNANCA.md` §3.2;
+  `docs/RUBRICA_DE_REVISAO.md` §7). Quando a entrega contradiz o texto de uma operação, o laudo
+  leva `--achado-processo modelo "<operação e a divergência>"` e o texto fica como está. A escrita
+  é do `pantonic-model-designer`, despachado por quem conduz a sessão.
+- Saída: as duas linhas de veredito ao chamador, o dossiê `Ato de modelo` de `conflito` quando o
+  passo 7 o exigir, e o laudo em documento próprio, gravado pelo gerador
   em `docs/RDO/laudos/<plano>-<tarefa>.md`.
 - O laudo carrega o **pacote**: veredito, percentual, dimensão bloqueante, recomendação e
   pendência. Com esses cinco campos o `scrum-master` fecha o registro da tarefa sem falha, e é essa
@@ -96,6 +101,13 @@ das faixas. Abra a régua durante a revisão; marcação feita de memória é ma
    evidência nomeada.
 5. **Achados de processo** — separe o que acusa o dossiê, a doutrina ou a rubrica, nomeie o alvo e
    dê a rota (tíquete indexado, item de replanejamento ou emenda à rubrica).
+5a. **Modelo de domínio** — leia o campo `Operação do modelo` do card. Para cada operação citada,
+compare o texto dela com o que está no repositório. Corresponde: nada a fazer — o andamento do
+modelo é derivado das tarefas e ninguém o grava. Não corresponde: o laudo leva
+`--achado-processo modelo "<operação e a divergência>"`, e você devolve, junto com o laudo, o
+dossiê `Ato de modelo` de `conflito` com os seis campos da norma. Você não abre o plano para
+escrever, em nenhuma hipótese. Plano em forma anterior, sem o campo `Operação do modelo`: nada a
+fazer.
 6. **Laudo** — emita pelo gerador, com um flag por dimensão:
 
    ```
@@ -113,13 +125,19 @@ das faixas. Abra a régua durante a revisão; marcação feita de memória é ma
    loop — que a roteia ao **planejamento** (G-REPLAN/G-NOASK, `GOVERNANCA.md` §7 itens 17-18);
    ao dono chega só o que o planejador classificar como estratégico, nunca a sua linha direto. Percentual, veredito, bloqueante e recomendação saem do cálculo, e marcação inconsistente
    com a régua faz o gerador falhar.
-7. **Retorno ao chamador** — duas linhas, nada além:
+7. **Retorno ao chamador** — as duas linhas fixas e, quando houver, o dossiê:
 
    ```
    <tarefa> <veredito> <percentual> bloqueante=<dimensão|nenhuma>
    laudo=<caminho>
    ```
 
+   **Nada além disso, com uma exceção fechada:** se o passo `5a` apurou divergência entre a
+   entrega e o texto de uma oper
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
