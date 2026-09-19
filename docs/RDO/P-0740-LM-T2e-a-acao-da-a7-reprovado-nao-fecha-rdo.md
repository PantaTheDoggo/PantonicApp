# RDO — P-0740 · LM-T2e

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T2e` — A ação da `A7`: `reprovado` não fecha RDO
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — a última regra do bloco A que manda fazer o que o instrumento de fechamento recusa passa a materializar o desfecho pela via que a `DP-F` prevê, e a frase de partição que a `LM-T2d` escreveu no mesmo arquivo passa a ser verdadeira.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md`

**Verificação:** (`DM-24`: bloco cercado, `-SimpleMatch`, os **dois** valores rodados; as baselines abaixo foram medidas no `ESC-9` com estes mesmos comandos, extraídos deste card, e **nos dois mundos** — a árvore de hoje e uma cópia com a substituição do Passo 1 já aplicada. Os padrões evitam acento e crase **por recorte de subcadeia do texto real**, nunca reescrevendo palavra do arquivo: reescrever `última` como `ultima` produz padrão que casa **0 antes e 0 depois** e não mede nada — é o `AE-23`, achado no ato do despacho desta própria tarefa) 1. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'e retentativas gastas = 1 | fecha o RDO como' -SimpleMatch | Measure-Object).Count" ``` → **0** (a ação velha da `A7` desapareceu). **Medido antes: 1**. 2. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'desfecho de RDO' -SimpleMatch | Measure-Object).Count" ``` → **1** (a ação nova entrou). **Medido antes: 0**. 3. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'materializa a tarefa como' -SimpleMatch | Measure-Object).Count" ``` → **2** (`A6a` e `A7`). **Medido antes: 1**. É esta linha que discrimina a troca completa da que só apaga a ação velha. 4. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'retentativa (' -SimpleMatch | Measure-Object).Count" ``` → **1**, **inalterado** (`DM-32` (ii)): o único casamento é a linha 230, da seção *O que obriga parada* (``… última retentativa (`A7`); plano não-pronto (`B3`) …``), que esta tarefa **não** toca. **Medido antes: 1; medido depois: 1**, na cópia com a substituição do Passo 1 já aplicada — e o casamento é a **mesma linha 230** nos dois mundos, conferido. O padrão pega o acento pelo **que vem depois dele**, e por isso não o reescreve; a ação nova da `A7` também diz *"última retentativa"*, mas sem o parêntese — qualquer padrão sobre a expressão inteira iria a **2** e deixaria de ser invariante. 5. `python -m pytest tests/ -q` → verde, **sem número fixo de piso** (`DM-23`): o piso é o total que a árvore tiver **no despacho**, re-medido por quem despacha; esta tarefa não acrescenta teste e **não pode reduzir** esse total. Referência histórica, não aceite: `171 passed` em 2026-09-19 (`ESC-9`).

