# Evidência de revisão — P-0753 AF-T18

## Diff (`git diff --stat`)
```
README.md                                          | 36 ++++++++++++++--------
 docs/DIARIO_DE_OBRAS.md                            |  4 +--
 docs/plans/P-0753-auditoria-estagio-1/estado.tsv   |  2 +-
 .../evidencia/P-0753-AF-T18-medida.json            | 36 ++++++++++++++++++++++
 docs/telemetria.tsv                                |  2 ++
 5 files changed, 64 insertions(+), 16 deletions(-)
```

## Arquivos tocados
- `README.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0753-auditoria-estagio-1/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T18-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `cf943b8c64e4297be76926f2ded6e867b19088e3`
- Arquivos-alvo declarados: `README.md`
- Arquivos tocados: `README.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T18-medida.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T18-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `README.md`
```
diff --git a/README.md b/README.md
index 59af694..09838b8 100644
--- a/README.md
+++ b/README.md
@@ -692,8 +692,9 @@ que o dono aceita ou recusa. Quem escreve o modelo é um agente só, o `pantonic
 escreve na autoria, emenda quando uma decisão muda o que o plano entrega e resolve conflito entre o
 texto e a entrega. Nenhum
 outro papel escreve ali; quem precisa de um ato de modelo devolve um dossiê fechado, e quem conduz
-a sessão o despacha. O instrumento `.claude/tools/modelo.py` confere a seção (`check`) e gera a
-leitura do dono (`show`), que abre pelo estágio atual. Planos escritos antes desta doutrina não são
+a sessão o despacha. O instrumento `.claude/tools/modelo.py` confere a seção vigente e a versão
+pendente (`check`) e gera a leitura do dono (`show`), que abre pelo estágio atual e, com `--drift`,
+mostra o que muda entre as duas versões, contratos inclusive. Planos escritos antes desta doutrina não são
 migrados: o instrumento os reconhece como forma anterior e não bloqueia nada.
 
 ## 9. O fechamento de tarefa e uma tarefa por contexto
@@ -902,22 +903,29 @@ tarefa:
 Os instrumentos do backlog vivem em `.claude/tools/` e são o que torna o diário operável por comando
 em vez de por leitura:
 
-- `.claude/tools/backlog.py` — o instrumento do diário de obras, em sete verbos: `next` seleciona a
-  próxima tarefa de forma determinística, `show` devolve o dossiê verbatim de um item, `check` faz o
-  lint da gramática do diário e dos planos, `status` e `start` transicionam uma tarefa e projetam a
-  mudança nos registros derivados, `drain` leva o inbox de planos ao índice, e `diretiva` reescreve
-  a linha de priorização.
+- `.claude/tools/backlog.py` — o instrumento do diário de obras, em oito verbos: `next` seleciona a
+  próxima tarefa de forma determinística e imprime o card inteiro, `show` devolve o card inteiro de
+  um item, `check` faz o lint da gramática do diário e dos planos — o plano recém-esboçado, com o
+  estado registrado e ainda fora da fila, inclusive —, `status` e `start` transicionam uma tarefa e
+  projetam a mudança nos registros derivados, `despachar` roda os gates do despacho, materializa
+  `in-progress`, grava a tarefa corrente com o ponto de partida e imprime o card, `drain` leva o
+  inbox de planos ao índice, e `diretiva` reescreve a linha de priorização.
 - `.claude/tools/backlog_hook.py` — o hook do ponto de carga: quando o prompt traz o gatilho de
   retomada, injeta o dossiê da próxima tarefa como contexto adicional da sessão; sem o gatilho, não
   escreve nada e sai com zero.
-- `.claude/tools/encerrar.py` — o instrumento de fechamento, em três verbos: `handover` registra no
+- `.claude/tools/encerrar.py` — o instrumento de fechamento, em cinco verbos: `handover` registra no
   próprio card, de máquina, o que quem vem depois espera da tarefa (o que foi entregue, com o que se
   pode contar, o que não refazer, o que fica pendente), e é esse campo que a seleção da próxima tarefa
   devolve à sucessora; `tarefa` leva a tarefa em revisão a concluída num ato só — confere o modelo do
   plano, projeta o estado, escreve o registro da tarefa em três seções (humano, máquina, histórico)
-  com o pacote transcrito do laudo, garante a linha de telemetria e registra os achados com rota;
-  `plano` fecha o plano sem tarefa aberta — estado, relatório de entrega nas mesmas três seções e uma
-  linha no diário. Os três recusam sem escrever quando falta insumo.
+  com o pacote transcrito do laudo, garante a linha de telemetria e registra com rota os achados,
+  inclusive cada achado de processo do laudo; `marco` grava o resultado que o dono deu num marco em
+  todos os lugares onde o marco aparece; `operacoes` gera o esqueleto do relatório de operações e
+  confere a cobertura dele; `plano` fecha o plano sem tarefa aberta — estado, relatório de entrega
+  nas mesmas três seções e uma linha no diário. Os cinco recusam sem escrever quando falta insumo.
+- `.claude/tools/prevoo.py` — o pré-voo do pedido: conf
```
[truncado em 4000 caracteres]

## Medida do executor
- Arquivo: docs\plans\P-0753-auditoria-estagio-1\evidencia\P-0753-AF-T18-medida.json; mundo: depois; gerado em: 2026-09-27T16:56:18+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('README.md').read_text(encoding='utf-8');print(t.count('em sete verbos'),t.count('em oito verbos'),t.count('em cinco verbos'),t.count('prevoo.py'),t.count('Quem escreve a linha é o hook'))"` | 0 | true |
| 2 | `pwsh -NoProfile -File .claude/checks/check-readme.ps1` | 0 | true |
| 3 | `python -m pytest -q` | 0 | true |
| 4 | `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
