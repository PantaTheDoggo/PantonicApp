"""DOM-T9 (`docs/plans/P-0743-modelo-de-dominio.md` `### DOM-T9`) — TF de `.claude/tools/modelo.py`:
os verbos `check` e `show` sobre a forma nova do modelo de domínio (objetos com propriedades,
fluxo de operações com `altera:`, estado inicial e final, registro de versões e versão pendente),
contra as fixtures sintéticas de `tests/fixtures/modelo/` (nenhuma é card vivo de plano —
`DM-38` (ii)). Padrão de carga do módulo idêntico a `tests/test_card_check.py` (`.claude/` não é
pacote importável).

Gramática lida (residência única: skill `diario-de-obras`, subseção "Modelo de domínio (seção do
plano)"): cabeçalho `**Estado do modelo:**`, `### 1.1 Objetos` (com `propriedades`),
`### 1.2 Fluxo de operações` (pares `- **OP-<n>** — <texto>` /
`  - \x60precisa de: ...\x60 · \x60altera: ...\x60 · \x60tarefas: ...\x60`), `### 1.3 Estado inicial
e estado final` e `### 1.4 Registro de versões`. A versão pendente nasce como o bloco irmão
`## 1A. Modelo conceitual — versão pendente de validação`.

`check` julga a seção contra o vocabulário fechado de violações `V1`..`V20` (`### 16` do plano) e
`show` deriva a leitura do dono a partir do andamento real das tarefas — nunca gravado (`M-3`) —,
com `--pendente` para o bloco `## 1A` e `--drift` para a diferença entre as duas versões. Ambos
carregam `backlog.py` por caminho (`importlib.util.spec_from_file_location`) e chamam
`backlog._parse_plano` para obter `Plano.tarefas`; `backlog.py` não é reescrito (`I-1`).

Os testes de `V15`..`V20` chamam `validar`/`montar_drift` diretamente com `Modelo`/`Operacao`/
`Objeto` sintéticos e um `plano` stub (`SimpleNamespace`), sem fixture própria — mesmo padrão já
usado por `test_tf_show_estagio_pula_operacao_concluida_fora_de_ordem` (variação inline, sem
arquivo). `test_tf_show_desde_filtra_mudancas` não sobrevive à forma nova: `--desde` não está na
superfície normativa de `### 16` (só `--plano`, `--root`, `--pendente`, `--drift`) — mudanças por
data foram substituídas por versões e drift; o piso de regressão desconta este teste removido."""
from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path
from types import SimpleNamespace

_ROOT = Path(__file__).resolve().parents[1]
_MODELO_PATH = _ROOT / ".claude" / "tools" / "modelo.py"
_FIXTURES = _ROOT / "tests" / "fixtures" / "modelo"
_PLANO_INVALIDO = _FIXTURES / "plano-invalido.md"
_PLANO_INVALIDO_2 = _FIXTURES / "plano-invalido-2.md"
_PLANO_SEM_CABECALHO = _FIXTURES / "plano-sem-cabecalho.md"
_PLANO_SEM_MODELO = _FIXTURES / "plano-sem-modelo.md"
_PLANO_FORMA_ANTERIOR = _FIXTURES / "plano-forma-anterior.md"
_PLANO_SEM_ESTADO = _FIXTURES / "plano-sem-estado.md"
_FLUXO_VALIDO = _FIXTURES / "fluxo-valido.md"
_FLUXO_CONCLUIDO = _FIXTURES / "fluxo-concluido.md"
_FLUXO_PENDENTE = _FIXTURES / "fluxo-pendente.md"


def _load_modelo():
    spec = importlib.util.spec_from_file_location("modelo", _MODELO_PATH)
    modulo = importlib.util.module_from_spec(spec)
    # Dataclasses com `from __future__ import annotations` resolvem anotações via
    # `sys.modules[cls.__module__]` — precisa estar registrado antes do exec_module (mesmo padrão
    # de `tests/test_backlog.py`).
    sys.modules[spec.name] = modulo
    spec.loader.exec_module(modulo)
    return modulo


def _plano_stub(tarefas):
    return SimpleNamespace(id="P-TESTE", titulo="Plano de teste sintético", tarefas=tarefas)


