# RDO — P-0743 · DOM-T3a

**Plano:** `docs/plans/P-0743-modelo-de-dominio.md`
**Tarefa:** `DOM-T3a` — O que o instrumento e a gramática dizem de si mesmos
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** o texto em que `.claude/tools/modelo.py` se descreve — docstring do módulo e `--help` — e o preâmbulo da skill `diario-de-obras` que **nomeia** a subseção da gramática passam a descrever a forma nova, sem nenhum resíduo da forma anterior fora dos literais normativos de saída.

**Arquivos-alvo:** - `.claude/tools/modelo.py` — **arquivo inteiro**. As duas regiões abaixo são as únicas que mudam, mas o aceite é de coerência do módulo todo (`I-10`): (a) o docstring do módulo, da aspa tripla de abertura da linha 1 à de fechamento, 14 linhas medidas em 2026-09-20; (b) o argumento `description=(...)` do `argparse.ArgumentParser` dentro de `main()`, localizado por `grep -n 'description=(' .claude/tools/modelo.py` — linha 438 em 2026-09-20, e o número se re-deriva no despacho (`I-5`). - `.claude/skills/diario-de-obras/SKILL.md` — **arquivo inteiro**. Muda só o preâmbulo da seção `## Gramática legível por máquina`, localizado por conteúdo (o bloco de três linhas transcrito abaixo; linhas 134-136 em 2026-09-20).

**Verificação:** ``` grep -c 'oraç' .claude/tools/modelo.py ``` imprime `1` (hoje imprime `2`, medido 2026-09-20) — a única sobrevivente é a linha do literal normativo de saída de forma anterior. ``` grep -c "plano na forma de orações (sem '### 1.2 Fluxo de operações')" .claude/tools/modelo.py ``` imprime `1`, **inalterado** (hoje imprime `1`, medido 2026-09-20). ``` grep -c 'MC-T2' .claude/tools/modelo.py ``` imprime `0` (hoje imprime `2`, medido 2026-09-20). ``` grep -c 'P-0741' .claude/tools/modelo.py ``` imprime `0` (hoje imprime `1`, medido 2026-09-20). ``` grep -c '1\.1 Vocabulário' .claude/tools/modelo.py ``` imprime `0` (hoje imprime `1`, medido 2026-09-20). ``` grep -c 'V1\.\.V9' .claude/tools/modelo.py ``` imprime `0` (hoje imprime `1`, medido 2026-09-20). ``` grep -c 'V1\.\.V14' .claude/tools/modelo.py ``` imprime `1` (hoje imprime `0`, medido 2026-09-20). ``` python .claude/tools/modelo.py --help ``` sai `0`; a saída contém `V1..V14` e **não** contém `V1..V9`. ``` grep -c 'P-0741' .claude/skills/diario-de-obras/SKILL.md ``` imprime `0` (hoje imprime `1`, medido 2026-09-20). ``` grep -c 'Modelo conceitual (seção do plano)' .claude/skills/diario-de-obras/SKILL.md ``` imprime `0` (hoje imprime `1`, medido 2026-09-20). ``` grep -c 'P-0743' .claude/skills/diario-de-obras/SKILL.md ``` imprime `1` ou mais (hoje imprime `0`, medido 2026-09-20). ``` python .claude/tools/modelo.py check --plano docs/plans/P-0744-spec-do-planejador.md ``` sai `0` e imprime `modelo: OK — 3 operações, 4 objetos, 3 tarefas, 0 mudanças` — **inalterado** (hoje idem, medido 2026-09-20: este card não pode mexer neste resultado). ``` python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md ``` sai `2` e imprime `modelo: forma anterior — plano na forma de orações (sem '### 1.2 Fluxo de operações')` — **inalterado** (hoje idem, medido 2026-09-20). ``` python -m pytest tests -q ``` passa, com total **não menor** que o total re-medido no despacho. Referência datada: **249 em 2026-09-20**.

