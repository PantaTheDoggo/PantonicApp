# RDO — P-0749 · SAN-T6a

**Plano:** `docs/plans/P-0749-saneamento-artefatos.md`
**Tarefa:** `SAN-T6a` — O glossário diz o contador como a regra o diz
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Corretivo da `SAN-T6` (`AE-5` (b)): no glossário do `README.md`, o item *Plano `P-<n>`* deixa de chamar o contador de "global" e passa a dizê-lo como o item 1 do `G-PLANREADY` (`M4`) e `GOVERNANCA.md` §7 item 11: contador monotônico do repositório.

**Arquivos-alvo:** - `README.md`

**Verificação:** 1. ``` pwsh -NoProfile -File .claude/checks/check-readme.ps1 ``` → **exit 0, com a linha que começa por `check-readme: OK - 10 agente(s), 11 skill(s), 20 guardrail(s)`**. **Medido antes: exit 0, a mesma linha** (2026-09-25; e com `M5` aplicado numa cópia, `-Root` em `$env:TEMP`). 2. ``` pwsh -NoProfile -Command '(@(foreach ($p in "contador global monot","identificado por contador monotônico do repositório") { @(Select-String -LiteralPath README.md -SimpleMatch -Pattern $p).Count })) -join " / "' ``` → **0 / 1**. **Medido antes: 1 / 0** (2026-09-25; `0 / 1` com `M5` aplicado numa cópia). 3. ``` python -m pytest tests -q ``` → **o total do despacho, nenhuma falha**. **Medido antes: 353 passed** (2026-09-25).

**Pronto quando:** - kit.porta de entrada — descreve pasta por plano, tabela de estado e a regra do texto mínimo — Verificação 1, 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Fundamento:** DSA-23, DSA-3; I-5; `AE-5`.
- **Depende de:** `SAN-T6`
- **Operação do modelo:** `OP-6` - OP-6: O mantenedor da porta de entrada do repositório reescreve a descrição pública do kit: pasta por plano, tabela de estado e artefato de humano mínimo. - precisa de: kit — Quem implementa recebe essas ferramentas e esses textos. O que já está gravado continua sendo lido como hoje.; plano novo — Quem implementa não o escreve. A forma com que ele nasce mostra se o kit mudou.
- **Camada e fronteira:** só o `README.md`, uma linha do glossário (a linha 159 em 2026-09-25).
- **Passos:** 1. Rodar a Verificação 1 e 2 e conferir os valores "antes". 2. Aplicar `M5` com `Edit`. 3. Rodar a Verificação 1 a 3. 4. Devolver ao chamador a troca aplicada: o veredito do dono sobre `M5` sobe com o de `M1`..`M4` no relatório de encerramento (DSA-23) e não é critério desta revisão.
- **Restrições desta tarefa:** I-5; as contagens que o `README.md` anuncia não mudam.
- **Não fazer:** não refluir o parágrafo; não editar outra linha do `README.md`; não tocar `GOVERNANCA.md` nem a doutrina.
- **Contingências:** 1. se o texto antigo não aparecer exatamente uma vez → parar e sinalizar `blocked` razão `dependencia`, devolvendo a contagem.
- **Testes:** nenhum novo; guarda `check-readme.ps1`.
- **Fora do escopo desta tarefa:** qualquer outra linha do `README.md`; a régua de autoria (`AE-5` (a) e (c), `TK-72`).

## Execução

**Consumo:** 11 tool uses, 47.1 k tokens, 59.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: nenhuma; achado de processo (README.md:1045 ainda diz contador sequencial global) com rota em AE-6 do P-0749

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
