# RDO — P-0748 · TLG-T3h

**Plano:** `docs/plans/P-0748-tela-do-gerente.md`
**Tarefa:** `TLG-T3h` — O painel dá uma linha a cada `status` do mesmo comando, e a skill cita o evento da volta em hand-back
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório com os campos do evento e a grava no arquivo de progresso, trocando o identificador da tarefa pelo título dela e o do plano pelo título do plano; a frase da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit. O gancho deixa de copiar texto marcado pelo condutor, e toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — segue fora do arquivo.

**Arquivos-alvo:** - `.claude/tools/progresso_hook.py:259` — o `re.search` de `backlog\.py status` na regra 2 e o `if m:` da linha seguinte (únicos no arquivo) - `tests/test_progresso_hook.py:1215` — fim do arquivo; a função nova entra depois da última - `.claude/skills/scrum-master/SKILL.md:332` — a linha da tabela que começa por | `M-4` | (única; localizar pelo texto) - `.claude/skills/scrum-master/SKILL.md:336` — a linha da tabela que começa por | `M-7` | (única; localizar pelo texto) - `.claude/skills/scrum-master/SKILL.md:338` — a linha da tabela que começa por | `M-9` | (única; localizar pelo texto) - `.claude/skills/scrum-master/SKILL.md:349` — a linha da tabela que começa por | `M-16` | (única; localizar pelo texto) - `.claude/skills/scrum-master/SKILL.md:369` — o bullet de `## Guardrails` que começa por `- O gerente acompanha a execução num painel` (único)

**Verificação:** 1. `python -m pytest tests/test_progresso_hook.py -q` → antes `32 passed` (medido 2026-09-24 pelo consultor), depois `33 passed`. 2. `python -m pytest tests/ -q` → `<N> passed`, com `<N>` = total re-medido no despacho (medido 2026-09-24, acionamento 16: `312 passed`); depois `<N>+1`. 3. Contagens (linhas) de `re.finditer(r"backlog` e de `re.search(r"backlog\.py status` no gancho e de `UserPromptSubmit` na skill, bloco cercado (colar numa sessão PowerShell na raiz): ``` "conta " + ((@(@('.claude/tools/progresso_hook.py','re.finditer(r"backlog'),@('.claude/tools/progresso_hook.py','re.search(r"backlog\.py status'),@('.claude/skills/scrum-master/SKILL.md','UserPromptSubmit')) | ForEach-Object { (Select-String -SimpleMatch -Path $_[0] -Pattern $_[1] | Measure-Object).Count }) -join ' ') ``` → antes `conta 0 1 0`, depois `conta 1 0 5` (medido 2026-09-24 em `powershell` 5.1 e `pwsh`, na árvore e numa cópia com a mudança). 4. Igualdade da tabela da skill com a `### 4.1`, bloco cercado por conter barra invertida: ``` python -c "import re;f=lambda p:[l.rstrip() for l in open(p,encoding='utf-8') if re.match(r'^\| .M-\d+b?. \|',l)];a=f('.claude/skills/scrum-master/SKILL.md');b=f('docs/plans/P-0748-tela-do-gerente.md');print('iguais',sum(x==y for x,y in zip(a,b)),'de',len(a),len(b))" ``` → antes `iguais 20 de 24 24` (medido 2026-09-24, depois de `DTG-52` mudar a `M-4`, a `M-7`, a `M-9` e a `M-16` da `### 4.1`), depois `iguais 24 de 24 24`. 5. `(Select-String -Path .claude/tools/progresso_hook.py -Pattern "^(from|import) (rdo|backlog|telemetria|modelo|ocupacao|materializar|subprocess)\b" | Measure-Object).Count` e `(Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern "print(" | Measure-Object).Count` → antes `0` e `0`, depois `0` e `0`.

