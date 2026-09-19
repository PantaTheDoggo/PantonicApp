# RDO — P-0740 · LM-T15

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T15` — O vocabulário do guarda, nos quatro sítios: aceite por ausência, não por presença
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — deixar as **quatro** conferências de numeral do `.claude/checks/check-readme.ps1` coerentes entre si. A `LM-T14` estendeu o `$numeralMap` até `trinta` e consertou **uma** captura e **uma** mensagem; as irmãs ficaram para trás, e o guarda hoje **recusa** um numeral que está no próprio mapa.

**Arquivos-alvo:** - `.claude/checks/check-readme.ps1` - `CHANGELOG.md` — a linha do bloco não lançado.

**Verificação:** (a forma deste bloco é o produto do `ESC-32`: cada troca de literal vai em **par** — presença do novo **e ausência do velho, contada no arquivo inteiro**. A ausência é o que cobre os irmãos; a presença sozinha foi o que deixou passar o `AE-52` e o `AE-57`.) 1. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern 'por extenso até vinte' -SimpleMatch | Measure-Object).Count" ``` → **0**: nenhum sítio sobra anunciando o teto antigo. **Medido antes: 3**. 2. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern 'por extenso até trinta' -SimpleMatch | Measure-Object).Count" ``` → **4**: os quatro sítios anunciam o mesmo teto. **Medido antes: 1**. 3. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern '(\S+) agentes' -SimpleMatch | Measure-Object).Count" ``` → **0**. **Medido antes: 1**. 4. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern '(\S+) skills' -SimpleMatch | Measure-Object).Count" ``` → **0**. **Medido antes: 1**. 5. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern '\*\*(\S+)\*\* regras falham' -SimpleMatch | Measure-Object).Count" ``` → **0**. **Medido antes: 1**. 6. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern 'falham como teste executável, \*\*(\S+)\*\* dependem' -SimpleMatch | Measure-Object).Count" ``` → **0**. **Medido antes: 1**. 7. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/checks/check-readme.ps1 -Pattern '^O kit são (.+?) agentes' -SimpleMatch | Measure-Object).Count" ``` → **1**: a captura nova, ancorada. **Medido antes: 0**. 8. ``` pwsh -NoProfile -Command "(Select-String -Path CHANGELOG.md -Pattern 'o vocabulário do guarda fica coerente entre os quatro sítios' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. 9. ``` pwsh -NoProfile -File .claude/checks/check-readme.ps1 ``` → **exit 0** sobre o repo real, **inalterado**: as contagens de hoje (nove agentes, dez skills, vinte regras, sete/treze/uma) continuam conferindo. **Medido antes: exit 0** — veredito invariante (critério (xviii)). 10. ``` python -m pytest tests/ -q ``` → verde, **sem reduzir** o total re-medido no despacho (`DM-23`): esta tarefa não acrescenta teste. **Medido antes: exit 0** — veredito invariante; referência **datada**, e não aceite: `201 passed` em 2026-09-19.

**Pronto quando:** as quatro capturas aceitam numeral composto com âncora provada, as quatro mensagens anunciam `até trinta`, a prova por mutação saiu nos dois sentidos para os quatro sítios, a linha do `CHANGELOG.md` existe, e as **dez** linhas de `Verificação` saem nos valores declarados.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` · 2026-09-19 — card novo do `ESC-32` (2026-09-19), resíduo medido da própria `LM-T14` (`AE-57`). **Não é investimento novo: é a terminação da entrega de ontem** — a distinção que o `ESC-31` usou para adiar a atribuição por hunk (construir capacidade nova para servir poucas revisões) **não** se aplica aqui, porque nada se constrói: fecha-se o que já foi aberto.
- **Esforço:** low
- **Depende de:** nada. Nada depende desta.
- **Produto do módulo:** - **(a) As quatro capturas passam a aceitar numeral composto, com âncora que impede a captura gulosa.** Literais medidos no `ESC-32` (os quatro foram rodados contra o `README.md` de hoje e devolveram, nesta ordem, `nove`, `dez`, `Sete`, `treze`): - `(\S+) agentes` vira `^O kit são (.+?) agentes`; - `(\S+) skills` vira `agentes, (.+?) skills`; - `\*\*(\S+)\*\* regras falham como teste executável` vira `^\*\*(.+?)\*\* regras falham como teste executável`; - `falham como teste executável, \*\*(\S+)\*\* dependem de gate de review` vira a mesma forma com `(.+?)` no lugar de `(\S+)`. A âncora não é decoração: `(.+?) agentes` sem ela captura *"O kit são nove"*, porque a busca é da posição zero — foi medido antes de prescrever. - **(b) As quatro mensagens de vocabulário dizem a mesma coisa.** As **três** que ainda anunciam `por extenso até vinte` passam a `por extenso até trinta`, que é o que o mapa entrega desde a `LM-T14`. Nenhuma outra palavra das mensagens muda. - **(c) A linha do `CHANGELOG.md`**, no bloco não lançado, contendo o literal `o vocabulário do guarda fica coerente entre os quatro sítios`.
- **Restrições desta tarefa:** o `README.md` **não** é tocado — as frases de hoje estão certas, e a prova de numeral composto acontece na cópia. O `$numeralMap` **não** muda: ele já vai a `trinta`. Nenhuma checagem muda de veredito sobre o repo de hoje, e a `Verificação` 9 é quem tranca isso. Nenhuma seção nova entra na enumeração do `.SYNOPSIS` — a contagem de **seis** checagens continua certa, porque nada se acrescenta, só se uniformiza.
- **Não fazer:** não renumerar checagens; não estender o guarda a outras seções; não mexer no `README.md` nem em `GOVERNANCA.md`; não tocar `card_check.py`; não commitar.
- **Contingências:** 1. se alguma das quatro capturas novas devolver token diferente do medido no `ESC-32` (`nove`, `dez`, `Sete`, `treze`) no despacho → **parar** e sinalizar `blocked` razão `premissa`, citando o token obtido: a âncora estaria errada, e publicar captura gulosa é falso verde; 2. se a prova por mutação **não** sair `exit 0` com os quatro numerais compostos → **parar**: é o mesmo defeito do `AE-57` reaparecendo, e desta vez o card existia para fechá-lo.

