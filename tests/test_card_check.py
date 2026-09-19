"""LM-T5b (`docs/plans/P-0740-loop-de-modulos.md` `### LM-T5b`) — TF/TR de
`.claude/tools/card_check.py`: a régua de autoria roda o comando publicado no bloco `Verificação`
de um card e compara com o `Medido antes` declarado, contra os três cards sintéticos de
`tests/fixtures/card_check/plano-exemplo.md` (`EX-T1`/`EX-T2`/`EX-T3`, nenhum card vivo de plano —
`DM-38` (ii)). Padrão de carga do módulo idêntico a `tests/test_review_evidence.py` (`.claude/`
não é pacote importável)."""
from __future__ import annotations

import importlib.util
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_CARD_CHECK_PATH = _ROOT / ".claude" / "tools" / "card_check.py"
_PLANO_FIXTURE = _ROOT / "tests" / "fixtures" / "card_check" / "plano-exemplo.md"


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
