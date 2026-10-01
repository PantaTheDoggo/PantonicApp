# Passagem — achados da auditoria final do kit, para planejar o plano sucessor

**Data:** 2026-09-28 · **Para:** o agente que vai planejar o plano das recomendações · **Origem:** plano "Auditoria final do kit: os herdados e o relatório de auditoria nova" (`P-0754`), 16/16 tarefas fechadas.
**Fonte da verdade dos achados:** `docs/audits/AUDITORIA_FINAL_KIT.md` (307 linhas). Este arquivo é índice e roteiro: não substitui o relatório nem repete o conteúdo dele.

## 1. O que você recebe

| o quê | onde | linhas |
|---|---|---|
| 43 cláusulas testadas (`K-01`..`K-43`) | relatório §2 | a partir da 35 |
| 54 registros medidos, com avaliação | relatório §3 | 85–145 |
| conclusão por dimensão e veredito geral | relatório §4 | 146–162 |
| 31 recomendações (`R-01`..`R-31`), cada uma com origem, ação e verificação | relatório §5 | 163–(§6) |
| custo medido por papel e da sessão principal | relatório §6 | — |
| avaliação passo a passo do `scrum-master` (P1..P10), a matéria do `AE-95` | relatório §8 | 290–fim |
| achados de processo da execução (`AE-96`..`AE-119`) | `docs/plans/P-0754-auditoria-final/plano.md`, `## 9. Achados da execução` | fim do arquivo |
| decisões da auditoria e dos reparos (`DAU-32`, `DAU-33`) | mesmo plano, `## 3` | — |
| cenário do consultor (o que ficou em vigília) | `docs/plans/P-0754-auditoria-final/cenario.md` | — |

Leia o relatório por seção (§5 e §3 primeiro); não leia o `plano.md` do `P-0754` inteiro: ele tem mais de 1.000 linhas.

## 2. Os achados, agrupados para planejar

Grupos por tema. Cada `R` está fechada no relatório §5; aqui só o agrupamento e o que exige decisão do dono.

| tema | recomendações | observação para o planejamento |
|---|---|---|
| Custo da orquestração | `R-01`, `R-02`, `R-03` | `R-01` (loop em contexto novo) é a de maior efeito medido: 285,6k de contexto por turno no loop real, 485,6k no fictício. `R-02` (despacho por arquivo) foi medida: saída do Passo 4 caiu de 3,06k para 0,72k por tarefa |
| Modelo × card × versão | `R-04`, `R-06`, `R-07`, `R-08` | **`R-04` é decisão do dono** (doutrina: o que o gate do despacho julga, ou a rota da emenda que cria operação). As quatro mexem em `modelo.py`, `encerrar.py` e na skill `scrum-master`: arquivos compartilhados, em série |
| Medida da rodada de replanejamento (`H-16`) | `R-05` | responde o item herdado; mexe em `card_check.py` e `caminhos.py` |
| `card_check` | `R-09`, `R-10`, `R-11` e as `R-26`..`R-31` que tocarem o instrumento | mesmo arquivo, em série |
| Evidência do revisor | `R-12`, `R-13`, `R-14` | `review_evidence.py`, em série |
| Hooks e telemetria | `R-15`, `R-16`, `R-24` | `R-24` é do hook **global** do pytest (`~/.claude/hooks/`), fora deste repositório: projeção via `materializar.py`, ato do dono |
| Instrumentos de backlog e fechamento | `R-17`, `R-18`, `R-19`, `R-20` | `prevoo.py`, `backlog.py`, `encerrar.py`, skill `scrum-master` |
| Doutrina do planejador e comunicação | `R-21`, `R-22`, `R-23`, `R-25` | **`R-21` é decisão do dono** (régua de profundidade por classe do plano) |
| Registros sem recomendação na 1ª versão | `R-26`..`R-31` | acrescentadas pelo consultor na revisão (`DAU-33`), **sem revisão própria** — confira antes de usar (§4, passo 5) |

## 3. O que ficou pendente no `P-0754` (não é do plano sucessor, mas bloqueia a fila)

