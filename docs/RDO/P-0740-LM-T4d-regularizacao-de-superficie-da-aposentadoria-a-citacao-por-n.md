# RDO — P-0740 · LM-T4d

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T4d` — Regularização de superfície da aposentadoria: a citação por **nome**
**Modelo:** Sonnet · **Classe:** mecanica
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — nenhuma superfície viva cita **pelo nome** uma skill que a `LM-T4` aposentou; cada citação passa a apontar para quem herdou a responsabilidade.

**Arquivos-alvo:** - `.claude/skills/bootstrap-pantonic/SKILL.md` - `.claude/skills/diario-de-obras/SKILL.md` - `.claude/global/docs/GOVERNANCA_MEMORIAS.md` - `GOVERNANCA.md` (**só** o item 17 da §7, e **só** o nome — ver `Restrições`) - `README.md` (**só** a linha 17 da tabela *Os guardrails*, e **só** o nome)

**Verificação:** 1. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/bootstrap-pantonic/SKILL.md -Pattern 'proximo-passo' -SimpleMatch | Measure-Object).Count" ``` → **0**. **Medido antes: 1**. 2. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/bootstrap-pantonic/SKILL.md -Pattern 'passagem-de-bastao' -SimpleMatch | Measure-Object).Count" ``` → **≥ 1**. **Medido antes: 0**. 3. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/bootstrap-pantonic/SKILL.md,.claude/skills/diario-de-obras/SKILL.md,.claude/global/docs/GOVERNANCA_MEMORIAS.md,GOVERNANCA.md,README.md,docs/DOC_MAP.md,.claude/README.md,.claude/skills/scrum-master/SKILL.md -Pattern '`proximo-passo`' -SimpleMatch | Measure-Object).Count" ``` → **0**. **Medido antes: 5**. 4. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/bootstrap-pantonic/SKILL.md,.claude/skills/diario-de-obras/SKILL.md,.claude/global/docs/GOVERNANCA_MEMORIAS.md,GOVERNANCA.md,README.md,docs/DOC_MAP.md,.claude/README.md,.claude/skills/scrum-master/SKILL.md -Pattern '`handover`' -SimpleMatch | Measure-Object).Count" ``` → **0**. **Medido antes: 3**. 5. ``` pwsh -NoProfile -Command ".claude/checks/check-readme.ps1 | Out-Null; exit $LASTEXITCODE" ``` → **exit 0**, **inalterado** — guarda de regressão: trocar o **nome** citado na linha 17 não pode mexer na contagem de guardrails que a `LM-T4` fechou em 19. **Medido antes: exit 0** (o valor vai **sem ponto final** dentro do negrito: `exit 0.` seria lido como texto e não como código de saída — defeito meu, pego pelo `card_check` no `ESC-21`).

