---
name: handover
description: Encerra uma tarefa Pantonic* com handover limpo — atualiza o diário de obras, registra estado e prepara a troca de contexto. Usar ao concluir, bloquear ou interromper qualquer tarefa; nunca iniciar outra tarefa no mesmo contexto.
---

# handover — encerramento de tarefa e troca de contexto

Regra de ouro (`~/.claude/CLAUDE.md` Regra 2; `GOVERNANCA.md` §4.3 no hub do kit): **uma tarefa
por contexto**. Toda tarefa termina com este fluxo; a próxima tarefa começa em contexto limpo,
invocada pelo usuário.

## Fluxo

1. **Gate** — se a tarefa está sendo dada como concluída, a skill `guardrails-check` já deve
   ter passado (Tier 2 no mínimo — dirs tocados + `tests/conformance/` verde; Tier 3 completo só
   quando a própria tarefa/sprint exigir, ver skill `guardrails-check`). Sem gate verde, o
   destino é `blocked` ou permanece `in progress`, nunca `done`.

2. **Atualizar o diário de obras** (skill `diario-de-obras`):
   - Status: `in review` (pronto para validação do usuário), `done` (validado/trivial),
     `blocked` (com razão) ou `in progress` (interrompida — anotar ponto de parada).
   - Preencher "Notas de execução" da tarefa (≤ ~5 linhas + ponteiros): o que foi feito, arquivos
     tocados (`caminho:linha`), o **comando de verificação colado do terminal** (não a intenção de
     verificar — `GOVERNANCA.md` §4.2) com os testes criados (TF/TR), desvios do plano, piso de
     regressão anterior × atual.
     **Nunca na célula do índice** (guardrail generalizado em `diario-de-obras`): se a tarefa
     pertence a um `### <ID>` do diário, o destino é a "Notas de execução" daquela seção; se a
     sprint vive inteiramente em `docs/plans/P-*.md` (índice com linha única, sem heading no
     diário), o destino é uma seção do próprio plano — a célula do índice fica travada em
     status + ≤ ~1-2 frases + ponteiro. Registrar também
     `Consumo: ver docs/telemetria.tsv` — **ponteiro, nunca o número em prosa**. A
     medida vai como uma linha nova em `docs/telemetria.tsv` (`data`, `projeto`, `tarefa`,
     `modelo`, `tool_uses`, `tokens_k`, `duracao_s`, `fonte`), apendada pelo **orquestrador** a
     partir do bloco `<usage>` da notificação de conclusão do subagente (`fonte: usage`), nunca
     por estimativa do próprio subagente no texto do handover (auto-relato subestima o consumo
     real). Execução inline, sem bloco `<usage>` a ler, entra com `fonte: contado`; consumo
     perdido com a sessão, com `fonte: nao_medido`. Se este fluxo roda dentro do subagente antes
     de retornar, deixar o placeholder e o orquestrador escreve a linha da série ao processar a
     notificação (`GOVERNANCA.md` §4.2).
   - **Dono do gatilho de condensação:** se o diário exceder ~500 linhas OU o bullet
     recém-escrito exceder ~10 linhas, rodar a operação Condensar (skill `diario-de-obras`) na
     mesma sessão — nota longa vale 1 leitura, ponteiro vale para sempre. O flip de status da
     sprint (`backlog`↔`in progress`↔`done`) acompanha o início/fim de suas tarefas — índice
     nunca defasado do WIP real.
   - **Achado fora de escopo com ação futura** (falha de teste pré-existente OU risco/
     recomendação registrado só em decision record/prosa) vira, NA MESMA SESSÃO: (a) entrada
     apensada à seção `## Achados da execução` ao FINAL do plano de origem
     (`docs/plans/P-*.md` — apenso é permitido; o corpo do plano segue imutável), com o
     contexto que o motivou (tarefa de origem, evidência, por que pode ser pertinente), e
     (b) linha de índice no diário com âncora apontando para essa seção do plano. Nota em
     prosa não satisfaz o guardrail; piso vermelho não indexado transfere a forense para o
     próximo gate. `TK-*` solto (seção no próprio diário) só quando a tarefa de origem for
     avulsa, sem plano-pai — decisão do dono 2026-07-16: achado fora do plano perde o
     contexto e vira pilha indecidível quando o plano acaba.
   - **Gate de triagem no fechamento de sprint:** o flip da sprint para `done` exige triagem
     da seção `## Achados da execução` do plano — cada achado sai com rota: (a) tarefa em
     plano derivado, (b) decisão do dono (`AskUserQuestion` em lote, 1 round-trip), ou
     (c) rejeitado com razão de 1 linha na própria entrada. Sprint não fecha com achado sem
     rota.
   - **Nota-forward de obsolescência:** obsolescência de plano/audit descoberta na execução
     (arquivo movido, contagem mudada, escopo invalidado) que afete tarefas RESTANTES do mesmo
     plano é registrada junto à sugestão de próxima tarefa — o plano histórico não se edita; a
     nota do diário é o canal vivo.

