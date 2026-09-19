# RDO — P-0740 · LM-T3b

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T3b` — O campo termina no bullet: `_parsear_campos` e a autoridade mecânica do `escopo`
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — o conjunto de `Arquivos-alvo` que o dossiê declara passa a ser o que o card lista, para que a dimensão `escopo` continue **mecânica** em vez de depender de julgamento sobre ruído.

**Arquivos-alvo:** - `.claude/tools/rdo.py` - `tests/test_rdo.py`

**Verificação:** (`DM-12`: as baselines abaixo foram medidas pelo consultor no `ESC-12`, **emulando o reparo** sobre os cards reais deste plano, não sobre fixture) 1. Extração sobre o card da `LM-T2b`, pelo instrumento: ``` python -c "import sys;sys.path.insert(0,'.claude/tools');import rdo,review_evidence as r;from pathlib import Path;L=Path('docs/plans/P-0740-loop-de-modulos.md').read_text(encoding='utf-8').splitlines();i=next(k for k,x in enumerate(L) if x.startswith('### LM-T2b '));j=next(k for k in range(i+1,len(L)) if L[k].startswith('### '));print(len(r.extrair_arquivos_alvo(rdo._parsear_campos(L[i+1:j])[0])))" ``` → **2**. **Medido antes: 9**; e **medido depois: 2**, na emulação do reparo. 2. A mesma extração sobre `LM-T2e`, `LM-T3a`, `LM-T4`, `LM-T5` e `LM-T6` → **1, 2, 5, 1, 2**, **inalteradas**. Medidas nos dois mundos no `ESC-12`, iguais nos dois: é a linha que impede o reparo de cortar alvo legítimo. 3. `python -m pytest tests/ -q` → verde, com **dois testes a mais** que o total re-medido no despacho (`DM-23`). Referência histórica, não aceite: `175 passed` em 2026-09-19.

**Pronto quando:** a extração da `LM-T2b` devolve 2, as cinco extrações da `Verificação` 2 seguem em 1, 2, 5, 1, 2, os dois testes existem e a suíte fica verde sem reduzir o total.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` (despachada em 2026-09-19; gateada por medida própria do loop — o consultor caiu por limite de sessão, `ESC-22`) — card novo do `ESC-12` (2026-09-19), residência única do `AE-27` item 2.
- **Esforço:** low
- **Depende de:** `LM-T3a` (fechada — é o contrato do mesmo instrumento) e `DM-35` (iii). **Precede a `LM-T6`**: o piloto mede o loop de ponta a ponta, e a autoridade mecânica do `escopo` é um dos contratos que ele exercita.
- **A causa, medida no `ESC-12` (é de gramática, não de heurística):** `_parsear_campos` (`.claude/tools/rdo.py:186`) encerra o campo corrente **só** quando a linha casa `_CAMPO_RE` (`- **Rótulo:** …`). Um bullet de prosa cujo rótulo não termina em `:**` — como `- **A calibração medida no \`ESC-3\` (2026-09-18) — residência única desta tabela.**` — **não** encerra nada, e todas as linhas indentadas seguintes (a tabela de calibração inteira) continuam sendo anexadas a `arquivos-alvo`. Depois, `_eh_caminho` aceita `251.1` e `message.id` como caminho, porque têm "extensão". Medido na `LM-T2b`: **9** alvos extraídos contra **2** declarados — `message.id`, `251.1`, `505.2`, `2330.8`, `946.9`, `.jsonl` e `telemetria_hook.py` entraram, gerando sete seções de diff vazias.
- **Produto do módulo:** (a) em `_parsear_campos`, **um bullet de topo encerra o campo corrente**, case ele `_CAMPO_RE` ou não — hoje só campo canônico encerra; linha indentada continua alimentando o campo, como hoje; (b) o docstring da função enuncia a regra e a razão medida (`AE-27` item 2), citando o caso da `LM-T2b`.
- **Restrições desta tarefa:** `_eh_caminho` e `_classificar_campo_alvos` (`.claude/tools/review_evidence.py`) ficam **intocados** — a causa medida é o **limite do campo**, e alargar a gramática de caminho seria tratar o sintoma; `review_evidence.py` **não** está nos alvos. Nenhum outro campo do dossiê muda de semântica.
- **Não fazer:** não tocar `.claude/tools/review_evidence.py` nem `tests/test_review_evidence.py`; não mexer nos baldes da `DB-25` (o `registro_orquestracao` está **certo**, medido no `ESC-12`: `docs/telemetria.tsv` já cai nele); não tocar card nenhum do plano para "contornar" o parser; não commitar.
- **Contingências:** 1. se `_parsear_campos` não estiver na forma citada (o `for` com `_CAMPO_RE.match`, o ramo de linha indentada e `em_extra`) → parar e sinalizar `blocked` razão `premissa`, citando a forma encontrada; 2. se a `Verificação` 2 mudar para qualquer card → **parar e sinalizar `blocked` razão `premissa`**: o reparo estaria cortando alvo legítimo, e isso é decisão de consultor, não de execução.

## Execução

**Consumo:** 19 tool uses, 64.2 k tokens, 133.5 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: Invariante de aceite publicado como literal envelheceu em um dia (LM-T4: 5 para 8 por reescrita legitima de outro card) e quase disparou blocked indevido: a secao 8 da rubrica e a linha LM-T3b da 8.2 precisam de decisao no planejamento pos-marco - invariante de contingencia em relacao, nunca em literal.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
