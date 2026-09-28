# Cenário do TK-78 — autoridade sobre o tíquete para o que cobre

Teto: 15k tokens. Escrito só pelo `pantonic-consultant`, com `Edit` mínimo, a cada acionamento. Residência do tíquete: `docs/DIARIO_DE_OBRAS.md`, `## TK-78` (tíquete avulso, sem modelo de domínio: nenhum dossiê `Ato de modelo` cabe aqui).

## Decisões vivas

- Semântica vinculante (adendo do dono de 2026-09-24, verbatim no cabeçalho do `## TK-78`): modelo ativo **acima** do indicado segue e anota a divergência em uma linha; **abaixo** do indicado para e pede ao dono o `/model` do melhor. Vale para as cinco superfícies do gate: `scrum-master` passo 1, `modelo-por-fase`, `GOVERNANCA.md` §3 (linha *Orquestração* e bullet *Gatilho operacional*), `README.md` §4 e o hook `_NUDGE["execution"]`.
- `CT-1` (acionamento 1, gatilho 2, `B1` sobre `AE-1`): `rota=resolve`, sem `estrategico=`. `TK-78a` fica `done`; o que ela não cobriu vira o corretivo `TK-78d` (letra nova porque `backlog.py` só lê `TK-\d+[a-z]`; `TK-78a1` não parseia), posicionado no arquivo antes da `TK-78b`, que passa a depender de `TK-78a` e `TK-78d`. Literais re-medidos na árvore em 2026-09-24; cada **depois** da Verificação medido sobre cópia com as três substituições aplicadas (script temporário, já descartado); `check-drift`, `check-readme` exit `0`; suíte `277 passed`; nenhum teste prende os literais trocados. `backlog.py check` exit `0`; `next` → `TK-78d`.

## Fila

- `TK-78d` (`ready`) → `TK-78b` (`ready`, depende de `TK-78a`, `TK-78d`) → `TK-78c` (`ready`, depende de `TK-78a`; posição no arquivo a põe depois da `TK-78b`). Fechado o `TK-78`, a diretiva volta ao `P-0748`.

## Achados abertos

- `AE-1`: absorvido por `TK-78d` (ponteiro no próprio achado); fecha quando a `TK-78d` fechar.
- `AE-2`: `modelo.py check --plano TK-78` quebra com `FileNotFoundError` em alvo de tíquete — rota já dada pelo loop (`TK-66`/`TK-74`), fora deste acionamento.

## Matéria inconclusiva

- As `systemMessage` do hook (`considere /model sonnet`, `Considere /model haiku`) sugerem ao dono o rebaixamento sem mandar parar; a `TK-78a` proibiu tocá-las e a `TK-78d` as deixa fora do escopo. Se o dono ler isso como ruído, é matéria de card novo, não desta fila.
- `modelo-por-fase/SKILL.md:16` ("institucionaliza a *parada* e o *pedido explícito*") ficou literal; lido com o *Gate de subida* logo abaixo, não manda rebaixar — não entrou no corretivo.
