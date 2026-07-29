# Candidatos a mudança — backlog priorizado (`C-NN`)

Origem: `docs/plans/P-0729-v2-confronto.md` §2 `T4` (Estágio 2 da iniciativa `PANTONIC-V2`).
Insumo único: `docs/benchmark/RELATORIO_CONSOLIDADO.md` (`V2C-T3`, 808 linhas, 16 vereditos +
6 dimensões novas + 8 descartes + 8 vieses).

**Regra de rastreabilidade (bloqueante):** todo `C-NN` cita a seção e as linhas do consolidado que
o originaram. Candidato sem origem no consolidado é ideia do executor e **não entra** — por isso as
seções §4 e §5 deste arquivo registram, com motivo, o que deliberadamente **não** virou candidato.

**O que este arquivo não faz:** não decide. A coluna de decisão do dono é preenchida em `V2C-T5`
(`adotar` / `adaptar` / `rejeitar` / `adiar`, com uma linha de motivo quando ≠ `adotar`), e só depois
o `V2C-T6` converte os candidatos ratificados em tarefas do Estágio 3B. A recomendação do planejador
está visível em cada ficha, mas é recomendação — não decisão tomada.

**Fonte da verdade da decisão:** a linha `Decisão do dono` **dentro da ficha** de cada candidato. O
índice da §1 não tem coluna de decisão de propósito, para não criar dois lugares onde a mesma
decisão pode divergir.

**Ratificação (`V2C-T5`) — concluída em 2026-07-29, 15/15 decididos.** `adotar` 12 (`C-01`, `C-02`, `C-03`, `C-04`, `C-05`, `C-06`, `C-07`, `C-09`, `C-11`, `C-12`, `C-13`, `C-14`) · `adaptar` 2 (`C-08`, `C-10`) · `adiar` 1 (`C-15`) · `rejeitar` 0. Uma única divergência da recomendação do planejador: `C-14` (recomendado `adiar`, decidido `adotar`). Esforço somado dos 14 ativos: **19 tarefas atômicas estimadas**. Insumo fechado para o `V2C-T6`.

---

## 1. Índice priorizado

Ordem = prioridade sugerida. `I` = impacto (1 baixo … 3 alto), `E` = esforço em tarefas atômicas
estimadas, `I÷E` = a razão que ordena. A única quebra da ordem aritmética é o `C-01`, justificada
na §2.

| # | Candidato | Origem | I | E | I÷E | Recomendação |
|---|---|---|---|---|---|---|
| `C-01` | Checador/gerador executável do kit | D9 + D11 + D14 | 3 | 3 | 1,0 | adotar |
| `C-02` | Allowlist de subcomandos destrutivos por agente | D13 | 3 | 1 | 3,0 | adotar |
| `C-03` | Tabela de precedência e residência da doutrina | D17 | 3 | 1 | 3,0 | adotar |
| `C-04` | Teto de contexto graduado por classe de tarefa | D6 | 3 | 1 | 3,0 | adotar |
| `C-05` | Checkpoint intermediário para perda de contexto não planejada | D19 | 3 | 1 | 3,0 | adotar |
| `C-06` | `file:line` + comando de validação no dossiê da tarefa | D5 | 2 | 1 | 2,0 | adotar |
| `C-07` | Gatilho de revisão e deprecação da própria doutrina | D21 | 2 | 1 | 2,0 | adotar |
| `C-08` | Commits assinados no branch de distribuição + verificação no sync | D22 | 2 | 1 | 2,0 | adaptar |
| `C-09` | Registro de consumidores e versões instaladas | D18 | 2 | 1 | 2,0 | adotar |
| `C-10` | Inbox de memória: separar descobrir de aprovar | D7 | 2 | 1 | 2,0 | adaptar |
| `C-11` | Piso de regressão como comando (ratchet) na doutrina | D8 | 3 | 2 | 1,5 | adotar |
| `C-12` | Repatriar ao repo a doutrina Pantonic que vive no CLAUDE.md global | D15 | 3 | 2 | 1,5 | adotar |
| `C-13` | Telemetria de consumo em linha append-only estruturada | D12 | 2 | 2 | 1,0 | adotar |
| `C-14` | Compatibilidade por major entre kit e consumidor | D10 (delta) | 1 | 1 | 1,0 | adiar |
| `C-15` | Reversibilidade do trabalho do agente (snapshot paralelo) | D20 | 2 | 4 | 0,5 | adiar |

**Cobertura:** os 5 vereditos `ADOTAR` viram 3 candidatos (`C-01` consolida D9+D11+D14, conforme
`RELATORIO_CONSOLIDADO.md:518-521`; `C-02` = D13; `C-11` = D8); os 5 `ADAPTAR` viram 1 candidato cada
(`C-06` D5, `C-04` D6, `C-10` D7, `C-13` D12, `C-12` D15); as 6 dimensões novas viram 1 cada (`C-03`
D17, `C-09` D18, `C-05` D19, `C-15` D20, `C-07` D21, `C-08` D22); dos 5 `MANTER` sai apenas o delta
de D10 (`C-14`); o `REJEITAR` de D2 não gera candidato. Total: 15.

