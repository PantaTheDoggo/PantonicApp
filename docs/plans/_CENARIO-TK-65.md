# Cenário do TK-65 — autoridade sobre o tíquete para o que cobre

Teto: 15k tokens. Escrito só pelo `pantonic-consultant`, com `Edit` mínimo, a cada acionamento. Residência do tíquete: `docs/DIARIO_DE_OBRAS.md`, `## TK-65` (tíquete avulso, sem modelo de domínio: nenhum dossiê `Ato de modelo` cabe aqui).

## Decisões vivas

- `CT65-1` (acionamento 1, gatilho 3: `review_evidence.py` exit 1 no `TK-65b`, `campo obrigatório ausente em 'TK-65b': 'pronto-quando'`): `rota=resolve`, sem `estrategico=`. Lacuna de autoria do card, não da entrega: `rdo.py:309` exige `objetivo`, `verificacao`, `pronto-quando`, e só o `TK-65a` tinha o terceiro. Acrescido `- **Pronto quando:**` aos `TK-65b`, `TK-65c` e `TK-65d`, cada um restrito ao critério que a própria Verificação já media (sem escopo novo). O `TK-65b` segue em `review`; a entrega do executor não foi tocada. Medido depois do reparo, em 2026-09-24: `review_evidence.py` do `TK-65b` (mesmo `--desde`, `--out` temporário) exit `0`; o mesmo gate sobre `TK-65c` e `TK-65d` (`--desde HEAD`) exit `0`; `PYTHONIOENCODING= python -X utf8=0 .claude/tools/backlog.py --help` exit `0`; `backlog.py check` exit `1` só com as três `C-12` que o `TK-65d` saneia.

- `CT65-2` (acionamento 2, gatilho 1: `TK-65c` `blocked` premissa, executor sem edição): `rota=resolve`, sem `estrategico=`. Impedimento **procedente**: o card deixava o ramo acusar/recusar aberto no Objetivo e no Pronto quando. Fechado em **acusar** (escreve, exit 0, `mensagem` com a contagem de reconhecidos e cada id descartado): a diretiva viva do dono (linha 2 do diário) usa a cauda de propósito para a sequência completa — medido em 2026-09-24, 3 ids reconhecidos e 19 ids de item na cauda —, e recusar a tornaria ingravável, contra o "Não fazer" do card (o reparo é tornar o descarte audível). "Id descartado" definido como crase da cauda que está em `_ids_da_arvore` e não no retorno de `_parse_diretiva` (crase como `done`/`next` fica fora). Âncoras do card re-medidas: `transacionar_diretiva` `:1474`, `_parse_diretiva` `:351`, print em `main()` `:1706`. Medido depois do reparo: `review_evidence.py` do `TK-65c` (`--desde HEAD`) exit `0`; `pytest tests/test_backlog.py` 86 passed; `backlog.py check` exit `1` só com as três `C-12` do `TK-65d`; `next` devolve `TK-65c`. Forma literal do aviso deliberadamente não fixada (inconclusivo: só o conteúdo).

## Fila

- `TK-65b` `done`. `TK-65d` (`ready`) → `TK-65c` (`ready`, redespacho após `CT65-2`). Nenhum depende do outro; o corretivo antes do `TK-65c` devolve o `check` a exit 0. Nota: o `next` hoje devolve `TK-65c` primeiro (ordem de documento); a ordem aqui é recomendação, não trava.

## Achados abertos

- `AE-65-1`: o passo 3 do loop (`G-PLANREADY` + Gate de delegação) despachou o `TK-65b` sem o campo que o `rdo.py` exige, e a lacuna só apareceu no passo 6, com a entrega pronta. Nenhum instrumento anterior ao `review_evidence.py` confere os três campos obrigatórios do dossiê em card de diário. Sem card: ver *Matéria inconclusiva*.

## Matéria inconclusiva

- Onde o `AE-65-1` fecha — violação nova do `backlog.py check` (card não-terminal sem `Objetivo`/`Verificação`/`Pronto quando`) ou item do Gate de delegação — não foi decidido: não é um dos três defeitos medidos que definem o `TK-65`, e um lint novo sobre a árvore viva exige medir antes quantos cards de diário hoje o violariam. Matéria de tíquete próprio, se o loop a abrir.
