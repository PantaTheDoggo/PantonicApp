---
name: diario-de-obras
description: Cria e mantém o diário de obras do projeto Pantonic* — kanban central em docs/DIARIO_DE_OBRAS.md com índice, status e arquivamento de planejamentos. Usar ao registrar um plano novo, abrir tíquete avulso, mudar status de tarefa ou condensar itens concluídos.
---

# diario-de-obras — kanban central do projeto

O diário de obras (`docs/DIARIO_DE_OBRAS.md`) é o documento centralizado onde todo planejamento
e tíquete avulso é arquivado, com identificação imediata do trabalho e seu status
(GOVERNANCA.md §4.2).

## Estrutura do documento

```markdown
# Diário de Obras — <projeto>

**Diretiva de priorização:** <vazio = heurística padrão | "Priorize <iniciativa/bug>">

## Índice
| ID | Título | Status | Âncora |
|---|---|---|---|
| S1-T3 | <título curto> | in progress | `## S1 — <sprint>` |
| TK-042 | <título curto> | backlog | `## TK-042` |

## <um heading `##` por sprint/tíquete, apêndice cronológico>
```

- **Status válidos:** `backlog`, `in progress`, `in review`, `blocked`, `done`, `cancelled`,
  `superseded`. Os três terminais são `done`, `cancelled` e `superseded` (todos condensam para o
  histórico): `done` = entregue e de pé; `cancelled` = nunca feito, descartado; `superseded` =
  feito ou parcial, porém tornado obsoleto por um entendimento novo — o trabalho pode sobreviver
  no código, a rota não. `superseded` sai do backlog (não é escolhível) como `done`/`cancelled`.
- **IDs:** `S<n>-T<m>` para tarefas de sprint; `TK-<seq>` para tíquetes avulsos.
- O índice fica **no topo** e tem UMA linha por item — é por ele que o executor localiza sua
  tarefa sem ler seções irrelevantes. Toda mudança de status atualiza índice E seção.
- **A célula "Título" do índice NUNCA recebe prosa de resultado de execução.** Handover de
  execução (skill `handover`) escreve o detalhe (o que foi feito, testes, consumo) na seção
  própria (`### <ID>` no diário) ou, para sprint que vive inteiramente em `docs/plans/P-*.md`
  (linha única no índice, sem heading no diário), numa seção do próprio plano (`## Notas de
  execução` / `## Achados da execução`) — nunca de volta na linha do índice. A célula do índice
  fica travada em ≤ ~1-2 frases + status + ponteiro, ponto final; se um handover for editá-la
  para além disso, é sinal de que falta a seção/satélite de destino — criar a seção, não apensar
  ao índice (defeito medido: `TK-DIARIO-SANEAMENTO`, célula de `SPRINT-REVEALENV` cresceu de
  ~2.5k para ~5k chars por handovers sucessivos apensando parágrafos). Mesmo mecanismo do
  "Guardrail anti-log-narrativo" abaixo, generalizado para toda tarefa — não só planos derivados.
- **Diretiva de priorização** é a linha imediatamente abaixo do título (GOVERNANCA §4.2). Guia a
  skill `proximo-passo` quando o usuário pede para seguir o backlog sem nomear tarefa. Vazia por
  padrão — heurística: destravar `blocked` → concluir `in progress` (WIP de 1 iniciativa por vez)
  → bugs → demais por FIFO (ordem de entrada no índice).
- **Sprints multi-tarefa** (`## SPRINT-<nome>`) têm, imediatamente abaixo do `**Objetivo:**`, a
  linha `**Próxima tarefa da sprint:** <ID> (<ponteiro ao dossiê>)` — atualizada a cada handover,
  ANTES das `**Notas de execução:**` (que crescem por apensamento a cada tarefa concluída).
  Heading + essa linha cabem num Read curto, sem varrer notas de execução potencialmente longas.

## Formato de uma tarefa atômica

```markdown
### S1-T3 — <título>  [status]
- **Objetivo:** <uma frase>
- **Arquivos-alvo:** <caminhos exatos>
- **Contratos/classes:** <Protocols, classes envolvidas>
- **Testes:** TF-<id> (novo), TR-<id> (tranca), suítes a rodar
- **Pronto quando:** <critério objetivo>
- **Notas de execução:** <≤ ~5 linhas + ponteiros (decision record, commit); preenchido pelo
  executor no handover — custo composto: nota extensa é relida por todo agente em toda tarefa
  futura>
```

## Operações

1. **Registrar plano** — apensar a seção do sprint com o checklist completo; inserir cada tarefa
   no índice como `backlog`.
   Plano que antecipa múltiplas rodadas de Q&A mantém tabela única "Decisões" (id → valor → 1
   linha) referenciada pelas seções, em vez de restatar cada regra em prosa em cada seção
   (reduz fan-out de Edits por rodada de confirmação).
2. **Mudar status** — atualizar a linha do índice e o `[status]` da seção; `blocked` exige razão
   registrada em "Notas de execução".