## 2. A ordenação, explicitada

O critério é impacto ÷ esforço, com três desempates aplicados nesta ordem: (1) ataca defeito **já
manifesto** vence prevenir defeito possível; (2) destrava outros candidatos vence isolado; (3) menor
risco vence.

Foi o desempate (2) que colocou `C-03` (tabela de precedência) à frente de `C-04`, `C-10` e `C-12`:
os três decidem **onde** uma regra passa a morar, e sem a régua de residência podem nascer no lugar
errado — trabalho a refazer.

**A única quebra da ordem aritmética é o `C-01`** (I÷E = 1,0, o que o colocaria em 13º). Ele vai
para 1º porque o consolidado não o classifica como o melhor candidato, e sim como uma **precondição**:
"A única coisa que o PantonicApp deveria mudar primeiro" (§1, linhas 81-99) e, no descarte 8
(linhas 738-744), a ordem é enunciada como regra — "primeiro o enforcement vira código, só então
discutir automação sem supervisão". A razão I÷E mede benefício por tarefa e não sabe medir
habilitação: enquanto o enforcement do hub for 0% executável, todo candidato textual desta lista é
adicionado à mesma superfície que ninguém verifica. Registrar a quebra em vez de inflar o `I` do
`C-01` é deliberado — o número continua honesto e a decisão fica visível para o dono derrubar.

**Onde o esforço foi estimado para cima:** `C-01` (3 tarefas) porque a regra de decomposição do
`V2C-T6` divide doutrina e mecânica em passes diferentes; `C-15` (4+) é a única estimativa importada
de fora — `BM-10` estima ~40h para o desenho de referência (`RELATORIO_CONSOLIDADO.md:611-614`).

**Blocos para a ratificação (`V2C-T5`), para 1 round-trip por bloco em vez de 15:**
enforcement executável (`C-01`, `C-02`, `C-11`) · topologia da doutrina (`C-03`, `C-12`, `C-07`) ·
custo e continuidade (`C-04`, `C-05`, `C-13`) · rastro e memória (`C-06`, `C-10`) · cadeia de
distribuição (`C-08`, `C-09`, `C-14`) · reversibilidade (`C-15`).

---

## 3. Candidatos

### `C-01` — Checador/gerador executável do kit

- **Origem:** D9 + D11 + D14 — `RELATORIO_CONSOLIDADO.md` §1 (81-99), §2 D9 (318-324), §2 D11
  (367-372), §2 D14 (449-454), resumo (518-521).
- **Mudança:** um script do hub que valida a estrutura dos 17 artefatos de extensão e **gera** o
  `.claude/README.md` a partir do disco, falhando quando o versionado divergir do regenerado.
- **Artefato-alvo:** script novo em `.claude/` (dois modos: validar / gerar);
  `.claude/README.md` passa a ser derivado; ponteiro em `GOVERNANCA.md` §9; chamada na skill
  `.claude/skills/guardrails-check/SKILL.md`.
- **Impacto (3):** converte a **forma** do enforcement de texto para código na dimensão em que o
  corpus está mais adiante (D9 é `+` em 13 de 21) e cobre 3 dimensões com uma peça. Ataca um defeito
  **já existente**: `.claude/README.md:8-19` lista 8 agentes contra 9 em disco (anti-prática 1 do
  `BM-00`). Padrão copiado de `BM-15§D9` (regenera e falha se diferir) e `BM-07§D8`
  (`skill:validate`), explicitamente **não** de `BM-14§D9` (bloqueio por casamento de string, frágil
  por admissão do próprio relatório).
- **Esforço (3 tarefas atômicas):** (a) modo validador de frontmatter/estrutura; (b) modo gerador do
  README + comparação de deriva; (c) doutrina e integração (`GOVERNANCA.md` §9 + `guardrails-check`).
- **Risco:** baixo — o hub não tem código de produção a quebrar. Risco real é de escopo: o script
  crescer para validar semântica de doutrina, que é o que `BM-14` mostra dar errado.
- **Dependências:** nenhuma. É pré-requisito **conceitual** (não técnico) de todo candidato textual
  desta lista, e do próprio Estágio 3A.
- **Sobreposição com o `P-0722`:** reforça as 5 sem duplicar nenhuma — as 5 são conteúdo textual,
  este é a forma. Compartilha o padrão com `V2M-T5` (check executável de código morto): mesmo tipo
  de artefato, alvo diferente (kit do hub × código do consumidor); se ambos forem adiante, o `V2C-T6`
  deve decidir se são um script com dois checks ou dois scripts. Não contradiz nada.
- **Recomendação do planejador:** adotar.
- **Decisão do dono (`V2C-T5`):** **adotar** — 2026-07-29, conforme a recomendação do planejador.

### `C-02` — Allowlist de subcomandos destrutivos por agente

- **Origem:** D13 — `RELATORIO_CONSOLIDADO.md` §1 (74-79), §2 D13 (403-430).
- **Mudança:** restringir, para os agentes que têm `Bash`, os subcomandos de `git`/`gh` a uma lista
  segura — sem `push --force`, `reset --hard`, `branch -D`.
