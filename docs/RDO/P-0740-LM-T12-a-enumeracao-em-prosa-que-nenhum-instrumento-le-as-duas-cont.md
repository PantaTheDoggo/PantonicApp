# RDO — P-0740 · LM-T12

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T12` — A enumeração em prosa que nenhum instrumento lê: as duas contagens do README e a `A3c` nas três listas do loop
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — fechar o invariante de contagem do `DM-18` (i) na metade que o instrumento **não** enxerga. A `LM-T11` publicou o vigésimo guardrail e deixou duas frases de prosa do `README.md` falsas com o guarda **verde**; e publicou a `A3c` na tabela do bloco A sem entrar nas três enumerações da própria skill que roteia por ela.

**Arquivos-alvo:** - `README.md` — as duas frases de contagem da seção *Os guardrails*. - `.claude/checks/check-readme.ps1` — o guarda passa a ler as duas frases. - `.claude/skills/scrum-master/SKILL.md` — as três enumerações que ignoram a `A3c`. - `CHANGELOG.md` — a linha do bloco não lançado.

**Verificação:** 1. ``` pwsh -NoProfile -Command "(Select-String -Path README.md -Pattern 'Vinte regras mínimas obrigatórias' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. 2. ``` pwsh -NoProfile -Command "(Select-String -Path README.md -Pattern 'Dezenove regras mínimas obrigatórias' -SimpleMatch | Measure-Object).Count" ``` → **0** (a frase falsa não sobrevive). **Medido antes: 1**. 3. ``` pwsh -NoProfile -Command "(Select-String -Path README.md -Pattern '**treze** dependem de gate de review' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. 4. ``` pwsh -NoProfile -Command "(Select-String -Path README.md -Pattern '**doze** dependem de gate de review' -SimpleMatch | Measure-Object).Count" ``` → **0**. **Medido antes: 1**. 5. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern 'regras mínimas obrigatórias' -SimpleMatch | Measure-Object).Count" ``` → **≥ 1**: o guarda passa a citar a frase que lê. **Medido antes: 0** — é este zero que mede o defeito, porque o invariante estava guardado só na metade que o script enxerga. 6. ``` pwsh -NoProfile -File .claude/checks/check-readme.ps1 ``` → **exit 0**, com a saída citando as frases conferidas. **Medido antes: exit 0** — veredito invariante (critério (xviii)); hoje ele sai verde **com as duas frases falsas**, e é por isso que este item sozinho não discrimina: quem discrimina são os itens de literal acima. 7. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'A3c' -SimpleMatch -CaseSensitive | Measure-Object).Count" ``` → **≥ 5**: a linha da tabela mais as quatro citações novas. **Medido antes: 1**. 8. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'chega **sempre** pelo' -SimpleMatch | Measure-Object).Count" ``` → **0**. **Medido antes: 1**. 9. ``` pwsh -NoProfile -Command "(Select-String -Path CHANGELOG.md -Pattern 'a enumeração em prosa entra no guarda' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. 10. ``` python -m pytest tests/ -q ``` → verde, **sem reduzir** o total re-medido no despacho (`DM-23`): esta tarefa não acrescenta teste. **Medido antes: exit 0** — veredito invariante (critério (xviii)); referência **datada**, e não aceite: `197 passed` em 2026-09-19.

**Pronto quando:** as duas frases do `README.md` dizem a verdade e o guarda as **lê**; a `A3c` aparece nas três enumerações da skill e o advérbio `sempre` saiu do bullet de parada; a linha do `CHANGELOG.md` existe; e as **dez** linhas de `Verificação` saem nos valores declarados.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` · 2026-09-19 — card novo do `ESC-29` (2026-09-19), **primeiro da fila restante**: o item (c) corrige a skill que **governa o loop enquanto ele roda**, e errar rota custa mais do que adiar a `LM-T4c`.
- **Esforço:** medium
- **Depende de:** nada. Nada depende desta.
- **Produto do módulo:** - **(a) As duas frases do `README.md`, com o literal exato.** A primeira linha de prosa da seção *Os guardrails* passa a ser, verbatim: `Vinte regras mínimas obrigatórias, válidas em todo projeto da família, sem exceção.` Na frase das três formas, **só** o numeral do meio muda: `**doze**` vira `**treze**`. O resto da frase — inclusive a oração *"uma delas soma as duas formas, e por isso aparece nas duas contagens"* — fica **literal**. Recontagem medida no `ESC-29` sobre a coluna *Como é enforceada* da própria tabela: **20** linhas, **7** com `Teste executável`, **13** com `Gate de review`, `Instrução de agente` ou `Gate de planejamento`, **1** com `Enforcement de permissão`, e **1** linha nas duas primeiras classes (a de número oito) — de modo que `teste + gate - ambos + permissão` fecha em **20**. - **(b) O guarda lê as duas frases.** `.claude/checks/check-readme.ps1` ganha, na checagem que já compara a tabela de guardrails com `GOVERNANCA.md` §7, duas conferências novas, **reusando o `$numeralMap` que o próprio script já tem** (por extenso até vinte): - a linha da seção que casa `regras mínimas obrigatórias` tem o numeral igual ao número de linhas da tabela (`$readmeGuardrailCount`); - a linha da seção que casa `regras falham como teste executável` tem os dois numerais iguais às contagens derivadas da coluna *Como é enforceada* pelos literais `Teste executável` e `Gate de review|Instrução de agente|Gate de planejamento`, e a identidade `teste + gate - ambos + permissão` fecha no total da tabela (`Enforcement de permissão` é o terceiro literal). Frase ausente, numeral fora do vocabulário ou divergência **falham** com mensagem que nomeia o número declarado e o medido, no mesmo formato das mensagens que o script já emite. A linha de sucesso do guarda passa a citar as frases conferidas. - **(c) A `A3c` nas três enumerações de `.claude/skills/scrum-master/SKILL.md`.** Literais: - no *Passo 8 — Roteamento, bloco A*, campo `Gatilho`: `regras A1..A3b` vira `regras A1..A3c`; - no *Relatório de encerramento*, primeiro bullet: `inclusive A6a e A8a` vira `inclusive A3c, A6a e A8a`; - na seção *O que obriga parada e o que segue com registro*, a `A3c` entra nos **dois** bullets, porque é a única regra do bloco A com desfecho **condicional**: em *Obriga parada*, como recusa de ferramenta **sem** fallback declarado; em *Segue com registro*, como recusa de ferramenta **com** fallback declarado, que redespacha a mesma tarefa sem consumir retentativa. No mesmo ato cai o advérbio **sempre** do bullet de parada — ele afirma que a escalada chega só pelo `pendencia=` ou pela recomendação `escalar`, e a `A3c` é o contraexemplo: ela nem despacha o `reviewer`, então não há laudo de onde a recomendação viesse. - **(d) A linha do `CHANGELOG.md`**, no bloco não lançado, contendo o literal `a enumeração em prosa entra no guarda`.
- **Restrições desta tarefa:** a tabela de guardrails do `README.md` **não** é reescrita — nenhuma linha entra, sai ou muda de coluna; o que muda é a prosa que a conta. A tabela do bloco A da skill também fica **intocada**: a `A3c` já está lá, e o defeito é das enumerações. Nenhum guardrail novo é criado. Nenhum card do plano é reescrito. `GOVERNANCA.md` §7 não é tocado: ele é a fonte, e está certo.
- **Não fazer:** não estender o guarda para outras seções do `README.md` (a classe é conhecida, mas o alvo deste card é a seção *Os guardrails*); não tocar `.claude/tools/card_check.py`; não criar fixture sintética de kit para provar o guarda (o `-Root` existe, e a prova do mundo sem a mudança são os itens de literal); não commitar.
- **Contingências:** 1. se a recontagem da coluna *Como é enforceada* der números diferentes de **7**, **13** e **1** no despacho (alguém mexeu na tabela) → **usar os números medidos no ato**, escrever a frase com eles e **reportar a divergência no retorno**: o aceite é a identidade `teste + gate - ambos + permissão = total`, não os três literais; 2. se `pwsh -NoProfile -File .claude/checks/check-readme.ps1` já sair **exit 1** antes de qualquer edição → parar e sinalizar `blocked` razão `premissa`, citando a saída: o guarda estaria quebrado por outra causa, e este card não a investiga.

