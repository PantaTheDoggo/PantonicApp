---
name: modelo-por-fase
description: Gatilho operacional da regra "modelo por fase" (GOVERNANCA.md §3) — classifica a fase do trabalho (intelectual/execução/varredura), confere o modelo ativo contra a tabela vinculante e para para pedir o /model correto ao dono. Usar no início de qualquer tarefa/subagente, ao trocar de fase no meio de uma sessão, ou quando o hook global de nudge (UserPromptSubmit) disparar o aviso.
---

# modelo-por-fase — gatilho operacional do modelo por fase

A **regra** mora em `GOVERNANCA.md` §3 (tabela de agentes/modelo/responsabilidade) e §3.1
(residência e precedência da doutrina); o **enforcement automático** é o hook global
`~/.claude/hooks/modelo_por_fase_userpromptsubmit.py` (UserPromptSubmit, fora deste repo,
não versionado no kit). Esta skill é só o **gatilho manual** — não recopia a doutrina, aponta
para ela. Em caso de dúvida sobre a regra em si, `GOVERNANCA.md` §3 é a fonte, não este arquivo.

**Fato técnico já medido, não reinvestigar:** nenhum agente troca o próprio modelo em tempo de
execução — o schema de saída de hook não tem campo de modelo. Só o dono (`/model`) ou config
estática trocam. Esta skill institucionaliza a *parada* e o *pedido explícito*, nunca a troca em
si.

## Regra de decisão (fonte: `GOVERNANCA.md` §3)

| Fase | Modelo | Sinal típico |
|---|---|---|
| Intelectual (planejar/arquitetar/auditar/decidir/especificar) | Opus (Fable só sob pedido explícito do dono) | PRD, arquitetura, spec, decomposição, auditoria, parecer |
| Execução (implementar/editar/testar/corrigir) | Sonnet | Uma tarefa atômica do diário de obras, TDD |
| Varredura (search/grep/leitura ampla) | Haiku (ou subagente de coleta) | Levantar contexto antes de planejar/executar |

## Os três gatilhos

1. **Início de tarefa/sessão/subagente** — antes de decidir, implementar ou varrer, classifique a
   fase do trabalho que está prestes a começar e confira o modelo ativo contra a tabela acima.
2. **Troca de fase no meio da mesma sessão** — ex.: planejamento terminou, o próximo passo é
   implementar. Repita o gate; não herde o modelo da fase anterior por inércia.
3. **Nudge do hook global** — quando `modelo_por_fase_userpromptsubmit.py` emitir o aviso
   (`systemMessage` + `additionalContext`), esta skill é o procedimento que traduz o aviso em
   ação (passo "Gate de parada" abaixo). O hook é heurística de palavra-chave sobre o prompt do
   dono; esta skill cobre também os casos que o hook não vê (ex.: subagente sem hook rodando,
   troca de fase decidida pelo próprio agente sem novo prompt do dono).

## Gate de parada

Se o modelo ativo **não bate** com a fase:

- **Pare** — não prossiga a fase com o modelo errado (não decida sozinho, não assuma que "dessa
  vez tanto faz").
- **Peça** ao dono, de forma explícita, o comando `/model <opus|sonnet|haiku>` correspondente.
- Só o dono decide inverter a tabela para um agente de **execução** (custo caro em execução
  exige OK explícito e registrado — `GOVERNANCA.md` §3, penúltimo bullet). Para as demais fases
  não há inversão silenciosa possível: preferência genérica de memória não decide isso.
- Se o modelo já bate com a fase, siga sem ruído — o gate não é anúncio a cada turno.

## Convenção de anúncio (Regra 5, `~/.claude/CLAUDE.md`)

Depois de uma troca de modelo efetivada (`<local-command-stdout>` de "Set model to X" no
histórico), a **primeira resposta seguinte** abre com:

> 🟡 **Troca de modelo:** `modelo-anterior` → `modelo-novo`

Uma vez por troca — não repetir a cada turno enquanto o modelo permanecer o mesmo.

## Limites do hook (falsos positivos aceitos)

O hook classifica por palavra-chave sobre o **texto do prompt**, não sobre o trabalho real que o
turno vai fazer. Caso medido em 2026-07-30: o prompt de retomada de backlog ("execute a próxima
tarefa") disparava o nudge de "execução mecânica" (Sonnet), mas o trabalho real do turno era
orquestração + delegação (fase intelectual, Opus correto) — falso positivo corrigido nesta mesma
tarefa (`V2M-T2`) com uma lista de exclusão para frases de retomada de backlog/entrada de
slash-command (`proximo passo`, `proxima tarefa`, `execute a proxima`, `pegue o backlog` etc.),
checada antes da classificação de execução; essas frases agora resultam em silêncio (sem nudge),
consistente com o próprio princípio do hook ("sem sinal claro ⇒ silêncio").
Fora desse carve-out, a heurística continua sujeita a falsos positivos/negativos por natureza
(é palavra-chave, não intenção) — qualquer novo caso medido segue o mesmo tratamento: correção
barata e local no hook, ou registro aqui como aceito com motivo, nunca redesenho do classificador
por iniciativa do executor.
