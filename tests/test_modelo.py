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

`check` julga a seção contra o vocabulário fechado de violações `V1`..`V21` (`### 16` do plano) e
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
import shutil
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
_FLUXO_PENDENTE_CONTRATO = _FIXTURES / "fluxo-pendente-contrato.md"
_PLANO_SEM_LASTRO = _FIXTURES / "plano-sem-lastro.md"
_PLANO_COM_LASTRO = _FIXTURES / "plano-com-lastro.md"
_PLANO_TERMINAL_SEM_LASTRO = _FIXTURES / "plano-terminal-sem-lastro.md"


def _load_modelo():
    spec = importlib.util.spec_from_file_location("modelo", _MODELO_PATH)
    modulo = importlib.util.module_from_spec(spec)
    # Dataclasses com `from __future__ import annotations` resolvem anotações via
    # `sys.modules[cls.__module__]` — precisa estar registrado antes do exec_module (mesmo padrão
    # de `tests/test_backlog.py`).
    sys.modules[spec.name] = modulo
    spec.loader.exec_module(modulo)
    return modulo


def _plano_stub(tarefas, status="in-progress"):
    return SimpleNamespace(
        id="P-TESTE", titulo="Plano de teste sintético", tarefas=tarefas, status=status
    )


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


def test_tf_check_v21_objeto_sem_lastro_declarado(capsys):
    """`plano-sem-lastro.md` tem dois objetos sem a sexta coluna de `### 1.1` — `check` acusa
    `V21` uma vez por objeto e sai 1 (`DLS-1`, `DLS-17`)."""
    modelo = _load_modelo()

    codigo = modelo.main(["check", "--plano", str(_PLANO_SEM_LASTRO), "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 1
    assert "V21 objeto — objeto sem lastro declarado insumo do teste" in saida.err
    assert "V21 objeto — objeto sem lastro declarado resultado do teste" in saida.err
    assert "modelo: FALHOU — 2 violação(ões)" in saida.err


def test_tf_check_v21_cabecalho_qualificado_nao_acusa_sai_zero(capsys):
    """`plano-com-lastro.md` declara a coluna sob o cabeçalho qualificado `lastro na §0` — o
    casamento é por prefixo (`DLS-15`), `check` não acusa `V21` e sai 0."""
    modelo = _load_modelo()

    codigo = modelo.main(["check", "--plano", str(_PLANO_COM_LASTRO), "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 0
    assert "modelo: OK" in saida.out


def test_tf_check_v21_nao_alcanca_status_terminal_sai_zero(capsys):
    """`plano-terminal-sem-lastro.md` está `done` — a violação `V21` não alcança plano em status
    terminal (`DLS-12`), mesmo sem a coluna de lastro."""
    modelo = _load_modelo()

    codigo = modelo.main(
        ["check", "--plano", str(_PLANO_TERMINAL_SEM_LASTRO), "--root", str(_ROOT)]
    )
    saida = capsys.readouterr()

    assert codigo == 0
    assert "modelo: OK" in saida.out


def test_tf_check_operacao_com_e_sem_campo_lastro_mesmo_conjunto():
    """A linha de máquina de `### 1.2` é lida com e sem o quarto campo `lastro:` — as duas formas
    produzem o mesmo conjunto de `precisa_de`/`altera`/`tarefas` (`F-17`)."""
    modelo = _load_modelo()

    linhas_sem = _FLUXO_VALIDO.read_text(encoding="utf-8").splitlines()
    linhas_com = _PLANO_COM_LASTRO.read_text(encoding="utf-8").splitlines()
    modelo_sem = modelo.extrair_modelo(linhas_sem, modelo._HEADING_VIGENTE)
    modelo_com = modelo.extrair_modelo(linhas_com, modelo._HEADING_VIGENTE)

    assert len(modelo_sem.operacoes) == 3
    assert len(modelo_com.operacoes) == 1
    op = modelo_com.operacoes[0]
    assert op.precisa_de == ["insumo com lastro"]
    assert op.altera == ["resultado com lastro.status"]
    assert op.tarefas == ["LT2-T1"]


def test_tf_check_estado_tres_e_quatro_colunas_mesmo_conjunto():
    """`### 1.3` com três colunas (`fluxo-valido.md`) e com quatro (`plano-com-lastro.md`)
    produzem o mesmo conjunto de propriedades com estado (`F-17`)."""
    modelo = _load_modelo()

    linhas_tres = _FLUXO_VALIDO.read_text(encoding="utf-8").splitlines()
    linhas_quatro = _PLANO_COM_LASTRO.read_text(encoding="utf-8").splitlines()
    modelo_tres = modelo.extrair_modelo(linhas_tres, modelo._HEADING_VIGENTE)
    modelo_quatro = modelo.extrair_modelo(linhas_quatro, modelo._HEADING_VIGENTE)

    assert len(modelo_tres.estado) == 4
    assert len(modelo_quatro.estado) == 2
    assert ("resultado com lastro.status", "rascunho", "validado") in modelo_quatro.estado


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


def test_tf_check_objeto_sem_lastro_v21():
    """Objeto com `lastro` vazio dispara `V21`, com o plano em status não terminal."""
    modelo = _load_modelo()

    objeto = modelo.Objeto(
        nome="objeto sem lastro", contrato="c", origem="externo", propriedades=["estado"]
    )
    modelo_sintetico = modelo.Modelo(
        versao=1,
        data="2026-09-22",
        objetos=[objeto],
        estado=[("objeto sem lastro.estado", "i", "f")],
    )
    plano = _plano_stub([], status="in-progress")

    violacoes = modelo.validar(modelo_sintetico, plano)

    assert any(
        v.startswith("V21 objeto — objeto sem lastro declarado") for v in violacoes
    )


def test_tf_check_objeto_sem_lastro_nao_alcanca_status_terminal_v21():
    """A mesma ausência de lastro, com o plano em status terminal (`done`), não dispara `V21`
    (`DLS-12`)."""
    modelo = _load_modelo()

    objeto = modelo.Objeto(
        nome="objeto sem lastro", contrato="c", origem="externo", propriedades=["estado"]
    )
    modelo_sintetico = modelo.Modelo(
        versao=1,
        data="2026-09-22",
        objetos=[objeto],
        estado=[("objeto sem lastro.estado", "i", "f")],
    )
    plano = _plano_stub([], status="done")

    violacoes = modelo.validar(modelo_sintetico, plano)

    assert not any(v.startswith("V21") for v in violacoes)


def test_tf_check_pendente_roda_o_vocabulario(capsys):
    """`fluxo-pendente-contrato.md` tem, no bloco `## 1A`, a `OP-3` citando o objeto inexistente
    `objeto fantasma` — `check` passa a julgar a versão pendente pelo mesmo vocabulário da
    vigente (`OP-14`) e sai 1 com a violação prefixada `1A: ` (a regra de hoje, que não julga a
    pendente, sairia 0)."""
    modelo = _load_modelo()

    codigo = modelo.main(
        ["check", "--plano", str(_FLUXO_PENDENTE_CONTRATO), "--root", str(_ROOT)]
    )
    saida = capsys.readouterr()

    assert codigo == 1
    assert "1A: V5 OP-3 — objeto inexistente objeto fantasma" in saida.err


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


def test_tf_drift_mostra_contrato_alterado(capsys):
    """`fluxo-pendente-contrato.md` muda o contrato de `resultado um` entre vigente e pendente,
    sem mudar as propriedades — `--drift` acrescenta a linha de contrato (`OP-14`; a regra de
    hoje não imprime linha de objeto nenhuma para ele, porque as propriedades não mudaram)."""
    modelo = _load_modelo()

    codigo = modelo.main(
        ["show", "--plano", str(_FLUXO_PENDENTE_CONTRATO), "--drift", "--root", str(_ROOT)]
    )
    saida = capsys.readouterr()

    assert codigo == 0
    assert (
        "[~] resultado um — contrato: um registro validado => um registro validado e datado"
        in saida.out
    )


def test_tf_check_plano_inexistente_sai_2_sem_traceback(tmp_path, capsys):
    """TF da TK-74b: `check` com `--plano` que não é arquivo sai em uma linha com exit `2`."""
    codigo = _load_modelo().main(["check", "--plano", "TK-74", "--root", str(tmp_path)])

    assert codigo == 2
    assert "modelo: plano não encontrado 'TK-74'" in capsys.readouterr().out


def test_tf_show_plano_inexistente_sai_2_sem_traceback(tmp_path, capsys):
    """TF da TK-74b: `show` com `--plano` que não é arquivo sai em uma linha com exit `2`."""
    codigo = _load_modelo().main(["show", "--plano", "TK-74", "--root", str(tmp_path)])

    assert codigo == 2
    assert "modelo: plano não encontrado 'TK-74'" in capsys.readouterr().out


_MODELO_PENDENTE_TEXTO = """# P-0999 — Plano com versão pendente
**Prefixo das tarefas no diário:** `EX-T<n>`

## 1. Modelo conceitual

**Estado do modelo:** versão 1 · 2026-09-10 · autor: modelador · 1 operações · 2 propriedades · situação: vigente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem | lastro |
|---|---|---|---|---|---|
| insumo | dado de entrada | status | um registro por rodada | externo | lastro da fixture |
| produto | o produto da primeira operação | status | um registro validado | OP-1 | lastro da fixture |

### 1.2 Fluxo de operações

- **OP-1** — Primeira operação da fixture.
  - `precisa de: insumo` · `altera: produto.status` · `tarefas: EX-T1`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final |
|---|---|---|
| insumo.status | lido | lido |
| produto.status | rascunho | validado |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 1 | 2026-09-10 | vigente | modelador |
| 2 | 2026-09-21 | pendente | modelador, emenda |

## 1A. Modelo conceitual — versão pendente de validação

**Estado do modelo:** versão 2 · 2026-09-21 · autor: modelador · 2 operações · 3 propriedades · situação: pendente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem | lastro |
|---|---|---|---|---|---|
| insumo | dado de entrada | status | um registro por rodada | externo | lastro da fixture |
| produto | o produto da primeira operação | status | um registro validado | OP-1 | lastro da fixture |
| resultado | o produto da segunda operação | nível | um relatório derivado | OP-2 | lastro da fixture |

### 1.2 Fluxo de operações

- **OP-1** — Primeira operação da fixture.
  - `precisa de: insumo` · `altera: produto.status` · `tarefas: EX-T1`
- **OP-2** — Segunda operação, nova na versão pendente.
  - `precisa de: produto` · `altera: resultado.nível` · `tarefas: @TAREFAS_OP2@`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final |
|---|---|---|
| insumo.status | lido | lido |
| produto.status | rascunho | validado |
| resultado.nível | inicial | alto |

## 5. Tarefas

### EX-T1 — Um [Sonnet · classe mecanica]
- **Operação do modelo:** `OP-1`
  - OP-1: @TEXTO_OP1@
  - precisa de: insumo — um registro por rodada
"""

_CARD_OP2_TEXTO = """
### EX-T2 — Dois [Sonnet · classe mecanica]
- **Operação do modelo:** `@OP_CARD2@`
  - @OP_CARD2@: @TEXTO_OP2@
  - precisa de: produto — um registro validado
"""


def _raiz_modelo_pendente(
    tmp_path: Path,
    tarefas_op2: str = "",
    card_op2: bool = False,
    texto_op1: str = "Primeira operação da fixture.",
    texto_op2: str = "Segunda operação, nova na versão pendente.",
    op_card2: str = "OP-2",
) -> tuple[Path, Path]:
    """RAF-T19: raiz sintética com cópias de `backlog.py`/`caminhos.py` e um plano com versão
    pendente (`## 1A`), para exercitar `--so-vigente` sem depender de `## 1A` existir no plano
    real (a versão 2 do modelo foi promovida a vigente no Marco 3)."""
    raiz = tmp_path / "raiz"
    ferramentas = raiz / ".claude" / "tools"
    ferramentas.mkdir(parents=True)
    shutil.copy2(_ROOT / ".claude" / "tools" / "backlog.py", ferramentas / "backlog.py")
    shutil.copy2(_ROOT / ".claude" / "tools" / "caminhos.py", ferramentas / "caminhos.py")

    texto = _MODELO_PENDENTE_TEXTO.replace("@TAREFAS_OP2@", tarefas_op2).replace(
        "@TEXTO_OP1@", texto_op1
    )
    if card_op2:
        texto = texto + _CARD_OP2_TEXTO.replace("@OP_CARD2@", op_card2).replace(
            "@TEXTO_OP2@", texto_op2
        )

    plano = raiz / "docs" / "plans" / "P-0999-pendente.md"
    plano.parent.mkdir(parents=True)
    plano.write_text(texto, encoding="utf-8")
    return raiz, plano


def test_tf_so_vigente_ignora_a_versao_pendente(tmp_path, capsys):
    """TF (RAF-T19): `tarefas_op2` vazio (a `OP-2` da `## 1A` sem card) — `check --so-vigente`
    sai 0 com `modelo: OK — 1 operações` no stdout e sem `1A:` no stderr (hoje o argparse recusa
    a flag e sai 2)."""
    modelo = _load_modelo()
    raiz, plano = _raiz_modelo_pendente(tmp_path)

    codigo = modelo.main(["check", "--plano", str(plano), "--root", str(raiz), "--so-vigente"])
    saida = capsys.readouterr()

    assert codigo == 0
    assert "modelo: OK — 1 operações" in saida.out
    assert "1A:" not in saida.err


def test_tr_sem_so_vigente_julga_as_duas_versoes(tmp_path, capsys):
    """TR (RAF-T19): o mesmo plano, sem a flag, sai 1 com `1A: V1 OP-2 — operação sem tarefa` no
    stderr (a regra concorrente, julgar sempre só a vigente, sairia 0)."""
    modelo = _load_modelo()
    raiz, plano = _raiz_modelo_pendente(tmp_path)

    codigo = modelo.main(["check", "--plano", str(plano), "--root", str(raiz)])
    saida = capsys.readouterr()

    assert codigo == 1
    assert "1A: V1 OP-2 — operação sem tarefa" in saida.err


def test_tf_so_vigente_card_da_operacao_nova_nao_e_v4(tmp_path, capsys):
    """TF (RAF-T19): `tarefas_op2="EX-T2"` e o card `EX-T2` citando a `OP-2` — `check` sai 0 sem
    a flag e sai 0 com ela (hoje sai 1 com `V4 EX-T2 — operação inexistente OP-2`)."""
    modelo = _load_modelo()
    raiz, plano = _raiz_modelo_pendente(tmp_path, tarefas_op2="EX-T2", card_op2=True)

    codigo_sem_flag = modelo.main(["check", "--plano", str(plano), "--root", str(raiz)])
    capsys.readouterr()
    codigo_com_flag = modelo.main(
        ["check", "--plano", str(plano), "--root", str(raiz), "--so-vigente"]
    )
    capsys.readouterr()

    assert codigo_sem_flag == 0
    assert codigo_com_flag == 0


def test_tr_so_vigente_operacao_ausente_das_duas_segue_v4(tmp_path, capsys):
    """TR (RAF-T19): o card `EX-T2` cita `OP-9` — `check --so-vigente` sai 1 com
    `V4 EX-T2 — operação inexistente OP-9`."""
    modelo = _load_modelo()
    raiz, plano = _raiz_modelo_pendente(
        tmp_path, tarefas_op2="EX-T2", card_op2=True, op_card2="OP-9"
    )

    codigo = modelo.main(["check", "--plano", str(plano), "--root", str(raiz), "--so-vigente"])
    saida = capsys.readouterr()

    assert codigo == 1
    assert "V4 EX-T2 — operação inexistente OP-9" in saida.err


def _raiz_pendente_fora_de_sequencia(tmp_path: Path) -> tuple[Path, Path]:
    """RAF-T19a: a raiz de `_raiz_modelo_pendente` com o card da `OP-2` e a `## 1A` em versão 3
    contra a vigente 1, para que só a `V20` distinga o `check` com e sem `--so-vigente`."""
    raiz, plano = _raiz_modelo_pendente(tmp_path, tarefas_op2="EX-T2", card_op2=True)
    texto = plano.read_text(encoding="utf-8")
    plano.write_text(
        texto.replace("**Estado do modelo:** versão 2 ·", "**Estado do modelo:** versão 3 ·"),
        encoding="utf-8",
    )
    return raiz, plano


def test_tf_so_vigente_pendente_fora_de_sequencia_nao_e_v20(tmp_path, capsys):
    """TF (RAF-T19a): pendente em versão 3 contra a vigente 1 — `check --so-vigente` sai 0 sem
    `V20` no stderr (sem a guarda `not so_vigente` sairia 1 com a `V20`)."""
    modelo = _load_modelo()
    raiz, plano = _raiz_pendente_fora_de_sequencia(tmp_path)

    codigo = modelo.main(["check", "--plano", str(plano), "--root", str(raiz), "--so-vigente"])
    saida = capsys.readouterr()

    assert codigo == 0
    assert "V20" not in saida.err


def test_tr_sem_so_vigente_pendente_fora_de_sequencia_segue_v20(tmp_path, capsys):
    """TR (RAF-T19a): o mesmo plano, sem a flag, sai 1 com
    `V20 secao — versão pendente fora de sequência` no stderr."""
    modelo = _load_modelo()
    raiz, plano = _raiz_pendente_fora_de_sequencia(tmp_path)

    codigo = modelo.main(["check", "--plano", str(plano), "--root", str(raiz)])
    saida = capsys.readouterr()

    assert codigo == 1
    assert "V20 secao — versão pendente fora de sequência" in saida.err


def test_tf_texto_divergente_v22_da_vigente(tmp_path, capsys):
    """TF (RAF-T21): `tarefas_op2="EX-T2"`, `card_op2=True` e o `EX-T1` com o texto `Primeira
    operação da fixture, na redação antiga.` — `check` sai 1 com `V22 EX-T1 — texto de OP-1
    diverge da versão 1` no stderr (hoje sai 0)."""
    modelo = _load_modelo()
    raiz, plano = _raiz_modelo_pendente(
        tmp_path,
        tarefas_op2="EX-T2",
        card_op2=True,
        texto_op1="Primeira operação da fixture, na redação antiga.",
    )

    codigo = modelo.main(["check", "--plano", str(plano), "--root", str(raiz)])
    saida = capsys.readouterr()

    assert codigo == 1
    assert "V22 EX-T1 — texto de OP-1 diverge da versão 1" in saida.err


def test_tr_texto_divergente_so_em_espacos_nao_e_v22(tmp_path, capsys):
    """TR (RAF-T21): o `EX-T1` com `Primeira  operação da fixture. ` (espaço duplo e espaço na
    ponta) — `check` sai 0 (a regra concorrente, comparação literal, acusaria `V22`)."""
    modelo = _load_modelo()
    raiz, plano = _raiz_modelo_pendente(
        tmp_path,
        tarefas_op2="EX-T2",
        card_op2=True,
        texto_op1="Primeira  operação da fixture. ",
    )

    codigo = modelo.main(["check", "--plano", str(plano), "--root", str(raiz)])
    saida = capsys.readouterr()

    assert codigo == 0
    assert "V22" not in saida.err


def test_tf_texto_divergente_v22_da_pendente(tmp_path, capsys):
    """TF (RAF-T21): o `EX-T2` com o texto `Outra redação da segunda operação.` — `check
    --so-vigente` sai 1 com `V22 EX-T2 — texto de OP-2 diverge da versão 2` (hoje sai 0)."""
    modelo = _load_modelo()
    raiz, plano = _raiz_modelo_pendente(
        tmp_path,
        tarefas_op2="EX-T2",
        card_op2=True,
        texto_op2="Outra redação da segunda operação.",
    )

    codigo = modelo.main(
        ["check", "--plano", str(plano), "--root", str(raiz), "--so-vigente"]
    )
    saida = capsys.readouterr()

    assert codigo == 1
    assert "V22 EX-T2 — texto de OP-2 diverge da versão 2" in saida.err


def _modelo_drift(modelo, textos: list[str], estado: list[tuple[str, str, str]], versao: int):
    """Monta um `Modelo` sintético para os testes de drift entre versões (RAF-T22): operações
    `OP-1`..`OP-n` na ordem de `textos`, sem `precisa_de`/`altera`/`tarefas`."""
    operacoes = [
        modelo.Operacao(numero=numero, texto=texto)
        for numero, texto in enumerate(textos, start=1)
    ]
    return modelo.Modelo(versao=versao, data="2026-09-28", operacoes=operacoes, estado=estado)


def test_tf_drift_versoes_insercao_mostra_nova_e_renumerada():
    """TF (RAF-T22, R-07/DRF-16): a pendente insere `Nova.` entre `Primeira.` e `Segunda.` — o
    casamento por texto primeiro reconhece `Segunda.` como a mesma operação renumerada (`[=] OP-3
    (era OP-2)`) e só `Nova.` sai como inserção (`[+] OP-2`); hoje, casando só por número, sairiam
    `[+] OP-3 — Segunda.` e `[~] OP-2 — Segunda. => Nova.`."""
    modelo = _load_modelo()
    vigente = _modelo_drift(modelo, ["Primeira.", "Segunda."], [], 1)
    pendente = _modelo_drift(modelo, ["Primeira.", "Nova.", "Segunda."], [], 2)

    resultado = modelo.montar_drift(vigente, pendente)
    linhas = resultado.splitlines()

    assert "[+] OP-2 — Nova." in linhas
    assert "[=] OP-3 (era OP-2)" in linhas
    assert not any(linha.startswith("[~] OP-") or linha.startswith("[-] OP-") for linha in linhas)


def test_tr_drift_versoes_texto_alterado_segue_por_numero():
    """TR (RAF-T22): sem par de texto igual, `OP-1` casa por número entre as duas versões e sai
    como alteração (`[~]`) — a regra concorrente, casar só por texto, daria `[+] OP-1` (pendente)
    e `[-] OP-1` (vigente) por não achar par nenhum."""
    modelo = _load_modelo()
    vigente = _modelo_drift(modelo, ["Primeira."], [], 1)
    pendente = _modelo_drift(modelo, ["Primeira, reescrita."], [], 2)

    resultado = modelo.montar_drift(vigente, pendente)
    linhas = resultado.splitlines()

    assert "[~] OP-1 — Primeira. => Primeira, reescrita." in linhas
    assert not any(linha.startswith("[+] OP-") or linha.startswith("[-] OP-") for linha in linhas)


def test_tf_drift_versoes_propriedade_de_uma_versao_so():
    """TF (RAF-T22, DRF-16): `x.c` só existe na vigente e `x.b` só existe na pendente — `_diff_estado`
    hoje só mostra chave presente nas duas versões, então nenhuma das duas linhas aparecia."""
    modelo = _load_modelo()
    vigente = _modelo_drift(
        modelo, ["Única."], [("x.a", "-", "fim"), ("x.c", "-", "baixo")], 1
    )
    pendente = _modelo_drift(
        modelo, ["Única."], [("x.a", "-", "fim"), ("x.b", "-", "alto")], 2
    )

    resultado = modelo.montar_drift(vigente, pendente)
    linhas = resultado.splitlines()

    assert "[+] x.b — alto" in linhas
    assert "[-] x.c — baixo" in linhas


def test_tf_drift_contrato_da_operacao_mostra_precisa_e_altera():
    """TF (RAF-T22a, AE-187/DRF-73): `OP-1` tem o mesmo texto e o mesmo número nas duas versões e
    muda só `precisa de:` e `altera:` — o drift mostra as duas listas; hoje o par de texto igual não
    emite linha nenhuma e `montar_drift` devolve `sem drift`."""
    modelo = _load_modelo()
    vigente = modelo.Modelo(versao=1, data="2026-09-28", operacoes=[
        modelo.Operacao(numero=1, texto="Única.", precisa_de=["a"], altera=["x.a"]),
    ])
    pendente = modelo.Modelo(versao=2, data="2026-09-28", operacoes=[
        modelo.Operacao(numero=1, texto="Única.", precisa_de=["a", "b"], altera=["x.a", "x.b"]),
    ])

    linhas = modelo.montar_drift(vigente, pendente).splitlines()

    assert "[~] OP-1 — precisa de: a => a, b" in linhas
    assert "[~] OP-1 — altera: x.a => x.a, x.b" in linhas


def test_tr_drift_contrato_da_operacao_ignora_tarefas():
    """TR (RAF-T22a, DRF-73): `OP-1` muda só `tarefas:`, que é lastro e não modelo — o drift segue
    `sem drift`; a regra concorrente, comparar todo o sub-bullet, daria uma linha de `tarefas:`."""
    modelo = _load_modelo()
    vigente = modelo.Modelo(versao=1, data="2026-09-28", operacoes=[
        modelo.Operacao(numero=1, texto="Única.", tarefas=["EX-T1"]),
    ])
    pendente = modelo.Modelo(versao=2, data="2026-09-28", operacoes=[
        modelo.Operacao(numero=1, texto="Única.", tarefas=["EX-T1", "EX-T1a"]),
    ])

    assert modelo.montar_drift(vigente, pendente) == "sem drift"
