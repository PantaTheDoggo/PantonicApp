# RDO — P-0739 · BKL-T12

**Plano:** `docs/plans/P-0739-backlog-instrumento.md`
**Tarefa:** `BKL-T12` — Aferição do pickup e revisão do `README.md` com veredito do dono
**Modelo:** Opus · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** o custo do pickup novo é medido e publicado em `docs/CUSTO_DO_PICKUP.md`, e o `README.md` mais o `docs/DOC_MAP.md` passam a descrever o pickup por instrumento — com o veredito do dono sobre o espelho (`DB-20`).

**Arquivos-alvo:** - `docs/CUSTO_DO_PICKUP.md` - `README.md` - `docs/DOC_MAP.md`

**Verificação:** 1. ``` pwsh -NoProfile -Command "(Select-String -Path docs/CUSTO_DO_PICKUP.md -Pattern '^## 14 ' | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. 2. ``` pwsh -NoProfile -Command "(Select-String -Path docs/DOC_MAP.md -Pattern '## 14 ' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. O par com o item 1 é a conferência contra a fonte: a seção existe no documento **e** está indexada no mapa, que é a porta de entrada obrigatória. 3. ``` pwsh -NoProfile -Command "(Select-String -Path README.md -Pattern 'backlog_hook.py' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. O literal é o do hook porque o `README.md` de hoje não cita nenhum dos dois instrumentos, e o hook é o item que a seção de ferramentas ganha. 4. ``` pwsh -NoProfile -Command "pwsh -NoProfile -File .claude/checks/check-readme.ps1 > $null 2>&1; $LASTEXITCODE" ``` → **0**, invariante. **Medido antes: 0**. 5. ``` pwsh -NoProfile -Command "(git status --short -- docs/CUSTO_DO_PICKUP.md README.md docs/DOC_MAP.md | Measure-Object).Count" ``` → **3**, uma linha por caminho. **Medido antes: 0**. Recorte por pathspec porque a árvore de trabalho carrega registro de orquestração alheio a esta tarefa (`DB-29`).

**Pronto quando:** os cinco itens de `Verificação` dão o resultado descrito; a seção nova de `docs/CUSTO_DO_PICKUP.md` traz o número **medido** do pickup novo contra os 77.457 chars da `## 3` e o alvo de 40.000 da `## 6`, em no máximo 30 linhas; e o dono deu o veredito do espelho (`DB-20`).

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20
- **Esforço:** medium
- **Depende de:** `BKL-T11a`
- **Razão da dependência e insumos (`DB-50`):** sem o hook no ponto de carga **falando** não há pickup novo para medir — e o hook só passou a falar no `BKL-T11a` (`DB-52`). Decisões: `DB-20` (o aceite do dono é parte desta tarefa) e o método `DC-4` de `docs/CUSTO_DO_PICKUP.md` (chars da saída do hook numa sessão nova mais o 1º `usage`). Fatos: a `## 3` de `docs/CUSTO_DO_PICKUP.md` (77.457 chars do pickup medido) e a `## 6` do mesmo arquivo (alvo de 40.000 chars).
- **Passos:** 1. Medir o pickup novo pelo método `DC-4`: chars da saída do hook numa sessão nova, mais o 1º `usage` dessa sessão. 2. Publicar em `docs/CUSTO_DO_PICKUP.md` a seção `## 14 `, de no máximo 30 linhas, com o número medido no passo 1 confrontado com os 77.457 chars da `## 3` e com o alvo de 40.000 da `## 6`. O número da seção é **14** porque a última seção do arquivo hoje é a `## 13` — medido em 2026-09-19. A `BKL-T9` dizia `## 15`: número de 2026-09-15, que não se copia. 3. Em `docs/DOC_MAP.md:104`, dentro da lista `**Seções:**` do bloco `## docs/CUSTO_DO_PICKUP.md`, acrescentar a entrada da seção nova imediatamente **depois** da entrada de `## 13`. 4. Em `README.md`, acrescentar `.claude/tools/backlog.py` e `.claude/tools/backlog_hook.py` à seção de ferramentas, e reescrever o §9 do fluxo para descrever o pickup por instrumento. 5. Rodar `pwsh -NoProfile -File .claude/checks/check-readme.ps1`. 6. Apresentar o espelho ao dono e registrar o veredito dele (`DB-20`).
- **Restrições desta tarefa (copiadas inline; nenhuma vale por ponteiro):** - **Teto da seção nova:** no máximo 30 linhas em `docs/CUSTO_DO_PICKUP.md`, contadas com `(Get-Content <arquivo>).Count` sobre o recorte — `Measure-Object -Line` ignora linha vazia e erra o número. - **Frase que conta item fecha no mesmo ato:** se a seção de ferramentas do `README.md` tiver frase que declare o número de ferramentas, ela se atualiza na mesma edição. O `.claude/checks/check-readme.ps1` confere as contagens de agentes, skills e guardrails e **não** confere essa frase. - **O número publicado é o medido no passo 1, nunca estimado:** a seção traz o valor observado numa sessão nova, com a data da medida. - **O aceite do dono é parte da tarefa** (`DB-20`): a entrega não fecha sem o veredito dele sobre o espelho.
- **Não fazer:** - Não editar `.claude/tools/`, `.claude/skills/`, `docs/DIARIO_DE_OBRAS.md` nem `docs/plans/P-0739-backlog-instrumento.md`. - Não renumerar nenhuma seção existente de `docs/CUSTO_DO_PICKUP.md`.
- **Contingências:** - se o hook não injetar contexto na sessão nova → parar e sinalizar `blocked` razão `dependencia`, nomeando o `BKL-T11`; - se `docs/CUSTO_DO_PICKUP.md` já tiver uma seção `## 14 ` → seguir com o próximo número livre de seção e devolver, na linha de retorno da entrega, `contingência 2 acionada: seção publicada com outro número`; - se o guarda do item 4 da `Verificação` sair diferente de 0 → parar e sinalizar `blocked` razão `premissa`, colando a linha de saída do guarda; - se o dono não der o veredito no mesmo despacho → parar e sinalizar `blocked` razão `dependencia`, com os três arquivos já gravados.
- **Fora do escopo desta tarefa:** nada deste plano fica depois dela — o `BKL-T12` é a última tarefa do `P-0739`.
- **Notas de execução:** - 2026-09-20 `review` — Passos 1-5 entregues, aprovada com ressalva 88%, bloqueante nenhuma. Passo 6 (veredito do dono, DB-20) ABERTO: a tarefa nao fecha sem ele. Laudo preservado, RDO nao fechado. Ver AE-40.

## Execução

**Consumo:** 32 tool uses, 97.2 k tokens, 355.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: As duas metades da pendencia foram resolvidas: o usage_1 foi medido em 2026-09-20 (TK-58a..TK-58d, 39.650 tk, par do DC-4 declarado aberto por nao isolar o pickup) e o dono deu o veredito sobre o espelho em 2026-09-20, declarando o plano concluido.

## Laudo

**Veredito:** ressalva

**Percentual:** 88%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