- **Artefato-alvo:** frontmatter/permissões dos agentes com `Bash` em `.claude/agents/*.md` e
  `.claude/settings*.json`; regra correspondente em `GOVERNANCA.md` §7.
- **Impacto (3):** hoje a allowlist de comandos destrutivos é literalmente `NÃO ENCONTRADO`
  (`BM-00§D13`); o único sandbox existente é o `tools:` dos auditores. Adota `BM-15§D13`, o padrão
  mais barato e menos frágil do corpus (declarativo, sem parsing), evitando o defeito que
  `BM-14` (anti-prática 1) documenta. O corpus traz o único incidente real (`BM-16§D13`) para
  dimensionar a consequência.
- **Esforço (1 tarefa atômica):** configuração, não código (`RELATORIO_CONSOLIDADO.md:430`).
- **Risco:** baixo-médio — allowlist apertada demais trava execução legítima; o modo de falha é
  ruidoso (comando negado), não silencioso, o que é o lado bom da troca.
- **Dependências:** nenhuma.
- **Sobreposição com o `P-0722`:** nenhuma das 5 guardrails toca permissão de ferramenta — é
  ortogonal. Não reforça, não duplica, não contradiz.
- **Recomendação do planejador:** adotar.
- **Decisão do dono (`V2C-T5`):** **adotar** — 2026-07-29, conforme a recomendação do planejador.

### `C-03` — Tabela de precedência e residência da doutrina

- **Origem:** D17 (dimensão nova) — `RELATORIO_CONSOLIDADO.md` §3 (531-552).
- **Mudança:** declarar, em uma tabela, qual das quatro superfícies de doutrina vence quando duas
  colidem e que tipo de conteúdo mora em cada uma (CLAUDE.md global · `GOVERNANCA.md` · skill ·
  agente).
- **Artefato-alvo:** seção nova em `GOVERNANCA.md` (§3 ou §7); nenhum código.
- **Impacto (3):** hoje a fronteira entre as superfícies é ela própria uma regra que vive na
  superfície mais volátil, fora de todo repositório (`BM-00§D15`). `BM-10` (fora da grade) enuncia
  o problema em framework real ("nenhum guia de escopo dizendo use regra para X, hook para Y") e
  `BM-02§D15` mostra a forma resolvida (hierarquia declarada). Destrava `C-04`, `C-10` e `C-12`, que
  todos precisam saber onde a regra passa a morar.
- **Esforço (1 tarefa atômica):** uma tabela + a decisão de residência por tipo de conteúdo.
- **Risco:** baixo em execução; o risco é de conteúdo — uma tabela que descreva a topologia atual em
  vez de decidi-la não resolve nada.
- **Dependências:** nenhuma. É dependência de `C-04`, `C-10` e `C-12`.
- **Sobreposição com o `P-0722`:** reforça `G-PLANREADY` e `G-EXECREADY` indiretamente (um gate só é
  verificável se o agente sabe onde a regra do gate mora) e **é a régua que decide** onde a `V2M-T3`
  promove `G-PLANFIDELITY`/`G-EXECREADY` ao CLAUDE.md global. Não duplica nem contradiz; se ambos
  forem adiante, `C-03` deveria vir antes de `V2M-T3`.
- **Recomendação do planejador:** adotar.
- **Decisão do dono (`V2C-T5`):** **adotar** — 2026-07-29, conforme a recomendação do planejador.

### `C-04` — Teto de contexto graduado por classe de tarefa

- **Origem:** D6 — `RELATORIO_CONSOLIDADO.md` §2 D6 (220-237).
- **Mudança:** substituir o teto único de ~40 tool uses por classes de tarefa com teto próprio.
- **Artefato-alvo:** tabela em `GOVERNANCA.md` §3 (hoje `GOVERNANCA.md:67-69`) — a residência final
  depende do `C-03`; nenhum código.
- **Impacto (3):** o teto único vale igual para uma correção de uma linha e para um relatório de
  confronto, e a série histórica registra 5 estouros (`BM-00§D12`) — sinal de que o número único ora
  sobra ora falta. `BM-04§D6` gradua por complexidade (200/1.000/2.500 tokens) e é uma das duas
  únicas ocorrências de orçamento explícito em 21 frameworks: mexe na dimensão em que o Pantonic
  lidera.
- **Esforço (1 tarefa atômica):** uma tabela na doutrina, zero código.
- **Risco:** baixo, com um efeito colateral a evitar na redação: classe com teto generoso vira
  desculpa para estourar em vez de replanejar, invertendo o propósito do teto.
- **Dependências:** `C-03` (parte da doutrina de orçamento vive hoje no CLAUDE.md global do usuário,
  `BM-00§D6`); `C-13` opcionalmente antes, para calibrar os tetos por série medida em vez de por
  estimativa — juízo do planejador, não recomendação escrita no consolidado.
- **Sobreposição com o `P-0722`:** nenhuma das 5 trata de orçamento. Toca a mesma seção que a
  `V2M-T1` edita (`GOVERNANCA.md` §3/§7), então o `V2C-T6` deve sequenciar as duas para não gerar
  conflito de edição.