def _tarefa_stub(id_, texto=""):
    return SimpleNamespace(id=id_, texto=texto)


def test_tf_check_fluxo_valido_sai_zero(capsys):
    """`fluxo-valido.md` tem quatro objetos (uma propriedade cada), três operações e três tarefas
    — `check` sai 0 com a linha
    `modelo: OK — 3 operações, 4 objetos, 4 propriedades, 3 tarefas, versão 1`."""
    modelo = _load_modelo()

    codigo = modelo.main(["check", "--plano", str(_FLUXO_VALIDO), "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 0
    assert "modelo: OK — 3 operações, 4 objetos, 4 propriedades, 3 tarefas, versão 1" in saida.out


def test_tf_check_forma_nova_sai_zero(capsys):
    """A linha `modelo: OK — ` traz as cinco contagens da `### 16`: operações, objetos,
    propriedades, tarefas e versão, nesta ordem."""
    modelo = _load_modelo()

    codigo = modelo.main(["check", "--plano", str(_FLUXO_VALIDO), "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 0
    padrao = (
        r"^modelo: OK — \d+ operações, \d+ objetos, \d+ propriedades, \d+ tarefas, versão \d+"
    )
    assert re.match(padrao, saida.out)


def test_tf_check_invalido_lista_catorze_violacoes_na_ordem(capsys):
    """As catorze violações do vocabulário `V1`..`V14` disparam, uma vez cada, somando as duas
    metades da fixture (`plano-invalido.md` e `plano-invalido-2.md` — contingência 2 da `DOM-T3`:
    a numeração estrita de `V8`..`V11` não convive, num só arquivo, com as violações de sujeito
    `OP-<n>` mais simples sem uma esconder a outra). Cada metade sai 1, e a ordem dentro de cada
    uma é a que a `### 16` fixa: sujeito `OP-<n>`/`secao` pela ordem do arquivo, depois `objeto`
    pela ordem da tabela, depois `<ID>` pela ordem das tarefas. As duas fixtures têm propriedades,
    `altera:`, estado e registro de versões válidos, para que só as catorze violações-alvo
    disparem (`V15`..`V20` ficam limpas)."""
    modelo = _load_modelo()

    codigo_a = modelo.main(["check", "--plano", str(_PLANO_INVALIDO), "--root", str(_ROOT)])
    saida_a = capsys.readouterr()
    codigo_b = modelo.main(["check", "--plano", str(_PLANO_INVALIDO_2), "--root", str(_ROOT)])
    saida_b = capsys.readouterr()

    assert codigo_a == 1
    assert codigo_b == 1

    esperado_a_na_ordem = [
        "V13 secao — cabeçalho, objetos, estado ou registro de versões ausente",
        "V5 OP-1 — objeto inexistente objeto fantasma",
        "V1 OP-2 — operação sem tarefa",
        "V3 OP-3 — tarefa inexistente EX-T99",
        "V12 OP-4 — literal técnico no texto",
        "V6 objeto — objeto externo sem uso objeto sem uso",
        "V7 objeto — origem inexistente objeto orfão",
        "V2 EX-T2 — tarefa sem operação",
        "V4 EX-T3 — operação inexistente OP-77",
        "V14 EX-T4 — contrato ausente para OP-2",
    ]
    posicoes_a = [saida_a.err.index(linha) for linha in esperado_a_na_ordem]
    assert posicoes_a == sorted(posicoes_a)
    assert "modelo: FALHOU — 10 violação(ões)" in saida_a.err

    esperado_b_na_ordem = [
        "V9 OP-2 — operação desencadeada",
        "V10 OP-3 — objeto produzido depois objeto de OP-5",
        "V8 OP-3 — fora da sequência",
        "V11 OP-3 — identificador duplicado",
    ]
    posicoes_b = [saida_b.err.index(linha) for linha in esperado_b_na_ordem]
    assert posicoes_b == sorted(posicoes_b)
    assert "modelo: FALHOU — 4 violação(ões)" in saida_b.err


def test_tf_check_sem_cabecalho_v13(capsys):
    """`plano-sem-cabecalho.md` está na forma nova, mas sem `**Estado do modelo:**` — `check` sai 1
    com a violação `V13 secao`, no literal novo que a `### 16` republica."""
    modelo = _load_modelo()

    codigo = modelo.main(["check", "--plano", str(_PLANO_SEM_CABECALHO), "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 1
    assert (
        "V13 secao — cabeçalho, objetos, estado ou registro de versões ausente" in saida.err
    )


def test_tf_check_v13_literal_novo():
    """O literal exato de `V13` que a `### 16` republica, disparado por `validar` sobre um modelo
    sintético sem cabeçalho."""
    modelo = _load_modelo()

    modelo_sintetico = modelo.Modelo(versao=1, data="2026-09-21", cabecalho_presente=False)
    plano = _plano_stub([])

    violacoes = modelo.validar(modelo_sintetico, plano)

    assert "V13 secao — cabeçalho, objetos, estado ou registro de versões ausente" in violacoes


def test_tf_check_objeto_sem_propriedade_v15():
    """Objeto com `propriedades` vazia dispara `V15`."""
    modelo = _load_modelo()

    objeto = modelo.Objeto(
        nome="objeto sem propriedade", contrato="c", origem="externo", propriedades=[]
    )
    modelo_sintetico = modelo.Modelo(versao=1, data="2026-09-21", objetos=[objeto])
    plano = _plano_stub([])

    violacoes = modelo.validar(modelo_sintetico, plano)

    assert any(
        v.startswith("V15 objeto — objeto sem propriedade") for v in violacoes
    )


def test_tf_check_altera_propriedade_inexistente_v16():
    """`altera:` citando `<objeto>.<propriedade>` que não está na tabela de objetos dispara
    `V16`."""
    modelo = _load_modelo()

    objeto = modelo.Objeto(nome="objeto x", contrato="c", origem="externo", propriedades=["estado"])
    operacao = modelo.Operacao(
        numero=1,
        texto="Opera sobre objeto x.",
        precisa_de=["objeto x"],
        altera=["objeto x.propriedade inexistente"],
        tarefas=["T-1"],
    )
    modelo_sintetico = modelo.Modelo(
        versao=1, data="2026-09-21", objetos=[objeto], operacoes=[operacao]
    )
    plano = _plano_stub([_tarefa_stub("T-1")])

    violacoes = modelo.validar(modelo_sintetico, plano)

    assert any(v.startswith("V16 OP-") for v in violacoes)


def test_tf_check_propriedade_sem_estado_v17():
    """Propriedade da tabela de objetos sem linha em `### 1.3 Estado inicial e estado final`
    dispara `V17`."""
    modelo = _load_modelo()

    objeto = modelo.Objeto(nome="objeto y", contrato="c", origem="externo", propriedades=["estado"])
    modelo_sintetico = modelo.Modelo(versao=1, data="2026-09-21", objetos=[objeto], estado=[])
    plano = _plano_stub([])

    violacoes = modelo.validar(modelo_sintetico, plano)

    assert any(v.startswith("V17 objeto — propriedade sem estado") for v in violacoes)


def test_tf_check_operacao_sem_altera_v18():
    """Operação sem `altera:`, ou com `altera:` vazio, dispara `V18`."""
    modelo = _load_modelo()

    operacao = modelo.Operacao(
        numero=1, texto="Opera sem alterar nada.", precisa_de=[], altera=[], tarefas=["T-1"]
    )
    modelo_sintetico = modelo.Modelo(versao=1, data="2026-09-21", operacoes=[operacao])
    plano = _plano_stub([_tarefa_stub("T-1")])

    violacoes = modelo.validar(modelo_sintetico, plano)

    assert any(v.startswith("V18 OP-") for v in violacoes)


def test_tf_check_registro_sem_vigente_unico_v19():
    """`### 1.4 Registro de versões` sem exatamente uma linha `vigente` dispara `V19` — aqui, com
    duas."""
    modelo = _load_modelo()

    modelo_sintetico = modelo.Modelo(
        versao=1,
        data="2026-09-21",
        versoes=[
            "| 1 | 2026-09-10 | vigente | dono |",
            "| 2 | 2026-09-21 | vigente | dono |",
        ],
    )
    plano = _plano_stub([])

    violacoes = modelo.validar(modelo_sintetico, plano)

    assert any(v.startswith("V19 secao") for v in violacoes)


def test_tf_check_pendente_fora_de_sequencia_v20():
    """`## 1A` presente com versão diferente da vigente mais um dispara `V20`."""
    modelo = _load_modelo()

    modelo_vigente = modelo.Modelo(versao=1, data="2026-09-10")
    modelo_pendente = modelo.Modelo(versao=3, data="2026-09-21")
    plano = _plano_stub([])

    violacoes = modelo.validar(modelo_vigente, plano, modelo_pendente)

    assert any(v.startswith("V20 secao") for v in violacoes)


def test_tf_check_forma_anterior_sai_dois(capsys):
    """`plano-forma-anterior.md` tem `## 1. Modelo conceitual`, mas não tem `### 1.2 Fluxo de
    operações` (é a forma de orações da `MC-T2`) — `check` sai 2 com a substring `modelo: forma
    anterior — plano na forma de orações`. Poder discriminante: a regra concorrente (tratar forma
    anterior como plano sem seção) daria `modelo: ausente — plano anterior à doutrina`, que é
    diferente."""
    modelo = _load_modelo()

    codigo = modelo.main(["check", "--plano", str(_PLANO_FORMA_ANTERIOR), "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 2
    assert "modelo: forma anterior — plano na forma de orações" in saida.out


def test_tf_check_sem_estado_sai_dois(capsys):
    """`plano-sem-estado.md` tem `## 1` e `### 1.2 Fluxo de operações`, mas não `### 1.3 Estado
    inicial e estado final` — `check` sai 2 com `modelo: forma anterior — plano sem estado inicial
    e final`. Poder discriminante: a regra concorrente (tratar como violação `V13`) daria exit
    `1`."""
    modelo = _load_modelo()

    codigo = modelo.main(["check", "--plano", str(_PLANO_SEM_ESTADO), "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 2
    assert "modelo: forma anterior — plano sem estado inicial e final" in saida.out


def test_tf_check_sem_modelo_sai_dois(capsys):
    """`plano-sem-modelo.md` não tem `## 1. Modelo conceitual` — `check` sai 2 com a substring
    `modelo: ausente — plano anterior à doutrina`."""
    modelo = _load_modelo()

    codigo = modelo.main(["check", "--plano", str(_PLANO_SEM_MODELO), "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 2
    assert "modelo: ausente — plano anterior à doutrina" in saida.out


def test_tf_show_tres_rotulos_e_estagio_atual(capsys):
    """`show` sobre `fluxo-valido.md` traz os três rótulos de andamento, uma vez cada, e a linha de
    estado com `estágio atual: OP-2 —` — a primeira operação não concluída."""
    modelo = _load_modelo()

    codigo = modelo.main(["show", "--plano", str(_FLUXO_VALIDO), "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 0
    assert saida.out.count("[concluída]") == 1
    assert saida.out.count("[em curso ]") == 1
    assert saida.out.count("[prevista ]") == 1
    assert "estágio atual: OP-2 —" in saida.out


def test_tf_show_estagio_pula_operacao_concluida_fora_de_ordem():
    """Variação inline (sem fixture própria): a primeira operação está `prevista` e a segunda
    `concluída` — `derivar_estagio` devolve `OP-1 —`, a primeira operação não concluída na ordem do
    fluxo. Poder discriminante: a regra concorrente (primeira `em curso`, ou primeira não
    `prevista`) devolveria `OP-2`."""
    modelo = _load_modelo()

    op1 = modelo.Operacao(numero=1, texto="Primeira, ainda não iniciada", tarefas=["T-1"])
    op2 = modelo.Operacao(numero=2, texto="Segunda, já concluída", tarefas=["T-2"])
    modelo_sintetico = modelo.Modelo(versao=1, data="2026-09-20", operacoes=[op1, op2])
    status_por_id = {"T-1": "ready", "T-2": "done"}

    estagio = modelo.derivar_estagio(modelo_sintetico, status_por_id)

    assert estagio.startswith("OP-1 —")


def test_tf_show_fluxo_concluido_sem_estagio(capsys):
    """`fluxo-concluido.md` tem as três tarefas fechadas — a linha de estado termina em `estágio
    atual: concluído`, e a saída não tem `[prevista ]` nem `[em curso ]`."""
    modelo = _load_modelo()

    codigo = modelo.main(["show", "--plano", str(_FLUXO_CONCLUIDO), "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 0
    assert "estágio atual: concluído" in saida.out
    assert "[prevista ]" not in saida.out
    assert "[em curso ]" not in saida.out


def test_tf_show_forma_anterior_sai_dois(capsys):
    """`show` sobre `plano-forma-anterior.md` sai 2 com a mesma substring de forma anterior que
    `check` imprime."""
    modelo = _load_modelo()

    codigo = modelo.main(["show", "--plano", str(_PLANO_FORMA_ANTERIOR), "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 2
    assert "modelo: forma anterior — plano na forma de orações" in saida.out


def test_tf_show_vigente_por_omissao(capsys):
    """`show` sobre `fluxo-pendente.md`, sem modificador, mostra só a versão vigente: a saída não
    contém o objeto nem a versão que só existem no bloco `## 1A`. Poder discriminante: a regra
    concorrente (mostrar a mais recente) mostraria a pendente."""
    modelo = _load_modelo()

    codigo = modelo.main(["show", "--plano", str(_FLUXO_PENDENTE), "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 0
    assert "resultado beta" not in saida.out
    assert "situação: vigente" in saida.out
    assert "situação: pendente" not in saida.out


def test_tf_show_pendente(capsys):
    """`--pendente` sobre `fluxo-pendente.md` traz a versão pendente: o objeto novo do bloco
    `## 1A` e `situação: pendente` aparecem na saída."""
    modelo = _load_modelo()

    codigo = modelo.main(
        ["show", "--plano", str(_FLUXO_PENDENTE), "--pendente", "--root", str(_ROOT)]
    )
    saida = capsys.readouterr()

    assert codigo == 0
    assert "resultado beta" in saida.out
    assert "situação: pendente" in saida.out


def test_tf_show_drift_tres_marcadores(capsys):
    """`--drift` sobre `fluxo-pendente.md` traz os três marcadores de diferença, de três caracteres
    com os colchetes: `[+]`, `[-]` e `[~]`."""
    modelo = _load_modelo()

    codigo = modelo.main(["show", "--plano", str(_FLUXO_PENDENTE), "--drift", "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 0
    assert saida.out.startswith("# Drift do modelo — ")
    assert "[+]" in saida.out
    assert "[-]" in saida.out
    assert "[~]" in saida.out


def test_tf_show_drift_sem_pendente_sai_dois(capsys):
    """`--drift` sobre `fluxo-valido.md`, que não tem `## 1A`, sai 2 com `modelo: sem versão
    pendente`."""
    modelo = _load_modelo()

    codigo = modelo.main(["show", "--plano", str(_FLUXO_VALIDO), "--drift", "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 2
    assert "modelo: sem versão pendente" in saida.out


def test_tf_show_drift_sem_diferenca():
    """Variação inline (sem fixture própria, mesmo padrão de
    `test_tf_show_estagio_pula_operacao_concluida_fora_de_ordem`): vigente e pendente têm objetos,
    fluxo e estado idênticos — `montar_drift` não encontra diferença nenhuma e devolve `sem
    drift`."""
    modelo = _load_modelo()

    objeto = modelo.Objeto(
        nome="insumo", contrato="um registro", origem="externo", propriedades=["status"]
    )
    operacao = modelo.Operacao(
        numero=1,
        texto="Única operação.",
        precisa_de=["insumo"],
        altera=["insumo.status"],
        tarefas=["EX-T1"],
    )
    estado = [("insumo.status", "rascunho", "validado")]
    vigente = modelo.Modelo(
        versao=1, data="2026-09-10", objetos=[objeto], operacoes=[operacao], estado=estado
    )
    pendente = modelo.Modelo(
        versao=2, data="2026-09-20", objetos=[objeto], operacoes=[operacao], estado=estado
    )

    resultado = modelo.montar_drift(vigente, pendente)

    assert resultado == "sem drift"
