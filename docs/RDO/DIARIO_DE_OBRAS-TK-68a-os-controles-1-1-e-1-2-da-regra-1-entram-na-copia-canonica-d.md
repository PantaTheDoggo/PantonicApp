# RDO — DIARIO_DE_OBRAS · TK-68a

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-68a` — Os Controles 1.1 e 1.2 da Regra 1 entram na cópia canônica do kit
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `.claude/global/CLAUDE.md` passa a carregar, sob a Regra 1 e antes da Regra 2, os Controles 1.1 e 1.2 com o texto exato do arquivo do dono. É o que torna seguro o `apply` do fechamento do tíquete: sem os controles no kit, o `apply` os apaga de `~/.claude/CLAUDE.md`.

**Arquivos-alvo:** - `.claude/global/CLAUDE.md` - `tests/test_global_claude.py` (novo)

**Verificação:** no PowerShell, na raiz do repositório; **antes** medido em 2026-09-25. 1. `(Select-String -Path .claude/global/CLAUDE.md -Pattern "^### Controle 1\.[12] ").Count` — antes `0`, depois `2` 2. `(Get-Content .claude/global/CLAUDE.md -Encoding utf8).Count` — antes `182`, depois `210` 3. `git diff --no-index --ignore-cr-at-eol --numstat "$env:USERPROFILE/.claude/CLAUDE.md" .claude/global/CLAUDE.md` — antes `17	29`, depois `17	1` (sobra só a Regra 8/9, que é do kit) 4. `python -m pytest tests/test_global_claude.py -q` → verde 5. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho mais o teste novo

**Pronto quando:** o canônico do kit carrega os Controles 1.1 e 1.2 com o literal do arquivo do dono, o diff contra `~/.claude/CLAUDE.md` se reduz às linhas em que o kit é o mais novo, e o TR guarda a presença dos dois controles.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Fundamento:** tabela de reconciliação acima, linha `CLAUDE.md` (a).
- **Passos:** 1. Em `.claude/global/CLAUDE.md`, substitua o **Texto atual 1** pelo **Texto novo 1**. 2. Crie `tests/test_global_claude.py` com o teste descrito em **Testes**. 3. Rode as Verificações.
- **Texto novo 1:** ~~~~ prossiga com a implementação em uma nova mensagem/turno iniciada pelo usuário. ### Controle 1.1 — Persistir o plano **é** encerramento do planejamento, não execução Ao sair do Plan Mode com plano aprovado, **grave o plano no repositório antes de encerrar o turno**: em projeto Pantonic*, `docs/plans/P-<MMDD>-<slug>.md` + uma linha apensada a `docs/plans/_INBOX.md`. Isso **não** é execução e a Regra 1 **não** o proíbe — o que a Regra 1 proíbe é começar a implementar. Só depois de gravado o turno encerra. **Motivo:** em Plan Mode o agente não pode escrever arquivo; depois da aprovação a Regra 1 manda parar. Lido literalmente, o arquivamento não tem onde morar, e o plano só existe no contexto da sessão — que o `/clear` seguinte destrói. Defeito medido em 2026-09-04 (PantonicVideo): dois planos aprovados no mesmo dia, nenhum gravado em `docs/plans/`, nenhum no `_INBOX.md`; a retomada seguinte de backlog encontrou fila vazia e reportou "nada a fazer" com dois planos aprovados pendurados. O harness salva uma cópia em `~/.claude/plans/<slug-aleatório>.md`, mas esse nome não é rastreável a partir do backlog — não substitui o arquivamento canônico. ### Controle 1.2 — Não abrir sessão de planejamento sobre alvo que já tem plano aprovado Antes de entrar em Plan Mode para um tíquete/iniciativa, verifique se ele já tem plano vivo (`docs/plans/`, `_INBOX.md`, índice do diário). Se já tiver, **não replaneje**: ou executa o que está aprovado, ou emenda o plano existente por decisão explícita do dono. Planejar duas vezes o mesmo alvo produz dois planos vivos disputando a mesma rota — que é exatamente o que a regra de convergência de uma iniciativa proíbe (skill `diario-de-obras`, "Planos derivados"). **Motivo:** mesmo incidente de 2026-09-04 — a segunda sessão custou um contexto inteiro de Opus e produziu um artefato descartado pelo dono. A causa dela foi o Controle 1.1: como o primeiro plano não estava gravado em lugar nenhum rastreável, a sessão seguinte não tinha como saber que ele existia. ## Regra 2 — Integridade do contexto ~~~~
- **Restrições desta tarefa:** - A edição é substituição literal; o texto novo entra exatamente como está no bloco, sem reescrita editorial (o arquivo do dono é a fonte do literal, e o `apply` o sobrescreve com esta cópia). O arquivo tem final de linha LF: preserve. - Não commitar. - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui.
- **Não fazer:** não rodar `materializar.py apply` nem escrever em `C:\Users\panta\.claude\` — o `apply` é o último passo do fechamento do tíquete, do condutor, nas condições da autorização acima; não tocar a Regra 8 nem a Regra 9 do kit (são a versão mais nova); não editar `.claude/global/docs/GOVERNANCA_MEMORIAS.md` nem `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` (a versão do kit prevalece, tabela acima); não tocar `.claude/sync-kit.ps1`.
- **Contingências:** - se o **Texto atual 1** não for encontrado **exatamente uma vez** → parar e sinalizar `blocked` razão `premissa`, colando a contagem - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** TR novo em `tests/test_global_claude.py`, lendo `.claude/global/CLAUDE.md` em UTF-8: `### Controle 1.1 —` e `### Controle 1.2 —` aparecem uma vez cada, nessa ordem, depois de `## Regra 1 —` e antes de `## Regra 2 —`. Falha sobre o arquivo anterior, passa sobre o novo — é a guarda de que o canônico não volta a perder os controles, que o `apply` apagaria do dono.

## Execução

**Consumo:** 8 tool uses, 49.4 k tokens, 165.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
