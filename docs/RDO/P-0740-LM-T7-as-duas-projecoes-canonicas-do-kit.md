# RDO — P-0740 · LM-T7

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T7` — As duas projeções canônicas do kit
**Modelo:** Sonnet · **Classe:** mecanica
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** pôr as duas projeções versionadas do kit em dia com as definições de agente que já estão em disco. Um tema só, mecânico: **a projeção**, nunca a definição. As duas estão vermelhas hoje por atos do dono fora de ciclo de tarefa — `DM-8` reescreveu as descrições de executor e reviewer, e o `pantonic-consultant` foi criado em 2026-09-18.

**Arquivos-alvo:** - `.claude/README.md` - `README.md` - `CHANGELOG.md`

**Verificação:** (toda linha foi **rodada** na `RP-5` e na `ESC-1`, com a saída de antes **e** a de depois medidas; nenhuma é deduzida — `DM-12`) 1. `pwsh -NoProfile -Command ".claude/checks/kit_check.ps1 -Mode check-drift | Out-Null; exit $LASTEXITCODE"` → **exit 0**. **Antes (medido):** exit **1**, `kit_check: check-drift FALHOU (6 problema(s))`, com `README.md diverge do regenerado (5 linha(s) diferente(s))`. Medido também que o passo 2 sozinho leva este comando a exit 0, com a saída `kit_check: check-drift OK - .claude/README.md == regenerado (9 agente(s), 11 skill(s)); materializacao do alvo 'projeto' == canonico.` 2. `pwsh -NoProfile -Command "& .claude/checks/check-readme.ps1 | Out-Null; exit $LASTEXITCODE"` → **exit 0**. **Antes (medido):** exit **1**, `check-readme: FALHOU (1 problema(s))` — `Agente 'pantonic-consultant' (.claude/agents/pantonic-consultant.md) não aparece na tabela de Agentes de 'Anatomia do kit'.` **Depois, medido na `ESC-1` com a linha do passo 1 inserida e revertida no mesmo ato:** exit 0, `check-readme: OK - 9 agente(s), 11 skill(s), 18 guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade válida.` 3. `pwsh -NoProfile -Command ".claude/checks/kit_check.ps1 -Mode validate | Out-Null; exit $LASTEXITCODE"` → **exit 0**, inalterado (medido antes: exit 0, `kit_check: OK - 9 agente(s), 11 skill(s) e 21 entrada(s) canonica(s) validados; VERSION == KIT_VERSION ('0.0.0')`). 4. Efeito nos dois arquivos-alvo, com baseline medida na `ESC-1` (**zero** ocorrências de `pantonic-consultant` em cada um deles hoje): `pwsh -NoProfile -Command "(Select-String -Path README.md -Pattern 'pantonic-consultant' -SimpleMatch | Measure-Object).Count"` → ≥ 1, e o mesmo comando sobre `.claude/README.md` → ≥ 1. 5. `python -m pytest tests/ -q` → verde, piso ≥ **145** (medido: `145 passed`). Esta tarefa não acrescenta teste; o piso tranca a suíte de conformance contra edição de doutrina.

**Pronto quando:** a tabela **Agentes** de `README.md` lista o `pantonic-consultant`; `.claude/README.md` está regenerado pelo instrumento; `CHANGELOG.md` traz a linha sob `## [Não lançado]`; e as cinco linhas de `Verificação` saem como escritas — em especial `check-drift` e `check-readme.ps1` em **exit 0**, que hoje saem 1.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` — despachada em 2026-09-18 pelo `scrum-master`. **Reescrita pelo `ESC-1` (2026-09-18)**: o card cobria também a concessão de `Bash` ao `pantonic-planner`, e esse passo é inexecutável por qualquer agente desta sessão (`AE-11`). A parte de definição de agente saiu para a `LM-T8`, pendente de ato do dono; o que ficou aqui está **despachável agora** e não depende dela (`DM-17` (iii)).
- **Esforço:** low
- **Depende de:** `DM-16` (iv) e `DM-17`. Nenhuma tarefa anterior. **Precede a `LM-T4`:** a `Verificação` 1 da `LM-T4` exige `check-drift` exit 0, que hoje sai **exit 1**; quem o recoloca em 0 é o passo 2 desta tarefa — e só ele, medido na `RP-5`.
- **Produto do módulo:** (a) a linha do `pantonic-consultant` na tabela **Agentes** de `README.md` › *Anatomia do kit*, que é escrita à mão e não é gerada; (b) `.claude/README.md` regenerado **pelo instrumento**, nunca à mão; (c) uma linha em `CHANGELOG.md` sob `## [Não lançado]`. 1. Em `README.md`, na tabela **Agentes** da seção *Anatomia do kit*, inserir **imediatamente antes** da linha que começa com `| ` + crase + `pantonic-scout` (âncora medida na `ESC-1`: uma única ocorrência no arquivo) a linha: ``` | `pantonic-consultant` | Opus | Consultor de **um** plano em execução: instanciado uma vez, mantido de standby com o cenário inteiro e acionado a cada escalonamento para desbloquear impedimento de executor e reparar o modelo funcional do plano. Não implementa entrega, não julga e não commita. | ``` 2. Regenerar a projeção do kit pelo instrumento, sem editar a região marcada à mão: `pwsh -NoProfile -Command ".claude/checks/kit_check.ps1 -Mode generate; exit $LASTEXITCODE"` → exit 0, com a saída medida `kit_check: generate OK - README.md regenerado: 9 agente(s), 11 skill(s).` O efeito medido no arquivo foi de **3 inserções e 2 remoções** em `.claude/README.md`. 3. Em `CHANGELOG.md`, como primeiro item da seção `## [Não lançado]`: ``` - Projeções canônicas do kit em dia com as definições de agente em disco: `.claude/README.md` regenerado por `kit_check -Mode generate` e a tabela de Agentes de `README.md` passa a listar o `pantonic-consultant`. `check-drift` e `check-readme.ps1` voltam a exit 0. ```
- **Restrições desta tarefa:** `.claude/README.md` só muda **pelo passo 2** — editar a região marcada à mão faz o `check-drift` divergir de novo na regeneração seguinte. A tabela de `README.md` é **outra** superfície, não gerada: ali a linha se escreve à mão, com o literal do passo 1. **Nenhum arquivo de `.claude/agents/` é tocado** (`DM-17` (ii)): esta tarefa projeta o que já está lá e não altera definição de agente nenhuma.
- **Não fazer:** não editar `.claude/agents/pantonic-planner.md` nem qualquer outro arquivo de `.claude/agents/` — a edição é negada pela camada de permissão do harness e contorná-la por `Write`/`Bash` é proibido (`AE-11`, `DM-17`); se o passo 2 alterar algo fora das regiões marcadas, parar. Não publicar `DM-2`..`DM-5` em doutrina (é a `LM-T4`); não tocar `GOVERNANCA.md`, skill nenhuma nem instrumento de `.claude/tools/`; não rodar `python .claude/tools/backlog.py check` nem tratá-lo como aceite (`AE-1`); não commitar (commit é ato do loop, no marco de validação).
- **Contingências:** 1. se a tabela **Agentes** de `README.md` já contiver uma linha `pantonic-consultant` → não duplicar: seguir para o passo 2 e devolver `contingência 1 acionada: linha já existia`; 2. se, depois do passo 2, o `check-drift` continuar exit 1 por problema que **não** seja divergência de tabela de agentes/skills (ex.: materialização do alvo `projeto`) → seguir com a entrega e devolver `contingência 2 acionada: <o problema que restou>`; 3. se o `check-readme.ps1` apontar problema **adicional** ao do `pantonic-consultant` → seguir com a entrega, corrigir só o do consultor e devolver `contingência 3 acionada: <problema remanescente>`.

## Execução

**Consumo:** 17 tool uses, 49.8 k tokens, 67 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: README.md:760 anuncia 'oito agentes' e a tabela logo abaixo lista nove desde esta entrega: corrigir a frase e fechar o furo de guarda que a deixou passar verde sao trabalho da proxima rodada, nao desta revisao.

## Laudo

**Veredito:** ressalva

**Percentual:** 90%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
