# Evidência de revisão — P-0743 DOM-T3a

## Diff (`git diff --stat`)
```
.claude/README.md                          |   2 +-
 .claude/agents/pantonic-consultant.md      |   4 +-
 .claude/agents/pantonic-planner.md         |  46 +-
 .claude/agents/pantonic-reviewer.md        |   9 +-
 .claude/skills/diario-de-obras/SKILL.md    |  28 +-
 .claude/skills/passagem-de-bastao/SKILL.md |   6 +-
 .claude/skills/scrum-master/SKILL.md       |  35 +-
 .claude/tools/rdo.py                       |   8 +-
 GOVERNANCA.md                              |  61 ++-
 README.md                                  |  15 +-
 docs/DIARIO_DE_OBRAS.md                    |  57 +-
 docs/RDO/INDEX.md                          |  10 +
 docs/RUBRICA_DE_REVISAO.md                 |   7 +-
 docs/plans/P-0741-modelo-conceitual.md     | 842 ++++++++++++++++++++++++++---
 docs/plans/_INBOX.md                       |   3 +-
 docs/plans/_INBOX_HISTORICO.md             |   2 +
 docs/telemetria.tsv                        |  30 +
 tests/test_rdo.py                          |  19 +
 18 files changed, 1073 insertions(+), 111 deletions(-)
```

## Arquivos tocados
- `.claude/README.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-consultant.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-planner.md` — atribuição: alheio; estado git: ` M`
- `.claude/agents/pantonic-reviewer.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/diario-de-obras/SKILL.md` — atribuição: da entrega; estado git: ` M`
- `.claude/skills/passagem-de-bastao/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/skills/scrum-master/SKILL.md` — atribuição: alheio; estado git: ` M`
- `.claude/tools/modelo.py` — atribuição: da entrega; estado git: `??`
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
- `docs/RUBRICA_DE_REVISAO.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0741-modelo-conceitual.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0743-modelo-de-dominio.md` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0744-spec-do-planejador.md` — atribuição: alheio; estado git: `??`
- `docs/plans/_INBOX.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/_INBOX_HISTORICO.md` — atribuição: alheio; estado git: ` M`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/fixtures/modelo/fluxo-concluido.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/fluxo-valido.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-forma-anterior.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-invalido-2.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-invalido.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-sem-cabecalho.md` — atribuição: alheio; estado git: `??`
- `tests/fixtures/modelo/plano-sem-modelo.md` — atribuição: alheio; estado git: `??`
- `tests/test_modelo.py` — atribuição: alheio; estado git: `??`
- `tests/test_rdo.py` — atribuição: alheio; estado git: ` M`