3. **Registrar decisões e lições** (se houver):
   - Mudança comportamental intencional → decision record `D-*` no doc AS-IS.
   - Incidente com diagnóstico não-óbvio → entrada no doc de lições aprendidas.

4. **Mensagem de handover ao usuário** (última saída do contexto, ≤ ~15 linhas) — **ponteiro +
   deltas, nunca repete o conteúdo já escrito no diário** (o diário é o registro canônico; pagar
   o mesmo texto duas vezes é custo composto sem benefício):
   - Tarefa e status final; o que validar e como (comando/fluxo de teste manual, se aplicável).
   - Iniciativa/plano de origem da tarefa (sprint no diário, ou "tíquete avulso").
   - **Índice de conclusão do plano**: `<done>/<total>` tarefas daquele plano no índice do
     diário (contar as linhas com a mesma âncora), com percentual. Se a tarefa era um tíquete
     avulso, omitir este item.
   - Próxima tarefa sugerida do diário (ID + título), SEM iniciá-la.
   - Recomendação explícita: limpar o contexto (`/clear` ou nova sessão) antes de invocar a
     próxima tarefa. Se a statusline indicar contexto alto (⚠️/🔴), a limpeza é obrigatória,
     não sugestão — diga isso.

## Checkpoint intermediário (contexto acabando **sem** plano de parada)

O handover acima fecha uma tarefa que chegou ao fim. O checkpoint é outra coisa: a tarefa **não**
acabou e o contexto vai acabar antes dela. Sem ele, a descoberta já paga (onde está o código, o
que já foi decidido, o que já foi descartado) morre com o contexto e o próximo contexto a
reexecuta do zero — pagando duas vezes pelo mesmo achado.

O checkpoint é **ponteiro de estado, não relatório intermediário**: não narra o que foi feito, não
justifica decisões, não repete o que já está no diário ou no plano. Ele existe para que outro
contexto retome sem redescobrir.

- **Gatilho** — o consumo cruza **2/3 do teto da classe** da tarefa (tabela de classes em
  `GOVERNANCA.md` §3): ≤15 → **10**; ≤40 → **27**; ≤60 → **40**; ≤30 → **20**; classe
  investigação → 2/3 do teto prescrito no dossiê. Também dispara **antes** disso se o executor
  concluir, por qualquer motivo, que vai estourar. Não esperar o estouro: no estouro já não há
  orçamento para escrever o checkpoint.
- **Entregável** — até **5 linhas** no diário, na "Notas de execução" da tarefa em curso, uma
  linha por item:
  1. o que já está **descoberto e decidido** (inclusive rotas descartadas — descarte é achado);
  2. o que **falta**;
  3. **arquivos tocados**, com `caminho:linha`;
  4. o **próximo passo exato** (a ação seguinte, não o objetivo da tarefa);
  5. o que **não precisa ser refeito**.
- **Teto do próprio checkpoint: 2 tool uses** — um `Grep` para achar a âncora da tarefa e um
  `Edit`. O checkpoint tem de custar menos que a descoberta que preserva; se está custando mais
  que 2 chamadas, ele virou relatório e perdeu a razão de existir. Sem releitura de verificação,
  sem varredura para "completar" o estado.
- Depois de escrever o checkpoint, a tarefa fica `in progress` com o ponto de parada anotado —
  nunca `done`, nunca `blocked` (não há impedimento externo; acabou o orçamento).

**Exemplo (caso real da `proximo-passo`: subagente caiu sem bloco `<usage>`)** — cinco linhas:

> Descoberto/decidido: rota A confirmada; rota B descartada (não suporta X). · Falta: aplicar o
> mesmo ajuste aos 2 call sites restantes. · Tocados: `src/foo/bar.py:112-140`,
> `tests/test_bar.py:88`. · Próximo passo: editar `src/foo/baz.py:57` no mesmo padrão de
> `bar.py:118`. · Não refazer: o mapeamento de call sites (grep já rodado, 3 achados) e a escolha
> da rota A.

## Trava de contexto (vale para QUALQUER agente, não só o executor)

Depois do handover, se o usuário pedir a próxima tarefa **no mesmo contexto**, não inicie:
responda com o ID/título da tarefa, repita a recomendação de `/clear` (ou `/compact`) e
aguarde. A trava só cai se o usuário, já avisado, insistir explicitamente em seguir no mesmo
contexto.

Se o orquestrador detectar que já fechou ≥2 entregáveis distintos na mesma janela sem passar
por handover (dono emendando instruções), emitir por conta própria o aviso "múltiplas tarefas
concluídas nesta janela — recomenda-se `/compact`" — não depender de o dono lembrar.

## Proibições

- Iniciar outra tarefa no mesmo contexto, mesmo que "pequena" — inclusive pelo agente
  principal, fora do executor.
- Marcar `done` com conformance vermelho ou piso de regressão abaixo do registrado.
- Deixar o diário desatualizado — o diário é a única fonte de verdade de status; se o handover
  não o atualizou, o handover não aconteceu.
