# Evidência de revisão — P-0755 RAF-T40

## Diff (`git diff --stat`)
```
README.md                                          | 47 +++++++++++++---------
 docs/DIARIO_DE_OBRAS.md                            |  4 +-
 .../estado.tsv                                     |  2 +-
 .../evidencia/P-0755-RAF-T40-medida-depois.json    | 15 +++++++
 docs/telemetria.tsv                                |  1 +
 5 files changed, 48 insertions(+), 21 deletions(-)
```

## Arquivos tocados
- `README.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: registro da orquestração; estado git: ` M`
- `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv` — atribuição: registro da orquestração; estado git: `??`
- `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T40-medida-depois.json` — atribuição: registro da orquestração; estado git: `??`
- `docs/telemetria.tsv` — atribuição: registro da orquestração; estado git: ` M`

## Escopo
- Recorte: desde `3ad4182ff09171fb549b970a7c593beaf43ec1a2`
- Arquivos-alvo declarados: `README.md`
- Arquivos tocados: `README.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T40-medida-depois.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0755-recomendacoes-auditoria-final/estado.tsv`, `docs/plans/P-0755-recomendacoes-auditoria-final/evidencia/P-0755-RAF-T40-medida-depois.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `README.md`
```
diff --git a/README.md b/README.md
index 28afa3f..fc9cb4e 100644
--- a/README.md
+++ b/README.md
@@ -473,7 +473,7 @@ cada transição do loop, com o título da tarefa — do card de plano ou do tí
 ferramenta entre duas linhas; as frases estão na seção *Repertório de mensagens ao gerente* da
 `scrum-master`. Para abrir o painel, no terminal integrado do VS Code, na raiz do repositório:
 `Get-Content -Path .claude/estado/progresso.txt -Wait -Tail 30 -Encoding utf8` (o arquivo nasce
-com a primeira linha gerada). No fim da janela, o gerente lê um relatório. A transição
+com a primeira linha gerada). No fim da janela, o gerente lê um relatório. O loop de um plano recém-planejado abre numa janela nova, com o plano gravado como único insumo: a janela que planejou encerra no Marco 1. A transição
 entre uma tarefa e a seguinte é maquinário interno do loop; os cinco passos abaixo são a parte dela
 que o gerente precisa conhecer para argumentar sobre o fluxo. FIFO aparece só no fim do segundo
 passo, como último desempate.
@@ -508,7 +508,7 @@ são **re-derivados por um comando barato agora**, nunca copiados do plano, porq
 dentro da própria sprint; string destinada a `assert` é citação colada do output, nunca paráfrase; e a
 divisão se decide **por assunto, não por volume** — um card se parte quando cruza dois assuntos, nunca
 quando cruza muitas regiões do mesmo assunto. O gate `G-PLANREADY` precede todas: tarefa de plano
-aberto é devolvida ao planejamento.
+aberto é devolvida ao planejamento. Passados os gates, o despacho grava o pacote da tarefa — o card, os handovers, a leitura do modelo e as âncoras conferidas no arquivo de hoje — num arquivo fora do versionamento, e quem conduz repassa ao executor só o texto pronto do despacho que o comando imprime, sem reconferir âncora à mão.
 
 **Passo 5 — fechar a tarefa e seguir, ou encerrar a janela.** Julgada a entrega, o loop registra o
 resultado no RDO da tarefa, apende a linha de consumo medido à série e passa ao próximo item da fila;
@@ -690,13 +690,13 @@ secundário, declarado numa seção à parte e sob a responsabilidade inteira de
 
 O modelo **versiona, não se reescreve**: quando uma decisão muda o que o plano entrega, a versão
 nova nasce ao lado da vigente, marcada como pendente, e as duas coexistem até o marco seguinte, em
-que o dono aceita ou recusa. Quem escreve o modelo é um agente só, o `pantonic-model-designer`: ele
+que o dono aceita ou recusa; no aceite, o comando do marco promove a versão aceita, cobrando a linha de validação do consultor, e só chama o modelador quando encontra conflito. Quem escreve o modelo é um agente só, o `pantonic-model-designer`: ele
 escreve na autoria, emenda quando uma decisão muda o que o plano entrega e resolve conflito entre o
 texto e a entrega. Nenhum
 outro papel escreve ali; quem precisa de um ato de modelo devolve um dossiê fechado, e quem conduz
 a sessão o despacha. O instrumento `.claude/tools/modelo.py` confere a seção vigente e a versão
-pendente (`check`) e gera a leitura do dono (`show`), que abre pelo estágio atual e, com `--drift`,
-mostra o que muda entre as duas versões, contratos inclusive. Planos escritos antes desta doutrina não são
+pendente (`check`; com `--so-vigente`, que o despacho usa, só a vigente, e a pendente fica para o marco), recusa o card cujo texto copiado da operação difere do da versão que ele cita e gera a leitura do dono (`show`), que abre pelo estágio atual e, com `--drift`,
+mostra o que muda entre as duas versões — a operação nova, a renumerada e a alterada, e a propriedade que só uma delas tem —, contratos inclusive. Planos escritos antes desta doutrina não são
 migrados: o instrumento os reconhece como forma anterior e não bloqueia nada.
 
 ## 9. O fechamento de tarefa e uma tarefa por contexto
@@ -746,7 +746,7 @@ edita; a nota no diário é o canal vivo.
 **Relatório de encerramento.** A janela fala com o gerente **uma vez**, na parada: **ponteiro mais
 deltas**, nunca repetindo o que já foi escrito no regi
```
[truncado em 4000 caracteres]

## Linhas removidas dos testes
- nenhum arquivo de teste entre os alvos

## Medida do executor
- Arquivo: docs\plans\P-0755-recomendacoes-auditoria-final\evidencia\P-0755-RAF-T40-medida-depois.json; mundo: depois; gerado em: 2026-09-30T06:27:01+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('README.md').read_text(encoding='utf-8');n=['card_check.py','modelo.py','encerrar.py','backlog.py','review_evidence.py','backlog_hook.py','telemetria_hook.py','progresso_hook.py','prevoo.py','materializar.py','custo_sessao.py'];e=['abre numa janela nova','sem reconferir âncora à mão','só chama o modelador quando encontra conflito','--so-vigente','a propriedade que só uma delas tem','Na parada de marco','rodada por quem conduz antes de despachar o planejador','C-18','que ele julga só na versão vigente','não cita mais nenhum item vivo','nunca o relato de um subagente','encerrar: B1','--consultor','as linhas que a entrega removeu','que o próprio pedido manda criar','uma por agente'];print('guia=%d-%d-%d'%(sum(x in t for x in n),sum(x in t for x in e),t.count('append-only e é a')))"` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 1
  ```
  docs\audits\sonda-2026-09-28\passos.py:13: docs.audits.sonda-2026-09-28.passos.passo (function) - sem chamador de producao alcancavel
  dead_code: FALHOU - 1 achado(s) de simbolo de producao sem chamador.
  ```
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): não conforme
- Veredito mecânico (`testes`): conforme
