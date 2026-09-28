"""P-0749 SAN-T1 — TF de `.claude/tools/caminhos.py`, carregado por caminho (`.claude/` não é
pacote importável), mesmo padrão dos demais testes de ferramenta do kit."""
from __future__ import annotations

import importlib.util
from pathlib import Path

_CAMINHOS_PATH = Path(__file__).resolve().parents[1] / ".claude" / "tools" / "caminhos.py"


def _carregar_caminhos():
    spec = importlib.util.spec_from_file_location("caminhos", _CAMINHOS_PATH)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


caminhos = _carregar_caminhos()


def test_tf_san_1_id_aceita_zero_e_legado():
    assert caminhos.ID_PLANO_RE.match("P-0")
    assert caminhos.ID_PLANO_RE.match("P-12")
    assert caminhos.ID_PLANO_RE.match("P-0749")
    assert not caminhos.ID_PLANO_RE.match("P-")
    assert not caminhos.ID_PLANO_RE.match("P-12a")


def test_tf_san_2_id_do_plano_nas_duas_formas():
    assert caminhos.id_do_plano(Path("docs/plans/P-0-gama/plano.md")) == "P-0"
    assert caminhos.id_do_plano(Path("docs/plans/P-12-x/plano.md")) == "P-12"
    assert caminhos.id_do_plano(Path("docs/plans/P-0749-saneamento-artefatos.md")) == "P-0749"
    assert caminhos.id_do_plano(Path("tmp/plano.md")) is None


def test_tf_destino_medida_tres_residencias():
    """`TK-92a` — `destino_medida` cobre as três residências pela mesma função: tíquete do
    diário e plano legado caem em `<raiz>/docs/RDO/evidencia`, plano em pasta grava ao lado
    do plano, em `<pasta>/evidencia`."""
    raiz = Path("/raiz")

    assert caminhos.destino_medida(
        raiz, Path("docs/DIARIO_DE_OBRAS.md"), "TK-1a"
    ) == raiz / "docs" / "RDO" / "evidencia" / "DIARIO_DE_OBRAS-TK-1a-medida.json"

    assert caminhos.destino_medida(
        raiz, Path("docs/plans/P-0001-x.md"), "T1"
    ) == raiz / "docs" / "RDO" / "evidencia" / "P-0001-T1-medida.json"

    assert caminhos.destino_medida(
        raiz, Path("docs/plans/P-0002-y/plano.md"), "T2"
    ) == Path("docs/plans/P-0002-y") / "evidencia" / "P-0002-T2-medida.json"


def test_tf_san_3_arquivos_de_plano(tmp_path):
    base = tmp_path / "docs" / "plans"
    base.mkdir(parents=True)
    (base / "P-0749-a.md").write_text("a", encoding="utf-8")
    (base / "P-0-b").mkdir()
    (base / "P-0-b" / "plano.md").write_text("b", encoding="utf-8")
    (base / "_INBOX.md").write_text("inbox", encoding="utf-8")
    (base / "P-1-c").mkdir()
    (base / "P-2-d").mkdir()
    (base / "P-2-d" / "outro.md").write_text("outro", encoding="utf-8")

    resultado = caminhos.arquivos_de_plano(tmp_path)

    assert resultado == [
        tmp_path / "docs" / "plans" / "P-0-b" / "plano.md",
        tmp_path / "docs" / "plans" / "P-0749-a.md",
    ]


def test_tf_san_5_linha_viva_do_inbox():
    m1 = caminhos.CAMINHO_PLANO_INBOX_RE.search("- `docs/plans/P-0-gama/plano.md` — nota")
    assert m1 and m1.group(0) == "docs/plans/P-0-gama/plano.md"

    m2 = caminhos.CAMINHO_PLANO_INBOX_RE.search(
        "- `docs/plans/P-0749-saneamento-artefatos.md` — nota"
    )
    assert m2 and m2.group(0) == "docs/plans/P-0749-saneamento-artefatos.md"


def test_tf_san_16_cli_lista_os_planos(tmp_path, capsys):
    base = tmp_path / "docs" / "plans"
    base.mkdir(parents=True)
    (base / "P-0749-a.md").write_text("a", encoding="utf-8")
    (base / "P-0-b").mkdir()
    (base / "P-0-b" / "plano.md").write_text("b", encoding="utf-8")

    codigo = caminhos.main(["--root", str(tmp_path)])

    assert codigo == 0
    saida = capsys.readouterr().out
    assert saida == "P-0\tdocs/plans/P-0-b/plano.md\nP-0749\tdocs/plans/P-0749-a.md\n"


def test_tf_san_4_pasta_por_id_sem_colisao_de_prefixo(tmp_path):
    base = tmp_path / "docs" / "plans"
    base.mkdir(parents=True)
    (base / "P-1-a").mkdir()
    (base / "P-1-a" / "plano.md").write_text("a", encoding="utf-8")
    (base / "P-12-b").mkdir()
    (base / "P-12-b" / "plano.md").write_text("b", encoding="utf-8")

    assert caminhos.pasta_por_id(tmp_path, "P-1") == base / "P-1-a"
    assert caminhos.pasta_por_id(tmp_path, "P-12") == base / "P-12-b"
    assert caminhos.pasta_por_id(tmp_path, "P-9") is None


def test_tf_san_6_formatar_id_preserva_largura():
    assert caminhos.formatar_id(750, 4) == "P-0750"
    assert caminhos.formatar_id(1, 1) == "P-1"
    assert caminhos.formatar_id(10, 1) == "P-10"
