# RDO — P-0748 · TLG-T1

**Plano:** `docs/plans/P-0748-tela-do-gerente.md`
**Tarefa:** `TLG-T1` — A sonda de viabilidade diante do dono
**Modelo:** Sonnet · **Classe:** investigacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O investigador encena, diante do dono, as quatro formas de uma saída chegar à tela — uma busca feita pelo próprio condutor, buscas e leituras feitas dentro de um agente despachado, a resposta de um gancho da ferramenta e a linha de status —; o dono anota o que cada uma mostra, e dessa tabela sai o veredito de viabilidade, sim ou não.

**Arquivos-alvo:** - `.claude/settings.json:22` — âncora `"hooks": {` (bloco temporário inserido logo abaixo e removido no passo 7) - `docs/plans/P-0748-tela-do-gerente.md §2.1` — a seção nova `### 2.2 Agregado da sonda de viabilidade (TLG-T1)` entra **depois** do último bullet da `### 2.1` e **antes** do `---` que precede `## 3. Decisões`

**Verificação:** 1. `(Select-String -Path docs/plans/P-0748-tela-do-gerente.md -Pattern "^### 2\.2 Agregado da sonda de viabilidade" | Measure-Object).Count` (âncora de início de linha: o próprio card cita o título indentado e dentro de crases, e essas linhas não contam, `DTG-16`) → antes `0`, depois `1` (medido 2026-09-24). 2. `(Select-String -Path docs/plans/P-0748-tela-do-gerente.md -Pattern "^\*\*Veredito de viabilidade \(Marco 2\):\*\* (sim|não) " | Measure-Object).Count` (mesma âncora; exige `sim` ou `não` preenchido) → antes `0`, depois `1` (medido 2026-09-24). 3. `(Select-String -SimpleMatch -Path .claude/settings.json -Pattern "SONDA-HOOK-C" | Measure-Object).Count` → antes `0` (medido 2026-09-23), **durante a sonda** `1`, depois do passo 7 `0`. 4. `(Select-String -SimpleMatch -Path .claude/settings.json -Pattern '"PostToolUse"' | Measure-Object).Count` → antes `0`, depois do passo 7 `0` (medido 2026-09-24); e `python -c "import json; json.load(open('.claude/settings.json', encoding='utf-8')); print('json ok')"` → `json ok`. Conferência por conteúdo, não por `git diff`: o arquivo é ignorado pelo git (`.gitignore:5`), e `git diff --quiet` sobre ele sai `0` sempre (`DTG-16`).

