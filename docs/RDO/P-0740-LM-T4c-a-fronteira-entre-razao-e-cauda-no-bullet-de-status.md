# RDO — P-0740 · LM-T4c

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T4c` — A fronteira entre razão e cauda no bullet de `Status`
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — a cauda em prosa sobrevive **também** no ramo canônico, que é o que o próprio módulo emite ao transitar para `blocked` com `--razao`.

**Arquivos-alvo:** - `.claude/tools/backlog.py` - `tests/test_backlog.py`

**Verificação:** 1. ``` python -c "import sys;sys.path.insert(0,'.claude/tools');import backlog;m=backlog.STATUS_BULLET_RE.match('- **Status:** `blocked` · 2026-09-19 · premissa — cauda viva');print('razao-limpa' if m.group(2)=='premissa' and m.group(3)=='cauda viva' else 'razao-suja')" ``` → **razao-limpa**. **Medido antes: razao-suja**. Saída deliberadamente **ASCII**, para não depender da codificação do filho (`AE-33` item 2). 2. ``` python -m pytest tests/test_backlog.py -q ``` → verde, com **dois testes a mais** que o total re-medido no despacho (`DM-23`). **Medido antes: exit 0** — veredito invariante; a relação *dois a mais* é do reviewer, que mede o módulo antes e depois na mesma janela. Referência **datada**, e não aceite: `45 passed` em 2026-09-19 (`ESC-28`; era `41` na autoria, e o reparo do `AE-47` somou 4 TF ao mesmo módulo). 3. ``` python -c "import sys;sys.path.insert(0,'.claude/tools');import backlog;from pathlib import Path;L=[l for l in Path('docs/plans/P-0740-loop-de-modulos.md').read_text(encoding='utf-8').splitlines() if l.startswith('- **Status:**')];print('iguais' if len(L)==sum(1 for l in L if backlog.STATUS_BULLET_RE.match(l)) else 'divergem')" ``` → **iguais**, **inalterado**: a leitura dos bullets do plano não regride. **Medido antes: iguais** — o comando publica o **veredito**, não os dois totais: a contagem de cards do plano é corpus que qualquer outra entrega move (era `26 26` na autoria, é `29 29` em 2026-09-19), e veredito binário é invariante a ela (`ESC-28`).

**Pronto quando:** o ramo canônico separa razão de cauda, o round-trip `blocked → ready` preserva a prosa, os dois testes existem, e as três linhas de `Verificação` saem como escritas.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` · 2026-09-19 — card novo do `ESC-19` (2026-09-19), residência única do `AE-35` item 1. **Declarado PÓS-MARCO**: não entra antes da `LM-T6`, por decisão registrada no `DM-42` (ii).
- **Esforço:** low
- **Depende de:** `LM-T4b` (fechada — é o módulo dela que esta tarefa completa). Nada depende desta.
- **A causa, medida no `ESC-19` por introspeção — é de gramática, não de escrita:** `STATUS_BULLET_RE` (`:76`) é `` ^- \*\*Status:\*\* `([a-z-]+)`(?: · \d{4}-\d{2}-\d{2}(?: · (.+))?|.*?)(?: — (.+))?$ ``. O grupo da razão é `(.+)` **guloso** e o da cauda é opcional, de modo que **nada força a divisão no ` — `**. Medido sobre a linha que o próprio módulo escreve (`- **Status:** `blocked` · 2026-09-19 · premissa — cauda viva`): `razao='premissa — cauda viva'` e `cauda=None`; na transição seguinte para `ready`, `razao` vira `None` por não haver `--razao`, `cauda` já era `None`, e a linha sai **`- **Status:** `ready` · <hoje>`** — a prosa **some**. O ramo em prosa (`(2026-01-01) — cauda viva`) está **correto** e não se toca: `razao=None`, `cauda='cauda viva'`.
- **Produto do módulo:** (a) `STATUS_BULLET_RE` separa razão e cauda **nos dois ramos**, pela fronteira acima; (b) o docstring do módulo (`:21`) enuncia a fronteira com o caso medido; (c) nada mais muda — escrita, vocabulário, `_TRANSICOES` e forma canônica ficam como estão.
- **Restrições desta tarefa:** a **escrita** não muda — `transacionar_status` já preserva a cauda que o leitor lhe entrega, e o defeito é do **leitor**. `_TRANSICOES`, vocabulário de estados e forma canônica ficam intocados. Nenhum card do plano é reescrito.
- **Não fazer:** não tocar `docs/plans/P-0739-backlog-instrumento.md` (o plano está estacionado por ato do dono, e esta matéria **não** é dele — `DM-42` (i)); não tocar `card_check.py`; não commitar.
- **Contingências:** 1. se `STATUS_BULLET_RE` não estiver na forma citada → parar e sinalizar `blocked` razão `premissa`, citando a encontrada; 2. se a `Verificação` 3 deixar de sair com os dois números iguais → **parar**: a fronteira nova estaria cortando bullet legítimo, e isso é decisão de consultor.

## Execução

**Consumo:** 20 tool uses, 74.2 k tokens, 195.1 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: Contrato de razao do backlog.py assimetrico: o leitor tem fronteira estrita (LM-T4c) e o escritor aceita --razao com travessao sem validar - razao nao round-trippavel em duas bordas medidas; decidir no replanejamento do P-0740 se o escritor valida, normaliza ou se a degradacao e aceitavel.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

1) O par de testes nomeados pelo card e suficiente para o que o card prometeu e cego para o contrato que ele deixou aberto: o TF fixa a linha canonica e o TR fixa o round-trip com razao limpa - nenhum dos dois toca razao com travessao, que e exatamente onde a fronteira nova cria comportamento novo. Foi o exercicio ponta a ponta pela CLI (verbos status/show/next/check sobre copia de fixture) que expos as duas bordas, nao a leitura do diff. 2) Confronto old-vs-new sobre o corpus inteiro (46 bullets de Status em docs/plans/*.md + docs/DIARIO_DE_OBRAS.md) e barato e mais forte que a Verificacao 3 do card, que so mede um plano: 0 bullets perderam match, 5 mudaram de grupos, e as 5 sao exatamente o defeito que a tarefa foi corrigir. Vale como padrao de aceite para card que mexe em regex de corpus. 3) A janela --desde f1afbd3 misturou cinco entregas nos MESMOS dois arquivos-alvo (LM-T4c e o reparo AE-47/ESC-27 do consultor); a separacao foi limpa porque o diff e cirurgico - 3 hunks da entrega (docstring :18, STATUS_BULLET_RE :78, strip em _extrair_status :210) e 2 testes com os nomes literais do card, contra 6 hunks e 4 TF do AE-47. Piso do modulo: 41 (autoria) -> 45 (AE-47) -> 47 medido agora, isto e 45 + os dois testes, como a relacao do card manda.

## Fechamento

**Desdobramento:** aprovado