**Pronto quando:** - `stream de dados.arquivo de progresso` — *existe e é alimentado pela função do kit a cada transição do loop: guarda uma linha do repertório por transição, na ordem em que o loop as atravessa, gerada a partir do evento e não da memória do agente — nenhuma linha se perde por o condutor ter esquecido a forma —, e nada mais: nenhuma busca, leitura ou saída de comando, e nenhuma chamada feita dentro dos agentes despachados* — Verificação 1 (`TF-GER-30`), 3 e 4.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-24
- **Fundamento:** `DTG-52` (consultor, acionamento 16), `AE-25`, `AE-26`, `AE-16`, `DTG-39`, `DTG-47`.
- **Depende de:** `TLG-T3g`
- **Operação do modelo:** `OP-3` - OP-3: O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório com os campos do evento e a grava no arquivo de progresso, trocando o identificador da tarefa pelo título dela e o do plano pelo título do plano; a frase da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit. O gancho deixa de copiar texto marcado pelo condutor, e toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — segue fora do arquivo. - precisa de: stream de dados — Quem implementa recebe o loop do condutor — as transições que ele atravessa a cada tarefa e o que ele tem em mãos em cada uma —, a função do kit que gera a linha a partir do evento de cada transição, e o arquivo de progresso onde essa função grava. A ferramenta que roda os agentes e o painel que mostra o arquivo ficam como estão.; tarefa — Quem implementa lê dela o que preenche as mensagens: qual tarefa, o título dela, qual passo e o que o passo pede. Nada nela muda.; mente do agente — Quem implementa usa a intenção que o condutor já tem em mãos — o que ele pediu ao agente e o que o agente devolveu — como campo do evento que a função recebe. O raciocínio interno fica fora da tela, e nenhum agente é reescrito para mudar a forma como entende o passo.
- **Camada e fronteira:** kit — `.claude/tools/progresso_hook.py` (a regra 2, `backlog.py status`), `tests/test_progresso_hook.py` (uma função nova, `TF-GER-30`) e **cinco** linhas da `scrum-master`: `M-4`, `M-7`, `M-9` e `M-16` da seção *Repertório de mensagens ao gerente* (cópia legível da `### 4.1`, que o consultor já mudou em `DTG-52`) e o bullet do painel em `## Guardrails`. Todo o resto fica como está.
- **Domínio:** (a) *status encadeado* = dois ou mais `backlog.py status <ID> <estado>` no mesmo comando `Bash` (`AE-25`). Hoje a regra 2 casa só o primeiro (`re.search`) e a linha do segundo se perde; depois, cada `status` do comando gera a linha dele, na ordem do comando. (b) *volta em hand-back* = o agente entrega com `handback` = `send`: o `PostToolUse` do `Agent` só grava `pendentes[agentId]`, e a linha de volta sai no `UserPromptSubmit` cujo `prompt` começa por `<agent-message from="<agentId>">` (`DTG-39`, regra 5b do gancho). O código já faz isso; a skill não o diz (`AE-26`).
- **Contratos/classes:** assinaturas, `FRASES` e o corpo da regra 2 inalterados. Só a abertura da regra 2 muda — duas linhas viram uma, e o corpo, que já está no recuo do `for`, fica como está: ``` m = re.search(r"backlog\.py status (\S+) ([a-z-]+)", cmd) if m: ``` → ``` for m in re.finditer(r"backlog\.py status (\S+) ([a-z-]+)", cmd): ``` Medido pelo consultor em 2026-09-24 numa cópia temporária: o `diff` com a árvore dá só `259,260c259`.
- **Texto novo, literal:** na `scrum-master`, (1) as linhas que começam por `` | `M-4` | ``, `` | `M-7` | ``, `` | `M-9` | `` e `` | `M-16` | `` passam a ser, inteiras, as linhas de mesmo início da `### 4.1` do plano (copiar do plano, não redigitar); (2) no bullet de `## Guardrails` que começa por `- O gerente acompanha a execução num painel`, o trecho `` (eventos `PreToolUse`, `PostToolUse` e `Stop`) `` passa a ser `` (eventos `PreToolUse`, `PostToolUse`, `UserPromptSubmit` — a volta do agente que entrega em hand-back, `DTG-39` — e `Stop`) ``. Editar com `Edit`, preservando o fim de linha `CRLF` da cópia de trabalho.
- **Passos:** 1. Rodar a Verificação 1, 3 e 4 e anotar (contingências 1 e 2). 2. Trocar a abertura da regra 2 do gancho (`Contratos/classes`). 3. Inserir o `TF-GER-30` de `Testes`. 4. Trocar as cinco linhas da skill (`Texto novo, literal`). 5. Rodar a Verificação 1 a 5.
- **Restrições desta tarefa:** `I-3` — nenhum comando, marcador ou flag novo do condutor; `I-11` — o gancho segue sem imprimir e saindo sempre `0`; `DTG-36` — `FRASES` não muda; `AE-10` — nenhum passo nem verificação roda `progresso_hook.py` contra o `.claude/estado/` real; `I-7` — o total de `pytest tests/` não cai.
- **Não fazer:** não editar outra instrução do gancho (a regra 3, `review_evidence.py`, segue com `re.search`: um só `--tarefa` por comando); não editar outra linha da skill, a `### 4.1` do plano nem o `README.md`; não apagar nem reescrever `.claude/estado/progresso.txt` ou `progresso-estado.json`; não alterar asserção de outro `TF`.
- **Contingências:** 1. se `python -m pytest tests/test_progresso_hook.py -q` antes da edição não sai `32 passed` → parar e sinalizar `blocked` razão `dependencia`, devolvendo a linha impressa; 2. se a Verificação 3 antes da edição não imprime `conta 0 1 0`, ou a 4 `iguais 20 de 24 24` → parar e sinalizar `blocked` razão `premissa`, devolvendo a linha impressa; 3. se `python -m pytest tests/ -q` reduz o total por teste **fora** de `tests/test_progresso_hook.py` → parar e sinalizar `blocked` razão `dependencia` com o nome do teste.
- **Testes:** `tests/test_progresso_hook.py`. Uma função nova, no fim do arquivo, com o separador de comentário dos outros `TF`: ``` # --- TF-GER-30 ---------------------------------------------------------------------- def test_tf_ger_30_dois_status_no_mesmo_comando(estado, raiz): rodar(payload_next( "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n" "- **Objetivo:** Fazer x.\n" ), estado, raiz) antes = len(progresso(estado)) p1 = P(hook_event_name="PreToolUse", tool_name="Bash", tool_input={"command": ( "python .claude/tools/backlog.py status TLG-T9 done && " "python .claude/tools/backlog.py status TLG-T10 in-progress" )}) rodar(p1, estado, raiz) assert progresso(estado)[antes:] == [ 'Scrum master vai fechar a tarefa "Um título de teste" como done: registrar estado, RDO e telemetria.', 'Tarefa "Outro título": gates aprovados; vou materializar in-progress e gravar o ponto de partida.', ] ``` Medido pelo consultor em 2026-09-24 numa cópia temporária: com o `TF-GER-30` e o gancho da árvore, `1 failed, 32 passed` (a lista sai só com a linha do primeiro `status`); com a abertura nova e a skill trocada, `33 passed`. Suítes: `python -m pytest tests/test_progresso_hook.py -q`; `python -m pytest tests/ -q`.
- **Fora do escopo desta tarefa:** `review_evidence.py` repetido no mesmo comando (nenhum caso medido); prosa depois da linha de retorno (`AE-23`); a docstring de `tests/test_progresso_hook.py`, que já cita os quatro eventos; propagação aos kits derivados (`DTG-8`).

## Execução

**Consumo:** 28 tool uses, 72.6 k tokens, 185.7 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: nenhuma; ressalva de rota: TF-GER-30 inserido entre TF-CAP-2 e TF-CAP-3 (AE-28); evidencia de nao rastreados (TK-55)

## Laudo

**Veredito:** ressalva

**Percentual:** 94%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