- **Recomendação do planejador:** adotar.
- **Decisão do dono (`V2C-T5`):** **adotar** — 2026-07-29, conforme a recomendação do planejador.

### `C-05` — Checkpoint intermediário para perda de contexto não planejada

- **Origem:** D19 (dimensão nova) — `RELATORIO_CONSOLIDADO.md` §3 (582-602).
- **Mudança:** procedimento de checkpoint no diário quando o consumo cruza uma fração do teto, para
  que a descoberta já paga não seja refeita no contexto seguinte.
- **Artefato-alvo:** `.claude/skills/handover/SKILL.md` (ou skill própria) + regra em
  `GOVERNANCA.md` §4.3; nenhuma infraestrutura nova.
- **Impacto (3):** a doutrina cobre bem a troca **planejada** de contexto (uma tarefa por contexto,
  `handover`, diário como estado) e não cobre a não planejada — que acontece de fato, com 5 casos
  medidos (`BM-00§D12`). O custo hoje é reexecutar a descoberta inteira, o oposto exato do que D6
  protege. `BM-19` (fora da grade) trata reconexão como orquestração própria (`apm-9-recover`,
  `summarize-session`); `BM-20§D7` preserva estado ao atingir o máximo de iterações.
- **Esforço (1 tarefa atômica)** na versão mínima (procedimento); o consolidado estima o custo da
  dimensão como "baixo a médio", e a faixa média corresponde a versões com infraestrutura, fora do
  escopo deste candidato.
- **Risco:** baixo. Atenção a não transformar checkpoint em relatório intermediário caro — o
  checkpoint tem de custar menos que a descoberta que ele preserva.
- **Dependências:** nenhuma; combina com `C-13` (o gatilho é a própria medida de consumo).
- **Sobreposição com o `P-0722`:** nenhuma das 5. Complementa `G-EXECREADY` pelo outro extremo — o
  gate cuida da entrada da tarefa, este cuida da interrupção no meio.
- **Recomendação do planejador:** adotar.
- **Decisão do dono (`V2C-T5`):** **adotar** — 2026-07-29, conforme a recomendação do planejador.

### `C-06` — `file:line` + comando de validação no dossiê da tarefa

- **Origem:** D5 — `RELATORIO_CONSOLIDADO.md` §2 D5 (198-216).
- **Mudança:** o dossiê da tarefa atômica passa a exigir, nos campos que hoje são prosa
  ("arquivos-alvo", "testes"), ponteiro `file:line` e o **comando** de validação.
- **Artefato-alvo:** template de tarefa em `.claude/skills/diario-de-obras/SKILL.md`; campo
  correspondente em `.claude/skills/handover/SKILL.md`; `GOVERNANCA.md` §4.2.
- **Impacto (2):** o Pantonic tem os dois extremos do rastro (requisito no dossiê, comportamento
  trancado por TF+TR) e nada no meio — nenhum ponteiro verificável liga um ao outro. `BM-20§D5` é o
  padrão operacional (cada passo carrega `file:line`, comando de validação e artefato esperado) e é
  o **único** pedaço de D5 que se adota: a matriz formal de rastreabilidade fica descartada (§4,
  descarte 1).
- **Esforço (1 tarefa atômica):** alteração de template, sem código.
- **Risco:** baixo. `file:line` envelhece; o campo tem de ser tratado como ponteiro de leitura, não
  como contrato — se virar dado a manter, custa mais do que entrega.
- **Dependências:** nenhuma.
- **Sobreposição com o `P-0722`:** **reforça `G-EXECREADY` diretamente** — é o gate de prontidão
  ganhando campos verificáveis em vez de julgamento. Não duplica (o gate diz *quando* barrar; este
  diz *o que* o dossiê contém) e não contradiz. Sequenciar depois da `V2M-T1`, que escreve o gate.
- **Recomendação do planejador:** adotar.
- **Decisão do dono (`V2C-T5`):** **adotar** — 2026-07-29, conforme a recomendação do planejador.

### `C-07` — Gatilho de revisão e deprecação da própria doutrina

- **Origem:** D21 (dimensão nova) — `RELATORIO_CONSOLIDADO.md` §3 (630-649).
- **Mudança:** instituir o caminho de **saída** de uma regra: revisão periódica com pergunta única
  ("esta regra mudou algum comportamento nos últimos N meses?"), marcação de obsolescência e período
  de transição antes da remoção.
- **Artefato-alvo:** `GOVERNANCA.md` §7 (política) + gatilho na skill `checar-versao-kit` ou
  `guardrails-check`.
- **Impacto (2):** nenhuma regra jamais saiu do framework: 8 guardrails escritas + 5 decididas e
  ~600 linhas lidas por todo agente em toda sessão (`BM-00§D9`, `BM-00§D14`). Como cada linha é
  reenviada em cada turno, doutrina que só cresce é imposto crescente sobre exatamente a dimensão em
  que o framework lidera (D6). `BM-12` (fora da grade) propõe a política de N versões menores;
  `BM-07§D3` dá o gatilho barato (re-review a cada 6 meses); `BM-17` (fora da grade) mostra duas
  versões coexistindo sem breaking change.
