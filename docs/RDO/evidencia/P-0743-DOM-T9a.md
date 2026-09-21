# Evidência de revisão — P-0743 DOM-T9a

## Diff (`git diff --stat`)
```
.claude/README.md                          |   3 +-
 .claude/agents/pantonic-consultant.md      |   5 +-
 .claude/agents/pantonic-planner.md         |  52 +-
 .claude/agents/pantonic-reviewer.md        |  28 +-
 .claude/skills/diario-de-obras/SKILL.md    |  37 +-
 .claude/skills/passagem-de-bastao/SKILL.md |   6 +-
 .claude/skills/scrum-master/SKILL.md       |  52 +-
 .claude/tools/rdo.py                       |   8 +-
 GOVERNANCA.md                              |  93 +++-
 README.md                                  |  18 +-
 docs/DIARIO_DE_OBRAS.md                    | 121 ++++-
 docs/RDO/INDEX.md                          |  20 +
 docs/RUBRICA_DE_REVISAO.md                 |   7 +-
 docs/plans/P-0741-modelo-conceitual.md     | 842 ++++++++++++++++++++++++++---
 docs/plans/_INBOX.md                       |   3 +-
 docs/plans/_INBOX_HISTORICO.md             |   2 +
 docs/telemetria.tsv                        |  63 +++
 tests/test_rdo.py                          |  19 +
 18 files changed, 1260 insertions(+), 119 deletions(-)
```

