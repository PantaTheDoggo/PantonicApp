# RDO — P-0743 · DOM-T3b

**Plano:** `docs/plans/P-0743-modelo-de-dominio.md`
**Tarefa:** `DOM-T3b` — A referência cruzada do docstring
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** o docstring de `.claude/tools/modelo.py` idêntico, linha a linha, ao bloco cercado deste card — em particular apontando o invariante `I-1` do `P-0743`, que é o que a frase explica, e não o `I-3`.

**Arquivos-alvo:** - `.claude/tools/modelo.py` - só o docstring do módulo, da aspa tripla de abertura da linha 1 à de fechamento da linha 15 (medido 2026-09-20; os números se re-derivam no despacho, `I-5`)

**Verificação:** ``` grep -c 'I-3' .claude/tools/modelo.py ``` imprime `0` (hoje imprime `1`, na linha 14, medido 2026-09-20). ``` grep -n 'I-1' .claude/tools/modelo.py ``` imprime **exatamente uma** linha, a 14 (hoje não imprime nenhuma, medido 2026-09-20). ``` sed -n '1,15p' .claude/tools/modelo.py ``` sai idêntico, linha a linha, ao bloco cercado deste card (`I-11`). ``` python .claude/tools/modelo.py --help ``` sai `0`; a saída contém `V1..V14` — **inalterada** (hoje idem, medido 2026-09-20). ``` python .claude/tools/modelo.py check --plano docs/plans/P-0744-spec-do-planejador.md ``` sai `0` e imprime `modelo: OK — 3 operações, 4 objetos, 3 tarefas, 0 mudanças` — **inalterado**. ``` python -m pytest tests -q ``` passa, com total **não menor** que o re-medido no despacho. Referência datada: **249 em 2026-09-20**.

**Pronto quando:** `sed -n '1,15p' .claude/tools/modelo.py` é idêntico, linha a linha, ao bloco cercado deste card; `grep -c 'I-3'` imprime `0`; `--help` e os dois `check` seguem inalterados; a suíte passa no piso; e a linha de retorno traz a declaração de fidelidade do `I-11`.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20
- **Depende de:** `DOM-T3a`
- **Fundamento:** `D-18`; invariantes `I-3`, `I-11`, `I-12`; achado `AE-8`. Card corretivo criado no escalonamento `ESC-2` (consultor de plano, 2026-09-20): a `DOM-T3a` passou em 11/11 greps de aceite e ainda assim publicou `(I-3 do P-0743)` onde o bloco literal dela mandava `(I-1 do P-0743)` — token herdado do docstring substituído, invisível a aceite por contagem de resíduo. Nenhum card restante toca `.claude/tools/modelo.py`.
- **Oração do modelo:** `M-5`, `M-6`, `M-7` - M-5: Um instrumento confere o modelo novo: toda operação tem tarefa, toda tarefa tem operação, todo objeto citado existe, a numeração é a ordem do encadeamento e nenhuma operação depende de objeto que só nasce depois dela. - M-6: O mesmo instrumento gera a leitura do dono, abrindo pelo estágio atual e mostrando o fluxo inteiro com o que já concluiu, o que está em curso e o que ainda não começou. - M-7: Planos escritos na forma anterior continuam legíveis e não bloqueiam nada: o instrumento os reconhece como forma anterior e segue.
- **Camada e fronteira:** ferramenta do kit, em `.claude/tools/`. Um token de texto de descrição. Nenhuma linha de comportamento, nenhum literal de saída, nenhuma assinatura.
- **Contratos/classes:** nenhum.
- **Passos:** 1. Imprimir o docstring vigente com `sed -n '1,15p' .claude/tools/modelo.py` e confrontá-lo, linha a linha, com o bloco cercado acima. 2. Corrigir a única linha divergente, trocando `(\`I-3\` do` por `(\`I-1\` do`. Nenhuma outra linha do arquivo é tocada. 3. Repetir o passo 1 e devolver, na linha de retorno, `fidelidade conferida: docstring — 15 linhas idênticas ao bloco cercado da DOM-T3b` (`I-11`). 4. Rodar as verificações abaixo.
- **Restrições desta tarefa:** - Nenhuma linha fora do docstring muda. Em particular, o `description=(...)` de `main()` já está correto e **não** se toca. - Nenhum literal de saída de `modelo.py` muda (`I-3`). - Não editar `backlog.py`, `review_evidence.py` nem `card_check.py` (`I-1`). - Piso de regressão é relação (`I-2`): nenhum teste entra nem sai. Referência datada: **249 em 2026-09-20**. - Nenhuma contingência deste card cria arquivo (`I-10`). - Não commitar (`I-6`).
- **Não fazer:** - Não reescrever o docstring inteiro "por segurança": catorze das quinze linhas já estão certas, e reescrever é como o `AE-8` nasceu. - Não tocar `.claude/skills/diario-de-obras/SKILL.md`: a entrega da `DOM-T3a` ali está conforme. - Não tocar `README.md`, `.claude/README.md`, `GOVERNANCA.md` nem `docs/RUBRICA_DE_REVISAO.md`.
- **Contingências:** 1. Se o passo 1 encontrar **mais de uma** linha divergente do bloco cercado → corrigir todas no mesmo ato, pelo bloco cercado, e devolver `contingência 1 acionada: <linhas corrigidas>` (`I-8`).
- **Testes:** nenhum teste novo — a entrega é um token de texto de descrição.
- **Fora do escopo desta tarefa:** o agente (`DOM-T4`), as definições de conduta (`DOM-T5`), a documentação pública (`DOM-T6`), e qualquer outra linha de `.claude/tools/modelo.py`.

## Execução

**Consumo:** 9 tool uses, 49.1 k tokens, 69.5 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: fidelidade conferida: docstring — 15 linhas idênticas ao bloco cercado da DOM-T3b; conferida pelo revisor por md5sum (b6593ff55d30f7e62dfc07388d4c1c61) e diff -u sem saída

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

Primeiro exercício do I-11 (aceite de transcrição bloco contra bloco) e ele discrimina: md5sum do recorte bate com o do bloco cercado do card, diff -u sem uma linha de saída, e o confronto contra o retrato pré-entrega mostra exatamente um hunk — linha 14, I-3 para I-1. Nove turnos para um token: é o custo de um card corretivo que o aceite por contagem de ocorrências da DOM-T3a (11/11 verdes, AE-8) não teria evitado.

## Fechamento

**Desdobramento:** aprovado
