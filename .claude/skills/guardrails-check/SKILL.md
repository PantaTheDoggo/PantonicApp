---
name: guardrails-check
description: Verifica os guardrails de clean architecture de um projeto Pantonic* antes de marcar uma tarefa como concluída — regra de camadas, ACL, MVVM, egress G6, namespace de estado, conformance e piso de regressão. Usar ao final de toda tarefa de execução ou em auditoria.
---

# guardrails-check — gate de qualidade Pantonic*

Rodar ao final de toda tarefa (obrigatório antes de `in review`/`done`) ou sob demanda em
auditoria. Referências: GOVERNANCA.md §7, ARQUITETURA_PANTONICA.md §1, §13.

## Checklist executável

1. **Tier 1 (durante a tarefa)** — só os dirs de teste que a mudança toca
   (`/lean-test tests/<area> -x`); skill `test-tiers` deriva o subconjunto do
   `git diff --name-only` quando o mapeamento não for óbvio.
2. **Tier 2 (ao fechar a tarefa, obrigatório)** — dirs do Tier 1 + `tests/conformance/` (regra
   de camadas por AST, ACL, mirror drift, allowlist de imports de plugins) — bloqueante, nunca
   waivable.
3. **Boundary** — `tests/boundary/`: namespace de estado (`plugins.<nome>.*`), quando a tarefa
   tocar estado de plugin.
4. **Tier 3 (piso de regressão completo — gate de sprint/fase, não de toda tarefa)** — a suíte
   inteira via `/lean-test` sem args, com a contagem de verdes comparada ao piso registrado
   (diário de obras / doc AS-IS). Roda de fato quando: (b) é a última tarefa do sprint/fase
   (gate de fechamento já previsto no próprio plano); ou (c) o usuário pedir um passe completo.
   Quando (a) a tarefa toca `contracts/`, `infracore/` ou serviço compartilhado (alto raio de
   explosão), o executor **não** roda Tier 3 por conta própria — decidir rodar é prerrogativa do
   dono/orquestrador (`CLAUDE.md` global, Regra 7; `integration-executor` R-3); o executor só
   **recomenda** o passe completo no handover, com a razão (raio de explosão). Nas demais
   tarefas o gate é Tier 2, e o piso é conferido no gate de sprint. Piso subiu → nada a fazer;
   desceu → tarefa **não está pronta**.
5. **Kit agêntico (projeto que tem `.claude/checks/kit_check.ps1`) — bloqueante como o Tier 2** —
   `pwsh .claude/checks/kit_check.ps1 -Mode validate` (estrutura do kit + paridade
   `VERSION` == `.claude/KIT_VERSION`) e `pwsh .claude/checks/kit_check.ps1 -Mode check-drift`
   (índice derivado `.claude/README.md` versus o disco); ambos precisam sair `0`. Deriva →
   regenerar com `-Mode generate`, **nunca** editar o `.claude/README.md` à mão
   (`GOVERNANCA.md` §9).

Sempre `/lean-test` (ou skill `lean-test`) — saída filtrada (só falhas + sumário) — nunca
`pytest` puro despejando o log inteiro no contexto (`CLAUDE.md` global, Regra 3).

## Checklist de review (o que AST não pega)

- [ ] Import novo respeita a direção `infracore ← contracts ← services ← plugins`?
- [ ] Dependência externa nova está confinada a UM serviço com Protocol em `contracts/`?
- [ ] ViewModel continua QtCore-only? Model continua sem Qt? Geometria/estilo/`QScreen` só na
      shell (`infracore/ui_shell/`)?
- [ ] Nenhum trabalho pesado no UI thread (tudo via `task_runner_service`)?
- [ ] Sinais usados só para observação (sem polling)? Payload é Pydantic `extra="forbid"`?
- [ ] Tipo que cruza camadas foi espelhado verbatim em `contracts/` (mirror discipline)?
- [ ] Nenhum teste deletado às cegas — teste com significado alterado foi reescrito?
- [ ] Mudança comportamental intencional tem decision record (`D-*`) no doc AS-IS?

## Padrão de código (limiares canônicos)

Lar canônico dos limiares numéricos de clean code — outros agentes (auditor de arquitetura,
executor, agente de refactor) **referenciam** esta seção em vez de repetir os números; mudar um
limiar é editar só aqui.

- **Automático (ruff — gate de conformance):** complexidade ciclomática (`C901`,
  `max-complexity=10`), imports/variáveis mortos (`F401`/`F841`), comprimento de linha (`E501`).
  Cobre também o que seria "função >40 linhas" e boa parte de PEP 8 — redundante manter como
  item manual separado; o gate de complexidade já pega a mesma forma de função problemática.
  Uma violação nova vira `# noqa` pontual + decision record, nunca supressão silenciosa.
- **Manual (não capturado por AST/ruff — checklist de review, citar `path:line`):**
  - Classe com **>7 métodos públicos**.
  - Duplicação de lógica **≥6 linhas** entre arquivos novos/tocados.

## Veredito

Todo item do checklist de review marcado como **desvio** cita `path:line` da evidência — um
desvio sem `path:line` é rubber-stamping, não veredito. Colar o bloco abaixo (preenchido) nas
"Notas de execução" da tarefa no diário de obras:

```
Veredito — <ID da tarefa>
Suítes: <tier rodado, ex. "Tier 2 (tests/conformance/)"> — <resultado, ex. "59 verdes">
  <se o piso completo não rodou: por qual critério ficou para o gate de sprint; se a tarefa
  tocou contracts/, infracore/ ou serviço compartilhado — critério (a) — recomendação de passe
  completo para o dono/orquestrador decidir>
Piso: <antes> → <depois> (ou "sem mudança de piso")
Kit: <kit_check -Mode validate / -Mode check-drift — exit 0 | n/a (projeto sem kit_check.ps1)>
Checklist de review: <ok | desvio path:line — descrição> (uma linha por item verificado)
```

**Qualquer item vermelho = tarefa não concluída** — registrar no diário de obras (`blocked` ou
permanece `in progress`) com a razão.
