# Roteiro do plano sucessor da auditoria final — 2026-09-28

**Insumo:** `docs/audits/HANDOVER_AUDITORIA_FINAL_2026-09-28.md` (roteiro de conferência) e
`docs/audits/AUDITORIA_FINAL_KIT.md` (fonte dos achados, `R-01`..`R-31`).
**Para:** o dono, na decisão de abrir o plano sucessor; depois, o `pantonic-planner` na autoria.
**Estado:** proposta. Não é plano registrado: o `P-0755` só nasce pelo procedimento do kit depois
do veredito do dono no Marco 3 do `P-0754` (`DAU-1`).

## 1. Conferência dos achados (double check)

Todos os valores do handover §4 re-medidos em 2026-09-28 e iguais: HEAD `2513964`; `git status`
86 linhas; próximo id `P-0755`; 31 `R`, 43 `K`, 54 registros; `card_check AUF-T16 --mundo depois`
OK; `backlog.py check` OK; `modelo.py check` OK (16 operações, versão 1); 521 testes coletados.

Cobertura por script (handover §4 passo 4): 36 registros não-adequados (15 `inadequado`,
21 `oportunidade`), 0 sem linha `Origem:`; 0 cláusula `K` sem registro; o registro 9 é origem de
`R-01` e `R-21`, o 37 de `R-06` e `R-08` — sem defeito.

Âncoras de instrumento confirmadas na árvore: `backlog_hook.py:33` (`_GATILHO`, `R-15`);
`telemetria_hook.py:338-339` (`R-16`); `modelo.py:482` e `:499` (`_diff_fluxo`, `_diff_estado`,
`R-07`), `:420-422` (`V4`/`V14`, `R-06`); `encerrar.py:1000-1004` (`R-08`); `card_check.py:105`
(`python`/`pwsh`, `R-11`), `:98` (par inline recusa `,;.`, `R-10`), `:343-344` (bloco cercado
ignora `--mundo`, `R-09`); `caminhos.py:110-116` (medida na pasta do `--plano`, `R-05`);
`review_evidence.py:558` e `:691` (`fnmatchcase`, `R-30`), `:351` e `:396` (porcelain sem `-z`,
`R-31`), `:639`/`:662` (binário sem marca de novo, `R-14`), `:992` (medida ao lado do `--out`,
`R-13`); `encerrar.py:556` (dedupe por texto literal, `R-19`); `backlog.py:112` (só o prefixo de
tarefa é lido; o plano declara `Prefixo das decisões`, `R-28`).

Premissa da `R-04` confirmada por leitura, não por reprodução (o `P-0755` foi descartado e a cópia
em `%TEMP%` já tem a versão promovida): `modelo.py:586-589` valida a `## 1A` com `validar(...,
pendente=True)`, e `validar` aplica `V1` (operação sem tarefa) em qualquer bloco (`:356`);
`backlog.py:2117` roda o `check` no despacho. Logo, emenda que cria operação sem card recusa o
despacho por construção.

Divergências achadas:

1. **`R-24` não é fora do repositório.** A fonte do hook do pytest é
   `.claude/global/hooks/pytest_pretooluse.py`, idêntica à projeção em `~/.claude/hooks/`
   (`diff -q` sem diferença). Card normal no plano; só a projeção (`materializar.py apply`) é ato
   do dono.
2. **`R-29` remedeia o mesmo incidente da `R-15`.** Os registros 18 e 42 descrevem a mesma
   injeção (15 KB do card `AUF-T16`, 3 vezes, por gatilho em relatório de subagente). A `R-15`
   remove a causa; a `R-29` restringe o `next` a um "plano corrente" que o instrumento não
   define. Candidata a "registrar e não agir".