- **Esforço (1 tarefa atômica):** política + gatilho, sem código.
- **Risco:** baixo. Risco de virar cerimônia periódica que ninguém executa — o gatilho precisa
  pendurar-se em algo que já roda (fechamento de versão do kit), não em calendário.
- **Dependências:** nenhuma. Ganha valor **depois** do Estágio 3A, que é justamente uma rodada de
  crescimento da doutrina (5 guardrails novas).
- **Sobreposição com o `P-0722`:** nenhuma das 5 prevê saída de regra — este candidato é o
  contrapeso das 5, e a rodada que as adiciona é o melhor momento para instituí-lo. Não duplica nem
  contradiz.
- **Recomendação do planejador:** adotar.
- **Decisão do dono (`V2C-T5`):** **adotar** — 2026-07-29, conforme a recomendação do planejador.

### `C-08` — Commits assinados no branch de distribuição + verificação no sync

- **Origem:** D22 (dimensão nova) — `RELATORIO_CONSOLIDADO.md` §3 (653-676).
- **Mudança:** na versão mínima, exigir commits assinados no branch `kit` e verificar a assinatura no
  passo de sync do consumidor.
- **Artefato-alvo:** `.claude/sync-kit.ps1`; `GOVERNANCA.md` §10.
- **Impacto (2):** o que se propaga por `git subtree` são agentes e skills — instruções que rodam com
  as ferramentas que o frontmatter concede (`BM-00§D13`); um artefato adulterado no hub vira execução
  em todos os consumidores sem verificação intermediária. `BM-16§D13` mostra que o comprometimento
  real do corpus veio de **credencial**, não de repositório público, o que é exatamente o vetor de um
  hub local. `BM-19§D13` descreve o risco estrutural (templates injetando instruções) e admite não
  ter assinatura nem varredura.
- **Esforço (1 tarefa atômica)** na versão mínima. A versão completa (assinatura e varredura de
  conteúdo por artefato) é de custo alto e o corpus inteiro a deixa em aberto — fora deste candidato.
- **Risco:** médio operacional — verificação de assinatura mal configurada bloqueia o sync, e o sync
  é o único caminho de distribuição.
- **Dependências:** nenhuma; toca o mesmo arquivo que `C-09`.
- **Sobreposição com o `P-0722`:** nenhuma. Ortogonal às 5.
- **Recomendação do planejador:** adaptar — só a versão mínima, com o escopo completo registrado
  como não adotado.
- **Decisão do dono (`V2C-T5`):** **adaptar** — 2026-07-29, conforme a recomendação do planejador. Motivo: só a versão mínima (commits assinados no branch `kit` + verificação da assinatura no sync); a varredura de conteúdo por artefato fica registrada como **não adotada**.

### `C-09` — Registro de consumidores e versões instaladas

- **Origem:** D18 (dimensão nova) — `RELATORIO_CONSOLIDADO.md` §3 (556-578).
- **Mudança:** um arquivo no hub listando consumidor, versão instalada e data do último sync,
  atualizado pelo mesmo passo que aplica a versão.
- **Artefato-alvo:** arquivo novo no hub (ex. `docs/CONSUMIDORES.md`); escrita automática em
  `.claude/sync-kit.ps1`; `GOVERNANCA.md` §10.
- **Impacto (2):** hoje é impossível responder "quais consumidores ainda não receberam a guardrail
  X" sem abrir cada repositório. `BM-12` (anti-prática 3) enuncia a falta pelo lado do produtor e
  propõe exatamente este artefato; `BM-19§D10` resolve pelo lado do consumidor
  (`.apm/metadata.json`); `BM-15` (fora da grade) admite a lacuna correlata (quebra de
  compatibilidade cruzada não detectada).
- **Esforço (1 tarefa atômica):** arquivo + escrita no passo de sync que já existe.
- **Risco:** baixo. Registro escrito à mão vira o mesmo defeito do `.claude/README.md` (mente em
  silêncio) — só vale se o `sync-kit.ps1` escrever.
- **Dependências:** nenhuma; mesmo arquivo-alvo de `C-08` e `C-14`, que o `V2C-T6` pode agrupar.
- **Sobreposição com o `P-0722`:** nenhuma diretamente. Habilita a `P-0729-v2-documentacao` `T4`
  (distribuição das 5 guardrails), que hoje não tem como conferir a quem chegou.
- **Recomendação do planejador:** adotar.
- **Decisão do dono (`V2C-T5`):** **adotar** — 2026-07-29, conforme a recomendação do planejador.

### `C-10` — Inbox de memória: separar descobrir de aprovar

- **Origem:** D7 — `RELATORIO_CONSOLIDADO.md` §2 D7 (241-258).
- **Mudança:** candidato a memória entra numa fila e só é promovido a memória por ato do dono, em vez
  de o agente gravar no momento em que descobre.
- **Artefato-alvo:** doutrina de memória (residência a definir pelo `C-03` — hoje a governança de
  memória vive fora do repo) + a skill de memória correspondente.