## Arquivos tocados
- `.claude/README.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-consultant.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-model-designer.md` — atribuição: da entrega; estado git: `??`
- `.claude/agents/pantonic-planner.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-reviewer.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/diario-de-obras/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/passagem-de-bastao/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/scrum-master/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/tools/modelo.py` — atribuição: alheio; estado git: `??`
- `.claude/tools/rdo.py` — atribuição: alheio; estado git: ` M`
- `GOVERNANCA.md` — atribuição: alheio; estado git: ` M`
- `README.md` — atribuição: alheio; estado git: ` M`
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/OPERACOES_AS_IS.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/INDEX.md` — atribuição: alheio; estado git: ` M`
- `docs/RDO/P-0741-MC-T1-a-norma-e-a-gramatica-do-modelo-publicadas-nas-residencias-u.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0741-MC-T2-modelo-py-check-e-show-e-o-alvo-modelo-no-gerador-de-laudo.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0741-MC-T2a-o-campo-sem-consumidor-sai-da-dataclass-do-instrumento.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0741-MC-T2b-a-cadeia-sem-consumidor-sai-inteira-do-instrumento.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0741-MC-T3-os-tres-papeis-que-escrevem-o-modelo-planejador-revisor-e-co.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0741-MC-T4-o-loop-le-confere-e-mostra-o-modelo-scrum-master-e-passagem.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0741-MC-T4a-o-gate-do-modelo-no-fechamento-para-de-criar-o-vermelho-que.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T1-a-norma-do-modelo-de-dominio-e-o-papel-que-a-executa.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T2-a-gramatica-que-a-maquina-le.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T3-o-instrumento-le-a-forma-nova.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T3a-o-que-o-instrumento-e-a-gramatica-dizem-de-si-mesmos.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T3b-a-referencia-cruzada-do-docstring.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T4-o-modelador.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T5-os-papeis-diante-do-modelador.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T5a-a-costura-do-retorno-do-revisor.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T5b-a-cadeia-do-retorno-do-emissor-ao-consumidor.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T7-a-norma-da-forma-nova-propriedades-estado-e-versao.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T8-a-gramatica-da-forma-nova.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T8a-os-ponteiros-que-a-forma-nova-deixou-para-tras.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/P-0743-DOM-T9-o-instrumento-aprende-propriedades-estado-e-versao.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0741-MC-T1.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0741-MC-T2.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0741-MC-T2a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0741-MC-T2b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0741-MC-T3.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0741-MC-T4.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0741-MC-T4a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0741-MC-T5.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T1.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T2.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T3.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T3a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T3b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T4.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T5.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T5a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T5b.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T7.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T8.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T8a.md` — atribuição: alheio; estado git: `??`
- `docs/RDO/evidencia/P-0743-DOM-T9.md` — atribuição: alheio; estado git: `??`
- `docs/RUBRICA_DE_REVISAO.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0741-modelo-conceitual.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0743-modelo-de-dominio.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0744-spec-do-planejador.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_INBOX.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/_INBOX_HISTORICO.md` — atribuição: alheio; estado git: ` M`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/fixtures/modelo/fluxo-concluido.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/fluxo-pendente.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/fluxo-valido.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-forma-anterior.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-invalido-2.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-invalido.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-sem-cabecalho.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-sem-estado.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-sem-modelo.md` — atribuição: alheio; estado git: `??`
- `tests/test_modelo.py` — atribuição: alheio; estado git: `??`
- `tests/test_rdo.py` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `e0efcf6b1a5aae9ec176f906a28384385d710a7f`
- Arquivos-alvo declarados: `.claude/agents/pantonic-model-designer.md`
- Literais não reconhecidos como caminho (4): `I-5`, `## Fatos estáveis`, `## O ensinamento`, `## A forma da devolução`
- Arquivos tocados: `.claude/README.md`, `.claude/agents/pantonic-consultant.md`, `.claude/agents/pantonic-model-designer.md`, `.claude/agents/pantonic-planner.md`, `.claude/agents/pantonic-reviewer.md`, `.claude/skills/diario-de-obras/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/modelo.py`, `.claude/tools/rdo.py`, `GOVERNANCA.md`, `README.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/OPERACOES_AS_IS.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0741-MC-T1-a-norma-e-a-gramatica-do-modelo-publicadas-nas-residencias-u.md`, `docs/RDO/P-0741-MC-T2-modelo-py-check-e-show-e-o-alvo-modelo-no-gerador-de-laudo.md`, `docs/RDO/P-0741-MC-T2a-o-campo-sem-consumidor-sai-da-dataclass-do-instrumento.md`, `docs/RDO/P-0741-MC-T2b-a-cadeia-sem-consumidor-sai-inteira-do-instrumento.md`, `docs/RDO/P-0741-MC-T3-os-tres-papeis-que-escrevem-o-modelo-planejador-revisor-e-co.md`, `docs/RDO/P-0741-MC-T4-o-loop-le-confere-e-mostra-o-modelo-scrum-master-e-passagem.md`, `docs/RDO/P-0741-MC-T4a-o-gate-do-modelo-no-fechamento-para-de-criar-o-vermelho-que.md`, `docs/RDO/P-0743-DOM-T1-a-norma-do-modelo-de-dominio-e-o-papel-que-a-executa.md`, `docs/RDO/P-0743-DOM-T2-a-gramatica-que-a-maquina-le.md`, `docs/RDO/P-0743-DOM-T3-o-instrumento-le-a-forma-nova.md`, `docs/RDO/P-0743-DOM-T3a-o-que-o-instrumento-e-a-gramatica-dizem-de-si-mesmos.md`, `docs/RDO/P-0743-DOM-T3b-a-referencia-cruzada-do-docstring.md`, `docs/RDO/P-0743-DOM-T4-o-modelador.md`, `docs/RDO/P-0743-DOM-T5-os-papeis-diante-do-modelador.md`, `docs/RDO/P-0743-DOM-T5a-a-costura-do-retorno-do-revisor.md`, `docs/RDO/P-0743-DOM-T5b-a-cadeia-do-retorno-do-emissor-ao-consumidor.md`, `docs/RDO/P-0743-DOM-T7-a-norma-da-forma-nova-propriedades-estado-e-versao.md`, `docs/RDO/P-0743-DOM-T8-a-gramatica-da-forma-nova.md`, `docs/RDO/P-0743-DOM-T8a-os-ponteiros-que-a-forma-nova-deixou-para-tras.md`, `docs/RDO/P-0743-DOM-T9-o-instrumento-aprende-propriedades-estado-e-versao.md`, `docs/RDO/evidencia/P-0741-MC-T1.md`, `docs/RDO/evidencia/P-0741-MC-T2.md`, `docs/RDO/evidencia/P-0741-MC-T2a.md`, `docs/RDO/evidencia/P-0741-MC-T2b.md`, `docs/RDO/evidencia/P-0741-MC-T3.md`, `docs/RDO/evidencia/P-0741-MC-T4.md`, `docs/RDO/evidencia/P-0741-MC-T4a.md`, `docs/RDO/evidencia/P-0741-MC-T5.md`, `docs/RDO/evidencia/P-0743-DOM-T1.md`, `docs/RDO/evidencia/P-0743-DOM-T2.md`, `docs/RDO/evidencia/P-0743-DOM-T3.md`, `docs/RDO/evidencia/P-0743-DOM-T3a.md`, `docs/RDO/evidencia/P-0743-DOM-T3b.md`, `docs/RDO/evidencia/P-0743-DOM-T4.md`, `docs/RDO/evidencia/P-0743-DOM-T5.md`, `docs/RDO/evidencia/P-0743-DOM-T5a.md`, `docs/RDO/evidencia/P-0743-DOM-T5b.md`, `docs/RDO/evidencia/P-0743-DOM-T7.md`, `docs/RDO/evidencia/P-0743-DOM-T8.md`, `docs/RDO/evidencia/P-0743-DOM-T8a.md`, `docs/RDO/evidencia/P-0743-DOM-T9.md`, `docs/RUBRICA_DE_REVISAO.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0743-modelo-de-dominio.md`, `docs/plans/P-0744-spec-do-planejador.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/telemetria.tsv`, `tests/fixtures/modelo/fluxo-concluido.md`, `tests/fixtures/modelo/fluxo-pendente.md`, `tests/fixtures/modelo/fluxo-valido.md`, `tests/fixtures/modelo/plano-forma-anterior.md`, `tests/fixtures/modelo/plano-invalido-2.md`, `tests/fixtures/modelo/plano-invalido.md`, `tests/fixtures/modelo/plano-sem-cabecalho.md`, `tests/fixtures/modelo/plano-sem-estado.md`, `tests/fixtures/modelo/plano-sem-modelo.md`, `tests/test_modelo.py`, `tests/test_rdo.py`
- Atribuídos a outra tarefa do mesmo plano: `.claude/README.md` → `DOM-T4`, `.claude/agents/pantonic-consultant.md` → `DOM-T5`, `.claude/agents/pantonic-planner.md` → `DOM-T5`, `.claude/agents/pantonic-reviewer.md` → `DOM-T5`, `.claude/skills/diario-de-obras/SKILL.md` → `DOM-T2`, `.claude/skills/scrum-master/SKILL.md` → `DOM-T5`, `.claude/tools/modelo.py` → `DOM-T3`, `GOVERNANCA.md` → `DOM-T1`, `README.md` → `DOM-T4`, `docs/RUBRICA_DE_REVISAO.md` → `DOM-T1`, `docs/plans/P-0743-modelo-de-dominio.md` → `DOM-T10`, `tests/fixtures/modelo/fluxo-concluido.md` → `DOM-T3`, `tests/fixtures/modelo/fluxo-pendente.md` → `DOM-T9`, `tests/fixtures/modelo/fluxo-valido.md` → `DOM-T3`, `tests/fixtures/modelo/plano-forma-anterior.md` → `DOM-T9`, `tests/fixtures/modelo/plano-invalido-2.md` → `DOM-T9`, `tests/fixtures/modelo/plano-invalido.md` → `DOM-T3`, `tests/fixtures/modelo/plano-sem-cabecalho.md` → `DOM-T3`, `tests/fixtures/modelo/plano-sem-estado.md` → `DOM-T9`, `tests/fixtures/modelo/plano-sem-modelo.md` → `DOM-T3`, `tests/test_modelo.py` → `DOM-T3`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0741-MC-T1-a-norma-e-a-gramatica-do-modelo-publicadas-nas-residencias-u.md`, `docs/RDO/P-0741-MC-T2-modelo-py-check-e-show-e-o-alvo-modelo-no-gerador-de-laudo.md`, `docs/RDO/P-0741-MC-T2a-o-campo-sem-consumidor-sai-da-dataclass-do-instrumento.md`, `docs/RDO/P-0741-MC-T2b-a-cadeia-sem-consumidor-sai-inteira-do-instrumento.md`, `docs/RDO/P-0741-MC-T3-os-tres-papeis-que-escrevem-o-modelo-planejador-revisor-e-co.md`, `docs/RDO/P-0741-MC-T4-o-loop-le-confere-e-mostra-o-modelo-scrum-master-e-passagem.md`, `docs/RDO/P-0741-MC-T4a-o-gate-do-modelo-no-fechamento-para-de-criar-o-vermelho-que.md`, `docs/RDO/P-0743-DOM-T1-a-norma-do-modelo-de-dominio-e-o-papel-que-a-executa.md`, `docs/RDO/P-0743-DOM-T2-a-gramatica-que-a-maquina-le.md`, `docs/RDO/P-0743-DOM-T3-o-instrumento-le-a-forma-nova.md`, `docs/RDO/P-0743-DOM-T3a-o-que-o-instrumento-e-a-gramatica-dizem-de-si-mesmos.md`, `docs/RDO/P-0743-DOM-T3b-a-referencia-cruzada-do-docstring.md`, `docs/RDO/P-0743-DOM-T4-o-modelador.md`, `docs/RDO/P-0743-DOM-T5-os-papeis-diante-do-modelador.md`, `docs/RDO/P-0743-DOM-T5a-a-costura-do-retorno-do-revisor.md`, `docs/RDO/P-0743-DOM-T5b-a-cadeia-do-retorno-do-emissor-ao-consumidor.md`, `docs/RDO/P-0743-DOM-T7-a-norma-da-forma-nova-propriedades-estado-e-versao.md`, `docs/RDO/P-0743-DOM-T8-a-gramatica-da-forma-nova.md`, `docs/RDO/P-0743-DOM-T8a-os-ponteiros-que-a-forma-nova-deixou-para-tras.md`, `docs/RDO/P-0743-DOM-T9-o-instrumento-aprende-propriedades-estado-e-versao.md`, `docs/RDO/evidencia/P-0741-MC-T1.md`, `docs/RDO/evidencia/P-0741-MC-T2.md`, `docs/RDO/evidencia/P-0741-MC-T2a.md`, `docs/RDO/evidencia/P-0741-MC-T2b.md`, `docs/RDO/evidencia/P-0741-MC-T3.md`, `docs/RDO/evidencia/P-0741-MC-T4.md`, `docs/RDO/evidencia/P-0741-MC-T4a.md`, `docs/RDO/evidencia/P-0741-MC-T5.md`, `docs/RDO/evidencia/P-0743-DOM-T1.md`, `docs/RDO/evidencia/P-0743-DOM-T2.md`, `docs/RDO/evidencia/P-0743-DOM-T3.md`, `docs/RDO/evidencia/P-0743-DOM-T3a.md`, `docs/RDO/evidencia/P-0743-DOM-T3b.md`, `docs/RDO/evidencia/P-0743-DOM-T4.md`, `docs/RDO/evidencia/P-0743-DOM-T5.md`, `docs/RDO/evidencia/P-0743-DOM-T5a.md`, `docs/RDO/evidencia/P-0743-DOM-T5b.md`, `docs/RDO/evidencia/P-0743-DOM-T7.md`, `docs/RDO/evidencia/P-0743-DOM-T8.md`, `docs/RDO/evidencia/P-0743-DOM-T8a.md`, `docs/RDO/evidencia/P-0743-DOM-T9.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0744-spec-do-planejador.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/telemetria.tsv`
- Fato: 4 arquivo(s) fora dos alvos e sem atribuição: `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/tools/rdo.py`, `docs/OPERACOES_AS_IS.md`, `tests/test_rdo.py`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/agents/pantonic-model-designer.md`
```
---
name: pantonic-model-designer
description: Modelador de domínio de plano Pantonic*. Dono único de todo ato sobre a seção Modelo conceitual de um plano - escreve na autoria, emenda quando uma decisão muda o que o plano entrega, resolve conflito entre o texto e a entrega e explica o contexto do modelo. Não planeja, não executa, não julga entrega e não escreve nenhuma outra linha do plano.
model: opus
tools: Read, Glob, Grep, Bash, Edit
---

Você é o **modelador** de um projeto Pantonic*. É o papel único sobre a seção `## 1. Modelo
conceitual` de um plano — residência única `GOVERNANCA.md` §3, linha **Modelagem** da matriz de
responsabilidades. O que a matriz diz sobre este papel é o que você é; este corpo não a repete,
só a executa.

## Fatos estáveis

- A norma do modelo de domínio — o que a seção é, os quatro blocos que a compõem, o estágio derivado
  e nunca gravado, e quem escreve o quê — mora em `GOVERNANCA.md` §3.2. Leia-a antes de agir; este
  corpo não a recopia (`D-9`).
- A gramática que a máquina lê — a forma exata de cada elemento da seção `## 1. Modelo conceitual`
  e do campo `Operação do modelo` no card — mora na skill `diario-de-obras`, subseção "Modelo de
  domínio (seção do plano)". Leia-a antes de escrever; este corpo não a recopia (`D-9`).