**Pronto quando:** a tabela `### 2.2` com quatro linhas preenchidas com `sim`/`não` (ou `não medida` só na linha (c)) e a linha de veredito — é o **fato** que `stream de dados.viabilidade medida` exige: *medida diante do dono, uma linha por mecanismo com o que ele viu, e o veredito sim ou não tirado dessa tabela; sendo não, a única alternativa já pensada sobe ao dono como decisão* — Verificação 1 e 2.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-24
- **Fundamento:** `DTG-3` (sonda antes da recomendação), `DTG-9` (hook só entra se alterar a tela), `DTG-14` (execução no topo, hook gravado antes da sessão), `F-1`, `F-3`, `F-9` (nenhum `PostToolUse` vigente; settings do projeto limpo), `F-17` (`pantonic-scout` existe), hipóteses `H-1`..`H-4` que a sonda mede, `R-1`.
- **Operação do modelo:** `OP-1` - OP-1: O investigador encena, diante do dono, as quatro formas de uma saída chegar à tela — uma busca feita pelo próprio condutor, buscas e leituras feitas dentro de um agente despachado, a resposta de um gancho da ferramenta e a linha de status —; o dono anota o que cada uma mostra, e dessa tabela sai o veredito de viabilidade, sim ou não. - precisa de: tela do monitor — Quem implementa não mexe nela: só a observa, na sonda do começo e na validação do fim. É nela que se prova que o stream mudou.
- **Camada e fronteira:** kit (`.claude/`), sem código de produto. Toca `.claude/settings.json` **do projeto** (edição temporária, desfeita ao fim) e este plano (seção nova `### 2.2`). Não toca `C:\Users\panta\.claude\settings.json`, nenhum agente, nenhuma skill. **Esta tarefa não se delega:** é executada no topo da sessão pelo agente que a conduz, em modelo Sonnet, com o dono olhando a extensão VS Code; o despacho do passo (b) é a única chamada de subagente, e é ela mesma o objeto medido.
- **Domínio:** *tela do monitor* = painel da extensão VS Code do Claude Code (`DTG-1`); *forma de chegar à tela* = uma das quatro: (a) chamada de ferramenta do topo, (b) chamada de ferramenta dentro de subagente, (c) stdout de hook `PostToolUse`, (d) `statusLine`.
- **Contratos/classes:** nenhum código. Forma do agregado (tabela de quatro linhas + uma linha de veredito), literal: ``` ### 2.2 Agregado da sonda de viabilidade (TLG-T1) Medido pelo dono na extensão VS Code em <AAAA-MM-DD>, sessão reaberta com o hook (c) gravado. | forma | mecanismo | observado pelo dono | o que apareceu na tela | |---|---|---|---| | (a) | `Grep` feito pelo condutor no topo | sim / não | <uma frase> | | (b) | 3 `Grep` + 1 `Read` dentro de um subagente despachado | sim / não | <uma frase: "só a linha do despacho" ou "as quatro chamadas no topo"> | | (c) | stdout de um hook `PostToolUse` (`SONDA-HOOK-C`) | sim / não / não medida | <uma frase> | | (d) | `statusLine` configurada no settings global | sim / não | <uma frase> | **Veredito de viabilidade (Marco 2):** sim / não — regra: `sim` se e só se a linha (b) registra "só a linha do despacho". ``` Na coluna `observado pelo dono`, `sim` significa "a saída dessa forma **aparece** no fluxo principal da extensão"; `não`, "não aparece".
- **Método de sondagem:** corpus = esta própria sessão; métrica = sim/não por forma, anotado pelo dono; agregado = a tabela acima, ≤ 12 linhas, sem dado bruto. 1. **Preparar o hook (c), antes da sessão de observação.** Em `.claude/settings.json`, logo abaixo da linha `"hooks": {` (linha 22), inserir o bloco literal (vírgula final incluída, porque `"PreToolUse"` vem em seguida): ``` "PostToolUse": [ { "matcher": "Grep", "hooks": [ { "type": "command", "command": "python -c \"print('SONDA-HOOK-C')\"" } ] } ], ``` Conferir `python -c "import json; json.load(open('.claude/settings.json', encoding='utf-8')); print('json ok')"` → `json ok`. Dizer ao dono, em uma linha: `Hook de sonda gravado; feche e reabra esta sessão da extensão para ele carregar, e me diga "pronto".` Encerrar o turno. 2. **Forma (a)** — com a sessão reaberta: uma chamada `Grep` no topo, padrão `TLG-T1`, caminho `docs/plans/P-0748-tela-do-gerente.md`, `output_mode` `content`. Escrever ao dono: `Forma (a) feita: o Grep do topo. Anote o que apareceu.` 3. **Forma (c)** — o mesmo `Grep` do passo 2 disparou o hook (matcher `Grep`). Escrever ao dono: `Forma (c): o texto SONDA-HOOK-C apareceu em algum lugar da tela? Anote sim ou não.` 4. **Forma (b)** — uma chamada `Agent`, `subagent_type` `pantonic-scout`, prompt literal: `Sonda P-0748 forma (b). Rode, nesta ordem, três Grep — padrões OP-1, OP-2 e OP-3, cada um no arquivo docs/plans/P-0748-tela-do-gerente.md, output_mode content — e um Read de docs/plans/_CAMPANHA-P-0748.md com limit 5. Devolva uma única linha: "sonda-b: 3 grep + 1 read feitos".` Escrever ao dono: `Forma (b) feita: o subagente rodou quatro chamadas. Na tela apareceu só a linha do despacho, ou as quatro chamadas no topo? Anote.` 5. **Forma (d)** — escrever ao dono: `Forma (d): a linha de status (statusLine do settings global) aparece na extensão? Anote sim ou não.` 6. **Registrar o agregado:** o dono dita as quatro anotações; gravar a `### 2.2` no plano na forma literal de `Contratos/classes`, com a data e o veredito pela regra da última linha. 7. **Remover o hook:** apagar do `.claude/settings.json` exatamente o bloco inserido no passo 1 (as doze linhas, de `"PostToolUse": [` à `],`), restaurando `"hooks": {` seguido diretamente de `"PreToolUse": [`. Conferir com a Verificação 3 e 4.
- **Restrições desta tarefa:** `I-1` — nenhum arquivo fora deste repositório é editado; o settings **global** fica intocado. `I-4` — a `### 2.2` registra só o que o dono viu, nunca hipótese. `I-6` — o veredito é aceite de **marco** (Marco 2), não desta tarefa: a tarefa fecha com a tabela gravada, seja o veredito `sim` ou `não`. Nenhum agente, skill ou instrumento é editado.
- **Não fazer:** não despachar `pantonic-executor` para esta tarefa; não editar `C:\Users\panta\.claude\settings.json`; não deixar o bloco `PostToolUse` no settings ao fim; não interpretar (c) ou (d) como veredito — só (b) decide; não repetir a sonda para "confirmar"; não iniciar `TLG-T2` neste contexto.
- **Contingências:** - se a chamada `Agent` não oferece `subagent_type` `pantonic-scout` → seguir com `general-purpose` e o mesmo prompt, anotando `(subagente general-purpose)` na coluna `mecanismo` da linha (b); - se o dono não reabre a sessão (passo 1) → seguir com os passos 2, 4, 5 e 6 assim mesmo, registrar (c) como `não medida` e a frase `sessão não reaberta`; o veredito segue só de (b); - se `python -c "import json; …"` do passo 1 falha → parar e sinalizar `blocked` razão `ferramenta`, devolvendo a linha de erro; restaurar o arquivo apagando à mão o bloco do passo 1 (o arquivo é ignorado pelo git, `.gitignore:5`: não há `git checkout` que o restaure, `DTG-16`) e conferir de novo o `json ok` antes de parar; - se (b) registra "as quatro chamadas no topo" → veredito `não`; gravar a tabela e fechar a tarefa normalmente — a rodada de decisões sobre `R-1` é ato da orquestração no Marco 2, não deste card.
- **Testes:** nenhum teste novo (tarefa de investigação); nenhuma suíte é tocada.
- **Fora do escopo desta tarefa:** a resposta a `R-1` — é do dono, no Marco 2, e entra em `DTG-12`; qualquer edição no loop (`TLG-T3`, `TLG-T4`).

## Execução

**Consumo:** 5 tool uses, 15.1 k tokens, 27.6 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: Marco 2: a ### 2.2 mediu veredito de viabilidade 'nao' ((b) = as quatro chamadas no topo, H-3 = nao); pela ## 6 item 1 e R-1 a rodada de decisoes sobre R-1 sobe ao dono e a resposta entra em DTG-12 (hoje vazia) antes de TLG-T3, que para em premissa sem ela; o veredito 'viavel' do condutor no Marco 1 fica contrariado pela medida

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

Tarefa executada no topo: o SubagentStop so mede subagentes; o consumo do topo de uma tarefa 'Sonnet + dono' nao entra na serie. O consumo registrado aqui e o do subagente da forma (b), unica medida da execucao; consultor e revisao tem linhas proprias na telemetria (TLG-T1-consultor-1, TLG-T1-revisao).

## Fechamento

**Desdobramento:** aprovado