- **Impacto (2):** o Pantonic já tem governança de memória escrita (lar canônico único, 1 fato por
  arquivo, índice obrigatório), mas a decisão de gravar é do próprio agente que está gravando — não
  há separação entre descobrir e aprovar. `BM-08§D7`/`§D16` é a única prática do corpus que ataca
  isso (inbox + revisão explícita antes de aplicar).
- **Esforço (1 tarefa atômica):** procedimento + campo de fila.
- **Risco:** baixo. Fila sem hábito de drenagem acumula e o agente volta a gravar direto.
- **Dependências:** `C-03` (a doutrina de memória mora fora do repo hoje; o candidato precisa saber
  onde a regra nova mora antes de ser escrita).
- **Sobreposição com o `P-0722`:** nenhuma. Reforça o padrão de `G-PLANREADY`/`G-EXECREADY` na
  forma (nada entra sem gate), em superfície diferente.
- **Recomendação do planejador:** adaptar — só a fila e a promoção pelo dono; a análise automática de
  transcrições de `BM-08§D7` exigiria infraestrutura fora do escopo do hub e fica de fora.
- **Decisão do dono (`V2C-T5`):** **adaptar** — 2026-07-29, conforme a recomendação do planejador. Motivo: só a fila e a promoção pelo dono; a análise automática de transcrições (`BM-08§D7`) exigiria infraestrutura fora do escopo do hub e fica **de fora**.

### `C-11` — Piso de regressão como comando (ratchet) na doutrina

- **Origem:** D8 — `RELATORIO_CONSOLIDADO.md` §1 (66-72), §2 D8 (262-285).
- **Mudança:** o "piso de regressão nunca desce" deixa de ser verificado por leitura e disciplina e
  passa a ser um comando que falha o build no consumidor.
- **Artefato-alvo:** `GOVERNANCA.md` §4.4 (doutrina do TDD/piso) + receita de ratchet referenciável
  pelos consumidores; a adoção acontece **nos consumidores** — o hub não tem código a testar
  (`BM-00§D1`).
- **Impacto (3):** é a anti-prática 2 que o próprio auto-retrato registra — o hub prescreve TDD com
  TF+TR e tem `tests/**` vazio. `BM-18§D8` mostra a mesma ideia como gate de CI que não deixa a
  métrica cair (`test:coverage:ratchet`, ~2 dias de custo declarado); `BM-04§D8` é o retrato do risco
  de não fazer (framework de qualidade com 0% de cobertura própria).
- **Esforço (2 tarefas atômicas):** (a) redação da doutrina; (b) a receita/comando de ratchet.
- **Risco:** médio — muda o gate de CI dos consumidores, e o consumidor de prova é o `PantonicVideo`.
- **Dependências:** a distribuição ao consumidor é a `P-0729-v2-documentacao` `T4`.
- **Sobreposição com o `P-0722`:** **tensão real com `G-DEADCODE`** (proibição de código morto
  testado): um piso baseado em contagem cria incentivo a manter o teste de código morto para não
  derrubar a métrica. A redação tem de fixar o piso como **comportamental**, não percentual — que é
  também o motivo do descarte 5 (`RELATORIO_CONSOLIDADO.md:716-720`). Reforça `G-DEADCODE` se
  redigido assim; contradiz se redigido como percentual.
- **Recomendação do planejador:** adotar, com a tensão acima resolvida no texto.
- **Decisão do dono (`V2C-T5`):** **adotar** — 2026-07-29, conforme a recomendação do planejador. A tensão com `G-DEADCODE` é resolvida no texto: o piso é **comportamental** (comportamentos trancados por TF+TR), **nunca percentual de cobertura** — vínculo bloqueante para a tarefa de redação.

### `C-12` — Repatriar ao repo a doutrina Pantonic que vive no CLAUDE.md global

- **Origem:** D15 — `RELATORIO_CONSOLIDADO.md` §2 D15 (458-480).
- **Mudança:** separar o que é regra de **todos** os projetos do dono (fica global) do que é doutrina
  **Pantonic** (desce para o repo versionado e viaja no kit), movendo o texto e ajustando ponteiros.
- **Artefato-alvo:** `~/.claude/CLAUDE.md` (fora do repo) → `GOVERNANCA.md`; ponteiros nas skills e
  agentes que citam as regras movidas.
- **Impacto (3):** achado concreto do consolidado — o orçamento de contexto (`BM-00§D6`) e a
  telemetria de consumo (`BM-00§D12`) citam `C:\Users\panta\.claude\CLAUDE.md:30,107`, isto é, um
  consumidor que receba o kit por `git subtree` **não recebe** dois dos diferenciais que o `BM-00`
  apresenta como do framework. `BM-02§D15` dá a divisão (overrides de time versionados × pessoais
  gitignored); `BM-01§D15` mostra o custo de não fazer ("duplicação = divergência").
- **Esforço (2 tarefas atômicas):** (a) decisão de residência item a item; (b) mover texto e corrigir
  ponteiros.
