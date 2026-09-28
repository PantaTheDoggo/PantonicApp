# RDO — P-0748 · TLG-T3g

**Plano:** `docs/plans/P-0748-tela-do-gerente.md`
**Tarefa:** `TLG-T3g` — O painel reconhece o retorno do agente com o `%` ou o colchete a mais
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório com os campos do evento e a grava no arquivo de progresso, trocando o identificador da tarefa pelo título dela e o do plano pelo título do plano; a frase da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit. O gancho deixa de copiar texto marcado pelo condutor, e toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — segue fora do arquivo.

**Arquivos-alvo:** - `.claude/tools/progresso_hook.py:187` — o padrão de `re.match` da `M-4` em `de_volta` (único no arquivo) - `.claude/tools/progresso_hook.py:195` — o padrão de `re.match` da `M-7` em `de_volta` (único no arquivo) - `tests/test_progresso_hook.py:269` — test_tf_ger_6_agente_de_volta_executor; a asserção nova entra depois da última - `tests/test_progresso_hook.py:286` — test_tf_ger_7_agente_de_volta_revisor; a asserção nova entra depois da única - `.claude/skills/scrum-master/SKILL.md:332` — a linha da tabela que começa por | `M-4` | (única; localizar pelo texto) - `.claude/skills/scrum-master/SKILL.md:336` — a linha da tabela que começa por | `M-7` | (única; localizar pelo texto)

**Verificação:** 1. `python -m pytest tests/test_progresso_hook.py -q` → antes `32 passed` (medido 2026-09-24 pelo consultor), depois `32 passed`. 2. `python -m pytest tests/ -q` → `<N> passed`, com `<N>` = total re-medido no despacho (medido 2026-09-24, acionamento 15: `312 passed`); o total não muda. 3. Contagens dos dois padrões tolerantes no gancho e na skill, bloco cercado (colar numa sessão PowerShell na raiz): ``` "tolera " + ((@('.claude/tools/progresso_hook.py','.claude/skills/scrum-master/SKILL.md') | ForEach-Object { $f = $_; @('[?pendencia=', '(\d+)%? bloqueante') | ForEach-Object { (Select-String -SimpleMatch -Path $f -Pattern $_ | Measure-Object).Count } }) -join ' ') ``` → antes `tolera 0 0 0 0`, depois `tolera 1 1 1 1` (medido 2026-09-24 em `powershell` 5.1 e `pwsh`, na árvore e numa cópia com a mudança). 4. Igualdade da tabela da skill com a `### 4.1`, bloco cercado por conter barra invertida: ``` python -c "import re;f=lambda p:[l.rstrip() for l in open(p,encoding='utf-8') if re.match(r'^\| .M-\d+b?. \|',l)];a=f('.claude/skills/scrum-master/SKILL.md');b=f('docs/plans/P-0748-tela-do-gerente.md');print('iguais',sum(x==y for x,y in zip(a,b)),'de',len(a),len(b))" ``` → antes `iguais 22 de 24 24` (medido 2026-09-24, depois de `DTG-51` mudar a `M-4` e a `M-7` da `### 4.1`), depois `iguais 24 de 24 24`. 5. `(Select-String -Path .claude/tools/progresso_hook.py -Pattern "^(from|import) (rdo|backlog|telemetria|modelo|ocupacao|materializar|subprocess)\b" | Measure-Object).Count` e `(Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern "print(" | Measure-Object).Count` → antes `0` e `0`, depois `0` e `0`.