## Escopo
- Recorte: desde `e0efcf6`
- Arquivos-alvo declarados: `.claude/tools/modelo.py`, `argparse.ArgumentParser`, `.claude/skills/diario-de-obras/SKILL.md`
- Literais não reconhecidos como caminho (6): `I-10`, `description=(...)`, `main()`, `grep -n 'description=(' .claude/tools/modelo.py`, `I-5`, `## Gramática legível por máquina`
- Arquivos tocados: `.claude/README.md`, `.claude/agents/pantonic-consultant.md`, `.claude/agents/pantonic-planner.md`, `.claude/agents/pantonic-reviewer.md`, `.claude/skills/diario-de-obras/SKILL.md`, `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/skills/scrum-master/SKILL.md`, `.claude/tools/modelo.py`, `.claude/tools/rdo.py`, `GOVERNANCA.md`, `README.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/OPERACOES_AS_IS.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0741-MC-T1-a-norma-e-a-gramatica-do-modelo-publicadas-nas-residencias-u.md`, `docs/RDO/P-0741-MC-T2-modelo-py-check-e-show-e-o-alvo-modelo-no-gerador-de-laudo.md`, `docs/RDO/P-0741-MC-T2a-o-campo-sem-consumidor-sai-da-dataclass-do-instrumento.md`, `docs/RDO/P-0741-MC-T2b-a-cadeia-sem-consumidor-sai-inteira-do-instrumento.md`, `docs/RDO/P-0741-MC-T3-os-tres-papeis-que-escrevem-o-modelo-planejador-revisor-e-co.md`, `docs/RDO/P-0741-MC-T4-o-loop-le-confere-e-mostra-o-modelo-scrum-master-e-passagem.md`, `docs/RDO/P-0741-MC-T4a-o-gate-do-modelo-no-fechamento-para-de-criar-o-vermelho-que.md`, `docs/RDO/P-0743-DOM-T1-a-norma-do-modelo-de-dominio-e-o-papel-que-a-executa.md`, `docs/RDO/P-0743-DOM-T2-a-gramatica-que-a-maquina-le.md`, `docs/RDO/P-0743-DOM-T3-o-instrumento-le-a-forma-nova.md`, `docs/RDO/evidencia/P-0741-MC-T1.md`, `docs/RDO/evidencia/P-0741-MC-T2.md`, `docs/RDO/evidencia/P-0741-MC-T2a.md`, `docs/RDO/evidencia/P-0741-MC-T2b.md`, `docs/RDO/evidencia/P-0741-MC-T3.md`, `docs/RDO/evidencia/P-0741-MC-T4.md`, `docs/RDO/evidencia/P-0741-MC-T4a.md`, `docs/RDO/evidencia/P-0741-MC-T5.md`, `docs/RDO/evidencia/P-0743-DOM-T1.md`, `docs/RDO/evidencia/P-0743-DOM-T2.md`, `docs/RDO/evidencia/P-0743-DOM-T3.md`, `docs/RUBRICA_DE_REVISAO.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0743-modelo-de-dominio.md`, `docs/plans/P-0744-spec-do-planejador.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/telemetria.tsv`, `tests/fixtures/modelo/fluxo-concluido.md`, `tests/fixtures/modelo/fluxo-valido.md`, `tests/fixtures/modelo/plano-forma-anterior.md`, `tests/fixtures/modelo/plano-invalido-2.md`, `tests/fixtures/modelo/plano-invalido.md`, `tests/fixtures/modelo/plano-sem-cabecalho.md`, `tests/fixtures/modelo/plano-sem-modelo.md`, `tests/test_modelo.py`, `tests/test_rdo.py`
- Atribuídos a outra tarefa do mesmo plano: `.claude/README.md` → `DOM-T4`, `.claude/agents/pantonic-consultant.md` → `DOM-T5`, `.claude/agents/pantonic-planner.md` → `DOM-T5`, `.claude/agents/pantonic-reviewer.md` → `DOM-T5`, `.claude/skills/scrum-master/SKILL.md` → `DOM-T5`, `GOVERNANCA.md` → `DOM-T1`, `README.md` → `DOM-T4`, `docs/RUBRICA_DE_REVISAO.md` → `DOM-T1`, `tests/fixtures/modelo/fluxo-concluido.md` → `DOM-T3`, `tests/fixtures/modelo/fluxo-valido.md` → `DOM-T3`, `tests/fixtures/modelo/plano-invalido.md` → `DOM-T3`, `tests/fixtures/modelo/plano-sem-cabecalho.md` → `DOM-T3`, `tests/fixtures/modelo/plano-sem-modelo.md` → `DOM-T3`, `tests/test_modelo.py` → `DOM-T3`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/RDO/INDEX.md`, `docs/RDO/P-0741-MC-T1-a-norma-e-a-gramatica-do-modelo-publicadas-nas-residencias-u.md`, `docs/RDO/P-0741-MC-T2-modelo-py-check-e-show-e-o-alvo-modelo-no-gerador-de-laudo.md`, `docs/RDO/P-0741-MC-T2a-o-campo-sem-consumidor-sai-da-dataclass-do-instrumento.md`, `docs/RDO/P-0741-MC-T2b-a-cadeia-sem-consumidor-sai-inteira-do-instrumento.md`, `docs/RDO/P-0741-MC-T3-os-tres-papeis-que-escrevem-o-modelo-planejador-revisor-e-co.md`, `docs/RDO/P-0741-MC-T4-o-loop-le-confere-e-mostra-o-modelo-scrum-master-e-passagem.md`, `docs/RDO/P-0741-MC-T4a-o-gate-do-modelo-no-fechamento-para-de-criar-o-vermelho-que.md`, `docs/RDO/P-0743-DOM-T1-a-norma-do-modelo-de-dominio-e-o-papel-que-a-executa.md`, `docs/RDO/P-0743-DOM-T2-a-gramatica-que-a-maquina-le.md`, `docs/RDO/P-0743-DOM-T3-o-instrumento-le-a-forma-nova.md`, `docs/RDO/evidencia/P-0741-MC-T1.md`, `docs/RDO/evidencia/P-0741-MC-T2.md`, `docs/RDO/evidencia/P-0741-MC-T2a.md`, `docs/RDO/evidencia/P-0741-MC-T2b.md`, `docs/RDO/evidencia/P-0741-MC-T3.md`, `docs/RDO/evidencia/P-0741-MC-T4.md`, `docs/RDO/evidencia/P-0741-MC-T4a.md`, `docs/RDO/evidencia/P-0741-MC-T5.md`, `docs/RDO/evidencia/P-0743-DOM-T1.md`, `docs/RDO/evidencia/P-0743-DOM-T2.md`, `docs/RDO/evidencia/P-0743-DOM-T3.md`, `docs/plans/P-0741-modelo-conceitual.md`, `docs/plans/P-0743-modelo-de-dominio.md`, `docs/plans/P-0744-spec-do-planejador.md`, `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/telemetria.tsv`
- Fato: 6 arquivo(s) fora dos alvos e sem atribuição: `.claude/skills/passagem-de-bastao/SKILL.md`, `.claude/tools/rdo.py`, `docs/OPERACOES_AS_IS.md`, `tests/fixtures/modelo/plano-forma-anterior.md`, `tests/fixtures/modelo/plano-invalido-2.md`, `tests/test_rdo.py`
- Veredito mecânico: (aberto — depende de declaração de desvio na entrega, não coletada por este script; ver docs/RUBRICA_DE_REVISAO.md:63-77)

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `.claude/tools/modelo.py`
```
"""`modelo.py` — os verbos `check` e `show` sobre a seção `## 1. Modelo conceitual` de um plano,
na superfície normativa da `### 6. Superfície do instrumento modelo.py` de
`docs/plans/P-0743-modelo-de-dominio.md`.

Gramática lida (residência única: skill `diario-de-obras`, subseção "Modelo de domínio (seção do
plano)"): cabeçalho `**Estado do modelo:**`, tabela `### 1.1 Objetos`, `### 1.2 Fluxo de
operações` — pares de linhas `- **OP-<n>** — <texto>` e o sub-bullet com `precisa de:` e
`tarefas:`, com subtítulos `**A. …**` livres — e tabela `### 1.3 Mudanças do modelo`.

`check` julga a seção contra o vocabulário fechado de violações `V1`..`V14` (`### 6` do `P-0743`)
e `show` deriva a leitura do dono a partir do modelo real: ela abre pelo estágio atual, que é a
primeira operação ainda não concluída, derivada do status das tarefas e não gravada por nenhum
papel. Ambos carregam `backlog.py` por caminho (`importlib.util.spec_from_file_location`) e
chamam `backlog._parse_plano` para obter `Plano.tarefas`; `backlog.py` não é reescrito (`I-3` do
`P-0743`)."""
from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


