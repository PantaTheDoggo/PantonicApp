# RDO — DIARIO_DE_OBRAS · TK-65a

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-65a` — `check` recusa id de `Depende de:` que não é item
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** acrescentar ao `check` uma violação de vocabulário fechado (`C-*`, como as demais) que acuse `- **Depende de:**` citando id sem item correspondente na árvore, e prosa no campo.

**Arquivos-alvo:** - `.claude/tools/backlog.py` - `tests/test_backlog.py`

**Verificação:** par presença-ausência sobre fixture — `check` acusa a violação sobre um plano cujo card cita em `Depende de:` um id que não é item (ex.: `` `DMC-1` ``), e **não** acusa sobre o mesmo plano com o campo em ids de tarefa; `python -m pytest tests/test_backlog.py` verde.

**Pronto quando:** a violação nova existe, é nomeada no vocabulário fechado do `check`, e o teste é par presença-ausência sobre corpus em que as duas leituras dariam resultados diferentes.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-24
- **Caso medido que motivou (2026-09-20):** `check` devolveu `check: OK — nenhuma violação` sobre a árvore em que as cinco tarefas do `P-0741` estavam inselecionáveis, e `next` devolveu `nada delegável — 0 elegível(is) · blocked 0`. O lint aprovou um plano que o seletor não consegue percorrer; o defeito só apareceu no gate de despacho, com a janela já aberta.
- **Não fazer:** não mexer em `_eh_elegivel` nem na semântica de `next` — o campo é lista de ids de item por gramática publicada (skill `diario-de-obras`, *Item e residência*); o que falta é o lint recusar quem desvia, não o seletor tolerar.
- **Notas de execução:** - 2026-09-24 `review` — C-12 no check (_depende_checks); 4 TF/TR em tests/test_backlog.py, 84 verdes. Arvore viva: 3 C-12 em itens done (TK-54a:1310 prosa + id "## TK-54"; TK-78c:3882 prosa) - fora dos alvos do card, reportados ao dono

## Execução

**Consumo:** 0 tool uses, 0.0 k tokens, 0.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: consumo do executor nao medido: execucao inline no contexto principal, sem notificacao de subagente (os zeros deste RDO sao ausencia de medida, nao medida zero); achado da arvore viva (3 C-12 em TK-54a e TK-78c) roteado ao TK-65d

## Laudo

**Veredito:** ressalva

**Percentual:** 94%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Registro da tarefa encaminhou o achado da arvore viva so como 'reportados ao dono', sem tiquete; verificacao dada como '84 verdes' em vez de exit code. Execucao inline deixa docs/telemetria.tsv sem linha medida para a tarefa.

## Fechamento

**Desdobramento:** aprovado com ressalva
