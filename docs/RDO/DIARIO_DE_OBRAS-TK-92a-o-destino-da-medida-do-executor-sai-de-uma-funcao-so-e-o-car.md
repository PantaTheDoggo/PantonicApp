# RDO — DIARIO_DE_OBRAS · TK-92a

# Humano

Tarefa "O destino da medida do executor sai de uma função só, e o `card_check --gravar` sem caminho grava nele" concluída em 2026-09-27.
O lugar onde o executor grava a medida e onde o revisor a procura passou a sair de uma função só.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Tíquete "A medida do executor de card de tíquete grava onde o `review_evidence.py` não procura": 1/1 tarefas concluídas; nenhuma tarefa pronta na fila dele.
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achados registrados no plano, com rota: 2 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-92a` — O destino da medida do executor sai de uma função só, e o `card_check --gravar` sem caminho grava nele
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** 1. `.claude/tools/caminhos.py` ganha `destino_medida(raiz, plano_path, tarefa)`: plano em pasta → `<pasta>/evidencia/<id>-<tarefa>-medida.json`; qualquer outro (plano legado, `docs/DIARIO_DE_OBRAS.md`) → `<raiz>/docs/RDO/evidencia/<id ou stem>-<tarefa>-medida.json`, com `<id ou stem>` = `id_do_plano(plano_path) or Path(plano_path).stem`, a regra que `montar_documento` usa hoje; 2. `montar_documento` de `.claude/tools/review_evidence.py` procura a medida em `destino_medida(root, plano_path, <tarefa>)`; com `dir_evidencia` informado, no mesmo nome de arquivo dentro de `dir_evidencia`, como hoje; 3. `--gravar` de `.claude/tools/card_check.py` aceita vir sem caminho e então grava em `destino_medida(<--root>, <--plano>, <tarefa>)`; com caminho, igual a hoje; ausente, não grava; 4. a doutrina manda rodar `--gravar` sem caminho (os dois trechos de `Passos`).

**Arquivos-alvo:** - `.claude/tools/caminhos.py` - `.claude/tools/review_evidence.py` - `.claude/tools/card_check.py` - `.claude/agents/pantonic-executor.md` - `.claude/skills/scrum-master/SKILL.md` - `tests/test_caminhos.py` - `tests/test_card_check.py`

**Verificação:** 1. `python -c "import sys;sys.path.insert(0,'.claude/tools');import caminhos as c;from pathlib import Path;print(c.destino_medida(Path('.'),Path('docs/DIARIO_DE_OBRAS.md'),'TK-86a').as_posix())"` → `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-86a-medida.json` — antes `exit 1`, depois `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-86a-medida.json`. 2. `python -c "from pathlib import Path;fs=['.claude/agents/pantonic-executor.md','.claude/skills/scrum-master/SKILL.md'];print(sum(Path(f).read_text(encoding='utf-8').count('<P-n>-<ID>-medida.json') for f in fs))"` → `0` — antes `2`, depois `0`. 3. `python -c "from pathlib import Path;fs=['.claude/agents/pantonic-executor.md','.claude/skills/scrum-master/SKILL.md'];print(sum(Path(f).read_text(encoding='utf-8').count('caminhos.destino_medida') for f in fs))"` → `2` — antes `0`, depois `2`. 4. `python -m pytest tests/test_caminhos.py tests/test_card_check.py -q -k "destino_medida or gravar_sem_caminho"` → verde — antes `exit 5`, depois `exit 0`. 5. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`. 6. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `kit_check: check-drift OK` — antes `exit 0`, depois `exit 0`.