def _default_root() -> Path:
    return Path(__file__).resolve().parent.parent.parent


def _forcar_utf8(stream) -> None:
    """Console cp1252 do Windows estoura `UnicodeEncodeError` ao imprimir `—` — duplicado do
    mesmo utilitário de `card_check.py`/`review_evidence.py` (`DM-11`, sem import cruzado)."""
    reconfigure = getattr(stream, "reconfigure", None)
    if reconfigure is not None:
        reconfigure(encoding="utf-8", errors="replace")


def _load_backlog(root: Path):
    caminho = root / ".claude" / "tools" / "backlog.py"
    spec = importlib.util.spec_from_file_location("backlog", caminho)
    modulo = importlib.util.module_from_spec(spec)
    # Dataclasses com `from __future__ import annotations` resolvem anotações via
    # `sys.modules[cls.__module__]` — precisa estar registrado antes do exec_module (mesmo padrão
    # de `tests/test_backlog.py`).
    sys.modules[spec.name] = modulo
    spec.loader.exec_module(modulo)
    return modulo


# --------------------------------------------------------------------------- #
# Modelo de dados
# --------------------------------------------------------------------------- #


@dataclass
class Operacao:
    numero: int
    texto: str
    precisa_de: list[str] = field(default_factory=list)
    tarefas: list[str] = field(default_factory=list)