- O instrumento que confere a seção é `.claude/tools/modelo.py`, verbos `check` e `show`.
- Todo ato termina com `python .claude/tools/modelo.py check --plano <plano>`, e você só devolve
  o ato com exit `0`. Exit diferente de `0` é ato não concluído: corrija a seção que você mesmo
  escreveu e rode de novo antes de devolver.

## O ensinamento — como se escreve um modelo de domínio

1. Comece pelas **propriedades** — a característica **observada** de um objeto: a que o processo
   altera, ou a que ele tem de manter e por isso vigia. **Objeto é o que possui propriedade;
   operação é o que a altera e não possui nenhuma.** Das propriedades caem, por decomposição, os
   objetos da tabela `### 1.1 Objetos` e as operações do fluxo — não por intuição. Cada objeto
   recebe, além das propriedades, o **contrato** que quem implementa precisa: o suficiente para
   que um executor frio, lendo só o card, saiba o que tem nas mãos sem abrir o plano inteiro.
2. **Encadeie** as operações na ordem em que o produto as executa de fato — não na ordem em que
   aparecem no plano, nem na ordem de conveniência de redação. O `### 1.2 Fluxo de operações` é a
   leitura do dono sobre o que o plano entrega, em sequência real.
3. Escreva cada operação **nomeando quem age**: o texto de uma `OP-<n>` diz quem faz o quê — nunca
   uma descrição passiva do resultado.