## Execução

**Consumo:** 24 tool uses, 83.5 k tokens, 194.5 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

Guarda provado por mutacao fora do repo: com -Root sobre copia em TEMP (README, VERSION, GOVERNANCA.md, .claude/agents, .claude/skills, .claude/README.md, .claude/KIT_VERSION), cinco mutacoes independentes foram vistas falhar - 20->19 (declara 19 vs 20), numeral fora do vocabulario ('Cinquenta'), Sete->Oito (8 vs 7), treze->doze (12 vs 13) e frase das formas ausente - e a identidade 'teste + gate - ambos + permissao' foi vista falhar isolada ao crescer a tabela para 21 linhas (fecha em 20 vs 21). Recontagem independente da coluna 'Como e enforceada': Teste executavel = 7 (1-6, 8); gate/instrucao/planejamento = 13 (7-12, 14-20); permissao = 1 (13); ambos = 1 (8); 7+13-1+1 = 20 = linhas da tabela - os 7/13/1 do executor conferem sem divergencia, logo a contingencia 1 nao foi acionada. Limite conhecido, sem falso verde: o numeralMap vai so ate 'vinte'; na 21a regra a frase por extenso ('Vinte e um') sera lida como token 'Vinte' e o guarda falhara com mensagem '20 vs 21' - fail-closed, mas o remedio sera escrever o numeral em digito ou estender o mapa.

## Fechamento

**Desdobramento:** aprovado