@dataclass
class Objeto:
    nome: str
    contrato: str
    origem: str


@dataclass
class Modelo:
    versao: int
    data: str
    objetos: list[Objeto] = field(default_factory=list)
    operacoes: list[Operacao] = field(default_factory=list)
    mudancas: list[str] = field(default_factory=list)
    tabela_objetos: list[str] = field(default_factory=list)
    subtitulos: dict[int, str] = field(default_factory=dict)
    cabecalho_presente: bool = True
    mudancas_presente: bool = True


_MSG_AUSENTE = "modelo: ausente — plano anterior à doutrina (sem '## 1. Modelo conceitual')"

_MSG_FORMA_ANTERIOR = (
    "modelo: forma anterior — plano na forma de orações (sem '### 1.2 Fluxo de operações')"
)

_OPERACAO_HEADER_RE = re.compile(r"^- \*\*OP-(\d+)\*\* — (.+)$")
_OPERACAO_LINHA_RE = re.compile(r"^  - `precisa de: ([^`]*)` · `tarefas: ([^`]*)`$")
_SUBTITULO_RE = re.compile(r"^\*\*[A-Z]\. .+\*\*$")
_CAMPO_OPERACAO_RE = re.compile(r"^- \*\*Operação do modelo:\*\* (.+)$", re.MULTILINE)
_ID_OP_RE = re.compile(r"`(OP-\d+)`")
_CABECALHO_VALOR_RE = re.compile(r"\*\*Estado do modelo:\*\* versão (\d+) · (\d{4}-\d{2}-\d{2})")
_MUDANCA_DATA_RE = re.compile(r"^\|\s*MD-\d+\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|")
_ORIGEM_OP_RE = re.compile(r"^OP-(\d+)$")

_STATUS_CONCLUSIVO = {"done", "cancelled"}
_STATUS_EM_CURSO = {"in-progress", "review"}


