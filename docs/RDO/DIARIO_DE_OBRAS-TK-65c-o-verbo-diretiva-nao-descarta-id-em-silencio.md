# RDO — DIARIO_DE_OBRAS · TK-65c

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-65c` — O verbo `diretiva` não descarta id em silêncio
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `diretiva` passa a **acusar** — escreve a linha e avisa, exit 0 — o texto em que há id de item entre crases **depois** do ` — `, que o `next` não lê; o aviso diz quantos ids reconheceu antes do ` — ` e nomeia cada id descartado. Recusar a escrita está fora: a diretiva viva do dono (linha 2 do diário, 2026-09-24) usa a cauda de propósito para a sequência completa, e medida em 2026-09-24 ela tem 3 ids reconhecidos e 19 ids de item na cauda — recusar a tornaria ingravável.

**Arquivos-alvo:** - `.claude/tools/backlog.py` (`transacionar_diretiva`, `:1474`; `_parse_diretiva`, `:351`, só leitura) - `tests/test_backlog.py`

**Verificação:** par presença-ausência por `transacionar_diretiva` sobre fixture cuja árvore tem os ids citados — diretiva ``Priorize `A` — e depois `B`, `C` `` (os três ids de item): `exit_code == 0`, a linha é escrita, e `mensagem` contém `B` e `C` e a contagem 1 de reconhecidos; diretiva ``Priorize `A` — texto com `done` `` : `mensagem` idêntica à de hoje para a mesma árvore (nenhum aviso de descarte). `python -m pytest tests/test_backlog.py` verde (86 passed em 2026-09-24).

**Pronto quando:** `transacionar_diretiva` segue escrevendo e saindo `exit_code 0` em toda forma; com id descartado, o aviso nomeia cada um e a contagem de reconhecidos, e chega ao console pela via que `main()` já usa (`print(resultado.mensagem)`, `:1706`), concatenado por quebra de linha ao aviso de `_regenerar_bloco_fila` quando os dois existem; sem id descartado, `mensagem` é a de hoje; o conjunto que `_parse_diretiva` devolve não muda; o teste é par presença-ausência sobre as duas formas.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-24 — ramo acusar/recusar fechado em **acusar** pelo consultor (acionamento 2 do `TK-65`, `CT65-2`).
- **Id descartado, definição única:** texto entre crases na cauda (depois do primeiro ` — `) que está em `_ids_da_arvore(modelo)` (`:518`) e **não** está entre os ids que `_parse_diretiva` devolve; sem repetição, na ordem em que aparece. Crase que não é id de item (`done`, `next`, nome de arquivo) não é descartado e não entra no aviso.
- **Caso medido que motivou (2026-09-20):** `_parse_diretiva` sobre ``**Diretiva de priorização:** Priorize `P-0741` — e depois `TK-57`, `TK-56` `` devolve `['P-0741']`: os tíquetes que a própria diretiva do dono manda priorizar saem da fila sem aviso. Na janela do `P-0741` isso produziu uma fila filtrada a um único item e uma inversão de prioridade que só a leitura do código explicou.
- **Não fazer:** não passar a colher ids da cauda livre — a cauda é para humanos por gramática publicada (skill `diario-de-obras`, *Cabeçalho do diário*); o reparo é tornar o descarte **audível**, não mudar o que o campo significa.

## Execução

**Consumo:** 36 tool uses, 80.5 k tokens, 177.8 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: consumo acima e do redespacho; o 1o despacho devolveu blocked premissa sem editar (7 tool uses, 56.7k, 88.8s, telemetria TK-65c) e o consultor fechou o ramo em acusar (CT65-2)

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

Com o card fechado em ACUSAR, a entrega saiu em um passe so. Exercicio ponta a ponta com a diretiva viva do dono: 3 ids reconhecidos e 19 descartados, sem repetir. Achados roteados: nao rastreados no dossie -> TK-55; ramo concatenado sem teste -> TK-65e; check fora da bateria de guardas -> pendencia ao dono, saneamento do corpus -> TK-65d.

## Fechamento

**Desdobramento:** aprovado
