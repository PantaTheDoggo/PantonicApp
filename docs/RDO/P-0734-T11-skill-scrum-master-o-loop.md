# RDO — P-0734 · T11

**Plano:** `docs/plans/P-0734-execucao-autonoma.md`
**Tarefa:** `T11` — Skill `scrum-master`: o loop
**Modelo:** Opus · **Classe:** redacao · **Teto:** 30
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** materializar o papel de orquestração como procedimento reexecutável (`DA-1`).

**Arquivos-alvo:** cria `.claude/skills/scrum-master/SKILL.md`; regenera `.claude/README.md`.

**Verificação:** bateria do §3; percurso a seco do fluxo sobre uma tarefa já fechada do `P-0733`, registrado na própria tarefa, sem executar nada.

**Pronto quando:** todo passo do fluxo tem gatilho, entrada e saída declarados, e nenhum passo depende de juízo não roteado.

**Dossiê fechado por:** `T2` (transporte) e `T3` (tabela de roteamento e tetos). **Não delegável antes das duas.**

**Extras (rótulos livres do plano, verbatim):**

- **Fluxo a escrever, na ordem:** gate de modelo do contexto principal (`modelo-por-fase`, `DA-8`) → seleção da próxima tarefa do plano, sempre sequencial, nunca em paralelo → gates herdados (`G-PLANREADY` e gate de delegação, **apontados**, nunca recopiados — a `T12` garante que existam num lugar só) → despacho do executor com o modelo declarado no plano → recepção do pacote de retorno pelo transporte da `T2` → despacho do reviewer → leitura do veredito → roteamento pela tabela da `T3` → arquivamento via `rdo.py close` → decisão de continuar ou encerrar a janela.
- **Encerramento de janela:** pelo proxy que a `T13` implementar, ou pelos tetos numéricos da `T3` enquanto não houver proxy — nunca por percepção de contexto, que o modelo não tem (§2, item 3).
- **Proibições:** o scrum-master não implementa, não julga entrega e não decide arquitetura; ponto de decisão do dono **para o loop** e o devolve.

## Execução

*(Preenchido pelo executor ao fechar a tarefa — campos fixos do pacote de retorno da `DP-A`,
`docs/plans/P-0734-execucao-autonoma.md` `### DP-A`. Teto total 44 linhas. Campo sem conteúdo é
preenchido com `nenhum` explícito; campo ausente é pacote inválido.)*

- **tarefa** (teto 1 linha):
- **status** (teto 1 linha — `entregue` | `parcial` | `bloqueado`):
- **arquivos_tocados** (teto 15 linhas — um por linha: caminho + `criado`/`editado`/`removido`):
- **desvios_do_dossie** (teto 8 linhas — o que o dossiê mandava e saiu diferente, com motivo; ou `nenhum`):
- **verificacao** (teto 6 linhas — cada comando da bateria do §3 com o exit code colado, não parafraseado):
- **achados** (teto 8 linhas — o que apareceu fora do escopo, cada um com rota: tíquete, ou `sem ação`):
- **orcamento** (teto 1 linha — `<teto declarado> x <tool uses gastos>`):
- **pendencia_para_o_dono** (teto 4 linhas — decisão de arquitetura/requisito levantada; ou `nenhuma`):

## Laudo

*(Calculado e gravado por `python .claude/tools/rdo.py laudo` — nunca redigido. Vazio até a
chamada do subcomando.)*
