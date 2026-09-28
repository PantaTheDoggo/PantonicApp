# RDO — P-0748 · TLG-T3f

**Plano:** `docs/plans/P-0748-tela-do-gerente.md`
**Tarefa:** `TLG-T3f` — O estado do gancho não guarda chave que ninguém lê
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório com os campos do evento e a grava no arquivo de progresso, trocando o identificador da tarefa pelo título dela e o do plano pelo título do plano; a frase da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit. O gancho deixa de copiar texto marcado pelo condutor, e toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — segue fora do arquivo.

**Arquivos-alvo:** - `.claude/tools/progresso_hook.py:250` — a instrução estado_loop["encerrada"] = False da regra 1 (única no arquivo) - `tests/test_progresso_hook.py:127` — a asserção estado_loop["aberta"] is True de test_tf_ger_2_tarefa_escolhida_primeira_da_sessao; a nova entra logo depois dela - `.claude/skills/scrum-master/SKILL.md:328` — a linha da tabela que começa por | `M-1` | (única; localizar pelo texto)

**Verificação:** 1. `python -m pytest tests/test_progresso_hook.py -q` → antes `32 passed` (medido 2026-09-24 pelo consultor), depois `32 passed`. 2. `python -m pytest tests/ -q` → `<N> passed`, com `<N>` = total re-medido no despacho (medido 2026-09-24, acionamento 14: `312 passed`); o total não muda. 3. Contagens de `encerrada` no gancho e na skill, bloco cercado (colar numa sessão PowerShell na raiz): ``` "encerrada " + ((@('.claude/tools/progresso_hook.py','.claude/skills/scrum-master/SKILL.md') | ForEach-Object { (Select-String -SimpleMatch -Path $_ -Pattern 'encerrada' | Measure-Object).Count }) -join ' ') ``` → antes `encerrada 1 1`, depois `encerrada 0 0` (medido 2026-09-24 em `powershell` 5.1 e `pwsh`, na árvore e numa cópia com a mudança). 4. Igualdade da tabela da skill com a `### 4.1`, bloco cercado por conter barra invertida: ``` python -c "import re;f=lambda p:[l.rstrip() for l in open(p,encoding='utf-8') if re.match(r'^\| .M-\d+b?. \|',l)];a=f('.claude/skills/scrum-master/SKILL.md');b=f('docs/plans/P-0748-tela-do-gerente.md');print('iguais',sum(x==y for x,y in zip(a,b)),'de',len(a),len(b))" ``` → antes `iguais 23 de 24 24` (medido 2026-09-24, depois de `DTG-50` mudar a `M-1` da `### 4.1`), depois `iguais 24 de 24 24`. 5. `(Select-String -Path .claude/tools/progresso_hook.py -Pattern "^(from|import) (rdo|backlog|telemetria|modelo|ocupacao|materializar|subprocess)\b" | Measure-Object).Count` e `(Select-String -SimpleMatch -Path .claude/tools/progresso_hook.py -Pattern "print(" | Measure-Object).Count` → antes `0` e `0`, depois `0` e `0`.