def _extrair_tabela(secao: list[str], heading: str) -> list[str]:
    idx = next((i for i, l in enumerate
```
[truncado em 4000 caracteres]

### `argparse.ArgumentParser`
```
(sem diferença coletável — arquivo ausente na árvore de trabalho)
```

### `.claude/skills/diario-de-obras/SKILL.md`
```
diff --git a/.claude/skills/diario-de-obras/SKILL.md b/.claude/skills/diario-de-obras/SKILL.md
index fd525c0..f44ca85 100644
--- a/.claude/skills/diario-de-obras/SKILL.md
+++ b/.claude/skills/diario-de-obras/SKILL.md
@@ -131,7 +131,9 @@ objeto:
 
 Transcrição normativa de `docs/plans/P-0739-backlog-instrumento.md` §2.1–§2.4 e §2.7 — é a
 gramática que `.claude/tools/backlog.py` (§3 do mesmo plano) lê e escreve. Esta seção é a
-residência única do texto; o plano de origem não a recopia depois da transcrição.
+residência única do texto; o plano de origem não a recopia depois da transcrição. A subseção
+"Modelo de domínio (seção do plano)" transcreve `docs/plans/P-0743-modelo-de-dominio.md` §5 e é
+lida por `.claude/tools/modelo.py`.
 
 ### Item e residência
 
@@ -170,11 +172,27 @@ Linha viva: começa com `- ` e contém um caminho `docs/plans/P-NNNN-<slug>.md`
 Drenada: prefixada `- [drenado AAAA-MM-DD] ` e movida **verbatim** para `_INBOX_HISTORICO.md`.
 Contador: `**Próximo id de plano: P-NNNN.**` — `drain` o recalcula como `max(id visto) + 1`.
 
-### Máquina de transições (forma para o instrumento)
+### Modelo de domínio (seção do plano)
 
-Tabela da residência única acima ("Status — residência única" → "Máquina de transições") transcrita
-para `_TRANSICOES: dict[tuple[str, str], ...]`; `blocked` exige `--razao`; `done`/`cancelled` são
-terminais; `superseded` só para plano. Transição fora da tabela → exit 1 sem escrever nada.
+Seção `## 1. Modelo conceitual` do plano (`GOVERNANCA.md` §3.2), delimitada pelo próximo heading de
+nível 2. Dentro dela, nesta ordem:
+
+| elemento | forma | regra |
+|---|---|---|
+| cabeçalho | `**Estado do modelo:** versão <n> · AAAA-MM-DD · autor: <papel> · <k> operações · última mudança: <MD-<n> \| nenhuma>` | linha única; obrigatória (`V13`) |
+| objetos | `### 1.1 Objetos` + tabela `\| objeto \| o que é \| contrato \| origem \|`; `<objeto>` é um nome em linguagem corrente, único na tabela; `<origem>` é `externo` ou `OP-<n>` | obrigatória (`V13`); `<origem>` `OP-<n>` existe no fluxo (`V7`); objeto de origem `externo` é citado por alguma operação (`V6`) |
+| operações | `### 1.2 Fluxo de operações`; cada operação é o par de linhas: `- **OP-<n>** — <texto>` e, na linha seguinte, `  - \`precisa de: <objeto>[, <objeto>]\` · \`tarefas: <ID>[, <ID>]\`` | numeração `1..k` na ordem do encadeamento, sem salto (`V8`); `<n>` único (`V11`); `<texto>` sem crase e sem `/` (`V12`); todo `<objeto>` existe na tabela de objetos (`V5`); toda `<ID>` existe como `### <ID> — …` no plano (`V3`); lista de tarefas não vazia (`V1`); operação com `<n>` maior que 1 cita ao menos um objeto de origem `OP-<m>` (`V9`), e esse `<m>` é menor que `<n>` (`V10`). Subtítulos `**A. …**` entre operações são livres e ignorados |
+| mudanças | `### 1.3 Mudanças do modelo` + tabela `\| id \| data \| autor \| operações \| o que mudou e por quê \|`; linha `\| MD-<n> \| AAAA-MM-DD \| <papel> · <ref> \| OP-<a>, OP-<b> \| <texto> \|`; sem mudança, uma linha com `—` nas quatro primeiras células | obrigatória (`V13`) |
+| campo do card | `- **Operação do modelo:** \`OP-<a>\`[, \`OP-<b>\`]` como campo de todo `### <ID> — …` do plano, seguido, por operação citada, de dois sub-bullets: `  - OP-<a>: <texto copiado>` e `  - precisa de: <objeto> — <contrato copiado>[; <objeto> — <contrato copiado>]` | obrigatório em toda tarefa do plano (`V2`); toda `OP-<a>` citada existe (`V4`); os dois sub-bullets existem para cada operação citada (`V14`) |
+
+**Andamento, nunca gravado.** Nenhum elemento da seção carrega estado. `modelo.py show` deriva:
+operação `concluída` quando todas as tarefas dela estão `done` ou `cancelled`; `em curso` quando
+alguma está `in-progress` ou `review`; `prevista` nos demais casos. O **estágio atual** é a
+primeira operação não `concluída`, e é `concluído` quando não há nenhuma.
+
+Plano sem a seção `## 1. Modelo conceitual`, e plano com a seção mas sem o heading
+`### 1.2 Fluxo de operações`, são **forma anterior**: `modelo.py ch
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
