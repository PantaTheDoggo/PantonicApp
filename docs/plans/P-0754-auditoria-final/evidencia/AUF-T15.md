# Evidência de revisão — P-0754 AUF-T15

## Diff (`git diff --stat`)
```
README.md                                                 | 12 ++++++++++--
 docs/DIARIO_DE_OBRAS.md                                   |  4 ++--
 docs/plans/P-0754-auditoria-final/estado.tsv              |  2 +-
 .../evidencia/P-0754-AUF-T15-medida.json                  | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 5 files changed, 29 insertions(+), 5 deletions(-)
```

## Arquivos tocados
- `README.md` — atribuição: da entrega; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0754-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T15-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `555704acb3d2289d94e5784e4724e89ce385a795`
- Arquivos-alvo declarados: `README.md`
- Arquivos tocados: `README.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T15-medida.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T15-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `README.md`
```
diff --git a/README.md b/README.md
index cc12a66..28afa3f 100644
--- a/README.md
+++ b/README.md
@@ -469,7 +469,7 @@ por transição — por exemplo `Tarefa "A porta de entrada diz como o dono acom
 painel". Passo: conferir os gates e preparar o despacho.` e `Agente revisor devolveu a tarefa "A
 porta de entrada diz como o dono acompanha a execução no painel": aprovado 100%, bloqueante
 nenhuma.` —, gerada por um gancho do kit (`.claude/tools/progresso_hook.py`) a partir do evento de
-cada transição do loop, com o título da tarefa no lugar da sigla e sem nenhuma saída de
+cada transição do loop, com o título da tarefa — do card de plano ou do tíquete do diário — no lugar da sigla e sem nenhuma saída de
 ferramenta entre duas linhas; as frases estão na seção *Repertório de mensagens ao gerente* da
 `scrum-master`. Para abrir o painel, no terminal integrado do VS Code, na raiz do repositório:
 `Get-Content -Path .claude/estado/progresso.txt -Wait -Tail 30 -Encoding utf8` (o arquivo nasce
@@ -630,7 +630,9 @@ linha de motivo.
 3. **Todas as decisões tomadas no fechamento — nada postergado.** Nenhuma escolha que pertença ao
    dono fica "a resolver na execução".
 4. **Linear.** Sem referência para frente, sem ramo condicional não resolvido, sem "TBD". O executor
-   lê de cima a baixo e sabe o que fazer sem inferir.
+   lê de cima a baixo e sabe o que fazer sem inferir. A contingência do card faz parte dele: tem a
+   ação fechada, não contraria as restrições do próprio card e declara entre os alvos o arquivo que
+   escreve.
 5. **Gate de publicação.** Um plano só é registrado no `_INBOX.md` e no diário quando não tem questão
    pendente, bloco a preencher, nem tarefa cujo conteúdo dependa de artefato que ainda não existe.
 
@@ -924,6 +926,12 @@ em vez de por leitura:
   todos os lugares onde o marco aparece; `operacoes` gera o esqueleto do relatório de operações e
   confere a cobertura dele; `plano` fecha o plano sem tarefa aberta — estado, relatório de entrega
   nas mesmas três seções e uma linha no diário. Os cinco recusam sem escrever quando falta insumo.
+- `.claude/tools/review_evidence.py` — a evidência que o revisor recebe de cada tarefa: a partir do
+  ponto de partida gravado no despacho (`--capturar-ref`), mostra como diferença contra ele o que a
+  entrega mudou — o arquivo criado depois dele, marcado como novo; o versionado que a lista de
+  ignorados também cobre; o que não é texto, comparado pelo conteúdo bruto —, expande o alvo do card
+  escrito com curinga e conta como registro da condução o que quem conduz escreve nos próprios
+  registros, antes de procurar outra tarefa que o tenha declarado.
 - `.claude/tools/prevoo.py` — o pré-voo do pedido: confere cada caminho, símbolo e flag que o texto
   do dono cita e imprime a tabela `citado | existe | onde`, que abre o plano antes de qualquer
   campanha.

```

## Medida do executor
- Arquivo: docs\plans\P-0754-auditoria-final\evidencia\P-0754-AUF-T15-medida.json; mundo: depois; gerado em: 2026-09-28T15:27:32+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;t=Path('README.md').read_text(encoding='utf-8');print('[%d-%d-%d]'%(t.count('do card de plano ou do tíquete do diário'),t.count('a evidência que o revisor recebe de cada tarefa'),t.count('A contingência do card faz parte dele')))"` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
