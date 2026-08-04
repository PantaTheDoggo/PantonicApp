# Changelog

Todas as mudanças notáveis do framework Pantonic* (doutrina em `GOVERNANCA.md`/`ARQUITETURA_*` +
kit agêntico em `.claude/`) são registradas aqui. `VERSION` (raiz) e `.claude/KIT_VERSION` carregam
sempre o mesmo valor — ver `GOVERNANCA.md` §10.

Versionamento: [Semantic Versioning](https://semver.org/lang/pt-BR/), com significado declarado em
`GOVERNANCA.md` §10 — MAJOR exige ação do consumidor, MINOR adiciona artefato/guardrail
compatível, PATCH corrige redação.

## [Não lançado]

- `V2K-T17`: residência da doutrina do `~/.claude/CLAUDE.md` global corrigida — a disciplina de
  coleta condensada (git, listagens, arquivos grandes, comandos verbosos), o batching de chamadas
  independentes e a cadência de testes passam a viajar em `GOVERNANCA.md` §3/§4.4 (kit); a
  telemetria medida pela notificação (nunca auto-relato) passa a residir em `GOVERNANCA.md` §4.2.
  O que era só duplicata (onboarding ATIVO/HISTÓRICO, DOC_MAP, fatos estáveis de agente, modelo
  por fase, orçamento de turnos) saiu do global, que mantém apenas o princípio condensado
  apontando para o kit.

## 1.4.0 — 2026-07-30

- `GOVERNANCA.md` §7 passa de **8 para 13 guardrails**: **G-DEADCODE** (proibição de código morto
  testado — cobertura por teste não confere "vivo"; rota abandonada morre no mesmo commit),
  **G-PLANFIDELITY** (executor não troca a rota arquitetural aprovada; para e escala),
  **G-PREMISE** (premissa que embasa abandono de rota exige spike, não asserção),
  **G-PLANREADY** (dever do planejador — 5 condições de fechamento de plano) e **G-EXECREADY**
  (dever do executor — não decide, não pergunta, recusa plano não-pronto). Cada uma nasce com
  enforcement declarado (`V2M-T1`, `docs/plans/P-0729-v2-melhoria.md` §3; doutrina herdada do
  `P-0722`, ratificada em 2026-07-22).
- **G-PLANREADY item 5 — gate de publicação** (decisão do dono 2026-07-29, doutrina nova): plano
  não se publica em aberto; trabalho que depende de insumo futuro divide-se em dois planos, e o
  dependente é autorado já fechado como a última tarefa do plano que produz o insumo.
- **Contador sequencial de planos materializado** (`V2M-T4`): a regra já normativa no
  `GOVERNANCA.md` §7 (`G-PLANREADY` item 1, `P-NNNN-<slug>.md` com `NNNN` monotônico global,
  nunca reutilizado) ganha registro executável — `docs/plans/_INBOX.md` passa a ser o registro do
  contador, com o próximo id declarado no cabeçalho (`P-0730`); elimina a colisão de nomenclatura
  por data que gerou dois `P-0722` e quatro `P-0729`. Superfícies do kit alinhadas
  (`.claude/skills/diario-de-obras/SKILL.md`, `.claude/skills/bootstrap-pantonic/SKILL.md`); os
  planos existentes `P-0721`..`P-0729` são grandfathered — mantêm o nome atual, não renomeados.
- Materializado o enforcement nos três artefatos do kit que executam essas regras: `G-EXECREADY`
  virou o **passo 1** do protocolo do agente `pantonic-executor` (recusa plano não-pronto antes de
  qualquer edição), `G-PLANREADY` virou gate explícito da skill `proximo-passo` (não delega tarefa
  de plano aberto) e da skill `diario-de-obras` (operação "Registrar plano" verifica o gate antes
  de apensar) (`V2M-T1`).
- `GOVERNANCA.md` §3 ganhou o **gatilho operacional do modelo por fase**: ponteiro para a skill
  `modelo-por-fase` do kit versionado, com a residência declarada sob a régua de §3.1 — a regra
  mora na doutrina versionada, a skill é gatilho e o hook (global) é enforcement (`V2M-T1`; a
  skill em si é a `V2M-T2`).
- Criada a skill `.claude/skills/modelo-por-fase/SKILL.md` — gatilho operacional da regra de
  modelo por fase: três gatilhos (início de tarefa/subagente, troca de fase na mesma sessão,
  nudge do hook global), gate de parada (pedir `/model` explícito ao dono, nunca decidir/trocar
  sozinho) e a convenção de anúncio da Regra 5. Reside **no kit versionado**, não em
  `~/.claude/skills/` — `DM-7` (2026-07-30) rebaseia a `DP-G3` de 2026-07-22 pela régua de
  residência de `GOVERNANCA.md` §3.1 (skill que só existe fora do repo não viaja no subtree).
  Revisado também `~/.claude/hooks/modelo_por_fase_userpromptsubmit.py` (global, fora do kit):
  falso positivo medido (prompt de retomada de backlog classificado como "execução mecânica"
  quando o trabalho real era orquestração/delegação) corrigido com uma lista de exclusão
  checada antes da classificação (`V2M-T2`).
- **G-PLANFIDELITY e G-EXECREADY promovidas ao `~/.claude/CLAUDE.md` global** como Regra 8
  (conduta universal de executor, não doutrina específica de Pantonic): `GOVERNANCA.md` itens 10
  e 13 passam a apontar para o texto normativo global em vez de duplicá-lo (nome do item e
  *Enforcement* preservados). Absorvido no mesmo ato o `TK-01` (achado fora de escopo da
  `V2M-T2`): `GOVERNANCA.md` §3 e o bullet acima corrigidos para descrever a skill
  `modelo-por-fase` como residente no kit versionado, não `~/.claude/skills/` (`V2M-T3`).
- **`V2M-T5` fechada — check executável de código morto testado (G-DEADCODE), Estágio 3A
  encerrado 5/5.** `.claude/checks/dead_code.py` (alcançabilidade por AST a partir de entry
  points, três rodadas de ajuste estrutural — auto-vivo para POC/seed de diretório, import
  relativo em `_resolve_import_targets`, override de virtual Qt) wireado como item **6**,
  bloqueante, do "Checklist executável" de `.claude/skills/guardrails-check/SKILL.md`. Baseline do
  `PantonicVideo` confirmado em `exit 0` pela campanha `SPRINT-DEADCODE` daquele repositório (92
  símbolos removidos, `docs/plans/P-0730-limpeza-codigo-morto.md`), destravando o gate que estava
  bloqueado desde 2026-07-30. Confirmado nesta sessão: `python .claude/checks/dead_code.py`
  (root = PantonicApp) e `--root D:\workspaces\PantonicVideo` → `OK - 0 achado(s)` nos dois; fixture
  sintética (`orphan_helper` referenciado só por teste) → exit 1, 1 achado exato.

## 1.3.0 — 2026-07-30

- Criado o validador estrutural do kit `.claude/checks/kit_check.ps1 -Mode validate`: confere a
  estrutura de `.claude/` (agentes, skills, checks) e a paridade `VERSION` == `.claude/KIT_VERSION`
  exigida por `GOVERNANCA.md` §10 (`V2K-T1`, `docs/plans/P-0729-v2-melhoria-candidatos.md` §3).
- Adicionados os modos `-Mode generate` e `-Mode check-drift` ao mesmo script: o índice
  `.claude/README.md` passa a ser **gerado** a partir do disco e a deriva entre índice e conteúdo
  real vira falha detectável (defeito medido na adoção: 8/9 agentes e 6/8 skills listados)
  (`V2K-T2`, mesmo plano).
- Declarado em `GOVERNANCA.md` §9 que o enforcement do kit é **código**: `.claude/README.md` é
  artefato derivado que não se edita à mão, `kit_check.ps1` é o comando canônico, e regra do kit
  não verificável pelo script nasce com o motivo escrito. Os dois modos foram pendurados no gate
  `guardrails-check` (item 5 do checklist executável + linha `Kit:` no veredito) (`V2K-T3`, mesmo
  plano; fecha o Bloco A de enforcement executável).
- Declarada a topologia da própria doutrina em `GOVERNANCA.md` §3.1: tabela das quatro superfícies
  (CLAUDE.md global · doutrina versionada · skill · agente) com o que mora e o que não mora em cada
  uma, duas regras de precedência (específico vence geral; empate → versionado vence
  não-versionado) e o teste de residência em quatro perguntas. Hook é declarado mecanismo de
  enforcement, não quinta superfície (`V2K-T4`, mesmo plano; fecha o Bloco A).
- Regra nova no passo de handover da skill `proximo-passo`: quando a tarefa executada deixa um
  ponto para o dono decidir, o próximo passo sugerido é **a decisão**, com fato medido, implicação
  de cada opção, o que trava sem resposta e recomendação — não a próxima tarefa do backlog.

## 1.2.0 — 2026-07-29

- Criado o agente coletor `pantonic-benchmarker` (Haiku, somente `Read/Write/Glob/Grep/WebFetch`)
  e materializado o esquema fixo de 16 dimensões em `docs/benchmark/_ESQUEMA.md`; agente listado
  em `.claude/README.md` (`V2B-T2`, `docs/plans/P-0729-v2-benchmarking.md` §5).

## 1.1.0 — 2026-07-29

- Instituído o controle de versão do framework: `VERSION` (raiz) e `.claude/KIT_VERSION` passam a
  carregar sempre o mesmo valor, com a regra de paridade e o significado de MAJOR/MINOR/PATCH
  documentados em `GOVERNANCA.md` §10 (`V2B-T1`, `docs/plans/P-0729-v2-benchmarking.md` §5).

## 1.0.1 — versão anterior publicada por tag (`kit-v1.0.1`)

## 1.0.0 — versão anterior publicada por tag (`kit-v1.0.0`)
