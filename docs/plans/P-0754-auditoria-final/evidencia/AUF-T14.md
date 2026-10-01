# Evidência de revisão — P-0754 AUF-T14

## Diff (`git diff --stat`)
```
docs/DIARIO_DE_OBRAS.md                                   |  6 +++---
 docs/plans/P-0752-fato-no-ponto-de-uso.md                 |  2 +-
 docs/plans/P-0753-auditoria-estagio-1/plano.md            |  4 ++--
 docs/plans/P-0754-auditoria-final/estado.tsv              |  2 +-
 .../evidencia/P-0754-AUF-T14-medida.json                  | 15 +++++++++++++++
 docs/telemetria.tsv                                       |  1 +
 6 files changed, 23 insertions(+), 7 deletions(-)
```

## Arquivos tocados
- `docs/DIARIO_DE_OBRAS.md` — atribuição: da entrega; estado git: ` M`
- `docs/plans/P-0752-fato-no-ponto-de-uso.md` — atribuição: da entrega; estado git: ` M`
- `docs/plans/P-0753-auditoria-estagio-1/plano.md` — atribuição: da entrega; estado git: ` M`
- `docs/plans/P-0754-auditoria-final/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T14-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `186415d950a563c4a17f1625d447c003158d3e82`
- Arquivos-alvo declarados: `docs/plans/P-0753-auditoria-estagio-1/plano.md`, `docs/plans/P-0752-fato-no-ponto-de-uso.md`, `docs/DIARIO_DE_OBRAS.md`
- Arquivos tocados: `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0752-fato-no-ponto-de-uso.md`, `docs/plans/P-0753-auditoria-estagio-1/plano.md`, `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T14-medida.json`, `docs/telemetria.tsv`
- Registro da orquestração (não atribuível a tarefa): `docs/plans/P-0754-auditoria-final/estado.tsv`, `docs/plans/P-0754-auditoria-final/evidencia/P-0754-AUF-T14-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `docs/plans/P-0753-auditoria-estagio-1/plano.md`
```
diff --git a/docs/plans/P-0753-auditoria-estagio-1/plano.md b/docs/plans/P-0753-auditoria-estagio-1/plano.md
index 6e0b3eb..3716c37 100644
--- a/docs/plans/P-0753-auditoria-estagio-1/plano.md
+++ b/docs/plans/P-0753-auditoria-estagio-1/plano.md
@@ -1750,8 +1750,8 @@ docstring de `backlog.py`, F-33).
 - **AE-18** (`AF-T12`, fechamento, 2026-09-27) — achado de processo (dossiê): AF-T12: o card prescreve _backlog.transacionar_status como escrita (3), que faz checagens proprias, e exige ao mesmo tempo 'todas as checagens antes da primeira escrita' sem dizer como conciliar (ex.: chamar checar_transicao antes da escrita (1)). Tambem ficaram sem fechamento: a forma de <plano> no dossie (a entrega usou caminho relativo ao repo), o strip() da frase e duas recusas a mais (plano sem id no nome; plano fora do backlog). **Rota:** a conciliação sanada no `DAF-43` (`checar_transicao` roda antes da escrita (1)); o resto — forma de `<plano>` no dossiê, `strip()` da frase, as duas recusas a mais — não é erro (entrega coerente com o contrato, lacuna de autoria do card): auditoria final
 - **AE-19** (`AF-T13`, fechamento, 2026-09-27) — achado de processo (dossiê): AF-T13: o contrato do --checar não tem poder discriminante para seção ausente — 'nao citados' conta o ID em crase em qualquer lugar do documento e a tabela do arco que o próprio esqueleto gera já cita toda tarefa, e 'sem os quatro blocos' só itera seções existentes; medido em cópia do P-0753: seção inteira de AF-T1 apagada, --checar sai 0 com 'nenhum'/'nenhum', enquanto o item 6 da skill promete 'toda seção de tarefa com os quatro blocos'. **Rota:** corrigido no ato pelo consultor (`DAF-44`, regra `A8`; sem `AF-T13a`, diretiva do dono de 2026-09-26) — linha `sem seção: <ids>` no `--checar` (tarefa não `cancelled` sem `` ## `<ID>` — ``), exit `1` quando não vazia; TR `test_tr_esqueleto_de_operacoes_checar_secao_apagada` apaga a seção inteira (vermelho antes do reparo, verde depois); skill `entrega-de-encerramento` item 6 atualizada; suíte `488 passed`. Fechado. (rota do laudo: card de replanejamento do P-0753)
 - **AE-20** (`AF-T14`, fechamento, 2026-09-27) — achado de processo (dossiê): Restrição do AF-T14 justifica 'modelo.py check sobre o P-0753 sai 0' com '(o plano não tem ## 1A)', fato falso desde a versão 2 pendente gravada pelo modelador após a AF-T7 (plano.md:173); a restrição segue verdadeira (exit 0 re-medido, agora exercitando o caminho pendente sobre plano real). **Rota:** auditoria final — diretiva do dono de 2026-09-26: nenhum card nem tiquete novo por ajuste (rota do laudo: sem ação sobre a entrega; item de replanejamento do P-0753 — restrição que cita estado do plano re-confere o parêntese quando o modelador grava versão pendente)
-- **AE-21** (`AF-T14`, fechamento, 2026-09-27) — achado de processo (dossiê): O dossiê de evidência truncou o diff de modelo.py em 4000 caracteres antes da linha que materializa o Passo 2 (_diff_objetos, contrato); a leitura exigiu abrir o repositório. **Rota:** sem ação — teto conhecido do instrumento; registrado para o agregado.
-- **AE-22** (`AF-T16`, fechamento, 2026-09-27) — achado de processo (dossiê): AF-T16: as quatro linhas de Verificação saíram 'esperado, não ensaiado' (RUBRICA §8 xii-b) e a única linha comportamental exercita só o check-readme; o kit_check só emite acento em caminho de falha, sem linha que o discrimine (xvii). A revisão mediu os dois mundos: check-readme antes True/depois False; kit_check check-drift com -KitRoot vazio sai 1 com 'não' íntegro e 0 U+FFFD. **Rota:** auditoria final — diretiva do dono de 2026-09-26: nenhum card nem tiquete novo por ajuste (rota do laudo: item de replanejamento do P-0753 — autoria de Verificação com o valor antes ensaiado no ato).
+- **AE-21** (`AF-T14`, fechamento, 2026-09-27) — achado de processo (dossiê): O dossiê de evidência truncou o diff de modelo.py em 4000 caracteres antes da linha que materializa o Passo 2 (_diff_objetos, contrato); a leitura exigiu abrir o repositório. **Rota:
```
[truncado em 4000 caracteres]