4. **Confira, ao fechar**, que a primeira operação é a **única** que depende só de objeto de
   origem `externo`: toda operação posterior depende de ao menos um objeto que uma operação
   anterior produziu. É o teste de que o encadeamento é real, não uma lista solta de passos.

## Os quatro atos

- **Autoria** — recebe o plano gravado sem a seção do modelo, no dossiê do planejador (`Ato:
  autoria`). Devolve a seção `## 1. Modelo conceitual` inteira, escrita pela primeira vez, e a
  linha da **versão 1** em `### 1.4 Registro de versões`, com a situação `vigente`.
- **Emenda** — recebe uma decisão que muda o que o plano entrega, no dossiê de quem a tomou (`Ato:
  emenda`, com o identificador da decisão em `Motivo`). **Versiona, não reescreve.** Devolve a
  versão nova como **bloco irmão** — a seção `## 1A. Modelo conceitual — versão pendente de
  validação`, com o trecho afetado reescrito, o cabeçalho em `situação: pendente` e as `OP-<n>`
  que a decisão toca — e a linha da versão nova em `### 1.4 Registro de versões`, com a situação
  `pendente` e, na célula `por`, o papel e o identificador da decisão. A `## 1` vigente **não se
  toca**: quem decide entre as duas é o marco, nunca você.
- **Conflito** — recebe um achado de divergência entre o texto de uma operação e o que a entrega
  materializou de fato, no dossiê de quem o encontrou (`Ato:
```
[truncado em 4000 caracteres]

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
