# P-0734 — Execução autônoma: o scrum-master do loop de tarefas

- **Origem:** 2026-08-08 — pedido do dono: a execução do backlog deixa de exigir um round-trip
  humano por tarefa (abrir contexto novo, invocar `proximo-passo`, escolher modelo) e passa a ser
  um loop conduzido pelo próprio agente, com revisão por laudo e arquivamento em RDO
- **Iniciativa:** `EXECUCAO-AUTONOMA` · **Prefixo de tarefa:** `EXA-`
- **Depende de:** nada em execução. Convive com `P-0733-divida-do-hub` (`in progress`); não toca
  nenhum dos 12 tíquetes daquele plano nem os artefatos que ele reescreve
- **Fecha em:** aceite do dono sobre o `README.md` (`T17`), depois do piloto medido (`T16`).
  **Sem bump e sem tag:** a versão está congelada em `0.0.0` (`DE-7`) e todo registro de mudança
  vai para a seção `[Não lançado]` do `CHANGELOG.md`
- **Checagem de versão do kit:** modo hub — versão **congelada em `0.0.0`**, comparação local ×
  remoto **suspensa**, nada a comparar. Gatilho de revisão de doutrina (`GOVERNANCA.md` §7.1):
  a rodada armada pelo fechamento do `P-0732` já está **atribuída** à `DHB-T2` do `P-0733`, em
  execução — este plano **não** a herda e não abre rodada nova

## 0. O problema

O fluxo vigente de execução de backlog custa ao dono **um round-trip por tarefa atômica**: abrir
contexto novo, invocar a skill `proximo-passo`, conferir o modelo ativo, ler o handover, limpar o
contexto, repetir. Três consequências medidas ou observáveis:

**O dono é o escalonador.** A escolha de modelo por fase é vinculante (`GOVERNANCA.md` §3) mas não é
automatizável no contexto principal: nenhum agente troca o próprio modelo. Hoje isso significa que
**cada** tarefa exige do dono a decisão "que modelo esta fase pede" — trabalho de despacho, não de
governo.

**Não existe revisão entre a execução e o registro.** O executor escreve as próprias notas no diário
e declara o próprio pronto. Os guardrails executáveis (`guardrails-check`, conformance, piso de
regressão) cobrem o que é mecânico; nada cobre a pergunta "o que foi entregue é o que a tarefa
pedia?". Desvio de escopo, critério de pronto atendido pela metade, mau cheiro introduzido e
insuficiência de decomposição só aparecem depois — quando aparecem, e sempre longe da tarefa que os
gerou.

**O registro de fechamento é redigido, não gerado.** O formato do bullet do diário, da linha
`Consumo:`, das "Notas de execução" e do handover está escrito em prosa normativa dentro de
`.claude/skills/handover/SKILL.md`, `.claude/skills/proximo-passo/SKILL.md` e
`.claude/agents/pantonic-executor.md`. Esse texto é **pago em todos os turnos de todos os
subagentes**, e mesmo assim o formato deriva — porque cada agente o reaprende por leitura. O
fechamento em si custa Grep + Read + Edit em documentos grandes, com ingestão, quando poderia custar
uma chamada de função.

Os três problemas têm o mesmo remédio: **um papel de orquestração que despacha, um papel de revisão
que julga contra o dossiê, e um documental que se gera em vez de se redigir.**

## 1. Decisões (fechadas no ato do planejamento)

| id | Decisão | Origem |
|---|---|---|
| `DA-1` | **O scrum-master é uma skill, não um agente.** O papel vive no **contexto principal**, materializado como `.claude/skills/scrum-master/`, porque o loop autônomo precisa de um ponto onde o dono interrompe sem derrubar a sessão: a orquestração é o único elo que não pode ficar fora do alcance direto de quem responde por ela. É também o que o teste de residência manda (`GOVERNANCA.md` §3.1, pergunta 3: procedimento reexecutável com gatilho → skill). **O motivo original caiu e foi substituído.** O plano fundava a decisão numa impossibilidade técnica — subagente não invocaria subagente —, e a `T1` mediu o contrário: aninhamento funciona, observado até profundidade 3. A decisão foi reexaminada e **mantida**, com o argumento trocado de impossibilidade para controle; profundidade 3 observada numa única tentativa não é base para pendurar a arquitetura do orquestrador. | planejamento, 2026-08-08; reexaminada e ratificada pelo dono após a `T1`, 2026-08-08 |
| `DA-2` | **O reviewer é um agente** (`.claude/agents/pantonic-reviewer.md`), subagente de contexto próprio, **sem ferramenta de edição de código**: lê repositório e escreve **só** no caminho do laudo. Independência não é pedida ao prompt — é imposta pela lista de ferramentas. | planejamento, 2026-08-08 |
| `DA-3` | **Alcance: hub primeiro, medir, depois propagar** (decisão do dono, 2026-08-08). Nenhuma tarefa deste plano toca os repositórios derivados. A promoção a kit distribuído tem **gatilho registrado** no §7, condicionado ao resultado do piloto da `T16`. | dono, 2026-08-08 |
| `DA-4` | **Três decisões de desenho são postergadas por decisão do dono** (2026-08-08) e viram tarefas próprias: transporte do pacote de retorno (`T2`), política de autonomia e tetos (`T3`), formato estruturado da tarefa no plano (`T4`). **Cada uma dessas tarefas fecha, no seu próprio escopo, o dossiê das tarefas que dependem dela** — caso contrário este plano estaria publicando tarefas abertas, exatamente o que `G-PLANREADY` item 5 proíbe. Uma tarefa dependente cujo dossiê ainda não foi fechado **não é delegável**, e a skill `proximo-passo` deve recusá-la. | dono + planejamento, 2026-08-08 |
| `DA-5` | **Fronteira de registro, sem terceira fonte:** o **RDO** (`docs/RDO/<plano>-<tarefa>-<slug>.md`) passa a ser o **registro canônico da tarefa** (dossiê, laudo, desdobramento, ponteiros); o **diário de obras** fica reduzido a kanban — índice, status e ponteiro para o RDO; `docs/telemetria.tsv` continua **fonte única do número** de consumo. Nenhum dos três repete o conteúdo do outro. Efeito colateral pretendido: o diário para de crescer, e o gatilho de condensação de ~500 linhas deixa de ser recorrente. | planejamento, 2026-08-08 |
| `DA-6` | **O percentual do laudo é calculado, nunca autorado.** O reviewer preenche dimensões discretas; o percentual é derivado por função. Percentual escrito por modelo não compara entre tarefas — converge para um valor de conforto e perde poder de série. **Vermelho em dimensão bloqueante reprova independentemente do percentual**, para que "92% aprovado" nunca conviva com conformance vermelho. | planejamento, 2026-08-08 |
| `DA-7` | **A camada mecânica é autoridade sobre o que ela mede.** Onde o script (guardrails, conformance, piso, escopo, dead code) deu vermelho, o reviewer **não pode** marcar `conforme`; ele julga apenas as dimensões que exigem juízo. Contramedida explícita à leniência de reviewer-modelo. | planejamento, 2026-08-08 |
| `DA-8` | **Gestão de modelo é meio-automatizável, e o plano declara qual metade.** Modelo de **subagente**: automatizável — o parâmetro `model` da chamada sobrepõe o `model:` do arquivo do agente, e a escolha passa a ser **registrada no plano**, não decidida no ato. Modelo do **contexto principal**: não automatizável — o loop do scrum-master **para e pede `/model`** ao dono em vez de rodar caro, usando a skill `modelo-por-fase` como gatilho. Sem isso, planejar em Opus e dizer "execute" faria o loop inteiro rodar em Opus, que é o desperdício que a Regra 1 do CLAUDE.md global existe para impedir. | planejamento, 2026-08-08 |
| `DA-9` | **REVOGADA em 2026-08-08 pelo dono; substituída pela `DA-11`.** Lia a regra "uma tarefa por contexto" como "uma tarefa por contexto **de executor**", abrindo exceção por papel para o orquestrador. O veredito do dono é que não há exceção a abrir — conduzir um plano **é** uma tarefa, de modo que o orquestrador nunca contrariou a premissa; o que estava errado era a **régua** (contar tarefas), não o alcance da regra. | revogada pelo dono, 2026-08-08 |
| `DA-10` | **Nenhum guardrail novo em `GOVERNANCA.md` §7 por este plano.** O que o plano cria é papel, instrumento e formato; guardrail se abre quando há regra sem enforcement, e aqui o enforcement nasce junto (rubrica + camada mecânica + tetos). Se o piloto da `T16` revelar um vão de doutrina, ele vira achado com rota, não guardrail improvisado no meio da execução. | planejamento, 2026-08-08 |
| `DA-11` | **PARCIALMENTE REVOGADA em 2026-08-13 pela `DP-Q` (§21) — não ler a cláusula *Enforcement* sem o §21 à vista.** **Permanecem normativas** as duas condições (coesão e capacidade), a fronteira que impede o gatilho fatal de disparar em tudo e as consequências para quem executa e para quem orquestra. **Caiu o enforcement:** o teto de tool uses por classe deixa de ser *proxy operante* de capacidade — número arbitrário não recusa entrega, não roteia, não encerra tarefa e não encerra janela —, e o que encerra janela são as duas condições que o `GOVERNANCA.md` §4.3 governa; a `T13` deixa de ser instrumento opcional e passa a ser o único critério de capacidade disponível ao agente (§5). A frase abaixo sobre o proxy operante é registro do que foi ratificado à época, não regra vigente. **A Regra 2 governa integridade de contexto, não contagem de tarefas.** Um contexto sustenta **um cenário coerente**, sob duas condições independentes — basta uma cair para o contexto acabar. **Coesão:** tudo que entra pertence ao mesmo cenário e não o contradiz; material de outro cenário, premissa derrubada no meio do trabalho, rota bifurcada, fontes divergentes do mesmo fato ou informação ambígua que muda o já feito **poluem**, e poluição é **fatal e imediata** — para-se ao primeiro sinal, porque o que for decidido depois do sinal já é decisão poluída. **Capacidade:** mesmo coeso, o desempenho cai com a ocupação; o teto de trabalho é **~50% da janela**, com encerramento planejado. A fronteira que impede o gatilho fatal de disparar em tudo: a contradição é fatal quando atinge o **cenário** (premissa, rota, contrato), não quando atinge um **detalhe** que o próprio contexto já sobrescreveu — corrigir o próprio erro não é poluição. Consequências: "uma tarefa por contexto" permanece **inalterada** como forma operacional de quem executa, e o limite do orquestrador deixa de ser exceção e passa a ser **derivado** — a janela dele é o plano, não a tarefa, e encerra na troca de plano/iniciativa (troca de cenário) ou na capacidade, o que vier antes. Enforcement: os ~50% não são auto-observáveis hoje (§2, item 3) e dependem do proxy da `T13`; até ele existir, o proxy operante continua sendo o teto de tool uses por classe (§3). | dono, 2026-08-08, ratificada com o texto à vista |
| `DA-12` | **Modelo dos dois papéis novos: Orquestração em Sonnet, Revisão em Opus.** A `T6a` precisava preencher a coluna *Modelo* da matriz e o dossiê não fixava valor; o executor derivou Sonnet para os dois e escalou. Decisão do dono: **Sonnet na Orquestração** — despacho, roteamento e arquivamento não são juízo, e o loop já para para pedir `/model` quando a fase exige outro modelo (`DA-8`) — e **Opus na Revisão**, porque as dimensões de maior peso da rubrica (`criterio-de-pronto`, `testes`, `guardas`) são juízo puro, reviewer no mesmo modelo do executado tende a ratificar, e o laudo é o único gate entre a entrega e o `done` sem round-trip humano. A camada mecânica (`DA-6`/`DA-7`) cobre o que é medível, não o que é julgado. Custo contido: um laudo é leitura de dossiê + diff, não implementação. **Consequência para a `T10`:** o `model:` do `.claude/agents/pantonic-reviewer.md` nasce `opus`, sem re-derivação. | dono, 2026-08-08 |

**Trade-off da `DA-5`,** explícito porque tem custo real. Mover o registro canônico do diário para o
RDO significa que **toda ferramenta e todo texto que hoje apontam para as "Notas de execução" do
diário passam a apontar para outro lugar** — `.claude/skills/handover/SKILL.md`,
`.claude/skills/proximo-passo/SKILL.md`, `.claude/skills/diario-de-obras/SKILL.md` e
`.claude/agents/pantonic-executor.md`. *Alternativa rejeitada:* RDO como camada adicional, mantendo
as notas no diário — recusada porque criaria duas fontes que divergem na primeira edição, que é
exatamente o defeito que `GOVERNANCA.md` §4.2 já nomeia ao proibir copiar o número de consumo para
o diário. *Por que o custo é aceitável:* os quatro artefatos já vão ser tocados pela `T15`
(enxugamento), e o diário já está em 937 linhas com condensação atrasada (`TK-10`) — a fronteira
nova resolve a causa, não o sintoma.

## 2. Restrições de plataforma (insumo — a `T1` mede, nada se infere depois)

Quatro fatos do harness governam o desenho. Os três primeiros eram **premissas declaradas**, e a
`T1` as mediu — evidência colada em `docs/audits/SPIKE_HARNESS_EXECUCAO_AUTONOMA.md`:

1. **Aninhamento de subagentes.** Premissa: subagente não invoca subagente. **Derrubada** —
   aninhamento funciona, observado até profundidade 3. A `DA-1` foi reexaminada e mantida por outro
   motivo; nenhuma tarefa posterior pode invocar a impossibilidade técnica como argumento.
2. **Sobreposição de modelo por chamada.** Premissa: o parâmetro `model` da invocação de agente
   vence o `model:` do arquivo do agente. **Confirmada** — a `DA-8` é implementável.
3. **Observabilidade do próprio contexto.** Fato: **o modelo não enxerga a própria ocupação de
   contexto** — a indicação de percentual é da interface do dono, não do agente. O critério "acima
   de 50% prepara o handover" **não é implementável como escrito** e precisa de proxy: um hook que
   meça o transcript e injete o aviso, ou um contador de tarefas por janela calibrado pela série de
   `docs/telemetria.tsv`. **Parcial** — o payload de `PreToolUse` expõe `transcript_path`, então o
   proxy por hook é viável (nenhum bloco de uso de tokens vem pronto: exige parsear o `.jsonl`); a
   variante do contador não foi medida e é o `TK-23`.
4. **Custo do loop.** O único item que cresce monotonicamente no contexto do orquestrador é **o que
   os subagentes devolvem a ele**. Tudo o mais (dossiês, laudos, evidências) pode viver em arquivo e
   ser lido por contextos descartáveis. É a variável que a `T2` decide e que determina quantas
   tarefas cabem numa janela.

Estado atual medido do repositório, como linha de base do piloto (`T16`):
`docs/telemetria.tsv` é a série existente; `docs/DIARIO_DE_OBRAS.md` está em 937 linhas; o hub tem
suíte `pytest` (`pytest.ini`, `tests/`) e quatro guardas executáveis em `.claude/checks/`
(`kit_check.ps1`, `check-readme.ps1`, `dead_code.py`, `ratchet_piso.py`).

## 3. Invariante de execução (vale para todas as tarefas)

1. **Nenhuma tarefa deste plano executa o loop que ele projeta.** O plano se executa pelo fluxo
   vigente (`proximo-passo`, uma tarefa por contexto) até a `T16`, que é o piloto. Usar a
   ferramenta enquanto ela é construída confunde defeito de desenho com defeito de execução.
2. **Instrumento nasce com teste.** Todo script Python deste plano entra com teste em `tests/`, e o
   piso de regressão da suíte nunca desce. Documental gerado por função sem teste é documental que
   deriva em silêncio.
3. **Formato mora no código, prosa mora no doc.** Uma vez que um CLI produza um artefato, a
   especificação do formato **sai** dos prompts de skill/agente e fica no código — a `T15` mede e
   executa essa remoção. Manter as duas é a duplicata que `GOVERNANCA.md` §3.1 manda apagar.
4. **Redação.** `.claude/skills/redacao-doc/SKILL.md` é normativa em tudo que este plano manda
   escrever em documento publicado. O plano é registro e é isento; o que ele produz não é.
5. **Regime de teto deste plano — fixado pela `DP-Q` (§21), enunciado do dono de 2026-08-13; deixa
   de ser interino.** O teto declarado no cabeçalho de cada tarefa é **alarme, nunca bloqueio**:
   nenhuma tarefa para, é impedida, é recusada ou fica incompleta por ter cruzado o número, e nenhum
   ramo de roteamento se abre por causa dele. Quem delega **não escreve cláusula de parada dura por
   teto** no dossiê de delegação, e quem executa registra o consumo e seus sinais no fechamento em vez
   de interromper a entrega. O número continua sendo medido e apendado a `docs/telemetria.tsv` sem
   exceção — **medir permanece; decidir por medida sai**, e é o agregado da série que tem valor. O
   registro qualitativo por tarefa, quando houver, mora no card "Lições aprendidas na tarefa" do
   laudo. O que encerra janela são as duas condições não arbitrárias do `GOVERNANCA.md` §4.3 —
   **coesão** e **capacidade** —, sendo a `T13` o instrumento de capacidade; entre a `T49` e a
   `T13`, o encerramento se apoia só em coesão e no fim do plano. **A `DP-L` não se forma neste
   plano:** a `T34` foi cancelada por absorção em 2026-08-12 e a matéria de limites se revê
   **inteira, em plano próprio**, aberto depois que este fechar (desdobramento na `T17`, item 4);
   **nenhum número novo entra no lugar dos que caem**.
6. **Verificação de fechamento de toda tarefa** — os quatro em exit 0:
   `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate`,
   `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift`,
   `pwsh -NoProfile -File .claude/checks/check-readme.ps1`,
   `python -m pytest` na raiz do hub.

## 4. Tarefas

### T1 — Spike: o que o harness permite [Sonnet · classe investigação · teto 20]
- **Objetivo:** medir as três premissas do §2 antes de qualquer linha de implementação, para que
  `DA-1`, `DA-8` e o desenho dos hooks se apoiem em fato, não em suposição.
- **Arquivos-alvo:** cria `docs/audits/SPIKE_HARNESS_EXECUCAO_AUTONOMA.md`. Nenhum outro arquivo é
  tocado.
- **Método de sondagem (prescrito — não improvisar):**
  1. **Aninhamento:** invocar um subagente barato cuja instrução seja tentar invocar outro
     subagente; registrar o resultado literal (erro, ferramenta ausente, ou sucesso).
  2. **Sobreposição de modelo:** invocar `pantonic-scout` (arquivo fixa modelo barato) passando
     `model` diferente na chamada; registrar qual modelo a notificação de conclusão reporta.
  3. **Observabilidade de contexto:** inventariar os eventos de hook disponíveis e quais campos
     cada um recebe (em especial se algum expõe caminho de transcript e/ou bloco de uso), a partir
     da documentação da ferramenta e de um hook de sonda que apenas registra o payload recebido.
  4. **Ciclo de vida de arquivo entre agentes:** confirmar que um arquivo escrito por um subagente é
     legível por outro subagente da mesma sessão (premissa do transporte por arquivo, `T2`).
- **Forma do entregável — para cada uma das quatro sondas, quatro campos:** premissa, o que foi
  feito (comando/chamada), o que foi observado (saída colada, não parafraseada), veredito
  (`confirmada` / `derrubada` / `parcial`, com o que fica indefinido).
- **Proibido:** propor desenho, escolher rota ou alterar qualquer artefato do kit. O entregável é
  medição.
- **Verificação:** bateria do §3; o documento tem as quatro sondas com veredito explícito.
- **Pronto quando:** cada premissa do §2 tem veredito com evidência colada, e as tarefas `T2`,
  `T3`, `T12` e `T13` conseguem decidir sem repetir nenhuma sonda.

### T2 — Decisão: transporte do pacote de retorno [Opus · classe redação/planejamento · teto 30]
- **Objetivo:** fechar a decisão postergada `DP-A` — como o executor entrega o resultado ao
  scrum-master — e **fechar o dossiê das tarefas que dependem dela** (`T8`, `T10`, `T11`).
- **Insumo:** `T1` sonda 4; série de `docs/telemetria.tsv`; tamanho real dos handovers já escritos
  no diário (amostra medida, não estimada).
- **Opções a confrontar, com custo medido para cada uma:** (a) **por arquivo** — executor escreve
  o pacote em caminho combinado e devolve confirmação de uma linha; reviewer lê o arquivo; o
  orquestrador ingere só o veredito; (b) **por contexto** — pacote de campos fixos devolvido na
  resposta e repassado ao reviewer; (c) **híbrido por tamanho**.
- **Critério de decisão declarado:** quantas tarefas cabem numa janela sob cada opção, calculado a
  partir do tamanho medido dos handovers da série — não por preferência estética.
- **Entregável, três partes:** (1) decision record `DP-A` com opção escolhida, número que a
  sustenta e alternativas rejeitadas com motivo; (2) **especificação de campos fixos do pacote de
  retorno**, com teto de linhas; (3) **dossiês fechados** das tarefas dependentes, apensados a este
  plano na seção `## Dossiês fechados por decisão` (o corpo do plano permanece imutável).
- **Ratificação:** a escolha é de arquitetura de processo — vai ao dono antes de ser gravada
  (`AskUserQuestion`, um round-trip), conforme `G-PLANREADY` item 5.
- **Verificação:** bateria do §3; `T8`, `T10` e `T11` passam no gate de delegação da
  `proximo-passo` sem nenhuma cláusula "investigue" ou ramo não resolvido.
- **Pronto quando:** a decisão está gravada com o número que a justifica, e nenhuma tarefa
  dependente ainda precisa decidir algo para começar.

### T3 — Decisão: política de autonomia, tetos e escalada [Opus · classe redação/planejamento · teto 30]
- **Objetivo:** fechar `DP-B` — quando o loop segue sozinho, quando para e devolve ao dono — e
  fechar o dossiê da `T10`.
- **Questões a resolver, todas com número, nenhuma com adjetivo:** teto de **retentativas** por
  tarefa reprovada; teto de **tarefas por janela**; teto de **consumo acumulado** por janela;
  classificação do que **obriga parada** (decisão de arquitetura ou requisito, executor `blocked`,
  reprovação após a última retentativa, achado que invalida a rota do plano) versus o que segue
  **com registro** (ressalva não bloqueante, achado fora de escopo com rota).
- **Régua herdada, não reinventada:** a fronteira "o que é ponto do dono" já está escrita em
  `.claude/skills/proximo-passo/SKILL.md` (decisão de arquitetura/requisitos sim; evento intrínseco
  do plano não) e é insumo, não objeto de redecisão. `DP-B` decide o **comportamento do loop**
  diante de cada classe, não a classificação.
- **Entregável:** decision record `DP-B` + **tabela de roteamento** (estado do laudo → ação do
  scrum-master), pronta para ser transcrita pela `T10` sem interpretação + dossiê fechado da `T10`.
- **Ratificação:** apetite de risco é do dono — vai a ele com a recomendação e o custo de cada
  opção (`AskUserQuestion`, um round-trip).
- **Verificação:** bateria do §3; a tabela de roteamento é total (todo estado possível do laudo tem
  exatamente uma ação) e não contém ramo que exija juízo do orquestrador.
- **Pronto quando:** existe tabela determinística de roteamento com tetos numéricos, e nenhum
  caminho leva a "o orquestrador avalia".

### T4 — Decisão: formato estruturado da tarefa no plano [Opus · classe redação/planejamento · teto 30]
- **Objetivo:** fechar `DP-C` — que forma a tarefa assume dentro de `docs/plans/P-*.md` para ser
  consumível por script sem deixar de ser legível pelo dono — e fechar o dossiê da `T8`.
- **Insumo medido:** varredura dos planos vivos e recentes (`P-0731`, `P-0732`, `P-0733`, este) para
  levantar quais campos já existem de fato em todas as tarefas (objetivo, arquivos-alvo,
  verificação, pronto quando, modelo, classe/teto) e quais variam de redação entre planos.
- **Opções a confrontar:** (a) bloco estruturado por tarefa dentro do próprio `.md`; (b) convenção
  de linhas rotuladas extraída por expressão regular; (c) arquivo de dados irmão do plano.
- **Critério de decisão declarado:** resistência à deriva (o que acontece quando alguém edita só um
  dos lados) e custo de migração dos planos existentes — o formato escolhido **não pode** invalidar
  plano fechado, pela mesma régua que preservou os nomes de plano em `DP-G5`.
- **Entregável:** decision record `DP-C` + **esquema de campos** (nomes, obrigatoriedade, valores
  aceitos para `classe` e `modelo`) + política para planos legados + dossiê fechado da `T8` +
  instrução de autoria a ser incorporada ao `pantonic-planner` (a incorporação em si é da `T15`).
- **Verificação:** bateria do §3; o esquema aplicado a mão a três tarefas deste plano produz os
  mesmos campos sem ambiguidade.
- **Pronto quando:** existe um esquema que um script consegue ler e que um humano continua lendo,
  com a política de plano legado escrita.

### T5 — Rubrica do laudo [Opus · classe redação de doutrina · teto 30]
- **Objetivo:** definir **o que** se avalia numa tarefa executada, antes de existir qualquer
  ferramenta que avalie — ferramenta que verifica régua não escrita mede ruído.
- **Arquivos-alvo:** cria `docs/RUBRICA_DE_REVISAO.md` (documento publicado, sujeito à
  `redacao-doc`).
- **Conteúdo — para cada dimensão, cinco campos:** nome, pergunta que ela responde, **fonte da
  evidência** (mecânica ou de juízo), se é **bloqueante**, e o que caracteriza cada nível
  (`conforme` / `parcial` / `não conforme` / `não se aplica`).
- **Dimensões de partida, a serem confirmadas ou corrigidas na tarefa:** critério de pronto
  atendido; fidelidade de escopo (arquivos tocados ⊆ arquivos-alvo declarados); testes exigidos
  presentes e verdes; conformance e piso de regressão; fidelidade à rota do plano (`G-PLANFIDELITY`);
  ausência de código morto e de resíduo (`G-DEADCODE`); higiene de registro (achado fora de escopo
  com rota, telemetria com ponteiro).
- **Cálculo:** peso por dimensão e fórmula do percentual, **determinística**, com a regra de
  dominância de `DA-6` (bloqueante vermelha ⇒ reprovado, qualquer que seja o percentual). A
  fórmula é escrita aqui e **implementada** na `T8` — não redecidida lá.
- **Classe de achado que não é defeito de código:** a rubrica declara uma via para o achado que
  denuncia **defeito do plano** (tarefa mal decomposta, critério de pronto não verificável,
  pressão sobre a arquitetura). Sem essa via, o loop corrige o sintoma e reincide na causa.
- **Verificação:** bateria do §3; a rubrica aplicada a mão a duas tarefas já fechadas do `P-0732`
  produz veredito coerente com o que o diário registra sobre elas.
- **Pronto quando:** cada dimensão tem fonte de evidência declarada, o percentual é calculável sem
  juízo, e existe rota para achado de processo.

### T6a — Doutrina: papéis e fronteira de registro [Opus · classe redação de doutrina · teto 30]
- **Objetivo:** `DA-5` — a doutrina passa a admitir o loop antes de o loop existir: quem despacha,
  quem julga e onde o registro da tarefa mora.
- **Arquivos-alvo:** `GOVERNANCA.md` §3 (matriz de responsabilidades) e §4.2 (diário de obras);
  `docs/RESIDENCIA_DOUTRINA.md` se a fronteira nova exigir entrada.
- **Conteúdo:**
  - **§3, matriz:** duas linhas novas — **Orquestração** (o scrum-master: despacha, roteia,
    arquiva; **não** implementa, **não** julga entrega, **não** decide arquitetura) e **Revisão**
    (o reviewer: julga entrega contra dossiê e emite laudo; **não** corrige o que aponta, **não**
    replaneja). Coluna *Modelo* preenchida para as duas. A matriz é o lugar canônico dos papéis;
    nenhuma skill ou agente repete a fronteira, todos apontam.
  - **§4.2:** a fronteira de `DA-5` — diário como kanban, RDO como registro canônico da tarefa,
    `telemetria.tsv` como fonte única do número. O texto que hoje manda escrever "Notas de
    execução" no diário passa a apontar para o RDO.
- **Cuidado:** nenhum item novo em §7 (`DA-10`); nenhuma menção a repositório derivado (`DA-3`).
  A integridade de contexto é escopo da `T6b` — não antecipar nada dela aqui.
- **Verificação:** bateria do §3; `Grep` por "Notas de execução" em `GOVERNANCA.md` → só ocorrências
  que apontam para o RDO.
- **Pronto quando:** um agente que leia só a `GOVERNANCA.md` entende quem despacha, quem julga e
  onde o registro da tarefa mora.

### T6b — Doutrina: integridade do contexto [Opus · classe redação de doutrina · teto 30]

> **DOSSIÊ PARCIALMENTE REVOGADO em 2026-08-13 pela `DP-Q` (§21) — não ler o bullet *Enforcement*
> sem o §21 à vista.** **Permanece** tudo que a tarefa transcreveu: as duas condições, a resposta ao
> caso fatal e os arquivos-alvo, já entregues. **Caiu a cláusula de enforcement:** o teto de tool
> uses por classe não é *proxy operante* de capacidade, porque número arbitrário não encerra janela;
> o `GOVERNANCA.md` §4.3 foi reescrito por isso e o gatilho de checkpoint deixou de ser numérico. O
> corpo abaixo fica intocado, como registro do que foi decidido à época.

- **Dossiê fechado por:** `DA-11`, ratificada pelo dono com o texto normativo à vista. O executor
  **transcreve** o conteúdo abaixo nas superfícies medidas; não redecide nem reformula a regra.
- **Objetivo:** substituir a régua da Regra 2 — de contagem de tarefas para integridade de contexto
  —, dando ao caso **fatal** (poluição) a resposta que hoje não existe: a doutrina só tem a resposta
  planejada (checkpoint em 2/3 do teto, §4.3), nada para a contradição que atinge o cenário.
- **Arquivos-alvo (medidos nesta rodada — nenhum outro):**
  - `~/.claude/CLAUDE.md`, Regra 2 — **texto íntegro**; é o lar canônico
    (`docs/RESIDENCIA_DOUTRINA.md` classifica o item 2.1 como `global`/P1). Fora do repositório.
  - `GOVERNANCA.md` §4.3 — forma **condensada** (padrão `DR-A`, sem segunda cópia plena): as duas
    condições e a resposta fatal.
  - `GOVERNANCA.md` §7, item 7 ("Disciplina de contexto") — **reescrita do item existente**, não
    item novo: `DA-10` permanece intacta.
  - `docs/RESIDENCIA_DOUTRINA.md`, seção "Regra 2" — o item 2.1 e a nota de colisão, que aponta
    "§7 item 8" quando o item 8 hoje é `G-DEADCODE` (drift de numeração; cai junto).
  - `README.md` — **duas** ocorrências, e só elas: o verbete **Contexto** do glossário (a definição
    ganha as duas condições) e a linha **7** da tabela de guardrails do §10 (acompanha a reescrita
    do item). O título do §9 ("Handover e uma tarefa por contexto") e os demais usos de "contexto
    limpo" permanecem válidos e **não** são tocados — a forma operacional do executor não muda.
- **Conteúdo normativo (ratificado):**
  - Um contexto sustenta **um cenário coerente**. Segue enquanto tudo que entra pertence a esse
    cenário; entrando material de outro cenário, ou material que contradiz o que já está lá, o
    contexto está **poluído** — e contexto poluído não se recupera, se substitui.
  - **Duas condições independentes; basta uma cair para o contexto acabar.** *Coesão:* violação
    **fatal e imediata** — parar ao primeiro sinal, nunca "termino o que está aberto e limpo
    depois", porque o que for decidido depois do sinal já é decisão poluída. *Capacidade:* mesmo
    coeso, o desempenho cai com a ocupação; teto de trabalho **~50% da janela**, violação gradual,
    encerramento planejado.
  - **Sinais de poluição** (checagem obrigatória, lista não exaustiva): material de outra tarefa,
    outro plano ou outra iniciativa entrou no contexto; premissa que sustentava o trabalho foi
    derrubada no meio dele; a rota bifurcou ou uma decisão do dono contradiz o que já foi ingerido;
    duas fontes do mesmo fato divergem sem descarte imediato; entrou informação ambígua ou
    controversa que muda o que já foi feito.
  - **O que não é poluição:** corrigir o próprio erro, sobrescrever valor errado, refinar detalhe.
    A contradição é fatal quando atinge o **cenário** (premissa, rota, contrato), não quando atinge
    um **detalhe** que o próprio contexto já substituiu.
  - **Consequências práticas:** para quem executa, **uma tarefa por contexto**, inalterado; para
    quem orquestra, conduzir um plano **é** uma tarefa — o contexto atravessa várias tarefas
    atômicas sem violar nada, porque o cenário é o mesmo, e encerra na **troca de plano ou
    iniciativa** (troca de cenário) ou na capacidade, o que vier antes.
  - **Como aplicar:** sinal de poluição ou capacidade cruzada → checkpoint de até 5 linhas de
    ponteiro de estado (teto 2 tool uses) → handover → contexto novo. Nada se inicia depois do
    sinal.
- **Enforcement, escrito sem promessa vazia:** o teto de ~50% não é auto-observável hoje; enquanto
  o proxy de ocupação não existir, o proxy operante é o **teto de tool uses por classe** (§3). O
  item 7 do §7 permanece na classe "instrução de agente" e ganha o check quando o proxy existir.
- **Redação:** `GOVERNANCA.md` e `README.md` são classe **publicado** (`redacao-doc`) — o texto novo
  nasce **sem ID de processo**: nada de `DA-11`, `T13`, `P-0734` ou data de decisão no corpo. O
  ponteiro para o proxy futuro é afirmado inline ("enquanto não houver proxy de ocupação..."),
  nunca por ID de tarefa. A `~/.claude/CLAUDE.md` não é doc publicado e segue a forma das outras
  regras (motivo + como aplicar).
- **Cuidado:** nenhum item novo em §7 (`DA-10`) — o item 7 é reescrito, não somado; nenhuma menção
  a repositório derivado (`DA-3`); não tocar as skills `handover`, `proximo-passo` e
  `bootstrap-pantonic`, que só apontam para a regra.
- **Verificação:** bateria do §3, com `check-readme.ps1` em exit 0 (as duas linhas do espelho);
  `Grep` por "uma tarefa por contexto" em `GOVERNANCA.md` e `README.md` → nenhuma ocorrência
  remanescente que afirme a regra como contagem sem a condição de coesão.
- **Pronto quando:** um agente que leia só a Regra 2 sabe **quando parar na hora** e **quando
  encerrar de forma planejada**, e sabe por que o orquestrador atravessa várias tarefas sem abrir
  exceção.

### T7 — `telemetria.py`: a série deixa de ser editada à mão [Sonnet · classe implementação padrão · teto 40]
- **Objetivo:** provar o padrão "documental por função" no menor pedaço possível, e eliminar a
  edição manual de `docs/telemetria.tsv` — que hoje custa Grep + Read + Edit e admite coluna
  trocada em silêncio.
- **Arquivos-alvo:** cria `.claude/tools/telemetria.py` e `tests/test_telemetria.py`. Toca
  `.claude/checks/kit_check.ps1` **apenas** se o modo `validate` inventariar diretórios do kit e
  precisar conhecer `.claude/tools/`.
- **Interface:** subcomando `append` com um argumento por coluna existente (`data`, `projeto`,
  `tarefa`, `modelo`, `tool_uses`, `tokens_k`, `duracao_s`, `fonte`), `fonte` restrita ao conjunto
  já normativo (`usage` / `contado` / `nao_medido`). Validação de tipo e de domínio; escrita
  atômica em modo append; falha ruidosa e exit não-zero em coluna inválida.
- **Cuidado:** a série existente é insumo histórico — nenhuma linha é reescrita, reordenada ou
  normalizada. O script só apende.
- **Verificação:** bateria do §3; teste cobrindo linha válida, `fonte` inválida, campo numérico não
  numérico e preservação byte a byte do conteúdo anterior.
- **Pronto quando:** registrar consumo é uma chamada, o formato não está mais em prosa em lugar
  nenhum, e a série antiga continua íntegra.

### T8 — `rdo.py`: o registro da tarefa se gera — **partida em `T8a`/`T8b`/`T8c` por orçamento**
- **Dossiê fechado por:** `T2` (campos do pacote de retorno), `T4` (esquema da tarefa no plano),
  `T5` (rubrica e fórmula) — as três `done`.
- **Motivo da partição:** a fatia mais simples desta mesma classe (`T7`, `telemetria.py`, **um**
  subcomando, um arquivo de teste) consumiu **35 tool uses contra o teto 40**. Esta tarefa tem três
  subcomandos, o template, o índice gerado e teste por subcomando — a soma passa do teto por
  construção, e o teto é alarme: o controle é dividir antes de delegar. As três fatias são
  sequenciais (`T8a` → `T8b` → `T8c`), cada uma com verificação própria e teto próprio da classe.

### T8a — `rdo.py new`: o documento e o template [Sonnet · classe implementação padrão · teto 40]
- **Objetivo:** o RDO de uma tarefa nasce de uma chamada de função, não de redação — o agente
  precisa saber a assinatura, nunca o formato.
- **Arquivos-alvo:** cria `.claude/tools/rdo.py`, o template do documento e `tests/test_rdo.py`;
  cria o diretório `docs/RDO/`.
- **Interface:** subcomando `new` — abre o RDO a partir do identificador de plano/tarefa, puxando o
  dossiê do plano pelo esquema da `DP-C` (leitura tolerante de plano legado) e materializando o
  documento a partir do template com os campos fixos do pacote de retorno da `DP-A`.
- **Invariantes:** campos fixos do documento vivem no **template**, não no prompt de nenhum agente;
  escrita atômica e falha ruidosa com exit não-zero, no mesmo padrão de `.claude/tools/telemetria.py`.
- **Cuidado:** `laudo` e `close` são as fatias `T8b`/`T8c` — não implementar aqui; o índice de
  `docs/RDO/` é da `T8c`; `kit_check.ps1 -Mode validate` só inventaria `agents/`/`skills/`
  (confirmado na `T7`) — não tocar.
- **Verificação:** bateria do §3, com a suíte partindo de **6 testes passando** (piso: 6 + os novos);
  teste do `new` sobre tarefa real do plano e de identificador inexistente (exit != 0, nada escrito).
- **Pronto quando:** `new` produz o documento aberto com todos os campos do pacote, e o formato do
  RDO não está escrito em nenhum prompt.

### T8b — `rdo.py laudo`: o veredito é calculado [Sonnet · classe implementação padrão · teto 40]
- **Dossiê fechado por:** `T5` (rubrica, pesos, faixas) e `T3` (domínio do veredito). **Não
  delegável antes da `T8a`.**
- **Objetivo:** o laudo é calculado, nunca redigido — percentual e veredito saem da fórmula, não do
  juízo de quem preenche.
- **Arquivos-alvo:** `.claude/tools/rdo.py`, o template, `tests/test_rdo.py`.
- **Interface:** subcomando `laudo` — recebe as marcações das dimensões da rubrica, observações e
  recomendações; **calcula** percentual e veredito pela fórmula e pelas faixas de
  `docs/RUBRICA_DE_REVISAO.md` e grava a seção no RDO aberto.
- **Invariantes:** percentual e veredito **não** são aceitos como argumento (`DA-6`) — passá-los é
  erro; dimensão marcada `conforme` contra vermelho mecânico é rejeitada com erro (`DA-7`);
  `não conforme` em dimensão bloqueante domina o percentual; o domínio do veredito não é ampliado.
- **Cuidado:** pesos, faixas e conjunto de dimensões são **copiados** da rubrica, nunca
  reinterpretados; não implementar `close`.
- **Verificação:** bateria do §3; testes para o cálculo, para a dominância de bloqueante sobre
  percentual alto, para a recusa de percentual/veredito por argumento e para a recusa de `conforme`
  contra vermelho mecânico.
- **Pronto quando:** nenhuma chamada consegue produzir `aprovado` com bloqueante preenchida, e o
  percentual nunca vem de fora.

### T8c — `rdo.py close` e o índice gerado [Sonnet · classe implementação padrão · teto 40]
- **Não delegável antes da `T8b`.**
- **Objetivo:** fechar o registro e manter o índice de `docs/RDO/` como artefato gerado.
- **Arquivos-alvo:** `.claude/tools/rdo.py`, `tests/test_rdo.py`, `docs/RDO/` (índice).
- **Interface:** subcomando `close` — registra o desdobramento (roteamento da `DP-B`), fecha o
  documento e regenera o índice de `docs/RDO/`.
- **Invariantes:** o índice é **gerado** por varredura do diretório, nunca redigido nem apendado às
  cegas; `close` sobre RDO inexistente ou já fechado falha ruidosamente; escrita atômica.
- **Verificação:** bateria do §3; testes para o `close`, para a regeneração do índice a partir de
  mais de um RDO e para a recusa de fechar RDO inexistente.
- **Pronto quando:** um RDO completo é produzido por três chamadas, sem que nenhum agente conheça o
  formato do documento, e o índice reflete o diretório sem edição manual.

### T9 — `review_evidence.py`: a camada mecânica da revisão

**Partida em `T9a`/`T9b` por orçamento (2026-08-08, no despacho).** A tarefa reunia duas metades
tecnicamente distintas — coleta por `git` e invocação de seis subprocessos de guarda — mais um
padrão de teste sem precedente na suíte (repositório `git` de fixture), contra um teto de 40; a
série da `T8` (48/26/38 contra 40) media o mesmo formato de tarefa acima do teto. O objetivo, a
invariante e o critério de pronto originais permanecem, distribuídos entre as duas fatias.

**Objetivo (das duas):** o reviewer recebe evidência compacta pronta em vez de varrer o
repositório — é o que impede a revisão de custar mais que a execução.

**Invariante (das duas):** a saída é **fato com veredito mecânico**, sem interpretação — quem
interpreta é o reviewer. Onde a evidência dá vermelho, a marcação da dimensão correspondente já
vem travada (`DA-7`).

### T9a — `review_evidence.py`: diff, escopo e a forma do dossiê [Sonnet · classe implementação padrão · teto 40]
- **Objetivo:** a metade `git` da evidência — o reviewer recebe *o que mudou* e *se saiu do
  escopo* já apurado.
- **Arquivos-alvo:** cria `.claude/tools/review_evidence.py` e `tests/test_review_evidence.py`.
  Nenhum outro arquivo é tocado — em particular, **não** editar `.claude/tools/rdo.py`
  (`.claude/README.md` não indexa `.claude/tools/`, então nada é regenerado).
- **Conteúdo:** CLI `argparse` no padrão dos irmãos; arquivos-alvo declarados extraídos do dossiê
  da tarefa no plano por **reuso** de `extrair_dossie` (`.claude/tools/rdo.py:186`); estatística do
  diff e lista de arquivos tocados; confronto de escopo produzindo o veredito mecânico da dimensão
  `escopo` (`docs/RUBRICA_DE_REVISAO.md:63-77`); trechos de diff dos arquivos-alvo com teto de
  tamanho declarado e truncamento visível. A seção da bateria de guardas nasce **nomeada e vazia**,
  para a `T9b` preencher sem reescrever o renderizador.
- **Verificação:** bateria do §3; testes com repositório de fixture `git` cobrindo escopo
  respeitado, escopo violado e truncamento pelo teto.
- **Pronto quando:** um único comando produz o documento com diff, arquivos tocados, veredito de
  escopo e trechos truncados, e a seção de guardas existe vazia e nomeada.

### T9b — `review_evidence.py`: a bateria de guardas [Sonnet · classe implementação padrão · teto 40]
- **Não delegável antes da `T9a`.**
- **Objetivo:** preencher a seção que a `T9a` deixou nomeada, com o exit code colado de cada
  guarda da bateria de `GOVERNANCA.md` §3.
- **Arquivos-alvo:** `.claude/tools/review_evidence.py`, `tests/test_review_evidence.py` (ambos já
  existentes).
- **Conteúdo:** invocação dos seis comandos da bateria com captura de exit code e saída; veredito
  mecânico travado das dimensões `guardas` (`docs/RUBRICA_DE_REVISAO.md:94-106`, autoridade
  integral, sem faixa de juízo) e `testes` (`:79-92`), conforme `DA-7`.
- **Verificação:** bateria do §3; teste de guarda vermelha (comando em exit não-zero ⇒ dimensão
  travada), mais regressão do que a `T9a` entregou.
- **Pronto quando:** o reviewer consegue julgar a partir de um único artefato compacto, sem abrir o
  repositório para descobrir o que mudou.

### T10 — Agente `pantonic-reviewer` [Opus · classe redação de doutrina · teto 30]
- **Objetivo:** `DA-2` — criar o papel que julga a entrega contra o dossiê.
- **Arquivos-alvo:** cria `.claude/agents/pantonic-reviewer.md`; regenera `.claude/README.md` se o
  inventário de agentes mudar.
- **Conteúdo:** papel (o que faz e o que **não** faz, apontando para a matriz da `T6a` sem repetir);
  fatos estáveis que ele precisa a frio; protocolo — ler dossiê, ler pacote de retorno, ler dossiê
  de evidência (`T9`), marcar as dimensões da rubrica (`T5`), emitir o laudo via `rdo.py laudo`
  (`T8`); proibições — não editar código, não corrigir o que aponta, não replanejar, não marcar
  `conforme` contra vermelho mecânico.
- **Lista de ferramentas:** somente leitura sobre o repositório, mais o necessário para gravar o
  laudo. A independência é imposta pela lista, não pedida ao texto.
- **Modelo:** declarado no arquivo conforme a matriz da `T6a`.
- **Verificação:** bateria do §3 (`kit_check.ps1 -Mode validate` cobre a contagem de agentes).
- **Pronto quando:** o arquivo descreve um papel que não consegue, por construção, consertar o que
  aponta.

### T11 — Skill `scrum-master`: o loop [Opus · classe redação de doutrina · teto 30]
- **Dossiê fechado por:** `T2` (transporte) e `T3` (tabela de roteamento e tetos). **Não delegável
  antes das duas.**
- **Objetivo:** materializar o papel de orquestração como procedimento reexecutável (`DA-1`).
- **Arquivos-alvo:** cria `.claude/skills/scrum-master/SKILL.md`; regenera `.claude/README.md`.
- **Fluxo a escrever, na ordem:** gate de modelo do contexto principal (`modelo-por-fase`, `DA-8`)
  → seleção da próxima tarefa do plano, sempre sequencial, nunca em paralelo → gates herdados
  (`G-PLANREADY` e gate de delegação, **apontados**, nunca recopiados — a `T12` garante que existam
  num lugar só) → despacho do executor com o modelo declarado no plano → recepção do pacote de
  retorno pelo transporte da `T2` → despacho do reviewer → leitura do veredito → roteamento pela
  tabela da `T3` → arquivamento via `rdo.py close` → decisão de continuar ou encerrar a janela.
- **Encerramento de janela:** pelo proxy que a `T13` implementar, ou pelos tetos numéricos da `T3`
  enquanto não houver proxy — nunca por percepção de contexto, que o modelo não tem (§2, item 3).
- **Proibições:** o scrum-master não implementa, não julga entrega e não decide arquitetura; ponto
  de decisão do dono **para o loop** e o devolve.
- **Verificação:** bateria do §3; percurso a seco do fluxo sobre uma tarefa já fechada do `P-0733`,
  registrado na própria tarefa, sem executar nada.
- **Pronto quando:** todo passo do fluxo tem gatilho, entrada e saída declarados, e nenhum passo
  depende de juízo não roteado.

### T12 — Reconciliação com `proximo-passo` [Opus · classe redação de doutrina · teto 30]
- **Objetivo:** impedir que os gates existam em dois lugares — duplicata é a próxima divergência
  (`GOVERNANCA.md` §3.1).
- **Arquivos-alvo:** `.claude/skills/proximo-passo/SKILL.md`; `.claude/skills/scrum-master/SKILL.md`;
  `.claude/skills/handover/SKILL.md` no que a fronteira da `T6a` tiver deslocado.
- **Conteúdo:** decidir e aplicar, com motivo escrito, uma de duas formas — (a) `proximo-passo`
  permanece como modo de **tarefa única** e o `scrum-master` como modo de **loop**, com os gates
  extraídos para um único lugar referenciado pelos dois; ou (b) `proximo-passo` é absorvida e vira
  ponteiro. Em qualquer das duas, **o texto dos gates existe uma vez só**, e a cópia perdedora é
  apagada no mesmo ato.
- **Cuidado:** a heurística de priorização, a diretiva do diário e a drenagem dos inboxes continuam
  existindo — a reconciliação decide **onde** moram, não se sobrevivem.
- **Verificação:** bateria do §3; `Grep` pelo texto dos gates no kit → uma ocorrência normativa,
  demais são ponteiro.
- **Pronto quando:** existe exatamente um lugar que define `G-PLANREADY` e o gate de delegação, e os
  dois modos de entrada apontam para ele.

### T13 — Proxy de ocupação de contexto [Sonnet · classe implementação padrão · teto 40]
- **Dossiê fechado por:** `T1` sonda 3.
- **Objetivo:** dar ao scrum-master um sinal de "a janela está acabando" que ele consiga enxergar —
  já que a ocupação real não lhe é observável (§2, item 3).
- **Arquivos-alvo:** conforme o veredito da `T1` — hook em `settings.json` mais script de medição em
  `.claude/tools/`, ou, se o evento necessário não existir, o contador calibrado dentro da skill
  `scrum-master`, mais teste; e as duas superfícies que o campo *Conteúdo* obriga quando o proxy
  existe — `.claude/skills/scrum-master/SKILL.md` (o comportamento ao receber o aviso) e
  `GOVERNANCA.md` §4.3 (o bullet *Capacidade*, que passa a nomear o instrumento).
  *Nota de conciliação, 2026-08-15:* as duas últimas superfícies entraram por conciliação de dossiê
  já executado (`DP-H` §13 — dossiê de tarefa executada é **orientação** e se concilia), a partir do
  item de replanejamento do laudo da própria `T13`: o campo não as nomeava, a entrega as tocou por
  consequência obrigatória (`G-SURFACE`) e o escopo foi julgado contra o campo *Conteúdo*, sem punir
  a execução pelo campo incompleto. Concilia-se a orientação; o que narra o ocorrido — bullet de
  fechamento, RDO, telemetria e histórico — permanece intocado.
- **Conteúdo:** limiar declarado em número; aviso injetado no contexto do orquestrador quando
  cruzado; comportamento do scrum-master ao recebê-lo (encerrar a tarefa corrente, arquivar,
  preparar o handover de janela e parar).
- **Resultado negativo é resultado:** se a `T1` derrubar a viabilidade do hook, a tarefa entrega o
  contador calibrado pela série de `docs/telemetria.tsv` **e** registra a inviabilidade com a
  evidência — não fica em aberto nem finge que o proxy existe.
- **Verificação:** bateria do §3; teste do cálculo do limiar.
- **Pronto quando:** o loop tem um critério de encerramento de janela que ele próprio consegue
  avaliar, seja qual for o mecanismo.

### T14 — Telemetria sem turno de agente [Sonnet · classe implementação padrão · teto 40]
- **Dossiê fechado por:** `T1` sonda 3 e **`DP-R` (§22)**, **conciliado em 2026-08-15**: com a `T53`
  cancelada por absorção, a dependência passa para a **`RPC-T2` do `P-0735`**. **Depende da `T7` e da
  `RPC-T2`** — a residência versionada do hook precisa existir antes desta tarefa declarar hook
  nenhum, sob pena de repetir o `TK-43`. A residência canônica onde a declaração entra é
  `.claude/projecoes.json` (chave `chaves.hooks` do alvo `projeto`), e o materializador é
  `python .claude/tools/materializar.py apply`; onde o texto abaixo diz `.claude/hooks/hooks.json` e
  `hooks_sync.py`, leia esses dois.
- **Objetivo:** se o harness expuser o consumo do subagente a um hook, a linha da série passa a ser
  escrita **sem gastar turno nenhum** — automatizando por completo a regra de telemetria medida.
- **Arquivos-alvo:** `.claude/hooks/hooks.json` (a **declaração** do hook, com o caminho do comando
  escrito em `{KIT_ROOT}`, como a `T53` fixou), `.claude/tools/telemetria_hook.py` (script que traduz
  o payload em chamada a `telemetria.py append`) e `tests/test_telemetria_hook.py`.
  **`.claude/settings.json` não é alvo de edição:** ele é **produto** de
  `python .claude/tools/hooks_sync.py apply`, executado depois que a declaração entra no canônico.
  Rota anterior invalidada em 2026-08-15: o dossiê nomeava `settings.json` como residência, e esse
  arquivo é ignorado pelo git (`.gitignore:3`) — nada dali viaja para consumidor nenhum.
- **Invariante:** o hook **apenas apende** à série; ele não escreve no diário, não fecha tarefa e
  não emite juízo. Hook sem regra escrita atrás dele é doutrina invisível — a regra já está em
  `GOVERNANCA.md` §4.2 e não é reescrita aqui.
- **Invariante de residência (`DP-R`):** nenhum hook nasce direto no arquivo local de máquina; o que
  o kit distribui é a declaração canônica, e a máquina recebe só a materialização. Falha aberta
  total e filtro por contexto seguem a mesma regra do proxy da `T13`: hook não bloqueia chamada de
  ferramenta em nenhuma circunstância.
- **Resultado negativo é resultado:** inviável ⇒ registrar a evidência e manter o fluxo da `T7`
  (chamada explícita pelo orquestrador), sem deixar pendência aberta — e **nada fica
  meio-registrado**: se o evento não existir ou não trouxer o consumo, `hooks.json` não recebe
  entrada nenhuma e o `settings.json` local permanece igual ao produto do `apply`, o que
  `kit_check -Mode check-drift` prova em exit 0.
- **Verificação:** bateria do §3 item 6; teste do tradutor com payload de fixture.
- **Pronto quando:** ou a série se alimenta sozinha **em qualquer projeto que materialize o kit**,
  ou está escrito por que não pode, com a medida que sustenta a conclusão.
- **Nota de 2026-08-19 — fechada em ramo B, com o vão nomeado.** A execução mediu um **terceiro**
  ramo, que o dossiê não enumerava: o consumo do subagente **está** exposto ao hook
  (`SubagentStop` → `agent_transcript_path`), e o que falta é a **identidade da tarefa**, que não é
  campo de schema do harness. O ramo B foi cumprido à risca — nenhuma declaração, nenhum script,
  nenhum teste —, e a evidência ficou como **Sonda 5** em
  `docs/audits/SPIKE_HARNESS_EXECUCAO_AUTONOMA.md:154-195`. O dono decidiu a rota em 2026-08-19
  (`DP-S`, §23): a identidade passa a viajar por estado gravado pelo `scrum-master` no despacho. A
  continuação é a **`T55`**; esta tarefa **não é reaberta**.

### T15 — Enxugamento dos prompts absorvidos pelos instrumentos [Sonnet · classe implementação padrão · teto 40]
- **Objetivo:** invariante 3 do §3 — o texto de formato que virou código **sai** dos prompts. É onde
  a economia se realiza: esse texto é pago em todos os turnos de todos os subagentes.
- **Arquivos-alvo:** `.claude/skills/handover/SKILL.md`, `.claude/skills/proximo-passo/SKILL.md`,
  `.claude/skills/diario-de-obras/SKILL.md`, `.claude/agents/pantonic-executor.md`,
  `.claude/agents/pantonic-planner.md` (esquema de autoria de tarefa, `T4`); regenerar
  `.claude/README.md`.
- **Método:** medir antes (contagem de linhas por artefato), remover **apenas** o que um instrumento
  passou a garantir, substituir por ponteiro à assinatura do CLI, medir depois. Regra de corte: sai
  o **formato**; fica a **regra**.
- **Cuidado:** nada de remover regra que nenhum instrumento passou a cobrir — economia não é motivo
  para abrir mão de guardrail (`GOVERNANCA.md` §3, eixo de justificação).
- **Verificação:** bateria do §3; a redução medida registrada no RDO da tarefa.
- **Pronto quando:** nenhum agente precisa conhecer o formato de um artefato que um CLI gera, e a
  redução está medida em número.

### T16 — Piloto medido [Sonnet · classe investigação · teto prescrito 45]
- **Objetivo:** rodar o loop completo sobre trabalho real e comparar com a série — a única prova de
  que o desenho entrega o que promete.
- **Escopo do piloto:** um recorte de tarefas ainda abertas do `P-0733-divida-do-hub`, conduzido
  pela skill `scrum-master` de ponta a ponta, com RDO e laudo por tarefa.
- **Medidas a coletar, todas contra a linha de base de `docs/telemetria.tsv`:** consumo por tarefa;
  quantas tarefas couberam numa janela; quantos laudos reprovaram e o que a reprovação pegou; quanto
  custou a revisão em relação à execução.
- **Registro qualitativo, por ocorrência:** cada acionamento do dono durante o piloto entra no
  relatório com a **causa** que o motivou, classificada pelo §19 — questão que é dele (ambiguidade,
  conflito de requisito ou de aceitação) ou caminho feliz. O registro é por ocorrência, e o total
  de acionamentos não é medida de nada.
- **Entregável:** relatório em `docs/audits/` com as medidas, mais os RDOs produzidos, mais a lista
  de defeitos de desenho encontrados — cada um com rota (correção nesta iniciativa, tíquete
  avulso, ou aceito com motivo).
- **Gate explícito:** o piloto **pode reprovar**. Reprovação não vira correção improvisada dentro
  da tarefa — vira achado com rota e decisão do dono (`G-PLANFIDELITY`).
- **Verificação:** bateria do §3; as tarefas do piloto fecham pelo padrão vigente de qualidade,
  sem exceção concedida por serem piloto.
- **Critério de aceitação (§19, vinculante):** o piloto **reprova** quando o framework aciona o dono
  em **caminho feliz ou caminho natural** — sem pendência aberta e sem demanda que seja dele —, e
  parar para que ele limpe o contexto ou invoque a tarefa seguinte é o caso exemplar. **Uma só**
  ocorrência basta para reprovar. Acionamento cuja causa é questão do dono — ambiguidade, conflito
  de requisito ou de aceitação — é legítimo, ilimitado, se registra com a questão que o motivou e
  não pesa contra a entrega.
- **Pronto quando:** existe comparação numérica entre o fluxo novo e a série histórica, cada defeito
  encontrado tem rota, e o critério de aceitação do §19 foi aferido explicitamente, com cada
  acionamento do dono registrado pela **causa** que o motivou.

### T17 — `README.md`, `CHANGELOG.md` e veredito do dono [Opus + dono]
- **Objetivo:** dever 2 de `G-README` — a sprint encerra com a revisão do documento canônico, e o
  gate de sentido é do dono.
- **Arquivos-alvo:** `README.md` (papéis, fluxo de execução, anatomia do kit, contagens);
  `CHANGELOG.md` seção `[Não lançado]`; `docs/DIARIO_DE_OBRAS.md` (veredito).
- **Forma, nesta ordem:**
  1. `CHANGELOG.md` `[Não lançado]`: bloco consolidado — papéis novos, RDO como registro canônico,
     instrumentos, hooks, e a nota de migração para quem tinha "Notas de execução" no diário.
     **Proibido:** número de versão novo, tag, instrução de migração por número (`DE-7`).
  2. `pwsh -NoProfile -File .claude/checks/check-readme.ps1` — paridade estrutural. O guarda é
     instrumento desta atividade, **nunca** gate automático de pronto.
  3. Leitura corrida do README pelo dono: (a) o texto descreve o framework que ele governa?
     (b) alguma afirmação está equivocada, confusa ou desatualizada? (c) um cliente decidiria adotar
     — ou rejeitar — com base nisto, e a decisão seria justa?
  4. **Desdobramento para o plano seguinte** (decisão do dono, 2026-08-12): registrar em
     `docs/plans/_INBOX.md`, como linha de plano a autorar **depois** que este fechar, a **revisão
     da matéria de consumo** — teto por tarefa, alarme de consumo, telemetria e o que o framework faz
     com o número. A matéria se revê **inteira e em plano próprio**, não em card deste: a hipótese a
     confrontar com a série é que tanto alarme de teto **não paga o que custa**, já que todo
     cruzamento acaba justificado e nenhum produz a consequência que a doutrina prescreve. A linha do
     inbox é o **registro** do desdobramento — autorar o plano é ato de planejamento posterior, fora
     do escopo desta tarefa —, e carrega o que o plano novo absorve:
     - o **`TK-32`**, com o regime interino em vigor (teto é alarme, nunca bloqueio) até que aquele
       plano decida;
     - a **`T34` cancelada** deste plano, cujo corpo é o material absorvido: o insumo do dono (§15),
       a **medição obrigatória de três números** sobre `docs/telemetria.tsv` — (a) quantas tarefas
       **por classe** cruzaram o teto e por quanto, (b) em quantos cruzamentos a consequência
       prescrita pela doutrina de fato ocorreu, (c) o custo do **próprio controle** em turnos — e o
       conteúdo que a decisão precisa cobrir (o que substitui o porteiro por tarefa, onde o número
       vive entre tarefas e quem o escreve, o que acontece com a tabela de classes de
       `GOVERNANCA.md` §3, e o veredito sobre a hipótese, com a série citada);
     - a **`DP-L` não formada**: nenhuma posição sobre uso e teto é decidida dentro do `P-0734`.
- **Verificação:** veredito registrado no diário; reprovação gera rodada nova de redação, não segue
  adiante; a linha do desdobramento existe no `docs/plans/_INBOX.md`.
- **Pronto quando:** aceite explícito do dono registrado no diário, veredito sobre o critério de
  aceitação do §19 (o loop entregou a autonomia enunciada?) e desdobramento registrado. **Fecha o
  plano.**

### T18 — `rdo.py laudo`: documento próprio e recomendação de domínio fechado [Sonnet · classe implementacao · teto 40]
- **Dossiê fechado por:** `DP-D` (§9), ratificada. Primeira tarefa depois do replanejamento.
- **Objetivo:** o laudo deixa de ser uma seção de um RDO já aberto e passa a ser o documento que o
  revisor assina, emitindo — junto do veredito calculado — a recomendação que roteia o loop.
- **Arquivos-alvo:** `.claude/tools/rdo.py` (`calcular_laudo:457`, `cmd_laudo:501`, o subparser
  `laudo:751`), o template, `tests/test_rdo.py`.
- **Interface:** `laudo` passa a gravar em `docs/RDO/laudos/<plano>-<tarefa>.md`, criando o diretório
  se preciso, em vez de escrever dentro de um RDO. `calcular_laudo` passa a devolver também
  `recomendacao`, derivada assim:

  | veredito calculado | `bloqueante` | recomendação |
  |---|---|---|
  | `aprovado` | `nenhuma` | `seguir` |
  | `ressalva` | `nenhuma` | `seguir com ressalva` |
  | `reprovado` | qualquer | `refazer` |

  Mais o argumento `--escalar "<uma linha>"`: quando presente, a recomendação é `escalar`
  **independentemente** da tabela, e a linha é gravada como a pendência que a regra `B1` consome.
- **Invariantes:** a recomendação **não** é aceita como valor por argumento (mesma regra que `DA-6`
  já impõe a percentual e veredito) — o único canal de entrada do revisor é `--escalar`; o domínio é
  fechado nos quatro valores e o CLI recusa qualquer outro; escrita atômica e falha ruidosa, no
  padrão dos irmãos.
- **Cuidado:** não tocar `cmd_new` nem `cmd_close` — são a `T19`; não alterar pesos, faixas nem o
  conjunto de dimensões da rubrica, que continuam copiados de `docs/RUBRICA_DE_REVISAO.md`.
- **Verificação:** bateria do §3; testes para as três derivações da tabela, para a dominância de
  `escalar` sobre veredito `aprovado`, para a recusa de recomendação passada como valor e para o
  caminho de saída novo.
- **Pronto quando:** nenhuma chamada produz recomendação fora dos quatro valores, e o laudo existe
  como documento próprio sem depender de RDO aberto.

### T22 — Avaliação da lista de estados e fechamento da linguagem ubíqua [Opus · classe redacao · teto 30]
- **Dossiê fechado por:** `DP-E` (§10), enunciado 4 deslocado para tarefa própria e alcance
  (loop + kanban) já decidido. **Não delegável antes da `T18`** apenas por ordem de fila; não depende
  de nenhum artefato de código.
- **Objetivo:** fechar a `DP-F` — decidir se os sete estados enunciados pelo dono são *suficientes*,
  *exagerados* ou *insuficientes*, publicar a lista final e o mapa de tradução do vocabulário
  vigente. Nenhum artefato é conformado aqui; esta tarefa só produz o decision record que torna a
  conformidade mecânica.
- **Arquivos-alvo:** `docs/plans/P-0734-execucao-autonoma.md`, seção `## Dossiês fechados por
  decisão`, novo `### DP-F` imediatamente após o `### DP-C`. **Nenhum outro arquivo.**
- **Conteúdo — os sete itens que a `DP-F` fecha (nenhum pode sair com "a decidir"):**
  1. **Veredito estado a estado** sobre `triage`, `ready`, `blocked`, `in-progress`, `review`,
     `done`, `cancelled`, com o critério declarado por escrito: um estado existe se **alguém age
     diferente por causa dele** no loop (`scrum-master`) ou no kanban (escolha da próxima tarefa);
     estado sem consequência operacional observável neste repo é **exagero**, transição real sem
     estado que a nomeie é **insuficiência**.
  2. **Lista final**, uma linha por estado: nome, significado, o que dispara a entrada nele. O
     escritor é sempre o `scrum-master` (`DP-E`, enunciado 2) — não repetir por estado.
  3. **Máquina de transições**: quais transições são legais, e quais dos dois gatilhos da `DP-E`
     (invocação do revisor; escrita do RDO) cada uma dispara. Sem isso a conformidade não é
     verificável.
  4. **Alcance por objeto**: a lista governa **tarefa**. Decidir explicitamente se governa também
     **plano/iniciativa** — hoje `docs/DIARIO_DE_OBRAS.md` marca plano com `superseded`, que não é
     estado de tarefa. Se não governar, nomear o vocabulário separado que permanece e onde ele
     reside.
  5. **Tabela de tradução fechada**, um destino para cada termo vigente: `backlog`, `in progress`,
     `done`, `blocked`, `superseded`, `cancelled` (kanban de hoje) e `entregue`, `parcial`,
     `bloqueado` (trio revogado pela `DP-E`). Cada termo vira um estado da lista, **morre**, ou é
     declarado pertencente a outro vocabulário.
  6. **Critério de classificação de ocorrência** para as varreduras `T23`..`T27`: (i) `status` de
     tarefa, (ii) veredito de rubrica, (iii) homônimo — com **um exemplo real de cada**, colhido dos
     arquivos do repo (o §10.2 já registra dois: `parcial` de rubrica em `review_evidence.py:132` e
     `git status --porcelain` em `review_evidence.py:116`).
  7. **Recorte da conformidade**: confirmar — ou corrigir com justificativa — a superfície repartida
     entre `T23`..`T27`, a conformidade delegada do §10.4 e o que fica **fora** por ser registro
     histórico: `docs/DIARIO_HISTORICO.md`, `docs/benchmark/**`, `docs/audits/**`, planos fechados
     `P-0721`..`P-0732`, `Base.txt`, os bullets de fechamento já escritos no diário e os decision
     records `DP-A`..`DP-E` — que registram o que foi decidido à época e não se reescrevem.
- **Gate declarado (não é questão aberta do plano):** a `DP-F` é escrita como **proposta fechada** e
  a tarefa **PARA** para ratificação do dono, com o texto à vista — mesmo procedimento da `DP-D`
  (§9). Nada a jusante é delegável antes do "ratificado": nem `T23`..`T27`, nem a reescrita de
  `T19`/`T20`/`T21`.
- **Invariantes:** esta tarefa **não edita nenhum artefato de conformidade** — nem código, nem
  skill, nem doutrina, nem o kanban; não reabre o que a `DP-E` fechou (fronteira de escrita do
  laudo, nome do papel, alcance loop + kanban, existência dos dois gatilhos, o que da `DP-D` cai e o
  que fica); `.claude/skills/redacao-doc/SKILL.md` é normativa (invariante 4 do §3).
- **Cuidado:** contagem bruta de ocorrência **não** é medida de trabalho (§10.2, três vocabulários);
  não inventar estado para cobrir caso hipotético — o critério é consequência operacional observada
  neste repo; não decidir a materialização em código (isso é a reescrita da `T19`).
- **Verificação:** bateria do §3; releitura do `### DP-F` conferindo que os sete itens estão
  respondidos e que a tabela de tradução não deixa termo vigente sem destino.
- **Pronto quando:** existe `### DP-F` com lista final, máquina de transições e tabela de tradução
  fechada, marcado como **aguardando ratificação**, e o dono tem o texto à vista.

> **`T23` partida em `T23a`/`T23b` por orçamento (orquestrador, 2026-08-11).** A contagem de
> write-clusters da tarefa como publicada ficou em ~15-16 (o bloco normativo novo mais ~7 regiões
> de tradução em cada skill), acima da linha de 8 do item 5 do gate de delegação, que manda dividir
> **antes** de delegar. O corte é por arquivo, e não por tipo de mudança: cada fatia é um alvo único
> e a segunda depende da primeira apenas por ter para onde apontar. Nenhum conteúdo do dossiê
> original foi alterado — só repartido.

### T23a — Conformidade: residência única no `diario-de-obras` [Opus · classe redacao · teto 15]
- **Dossiê fechado por:** `DP-E` (§10.2, §10.4) e `DP-F` (`T22`, ratificada em 2026-08-11).
- **Objetivo:** a skill que **define** o kanban passa a ser a **residência única** da lista final, da
  máquina de transições e da tabela de alcance por objeto — e o próprio arquivo passa a falar só a
  lista final.
- **Arquivo-alvo (único):** `.claude/skills/diario-de-obras/SKILL.md`.
- **Conteúdo:**
  - Substituir o bullet **Status válidos** (hoje `:28-32`) pela residência única, enunciada uma vez:
    a **lista final** (item 2 da `DP-F`, uma linha por estado), a **máquina de transições** (item 3,
    com os três fechamentos: terminais sem saída, só os dois gatilhos marcados disparam ação,
    `cancelled`/`blocked` não disparam RDO) e a **tabela de alcance por objeto** (item 4, com a
    exceção declarada de `superseded` como estado exclusivo de plano/iniciativa).
  - Registrar, uma vez e não linha a linha, a fronteira de escrita do `status` da `DP-G`: o
    `scrum-master` é o único que **materializa** o valor, em qualquer estado, e o executor é **autor**
    de `review` e `blocked` — e de mais nada. *(Conciliado na rodada de 2026-08-11 pela `DP-H`, item
    de recência restrita ao desenvolvimento; fecha o `TK-31`. O artefato que este dossiê governa já
    havia sido corrigido pela `T28` — a conciliação alcança a orientação, não o que narra o
    ocorrido.)*
  - No restante do arquivo, classificar cada ocorrência pelos três tipos do item 6 da `DP-F` e
    aplicar a tabela de tradução do item 5 **só nas do tipo (i)**.
- **Invariantes:** **nenhuma regra muda de conteúdo — só de termo**; toda transição citada existe na
  máquina da `DP-F`; nenhum gate é recopiado (continuam apontados); a lista aparece enunciada em um
  único lugar do repositório.
- **Cuidado:** `git status` e veredito de rubrica não são `status` de tarefa; `entregue` (`:30`,
  `:134`) e `parcial` (`:31`) são prosa de tipo (iii) — `:30-31` desaparecem com o bullet
  substituído, `:134` **não se traduz**; exemplo colado que cite tarefa real já fechada é registro
  histórico e não se reescreve.
- **Verificação:** bateria do §3; Grep `in progress|in review` no arquivo com resultado **vazio**
  (medido em 2026-08-11 antes da tarefa: **4** ocorrências); Grep `backlog` **não** vai a zero — as
  ocorrências que sobrarem são todas do substantivo (o conjunto), nunca status (medido antes: **8**).
- **Pronto quando:** o arquivo usa exclusivamente a lista final, a lista/máquina/alcance aparecem
  enunciadas uma única vez, e nenhuma regra do kanban mudou de efeito.

### T23b — Conformidade: `proximo-passo` aponta para a residência [Opus · classe redacao · teto 15]
- **Dossiê fechado por:** `DP-E` (§10.2, §10.4) e `DP-F` (`T22`). **Não delegável antes da `T23a`
  `done`** — depende da residência única existir para apontar.
- **Objetivo:** a skill que **consome** o kanban passa a falar a lista final e a **apontar** para a
  residência, sem reenunciá-la.
- **Arquivo-alvo (único):** `.claude/skills/proximo-passo/SKILL.md`.
- **Conteúdo:**
  - Classificar cada ocorrência pelos três tipos do item 6 da `DP-F` e traduzir só as do tipo (i)
    pela tabela do item 5: heurística de escolha (hoje `in progress`, `backlog`, FIFO) e proibições
    (hoje `superseded`, `blocked` não-postergado).
  - Onde a skill citar `superseded`, **nomear que está usando o vocabulário de plano/iniciativa**
    (item 4 da `DP-F`): `superseded` não é estado de tarefa.
  - Onde couber, apontar para a residência única fixada na `T23a` em vez de reenunciar estados.
- **Invariantes:** **nenhuma regra de escolha muda de efeito — só de termo**; nenhuma lista de
  estados é recopiada; nenhum gate é recopiado.
- **Cuidado:** `bloqueado` (`:129`) e `PARCIAL` (`:151`) são tipo (iii)/prosa e **não se traduzem**;
  `<done>/<total>` do relatório de handover é contagem, não status a reescrever.
- **Verificação:** bateria do §3; Grep `in progress|in review` no arquivo com resultado **vazio**
  (medido em 2026-08-11 antes da tarefa: **6** ocorrências); Grep `backlog` **não** vai a zero — o
  que sobrar é o substantivo (medido antes: **9**).
- **Pronto quando:** a skill usa exclusivamente a lista final, não reenuncia a lista, e nenhuma regra
  de escolha de tarefa mudou de efeito.

### T24 — Conformidade: o restante do kit executável [Opus · classe redacao · teto 30]
- **Dossiê fechado por:** `DP-E` (§10.2, §10.4) e `DP-F` (`T22`). **Não delegável antes da
  ratificação da `DP-F`.** Independente da `T23` — arquivos disjuntos.
- **Objetivo:** o resto dos prompts do kit para de citar vocabulário morto.
- **Arquivos-alvo** *(contagem medida em 2026-08-11)*: `.claude/skills/handover/SKILL.md` (5),
  `.claude/skills/modelo-por-fase/SKILL.md` (3), `.claude/skills/guardrails-check/SKILL.md` (1),
  `.claude/skills/bootstrap-pantonic/SKILL.md` (1), `.claude/agents/pantonic-executor.md` (1),
  `.claude/README.md` (1). Volume pequeno e mecânico: se a tradução da `DP-F` for direta, a tarefa
  fecha bem abaixo do teto.
- **Conteúdo:** mesma classificação em três tipos e mesma tabela de tradução da `T23`; onde o texto
  enumerar estados, trocar a enumeração por **ponteiro** para a residência única fixada na `T23`.
- **Invariantes:** conteúdo de regra inalterado; nenhuma lista de estados recopiada; `.claude/README.md`
  é espelho — se o inventário de agentes/skills não mudar, só o termo muda.
- **Cuidado:** `.claude/skills/scrum-master/SKILL.md` e `.claude/agents/pantonic-reviewer.md`
  **estão fora desta tarefa** (conformidade delegada à `T21`/`T20`, §10.4) — não tocar.
- **Verificação:** bateria do §3; Grep dos termos mortos nos seis arquivos, com resultado vazio.
- **Pronto quando:** nenhum dos seis arquivos cita termo morto, e nenhum deles reenuncia a lista.

### T25 — Conformidade: espelho e índices [Opus · classe redacao · teto 30]
- **Dossiê fechado por:** `DP-E` (§10.2, §10.4) e `DP-F` (`T22`). **Não delegável antes da
  ratificação da `DP-F`.**
- **Objetivo:** a porta de entrada do projeto e os índices deixam de ensinar vocabulário morto.
- **Arquivos-alvo** *(contagem medida em 2026-08-11)*: `README.md` (21), `CHANGELOG.md` (3),
  `docs/DOC_MAP.md` (1), `docs/RESIDENCIA_DOUTRINA.md` (1).
- **Conteúdo:** classificação em três tipos e tradução, como na `T23`. O `README.md` é **espelho**:
  descreve o vocabulário e aponta para a residência normativa, nunca a substitui. O `CHANGELOG.md`
  ganha a entrada da mudança de vocabulário; **entradas antigas não se reescrevem** (registro do que
  foi lançado à época). Em `docs/RESIDENCIA_DOUTRINA.md`, registrar onde a lista de estados reside
  agora, se a residência mudou de arquivo.
- **Invariantes:** paridade estrutural do espelho preservada; nada de doutrina nova nascendo no
  README; entradas históricas do CHANGELOG intactas.
- **Cuidado:** o `README.md` também será revisado no fecho da sprint (`T17`) — esta tarefa é
  conformidade de vocabulário, não a revisão de sentido.
- **Verificação:** bateria do §3; `pwsh .claude/checks/check-readme.ps1` com exit 0; Grep dos termos
  mortos nos quatro arquivos (fora das entradas históricas do CHANGELOG), com resultado vazio.
- **Pronto quando:** o espelho passa, os índices apontam para a residência certa e nenhum termo
  morto sobrevive fora de registro histórico.

### T26 — Conformidade: doutrina normativa [Opus · classe redacao · teto 30]
- **Dossiê fechado por:** `DP-E` (§10.2, §10.4), `DP-F` (`T22`), `DP-G` e `DP-H` (§13). **Não
  delegável antes da ratificação da `DP-F` nem da ratificação da `DP-I`** (a decisão que a `T29`
  fecha): a premissa de que **não existe campo material de `status` por tarefa** cai com o artefato
  `tarefa`, e é ele que diz onde o valor é gravado. *(Dossiê reescrito na rodada de 2026-08-11 pela
  `DP-H`.)*
- **Objetivo:** a doutrina do kit e a rubrica passam a distinguir explicitamente `status` de tarefa
  e veredito de rubrica — que hoje compartilham palavras.
- **Arquivos-alvo** *(contagem medida em 2026-08-11)*: `GOVERNANCA.md` (12),
  `docs/RUBRICA_DE_REVISAO.md` (15), `ARQUITETURA_PANTONICA.md` (3).
- **Conteúdo:** em `GOVERNANCA.md`, o vocabulário de `status` de tarefa segue a lista final e a
  matriz de responsabilidades registra a fronteira da `DP-G` — o `scrum-master` é o único que
  **materializa** o `status`, em qualquer estado, e o executor é **autor** de `review` e `blocked`,
  e de mais nada — e que **o laudo é escrito só pelo `reviewer`** (`DP-E`, enunciado 3), sem
  recopiar a lista de estados nem o enunciado do absoluto que a `DP-G` derrubou. O **lugar** onde o
  valor é materialmente gravado é o que a `DP-I` fixar, e esta tarefa **transcreve** esse lugar sem
  reinterpretá-lo. Em `docs/RUBRICA_DE_REVISAO.md`, a expectativa medida é **quase nenhuma
  substituição**: as ocorrências são veredito (`conforme`/`parcial`/`não conforme`); o trabalho é
  tornar isso explícito onde o texto ficar ambíguo. Em `ARQUITETURA_PANTONICA.md`, só o que for
  vocabulário de status de tarefa.
- **Invariantes:** **pesos, faixas e dimensões da rubrica não mudam** — são decisão da `T5`, fora
  desta tarefa; o termo *inspetor* não entra em nenhum artefato (`DP-E`); doutrina não ganha regra
  nova aqui.
- **Cuidado:** `GOVERNANCA.md` é doc grande — entrar por `docs/DOC_MAP.md` e Grep de âncora, nunca
  Read integral; se a substituição na rubrica for zero, registrar "zero" como resultado, não como
  omissão; as contagens de 2026-08-11 valem **antes** da `T31`, que passa nos mesmos dois arquivos
  para o resíduo de `pacote de retorno` — remedir na entrada, e não tocar o que ela já corrigiu.
- **Verificação:** bateria do §3; Grep dos termos mortos nos três arquivos, com resultado vazio ou
  com cada sobrevivente justificado no registro da tarefa como veredito/homônimo.
- **Pronto quando:** os três arquivos distinguem sem ambiguidade os dois vocabulários, e a
  responsabilidade de escrita do `status` está registrada onde ela mora.

### T27 — Conformidade: kanban, planos vivos e varredura de fecho [Opus · classe redacao · teto 30]
- **Dossiê fechado por:** `DP-E` (§10.2, §10.4) e `DP-F` (`T22`). **Não delegável antes da `T23`,
  `T24`, `T25` e `T26`** — a varredura de fecho mede o resultado delas.
- **Objetivo:** o registro material do `status` — o kanban e os planos vivos — passa à lista final, e
  o repositório inteiro é varrido para provar que não sobrou vocabulário morto vivo.
- **Arquivos-alvo** *(contagem medida em 2026-08-11)*: `docs/DIARIO_DE_OBRAS.md` (39),
  `docs/plans/_INBOX.md` (12), `docs/plans/P-0734-execucao-autonoma.md` (46, **só os marcadores
  vivos**), `docs/plans/P-0733-divida-do-hub.md` (1),
  `docs/RDO/P-0734-T11-skill-scrum-master-o-loop.md` (1).
- **Conteúdo:**
  - **Só marcador vivo migra.** Marcador vivo é o que descreve o estado **atual** de uma tarefa, de
    um plano ou de um tíquete. **Registro já escrito não se reescreve:** bullets de fechamento,
    **todo dossiê de decisão deste plano** (`DP-A` em diante, incluindo os das rodadas de
    replanejamento dos §9 a §20), RDO já emitido e prosa que narra o que aconteceu à época ficam como
    estão — reescrevê-los falsificaria o registro. Marca de revogação **não é** reescrita: onde a
    `T47` marcou um dossiê como derrubado, a marca fica e o corpo continua intocado.
  - Aplicar a tabela de tradução da `DP-F` aos marcadores vivos, incluindo os tíquetes do
    `_INBOX.md` e a linha de índice de cada iniciativa do diário.
  - **Varredura de fecho** sobre o repo, excluído o recorte histórico do item 7 da `DP-F`: Grep de
    cada termo morto e do termo `inspetor`. Cada ocorrência remanescente é classificada nos três
    tipos e justificada por escrito; a única exceção conhecida de `inspetor` é a nota de vocabulário
    do §10 deste plano, que registra a abolição do termo e por isso o cita.
  - **Resíduo em código vira tíquete, não edição.** Se a varredura achar `status` de tarefa em
    `.claude/tools/telemetria.py` (2 ocorrências medidas), `.claude/tools/review_evidence.py` (6) ou
    `tests/test_review_evidence.py` (5) — todas classificadas como veredito ou homônimo na medição
    de 2026-08-11 —, o achado entra como tíquete em `docs/plans/_INBOX.md`. Renomear vocabulário em
    código é tarefa de implementação, com testes, e não se faz dentro de uma varredura documental.
- **Invariantes:** nenhum bullet histórico reescrito; nenhum arquivo da conformidade delegada
  (`rdo.py`, `rdo_template.md`, `tests/test_rdo.py`, `pantonic-reviewer.md`, `scrum-master/SKILL.md`)
  tocado aqui; nenhuma edição em `.py` ou em `tests/`.
- **Cuidado:** `docs/DIARIO_DE_OBRAS.md` é doc grande e de escrita concorrente — editar por âncora,
  nunca reescrever seção inteira; a maior parte das 46 ocorrências deste plano é citação dentro de
  decision record e **não** se toca.
- **Verificação:** bateria do §3; a varredura de fecho fica registrada com a contagem final por
  termo e a justificativa de cada sobrevivente.
- **Pronto quando:** todo marcador vivo usa a lista final, todo sobrevivente de termo morto está
  justificado por escrito, e nenhum resíduo de código foi editado por esta tarefa — só tiquetado.

### T19 — `rdo.py`: o RDO se gera no fechamento [Sonnet · classe implementacao · teto 40]
- **Dossiê fechado por:** `DP-D` (§9), `DP-F`, `DP-G` e `DP-H` (§13). **Não delegável antes da
  `T18`** — o `pacote` que o `close` recebe é o conjunto que a `T18` passou a calcular **dentro do
  laudo**. *(Dossiê reescrito na rodada de 2026-08-11 pela `DP-H`: o `close` deixa de ler o laudo
  persistido e passa a receber o `pacote` por argumento do `scrum-master`, e o RDO deixa de pendurar
  ponteiro para documento que é descartado.)* Todos os números de linha abaixo valem para o estado
  de `.claude/tools/rdo.py` **depois** da `T18`. **Teto rígido: 40 tool uses — PARE e reporte ao
  atingir 40**, mesmo com frente aberta; o escopo já foi medido em ~7 write-clusters e estourar é
  sinal de decomposição errada, não licença para seguir.
- **Objetivo:** o RDO deixa de ser aberto no início e passa a ser **gerado no fechamento** (`D3`), a
  partir do plano, do laudo, do consumo medido e do desdobramento calculado. É o que dissolve a
  circularidade `close` ↔ laudo registrada no fechamento da `T11`.
- **Premissa de escopo, derivada e declarada:** o RDO é escrito **por uma única transição**,
  `review` → `done` (gatilho 2 da `DP-E`; `DP-F` item 3, fechamento (c)). Tarefa que termina em
  `cancelled` e tarefa que para em `blocked` **não** produzem RDO — o gasto fica na telemetria e o
  juízo fica no laudo. Logo o `close` só é chamado sobre tarefa aceita: **não existe `--status`**, nem
  no `laudo` nem no `close`, e nenhum `status` é lido de lugar nenhum.
- **Segunda premissa de escopo, da `DP-H` (§13, itens 3 e 4):** o laudo é documento **consumido e
  descartado** pelo `scrum-master`, e o `pacote` é o conjunto de informações obrigatórias **contidas
  no laudo**, suficientes para invocar este script sem falha. Consequência direta: o `close`
  **não lê arquivo de laudo** — recebe o `pacote` por argumento, de quem consumiu o laudo — e o RDO
  **não carrega ponteiro** para o laudo, porque o documento é apagado depois de consumido (decisão do
  dono de 2026-08-11, alternativa `a`, registrada nos achados do §9). O que não estiver no `pacote`
  não entra no RDO por improviso: o critério do que mais mereceria retenção é a `T30`, e qualquer
  acréscimo é materializado por card autorado depois da ratificação dela — nunca aqui.
- **Arquivos-alvo:** `.claude/tools/rdo.py`, `.claude/tools/rdo_template.md`, `tests/test_rdo.py`.
- **Conteúdo, em cinco frentes:**
  - **(a) `close` passa a criar o documento.** CLI final:
    `close --plano <caminho do .md> --tarefa <ID> --tool-uses <N> --tokens-k <N> --duracao-s <N>
    --veredito <aprovado|ressalva> --percentual <N> --bloqueante <dimensão|nenhuma>
    --recomendacao "<uma linha>" --pendencia-laudo "<uma linha|nenhuma>"
    [--pendencia "<uma linha>"] [--rdo-dir] [--template]
    [--esquema-legado --modelo --classe --teto]`. Os quatro últimos são os do subparser `new:771-778`,
    **movidos verbatim** — sem eles o `T17` (cabeçalho legado) deixaria de fechar. Os **cinco**
    argumentos do meio são o `pacote` da `DP-H` (item 4) e são **obrigatórios**: é o que faz "invocar
    o script sem falha" ser verificável. `--veredito` tem domínio fechado `{aprovado, ressalva}` por
    `choices` (a premissa de escopo torna `reprovado`/`bloqueado` inalcançáveis); `--percentual` é
    inteiro em `0..100`; `--bloqueante` aceita `nenhuma`; `--recomendacao` e `--pendencia-laudo` são
    de **uma linha**, recusadas por `_contar_linhas:620` quando vierem com mais. Saem `--rdo`,
    `--status`, `--laudos-dir`, `--arquivos-tocados`, `--desvios-do-dossie`, `--verificacao`,
    `--achados`, `--orcamento` e `--pendencia-para-o-dono`.
  - **(b) Fluxo de `cmd_close:689`,** nesta ordem: 1) `extrair_dossie:190` com os mesmos argumentos
    de `cmd_new:329`; 2) `plano_id` pela regra de `cmd_new:343`; 3) os cinco campos do `pacote` vêm
    **dos argumentos**, transcritos sem recálculo — o `close` **não abre nenhum arquivo de laudo** e
    não conhece o diretório de laudos; argumento ausente é falha ruidosa do próprio `argparse`;
    4) `orcamento_estourado = tool_uses > dossie.teto`, com o teto vindo **sempre** do
    cabeçalho (`extrair_dossie` devolve inteiro nos dois esquemas, inclusive em `teto prescrito N`),
    nunca de argumento; 5) `desdobramento = calcular_desdobramento(veredito, orcamento_estourado)`
    — ver item (c); 6) render do template em
    `<rdo-dir>/<plano_id>-<tarefa>-<slug do título>.md` (naming de `cmd_new:345`), escrita atômica,
    destino já existente é falha ruidosa — é o que substitui a checagem de "RDO já fechado";
    7) `_regenerar_indice:652` roda como hoje.
  - **(c) `calcular_desdobramento` encolhe para o domínio que sobrou.** Assinatura nova
    `calcular_desdobramento(veredito, orcamento_estourado)` em `:624`. Saem os parâmetros `status`
    (o `close` não o tem mais) e `bloqueante` (já era **morto no corpo** — `TK-29`, que **fecha
    nesta tarefa**). Saem, com eles, os ramos `bloqueado` e `reprovado`, **inalcançáveis** sob a
    premissa de escopo: tarefa bloqueada ou reprovada não chega ao `close`. Ramo morto testado é o
    que o `G-DEADCODE` proíbe. Tabela final, dois ramos e uma precedência:

    | condição | desdobramento |
    |---|---|
    | `orcamento_estourado` | `estouro` — vence o veredito |
    | `veredito=ressalva` | `aprovado com ressalva` |
    | `veredito=aprovado` | `aprovado` |

  - **(d) `--pendencia` e a composição do campo.** Uma linha; mais de uma, falha ruidosa por
    `_contar_linhas:620`. O campo `**Pendência para o dono:**` do RDO é composto assim:

    | `--pendencia` | `--pendencia-laudo` | linha(s) gravada(s) no RDO |
    |---|---|---|
    | ausente | `nenhuma` | `nenhuma` |
    | ausente | `<Y>` | `laudo: <Y>` |
    | `<X>` | `nenhuma` | `executor: <X>` |
    | `<X>` | `<Y>` | `executor: <X>` e `laudo: <Y>`, nesta ordem, uma por linha |

  - **(e) O que morre e o que fica.** Morrem `cmd_new:324`, o subparser `new:768`, os testes do
    `new`, `_CAMPOS_PACOTE_ORDEM:584`, `_TETO_CAMPO_PACOTE:594`, `_STATUS_VALIDOS:604`,
    `_FECHAMENTO_MARCADOR_RE:606`, `_EXECUCAO_CAMPO_VAZIO_RE:607` e `_ORCAMENTO_RE:613`.
    `_LAUDO_VEREDITO_RE:611` e `_LAUDO_BLOQUEANTE_RE:612` **perdem o único consumidor que este dossiê
    lhes dava** (o `close` não lê laudo): sobrevivem apenas se algum caminho vivo do `laudo` (`T18`)
    as usar depois da mudança — sem uso vivo, morrem junto com o resto, e o juiz é `dead_code.py` em
    exit 0, não o julgamento do executor. **Permanecem** `extrair_dossie:190` (`review_evidence.py` a reusa, e removê-la quebra o irmão),
    `_slugify`, `_render`, `_contar_linhas:620`, `_TITULO_RDO_RE:614`, `_DESDOBRAMENTO_RE:615` e
    `_regenerar_indice:652`.
- **Template (`rdo_template.md`), seção a seção:** o título `# RDO — {{PLANO_ID}} · {{TAREFA_ID}}`, o
  cabeçalho de quatro linhas e a seção `## Dossiê` **não mudam** (`_TITULO_RDO_RE` depende do
  título). `## Execução` perde os oito bullets do pacote e passa a **duas** linhas de campo:
  **Consumo** — `{{TOOL_USES}}` tool uses contra o teto `{{TETO}}`, `{{TOKENS_K}}` k tokens,
  `{{DURACAO_S}}` s, com a fonte `<usage>` nomeada na própria linha — e **Pendência para o dono**,
  `{{PENDENCIA}}`. `## Laudo` passa a **quatro** linhas de campo — Veredito, Percentual, Dimensão
  bloqueante, Recomendação —, todas vindas do `pacote`. A linha de ponteiro **não nasce**:
`{{LAUDO_PATH}}` fica **fora** do template, porque o laudo é apagado depois de consumido (`DP-H`
item 3) e RDO não pendura referência a documento inexistente. Nasce no
  template a seção `## Fechamento`, com a linha **Desdobramento** e `{{DESDOBRAMENTO}}`, hoje
  concatenada em código (`cmd_close:745`) — formato mora no template. Os rótulos em negrito seguem o
  molde `**<Rótulo>:** <valor>` já usado pelo laudo, e `_DESDOBRAMENTO_RE:615` continua casando com a
  linha do desdobramento.
- **Invariantes:** o RDO nunca repete a prosa do laudo — carrega **os campos do `pacote`**, e mais
  nada (`DA-5`); `arquivos_tocados` e `verificacao` **não voltam** ao RDO (o `D2` os realocou para
  `review_evidence.py`), e `desvios_do_dossie`/`achados` **não ganham residência**: eles vivem no
  laudo, que é descartado — o que deveria sobreviver a esse descarte é a matéria da `T30`, e nada
  entra no documento por improviso desta tarefa; nenhum juízo é **originado** por argumento —
  `percentual`, `veredito`, `bloqueante` e `recomendação` continuam **calculados** por `rdo.py laudo`
  (`DA-6`) e chegam ao `close` apenas **transcritos** por quem consumiu o laudo (`DP-H` item 4), de
  modo que nenhum agente inventa juízo; o único argumento de conteúdo **autoral** é `--pendencia`,
  canal do executor; `close` com campo do `pacote` ausente, com `--veredito` fora do domínio ou sobre
  RDO já existente falha ruidosamente; escrita atômica; o formato continua morando no template, não
  em prompt de agente (invariante 3 do §3).
- **Cuidado:** os RDOs de `T1`..`T10` **não** são retroagidos (decidido na ratificação da `DP-D`) —
  não gerar documento para tarefa histórica; o único RDO existente
  (`docs/RDO/P-0734-T11-skill-scrum-master-o-loop.md`) foi escrito sob o formato antigo e **não** é
  reescrito nem regravado por esta tarefa. A `T18` **não é tocada em nenhum ponto** — tabela de
  recomendação, `--escalar`, caminho de saída e atomicidade do laudo ficam como estão, e o `laudo`
  **não** ganha argumento novo. Não tocar `review_evidence.py` nem `telemetria.py`; a skill
  `scrum-master` é a `T21a`/`T21b` e o agente revisor é a `T20`. Os testes usam `--rdo-dir` em
  `tmp_path`, nunca o `docs/RDO` real — e **nenhum** teste do `close` cria arquivo de laudo, porque o
  comando não o lê mais.
- **Verificação:** bateria do §3, mais testes para: (1) geração completa a partir de plano +
  `pacote` + consumo; (2) recusa de fechar com **cada um** dos cinco argumentos do `pacote` ausente;
  (3) recusa de `--veredito` fora de `{aprovado, ressalva}` e de `--percentual` fora de `0..100`;
  (4) regeneração do índice com mais de um RDO; (5) ausência do subcomando `new` e do argumento
  `--laudos-dir` na CLI do `close`; (6) os três ramos da tabela do item (c), com a precedência do estouro sobre o veredito
  (`aprovado` + estouro dá `estouro`; `ressalva` sem estouro dá `aprovado com ressalva`; `aprovado`
  sem estouro dá `aprovado`); (7) as quatro linhas da tabela do item (d), incluindo `--pendencia` de
  duas linhas recusada; (8) fechar duas vezes a mesma tarefa falha na segunda.
- **Pronto quando:** um RDO completo nasce de **uma** chamada de `close` no fechamento; nenhum agente
  conhece o formato do documento; `rdo.py --help` não oferece mais `new`; nenhum `status` aparece na
  CLI, no corpo ou no template; nenhuma leitura de arquivo de laudo sobrevive no `close` e nenhum
  ponteiro para o laudo sobrevive no template; a suíte fecha verde sem piso de regressão perdido.

### T20 — `pantonic-reviewer`: o revisor sem pacote [Opus · classe redacao · teto 30]
- **Dossiê fechado por:** `DP-D` (§9), `DP-F`, `DP-G` e `DP-H` (§13). **Não delegável antes da
  `T18`** — o protocolo cita a saída que ela cria. *(Dossiê reescrito na rodada de 2026-08-11 pela
  `DP-H`: `pacote` deixa de ser objeto morto — ele existe **dentro do laudo** —, e o que morre é o
  `pacote de retorno` do executor.)*
- **Objetivo:** `D4` — o revisor julga a entrega contra o dossiê e o diff, nunca contra a narrativa
  de quem executou.
- **Arquivos-alvo:** `.claude/agents/pantonic-reviewer.md`. `.claude/README.md` só é regenerado se o
  inventário de agentes mudar — e não muda, porque isto é edição.
- **Conteúdo, em três frentes:**
  - **(a) Entrada.** O protocolo troca "ler o pacote de retorno" por **ler o dossiê da tarefa no
    plano, o dossiê de evidência de `review_evidence.py` e o diff**. Nenhuma das três é narrativa do
    executor. O `pacote de retorno` — objeto de oito campos devolvido pelo executor — **não existe**;
    o `pacote` que existe é o da `DP-H` (item 4), **produzido pelo `reviewer` dentro do laudo**.
  - **(b) Saída.** As duas linhas de veredito mais o laudo em documento próprio, emitido pelo
    gerador. O laudo **carrega o `pacote`** — veredito, percentual, dimensão bloqueante, recomendação
    e pendência —, cuja suficiência é o critério: com esses cinco campos o `scrum-master` invoca o
    `rdo.py close` sem falha (`DP-H` item 4). O laudo é **consumido e descartado** por ele (`DP-H`
    item 3): o `reviewer` não o trata como residência durável, não remete o leitor a ele para
    completar o juízo, e não conta com ele existir numa rodada seguinte. O revisor
    **não declara `status`** e nenhuma palavra do vocabulário de `status` entra na
    saída dele (`DP-E` enunciado 3; `DP-G` item 1: ele está fora da fronteira nos dois atos, autoria
    e materialização). `--escalar` **é** dele, e é por onde a pendência de arquitetura ou requisito
    chega ao loop.
  - **(c) Conformidade de vocabulário do arquivo** (conformidade delegada, §10.4), contra a `DP-F`:
    traduzir **só** ocorrência de tipo (i). O `parcial` do veredito de rubrica é tipo (ii) e
    **permanece**; `entregue` e `bloqueado` como status **não sobrevivem** no arquivo.
- **Invariantes:** as proibições vigentes permanecem inteiras (não edita código, não corrige o que
  aponta, não replaneja, não marca `conforme` contra vermelho mecânico — `DA-7`); o `model: opus`
  permanece (`DA-12`); a lista de ferramentas **não** é alterada aqui — o escopo de `Bash` é o
  `TK-27` e tem rota própria.
- **Cuidado:** `.claude/skills/redacao-doc/SKILL.md` é normativa (invariante 4 do §3); nenhuma
  ocorrência de "pacote de retorno" pode sobrar no arquivo (medido em 2026-08-11: **3** —
  `:30`, `:39`, `:71`). Classificar antes de substituir (`DP-F` item 6) — a contagem bruta de
  `parcial` superestima o trabalho, e a de `pacote` também: o termo sobrevive na acepção da `DP-H`.
- **Verificação:** bateria do §3; Grep por `pacote de retorno` no arquivo com resultado vazio; cada
  ocorrência remanescente de `pacote` justificada na tarefa como a acepção da `DP-H` (conjunto
  obrigatório dentro do laudo); Grep por `entregue|bloqueado` no arquivo com resultado vazio.
- **Pronto quando:** o arquivo descreve um revisor cuja única entrada é dossiê + evidência + diff,
  cuja saída roteia o loop por campo, e que não produz `status` em nenhuma linha.

### T21 — Skill `scrum-master`: o loop reescrito — **partida em `T21a`/`T21b` por orçamento**
A reescrita contra `DP-F` + `DP-G` levou a contagem de write-clusters do arquivo único a **~9**,
acima da linha de 8 do item 5 do gate de delegação. O corte é por **natureza da edição** —
procedimento (`T21a`) e tabela transcrita mais vocabulário (`T21b`) —, sem alterar nada do conteúdo
decidido. `T21b` sucede `T21a` no mesmo arquivo; dois agentes não o tocam ao mesmo tempo.

### T21a — Skill `scrum-master`: os passos do loop [Opus · classe redacao · teto 30]
- **Dossiê fechado por:** `DP-D` (§9), `DP-F` e `DP-G`. **Não delegável antes da `T19` e da `T20`** —
  os passos citam os comandos e a saída que elas fixam.
- **Objetivo:** alinhar os passos do loop ao fluxo ratificado, removendo o ponto aberto que hoje o faz
  parar no passo 9 e materializando a fronteira de `status` da `DP-G`.
- **Arquivos-alvo:** `.claude/skills/scrum-master/SKILL.md` — seções `## Estado do loop` e
  `### Passo 2` a `### Passo 9`.
- **Conteúdo, passo a passo:**
  - **`## Estado do loop`** — além dos três contadores da `DP-B` (retentativas da tarefa corrente,
    tarefas fechadas na janela, consumo acumulado), o loop passa a manter a **fila corrente e a ordem
    dela**, porque `A3a` a reordena em execução. Nada mais entra.
  - **Passo 2** — a seleção lê a fila corrente (reordenada, se `A3a` já agiu nesta janela), não a
    ordem original do §5 do plano.
  - **Passo 3** — antes de delegar, o `scrum-master` **materializa `ready` → `in-progress`**
    (`DP-G` item 1, consequência 3): o executor recebe a tarefa já em `in-progress` e nunca produz
    esse valor.
  - **Passo 4** — o despacho instrui o executor a devolver **uma** das duas linhas da gramática do
    item 2 da `DP-G`: `<tarefa> review [pendencia=<uma linha>]` ou
    `<tarefa> blocked motivo=<dependencia|premissa> <uma linha de razão>`. Sai a instrução de
    `rdo.py new`. O despacho declara também a **regra de desempate** (`DP-G` item 3): na dúvida entre
    os dois motivos, `premissa`.
  - **Passo 5** — a recepção passa a ser essa linha. O `scrum-master` **materializa** o valor
    devolvido, transcrevendo sem discricionariedade (`DP-G` item 1): não converte `blocked` em
    `review`, não converte `review` em `done`, não reclassifica o motivo. Palavra fora do domínio,
    `blocked` sem `motivo=`, ou `motivo=` fora do par ⇒ **retorno inválido**, regra `A2` (o termo
    `pacote` fica reservado à acepção da `DP-H`, item 4 — o conjunto obrigatório dentro do laudo). Os `tools`
    gastos são lidos do bloco `<usage>` da notificação de conclusão, **nunca** do relato do executor.
  - **Passo 6** — **gatilho 1** da `DP-E`: a entrada em `review` é o que invoca o revisor. Ele é
    despachado com **o mesmo dossiê** que o executor recebeu, mais o dossiê de evidência; nenhum
    caminho de RDO é repassado, porque não existe RDO ainda. Tarefa que voltou `blocked` **não**
    passa por aqui (`DP-G` item 4): não há entregável a julgar.
  - **Passo 9** — **gatilho 2** da `DP-E`: a entrada em `done` é o que escreve o RDO, por **uma**
    chamada de `rdo.py close` com o consumo medido **e com o `pacote` extraído do laudo** (`DP-H`
    item 4: veredito, percentual, dimensão bloqueante, recomendação e pendência, passados como
    argumentos). Consumido o laudo, o `scrum-master` o **apaga** (`DP-H` item 3, decisão do dono de
    2026-08-11, alternativa `a`) — nada do laudo é reinserido numa rodada seguinte, e o RDO não
    guarda ponteiro para ele. O bloco "Ponto aberto — o loop para aqui até o
    dono decidir" **sai**. Tarefa que termina em `cancelled`, e tarefa que para em `blocked`, **não**
    disparam RDO (`DP-F` item 3, fechamento (c)); o gasto continua registrado pela telemetria.
- **Invariantes:** a fonte normativa continua sendo este plano (§9, `DP-F`, `DP-G`), e a skill
  continua sendo forma operacional — a nota "divergência resolve a favor da seção" permanece; nenhum
  gate é recopiado (`G-PLANREADY` e o gate de delegação continuam **apontados**, e a `T12` depende
  disso); a lista de estados, a máquina e o alcance por objeto **não são recopiados** aqui — a
  residência única é `.claude/skills/diario-de-obras/SKILL.md` (`DP-F` item 4).
- **Cuidado:** não tocar os passos 1, 7, 8 e 10 nem as seções `## Tabelas de roteamento`,
  `## Relatório de encerramento`, `## Proibições` e `## Guardrails` — as tabelas são a `T21b`. No
  texto que esta tarefa escrever, o termo único é **`reviewer`** (`DP-K` §14.2 item 2): o passo 6
  passa a se chamar **Despacho do `reviewer`**, e as sete ocorrências de *revisor* nos passos 5–9
  (`:94`, `:96`, `:100`, `:108`, `:111`, `:115`, `:135`) saem junto com a reescrita, a custo marginal
  zero. A `description` do frontmatter (`:3`) **não** é tocada aqui — é linha espelhada e pertence à
  `T33`.
- **Verificação:** bateria do §3; Grep por `pacote de retorno` nas seções alteradas com resultado
  vazio.
- **Pronto quando:** todo passo alterado tem gatilho, entrada e saída declarados; os dois gatilhos da
  `DP-E` estão nomeados nos passos 6 e 9; nenhum passo depende de juízo não roteado.

### T21b — Skill `scrum-master`: tabelas de roteamento e vocabulário [Opus · classe redacao · teto 30]
- **Dossiê fechado por:** `DP-B`, `DP-F` e `DP-G` (item 4). **Não delegável antes da `T21a`** — mesmo
  arquivo.
- **Objetivo:** transcrever as tabelas de roteamento no estado ratificado e fechar a conformidade de
  vocabulário do arquivo (conformidade delegada, §10.4).
- **Arquivos-alvo:** `.claude/skills/scrum-master/SKILL.md` — seções `## Tabelas de roteamento`,
  `## Relatório de encerramento`, `## Proibições` e `## Guardrails`, mais a varredura do arquivo
  inteiro.
- **Conteúdo:**
  - **Bloco A.** `A3` é **partida** em `A3a` (`motivo=dependencia`: reordena a fila para que a
    bloqueada suceda a que a bloqueia, materializa `blocked` com a razão, **não** despacha revisor,
    **não** escreve RDO, **não** consome retentativa, **não** incrementa o contador de tarefas
    fechadas → **segue**) e `A3b` (`motivo=premissa`: materializa `blocked` com a razão, **não**
    despacha revisor, **não** escreve RDO → **PARA**, escalada ao dono). `A5` **sai** da tabela —
    `parcial` morreu como status e entrega incompleta é veredito do revisor (`DP-G` item 4). `A4`
    passa a ler o `<usage>`; `A6`/`A8`/`A9` passam a ler a **recomendação** do laudo em vez de
    derivar o desdobramento do veredito; `A6` passa a despachar um executor **novo em contexto novo**
    com o dossiê original mais as **diretivas atualizadas** que o `scrum-master` extraiu da
    recomendação — **nunca o caminho do laudo** (`DP-H` item 3: o laudo é descartado e não se
    reinsere; o `D6` fica reconciliado neste ponto). `A1`, `A2` e `A7` não mudam, e a precedência
    "a primeira que casa vence" permanece.
  - **Bloco B.** `B1` passa a ler a pendência do retorno do executor (`pendencia=`) ou a recomendação
    `escalar` do laudo. `B2`, `B3` e `B4` não mudam, e os três tetos da `DP-B` permanecem nos valores
    vigentes.
  - **Descarte do laudo em qualquer ramo** *(`DP-K` §14.4)*. O laudo é **efêmero** e morre no consumo,
    não só no fechamento: `A6` (reexecução), `A7`/`A8`/`A9` e `B1` (escalada) também o **descartam**
    depois de extraída a recomendação. Nenhuma linha de tabela guarda ponteiro para o laudo, e nada
    dele é reinserido em rodada seguinte — o que a reexecução precisa saber viaja nas **diretivas
    atualizadas**. O apagamento no fechamento continua sendo o passo 9 da `T21a`, que **não se
    reabre**.
  - **Vocabulário.** Traduzir **só** ocorrência de tipo (i) da `DP-F` item 6, no arquivo inteiro:
    `in progress` → `in-progress`, `in review` → `review`, `backlog` (status) → `ready`. `entregue`,
    `parcial` e `bloqueado` como **status** não sobrevivem; `parcial` como **veredito de rubrica**
    permanece, e `bloqueado` em prosa corrente permanece. Classificar antes de substituir. **Entra
    também** (`DP-K` §14.2 item 2) *revisor* → **`reviewer`** no **corpo** do arquivo — as quatro
    ocorrências medidas em `:185`, `:186`, `:187` e `:236`, mais o que a `T21a` porventura não tenha
    convertido —, **exceto** a `description` do frontmatter (`:3`), que é linha espelhada e pertence à
    `T33`. Tocar a `description` aqui quebraria a paridade de `check-readme.ps1` no fecho desta tarefa.
- **Invariantes:** nenhuma regra muda de efeito além do que está declarado acima; as proibições e o
  relatório de encerramento só mudam onde citam o pacote de retorno ou o vocabulário morto; o
  frontmatter **não** é editado.
- **Cuidado:** não reabrir os passos entregues pela `T21a`; a tabela é **transcrição** das decisões,
  não reinterpretação — divergência resolve a favor da seção.
- **Verificação:** bateria do §3; Grep por `pacote de retorno` no arquivo com resultado vazio; Grep
  por `in progress|in review` com resultado vazio; Grep case-insensitive por `revisor` no arquivo com
  **exatamente uma** sobrevivente — a `description` do frontmatter (`:3`), que é da `T33`; percurso a
  seco do fluxo sobre uma tarefa já fechada, registrado na própria tarefa, sem executar nada.
- **Pronto quando:** as duas tabelas refletem `A1`..`A9` (com `A3` partida e `A5` ausente) e
  `B1`..`B4` no estado ratificado, e o arquivo não carrega termo morto de `status`.

### T28 — Sanitização: o texto vigente reconciliado com a `DP-G` [Opus · classe redacao · teto 15]
- **Dossiê fechado por:** `DP-G` item 5 (encomenda `E1` do §11.4, decidida pelo dono em 2026-08-11).
- **Objetivo:** a `DP-G` contradiz a parte **absoluta** de três frases já escritas — e a correção não
  se faz por edição silenciosa no lugar onde ela é descoberta. Esta tarefa reconcilia as quatro
  superfícies medidas, e só elas.
- **Ressalva de escopo, declarada para não ser recusada:** o item 7 da `DP-F` põe os decision records
  `DP-A`..`DP-F` **fora** das varreduras de conformidade de vocabulário. Esta tarefa **não é**
  conformidade de vocabulário: é reconciliação de contradição normativa entre decisões ratificadas,
  encomendada nominalmente. As duas coisas não se confundem e o item 7 continua valendo para o que
  ele governa.
- **Arquivos-alvo:** `docs/plans/P-0734-execucao-autonoma.md` (§10.2 e `DP-F` itens 2 e 3) e
  `.claude/skills/diario-de-obras/SKILL.md` (`## Status — residência única`).
- **Conteúdo — quatro edições, nenhuma a mais**, conforme a tabela do item 5 da `DP-G`:
  1. **`§10.2`, enunciado 2** — "o `scrum-master` é o **único** papel que o escreve… nem o executor…
     escrevem `status`" passa a dizer: único que **materializa**; o executor é **autor** de `review` e
     `blocked`. Ponteiro para a `DP-G` na própria frase.
  2. **`DP-F` item 2, linha *Escritor*** — mesma correção, com ponteiro.
  3. **`DP-F` item 3, frase de abertura** — "Toda transição é uma escrita do `scrum-master`" passa a
     "toda transição é **materializada** pelo `scrum-master`; a **autoria** de `in-progress` →
     `review` e `in-progress` → `blocked` é do executor".
  4. **Residência única** em `.claude/skills/diario-de-obras/SKILL.md` — a linha *Escritor* que a
     `T23a` copiou recebe a mesma correção, no lugar onde ela é normativa.
- **Invariantes:** a lista dos sete, a máquina de transições, o alcance por objeto, a tabela de
  tradução e o recorte da conformidade **permanecem íntegros** — a `DP-G` mudou quem produz o valor,
  não quais valores existem nem quando se transita. Nenhuma outra frase dos decision records é
  tocada; nenhuma tarefa é reaberta; nenhum artefato fora dos dois arquivos-alvo é editado.
- **Cuidado:** a residência única é o **único** lugar onde a regra é enunciada para o kit — não
  recopiar a correção em nenhum outro artefato, que aponta e não repete. `redacao-doc` não se aplica
  a decision record (classe registro), mas se aplica à skill.
- **Verificação:** bateria do §3; Grep por `único papel que o escreve|uma escrita do` no plano e na
  skill com resultado vazio; Grep por `DP-G` nos dois arquivos com pelo menos uma ocorrência cada.
- **Pronto quando:** nenhuma das quatro superfícies afirma que o `scrum-master` é o único a escrever
  `status`, e as quatro apontam para a `DP-G` como fonte da fronteira.

### T29 — Artefato `tarefa`: definição, autores e canal [Opus · classe redacao · teto 30]
- **Dossiê fechado por:** `DP-H` (§13, item 1) e **`DP-K` (§14, item 3 e §14.5)**. **Não delegável
  antes da `T21b`** — a definição descreve o canal por onde o loop já escrito conversa, e reescrever o
  loop depois custaria a mesma edição duas vezes. *(Dossiê reescrito na rodada de 2026-08-11 pela
  `DP-K`: o dono respondeu a pergunta que forçava a escalada, e o ramo de escalada por residência
  saiu.)*
- **Objetivo:** a pergunta "o que é uma tarefa" voltou três vezes e vinha sendo respondida por
  remendo. Esta tarefa **fecha a decisão `DP-I`**. **Boa parte já está pré-decidida pelo dono**
  (`DP-K` §14.2 item 3): das cinco perguntas abaixo, **três são transcrição** — a `T29` as escreve a
  partir do enunciado ratificado e **não delibera** sobre elas. O que **sobra decidir** são as
  perguntas **2** e **3**.
- **Insumo fechado (não se reabre, não se reinterpreta)** — a hierarquia dos quatro artefatos
  canônicos da `DP-K`: **plano** (materialização de um objetivo com sua implementação; antecede todas
  as tarefas, e toda tarefa deriva dele), **tarefa** (escopo localizado do plano numa unidade de
  execução com contexto coeso e finalidade granular; artefato canônico de comunicação **entre os
  agentes**; fonte da verdade da tarefa **em execução**), **laudo** (comunicação de uma revisão
  realizada; **efêmero**, existe só enquanto a tarefa está em execução; move para `done` ou devolve
  para `in-progress`) e **RDO** (comunicação do projeto **com o dono**; documento da verdade da
  **entrega**; pressupõe tarefa finalizada). **A tarefa não substitui nenhum dos outros três.**
- **Arquivos-alvo:** `docs/plans/P-0734-execucao-autonoma.md` — uma seção nova `### DP-I`, dentro de
  `## Dossiês fechados por decisão`. **Nenhum artefato publicado é tocado aqui.**
- **Conteúdo — cinco perguntas, três transcritas e duas decididas:**
  1. **Definição — transcrição.** O que o artefato é, na formulação do dono: escopo localizado do
     plano, unidade de execução com contexto coeso e finalidade granular, canal canônico entre os
     agentes e fonte da verdade da tarefa em execução. Nada a deliberar.
  2. **Autores e escrita — a decidir.** O que cada um dos três escreve nele, dentro das fronteiras já
     ratificadas: `DP-G` (autoria × materialização do `status`), `DP-D`/`DA-6` (juízo é do `reviewer`,
     calculado, nunca narrado) e o consumo medido, que é do `scrum-master`.
  3. **Conteúdo obrigatório — a decidir.** Quais campos o artefato carrega e de quem é cada um — em
     particular **onde o `status` da tarefa é materialmente gravado**, que é o que a `T26` transcreve
     depois. É a pergunta que a `DP-H` §13.2 transferiu para cá.
  4. **Mapeamento sobre o material existente — transcrição.** Dossiê no plano (`DP-C`), laudo (`T18`),
     RDO (`T19`) e linha do diário, encaixados na hierarquia do insumo fechado: **nenhuma residência
     se move**, e a `DP-I` apenas declara qual material **materializa** o artefato `tarefa` hoje e
     como cada um dos outros três se relaciona com ele.
  5. **Ciclo de vida — transcrição.** Nasce do plano, vive enquanto a tarefa não é terminal, e termina
     com ela; o laudo é efêmero dentro desse intervalo e o RDO nasce no fechamento. A `T29` transcreve
     e apenas **casa** isso com a máquina de estados da `DP-F`, sem alterá-la.
- **Invariantes:** a decisão é **incremental sobre o já ratificado** — não revoga `DP-C`, `DP-D`,
  `DP-E`, `DP-F`, `DP-G`, `DP-H` nem `DP-K`, e não move a residência única do `status`; **nenhuma
  residência de artefato se move** (o dono já decidiu que a `tarefa` não substitui plano, laudo nem
  RDO) — proposta de mover residência que apareça no desenho é **achado tiquetado**, não decisão desta
  tarefa e não pergunta nova ao dono. Nenhuma tarefa nova é autorada aqui — a materialização é
  autorada pela rodada de replanejamento que consumir a ratificação. `redacao-doc` não se aplica a
  decision record (classe registro).
- **Cuidado:** o plano é doc grande — entrar por Grep de âncora, nunca Read integral; `DP-C` (esquema
  do cabeçalho), `DP-G` e `DP-K` §14.2 são leitura obrigatória e ficam **intocadas**; *inspetor* e
  *revisor* não entram no texto (o termo único é `reviewer`, `DP-K` item 2).
- **Verificação:** bateria do §3; a seção `### DP-I` responde às cinco perguntas — as três de
  transcrição fiéis ao enunciado da `DP-K`, as duas de decisão com recomendação explícita — sem bloco
  a preencher e sem pergunta pendente ao dono além das duas; Grep por `DP-I` no plano com pelo menos
  uma ocorrência; nenhum arquivo fora do plano no diff.
- **Pronto quando:** a `DP-I` está escrita como proposta completa e **para** para ratificação
  **apenas das perguntas 2 e 3** — as outras três já vieram decididas e são registradas como
  transcrição, não como proposta. Nada é materializado antes do aceite; a ratificação continua em lote
  com a `DP-J`, para que o round-trip do dono seja **um**.

### T30 — Utilidade: o que o `scrum-master` colhe do laudo e o que ele descarta [Opus · classe redacao · teto 30]
- **Dossiê fechado por:** `DP-H` (§13, item 3) e **`DP-K` (§14.4)**. **Não delegável antes da `T19`** —
  o `pacote` que o `close` consome é o piso sobre o qual o critério opera.
- **Insumo fechado (`DP-K`):** o laudo é **efêmero por definição do dono** — existe só enquanto a
  tarefa está em execução e morre no consumo, **qualquer que seja o desdobramento**: fechamento,
  devolução para `in-progress` ou escalada. Logo o critério de utilidade vale nos **três** ramos, e
  não só no fechamento: o que a reexecução precisa saber viaja nas **diretivas atualizadas** que o
  `scrum-master` extraiu (`T21b`, `A6`), nunca por releitura do laudo.
- **Objetivo:** fechar a decisão **`DP-J`** — o critério pelo qual o `scrum-master` colhe do laudo o
  que é insumo do desdobramento e **descarta o resto**. É a resposta que os achados do §9 adiaram
  ("a definição de informações úteis não se resolve aqui"). Também **decide e para**.
- **Arquivos-alvo:** `docs/plans/P-0734-execucao-autonoma.md` — uma seção nova `### DP-J`, dentro de
  `## Dossiês fechados por decisão`. **Nenhum artefato publicado é tocado aqui.**
- **Conteúdo, em quatro frentes:**
  - **(a) O critério.** O que qualifica uma informação do laudo como útil: ela **decide** algo no
    desdobramento, ou o RDO **precisa** dela para ser registro suficiente da tarefa. O que não faz
    nem uma coisa nem outra é poluição de contexto e morre com o laudo.
  - **(b) Aplicação campo a campo** ao laudo que a `T18` emite: cada campo é classificado em (i)
    entra no `pacote` (obrigatório, `DP-H` item 4), (ii) é consumido no desdobramento e morre, (iii)
    não deveria existir. Campo sem veredito é dossiê não cumprido.
  - **(c) O campo opcional "Lições aprendidas na tarefa"**, encomendado pelo dono nos achados do §9 —
    recomendação sobre o **processo e a tarefa em si, nunca sobre o entregável**: existe? em qual
    documento? quem escreve? A `DP-J` responde as três. **Insumo do dono de 2026-08-11 (§15):** o
    campo **existe** e recebe uma segunda carga — é ele que transporta consumo e sinal de teto de uma
    tarefa à seguinte, até o fecho do plano. A `DP-J` continua respondendo residência e autoria; o que
    ela não pode mais decidir é a **não-existência** do campo.
  - **(d) Efeito declarado.** Se o critério implicar reter algo **além** do `pacote`, a mudança é
    **autorada como card novo** pela rodada que consumir a ratificação. A `T30` não materializa, não
    edita `rdo.py`, não edita o template e **não reabre a `T19`**.
- **Invariantes:** o `pacote` da `DP-H` item 4 é **piso, não teto** — o critério pode acrescentar,
  jamais remover a suficiência de invocar o `close` sem falha; pesos, faixas e dimensões da rubrica
  não mudam (são da `T5`); o RDO continua **sem ponteiro** para o laudo em qualquer hipótese, porque
  o laudo é apagado; o RDO do projeto tem mecânica própria e está fora desta conciliação
  (`DP-H` §12.1); nenhum arquivo fora do plano é editado.
- **Cuidado:** `docs/RUBRICA_DE_REVISAO.md` e `.claude/tools/rdo_template.md` são **leitura**, não
  alvo. Utilidade é critério de **retenção**, não de qualidade da entrega — não confundir com as sete
  dimensões da rubrica.
- **Verificação:** bateria do §3; a `DP-J` classifica **todos** os campos do laudo vigente, sem campo
  sem destino; a pergunta (c) tem resposta sim/não com residência declarada; Grep por `DP-J` no plano
  com pelo menos uma ocorrência; diff restrito ao plano.
- **Pronto quando:** existe um critério reexecutável de utilidade, cada campo do laudo tem destino
  declarado, o campo "Lições aprendidas" tem resposta com residência, e a decisão está **parada**
  para ratificação do dono.

### T31 — Conformidade: o resíduo de `pacote de retorno` nos artefatos publicados [Opus · classe redacao · teto 15]
- **Dossiê fechado por:** `DP-H` (§13, item 4). Delegável logo depois da `T20`.
- **Objetivo:** o objeto morto — o pacote de oito campos que o executor devolvia — sai do texto
  vigente dos artefatos publicados, e a palavra `pacote` passa a ter **uma** acepção no kit.
- **Arquivos-alvo** *(contagem medida em 2026-08-11)*: `GOVERNANCA.md` (**1** — §3, linha
  *Orquestração* da matriz de responsabilidades), `docs/RUBRICA_DE_REVISAO.md` (**6** — `:53`, `:73`,
  `:111`, `:126`, `:138`, `:252`) e `.claude/skills/diario-de-obras/SKILL.md` (**2** — `:72`, `:92`).
- **Conteúdo, arquivo a arquivo:**
  - **`GOVERNANCA.md`** — a orquestração passa a rotear **o retorno do executor** (a linha da
    gramática da `DP-G`) e **o laudo do `reviewer`**; o roteamento em si (aprovado segue, reprovado
    volta ao mesmo escopo, escalado sobe ao dono) **não muda**.
  - **`docs/RUBRICA_DE_REVISAO.md`** — onde a *fonte da evidência* cita o pacote, ela passa a citar
    **o dossiê de evidência de `review_evidence.py` e o diff**, que é onde o `D2` realocou arquivos
    tocados, desvios e verificação; a pendência de arquitetura ou requisito sobe pelo `--escalar` do
    laudo, não por campo de pacote.
  - **`.claude/skills/diario-de-obras/SKILL.md`** — as duas linhas (o estado `review` e a transição
    `in-progress` → `review`) passam a dizer que o executor devolve **a linha de retorno** da `DP-G`.
- **Invariantes:** **nenhuma regra muda de efeito — só o objeto citado**; pesos, faixas e dimensões
  da rubrica não mudam; a lista de estados, a máquina de transições e o alcance por objeto ficam
  intocados; a palavra `pacote` só sobrevive na acepção da `DP-H` item 4 e, onde sobreviver, aparece
  **qualificada** ("o `pacote` do laudo"); nada de novo é enunciado em lugar nenhum.
- **Cuidado:** `GOVERNANCA.md` é doc grande — entrar por `docs/DOC_MAP.md` e Grep de âncora, nunca
  Read integral; a residência única é normativa para o kit inteiro, então a correção mora lá e não se
  recopia; `redacao-doc` se aplica aos três arquivos; **não confundir com a `T26`**, que é vocabulário
  de `status` e passa depois nos dois primeiros, **nem com a `T33`**, que é vocabulário de papel
  (`revisor` → `reviewer`) e não toca nenhum destes três arquivos.
- **Verificação:** bateria do §3; Grep por `pacote de retorno` nos três arquivos com resultado
  **vazio**; Grep por `pacote` nos três com cada sobrevivente justificado no registro da tarefa como
  a acepção da `DP-H`.
- **Pronto quando:** nenhum artefato publicado descreve pacote devolvido pelo executor, e o kit usa a
  palavra numa acepção só.

### T32 — Doutrina: o desempate do framework escala ao dono [Opus · classe redacao · teto 15]
- **Dossiê fechado por:** `DP-K` (§14.2, item 1). **Delegável a qualquer momento** — não depende de
  nenhuma outra tarefa da fila e nenhuma depende dela.
- **Objetivo:** o buraco que o `§12.1` e a `DP-H` (§13.2) declararam explicitamente **não decidido** —
  o critério de desempate do framework em si — foi decidido pelo dono e ganha residência em artefato
  publicado: **ambiguidade no framework escala ao dono**.
- **Arquivos-alvo:** `GOVERNANCA.md`, seção **§3.1 — Residência e precedência da doutrina**, bloco
  **"Precedência, quando duas superfícies colidem"** (hoje com duas regras numeradas, seguidas do
  parágrafo "Colisão não se resolve com as duas cópias vivas…"). **Nenhum outro arquivo é tocado.**
- **Conteúdo — uma regra nova e nada mais:** entra a **regra 3**, depois de "Empate → versionado vence
  não-versionado": exauridas as regras 1 e 2, **a ambiguidade não se resolve embaixo** — nem por
  palpite do agente, nem por antiguidade, nem por recência. Ela **escala ao dono**, que é o desempate
  do framework. Duas frases de alcance, na mesma regra: (a) a **regra de recência** é de
  desenvolvimento do framework, vale dentro dos planos e **não** é critério de desempate de doutrina
  publicada; (b) escalar é **parar e perguntar**, não escolher e informar — é a mesma rota que o
  executor já tem (Regra 8 do CLAUDE.md global, regra `A3` da `DP-B`) e que o laudo `escalar` já dá à
  máquina de estados.
- **Invariantes:** **nenhuma seção nova** — §3.1 já é a superfície que decide colisão de doutrina, e o
  teste de residência das quatro perguntas **não muda**; as regras 1 e 2 ficam **intocadas**, e o
  parágrafo "Colisão não se resolve com as duas cópias vivas…" permanece onde está; nada da mecânica
  do `P-0734` (laudo, RDO, `status`, `pacote`) entra aqui — a regra é do framework, não do loop; a
  palavra *recência* aparece só para **negar** que ela seja desempate publicado (`DP-H` item 2).
- **Cuidado:** `GOVERNANCA.md` é doc grande — entrar por `docs/DOC_MAP.md` e Grep de âncora, nunca
  Read integral; `redacao-doc` se aplica; a `T31` e a `T26` também passam neste arquivo, em **âncoras
  diferentes** (§3, matriz de responsabilidades, e vocabulário de `status`) — não tocar o que é delas.
- **Verificação:** bateria do §3; Grep por `escala` na §3.1 com a regra 3 presente; o bloco de
  precedência tem **três** regras numeradas e nenhuma outra mudança no arquivo (diff de um só bloco).
- **Pronto quando:** o `GOVERNANCA.md` diz, em artefato publicado, o que o framework faz diante de
  ambiguidade que a precedência não resolve — e nenhum agente precisa inventar critério.

### T33 — Conformidade: `reviewer` nas linhas espelhadas e no resíduo fora do loop [Opus · classe redacao · teto 15]
- **Dossiê fechado por:** `DP-K` (§14.2, item 2). **Não delegável antes da `T21b`** — a `T21a` e a
  `T21b` reescrevem as 11 ocorrências do **corpo** do `SKILL.md` do `scrum-master`; esta tarefa fecha
  o que sobra, e rodar antes duplicaria trabalho e correria risco de regressão.
- **Objetivo:** `reviewer` passa a ser o **termo único** no texto vivo do kit e dos artefatos
  publicados. O que resta depois da `T21a`/`T21b` são **linhas espelhadas** (que só mudam em conjunto,
  sob pena de quebrar a paridade) e duas ocorrências fora do loop.
- **Arquivos-alvo e ocorrências** *(medidas em 2026-08-11, case-insensitive — **remedir na entrada**,
  porque a `T19` reescreve `tests/test_rdo.py` e a `T21a`/`T21b` reescrevem o corpo do `SKILL.md`)*:
  - `.claude/skills/scrum-master/SKILL.md` `:3` — `description` do frontmatter (**espelhada**).
  - `README.md` `:755` — espelho da `description` da skill (**muda com a de cima, verbatim**).
  - `.claude/README.md` `:57` — espelho da `description` da skill (**idem**).
  - `.claude/agents/pantonic-reviewer.md` `:3` — `description` do agente (**espelhada**) e `:8` —
    "Você é o **revisor**" (prosa de abertura).
  - `.claude/README.md` `:19` — espelho da `description` do agente (**muda com a `:3` acima**).
  - `tests/test_rdo.py` `:186` — docstring; **só a palavra**, nenhuma asserção e nenhum comportamento.
- **Conteúdo:** substituição **palavra por palavra**, `revisor`/`Revisor` → `reviewer`/`Reviewer`,
  preservando concordância ("o `reviewer`", "do `reviewer`"). As três cópias de cada `description`
  (skill e agente) mudam **no mesmo ato**, com o texto idêntico caractere a caractere — é o que
  `check-readme.ps1` verifica.
- **Invariantes:** **nenhuma regra muda de efeito — só o termo**; nada de novo é enunciado; nenhum
  campo, tabela, peso ou passo é tocado; **registro não se toca** (`docs/DIARIO_DE_OBRAS.md`,
  `docs/DIARIO_HISTORICO.md`, `docs/RDO/`, `docs/telemetria.tsv` ficam como estão, `DP-K` §14.2); o
  plano é desenvolvimento e **não** é varrido; `docs/benchmark/BM-03-fission-ai-openspec.md:26` fica —
  é o *Revisor* do **OpenSpec**, papel de framework externo.
- **Cuidado:** o corpo do `SKILL.md` do `scrum-master` já foi corrigido pela `T21a`/`T21b` — se ainda
  houver ocorrência lá, corrigir e **registrar como regressão**, não como escopo novo; `tests/` só
  aceita mudança de docstring nesta tarefa, e qualquer outra alteração é desvio de dossiê.
- **Verificação:** bateria do §3, com `check-readme.ps1` em **exit 0** (paridade dos espelhos) e
  `python -m pytest tests -q` verde; Grep case-insensitive por `revisor` em `.claude/`, `README.md` e
  `tests/` com resultado **vazio**.
- **Pronto quando:** o kit e os artefatos publicados usam **um** termo para o papel, os três espelhos
  de cada `description` estão idênticos, e o registro histórico permanece intocado.

### T34 — Doutrina: uso e teto são medida agregada, não porteiro de tarefa [CANCELADA — absorvida pelo desdobramento da `T17`, item 4]
- **Cancelada em 2026-08-12, por decisão do dono.** A matéria de uso e teto se revê **inteira e em
  plano próprio**, aberto depois que este fechar: formar a `DP-L` aqui decidiria agora o que aquele
  plano revê por inteiro. Nenhuma `DP-L` é formada neste plano, a `T34` sai da fila (§5) e a
  ratificação em lote fica com `DP-I` e `DP-J`. O regime interino do §3 item 5 — teto é alarme, nunca
  bloqueio — **vigora até a decisão do plano seguinte**.
- **O corpo abaixo permanece como material absorvido**, não como tarefa a executar: o insumo do dono
  (§15), a medição obrigatória de três números e o conteúdo previsto da decisão são o insumo de
  abertura do plano novo, e a `T17` item 4 aponta para cá. Nada disto se executa dentro do `P-0734`.
- **Dossiê fechado por:** insumo do dono de 2026-08-11 (**§15**), que fixa o enunciado, o portador e a
  pergunta a fechar.
- **Objetivo:** fechar a decisão **`DP-L`** — o que o framework faz com número de uso e com teto. O
  enunciado do dono é que a medida é **agregada**, lida em conjunto no fecho do plano, e não um
  porteiro que decide tarefa a tarefa. A tarefa também responde, **com a série medida**, se o controle
  por tarefa paga o que custa.
- **Insumo fechado (dono, 2026-08-11 — §15):**
  1. a questão é de **conceito de framework**, não de desenvolvimento deste projeto: a residência
     final é artefato publicado, e este plano é só onde a decisão se forma;
  2. uso e teto são medidas de **agregado**, não de indivíduo — avaliar tarefa a tarefa mede ruído;
  3. o portador entre tarefas é o card **"Lições aprendidas na tarefa"**, que carrega metainformação
     **da tarefa e não do entregável** (existência confirmada pelo mesmo insumo; residência e autoria
     vêm da `DP-J`, `T30`), acumulando até o **fecho do plano**;
  4. a hipótese do dono é que o controle vigente é **mais poluição do que economia efetiva** — é essa
     conclusão que a tarefa fecha, e ela é **confrontada com a série, nunca assumida**;
  5. até a posição final, o teto **não bloqueia nem impede** tarefa (§3, item 5).
- **Arquivos-alvo:** `docs/plans/P-0734-execucao-autonoma.md` — uma seção nova `### DP-L`, dentro de
  `## Dossiês fechados por decisão`. **Nenhum artefato publicado é tocado**: a materialização em
  `GOVERNANCA.md` §3 é autorada como card novo pela rodada que consumir a ratificação, mesmo padrão da
  `T30` item (d).
- **Medição obrigatória, antes de decidir** — sobre `docs/telemetria.tsv` (fonte única do número) e as
  linhas `Consumo:` do diário e do histórico:
  - (a) quantas tarefas **por classe** cruzaram o teto declarado, e por quanto;
  - (b) em quantos cruzamentos a consequência que a doutrina prescreve ("estourar é sinal de
    decomposição errada — replanejar, não continuar") **de fato ocorreu**, e em quantos a tarefa
    apenas seguiu, parou incompleta ou empurrou o resto para o contexto seguinte;
  - (c) o custo do **próprio controle**: turnos gastos em declarar teto no dossiê, contar, anunciar a
    aproximação e relatar o estouro.
  Sem os três números a decisão é opinião, e o item 4 do insumo deixa de ser hipótese testada.
- **Conteúdo do `DP-L`:** o enunciado do agregado; o que substitui o porteiro por tarefa (alarme sem
  parada, nada, ou corte só quando o agregado do plano acusa); onde o número vive entre tarefas e quem
  o escreve; o que acontece com a tabela de classes de `GOVERNANCA.md` §3 — permanece como referência
  de calibração, encolhe ou sai; e o **veredito sobre a hipótese** do item 4, com a série citada.
- **Invariantes:** `docs/telemetria.tsv` continua **fonte única do número** e não é editado aqui;
  decidir não é materializar — a tabela de classes não é apagada nesta tarefa; a `DP-J` **não é
  reaberta**: o card é consumido como insumo, e se a `T30` lhe der residência diferente da esperada, a
  `DP-L` declara a dependência em vez de inventar a sua; nenhum arquivo fora deste plano é editado.
- **Cuidado:** agregado não é média — estouro concentrado numa classe é sinal, e o `DP-L` precisa
  dizer o que faz com ele; não confundir com a `T13`, que escolhe proxy de **ocupação de contexto**
  (janela), não de turno; o regime interino do §3 item 5 é do desenvolvimento deste plano e **não**
  entra em artefato publicado.
- **Verificação:** bateria do §3; os três números da medição presentes, cada um com a fonte citada;
  Grep por `DP-L` no plano com ao menos uma ocorrência; diff restrito ao plano.
- **Pronto quando:** existe enunciado reexecutável de uso e teto como medida agregada, com portador
  declarado, o veredito sobre a hipótese do dono apoiado na série, e a decisão **parada** para a
  ratificação em lote com `DP-I` e `DP-J`.

### T35 — Auditoria: a matriz de responsabilidades como autoridade exaustiva [Opus · classe investigacao · teto 30]
- **Dossiê fechado por:** `DP-M` (§16.2 item 1, §16.3 e §16.5). **Precondição da `T36`** — a golden
  rule transforma a matriz em autoridade exaustiva, e publicá-la sobre matriz incompleta põe todo
  papel vivo fora de conformidade no mesmo ato. **Não decide nada e não para.**
- **Objetivo:** medir a matriz de responsabilidades de `GOVERNANCA.md` §3 contra os papéis vivos do
  kit e **fechar por transcrição** toda lacuna cuja responsabilidade já está publicada no prompt do
  próprio papel.
- **Objeto da medida** *(medido em 2026-08-11 — re-derivar na entrada)*: a tabela `| Papel | Modelo |
  Responde por | Não faz |` em `GOVERNANCA.md:88-96`, hoje com **7 linhas** (dono/gerente,
  planejamento, orquestração, execução, revisão, coleta, auditoria).
- **Fontes a ler — leitura dirigida, nunca Read integral:** de cada arquivo, só o `description` do
  frontmatter e o bloco que declara o que ele faz e o que não faz (Grep de âncora `^## ` e leitura
  com `offset`/`limit`):
  - `.claude/agents/pantonic-planner.md`, `.claude/agents/pantonic-executor.md`,
    `.claude/agents/pantonic-reviewer.md`, `.claude/agents/pantonic-scout.md`,
    `.claude/agents/pantonic-auditor-arch.md`, `.claude/agents/pantonic-auditor-cleancode.md`,
    `.claude/agents/pantonic-benchmarker.md`, `.claude/agents/pantonic-fora-da-caixa.md`;
  - `.claude/skills/scrum-master/SKILL.md` (o papel de **orquestração** vive numa skill, não num
    agente — entra pela linha que já existe).
- **Lacunas já visíveis na medida de 2026-08-11** *(re-derivar, não copiar)*: `pantonic-benchmarker` e
  `pantonic-fora-da-caixa` **não têm papel correspondente** na matriz; `pantonic-auditor-arch` e
  `pantonic-auditor-cleancode` compartilham a linha *Auditoria*, que já nomeia os dois.
- **Ação, em três passos:**
  1. Montar a tabela **arquivo × linha da matriz**, uma linha por papel vivo.
  2. Classificar cada lacuna em **(a) transcrição** — a responsabilidade já está publicada no prompt
     do próprio papel e falta só na matriz — ou **(b) doutrina nova** — a responsabilidade não está
     escrita em lugar nenhum.
  3. Fechar as **(a)** na matriz, uma linha por papel, com o texto derivado do que o prompt já
     declara. As **(b)** viram **tíquete indexado** em `docs/DIARIO_DE_OBRAS.md` e sobem ao dono no
     handover.
- **Arquivos-alvo de escrita:** `GOVERNANCA.md` §3 — apenas a tabela da matriz;
  `docs/plans/P-0734-execucao-autonoma.md` — subseção nova `### 16.7 Auditoria de completude da
  matriz — resultado`, ao final do §16, com a tabela da medida e a classificação de cada lacuna;
  `docs/DIARIO_DE_OBRAS.md` — só se existir lacuna **(b)**, como tíquete novo na tabela de tíquetes.
- **Invariantes:** **a auditoria não cria responsabilidade** — o que não está publicado não entra na
  matriz; nenhuma proibição é podada aqui (é a `T37`) e a coluna *Não faz* **não** ganha proibição
  nova; o guardrail 15 **não** é escrito aqui (é a `T36`); `README.md`, `.claude/**` e
  `docs/RDO/**` não são tocados; nenhuma regra de modelo por fase muda.
- **Redação:** `.claude/skills/redacao-doc/SKILL.md` é normativa no que entra em `GOVERNANCA.md` — sem
  narrativa de proveniência e sem ID de tarefa ou de plano no corpo do arquivo publicado.
- **Cuidado:** `GOVERNANCA.md` é doc grande — entrar por `docs/DOC_MAP.md` e Grep de âncora
  (`^## 3\. Operações agênticas`), nunca Read integral; a matriz é tabela markdown de 4 colunas e a
  célula é longa: editar linha inteira, não fragmento; papel que existe só como skill não vira linha
  nova se a linha do papel já existir.
- **Verificação:** os quatro checks do §3 item 6 em exit 0; a tabela do `### 16.7` cobre **todos** os
  arquivos listados acima, cada um com veredito (coberto / lacuna (a) fechada / lacuna (b)
  escalada); contagem de linhas da matriz em `GOVERNANCA.md` re-derivada no fechamento (Grep
  `^\|\s\*\*` na âncora do §3, com o número antes e depois registrado).
- **Pronto quando:** existe medida completa dos papéis vivos contra a matriz, toda lacuna de
  transcrição está fechada nela e toda lacuna de doutrina nova está registrada como tíquete e
  escalada — de modo que a `T36` publique a regra sobre matriz completa.

### T36 — Doutrina: guardrail 15 (`G-SCOPE`) e o espelho em lockstep [Opus · classe redacao · teto 30]
- **Dossiê fechado por:** `DP-M` (§16.2, escolha 1). **Não delegável antes da `T35` `done`.**
  Transcreve decisão ratificada e **não para** para aceite.
- **Objetivo:** a golden rule entra na doutrina publicada como **guardrail 15**, a matriz do §3 passa
  a apontar para ela, e o espelho do README sobe para **15 linhas no mesmo ato**.
- **Arquivos-alvo (quatro, e só quatro):**
  1. `GOVERNANCA.md` §7 — item **15** novo, imediatamente **após** o item 14 e **antes** do parágrafo
     "Esses guardrails são materializados em cada projeto como:".
  2. `GOVERNANCA.md` §3 — o bullet "**Papéis não são intercambiáveis**" (`:103-104`) ganha o ponteiro
     para o §7 item 15, **sem reenunciar a regra**.
  3. `README.md` §10 "Os guardrails" (`:685`) — a linha `| 15 | … |` na tabela, o numeral de abertura
     ("Quatorze regras mínimas…" → "Quinze…", `:689`) e a contagem das formas de enforcement.
  4. `CHANGELOG.md` — **uma** linha sob `[Não lançado]`, no formato das linhas já existentes da seção.
- **Texto do item 15 — transcrição do enunciado do dono, a redigir assim:** `G-SCOPE` — **o agente se
  atém estritamente às suas responsabilidades declaradas; o que não está escrito é proibido**. A
  residência do escopo de cada papel é a **matriz de responsabilidades (§3)**, que é autoridade
  **exaustiva**: o que ela não declara, nenhum agente faz. Prompt de agente **não cria**
  responsabilidade por conta própria — descrever-se fazendo o que a matriz não declara é violação, não
  extensão. Proibição em prompt só se justifica quando restringe o exercício da **própria**
  responsabilidade declarada; a que apenas repete "não faça o que é de outro papel" é redundante e
  sai. *Enforcement:* instrução em todo arquivo de agente e em toda skill que carrega papel; gate de
  review sobre prompt novo ou alterado.
- **Linha do README (espelho, uma linha de tabela):** `| 15 | `G-SCOPE`: o agente se atém estritamente
  às responsabilidades declaradas na matriz de papéis — o que não está escrito é proibido | **Instrução
  de agente** + **gate de review** |`.
- **Contagem, que é o que o guarda mede:** `check-readme.ps1` compara **números, não texto** — linhas
  `| N |` da seção "Os guardrails" do README contra itens `^\d+\. \*\*` de `GOVERNANCA.md` §7, entre
  `## 7. Guardrails dos agentes` e `### 7.1` (`.claude/checks/check-readme.ps1:158-199`). Medido em
  2026-08-11: **14 × 14**; ao fim desta tarefa, **15 × 15**.
- **Prosa de contagem do README** (parágrafo "**Seis** regras falham como teste executável…", `:710`):
  **recontar as três famílias sobre a tabela depois da inserção** e escrever os números resultantes. O
  número recontado manda — essa prosa não é medida pelo guarda, e qualquer divergência do texto
  vigente entra no registro da tarefa como achado, nunca como doutrina nova.
- **Redação (`.claude/skills/redacao-doc/SKILL.md`, normativa aqui):** sem narrativa de proveniência e
  **sem ID de tarefa nem de plano no corpo** — `DP-M`, `P-0734` e `T36` **não** aparecem em
  `GOVERNANCA.md` nem no `README.md`; o item 15 se enuncia como regra vigente, não como decisão datada.
- **Invariantes:** nenhum dos 14 itens vigentes é reescrito; o §3 **aponta**, não recopia; o README é
  espelho e **nenhuma regra nasce lá**; nenhum prompt de agente ou skill é editado aqui (é a `T37`);
  `docs/RESIDENCIA_DOUTRINA.md` **não** é tocado — a regra não colide com doutrina global; congelamento
  pré-lançamento em vigor (`GOVERNANCA.md` §10): **sem bump** de `VERSION` nem de `.claude/KIT_VERSION`.
- **Cuidado:** `GOVERNANCA.md` e `README.md` são docs grandes — entrar por Grep de âncora
  (`^## 7\. Guardrails`, `^### 7\.1`, `^## \d+\. Os guardrails`), nunca Read integral; o marcador
  `### 7.1` é o fim da lista para o guarda: nada do item 15 pode cair depois dele.
- **Verificação:** os quatro checks do §3 item 6 em exit 0, com `pwsh .claude/checks/check-readme.ps1`
  imprimindo **`15 guardrail(s)`** na linha de OK; Grep `^15\. \*\*` em `GOVERNANCA.md` = 1 ocorrência;
  Grep `^\| 15 \|` em `README.md` = 1 ocorrência; Grep `DP-M|P-0734` em `GOVERNANCA.md` e `README.md`
  com resultado **vazio**.
- **Pronto quando:** a golden rule existe na doutrina publicada como item 15, a matriz aponta para ela,
  o espelho tem 15 linhas com o numeral e a contagem de formas coerentes, e o guarda passa.

### T37 — Conformidade: poda das proibições que a matriz passa a derivar [Opus · classe redacao · teto 15]
- **Dossiê fechado por:** `DP-M` (§16.3 e §16.4). **Não delegável antes da `T36` `done`** — sem a
  regra publicada, a proibição podada fica sem de onde derivar.
- **Objetivo:** os dois prompts que mais repetem fronteira de outro papel param de repeti-la. **Nenhuma
  regra perde efeito** — o que sai passa a valer pela matriz (§3) somada ao guardrail 15.
- **Critério aplicado (é do §16.4, não é julgamento do executor):** sobrevive a proibição que restringe
  o exercício da **própria** responsabilidade declarada; sai a que apenas repete que o papel não faz o
  que é **de outro**.
- **Arquivo-alvo 1 — `.claude/skills/scrum-master/SKILL.md`, bloco `## Proibições`** *(medido em
  2026-08-11 em `:273`; a `T33` já passou neste arquivo — **re-localizar o bloco na entrada**)*. Saem
  **quatro** bullets, nomeados pelo início e cada um com a célula da matriz que o produz:
  - "Não implementa. Nenhuma edição de código…" → linha **Execução** da matriz.
  - "Não julga entrega…" → linha **Revisão** ("o veredito é da revisão", que a própria linha
    *Orquestração* já repete).
  - "Não decide arquitetura nem requisito…" → linhas **Planejamento** e **Dono/gerente**.
  - "Não reescreve dossiê…" → linha **Planejamento**.
  **Permanecem:** "Não abre o RDO nem o laudo…" — **não se toca aqui**, é objeto da `T39` — e "Não
  despacha duas tarefas em paralelo, e não encerra a janela por percepção de contexto", que é fronteira
  interna do próprio loop.
- **Arquivo-alvo 2 — `.claude/agents/pantonic-reviewer.md`, bloco `## Proibições`** *(medido em
  2026-08-11 em `:83`)*. Saem **cinco** bullets:
  - "A única escrita permitida é o laudo…" → a matriz já diz, na linha **Revisão**, "escrita restrita
    ao caminho do laudo — independência imposta pela lista de ferramentas".
  - "Não corrige o que aponta…" → está literal na coluna *Não faz* da linha **Revisão**.
  - "Não replaneja e não decide rota…" → idem, mais a linha **Planejamento**.
  - "Não declara `status` de tarefa…" → linhas **Execução** e **Orquestração** (`DP-G`).
  - "Não julga mais de uma tarefa por contexto." → a linha **Revisão** já declara "julgar a entrega de
    **uma** tarefa".
  **Permanecem três**, porque restringem o exercício da própria responsabilidade: "Não marca `conforme`
  contra vermelho mecânico", "Não completa critério de pronto inverificável por conta própria" e "Não
  escreve percentual nem veredito".
- **Invariantes:** nada novo é enunciado nos dois arquivos; nenhum passo, tabela, campo, contador ou
  gatilho é tocado; o bloco `## Guardrails` do `scrum-master` fica **fora** desta tarefa; nenhum outro
  prompt do kit é podado aqui — proibição derivada encontrada em outro arquivo é **achado registrado**,
  não escopo (`DP-M` §16.5).
- **Cuidado:** contar os bullets de cada bloco **na entrada** e registrar o antes/depois; se um bullet
  já não existir, registrar o fato e seguir — **não** procurar substituto nem recriar a regra em outro
  lugar; nenhum dos dois arquivos ganha ponteiro explicativo para o guardrail 15 (o prompt não recopia
  doutrina).
- **Verificação:** os quatro checks do §3 item 6 em exit 0; Grep do início de cada um dos nove bullets
  removidos, nos dois arquivos, com resultado **vazio**; Grep "Não abre o RDO" no `scrum-master` ainda
  com **1** ocorrência (é a `T39` que a remove).
- **Pronto quando:** os dois blocos `## Proibições` só contêm fronteira interna do próprio papel, e
  nenhuma proibição do tipo "não faça o que é de outro papel" sobrevive nesses dois arquivos.

### T38 — Laudo mínimo: `--observacoes` sai do gerador [Sonnet · classe mecanica · teto 15]
- **Dossiê fechado por:** `DP-M` (§16.2, escolha 2). Mecanicamente independente da `T35`..`T37`, mas
  **precede a `T39`**: é esta remoção que dispensa a proibição do `TK-33` item 3.
- **Objetivo:** o laudo passa a ser **mínimo e suficiente** — só campo fechado ou calculado, mais a
  linha de pendência que o roteamento consome.
- **Arquivos-alvo (dois):**
  - `.claude/tools/rdo.py` — sai o argumento `--observacoes` (`:701`), sai a variável `observacoes`
    (`:479`) e sai a linha `**Observações:** {observacoes}` do corpo do laudo (`:491`). `cmd_laudo`
    fica com os cinco campos calculados mais a tabela de níveis.
  - `.claude/agents/pantonic-reviewer.md` — o bloco de comando do passo 6 (`:59-65`) perde
    `--observacoes "<texto>"`; a prosa vizinha que descreve os flags (`:67-72`) não cita mais
    observações. **Só isso neste arquivo** — o bloco `## Proibições` é da `T37`.
- **Risco assumido e já ratificado pelo dono:** marcação abaixo de `conforme` pode ficar **sem
  justificativa registrada**. **Não se cria campo substituto**, e `--escalar` continua sendo o único
  canal de pendência.
- **Invariantes:** `calcular_laudo` e o cálculo de percentual, veredito, bloqueante, recomendação e
  pendência **não mudam**; nenhum outro flag sai; destino do laudo e escrita atômica ficam como estão;
  `docs/RUBRICA_DE_REVISAO.md` **não** é tocado (medido em 2026-08-11: não cita o campo); nenhum
  documento de doutrina é editado nesta tarefa.
- **Cuidado:** medido em 2026-08-11, **nenhuma asserção em `tests/` cita `Observações` nem
  `--observacoes`**; se a suíte acusar, a asserção é atualizada **nesta mesma tarefa** — é o mesmo
  write-cluster e não amplia escopo.
- **Verificação:** os quatro checks do §3 item 6 em exit 0 (`python -m pytest` verde inclusive);
  `python .claude/checks/dead_code.py` em exit 0; Grep `observacoes|Observações` (case-insensitive) em
  `.claude/` com resultado **vazio**.
- **Pronto quando:** o gerador rejeita o flag, o laudo emitido não tem prosa livre além da linha de
  pendência, e a suíte está verde.

### T39 — `TK-33`: passos 7 e 8, a acepção de `pacote` em `A2` e a proibição que a `DP-M` dispensa [Opus · classe redacao · teto 15]
- **Dossiê fechado por:** `DP-M` (§16.4) e o `TK-33` de `docs/DIARIO_DE_OBRAS.md`. **Não delegável
  antes da `T38` `done`** — o item 3 só fecha depois de `Observações` sair do laudo.
- **Arquivo-alvo (único):** `.claude/skills/scrum-master/SKILL.md` *(linhas medidas em 2026-08-11; a
  `T37` já passou no bloco de proibições — **re-localizar por âncora**, não por número)*.
- **Conteúdo, quatro pontos:**
  1. **Passo 8, gatilho (`:153`)** — "passo 5 concluído (regras `A1`..`A5`)" passa a ler `A1`..`A4`:
     `A5` não existe, e as regras avaliadas depois do passo 5 são `A1`, `A2`, `A3a`, `A3b` e `A4`.
  2. **Passo 7 — *Leitura do veredito* (`:140-149`)** — passa a colher também a **recomendação**, que
     `A6`, `A8`, `A9` e `B1` leem e que nenhum passo colhia. Fechado pelo §16.4: a recomendação é campo
     **fechado** do laudo e o passo 7 a lê **de lá**; o retorno de duas linhas do `reviewer` **não
     muda** e nenhum campo novo é criado. A saída do passo passa a ser a tripla (`veredito`,
     `bloqueante`, `recomendação`), e o roteamento do passo 8 a recebe assim.
  3. **Regra `A2` (`:215`)** — "pacote ausente ou inválido" passa a dizer **retorno** ausente ou
     inválido: `A2` julga o retorno do **executor**, e `pacote` passou a nomear os cinco campos **do
     laudo** (`DP-H`, item 4). Só o termo muda; a condição e o encaminhamento ficam idênticos.
  4. **Bloco `## Proibições`** — sai o bullet "Não abre o RDO nem o laudo…", **sem fronteira
     substituta**: com `Observações` fora (`T38`), o laudo só tem campo fechado ou calculado, e os
     passos 7 e 9 o leem por desenho.
- **Invariantes:** nenhuma tabela de roteamento muda de **efeito** — só `A2` muda de termo; nenhum
  contador, teto ou gatilho novo; o passo 9 fica exatamente como está; **nada é acrescentado ao retorno
  do `reviewer`**; os demais bullets de `## Proibições` ficam como a `T37` os deixou; nenhum outro
  arquivo do kit é editado.
- **Registro:** a linha do `TK-33` na tabela de tíquetes de `docs/DIARIO_DE_OBRAS.md` vai a **`done`**
  no fechamento desta tarefa, com os três itens nomeados.
- **Verificação:** os quatro checks do §3 item 6 em exit 0; Grep `A5` no arquivo com **exatamente 1**
  ocorrência — a de `:206-207`, que **narra a queda** de `A5` como fonte normativa e **fica**; Grep
  `pacote ausente` **vazio**; Grep `Não abre o RDO` **vazio**; Grep `recomenda` dentro do bloco do
  passo 7 com ao menos **1** ocorrência.
- **Pronto quando:** os três itens do `TK-33` estão fechados no arquivo, o vocabulário de `A2` está
  reconciliado, e o tíquete está `done` no diário.

### T40 — Alinhamento do executor: o prompt para de escrever e passa a sinalizar [Opus · classe redacao · teto 15]
- **Dossiê fechado por:** `DP-N` (§17), ratificada pelo dono em 2026-08-12. Fecha o `TK-35`.
- **Objetivo:** o prompt do executor descreve o papel que a `DP-N` fixou — entregar código
  funcional e conforme, e sinalizar. Nada de escrita no diário, nada de registro da própria entrega.
- **Arquivo-alvo (único):** `.claude/agents/pantonic-executor.md` *(âncoras medidas em 2026-08-12;
  o arquivo foi tocado pela `T24`, que trocou só termos)*.
- **Conteúdo, sete pontos:**
  1. **Abertura (`:7-8`)** — acrescentar a responsabilidade que o dono enunciou: entregar o código
     **funcional e conforme com as regras do projeto** (testes passando, golden rules cumpridas);
     **aferir a aceitação da entrega não é dele** — é do `reviewer`.
  2. **Fato estável de economia de turnos (`:20-25`)** — "reporta a recomendação no handover" e
     "reportar no handover, não só continuar" passam a apontar o **sinal ao `scrum-master`**; o
     número de orçamento (`~≤40`) **não é objeto desta tarefa** (é do `TK-04`).
  3. **Fato estável do `Consumo:` (`:26-28`)** — **sai inteiro**: o executor não grava placeholder
     nem número, porque não escreve no diário. Quem orquestra grava o consumo do dado medido.
  4. **Achado fora de escopo (`:29-30`)** — deixa de ser "tíquete indexado no diário na mesma
     sessão" e passa a ser **uma linha do sinal**; quem indexa o tíquete é o `scrum-master`.
  5. **Passo 2 (`:48-49`)** — sai "marque `in-progress`": materializar `status` é do `scrum-master`
     em qualquer estado (`DP-G`). O passo fica só em localizar a própria tarefa pelo índice.
  6. **Passo 4 (`:53-56`)** — "marque `blocked` no diário com a razão e faça handover" vira
     **sinalizar `blocked` com a razão tipada** (`dependencia` ou `premissa`, `DP-G`) e encerrar. A
     cláusula "o handover declara os chamadores de produção de cada símbolo novo" **sai**: a
     alcançabilidade é medida por `.claude/checks/dead_code.py` e julgada na dimensão `guardas` do
     laudo — a regra `G-DEADCODE` continua valendo para o executor, só não tem mais declaração em
     prosa.
  7. **Passos 5 e 6 (`:57-61`)** — o passo 5 é reenunciado como **responsabilidade de entrega**
     (suíte da área + conformance + piso; a entrega sai tecnicamente correta), e o passo 6 deixa de
     invocar a skill `handover`, de atualizar o diário e de registrar o que foi feito: **sinaliza
     `review` e encerra**.
- **Invariantes:** nenhuma regra de execução muda de efeito — TDD, escopo estrito, `G-EXECREADY`,
  `G-PLANFIDELITY`, regra de dependência, ACL, higiene de busca e a proibição de iniciar outra tarefa
  no mesmo contexto ficam como estão; o arquivo **não** ganha lista de estados (aponta para a
  residência única quando precisar); o `frontmatter` não muda; nada do `reviewer` ou do
  `scrum-master` é reenunciado aqui.
- **Cuidado:** se o `description` do frontmatter mudar, `.claude/README.md` precisa ser regenerado
  (`pwsh .claude/checks/kit_check.ps1 -Mode generate`) — por isso ele não muda.
- **Verificação:** os quatro checks do §3 item 6 em exit 0; Grep `handover` no arquivo → **vazio**;
  Grep `diário` → só a ocorrência do passo 2 (localizar a tarefa pelo índice).
- **Pronto quando:** o prompt não manda o executor escrever em lugar nenhum, a responsabilidade de
  entrega técnica está enunciada, e o `TK-35` está `done` no diário.

### T41 — As superfícies que descrevem o executor [Opus · classe redacao · teto 30]
- **Dossiê fechado por:** `DP-N` (§17). **Não delegável antes da `T40` `done`** — a doutrina
  descreve o prompt, e descrever antes de ele mudar inverte a ordem.
- **Objetivo:** doutrina, espelho e a skill que delega param de mandar o executor escrever.
- **Arquivos-alvo e âncoras** *(medidas em 2026-08-12)*:
  1. `GOVERNANCA.md:93` — matriz de responsabilidades §3, linha **Execução**: "registrar o resultado
     no diário de obras e fazer handover" sai da coluna *Responde por*, que passa a declarar a
     entrega tecnicamente correta e o **sinal** (`review`/`blocked`); a coluna *Não faz* recebe que
     ele não escreve no diário, não registra o resultado da própria entrega e não afere a própria
     aceitação. **A matriz é autoridade exaustiva** (`DP-M`, guardrail 15) — é ela que produz a
     proibição, sem bullet novo em prompt nenhum.
  2. `GOVERNANCA.md:301-302` — §4.2: "O executor grava no diário o placeholder literal
     `Consumo: (preenchido pelo orquestrador via notificação)`" passa a dizer que **quem orquestra**
     grava o registro do consumo, a partir do dado medido da notificação. O princípio — telemetria
     vem da medição, nunca do auto-relato — **não muda**, e o desvio medido de 11-44% continua sendo
     a razão afirmada inline.
  3. `README.md:833` e `README.md:928` — espelho das duas superfícies acima, em lockstep.
  4. `.claude/skills/proximo-passo/SKILL.md:150-155` — "O dossiê instrui o executor a gravar no
     diário o placeholder literal … — ou a não editar o diário (orquestrador escreve o bullet
     inteiro)" perde a primeira alternativa: resta a segunda, que passa a ser a única forma.
  5. `.claude/skills/guardrails-check/SKILL.md:8` — "obrigatório antes de `review`/`done`" passa a
     "antes de sinalizar `review`": o executor nunca sinaliza `done`.
- **Invariantes:** nenhum princípio muda — só o portador do ato; paridade estrutural do espelho
  preservada; nenhuma doutrina nova nasce no README; nenhuma lista de estados é recopiada.
- **Cuidado — fora desta tarefa, por decisão do dono (`TK-36`):** o §9 do `README.md` (*Handover e
  uma tarefa por contexto*) inteiro, `GOVERNANCA.md:333`/`:338`/`:342` (§4), `:240` (cerimônias),
  o *enforcement* dos itens 8 e 9 do §7 ("gate de review no handover") e as skills `handover` e
  `proximo-passo` além da cláusula nomeada acima. Reorganizar a passagem de bastão é o `TK-36`;
  esta tarefa só tira do executor o que a `DP-N` tirou.
- **Verificação:** os quatro checks do §3 item 6 em exit 0, com `check-readme.ps1` cobrindo o
  espelho; Grep `executor grava` em `GOVERNANCA.md` e `README.md` → **vazio**; Grep `handover` na
  linha 93 de `GOVERNANCA.md` → **vazio**.
- **Pronto quando:** nenhuma das cinco superfícies atribui escrita ao executor, e o que sobrou de
  `handover` no repositório está inteiramente dentro do recorte do `TK-36`.

### T42 — Doutrina: a resposta na descoberta de não-conformidade de escopo [Opus · classe redacao · teto 15]
- **Dossiê fechado por:** `DP-O` (§18), ratificada pelo dono em 2026-08-12. **Precede a `T43` e a
  `T44`** — é a régua que as duas aplicam.
- **Objetivo:** o guardrail 15 passa a dizer o que se faz quando a violação é **encontrada em
  artefato existente**, e não só o que se barra em prompt novo.
- **Arquivos-alvo e âncoras** *(medidas em 2026-08-12)*: `GOVERNANCA.md:585-592` (§7, item 15) e
  `README.md:709` (espelho §10, linha `| 15 |` da tabela de guardrails).
- **Conteúdo:** o item 15 ganha duas cláusulas, e **nenhum enunciado existente muda**:
  1. **Resposta na descoberta.** Artefato do framework que atribui a um agente ato **não endossado**
     pela matriz — ou que carrega papel que a matriz **sequer cita** — é **não-conformidade grave**:
     para-se e regulariza, em vez de enfileirar como dívida.
  2. **A lacuna oposta não se resolve no ato.** Quando o ato atribuído é **real e necessário** mas a
     matriz não o declara, a falta é **da matriz**, e criar a responsabilidade no prompt é
     exatamente a violação: registra-se e **sobe ao dono** (mesma regra da `DP-M`, §16.5).
  O *enforcement* ganha a **varredura** ao lado do gate de prompt novo ou alterado.
- **Invariantes:** o enunciado do guardrail não muda; **nenhum guardrail novo** — a contagem
  permanece **15 × 15** e o espelho fica em lockstep; nenhuma responsabilidade nova nasce aqui.
- **Verificação:** os quatro checks do §3 item 6 em exit 0, com `check-readme.ps1` reportando
  **15 guardrail(s)**.
- **Pronto quando:** o item 15 declara a resposta na descoberta e a rota da lacuna, e o espelho as
  reproduz sem mudar a contagem.

### T43 — Sanitização: o kit executável contra a matriz [Opus · classe redacao · teto 40]
- **Dossiê fechado por:** `DP-O` (§18). **Não delegável antes da `T42`** (a régua) **nem da `T41`**
  (as superfícies do executor já nomeadas, para não colidirem).
- **Objetivo:** nenhum prompt do kit atribui a um agente ato que a matriz de responsabilidades
  (`GOVERNANCA.md` §3) não endossa.
- **Universo fechado** *(medido em 2026-08-12)*: os **8** arquivos de `.claude/agents/` e os **11**
  `SKILL.md` de `.claude/skills/`. Nada fora disso.
- **Método prescrito** (não improvisar): **uma** coleta programática primeiro — varrer o universo
  pelos verbos atributivos (`atualiz`, `registr`, `escrev`, `grav`, `decid`, `marc`, `fecha`,
  `julg`, `aprova`, `delega`, `invoca`, `emite`) com saída para arquivo no scratchpad —, depois
  leitura dirigida só das regiões que a coleta apontou. Doc > 500 linhas entra por `docs/DOC_MAP.md`,
  nunca por Read integral.
- **Classificação por ocorrência, e só estas três:**
  - **(a) endossado** pela linha do papel na matriz → fica como está;
  - **(b) não endossado e dispensável** → sai, ou é reescrito para o que a matriz declara;
  - **(c) não endossado, mas o ato é real e necessário** → **lacuna da matriz**: **não se decide
    aqui**. Vira linha do relatório **e tíquete indexado** no diário, e sobe ao dono.
- **Entregável:** as edições da classe (b) **mais** o relatório
  `docs/audits/CONFORMIDADE_MATRIZ_2026-08-12.md`, uma linha por ocorrência, com arquivo, linha,
  papel, o que o texto atribui, veredito (a/b/c) e ação.
- **Invariantes:** **nenhuma responsabilidade nova** é criada em prompt nenhum; **nenhuma proibição
  nova** entra em prompt (a matriz mais o item 15 já a produzem — `DP-M`, §16.4); a matriz **não é
  editada** por esta tarefa; `.claude/skills/scrum-master/SKILL.md`, `.claude/agents/pantonic-reviewer.md`
  e `.claude/agents/pantonic-executor.md` são reconferidos pelo mesmo critério, mas o que a `T37` e a
  `T40` já resolveram **não se reabre**.
- **Verificação:** os quatro checks do §3 item 6 em exit 0; o relatório existe com uma linha por
  ocorrência; toda ocorrência de classe (c) tem tíquete indexado no diário.
- **Pronto quando:** todo prompt do kit descreve só o que a matriz endossa, e o que não coube nela
  está no relatório e no índice de tíquetes, nunca resolvido por conta própria.

### T44 — Sanitização: doutrina, espelho e índices contra a matriz [Opus · classe redacao · teto 40]
- **Dossiê fechado por:** `DP-O` (§18). **Não delegável antes da `T43`** — a doutrina descreve o
  kit, e o relatório da `T43` já traz metade das âncoras.
- **Objetivo:** a doutrina publicada e seus índices param de atribuir a um agente o que a matriz não
  declara.
- **Universo fechado:** `GOVERNANCA.md`, `README.md`, `ARQUITETURA_PANTONICA.md`,
  `docs/RUBRICA_DE_REVISAO.md`, `docs/RESIDENCIA_DOUTRINA.md`, `docs/DOC_MAP.md`.
- **Método e classificação:** idênticos aos da `T43`; as linhas novas vão para a **seção 2** do mesmo
  relatório `docs/audits/CONFORMIDADE_MATRIZ_2026-08-12.md`.
- **Cuidado:** o `README.md` é **espelho** — a correção nasce na fonte e desce, nunca o contrário;
  `.claude/README.md` é **região gerada** e não se edita à mão; registro do que aconteceu à época
  (entradas do `CHANGELOG.md`, RDOs emitidos, bullets de fechamento do diário, seções do
  `docs/DIARIO_HISTORICO.md`) **não se reescreve** — se contradiz a matriz de hoje, é história, não
  não-conformidade; o recorte do `TK-36` (o §9 do README e a doutrina de handover) **fica de fora**.
- **Verificação:** os quatro checks do §3 item 6 em exit 0, com `check-readme.ps1` cobrindo o
  espelho; relatório com a seção 2 preenchida; toda ocorrência de classe (c) com tíquete indexado.
- **Pronto quando:** doutrina, espelho e índices só atribuem o que a matriz endossa, e o que sobrou
  está declarado como lacuna da matriz, no relatório e no índice.

### T45 — `TK-39`: o critério de aceitação deixa de ser contagem [Opus · classe redacao · teto 25]
- **Dossiê fechado por:** enunciado do dono de 2026-08-13 (§19, reescrito por esta tarefa). **Card
  prioritário — executa antes da `T29`.** Nenhuma questão owner-gated pendente: o critério foi
  enunciado e o recorte do que é e do que não é alvo está fixado abaixo.
- **Objetivo:** o critério de aceitação do plano para de se apoiar em **número de acionamentos do
  gerente** e passa a se apoiar na **causa** de cada acionamento.
- **O que a decisão do dono fixa** (transcrever, não reinterpretar):
  1. **Contagem de round-trip morre como conceito de aceitação.** Um teto de vezes que o gerente é
     acionado ou não tem valor, ou, existindo, é **arbitrário** — não há como derivar esse limite de
     nada. Métrica arbitrária não governa aceitação.
  2. **A responsabilidade do gerente é ilimitada onde ela é dele:** dirimir ambiguidade e resolver
     conflito, sobretudo de **requisitos** e de **aceitação**. Nenhuma métrica pode restringi-la.
  3. **Risco fatal declarado:** o agente decidir aspecto de aceitação sem estar **inequivocamente**
     seguro de que é a melhor solução. Escalada é o comportamento **desejado**, nunca um custo a
     minimizar.
  4. **Critério objetivo de ineficiência:** é entrega ineficiente quando o framework solicita
     acionamento do gerente em **caminho feliz ou caminho natural** — sem pendência e sem demanda
     que seja dele. Exemplo do dono: parar para que ele limpe o contexto e invoque a tarefa seguinte
     é acionamento em caminho feliz — o plano corre sem problema, e ele está **mediando execução
     normal**, que é a ineficiência que o framework existe para eliminar.
- **Alvos, medidos em 2026-08-13:**
  - `docs/plans/P-0734-execucao-autonoma.md` **§19** (`:3652-3673`) — reescrever: sai "round-trip de
    despacho reprova", entra a classificação **por causa**. Sai qualquer contagem.
  - **`### T16`** — `:553` (a medida "quantos round-trips o dono precisou dar") e `:564-569` (a
    cláusula de aceitação e o "Pronto quando" que mandam **classificar e contar**). A medida passa a
    ser **qualitativa e por ocorrência**: cada acionamento do dono é registrado com a **causa**, e a
    presença de **um só** acionamento de caminho feliz já é achado de ineficiência.
  - **`### T17`** — conferir que o veredito do dono referencia o §19 reescrito, sem contagem.
  - `GOVERNANCA.md` — residência do conceito na doutrina: **§4.3 Execução em contexto limpo**
    (`:312-346`), onde mora a doutrina de limpar contexto e abrir a tarefa seguinte, com o gancho
    para **§3.1 `:201`** ("sem desempate → escala ao dono"), que é a regra de ambiguidade que este
    critério complementa.
  - `.claude/skills/scrum-master/SKILL.md` — a skill que conduz o loop precisa saber **quando parar
    é correto** (pendência, ambiguidade, conflito de requisito ou de aceitação) e **quando parar é
    defeito** (caminho feliz).
- **Fora do alvo, declarado — não tocar:**
  - Toda ocorrência de "round-trip" que é **registro do que aconteceu** (`§6` tabela de riscos
    `:1938`; `:1909`, `:1921`, `:1925`, que narram as ratificações já ocorridas; `:2156`): é
    história, não critério.
  - O **batching de decisão** (`:1234`, `:1865`; `.claude/skills/handover/SKILL.md:58`;
    `.claude/skills/proximo-passo/SKILL.md:61`, "1 round-trip, não N"): não limita o gerente — impede
    **fragmentar em N prompts uma decisão que já é dele**, e vai na mesma direção do critério novo.
    Preservar.
  - `docs/RESIDENCIA_DOUTRINA.md:171` — registro de uma ratificação ocorrida.
- **Invariantes:** nenhum número novo entra no lugar do que sai; **nenhum guardrail novo é criado**
  (a contagem de guardrails do espelho permanece 15 × 15 e as seções com Fonte da verdade permanecem
  14 — o `check-readme.ps1` reporta as duas); o espelho do `README.md` **não** é tocado aqui — a
  consolidação do README é da `T17`, que fecha o plano, e antecipá-la faria a mesma seção ser
  reescrita duas vezes.
- **Verificação:** bateria do §3 item 6, os quatro em exit 0, com `check-readme.ps1` reportando
  **15 guardrail(s)** e **14 seção(ões) com Fonte da verdade válida**, e `python -m pytest` no piso
  **39**; Grep por `round.?trip` nos alvos, conferindo que nenhuma ocorrência remanescente é critério
  de aceitação por contagem.
- **Pronto quando:** o critério de aceitação do plano é qualitativo e classificado por causa, a
  doutrina hospeda o conceito, a skill que conduz o loop sabe distinguir parada legítima de parada
  defeituosa, e nenhuma contagem de acionamentos sobrevive como controle.

### T46 — Doutrina: guardrail 16 (`G-SURFACE`) e o espelho em lockstep [Opus · classe redacao · teto 25]
- **Dossiê fechado por:** `DP-P` (§20), enunciado do dono de 2026-08-13. **Bloco prioritário —
  executa antes da `T29`, e é a régua que a `T47` e a `T48` aplicam.** Nenhuma questão owner-gated
  pendente: a regra foi enunciada; o nome do guardrail e a residência são escolha de planejamento,
  já fixadas abaixo.
- **Objetivo:** publicar como guardrail nomeado a golden rule enunciada pelo dono — **mudança de
  decisão estruturante regulariza a superfície de contato inteira, no ato**.
- **O que a decisão do dono fixa** (transcrever, não reinterpretar):
  1. **O gatilho é a decisão estruturante:** correção ou modificação de **objetivo-chave**,
     **requisito** ou **caso de uso**. Não é toda mudança — é a que altera o que o trabalho *é*.
  2. **A ação é imediata e cobre toda a superfície de contato**, não só o artefato onde a decisão
     foi tomada. Regularização a posteriori não é opção.
  3. **O custo de adiar é o que a regra existe para evitar:** o agente seguinte, que não tem o
     contexto do ato, para para pedir a regularização — e, no pior caso, ingere texto vigente e
     texto derrubado lado a lado, que é o sinal de poluição da Regra 2 (`GOVERNANCA.md` §4.3).
- **Alvos, medidos em 2026-08-13:**
  - `GOVERNANCA.md` **§7** — item **16** novo, inserido depois do item 15 (`:594-608`) e **antes**
    do parágrafo "Esses guardrails são materializados..." (`:610`). Formato idêntico ao dos itens
    vizinhos, com a linha `*Enforcement:*` fechando.
  - `README.md` **§10 "Os guardrails"** — linha `| 16 | ... |` na tabela, imediatamente depois da
    linha 15 (`:712`), com a mesma forma de duas colunas (enunciado curto | enforcement).
- **Enforcement a declarar:** gate de planejamento (a rodada que fecha a decisão estruturante já
  emite os cards de regularização, e o plano não avança sem eles) + gate de review.
- **Fora do alvo, declarado — não tocar:** a matriz de responsabilidades do §3 (nenhum papel novo
  nasce aqui); a §7.1 (porta de saída de guardrail); `check-readme.ps1`, que conta guardrail
  dinamicamente e passa a reportar **16** sem edição nenhuma.
- **Invariantes:** nenhum guardrail existente é alterado ou removido; a contagem do espelho passa de
  **15 × 15** para **16 × 16**, verificada pelo `check-readme.ps1`; as seções com Fonte da verdade
  permanecem **14**.
- **Verificação:** bateria do §3 item 6, os quatro em exit 0, com `check-readme.ps1` reportando
  **16 guardrail(s)** e **14 seção(ões) com Fonte da verdade válida**, e `python -m pytest` no piso
  **39**.
- **Pronto quando:** a golden rule é guardrail nomeado na doutrina, espelhada no README na mesma
  rodada, e o `check-readme.ps1` fecha em 16 × 16.

### T47 — Consolidação, universo 1: o plano `P-0734` [Opus · classe redacao · teto 40]
- **Dossiê fechado por:** `DP-P` (§20). **Sucede a `T46`** — varrer antes de a régua existir mede
  contra doutrina incompleta, pela mesma razão que ordenou o bloco da `DP-O`.
- **Objetivo:** este plano passa a enunciar **uma** vez o entendimento vigente dos objetivos, e todo
  texto derrubado por rodada posterior fica inequivocamente marcado como derrubado.
- **Fato que abre a tarefa** (medido em 2026-08-13): o plano tem **3745 linhas** e **sete rodadas de
  replanejamento** empilhadas (§9 a §20). Pelo menos quatro camadas de texto vigente convivem com
  texto revogado: `DA-9` revogada pela `DA-11`; `DP-D` (§9) parcialmente revogada pela `DP-E`
  (§10.3); `T34` cancelada por absorção em 2026-08-12 com o corpo do card preservado; e o §19
  reescrito pela `T45`, cujo primeiro resíduo medido é o `TK-40`.
- **Método prescrito** (classe consolidação sobre artefato grande — Read integral estoura e Grep
  cru colapsa): sonda programática via scratchpad que emita o mapa de seções com faixas de linha e
  o índice de todos os `DP-*`/`DA-*`/`DE-*`/`T<n>` com o estado declarado de cada um; só então
  leitura dirigida das faixas que a sonda apontar como conflitantes.
- **Classificação obrigatória de cada ocorrência** (mesma régua da `DP-O`):
  - **(a) história** — narra o que aconteceu à época (bullet de fechamento, ratificação ocorrida,
    snapshot de fila dentro de rodada antiga, corpo de card cancelado preservado como material
    absorvido). **Não se toca.**
  - **(b) texto vigente que contradiz o entendimento atual** — enunciado normativo, dossiê de tarefa
    ainda não executada, mitigação de risco, cláusula de aceitação. **Regulariza no ato.**
  - **(c) contradição que só o dono resolve** — duas leituras defensáveis do objetivo, requisito ou
    caso de uso. **Para, registra e sobe** (`G-SCOPE`, `G-EXECREADY`); não se decide aqui.
- **Alvo:** `docs/plans/P-0734-execucao-autonoma.md` (arquivo único). Inclui o **`TK-40`**, que é
  ocorrência de classe (b) já medida: §6 (`:2000`) promete que a `T16` "mede quantos round-trips de
  fato desapareceram", e a `T16` reescrita não conta mais — a mitigação passa a se apoiar no
  registro qualitativo por ocorrência, com o RDO seguindo como instrumento compensatório (`DA-5`).
- **Entregável:** as edições de classe (b) **mais** o relatório
  `docs/audits/CONSOLIDACAO_SUPERFICIE_2026-08-13.md`, com uma linha por ocorrência (âncora, classe,
  o que foi feito), e a lista de classe (c) separada, se houver.
- **Fora do alvo, declarado — não tocar:** `docs/DIARIO_HISTORICO.md` e os bullets de fechamento do
  `docs/DIARIO_DE_OBRAS.md` (registro do ocorrido); os demais planos, vivos ou fechados; o
  `README.md` (universo 2, é da `T48`); nenhuma decisão já ratificada é reaberta — consolidar é
  tornar legível o que foi decidido, nunca decidir de novo.
- **Invariantes:** nenhuma decisão ratificada muda de conteúdo; nenhum card é cancelado ou criado;
  as contagens do espelho e o piso da suíte não se movem.
- **Verificação:** bateria do §3 item 6, os quatro em exit 0, com `check-readme.ps1` reportando
  **16 guardrail(s)** (a `T46` já entrou) e **14 seção(ões)**, e `python -m pytest` no piso **39**.
- **Pronto quando:** o plano enuncia o entendimento vigente uma vez só, o texto derrubado está
  marcado como derrubado, o relatório existe e toda ocorrência de classe (c) subiu ao dono em vez
  de ser resolvida embaixo.

### T48 — Consolidação, universo 2: os artefatos publicados do framework [Opus · classe redacao · teto 40]
- **Dossiê fechado por:** `DP-P` (§20). **Sucede a `T47`**, pela mesma razão que pôs a `T43` antes
  da `T44`: o plano consolidado é a referência contra a qual os artefatos publicados se medem, e o
  relatório da `T47` já traz metade das âncoras.
- **Objetivo:** os artefatos que o framework publica — doutrina, espelho, kit executável e índices —
  descrevem os objetivos vigentes da iniciativa, sem resíduo do entendimento derrubado.
- **Universo fechado e declarado:** `GOVERNANCA.md`; `README.md`; `.claude/` (agentes, skills,
  checks); `docs/DOC_MAP.md`, `docs/RESIDENCIA_DOUTRINA.md`, `docs/CONSUMIDORES.md`,
  `ARQUITETURA_PANTONICA.md`, `CHANGELOG.md`.
- **Método e classificação:** os mesmos da `T47`, itens (a)/(b)/(c), com a régua do `G-SURFACE`
  publicada pela `T46`.
- **Entregável:** as edições de classe (b) **mais** a segunda metade do mesmo relatório
  `docs/audits/CONSOLIDACAO_SUPERFICIE_2026-08-13.md`, na mesma forma de uma linha por ocorrência.
- **Fora do alvo, declarado — não tocar:** `docs/DIARIO_HISTORICO.md`; entradas de `CHANGELOG.md`
  que narram versão já publicada; `docs/benchmark/` (corpus medido à época); a matriz de
  responsabilidades do §3, que só muda por decisão do dono.
- **Invariantes:** nenhum guardrail nasce ou sai aqui (o 16 é da `T46`); a contagem fecha em
  **16 × 16** e **14 seções**; nenhum bump de versão (`DE-7`, congelamento em `0.0.0`).
- **Verificação:** bateria do §3 item 6, os quatro em exit 0, com `check-readme.ps1` em **16
  guardrail(s)** e **14 seção(ões)**, e `python -m pytest` no piso **39**; Grep de fecho pelos
  termos do entendimento derrubado que a `T47` listar, conferindo que nenhuma ocorrência
  remanescente é enunciado vigente.
- **Pronto quando:** os dois universos estão varridos contra a régua, o relatório único cobre os
  dois, e o framework inteiro descreve os mesmos objetivos que o plano consolidado enuncia.

### T49 — A regra na doutrina: número arbitrário não governa fluxo [Opus · classe redacao · teto 30]
- **Dossiê fechado por:** `DP-Q` (§21), enunciado do dono de 2026-08-13. **Bloco prioritário —
  executa antes da `T29`, e é a régua que a `T50` e a `T51` aplicam.** Nenhuma questão owner-gated
  pendente: a decisão foi enunciada e o recorte do que fica para o plano futuro está fixado.
- **Objetivo:** a doutrina para de eleger número arbitrário como porteiro de fluxo, e passa a tratar
  custo e consumo como **informação de agregado**.
- **O que a decisão do dono fixa** (transcrever, não reinterpretar):
  1. **Teto numérico é a mesma questão do limite de round-trips:** número arbitrário só gera
     **ruído**, e ação baseada em ruído é decisão equivocada.
  2. **Custo e consumo são informativos e não têm valor em isolamento.** Só rendem insight
     **analisados em conjunto**. A série (`docs/telemetria.tsv`) continua sendo alimentada sem
     exceção — é o agregado que tem valor.
  3. **Residência do registro por tarefa, por ora:** o card **"Lições aprendidas na tarefa"** do
     laudo do `reviewer`, e só **quando ele enxergar** algo. Fora disso, **desconsiderar**.
  4. **Limite não conscientemente delimitado que afeta o fluxo é vício.** Um teto arbitrário
     encerrando tarefa legítima é o caso exemplar, e a resposta é parar, reescrever a regra e
     sanitizar os artefatos atingidos — que é o `G-SURFACE` operando.
  5. **A matéria de limites não é doutrinada neste plano.** Ela se revê inteira no plano próprio já
     previsto (desdobramento da `T17` item 4, onde a `T34` foi absorvida). Aqui só cai o que governa
     fluxo; nada de teto novo entra no lugar.
- **Alvos:**
  - `GOVERNANCA.md` **§4.3** — a cláusula *"enquanto não houver proxy de ocupação disponível ao
    agente, o proxy operante é o teto de tool uses por classe (§3)"* é exatamente o vício: elege o
    número arbitrário como critério operante de encerramento. **Cai.** Ficam as duas condições que
    já governam o contexto e não são arbitrárias — **coesão** (poluição, fatal e imediata) e
    **capacidade** (ocupação da janela).
  - `GOVERNANCA.md` **§3** — a tabela de tetos por classe passa a ser declarada **referência
    informativa de dimensionamento**, nunca gate: não recusa entrega, não roteia e não encerra
    janela. A tabela **permanece** (o dado alimenta a série); o que sai é o poder de porteiro.
  - `README.md` — espelho das duas seções acima, em lockstep.
  - `docs/plans/P-0734-execucao-autonoma.md` **§3 item 5** — o "regime interino de teto" deixa de ser
    interino e passa a ser o **regime deste plano**, com o ponteiro para a `DP-Q`; e o topo do
    `### DP-B` recebe a marca de revogação parcial (caem os tetos que roteiam; permanece o resto).
- **Fora do alvo, declarado — não tocar:** `docs/telemetria.tsv` e a doutrina de telemetria do §4.2
  (a série é o agregado que a decisão **preserva**); as tabelas de roteamento do `scrum-master`
  (é a `T50`); o gerador de laudo e o de RDO (é a `T51`); nenhum guardrail nasce ou sai.
- **Invariantes:** nenhum número novo entra no lugar do que sai; a contagem do espelho permanece
  **16 × 16** e as seções com Fonte da verdade **14**; sem bump de versão (`DE-7`).
- **Verificação:** bateria do §3 item 6, os quatro em exit 0, com `check-readme.ps1` em **16
  guardrail(s)** e **14 seção(ões)**, e `python -m pytest` no piso **39**.
- **Pronto quando:** a doutrina não elege mais número arbitrário como critério de encerramento ou de
  roteamento, custo e consumo estão declarados como informação de agregado, e a residência do
  registro por tarefa está nomeada.

### T50 — A regra no loop: `A4` e `B2` deixam de rotear por número [Opus · classe redacao · teto 30]
- **Dossiê fechado por:** `DP-Q` (§21). **Sucede a `T49`** — a skill materializa a doutrina, e
  reescrever a tabela antes de a régua estar publicada mede contra doutrina incompleta.
- **Objetivo:** o loop para de encerrar tarefa legítima e janela legítima por número arbitrário.
- **Alvos, medidos em 2026-08-13** em `.claude/skills/scrum-master/SKILL.md` (293 linhas):
  - **`A4`** (`:224`) — *"`tools` gastos (bloco `<usage>`) > teto declarado, com qualquer `status`"*
    deixa de ser condição de roteamento. O estouro não retém a entrega nem dispara replanejamento:
    o consumo medido segue para a série, e o que houver de qualitativo entra pelo card "Lições
    aprendidas na tarefa" do laudo, quando o `reviewer` enxergar. A linha sai da tabela do bloco A
    ou é reescrita sem poder de rota — a forma é escolha de redação, o efeito é fixo.
  - **`B2`** (`:249`) — *"tarefas fechadas na janela = 10 **ou** consumo acumulado ≥ 900 k tokens"*
    é o vício nomeado pelo dono: dois números que ninguém deriva de nada, encerrando trabalho
    legítimo. **Caem os dois.** O encerramento de janela passa a se apoiar nas condições não
    arbitrárias do `GOVERNANCA.md` §4.3 — **coesão** (sinal de poluição, que é fatal e imediato) e
    **capacidade** (ocupação da janela) —, e o instrumento de ocupação é a `T13`.
  - **Lista "Obriga parada"** (`:258`) — saem *"estouro de teto (`A4`)"* e *"teto de janela
    (`B2`)"*. Permanecem as paradas de causa: `pendencia=`, `escalar`, `premissa` (`A3b`),
    reprovação após a última retentativa (`A7`), plano não-pronto (`B3`).
  - **Parágrafo de fecho** (`:269-271`) — a frase *"O encerramento de janela (`B2`) mede ocupação —
    tarefas fechadas e consumo —, e o que sobe ao dono fica fora dessa conta"* passa a dizer que
    ocupação é ocupação da janela de contexto, não contagem de tarefas nem de tokens gastos.
  - **Tabela de contadores** (`:25`) e a linha `:299` (*"o teto de tool uses da tarefa é o da classe
    registrada"*) — reconciliar com o acima: contador que só existia para alimentar `A4`/`B2` perde
    a coluna `teto`; o que permanece é medição para a série.
- **Fora do alvo, declarado — não tocar:** `A1`, `A2`, `A3a`, `A3b`, `A5`..`A9`, `B1`, `B3`, `B4`;
  a seção "Parada defeituosa" (`:263-267`), publicada pela `T45` e vigente; a `T13`, que continua
  como está na fila, apenas repositionada (§5).
- **Invariantes:** nenhum teto novo entra no lugar; nenhuma parada de **causa** é enfraquecida — a
  decisão remove porteiro numérico, nunca escalada legítima; `check-drift` verde (a edição é de
  skill, então `.claude/README.md` regenera junto).
- **Verificação:** bateria do §3 item 6, os quatro em exit 0, com `check-readme.ps1` em **16
  guardrail(s)** e **14 seção(ões)**, e `python -m pytest` no piso **39**; Grep por `teto` no
  `SKILL.md`, conferindo que nenhuma ocorrência remanescente governa rota ou encerramento.
- **Pronto quando:** nenhuma linha das tabelas de roteamento encerra tarefa ou janela por número, as
  paradas de causa continuam intactas, e o encerramento de janela aponta para ocupação e coesão.

### T51 — Sanitização da superfície atingida — **partida em `T51a`/`T51b` por orçamento**
- **Dossiê fechado por:** `DP-Q` (§21). **Sucede a `T50`** — doutrina e loop primeiro, porque é
  deles que a superfície deriva, e o relatório das duas já traz as âncoras.
- **Objetivo:** nenhum artefato do framework continua tratando teto como porteiro, e a residência do
  registro qualitativo de consumo está materializada.
- **Universo fechado e declarado, com a contagem bruta de `teto` medida em 2026-08-13:**
  `.claude/tools/rdo.py` (25), `.claude/tools/review_evidence.py` (21), `.claude/tools/rdo_template.md`
  (1), `docs/RUBRICA_DE_REVISAO.md` (2), `.claude/skills/diario-de-obras/SKILL.md` (2),
  `.claude/README.md` (1), `docs/RESIDENCIA_DOUTRINA.md` (3), os arquivos de agente
  (`pantonic-executor.md`, `pantonic-reviewer.md`) e os testes `tests/test_rdo.py` (3) e
  `tests/test_review_evidence.py` (4). A contagem bruta é ponto de partida, não alvo: a maioria é
  **medição legítima** e permanece.
- **Uma âncora no próprio plano, herdada da `T49`:** a **`DA-11`** e a prosa que a elabora ainda
  enunciam *"até ele existir, o proxy operante continua sendo o teto de tool uses por classe"* —
  premissa ratificada que a `DP-Q` derruba. Recebe **marca de revogação parcial** no mesmo formato
  que a `T47` deu à `DP-A`/`DP-B` e a `T49` deu ao `### DP-B`: corpo intocado, marca no topo. Âncoras
  a re-derivar por Grep.
- **Régua de corte, em uma linha:** medir e registrar consumo **permanece**; **decidir** por consumo
  **sai**. Onde o código ou o prompt usa o teto para reprovar, rotear, encerrar ou recusar, o poder
  cai; onde ele só informa ou alimenta a série, fica.
- **Materialização a entregar:** o card **"Lições aprendidas na tarefa"** do laudo é a residência do
  registro qualitativo de consumo, e só é preenchido **quando o `reviewer` enxergar** algo — nunca
  obrigatoriamente. Isso é **insumo fechado para a `DP-J`**, não resolução dela: a `T30` continua na
  fila e continua indo à ratificação em lote com a `DP-I`.
- **Entregável:** as edições **mais** um terceiro bloco no relatório já existente
  `docs/audits/CONSOLIDACAO_SUPERFICIE_2026-08-13.md`, na mesma forma de uma linha por ocorrência,
  com a mesma classificação (a)/(b)/(c) das `T47`/`T48`.
- **Fora do alvo, declarado — não tocar:** `docs/telemetria.tsv` e o §4.2 (a série é preservada por
  desenho); `docs/DIARIO_HISTORICO.md`, os bullets de fechamento do diário, os RDOs já emitidos e as
  entradas de `CHANGELOG.md` de versão publicada (registro do ocorrido); os planos, vivos ou
  fechados, exceto o `P-0734`, já tratado pela `T49`; `docs/benchmark/`.
- **Invariantes:** nenhum teste é apagado ou afrouxado para caber na mudança — teste que verifica
  gate removido é reescrito para verificar o comportamento novo, e o piso **39** não desce; espelho
  em **16 × 16** e **14 seções**; sem bump (`DE-7`).
- **Verificação:** bateria do §3 item 6, os quatro em exit 0; Grep de fecho por `teto` no universo,
  conferindo que nenhuma ocorrência remanescente decide.
- **Pronto quando:** medir consumo continua em toda parte, decidir por consumo não existe em lugar
  nenhum, o card de lições aprendidas é a residência nomeada do qualitativo, e o relatório cobre o
  terceiro bloco.
- **Partição:** ~13 write-clusters medidos, acima da linha de 8 do gate de delegação, e com duas
  naturezas distintas — mudança de comportamento com teste (`T51a`) e redação (`T51b`). Entre as
  duas a ordem é forçada: a `T51b` descreve o instrumento, e descrever antes de ele mudar inverte a
  ordem, pela mesma razão que pôs a `T40` antes da `T41`.

### T51a — Sanitização, o instrumento: o gerador para de decidir por consumo [Sonnet · classe implementação padrão · teto 40]
- **Objetivo:** nenhum instrumento executável calcula veredito, desdobramento ou reprovação a partir
  de consumo. Medir e imprimir permanece; ramificar sai.
- **Alvos:** `.claude/tools/rdo.py` — medido pela `T50`: `calcular_desdobramento` decide por
  `orcamento_estourado = args.tool_uses > dossie.teto` (`:517` e `:608-609`), que é exatamente o
  poder de rota que a `DP-Q` remove; `.claude/tools/review_evidence.py`;
  `.claude/tools/rdo_template.md`; e os testes `tests/test_rdo.py` e `tests/test_review_evidence.py`.
  Âncoras a re-derivar por Grep.
- **Invariante de teste:** nenhum teste é apagado ou afrouxado para caber na mudança — teste que
  verificava o gate removido é **reescrito** para verificar o comportamento novo (o consumo é
  medido e impresso, e nenhum desdobramento se abre por causa dele). O piso **39** não desce.
- **Pronto quando:** o gerador mede e registra consumo sem ramificar por ele, e a suíte prova isso.

### T51b — Sanitização, a descrição: prompts, índices e a marca da `DA-11` [Opus · classe redacao · teto 30]
- **Objetivo:** nenhum texto que descreve papéis, rubrica ou navegação continua atribuindo ao teto
  poder de porteiro.
- **Alvos:** `docs/RUBRICA_DE_REVISAO.md`; `.claude/agents/pantonic-executor.md` e
  `.claude/agents/pantonic-reviewer.md`; `.claude/skills/diario-de-obras/SKILL.md`;
  `docs/RESIDENCIA_DOUTRINA.md`; `.claude/README.md` (regenerado, se agente ou skill mudar); e a
  **marca de revogação parcial da `DA-11`** no próprio plano, conforme o bullet herdado acima.
- **Entregável adicional:** o **terceiro bloco** do relatório
  `docs/audits/CONSOLIDACAO_SUPERFICIE_2026-08-13.md`, cobrindo as duas sub-tarefas.
- **Pronto quando:** a descrição concorda com o instrumento e com a doutrina, e o relatório fecha os
  três blocos.

### T52 — Fecho do bloco `DP-Q`: o gatilho residual e a residência não materializada [Sonnet · classe implementação padrão · teto 40]
- **Dossiê fechado por:** `DP-Q` (§21). **Fecha o bloco** — os dois itens são resíduo medido pela
  `T51b`, e o `G-SURFACE` proíbe enfileirar como dívida o que a decisão estruturante atingiu.
- **Parte 1 — o gatilho residual.** `.claude/skills/handover/SKILL.md`, seção "Checkpoint
  intermediário": o gatilho ainda é *"quando o consumo cruza **2/3 do teto da classe**"*. É número
  disparando encerramento, e contradiz o `GOVERNANCA.md` §4.3 já reescrito pela `T49`, que trocou
  exatamente esse gatilho por um qualitativo. **Transcrever** o critério vigente do §4.3 — nada se
  reinterpreta aqui. O teto de **2 tool uses do próprio checkpoint** permanece: é prescrição de
  esforço do artefato, não decisão por consumo.
- **Parte 2 — a residência não materializada.** O card **"Lições aprendidas na tarefa"** é nomeado
  pela doutrina (`GOVERNANCA.md` §3), pela skill `scrum-master` e pelo prompt do `pantonic-reviewer`
  como a residência do registro qualitativo, mas **nenhum gerador o emite**: nem `cmd_laudo` de
  `.claude/tools/rdo.py` nem `.claude/tools/rdo_template.md` têm o card. Residência nomeada e não
  materializada deixa a `DP-Q` inerte. O card passa a ser emitido, **discricionário por desenho** —
  preenchido quando o `reviewer` enxergar algo, e vazio quando não houver o que observar.
- **Fronteira declarada contra a `DP-J`:** esta tarefa materializa a **residência** que a `DP-Q` item
  3 já fixou; ela **não** decide o que o `scrum-master` colhe ou descarta do laudo, que é a `T30` e
  segue à ratificação em lote com a `DP-I`.
- **Invariantes:** nenhum teto novo entra; nenhum teste é apagado ou afrouxado — o card novo entra
  com teste, e o piso **39** não desce (sobe, se somar); espelho em **16 × 16** e **14 seções**; sem
  bump (`DE-7`); `check-drift` verde (a edição é de skill, `.claude/README.md` regenera junto).
- **Verificação:** bateria do §3 item 6, os quatro em exit 0.
- **Pronto quando:** nenhum número dispara checkpoint, o card de lições aprendidas existe no
  documento que o gerador emite, e a suíte prova as duas coisas.

### T53 — `TK-43`: a residência versionada do hook e o materializador [CANCELADA — absorvida pelo `P-0735` §6.1, 2026-08-15]
- **Absorção.** O corpo abaixo permanece como **material absorvido**: ele é insumo integral das
  `RPC-T2` e `RPC-T3` do `P-0735-residencia-e-ponto-de-carga`, que resolvem em forma geral a matéria
  que esta tarefa resolvia em forma particular. Some apenas a residência particular que ela
  prescrevia — `.claude/hooks/hooks.json` **não nasce**, porque uma segunda declaração ao lado do
  manifesto único `.claude/projecoes.json` seria a duplicata que a régua de residência proíbe.
  Nenhuma tarefa sai mais daqui.
- **Dossiê fechado por:** `DP-R` (§22). Quita a **parte executável** do `TK-43`; a superfície de
  doutrina é a `T54`, que executa imediatamente depois.
- **Objetivo:** o hook que o kit distribui deixa de morar num arquivo ignorado pelo git. A
  declaração passa a ser artefato versionado do kit, e o `.claude/settings.json` da máquina passa a
  ser **produto de comando idempotente**, nunca origem — de modo que o proxy da `T13` (e todo hook
  futuro, incluindo o da `T14`) chegue a qualquer projeto que materialize o kit.
- **Arquivos-alvo:**
  - `.claude/hooks/hooks.json` — **novo**, a residência canônica.
  - `.claude/tools/hooks_sync.py` — **novo**, o materializador/verificador.
  - `tests/test_hooks_sync.py` — **novo**.
  - `.claude/checks/kit_check.ps1` — **editado**, dois blocos (um em `-Mode validate`, um em
    `-Mode check-drift`).
  - `.claude/settings.json` — **não se edita à mão**: passa a ser reescrito pela execução de
    `python .claude/tools/hooks_sync.py apply` dentro desta tarefa.
- **Formato do canônico.** JSON com **uma única chave de topo, `hooks`**, no mesmo esquema que o
  harness lê dentro de `settings.json` (evento → lista de `{matcher, hooks:[{type, command}]}`), com
  o caminho do comando escrito pelo placeholder **`{KIT_ROOT}`**. Conteúdo inicial é **exatamente o
  hook vigente**, transcrito: evento `PreToolUse`, matcher `.*`, comando
  `python {KIT_ROOT}/tools/ocupacao.py`. **Nenhum hook novo nasce nesta tarefa** — ela move o que já
  existe e cria o mecanismo.
- **Ancoragem — as duas topologias, resolvidas sem pergunta.** O script resolve a raiz do kit a
  partir do próprio caminho (mesmo desenho de `sync-kit.ps1`, que roda tanto do hub quanto de
  `<consumidor>/.claude/kit/`):
  - **hub** — raiz do kit é `<repo>/.claude` (o diretório que contém `hooks/`, `tools/`, `checks/`);
    destino é `<raiz-do-kit>/settings.json`; `{KIT_ROOT}` resolve para `.claude`.
  - **consumidor** — raiz do kit é `<repo>/.claude/kit`; destino é o `settings.json` do **pai**
    (`<repo>/.claude/settings.json`); `{KIT_ROOT}` resolve para `.claude/kit`.
  - **regra única que decide:** se o nome do diretório-raiz do kit for `kit`, o destino é o pai;
    caso contrário é ele mesmo. O valor substituído usa separador POSIX em qualquer plataforma.
  - `--kit-root <caminho>` sobrepõe a resolução, para provar contra fixture sintética sem escrever
    no repositório real — mesmo desenho de `-KitRoot` (`kit_check.ps1`) e `--root`
    (`dead_code.py`, `ratchet_piso.py`).
- **CLI — três subcomandos, nenhum interativo.**
  - `apply` — materializa no `settings.json` local.
  - `check` — valida **o canônico** (não olha a máquina).
  - `drift` — compara **local × canônico**.
  Todos aceitam `--kit-root`; todos saem 0 em sucesso e 1 em falha, imprimindo **uma linha por
  problema**.
- **Semântica do `apply` — o que ela nunca pode destruir.** Toda chave de topo que não seja `hooks`
  é preservada com o valor intacto (hoje `permissions.deny`, com as **6 entradas** que o guardrail 13
  exige). Dentro de `hooks`, por evento: as entradas canônicas entram primeiro, na ordem declarada,
  com o comando já resolvido; as entradas locais **não-kit** são preservadas depois, na ordem
  original; as entradas locais **de kit** que não constam do canônico são removidas (são resíduo).
  `settings.json` ausente ⇒ cria o arquivo só com `hooks`. Escrita com indentação de 2 espaços,
  newline final, UTF-8 sem BOM, e **idempotente**: conteúdo resultante igual ao do disco não gera
  escrita.
- **O que é "entrada de kit".** Aquela cujo `command` referencia caminho sob a raiz do kit resolvida
  (`<KIT_ROOT>/tools/`, `<KIT_ROOT>/checks/`, `<KIT_ROOT>/hooks/`). Todo o resto é configuração de
  máquina do dono do repositório e é **intocável** — inclusive hook global e hook de ferramenta
  alheia ao kit.
- **O que o `check` exige do canônico:** o arquivo existe e parseia; `hooks` é objeto; cada entrada
  tem `matcher` e lista `hooks` não vazia, com `type: "command"` e `command` não vazio; e todo
  `command` que use `{KIT_ROOT}` aponta para arquivo **existente** sob a raiz do kit.
- **O que o `drift` acusa (exit 1):** (a) `settings.json` inexistente; (b) entrada canônica ausente
  do local, ou presente com comando diferente do resolvido; (c) entrada **de kit** no local que não
  está declarada no canônico — esta é a guarda de regressão do próprio `TK-43`, e é o que impede
  alguém de voltar a registrar hook direto no arquivo de máquina. Toda mensagem de falha traz o
  comando de remédio: `python <KIT_ROOT>/tools/hooks_sync.py apply`.
- **O que `kit_check.ps1` passa a exigir.** `-Mode validate` ganha um **bloco 4** (depois da
  paridade de versão) que chama `python <kitRoot>/tools/hooks_sync.py check --kit-root <kitRoot>` e
  agrega cada linha da saída à lista `$errors` do modo; a linha de OK do modo passa a citar também a
  contagem de hooks canônicos. `-Mode check-drift` ganha bloco equivalente com `drift`, agregado ao
  mesmo relatório de falha do modo — o modo continua checando `.claude/README.md`, e agora falha
  também por materialização ausente ou divergente. `python` indisponível ou saída não interpretável
  **falha ruidosamente**; nenhum dos dois modos passa em silêncio por não conseguir checar.
- **Testes (mínimo 9, fixtures sintéticas em `tmp_path`, nunca escrevendo no repositório real):**
  1. `apply` no layout hub materializa o hook **e** devolve `permissions.deny` byte a byte igual;
  2. `apply` no layout consumidor (`<repo>/.claude/kit`) grava o comando com prefixo `.claude/kit/`
     e escreve no `settings.json` do pai;
  3. `apply` é idempotente — segunda execução não altera o conteúdo;
  4. `apply` preserva hook local não-kit e remove entrada de kit obsoleta;
  5. `apply` sobre `settings.json` ausente cria o arquivo só com `hooks`;
  6. `check` falha quando o canônico aponta comando para arquivo inexistente;
  7. `drift` falha com `settings.json` ausente, e a mensagem contém o comando de remédio;
  8. `drift` falha com hook de kit presente no local e ausente do canônico (regressão do `TK-43`);
  9. `drift` sai 0 contra o repositório real depois do `apply` (leitura pura, sem escrita).
- **Invariantes.** Nenhum hook novo nasce aqui. **Nenhum repositório derivado é tocado** (`DA-3`):
  `docs/CONSUMIDORES.md` registra **0/6** consumidores com `.claude/kit/`, então a exigência nova não
  muda o estado de consumidor nenhum hoje, e o artefato viaja pelo subtree de `.claude/` quando
  algum instalar. **`sync-kit.ps1` não muda:** o contrato dele é espelhar `skills/` e `agents/` no
  namespace plano do consumidor, e `hooks/` viaja como `tools/` e `checks/` já viajam — dentro de
  `.claude/kit/`; dobrar a materialização de hook dentro dele estenderia o contrato de um script
  provado ponta a ponta, sem medida que justifique, e fica para o gatilho de propagação do §7. Sem
  bump (`DE-7`). Espelho em **16 guardrails × 14 seções** inalterado. Nenhum teste some — a suíte
  fechou a `T13` em **52 passed** e a contagem sobe.
- **Verificação:** bateria do §3 item 6, os quatro em exit 0 — e, especificamente, `check-drift`
  vermelho quando a materialização é desfeita à mão, provado uma vez durante a tarefa.
- **Pronto quando:** o hook canônico existe versionado, o `settings.json` local é produto de comando
  idempotente com o `permissions.deny` intacto, e a bateria de fechamento fica vermelha tanto se
  alguém desfizer a materialização quanto se alguém registrar hook de kit direto no arquivo local.

### T54 — `TK-43`: a superfície que diz onde hook mora e o que viaja [CANCELADA — absorvida pelo `P-0735` §6.1, 2026-08-15]
- **Absorção.** A superfície que esta tarefa regularizava está coberta: `GOVERNANCA.md` §3.1 na
  rodada de doutrina de 2026-08-15, `README.md` §11/§13 na `RPC-T1`, `.gitignore` e `CHANGELOG.md` na
  `RPC-T8`. Um item do corpo abaixo é **revogado**: o *Cuidado* mandava manter como está o bullet do
  hook global do `modelo-por-fase` (`GOVERNANCA.md` §3), pelo critério de que hook de kit é o que
  executa comando do kit; a régua nova classifica por **de quem é o conteúdo**, aquele hook é
  enforcement de regra publicada, e o bullet já foi conciliado. Nenhuma tarefa sai mais daqui.
- **Dossiê fechado por:** `DP-R` (§22). **Executa imediatamente depois da `T53`**, na mesma janela
  sempre que couber: o `G-SURFACE` manda regularizar a superfície de contato da decisão no ato, e
  entre as duas tarefas a doutrina publicada afirma o contrário do que o kit passou a fazer.
- **Objetivo:** o texto publicado deixa de dizer que hook não viaja e passa a dizer onde ele mora,
  como se materializa e o que o guarda cobra — sem o que o `TK-43` volta a acontecer por leitura
  correta do documento errado.
- **Arquivos-alvo e a edição exata de cada um:**
  1. **`.gitignore`, comentário do bloco das linhas 1–3.** O comentário vigente
     ("Configuração local de máquina (permissões, overrides de sessão) — nunca canônica") continua
     verdadeiro e **as duas entradas ignoradas permanecem**; o que falta é o ponteiro que evita a
     releitura errada. Acrescentar ao comentário: o hook canônico do kit mora em
     `.claude/hooks/hooks.json`, versionado, e este arquivo é só a materialização local produzida por
     `python .claude/tools/hooks_sync.py apply`.
  2. **`GOVERNANCA.md` §3.1 (`:196-197`), o parágrafo "Hook (`settings.json`) não é uma quinta
     superfície".** Duas coisas mudam e uma **não** muda: permanece que hook **não é** superfície de
     doutrina, e que hook sem regra escrita atrás dele é doutrina invisível; cai a cláusula final
     **"e não viaja"**, e a residência citada deixa de ser `settings.json`. O texto novo diz que o
     hook do kit **é versionado** (`.claude/hooks/hooks.json`) e **viaja com o kit**, materializando-se
     no `settings.json` local por comando idempotente, com a divergência acusada por
     `kit_check.ps1 -Mode check-drift`.
  3. **`README.md` §11 "Anatomia do kit".** (a) A frase de abertura (`:741`) passa a incluir a
     residência de hooks entre o que "viaja junto para todo projeto consumidor". (b) Logo depois da
     lista de verificadores (que termina em `:786`), entra um parágrafo curto nomeando
     `.claude/hooks/hooks.json` como a declaração canônica e `.claude/tools/hooks_sync.py` como o
     comando que a materializa, com a divergência coberta pelo `check-drift`. (c) **Correção
     incidental medida nesta rodada de planejamento:** a mesma frase de abertura diz "dez skills",
     enquanto o disco e a tabela da própria seção têm **onze** — o guarda `check-readme.ps1` compara
     tabela × disco e não lê o número em prosa, por isso a deriva passou. Trocar por "onze".
  4. **`README.md` §13 "Distribuição e versão", parágrafo "O que é." (`:870-874`).** Frase final
     nova: configuração de máquina (`.claude/settings.json`) **nunca viaja** — é ignorada pelo git —,
     e o que viaja é a declaração canônica do hook, materializada no arquivo local por comando, com
     `kit_check.ps1 -Mode check-drift` acusando materialização ausente ou divergente.
  5. **`CHANGELOG.md`, sob `## [Não lançado]`.** Uma entrada, na forma das vizinhas, registrando a
     residência versionada de hook e a exigência nova do `kit_check`, marcada `(EXA-T53`/`EXA-T54)`.
- **Cuidado.** `.claude/skills/`, `.claude/agents/` e `GOVERNANCA.md` §9 **não** são alvo: o §9
  descreve a materialização que o `sync-kit.ps1` faz de `skills/` e `agents/`, que esta decisão não
  altera, e `hooks/` viaja pelo mesmo caminho de `tools/` e `checks/`, que aquele parágrafo também
  não enumera — não há contradição a conciliar ali. O bullet do §3 sobre o **hook global** do
  `modelo-por-fase` (`:114-120`) também **fica como está**: pelo critério da `DP-R`, hook de kit é o
  que executa comando do kit, e aquele não executa.
- **Invariantes.** `.claude/skills/redacao-doc/SKILL.md` é normativa (§3 item 4). Nenhum guardrail novo
  (`DA-10`) — espelho em **16 × 16** e **14 seções**. Sem bump (`DE-7`). Nenhuma linha de narrativa
  histórica é reescrita: bullets de fechamento, RDOs e entradas já publicadas do `CHANGELOG.md`
  contam o que aconteceu à época.
- **Verificação:** bateria do §3 item 6, os quatro em exit 0; `Grep` por `settings.json` em
  `GOVERNANCA.md` e `README.md` → nenhuma ocorrência restante que descreva esse arquivo como
  residência de hook do kit (as do guardrail 13, sobre `permissions.deny`, permanecem e são
  corretas).
- **Pronto quando:** um leitor que só tenha o `README.md` e o `GOVERNANCA.md` sabe onde declarar um
  hook novo, sabe que o arquivo de máquina é produto, e não erra do jeito que o `TK-43` documenta.

### T55 — Identidade da tarefa por estado do loop: a série se alimenta sozinha [Sonnet · classe implementação padrão · teto 40]
- **Dossiê fechado por:** `DP-S` (§23), autorado na rodada de replanejamento de 2026-08-19. **Depende
  da `T7`** (o CLI `telemetria.py append`, que o hook consome) e da **`RPC-T2`** (o manifesto
  `.claude/projecoes.json`, onde a declaração do hook entra). Ambas `done`. A `T14` mediu o consumo e
  parou na identidade; esta tarefa fecha o vão que ela deixou, pela rota que o dono aprovou.
- **Objetivo:** a linha de `docs/telemetria.tsv` passa a ser escrita **sem gastar turno nenhum** — o
  `scrum-master` grava a tarefa corrente no ato do despacho, e o hook de `SubagentStop` lê a
  identidade de lá em vez de inferi-la da prosa do prompt.
- **Arquivos-alvo:**
  1. `.claude/skills/scrum-master/SKILL.md`, **Passo 4 — Despacho do executor** (`:84-107`): o passo
     passa a gravar `.claude/estado/tarefa-corrente.json` **antes** de invocar o
     `pantonic-executor`, com os campos que a linha da série exige e que só o loop conhece
     (`tarefa`, `projeto`, `modelo`, `plano`, carimbo de despacho). A **tarefa corrente** já é estado
     declarado do loop (`## Estado do loop`, `:31-32`) — o que muda é que ela passa a ser
     **escrita** num ponto que outro processo lê. Nenhum contador novo entra na tabela do `:25-29`.
  2. `.claude/tools/telemetria_hook.py` (novo): traduz o payload de `SubagentStop` em chamada a
     `python .claude/tools/telemetria.py append`, com as 8 flags obrigatórias
     (`--data`, `--projeto`, `--tarefa`, `--modelo`, `--tool_uses`, `--tokens_k`, `--duracao_s`,
     `--fonte`) — `--fonte usage`, porque o número vem do transcript do subagente e não de contagem
     do orquestrador.
  3. `.claude/projecoes.json`, `alvos.projeto.chaves.hooks` (`:7-19`): entra a chave `SubagentStop`,
     com o comando escrito em `{KIT_ROOT}` — mesma forma da entrada `PreToolUse` → `ocupacao.py` que
     já está ali. O `settings.json` local **não** é alvo de edição: é produto de
     `python .claude/tools/materializar.py apply`.
  4. `.gitignore`: entra `.claude/estado/`, no bloco de local de máquina (`:1-5`), com o comentário
     dizendo o que o diretório é.
  5. `tests/test_telemetria_hook.py` (novo): payload de fixture → linha esperada; ausência de estado
     → exit 0 sem escrita; `agent_type` fora do filtro → exit 0 sem escrita; transcript com N
     entradas `assistant` → soma esperada de `tokens_k` e contagem esperada de `tool_uses`.
- **Como os números saem do transcript** (medido na Sonda 5, `docs/audits/SPIKE_HARNESS_EXECUCAO_AUTONOMA.md:154-195`):
  `agent_transcript_path` aponta para um `.jsonl` exclusivo do subagente, com `message.usage` e
  `message.model` por entrada. `tokens_k` = soma de `input_tokens + cache_creation_input_tokens +
  cache_read_input_tokens + output_tokens` das entradas `assistant`; `tool_uses` = contagem de blocos
  `tool_use`; `duracao_s` = diferença entre o primeiro e o último `timestamp`. Mesmo padrão de parse
  que `ocupacao.py` (`T13`) já usa — não se inventa leitor novo.
- **Calibração obrigatória:** antes de declarar pronto, comparar o `tokens_k` que o hook calcula com
  o bloco `<usage>` de **um** despacho aninhado trivial. Divergência sistemática é resultado a
  registrar, não a esconder.
- **Invariantes.** O hook **apenas apende** à série: não escreve no diário, não fecha tarefa, não
  emite juízo (`GOVERNANCA.md` §4.2). **Falha aberta total** — hook não bloqueia nem atrasa nada, em
  nenhuma circunstância, como o proxy da `T13`. **Sem estado ⇒ silêncio e exit 0**, preservando
  intacto o fluxo manual da `T7` (chamada explícita pelo orquestrador) para toda execução fora do
  loop. O estado é consumido **depois** de a linha ser escrita, o que limita a staleness a uma
  janela. Nenhum hook nasce direto no arquivo local de máquina (`DP-R` §22.2 item 1). Sem guardrail
  novo (`DA-10`), sem bump e sem tag (`DE-7`).
- **Cuidado.** `.claude/tools/telemetria.py` **não** é alvo: o hook é **cliente** do CLI que a `T7`
  entregou, e duplicar validação de coluna ali recriaria o gabarito que a `T15` acabou de tirar dos
  prompts. `GOVERNANCA.md` §4.2 também não é alvo — a regra de telemetria medida já está escrita e
  não muda; o que muda é quem a executa.
- **Verificação:** bateria do §3 item 6, os quatro em exit 0 — inclusive
  `python .claude/tools/materializar.py check`, que prova a declaração materializada; suíte `pytest`
  com o piso vigente mais os testes novos.
- **Pronto quando:** um despacho do `scrum-master` produz a linha em `docs/telemetria.tsv` sem
  nenhum turno de agente gasto nisso, e um despacho fora do loop continua funcionando pelo caminho
  manual da `T7`.

## 5. Ordem de execução

`T1` → `T2` → `T3` → `T4` → `T5` → `T6a` → `T6b` → `T7` → `T8` → `T9` → `T10` → `T11` → `T18` →
`T22` → [ratificação do dono] → `T23a` → [rodada de replanejamento: `DP-G` + reescrita dos dossiês
`T19`/`T20`/`T21`] → `T28` → [rodada de replanejamento: `DP-H` (§13) + cards `T29`/`T30`/`T31`] →
[rodada de replanejamento: `DP-K` (§14) + cards `T32`/`T33`] →
**`T19` → `T20` → `T31` → `T32` → `T21a` → `T21b` → `T33` → `T35` → `T36` → `T37` → `T38` → `T39` →
`T23b` → `T24` → **`T40` → `T41` → `T42` → `T43` → `T44`** → `T25` → **`T45` → `T46` → `T47` →
`T48` → `T49` → `T50` → `T51a` → `T51b` → `T52` → `T13`** →
[rodada de replanejamento: `DP-R` (§22) + cards `T53`/`T54`] → ~~`T53` → `T54`~~ *(canceladas por
absorção em 2026-08-15; a matéria corre no `P-0735`, e este plano fica `blocked` até ele fechar)* →
`T29` → `T30` →
[ratificação em lote: `DP-I` e `DP-J`] → `T26` → `T27`** → `T12` → `T14` → `T15` → **`T55`** →
`T16` → `T17` (dono).

**Um card inserido em 2026-08-19, pela `DP-S` (§23).** A `T14` fechou em **ramo B**: mediu que o
consumo do subagente está exposto ao hook e que o que falta é a **identidade da tarefa**, que não é
campo de schema do harness. O dono decidiu a rota, e o card entra **logo depois da `T15` e antes da
`T16`**, por duas razões declaradas. Primeiro, o card edita o Passo 4 do `scrum-master`, que é
exatamente a superfície que a `T16` pilota — pilotar antes e mudar depois invalidaria a medida do
piloto. Segundo, a automação existindo antes do piloto faz o próprio piloto se medir sozinho, que é
o caso de uso que a `T14` perseguia. O denominador do plano passa de **60** para **61**.

**Dois cards inseridos em 2026-08-15, pela `DP-R` (§22).** Entram **em bloco, logo depois da `T13`**
e **antes da `T29`**, na ordem `T53` → `T54`: a `T53` cria a residência e o guarda, a `T54`
regulariza o texto que descreve os dois — inverter faria a doutrina descrever artefato inexistente.
O bloco precede a `T29` por dois motivos declarados. Primeiro, o `G-SURFACE`: a decisão do dono é
estruturante e a superfície se regulariza **no ato**, não como dívida enfileirada. Segundo, o estado
medido: o único instrumento de **capacidade** que o agente tem (a `T13`) hoje só existe na máquina do
dono, de modo que a condição do `GOVERNANCA.md` §4.3 é regra publicada sem meio de cumprimento em
consumidor nenhum. A `T14` deixa de ser executável antes do bloco — o dossiê dela foi reescrito na
mesma rodada e agora depende da `T53`.

**Conciliação de 2026-08-15.** O bloco `T53`/`T54` foi **cancelado por absorção** pelo `P-0735`, que
resolve em forma geral a mesma matéria; este plano fica `blocked` em 49/60 e destrava no fechamento
dele. A fila, ao destravar, retoma em `T29`, e a dependência da `T14` passa para a `RPC-T2`.

**Três cards inseridos em 2026-08-13, pela `DP-Q` (§21), e a `T13` repositionada.** Os três entram
**em bloco**, logo depois da `T48` e antes da `T29`, na ordem `T49` → `T50` → `T51`, pela mesma
razão que ordenou o bloco da `DP-O`: a `T49` é a **régua** na doutrina, a `T50` a materializa no
loop e a `T51` varre a superfície que deriva das duas — inverter faria a varredura medir contra
doutrina incompleta. A **`T13`** (proxy de ocupação) sai do fim da fila e passa a suceder o bloco:
com a queda do teto de tool uses como proxy operante de encerramento (`T49`), ela deixa de ser
instrumento opcional e passa a ser o único critério de **capacidade** disponível ao agente. A
consequência é declarada e aceita: entre a `T49` e a `T13`, o encerramento de janela se apoia só em
**coesão** — o sinal de poluição, que é fatal e imediato — e no fim do plano. Nenhum número
substitui os que caem, por decisão do dono: a matéria de limites se revê inteira no plano próprio
(§21 item 5).

**Quatro cards inseridos em 2026-08-13, à frente da `T29`.** O primeiro é a `T45` (`TK-39`), card
prioritário que parou a fila porque o critério de aceitação estava escrito como contagem, e enquanto
estivesse a `T16` e a `T17` afeririam a coisa errada. Os três seguintes vêm da `DP-P` (§20) e entram
**em bloco**, na ordem `T46` → `T47` → `T48`, por três razões declaradas: a `T46` é a **régua** que
as outras duas aplicam — varrer antes de o `G-SURFACE` estar publicado mede contra doutrina
incompleta, exatamente como a `T42` precedeu a `T43` e a `T44`; a `T47` precede a `T48` porque o
plano consolidado é a referência contra a qual os artefatos publicados se medem, e seu relatório já
traz metade das âncoras da `T48`; e o bloco inteiro precede a `T29` porque é ela que definiria o
artefato `tarefa` lendo um plano com quatro camadas de texto vigente e derrubado convivendo. O bloco
**não introduz ponto de parada** — transcreve decisão enunciada pelo dono —, mas a `T47` e a `T48`
param diante de toda ocorrência de classe (c), que sobe ao dono.

**A `T34` saiu da fila em 2026-08-12**, cancelada por absorção (decisão do dono): a matéria de uso e
teto se revê inteira, em plano próprio, aberto depois que este fechar — o desdobramento é o item 4 da
`T17`. A ratificação em lote perde a `DP-L` e fica com `DP-I` e `DP-J`.

**Dois cards inseridos em 2026-08-12, pela `DP-N` (§17).** Eles entram **logo depois da `T24`**, e
antes da `T25`, por consumo medido: enquanto o prompt do executor mandar escrever no diário, toda
rodada de execução reproduz o desvio que o `TK-35` mediu — e a `T25` (espelho e índices) passa por
`README.md`, onde uma das superfícies da `T41` mora. `T40` antes de `T41` porque a doutrina descreve
o prompt: descrever antes de ele mudar inverte a ordem.

**Três cards inseridos em 2026-08-12, pela `DP-O` (§18).** Entram **em bloco, logo depois da `T41`**,
na ordem `T42` → `T43` → `T44`, por três razões declaradas: a `T42` é a **régua** que as outras duas
aplicam (varrer antes de a resposta na descoberta estar publicada mede contra doutrina incompleta); a
`T43` precede a `T44` porque a doutrina descreve o kit, e o relatório da `T43` já traz metade das
âncoras da `T44`; e o bloco inteiro precede a `T25` porque a `T44` e a `T25` passam pelo mesmo
`README.md` — invertê-las faria a conformidade de vocabulário rodar sobre texto que a sanitização
ainda vai reescrever.

**Cinco cards inseridos em 2026-08-11, pela rodada da `DP-M` (§16).** Eles entram **em bloco e logo
depois da `T33`**, na ordem interna que o dono fixou — `T35` → `T36` → `T37` → `T38` → `T39` —, e o
bloco inteiro **precede a `T23b`** por quatro consumos medidos, não por conveniência:

- **`T35` antes de `T36`** é precondição declarada: a golden rule torna a matriz autoridade exaustiva,
  e publicá-la sobre matriz incompleta põe todo papel vivo fora de conformidade no ato da publicação.
- **`T36` antes de `T37`**: a poda só é legítima depois que existe de onde derivar — sem o item 15
  publicado, remover proibição é perder regra, não mudá-la de residência.
- **`T38` antes de `T39`**: a proibição do `TK-33` item 3 sai porque o laudo perdeu a prosa livre;
  invertê-las abriria uma janela em que a fronteira some com `Observações` ainda no documento.
- **O bloco antes da `T25`** (espelho e índices), pela mesma razão que já posicionou a `T33`: a `T36`
  mexe na tabela de guardrails do `README.md` e na contagem que `check-readme.ps1` compara, e a `T25`
  precisa medir a paridade **já corrigida**. **Antes da `T30`** (utilidade) porque a `T38` muda **o que
  o laudo contém**, e o critério de utilidade se decide sobre o laudo final, não sobre o vigente. E
  **antes da `T26`** (doutrina normativa), que passa em `GOVERNANCA.md` depois que a matriz e a lista
  de guardrails estabilizaram.

Não há colisão de arquivo com a `T24`, cujo dossiê já exclui `.claude/skills/scrum-master/SKILL.md` e
`.claude/agents/pantonic-reviewer.md`. O bloco **não introduz ponto de parada**: os cinco cards
transcrevem decisão já ratificada, e a única parada dura da fila continua sendo a ratificação em lote
de `DP-I` e `DP-J`.

**Um card inserido em 2026-08-11, pelo insumo do dono sobre uso e teto (§15) — e cancelado em
2026-08-12.** A `T34` sucedia a `T30` porque consumia o card "Lições aprendidas na tarefa" que a
`DP-J` acabou de posicionar, e parava na mesma ratificação que `DP-I` e `DP-J`. **Cancelada por
absorção**, por decisão do dono: com a matéria de consumo desdobrada para plano próprio, formar a
`DP-L` aqui seria decidir agora o que aquele plano revê por inteiro — decisão com prazo de validade
de um plano. O corpo do card permanece como **material absorvido** (o insumo do §15, os três números
da medição obrigatória e o conteúdo previsto da decisão), e é dele que o plano seguinte parte. O
regime interino do §3 item 5 continua permitindo que a fila siga, e passa a vigorar até aquela
decisão.

**Dois cards inseridos em 2026-08-11, pela rodada da `DP-K`.** A `T32` (desempate do framework) é
**independente** — não depende de nada e nada depende dela; entra depois da `T31` por ser a segunda
passada curta em `GOVERNANCA.md`, em âncora disjunta (§3.1, contra a §3 da `T31`), e não introduz
ponto de parada. A `T33` (`reviewer`) sucede a `T21b` porque a `T21a` e a `T21b` já reescrevem as 11
ocorrências do corpo do `SKILL.md` do `scrum-master`: rodar antes seria pagar a mesma edição duas
vezes e arriscar regressão. Ela também sucede a `T19`, que reescreve `tests/test_rdo.py`, e **precede
a `T25`** (espelho e índices), que passa depois a medir a paridade já corrigida. A `T19` **não muda**
com esta rodada e segue delegável exatamente como estava.

**Fila reordenada de novo em 2026-08-11, pela rodada da `DP-H`.** A `T19` reabre a fila porque o
insumo que a travava foi consumido: o `close` deixa de ler laudo e passa a receber o `pacote` por
argumento. A `T31` entra logo depois da `T20` porque quita, nos artefatos publicados, o mesmo objeto
morto que os dois dossiês acabam de expurgar — e passa **antes** da `T26` nos dois arquivos que as
duas compartilham. A `T29` (artefato `tarefa`) sucede a `T21b` para não obrigar a reescrever o loop
duas vezes, e **precede a `T26`**, cuja premissa ela derruba: com o artefato definido existe campo
material de `status` por tarefa, e é a `DP-I` que diz onde ele é gravado. A `T30` (utilidade) sucede
a `T19` porque opera sobre o `pacote` já materializado, e **não** o reabre: seu efeito é decisão,
materializada por card autorado depois do aceite. As duas decisões param juntas para ratificação —
`T29` e `T30` são adjacentes exatamente para que o round-trip do dono seja **um**, não dois.

**Fila reordenada em 2026-08-11, por decisão do dono.** A ordem anterior punha `T24`..`T27` antes da
reescrita dos três dossiês; como **nenhuma tarefa pode ser concluída antes de o loop existir** — a
transição `review` → `done` é do `scrum-master` (`DP-G`) —, as tarefas de conformidade passam a
**suceder** o loop. A `T23b` foi executada e ficou `blocked` por esse motivo: o entregável existe e é
a conclusão que falta, então ela reentra na fila logo depois de `T21b`, para ser fechada, não
refeita. A `T28` vem **antes** da `T19` porque reconcilia o texto normativo que as três tarefas
seguintes leem.

`T18`..`T21` entraram no replanejamento de 2026-08-10 (§9) e ficam **antes** da `T12` porque a
reconciliação de gates só é estável depois que a skill para de mudar. Entre elas a ordem é forçada
pelo consumo: a `T19` consome a recomendação que a `T18` emite, e a `T21` cita os comandos e a saída
que a `T19` e a `T20` fixam.

`T22`..`T28` entraram nos replanejamentos de 2026-08-11 (`DP-E`, §10; `DP-G`, §11). A `T22` vem
**antes** de tudo o que materializa vocabulário de `status`, porque executar `T19`/`T20`/`T21` antes
dela seria codificar uma lista que ainda podia mudar; ela decide e **para** para ratificação. A
`T23a` a segue de imediato por ser a residência única — todo o resto aponta para ela. `T23b`, `T24`,
`T25` e `T26` conformam famílias disjuntas de artefatos e são independentes entre si (podem ir em
qualquer ordem, ou em paralelo, se houver janela); a `T27` fecha porque mede o resultado das quatro.
As duas rodadas de replanejamento são **atos de planejamento**, não tarefas do plano — por isso
aparecem entre colchetes.

A `T21` foi partida em `T21a` (passos do loop) e `T21b` (tabelas de roteamento e vocabulário) por
volume medido — ~9 write-clusters num arquivo só, acima da linha de 8 do gate de delegação. Entre as
duas a ordem é forçada: mesmo arquivo, e a `T21b` transcreve tabelas que citam os passos.

Linear, sem ramo condicional. O spike (`T1`) vem antes de tudo porque três decisões e dois hooks se
apoiam em premissas de plataforma que ninguém mediu. As decisões (`T2`..`T4`) precedem os
instrumentos porque cada uma **fecha o dossiê** de uma tarefa posterior (`DA-4`) — invertê-las
publicaria tarefa aberta. A rubrica (`T5`) precede a ferramenta que a calcula, e a doutrina
(`T6a`/`T6b`) precede tudo o que a materializa, pela mesma razão que ordenou o `P-0732`: ferramenta
que verifica regra não escrita mede ruído. A doutrina foi partida em duas por volume medido: a
`T6a` grava papéis e fronteira de registro, a `T6b` grava a integridade do contexto em cinco
superfícies — juntas estouravam o teto da classe. Entre os instrumentos, `telemetria.py` (`T7`) vem primeiro por ser o
menor pedaço que prova o padrão de documental-por-função antes de ele ser aplicado ao artefato
grande. Os papéis (`T10`, `T11`) vêm depois dos instrumentos que eles chamam. A reconciliação
(`T12`) segue imediatamente a criação da skill, para que a duplicata de gates não sobreviva a uma
única tarefa. Os hooks (`T13`, `T14`) vêm por último entre os instrumentos porque ambos podem ser
declarados inviáveis pela `T1` sem travar nada. O enxugamento (`T15`) só é possível depois que os
instrumentos existem, e o piloto (`T16`) só mede algo real depois do enxugamento. O aceite (`T17`)
fecha.

**Três round-trips do dono são previstos e inevitáveis:** ratificação da `T2`, da `T3` e da doutrina
de contexto (porque toca a Regra 2 do CLAUDE.md global). Se `T2` e `T3` forem executadas em
sequência próxima, suas ratificações podem ser levadas ao dono em lote — mas nenhuma das duas
grava decisão sem aceite. O terceiro **já foi gasto**: a `DA-11` foi ratificada com o texto à vista
antes de a `T6b` ser escrita, de modo que a `T6b` chega ao executor como transcrição, sem parada.

`T2`, `T3`, `T4`, `T5`, `T6a`, `T6b`, `T10`, `T11`, `T12`, `T20`, `T21a`, `T21b`, `T22`, `T23a`,
`T23b`, `T24`, `T25`, `T26`, `T27`, `T28`, `T29`, `T30`, `T31` e `T17` são Opus (decisão, doutrina e
redação canônica);
`T1`, `T7`, `T8`, `T9`, `T13`, `T14`, `T15`, `T16`, `T18` e `T19` são Sonnet; a validação final da
`T17` é do dono.

**Um quarto round-trip do dono** entrou com a `DP-E`: a ratificação da lista final de estados
(`T22`). Ele é inevitável — linguagem ubíqua é decisão do dono do domínio — e é o único ponto de
parada dura de `T22`..`T27`.

**Um quinto round-trip** entrou com a `DP-H`: a ratificação, **em lote**, da `DP-I` (artefato
`tarefa`, `T29`) e da `DP-J` (utilidade, `T30`). É inevitável pela mesma razão — o que a tarefa *é* e
o que se retém dela são conceito do framework, e conceito é do dono —, e é lote por desenho: as duas
tarefas são adjacentes na fila para que a parada seja uma só. Entre `T19` e `T25` não há nenhuma
parada dura.

## 6. Riscos

| Risco | Mitigação |
|---|---|
| Premissa de plataforma falsa derrubar o desenho no meio da execução | `T1` mede as três premissas antes de qualquer implementação; `DA-1` declara que a queda de uma delas é replanejamento, não improviso do executor |
| Loop autônomo virar bomba de custo sem o dono na cadeira | Tetos numéricos obrigatórios da `T3` (retentativa, tarefas por janela, consumo acumulado) e parada dura em ponto de decisão; `T13` entrega o critério de encerramento de janela mesmo se o hook for inviável |
| Reviewer-modelo aprovar tudo (leniência) | `DA-7`: a camada mecânica é autoridade sobre o que mede e trava a marcação; `DA-6`: bloqueante vermelha reprova independentemente do percentual; a rubrica é confrontada com tarefas já fechadas na `T5` |
| O dono perder consciência situacional ao sumir o round-trip por tarefa | O RDO é o instrumento compensatório (`DA-5`), e a `T16` **registra cada acionamento do dono pela causa** que o motivou, classificada pelo §19 — o piloto mostra **por que** o dono foi, ou não foi, chamado. Nenhuma contagem de acionamentos entra como controle: a cegueira aparece como acionamento legítimo que deixou de acontecer, não como número que subiu ou desceu |
| RDO virar terceira fonte e divergir do diário | `DA-5` corta a fronteira antes de existir ferramenta, e a `T6a` grava a fronteira na doutrina antes de a `T8` implementar |
| Duplicata de gates entre `proximo-passo` e `scrum-master` | `T12` é tarefa própria, imediatamente após a criação da skill, e exige uma única ocorrência normativa verificada por Grep |
| Enxugamento de prompt remover regra junto com formato | Regra de corte escrita na `T15` (sai o formato, fica a regra) e medição antes/depois; o eixo de justificação de `GOVERNANCA.md` §3 proíbe trocar guardrail por economia |
| Executar o plano usando a própria ferramenta que ele constrói | Invariante 1 do §3: o plano se executa pelo fluxo vigente até a `T16`, que é o piloto |
| Percentual de sucesso virar número de conforto sem poder de série | `DA-6`: percentual é calculado por fórmula fixa (`T5`) e o CLI **rejeita** percentual passado como argumento (`T8`) |

## 7. Fora de escopo (explícito)

- **Propagação aos repositórios derivados** (`DA-3`), com **gatilho registrado**: a promoção do
  scrum-master, do reviewer e dos instrumentos a kit distribuído entra por **plano próprio**,
  aberto pelo resultado do piloto da `T16`. Nenhuma tarefa deste plano toca um derivado.
- **Guardrail novo em `GOVERNANCA.md` §7** (`DA-10`).
- **Bump, tag e instrução de migração por número de versão** (`DE-7`).
- **Execução paralela de tarefas.** O loop é estritamente sequencial, por decisão do dono; paralelismo
  não é postergado, é recusado neste desenho.
- **Qualquer alteração no `P-0733-divida-do-hub`** além de emprestar tarefas ao piloto da `T16`. Os
  12 tíquetes daquele plano seguem a rota dele.
- **Tíquetes de backlog alheios ao assunto**, que continuam precisando de tarefa própria: `TK-10`
  (condensação do diário — note que `DA-5` reduz a **causa**, mas não condensa o que já está lá),
  `TK-08`, `TK-04`, `TK-06`, `TK-07`, `TK-15`, `TK-17`.

## 8. Achados abertos deste planejamento

- **Interação entre `DA-5` e `TK-10`:** a fronteira nova faz o diário parar de crescer, mas as 937
  linhas atuais continuam lá. Quando `TK-10` for executado, a condensação deve considerar que as
  "Notas de execução" históricas **não** migram para RDO — são registro histórico e ficam onde
  estão, pela mesma régua que preservou os bullets `Consumo:` anteriores à regra da fonte única.
- **`docs/DIARIO_DE_OBRAS.md` linha 15** descreve a `SPRINT-PANTONICV2` como "7 estágios
  encadeados", já corrigida em relação ao achado `TK-18`; sem ação.

## Dossiês fechados por decisão

*(preenchido pelas tarefas `T2`, `T3` e `T4`, conforme `DA-4`)*

### `DP-A` — Transporte do pacote de retorno *(fechada pela `T2`, ratificada pelo dono em 2026-08-08)*

> **PARCIALMENTE REVOGADA em 2026-08-10/11 — não ler sem o §9 (`DP-D`), o §10.3 (`DP-E`) e o §13
> (`DP-H`) à vista.** **Permanecem normativos** o princípio do transporte por arquivo, a medição que
> o sustenta e a proibição de prosa de subagente atravessar o orquestrador. **Caiu o objeto:** o
> *pacote de retorno* de oito campos devolvido pelo executor **não existe** (`DP-D`, `D2`); o RDO é
> criado no **fechamento**, pelo `scrum-master`, e não no início (`D3`); o reviewer recebe o **mesmo
> contexto do executor**, não o pacote em arquivo (`D4`); e o retorno do executor foi reduzido ao
> sinal de `review` ou `blocked`, e nada mais (`DP-N`, §17). Em consequência, os blocos **"Campos
> fixos do pacote de retorno"**, **"Linhas de contexto"** e **"Dossiês dependentes"** abaixo são
> **registro do que foi decidido em 2026-08-08**, não instrução vigente: o `pacote` que existe hoje
> vive **dentro do laudo** (`DP-H`, item 4) e o trio `entregue`/`parcial`/`bloqueado` saiu do
> vocabulário de `status` (`DP-E`; lista final na `DP-F`). O texto abaixo **não é reescrito** —
> decisão ratificada não muda de conteúdo, só ganha a marca do que a derrubou.

**Decisão: transporte por arquivo (opção `a`).** O executor grava o pacote de retorno no RDO da
tarefa e devolve **uma linha** de confirmação; o reviewer lê o arquivo pelo caminho recebido nessa
linha e devolve **duas linhas** de veredito. O orquestrador nunca ingere o corpo do pacote.

**Medição que sustenta a escolha.** Amostra de **29 handovers** já escritos na série mais recente
(`V2E-*`, `V2P-*`, em `docs/DIARIO_HISTORICO.md`): mediana **2 839 chars**, média 2 792, p90 3 926,
máximo 5 345 — em PT-BR ≈ **890 tokens de mediana e ~1 670 no maior**. Pegada por tarefa no contexto
do orquestrador, contando o despacho dos dois subagentes (~1,5k tokens, comum às três opções):

| opção | pegada por tarefa | tarefas por janela útil (~150k) |
|---|---|---|
| (a) por arquivo | ~1,6k tokens | ~90 |
| (b) por contexto | ~3,4k tokens (~4,0k no p90) | ~38 (~30 no p90) |
| (c) híbrido | entre as duas, com dois caminhos a manter | indeterminado por desenho |

O número de (b) é o dobro do de (a) porque o pacote entra **duas vezes** no contexto do
orquestrador: como resultado da chamada do executor e de novo como argumento do despacho ao
reviewer. Sob (a), o limite da janela deixa de ser o gargalo — quem a encerra passa a ser a política
de autonomia da `T3`, que é onde esse controle deve morar.

**Argumento decisivo, além do número.** A `DA-5` já obriga o pacote a virar RDO. A opção (b) não
elimina essa escrita: acrescenta uma cópia em contexto **por cima** dela. Sob (a) o arquivo não é
custo adicional — é o registro canônico que a `DA-5` manda produzir de qualquer forma, e o
transporte passa a ser um subproduto dele.

**Alternativas rejeitadas.** (b) *por contexto*: paga o mesmo RDO e mais ~1,8k tokens por tarefa em
duplicata, cortando a janela a menos da metade, sem que o orquestrador precise do conteúdo para
rotear — quem roteia é o veredito calculado (`DA-6`), não a prosa. (c) *híbrido por tamanho*: custa
dois transportes para especificar, testar e manter, mais um limiar numérico que envelhece, e o ramo
"pequeno" não economiza nada, porque a escrita do RDO acontece igual; `rdo.py` (`T8`) e o reviewer
(`T10`) passariam a ter dois modos de entrada em troca de nenhuma economia mensurável.

**Base de plataforma.** A sonda 4 da `T1` confirmou que arquivo escrito por um subagente é legível
por outro subagente da mesma sessão — a premissa do transporte por arquivo está medida, não suposta.

#### Campos fixos do pacote de retorno (arquivo)

Residência: seção `## Execução` do RDO da tarefa, `docs/RDO/<plano>-<tarefa>-<slug>.md`. Campos
obrigatórios, na ordem, com teto de linhas por campo — **teto total 44 linhas**. Campo sem conteúdo
é preenchido com `nenhum` explícito; campo ausente é pacote inválido.

| campo | teto | conteúdo |
|---|---|---|
| `tarefa` | 1 | identificador de plano e tarefa |
| `status` | 1 | `entregue` \| `parcial` \| `bloqueado` |
| `arquivos_tocados` | 15 | um por linha: caminho + `criado`/`editado`/`removido` |
| `desvios_do_dossie` | 8 | o que o dossiê mandava e saiu diferente, com motivo; ou `nenhum` |
| `verificacao` | 6 | cada comando da bateria do §3 com o exit code **colado**, não parafraseado |
| `achados` | 8 | o que apareceu fora do escopo, cada um com rota (tíquete, ou `sem ação`) |
| `orcamento` | 1 | teto declarado × tool uses gastos |
| `pendencia_para_o_dono` | 4 | decisão de arquitetura ou de requisito levantada pela execução; ou `nenhuma` |

O teto por campo é **do formato**, e mora no template de `rdo.py` (`T8`) — não no prompt de nenhum
agente (invariante 3 do §3). Estouro de teto é erro do CLI, não advertência em prosa.

#### Linhas de contexto (o que de fato atravessa o orquestrador)

Executor, **1 linha**, gramática fixa:

`<tarefa> <status> rdo=<caminho> tools=<gastos>/<teto> pendencia=<sim|nao>`

Reviewer, **2 linhas**, gramática fixa:

`<tarefa> <veredito> <percentual> bloqueante=<dimensão|nenhuma>`
`laudo=<caminho>`

Nada além dessas três linhas entra no contexto do orquestrador por tarefa. Prosa devolvida na
resposta de um subagente é violação do transporte, não zelo.

#### Dossiês dependentes — o que a `T2` fecha e o que continua aberto

- **`T8` (`rdo.py`)** — fechado por esta decisão: os **campos do pacote de retorno** e seus tetos
  (tabela acima) são a entrada do subcomando `new`/`close`, e o `close` valida teto por campo.
  **Continua aberto:** esquema da tarefa no plano (`T4`, subcomando `new`) e rubrica/fórmula (`T5`,
  subcomando `laudo`). **`T8` segue não delegável** até `T4` e `T5` fecharem.
- **`T10` (`pantonic-reviewer`)** — **fechado por esta decisão, integralmente no que dependia da
  `DP-A`**: "ler pacote de retorno" passa a significar *abrir o RDO no caminho recebido na linha de
  confirmação do executor*; a lista de ferramentas do agente precisa de leitura de arquivo do
  repositório e escrita apenas no caminho do laudo, sem nenhum modo de entrada por contexto. As
  demais dependências da `T10` (`T5` rubrica, `T6a` matriz de modelo, `T8` `rdo.py laudo`, `T9`
  evidência) são **precedência de ordem**, não dossiê aberto — todas a precedem no §5.
- **`T11` (`scrum-master`)** — fechado por esta decisão: o passo "recepção do pacote de retorno" do
  fluxo é *ler a linha de confirmação, extrair o caminho do RDO e repassá-lo ao reviewer como
  caminho* — o scrum-master **não abre o RDO**; e o passo "leitura do veredito" consome as duas
  linhas do reviewer. **Continua aberto:** tabela de roteamento e tetos (`T3`). **`T11` segue não
  delegável** até `T3` fechar.

### `DP-B` — Política de autonomia, tetos e escalada *(fechada pela `T3`, ratificada pelo dono em 2026-08-08)*

> **PARCIALMENTE REVOGADA em 2026-08-10/13 — não ler sem o §9 (`DP-D`), o §10.3 (`DP-E`), a `DP-F`,
> o §17 (`DP-N`) e o §21 (`DP-Q`) à vista.** **Permanecem normativos** o teto de retentativa (1), a
> ordem de precedência do bloco A e a fronteira "obriga parada × segue com registro". **Caíram os
> tetos que governam fluxo (`DP-Q`, §21):** o roteamento por estouro de teto de tool uses (`A4`) e
> os dois números de fim de janela do bloco B (dez tarefas fechadas e 900 k tokens acumulados) —
> número arbitrário não recusa entrega, não roteia, não encerra tarefa e não encerra janela; a
> medição segue alimentando `docs/telemetria.tsv` sem exceção, e o que encerra janela são coesão e
> capacidade (`GOVERNANCA.md` §4.3). O restante do bloco B permanece. **Caiu o
> domínio de entrada:** a regra `A2` lê um *pacote de retorno* que a `DP-D` (`D2`) apagou, e o trio
> `entregue`/`parcial`/`bloqueado` do bloco *"Domínio de entrada da tabela"*, de `A3` e de `A5` saiu
> do vocabulário de `status` (`DP-E`), substituído pela lista final da `DP-F`; o executor não devolve
> mais linha de status alguma (`DP-N`). A tabela de roteamento **vigente** é a transcrita em
> `.claude/skills/scrum-master/SKILL.md` pela `T21b`, contra a lista final. O texto abaixo **não é
> reescrito** — decisão ratificada não muda de conteúdo, só ganha a marca do que a derrubou.

**Decisão: três tetos numéricos e uma tabela de roteamento por precedência.** O loop nunca decide
continuar por percepção — continua enquanto nenhuma regra de parada casa e nenhum contador estoura.

#### Tetos

| teto | valor | o que conta | onde o loop lê |
|---|---|---|---|
| retentativas por tarefa reprovada | **1** | re-despachos do **mesmo dossiê** após laudo reprovado | contador do loop, zerado no início de cada tarefa |
| tarefas por janela | **10** | tarefas fechadas (`aprovado` ou `aprovado com ressalva`) desde o início da janela | contador do loop |
| consumo acumulado por janela | **900 k tokens** | soma do `tokens_k` das tarefas da janela | `docs/telemetria.tsv`, linha apendada a cada tarefa |

O teto de **tool uses por tarefa** não é decidido aqui: continua sendo o da classe registrada no
dossiê (`GOVERNANCA.md` §3). Esta decisão apenas define o que o loop faz quando ele estoura
(regra `A4`).

**Medição que sustenta.** Série de `docs/telemetria.tsv`, 99 tarefas: mediana **85 k tokens** e
**29 tool uses** por tarefa, p90 159 k/52, máximo 310 k/136; cadência real de **10 a 20 tarefas por
dia** de trabalho. Dez tarefas na mediana somam 850 k — o teto de consumo em 900 k morde primeiro
quando a janela pega tarefas mais pesadas que a mediana, que é o comportamento protetivo desejado, e
o de tarefas morde primeiro quando elas são leves. O teto de retentativa vem da mesma série: **4 das
99 tarefas** precisaram de segunda rodada, e a única que passou disso (`V2E-T9`) foi resolvida
**reescrevendo o dossiê** e partindo a tarefa, não repetindo a execução — reprovar duas vezes é
defeito de dossiê, e dossiê é domínio do planejamento (`~/.claude/CLAUDE.md` Regra 8), não do loop.
O teto de ingestão do transporte por arquivo (~90 tarefas/janela, `DP-A`) **não** é o que encerra a
janela: o gargalo é apetite de risco, e é onde este teto mora.

#### Domínio de entrada da tabela

Da **linha do executor** (`DP-A`): `status` ∈ {`entregue`, `parcial`, `bloqueado`}, `pendencia` ∈
{`sim`, `nao`}, `tools` gastos × teto. Da **linha do reviewer**: `veredito` ∈ {`aprovado`,
`ressalva`, `reprovado`} e `bloqueante` ∈ {nome da dimensão, `nenhuma`}. Este é o **domínio de saída
do laudo**: a rubrica da `T5` produz valores deste conjunto e o CLI da `T8` recusa qualquer outro —
a `T5` não o redefine. Por `DA-6`, `bloqueante` ≠ `nenhuma` implica `veredito` = `reprovado`, de modo
que a combinação "aprovado com bloqueante vermelha" não chega à tabela.

#### Tabela de roteamento — bloco A: o que fazer com a tarefa

Regras em **ordem de precedência**; a primeira que casa vence e nenhuma outra é avaliada.

| # | condição | ação do scrum-master |
|---|---|---|
| `A1` | notificação de queda do subagente (sem bloco `<usage>`) | uma tentativa de retomada por `SendMessage` ao mesmo `agentId` com "o que falta"; registra `PARCIAL — trecho pré-queda não medido`. Retomou → segue por `A2`..`A9`; não retomou → **PARA** |
| `A2` | pacote de retorno ausente ou inválido (campo faltando ou teto de campo estourado — erro do `rdo.py close`) | um reenvio de **formato** ao mesmo executor; **não** consome a retentativa de conteúdo. Inválido de novo → **PARA** |
| `A3` | `status=bloqueado` | despacha o reviewer assim mesmo, fecha o RDO como `bloqueado` → **PARA** |
| `A4` | `tools` gastos > teto declarado (estouro), com qualquer `status` | despacha o reviewer, fecha o RDO com o estouro registrado; **nunca retenta** — estouro é decomposição errada (`GOVERNANCA.md` §3) → **PARA**, replanejamento |
| `A5` | `status=parcial` sem estouro | despacha o reviewer e trata o resultado como reprovação para efeito de contador (cai em `A6` ou `A7`) |
| `A6` | `veredito=reprovado` e retentativas gastas = 0 | re-despacha o **mesmo** executor com o dossiê original + caminho do laudo + as dimensões vermelhas, **sem reescrever o dossiê**; contador := 1 → segue |
| `A7` | `veredito=reprovado` e retentativas gastas = 1 | fecha o RDO como `reprovado` → **PARA** |
| `A8` | `veredito=ressalva` e `bloqueante=nenhuma` | fecha o RDO como `aprovado com ressalva`; cada ressalva e cada item do campo `achados` vira achado **com rota** (tíquete ou `sem ação`) no RDO → segue |
| `A9` | `veredito=aprovado` e `bloqueante=nenhuma` | fecha o RDO como `aprovado` → segue |

`A1`..`A9` cobrem o produto cartesiano do domínio: `A1`/`A2` esgotam a ausência de pacote válido;
com pacote válido, `status` ∈ {`bloqueado`} cai em `A3` e o estouro de orçamento em `A4`,
independentemente do resto; o que sobra é `status` ∈ {`entregue`, `parcial`} dentro do teto, onde
`A5` reduz `parcial` ao mesmo tratamento de reprovação e `A6`..`A9` esgotam os três vereditos
possíveis. Nenhuma célula pede juízo: toda condição é valor de campo ou contador.

#### Tabela de roteamento — bloco B: continuar ou encerrar a janela

Avaliado **depois** de `A6`..`A9`, sobre a tarefa já fechada, e só quando o bloco A disse "segue".

| # | condição | ação do scrum-master |
|---|---|---|
| `B1` | `pendencia=sim` na tarefa recém-fechada | leva a pendência ao dono no relatório de encerramento → **PARA**, mesmo com veredito `aprovado` |
| `B2` | tarefas fechadas na janela = 10 **ou** consumo acumulado ≥ 900 k tokens | encerra com relatório de janela → **PARA** (encerramento normal, não falha) |
| `B3` | a próxima tarefa do plano é recusada pelo `G-PLANREADY` ou pelo gate de delegação | não delega → **PARA**, com o que falta fechar |
| `B4` | nenhuma das anteriores | despacha a próxima tarefa do plano, sempre sequencial |

#### O que obriga parada × o que segue com registro

A fronteira do que é **ponto do dono** é herdada de `.claude/skills/proximo-passo/SKILL.md` — decisão
de arquitetura ou de requisito sim, evento intrínseco do plano não — e não é redecidida aqui. O que
`DP-B` fixa é como cada classe **chega** ao loop, porque o scrum-master não classifica prosa:

- **Obriga parada:** decisão de arquitetura ou requisito, que chega **sempre** pelo campo
  `pendencia_para_o_dono` do pacote (`B1`) — o executor é obrigado a levantá-la ali, e um achado que
  invalida a rota do plano é esse caso; executor `bloqueado` (`A3`); reprovação depois da última
  retentativa (`A7`); estouro de teto (`A4`); teto de janela (`B2`); plano não-pronto (`B3`).
- **Segue com registro:** ressalva não bloqueante e achado fora de escopo **com rota**, ambos pelo
  campo `achados` (`A8`) — a rota é escrita pelo executor no RDO, e o loop só verifica que ela
  existe.

A rede de segurança da classificação é mecânica em dois pontos: a dimensão bloqueante do laudo
(`DA-6`) e a autoridade da camada mecânica sobre o que ela mede (`DA-7`). Nenhum dos dois depende do
scrum-master ler o corpo do RDO — ele nunca o abre (`DP-A`).

**Alternativas rejeitadas.** *Teto por tempo ou calendário*: não mede risco e a série mostra
duração de 41 s a 24 420 s para consumo comparável. *Teto por percentual de contexto do
orquestrador*: o modelo não enxerga a própria ocupação (§2 item 3, medido pela `T1`) — é o proxy que
a `T13` ainda vai construir, e até lá o encerramento é numérico. *Zero retentativa*: gastaria turno
do dono em falha trivial que uma re-execução com o laudo em mãos resolve. *Duas retentativas*: sem
respaldo na série — nenhuma tarefa medida foi salva por uma terceira execução do mesmo dossiê.
*Seis tarefas por janela*: menos de meia jornada, multiplica os round-trips que a iniciativa existe
para eliminar. *Vinte tarefas por janela*: raio de estrago de uma jornada inteira antes de o piloto
da `T16` ter medido qualquer coisa.

#### Dossiês dependentes — o que a `T3` fecha

- **`T11` (`scrum-master`)** — **fechado**. O passo "roteamento pela tabela da `T3`" é aplicar
  `A1`..`A9` e depois `B1`..`B4`, nesta ordem, transcritos sem interpretação. O passo "decisão de
  continuar ou encerrar a janela" é o bloco B. Os contadores que o loop mantém são três, e só três:
  retentativas da tarefa corrente, tarefas fechadas na janela e consumo acumulado (lido da linha que
  a telemetria já apenda). O encerramento por proxy de contexto continua sendo escopo da `T13`;
  enquanto ele não existir, `B2` é o único critério de encerramento por ocupação. **`T11` não tem
  mais dossiê aberto** — o que resta é precedência de ordem (`T4`..`T10` a precedem no §5).
- **`T10` (`pantonic-reviewer`) — adendo.** A `T2` já a fechou integralmente; esta decisão apenas
  fixa o **domínio** do que ela emite: `veredito` ∈ {`aprovado`, `ressalva`, `reprovado`} e
  `bloqueante=<dimensão|nenhuma>` na segunda linha da gramática fixa da `DP-A`.
- **`T5` (rubrica) — restrição herdada, não dossiê aberto.** A rubrica produz valores do domínio
  acima; ampliar o conjunto de vereditos tornaria a tabela parcial e exige voltar a esta decisão.

### `DP-C` — Formato estruturado da tarefa no plano *(fechada pela `T4`, 2026-08-08)*

**Decisão: convenção de linhas rotuladas, extraída por expressão regular (opção `b`) — ratificada,
não inventada.** A tarefa continua sendo prosa em Markdown dentro do próprio `docs/plans/P-*.md`; o
que esta decisão acrescenta é uma **gramática fixa** para o cabeçalho e para os rótulos que já
existem, mais um conjunto fechado de valores para `classe` e `modelo`. Não há segundo lado: o texto
que o dono edita é literalmente o texto que o script lê.

**Medição que sustenta a escolha.** Varredura dos **15 planos** de `docs/plans/`, **129 tarefas**
com cabeçalho `### T…`:

| fato medido | valor |
|---|---|
| cabeçalhos que já casam `^### (T[0-9a-z]+) — (.+?) \[` | **119 / 129 (92%)** |
| tarefas com `Objetivo` | 116 (90%) |
| tarefas com `Pronto quando` | 116 (90%) |
| tarefas com `Arquivos-alvo` | 104 (81%) |
| tarefas com `Verificação` | 93 (72%) |
| rótulos distintos, depois de normalizados | **130** |
| cabeçalhos com `classe` e `teto` | 18 e 17 — só neste plano |

Nos cinco planos mais recentes (`P-0730`..`P-0734`, 78 tarefas) os três primeiros campos aparecem em
95% delas. O formato, portanto, **já convergiu na prática**; o que não convergiu é o vocabulário — 130
rótulos distintos para quatro campos que importam, e duas grafias da mesma classe dentro deste único
plano (`classe redação/planejamento` e `classe redação de doutrina`, ambas a linha ≤30 de
`GOVERNANCA.md` §3). O esquema é extraído do corpus, não imposto sobre ele: é isso que zera o custo de
migração exigido pelo critério de decisão.

#### Gramática do cabeçalho

```
### <ID> — <título> [<modelo> · classe <classe> · teto <N>]<sufixo livre>
```

- **`<ID>`** — `T` seguido de dígitos e, opcionalmente, de uma letra minúscula (`T4`, `T3a`, `T12b`).
  O sufixo de letra é medido, não hipotético: planos partem tarefas na execução.
- **`<modelo>`** ∈ `Opus` | `Sonnet` | `Haiku`, **sem marcação de ênfase** — `[**Opus**]` do
  `P-0729` é deriva de grafia, não um valor diferente.
- **`<classe>`** — conjunto fechado de cinco *slugs*, um por linha da tabela de tetos de
  `GOVERNANCA.md` §3, que continua sendo a autoridade sobre o número:

  | slug | linha de `GOVERNANCA.md` §3 | teto |
  |---|---|---|
  | `mecanica` | Mecânica / pontual | 15 |
  | `implementacao` | Implementação padrão | 40 |
  | `comportamental` | Comportamental multi-camada | 60 |
  | `investigacao` | Investigação / mapeamento | sem default — prescrito no dossiê |
  | `redacao` | Redação de doutrina / planejamento | 30 |

- **`<N>`** — sempre escrito, para que o cabeçalho seja autossuficiente. Deve ser **igual ao teto da
  classe**, exceto em `investigacao`, onde qualquer valor é aceito porque a classe não tem default.
  Teto acima do default da classe é erro, não licença: escolher classe mais generosa depois do
  estouro já é falsificação da série (`GOVERNANCA.md` §3), e escolher teto mais generoso dentro da
  classe é a mesma falsificação por outra porta.
- **`<sufixo livre>`** — tudo depois do `]` é ignorado pelo parser (medido: `— **done (2026-08-05)**`,
  `— *herdado de `P-0722` Fase 1*`, `— *`C-01` (a)*`). **O status da tarefa nunca é lido do
  cabeçalho**: ele mora no diário e no RDO. Admitir status no cabeçalho criaria a segunda fonte da
  verdade que a `DA-5` acabou de eliminar.

#### Gramática do campo

```
- **<Rótulo>:** <conteúdo>
```

Primeira linha no nível zero de indentação do bloco da tarefa; a **continuação** é toda linha
seguinte mais indentada, até o próximo `- **` de nível zero ou o próximo cabeçalho `##`/`###`.

A **chave** do campo é o rótulo normalizado: recorta-se o texto antes do primeiro ` — `, `,` ou `(`,
minusculiza-se, removem-se acentos e os espaços viram hífen. É essa normalização que faz `Conteúdo —
para cada dimensão, cinco campos`, `Forma, nesta ordem` e `Por que não numerada (medido na T3…)`
caírem, respectivamente, em `conteudo`, `forma` e `por-que-nao-numerada` — e é por isso que as 129
tarefas já escritas são legíveis sem uma única edição.

#### Esquema de campos

| chave | rótulo canônico | obrigatoriedade | conteúdo |
|---|---|---|---|
| `objetivo` | `Objetivo` | **obrigatório** | o que a tarefa entrega e por quê |
| `arquivos-alvo` | `Arquivos-alvo` | **alternância** (ver abaixo) | caminho exato + verbo (`cria`/`edita`/`remove`) |
| `entregavel` | `Entregável` | **alternância** (ver abaixo) | o artefato produzido, quando ele não é arquivo do repositório |
| `verificacao` | `Verificação` | **obrigatório** | comandos e resultado esperado; a bateria do §3 pode ser referenciada |
| `pronto-quando` | `Pronto quando` | **obrigatório** | critério verificável, sem juízo |
| `dossie-fechado-por` | `Dossiê fechado por` | opcional, **reservado** | lista de tarefas; enquanto uma delas não estiver `done`, a tarefa **não é delegável** |
| qualquer outro | livre | opcional | preservado verbatim em `extras[<chave>]`, **nunca interpretado** |

**A alternância `arquivos-alvo` × `entregavel`** é achado da medição, não desenho de gabinete: as
únicas tarefas do corpus sem `Arquivos-alvo` que não são investigação são as de decisão, e todas as
quatro usam `Entregável` no lugar. **Exatamente um dos dois é obrigatório.** Sem essa regra, a
fidelidade de escopo do laudo (`T9`: arquivos tocados ⊆ arquivos-alvo declarados) não teria âncora em
tarefa de decisão e a dimensão viraria `não se aplica` por omissão de formato.

**`dossie-fechado-por` é promovido a campo reservado** porque é o que torna mecânica a regra `B3` da
`DP-B` ("a próxima tarefa é recusada pelo `G-PLANREADY`"): o scrum-master confronta a lista com o
status das tarefas no índice do diário, em vez de julgar prosa. As quatro ocorrências do corpus estão
todas neste plano e já têm essa semântica.

#### Política de plano legado

**Leitura tolerante, autoria estrita.**

1. **Plano fechado (`done`/`superseded`) não é reescrito** — mesma régua que preservou os nomes de
   plano em `DP-G5`. Reescrever plano fechado para satisfazer formato é invalidar registro, que é o
   custo que o critério de decisão proibiu.
2. O parser lê o que existe. Cabeçalho sem `classe`/`teto` produz campos nulos, não erro de leitura.
3. **`rdo.py new` (`T8`) falha ruidosamente** e nomeia o que faltou; `--esquema-legado` com
   `--modelo`/`--classe`/`--teto` explícitos é o único caminho para prosseguir, e o RDO registra
   `esquema=legado`. O supridor é argumento de linha de comando justamente para ficar visível no
   histórico do comando, não embutido no documento.
4. **Plano vivo com tarefa não iniciada é retrofitado por ato de planejamento**, nunca pela execução
   — a classe é escolhida no dossiê antes de delegar (`GOVERNANCA.md` §3), e escolher classe é
   planejar. Único caso hoje: **`P-0733`**, 12 tarefas não iniciadas com cabeçalho `[Opus]`/`[Sonnet]`
   sem `classe`/`teto`. Fora do escopo desta tarefa (que não edita outro plano): roteado como
   `TK-24`.
5. Planos autorados a partir de agora nascem conformes — a instrução vai para o `pantonic-planner` na
   `T15`.

**Alternativas rejeitadas.** (a) *bloco estruturado por tarefa dentro do próprio `.md`* — um bloco
cercado que reafirme objetivo e arquivos-alvo cria a deriva de dois lados **dentro de um arquivo só**,
que é pior que a de dois arquivos: nenhum diff a denuncia, porque os dois lados mudam no mesmo
commit ou nenhum muda. Substituir a prosa pelo bloco derruba a legibilidade que o critério exige
preservar, e a migração custaria 129 tarefas, 116 delas em plano fechado. (c) *arquivo de dados irmão
do plano* — dois arquivos, um que o humano edita e outro que o loop lê; a primeira divergência é
silenciosa e permanente, e é a duplicata que `GOVERNANCA.md` §3.1 manda apagar. Migração: 15 arquivos
a autorar, 12 deles para planos fechados que não podem ser invalidados. (d) *front-matter YAML por
plano* — carrega metadado do plano, não da tarefa; não responde à pergunta.

**Argumento decisivo, além do número.** É o mesmo da `DP-A`: o formato escolhido não acrescenta
artefato: ele **ratifica o artefato que já existe e que teria de existir de qualquer jeito**. Sob (b)
a resistência à deriva não depende de disciplina de ninguém — ela é estrutural, porque não há dois
lados para divergir.

#### Instrução de autoria (a ser incorporada ao `pantonic-planner` pela `T15`)

> Toda tarefa de plano é escrita como `### <ID> — <título> [<modelo> · classe <slug> · teto <N>]`,
> com `<modelo>` em {`Opus`, `Sonnet`, `Haiku`} sem ênfase, `<slug>` em {`mecanica`,
> `implementacao`, `comportamental`, `investigacao`, `redacao`} e `<N>` igual ao teto da classe em
> `GOVERNANCA.md` §3 (livre só em `investigacao`). O corpo traz, como linhas `- **Rótulo:**` no nível
> zero: `Objetivo`, `Verificação`, `Pronto quando` e **exatamente um** entre `Arquivos-alvo` e
> `Entregável`. `Dossiê fechado por` é escrito quando a tarefa depende de decisão ainda não fechada.
> Qualquer outro rótulo é livre e não é interpretado. Status de tarefa **não** vai no cabeçalho.

#### Dossiês dependentes — o que a `T4` fecha

- **`T8` (`rdo.py`)** — fechado no que dependia da `DP-C`: o subcomando `new` recebe o caminho do
  plano e o `<ID>`, localiza o cabeçalho, aplica a gramática acima e falha com exit ≠ 0 em cabeçalho
  fora do padrão, `classe` fora do conjunto, `teto` acima do default da classe, campo obrigatório
  ausente ou ausência da alternância `arquivos-alvo`/`entregavel`. `extras` entram no RDO verbatim.
  **Continua aberto:** rubrica e fórmula (`T5`, subcomando `laudo`). **`T8` segue não delegável até a
  `T5` fechar** — e essa é a última dependência: `T2`, `T3` e `T4` já fecharam as suas.
- **`T11` (`scrum-master`) — adendo.** A `DP-B` já a fechou; esta decisão apenas torna mecânica a
  regra `B3`: "plano não-pronto" passa a ter teste executável — cabeçalho ilegível pelo esquema,
  campo obrigatório ausente, ou `Dossiê fechado por` com tarefa ainda não `done`.
- **`T15` (remoção de formato dos prompts) — insumo, não dossiê aberto.** A instrução de autoria
  acima é o texto a incorporar; a medição do que sai dos prompts continua sendo escopo da `T15`.

### `DP-F` — Lista final de estados e mapa de tradução *(fechada pela `T22` e **ratificada pelo dono em 2026-08-11**, sem reserva)*

**O que esta decisão fecha:** a avaliação da lista de sete estados enunciada pelo dono (§10.1,
enunciado 4), a lista final de `status`, a máquina de transições, o alcance por objeto, a tabela de
tradução do vocabulário vigente e o recorte da conformidade. **Nenhum artefato é conformado aqui** —
esta seção existe para tornar mecânica a conformidade das `T23`..`T27` e a reescrita de
`T19`/`T20`/`T21`.

**Critério declarado.** Um estado existe se **alguém age diferente por causa dele**: o `scrum-master`
no loop (delegar, invocar o revisor, escrever o RDO, escalar) ou a escolha da próxima tarefa no
kanban (o item é elegível ou não é). Estado sem consequência operacional **observável neste repo** é
**exagero** e não entra; transição real que nenhum estado nomeia é **insuficiência** e obriga a criar
um. Grafia não é critério de existência — onde a lista do dono e o vocabulário vigente nomeiam o
mesmo estado, a escolha do termo é do dono, porque a linguagem ubíqua é dele, salvo colisão
declarada.

#### 1. Veredito estado a estado

| estado enunciado | veredito | consequência operacional observada neste repo |
|---|---|---|
| `triage` | **necessário — nomeia uma insuficiência real** | `docs/plans/_INBOX.md` é append-only e marca `[drenado]` a linha já avaliada; item ainda não drenado **não é escolhível** — o `proximo-passo` o avalia (passo 1, drenar o inbox), nunca o delega. O estado já existe materialmente e hoje não tem nome |
| `ready` | **necessário** | é o pool de escolha: o `proximo-passo` escolhe entre os itens elegíveis (hoje rotulados `backlog`) por diretiva de prioridade ou FIFO |
| `blocked` | **necessário** | item não escolhível com razão registrada, e com passo próprio de destrave quando a razão cai (`proximo-passo`, heurística 1); a validação postergada vive nesse estado |
| `in-progress` | **necessário** | WIP de 1: havendo um item em execução, nenhum segundo é aberto (`proximo-passo`, heurística 2) |
| `review` | **necessário** | é o **gatilho 1** da `DP-E` (invocação do `pantonic-reviewer`) e o estado de quem aguarda aceite do dono — a própria `T22` está nele enquanto esta seção não é ratificada. Já constava como válido em `.claude/skills/diario-de-obras/SKILL.md:28` (`in review`), sem uso medido no índice |
| `done` | **necessário** | terminal, sai do backlog, condensa para o histórico, e é o **gatilho 2** da `DP-E` (escrita do RDO) |
| `cancelled` | **necessário** | terminal e **distinto de `done`**: nunca feito, descartado — condensação e registro histórico dependem da distinção (caso real: `T13..T16` absorvidas no `P-0730-V2I`, ao lado de tarefas entregues) |

**Veredito global: a lista dos sete é *suficiente*.** Nenhum dos estados enunciados é exagero,
nenhuma transição observada ficou sem nome, nenhum estado novo entra. As duas correções são de
**grafia** e de **alcance**, não de conteúdo: `backlog` deixa de ser nome de estado e passa a nomear
só o conjunto (item 5), e `superseded` fica fora do vocabulário de tarefa (item 4).

#### 2. Lista final

**Escritor:** o `status` é **materializado** pelo `scrum-master`, e só por ele, em qualquer estado
(`DP-E`, enunciado 2) — não se repete linha a linha. A **autoria** de `review` e de `blocked` é do
executor; nos demais estados, autoria e materialização são ambas do `scrum-master` (`DP-G`, item 1).

| estado | significado | o que dispara a entrada |
|---|---|---|
| `triage` | item registrado, ainda não avaliado quanto a entrar no backlog | registro do item na fila de entrada (`docs/plans/_INBOX.md`) |
| `ready` | item aceito e elegível para execução | a triagem aceita o item; ou o planejamento cria a tarefa dentro de plano aprovado; ou um `blocked` é destravado |
| `blocked` | item que existe e não pode ser executado agora, com razão registrada | fato novo derruba a premissa; dependência não satisfeita; validação postergada; escalada do executor ou do laudo |
| `in-progress` | item em execução neste exato momento | o `scrum-master` delega o item a um contexto de execução |
| `review` | o entregável existe e aguarda aceite ou feedback de correção | o executor devolve o pacote de retorno |
| `done` | entregável aceito | laudo `seguir` ou `seguir com ressalva` acolhido e, onde o dono é o teste de sentido, o veredito dele |
| `cancelled` | item que não será executado, por qualquer motivo | a triagem recusa; o escopo é descartado; o item é absorvido por outro |

#### 3. Máquina de transições

Toda transição é **materializada** pelo `scrum-master`; a **autoria** de `in-progress` → `review` e
de `in-progress` → `blocked` é do executor (`DP-G`, item 1). A coluna **gatilho** cita os dois — e só
os dois — gatilhos fixados pela `DP-E` (enunciado 5).

| transição | quando | gatilho |
|---|---|---|
| (entrada) → `triage` | o item é registrado na fila de entrada | — |
| `triage` → `ready` | a triagem aceita: o item entra no kanban | — |
| `triage` → `cancelled` | a triagem recusa | — |
| `ready` → `in-progress` | o `scrum-master` delega (uma tarefa por contexto, WIP de 1) | — |
| `ready` → `blocked` | fato novo derruba a premissa, com razão registrada | — |
| `ready` → `cancelled` | escopo descartado ou absorvido por outro item | — |
| `blocked` → `ready` | a razão registrada não se aplica mais | — |
| `blocked` → `cancelled` | o bloqueio é permanente ou a rota mudou | — |
| `in-progress` → `review` | o executor devolve o pacote de retorno | **gatilho 1** — o `scrum-master` invoca o `pantonic-reviewer` |
| `in-progress` → `blocked` | o executor para e escala (Regra 8; regra `A3` da `DP-B`) | — |
| `review` → `done` | laudo `seguir` ou `seguir com ressalva`, mais o aceite do dono onde ele é o teste de sentido | **gatilho 2** — o `scrum-master` escreve o RDO |
| `review` → `in-progress` | laudo `refazer`, dentro do teto de retentativa (1, `DP-B`); a retentativa é agente novo (`D6`) | — |
| `review` → `blocked` | laudo `escalar`, ou `refazer` com o teto de retentativa esgotado | — |

**Fechamentos da máquina.** (a) `done` e `cancelled` são **terminais** e não têm saída: retrabalho
depois do `done` nasce como **item novo**, porque reabrir falsificaria o registro. (b) Só as duas
transições marcadas disparam ação automática; **nenhuma outra dispara nada**. (c) Item que termina em
`cancelled`, e item que para em `blocked` por escalada, **não** disparam RDO — o gasto continua
registrado pela telemetria (`T7`/`T14`); como isso se materializa em `rdo.py` é da reescrita da
`T19`, não desta decisão.

#### 4. Alcance por objeto

**A lista governa a tarefa e, por extensão, todo item do kanban.** O índice de
`docs/DIARIO_DE_OBRAS.md` tem **uma** coluna `Status`, compartilhada por iniciativa, plano, tíquete e
tarefa de sprint, e as regras de escolha do `proximo-passo` leem essa mesma coluna; dois vocabulários
disjuntos na mesma coluna seriam ambiguidade, não precisão. **Exceção declarada, única:**
`superseded` é estado **exclusivo de plano/iniciativa** e **não é estado de tarefa** — tarefa que a
realidade tornou obsoleta é `cancelled`; plano cuja premissa caiu é `superseded`, com ponteiro para o
substituto. Nem todo estado se aplica a todo objeto:

| objeto | estados aplicáveis |
|---|---|
| tíquete (fila de entrada) | `triage`, `ready`, `blocked`, `cancelled` |
| tarefa (de plano ou de sprint) | `ready`, `in-progress`, `review`, `done`, `blocked`, `cancelled` — **sem `triage`** (a tarefa nasce de plano já aprovado) e **sem `superseded`** |
| plano / iniciativa | `ready`, `in-progress`, `blocked`, `done`, `cancelled`, `superseded` — **sem `review`** (o aceite é das tarefas; o veredito do dono no fecho da sprint é tarefa em `review`) e **sem `triage`** (ideia de plano é triada como tíquete) |

**Residência única:** a lista, a máquina e esta tabela de alcance moram em
`.claude/skills/diario-de-obras/SKILL.md`, dona da forma do kanban; todo o resto **aponta** e não
recopia.

#### 5. Tabela de tradução — nenhum termo vigente fica sem destino

| termo vigente | destino | observação |
|---|---|---|
| `backlog` (como status) | **vira `ready`** | mesmo estado, termo do dono |
| `backlog` (como substantivo) | **permanece — outro vocabulário** | nomeia o **conjunto** dos itens elegíveis ("seguir o backlog", "drenar o inbox para o backlog"); não é status e não se traduz |
| `in progress` | **vira `in-progress`** | grafia do dono; token único, sem espaço, greppável e parseável |
| `in review` | **vira `review`** | já era declarado válido em `diario-de-obras/SKILL.md:28`, sem uso no índice |
| `done` | **permanece `done`** | inalterado |
| `blocked` | **permanece `blocked`** | inalterado |
| `cancelled` | **permanece `cancelled`** | inalterado |
| `superseded` | **permanece, restrito a plano/iniciativa** | não é estado de tarefa (item 4) |
| `entregue` | **morre** | trio revogado pela `DP-E`; trabalho aceito é `done` |
| `parcial` | **morre como status; a palavra permanece viva como veredito de rubrica** | outro vocabulário (`conforme`/`parcial`/`não conforme`), que não se traduz nem se substitui |
| `bloqueado` | **morre** | o estado é `blocked`; a palavra segue legítima em prosa corrente, sem valor de status |

Motivo da separação `backlog`/`ready`: hoje a mesma palavra nomeia o **conjunto** e o **estado**, e é
a única ambiguidade da lista vigente. Renomeando o estado, o conjunto continua se chamando backlog e
a ambiguidade some sem custo semântico.

#### 6. Classificação de ocorrência — os três tipos, com exemplo real de cada

| tipo | o que é | exemplo real |
|---|---|---|
| (i) `status` de item do kanban | o que esta decisão governa: valor da coluna `Status` ou do marcador de estado de um item | `.claude/skills/diario-de-obras/SKILL.md:22` — linha de índice `S1-T3` com `in progress` na coluna `Status` |
| (ii) veredito de rubrica | juízo de qualidade do laudo (`conforme`/`parcial`/`não conforme`), **não** é status | `.claude/tools/review_evidence.py:132` — a faixa `parcial` da rubrica |
| (iii) homônimo | a palavra em outro sentido, sem relação com o item do kanban | `.claude/tools/review_evidence.py:116` — `git status --porcelain=v1 --untracked-files=all` |

Regra: **classificar antes de substituir**; só o tipo (i) é traduzido. Contagem bruta de ocorrência
não é medida de trabalho (§10.2) — a contagem por arquivo nos dossiês `T23`..`T27` é sentido amplo,
e o número de edições reais será menor.

#### 7. Recorte da conformidade

**Confirmado sem alteração:** a repartição da superfície entre `T23` (as duas skills do kanban),
`T24` (o restante do kit executável), `T25` (espelho e índices), `T26` (doutrina normativa) e `T27`
(kanban, planos vivos e varredura de fecho); e a **conformidade delegada** do §10.4 — `.claude/tools/rdo.py`,
`.claude/tools/rdo_template.md`, `tests/test_rdo.py`, `.claude/agents/pantonic-reviewer.md` e
`.claude/skills/scrum-master/SKILL.md` ficam **fora** das varreduras porque sua conformidade é
entregue pela reescrita de `T19`/`T20`/`T21` contra esta seção.

**Uma correção, com justificativa:** `docs/RDO/P-0734-T11-skill-scrum-master-o-loop.md` **sai da
lista de arquivos-alvo da `T27`**. RDO já emitido é registro do que aconteceu à época, e o próprio
conteúdo da `T27` manda não reescrevê-lo — mantê-lo como alvo é contradição interna do dossiê. A
ocorrência permanece e entra na varredura de fecho como **sobrevivente justificado** (registro
histórico), nunca como pendência.

**Três adendos que a conformidade precisa conhecer** (não mudam a repartição): (a) a `T23` enuncia,
além da lista final, a **máquina do item 3** e a **tabela de alcance do item 4** — é isso que a
residência única cobre; (b) `T24`, `T25` e `T26` **não reenunciam** nada disso, apontam; (c) `in
progress` → `in-progress` é troca de grafia de alto volume no kanban, e vale a regra de sempre —
**só marcador vivo migra**.

**Fica fora, por ser registro histórico** (confirmado): `docs/DIARIO_HISTORICO.md`,
`docs/benchmark/**`, `docs/audits/**`, os planos fechados `P-0721`..`P-0732`, `Base.txt`, os bullets
de fechamento já escritos no diário, os RDO já emitidos e os decision records `DP-A`..`DP-F` —
**inclusive esta seção**, que cita os termos mortos justamente para matá-los. Fica fora também
**edição de código**: resíduo em `.claude/tools/*.py` e em `tests/` vira tíquete (`T27`), nunca
edição documental.

**Gate — cumprido.** Esta seção foi escrita como **proposta fechada**, sem item marcado "a decidir",
e o dono a **ratificou em 2026-08-11 sem reserva** — os três pontos levados à decisão (a partição de
`backlog` entre estado e conjunto, a grafia `in-progress` e `superseded` fora do vocabulário de
tarefa) foram acolhidos como escritos. O gate está aberto: `T23`..`T27` e a reescrita de
`T19`/`T20`/`T21` passam a ser delegáveis.

### `DP-G` — Fronteira de escrita do `status` entre executor e `scrum-master` *(fechada pela rodada de replanejamento e **ratificada pelo dono em 2026-08-11**, sem reserva)*

**O que esta decisão fecha:** a captura do §11 — quais valores de `status` o executor produz e quais
não produz, quem os grava onde o kanban os registra, e **qual sinal** diz ao `scrum-master` que a
tarefa da vez não deve ser feita agora e sim depois (a encomenda `E2`). Fecha também o que da `DP-E`
e da `DP-F` precisa ser reconciliado (a encomenda `E1`). **Nenhum artefato é conformado aqui.**

#### 1. Autoria e materialização são coisas diferentes — e o vão está na segunda

**Fato medido nesta rodada, não decidido.** Não existe hoje campo material de `status` por tarefa de
plano. A coluna `Status` do índice de `docs/DIARIO_DE_OBRAS.md` tem linha para **iniciativa, plano e
tíquete**; a tarefa de plano não tem linha própria — o estado dela aparece no **bullet de
fechamento**, escrito depois do fato, e na **posição da fila** do §5 do plano. "Escrever o `status`"
de uma tarefa, portanto, não é hoje editar uma célula que exista.

**Decisão.** A fronteira separa dois atos que o texto vigente trata como um só:

| ato | o que é | de quem é |
|---|---|---|
| **autoria** | determinar qual é o valor, por conhecer o fato que o produz | do executor para **`review`** e **`blocked`**, e de mais nenhum valor; do `scrum-master` para todos os demais |
| **materialização** | gravar o valor onde o kanban registra o estado do item | **exclusivamente do `scrum-master`**, em todos os estados, sem exceção |

Para os dois valores de autoria do executor, o `scrum-master` **transcreve sem discricionariedade**:
não converte `blocked` em `review`, não converte `review` em `done`, não reclassifica a razão. O que
ele decide é o **roteamento** (item 4), nunca o valor.

**Consequências fixadas, uma por enunciado do dono (§11.1):**

1. **Enunciado 1 — ACOLHIDO na autoria.** O executor é autor de exatamente dois valores, `review` e
   `blocked`. `done` não está no conjunto e nenhuma execução o produz.
2. **Enunciado 2 — ACOLHIDO integralmente.** `done` é do `scrum-master` em autoria **e** em
   materialização. Uma tarefa entregue por um executor permanece em `review` até que o loop a aceite.
3. **Enunciado 3 — ACOLHIDO sem correção.** `ready` → `in-progress` é escrita pelo `scrum-master`
   **antes** de delegar; o executor recebe a tarefa já em `in-progress` e nunca produz esse valor.
4. **Enunciado 4 — ACOLHIDO, com o sinal fixado no item 3 abaixo.**

O revisor continua **fora** da fronteira nos dois atos: não é autor nem materializador de `status`
(`DP-E`, enunciado 3, intacto).

#### 2. Gramática de retorno do executor — a palavra devolvida *é* o `status`

Substitui a linha do executor fixada em `D1` (`Done` \| `Done pendencia=<uma linha>`), que nomeava um
desfecho fora do vocabulário de `status`:

```
<tarefa> review [pendencia=<uma linha>]
<tarefa> blocked motivo=<dependencia|premissa> <uma linha de razão>
```

Domínio fechado em duas palavras. Retorno com qualquer outra palavra, sem `motivo=` em `blocked`, ou
com `motivo=` fora do par, é **pacote inválido** e cai em `A2` (um reenvio de formato, sem consumir a
retentativa de conteúdo). O canal `pendencia=` permanece como está (`D1`, `D2`, `D3` intactos): é
por onde decisão de arquitetura ou requisito chega ao loop, e ele é ortogonal ao `status`.

#### 3. `E2` — o `blocked` do executor é **um canal só, com razão tipada** (candidato **(a)**)

O tipo é campo de domínio fechado, lido como valor — nunca prosa interpretada (invariante da `DP-B`:
nenhuma célula da tabela pede juízo).

| `motivo=` | o que significa | o que o `scrum-master` faz |
|---|---|---|
| `dependencia` | a tarefa está certa e é performável; falta algo que **outra tarefa do mesmo plano** entrega — está só fora de ordem | **reordena a fila** para que a bloqueada suceda a que a bloqueia, materializa `blocked` com a razão registrada e **segue** para a próxima tarefa elegível |
| `premissa` | a premissa do dossiê caiu, ou o que falta **não** é entregue por nenhuma tarefa do plano | materializa `blocked` com a razão e **PARA** — escalada ao dono, replanejamento |

**Regra de desempate, declarada:** na dúvida sobre qual dos dois, o executor devolve `premissa`.
Reordenar por engano custa uma janela; escalar por engano custa um turno do dono, e é o executor
decidindo rota que a Regra 8 proíbe.

**O que o plano já prevê continua sendo carregado pela ordem do §5**, que é a dependência declarada
que já existe — nenhum campo novo entra na `DP-C`. A denúncia do executor cobre só o que a ordem não
podia prever: dependência **descoberta em execução**, que é o caso que o enunciado 4 nomeia.

#### 4. Consequência nas tabelas de roteamento da `DP-B`

Derivação de decisão já ratificada, não decisão nova. A materialização é da reescrita da `T21`.

| regra | veredito |
|---|---|
| `A3` (`status=bloqueado`) | **partida em duas pela razão tipada.** `A3a` (`motivo=dependencia`): reordena e **segue**. `A3b` (`motivo=premissa`): **PARA**. Em ambas cai o "despacha o reviewer assim mesmo" — não há entregável a julgar — e cai o "fecha o RDO como `bloqueado`", que a `DP-F` (item 3, fechamento (c)) já havia retirado |
| `A5` (`status=parcial` sem estouro) | **cai.** `parcial` morreu como `status` (`DP-F`, item 5) e não está no domínio de retorno do item 2. Entrega incompleta passa a ser juízo do **revisor** (veredito `parcial` da rubrica), que a `DA-6` já reservava a ele — o executor não classifica a própria entrega |
| `A1`, `A2`, `A4`, `A6`, `A7`, `A8`, `A9` | **inalteradas**, inclusive a precedência |
| `B1`..`B4` e os três tetos da `DP-B` | **inalterados**; `B1` continua lendo `pendencia=` do retorno ou a recomendação `escalar` do laudo |

A reordenação de `A3a` obedece ao teto de janela: ela não fecha tarefa, então não incrementa o
contador de tarefas fechadas, e a retentativa da tarefa reordenada **não** é consumida.

#### 5. `E1` — o que do texto vigente precisa ser reconciliado

A correção **não** é feita no lugar: vira tarefa própria, **`T28`**, com dossiê fechado no §4.

| superfície | o que é hoje | o que passa a ser |
|---|---|---|
| `§10.2`, enunciado 2 | "o `scrum-master` é o **único** papel que o escreve… nem o executor… escrevem `status`" | único que **materializa**; o executor é **autor** de `review` e `blocked` |
| `DP-F`, item 2, linha *Escritor* | "escrito **exclusivamente pelo `scrum-master`**" | mesma correção, com ponteiro para esta seção |
| `DP-F`, item 3, frase de abertura | "Toda transição é uma escrita do `scrum-master`" | toda transição é **materializada** pelo `scrum-master`; a **autoria** de `in-progress` → `review` e `in-progress` → `blocked` é do executor |
| `.claude/skills/diario-de-obras/SKILL.md`, `## Status — residência única` | a linha *Escritor* já copiada pela `T23a` | mesma correção, na residência |

Nada mais da `DP-E` e da `DP-F` é tocado: a lista dos sete, a máquina de transições, o alcance por
objeto, a tabela de tradução e o recorte da conformidade **permanecem íntegros** — esta decisão muda
quem produz o valor, não quais valores existem nem quando se transita.

#### 6. Alternativas rejeitadas

- **Executor grava o `status` no kanban.** É a leitura literal do enunciado 1, e foi recusada por
  medida: não existe campo material de `status` por tarefa de plano (item 1); criá-lo é artefato novo,
  fora do escopo desta rodada, e poria **dois escritores** no arquivo onde hoje há um só. A autoria
  fica fixada aqui, de modo que, se o campo material vier a existir, a materialização pode migrar sem
  reabrir esta decisão.
- **`E2` candidato (b) — palavra de retorno distinta para adiamento.** Criaria um vocabulário de
  retorno disjunto do `status`, que é exatamente o que a `DP-E` e a `DP-F` existiram para eliminar; e
  o item adiado continuaria em `blocked` ou `ready`, sem estado novo — a lista da `DP-F` está fechada.
- **`E2` candidato (c) — só dependência declarada no plano, sem denúncia do executor.** Não cobre o
  caso que o enunciado 4 nomeia, a dependência **descoberta em execução**. O que é previsível já é
  carregado pela ordem do §5, e essa parte de (c) foi **absorvida** (item 3).
- **Derivar o `blocked` do veredito do laudo.** O revisor não julga tarefa sem entregável, e a `DA-6`
  proíbe juízo que chegue por argumento em vez de cálculo.

#### 7. O que esta decisão encomenda

- **`T28`** — sanitização do texto vigente (`E1`), dossiê fechado no §4.
- **Reescrita de `### T19`, `### T20` e `### T21`** contra `DP-F` + `DP-G`, na mesma rodada de
  replanejamento — é onde a fronteira se materializa em CLI, em protocolo de agente e em passo de
  loop.

**Gate — cumprido.** Esta seção foi escrita como **proposta fechada**, sem item marcado "a decidir"
(`G-PLANREADY` item 5). Os dois pontos levados à decisão — a **fronteira autoria × materialização**
(item 1, com a leitura literal recusada no item 6) e a **razão tipada como canal único** (item 3) —
foram **acolhidos como escritos**, sem reserva. O gate está aberto: a `T28` e a reescrita de
`T19`/`T20`/`T21` passam a ser delegáveis.

## Achados da execução

- **`### Passo 8` cita `A1`..`A5` e cai no vão entre a `T21a` e a `T21b`** *(achado da `T21a`,
  2026-08-11)* — o passo 8 (`## Fluxo`) enumera o bloco A como "`A1`..`A5`". A `T21a` não o tocou
  (não está entre os passos do seu dossiê) e a `T21b` parte `A3` em `A3a`/`A3b` e **remove** `A5`,
  mas seus alvos são `## Tabelas de roteamento`, `## Relatório de encerramento`, `## Proibições` e
  `## Guardrails` — a varredura do arquivo inteiro que ela declara é só de **vocabulário**. Sem
  ação, a `T21b` fecha deixando o passo 8 apontando para uma regra que ela mesma apagou.
  Pertinência: é a referência que leva da tabela ao passo, e sai errada por consequência direta da
  própria `T21b`. Encaminhamento: carregar a correção no despacho da `T21b` — mesma rodada, mesmo
  arquivo, uma linha —, sem reabrir os passos entregues pela `T21a`.

- **Drift de numeração em `docs/RESIDENCIA_DOUTRINA.md:89`** *(achado da `T6b`, 2026-08-08)* — a
  seção "Regra 3", item 3.5, aponta "§7 item 8 ('docs grandes via índice')" quando esse conteúdo é
  do **item 7** de `GOVERNANCA.md` §7 (o item 8 é `G-DEADCODE`). É o mesmo drift que a `T6b`
  corrigiu na nota de colisão da seção "Regra 2", que era alvo medido do dossiê; a ocorrência da
  seção "Regra 3" ficou fora dos alvos e não foi tocada. Pertinência: `docs/RESIDENCIA_DOUTRINA.md`
  é o mapa de residência consultado antes de mover doutrina entre o global e o kit — ponteiro
  errado nele manda a próxima edição para o item errado. Indexado como `TK-25` no diário.

*(preenchido pelos executores)*

- **`T23a`, 2026-08-11 — a `DP-F` não diz o que acontece com `superseded` fora da lista de alcance.**
  O bullet substituído em `.claude/skills/diario-de-obras/SKILL.md` afirmava três fatos operacionais
  sobre `superseded` que a `DP-F` não reenuncia: que é **terminal**, que **condensa para o
  histórico** e que **sai do backlog (não é escolhível)**. A `DP-F` só o posiciona como estado
  exclusivo de plano/iniciativa (item 4); a máquina do item 3 é de tarefa e não tem nenhuma
  transição para `superseded`. Como o executor não inventa regra, a residência única fixada aqui
  enuncia só o que a `DP-F` ratificou — e esses três fatos ficaram sem residência no repositório.
  Pertinência: a operação "Condensar" da própria skill e a escolha do `proximo-passo` dependem de
  `superseded` ser não-escolhível. Ação futura: a `DP-F` (ou a reescrita da `T27`) precisa fechar as
  transições de plano/iniciativa para `superseded` e a terminalidade dele — decisão de planejamento,
  não de execução.

- **`T3`, 2026-08-08 — o dossiê da `T3` nomeia a tarefa dependente errada.** O corpo do plano manda a
  `T3` "fechar o dossiê da `T10`", mas a `T2` já havia fechado a `T10` integralmente e registrado que
  o que continuava aberto era a **`T11`** (tabela de roteamento e tetos). A `T3` fechou a `T11`, que é
  a dependência real, e deixou adendo na `T10` com o domínio de veredito. Sem ação no corpo do plano,
  que é imutável por desenho; sem consequência para a ordem do §5.
- **`T4`, 2026-08-08 — um plano vivo fica fora do esquema.** A `DP-C` mediu que `P-0733` tem **12
  tarefas não iniciadas** com cabeçalho sem `classe`/`teto`. Retrofit é ato de planejamento (a classe
  é escolhida antes de delegar, `GOVERNANCA.md` §3) e a `T4` não edita outro plano — roteado como
  **`TK-24`**. Sem consequência para este plano: `rdo.py` nasce com o caminho de legado por desenho
  (política, item 3), então o retrofit é higiene, não bloqueio.
- **`T4`, 2026-08-08 — duas grafias da mesma classe dentro deste plano.** Os cabeçalhos usam `classe
  redação/planejamento` (`T2`..`T4`) e `classe redação de doutrina` (`T5`, `T6a`, `T6b`) para a mesma linha
  ≤30 de `GOVERNANCA.md` §3. Sob a `DP-C` as duas colapsam no slug `redacao`. Corpo do plano não
  alterado (imutável por desenho); a leitura pelo esquema é feita pelo caminho de legado, como em
  qualquer plano anterior à decisão.
- **`T19`, 2026-08-11 — dossiê insuficiente para performar (G-EXECREADY).** O `### T19` manda
  `cmd_close` materializar o RDO "a partir do plano, do laudo, do consumo medido e do desdobramento
  calculado" e confirma, via `9.1`/`D2` desta própria seção, que a validação dos 8 campos do pacote
  sai — mas não diz de onde `close` passa a tirar o parâmetro `status` que `calcular_desdobramento`
  (`:589`, reusada sem mudança de assinatura declarada) continua exigindo: a partição do bloco A pela
  `D5` entre "passa ao laudo" (`A5`/`A6`/`A8`/`A9`) e "permanece no loop" (`A1`/`A2`/`A4`/`A7`/
  `B1`-`B3`) **omite `A3` (bloqueado)** das duas listas. Segunda lacuna: `D1` põe
  `pendencia_para_o_dono` em "retorno do executor (campo opcional) ou laudo", e o `### T19` não diz
  se `close` ganha um flag para esse canal opcional, nem qual. Executor não decidiu
  (G-PLANFIDELITY) — tarefa devolvida `blocked` ao diário sem nenhum arquivo de código tocado.
  Indexado como `TK-28` no diário.
- **`T19`, 2026-08-11 — o dono descreveu o fluxo em duas rodadas; a segunda corrige a primeira
  (sinal de poluição, Regra 2; checkpoint, nada iniciado).** Fluxo vigente, já com a correção:
  **`pacote` redefinido** como *os argumentos de que o script precisa para construir o RDO*. O
  executor conclui e devolve **`status`**, que é o gatilho do fechamento do scrum-master. O
  scrum-master invoca o `reviewer`, que **não lê pacote de retorno nenhum** — recebe o contexto do
  executor e atua sobre o **diff** — e **gera o pacote, inserindo-o no laudo**. O **laudo** é o gatilho do
  desdobramento. No desdobramento: recomendação de **fechamento** ⇒ o scrum-master **extrai o pacote
  do laudo** e invoca o script, que gera o RDO; recomendação **diferente de fechamento** ⇒ o pacote
  **pode e deve ser revisado** (exemplo do dono: rollback + retrabalho muda o `status` de `Done`
  para `In-progress`) e o loop aguarda a nova rodada — reexecução ou escalada — antes de desdobrar,
  em operação **ad-hoc**, porque a recomendação não é previsível de antemão.
  **Efeito sobre a `DP-D`:** `D3` (RDO no fechamento) e `D4` (revisor julga contra dossiê e diff,
  nunca contra narrativa de quem executou) **confirmadas**; `D2` **revista** — o pacote existe, mas
  produzido pelo **`reviewer`** dentro do laudo, nunca escrito pelo executor; `D1` **revista** — o
  `status` de conclusão é do executor **como gatilho**, e o valor que vai ao RDO é o do pacote
  gerado pelo `reviewer`, revisável pelo scrum-master fora do ramo de fechamento.
  **Os quatro pontos, respondidos pelo dono na mesma rodada:**
  1. **`status` é qualidade da tarefa**, e usa a **nomenclatura do kanban** deste diário — não se
     cria domínio próprio. **Agente não tem status** (o executor devolve conclusão, não estado) e
     **o pacote não tem status**: o pacote retrata o estado do *entregável*, não o da tarefa.
     Consequência: `entregue`/`parcial`/`bloqueado` sai; `parcial` não tem equivalente kanban e
     colapsa em `in progress`.
  2. **Fronteira de autonomia do scrum-master**, como um scrum master real: ele decide sobre a
     **tarefa** (`status`, desdobramento) e **não** sobre a **entrega** (diff, campos relativos a
     código). É o que resolve o pacote revisado — o scrum-master nunca reescreve campo de entrega
     do `reviewer`.
  3. **O laudo é efêmero**: só existe quando um `reviewer` é invocado e é **descartado depois de o
     scrum-master desdobrar**, porque é fonte potencial de poluição de contexto e **não pode ser
     reinserido numa nova rodada**. Havendo reexecução, o fluxo segue **sem memória do histórico**,
     só com diretivas atualizadas. O **caminho feliz** (o `reviewer` recomenda fechar) é o que se
     doutrina; **retrabalho e escalada não se doutrinam** — resolvem-se com o dono, porque é
     pertinente envolvê-lo em questão complexa.
  4. Consumo medido continua entrando por argumento do scrum-master e **não** é campo do pacote.

  **Destino do laudo — decidido pelo dono na mesma rodada (alternativa `a`):** o laudo é **apagado**
  depois de consumido; o RDO **absorve as informações úteis e larga o ponteiro**, sem pendurar
  referência a documento inexistente. A tarefa que fizer isso deve **inspecionar minuciosamente as
  informações obrigatórias do laudo**, para o RDO reter tudo o que é útil e descartar o resto. A
  **definição de "informações úteis" não se resolve aqui** — fica no escopo dessa tarefa ou de outra,
  porque exige avaliar os documentos **transitórios e permanentes** em conjunto, buscando o balanço
  entre reter o valor e descartar a poluição. Essa mesma tarefa avalia um **campo opcional
  "Lições aprendidas na tarefa"**: recomendação que o `reviewer` julgue pertinente sobre melhoria
  **do processo e da tarefa em si — nunca do entregável**. *(Essa avaliação virou card próprio na
  rodada de 2026-08-11: a `T30`, conceito de utilidade — `DP-H`.)*
  **Consequências ainda não decididas:** (a) a tabela `A1..A9`/`B1..B4` e `calcular_desdobramento`
  codificam exatamente o caminho triste que deixa de ser doutrinado — o desdobramento tende a
  colapsar em "fechar" × "parar e escalar ao dono"; (b) a `T18`, já entregue, grava o laudo como
  documento **persistente** em `docs/RDO/laudos/` e precisa ser reavaliada à luz do descarte e da
  absorção acima.
  Replanejamento em contexto novo, com `T19`, `T20` (revisor "sem pacote") e `T21` reabertas juntas.

## 9. Replanejamento — reconciliação do fluxo descrito pelo dono

**Estado: RATIFICADA pelo dono em 2026-08-10**, com o texto à vista e o desvio do `D1` declarado. A
`DP-D` revoga a parte de `DP-A` e `DP-B` que a descrição do dono redefine; o que ela não toca
permanece normativo. O insumo do lado do dono foi o registro de segunda mão do fechamento da `T11`
(`docs/DIARIO_DE_OBRAS.md`), conferido contra a proposta antes da ratificação.

> **A própria `DP-D` foi parcialmente revogada em 2026-08-11 pela `DP-E`.** O §10.3 é a tabela
> cláusula a cláusula do que caiu e do que permanece, e a *Nota de derivação de 2026-08-11* deste
> §9 está **revogada por inteiro**. Ler esta seção sem o §10.3 à vista lê texto derrubado como
> vigente.

### `DP-D` — Qual descrição é normativa *(ratificada pelo dono, 2026-08-10)*

**Decisão proposta:** a descrição do dono é normativa **no que ela redefine**; `DP-A` e `DP-B`
continuam normativas **no que ela não toca**. O critério é o da **recência restrita ao
desenvolvimento** (`DP-H`, §13): dentro dos planos de desenvolvimento do framework, o último
entendimento do autor reescreve a orientação anterior que ele contradiz — e, aqui, ele apaga o
objeto que a `DP-A` transportava. Sem **pacote de retorno** — o objeto de oito campos que o executor
devolvia, que não se confunde com o `pacote` do laudo (`DP-H`, item 4) — não há o que transportar, e a medição que sustentou a `DP-A` (29 handovers, mediana 2 839 chars)
continua válida como lição — prosa de subagente não atravessa o orquestrador — e é **melhor
atendida** pelo fluxo descrito, em que o executor devolve uma palavra.

O defeito registrado no fechamento da `T11` (circularidade `rdo.py close` ↔ laudo,
`.claude/tools/rdo.py:654`) **desaparece** sob esta reconciliação, porque some o objeto que fechava o
ciclo. Nenhuma das três correções cogitadas na época (partir `close`, flag `--sem-laudo`, revisar a
`DP-A`) é executada.

#### Divergência a divergência

| # | `DP-A`/`DP-B` ratificaram | o dono descreveu | veredito proposto |
|---|---|---|---|
| `D1` | executor devolve **5 campos** (`status`, `rdo`, `tools`, `pendencia`) | executor devolve **"Done"** | **acolher, com os consumos re-ancorados** — ver abaixo |
| `D2` | **pacote de 8 campos** gravado pelo executor no RDO | o pacote **não existe** | **acolher** — nenhum dos oito campos dependia do executor para existir (ver realocação) |
| `D3` | `rdo.py new` abre o RDO **no início** | o RDO é criado **no fim**, pelo scrum-master | **acolher** — mata a circularidade medida |
| `D4` | revisor recebe o **pacote em arquivo** | revisor recebe **o mesmo contexto do executor** | **acolher** — julga a entrega contra o dossiê e o diff, nunca contra a narrativa de quem executou |
| `D5` | desdobramento sai da **tabela** `A1..A9`/`B1..B4` | o **laudo carrega a recomendação** | **acolher com domínio fechado** — ver fronteira abaixo |
| `D6` | retentativa re-despacha o **mesmo** executor (`A6`) | retentativa é **agente novo em contexto novo** | **acolher** — contexto de execução reprovada está poluído (Regra 2) |

#### `D1` — para onde vão os três consumos da linha de 5 campos

O que a `DP-B` lia da linha do executor não some; passa a vir de fonte que não é o auto-relato de
quem está sendo julgado:

- **`tools` gastos (regra `A4`, estouro de teto) → bloco `<usage>` da notificação de conclusão.**
  Medido nesta rodada: as 8 linhas `EXA-*` de `docs/telemetria.tsv` têm `tool_uses` preenchido com
  `fonte=usage` — a contagem é medida, não relatada. Sob a `DP-A` o mesmo número vinha do executor,
  o que era regressão da própria doutrina (`~/.claude/CLAUDE.md` Regra 7; `GOVERNANCA.md` §4.2).
- **`status` (`entregue`/`parcial`/`bloqueado`) → laudo do revisor.** É juízo sobre a entrega, e o
  papel que julga é o revisor (`DA-2`), não o executado.
- **`pendencia` → laudo do revisor, com uma exceção declarada.** Pendência de arquitetura ou de
  requisito pode **não ser visível no diff** — é o que a execução descobriu e o artefato não mostra.
  **Único ponto em que esta proposta se desvia da descrição do dono:** o retorno do executor mantém
  um campo opcional, `Done` **ou** `Done pendencia=<uma linha>`. Sem esse canal, a regra `B1` (a que
  obriga parada para o dono) fica dependente de o revisor inferir do diff uma pendência que o diff
  não contém.
- **`rdo=<caminho>` → deixa de existir** (consequência de `D3`).

#### `D2` — realocação dos oito campos

| campo do pacote | passa a residir em |
|---|---|
| `tarefa` | plano + invocação (o loop já os tem) |
| `status` | laudo (`D1`) |
| `arquivos_tocados`, `verificacao` | `review_evidence.py` — já apura por `git` e já roda a bateria do §3 |
| `desvios_do_dossie`, `achados` | laudo |
| `orcamento` | notificação (`<usage>`) + teto do cabeçalho da tarefa |
| `pendencia_para_o_dono` | retorno do executor (campo opcional) ou laudo |

Nenhum campo é perdido; o que muda é **quem o produz**. Dois deles passam de auto-relato para
medição mecânica, que é a direção que `DA-6`/`DA-7` já apontavam.

#### `D5` — fronteira entre o que o loop sabe e o que o juiz sabe

A tabela da `DP-B` não morre: ela se divide pela origem da informação.

- **Permanece no loop** (só ele sabe): `A1` queda de subagente, `A2` retorno fora da gramática,
  `A4` estouro de teto (lido do `<usage>`), `A7` retentativa esgotada, `B1` pendência, `B2` tetos de
  janela, `B3` plano não-pronto.
- **Passa ao laudo** (só o juiz sabe): o desfecho de qualidade, hoje `A5`/`A6`/`A8`/`A9`. O laudo
  emite **recomendação de domínio fechado** — `seguir` | `seguir com ressalva` | `refazer` |
  `escalar` — junto do veredito calculado. O loop lê um campo; continua sem interpretar prosa, e
  `DA-6` (percentual calculado) e `DA-7` (autoridade da camada mecânica) ficam intactos.

Os três tetos da `DP-B` (retentativa 1, tarefas por janela 10, consumo 900 k) **permanecem
integralmente** — a base medida deles não foi tocada por nenhuma divergência.

#### Nota de derivação de 2026-08-11 — `status`, `A3` e o canal da pendência

> **REVOGADA POR INTEIRO no mesmo dia, pela `DP-E` (§10.3).** A premissa da cadeia — o `status` mora
> no laudo — caiu; o §10.3 percorre os quatro itens e declara o que cai junto e o que tem base
> própria que sobrevive. Nada aqui é instrução vigente; o bloco fica como registro da derivação.

*(Subordinada à `DP-D`. **Não altera o texto ratificado acima**: cada item declara de qual cláusula
decorre. Registrada quando o executor da `T19` recusou o dossiê por `G-EXECREADY` — achado `TK-28`.)*

1. **Residência material do `status`** *(decorre de `D1` e da linha `status` do `D2`)*. As duas
   cláusulas alocam `status` ao **laudo do revisor**. Fato medido em 2026-08-11: o documento de laudo
   que a `T18` entregou grava `Percentual`, `Veredito`, `Dimensão bloqueante`, `Recomendação`,
   `Pendência`, a tabela de níveis e `Observações` (`.claude/tools/rdo.py:556-567`), e **não** grava
   `status`; o subcomando `laudo` tampouco tem `--status`. A `T18` cumpriu o dossiê que recebeu — ele
   só falava da recomendação —, então a lacuna é de dossiê, não de execução. Derivação: o campo é
   materializado onde a `DP-D` já o alocou (o `laudo` ganha `--status` e o documento passa a
   carregá-lo), e o `close` o lê de lá. **Descartado** derivar `status` do veredito calculado: além
   de contrariar `D1` — é juízo próprio do revisor, não saída da rubrica —, tornaria `bloqueado`
   inalcançável, apagando na prática uma regra ratificada.
2. **`A3` na partição do `D5`** *(decorre de `D5` combinado com `D1`)*. O `D5` reparte a tabela
   **pela origem da informação**; `A3` não aparece em nenhuma das duas listas porque é o único caso
   em que **condição** e **ação** caem de lados diferentes: a condição (`status=bloqueado`) foi para
   o laudo por `D1`, e a ação (fechar o RDO como `bloqueado` e **PARAR**) é do loop, como toda ação
   do bloco A. Derivação: o loop conhece `A3` **pelo campo `Status` do laudo** — o mesmo documento de
   onde já lê a recomendação —, nunca por relato do executor. A recomendação não o substitui: os
   quatro valores (`seguir`, `seguir com ressalva`, `refazer`, `escalar`) não expressam `bloqueado`.
   O trecho "despacha o reviewer assim mesmo" da célula `A3` deixa de ser uma ação distinta, porque
   no fluxo novo o revisor é despachado **sempre**; o que resta de `A3` é "fecha como `bloqueado` →
   PARA". A célula continua **verdadeira como está escrita** — a `T21` mantém `A3` intacta, como o
   dossiê dela já diz.
3. **Precedência intacta** *(decorre de `D5`, último parágrafo: a tabela se divide, não muda)*.
   `A3` antes de `A4`, e os dois antes do que a recomendação roteia (`A5`..`A9`). É a precedência já
   codificada em `calcular_desdobramento` (`.claude/tools/rdo.py:624`), cuja **assinatura não muda**:
   `status` e `veredito` vêm do laudo, o estouro vem do `<usage>` medido contra o teto do cabeçalho.
4. **Canal do executor para a pendência** *(decorre da linha `pendencia_para_o_dono` do `D2`, da
   exceção declarada no `D1` e de `D3`)*. O `D2` deu ao campo duas residências — "retorno do executor
   (campo opcional) **ou** laudo" — e o `D3` pôs a geração do RDO no `close`. Derivação: sem um
   argumento no `close`, a metade "retorno do executor" não teria caminho até o documento, e a única
   exceção que a `DP-D` se permitiu em relação à descrição do dono ficaria sem efeito. O `close`
   ganha **um** argumento opcional de uma linha, `--pendencia`; o RDO grava as duas origens
   rotuladas, e nenhuma se perde. Nenhum outro argumento de conteúdo entra no `close`.

#### Ponto fechado na ratificação — retroação do RDO

**Decidido pelo dono em 2026-08-10, conforme a recomendação: não retroagir.** A regra da `DA-5` vale
daqui para a frente; `T1`..`T10` mantêm o diário como registro canônico, e o índice de `docs/RDO/`
cobre só as tarefas fechadas depois de o instrumento existir. O que sustentava a recomendação:

**Retroação do RDO.** `docs/RDO/` tem **1** RDO para **15** tarefas fechadas do `P-0734`; `T1`..`T10`
fecharam antes de o instrumento existir e têm o diário como registro canônico.
**Recomendação: não retroagir** — a regra vale daqui para a frente. Gerar 15 RDOs a partir de
bullets de diário produziria registro sem leitor e contraria o precedente já fixado no §8 (nota
histórica fica onde está). Custo aceito: o `P-0734` fica com dois registros canônicos por época, e o
índice de `docs/RDO/` cobre só a segunda.

### 9.1 Rebase — o que sobrevive do que já foi construído

| artefato | veredito | trabalho residual |
|---|---|---|
| `telemetria.py` (`T7`) | **intacto** | nenhum |
| `review_evidence.py` (`T9a`/`T9b`) | **intacto e mais central** | nenhum — sem pacote, é a única entrada mecânica do revisor |
| `rdo.py laudo` (`T8b`) | **sobrevive** | passa a emitir a recomendação de domínio fechado (`D5`) |
| `rdo.py` índice (`T8c`, parte) | **sobrevive** | nenhum |
| `rdo.py new` (`T8a`) | **perde objeto** | o subcomando sai; `extrair_dossie` e o template permanecem (a `T9a` já reusa `rdo.py:186`) |
| `rdo.py close` (`T8c`, parte) | **reescrito** | vira geração do RDO no fechamento, a partir de plano + laudo + `<usage>` + desdobramento; a validação dos 8 campos sai |
| `pantonic-reviewer` (`T10`) | **editado, não refeito** | protocolo troca "ler pacote de retorno" por "ler dossiê + evidência + diff"; ganha a recomendação na saída |
| `scrum-master` (`T11`) | **editado, não refeito** | passos 4, 5, 6 e 9 reescritos; o "ponto aberto" do passo 9 é removido; passos 1, 2, 3, 7, 8 e 10 sobrevivem |
| `DP-C` (esquema da tarefa) | **intacto** | nenhum |
| `T12`..`T17` | **intactos em intenção** | `T15` e `T16` ganham alvo diferente, não escopo diferente |

Nenhuma tarefa fechada precisa ser reaberta como reprovada: `T7`, `T9a`, `T9b` e `T10` entregaram o
que o dossiê pedia, e o que muda é a rota a jusante.

### 9.2 O que a ratificação destravou

Ratificada a `DP-D`, o plano volta a ser delegável por **quatro** tarefas novas — `T18`..`T21`, no
§4 —, depois das quais a ordem original retoma em `T12`. Os quatro dossiês foram escritos
**fechados** no mesmo ato da ratificação (`G-PLANREADY` item 5).

**São quatro e não três**, como a proposta anunciava: a fatia "revisor + laudo" reunia código
(`rdo.py laudo`) e doutrina (`.claude/agents/pantonic-reviewer.md`), que a `DP-C` não deixa conviver
num cabeçalho — ele declara **um** modelo e **uma** classe, e as duas metades caem em linhas
diferentes da tabela de tetos de `GOVERNANCA.md` §3. A numeração segue a ordem de execução, então o
`laudo` (que o `close` consome) vem antes da geração do RDO.

**Duas decisões de desenho fechadas aqui**, para que nenhum dos quatro dossiês chegue aberto ao
executor:

- **Residência do laudo.** Sem `rdo.py new` não existe RDO aberto onde gravar a seção do laudo. O
  laudo passa a ter **documento próprio**, `docs/RDO/laudos/<plano>-<tarefa>.md`, que é o artefato
  que o revisor assina; o RDO gerado no fechamento carrega os **campos** (veredito, percentual,
  bloqueante, recomendação) e um **ponteiro** para ele, nunca a prosa — repetir o corpo criaria a
  terceira fonte que a `DA-5` proíbe.
- **Como `escalar` entra no domínio fechado.** Três das quatro recomendações são **derivadas** do
  veredito calculado (`seguir`, `seguir com ressalva`, `refazer`); `escalar` não é derivável, porque
  pendência de arquitetura ou requisito é juízo do revisor sobre o que o artefato não mostra. Ela é
  marcada explicitamente, com a linha da pendência junto, e **domina** as outras três. É o que
  mantém a regra `B1` alimentada por um campo, sem o loop ler prosa.

---

## 10. `DP-E` — o `status` é da tarefa, não do laudo

**Estado: RATIFICADA pelo dono em 2026-08-11.** O enunciado foi capturado em contexto separado, sem
derivar nada (contradição de rota é sinal de poluição — `~/.claude/CLAUDE.md` Regra 2, e o que se
decide depois do sinal é decisão poluída); esta seção é a rodada de replanejamento que consumiu a
captura e fechou as decisões. A `DP-E` revoga a parte da `DP-D` (§9) que o enunciado do dono
contradiz; **o que ela não toca permanece normativo**, e o §10.3 declara item a item o que é cada
coisa.

**Nota de vocabulário — nome do papel.** O dono chamou de *inspetor* o papel que o kit materializa
como `pantonic-reviewer`. **Decidido:** o nome canônico do agente é `pantonic-reviewer` e a prosa
usa **revisor**; o termo *inspetor* está **abolido do vocabulário** do projeto, inclusive da
transcrição do §10.1 abaixo. A uniformização é de termo apenas — nenhum conteúdo do que o dono
enunciou foi alterado.

### 10.1 O que o dono enunciou

1. **`status` é característica da *tarefa*.** O laudo é documento de **entregável + lições
   aprendidas**; ele **não gerencia a informação de `status`**.
2. **Gerenciar o `status` é atribuição do `scrum-master`.**
3. **O laudo é escrito exclusivamente pelo revisor.** O `scrum-master` **só lê** o laudo, processa
   as informações úteis e descarta o resto.
4. **A linguagem ubíqua do `status` é padronizada em sete estados**, com o significado enunciado
   *(**este enunciado NÃO vira norma nesta rodada** — ver §10.2, item 4: ele é o insumo da `T22`,
   que avalia a lista antes de qualquer artefato ser conformado a ela)*:

   | estado | significado |
   |---|---|
   | `triage` | tarefa a ser avaliada se entra no backlog |
   | `ready` | tarefa inserida na pilha do backlog |
   | `blocked` | tarefa que existe, mas não pode ser executada atualmente |
   | `in-progress` | tarefa em execução neste exato momento |
   | `review` | tarefa concluída, carecendo de aceitação ou de feedback para correção do entregável |
   | `done` | entregável da tarefa aceito |
   | `cancelled` | tarefa que, por motivos genéricos, não será executada |

5. **Sugestão do dono sobre o gatilho do `scrum-master`:** `review` dispara a invocação do revisor;
   `done` é o estado em que o `scrum-master` está pronto para escrever o RDO.

### 10.2 Decisão

**Enunciado 1 — `status` é característica da tarefa. ACOLHIDO.** O laudo é documento de
**entregável + lições aprendidas** e **não carrega `status`**. Consequência imediata: `laudo
--status` não nasce, e nenhum campo de `status` da tarefa entra no documento de laudo. O que o laudo
carrega continua sendo o juízo de qualidade — percentual, veredito, dimensão bloqueante,
recomendação de domínio fechado, pendência, observações —, que é o que a `D5` alocou a ele e a
`DP-E` não toca.

**Enunciado 2 — gerenciar o `status` é atribuição do `scrum-master`. ACOLHIDO.** O `status` reside
na **tarefa**, no kanban, e o `scrum-master` é o **único** papel que o **materializa**. A **autoria**
é outro ato: o executor é autor de `review` e de `blocked` — os dois valores que devolve ao fim da
tarefa —, e o `scrum-master` transcreve sem discricionariedade (`DP-G`, item 1, que fixa a fronteira
entre autoria e materialização). O revisor (que escreve o laudo, enunciado 3) fica fora dos dois atos.

**Enunciado 3 — o laudo é escrito exclusivamente pelo revisor. ACOLHIDO.** Fronteira de escrita
fechada: o revisor **escreve** o laudo e é o único que o escreve; o `scrum-master` **só lê**, extrai
o que roteia o loop e descarta o resto. Consequência: o laudo permanece a fonte do juízo de
qualidade (`D5` intacto) e **deixa de ser fonte de `status`**.

**Enunciado 4 — os sete estados. NÃO VIRA NORMA NESTA RODADA — deslocado para tarefa própria.** A
lista enunciada é insumo, não decisão. Nasce a `T22`, que (a) **avalia** se os sete estados são
*suficientes*, *exagerados* ou *insuficientes*, fecha a lista final e o mapa de tradução do
vocabulário vigente, com **ratificação do dono como gate declarado no dossiê**; e (b) só depois
disso as tarefas de conformidade (`T23`..`T27`) aplicam a lista final aos artefatos. Nenhum artefato
é conformado a uma lista que ainda pode mudar, e nenhuma outra decisão desta seção depende de qual
seja a lista final.

**Enunciado 5 — gatilhos do loop. ACOLHIDO na estrutura, não na grafia.** O loop tem **dois**
gatilhos de estado: um estado que dispara a invocação do revisor (`review`, na grafia enunciada) e
um estado em que o `scrum-master` escreve o RDO (`done`, na grafia enunciada). O que a `DP-E` fixa é
a **existência e a posição dos dois gatilhos**; se a `T22` alterar a grafia ou o número de estados,
os gatilhos seguem a lista final sem que esta decisão seja reaberta. O gatilho de RDO é compatível
com a `D3` (o RDO nasce no fechamento) e a reforça: o RDO é escrito quando a tarefa entra no estado
de aceite.

**Alcance da padronização — decidido: loop *e* kanban.** A dúvida levantada na captura ("a
padronização alcança o kanban ou só o loop") está fechada pelo enunciado 1: se `status` é
característica da tarefa, o registro material do `status` da tarefa é o kanban
(`docs/DIARIO_DE_OBRAS.md`), e uma linguagem ubíqua que não alcança o registro material não é
ubíqua. A superfície de conformidade está fixada no dossiê da `T22` e repartida entre `T23`..`T27`.

**Três vocabulários que não se confundem — fato medido nesta rodada.** A contagem bruta de
ocorrências superestima a conformidade porque três vocabulários distintos usam as mesmas palavras:
(i) **`status` da tarefa** — o que esta decisão governa; (ii) **veredito da rubrica**
(`conforme`/`parcial`/`não conforme`), que é juízo de qualidade e **não** é status — medido: as seis
ocorrências de `.claude/tools/review_evidence.py` são todas veredito de rubrica ou `git status`, e
`docs/RUBRICA_DE_REVISAO.md` é majoritariamente desse tipo; (iii) **homônimos** (`git status
--porcelain`, `status` de plano/iniciativa como `superseded`). Classificar antes de substituir é
obrigação das tarefas de conformidade, e a fronteira entre (i) e (iii) para plano/iniciativa é uma
das perguntas que a `T22` fecha.

### 10.3 O que da `DP-D` (§9) é revogado e o que permanece

| cláusula da `DP-D` | veredito da `DP-E` |
|---|---|
| `D1`, linha "`status` (`entregue`/`parcial`/`bloqueado`) → laudo do revisor" | **REVOGADA.** É exatamente o que o enunciado 1 contradiz. O trio `entregue`/`parcial`/`bloqueado` deixa de ser vocabulário de `status`; qual vocabulário o substitui é da `T22` |
| `D1`, linha "`tools` gastos → bloco `<usage>`" | **PERMANECE** — medição, não auto-relato |
| `D1`, linha "`pendencia` → laudo, com canal opcional no retorno do executor" | **PERMANECE** integralmente, inclusive o desvio declarado (`Done` **ou** `Done pendencia=<uma linha>`) |
| `D1`, linha "`rdo=<caminho>` deixa de existir" | **PERMANECE** (consequência de `D3`) |
| `D2`, célula "`status` → laudo" da tabela de realocação | **REVOGADA** pelo mesmo motivo. O campo passa a residir na **tarefa**, escrito pelo `scrum-master` |
| `D2`, as outras sete células e o princípio "nenhum campo é perdido, muda quem o produz" | **PERMANECEM** |
| `D3` (RDO gerado no fechamento), `D4` (revisor julga dossiê + evidência + diff), `D6` (retentativa é agente novo) | **PERMANECEM**, intocadas |
| `D5`, recomendação de domínio fechado no laudo e partição da tabela pela origem da informação | **PERMANECE**. O laudo continua emitindo `seguir` \| `seguir com ressalva` \| `refazer` \| `escalar`, e o loop continua lendo campo, nunca prosa |
| `D5`, os três tetos da `DP-B` (retentativa 1, 10 tarefas por janela, 900 k) | **PERMANECEM** integralmente |
| Ponto fechado na ratificação de 2026-08-10 — **não retroagir** RDO de `T1`..`T10` | **PERMANECE** |
| §9.1 (tabela de rebase) e §9.2 (residência do laudo em documento próprio; `escalar` marcado e dominante) | **PERMANECEM**, com uma ressalva: a linha de `## Laudo` que a `T19` planejava incluir para `Status` não existe mais (consequência do enunciado 1), e isso é reescrita de dossiê, não mudança de decisão |

**A *Nota de derivação de 2026-08-11* (§9) está REVOGADA por inteiro**, como documento: ela é uma
cadeia de derivações cuja premissa (`status` mora no laudo) caiu no mesmo dia. Item a item:

1. *Residência material do `status`* — **cai**. `laudo --status` não nasce; o documento de laudo não
   grava `status`; o `close` não o lê de lá.
2. *`A3` na partição do `D5`* — **cai** a derivação (o loop conhecer `A3` pelo campo `Status` do
   laudo). A célula `A3` continua existindo e continua verdadeira no que manda fazer; **de onde o
   loop passa a saber que a tarefa está bloqueada é consequência da lista final** e é fechado na
   reescrita da `T21`, depois da `T22` — não nesta rodada.
3. *Precedência intacta* — **cai** no que ancora a origem do `status`; a **precedência do bloco A**
   (`A3` antes de `A4`, os dois antes do que a recomendação roteia) vem da `DP-B` e **permanece**
   intocada.
4. *Canal do executor para a pendência (`close --pendencia`)* — a derivação cai junto com a nota,
   mas **a base não foi tocada**: `D2` (célula `pendencia_para_o_dono`), a exceção declarada no `D1`
   e `D3` permanecem normativos, e continuam **encomendando** um canal do retorno do executor até o
   RDO. A materialização volta ao dossiê da `T19`, que será reescrito depois da `T22`.

### 10.4 O que a `DP-E` encomenda

- **`T22`** — avaliação da lista de estados e fechamento da linguagem ubíqua (`DP-F`), com gate de
  ratificação do dono. **Nada a jusante é delegável antes dela.**
- **`T23`..`T27`** — conformidade dos artefatos vivos à lista final, repartida por famílias e por
  volume medido.
- **`### T19`, `### T20`, `### T21`** — **pendentes de reescrita**, marcados como tal no §4. Não
  foram reescritos nesta rodada porque materializam o vocabulário de `status` que a `T22` avalia;
  reescrevê-los agora seria escrever contra uma lista que pode mudar. A reescrita é rodada de
  planejamento própria, imediatamente após a ratificação da `DP-F`.
- **Conformidade delegada.** Os artefatos que a `T19`/`T20`/`T21` reescrevem por inteiro
  (`.claude/tools/rdo.py`, `.claude/tools/rdo_template.md`, `tests/test_rdo.py`,
  `.claude/agents/pantonic-reviewer.md`, `.claude/skills/scrum-master/SKILL.md`) **não** entram nas
  varreduras `T23`..`T27`: sua conformidade é entregue pela própria reescrita, contra a `DP-F`. Dois
  agentes não tocam o mesmo arquivo; a `T27` verifica o resultado por varredura de fecho.

## 11. Captura — fronteira de escrita do `status` entre executor e `scrum-master`

**Estado: CONSUMIDO — fechado como `DP-G`** na rodada de replanejamento de 2026-08-11, ratificada
pelo dono no ato. Esta seção permanece como o **insumo** de que a decisão partiu; onde ela e a `DP-G`
divergirem, vale a `DP-G`. As duas encomendas do §11.4 estão respondidas: `E1` é a `T28` (§4) e `E2`
é o item 3 da `DP-G` — canal único com razão tipada.

### 11.1 O que o dono enunciou

1. **O executor escreve `status`, e escreve exatamente dois:** `review` e `blocked`. **Não** tem
   autonomia para escrever `done`.
2. **Só o `scrum-master` conclui uma tarefa como `done`.**
3. **O executor sempre *recebe* a tarefa já em `in-progress`;** a transição `ready` → `in-progress` é
   escrita pelo `scrum-master`, antes de delegar.
4. **Dependência descoberta em execução vira `blocked`:** o executor marca `blocked` e devolve ao
   `scrum-master`, que **reordena a fila** para que a tarefa bloqueada seja sucessora da que a
   bloqueia.

### 11.2 O que isto atinge (medido, não decidido)

- **`DP-E`, enunciado 2 (§10.2):** o texto vigente diz que o `scrum-master` é o **único** papel que
  escreve `status` e que "nem o executor (que devolve uma palavra, `D1`) nem o revisor escrevem
  `status`". O enunciado 1 acima **contradiz a parte absoluta** dessa frase. O que permanece: o
  revisor não escreve `status`, e `done` continua exclusivo do `scrum-master`.
- **`DP-F`, item 3 (máquina de transições):** as três transições envolvidas já existem e **não
  mudam de gatilho nem de condição** — `ready` → `in-progress`, `in-progress` → `review`,
  `in-progress` → `blocked`. Muda só a **coluna implícita de escritor**, hoje enunciada como "toda
  transição é uma escrita do `scrum-master`".
- **`DP-F`, item 2 (lista final):** a linha "**Escritor:** o `status` é escrito exclusivamente pelo
  `scrum-master`" precisa da mesma correção, e ela já foi copiada para a residência única em
  `.claude/skills/diario-de-obras/SKILL.md` pela `T23a`.

### 11.3 Consequência de fila, aplicada no ato

O enunciado 4 aplica-se à própria `T23b`: ela foi executada e o entregável existe, mas **não há
quem a conclua** — a transição `review` → `done` é do `scrum-master`, e a skill `scrum-master` só
passa a existir na forma reescrita depois de `T19`/`T20`/`T21`. A `T23b` volta ao backlog como
**`blocked`**, com a razão registrada, e a fila é reordenada para que ela suceda o loop. Mesmo
bloqueio se aplica a `T24`..`T27`, que fecham pelo mesmo caminho.

### 11.4 O que esta captura encomenda à rodada de replanejamento

Duas encomendas, decididas pelo dono em 2026-08-11. Nenhuma das duas é fechada aqui: ambas dependem
do texto da `DP-G`, que ainda não existe, e publicá-las abertas é o que o `G-PLANREADY` item 5
proíbe.

**`E1` — tarefa de sanitização do texto vigente.** A `DP-G` contradiz a parte absoluta do enunciado 2
da `DP-E` e a linha *Escritor* do item 2 da `DP-F`. Decisão do dono: isso **não** se resolve por
correção silenciosa no lugar — vira **tarefa própria de sanitização**, que reconcilia o texto vigente
com a `DP-G`. Superfícies medidas até aqui: `§10.2` (enunciado 2), `DP-F` item 2 (linha *Escritor*),
`DP-F` item 3 (a frase "toda transição é uma escrita do `scrum-master`") e a **residência única** em
`.claude/skills/diario-de-obras/SKILL.md`, para onde a `T23a` já copiou a linha *Escritor*. A rodada
de replanejamento autora o dossiê fechado e o registra no §4; o id sai na autoria (`T28` livre).

**`E2` — procedimento de denúncia do executor.** Decisão do dono: `T24`..`T27` **não** recebem
`blocked` explícito por bloqueio de fila — a fila reordenada basta como registro. Consequência que a
`DP-G` precisa fechar: **qual sinal chega ao `scrum-master` dizendo que a tarefa da vez não deve ser
feita agora, e sim depois**. Sem esse sinal a ordem só existe como prosa no diário, e o próximo
pickup escolhe `T24` pela heurística normal e bate na mesma parede.

A pergunta a fechar, enunciada: **o `blocked` do executor é um canal só, ou dois?** Hoje a mesma
palavra cobriria duas coisas com roteamento diferente — *a premissa caiu / a dependência não existe*
(o `scrum-master` escala ou replaneja) e *a tarefa está certa, só está fora de ordem* (o
`scrum-master` reordena e segue). Candidatos **não avaliados**, listados só para a rodada não
recomeçar do zero: (a) `blocked` único com **razão tipada**, e o tipo roteia; (b) palavra de retorno
distinta para adiamento, separada de `blocked`; (c) o executor não denuncia nada e a ordem vira
**dependência declarada no plano**, lida pelo `scrum-master` antes de delegar. A escolha entre elas é
da `DP-G`.

## 12. Insumo — a fronteira de escopo e o que ela reclassifica

**Estado: FECHADO em 2026-08-11 — derivado integralmente pela `DP-H` (§13).** As orientações abaixo
foram dadas em resposta ao levantamento de contradições aberto pelo fechamento da `T28`. O texto
permanece como está, por ser o insumo; o que ele produziu está no §13: o decision record, os cards
`T29`/`T30`/`T31`, a reescrita dos dossiês do §12.3 e a fila reordenada do §5. A `T19` **voltou a ser
delegável** com esse fechamento.

### 12.1 A fronteira: conceito do framework × desenvolvimento do framework

Duas coisas distintas estavam sendo tratadas como uma:

- **Conceito do framework** — o que o framework *é*. Reside nos artefatos publicados do framework.
- **Desenvolvimento do framework** — como ele está sendo construído. Reside no plano.

**Diante de qualquer orientação, a pergunta é: isto é conceito ou é desenvolvimento?** A maior parte
das orientações do dono é de desenvolvimento e fica escopada no plano; orientação de conceito vai
para os artefatos do framework.

**A regra de recência é de desenvolvimento.** O último entendimento do autor é canônico e reescreve
as orientações anteriores que ele contradiz — **restrito aos planos de desenvolvimento do
framework**. Ela **não** entra em artefato publicado do framework. O critério de desempate do
framework em si **não foi decidido**, e não se deriva deste.

**O RDO não entra nesta conciliação.** Ele é artefato com mecânica própria, do projeto, e não se
mistura com o desenvolvimento do framework.

### 12.2 Os seis pontos, reclassificados

1. **A "tarefa" vira artefato definido, em tarefa própria** — a questão voltou três vezes e para de
   ser respondida por remendo. A tarefa é um **documento com vários autores** — `scrum-master`,
   executor e reviewer —, o **principal canal de comunicação entre as partes**. O detalhamento do
   artefato é escopo da tarefa nova, executada em sequência. *(Conceito.)*
2. **A conciliação por recência fica restrita ao desenvolvimento** — §12.1. O invariante da `T27`
   ("registro já escrito não se reescreve") deixa de valer como isenção geral para orientação, e o
   RDO permanece fora. *(Desenvolvimento.)*
3. **Laudo — entendimento canônico vigente:** documento emitido pelo **reviewer** para o
   `scrum-master`, que o **consome e descarta**. O descarte existe porque o laudo é fonte potencial
   de poluição de contexto. O `scrum-master` coleta as informações **úteis** como insumo do
   desdobramento e descarta o resto; as informações do laudo **vivem apenas como argumento consumido
   no desdobramento**. O conceito de *utilidade* é card futuro. Só muda por decisão explícita do
   dono. *(Conceito — a matéria se concilia dentro do framework.)*
4. **Pacote — já decidido:** é o **conjunto de informações obrigatórias contidas no laudo**,
   suficientes para o `scrum-master` invocar o script de RDO sem falha. Não é objeto devolvido pelo
   executor. *(Conceito.)*
5. **`reviewer` é o nome canônico.** *(Conceito.)*
6. **Escopo primeiro:** na dúvida, perguntar se a discussão é de conceito ou de desenvolvimento
   antes de escolher onde a orientação reside. *(Desenvolvimento.)*

### 12.3 O que a rodada de replanejamento precisa reconciliar

- `T18` (entregue) grava o laudo como documento **persistente** em `docs/RDO/laudos/`, e o dossiê da
  `T19` manda o `close` lê-lo de lá com falha ruidosa se ausente — contra o descarte do item 3.
- O dossiê da `T19` e o da `T20` tratam `pacote` como objeto morto; pelo item 4 ele existe, dentro do
  laudo, com a suficiência declarada.
- `DP-D` §9 usa *inspetor* em seis linhas (item 5) e enuncia "o critério não é recência" (§12.1).
- `T26` manda gravar na `GOVERNANCA.md` que o `scrum-master` é o **único escritor** do `status`,
  contra a `DP-G`; e a premissa da `DP-G` — não existe campo material de `status` por tarefa —
  é derrubada pelo item 1, que dá material à tarefa.
- `pacote de retorno` sobrevive na residência única (`.claude/skills/diario-de-obras/SKILL.md`), na
  `docs/RUBRICA_DE_REVISAO.md` e na `GOVERNANCA.md`, sem tarefa que os cubra.
- `TK-31` fecha por conciliação, junto do item 5.
- Cards a autorar: o artefato **tarefa** (item 1) e o conceito de **utilidade** (item 3).

## 13. `DP-H` — a fronteira conceito × desenvolvimento, derivada

**Estado: FECHADA pela rodada de replanejamento de 2026-08-11, por derivação do insumo do dono
(§12), sem decisão nova.** O insumo já é orientação: esta seção **deriva** dele e não o reabre.
Nenhuma cláusula de `DP-A`..`DP-G` é revogada aqui; onde há reconciliação, ela está nomeada.

### 13.1 O que a `DP-H` ratifica

1. **A fronteira.** *Conceito do framework* (o que ele é — reside nos artefatos publicados) ×
   *desenvolvimento do framework* (como está sendo construído — reside no plano). Diante de qualquer
   orientação, a pergunta de escopo vem **antes** da escolha de residência.
2. **Recência restrita ao desenvolvimento.** Dentro dos planos de desenvolvimento do framework, o
   último entendimento do autor reescreve a orientação anterior que ele contradiz. Ela **não** entra
   em artefato publicado (`README.md`, `GOVERNANCA.md`, `ARQUITETURA_PANTONICA.md`), e o critério de
   desempate do framework em si **não foi decidido**. **Alcance:** dossiê de tarefa **já executada**
   é orientação e se concilia; o que **narra o ocorrido** — bullet de fechamento no diário, RDO,
   telemetria, histórico — é registro e **permanece intocado**. O invariante da `T27` ("registro já
   escrito não se reescreve") deixa de valer como isenção geral para orientação.
3. **Laudo.** Documento emitido pelo `reviewer` para o `scrum-master`, que o **consome e descarta**,
   porque é fonte potencial de poluição de contexto: ele colhe as informações úteis como insumo do
   desdobramento e descarta o resto, e o que veio do laudo vive **apenas como argumento consumido no
   desdobramento**. Confere com a decisão do dono de 2026-08-11 registrada nos achados do §9
   (alternativa `a`: o laudo é apagado; o RDO absorve o útil e **larga o ponteiro**). Só muda por
   decisão explícita do dono.
4. **Pacote.** Conjunto de informações obrigatórias **contidas no laudo**, suficientes para o
   `scrum-master` invocar o script de RDO **sem falha**. Não é objeto devolvido pelo executor — esse
   é o `pacote de retorno`, que está morto. **Reinterpretação declarada do `DA-6`:** juízo continua
   **calculado** por `rdo.py laudo` e nunca **originado** por agente; passar o valor calculado como
   argumento é **transcrição**, não autoria — o invariante protege a origem do juízo, não o canal.
5. **`reviewer` é o nome canônico**; *inspetor* sai do texto vigente.
6. **O RDO fica fora** desta conciliação: artefato do projeto, com mecânica própria.

### 13.2 O que a `DP-H` **não** decide

- **O critério de desempate do framework em si** — o item 2 vale para desenvolvimento e não se
  estende a artefato publicado. Quem quiser a regra para o framework precisa decidi-la.
- **Se o artefato `tarefa` substitui residências atuais** (dossiê no plano, laudo, RDO). A `T29` é
  incremental por invariante: se o desenho recomendado exigir mover residência, ela escala ao dono e
  para, em vez de decidir.
- **A forma portuguesa "revisor" em prosa corrente.** O identificador canônico é `reviewer` e
  *inspetor* está abolido; nenhuma varredura de "revisor" → "reviewer" é aberta por esta decisão.
- **A `DP-G` não é reaberta.** A queda da premissa "não existe campo material de `status` por tarefa"
  transfere para a `DP-I` a pergunta de **onde** o valor é materialmente gravado; **quem** o autora
  (executor, para `review` e `blocked`) e **quem** o materializa (só o `scrum-master`) continuam como
  a `DP-G` fixou.

### 13.3 Dossiês reconciliados nesta rodada

| superfície | o que mudou | fonte |
|---|---|---|
| `T19` | `close` deixa de ler laudo e recebe o `pacote` por argumento (cinco campos obrigatórios); `--laudos-dir` sai da CLI; template perde `{{LAUDO_PATH}}`; invariantes e verificação refeitos | itens 3 e 4 |
| `T20` | `pacote` deixa de ser objeto morto — existe dentro do laudo, com suficiência declarada; o que morre é `pacote de retorno`; o laudo é consumido e descartado | itens 3 e 4 |
| `T21a` | passo 9 passa a extrair o `pacote` do laudo, invocar o `close` com ele e **apagar** o laudo; "pacote inválido" vira "retorno inválido" no passo 5 | itens 3 e 4 |
| `T21b` | `A6` deixa de repassar o caminho do laudo na reexecução — vão o dossiê original e as diretivas atualizadas | item 3 |
| `DP-D`, achados do §9 | *inspetor* → `reviewer` (seis linhas); "o critério não é recência" passa a nomear a recência restrita ao desenvolvimento, preservando o argumento do objeto apagado | itens 1, 2 e 5 |
| `T23a` | a instrução de gravar o absoluto ("`status` escrito exclusivamente pelo `scrum-master`") passa à fronteira da `DP-G` — **fecha o `TK-31`** | item 2 |
| `T26` | some o absoluto; passa a depender da ratificação da `DP-I`, que fixa onde o `status` é gravado | itens 1 e 2 |
| kit publicado | o resíduo de `pacote de retorno` em `GOVERNANCA.md`, `docs/RUBRICA_DE_REVISAO.md` e `.claude/skills/diario-de-obras/SKILL.md` ganha cobertura: a `T31` | item 4 |

### 13.4 Cards autorados

`T29` (artefato `tarefa` → `DP-I`), `T30` (utilidade → `DP-J`) e `T31` (resíduo de `pacote de
retorno`). Os dois primeiros **decidem e param** para ratificação em lote; o terceiro é conformidade
e não para. Fila resultante, declarada no §5: `T19` → `T20` → `T31` → `T21a` → `T21b` → `T23b` →
`T24` → `T25` → `T29` → `T30` → [ratificação] → `T26` → `T27`.

## 14. `DP-K` — os quatro artefatos canônicos e o desempate do framework

**Estado: FECHADA pela rodada de replanejamento de 2026-08-11**, por **ratificação do dono** dos três
pontos que a `DP-H` devolveu (§13.2). O insumo entra e é derivado **na mesma passagem**: esta seção
registra o enunciado, declara o alcance de cada ponto pela fronteira do §12.1, reconcilia o texto
vigente e autora os cards. Nenhuma cláusula de `DP-A`..`DP-H` é revogada; onde há reconciliação, ela
está nomeada.

### 14.1 O que o dono enunciou

1. Em caso de ambiguidade no framework, **escalar para o dono**.
2. **Unificar para `reviewer`.**
3. O artefato **tarefa** *não* substitui os demais documentos. **Tarefa** é o artefato canônico de
   comunicação **entre os agentes** — a fonte da verdade da tarefa **em execução**. O **RDO** é o
   artefato canônico de comunicação do projeto **com o dono** — o documento da verdade da **entrega**,
   e pressupõe tarefa finalizada. O **laudo** é o artefato canônico de comunicação de **uma revisão
   realizada**: efêmero, só existe enquanto a tarefa está em execução, e tem por objetivo mover a
   tarefa para `done` ou devolvê-la para `in-progress`. O **plano** é o artefato canônico de
   materialização de um objetivo com sua implementação: antecede todas as tarefas, e **toda tarefa
   deriva do plano**. A tarefa é um **escopo localizado do plano**, numa unidade de execução com
   contexto coeso e finalidade granular.

### 14.2 O que a `DP-K` ratifica

1. **Desempate do framework — ambiguidade escala ao dono.** *(Conceito.)* Era o buraco que o §12.1 e a
   `DP-H` §13.2 declararam explicitamente **não decidido**. Fechado: exauridas as duas regras de
   precedência do `GOVERNANCA.md` §3.1 (específico vence geral; no empate, versionado vence
   não-versionado), a ambiguidade **não se resolve por palpite do agente nem por recência** — ela
   **escala ao dono**. A recência continua sendo regra de **desenvolvimento** (`DP-H` item 2) e não
   vira desempate do framework. **Residência:** `GOVERNANCA.md` §3.1 — *Residência e precedência da
   doutrina* —, que já é a superfície que decide colisão de doutrina; entra como **terceira regra de
   precedência**, sem seção nova. **Card:** `T32`. É a mesma rota que a máquina de estados já dá ao
   laudo `escalar` (`review` → `blocked`, `DP-F`) e que a `DP-B` dá ao executor: ambiguidade sobe,
   não se arbitra embaixo.
2. **`reviewer` é o termo único.** *(Conceito.)* A `DP-H` item 5 fixou o identificador e aboliu
   *inspetor*, mas deixou a forma portuguesa *revisor* livre em prosa (§13.2). O dono unificou: no
   texto **vivo** do kit e dos artefatos publicados, `reviewer` é a única forma — papel, prosa,
   `description` e tabela. **Alcance declarado:** o que **narra o ocorrido** (diário, histórico, RDO,
   telemetria) é registro e **permanece intocado**; o plano é desenvolvimento e concilia **quando a
   linha for tocada**, sem varredura; o *Revisor* do OpenSpec citado em
   `docs/benchmark/BM-03-fission-ai-openspec.md:26` é papel de **framework externo** e não é o nosso —
   fica. **Volume medido em 2026-08-11 (case-insensitive), no texto vivo — 18 ocorrências em 5
   arquivos:**

   | arquivo | ocorrências | dono da correção |
   |---|---|---|
   | `.claude/skills/scrum-master/SKILL.md` | 11 no corpo (`:94`, `:96`, `:100`, `:108`, `:111`, `:115`, `:135`, `:185`, `:186`, `:187`, `:236`) | `T21a` (7, passos 5–9) e `T21b` (4, tabelas e proibições) — **reescrevem essas mesmas linhas** |
   | `.claude/skills/scrum-master/SKILL.md` | 1 na `description` (`:3`) | `T33` — linha **espelhada**, muda junto com os espelhos |
   | `.claude/README.md` | 2 (`:19` espelho do agente, `:57` espelho da skill) | `T33` |
   | `README.md` | 1 (`:755`, espelho da skill) | `T33` |
   | `.claude/agents/pantonic-reviewer.md` | 2 (`:3` `description` espelhada, `:8` prosa) | `T33` |
   | `tests/test_rdo.py` | 1 (`:186`, docstring) | `T33` |

   **A `T31` não absorve o escopo:** ela já carrega 9 ocorrências em 3 arquivos sob teto 15, e as 18
   medidas somam 5 arquivos novos — o volume **estoura** o teto dela. A distribuição acima é por
   **residência**: 11 caem em cards que já reescrevem exatamente aquelas linhas (custo marginal zero),
   e as 6 restantes são **linhas espelhadas** ou fora do loop, que exigem paridade
   (`check-readme.ps1`) e por isso viram card próprio, a `T33`.
3. **A hierarquia dos quatro artefatos canônicos.** *(Conceito.)* Nenhum substitui o outro — é a
   resposta explícita à pergunta que a `DP-H` §13.2 devolveu:

   | artefato | o que é | interlocutor | ciclo de vida |
   |---|---|---|---|
   | **plano** | materialização de um objetivo com sua implementação | dono ↔ planejamento | **antecede** todas as tarefas; toda tarefa deriva dele |
   | **tarefa** | escopo localizado do plano, em unidade de execução com contexto coeso e finalidade granular; **fonte da verdade da tarefa em execução** | **entre os agentes** (`scrum-master`, executor, `reviewer`) | nasce do plano; vive enquanto a tarefa não é terminal |
   | **laudo** | comunicação de **uma revisão realizada** | `reviewer` → `scrum-master` | **efêmero**: só existe enquanto a tarefa está em execução; objetivo é mover para `done` ou devolver para `in-progress` |
   | **RDO** | documento da verdade da **entrega** | projeto → **dono** | **pressupõe tarefa finalizada**; nasce no fechamento e permanece |

   Consequência direta: a `T29` deixa de ter ramo de escalada por residência — o dono já respondeu que
   o artefato `tarefa` **não** substitui plano, laudo nem RDO.

### 14.3 O que a `DP-K` **não** decide

- **A forma do artefato `tarefa`** — campos, arquivo, quem escreve o quê, e **onde o `status` é
  materialmente gravado**. Continua sendo a `DP-I` (`T29`), agora com o ponto 3 como insumo fechado.
- **O critério de utilidade** (`DP-J`, `T30`). A hierarquia dá o **piso** — o que sobrevive ao laudo
  ou decidiu o desdobramento ou é registro necessário no RDO —, não o critério.
- **A `DP-F` não é reaberta:** os sete estados, a grafia (`in-progress` hifenizado, `ready`) e a
  máquina de transições continuam como ratificados. Ver §14.4.
- **O instrumento da escalada:** o ponto 1 fixa a **rota** (sobe ao dono), não canal novo — quem
  escala e como já está em `DP-B` (executor) e nas tabelas do `scrum-master` (`T21b`).
- **Nenhuma regra de recência entra em artefato publicado** (`DP-H` item 2, intocada).

### 14.4 Reconciliação medida — o ponto 3 contra o texto vigente

| superfície | medida | veredito |
|---|---|---|
| `DP-F` §3, máquina de transições | `review` → `done` (gatilho 2) e `review` → `in-progress` (laudo `refazer`) já existem, nomeadas | **confirmação** — o enunciado do dono nomeia a **finalidade** do laudo, não a enumeração da máquina |
| `DP-F`, `review` → `blocked` (laudo `escalar`, ou `refazer` com teto esgotado) | não é citado pelo dono | **não é contradição e não é aresta nova** — é a rota de escalada, que o **ponto 1 acabou de ratificar** como saída canônica da ambiguidade; permanece |
| "enquanto a tarefa estiver em execução" | `in-progress` é estado; `review` é outro (`DP-F`) | **alinhamento de leitura, sem mudança de grafia**: "em execução" aqui é *tarefa não terminal* (ciclo aberto), não o estado `in-progress`. O laudo **nasce** na entrada em `review` (gatilho 1) e **morre** no consumo pelo `scrum-master` |
| `DP-G` (autoria × materialização do `status`) | o laudo **recomenda**; não autora nem materializa `status` | **intocada** — recomendação não é autoria |
| `DP-H` item 3 (consumido e descartado) | descarte justificado por poluição de contexto | **reforçado**: a efemeridade passa a ser **propriedade do artefato**, enunciada pelo dono, e não só higiene de contexto |
| `T19` — `calcular_desdobramento(veredito, orcamento_estourado)`, `close` sem leitura de laudo, template sem `{{LAUDO_PATH}}` | o `close` opera sobre os cinco campos do `pacote` **já transcritos** como argumento | **compatível — nada muda**. A `T19` **segue delegável exatamente como está** |
| `T21a` passo 9 (apagar o laudo) | o apagamento está nomeado **só** no ramo `done` | **aresta real**: o laudo morre em **qualquer** desdobramento, não só no fechamento — a correção é uma linha na `T21b` (tabelas `A6`/`A7`/`B1`), não na `T21a`, cujo passo 9 já está correto no ramo que descreve |
| `T30` (utilidade) | o critério pressupunha o consumo no fechamento | **objeto intacto, piso ampliado**: como o laudo morre também na devolução e na escalada, o critério de utilidade vale nos três ramos — o que a reexecução precisa saber vem das **diretivas atualizadas**, nunca de reler o laudo |
| `T29` (artefato `tarefa`) | tinha ramo de escalada obrigatória por residência | **removido** — ver §14.5 e o dossiê reescrito |

### 14.5 Dossiês reconciliados e cards autorados

**Reconciliados nesta rodada:** `T29` (dossiê reescrito: sai o ramo de escalada por residência, entram
as definições do ponto 3 como insumo fechado, e o ponto de parada encolhe para o que sobrou a
decidir), `T30` (o laudo morre em qualquer desdobramento — o critério vale nos três ramos), `T21a`
(grafia canônica no texto que ela escreve), `T21b` (grafia canônica no corpo do arquivo, exceto a
`description` espelhada; e o descarte do laudo em `A6`/`A7`/`B1`), `T31` (fronteira declarada com a
`T33`).

**Cards autorados:** `T32` (desempate do framework → `GOVERNANCA.md` §3.1) e `T33` (`reviewer` nas
linhas espelhadas e no resíduo fora do loop). Nenhum dos dois decide nada: ambos **transcrevem**
decisão já ratificada, e por isso **não param** para aceite. Fila resultante, declarada no §5:
`T19` → `T20` → `T31` → `T32` → `T21a` → `T21b` → `T33` → `T23b` → `T24` → `T25` → `T29` → `T30` →
[ratificação] → `T26` → `T27`.

**Quanto da `DP-I` o dono já pré-decidiu:** das cinco perguntas da `T29`, **três** (definição,
mapeamento sobre o material existente e ciclo de vida) estão **respondidas** pelo ponto 3 — a `T29`
as **transcreve**. Sobram **duas**: autores e escrita, e conteúdo obrigatório (com o lugar material do
`status`, que a `T26` depende). O ponto de parada foi ajustado a esse resto no dossiê.

## 15. Insumo — uso e teto como medida agregada

**Estado: insumo do dono, 2026-08-11.** Não é decisão fechada — é o enunciado que fixa o escopo, o
portador e a pergunta da `T34`, cuja `DP-L` fecha e para para ratificação. O que disparou o insumo foi
o fechamento da `T31`: tarefa de classe redação com 9 pontos de edição em 3 arquivos consumiu os 15
tool uses do teto exatamente no fechamento e deixou a verificação órfã, que o orquestrador cobriu na
mesma rodada. A série já tinha o mesmo sinal em outras medidas (`T19` em 41 contra teto 40; a série
`UXROUND3` em 56/35, 61/40 e 112/50).

O insumo tem cinco pontos:

1. **A questão é de conceito de framework, não de desenvolvimento deste projeto.** O que se decide não
   é o número de uma tarefa nem o teto de uma classe: é o que o framework faz com uso e teto. A
   residência final é artefato publicado; este plano é onde a decisão se forma.
2. **Uso e teto são medidas de agregado, não de indivíduo.** Avaliadas tarefa a tarefa, medem ruído —
   a variação de uma tarefa isolada não distingue decomposição errada de tarefa que simplesmente
   custa o que custa. O valor da medida aparece no conjunto.
3. **O portador entre tarefas é o card "Lições aprendidas na tarefa".** Ele já existe por encomenda do
   dono e carrega metainformação **da tarefa, não do entregável** — é exatamente a natureza de uso e
   teto. Os números viajam nele de tarefa em tarefa e são lidos **em conjunto no fecho do plano**.
4. **Hipótese do dono, a confrontar:** o uso que se faz hoje desse controle é mais **poluição** do que
   valor ou economia efetiva. É hipótese, não premissa: a `T34` a confronta com a série medida e
   registra o veredito, seja ele qual for.
5. **Regime interino, com efeito imediato:** até a posição final, o teto **não é bloqueante nem
   impeditivo** de tarefa. A fila do plano segue sem esperar a `DP-L`. Materializado no §3, item 5.

**Reconciliação — decisão do dono, 2026-08-12.** Os cinco pontos acima permanecem como enunciados; o
que muda é **onde a posição se forma**. A matéria de uso e teto se revê **inteira e em plano próprio**,
aberto depois que o `P-0734` fechar, e não em card deste plano: a `T34` está **cancelada por absorção**
e nenhuma `DP-L` é formada aqui (§5; `### T34`). O ponto 1 fica reforçado — a questão é de conceito de
framework, e formar a posição dentro de um plano de desenvolvimento produziria decisão com prazo de
validade de um plano. O ponto 5 se prorroga: o regime interino vigora até a decisão do plano seguinte,
não até uma ratificação deste. O desdobramento é registrado pela `T17`, item 4, que carrega este §15,
o corpo da `T34` e o `TK-32` como insumo de abertura.

## 16. `DP-M` — a golden rule de escopo de agente e o laudo mínimo

**Estado: FECHADA por ratificação do dono em 2026-08-11.** O enunciado entra e é derivado na mesma
passagem: esta seção registra o que o dono disse, as duas escolhas que ele ratificou, o estado medido
que sustenta cada uma, o que a regra reclassifica no texto vigente e o fechamento do `TK-33`. Nenhuma
cláusula de `DP-A`..`DP-L` é revogada; onde há reconciliação, ela está nomeada.

### 16.1 O que o dono enunciou

O problema nunca foi **proibir** o `scrum-master` de ler o corpo do laudo — foi o laudo **ter corpo**.
Daí saem duas coisas, não uma:

1. **O laudo se padroniza por função, como o RDO, e passa a ser mínimo e suficiente.** Documento
   gerado por função com campo fechado ou calculado não tem prosa livre para alguém extrapolar; a
   fronteira deixa de precisar de vigilância porque o objeto deixa de oferecer a tentação.
2. **No lugar de coibir papel a papel, vale uma golden rule para todo agente** — *o agente se atém
   estritamente às suas responsabilidades declaradas; o que não é escrito é proibido*.

**Escopo declarado pelo dono:** isto é **conceito do framework**, não desenvolvimento dele (`DP-H`,
§13.2 item 1). A regra entra em **doutrina publicada**; o plano carrega **só as tarefas**.

### 16.2 O que a `DP-M` ratifica

1. **Golden rule de escopo — residência e forma.** *(Conceito.)* A regra mora em `GOVERNANCA.md` §7
   como **guardrail 15**, e a §3 (matriz de responsabilidades) **aponta** para ela sem reenunciá-la.
   O espelho `README.md` §10 sobe para **15 linhas, em lockstep** — é a contagem que
   `check-readme.ps1` compara (`.claude/checks/check-readme.ps1:158-199`: linhas `| N |` da seção "Os
   guardrails" do README contra itens `^\d+\. \*\*` de `GOVERNANCA.md` §7). **Consequência
   estrutural:** a matriz do §3 deixa de ser descrição e vira **autoridade exaustiva** — o que ela
   não declara, nenhum agente faz. **Cards:** `T35` (precondição) e `T36`.
2. **Laudo mínimo — `--observacoes` sai do gerador.** *(Conceito, materializado em instrumento.)* O
   campo de texto livre deixa de existir no laudo. **Risco assumido pelo dono:** marcação abaixo de
   `conforme` pode ficar **sem justificativa registrada**; não se cria campo substituto, e `--escalar`
   continua sendo o único canal de pendência. **Card:** `T38`.

### 16.3 Estado medido em 2026-08-11 (não se remede)

| fato | medida | consequência |
|---|---|---|
| o laudo já é gerado **por função** | `.claude/tools/rdo.py:481-492` — 6 dos 8 campos são fechados ou calculados | a padronização por função **já existe**; o que falta é tirar a prosa |
| prosa remanescente | `Pendência` (uma linha, consumida por `B1`) e `Observações` (texto livre, sem limite, **sem consumidor** — fora dos cinco campos do pacote) | só `Observações` é objeto da escolha 2 |
| residência do escopo de papel | `GOVERNANCA.md:104` já declara a matriz como **o único lugar** onde a fronteira de cada papel se declara | a residência **não muda**; falta a cláusula de fechamento |
| cláusula de fechamento | **não existe** — nada diz hoje que o não escrito é proibido | é exatamente o que o guardrail 15 acrescenta |
| completude da matriz | 7 papéis declarados (`GOVERNANCA.md:88-96`) contra os papéis vivos do kit | **precondição**: sob autoridade exaustiva, papel vivo fora da matriz nasce sem escopo — daí a `T35` |
| proibições que a regra devolve | 4 das 6 do `scrum-master` (`.claude/skills/scrum-master/SKILL.md:273`) e 5 das do `pantonic-reviewer` (`.claude/agents/pantonic-reviewer.md:83`) são do tipo "não faça o que é de outro papel" | passam a **derivar** da matriz e saem dos prompts — `T37` |

### 16.4 O que a regra reclassifica, e o fechamento do `TK-33`

**Critério de sobrevivência de uma proibição em prompt** — é ele que a `T37` aplica, e não julgamento
caso a caso: sobrevive a proibição que restringe o exercício da **própria** responsabilidade declarada
(fronteira **interna**); sai a que apenas repete que o papel não faz o que é **de outro**, porque a
matriz mais o guardrail 15 já a produzem. Poda não é revogação: **nenhuma regra perde efeito** — muda
de residência, da cópia no prompt para a matriz.

**`TK-33`, os três itens.** Os itens 1 e 2 continuam **mecânicos** e não dependem da `DP-M`; o item 3
é **decidido por ela**:

- **Item 3 — decidido.** A proibição *"Não abre o RDO nem o laudo"* **sai, sem fronteira substituta**.
  Com `Observações` fora, o laudo só tem campo fechado ou calculado: não sobra nada que o
  `scrum-master` possa extrapolar lendo, e os passos 7 e 9 leem o laudo **por desenho**.
- **Item 2 — fechado por derivação, sem decisão nova.** A `recomendação` que `A6`, `A8`, `A9` e `B1`
  leem é **campo fechado do laudo**, e é de lá que o passo 7 a colhe. O retorno de duas linhas do
  `reviewer` **não muda** (`DP-H`, `T21`) e nenhum campo novo é criado — a alternativa de acrescentar
  `recomendacao` ao retorno fica **recusada** aqui, para que o executor não a reabra.
- **Item 1 e o resíduo de `A2`** seguem como o tíquete os descreve: gatilho do passo 8 com `A5`
  inexistente, e `pacote` em `A2` na acepção velha (`A2` julga o **retorno** do executor; `pacote` são
  os cinco campos **do laudo**, `DP-H` item 4).

### 16.5 O que a `DP-M` **não** decide

- **Não cria responsabilidade nova para papel nenhum.** A `T35` fecha a matriz por **transcrição** do
  que já está publicado no prompt de cada papel; lacuna que exigiria doutrina nova vira **tíquete e
  sobe ao dono**, nunca invenção do executor.
- **Não abre varredura de proibições no kit inteiro.** A poda é dos dois arquivos medidos
  (`scrum-master` e `pantonic-reviewer`); proibição derivada em outro prompt é **achado**, não escopo.
- **Não reabre a `DP-K`** (hierarquia dos quatro artefatos) nem a `DP-J`/`T30`: o laudo continua
  efêmero, consumido e descartado — o que muda é **o que ele contém**, não o que se faz com ele.
- **Não mexe em versão.** Congelamento pré-lançamento em vigor (`GOVERNANCA.md` §10): sem bump, só a
  linha no `CHANGELOG.md` sob `[Não lançado]`.

### 16.6 Cards autorados e fila resultante

**Cinco cards, nenhum deles com ponto de parada:** `T35` (auditoria de completude da matriz — o
**resultado** dela é escrito como subseção nova `### 16.7`, ao final deste §16), `T36`
(guardrail 15 + espelho em lockstep), `T37` (poda das proibições derivadas), `T38` (`--observacoes`
sai do gerador) e `T39` (`TK-33`). Todos **transcrevem** decisão já ratificada e por isso **não param**
para aceite. Fila resultante, declarada no §5: `T33` → `T35` → `T36` → `T37` → `T38` → `T39` → `T23b`
→ `T24` → `T25` → `T29` → `T30` → `T34` → [ratificação em lote: `DP-I`, `DP-J`, `DP-L`] → `T26` →
`T27`.

### 16.7 Auditoria de completude da matriz — resultado

Medida executada na `T35` em 2026-08-12, papel vivo por papel vivo, contra a tabela
`| Papel | Modelo | Responde por | Não faz |` de `GOVERNANCA.md` §3. Os oito agentes de
`.claude/agents/` são o universo fechado do diretório; a orquestração é o único papel que vive numa
skill (`.claude/skills/scrum-master/SKILL.md`), e por já ter linha própria não gerou linha nova.
Contagem da matriz: **7 linhas antes, 9 depois**.

| Arquivo | Linha da matriz | Veredito |
|---|---|---|
| `.claude/agents/pantonic-planner.md` | **Planejamento** | Coberto — `## Suas responsabilidades` e `## O que você NUNCA faz` já estão transcritos nas duas colunas |
| `.claude/agents/pantonic-executor.md` | **Execução** | Coberto — uma tarefa por contexto sob TDD, handover, e a parada por plano não-pronto/obstáculo à rota já na coluna *Não faz* |
| `.claude/agents/pantonic-reviewer.md` | **Revisão** | Coberto — julgar uma entrega contra o dossiê e emitir o laudo, sem corrigir, replanejar ou fechar tarefa |
| `.claude/agents/pantonic-scout.md` | **Coleta** | Coberto — search/grep/leitura devolvidos como dossiê compacto, sem editar nem julgar |
| `.claude/agents/pantonic-auditor-arch.md` | **Auditoria** | Coberto — a linha nomeia o agente como uma das duas frentes permanentes |
| `.claude/agents/pantonic-auditor-cleancode.md` | **Auditoria** | Coberto — a linha nomeia o agente como a segunda frente permanente |
| `.claude/agents/pantonic-fora-da-caixa.md` | **Redesenho** (nova) | Lacuna **(a)** fechada — responsabilidade, saída e proibições já publicadas no prompt (`## Por que você existe`, `## Método por alvo`, POC validada fora do alvo, "propõe redesenhos — nunca os implementa"); modelo transcrito do frontmatter (`opus`) |
| `.claude/agents/pantonic-benchmarker.md` | **Benchmarking** (nova) | Lacuna **(a)** fechada — esquema fixo de 16 dimensões, evidência por URL ou `NÃO ENCONTRADO`, sem juízo sobre o PantonicApp, um repositório por invocação, todos já publicados em `## Guardrails do coletor`; modelo transcrito do frontmatter (`haiku`) |
| `.claude/skills/scrum-master/SKILL.md` | **Orquestração** | Coberto — papel que vive em skill, e a linha existente já responde por despachar, rotear pelo veredito e arquivar |

**Nenhuma lacuna (b).** Toda lacuna medida era de transcrição: os dois papéis ausentes tinham
responsabilidade e proibições publicadas no próprio prompt, e a matriz apenas não as espelhava.
Nenhuma responsabilidade nova foi criada, nenhuma proibição nova entrou na coluna *Não faz* das
sete linhas preexistentes e nenhuma proibição foi podada — a poda é da `T37`.

**Consequência para a `T36`:** a matriz está completa em relação aos papéis vivos, então a golden
rule pode ser publicada como autoridade exaustiva sem pôr papel vivo fora de conformidade no mesmo
ato. O número de aceite do espelho não muda por esta auditoria — a matriz é §3, e
`check-readme.ps1` compara a contagem de guardrails do §7.

## 17. `DP-N` — o executor sinaliza e nada mais; a coleta do entregável é do reviewer

**Estado: FECHADA por ratificação do dono em 2026-08-12**, com os três pontos que faltavam decididos
por ele na mesma passagem. Nenhuma cláusula de `DP-A`..`DP-M` é revogada: a `DP-G` fixou a **fronteira
de autoria** do `status` e esta seção fecha o que sobrava dela — **o que mais o executor faz** além de
sinalizar. Resposta: nada.

### 17.1 O que o dono enunciou

1. O executor **apenas atualiza o status da tarefa para `review` ou `blocked`**, e esse ato, na
   prática, é uma **mensagem para o `scrum-master`**. Nada mais é feito pelo executor.
2. A **coleta de informação do entregável é do `reviewer`**, que tem modelo mais potente, recebe o
   mesmo contexto de tarefa do executor e tem acesso ao **diff** — e é dessa posição que vem a
   isenção para aferir qualidade com honestidade e correção.
3. O `reviewer` gera o **laudo**, com o **pacote** (o que popula o script do RDO sem quebra) e uma
   **recomendação** para a responsabilidade de **desdobramento** do `scrum-master`.
4. É responsabilidade do executor **entregar o código funcional e conforme com as regras do
   projeto** — testes passando, golden rules seguidas. **Aferir a aceitação da entrega não é dele.**

### 17.2 O que a `DP-N` ratifica

1. **O executor não escreve em artefato nenhum do processo.** Não marca `in-progress`, não escreve
   bullet de fechamento, não invoca a skill `handover`, não registra o que fez e não grava linha de
   consumo. Ele **sinaliza** `review` ou `blocked`, e o sinal é mensagem — a materialização segue
   sendo do `scrum-master` em qualquer estado (`DP-G`, item 1). **Cards:** `T40` (o prompt), `T41`
   (as superfícies que o descrevem).
2. **Responsabilidade de entrega × responsabilidade de aceitação.** A verificação **fica** com o
   executor, mas com outro nome: ela não é aferição de aceitação, é o que faz a entrega sair
   tecnicamente correta. Alternativa recusada na ratificação: tirar a bateria do executor e deixá-la
   só no `review_evidence.py` — o executor passaria a sinalizar `review` sem saber se a suíte está
   verde, e o vermelho apareceria uma rodada depois.
3. **Achado fora de escopo vai numa linha do sinal.** O sinal já carrega conteúdo além do estado (a
   razão tipada do `blocked`, `DP-G`), então o achado é uma linha dele, e **quem indexa o tíquete é o
   `scrum-master`**. Nenhum papel novo nasce e nada se perde. Recusadas: deixar o achado só com o
   `reviewer` (perde o que o executor viu em arquivo que não editou, e por isso não está no diff) e
   manter o executor abrindo tíquete no diário (é escrita, e escrita é o que sai).
4. **O `reviewer` não muda.** Suas três entradas de julgamento — dossiê da tarefa, dossiê de
   evidência e diff — já são exatamente a coleta que o dono descreve, e o pacote de cinco campos mais
   a recomendação já são o que o laudo entrega (`DP-H` item 4, `DP-M`). "Mesmo contexto do executor"
   se lê como **o mesmo dossiê de tarefa**, e não como herdar a conversa de quem executou: narrativa
   de quem executou continua fora do julgamento (`.claude/agents/pantonic-reviewer.md:30-32`). Se o
   entendimento for outro, é emenda a esta seção — não interpretação de executor.

### 17.3 O que a `DP-N` **não** decide — e o `TK-36`

A passagem de bastão em si **não é reorganizada aqui**. Por decisão do dono, ela vira **tíquete
próprio (`TK-36`)**: reorganizar as skills `handover` e `proximo-passo` em **uma única skill nova**,
que execute a transição de tarefas suavemente — inclusive a passagem do contexto que precise ser
herdado de tarefa predecessora — e que tenha coerência com as responsabilidades do `scrum-master`
**sem exigir responsabilidade nova**. Se responsabilidade nova se mostrar necessária, o tíquete
**escala ao dono** em vez de criá-la.

Ficam com o `TK-36`, e por isso fora da `T41`: o §9 inteiro do `README.md` (*Handover e uma tarefa
por contexto*), `GOVERNANCA.md` §4 (`:333`, `:338`, `:342`) e §5 (`:240`, cerimônias), o *enforcement*
dos itens 8 e 9 do §7 ("gate de review no handover") e o corpo das duas skills.

**Superfície contraditória declarada, não omitida:** entre a `T41` e o `TK-36`, a doutrina do
handover ainda descreve um encerramento que o executor não faz mais. É contradição conhecida, com
dono e prazo — não é achado a redescobrir.

**O que segura o fluxo enquanto isso:** no fluxo `proximo-passo`, quem escreve o bullet de
fechamento, a telemetria e o índice é **o orquestrador** — prática já exercida na rodada da
`EXA-T23b` e agora obrigatória, não opcional (`T41`, item 4).

### 17.4 Cards autorados

**Dois, nenhum com ponto de parada:** `T40` (o prompt do executor) e `T41` (matriz §3, telemetria
§4.2, espelho do README, cláusula da `proximo-passo` e a linha da `guardrails-check`). Os dois
**transcrevem** decisão ratificada. Fila: entram logo depois da `T24` e antes da `T25` (§5). O
`TK-35` fecha na `T40`; o `TK-36` nasce aberto e **não** entra nesta fila — é escopo próprio, a
posicionar quando o dono o priorizar.

## 18. `DP-O` — a matriz é o limitador, e o texto que a contradiz é não-conformidade grave

**Estado: FECHADA por enunciado do dono em 2026-08-12**, na mesma passagem da `DP-N`. Não revoga
cláusula nenhuma: **estende a resposta** do guardrail 15 (`G-SCOPE`, `GOVERNANCA.md` §7 item 15) do
gate de prompt novo para o **artefato existente**, e converte a régua numa varredura com escopo
declarado.

### 18.1 O que o dono enunciou

A sanitização do framework quanto às responsabilidades do executor **vasculha todos os artefatos que
contradizem o entendimento vigente e regulariza**. E se faz à luz da **matriz de responsabilidades
como limitadora das responsabilidades de todos os agentes**, sob a premissa de que **tudo o que não é
permitido é proibido**: onde o texto do framework diz que um agente faz algo que a matriz **não
endossa** — ou que ela **sequer cita** —, isso é **não-conformidade grave**, e a resposta é **parar e
regularizar o quanto antes**.

### 18.2 O que a `DP-O` ratifica

1. **A régua já existe e não muda.** O item 15 do §7 já declara a matriz como autoridade exaustiva e
   já diz que prompt de agente **não cria** responsabilidade por conta própria. **Nada de novo entra
   no enunciado do guardrail**, e nenhum guardrail 16 nasce.
2. **O que entra é a resposta na descoberta.** Violação achada em artefato existente é
   **não-conformidade grave**, com resposta **parar e regularizar** — não vira linha de dívida a
   priorizar depois. O *enforcement* do item 15 passa a nomear a **varredura** ao lado do gate de
   prompt novo ou alterado. **Card:** `T42`.
3. **Alcance da varredura: todo artefato do framework**, em dois universos fechados e medidos —
   o **kit executável** (8 agentes + 11 skills, `T43`) e a **doutrina publicada com seus índices e
   espelho** (`T44`). O gatilho foi o executor, mas a régua vale para **todo** papel: violação da
   mesma classe em outro agente é a mesma não-conformidade.
4. **A lacuna oposta sobe ao dono.** Quando o ato atribuído pelo texto é **real e necessário** mas a
   matriz não o declara, a falta é da matriz — e resolver criando a responsabilidade no prompt é
   precisamente a violação. Registra-se como lacuna, vira tíquete indexado e sobe. É a mesma regra
   que a `DP-M` (§16.5) fixou para a auditoria de completude, agora aplicada na direção inversa.

### 18.3 O que a `DP-O` **não** decide

- **Não edita a matriz.** Nenhuma linha do §3 muda por esta decisão; a matriz só se altera por
  decisão do dono, alimentada pelas lacunas que a varredura registrar.
- **Não cria responsabilidade nem proibição.** Proibição em prompt continua sob o critério da `DP-M`
  (§16.4): sobrevive só a fronteira **interna** do próprio papel.
- **Não reescreve registro.** Bullet de fechamento, RDO emitido, entrada de `CHANGELOG.md` e seção do
  `docs/DIARIO_HISTORICO.md` narram o que aconteceu à época: contradizer a matriz de hoje ali é
  história, não não-conformidade.
- **Não invade o `TK-36`.** A doutrina de handover (o §9 do `README.md` e as superfícies listadas no
  §17.3) fica com aquele tíquete, mesmo quando a varredura cruzar com ela.
- **Não mexe em versão.** Congelamento pré-lançamento em vigor (`GOVERNANCA.md` §10).

### 18.4 Cards autorados

**Três, nenhum com ponto de parada:** `T42` (a resposta na descoberta, no item 15 e no espelho),
`T43` (kit executável) e `T44` (doutrina, espelho e índices). Os dois últimos entregam **edições da
classe (b) mais o relatório** `docs/audits/CONFORMIDADE_MATRIZ_2026-08-12.md`, e param — sem decidir
— diante de toda ocorrência da classe (c). Fila: bloco logo depois da `T41` (§5).

## 19. Critério de aceitação final — enunciado do dono (2026-08-13)

**Por que esta seção existe.** O plano vinha sem enunciado de aceitação. A origem (`:3`) e o §0
descrevem o **custo** que se quer eliminar; a `T16` **registra** cada acionamento do dono com a causa
que o motivou; a tabela de riscos (§6) trata o desaparecimento do round-trip como risco de consciência
situacional. Nenhum dos três diz **qual resultado aprova a entrega**, e um piloto que exigisse do dono
intervenção de despacho passaria pelo texto anterior. O enunciado abaixo fecha essa lacuna e é
**vinculante**.

**O estado final que aprova a entrega.** O dono **inicia o plano a ser realizado** — e nada mais. A
partir daí a skill `scrum-master` é acionada pelo agente do contexto corrente e se encarrega, sozinha,
de **criar os contextos novos**, **distribuir os handovers entre os agentes** e **resolver as questões
do projeto**, escalando ao dono **apenas quando a questão for dele**. As duas intervenções que o fluxo
vigente exige a cada tarefa — o dono limpar o contexto e o dono invocar a próxima tarefa — **deixam de
existir**.

**A aceitação classifica cada acionamento pela causa.** Não existe teto de vezes que o gerente pode
ser acionado: um limite desses ou não tem valor, ou é arbitrário — não há de onde derivá-lo —, e
métrica arbitrária não governa aceitação. Nenhum número de acionamentos aprova ou reprova a entrega.

- **Causa que é do gerente — legítima e ilimitada.** Dirimir ambiguidade e resolver conflito,
  sobretudo de **requisito** e de **aceitação**, é responsabilidade dele, e nenhuma métrica a
  restringe. O risco fatal declarado é o agente decidir aspecto de aceitação sem estar
  **inequivocamente** seguro de que é a melhor solução; diante dessa dúvida, escalar é o
  comportamento **desejado**, e nunca um custo a minimizar.
- **Causa que é ineficiência da entrega.** O framework solicitar acionamento do gerente em **caminho
  feliz ou caminho natural** — sem pendência aberta e sem demanda que seja dele. Parar para que ele
  limpe o contexto e invoque a tarefa seguinte é o caso exemplar: o plano corre sem problema e o
  gerente está **mediando execução normal**, que é exatamente a ineficiência que este framework
  existe para eliminar. **Uma só** ocorrência dessas já é achado de ineficiência; não há franquia
  a gastar.

A residência do conceito na doutrina publicada é `GOVERNANCA.md` §4.3, com o gancho para o §3.1
item 3 — a regra de ambiguidade sem desempate, que este critério complementa.

**Consequência direta para a unificação `handover` + `proximo-passo` (`TK-36`).** A skill que nascer
daquela unificação é **maquinário estrito do `scrum-master`**, na superfície **agente↔agente**, e é
**transparente para o gerente do projeto** — ele não a invoca, não a lê e não a acompanha. Ela prima
por **eficiência e qualidade da transição**, incluindo a herança de contexto entre tarefas
predecessora e sucessora; **não** é, e não deve virar, uma skill de comunicação com humano.

**Fronteira declarada contra o `TK-38`.** As duas superfícies são **eixos distintos e não se
misturam**: o `TK-38` governa a superfície **agente↔humano** (compreensão, expansão de nomenclatura,
suficiência do corpo da mensagem); o `TK-36` governa a superfície **agente↔agente**. Arrastar
requisito de comunicação humana para dentro da skill unificada acrescentaria custo a **toda iteração**
do loop autônomo — o oposto exato do objetivo deste plano — e é ambiguidade que **põe em risco a
aceitação da entrega final**. Nenhum planejamento derivado pode tratar os dois tíquetes como a mesma
matéria.

## 20. `DP-P` — decisão estruturante regulariza a superfície de contato, no ato

**Estado: FECHADA por enunciado do dono em 2026-08-13**, na rodada imediatamente seguinte ao
fechamento da `T45`. Não revoga cláusula nenhuma: **nomeia como guardrail** uma obrigação que o
plano vinha cumprindo por hábito, e converte a obrigação numa consolidação com escopo declarado.

### 20.1 O que o dono enunciou

Antes de o plano prosseguir é necessário promover a **sanitização e consolidação** do documento —
do contrário, fatalmente haverá um ponto em que o agente **para para solicitar a regularização a
posteriori**, sem o contexto do ato que a originou, ou, no pior cenário, há **risco de poluição**. E
isso vira **golden rule do framework**: mudanças de decisões estruturantes, como a correção ou a
modificação de **objetivos-chave, requisitos e casos de uso**, demandam **ação imediata de
regularização de toda a superfície de contato**.

### 20.2 O que a `DP-P` decide

1. **A regra é guardrail nomeado**, `G-SURFACE`, item **16** do `GOVERNANCA.md` §7, espelhado no
   `README.md` §10 na mesma rodada. Golden rule do dono vira guardrail — é a mesma rota que a `DP-M`
   deu ao escopo de agente, que virou o item 15.
2. **O gatilho é a decisão estruturante**, não toda mudança: correção ou modificação de
   objetivo-chave, requisito ou caso de uso — o que altera o que o trabalho *é*. Refinar redação,
   corrigir número ou trocar âncora não dispara a regra.
3. **A ação é imediata e a superfície é inteira.** A rodada de planejamento que fecha a decisão
   estruturante **emite os cards de regularização no mesmo ato**, e a fila não avança sem eles. O
   plano deixa de poder registrar a decisão nova e seguir com o texto antigo vivo em outro lugar.
4. **O custo que a regra evita é o da Regra 2.** Regularização a posteriori é paga por um agente que
   não tem o contexto do ato — e, se ele ingerir o texto vigente e o derrubado lado a lado antes de
   perceber, o contexto está poluído, e contexto poluído não se recupera, se substitui
   (`GOVERNANCA.md` §4.3).
5. **Aplicação imediata à própria iniciativa.** A `T45` acabou de mudar o critério de aceitação — uma
   decisão estruturante — e o `TK-40` é o primeiro resíduo medido dela. A consolidação é executada
   agora, em dois universos fechados: o **plano** (`T47`) e os **artefatos publicados** (`T48`).

### 20.3 O que a decisão **não** faz

- **Não reabre decisão ratificada.** Consolidar é tornar legível o que foi decidido; toda `DP-*`
  fechada permanece com o conteúdo que tem.
- **Não reescreve registro.** Bullet de fechamento, RDO emitido, entrada de `CHANGELOG.md`, seção do
  `docs/DIARIO_HISTORICO.md` e snapshot de fila dentro de rodada antiga narram o que aconteceu à
  época: divergir do entendimento de hoje ali é história, não não-conformidade.
- **Não cria papel nem responsabilidade.** A matriz do §3 não muda; a regularização é ato de
  planejamento e de redação, ambos já declarados.
- **Não mexe em versão.** Congelamento pré-lançamento em vigor (`GOVERNANCA.md` §10).

### 20.4 Cards autorados

**Três, nenhum com ponto de parada:** `T46` (o guardrail 16 e o espelho em lockstep), `T47`
(consolidação do plano) e `T48` (consolidação dos artefatos publicados). Os dois últimos entregam
**edições da classe (b) mais o relatório** `docs/audits/CONSOLIDACAO_SUPERFICIE_2026-08-13.md`, e
param — sem decidir — diante de toda ocorrência da classe (c). Fila: bloco à frente da `T29` (§5). O
`TK-40` é quitado dentro da `T47`, como ocorrência de classe (b) já medida.

## 21. `DP-Q` — número arbitrário não governa fluxo

**Estado: FECHADA por enunciado do dono em 2026-08-13**, ao decidir as duas ocorrências de classe
(c) que a `T47` fez subir (`TK-41`). É a **primeira aplicação real do `G-SURFACE`**: decisão
estruturante enunciada, cards de regularização emitidos no mesmo ato, fila parada até que a
superfície esteja regularizada.

### 21.1 O que o dono enunciou

O estouro de teto apresenta **a mesma questão do limite de round-trips**: são números arbitrários
que só geram **ruído**, e ações baseadas em ruído são decisões equivocadas. Há um plano futuro para
doutrinar a matéria, então esses limites **não são abordados neste plano**. Por ora, o entendimento
vigente é que informações de custo e consumo são **informativas** e **não têm valor em isolamento**:
só apresentam insight quando analisadas **em conjunto**. Essas informações são registradas hoje nas
**"lições aprendidas" do laudo do `reviewer`**, quando este **enxergar**; do contrário,
desconsiderar. O fim de janela segue o mesmo caminho — e, existindo risco de um **limite não
conscientemente delimitado** estar afetando o fluxo do processo, como é o caso de um teto arbitrário
encerrando uma tarefa legítima, isso é **vício**: para-se, abre-se card novo, reescreve-se a regra e
sanitizam-se os artefatos atingidos.

### 21.2 O que a `DP-Q` decide

1. **Nenhum teto numérico governa fluxo.** Não recusa entrega, não roteia, não encerra tarefa e não
   encerra janela. Caem, nominalmente, o roteamento por estouro de teto (`A4`) e os dois números do
   fim de janela (`B2`: dez tarefas fechadas, 900 k tokens acumulados).
2. **Medir permanece; decidir por medida sai.** A série `docs/telemetria.tsv` continua alimentada
   sem exceção — é exatamente o **agregado** que a decisão declara ter valor. O que se remove é o
   poder de porteiro, nunca a medição.
3. **A residência do qualitativo por tarefa é o card "Lições aprendidas na tarefa"** do laudo, e o
   preenchimento é **discricionário do `reviewer`** — quando ele enxergar algo. Sem observação, o
   número da tarefa isolado se **desconsidera**. Isto é **insumo fechado para a `DP-J`**, e não
   resolução dela: a `T30` segue na fila e segue à ratificação em lote com a `DP-I`.
4. **Limite não conscientemente delimitado que afeta o fluxo é vício**, e a resposta é a do
   `G-SURFACE`: parar, reescrever a regra e sanitizar a superfície atingida — não enfileirar como
   dívida.
5. **A matéria de limites não se doutrina aqui.** Ela se revê **inteira**, no plano próprio já
   previsto (desdobramento da `T17` item 4, onde a `T34` foi absorvida, e residência do `TK-32`).
   Nenhum número novo entra no lugar dos que caem — inclusive porque derivá-lo agora seria repetir o
   defeito que a decisão nomeia.
6. **O que passa a encerrar janela** são as duas condições que o `GOVERNANCA.md` §4.3 já governa e
   que **não** são arbitrárias: **coesão** (sinal de poluição, fatal e imediato) e **capacidade**
   (ocupação da janela de contexto). Cai, por ser o vício em forma explícita, a cláusula que elegia
   o teto de tool uses por classe como *proxy operante* de capacidade. A `T13` deixa de ser
   instrumento opcional e passa a ser o único critério de capacidade disponível ao agente, e por
   isso é repositionada na fila (§5). **Consequência declarada e aceita:** entre a `T49` e a `T13`,
   o encerramento se apoia só em coesão e no fim do plano.

### 21.3 O que a decisão **não** faz

- **Não enfraquece parada de causa.** `pendencia=`, `escalar`, `premissa` (`A3b`), reprovação após a
  última retentativa (`A7`) e plano não-pronto (`B3`) permanecem íntegros. A decisão remove porteiro
  numérico; escalada legítima continua **ilimitada** (§19).
- **Não apaga medição nem histórico.** A série, os RDOs emitidos, os bullets de fechamento e as
  entradas de `CHANGELOG.md` publicadas narram o que aconteceu à época.
- **Não cria guardrail.** O `G-SURFACE` (item 16) já é a régua; esta é a sua primeira aplicação.
- **Não mexe em versão.** Congelamento pré-lançamento em vigor (`GOVERNANCA.md` §10).

### 21.4 Cards autorados

**Três, nenhum com ponto de parada:** `T49` (a régua na doutrina), `T50` (a regra no loop) e `T51`
(sanitização da superfície atingida, com o terceiro bloco do relatório
`docs/audits/CONSOLIDACAO_SUPERFICIE_2026-08-13.md`). Fila: bloco logo depois da `T48` e antes da
`T29`, com a `T13` sucedendo-o (§5). O `TK-41` é quitado por esta decisão; a parte interina do
`TK-32` é absorvida aqui, e o restante daquele tíquete segue para o plano próprio.

## 22. `DP-R` — o hook canônico tem residência versionada; a máquina só recebe a materialização

**Estado: FECHADA.** O ***quê*** foi **decidido pelo dono em 2026-08-15**, sobre o `TK-43` aberto
pelo achado da `T13`. As **derivações de planejamento** — onde o artefato mora, como se materializa,
o que o guarda cobra e como a matéria se parte em tarefas — foram fechadas na rodada de
replanejamento do mesmo dia, **sem decisão nova de arquitetura nem de requisito**. Os dois blocos
estão separados abaixo de propósito: o §22.1 é do dono, o §22.3 é do planejamento.

### 22.1 O que o dono decidiu, e o que ele recusou

**Decidido:** hook canônico **ganha residência versionada própria**, com **materialização** no
`.claude/settings.json` local.

**Recusada** a alternativa que estava na mesa — assumir o proxy de ocupação como instrumento
só-do-hub. Motivo registrado com a decisão: o `GOVERNANCA.md` §4.3 afirma a **capacidade** como
condição vinculante para todo projeto Pantonic\*, não só para o hub; aceitar o proxy como local
transformaria regra publicada em regra sem meio de cumprimento no consumidor — o apodrecimento que a
§7.1 existe para impedir.

**O fato que abriu a decisão**, medido e não inferido: `.claude/settings.json` está em
`.gitignore:3`, sob o comentário "Configuração local de máquina — nunca canônica". A `T13` registrou
ali o hook do proxy porque o dossiê `### T13` nomeava esse arquivo como alvo; o instrumento funciona
na máquina do dono, mas nada dele viaja, e `kit_check` não o vê. A `T14` tinha o mesmo alvo e herdava
o mesmo defeito.

### 22.2 O que a decisão obriga

1. **Arquivo de máquina nunca é origem.** Hook do kit nasce em artefato versionado; o `settings.json`
   local é **produto**, e todo hook registrado direto nele é resíduo.
2. **Materializar não pode destruir.** A configuração de máquina do consumidor — a começar pelo
   `permissions.deny` que o guardrail 13 exige — sobrevive intacta a qualquer materialização.
3. **O que não se verifica, apodrece.** A residência nova entra acompanhada de guarda executável na
   bateria de fechamento, nos dois sentidos: canônico sem materialização **e** hook de kit no local
   sem declaração no canônico.

### 22.3 Derivações de planejamento (fechadas nesta rodada, não pelo dono)

1. **Residência:** `.claude/hooks/hooks.json` — arquivo versionado, uma chave de topo (`hooks`), no
   mesmo esquema que o harness lê. Não vai para `.claude/tools/` (que é instrumento executável) nem
   para `.claude/checks/` (que é verificador): é **declaração**, e ganha diretório próprio, que viaja
   no subtree de `.claude/` como `tools/` e `checks/` já viajam.
2. **Portabilidade do caminho:** o comando é escrito com o placeholder `{KIT_ROOT}`, resolvido na
   materialização — `.claude` no hub, `.claude/kit` no consumidor. Sem isso, o comando correto no hub
   seria um caminho inexistente no consumidor, e a distribuição continuaria decorativa.
3. **Materializador:** `.claude/tools/hooks_sync.py`, com `apply` / `check` / `drift`, idempotente,
   preservando toda chave de topo que não seja `hooks` e toda entrada de hook que não seja do kit.
   Python, e não PowerShell, por duas razões: manipulação de JSON com merge parcial, e o invariante
   §3 item 2 (instrumento nasce com teste) que a suíte `pytest` do hub já sustenta.
4. **Guarda:** `kit_check.ps1 -Mode validate` passa a exigir o **canônico** válido (existe, parseia,
   comandos apontam para arquivo existente); `-Mode check-drift` passa a exigir a **materialização**
   em dia, e falha também quando o local traz hook de kit não declarado. A ausência de
   `settings.json` **é** falha de `check-drift`, com o comando de remédio na mensagem: silenciar a
   ausência recriaria o `TK-43` com outra roupa. Os dois modos delegam ao `hooks_sync.py` para que a
   semântica de merge tenha **uma** implementação.
5. **`sync-kit.ps1` não muda.** O contrato dele é espelhar `skills/` e `agents/` no namespace plano do
   consumidor; hooks viajam pelo subtree e materializam por comando próprio. Estender um script
   provado ponta a ponta sem medida que justifique é o que o §7 posterga até o gatilho de propagação.
6. **Alcance — `DA-3` se mantém, e o porquê:** nenhum repositório derivado é tocado. `docs/CONSUMIDORES.md`
   registra **0/6** consumidores com `.claude/kit/` instalado, então a exigência nova não muda hoje o
   estado de consumidor nenhum; ela passa a valer no momento em que algum instalar o kit, que é
   exatamente o momento em que a materialização é um comando da instalação. A promoção do resto do
   desenho a kit distribuído continua com gatilho no §7, após o piloto da `T16`.
7. **Partição:** dois cards, `T53` (executável: residência, materializador, testes, guarda) e `T54`
   (superfície publicada: `.gitignore`, `GOVERNANCA.md` §3.1, `README.md` §11 e §13, `CHANGELOG.md`),
   por volume — um card só passaria de oito write-clusters — e por natureza, já que o segundo é
   redação de documento publicado, sob a `redacao-doc`. Executam **em bloco e em sequência**, com a
   consequência declarada e aceita: entre a `T53` e a `T54` a doutrina publicada está atrasada em
   relação ao kit, por uma tarefa.

### 22.4 O que a decisão **não** faz

- **Não cria superfície de doutrina.** Hook continua sendo **enforcement** de regra que mora em uma
  das quatro superfícies do §3.1 — o que muda é onde ele é declarado e o fato de que agora viaja.
- **Não move o hook global do `modelo-por-fase`** (`GOVERNANCA.md` §3, `:114-120`). Pelo critério
  desta decisão, hook **de kit** é o que executa comando do kit; aquele executa configuração de
  máquina do dono e permanece global.
- **Não cria guardrail** (`DA-10`), não bumpa versão (`DE-7`) e não reescreve narrativa histórica.
- **Não toca `permissions.deny` nem o guardrail 13** — a lista de subcomandos negados continua onde
  está, com as 6 entradas vigentes.

### 22.5 Questão adjacente, **não decidida** — sobe ao dono

O `permissions.deny` do guardrail 13 tem **o mesmo defeito de distribuição** que o `TK-43` documenta
para hook: é enforcement declarado de uma regra publicada, e vive num arquivo ignorado pelo git, de
modo que a allowlist de subcomandos destrutivos também não viaja para consumidor nenhum. A decisão de
2026-08-15 fala de **hook**, e estender o alcance a permissões seria requisito novo, não derivação —
por isso fica **fora** da `T53` e da `T54`, registrada aqui e reportada ao dono. Nada nesta rodada
depende dessa resposta: o materializador preserva `permissions.deny` intacto em qualquer cenário.

**Fechada em 2026-08-15.** A decisão do dono sobre o alcance do pacote respondeu a pergunta acima em
forma geral, e a invariante da régua nova (`GOVERNANCA.md` §3.1 — nada canônico mora só num ponto de
carga) a decide sem requisito novo: a lista de subcomandos negados é enforcement de regra publicada,
logo é canônica. Execução na `DL-7` do `P-0735`, que a torna chave declarada do manifesto de
projeções; `permissions.allow` permanece local de máquina.

### 22.6 Cards autorados

**Dois, nenhum com ponto de parada:** `T53` (a residência, o materializador e o guarda) e `T54` (a
superfície publicada). Fila: bloco logo depois da `T13` e antes da `T29` (§5). O `TK-43` é quitado
pelos dois; a `T14` teve o dossiê reescrito na mesma rodada, com a rota antiga invalidada e
dependência declarada da `T53`. O `TK-44` (dossiê de evidência não discrimina escopo) **não** é
matéria desta decisão e segue com tíquete próprio.

## 23. `DP-S` — a identidade da tarefa viaja por estado do loop, não por inferência sobre prosa

**Estado: FECHADA.** O ***quê*** foi **decidido pelo dono em 2026-08-19**, sobre o terceiro ramo que a
`T14` mediu. As **derivações de planejamento** — onde o estado mora, quem o escreve, o que o hook lê e
como a matéria se parte em tarefa — foram fechadas na rodada de replanejamento do mesmo dia, **sem
decisão nova de arquitetura nem de requisito**. Os dois blocos estão separados abaixo de propósito: o
§23.1 é do dono, o §23.3 é do planejamento.

### 23.1 O que o dono decidiu, e o que ele recusou

**Decidido:** o `scrum-master` **grava a tarefa corrente num ponto de estado conhecido do kit no ato
do despacho**, e o hook de `SubagentStop` lê a identidade de lá.

**Recusada** a alternativa que a própria `T14` levantou e descartou: inferir a identidade por regex
sobre a prosa do prompt do subagente. Motivo registrado com a decisão — inferência sobre texto livre
falha nos dois sentidos, e o sentido ruim é silencioso: ou não escreve nada, ou grava uma linha da
série com `tarefa` errada, que é pior do que linha ausente, porque contamina a única fonte de número
do framework.

**O fato que abriu a decisão**, medido e não inferido (Sonda 5,
`docs/audits/SPIKE_HARNESS_EXECUCAO_AUTONOMA.md:154-195`): o evento `SubagentStop` **existe** e o
payload traz `agent_id`, `agent_type` e `agent_transcript_path` — um `.jsonl` exclusivo do subagente,
com `message.usage` e `message.model` por entrada. O consumo, portanto, **está exposto**. O que não
existe é campo de schema que carregue a identidade da tarefa: ela vive só como texto livre no prompt.
O plano enumerava dois ramos (viável / inviável) e o medido foi um terceiro — só falta um **contrato**
que carregue a identidade até o hook.

### 23.2 O que a decisão obriga

1. **Identidade vem de contrato, nunca de inferência.** O que o hook precisa saber e o harness não
   carrega é **escrito** por quem sabe, no ato em que sabe.
2. **Ausência de estado é silêncio, não erro.** Despacho fora do loop não tem estado a ler; o hook
   sai em exit 0 sem escrever, e o fluxo manual da `T7` continua íntegro. Falha aberta total: hook
   não bloqueia nem atrasa chamada nenhuma, como o proxy da `T13`.
3. **O que não se verifica, apodrece.** A declaração do hook entra no canônico versionado e a
   materialização é cobrada pela bateria de fechamento — não se repete o `TK-43` com outra roupa.

### 23.3 Derivações de planejamento (fechadas nesta rodada, não pelo dono)

1. **Residência do estado:** `.claude/estado/tarefa-corrente.json`, **local de máquina**, no
   `.gitignore`. Pela pergunta zero da régua (`GOVERNANCA.md` §3.1), o conteúdo é fato de **uma
   sessão numa máquina** — qual tarefa está despachada agora —, não autoridade do framework: nada
   canônico mora ali, e nenhum consumidor precisa recebê-lo. O que viaja é a **declaração** do hook e
   o **código** que lê o estado, ambos versionados.
2. **Autor do estado:** o `scrum-master`, no **Passo 4** (`:84-107`), no ato do despacho. A tarefa
   corrente já é estado declarado do loop (`## Estado do loop`, `:31-32`); a mudança é de **forma**,
   não de escopo — ela passa a ser escrita onde outro processo lê. Nenhum contador novo entra na
   tabela do `:25-29`, e o "três contadores, e só três" segue verdadeiro.
3. **Hook:** `SubagentStop` → `.claude/tools/telemetria_hook.py`, declarado em
   `.claude/projecoes.json`, `alvos.projeto.chaves.hooks` (`:7-19`), com o comando em `{KIT_ROOT}` —
   mesma forma da entrada `PreToolUse` → `ocupacao.py` que já está ali. Nada nasce no
   `settings.json`, que é produto do `materializar.py apply`.
4. **Filtro e ordem:** o hook age só quando `agent_type` é papel do kit, e **consome** o estado
   depois de escrever a linha — a staleness fica limitada a uma janela, e um despacho abortado não
   deixa identidade órfã para o despacho seguinte herdar.
5. **Números:** `tokens_k` somado do `agent_transcript_path` (`input + cache_creation + cache_read +
   output` por entrada `assistant`), `tool_uses` por contagem de blocos `tool_use`, `duracao_s` pela
   diferença de `timestamp`. Mesmo padrão de parse que `ocupacao.py` já usa; nenhum leitor novo se
   inventa. `--fonte usage`, porque o número vem do transcript e não de contagem do orquestrador — e
   a calibração contra o `<usage>` de um despacho aninhado trivial é obrigatória antes de pronto.
6. **Partição:** **um** card, `[Sonnet · classe implementação padrão · teto 40]`. Seis
   write-clusters medidos (skill, script novo, manifesto, `.gitignore`, teste novo, calibração),
   dentro do limite de oito — não há razão de volume nem de natureza para partir.

### 23.4 O que a decisão **não** faz

- **Não altera `.claude/tools/telemetria.py`.** O hook é **cliente** do CLI que a `T7` entregou;
  duplicar validação de coluna ali recriaria o gabarito que a `T15` acabou de tirar dos prompts.
- **Não revoga o fluxo manual da `T7`.** Ele continua sendo o caminho de toda execução fora do loop,
  e é o que o silêncio do hook preserva.
- **Não torna o estado canônico.** Nenhum artefato do framework passa a depender de lê-lo; ele é
  insumo de um hook, e a ausência dele é caso previsto.
- **Não cria guardrail** (`DA-10`), **não bumpa versão nem tag** (`DE-7`) e não reescreve narrativa
  histórica: o bullet de fechamento da `T14`, o RDO dela e a linha de telemetria contam o que
  aconteceu à época, e o ramo B permanece o resultado correto daquela tarefa.

### 23.5 Cards autorados

**Um, sem ponto de parada:** `T55` (o estado, o hook, a declaração e o teste). Fila: logo depois da
`T15` e antes da `T16` (§5). O denominador do plano passa de **60** para **61**. A `T14` **não é
reaberta** — fechou corretamente em ramo B, e recebe só nota datada apontando para esta seção.

## 24. Rebase pelo `P-0737`

Este plano fica **`superseded`** por classificação (B) — substituído por
`docs/plans/P-0737-loop-autonomo.md`, que absorve as 9 tarefas abertas abaixo (8 absorvidas + 1
cancelada por absorção) e assume a iniciativa `EXECUCAO-AUTONOMA` como plano vivo único.

| Tarefa do `P-0734` | Matéria | Destino |
|---|---|---|
| `T29` — artefato `tarefa`, fecha a `DP-I` | doutrina · decide-e-para | **absorvida** → `AUT-T2` |
| `T30` — utilidade do laudo, fecha a `DP-J` | doutrina · decide-e-para | **absorvida** → `AUT-T3` |
| `T19` — `rdo.py`: o RDO se gera no fechamento | implementação | **absorvida** → `AUT-T4` |
| `T12` — reconciliação com `proximo-passo` | kit executável | **absorvida** → `AUT-T6` (a decisão que ela deveria tomar já veio pronta pela `DU-5`: forma (b)) |
| `T23b` — `proximo-passo` aponta para a residência única | kit executável | **absorvida** → `AUT-T6` (a skill-alvo deixa de existir; a skill nova nasce já falando a lista final da `DP-F`, o que entrega o efeito sem a edição) |
| `T26` — conformidade: doutrina normativa | doutrina | **absorvida** → `AUT-T8` |
| `T27` — conformidade: kanban, planos vivos e varredura de fecho | doutrina + kanban | **absorvida, dissolvida em duas** (`DU-10`) → `AUT-T8` (doutrina, com o `TK-30`) + `AUT-T9` (kanban, planos vivos e varredura) |
| `T17` — `README.md`, `CHANGELOG.md` e veredito do dono | fecho | **absorvida** → `AUT-T10` |
| `T16` — piloto medido | validação | **cancelada por absorção** — a matéria migra integral para o **plano recomendado do piloto** (`DU-3`), emitido pela `AUT-T10`. |
