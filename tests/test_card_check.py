"""LM-T5b (`docs/plans/P-0740-loop-de-modulos.md` `### LM-T5b`) — TF/TR de
`.claude/tools/card_check.py`: a régua de autoria roda o comando publicado no bloco `Verificação`
de um card e compara com o `Medido antes` declarado, contra os três cards sintéticos de
`tests/fixtures/card_check/plano-exemplo.md` (`EX-T1`/`EX-T2`/`EX-T3`, nenhum card vivo de plano —
`DM-38` (ii)). Padrão de carga do módulo idêntico a `tests/test_review_evidence.py` (`.claude/`
não é pacote importável)."""
from __future__ import annotations

import importlib.util
import json
import shutil
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_CARD_CHECK_PATH = _ROOT / ".claude" / "tools" / "card_check.py"
_PLANO_FIXTURE = _ROOT / "tests" / "fixtures" / "card_check" / "plano-exemplo.md"
_PLANO_CORPUS = _ROOT / "tests" / "fixtures" / "card_check" / "plano-corpus.md"
_PLANO_ANCORAS = _ROOT / "tests" / "fixtures" / "card_check" / "plano-ancoras.md"
_PLANO_PASTA = _ROOT / "tests" / "fixtures" / "card_check" / "P-0-pasta" / "plano.md"