### `docs/plans/P-0752-fato-no-ponto-de-uso.md`
```
diff --git a/docs/plans/P-0752-fato-no-ponto-de-uso.md b/docs/plans/P-0752-fato-no-ponto-de-uso.md
index 62c0723..29db437 100644
--- a/docs/plans/P-0752-fato-no-ponto-de-uso.md
+++ b/docs/plans/P-0752-fato-no-ponto-de-uso.md
@@ -838,4 +838,4 @@ Proposta aceita pela ordem acima (agente, 2026-09-26; a amostra e a classificaç
 - **AE-48** (`FPU-T9`, fechamento, 2026-09-26) — Revisor: a OP-9 declara 'nenhuma conferencia nova entra como frase de skill', e o card (Passo 2, DFP-12) acrescenta uma conferencia em prosa ao checklist da mensagem-ao-dono secao 1; a skill se chama 'a regua executavel dessa medida'; as Verificacoes 1-2 (arquivo existe; contagem >=3 do nome) nao discriminam o conteudo. **Rota:** triagem do consultor no mesmo card corretivo da OP-9: declarar a skill como a medida em prosa da DFP-12 (sem o rotulo regua executavel) e dar a Verificacao um item que confira o exemplo contra o arquivo citado **Destino (consultor, acionamento 9):** card corretivo `FPU-T9a` (DFP-21: defeito do card, sem drift do modelo; a Verificação 3 confere o exemplo contra a linha citada).
 - **AE-49** (`FPU-T9a`, fechamento, 2026-09-26) — Revisor: o Passo 3 do FPU-T9a publicou a linha nova do Exemplo em crase simples com crases internas escapadas por barra invertida, contra o criterio (xi) da RUBRICA secao 8 (literal com crase vai em bloco cercado); .claude/skills/fatos-frescos/SKILL.md:57 ficou com duas sequencias barra-crase. **Rota:** replanejamento do P-0752 via consultor: card corretivo da OP-9 que reescreve a linha 57 com o literal em bloco cercado e Verificacao que conta chr(92)+chr(96) no arquivo (antes 2, depois 0) **Destino (dono, 2026-09-26):** corrigido por ordem direta do dono, sem card: o Exemplo de `.claude/skills/fatos-frescos/SKILL.md` foi para dois blocos cercados `~~~~`; `python -c "from pathlib import Path;print(Path('.claude/skills/fatos-frescos/SKILL.md').read_text(encoding='utf-8').count(chr(92)+chr(96)))"` → `0`; `card_check --tarefa FPU-T9a --mundo depois` segue OK (a Verificação 3 dele confere as substrings do exemplo).
 - **AE-50** (`FPU-T7`, fechamento, 2026-09-27) — review_evidence: a ref de despacho (git stash create) não carrega arquivo não rastreado, e o trecho de encerrar.py/test_encerrar.py sai inteiro, sem diff **Rota:** auditoria final
-- **AE-51** (`FPU-T10`, fechamento, 2026-09-27) — docs/ACIONAMENTOS_CONSULTOR.tsv fora do git: a evidência cola o arquivo inteiro sem baseline e 'não mudar outro campo' só se confere por estrutura (mesma causa do AE-50) **Rota:** auditoria final
+- **AE-51** (`FPU-T10`, fechamento, 2026-09-27) — docs/ACIONAMENTOS_CONSULTOR.tsv fora do git: a evidência cola o arquivo inteiro sem baseline e 'não mudar outro campo' só se confere por estrutura (mesma causa do AE-50) **Rota:** auditoria final · **Desfecho (P-0754, AUF-T14, 2026-09-28):** encerrado sem mudança no kit — a premissa caiu: `docs/ACIONAMENTOS_CONSULTOR.tsv` é versionado desde o commit `2513964`, e `review_evidence.py` o trata como registro da condução.

```

