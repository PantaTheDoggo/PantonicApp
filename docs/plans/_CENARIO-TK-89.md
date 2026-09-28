# Cenário do TK-89 — autoridade sobre o tíquete para o que cobre

Teto: 15k tokens. Escrito só pelo `pantonic-consultant`, com `Edit` mínimo, a cada acionamento. Residência do tíquete: `docs/DIARIO_DE_OBRAS.md`, `## TK-89` (tíquete avulso, sem modelo de domínio: nenhum dossiê `Ato de modelo` cabe aqui). Origem: consultor do `P-0752`, acionamento 6 (`DFP-18`), achados `AE-38`, `AE-40`, `AE-41` do laudo da `FPU-T2`. Diretiva do dono vigente (2026-09-26): nenhum card nem tíquete novo por ajuste — achado novo vira `AE-<n>` com rota "auditoria final"; o tíquete fecha pelo condutor.

## Decisões vivas

- `CT89-1` (acionamento 1, gatilho 1, `TK-89a` `blocked` premissa pela contingência do próprio card): `rota=resolve`, sem `estrategico=`. A parada procede — defeito de autoria do card (o protótipo do consultor do `P-0752` mediu o acervo de cards, não a suíte). O corte `_LITERAL_APOS_ANCORA_RE.sub(r"\1", texto)` fica antes da varredura, para alvos **e** descartados (Objetivo do card: o literal da âncora não vai aos descartados, `DFP-16`). O único teste que cai, `test_tr_extrair_literais_nao_caminho_lista_o_descartado`, troca a entrada `rdo.py:79` por `rdo.py` (sem linha: deixa de ser âncora, o `re.compile` segue literal não caminho da `DB-27`); `assert` intactos; o teste irmão `test_tf_extrair_arquivos_alvo_aceita_arquivo_de_raiz_e_recusa_literal_de_regex` não muda. Descartado: cortar só na lista de alvos (descartados lidos do texto sem corte voltam a desalinhar na crase escapada — o defeito do item (1)); cancelar o card (o reparo cabe no card existente).
  - Medido em 2026-09-26 (protótipo na árvore, revertido; arquivos conferidos de volta): `tests/test_review_evidence.py` 55 passed; suíte 442 passed; `FPU-T2` 5 alvos, 0 descartados; campo do TF → `(['a/b.md', 'c/d.py'], [])`.
  - Card emendado: linha *Teste existente que muda*, Verificação 4, *Não fazer* e contingência reescrita. `card_check` OK; `backlog.py check` exit 0; `TK-89a` `ready`; `next` → `TK-89a`.

- `CT89-2` (acionamento 2, gatilho 3, gate `card_check` do passo 3 recusa o `TK-89b`, 2 itens "literal fora da linha"): `rota=resolve`, sem `estrategico=`. Âncora deslocada, não texto mudado: o `TK-88b` e o `TK-88c` desta janela somaram linhas ao `scrum-master` e a linha `B3` passou de `:283` a `:285`, texto intacto; `:62` e `RUBRICA_DE_REVISAO.md:341` seguem com o literal. Reparo: `:283` → `:285` no Arquivos-alvo e no Passo 2 do card (`docs/DIARIO_DE_OBRAS.md`), nada mais. Medido: `card_check --tarefa TK-89b` exit 0; `backlog.py check` exit 0; `next` → `TK-89b`. Descartado: card novo (diretiva do dono de 2026-09-26).

## Fila

- `TK-89a` `done` → `TK-89b` (`ready`, âncora reancorada em `CT89-2`). Com o `TK-89b` `done`, o condutor fecha o `TK-89`.

## Achados abertos

- Nenhum.

## Matéria inconclusiva

- Nenhuma.
