# RDO — DIARIO_DE_OBRAS · TK-87a

# Humano

Tarefa "O item do `backlog.py` termina no cabeçalho de nível 1 ou 2 seguinte" concluída em 2026-09-26.
O dossiê do último card de um plano não carrega mais as seções seguintes do plano: o item para no próximo cabeçalho de nível 1 ou 2 fora de bloco de código.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Tíquete "O dossiê do último card de um plano leva as seções seguintes do plano": 1/1 tarefas concluídas; nenhuma tarefa pronta na fila dele.
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-87a` — O item do `backlog.py` termina no cabeçalho de nível 1 ou 2 seguinte
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** em `_scan_items` de `.claude/tools/backlog.py`, o fim do item (`fim_idx`) passa a ser o menor entre o de hoje (linha antes do próximo cabeçalho de item, ou a última do arquivo) e a linha antes da primeira linha, depois do cabeçalho do item, que casa `NIVEL_1_OU_2_RE` fora de cerca de código. Uma linha que começa por três crases ou por `~~~` abre ou fecha a cerca. O `texto`, o `linha_fim` e as extrações de status, `Depende de` e `Tipo` do item passam a ler só essa faixa. A regra vive numa função auxiliar, chamada uma vez em `_scan_items`.

**Arquivos-alvo:** - `.claude/tools/backlog.py` - `tests/test_backlog.py`

**Verificação:** 1. `python -c "import subprocess,sys;o=subprocess.run([sys.executable,'.claude/tools/backlog.py','show','EBK-T14'],capture_output=True,text=True,encoding='utf-8').stdout;print(sum(1 for l in o.splitlines() if l.startswith('## ')))"` → `0` (linhas `## ` no dossiê do último card do `P-0751`) — antes `3`, depois `0`. 2. `python .claude/tools/backlog.py check` → `check: OK — nenhuma violação.` — antes `exit 0`, depois `exit 0`. 3. `python -m pytest tests/test_backlog.py -q -k scan_items_corta_no_nivel_2` → o teste novo verde — antes `exit 5`, depois `exit 0` (antes nenhum teste selecionado). 4. `python -m pytest tests/test_backlog.py -q` → verde — antes `exit 0`, depois `exit 0`. 5. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`.

**Pronto quando:** o dossiê do último card de um plano para no cabeçalho de nível 1 ou 2 seguinte, e cabeçalho dentro de cerca não corta o item.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Caso medido que motivou:** ver `## TK-87`.
- **Reparo medido (protótipo do consultor, 2026-09-26, cópia da árvore já apagada):** a auxiliar `_fim_na_secao(linhas, inicio_idx, fim_idx)` percorre de `inicio_idx + 1` a `fim_idx`, alternando a cerca, e devolve `j - 1` na primeira `NIVEL_1_OU_2_RE` fora dela. Com ela: `show EBK-T14` sem nenhuma linha `## `, `show TK-76a` ainda com o texto cercado, `check` da árvore OK, suíte `376 passed`. O teste abaixo falha sobre o `backlog.py` de hoje.
- **Testes (novo, em `tests/test_backlog.py`, com `_load_backlog`, nome começado por `test_scan_items_corta_no_nivel_2`):** TF sobre `backlog._scan_items(linhas, "p.md")`, com `linhas` = `# P-0999 — Plano`, vazia, `## 5. Tarefas`, vazia, `### X-T1 — Um [Sonnet · esforço low · classe implementacao]`, vazia, ``- **Status:** `ready` ``, vazia, `~~~~`, `## Dentro da cerca`, `~~~~`, vazia, `## 6. Ordem de execução`, vazia, `` `X-T1` ``, vazia, `## 8. Achados`, vazia, `- achado` → o item `X-T1` tem `linha_fim == 12`, o `texto` dele contém `## Dentro da cerca` e não contém `## 6. Ordem de execução`.
- **Não fazer:** não mudar `HEADING_RE` nem o `rdo.py`; não cortar em `### ` (tíquetes do diário têm subseções `### ` que são corpo); não mudar o teto `DB-7` de `_truncar`.
- **Contingências:** - se um teste existente cair com o reparo → parar e sinalizar `blocked` razão `premissa`, nomeando o teste (medido no protótipo: nenhum cai).
- **Handover:** 2026-09-26 · para quem vier depois - **Entregue:** _fim_na_secao em .claude/tools/backlog.py:303, chamada uma vez em _scan_items (.claude/tools/backlog.py:350); teste test_scan_items_corta_no_nivel_2 em tests/test_backlog.py:145 - **Contrato:** o item de _scan_items termina antes do primeiro cabeçalho # ou ## fora de cerca de código (três crases ou ~~~); texto, linha_fim, status, Depende de e Tipo leem só essa faixa; ### continua sendo corpo - **Não refazer:** o corte em nível 1/2 com respeito à cerca já está coberto por teste; show EBK-T14 sai sem linhas ## - **Pendente:** nenhum
- **Notas de execução:** - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-87a-o-item-do-backlog-py-termina-no-cabecalho-de-nivel-1-ou-2-se.md`, veredito aprovado 100%

## Execução

**Consumo:** 28 tool uses, 74.0 k tokens, 302.2 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master concluiu a tarefa "TK-86" e vai pegar a tarefa "O item do `backlog.py` termina no cabeçalho de nível 1 ou 2 seguinte".
Tarefa "O item do `backlog.py` termina no cabeçalho de nível 1 ou 2 seguinte". Passo: conferir os gates e preparar o despacho.
Tarefa "O item do `backlog.py` termina no cabeçalho de nível 1 ou 2 seguinte". Passo: conferir os gates e preparar o despacho.
Tarefa "O item do `backlog.py` termina no cabeçalho de nível 1 ou 2 seguinte": gates aprovados; vou materializar in-progress e gravar o ponto de partida.
Agente executor recebe a tarefa "O item do `backlog.py` termina no cabeçalho de nível 1 ou 2 seguinte" e vai executar: em `_scan_items` de `.claude/tools/backlog.py`, o fim do item (`fim_idx`) passa a
Agente executor devolveu a tarefa "O item do `backlog.py` termina no cabeçalho de nível 1 ou 2 seguinte": review — sem pendência.
Tarefa "O item do `backlog.py` termina no cabeçalho de nível 1 ou 2 seguinte": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O item do `backlog.py` termina no cabeçalho de nível 1 ou 2 seguinte" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O item do `backlog.py` termina no cabeçalho de nível 1 ou 2 seguinte": aprovado 100%, bloqueante nenhuma.
Scrum master vai fechar a tarefa "O item do `backlog.py` termina no cabeçalho de nível 1 ou 2 seguinte" como done: registrar estado, RDO e telemetria.
Scrum master vai fechar a tarefa "O item do `backlog.py` termina no cabeçalho de nível 1 ou 2 seguinte" como done: registrar estado, RDO e telemetria.
