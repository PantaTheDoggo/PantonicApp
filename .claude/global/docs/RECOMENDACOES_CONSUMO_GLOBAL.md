# Recomendações globais — governança de consumo (tokens E turnos)

**Origem:** auditoria do consumo da tarefa R6 do PantonicVideo (2026-07-08), que gastou ~30% do
limite de 5h numa única tarefa atômica. Case: executor subagente com **71 chamadas de ferramenta**,
contexto final ~189k tokens, ~19 min, rodando em **Opus**.

**Destino:** propagar para o CLAUDE.md global e para o kit agêntico Pantonic* reusável
(`D:\workspaces\PantonicApp\.claude\`, `GOVERNANCA.md`).

---

## 1. A equação de custo que a governança atual só ataca pela metade

```
custo total ≈ Σ por turno ( tamanho do contexto re-enviado × peso do modelo )
```

Três fatores multiplicativos: **tamanho do contexto**, **número de turnos**, **peso do modelo**.

- As Regras 3 e 4 atuais (economia de contexto, onboarding econômico) atacam **só o primeiro
  fator** — e funcionam: no case R6, o lado orquestrador foi barato (~8 chamadas cirúrgicas).
- O **número de turnos** não é citado por nenhuma regra, skill ou agente (verificado por grep em
  2026-07-08: as únicas menções a paralelismo são sobre spawns de agentes de planejamento).
- O **peso do modelo** está governado de forma contraditória (ver §2).

Cada turno re-envia o contexto acumulado inteiro. Um executor com 71 turnos sobre um contexto que
cresce até 189k re-envia, mesmo com cache, milhões de token-equivalentes. Reduzir o contexto por
turno sem governar o número de turnos deixa a maior alavanca solta.

## 2. Falha de premissa: modelo por fase deve valer também para subagentes

A Regra 1 global existe para que o modelo caro (Opus) planeje e o barato (Sonnet) execute. Mas a
atribuição de `model:` nos arquivos de agente pode inverter isso silenciosamente — no case, o
`pantonic-executor` (fase de **execução**, a mais token-intensiva) rodava em Opus por uma memória
de preferência (`feedback_opus_default`), contradizendo frontalmente o racional da Regra 1.

**Regra proposta:** o `model:` de um agente segue a **fase** dele, não uma preferência geral:
- Planejamento, auditoria, arquitetura → modelo caro (Opus) se o dono quiser.
- Execução (implementar, testar, editar) → modelo de execução (Sonnet), salvo tarefa
  individualmente marcada como de alto risco.
- Exploração/varredura → modelo barato (Haiku, ex.: context-scout).

Toda exceção é explícita no arquivo do agente **com o racional de custo confrontado com a
Regra 1**, nunca herdada de uma preferência genérica.

## 3. Falha de premissa: "delegar economiza tokens"

Delegação protege a **qualidade** do contexto do orquestrador (Regra 2) — não reduz consumo
total. O subagente parte frio e re-deriva contexto (CLAUDE.md, definição do agente, docs, código),
e cada skill carregada dentro dele é re-cobrada em todos os turnos seguintes.

**Regras propostas:**
- Contabilizar delegação como higiene de contexto, nunca como economia.
- Tarefa pequena (estimativa < ~15 turnos) → preferir execução inline num contexto novo
  (`/clear` + executar direto) em vez de subagente.
- O dossiê completo na delegação continua correto (evita re-descoberta), mas **não repetir no
  prompt o que já está nos "fatos estáveis" do arquivo do agente** — isso é pago duas vezes.

## 4. Lacuna nova — Regra proposta: economia de turnos

Candidata a "Regra 7" do CLAUDE.md global e a seção nova da GOVERNANCA do kit:

1. **Batching de chamadas independentes.** Leituras/greps sem dependência entre si vão na mesma
   mensagem (múltiplas tool calls por turno). N leituras em 1 turno custam 1 re-envio de
   contexto; em N turnos custam N re-envios.
2. **Cadência de testes, não só tier.** Os tiers governam *o quê* rodar; falta governar *quantas
   vezes*. Padrão: Tier 1 no máximo 2× por tarefa (após implementar; após corrigir) — nunca após
   cada micro-edição. Tier superior só no fechamento.
3. **Sem re-leitura de verificação.** Edit/Write falham ruidosamente; re-ler o arquivo editado
   "para conferir" é um turno inteiro desperdiçado.
4. **Orçamento de turnos por tarefa atômica.** Faixa esperada: ~≤40 tool uses. Estourar não é
   punição — é sinal de que a tarefa não era atômica (replanejar a decomposição) ou de método
   ruim (thrashing editar-testar-editar sem plano interno).
5. **Plano interno antes de editar.** Executor esboça a sequência de edições antes da primeira —
   reduz turnos de retrabalho.
6. **Cerimônia de fechamento enxuta.** Um único registro canônico (diário); relatório final =
   ponteiro + deltas, nunca o mesmo conteúdo duas vezes. Skills de fechamento carregadas dentro
   do subagente devem ser mínimas.

## 5. Lacuna de observabilidade: ninguém mede

O dono só percebeu o estouro pelo limite de 5h. O orquestrador **recebe** telemetria de cada
subagente concluído (tool uses, tokens, duração) e hoje a descarta.

**Regra proposta:** toda linha de handover/nota de diário registra
`Consumo: <N> tool uses, ~<X>k tokens, <modelo>`. Cria a série histórica que permite detectar
regressão de consumo por tarefa — mesmo racional do piso de regressão de testes, aplicado a custo.

## 6. Custo composto de docs vivos verbosos

Nota de execução extensa em doc vivo (diário, planning) é re-lida por **todo agente em toda
tarefa futura** — é a versão em docs do problema que a governança de memórias já resolve.
**Regra proposta:** nota de execução ≤ ~5 linhas + ponteiro (decision record, commit); operação
de condensação disparada por gatilho objetivo (contagem de linhas), não por juízo.