1. **Marco 3 do `P-0754`:** o dono lê o relatório e dá o veredito. Linha `| **Marco 3** |` do `plano.md` está `pendente`.
2. **Fechamento do plano:** depois do veredito, gerar o documento de validação (skill `entrega-de-encerramento`) e rodar `python .claude/tools/encerrar.py plano --plano docs/plans/P-0754-auditoria-final/plano.md --veredito "<frase do dono>" --operacoes <documento>`. Hoje `estado.tsv` tem o plano `ready` com as 16 tarefas `done`.
3. **Diretiva de priorização** (`docs/DIARIO_DE_OBRAS.md`, linha 4) ainda aponta o `P-0754`; o plano sucessor precisa reescrevê-la com `backlog.py diretiva` depois de nascer (é o defeito do registro 16).
4. **Nada foi commitado:** HEAD `2513964`; `git status --porcelain=v1 --untracked-files=all` tem 86 linhas (WIP das 16 tarefas + relatório + este arquivo). Commit é ato do dono.
5. **Duplicatas nos achados:** `AE-100`/`AE-101` repetem `AE-98`/`AE-99`; `AE-117`/`AE-118`/`AE-119` repetem `AE-111`/`AE-112`/`AE-113` (defeito `R-19`). Trate cada par como um item só.

## 4. Double check — rode antes de planejar

Cada passo traz o comando e o valor medido em 2026-09-28. Valor diferente é sinal de que a árvore andou: re-derive antes de usar o número.

1. **Árvore e contador.**
   `git rev-parse --short HEAD` → `2513964`
   `git status --porcelain=v1 --untracked-files=all` → 86 linhas
   `grep -o "Próximo id de plano: P-[0-9]*" docs/plans/_INBOX.md` → `Próximo id de plano: P-0755`
2. **O relatório está íntegro** (as seis verificações do card `AUF-T16`, todas juntas):
   `python .claude/tools/card_check.py --plano docs/plans/P-0754-auditoria-final/plano.md --tarefa AUF-T16 --mundo depois` → `card_check: OK - tarefa 'AUF-T16' fecha.`
3. **Contagens do relatório.**
   `grep -c "^### R-" docs/audits/AUDITORIA_FINAL_KIT.md` → `31`
   `grep -c "^| K-" docs/audits/AUDITORIA_FINAL_KIT.md` → `43`
   `grep -cE "^\| [0-9]+ \|" docs/audits/AUDITORIA_FINAL_KIT.md` → `54`
4. **Cobertura das recomendações** (o critério que as Verificações do card não mediam, `AE-111`): todo registro da §3 com avaliação `inadequado` ou `oportunidade` é citado numa linha `Origem:` da §5. Medido pelo consultor: 36 registros, 0 sem origem. Refaça por script antes de confiar — as `R-26`..`R-31` entraram depois da revisão.
5. **Revise as `R-26`..`R-31`** contra os registros 13, 14, 17, 18, 27 e 28 da §3: foram escritas pelo consultor no reparo (`DAU-33`) e nenhum revisor as julgou.
6. **Confira cada defeito de instrumento no código antes de escrever o card** — o relatório cita `arquivo:linha` medidos em 2026-09-28, e o WIP ainda não commitado pode ter movido linhas. Em especial:
   - `R-04`: reproduza a recusa do despacho com `## 1A` pendente (registro 31) — é a premissa da decisão do dono;
   - `R-15`: `backlog_hook.py:33` (`_GATILHO`) e o casamento em prompt de `<agent-message`;
   - `R-16`: `telemetria_hook.py:338-339` (id do plano tirado da primeira mensagem);
   - `R-06`/`R-07`: `modelo.py:482-509` (`_diff_fluxo`, `_diff_estado`) e as regras `V4`/`V14`.
7. **Checagens do kit verdes na partida.**
   `python .claude/tools/backlog.py check` → `check: OK — nenhuma violação.`
   `python .claude/tools/modelo.py check --plano docs/plans/P-0754-auditoria-final/plano.md` → `modelo: OK — 16 operações, 12 objetos, 23 propriedades, 16 tarefas, versão 1`
   `python -m pytest --co -q` → `521 tests collected`
8. **Não duplique plano vivo:** antes de planejar, `grep` pelo tema em `docs/plans/_INBOX.md` e no índice do diário (Controle 1.2 da Regra 1).

## 5. Onde estão os dados brutos da sonda (fora do repositório)

- `%TEMP%\claude\auditoria\p0754_retrato\` — retrato da árvore antes da sonda.
- `%TEMP%\claude\auditoria\p0754_artefatos\` — cópia integral do plano fictício `P-0755` descartado (plano, laudos, evidências, RDO), de `scratch_sonda/`, do teste e dos registros do kit depois da execução (`depois_docs_telemetria.tsv` tem as 18 linhas da série do plano fictício).
- `%TEMP%\claude\auditoria\registros.md` — anotações do auditor durante a execução.
- `%TEMP%\claude\auditoria\medir.py` e `passos.py` — medida da sessão principal pelo transcript (`message.usage`); é o protótipo do instrumento que a `R-01` precisa para verificar o ganho.

`%TEMP%` é volátil: se esses caminhos sumirem, o relatório é a fonte que resta.