def _load_card_check():
    spec = importlib.util.spec_from_file_location("card_check", _CARD_CHECK_PATH)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def test_tr_card_integro_sai_zero(capsys):
    """`EX-T1` tem os três elementos em seu único item, e o `Medido antes` declarado (`2`) bate
    com a saída real de `python -c "print(2)"` na árvore de teste — `card_check` sai 0."""
    card_check = _load_card_check()

    codigo = card_check.main(["--plano", str(_PLANO_FIXTURE), "--tarefa", "EX-T1", "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 0
    assert "card_check: OK" in saida.out


def test_tf_item_sem_medido_antes_falha(capsys):
    """`EX-T2` tem comando e `→`, mas nenhum `**Medido antes:**` — `card_check` sai 1 e nomeia o
    elemento `Medido antes` como ausente (sem (b): instrumento aprovaria item sem baseline)."""
    card_check = _load_card_check()

    codigo = card_check.main(["--plano", str(_PLANO_FIXTURE), "--tarefa", "EX-T2", "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 1
    assert "card_check: FALHOU" in saida.err
    assert "Medido antes" in saida.err


def test_tf_divergencia_de_valor_falha(capsys):
    """`EX-T3` declara `**Medido antes: 3**`, mas a saída real de `python -c "print(2)"` é `2` —
    `card_check` sai 1 e nomeia a divergência (sem (c): instrumento aprovaria baseline envelhecida)."""
    card_check = _load_card_check()

    codigo = card_check.main(["--plano", str(_PLANO_FIXTURE), "--tarefa", "EX-T3", "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 1
    assert "card_check: FALHOU" in saida.err
    assert "divergencia" in saida.err


def test_tf_item_numerado_fora_da_forma_e_nomeado(capsys):
    """`LM-T5c` matéria 1/2: `EX-T4` tem prosa entre `1.` e o bloco cercado — fora da forma da
    `### 8.1` (o bloco tem de vir logo após `N.`). O item não pode desaparecer em silêncio: o
    instrumento nomeia `item 1: fora da forma da 8.1` e sai 1 (sem (b): o item some sem uma linha
    sequer, que foi o falso verde reproduzido pelo reviewer da `LM-T5b`)."""
    card_check = _load_card_check()

    codigo = card_check.main(["--plano", str(_PLANO_FIXTURE), "--tarefa", "EX-T4", "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 1
    assert "card_check: FALHOU" in saida.err
    assert "item 1: fora da forma da 8.1" in saida.err


def test_tf_token_de_shell_isolado_e_recusado():
    """`LM-T5c` matéria 3/contrato de segurança (matéria 4): um token isolado que é operador de
    shell (`;`) ainda é recusado depois de `shlex.split` — o contrato de segurança continua de
    pé mesmo com a decisão passando a ser por token."""
    card_check = _load_card_check()

    motivo = card_check._validar_comando(
        'python -c "print(2)" ; python -c "print(3)"'
    )

    assert motivo is not None
    assert "token de shell isolado" in motivo
    assert "';'" in motivo


def test_tr_pipe_dentro_de_argumento_citado_executa():
    """`LM-T5c` matéria 3: `|` dentro de um argumento citado não é operador de shell — a execução
    é sem `shell=True`, então o token citado inteiro nunca é interpretado por um shell.
    `_validar_comando` não recusa, e `_rodar_comando` de fato executa o comando."""
    card_check = _load_card_check()
    comando = 'python -c "print(\'a|b\')"'

    assert card_check._validar_comando(comando) is None

    returncode, saida = card_check._rodar_comando(comando, _ROOT)

    assert returncode == 0
    assert "a|b" in saida


def test_tf_afericao_manual_sobre_comando_executavel_e_rejeitada(capsys):
    """`LM-T5c` matéria 4: `EX-T6` declara `**Aferição: manual**` sobre um item cujo comando
    (`python -c "print(2)"`) é executável — o marcador só vale sobre comando recusado ou ausente;
    sobre comando executável ele é uma porta dos fundos, e o instrumento rejeita com falha
    nomeada."""
    card_check = _load_card_check()

    codigo = card_check.main(["--plano", str(_PLANO_FIXTURE), "--tarefa", "EX-T6", "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 1
    assert "card_check: FALHOU" in saida.err
    assert "Aferição: manual" in saida.err
    assert "comando é executável" in saida.err


def test_tf_saida_acentuada_do_subprocesso_e_comparavel():
    """`LM-T5c` matéria 5: sem `encoding=\"utf-8\"`, o Windows decide pela `cp1252` e a saída
    acentuada do subprocesso chega corrompida, de modo que nenhum `Medido antes` com acento pode
    bater. `_rodar_comando` decodifica a saída como UTF-8 (`errors=\"replace\"`), e o literal
    acentuado volta a ser comparável."""
    card_check = _load_card_check()
    comando = (
        "python -c \"import sys; sys.stdout.reconfigure(encoding='utf-8'); "
        "print('café')\""
    )

    returncode, saida = card_check._rodar_comando(comando, _ROOT)

    assert returncode == 0
    assert "café" in saida


# --- FPU-T1 (DFP-3/DFP-14): forma inline sobre o corpus, marcador só no início de linha --------


def test_tf_corpus_ready_compara_antes(capsys):
    """`CX-T1` é `ready` (mundo `antes`, derivado do bullet `- **Status:**`): o comando imprime o
    valor declarado como `antes` (`a`) — `card_check` sai 0."""
    card_check = _load_card_check()

    codigo = card_check.main(["--plano", str(_PLANO_CORPUS), "--tarefa", "CX-T1", "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 0
    assert "card_check: OK" in saida.out


def test_tf_corpus_done_compara_depois(capsys):
    """`CX-T2` é `done` (mundo `depois`): o comando imprime o valor declarado como `depois` (`b`)
    — `card_check` sai 0. Forçado a comparar `antes` via `--mundo antes`, o mesmo comando diverge
    do valor `antes` (`a`) — sai 1, nomeando a divergência."""
    card_check = _load_card_check()

    codigo = card_check.main(["--plano", str(_PLANO_CORPUS), "--tarefa", "CX-T2", "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 0
    assert "card_check: OK" in saida.out

    codigo_antes = card_check.main(
        ["--plano", str(_PLANO_CORPUS), "--tarefa", "CX-T2", "--root", str(_ROOT), "--mundo", "antes"]
    )
    saida_antes = capsys.readouterr()

    assert codigo_antes == 1
    assert "card_check: FALHOU" in saida_antes.err
    assert "divergencia" in saida_antes.err


def test_tf_corpus_sem_antes_falha(capsys):
    """`CX-T3` é `ready` (mundo `antes`) e seu item não declara o par `antes`/`depois` — sem valor
    `antes` para comparar, `card_check` sai 1 nomeando o elemento ausente."""
    card_check = _load_card_check()

    codigo = card_check.main(["--plano", str(_PLANO_CORPUS), "--tarefa", "CX-T3", "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 1
    assert "card_check: FALHOU" in saida.err
    assert "sem valor antes" in saida.err


def test_tf_marcador_so_no_inicio_de_linha(capsys):
    """`CX-T4` tem a prosa `acionamento 1. medido` no campo `Contingências`, fora do início de
    linha — não pode virar item fantasma na `Verificação`, que tem um item só (`DFP-3`):
    `card_check` reconhece exatamente um item e sai 0."""
    card_check = _load_card_check()

    codigo = card_check.main(["--plano", str(_PLANO_CORPUS), "--tarefa", "CX-T4", "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 0
    assert "card_check: OK" in saida.out


def test_tf_prosa_na_continuacao_do_item_nao_vira_item():
    """`CX-T5` tem a prosa `acionamento 1. e conferido na revisão 2.` na linha de continuação do
    item 1 da `Verificação`, fora do início de linha — não pode virar item fantasma (`DFP-3`):
    `card_check.verificar_tarefa` reconhece exatamente dois itens e fecha."""
    card_check = _load_card_check()

    ok, falhas, medida = card_check.verificar_tarefa(_PLANO_CORPUS, "CX-T5", _ROOT)

    assert ok is True
    assert falhas == []
    assert len(medida["itens"]) == 2


# --- FPU-T3 (DFP-4/DFP-16): toda âncora `<caminho>:<linha>` leva o literal, e o gate confere ----
# a linha hoje.


def test_tf_ancora_com_literal_fecha(capsys):
    """`AN-T1` tem duas âncoras com literal em `Arquivos-alvo` (`alvo.txt:2` → `dois`,
    `alvo.txt:3` → `tres \\`x\\``) e a repetição de uma delas, sem literal, num Passo — a repetição
    passa porque o mesmo texto de âncora já tem literal em outra ocorrência do card. `card_check`
    sai 0."""
    card_check = _load_card_check()

    codigo = card_check.main(["--plano", str(_PLANO_ANCORAS), "--tarefa", "AN-T1", "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 0
    assert "card_check: OK" in saida.out


def test_tf_ancora_sem_literal_falha(capsys):
    """`AN-T2` cita `alvo.txt:2` só no Passo, sem literal em nenhuma ocorrência do card —
    `card_check` sai 1, nomeando `âncora sem literal`."""
    card_check = _load_card_check()

    codigo = card_check.main(["--plano", str(_PLANO_ANCORAS), "--tarefa", "AN-T2", "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 1
    assert "card_check: FALHOU" in saida.err
    assert "âncora sem literal" in saida.err


def test_tf_literal_fora_da_linha_falha(capsys):
    """`AN-T3` declara o literal `tres` para `alvo.txt:2`, mas a linha 2 é `dois` — `card_check`
    sai 1, nomeando `literal fora da linha`."""
    card_check = _load_card_check()

    codigo = card_check.main(["--plano", str(_PLANO_ANCORAS), "--tarefa", "AN-T3", "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 1
    assert "card_check: FALHOU" in saida.err
    assert "literal fora da linha" in saida.err


def test_tr_card_sem_ancora_nao_muda(capsys):
    """`AN-T4` não tem nenhuma âncora de arquivo:linha em `Arquivos-alvo` nem em `Passos` — a
    conferência de âncoras não acusa nada, e `card_check` sai 0 como antes da `FPU-T3`."""
    card_check = _load_card_check()

    codigo = card_check.main(["--plano", str(_PLANO_ANCORAS), "--tarefa", "AN-T4", "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 0
    assert "card_check: OK" in saida.out


# --- FPU-T5 (DFP-17): o executor devolve a medida como arquivo, e a evidência a incorpora -------


def test_tf_gravar_escreve_um_registro_por_item(tmp_path, capsys):
    """`--gravar <caminho.json>` grava a medida de `verificar_tarefa` (DFP-17): `CX-T1` fecha
    comparando `antes` (Status `ready`) com um item só, cujo comando bate — o JSON gravado tem
    `mundo == "antes"`, `tarefa == "CX-T1"` e um item com `exit == 0` e `bate is True`."""
    card_check = _load_card_check()
    destino = tmp_path / "medida.json"

    codigo = card_check.main(
        [
            "--plano",
            str(_PLANO_CORPUS),
            "--tarefa",
            "CX-T1",
            "--root",
            str(_ROOT),
            "--gravar",
            str(destino),
        ]
    )
    capsys.readouterr()

    assert codigo == 0
    dados = json.loads(destino.read_text(encoding="utf-8"))
    assert dados["mundo"] == "antes"
    assert dados["tarefa"] == "CX-T1"
    assert len(dados["itens"]) == 1
    assert dados["itens"][0]["exit"] == 0
    assert dados["itens"][0]["bate"] is True


def test_tf_gravar_guarda_a_cauda_da_saida(tmp_path, capsys):
    """`registro["saida"]` guarda a cauda da saída (`AE-37`), não a cabeça: o comando imprime
    500 caracteres de `x` seguidos de `FIM` — a `saida` gravada no JSON tem 400 caracteres e
    termina em `FIM`."""
    card_check = _load_card_check()
    plano = tmp_path / "plano.md"
    plano.write_text(
        "### T1 — Card inline cuja saída excede o teto [Sonnet · classe mecanica]\n"
        "- **Status:** `ready`\n"
        "- **Objetivo:** fixture de `card_check` cujo comando imprime mais de 400 caracteres,\n"
        "  terminados em `FIM`.\n"
        "- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.\n"
        "- **Verificação:**\n"
        "  1. `python -c \"print('x'*500+'FIM')\"` → `FIM` — antes `FIM`, depois `FIM`\n"
        "- **Pronto quando:** fixture existe e `card_check.py --tarefa T1` sai 0.\n",
        encoding="utf-8",
    )
    destino = tmp_path / "medida.json"

    codigo = card_check.main(
        [
            "--plano",
            str(plano),
            "--tarefa",
            "T1",
            "--root",
            str(_ROOT),
            "--gravar",
            str(destino),
        ]
    )
    capsys.readouterr()

    assert codigo == 0
    dados = json.loads(destino.read_text(encoding="utf-8"))
    saida = dados["itens"][0]["saida"]
    assert saida.endswith("FIM")
    assert len(saida) == 400


def test_tf_gravar_sem_caminho_grava_no_destino_derivado(tmp_path, capsys):
    """`TK-92a` — `--gravar` sem caminho grava em `caminhos.destino_medida(--root, --plano,
    --tarefa)`: com `plano-corpus.md` copiado como `docs/DIARIO_DE_OBRAS.md` numa raiz
    temporária (que carrega uma cópia de `rdo.py`/`caminhos.py`, como `verificar_tarefa`
    exige de qualquer `--root`), o destino é
    `docs/RDO/evidencia/DIARIO_DE_OBRAS-CX-T1-medida-antes.json`, dentro da própria raiz
    temporária — nada é gravado no repositório. Desde a `RAF-T15` (`R-05`) o nome leva o mundo
    efetivo da medida; `CX-T1` da fixture compara o mundo `antes`."""
    card_check = _load_card_check()
    ferramentas = tmp_path / ".claude" / "tools"
    ferramentas.mkdir(parents=True)
    shutil.copy2(_ROOT / ".claude" / "tools" / "rdo.py", ferramentas / "rdo.py")
    shutil.copy2(_ROOT / ".claude" / "tools" / "caminhos.py", ferramentas / "caminhos.py")
    plano = tmp_path / "docs" / "DIARIO_DE_OBRAS.md"
    plano.parent.mkdir(parents=True)
    plano.write_text(_PLANO_CORPUS.read_text(encoding="utf-8"), encoding="utf-8")

    codigo = card_check.main(
        ["--plano", str(plano), "--tarefa", "CX-T1", "--root", str(tmp_path), "--gravar"]
    )
    capsys.readouterr()

    assert codigo == 0
    destino = tmp_path / "docs" / "RDO" / "evidencia" / "DIARIO_DE_OBRAS-CX-T1-medida-antes.json"
    dados = json.loads(destino.read_text(encoding="utf-8"))
    assert dados["tarefa"] == "CX-T1"


# --- AF-T7 (DAF-18/DAF-39): status de plano em pasta lido de `estado.tsv`, não do card ----------


def test_tf_estado_tsv_done_compara_depois(capsys):
    """`CP-T1` (`tests/fixtures/card_check/P-0-pasta/`) não declara `- **Status:**` no card — o
    status `done` mora só na linha `CP-T1` de `estado.tsv`. `verificar_tarefa` passa a pasta do
    plano a `rdo._status_atual`, que lê essa linha: mundo `depois`, e o comando declarado
    (`python -c "print('b')"`) imprime `b`, batendo com o valor `depois` — `card_check` sai 0."""
    card_check = _load_card_check()

    codigo = card_check.main(["--plano", str(_PLANO_PASTA), "--tarefa", "CP-T1", "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 0
    assert "card_check: OK" in saida.out


def test_tr_estado_tsv_ready_compara_antes(capsys):
    """`CP-T2` está `ready` só em `estado.tsv` — mundo `antes`, e o comando declarado
    (`python -c "print('a')"`) imprime `a`, batendo com o valor `antes` — `card_check` sai 0."""
    card_check = _load_card_check()

    codigo = card_check.main(["--plano", str(_PLANO_PASTA), "--tarefa", "CP-T2", "--root", str(_ROOT)])
    saida = capsys.readouterr()

    assert codigo == 0
    assert "card_check: OK" in saida.out


# --- RAF-T13 (DRF-13 (i) e (ii)): mundo `depois` na forma 8.1 e literal com pontuação -----------


def _plano_com_item(tmp_path: Path, item: str) -> Path:
    plano = tmp_path / "plano.md"
    plano.write_text(
        "### RX-T1 — Card sintético do RAF-T13 [Sonnet · classe mecanica]\n"
        "- **Objetivo:** fixture de `card_check` para os testes de mundo `depois` na forma 8.1 e "
        "do par com pontuação no literal da forma inline.\n"
        "- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.\n"
        "- **Verificação:**\n"
        f"{item}"
        "- **Pronto quando:** fixture existe e `card_check.py --tarefa RX-T1` sai conforme o "
        "teste.\n",
        encoding="utf-8",
    )
    return plano


def _bloco(valor_impresso: str, esperado: str, medido_antes: str) -> str:
    return (
        "  1. ```\n"
        f"     python -c \"print('{valor_impresso}')\"\n"
        "     ```\n"
        f"     → {esperado}. **Medido antes: {medido_antes}**\n"
    )


def _rodar(card_check, plano: Path, mundo: str) -> int:
    return card_check.main(
        ["--plano", str(plano), "--tarefa", "RX-T1", "--root", str(_ROOT), "--mundo", mundo]
    )


def test_tf_bloco_cercado_mundo_depois_compara_com_o_esperado(tmp_path, capsys):
    """Bloco cercado que imprime `a`, esperado `imprime **b**`, `Medido antes: a`: `--mundo
    depois` compara com o literal do esperado (`b`), não com `Medido antes` — diverge e sai 1
    (hoje sai 0, comparando `a`). O mesmo bloco imprimindo `b` bate com o esperado e sai 0."""
    card_check = _load_card_check()

    plano = _plano_com_item(tmp_path, _bloco("a", "imprime **b**", "a"))
    codigo = _rodar(card_check, plano, "depois")
    saida = capsys.readouterr()
    assert codigo == 1
    assert "card_check: FALHOU" in saida.err
    assert "divergencia - esperado (depois) declara 'b'" in saida.err

    plano = _plano_com_item(tmp_path, _bloco("b", "imprime **b**", "a"))
    codigo = _rodar(card_check, plano, "depois")
    saida = capsys.readouterr()
    assert codigo == 0
    assert "card_check: OK" in saida.out


def test_tr_bloco_cercado_mundo_antes_segue_com_o_medido(tmp_path, capsys):
    """O mesmo bloco cercado de cima, comparado com `--mundo antes`, segue comparando com
    `Medido antes` (comportamento de hoje, intocado pela regra nova)."""
    card_check = _load_card_check()

    plano = _plano_com_item(tmp_path, _bloco("a", "imprime **b**", "a"))
    codigo = _rodar(card_check, plano, "antes")
    saida = capsys.readouterr()
    assert codigo == 0
    assert "card_check: OK" in saida.out

    plano = _plano_com_item(tmp_path, _bloco("b", "imprime **b**", "a"))
    codigo = _rodar(card_check, plano, "antes")
    saida = capsys.readouterr()
    assert codigo == 1
    assert "card_check: FALHOU" in saida.err
    assert "divergencia - Medido antes declara 'a'" in saida.err


def test_tf_bloco_cercado_mundo_depois_sem_literal_falha(tmp_path, capsys):
    """Esperado `imprime o valor`, sem negrito nem crase: `--mundo depois` não tem literal para
    comparar — o item não roda e `card_check` nomeia `esperado sem literal`."""
    card_check = _load_card_check()

    plano = _plano_com_item(tmp_path, _bloco("a", "imprime o valor", "a"))
    codigo = _rodar(card_check, plano, "depois")
    saida = capsys.readouterr()

    assert codigo == 1
    assert "card_check: FALHOU" in saida.err
    assert "item 1: esperado sem literal" in saida.err


def test_tf_par_com_crase_depois_aceita_ponto(tmp_path, capsys):
    """O par `antes`/`depois` com o literal inteiro entre crases aceita ponto dentro do valor
    (hoje a regex sem crase corta o literal em `a` e sai 0 com `--mundo depois`)."""
    card_check = _load_card_check()
    item = (
        "  1. `python -c \"print('a.txt: 2')\"` → `a.txt: 3` — antes `a.txt: 2`, "
        "depois `a.txt: 3`\n"
    )
    plano = _plano_com_item(tmp_path, item)

    codigo = _rodar(card_check, plano, "antes")
    saida = capsys.readouterr()
    assert codigo == 0
    assert "card_check: OK" in saida.out

    codigo = _rodar(card_check, plano, "depois")
    saida = capsys.readouterr()
    assert codigo == 1
    assert "card_check: FALHOU" in saida.err
    assert "declara 'a.txt: 3'" in saida.err


def test_tf_par_com_crase_antes_aceita_virgula(tmp_path, capsys):
    """O par `antes`/`depois` com o literal inteiro entre crases aceita vírgula dentro do valor
    `antes` (hoje a regex sem crase não fecha o par e sai 1 com `sem valor antes`)."""
    card_check = _load_card_check()
    item = "  1. `python -c \"print('x; z')\"` → `esperado` — antes `x, y`, depois `q`\n"
    plano = _plano_com_item(tmp_path, item)

    codigo = _rodar(card_check, plano, "antes")
    saida = capsys.readouterr()
    assert codigo == 1
    assert "card_check: FALHOU" in saida.err
    assert "divergencia - valor do mundo (antes) declara 'x, y'" in saida.err

    item2 = "  1. `python -c \"print('x, y')\"` → `esperado` — antes `x, y`, depois `q`\n"
    plano2 = _plano_com_item(tmp_path, item2)
    codigo2 = _rodar(card_check, plano2, "antes")
    saida2 = capsys.readouterr()
    assert codigo2 == 0
    assert "card_check: OK" in saida2.out


def test_tf_par_com_crase_so_depois_da_seta(tmp_path, capsys):
    """O par `antes`/`depois` só é procurado no trecho que começa na primeira `→` depois do
    comando: uma nota antes da seta com um par de crase próprio não pode ser lida no lugar do
    par real (hoje lê o par da nota e sai 1)."""
    card_check = _load_card_check()
    item = (
        "  1. `python -c \"print('a')\"` (nota: antes `z`, depois `z`) → `a` — antes `a`, "
        "depois `a`\n"
    )
    plano = _plano_com_item(tmp_path, item)

    codigo = _rodar(card_check, plano, "antes")
    saida = capsys.readouterr()
    assert codigo == 0
    assert "card_check: OK" in saida.out


def test_tr_par_com_crase_legado_sem_crase_segue_lido(tmp_path, capsys):
    """Par `antes`/`depois` sem crase (forma legado da `DFP-14`) segue lido pela `_ANTES_DEPOIS_RE`
    de sempre, intocada por esta tarefa."""
    card_check = _load_card_check()
    item = "  1. `python -c \"print(2)\"` → 3 — antes 2, depois 3\n"
    plano = _plano_com_item(tmp_path, item)

    codigo = _rodar(card_check, plano, "antes")
    saida = capsys.readouterr()
    assert codigo == 0
    assert "card_check: OK" in saida.out

    codigo = _rodar(card_check, plano, "depois")
    saida = capsys.readouterr()
    assert codigo == 1
    assert "card_check: FALHOU" in saida.err


# --- RAF-T14 (DRF-13 (iii) e (iv), DRF-36): git de leitura, <ref> do despacho, invariância ------


def _raiz_com_despacho(tmp_path: Path, tarefa: str, ref: str) -> Path:
    ferramentas = tmp_path / ".claude" / "tools"
    ferramentas.mkdir(parents=True)
    shutil.copy2(_ROOT / ".claude" / "tools" / "rdo.py", ferramentas / "rdo.py")
    shutil.copy2(_ROOT / ".claude" / "tools" / "caminhos.py", ferramentas / "caminhos.py")
    estado = tmp_path / ".claude" / "estado"
    estado.mkdir(parents=True)
    (estado / "tarefa-corrente.json").write_text(
        json.dumps({"tarefa": tarefa, "ref": ref}), encoding="utf-8"
    )
    return tmp_path


def test_tf_git_leitura_roda_ls_files(tmp_path, capsys):
    """`_COMANDOS_PERMITIDOS` ganha `git`, restrito aos subcomandos de leitura de `_GIT_LEITURA`:
    `git ls-files tests/test_card_check.py` é um deles — `--mundo antes` sai 0 (hoje sai 1,
    `primeiro token fora da lista fechada`, porque `git` não estava na lista)."""
    card_check = _load_card_check()
    item = (
        "  1. `git ls-files tests/test_card_check.py` → `tests/test_card_check.py` — "
        "antes `tests/test_card_check.py`, depois `tests/test_card_check.py`\n"
    )
    plano = _plano_com_item(tmp_path, item)

    codigo = _rodar(card_check, plano, "antes")
    saida = capsys.readouterr()

    assert codigo == 0
    assert "card_check: OK" in saida.out


def test_tf_git_leitura_recusa_subcomando_de_escrita(tmp_path, capsys):
    """`git commit` não está em `_GIT_LEITURA` — recusado com a razão nomeando o segundo token, e
    o comando nunca roda (hoje a razão é `primeiro token fora da lista fechada`, sem nomear o
    subcomando, porque `git` não estava na lista fechada)."""
    card_check = _load_card_check()
    item = "  1. `git commit -m x` → `x` — antes `x`, depois `x`\n"
    plano = _plano_com_item(tmp_path, item)

    codigo = _rodar(card_check, plano, "antes")
    saida = capsys.readouterr()

    assert codigo == 1
    assert "card_check: FALHOU" in saida.err
    assert "subcomando git 'commit' fora da lista de leitura" in saida.err


def test_tf_ref_do_despacho_entra_no_comando(tmp_path, capsys):
    """`<ref>` no comando é trocado pelo valor que o `despachar` gravou em
    `.claude/estado/tarefa-corrente.json` para a mesma tarefa: raiz com `ref` `abc123` para
    `RX-T1`, comando que imprime `<ref>` — `--mundo depois` compara com `abc123` e sai 0 (hoje
    imprime o literal `<ref>` e sai 1)."""
    card_check = _load_card_check()
    raiz = _raiz_com_despacho(tmp_path, "RX-T1", "abc123")
    plano = _plano_com_item(raiz, _bloco("<ref>", "imprime **abc123**", "<ref>"))

    codigo = card_check.main(
        ["--plano", str(plano), "--tarefa", "RX-T1", "--root", str(raiz), "--mundo", "depois"]
    )
    saida = capsys.readouterr()

    assert codigo == 0
    assert "card_check: OK" in saida.out


def test_tr_ref_do_despacho_de_outra_tarefa_falha(tmp_path, capsys):
    """O `tarefa-corrente.json` é de outra tarefa (`OUTRA-T1`): `_ref_do_despacho` devolve `None`
    para `RX-T1`, e o item com `<ref>` no comando falha nomeado, sem rodar."""
    card_check = _load_card_check()
    raiz = _raiz_com_despacho(tmp_path, "OUTRA-T1", "abc123")
    plano = _plano_com_item(raiz, _bloco("<ref>", "imprime **abc123**", "<ref>"))

    codigo = card_check.main(
        ["--plano", str(plano), "--tarefa", "RX-T1", "--root", str(raiz), "--mundo", "depois"]
    )
    saida = capsys.readouterr()

    assert codigo == 1
    assert "card_check: FALHOU" in saida.err
    assert "item 1: <ref> sem recorte do despacho para 'RX-T1'" in saida.err


def test_tf_invariancia_nao_medida_antes_e_medida_depois(tmp_path, capsys):
    """Item de invariância (`(invariância)`, `DRF-36`) sem par `antes`/`depois`: `--mundo antes`
    não roda o comando e grava `saida == 'não medida (invariância)'` sem falha (hoje sai 1, `sem
    valor antes`); `--mundo depois` roda e o `exit 1` real não bate com o `exit 0` esperado."""
    card_check = _load_card_check()
    item = '  1. `python -c "import sys;sys.exit(1)"` → `exit 0` (invariância)\n'
    plano = _plano_com_item(tmp_path, item)
    destino = tmp_path / "medida.json"

    codigo = card_check.main(
        [
            "--plano",
            str(plano),
            "--tarefa",
            "RX-T1",
            "--root",
            str(_ROOT),
            "--mundo",
            "antes",
            "--gravar",
            str(destino),
        ]
    )
    capsys.readouterr()

    assert codigo == 0
    dados = json.loads(destino.read_text(encoding="utf-8"))
    assert dados["itens"][0]["saida"] == "não medida (invariância)"

    codigo2 = card_check.main(
        ["--plano", str(plano), "--tarefa", "RX-T1", "--root", str(_ROOT), "--mundo", "depois"]
    )
    capsys.readouterr()

    assert codigo2 == 1


# --- RAF-T15 (R-05): a medida gravada fica na pasta do plano da árvore medida, com o mundo no nome


def test_tf_medida_gravada_com_o_mundo_na_pasta_da_raiz(tmp_path, capsys):
    """`RAF-T15` (`R-05`) — plano em pasta (`P-0007-z`) numa árvore `real`; `--root` aponta para
    uma árvore `copia` (com cópia de `rdo.py`/`caminhos.py`). `--gravar` sem caminho, rodado uma
    vez com `--mundo antes` e outra com `--mundo depois`, grava os dois na pasta do plano dentro
    de `copia`, cada um com o mundo no nome; `real` não ganha pasta de evidência — hoje grava um
    arquivo só, sem mundo, na árvore `real`."""
    card_check = _load_card_check()
    real = tmp_path / "real"
    copia = tmp_path / "copia"
    ferramentas = copia / ".claude" / "tools"
    ferramentas.mkdir(parents=True)
    shutil.copy2(_ROOT / ".claude" / "tools" / "rdo.py", ferramentas / "rdo.py")
    shutil.copy2(_ROOT / ".claude" / "tools" / "caminhos.py", ferramentas / "caminhos.py")
    pasta_plano = real / "docs" / "plans" / "P-0007-z"
    pasta_plano.mkdir(parents=True)
    plano = pasta_plano / "plano.md"
    plano.write_text(
        "### RX-T1 — Card inline para medida com mundo [Sonnet · classe mecanica]\n"
        "- **Status:** `ready`\n"
        "- **Objetivo:** fixture de `card_check` para a `RAF-T15`.\n"
        "- **Entregável:** nenhum — fixture sintética, não é card vivo de plano.\n"
        "- **Verificação:**\n"
        "  1. `python -c \"print('a')\"` → `a` — antes `a`, depois `b`\n"
        "- **Pronto quando:** fixture existe e `card_check.py --tarefa RX-T1` sai 0.\n",
        encoding="utf-8",
    )

    card_check.main(
        [
            "--plano", str(plano), "--tarefa", "RX-T1", "--root", str(copia),
            "--mundo", "antes", "--gravar",
        ]
    )
    capsys.readouterr()
    card_check.main(
        [
            "--plano", str(plano), "--tarefa", "RX-T1", "--root", str(copia),
            "--mundo", "depois", "--gravar",
        ]
    )
    capsys.readouterr()

    pasta_evidencia = copia / "docs" / "plans" / "P-0007-z" / "evidencia"
    assert sorted(p.name for p in pasta_evidencia.iterdir()) == [
        "P-0007-RX-T1-medida-antes.json",
        "P-0007-RX-T1-medida-depois.json",
    ]
    assert not (real / "docs" / "plans" / "P-0007-z" / "evidencia").exists()