**Pronto quando:** - `stream de dados.arquivo de progresso` — *existe e é alimentado pela função do kit a cada transição do loop: guarda uma linha do repertório por transição, na ordem em que o loop as atravessa, gerada a partir do evento e não da memória do agente — nenhuma linha se perde por o condutor ter esquecido a forma —, e nada mais: nenhuma busca, leitura ou saída de comando, e nenhuma chamada feita dentro dos agentes despachados* — Verificação 1 (`TF-GER-6`, `TF-GER-7`), 3 e 4.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-24
- **Fundamento:** `DTG-51` (consultor, acionamento 15), `AE-24`, `AE-14`, `DTG-40`, `DTG-47`.
- **Depende de:** `TLG-T5a`
- **Operação do modelo:** `OP-3` - OP-3: O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório com os campos do evento e a grava no arquivo de progresso, trocando o identificador da tarefa pelo título dela e o do plano pelo título do plano; a frase da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit. O gancho deixa de copiar texto marcado pelo condutor, e toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — segue fora do arquivo. - precisa de: stream de dados — Quem implementa recebe o loop do condutor — as transições que ele atravessa a cada tarefa e o que ele tem em mãos em cada uma —, a função do kit que gera a linha a partir do evento de cada transição, e o arquivo de progresso onde essa função grava. A ferramenta que roda os agentes e o painel que mostra o arquivo ficam como estão.; tarefa — Quem implementa lê dela o que preenche as mensagens: qual tarefa, o título dela, qual passo e o que o passo pede. Nada nela muda.; mente do agente — Quem implementa usa a intenção que o condutor já tem em mãos — o que ele pediu ao agente e o que o agente devolveu — como campo do evento que a função recebe. O raciocínio interno fica fora da tela, e nenhum agente é reescrito para mudar a forma como entende o passo.
- **Camada e fronteira:** kit — `.claude/tools/progresso_hook.py` (dois padrões de `de_volta`), `tests/test_progresso_hook.py` (duas asserções novas, em `TF-GER-6` e `TF-GER-7`) e **duas** linhas da seção *Repertório de mensagens ao gerente* da `scrum-master` (`M-4` e `M-7`, cópia legível da `### 4.1`, que o consultor já mudou em `DTG-51`). Todo o resto fica como está.
- **Domínio:** *variação inócua* = caractere a mais na primeira linha do retorno de agente que não muda o que ela diz: o `%` depois do percentual do revisor (`AE-24`: `TLG-T5a aprovado 100% bloqueante=nenhuma`, medido no painel) e o colchete de opcional em volta de `pendencia=` do executor (`AE-14`: `TLG-T4a review [pendencia=...]`, medido no painel). Hoje as duas formas caem na `M-16` genérica, com a linha crua e a sigla; depois, dão a `M-7` e a `M-4`. A gramática dos agentes (`pantonic-reviewer.md:131`, passo 4 da `scrum-master`) fica como está: quem lê tolera, quem escreve segue a forma exata. Prosa **depois** da primeira linha (`AE-23`) já não afeta o painel, porque `de_volta` lê só a primeira linha não vazia.
- **Contratos/classes:** assinaturas e `FRASES` inalteradas. Em `de_volta`, dois padrões mudam, e só eles: - `M-4`: `r"^(\S+) review(?:\s+pendencia=(.*))?$"` → `r"^(\S+) review(?:\s+\[?pendencia=(.*?)\]?)?$"` - `M-7`: `r"^(\S+) (\S+) (\d+) bloqueante=(.*)$"` → `r"^(\S+) (\S+) (\d+)%? bloqueante=(.*)$"` Medido pelo consultor em 2026-09-24 com `de_volta` do gancho novo: `X review pendencia=a]b` → `review — a]b.`; `X review [pendencia=a b]` → `review — a b.`; `X review` → `review — sem pendência.`; `X aprovado 100% bloqueante=nenhuma` → `aprovado 100%, bloqueante nenhuma.`; `X aprovado 100%% bloqueante=nenhuma` → `M-16`.
- **Texto novo, literal:** na `scrum-master`, as linhas que começam por `` | `M-4` | `` e por `` | `M-7` | `` passam a ser, inteiras, as linhas de mesmo início da `### 4.1` do plano (copiar do plano, não redigitar).
- **Passos:** 1. Rodar a Verificação 1, 3 e 4 e anotar (contingências 1 e 2). 2. Trocar os dois padrões do gancho (`Contratos/classes`). 3. Inserir as duas asserções de `Testes`. 4. Trocar as linhas `M-4` e `M-7` da skill (`Texto novo, literal`). 5. Rodar a Verificação 1 a 5.
- **Restrições desta tarefa:** `I-3` — nenhum comando, marcador ou flag novo do condutor; `I-11` — o gancho segue sem imprimir e saindo sempre `0`; `DTG-36` — `FRASES` não muda; `AE-10` — nenhum passo nem verificação roda `progresso_hook.py` contra o `.claude/estado/` real; `I-7` — o total de `pytest tests/` não cai.
- **Não fazer:** não editar outra instrução do gancho; não editar `.claude/agents/pantonic-reviewer.md`, `.claude/agents/pantonic-executor.md` nem o passo 4 da `scrum-master` (a gramática dos agentes não muda); não editar outra linha da skill, a `### 4.1` do plano nem o `README.md`; não apagar nem reescrever `.claude/estado/progresso.txt` ou `progresso-estado.json`; não alterar outra asserção dos `TF`.
- **Contingências:** 1. se `python -m pytest tests/test_progresso_hook.py -q` antes da edição não sai `32 passed` → parar e sinalizar `blocked` razão `dependencia`, devolvendo a linha impressa; 2. se a Verificação 3 antes da edição não imprime `tolera 0 0 0 0`, ou a 4 `iguais 22 de 24 24` → parar e sinalizar `blocked` razão `premissa`, devolvendo a linha impressa; 3. se `python -m pytest tests/ -q` reduz o total por teste **fora** de `tests/test_progresso_hook.py` → parar e sinalizar `blocked` razão `dependencia` com o nome do teste.
- **Testes:** `tests/test_progresso_hook.py`. Asserções novas, e só elas; nenhuma função nova. - `TF-GER-6` — depois da asserção de `e3`: ``` assert _volta_executor(tmp_path / "estado4", raiz, "TLG-T9 review [pendencia=uma coisa]") == ( 'Agente executor devolveu a tarefa "Um título de teste": review — uma coisa.' ) ``` - `TF-GER-7` — depois da asserção existente (a lista de duas linhas prova que o segundo retorno gerou linha própria): ``` rodar(P(hook_event_name="PostToolUse", tool_name="Agent", tool_input={"subagent_type": "pantonic-reviewer"}, tool_response={"content": [{"type": "text", "text": "TLG-T9 aprovado 100% bloqueante=nenhuma"}]}), estado, raiz) assert progresso(estado)[-2:] == [ 'Agente revisor devolveu a tarefa "Um título de teste": aprovado 100%, bloqueante nenhuma.' ] * 2 ``` Medido pelo consultor em 2026-09-24 numa cópia temporária: com as asserções e o gancho da árvore, `2 failed, 30 passed` (`TF-GER-6`, `TF-GER-7`); com as asserções, os dois padrões novos e a skill trocada, `32 passed`. Suítes: `python -m pytest tests/test_progresso_hook.py -q`; `python -m pytest tests/ -q`.
- **Fora do escopo desta tarefa:** prosa depois da linha de retorno (`AE-23`, tíquete de disciplina do `pantonic-executor`); outras variações que nenhum painel mostrou; a gramática escrita dos agentes; propagação aos kits derivados (`DTG-8`).

## Execução

**Consumo:** 23 tool uses, 57.9 k tokens, 93.3 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: nenhuma; dois achados de evidencia com rota TK-55 (AE-11)

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
