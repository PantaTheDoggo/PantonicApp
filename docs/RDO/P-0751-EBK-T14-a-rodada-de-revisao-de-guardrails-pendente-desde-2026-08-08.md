# RDO — P-0751 · EBK-T14

**Plano:** `docs/plans/P-0751-esgotar-backlog.md`
**Tarefa:** `EBK-T14` — A rodada de revisão de guardrails pendente desde 2026-08-08
**Modelo:** Opus · **Classe:** investigacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** registrar em `GOVERNANCA.md` §7.1, *Registro das rodadas*, a rodada disparada pelos planos fechados depois da rodada `P-0731`, aplicando o procedimento de §7.1 às guardrails em escopo, e marcar `OBSOLETA desde <rodada>` a que ficar sem caso citável.

**Arquivos-alvo:** - `GOVERNANCA.md`

**Verificação:** 1. Contagem da entrada nova: ``` (Select-String -Path GOVERNANCA.md -Pattern '^- \*\*.P-0750. — 2026-').Count ``` antes `0` (medido em 2026-09-25), depois `1`. 2. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho.

**Pronto quando:** a entrada `P-0750 — <data>` no *Registro das rodadas* de §7.1, com os planos que a dispararam, as treze em escopo, as sete fora por idade, cada isenta com o check e a linha de sumário de hoje, e cada uma das demais com o caso citável (arquivo e identificador) ou com a marca aplicada no item de §7.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Origem:** card `TK-67a` do diário de obras, seção `## TK-67`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-14` - OP-14: O card da rodada de revisão das regras de guarda sai de pronto para concluído, sobre o backlog que a operação anterior deixou. - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Método de sondagem:** 1. **Rótulo e gatilho.** A rodada se rotula pelo plano fechado mais recente, `P-0750`, e pela data da execução: `P-0750 — <AAAA-MM-DD>`. Os planos que a disparam são os `done` do índice de `docs/DIARIO_DE_OBRAS.md` fechados depois de 2026-08-08: `P-0732`, `P-0735`, `P-0736`, `P-0738`, `P-0739`, `P-0740`, `P-0741`, `P-0743`, `P-0745`, `P-0746`, `P-0747`, `P-0748`, `P-0749` e `P-0750` (medido em 2026-09-25). 2. **Escopo.** O registro ainda não tem duas rodadas do regime por plano, então a `1.4.0` segue como penúltima e o escopo é o mesmo da rodada `P-0731`: treze guardrails, por nome — regra de dependência, ACL, egress G6, namespace de estado, gate de conformance, allowlist de subcomandos destrutivos, piso de regressão, disciplina de contexto, `G-DEADCODE`, `G-PLANFIDELITY`, `G-PREMISE`, `G-PLANREADY` e `G-EXECREADY`. Fora por idade: `G-README`, `G-SCOPE`, `G-SURFACE`, `G-REPLAN`, `G-NOASK`, `G-MODULO` e `G-TOOLDENY`. 3. **Isenção, re-confirmada e não herdada.** Para cada uma das seis isentas na rodada `P-0731`, rodar hoje o check que a isentou e registrar a linha de sumário: em `D:\workspaces\PantonicVideo`, `python -m pytest tests/conformance/test_layer_imports.py tests/conformance/test_acl_no_external_in_plugins.py tests/conformance/test_filesystem_egress.py tests/boundary/test_state_writer_namespacing.py -q -rs`; no hub, `python -m pytest -q`; e a contagem de `permissions.deny` em `.claude/settings.json`. Check que não roda, que sai com `skip`/`xfail` no alvo ou cuja lista cobre tudo **não isenta**: a guardrail vai para o passo 4 e o check morto entra na entrada como achado. 4. **Pergunta única**, para cada guardrail em escopo e não isenta: *"Esta regra mudou algum comportamento desde a penúltima rodada registrada? Cite o caso."* Caso citável é ocorrência **registrada** entre 2026-08-08 e a data da execução — em `docs/DIARIO_DE_OBRAS.md`, `docs/DIARIO_HISTORICO.md`, `docs/plans/`, `docs/RDO/`, `docs/Entregas Aceitas/` ou no diário de `D:\workspaces\PantonicVideo` — em que a regra bloqueou algo, forçou correção ou embasou decisão. Suíte verde não é caso; lembrança sem registro não é caso. O caso se cita por arquivo e identificador (`AE-`, `DB-`, id de tarefa). 5. **Resultado.** Guardrail sem caso citável recebe, no próprio item de §7, a marca `OBSOLETA desde P-0750` — permanece em vigor por uma rodada, e a remoção é tarefa da rodada seguinte. Zero marcações é resultado legítimo.
- **Não fazer:** não criar guardrail; não remover guardrail (remoção é da rodada seguinte); não editar plano fechado; não tocar as matérias do `EBK-T12`.
- **Contingências:** - se `D:\workspaces\PantonicVideo` ou um dos quatro arquivos de teste não existir → a guardrail daquele check vai para o passo 4, e a entrada registra `check ausente: <caminho>`.

## Execução

**Consumo:** 27 tool uses, 104.3 k tokens, 276.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
