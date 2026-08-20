---
name: guardrails-check
description: Verifica os guardrails de clean architecture de um projeto Pantonic* antes de marcar uma tarefa como concluída — regra de camadas, ACL, egress G6, namespace de estado, conformance e piso de regressão. Usar ao final de toda tarefa de execução ou em auditoria.
---

# guardrails-check — gate de qualidade Pantonic*

Rodar ao final de toda tarefa (obrigatório antes de sinalizar `review`) ou sob demanda em
auditoria. Referências: GOVERNANCA.md §7, ARQUITETURA_PANTONICA.md §1, §12.

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
   inteira via `/lean-test` sem args. O piso é o conjunto de **comportamentos trancados**
   (`GOVERNANCA.md` §4.4), nunca contagem de verdes nem percentual de cobertura — ver item 7
   para o comando que prova isso. Roda de fato quando: (b) é a última tarefa do sprint/fase
   (gate de fechamento já previsto no próprio plano); ou (c) o usuário pedir um passe completo.
   Quando (a) a tarefa toca `contracts/`, `infracore/` ou serviço compartilhado (alto raio de
   explosão), o executor **não** roda Tier 3 por conta própria — decidir rodar é prerrogativa do
   dono/orquestrador (`CLAUDE.md` global, Regra 7); o executor só **recomenda** o passe completo
   no sinal de retorno, com a razão (raio de explosão). Nas demais
   tarefas o gate é Tier 2, e o piso é conferido no gate de sprint. Nenhum comportamento
   trancado perdido → nada a fazer; comportamento perdido → tarefa **não está pronta**.
5. **Kit agêntico (projeto que tem `.claude/checks/kit_check.ps1`) — bloqueante como o Tier 2** —
   `pwsh .claude/checks/kit_check.ps1 -Mode validate` (estrutura do kit + paridade
   `VERSION` == `.claude/KIT_VERSION`) e `pwsh .claude/checks/kit_check.ps1 -Mode check-drift`
   (índice derivado `.claude/README.md` versus o disco); ambos precisam sair `0`. Deriva →
   regenerar com `-Mode generate`, **nunca** editar o `.claude/README.md` à mão
   (`GOVERNANCA.md` §9).
6. **Código morto testado (`.claude/checks/dead_code.py`) — bloqueante, mesmo padrão do item 5** —
   `python .claude/checks/dead_code.py` (usa o `--root` default do próprio projeto); exit 0
   obrigatório. Cobertura por teste não confere "vivo" (`GOVERNANCA.md` §7, G-DEADCODE) — um
   achado é órfão real (remover no mesmo commit) ou dispatch dinâmico ainda não coberto pelas
   categorias auto-vivas do script (Pydantic validator, entry class de `manifest.json`, override
   de virtual do toolkit da camada de apresentação declarado pelo projeto), nunca allowlist de
   conveniência.
7. **Ratchet do piso comportamental (`.claude/checks/ratchet_piso.py`) — bloqueante, mesmo
   padrão dos itens 5 e 6** — `python .claude/checks/ratchet_piso.py` (usa o `--root` default do
   próprio projeto; consumidor versiona `tests/piso_comportamental.txt`, uma linha por
   comportamento trancado no formato `<pytest nodeid> — <comportamento em uma frase>`,
   `GOVERNANCA.md` §4.4). Compara a lista com `pytest --collect-only -q` e falha nomeando o
   comportamento perdido quando um nodeid do piso desapareceu da coleta; arquivo de piso ausente
   é OK explícito (consumidor que ainda não adotou não quebra o gate), nunca silêncio por engano.

8. **Guarda de drift do README espelho (projeto que tem `.claude/checks/check-readme.ps1`) —
   bloqueante como os itens 5-7** — `pwsh .claude/checks/check-readme.ps1`; exit 0 obrigatório.
   Verifica, tudo mecânico: todo agente/skill em disco aparece no README §7 e vice-versa; a versão
   citada no README (cabeçalho + §12) é igual a `VERSION` e a `.claude/KIT_VERSION`; o número de
   guardrails do README §8 é igual ao de `GOVERNANCA.md` §7; toda seção `## ` do README tem
   `> Fonte da verdade:` apontando para um arquivo que existe. Falha nomeando a divergência exata
   (agente/skill fora de sincronia, versão divergente, contagem de guardrails, seção sem fonte ou
   fonte inexistente) — nunca editar o README à mão para "consertar" o gate; o README é que está
   desatualizado.

Sempre `/lean-test` (ou skill `lean-test`) — saída filtrada (só falhas + sumário) — nunca
`pytest` puro despejando o log inteiro no contexto (`CLAUDE.md` global, Regra 3).

## Checklist de review (o que AST não pega)

- [ ] Import novo respeita a direção `infracore ← contracts ← services ← plugins`?
- [ ] Dependência externa nova está confinada a UM serviço com Protocol em `contracts/`?
- [ ] Nenhum trabalho pesado na thread que atende a superfície de entrada (tudo pela porta de
      execução assíncrona, via `task_runner_service`)?
- [ ] Sinais usados só para observação (sem polling)? Payload é Pydantic `extra="forbid"`?
- [ ] Tipo que cruza camadas foi espelhado verbatim em `contracts/` (mirror discipline)?
- [ ] Nenhum teste deletado às cegas — teste com significado alterado foi reescrito?
- [ ] Mudança comportamental intencional tem decision record (`D-*`) no doc AS-IS?

## Padrão de código (limiares canônicos)

Lar canônico dos limiares numéricos de clean code — outros agentes (auditor de arquitetura,
auditor de clean code, executor) **referenciam** esta seção em vez de repetir os números; mudar um
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
desvio sem `path:line` é rubber-stamping, não veredito. Colar o bloco abaixo (preenchido) no
retorno de fechamento de quem rodou o gate — o sinal da execução, ou o relatório da auditoria:

```
Veredito — <ID da tarefa>
Suítes: <tier rodado, ex. "Tier 2 (tests/conformance/)"> — <resultado, ex. "59 verdes">
  <se o piso completo não rodou: por qual critério ficou para o gate de sprint; se a tarefa
  tocou contracts/, infracore/ ou serviço compartilhado — critério (a) — recomendação de passe
  completo para o dono/orquestrador decidir>
Piso: <ratchet_piso.py — OK | comportamento(s) perdido(s) nomeados> (ou "sem piso declarado")
Kit: <kit_check -Mode validate / -Mode check-drift — exit 0 | n/a (projeto sem kit_check.ps1)>
Espelho: <check-readme.ps1 — exit 0 | divergência(s) nomeada(s) | n/a (projeto sem check-readme.ps1)>
Checklist de review: <ok | desvio path:line — descrição> (uma linha por item verificado)
```

**Qualquer item vermelho = tarefa não concluída** — sinalizar `blocked` com a razão tipada, em
vez de `review`.