3. **O instrumento de verificação da `R-01` só existia fora do repositório.** `medir.py` e
   `passos.py` (medida da sessão principal pelo transcript) foram copiados de
   `%TEMP%\claude\auditoria\` para `docs/audits/sonda-2026-09-28/`. A `R-01` os promove a
   instrumento do kit.
4. **`R-26`..`R-31`** (escritas pelo consultor na `DAU-33`, sem revisão): `R-26` e `R-27` são
   doutrina do planejador (Fases 4 e 5), coerentes com `R-05` e `R-09`; `R-27` depende de `R-11`
   ou de invólucro `python -c`. `R-28` viável (campo existe no cabeçalho do plano). `R-30` muda
   comportamento de curinga já em uso — o card levanta os alvos com `*` dos planos vivos.
   `R-31` toca dois pontos de leitura do porcelain, não um. `R-29` é a divergência 2.

## 2. Decisões do dono antes da autoria

| # | questão | opções | recomendação |
|---|---|---|---|
| D1 | `R-04` — rota `modelador` com operação nova × gate do despacho | (a) o `check` do despacho julga só a `## 1`; a `## 1A` é cobrada no marco (`--aceita-versao` exige `V1` fechado) e a rota `modelador` com operação nova enfileira a rodada de replanejamento sem parar a janela. (b) emenda que cria operação vira rota `planejador` (para a janela). | (a): preserva a doutrina "rota modelador segue" e a coexistência das versões até o marco; a rodada já existe como mecanismo. |
| D2 | `R-21` — régua de profundidade da Fase 4 por classe e tamanho do plano | adotar (o planejador escreve a régua) · registrar e não agir | adotar: é o único remédio ao custo de planejamento (28% do plano fictício). |
| D3 | `R-29` | manter como defesa em profundidade · registrar e não agir | registrar e não agir; a `R-15` fecha a causa. |
| D4 | forma do plano | um plano com cinco marcos · dois planos (custo + instrumentos; depois doutrina) | um plano: uma iniciativa, um contexto de orquestração; os marcos dão o ponto de parada. |

## 3. Marcos propostos (a decomposição em cards é do planejador)

Ordem por efeito medido e por arquivo compartilhado; dentro de cada marco, os itens do mesmo
arquivo vão em série.

| marco | tema | recomendações | arquivos em série |
|---|---|---|---|
| A | custo da orquestração | `R-01` (+ instrumento de medida), `R-02`, `R-03`, `R-15`, `R-24` | `backlog.py` (`despachar`), skill `scrum-master`, `backlog_hook.py`, `pytest_pretooluse.py` |
| B | instrumentos de revisão e medida | `R-13`, `R-14`, `R-30`, `R-31`, `R-12` · `R-09`, `R-10`, `R-11`, `R-05` · `R-26`, `R-27` | `review_evidence.py` + rubrica · `card_check.py` + `caminhos.py` · `pantonic-planner.md` |
| C | modelo × card × versão | `R-04` (D1), `R-06`, `R-07`, `R-08` | `modelo.py`, `encerrar.py`, skill `scrum-master` |
| D | backlog, fechamento e telemetria | `R-17`, `R-18`, `R-28`, (`R-29`), `R-19`, `R-20`, `R-16` | `prevoo.py`, `backlog.py`, `encerrar.py`, skill `scrum-master`, `telemetria_hook.py`, `progresso_hook.py` |
| E | doutrina do planejador e comunicação | `R-21` (D2), `R-22`, `R-23`, `R-25` | `pantonic-planner.md`, skill `scrum-master` (repertório de mensagens), `checar-versao-kit` |

O Marco A vai primeiro porque muda o custo de executar os quatro seguintes: `R-01` se aplica ao
próprio plano sucessor na prática (loop em janela nova) antes de ser doutrina.

## 4. Sequência de atos

1. Dono: veredito do Marco 3 do `P-0754` (ler o relatório).
2. Condução: `entrega-de-encerramento` do `P-0754` e `encerrar.py plano ... --veredito "<frase>"`.
3. Dono: commit do WIP (86 linhas) — inclui o relatório, o handover, este roteiro e a sonda.
4. Dono: responde D1..D4.
5. Janela nova de planejamento: `pantonic-planner` (Fase 0–1 com este roteiro e o relatório §5
   como insumo) → batedor → `pantonic-model-designer` → decomposição → Marco 1. Ao nascer,
   `backlog.py diretiva` reescreve a diretiva de priorização (hoje aponta o `P-0754`).
6. Janela nova de execução: loop do `scrum-master`, marco a marco.

## 5. Fora do plano

- Duplicatas de achados no `P-0754` (`AE-100`/`AE-101`, `AE-117`..`AE-119`): já cobertas pela
  `R-19`; não viram item.
- Estágios seguintes de `R-01` (medida do ganho) dependem do loop do próprio sucessor: a
  verificação é o custo por turno do transcript da janela de execução contra 285,6k.
