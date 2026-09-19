# RDO — P-0740 · LM-T14

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T14` — A superfície do próprio guarda: a enumeração que ele não fechou e o numeral que para em vinte
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — fechar, em `.claude/checks/check-readme.ps1`, os dois resíduos que a `LM-T12` deixou **no próprio arquivo que ela estendeu**: (a) a enumeração em prosa do `.SYNOPSIS`/`.DESCRIPTION` segue dizendo *"qualquer uma das 5 checagens mecânicas abaixo"* e listando `1..5`, sem a checagem `4b` que a `LM-T12` acrescentou — o card que fecha a classe reproduziu a classe (`AE-52`); (b) o `$numeralMap` vai só até `vinte` e a captura do numeral é de **um token** (`^(\S+) regras`), de modo que na vigésima primeira regra a frase por extenso (*"Vinte e uma regras mínimas obrigatórias"*) é lida como `Vinte` e o guarda falha com `20 vs 21`. É **fail-closed** — não há falso verde, e isso foi medido —, mas a mensagem acusa divergência onde há vocabulário curto.

**Arquivos-alvo:** - `.claude/checks/check-readme.ps1` — o bloco de documentação e o vocabulário de numerais. - `CHANGELOG.md` — a linha do bloco não lançado.

**Verificação:** 1. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern 'das 6 checagens mecânicas' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. 2. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern 'das 5 checagens mecânicas' -SimpleMatch | Measure-Object).Count" ``` → **0** (a contagem falsa não sobrevive). **Medido antes: 1**. 3. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern 'As duas frases de contagem em prosa' -SimpleMatch | Measure-Object).Count" ``` → **1**: o item novo da enumeração. **Medido antes: 0**. 4. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern 'vinte e uma' -SimpleMatch | Measure-Object).Count" ``` → **≥ 1**: o mapa passou de vinte, com a forma feminina. **Medido antes: 0**. 5. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern '^(.+?) regras mínimas obrigatórias' -SimpleMatch | Measure-Object).Count" ``` → **1**: a captura aceita a forma composta. **Medido antes: 0**. 6. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern '^(\S+) regras mínimas obrigatórias' -SimpleMatch | Measure-Object).Count" ``` → **0**: a captura de um token não sobrevive. **Medido antes: 1**. 7. ``` pwsh -NoProfile -Command "(Select-String -Path CHANGELOG.md -Pattern 'o guarda passa a contar acima de vinte' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. 8. ``` pwsh -NoProfile -File .claude/checks/check-readme.ps1 ``` → **exit 0** sobre o repo real, com a seção *Os guardrails* ainda em vinte regras: a mudança do vocabulário **não** altera o veredito de hoje. **Medido antes: exit 0** — veredito invariante (critério (xviii)). 9. ``` python -m pytest tests/ -q ``` → verde, **sem reduzir** o total re-medido no despacho (`DM-23`): esta tarefa não acrescenta teste. **Medido antes: exit 0** — veredito invariante; referência **datada**, e não aceite: `197 passed` em 2026-09-19.

**Pronto quando:** a enumeração do script diz **seis** e descreve a checagem das duas frases; o vocabulário passa de vinte com a forma composta capturada; a prova por mutação saiu nos dois sentidos; a linha do `CHANGELOG.md` existe; e as **nove** linhas de `Verificação` saem nos valores declarados.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` · 2026-09-19 — card novo do `ESC-30` (2026-09-19), veículo declarado do `AE-52` e do limite medido do `$numeralMap`. Não depende de nada e nada depende dela.
- **Esforço:** low
- **Depende de:** nada.
- **Produto do módulo:** - **(a) A enumeração fechada no mesmo ato.** O literal `das 5 checagens mecânicas` vira `das 6 checagens mecânicas`, e a lista `1..5` ganha o item `6.`, cuja primeira oração é, verbatim: `As duas frases de contagem em prosa da seção "Os guardrails"` — seguida da descrição do que a checagem confere: o numeral da frase de regras mínimas obrigatórias igual ao número de linhas da tabela, e os numerais da frase das três formas iguais às contagens derivadas da coluna *Como é enforceada*, com a identidade `teste + gate - ambos + permissão` fechando no total. O item registra que, no corpo do script, ela vive no bloco rotulado `4b`, por adjacência com a checagem de guardrails, e que a numeração da prosa conta **checagens**, não rótulos. - **(b) O numeral deixa de parar em vinte.** Duas mudanças, juntas, porque uma sem a outra não resolve: a captura do numeral da frase de regras passa de `^(\S+) regras mínimas obrigatórias` para `^(.+?) regras mínimas obrigatórias` (forma composta é mais de um token), e o `$numeralMap` ganha as entradas de `vinte e um` a `trinta`, **incluindo as formas femininas** de um e dois (`vinte e uma`, `vinte e duas`), já que a frase concorda com *regras*. O ramo de dígito (`^\d+$`) e o `ToLower()` que o script já aplica ficam como estão, e a mensagem de vocabulário passa a dizer até onde o mapa vai. - **(c) A linha do `CHANGELOG.md`**, no bloco não lançado, contendo o literal `o guarda passa a contar acima de vinte`.
- **Restrições desta tarefa:** nenhuma **checagem** muda de comportamento sobre o repo de hoje — o que muda é a documentação do script e o vocabulário de numerais. A frase do `README.md` **não** é tocada (ela está certa: são vinte). `GOVERNANCA.md` §7 não é tocado no repo real. A checagem de *Anatomia do kit*, que compartilha o `$numeralMap`, não muda de contrato: ela só passa a aceitar mais numerais. Nenhum card do plano é reescrito.
- **Não fazer:** não renumerar as checagens do corpo do script (o rótulo `4b` fica); não estender o guarda a outras seções do `README.md`; não trocar a frase por extenso por dígito no `README.md`; não commitar.
- **Contingências:** 1. se `pwsh -NoProfile -File .claude/checks/check-readme.ps1` já sair **exit 1** antes de qualquer edição → parar e sinalizar `blocked` razão `premissa`, citando a saída; 2. se a prova por mutação **não** sair `exit 0` com a forma composta depois da mudança → **parar**: a captura ou o mapa estariam errados, e publicar o guarda assim seria falso verde sobre a própria correção.

## Execução

**Consumo:** 44 tool uses, 89.6 k tokens, 337.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: Card de regularizacao do check-readme.ps1: tres das quatro mensagens de vocabulario ainda anunciam 'por extenso ate vinte' contra um numeralMap que vai a trinta, e as duas capturas de numeral irmas seguem de um token - a classe AE-52 reincide na primeira frase composta fora da de regras.

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

As nove linhas de Verificacao sairam todas nos valores declarados e o guarda segue exit 0 sobre o repo real; a divergencia interna do modulo nao aparece em nenhuma delas. Ela so apareceu no exercicio ponta a ponta sobre copia em TEMP: a prova por mutacao nos dois sentidos (exit 0 com 'Vinte e uma regras' sobre tabela de 21 linhas; exit 1 citando 20 e 21 ao reverter a frase) confirmou a metade correta, e o probe seguinte - numeral composto na frase irma do mesmo bloco 4b - expos a mensagem que ficou para tras. Licao de autoria: linha de aceite por literal ('das 6 checagens', 'vinte e uma') prova presenca, nunca coerencia entre irmaos do mesmo bloco; o aceite de coerencia do modulo (DM-3) precisa de um comando que rode o caminho completo, nao de mais um Select-String. O fail-closed foi preservado em todos os mundos testados: nenhum falso verde.

## Fechamento

**Desdobramento:** aprovado com ressalva
