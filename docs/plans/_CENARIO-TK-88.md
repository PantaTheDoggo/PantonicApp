# Cenário do TK-88 — autoridade sobre o tíquete para o que cobre

Teto: 15k tokens. Escrito só pelo `pantonic-consultant`, com `Edit` mínimo, a cada acionamento. Residência do tíquete: `docs/DIARIO_DE_OBRAS.md`, `## TK-88` (tíquete avulso, sem modelo de domínio: nenhum dossiê `Ato de modelo` cabe aqui). Dependentes fora do tíquete: o fechamento do `P-0751` (16/16) e a `FPU-T7` do `P-0752` (`Depende de: TK-88a`; I-4 daquele plano), com a `FPU-T10` atrás dela.

## Decisões vivas

- `CT-1`..`CT-4` (acionamento 1, gatilho 2, `B1` sobre o laudo da `TK-88a`, `ressalva 85`, bloqueante nenhuma, recomendação `escalar`): `rota=resolve`, sem `estrategico=`. Texto no `## TK-88`, parágrafo *Triagem do consultor*.
  - `CT-1` pendência do laudo → `TK-88c` (painel lê cada argumento na própria invocação; `rdo.py close` grava `**Plano:**` em barra normal; RDO publicadas corrigidas por regra, em todo `docs/**/*.md`). Não se reconstrói a `M-10` perdida; `progresso.txt` (fora do git) não se reescreve. Até o `TK-88c`: `encerrar.py` sozinho na linha de comando, sem nome de instrumento em texto de argumento.
  - `CT-2` fechamento sem medida → `TK-88b` (`--nao-medido "<razão>"` em `encerrar.py tarefa` e `rdo.py close`; recusa quando a série já mede a tarefa; hook `SubagentStop` só do `pantonic-executor`; sai da série a linha `TK-88a`/`usage` 60/186.4/464.1, que é a rodada do revisor — repete a `TK-88a-revisao` seguinte, 60/186.4/464.3; doutrina em `GOVERNANCA.md` §4.2, `scrum-master` Passo 9, `passagem-de-bastao` Parte 3).
  - `CT-3` execução fora do loop (evidência sem `--desde`) → doutrina da `TK-88b` (ref antes da primeira edição, `card_check --gravar`, `tarefa-corrente.json` só no despacho do executor).
  - `CT-4` pré-checagens duplicadas → `TK-88d` (`rdo.checar_close`, `backlog.checar_transicao`; linha `FECHADO` como o índice; stdout em gênero). Descartado declarar a duplicação: a `FECHADO` 1/2 contra o índice 1/1 já é a cópia divergindo.
- Diretiva reescrita por `backlog.py diretiva`: `TK-88` e `P-0752` antes do ` — ` (a diretiva só com `P-0752` deixava `next` em "nada delegável", porque `FPU-T7` espera a `TK-88a`). Ticket `TK-88` passou `review → in-progress` (pai em `review` tira os filhos da elegibilidade).
- Medido na árvore em 2026-09-26: `card_check` exit `0` em `TK-88b`, `TK-88c`, `TK-88d` e `FPU-T7` (inalterada); `backlog.py check` exit `0`; `next` → `TK-88b`; suíte `420 passed`. Depois das Verificações 2-3 do `TK-88c` ensaiado em cópia de `docs/` (regra aplicada, 16 arquivos): `False`/`False`.

## Fila

- `TK-88b` (`ready`) → **condutor fecha a `TK-88a`** pelo comando da nota dela (bloco cercado, com `--nao-medido` e três `--achado` roteados a `TK-88b`/`TK-88c`/`TK-88d`) → `TK-88c` (`ready`, depende de `TK-88b`) → `TK-88d` (`ready`, depende de `TK-88b`, `TK-88c`). Com a `TK-88a` `done`: a `FPU-T7` fica elegível e o `P-0751` pode fechar (`encerrar.py plano`, veredito do dono).

## Achados abertos

- Os três achados de processo e a pendência do laudo entram como `AE-<n>` no fechamento da `TK-88a` (os `--achado` do comando), já com rota; fecham com os corretivos.

## Matéria inconclusiva

- As RDO fechadas sob o defeito do painel ficam sem a própria linha `M-10` no `# Histórico` (decisão: omissão, não se reconstrói).
- Linhas `FECHADO` já publicadas no diário com contagem que inclui `cancelled` no total não se reescrevem (convenção divergente, não afirmação falsa).
- `FPU-T7` (duplicata na série) e `TK-88b` (linha `nao_medido`) convivem: duas linhas `nao_medido` da mesma tarefa com o mesmo modelo seriam recusadas pela regra da `FPU-T7` — só importa se alguém fechar a mesma tarefa duas vezes, o que o `encerrar.py` já recusa.
