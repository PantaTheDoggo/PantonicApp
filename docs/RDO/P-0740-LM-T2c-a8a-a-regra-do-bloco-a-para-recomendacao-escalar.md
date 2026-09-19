# RDO — P-0740 · LM-T2c

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T2c` — `A8a`: a regra do bloco A para `recomendacao=escalar`
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — o bloco A passa a ter regra para `recomendacao=escalar`. Sem ela, o `B1` que a `LM-T2` acabou de publicar é **inalcançável pela própria primeira condição**: o bloco B só é avaliado depois de o bloco A dizer "segue", e `escalar` não casa com `A6` (`refazer`), `A7` (`reprovado`), `A8` (`seguir com ressalva`) nem `A9` (`seguir`).

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md`

**Verificação:** (`DM-24`: comando em bloco cercado, `-SimpleMatch`, e os **dois** valores rodados; as baselines abaixo foram medidas no `ESC-7` com estes mesmos comandos) 1. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern '| `A8a` |' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0** — a célula não existe. 2. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'escalar não é desfecho de tarefa' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. 3. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'A8a' -SimpleMatch | Measure-Object).Count" ``` → **≥ 5** (a célula mais as quatro superfícies do produto (b)). **Medido antes: 0**. É esta linha que discrimina a entrega **completa** da entrega que só acrescenta a linha da tabela. 4. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern '`A8a`, `A8`, `A9` e `B1`' -SimpleMatch | Measure-Object).Count" ``` → **1** (a enumeração do Passo 7). **Medido antes: 0**. 5. `python -m pytest tests/ -q` → verde, **sem número fixo de piso** (`DM-23`): o piso é o total que a árvore tiver **no despacho**, re-medido por quem despacha; esta tarefa **não acrescenta teste** e **não pode reduzir** esse total. Referência histórica, não aceite: `165 passed` em 2026-09-19.

**Pronto quando:** a tabela do bloco A tem `A8a` entre `A7` e `A8`, com o texto literal acima; as quatro superfícies do produto (b) citam `A8a`; a frase do corpus medido está no parágrafo do bloco A; e as cinco linhas de `Verificação` saem como escritas.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` — despachada em 2026-09-19 pelo `scrum-master`. Era `ready` — card novo do `ESC-7` (2026-09-19), residência única do `AE-9`, que estava aberto desde a `LM-T1` com rota "matéria da `LM-T2`" e que a `LM-T2` **não podia** fechar: as `Restrições` dela mandavam o bloco A ficar intocado. Buraco de **alocação**, não de entrega — a `LM-T2` fechou `done` aprovada 100% exatamente por obedecer à restrição.
- **Esforço:** low
- **Depende de:** `LM-T2` (fechada — é a tabela dela que esta regra completa) e `DM-25`. **Precede a `LM-T4`**, que publica doutrina citando as tabelas de roteamento e tem o mesmo arquivo em `Arquivos-alvo`: publicar doutrina sobre um bloco A incompleto é a ordem invertida que a `DM-13` proíbe no eixo dela. As duas **não podem estar abertas ao mesmo tempo** sobre `.claude/skills/scrum-master/SKILL.md`.
- **Produto do módulo:** (a) a linha `A8a` na tabela do bloco A, com a precedência declarada; (b) as **quatro** superfícies do mesmo arquivo que enumeram as regras do bloco A postas em dia (Passo 7, gatilho do Passo 8, parágrafo do consumo do laudo, relatório de encerramento); (c) o corpus medido registrado em uma frase, para que a regra não pareça autorada de memória.
- **Fatos medidos no `ESC-7` (2026-09-19; re-derivar no despacho, o arquivo é da orquestração):** tabela do bloco A em `.claude/skills/scrum-master/SKILL.md:187-198`, com `A7` em `:196`, `A8` em `:197` e `A9` em `:198`; o parágrafo do consumo do laudo em `:199-204` (a enumeração ``` `A6`, `A7`..`A9` e `B1` ``` em `:203`); Passo 7 em `:124-128`, com a enumeração ``` lido por `A6`, `A8`, `A9` e `B1`. ``` quebrada entre `:126` e `:127`; gatilho do Passo 8 em `:132` (``` (regras `A1`..`A3b`) e passo 7 concluído (`A6`..`A9`) ```); relatório de encerramento em `:242`. **Baselines, com os comandos publicados abaixo:** `A8a` no arquivo → **0** ocorrências; a frase do produto (c) → **0**.
- **Corpus medido que a regra descreve (quatro ocorrências reais, janela de 2026-09-18/19):** `LM-T7` (veredito `ressalva`, 90%, bloqueante `nenhuma`, recomendação `escalar`), `LM-T3` (`ressalva` 91%), `LM-T2a` (`ressalva` 91%) e `LM-T2` (`aprovado` 100%). Em **todas** o `scrum-master` materializou o fechamento por julgamento próprio, porque a tabela não prescrevia o caso — improviso que a `DP-G` proíbe ("materializa **sem discricionariedade**"). Em nenhuma das quatro `bloqueante` era diferente de `nenhuma`; o caso `escalar` **com** bloqueante ainda não ocorreu, e é por isso que a regra o resolve por **precedência** (`A7` vence), e não por texto próprio. 1. Inserir na tabela do bloco A, **entre** a linha `A7` e a linha `A8`, a linha nova: ``` | `A8a` | `recomendacao=escalar` (com `bloqueante=nenhuma`) | **escalar não é desfecho de tarefa**: fecha o RDO pelo **veredito** transcrito — `aprovado` quando o veredito é `aprovado`, `aprovado com ressalva` quando é `ressalva` —, com cada achado do laudo saindo com rota, como em `A8`. A pendência **não** morre com o laudo: segue ao bloco B, onde o `B1` a registra como `AE-<n>` e a roteia ao consultor de plano. Precedência: `A6` e `A7` vencem esta regra — `bloqueante` diferente de `nenhuma` implica `veredito=reprovado`, que é `A7` —, e esta vence `A8` e `A9`, que leem a mesma recomendação | ``` 2. No Passo 7, substituir `lido por \`A6\`,` + quebra + `  \`A8\`, \`A9\` e \`B1\`.` por: ``` lido por `A6`, `A8a`, `A8`, `A9` e `B1`. ``` (a quebra de linha e a indentação de dois espaços são as do arquivo; só a lista muda). 3. No gatilho do Passo 8, trocar `passo 7 concluído (\`A6\`..\`A9\`)` por: ``` passo 7 concluído (`A6`..`A9`, inclusive `A8a`) ``` 4. No parágrafo que fecha o bloco A, trocar `\`A6\`, \`A7\`..\`A9\` e \`B1\`` por: ``` `A6`, `A7`..`A9` (inclusive `A8a`) e `B1` ``` e acrescentar, ao fim do mesmo parágrafo, a frase: ``` A `A8a` existe porque o caso foi medido **quatro vezes** na janela de 2026-09-18/19 (`LM-T7`, `LM-T3`, `LM-T2a` e `LM-T2`), todas com `bloqueante=nenhuma`, e em todas o loop materializou o fechamento **por julgamento próprio** — improviso que a `DP-G` proíbe. ``` 5. No relatório de encerramento, trocar `(\`A1\`..\`A9\` ou \`B0\`..\`B4\`, pelo identificador)` por: ``` (`A1`..`A9`, inclusive `A8a`, ou `B0`..`B4`, pelo identificador) ```
- **Testes:** **nenhum `pytest`** — declaração, não omissão (mesma razão da `LM-T2`, `AE-14`): a tabela do bloco A é prosa lida pelo `scrum-master`, sem sujeito executável. O que existe de executável nesta matéria já está trancado: `rdo.py close` aceita `--recomendacao "escalar"` como texto livre e calcula o desdobramento **pelo veredito**, que é exatamente o que a regra prescreve — nenhuma linha de código muda.
- **Restrições desta tarefa:** `A1`..`A3b`, `A6`, `A7`, `A8` e `A9` ficam **literais** — nenhuma condição e nenhuma ação delas muda; o que entra é uma linha nova e a precedência dela. O bloco B fica **intocado**: `B0` e `B1` são entrega fechada da `LM-T2` e já tratam a pendência. A numeração existente **não se renumera** — `A8a` é sufixo, pelo mesmo idioma de `LM-T4a`/`BKL-T2a`, justamente para não invalidar os identificadores já citados em RDOs e no diário.
- **Não fazer:** não tocar `.claude/tools/rdo.py` nem nenhum instrumento — a matéria é prosa e o `close` já faz o que a regra descreve; não tocar `GOVERNANCA.md` (é a `LM-T4`); não tocar `.claude/agents/` (`DM-17`); não escrever teste `pytest` para regra de prosa (`AE-14`); não commitar.
- **Contingências:** 1. se qualquer um dos cinco literais a substituir não existir no arquivo exatamente como transcrito (o arquivo é da orquestração e muda fora do ciclo) → parar e sinalizar `blocked` razão `premissa`, citando a linha encontrada; 2. se `python -m pytest tests/ -q` ficar vermelho → seguir com a entrega e devolver `contingência 2 acionada: <arquivo::teste> vermelho fora dos alvos` (esta tarefa não toca Python nenhum).

## Execução

**Consumo:** 11 tool uses, 56.6 k tokens, 65.8 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: Bloco A ainda incompleto para recomendacao=escalar: a tripla (reprovado, nenhuma, escalar) cai em A8a sem acao definida e o close a recusa, e escalar com bloqueante diferente de nenhuma com retentativas = 0 nao casa regra alguma - decidir no replanejamento antes da LM-T4.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