- **Risco:** médio-alto — mexe em arquivo fora do repo, que vale para projetos não-Pantonic do dono;
  erro aqui altera o comportamento de todas as sessões, inclusive fora desta família.
- **Dependências:** `C-03` decide a régua; este executa a mudança sob ela. O consolidado registra
  explicitamente que **exige decisão do dono** (linha 480).
- **Sobreposição com o `P-0722`:** conflito de sentido a resolver com a `V2M-T3`, que **promove**
  `G-PLANFIDELITY`/`G-EXECREADY` ao CLAUDE.md global (subida) enquanto este candidato desce doutrina
  Pantonic para o repo. Não são contraditórias — a `V2M-T3` sobe regra de escopo global e este desce
  regra de escopo Pantonic —, mas as duas precisam da mesma régua (`C-03`) para não se cruzarem.
- **Recomendação do planejador:** adotar.
- **Decisão do dono (`V2C-T5`):** **adotar** — 2026-07-29, conforme a recomendação do planejador.

### `C-13` — Telemetria de consumo em linha append-only estruturada

- **Origem:** D12 — `RELATORIO_CONSOLIDADO.md` §1 (32-38), §2 D12 (376-399).
- **Mudança:** manter a fonte (medida no bloco `<usage>`, nunca autorrelato) e mudar o suporte: de
  prosa no diário para linha estruturada append-only, agregável sem leitura humana.
- **Artefato-alvo:** arquivo de série novo (ex. `docs/telemetria.tsv`); escrita pela skill
  `.claude/skills/handover/SKILL.md` e pelo passo de fechamento da `proximo-passo`.
- **Impacto (2):** a fonte do Pantonic é melhor que a de qualquer externo (D12 é `+` em apenas 3 de
  21, e nenhum distingue medição de autorrelato); o formato é pior — detectar tendência exige reler o
  diário, e os 5 estouros viraram prosa repetida em vez de sinal (anti-prática 3 do `BM-00`).
  `BM-04§D12` dá a forma barata (JSONL append-only, rotação, análise periódica).
- **Esforço (2 tarefas atômicas):** (a) formato e arquivo; (b) escrita nos dois pontos de fechamento
  que hoje redigem a linha `Consumo:`.
- **Risco:** baixo, com um cuidado: duplicar a série (prosa + arquivo) recria o problema de duas
  fontes. A linha do diário deve passar a ser ponteiro, não cópia.
- **Dependências:** nenhuma. Se `C-04` for adotado, esta série é o que permite calibrar os tetos por
  dado medido.
- **Sobreposição com o `P-0722`:** nenhuma das 5. A regra que produz o dado é do CLAUDE.md global
  (`BM-00§D12`), então o `V2C-T6` deve sequenciar este candidato depois de `C-03`/`C-12` se ambos
  forem adotados.
- **Recomendação do planejador:** adotar.
- **Decisão do dono (`V2C-T5`):** **adotar** — 2026-07-29, conforme a recomendação do planejador.

### `C-14` — Compatibilidade por major entre kit e consumidor

- **Origem:** D10 (único delta com valor dentro de um veredito `MANTER`) —
  `RELATORIO_CONSOLIDADO.md` §2 D10 (328-348), especialmente 345-347.
- **Mudança:** casar compatibilidade por versão major entre kit e consumidor, no padrão de
  `BM-19§D10` (CLI v1.x só consome templates v1.x.x).
- **Artefato-alvo:** `.claude/skills/checar-versao-kit/SKILL.md`; `GOVERNANCA.md` §10.
- **Impacto (1):** o consolidado classifica o mecanismo atual como comparável aos melhores do corpus
  e superior em um ponto que nenhum externo tem (update como decisão humana obrigatória). Este delta
  é descrito como "barato mas não urgente enquanto o kit não tiver quebrado compatibilidade".
- **Esforço (1 tarefa atômica).**
- **Risco:** baixo.
- **Dependências:** nenhuma; mesmo arquivo-alvo de `C-08`/`C-09`.
- **Sobreposição com o `P-0722`:** nenhuma.
- **Recomendação do planejador:** adiar — reavaliar na primeira quebra de compatibilidade do kit. A
  linha existe para que o adiamento seja uma decisão registrada e não um esquecimento.
- **Decisão do dono (`V2C-T5`):** **adotar** — 2026-07-29, **divergindo da recomendação** (`adiar`): o delta é barato e toca os mesmos arquivos-alvo de `C-08`/`C-09`, então o custo marginal de fazê-lo nesta rodada é menor que o de uma rodada futura.

### `C-15` — Reversibilidade do trabalho do agente (snapshot paralelo)

- **Origem:** D20 (dimensão nova) — `RELATORIO_CONSOLIDADO.md` §3 (606-626).
- **Mudança:** desfazer o que o agente escreveu sem contaminar o histórico de trabalho — snapshot de
  segurança separado do commit com significado.
- **Artefato-alvo:** indefinido por desenho — o consolidado recomenda "considerar", não "adotar".
- **Impacto (2):** as aplicações da família escrevem no disco do usuário e a doutrina de execução é
  editar direto na árvore, com o git do próprio trabalho como única rede — o que empurra o executor a
  commitar cedo (poluindo o histórico) ou a não se proteger. `BM-10§D7` é o desenho de referência
  (repositório *shadow*, snapshot por ação de ferramenta, restauração seletiva).