**Pronto quando:** a medida de card de tíquete, de plano legado e de plano em pasta é gravada e procurada no mesmo caminho, dado por uma função só (Verificação 1 e 4), e a doutrina manda o `--gravar` sem caminho (Verificação 2 e 3). Medido em protótipo do consultor sobre cópia da árvore, apagada, em 2026-09-26: suíte `428 passed` → `430 passed`, `check-drift` OK.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-27
- **Passos:** 1. Em `.claude/agents/pantonic-executor.md`, item 5a, o trecho depois de `antigo:` vira o trecho depois de `novo:` (sem quebra nova e sem refluxo; o rótulo não entra no arquivo): ```text antigo: --mundo depois --gravar <evidencia>/<P-n>-<ID>-medida.json`, com `<P-n>` o id do plano (`P-0752`, nunca o caminho) e `<evidencia>` = `docs/RDO/evidencia` no plano legado ou `<pasta>/evidencia` no plano em pasta — a pasta em que `review_evidence.py` procura a medida; exit 1 novo: --mundo depois --gravar`, sem caminho — o destino é o de `caminhos.destino_medida`, o mesmo em que `review_evidence.py` procura a medida, em plano legado, plano em pasta e tíquete do diário; exit 1 ``` 2. Em `.claude/skills/scrum-master/SKILL.md`, Passo 5, Saída, idem (o trecho antigo está numa linha só do arquivo): ```text antigo: `<evidencia>/<P-n>-<ID>-medida.json` (`<P-n>` o id do plano; `<evidencia>` = `docs/RDO/evidencia` no legado, `<pasta>/evidencia` no plano em pasta), cuja ausência novo: o destino de `caminhos.destino_medida` (o `card_check.py --gravar` sem caminho grava ali e o `review_evidence.py` procura ali), cuja ausência ```
- **Contratos/classes:** `caminhos.destino_medida(raiz: Path, plano_path: Path, tarefa: str) -> Path`. O `card_check.py` carrega `caminhos.py` do diretório do próprio módulo, como o `review_evidence.py` já faz. O JSON gravado não muda.
- **Caso medido que motivou:** ver `## TK-92`.
- **Testes (novos):** TF `test_tf_destino_medida_tres_residencias` (`tests/test_caminhos.py`) — `docs/DIARIO_DE_OBRAS.md` e `TK-1a` → `<raiz>/docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-1a-medida.json`; `docs/plans/P-0001-x.md` e `T1` → `<raiz>/docs/RDO/evidencia/P-0001-T1-medida.json`; `docs/plans/P-0002-y/plano.md` e `T2` → `docs/plans/P-0002-y/evidencia/P-0002-T2-medida.json`. TF `test_tf_gravar_sem_caminho_grava_no_destino_derivado` (`tests/test_card_check.py`) — raiz temporária com o `plano-corpus.md` da fixture copiado como `docs/DIARIO_DE_OBRAS.md`, `--gravar` sem valor → exit `0` e `docs/RDO/evidencia/DIARIO_DE_OBRAS-CX-T1-medida.json` gravado na raiz temporária (nada gravado no repositório).
- **Não fazer:** não mudar o JSON gravado nem o nome que o `review_evidence.py` procura hoje em plano legado e em pasta; não renomear nem apagar `docs/RDO/evidencia/P-0751-TK-86a-medida.json`; não tocar `.claude/skills/fatos-frescos/SKILL.md` (o `--gravar <caminho>` que ele ensina segue válido); não tocar `_classificar_campo_alvos` (é do `TK-89a`).
- **Contingências:** - se um teste existente de `tests/test_review_evidence.py` sobre a seção de medida do executor cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste (no protótipo, nenhum caiu).
- **Handover:** 2026-09-27 · para `TK-93a` - **Entregue:** caminhos.destino_medida (.claude/tools/caminhos.py:110) usado por review_evidence para procurar e por card_check --gravar sem caminho para gravar; doutrina do executor e do scrum-master manda --gravar sem caminho - **Contrato:** a medida do executor grava e é achada pelo mesmo caminho, em plano legado, em pasta e no diário - **Não refazer:** nada a declarar - **Pendente:** nenhum
- **Notas de execução:** - 2026-09-27 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-92a-o-destino-da-medida-do-executor-sai-de-uma-funcao-so-e-o-car.md`, veredito aprovado 100%

## Execução

**Consumo:** 49 tool uses, 90.3 k tokens, 402.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

Exercício ponta a ponta feito em raiz temporária nas três residências (plano em pasta, plano legado, diário): card_check --gravar sem caminho grava exatamente onde review_evidence procura (em pasta, via --out padrão <pasta>/evidencia; nos outros, via destino_medida). A prova real do caminho do diário é esta própria revisão: o dossiê de evidência achou a medida do executor em docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-92a-medida.json.

## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master concluiu a tarefa "`rdo.py laudo --motivo` e o alvo `dossiê`" e vai pegar a tarefa "O destino da medida do executor sai de uma função só, e o `card_check --gravar` sem caminho grava nele".
Tarefa "O destino da medida do executor sai de uma função só, e o `card_check --gravar` sem caminho grava nele". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O destino da medida do executor sai de uma função só, e o `card_check --gravar` sem caminho grava nele" e vai executar o card.
Agente executor devolveu a tarefa "O destino da medida do executor sai de uma função só, e o `card_check --gravar` sem caminho grava nele": review — sem pendência.
Agente revisor recebe a tarefa "O destino da medida do executor sai de uma função só, e o `card_check --gravar` sem caminho grava nele" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O destino da medida do executor sai de uma função só, e o `card_check --gravar` sem caminho grava nele": aprovado 100%, bloqueante nenhuma.
Scrum master vai fechar a tarefa "O destino da medida do executor sai de uma função só, e o `card_check --gravar` sem caminho grava nele" como done: registrar estado, RDO e telemetria.
