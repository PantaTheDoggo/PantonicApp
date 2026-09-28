# RDO — DIARIO_DE_OBRAS · TK-88c

# Humano

Tarefa "O painel lê cada argumento da própria invocação, e o RDO publicado diz o plano e a tarefa certos" concluída em 2026-09-26.
O painel do gerente passou a ler cada comando pelo que ele próprio invoca, e as RDO já publicadas trazem o título e o caminho do plano certos.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Tíquete "O encerramento de tarefa e de plano vira um comando, com relatório em três seções e handover no card": 3/4 tarefas concluídas; próxima: "O fechamento pergunta ao `rdo.py` e ao `backlog.py` se pode escrever, em vez de copiar a regra deles".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achados registrados no plano, com rota: 2 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-88c` — O painel lê cada argumento da própria invocação, e o RDO publicado diz o plano e a tarefa certos
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** no ramo `PreToolUse` · `Bash` de `evento` em `.claude/tools/progresso_hook.py`, a linha de comando se lê por invocação: as frases de `backlog.py status` (`M-2`, `M-10`, `M-10b`), de `encerrar.py tarefa` (`M-10`), de `encerrar.py plano` (`M-18`) e de `review_evidence.py` (`M-5`, `M-13`) só saem quando o script é o programa de uma invocação — `python` (ou `python3`/`py`, com ou sem caminho e opções) seguido do caminho que termina no script e, onde há verbo, do verbo —, e `--tarefa`, `--plano` e `--atribuir` se leem só nos argumentos dessa invocação. Invocações se separam por `&&`, `||`, `;`, `|` e quebra de linha fora de aspas. Texto de argumento que cite o script (mensagem de commit, `--resumo`, `--achado`) não gera frase. `rdo.py close` grava a linha `**Plano:**` com barra normal, venha o caminho como vier. As RDO publicadas se corrigem: em todo `docs/**/*.md`, a frase do painel com `a tarefa "<ID>-revisao"` passa a `a tarefa "<título do card <ID>>"` (título do backlog), e a linha `**Plano:**` com barra invertida passa a barra normal (`CT-1` do `## TK-88`).

**Arquivos-alvo:** - `.claude/tools/progresso_hook.py` — `evento`, ramo `PreToolUse` · `Bash` - `.claude/tools/rdo.py` — `cmd_close`, valor de `PLANO_PATH` - `.claude/skills/scrum-master/SKILL.md` — repertório do painel, linhas `M-2`, `M-5`, `M-10`, `M-13` e `M-18`: o gatilho passa a dizer que o script e os argumentos se leem na própria invocação - `docs/RDO/P-0752-FPU-*.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-91a-*.md` e toda RDO que a regra acima achar em `docs/**/*.md` quando a tarefa rodar - `tests/test_progresso_hook.py`, `tests/test_rdo.py`