**Pronto quando:** os onze greps acima devolvem os números declarados, `--help` anuncia `V1..V14`, os dois `modelo.py check` devolvem exits e literais **inalterados**, a suíte inteira passa no piso da relação, e **nenhuma linha de `.claude/tools/modelo.py` ou de `.claude/skills/diario-de-obras/SKILL.md` descreve o modelo como orações numeradas com estado gravado** — exceto o literal normativo de saída que nomeia a forma anterior.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20
- **Depende de:** `DOM-T3`
- **Fundamento:** `D-14`, `D-16`; invariantes `I-1`, `I-3`, `I-10`; achados `AE-2` e `AE-5` desta execução. Card corretivo criado no escalonamento `ESC-1` (consultor de plano, 2026-09-20): a `DOM-T3` recortou `modelo.py` em quatro faixas de linhas e a `DOM-T2` confinou a edição da skill ao recorte da subseção; os dois recortes deixaram de fora o texto que **nomeia** a forma, e nenhum card restante o alcança.
- **Oração do modelo:** `M-1`, `M-5`, `M-6`, `M-7` - M-1: O modelo de um plano passa a descrever o que o plano entrega como objetos e operações encadeadas: cada objeto com o contrato que a implementação precisa, e cada operação nomeando quem age, o que faz e de que objetos precisa. - M-5: Um instrumento confere o modelo novo: toda operação tem tarefa, toda tarefa tem operação, todo objeto citado existe, a numeração é a ordem do encadeamento e nenhuma operação depende de objeto que só nasce depois dela. - M-6: O mesmo instrumento gera a leitura do dono, abrindo pelo estágio atual e mostrando o fluxo inteiro com o que já concluiu, o que está em curso e o que ainda não começou. - M-7: Planos escritos na forma anterior continuam legíveis e não bloqueiam nada: o instrumento os reconhece como forma anterior e segue.
- **Camada e fronteira:** ferramenta do kit (`.claude/tools/`) e skill do kit (`.claude/skills/`). Só texto de descrição: **nenhuma linha de comportamento muda**, nenhum literal de saída muda, nenhuma assinatura muda, nenhum teste vigente muda de resultado.
- **Contratos/classes:** nenhum. O card não cria, não remove e não renomeia símbolo algum.
- **Passos:** 1. Substituir o docstring do módulo de `.claude/tools/modelo.py` pelo literal acima, verbatim (`I-3`), preservando a linha `from __future__ import annotations` imediatamente abaixo dele. 2. Substituir o argumento `description=(...)` de `main()` pelo literal acima, verbatim, preservando a indentação e os parênteses que o arquivo já tem em volta. 3. Substituir as três linhas do preâmbulo de `SKILL.md` pelo literal acima, verbatim. 4. Varrer `.claude/tools/modelo.py` **inteiro** atrás de resíduo da forma anterior: `grep -n -e 'oraç' -e 'MC-T2' -e 'P-0741' -e 'V1\.\.V9' -e '1\.1 Vocabulário' .claude/tools/modelo.py`. **A única ocorrência que sobrevive** é a da linha do literal normativo de saída `modelo: forma anterior — plano na forma de orações (sem '### 1.2 Fluxo de operações')` (linha 84 em 2026-09-20). Qualquer outra ocorrência é resíduo e se corrige neste mesmo card, respeitada a contingência 1. 5. Varrer `.claude/skills/diario-de-obras/SKILL.md` **inteiro**: `grep -n -e 'Modelo conceitual' -e 'P-0741' .claude/skills/diario-de-obras/SKILL.md`. Toda ocorrência que **nomeie a subseção da gramática ou a residência dela** se corrige neste card, com o mesmo teor do literal acima; ocorrência que cite o `P-0741` como fato histórico de outro assunto fica como está. 6. Rodar as verificações abaixo.
- **Restrições desta tarefa:** - Nenhum literal de **saída** de `modelo.py` muda. Em particular, as duas mensagens de exit `2` e as quatorze substrings `V1`..`V14` ficam byte a byte como a `DOM-T3` as entregou — elas são a norma da §6 e estão afirmadas por teste. - Nenhuma linha de comportamento muda: nem `import`, nem expressão regular, nem função, nem dataclass, nem `_forcar_utf8`, nem o carregamento de `backlog.py` por `importlib` (`F-4`). - Não editar `.claude/tools/backlog.py`, `review_evidence.py` nem `card_check.py` (`I-1`). - Texto entra verbatim dos três blocos literais acima (`I-3`). - Piso de regressão é relação (`I-2`): este card **não remove nem acrescenta teste**; o total re-medido no despacho é o piso e a entrega o mantém. Referência datada: **249 em 2026-09-20**. - Nenhuma contingência deste card cria arquivo. Se alguma só puder ser cumprida criando arquivo não declarado nos `Arquivos-alvo`, o card está incompleto: sinalizar `blocked` razão `premissa` (`I-10`). - Não commitar (`I-6`).
- **Não fazer:** - Não tocar `docs/plans/P-0741-modelo-conceitual.md` nem nenhum outro plano do acervo (`D-3`). - Não reescrever a subseção `### Modelo de domínio (seção do plano)` de `SKILL.md`: ela é a entrega da `DOM-T2`, está aprovada, e este card conserta só o **preâmbulo que a nomeia**. - Não mexer em `tests/test_modelo.py` nem nas fixtures: o docstring de `tests/test_modelo.py` já foi corrigido pela `DOM-T3`. - Não tocar `README.md`, `.claude/README.md`, `GOVERNANCA.md` nem `docs/RUBRICA_DE_REVISAO.md`.
- **Contingências:** 1. Se o passo 4 encontrar resíduo em **linha de comportamento** (nome de símbolo, expressão regular, literal de saída) e não em texto de descrição → **não corrigir**: parar, sinalizar `blocked` razão `premissa` e devolver as linhas encontradas na linha de retorno. Resíduo em comportamento é defeito da `DOM-T3` e não cabe neste card. 2. Se o passo 5 encontrar em `SKILL.md` mais de uma frase que nomeie a subseção da gramática ou a residência dela → substituir **todas** pelo mesmo teor do literal acima e devolver na linha de retorno `contingência 2 acionada: <linhas corrigidas>` (`I-8`).
- **Testes:** nenhum teste novo — a entrega é texto de descrição, e a superfície de comportamento já está afirmada pelos dez testes da `DOM-T3`. A aferição são os greps de coerência abaixo, que discriminam a forma nova da anterior no **arquivo inteiro**, não só nas regiões editadas.
- **Fora do escopo desta tarefa:** o agente (`DOM-T4`), as definições de conduta (`DOM-T5`), a documentação pública e o `README.md` (`DOM-T6`), a subseção `### Modelo de domínio (seção do plano)` de `SKILL.md` (entrega da `DOM-T2`, aprovada) e qualquer edição em plano do acervo.

## Execução

**Consumo:** 16 tool uses, 58.0 k tokens, 87.2 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 94%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Modo de falha próprio da classe transcrição-verbatim: ao trocar um bloco inteiro por outro, um token do texto substituído sobreviveu (I-3 do docstring antigo ocupou o lugar de I-1 no novo), e nenhuma das onze linhas de aceite — todas contagens de ocorrência de resíduo — podia vê-lo, porque o token sobrevivente não era resíduo da forma anterior, era referência cruzada errada. Aceite por grep de resíduo é cego à fidelidade do literal; o que pega é o confronto do bloco entregue contra o bloco cercado do card.

## Fechamento

**Desdobramento:** aprovado com ressalva
