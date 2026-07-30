# Changelog

Todas as mudanças notáveis do framework Pantonic* (doutrina em `GOVERNANCA.md`/`ARQUITETURA_*` +
kit agêntico em `.claude/`) são registradas aqui. `VERSION` (raiz) e `.claude/KIT_VERSION` carregam
sempre o mesmo valor — ver `GOVERNANCA.md` §10.

Versionamento: [Semantic Versioning](https://semver.org/lang/pt-BR/), com significado declarado em
`GOVERNANCA.md` §10 — MAJOR exige ação do consumidor, MINOR adiciona artefato/guardrail
compatível, PATCH corrige redação.

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
