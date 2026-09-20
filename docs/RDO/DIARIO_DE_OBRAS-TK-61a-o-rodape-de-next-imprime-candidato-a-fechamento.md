# RDO — DIARIO_DE_OBRAS · TK-61a

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-61a` — O rodapé de `next` imprime candidato a fechamento
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** implementar a `DB-4` do `P-0739` na metade que falta — a expressão *candidato a fechamento* não existe em `.claude/tools/backlog.py` e o rodapé de `next` imprime só os três contadores mecânicos.

**Arquivos-alvo:** - `.claude/tools/backlog.py` - `tests/test_backlog.py` - `tests/fixtures/backlog/`

**Verificação:** `python .claude/tools/backlog.py next` sai **exit 0** e o rodapé traz **duas** linhas: a dos três contadores, **byte a byte como hoje**, e a nova, que sobre o corpus vivo imprime `candidato a fechamento: nenhum` (população medida em 2026-09-20: **zero**). `python .claude/tools/backlog.py check` exit 0; `python .claude/checks/dead_code.py` exit 0; `python -m pytest` verde, sem queda do piso de **236**.

**Pronto quando:** 1. **Definição, quatro cláusulas conjuntas.** Candidato a fechamento é pai (plano **ou** tíquete) que: (a) está no corpus da §2.0 (`DB-43`); (b) tem **>= 1 filho direto**; (c) tem **todos** os filhos diretos terminais — `done` ou `cancelled`, o vocabulário da §2.5 (`superseded` não entra: só plano o tem e plano não é filho); (d) **não é ele próprio terminal** (`done`/`cancelled`/`superseded`). **Medido em 2026-09-20, e é o que justifica (b) e (d):** sem (d) o rodapé carregaria **8** entradas permanentes, todas de pai já `done` (`TK-51`, `TK-53`, `TK-56`, `TK-57`, `TK-59`, `TK-60`, `TK-62`, `TK-64`); sem (b), mais **5** por verdade vacuosa, três delas de tíquete aberto sem subtarefa (`TK-38`, `TK-48`, `TK-55`). **A cláusula (d) é leitura declarada, não texto publicado:** a §2.5 não fala do status do pai. Ela deriva do enunciado do `DB-4` — o rodapé é lista de **decisão pendente**, e pai fechado não tem decisão pendente. Registrada assim para o dono poder derrubá-la sabendo o custo (as 8). 2. **Linha própria, e a linha dos três contadores não se toca.** A `DB-38` fixa aquela linha em *"três campos ... sempre os três"*: acrescentar um quarto campo contradiria norma publicada. O campo novo sai em **linha própria**, sob o mesmo `--- pendências mecânicas ---`, que é o *"uma linha cada"* do `DB-4`. Literal: `candidato a fechamento: <ID> (<done>/<total>), ...`, IDs em **ordem alfabética crescente** (`DB-37` E-1), `<done>/<total>` pela `DB-36`; sem população, o literal exato `candidato a fechamento: nenhum` (espelha `blocked: nenhum`). 3. **Mundo do teste: fixture, quatro casos.** Nada de aferir contra o diário vivo — ele muda por ato desta janela **e da outra janela de orquestração ativa**. A fixture traz: (i) pai vivo com >=1 filho, todos terminais → **aparece**; (ii) pai vivo com filho vivo → **não aparece**; (iii) pai já terminal com todos os filhos terminais → **não aparece**; (iv) pai com zero filhos → **não aparece**. Os quatro num corpus só, para que a asserção seja sobre a **linha inteira** e não sobre presença de substring. 4. **Regressão da linha antiga:** teste que afirma que a linha dos três contadores segue idêntica, com os três campos e os mesmos literais.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20 — **reescrito** no gate, antes do despacho: o aceite anterior citava `TK-51` e `TK-53` como casos vivos e ambos estão `done` desde então. Re-derivado em 2026-09-20 pelo instrumento, não por varredura.
- **Não fazer:** não alterar a linha `inbox de planos: ... · fila de memória: ... · blocked: ...`; não tocar `selecionar_next` nem a eleição de candidato a **despacho** (`_candidatos`, `_eh_elegivel`) — este card só acrescenta projeção de rodapé, não muda o que `next` elege; não aferir contra `docs/DIARIO_DE_OBRAS.md` nem contra `docs/plans/P-0741-modelo-conceitual.md`; não fechar nenhum pai (fechar é juízo do agente com o dono, que é o que a `DB-4` diz).

## Execução

**Consumo:** 37 tool uses, 95.1 k tokens, 255.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