**Pronto quando:** a linha `A7` da tabela do bloco A traz o texto literal acima; nenhuma outra linha do arquivo mudou; e as cinco linhas de `Verificação` saem como escritas.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` (despachada em 2026-09-19) — card novo do `ESC-9` (2026-09-19), residência única do `AE-22` e do `DM-32`.
- **Esforço:** low
- **Depende de:** `LM-T2d` (fechada — é a frase de partição dela que esta tarefa torna verdadeira) e `DM-32`. **Precede a `LM-T4`**, pela mesma razão da `LM-T2c` e da `LM-T2d`: mesmo arquivo em `Arquivos-alvo` (exclusão mútua viva) e doutrina não se publica sobre tabela de roteamento que se contradiz.
- **Produto do módulo:** uma célula — a **ação** da linha `A7` da tabela do bloco A. A **condição** da `A7` não muda; nenhuma linha nova entra na tabela; nenhuma enumeração do arquivo muda, porque `A7` já é citada em todas.
- **O defeito, medido no `ESC-9` (2026-09-19):** a `A7` manda *"fecha o RDO como `reprovado`"* e o instrumento recusa esse desfecho em três pontos, os três re-medidos agora: `python .claude/tools/rdo.py close ... --veredito reprovado` sai **exit 2** (`argument --veredito: invalid choice: 'reprovado' (choose from 'aprovado', 'ressalva')`); `calcular_desdobramento('reprovado')` levanta `RdoValidationError: veredito inesperado: 'reprovado'`; e o gatilho do Passo 9 é a entrada em `done`, que `blocked`/`cancelled` não disparam (`DP-F` item 3, fechamento c). 1. Na tabela do bloco A, substituir a linha inteira ``` | `A7` | `veredito=reprovado` e retentativas gastas = 1 | fecha o RDO como `reprovado`: **PARA** | ``` por ``` | `A7` | `veredito=reprovado` e retentativas gastas = 1 | `reprovado` **não é desfecho de RDO** e esta regra **não** fecha RDO: o RDO só nasce na transição `review` → `done` (`DP-F` item 3, fechamento c), e `rdo.py close --veredito` aceita só `aprovado` e `ressalva` (medido: exit 2, `invalid choice`; `calcular_desdobramento('reprovado')` levanta `RdoValidationError`). Materializa a tarefa como `blocked` razão `premissa` — reprovada duas vezes, o que caiu foi a premissa de que o card é executável como está —, com o `bloqueante` e a pendência do laudo transcritos na razão, e registra o achado como `AE-<n>` em `## Achados da execução` do plano: **PARA**. A escalada é a do `A3b`: a reprovação depois da última retentativa é nomeada no relatório de encerramento e a rodada de replanejamento vira a próxima tarefa do plano (`G-REPLAN`, `GOVERNANCA.md` §7 item 17). Precedência: `A6` e `A6a` vencem esta regra; ela vence `A8a`, `A8` e `A9` | ``` — nada mais do arquivo muda.
- **Testes:** **nenhum `pytest`** — declaração, não omissão, pela mesma razão da `LM-T2c` e da `LM-T2d` (`AE-14`): tabela de roteamento é prosa lida pelo `scrum-master`. E **nenhuma linha de código**: o `--veredito` do `rdo.py close` continua com dois valores (`DM-32` (i)).
- **Restrições desta tarefa:** `A1`..`A3b`, `A6`, `A6a`, `A8a`, `A8` e `A9` ficam **literais** — só a **ação** da `A7` muda, e a **condição** dela fica como está. O bloco B fica **intocado**. A seção *O que obriga parada e o que segue com registro* fica **intocada**: a `A7` continua encerrando a janela. Nenhum instrumento é tocado — em particular, **não** se alarga o `--veredito` do `rdo.py close` (`DM-32` (i)).
- **Não fazer:** não tocar `.claude/tools/` (a lacuna se fecha na prosa, `DM-26` (iii) e `DM-32` (i)); não tocar `GOVERNANCA.md` (é a `LM-T4`; a menção a *reprovado* em `GOVERNANCA.md` §3, linha da *Orquestração*, é sobre a **retentativa** do `A6`, não sobre fechamento de RDO — medido, nada a corrigir lá); não tocar `.claude/agents/` (`DM-17`); não refazer a `LM-T2d`; não escrever teste `pytest` para regra de prosa; não commitar.
- **Contingências:** 1. se a linha literal da `A7` a substituir não existir no arquivo exatamente como transcrita → parar e sinalizar `blocked` razão `premissa`, citando a linha encontrada; 2. se `python -m pytest tests/ -q` ficar vermelho → seguir com a entrega e devolver `contingência 2 acionada: <arquivo::teste> vermelho fora dos alvos`.

## Execução

**Consumo:** 7 tool uses, 44.4 k tokens, 39.1 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

Transcricao literal exata (943 chars, byte a byte) da celula da A7; o bloco A fecha como particao verificada par a par: reprovado so alcanca A6/A6a/A7 (o gerador so emite refazer|escalar para reprovado, rdo.py:469-474), e nenhuma regra remanescente fecha RDO com veredito que o rdo.py close recusa. A frase de particao que a LM-T2d deixou no arquivo passou a ser verdadeira. Nota de coerencia sem defeito: a celula da A8a nao lista a A6a entre as que a vencem, mas as condicoes das duas sao disjuntas por veredito, entao a ordem entre elas e vazia.

## Fechamento

**Desdobramento:** aprovado
