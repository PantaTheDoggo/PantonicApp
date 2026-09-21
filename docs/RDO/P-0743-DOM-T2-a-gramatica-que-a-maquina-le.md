# RDO — P-0743 · DOM-T2

**Plano:** `docs/plans/P-0743-modelo-de-dominio.md`
**Tarefa:** `DOM-T2` — A gramática que a máquina lê
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** a subseção `### Modelo conceitual (seção do plano)` da skill `diario-de-obras` substituída pela subseção `### Modelo de domínio (seção do plano)`, que é a gramática lida pelo instrumento.

**Arquivos-alvo:** - `.claude/skills/diario-de-obras/SKILL.md:175` (`### Modelo conceitual (seção do plano)`, até a linha imediatamente anterior a `## Formato de uma tarefa atômica`, hoje a 197)

**Verificação:** ``` grep -c 'Modelo de domínio (seção do plano)' .claude/skills/diario-de-obras/SKILL.md ``` imprime `1` (hoje imprime `0`). ``` grep -c 'Oração do modelo' .claude/skills/diario-de-obras/SKILL.md ``` imprime `0` (hoje imprime `1`, medido 2026-09-20). ``` grep -c 'Fluxo de operações' .claude/skills/diario-de-obras/SKILL.md ``` imprime `2` ou mais (hoje imprime `0`). `python .claude/tools/backlog.py check` imprime `check: OK — nenhuma violação.` e sai `0`.

**Pronto quando:** a subseção da skill é o bloco da §5 palavra por palavra, e nenhuma ocorrência de `Oração do modelo` resta na seção `## Gramática legível por máquina`.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20
- **Depende de:** `DOM-T1`
- **Fundamento:** `D-1`, `D-2`, `D-4`, `D-9`; fato `F-12`. O card transcreve o bloco cercado da §5 deste plano, residência única dele até a transcrição.
- **Oração do modelo:** `M-1`, `M-2`, `M-4` - M-1: O modelo de um plano passa a descrever o que o plano entrega como objetos e operações encadeadas: cada objeto com o contrato que a implementação precisa, e cada operação nomeando quem age, o que faz e de que objetos precisa. - M-2: O estado do modelo deixa de ser um status por frase e passa a ser uma posição no fluxo: o dono lê qual é o estágio atual, o que já ficou para trás e o que ainda vem. - M-4: Todo card de tarefa abre com o texto da operação que materializa e com o contrato dos objetos de que ela precisa, na mesma forma em todo plano.
- **Camada e fronteira:** skill de gramática. Nenhum código, nenhum teste.
- **Passos:** 1. Substituir a subseção inteira, do heading da linha 175 até a linha anterior ao heading `## Formato de uma tarefa atômica`, pelo bloco cercado `### Modelo de domínio (seção do plano)` da §5 deste plano, verbatim. 2. Percorrer a seção `## Gramática legível por máquina` inteira (a partir da linha 130) e trocar toda ocorrência de `Oração do modelo` por `Operação do modelo` e de `oração` por `operação` **dentro dessa seção apenas**. 3. Rodar as verificações abaixo.
- **Restrições desta tarefa:** - Texto entra verbatim do bloco cercado da §5 (`I-3`). - A troca do passo 2 é confinada à seção `## Gramática legível por máquina`; nenhuma outra seção do arquivo é tocada. - Não commitar (`I-6`).
- **Não fazer:** - Não tocar `GOVERNANCA.md` nem a rubrica: a `DOM-T1` já os fechou. - Não tocar `.claude/tools/modelo.py`: a gramática é texto; o instrumento é a `DOM-T3`. - Não alterar `### Inbox de planos` nem `## Formato de uma tarefa atômica`.
- **Contingências:** 1. Se a linha 175 não for `### Modelo conceitual (seção do plano)` → localizar o heading pelo texto exato com `grep -n`; se não existir no arquivo, parar e sinalizar `blocked` razão `premissa`. 2. Se o passo 2 encontrar ocorrência de `Oração do modelo` **fora** da seção `## Gramática legível por máquina` → deixar como está e registrar a ocorrência na linha de retorno como `contingência 2 acionada: <arquivo:linha>`.
- **Testes:** nenhum teste automatizado — a entrega é gramática em texto. A aferição é a verificação abaixo.
- **Fora do escopo desta tarefa:** o instrumento (`DOM-T3`), o agente (`DOM-T4`), a anatomia do card na definição do planejador (`DOM-T5`).

## Execução

**Consumo:** 5 tool uses, 60.5 k tokens, 107.7 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

Transcrição verbatim de bloco cercado com residência única declarada na origem é a classe mais barata da janela (5 tool uses, 60,5k): o executor não decide nada e o aceite é re-derivável por grep. O contraste a reter: a mesma economia produz o único defeito da entrega — card que renomeia uma coisa e confina a edição a um recorte deixa, por construção, toda referência externa àquele nome apontando para o vazio. Renomear é sempre tarefa de duas pontas.

## Fechamento

**Desdobramento:** aprovado