3. **Condensar** — quando itens `done`/`cancelled` dominarem o documento (ou ele passar de ~500
   linhas): (a) mover as seções concluídas para `docs/DIARIO_HISTORICO.md` (append-only), deixando
   no diário só a linha do índice com ponteiro; (b) se passar de 500 linhas mesmo assim, criar
   entrada no `docs/DOC_MAP.md`.
   Gatilhos adicionais: (c) uma única seção — mesmo `backlog` — que passe de ~300 linhas migra
   para arquivo satélite próprio (`docs/DIARIO_<ID>.md` ou `docs/audits/<ID>_LOG.md`,
   append-only), ficando no diário só a linha de índice + "última rodada: N / último achado:
   M"; (d) o dono do gatilho é o fechamento de cada tarefa (skill `handover`) — não existe
   "ninguém verifica". Tíquete acumulador (log de evidência que não fecha por desenho) nasce
   já como arquivo satélite + linha de índice, nunca como seção crescente do diário — também
   elimina colisão de append concorrente entre sessões.
4. **Registrar diretiva de priorização** — sobrescrever a linha "Diretiva de priorização" no
   topo do diário. Só acontece por pedido explícito do usuário (ex.: "Priorize iniciativa X",
   "priorize tarefas desse bug") — nunca inferida implicitamente de uma conversa. Ficar vazia
   quando o usuário não nomeou prioridade (heurística padrão assume).
5. **Drenar inbox de planos** — no início de qualquer sessão que vá tocar o diário (em especial
   ao abrir a skill `proximo-passo`), ler `docs/plans/_INBOX.md`. Cada linha não drenada aponta
   para um `docs/plans/P-<MMDD>-<slug>.md` gravado por um agente de planejamento (possivelmente em
   paralelo com outros); promover cada plano ainda não promovido para uma entrada no índice +
   heading do diário (ou manter o heading no próprio `docs/plans/P-*.md` com só a linha de índice
   apontando para lá, se o plano for grande), e marcar a linha do inbox como drenada (ex.:
   riscar/prefixar `[drenado]`) sem apagá-la — `_INBOX.md` é append-only.

## Planos derivados de uma investigação em curso (reconciliação obrigatória)

Uma iniciativa complexa gera descobertas, e cada descoberta tende a gerar um plano novo. O defeito
que isto governa: o plano novo passa a coexistir em silêncio com o de origem, e o executor volta a
"continuar" o plano de origem já superado — às vezes refazendo perguntas já respondidas. **No ato
de registrar um plano derivado**, classifique-o e aplique o efeito ao plano de origem. A
classificação é explícita e imediata, nunca fica implícita para "resolver depois":

- **(A) Fato novo que pode alterar o passo subsequente, mas ainda não substitui a rota** (uma
  verificação levantou uma hipótese que muda o próximo passo; a estratégia geral segue): o plano de
  origem vai para **`blocked`**, com razão registrada apontando o fato/plano novo. Não é escolhível
  até o fato ser resolvido. Destrava quando a hipótese é confirmada/descartada.
- **(B) Plano que muda completamente o entendimento do plano atual** (a premissa que o sustentava
  caiu; a rota agora é outra): o plano de origem inteiro vira **`superseded`** — obsoleto, fora do
  backlog, com ponteiro `substituído por: <plano novo>`. Código já entregue permanece; nenhuma
  tarefa nova sai dele. **Nunca deixar dois planos vivos disputando a mesma iniciativa.**
- **(C) Passo de verificação/validação enquanto há implementação pendente na mesma iniciativa**: a
  validação é **postergada** — registrada como `blocked` com razão `validação postergada até
  <tarefas de implementação> done`, e só volta a ser escolhível quando **todas** as implementações
  vivas fecharem. Não se abre rodada de validação enquanto existe implementação em aberto que possa
  invalidá-la (evita revalidar o que a próxima tarefa vai mudar).

**Regra de convergência:** uma iniciativa tem no máximo **UM** plano vivo (`backlog`/`in progress`/
`blocked` não-postergado) por vez. O plano vivo é sempre o mais recente cuja premissa não foi
contradita. Se ao drenar o inbox ou escolher tarefa você achar 2+ planos vivos na mesma iniciativa,
é sinal de que uma reconciliação A/B/C foi pulada: **rebasear antes de escolher** — marcar
`superseded` os planos cuja premissa a realidade atual contradiz, `blocked` os travados por fato
novo, e verificar se algum gap já foi tratado (por outra rota) mas ficou sem registro.

**Guardrail anti-log-narrativo:** uma célula da coluna "Título" do índice que vira **log de
descobertas sucessivas** é o mesmo defeito de uma seção que cresce demais — o gatilho de satélite
vale para ela: a saga migra para `docs/DIARIO_<ID>.md` (append-only), ficando no índice só **uma
frase** + status + ponteiro. Cada handover da saga escreve no satélite, nunca engorda a célula do
índice.

## Regras

- Grep pelo ID (`^### S1-T3` ou `^## TK-042`) antes de qualquer Read — nunca leia o diário
  inteiro.
- Nunca deletar itens: estados finais são `done` ou `cancelled`, e depois condensação para o
  histórico.
- Planos de agentes de planejamento paralelos nunca são escritos direto no diário: cada agente
  grava seu plano completo em `docs/plans/P-<MMDD>-<slug>.md` e apensa uma linha a
  `docs/plans/_INBOX.md` — evita conflito de edição concorrente no mesmo arquivo.
- Tíquete nascido de achado durante a execução de um plano vive na seção
  `## Achados da execução` apensada ao FINAL do próprio `docs/plans/P-*.md` (nunca fora do
  plano); o diário guarda só a linha de índice com âncora para lá. `TK-*` com seção no diário
  é reservado a demanda sem plano de origem. A sprint só flipa para `done` com todos os
  achados do plano triados (rota registrada) — ver skill `handover` §2.