## Execução

**Consumo:** 42 tool uses, 108.0 k tokens, 424.2 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: Abrir card no P-0740 para o residuo de escopo do numeralMap no check-readme.ps1: a tabela de vocabulario vive dentro do bloco Anatomia do kit e o bloco 4b a consome de fora, o que troca o diagnostico por excecao nao tratada quando a secao falta - nenhum dos tres cards da trinca declarou esse acoplamento como alvo.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

1) A ancora e substantiva e foi re-medida: sem ela, '(.+?) agentes' sobre a linha do README de hoje devolve 'O kit sao nove', e 'agentes, (.+?) skills' sem o prefixo devolve 'O kit sao nove agentes, dez'; com as capturas entregues os cinco sitios devolvem nove, dez, Sete, treze e Vinte. 2) A forma em par (ausencia contada no arquivo inteiro + presenca do novo) foi o que fechou a classe: a ausencia e universal e alcanca os irmaos, e e ela - nao a presenca - que prova que nenhum quinto sitio sobrou (grep no repo inteiro: zero 'extenso ate vinte', zero '(\S+)' no script). 3) A assimetria aparente de .ToLower() entre os dois sitios da Anatomia e os tres do bloco 4b NAO e uma quinta instancia da classe: hashtable de PowerShell e case-insensitive por construcao, e eu medi numeral composto em caixa alta passando nos cinco sitios. Registrar para que um card futuro nao 'conserte' uma divergencia que nao existe. 4) Prova por mutacao reproduzida por mim fora do repo: uma fixture de 21 agentes / 22 skills / 21 guardrails com numeral composto nos cinco sitios sai exit 0, e dez quebras (cinco por divergencia, cinco por numeral fora do vocabulario) saem exit 1, cada uma citando declarado vs medido ou o token recusado com 'ate trinta'. Repo real inalterado: md5 dos quatro arquivos e do git status identicos antes e depois; copia descartada. 5) Consumo (informativo, nao nota): 42 tool_uses / 108.0 tk_k, o maior das quatro irmas do dia num card de esforco 'low' - o custo esta na fixture da prova por mutacao, nao na edicao, e isso e esperado para card cuja parte comportamental so se prova fora do repo.

## Fechamento

**Desdobramento:** aprovado
