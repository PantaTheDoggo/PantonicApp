# RDO — P-0741 · MC-T5

**Plano:** `docs/plans/P-0741-modelo-conceitual.md`
**Tarefa:** `MC-T5` — O README explica o modelo, a aferição sobre o próprio plano e o veredito do dono (Marco 2)
**Modelo:** Opus · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** o `README.md` explica o modelo conceitual em §5 e §8 para o leitor externo; o loop gera `modelo.py show` sobre este plano e o dono lê; o aceite do dono fecha o Marco 2.

**Arquivos-alvo:** - `README.md` §5 (`## 5. O fluxo plano → execução`), §8 (`## 8. Planos: o que é um plano fechado`) e a região **gerada** entre `<!-- kit:agents:begin -->` e `<!-- kit:agents:end -->`, reescrita por instrumento e não à mão (`DMC-28`)

**Verificação:** 1. ``` pwsh -NoProfile -Command "(Select-String -Path README.md -Pattern '### 8.1 O modelo conceitual' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. 2. ``` pwsh -NoProfile -File .claude/checks/check-readme.ps1 ``` → **exit 0**. **Medido antes: exit 0**. 3. ``` python .claude/tools/modelo.py show --plano docs/plans/P-0741-modelo-conceitual.md ``` → **exit 0**. **Medido antes: exit 0**. (re-derivada pelo consultor em 2026-09-20, `ESC-3`: o instrumento passou a existir com a `MC-T2` e o `exit 2` de 2026-09-19 caducou; é invariância.) 4. ``` pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift ``` → **exit 0**. **Medido antes: exit 1**. (`DMC-28`; medido pelo consultor em 2026-09-20 — três linhas de um achado só, todas na linha do `pantonic-consultant`. É a guarda que a `MC-T3` virou e que esta tarefa fecha; o plano não termina com ela vermelha.)

**Pronto quando:** as quatro linhas devolvem o esperado e o veredito do dono está escrito no diário.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-24
- **Fundamento:** decisões `DMC-11`, `DMC-15`, a `DMC-28` do `ESC-4` (esta tarefa regenera a região marcada do README e devolve `check-drift` a exit 0), e do `ESC-2` a `DMC-21` (o regime transitório de confirmação expira nesta tarefa); fato `F-12`.
- **Depende de:** `MC-T1`, `MC-T2`, `MC-T2a`, `MC-T2b`, `MC-T3`, `MC-T4`, `MC-T4a`
- **Oração do modelo:** `M-4`, `M-20` - M-4: O modelo é a interface entre o dono e o loop: quem lê só o modelo entende o que o plano faz, o que já está pronto, o que está em andamento e o que mudou desde a última leitura. - M-20: Este plano é o primeiro a usar o modelo: a seção é confirmada e emendada pelas próprias regras que descreve, tarefa a tarefa, até o segundo marco, quando o dono lê a leitura gerada pelo instrumento e valida.
- **Camada e fronteira:** documentação pública do hub (`README.md`); leitura do dono.
- **Contratos/classes:** nenhum.
- **Passos:** 1. Em `README.md` §8, ao final da seção (antes de `## 9. O fechamento de tarefa`), inserir a subseção literal: ``` ### 8.1 O modelo conceitual — o que o dono lê Todo plano carrega, logo depois do pedido, a seção **Modelo conceitual**: um vocabulário, orações numeradas que afirmam o que o resultado faz em linguagem corrente, e uma lista de mudanças. O planejador escreve o modelo antes das tarefas e cada tarefa cita as orações que materializa; o executor as recebe no card; o revisor confirma cada oração ao aprovar a última tarefa dela, e só emenda o texto quando a divergência é inequívoca — na dúvida, abre achado de alvo `modelo`; o consultor e o planejador emendam o modelo quando uma decisão muda o que o plano entrega. O instrumento `modelo.py` confere a integridade (`check`) e gera a leitura do dono (`show`), que abre todo relatório de encerramento e todo marco. Quem lê só essa leitura sabe o que o plano faz, o que está pronto, o que está em curso e o que mudou. Norma: `GOVERNANCA.md` §3.2; gramática: skill `diario-de-obras`. O primeiro plano com modelo foi o `P-0741`. ``` 2. Em `README.md` §5, no parágrafo que começa com `Planejador e executor são papéis distintos` e termina com a linha `**sinaliza** \`blocked\` com a razão tipada e escala — não improvisa uma alternativa própria.` (linhas 416-420 em 2026-09-19), acrescentar ao final dessa última linha, na mesma linha, a frase: ` O plano nasce com o **modelo conceitual** (§8.1), e o dono dá go ou no-go lendo só ele — é o Marco 1 de todo plano.` 3. Rodar `pwsh .claude/checks/check-readme.ps1` e corrigir o que ele apontar **no README** (nunca no checker). 3a. Rodar `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` (`DMC-28`): o instrumento reescreve as duas regiões marcadas do `README.md` a partir de `.claude/agents/*.md` e `.claude/skills/*/SKILL.md`. A linha do `pantonic-consultant` está defasada desde a `MC-T3` (`AE-15` item 1) e é isso que a guarda `check-drift` acusa. Não editar a tabela à mão: ela é gerada. Depois, rodar `check-readme.ps1` de novo — as duas conferências têm de sair exit 0 ao mesmo tempo. 4. Rodar `python .claude/tools/modelo.py show --plano docs/plans/P-0741-modelo-conceitual.md` e colar a saída integral na linha de retorno da entrega, depois da linha de status, para que o orquestrador a leve ao dono no relatório (é a leitura do Marco 2). Nesta execução `M-4` e `M-20` ainda saem `[prevista]`: quem as confirma é o revisor desta tarefa, depois do passo 4 — não é defeito, e o `show` que o orquestrador roda no Marco 2 (`DMC-11`) já sai com as vinte confirmadas. 5. O aceite do dono (leitura da saída do passo 4 e do README) é registrado pelo orquestrador no diário (`GOVERNANCA.md` §4.5); a tarefa só fecha `done` com o veredito escrito.
- **Restrições desta tarefa:** texto do passo 1 verbatim; `check-readme.ps1` e `kit_check.ps1` intocados; nenhuma outra seção do README muda além de §5, §8 e das regiões **geradas** entre os marcadores `kit:agents` e `kit:skills`, que só mudam por `-Mode generate` (`DMC-28`).
- **Não fazer:** não alterar contagens de agentes/skills na frase de *Anatomia do kit* (não mudam, `F-12`); não editar o modelo deste plano (é o revisor que confirma); não reescrever a verificação 1 para agradar `card_check.py` — a reprovação `item 8: fora da forma da 8.1` deste card é falso positivo do instrumento, medido e registrado na `AE-12`.
- **Contingências:** 1. se `check-readme.ps1` apontar divergência fora de §5/§8 → corrigir só se for consequência direta do texto inserido; caso contrário parar e sinalizar `blocked` razão `premissa`. 2. se `modelo.py show` sair diferente de `0` → parar e sinalizar `blocked` razão `dependencia` (a `MC-T2`/`MC-T3` deixaram o modelo inválido). 3. se `kit_check.ps1 -Mode generate` alterar linha fora das duas regiões marcadas, ou se `check-drift` continuar exit `1` depois dele → parar e sinalizar `blocked` razão `premissa`, com a saída integral na razão: a causa não é a `description` da `MC-T3` e o diagnóstico da `AE-15` item 1 caiu.
- **Testes:** nenhum executável.
- **Nota ao revisor (regime transitório, `DMC-21` — não é tarefa do executor):** esta é a última tarefa do plano. Além de `M-4` e `M-20`, **confirme toda oração da §1.2 que ainda esteja `prevista` e cujas tarefas estejam todas em `done`, `cancelled` ou `review`**: ao fim desta revisão as vinte orações têm de estar `confirmada`, e é isso que o Marco 2 mostra ao dono. O regime transitório expira aqui.
- **Fora do escopo desta tarefa:** retrofit de planos anteriores; verbos de escrita do instrumento.

## Execução

**Consumo:** 19 tool uses, 61.0 k tokens, 162.1 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: dois achados de texto de card (AE-17): raiz e kit tratados como o mesmo README; Pronto quando de card de marco insatisfazivel no ato da revisao

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