**Pronto quando:** - `stream de dados.arquivo de progresso` — *existe e é alimentado pela função do kit a cada transição do loop: guarda uma linha do repertório por transição, na ordem em que o loop as atravessa, gerada a partir do evento e não da memória do agente — nenhuma linha se perde por o condutor ter esquecido a forma —, e nada mais: nenhuma busca, leitura ou saída de comando, e nenhuma chamada feita dentro dos agentes despachados* — Verificação 1 (`TF-GER-2`), 3 e 4.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-24
- **Fundamento:** `DTG-50` (consultor, acionamento 14), `AE-22`, `DTG-47`, `DTG-48`.
- **Depende de:** `TLG-T3e`
- **Operação do modelo:** `OP-3` - OP-3: O mantenedor do kit escreve a função que gera a linha do stream: a cada evento de transição do loop — tarefa escolhida, estado mudado, agente despachado, agente de volta, evidência coletada, tarefa fechada — ela monta a frase do repertório com os campos do evento e a grava no arquivo de progresso, trocando o identificador da tarefa pelo título dela e o do plano pelo título do plano; a frase da coleta de evidência diz o que se coleta — o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e das guardas do kit. O gancho deixa de copiar texto marcado pelo condutor, e toda outra saída — buscas, leituras, comandos e as chamadas feitas dentro dos agentes despachados — segue fora do arquivo. - precisa de: stream de dados — Quem implementa recebe o loop do condutor — as transições que ele atravessa a cada tarefa e o que ele tem em mãos em cada uma —, a função do kit que gera a linha a partir do evento de cada transição, e o arquivo de progresso onde essa função grava. A ferramenta que roda os agentes e o painel que mostra o arquivo ficam como estão.; tarefa — Quem implementa lê dela o que preenche as mensagens: qual tarefa, o título dela, qual passo e o que o passo pede. Nada nela muda.; mente do agente — Quem implementa usa a intenção que o condutor já tem em mãos — o que ele pediu ao agente e o que o agente devolveu — como campo do evento que a função recebe. O raciocínio interno fica fora da tela, e nenhum agente é reescrito para mudar a forma como entende o passo.
- **Camada e fronteira:** kit — `.claude/tools/progresso_hook.py` (uma instrução da regra 1 de `evento`), `tests/test_progresso_hook.py` (uma asserção nova em `TF-GER-2`) e **uma** linha da seção *Repertório de mensagens ao gerente* da `scrum-master` (`M-1`, cópia legível da `### 4.1`, que o consultor já mudou em `DTG-50`). Todo o resto fica como está.
- **Domínio:** *chave sem leitor* = chave do estado próprio (`.claude/estado/progresso-estado.json`) que o gancho grava e que nenhum código do kit lê; `encerrada` ficou assim com `TLG-T3e` (o `Stop` deixou de gravá-la `True` e de lê-la, `DTG-48`): só a regra 1 a grava, sempre `False` (`AE-22`). A chave que já está no `progresso-estado.json` da sessão corrente fica lá, inerte, até o `session_id` mudar (o estado se reinicia); ninguém a lê.
- **Contratos/classes:** assinaturas e `FRASES` inalteradas. Regra 1: sai a linha `estado_loop["encerrada"] = False`; a `estado_loop["aberta"] = True` antes dela fica.
- **Texto novo, literal:** na `scrum-master`, a linha que começa por `` | `M-1` | `` passa a ser, inteira, a linha de mesmo início da `### 4.1` do plano (copiar do plano, não redigitar).
- **Passos:** 1. Rodar a Verificação 1, 3 e 4 e anotar (contingências 1 e 2). 2. Apagar a instrução do gancho (`Contratos/classes`). 3. Inserir a asserção de `Testes`. 4. Trocar a linha `M-1` da skill (`Texto novo, literal`). 5. Rodar a Verificação 1 a 5.
- **Restrições desta tarefa:** `I-3` — nenhum comando, marcador ou flag novo do condutor; `I-11` — o gancho segue sem imprimir e saindo sempre `0`; `DTG-36` — `FRASES` não muda; `AE-10` — nenhum passo nem verificação roda `progresso_hook.py` contra o `.claude/estado/` real; `I-7` — o total de `pytest tests/` não cai.
- **Não fazer:** não editar outra instrução do gancho; não apagar nem reescrever `.claude/estado/progresso.txt` ou `progresso-estado.json`; não editar outra linha da skill, a `### 4.1` do plano nem o `README.md` (é `TLG-T5a`); não editar `modelo.py`, `.claude/projecoes.json` nem `.claude/settings.json`; não alterar outra asserção dos `TF`.
- **Contingências:** 1. se `python -m pytest tests/test_progresso_hook.py -q` antes da edição não sai `32 passed` → parar e sinalizar `blocked` razão `dependencia`, devolvendo a linha impressa; 2. se a Verificação 3 antes da edição não imprime `encerrada 1 1`, ou a 4 `iguais 23 de 24 24` → parar e sinalizar `blocked` razão `premissa`, devolvendo a linha impressa e a saída de `grep -rn "encerrada" .claude/tools .claude/skills`; 3. se `python -m pytest tests/ -q` reduz o total por teste **fora** de `tests/test_progresso_hook.py` → parar e sinalizar `blocked` razão `dependencia` com o nome do teste.
- **Testes:** `tests/test_progresso_hook.py`. Asserção nova, e só ela: `TF-GER-2` — logo depois de `assert estado_loop["aberta"] is True` (linha 127), `assert "encerrada" not in estado_loop`. Nenhuma função nova. Medido pelo consultor em 2026-09-24 numa cópia temporária: com a asserção e o gancho da árvore, `1 failed, 31 passed` (`TF-GER-2`); com a asserção, o gancho sem a instrução e a skill trocada, `32 passed`. Suítes: `python -m pytest tests/test_progresso_hook.py -q`; `python -m pytest tests/ -q`.
- **Fora do escopo desta tarefa:** a chave já gravada no `progresso-estado.json` da sessão corrente (inerte; sai com o reinício por sessão); a célula do `README.md` (`TLG-T5a`); o recorte `--desde` do dossiê (`AE-4`, `AE-5`, `AE-11`, `TK-55`); propagação aos kits derivados (`DTG-8`).

## Execução

**Consumo:** 18 tool uses, 55.0 k tokens, 93.6 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