### `docs/DIARIO_DE_OBRAS.md`
```
diff --git a/docs/DIARIO_DE_OBRAS.md b/docs/DIARIO_DE_OBRAS.md
index fec652e..d35968c 100644
--- a/docs/DIARIO_DE_OBRAS.md
+++ b/docs/DIARIO_DE_OBRAS.md
@@ -72,8 +72,8 @@ estão triados, todos com `**Rota:**` explícita.
    entrega e toda revisão exige aviso à mão mais reconciliação por hunk e mtime.
 
 <!-- fila:gerada -->
-**Fila corrente:** `P-0754` — Auditoria final do kit: os herdados e o relatório de auditoria nova (`docs/plans/P-0754-auditoria-final/plano.md:1-1041`) · fila: — · ready 2 · blocked 1 · in-progress 0
-- `P-0754` (`ready`, 13/16): próxima `AUF-T14`
+**Fila corrente:** nada delegável — 0 elegível(is) · blocked 1
+- `P-0754` (`ready`, 13/16): próxima —
 <!-- /fila:gerada -->
 
 > **⏹ Os quatro blocos de diretiva abaixo são HISTÓRICO — o `P-0743` fechou `done` 18/18 e foi
@@ -6082,7 +6082,7 @@ card: `TK-55`, `TK-67`, `TK-70`, `TK-72`, `TK-73` e `TK-81`; o `TK-71` fechou po
 - **Notas de execução:**
   - 2026-09-26 `ready` — aberto com os cards TK-90a e TK-90b (consultor P-0752, acionamento 10)
 - **AE-88** (`TK-90b`, fechamento, 2026-09-27) — rodada de replanejamento despachada ao planejador não tem canal de medida gravada (card_check --gravar); o verde só se confirmou por re-execução do revisor **Rota:** auditoria final
-- **AE-89** (`TK-90b`, fechamento, 2026-09-27) — LF-T2..LF-T5 do P-0742 passam do teto DB-7 de backlog.py show (8.000 caracteres) e saem truncados; a Fase 4 do planejador não confronta o tamanho do card com o teto **Rota:** auditoria final
+- **AE-89** (`TK-90b`, fechamento, 2026-09-27) — LF-T2..LF-T5 do P-0742 passam do teto DB-7 de backlog.py show (8.000 caracteres) e saem truncados; a Fase 4 do planejador não confronta o tamanho do card com o teto **Rota:** auditoria final · **Desfecho (P-0754, AUF-T14, 2026-09-28):** encerrado sem mudança no kit — a premissa caiu: o card de tarefa é isento do teto do `backlog.py show`, e os oito cards do `P-0742` saem inteiros, sem marca de truncado.
 
 
 

```

## Medida do executor
- Arquivo: docs\plans\P-0754-auditoria-final\evidencia\P-0754-AUF-T14-medida.json; mundo: depois; gerado em: 2026-09-28T15:20:59+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python -c "from pathlib import Path;c=[('docs/plans/P-0753-auditoria-estagio-1/plano.md','AE-21'),('docs/plans/P-0753-auditoria-estagio-1/plano.md','AE-22'),('docs/plans/P-0752-fato-no-ponto-de-uso.md','AE-51'),('docs/DIARIO_DE_OBRAS.md','AE-89')];print('[%s]'%'-'.join(str(sum(1 for l in Path(a).read_text(encoding='utf-8').splitlines() if l[4:9]==n and not l[9].isdigit() and 'Desfecho (P-0754, AUF-T14, 2026-09-28)' in l)) for a,n in c))"` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