**Verificação:** 1. `python -m pytest tests/test_progresso_hook.py tests/test_rdo.py -q -k "propria_invocacao or plano_em_barra"` → verde — antes `exit 5`, depois `exit 0` (antes nenhum teste selecionado). 2. `python -c "import re;from pathlib import Path;print(sum(len(re.findall('a tarefa '+chr(34)+'[A-Z][A-Za-z0-9-]*-revisao'+chr(34),p.read_text(encoding='utf-8'))) for p in Path('docs').rglob('*.md'))>0)"` → `False` — antes `True`, depois `False`. 3. `python -c "from pathlib import Path;print(sum(1 for p in Path('docs').rglob('*.md') for l in p.read_text(encoding='utf-8').splitlines() if l.startswith(chr(42)*2+'Plano:') and chr(92) in l)>0)"` → `False` — antes `True`, depois `False`. 4. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0` (piso re-medido no despacho).

**Pronto quando:** comando encadeado e script citado em argumento não trocam o título nem inventam frase no painel (Verificação 1), e nenhuma RDO publicada traz o id `-revisao` em frase do painel nem o caminho do plano com barra invertida (Verificações 2 e 3).

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Depende de:** `TK-88b`
- **Testes (novos):** TF `test_tf_m10_da_propria_invocacao_em_comando_encadeado` — `evento` sobre `python .claude/tools/telemetria.py append --tarefa X-revisao …; python .claude/tools/encerrar.py tarefa --plano <p> --tarefa X` → `M-10` com o título de `X` e `tarefa_fechada` = `X` (hoje sai o título `X-revisao`, reproduzido pelo revisor com `FPU-T8`); TR `test_tr_literal_em_argumento_nao_e_propria_invocacao` — `git commit -m "… encerrar.py plano …"` não gera `M-18`, e um `--resumo "encerrar.py tarefa --tarefa Y"` noutro comando não gera `M-10`; TF `test_tf_review_evidence_da_propria_invocacao` — o `--tarefa` de um comando anterior na linha não muda o título da `M-5`; TF `test_tf_close_grava_plano_em_barra` (`test_rdo.py`) — `cmd_close` com o caminho do plano em barra invertida grava a linha `**Plano:**` sem barra invertida.
- **Não fazer:** não tocar `encerrar.py` (o `**Plano:**` se corrige no `rdo.py`, que serve também o `rdo.py close` direto); não reescrever `.claude/estado/progresso.txt`; não reconstruir nas RDO a linha `M-10` que o defeito rotulou com o id `-revisao` (`CT-1`); não mudar o texto de `FRASES`; nas RDO, não tocar nada além das duas correções.
- **Contingências:** - se teste existente de `test_progresso_hook.py` fixar a detecção por substring (script citado em argumento gerando frase) → o teste que fixa o comportamento antigo é alvo da tarefa (`DM-33` do `P-0740`): ajustar e nomear no retorno. - se uma RDO trouxer `<ID>-revisao` cujo `<ID>` o backlog não conhece → parar e sinalizar `blocked` razão `premissa`, nomeando o arquivo.
- **Handover:** 2026-09-26 · para `TK-88d` - **Entregue:** progresso_hook.py lê script e argumentos por invocação (_dividir_invocacoes :248, _programa :293); rdo.py cmd_close grava **Plano:** em barra normal; 21 RDO corrigidas (-revisao → título; Plano: barra normal) - **Contrato:** comando encadeado ou script citado em argumento não troca o título nem gera frase no painel - **Não refazer:** nada a declarar - **Pendente:** nenhum
- **Notas de execução:** - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-88c-o-painel-le-cada-argumento-da-propria-invocacao-e-o-rdo-publ.md`, veredito aprovado 100%

## Execução

**Consumo:** 75 tool uses, 154.7 k tokens, 911.4 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

O revisor exercitou o hook com 16 formas de comando (cadeia com ;, &&, ||, |, heredoc de commit dentro de aspas, launcher py -3, interpretador com caminho absoluto e script entre aspas com barra invertida, --atribuir em invocação vizinha): todas deram a frase esperada. Fica de fora do que o card pediu, e não é defeito: 'python -X utf8 <script>' (a opção com valor é lida como o script) e o prefixo de variável de ambiente ('PYTHONUTF8=1 python ...') não geram frase; hoje nenhum instrumento do loop invoca assim.

## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master concluiu a tarefa "O fechamento de tarefa e de plano é um comando cada, com RDO e entrega em três seções e handover no card" e vai pegar a tarefa "O painel lê cada argumento da própria invocação, e o RDO publicado diz o plano e a tarefa certos".
Tarefa "O painel lê cada argumento da própria invocação, e o RDO publicado diz o plano e a tarefa certos". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O painel lê cada argumento da própria invocação, e o RDO publicado diz o plano e a tarefa certos" e vai executar: no ramo `PreToolUse` · `Bash` de `evento` em `.claude/tools/progresso_hook.py`, a linha de comando se lê por invocação: as frases de `backlog.py status` (`M-2`, `M-10`, `M-10b`), de `encerrar.py tarefa` (`M-10`), de `encerrar.py plano` (`M…
Agente executor devolveu a tarefa "O painel lê cada argumento da própria invocação, e o RDO publicado diz o plano e a tarefa certos": review — sem pendência.
Scrum master vai fechar a tarefa "O painel lê cada argumento da própria invocação, e o RDO publicado diz o plano e a tarefa certos" como done: registrar estado, RDO e telemetria.