- **Esforço (4+ tarefas atômicas):** a única estimativa importada do corpus — `BM-10` declara ~40h
  para o desenho de referência. É a dimensão mais cara da lista.
- **Risco:** alto — infraestrutura nova, snapshot por ação de ferramenta encarece cada turno, o que
  colide com a premissa de custo (D6).
- **Dependências:** nenhuma.
- **Sobreposição com o `P-0722`:** nenhuma.
- **Recomendação do planejador:** adiar. Se o dono quiser tratar, o caminho fechado é uma **tarefa de
  investigação** com teto de sondagem (o `V2C-T6` não conseguiria fechá-lo em tarefa de
  implementação sem informação que só a execução revelaria).
- **Decisão do dono (`V2C-T5`):** **adiar** — 2026-07-29, conforme a recomendação do planejador. Motivo: maior custo da lista (4+ tarefas; ~40h no desenho de referência do `BM-10`), risco alto e colisão com a própria premissa de custo por turno (D6). Permanece na lista para reavaliação futura.

---

## 4. Não convertido em candidato, com motivo

Registrado para que a ausência seja legível como decisão, e não como esquecimento.

1. **Licença e declaração de propriedade na raiz** — o consolidado a chama de "resíduo barato,
   **deliberadamente não promovido** a item de backlog": é higiene de repositório, não adoção da
   dimensão (`RELATORIO_CONSOLIDADO.md:149-151`). Dar-lhe um `C-NN` contrariaria a fonte. Se o dono
   quiser fazer, é um arquivo e não precisa desta lista.
2. **Os 5 vereditos `MANTER`** (D1, D3, D4, D10, D16) — nada a mudar por definição. O único delta com
   valor apontado em D10 virou `C-14`; o delta de D3 (gate de prontidão) **já está decidido** e
   pertence ao Estágio 3A (`G-PLANREADY`/`G-EXECREADY`), e recomendá-lo de novo aqui inflaria o
   backlog com trabalho que já tem dono (`RELATORIO_CONSOLIDADO.md:169-172`).
3. **O `REJEITAR` de D2** (publicação pública do hub) — motivo escrito no consolidado: importaria o
   bus factor 1 medido em `BM-09` (anti-prática 2) e a fila sem SLA de `BM-13` (anti-prática 1), sem
   nenhum benefício de doutrina (linhas 140-147).
4. **Os 8 descartes justificados** (`RELATORIO_CONSOLIDADO.md:680-744`) — matriz formal de
   rastreabilidade, adapter multi-harness, marketplace público, avaliação estatística por commit,
   meta de percentual de cobertura, multi-agente com message bus, auto-update no consumidor e modo
   sem aprovação. Cada um tem motivo de conflito com uma premissa Pantonic escrito na fonte. **Dois
   deles são o limite de candidatos desta lista:** o descarte 5 restringe a forma do `C-11` (piso
   comportamental, nunca percentual) e o descarte 8 fixa a precedência do `C-01` (enforcement vira
   código antes de qualquer conversa sobre automação sem supervisão).
5. **As 5 guardrails do `P-0722`** (G-DEADCODE, G-PLANFIDELITY, G-PREMISE, G-PLANREADY, G-EXECREADY)
   — decididas em 2026-07-22 e já mapeadas tarefa a tarefa no Estágio 3A
   (`docs/plans/P-0729-v2-melhoria.md` §1). O Estágio 2 pode **acrescentar**, nunca revogar: nenhum
   candidato desta lista as contradiz, e a única tensão encontrada (`C-11` × `G-DEADCODE`) está
   registrada na ficha, com a resolução proposta.

## 5. Duas ressalvas do corpus que valem para esta lista

Não invalidam nenhum candidato; mudam a força com que devem ser lidos
(`RELATORIO_CONSOLIDADO.md` §5).

- **Documentação não é prática** (viés 2, linhas 756-760): a matriz mede a **forma** do enforcement,
  não a conformidade obtida. Um framework com D9 "100% executável" pode estar validando trivialidades.
  Consequência direta: o `C-01` é recomendado porque converte a forma **e** conserta um defeito já
  manifesto — não porque a forma executável seja boa por si.
- **Parte dos `—` é orçamento de coleta** (viés 7, linhas 788-794): onde uma conclusão dependeu de
  uma célula `—` isolada, ela foi formulada como "o corpus não registra", não "o framework não tem".
  Nenhum candidato desta lista tem uma célula `—` isolada como única fundamentação.

---

**`V2C-T4` — Estágio 2 de `PANTONIC-V2`. 15 candidatos, 100% rastreáveis ao
`RELATORIO_CONSOLIDADO.md`, todos com esforço estimado e coluna de sobreposição com o `P-0722`
preenchida. Nenhuma decisão tomada: `V2C-T5` preenche a linha `Decisão do dono` de cada ficha, e só
então o `V2C-T6` autora o plano do Estágio 3B.**
