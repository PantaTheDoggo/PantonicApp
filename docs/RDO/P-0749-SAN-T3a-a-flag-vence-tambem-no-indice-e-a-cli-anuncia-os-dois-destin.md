# RDO — P-0749 · SAN-T3a

**Plano:** `docs/plans/P-0749-saneamento-artefatos.md`
**Tarefa:** `SAN-T3a` — A flag vence também no índice, e a CLI anuncia os dois destinos
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Corretivo da `SAN-T3` (`AE-3`): com `--rdo-dir` sobre plano em pasta o `close` volta a regenerar o `INDEX.md` do diretório da flag; o texto de ajuda de `rdo.py` e `review_evidence.py` anuncia o destino na pasta do plano ao lado do legado; a regressão `TK-62a` amputada pelo TF 15 volta inteira.

**Arquivos-alvo:** - `.claude/tools/rdo.py` - `.claude/tools/review_evidence.py` - `tests/test_rdo.py` - `tests/test_review_evidence.py`

**Verificação:** 1. ``` python -m pytest tests/test_rdo.py tests/test_review_evidence.py -q -k "tf_san or tr_san" ``` → **4 passed**. **Medido antes: 3 passed** (2026-09-25). 2. ``` python -c "import ast,pathlib;t=pathlib.Path('tests/test_review_evidence.py').read_text(encoding='utf-8');f={n.name:ast.get_source_segment(t,n) for n in ast.parse(t).body if isinstance(n,ast.FunctionDef)};print(int('codigo_falho' in f['test_tf_san_15_evidencia_na_pasta_do_plano']), int('codigo_falho' in f['test_cli_main_reconhece_tk_subtarefa_de_ticket_e_recusa_id_fora_da_gramatica']))" ``` → **`0 1`** (Git Bash). **Medido antes: `1 0`** (2026-09-25). 3. ``` pwsh -NoProfile -Command '@(Select-String -LiteralPath .claude/tools/rdo.py,.claude/tools/review_evidence.py -SimpleMatch -Pattern "<pasta-do-plano>").Count' ``` → **5**. **Medido antes: 0** (2026-09-25). 4. ``` python .claude/tools/rdo.py close --help > /dev/null && python .claude/tools/rdo.py laudo --help > /dev/null && python .claude/tools/review_evidence.py --help > /dev/null ``` → **exit 0**. **Medido antes: exit 0**. 5. ``` python -m pytest tests -q ``` → **o total anotado no passo 1 + 1, nenhuma falha**. **Medido antes: 351 passed** (2026-09-25; 352 com o reparo aplicado numa cópia da árvore). 6. ``` python .claude/checks/dead_code.py ``` → **exit 0**. **Medido antes: exit 0**.

**Pronto quando:** - kit.onde se gravam os registros da tarefa — flag explícita vence também no índice, e a CLI anuncia a pasta do plano ao lado do destino legado — Verificação 1, 2, 3

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Fundamento:** DSA-21, DSA-9; I-2; `AE-3`.
- **Depende de:** `SAN-T3`
- **Operação do modelo:** `OP-3` - OP-3: O mantenedor do registro faz os instrumentos de relato e de evidência gravarem o relato, o laudo e a evidência de cada tarefa de plano novo dentro da pasta do plano; tíquete e plano antigo seguem gravando onde gravam hoje. - precisa de: kit — Quem implementa recebe essas ferramentas e esses textos. O que já está gravado continua sendo lido como hoje.; acervo existente — Quem implementa não o toca. Ele prova que nada do que existe se perdeu.
- **Camada e fronteira:** kit, `.claude/tools/rdo.py`, `.claude/tools/review_evidence.py` e dois arquivos de teste. Nenhuma mudança de destino além do `INDEX.md` com flag.
- **Passos:** 1. Rodar `python -m pytest tests -q`; anotar o total. 2. Aplicar os blocos de `Texto novo, literal`. 3. Acrescentar ao fim de `tests/test_rdo.py` o TR de `Testes`. 4. Rodar a Verificação 1 a 6.
- **Restrições desta tarefa:** I-2 — sem flag, destino e índice como a `SAN-T3` entregou; nenhum teste grava no `docs/` real.
- **Não fazer:** não mudar a lógica de destino do `close`, do `laudo` nem do `review_evidence` (só a condição do índice); não tocar `caminhos.py`, `backlog.py` nem a doutrina (`SAN-T4`); não reescrever o TF 15 além de lhe tirar a cauda.
- **Contingências:** 1. se um texto antigo não aparecer literal, ou aparecer mais de uma vez → parar e sinalizar `blocked` razão `premissa`, devolvendo a linha.
- **Fora do escopo desta tarefa:** a doutrina que cita os destinos (`SAN-T4`); a evidência sem os não rastreados anteriores ao despacho (`AE-3` (c), fora do plano).

## Execução

**Consumo:** 38 tool uses, 69.7 k tokens, 157.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: nenhuma; achado de processo (rdo.py --help sai em cp1252 no pipe do Windows) com rota a tíquete de kit

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