**Pronto quando:** o `bootstrap-pantonic` copia `passagem-de-bastao` e não cita as aposentadas; nenhuma das oito superfícies varridas cita `` `proximo-passo` `` ou `` `handover` ``; o item 17 cita a skill certa; e as cinco linhas de `Verificação` saem como escritas.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` (despachada em 2026-09-19, antecipada à `LM-T3b` por decisão do loop — Diretiva item 4) — card novo do `ESC-21` (2026-09-19), residência única do `AE-37`. **Recomendação de ordem (a ordem é do loop, Diretiva item 4): antes da `LM-T3b`**, por urgência assimétrica medida — enquanto o `bootstrap-pantonic` mandar copiar skill que não existe, **todo projeto novo do framework nasce quebrado**, e o kit se propaga a cinco derivados.
- **Esforço:** low
- **Depende de:** `LM-T4` (fechada — é a aposentadoria dela que deixou o resíduo). Nada depende desta.
- **Fora do escopo, por decisão do `ESC-21` (`DM-44` (iii)):** `.claude/settings.json`, que traz `Edit(/.claude/skills/handover/**)` e `Edit(/.claude/skills/proximo-passo/**)` (linhas 5 e 6, medidas). É **superfície de permissão**, e regra de permissão não se altera por card: vai ao relatório de encerramento como **ato do dono**, junto do `DM-27` que a criou. As duas regras são **inócuas** — concedem `Edit` sobre diretório inexistente —, então a espera não custa nada.
- **O resíduo, medido no `ESC-21`:** citações **por nome** sobreviveram fora dos `Arquivos-alvo` da `LM-T4`, que varreu por **caminho** e estava certa no que media. Contagem com crase (a forma da citação normativa): `` `proximo-passo` `` → **5**, `` `handover` `` → **3**. As duas que importam: `.claude/skills/bootstrap-pantonic/SKILL.md:53` (manda **copiar** as duas para projeto novo) e `.claude/settings.json:5-6` (regra de permissão órfã, fora de escopo). As demais são ponteiros normativos em `diario-de-obras/SKILL.md` e um em `.claude/global/docs/GOVERNANCA_MEMORIAS.md:154`.
- **O mapa de sucessão — fechado aqui, para que o executor não decida nada (`DU-5`, `TK-36`):** - citação sobre **escolher a próxima tarefa, ler a diretiva, drenar inbox ou apurar a fila** → **`scrum-master`** (a `DU-5` diz, com todas as letras, que a responsabilidade da `proximo-passo` é **herdada pelo `scrum-master`**); - citação sobre **transição entre tarefas, fechamento, passagem de bastão ou herança de contexto** → **`passagem-de-bastao`**; - **a palavra** *handover* em prosa (`handover ao dono`, `handover de execução`) **não é citação de skill e não se toca** — é exatamente o eixo que o `AE-37` nomeia: nome ≠ palavra.
- **Passos:** 1. `bootstrap-pantonic/SKILL.md:53`: na lista de skills a copiar, **remover** `proximo-passo` e `handover` e **acrescentar** `passagem-de-bastao`. 2. `diario-de-obras/SKILL.md` e `.claude/global/docs/GOVERNANCA_MEMORIAS.md`: reapontar cada citação com crase pelo **mapa de sucessão** acima. Citação que **não** couber em nenhuma das duas regras do mapa → **parar** e sinalizar `blocked` razão `premissa`, citando a linha: o mapa é fechado, e ampliá-lo é decisão de consultor. 3. `GOVERNANCA.md` §7 item 17 e a linha 17 da tabela *Os guardrails* do `README.md`: trocar **apenas o nome da skill** citada, pelo mapa. Nada mais desses dois itens muda.
- **Restrições desta tarefa:** o **item 17** (`G-REPLAN`) tem **só o nome da skill** trocado — a substância dele continua fechada (`DM-12`, e é a proibição que a `LM-T4` respeitou corretamente); esta autorização é **estreita e explícita**, e é o `DM-33` (ii) aplicado de novo: o que colide com proibição vira **passo autorizado**, nunca improviso do executor. A palavra *handover* em prosa **não** se toca. `.claude/settings.json` **não** se toca (ato do dono). Nenhuma skill é criada, apagada ou renomeada aqui.
- **Não fazer:** não editar `.claude/settings.json`; não reabrir a substância do `G-REPLAN`; não tocar `.claude/agents/` (`DM-17`); não regenerar projeção (a contagem de skills não muda); não commitar.
- **Contingências:** 1. citação que não couber no mapa de sucessão → `blocked` razão `premissa`, com a linha citada; 2. se a `Verificação` 5 sair diferente de 0 → seguir com a entrega e devolver `contingência 2 acionada: check-readme exit <n>` — a contagem de guardrails é da `LM-T4`, não desta tarefa.

## Execução

**Consumo:** 27 tool uses, 61.9 k tokens, 132.1 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: README.md:748 (linha 17 da tabela Os guardrails) ficou com o mesmo nome duas vezes - roteamento das skills scrum-master/scrum-master - porque as duas antecessoras enumeradas colapsam numa so skill; corrigir exige autorizacao alem do 'so o nome' que o card deu, e a substancia do item 17 esta fechada por DM-12: decisao de planejamento, nao da execucao.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
