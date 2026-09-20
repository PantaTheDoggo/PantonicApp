"""EXA-T8b/T18/T19 (`docs/plans/P-0734-execucao-autonoma.md` `### T8b`/`### T18`/`### T19`) — TF/TR
de `.claude/tools/rdo.py laudo` e `close`. O RDO deixa de ser aberto no início (`new` morreu na
`T19`) e passa a ser gerado **inteiro** por `close`, na única transição que o produz (`review` →
`done`): `close` extrai o dossiê da tarefa do `.md` do plano pelo esquema da `DP-C`, recebe o
`pacote` (veredito/percentual/bloqueante/recomendação/pendência-do-laudo) e o consumo medido
(tool-uses/tokens-k/duração-s) por argumento — nunca lendo arquivo de laudo, que é descartado pelo
`scrum-master` (`DP-H`) —, **calcula** o desdobramento pela tabela de dois ramos da `T19` (item c) e
materializa o documento a partir do template (`.claude/tools/rdo_template.md`) numa única escrita
atômica, regenerando `docs/RDO/INDEX.md` por varredura do diretório.

EXA-T18 (`### T18`) não é tocada por esta rodada: `laudo` continua gravando documento próprio em
`docs/RDO/laudos/<plano>-<tarefa>.md`, **calculando** percentual, veredito, dimensão bloqueante e
recomendação (nunca aceitos como argumento — `DA-6`; camada mecânica é autoridade sobre o que ela
mede — `DA-7`).

`.claude/tools/` não é pacote importável (diretório com ponto no nome) — o módulo é carregado por
caminho via `importlib.util.spec_from_file_location`, mesmo padrão de `tests/test_telemetria.py` e
`tests/test_dead_code.py`.

Os testes de `close` usam tarefas **reais** já `done` do próprio plano (`T7`, `T8a`) como fixture de
dossiê — não um plano sintético —, porque `extrair_dossie` (reusada de `T8a`, e reusada também por
`review_evidence.py`) precisa de um cabeçalho real para extrair de. Todas as escritas vão para
`--rdo-dir` apontado a `tmp_path` (nunca o `docs/RDO` real do repositório); `--laudos-dir` não
existe mais na CLI de `close` porque o comando não lê laudo nenhum. `docs/plans/P-0734-execucao-
autonoma.md` é lido, nunca escrito, por este módulo."""
from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
_RDO_PATH = _ROOT / ".claude" / "tools" / "rdo.py"
_PLANO_REAL = _ROOT / "docs" / "plans" / "P-0734-execucao-autonoma.md"


def _load_rdo():
    spec = importlib.util.spec_from_file_location("rdo", _RDO_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# --- laudo (EXA-T8b / EXA-T18) — não tocado pela T19, suíte preservada -------------------------


def _argv_laudo(
    laudos_dir: Path, plano: str = "P-TESTE", tarefa: str = "T1", escalar: str | None = None,
    **overrides: str,
) -> list[str]:
    """`laudos_dir` é obrigatório (nunca `None`) para nenhum teste escrever no
    `docs/RDO/laudos/` real do repositório — sempre um subdiretório de `tmp_path`."""
    niveis = {
        "criterio-de-pronto": "conforme",
        "escopo": "conforme",
        "testes": "conforme",
        "guardas": "conforme",
        "rota": "conforme",
        "residuo": "conforme",
        "registro": "conforme",
    }
    niveis.update(overrides)
    argv = ["laudo", "--plano", plano, "--tarefa", tarefa, "--laudos-dir", str(laudos_dir)]
    if escalar is not None:
        argv += ["--escalar", escalar]
    for dimensao, nivel in niveis.items():
        argv += [f"--{dimensao}", nivel]
    return argv


def test_tf_laudo_calcula_percentual_veredito_e_recomendacao_pelas_tres_derivacoes(tmp_path):
    """TF da EXA-T18: as três recomendações derivadas da tabela — sem `--escalar`. Caso 1: tudo
    `conforme`, percentual 100, `veredito=aprovado` -> `recomendacao=seguir`. Caso 2: exemplo de
    `docs/RUBRICA_DE_REVISAO.md` §5 (`testes`/`residuo` em `parcial`), percentual 85,
    `veredito=ressalva` -> `recomendacao=seguir com ressalva`. Caso 3: `escopo` (bloqueante) em
    `nao-conforme`, percentual 88 mas dominância de bloqueante força `veredito=reprovado` ->
    `recomendacao=refazer`."""
    rdo = _load_rdo()
    casos = [
        (0, {}, "100", "aprovado", "nenhuma", "seguir"),
        (1, {"testes": "parcial", "residuo": "parcial"}, "85", "ressalva", "nenhuma",
         "seguir com ressalva"),
        (2, {"escopo": "nao-conforme"}, "88", "reprovado", "escopo", "refazer"),
    ]

    for i, overrides, percentual, veredito, bloqueante, recomendacao in casos:
        laudos_dir = tmp_path / f"caso-{i}"

        exit_code = rdo.main(_argv_laudo(laudos_dir, tarefa=f"T{i}", **overrides))

        assert exit_code == 0
        conteudo = (laudos_dir / f"P-TESTE-T{i}.md").read_text(encoding="utf-8")
        assert f"**Percentual:** {percentual}%" in conteudo
        assert f"**Veredito:** {veredito}" in conteudo
        assert f"**Dimensão bloqueante:** {bloqueante}" in conteudo
        assert f"**Recomendação:** {recomendacao}" in conteudo


def test_tr_laudo_escalar_domina_recomendacao_mesmo_com_veredito_aprovado(tmp_path):
    """TR: mesmo com todas as dimensões `conforme` (percentual 100%, `veredito=aprovado`, que sem
    `--escalar` daria `recomendacao=seguir`), a presença de `--escalar "<linha>"` força
    `recomendacao=escalar` e grava a linha como `Pendência` — dominante sobre a tabela."""
    rdo = _load_rdo()
    laudos_dir = tmp_path / "laudos"

    exit_code = rdo.main(
        _argv_laudo(laudos_dir, escalar="requisito de X nao esta claro no dossie")
    )

    assert exit_code == 0
    conteudo = (laudos_dir / "P-TESTE-T1.md").read_text(encoding="utf-8")
    assert "**Veredito:** aprovado" in conteudo
    assert "**Recomendação:** escalar" in conteudo
    assert "**Pendência:** requisito de X nao esta claro no dossie" in conteudo


def test_tr_laudo_recusa_recomendacao_percentual_e_veredito_como_argumento(tmp_path):
    """TR (`DA-6` estendida pela `T18`): `--recomendacao`, `--percentual` e `--veredito` não são
    flags aceitos — o argparse do subcomando `laudo` nem os declara, então passá-los é
    `unrecognized arguments`, exit != 0 (SystemExit do argparse), sem chegar a `cmd_laudo` nem
    escrever nada — o único canal de entrada do reviewer para a recomendação é `--escalar`."""
    rdo = _load_rdo()
    laudos_dir = tmp_path / "laudos"

    for flag, valor in (
        ("--recomendacao", "seguir"),
        ("--percentual", "90"),
        ("--veredito", "aprovado"),
    ):
        with pytest.raises(SystemExit) as exc:
            rdo.main(_argv_laudo(laudos_dir) + [flag, valor])
        assert exc.value.code not in (0, None)

    assert not laudos_dir.exists() or list(laudos_dir.glob("*.md")) == []


def test_tf_laudo_grava_documento_proprio_e_cria_diretorio(tmp_path):
    """TF da EXA-T18: `laudo` grava em `<laudos-dir>/<plano>-<tarefa>.md`, documento próprio —
    criando o diretório (inclusive aninhado, ainda inexistente) em vez de depender de um RDO já
    aberto por `new`."""
    rdo = _load_rdo()
    laudos_dir = tmp_path / "docs" / "RDO" / "laudos"
    assert not laudos_dir.exists()

    exit_code = rdo.main(_argv_laudo(laudos_dir, plano="P-0734", tarefa="T18"))

    assert exit_code == 0
    destino = laudos_dir / "P-0734-T18.md"
    assert destino.is_file()
    conteudo = destino.read_text(encoding="utf-8")
    assert conteudo.startswith("# Laudo — P-0734 · T18")
    assert "**Percentual:** 100%" in conteudo


def test_tf_laudo_card_licoes_aprendidas_entra_quando_fornecido(tmp_path):
    """TF da EXA-T52 (`DP-Q` §21 item 3): o card "Lições aprendidas na tarefa" — residência do
    registro qualitativo — passa a ser emitido no documento do laudo. Discricionário: quando o
    `--licoes-aprendidas` é fornecido, o texto entra sob o heading do card."""
    rdo = _load_rdo()
    laudos_dir = tmp_path / "laudos"

    exit_code = rdo.main(
        _argv_laudo(laudos_dir)
        + ["--licoes-aprendidas", "consumo alto por retrabalho de escopo mal decomposto"]
    )

    assert exit_code == 0
    conteudo = (laudos_dir / "P-TESTE-T1.md").read_text(encoding="utf-8")
    assert "## Lições aprendidas na tarefa" in conteudo
    assert "consumo alto por retrabalho de escopo mal decomposto" in conteudo


def test_tr_laudo_card_licoes_aprendidas_vazio_e_legitimo_sem_flag(tmp_path):
    """TR: sem `--licoes-aprendidas` (discricionário — o reviewer só preenche quando enxergar algo,
    `DP-Q` §21 item 3), o laudo grava normalmente (exit 0), o card existe no documento, mas o corpo
    fica vazio — vazio é estado legítimo, não defeito: nenhuma validação reprova a ausência e nenhum
    texto de preenchimento forçado (tipo "nenhuma") é gravado no lugar."""
    rdo = _load_rdo()
    laudos_dir = tmp_path / "laudos"

    exit_code = rdo.main(_argv_laudo(laudos_dir))

    assert exit_code == 0
    conteudo = (laudos_dir / "P-TESTE-T1.md").read_text(encoding="utf-8")
    assert "## Lições aprendidas na tarefa" in conteudo
    corpo_apos_card = conteudo.split("## Lições aprendidas na tarefa", 1)[1].strip()
    assert corpo_apos_card == ""


def test_tr_laudo_recusa_conforme_contra_vermelho_mecanico(tmp_path, capsys):
    """TR (`DA-7`): a camada mecânica é autoridade sobre o que ela mede — marcar `testes` como
    `conforme` quando a chamada também declara `testes` como vermelho mecânico é recusado, exit
    != 0, o identificador da dimensão nomeado em stderr, e nada é escrito."""
    rdo = _load_rdo()
    laudos_dir = tmp_path / "laudos"

    exit_code = rdo.main(
        _argv_laudo(laudos_dir, testes="conforme") + ["--vermelho-mecanico", "testes"]
    )

    assert exit_code != 0
    saida = capsys.readouterr()
    assert "testes" in saida.err
    assert not laudos_dir.exists() or list(laudos_dir.glob("*.md")) == []


def test_tr_laudo_recusa_nao_se_aplica_em_dimensao_que_nao_admite(tmp_path, capsys):
    """TR: `guardas` é uma das quatro dimensões que nunca admitem `nao-se-aplica`
    (`RUBRICA_DE_REVISAO.md` §5) — marcá-la assim é recusado, exit != 0, dimensão nomeada em
    stderr, e nada é escrito."""
    rdo = _load_rdo()
    laudos_dir = tmp_path / "laudos"

    exit_code = rdo.main(_argv_laudo(laudos_dir, guardas="nao-se-aplica"))

    assert exit_code != 0
    saida = capsys.readouterr()
    assert "guardas" in saida.err
    assert not laudos_dir.exists() or list(laudos_dir.glob("*.md")) == []


# --- close (EXA-T19) — o RDO nasce inteiro no fechamento ----------------------------------------


def _argv_close(tmp_path, tarefa="T7", omit=(), **overrides: str) -> list[str]:
    campos = {
        "--plano": str(_PLANO_REAL),
        "--tarefa": tarefa,
        "--tool-uses": "12",
        "--tokens-k": "80",
        "--duracao-s": "300",
        "--veredito": "aprovado",
        "--percentual": "100",
        "--bloqueante": "nenhuma",
        "--recomendacao": "seguir",
        "--pendencia-laudo": "nenhuma",
        "--rdo-dir": str(tmp_path),
    }
    campos.update(overrides)
    for chave in omit:
        campos.pop(chave, None)
    argv = ["close"]
    for flag, valor in campos.items():
        argv += [flag, valor]
    return argv


def test_tf_close_gera_rdo_completo_a_partir_do_plano_pacote_e_consumo(tmp_path):
    """TF da EXA-T19: uma única chamada de `close` sobre a `T7` (real, `done`) extrai o dossiê do
    plano (mesma gramática de `extrair_dossie` que `new` usava), transcreve o `pacote`
    (veredito/percentual/bloqueante/recomendação) e o consumo medido (tool-uses/tokens-k/duração-s)
    para o documento, calcula o desdobramento e grava `## Fechamento` — tudo numa única escrita.
    Nenhum arquivo de laudo é lido; `docs/RDO/INDEX.md` é regenerado."""
    rdo = _load_rdo()

    exit_code = rdo.main(_argv_close(tmp_path))

    assert exit_code == 0
    gerados = [p for p in tmp_path.glob("*.md") if p.name != "INDEX.md"]
    assert len(gerados) == 1
    conteudo = gerados[0].read_text(encoding="utf-8")

    # identidade da tarefa e dossiê extraído do corpo real da T7
    assert "T7" in conteudo
    assert "provar o padrão" in conteudo  # início do Objetivo real da T7
    assert "cria `.claude/tools/telemetria.py`" in conteudo  # Arquivos-alvo real da T7

    # consumo medido, transcrito (classe implementação padrão) — nenhum teto sobrevive no RDO
    assert "12 tool uses" in conteudo
    assert "80" in conteudo and "300" in conteudo
    assert "Teto" not in conteudo

    # pacote do laudo, transcrito sem recálculo
    assert "**Veredito:** aprovado" in conteudo
    assert "**Percentual:** 100%" in conteudo
    assert "**Dimensão bloqueante:** nenhuma" in conteudo
    assert "**Recomendação:** seguir" in conteudo

    # desdobramento calculado (aprovado, sem estouro) e sem ponteiro para laudo nenhum
    assert "**Desdobramento:** aprovado" in conteudo
    assert "{{" not in conteudo
    assert "LAUDO_PATH" not in conteudo
    assert "docs/RDO/laudos" not in conteudo
    assert "status" not in conteudo.lower()

    indice = (tmp_path / "INDEX.md").read_text(encoding="utf-8")
    assert gerados[0].name in indice


def test_tf_close_tokens_k_decimal_grava_sem_conversao(tmp_path):
    """TF (`P-0740` `LM-T1`, `DM-11`): `--tokens-k` aceita decimal de uma casa (`type=float`) e o
    grava no RDO sem conversão — `203.7` sai idêntico no documento."""
    rdo = _load_rdo()

    exit_code = rdo.main(_argv_close(tmp_path, **{"--tokens-k": "203.7"}))

    assert exit_code == 0
    gerados = [p for p in tmp_path.glob("*.md") if p.name != "INDEX.md"]
    conteudo = gerados[0].read_text(encoding="utf-8")
    assert "203.7" in conteudo


def test_tr_close_tokens_k_inteiro_grava_uma_casa_decimal_sempre(tmp_path):
    """TR (`DM-11`): `--tokens-k 80` grava `80.0` — uma casa decimal sempre, o que discrimina da
    regra concorrente `str(int)`, que daria `80` sem o `.0`."""
    rdo = _load_rdo()

    exit_code = rdo.main(_argv_close(tmp_path, **{"--tokens-k": "80"}))

    assert exit_code == 0
    gerados = [p for p in tmp_path.glob("*.md") if p.name != "INDEX.md"]
    conteudo = gerados[0].read_text(encoding="utf-8")
    assert "80.0" in conteudo


def test_tf_close_tokens_k_negativo_recusa(tmp_path, capsys):
    """TF (`P-0740` `LM-T1a`, `DM-15`): `--tokens-k -5` com `--plano` apontando arquivo
    **inexistente** sai exit 1 com `tokens_k: '-5' é negativo` no stderr — a regra concorrente
    (medida na `RP-5`) também saía exit 1, mas com `plano: arquivo não encontrado`; quem
    discrimina é a mensagem, provando que a guarda de domínio corre antes da checagem de
    `--plano` (`DM-15` (iii))."""
    rdo = _load_rdo()

    exit_code = rdo.main(
        _argv_close(tmp_path, **{"--plano": "NAO-EXISTE.md", "--tokens-k": "-5"})
    )

    assert exit_code == 1
    saida = capsys.readouterr()
    assert "rdo: FALHOU - tokens_k: '-5' é negativo" in saida.err
    assert [p for p in tmp_path.glob("*.md")] == []


def test_tf_close_tokens_k_nao_finito_recusa(tmp_path, capsys):
    """TF (`DM-15`): `--tokens-k nan` sai exit 1 com `tokens_k: 'nan' não é finito` — a regra
    concorrente (`argparse` `type=float`) convertia `nan` sem reclamar e a execução seguia até a
    checagem de `--plano`."""
    rdo = _load_rdo()

    exit_code = rdo.main(
        _argv_close(tmp_path, **{"--plano": "NAO-EXISTE.md", "--tokens-k": "nan"})
    )

    assert exit_code == 1
    saida = capsys.readouterr()
    assert "rdo: FALHOU - tokens_k: 'nan' não é finito" in saida.err
    assert [p for p in tmp_path.glob("*.md")] == []


def test_tf_close_tool_uses_negativo_recusa(tmp_path, capsys):
    """TF (`DM-15`): `--tool-uses -1` sai exit 1 com `tool_uses: '-1' é negativo` — a regra
    concorrente (`argparse` `type=int`) convertia e a execução seguia."""
    rdo = _load_rdo()

    exit_code = rdo.main(_argv_close(tmp_path, **{"--tool-uses": "-1"}))

    assert exit_code == 1
    saida = capsys.readouterr()
    assert "rdo: FALHOU - tool_uses: '-1' é negativo" in saida.err
    assert [p for p in tmp_path.glob("*.md")] == []


def test_tf_close_tokens_k_nao_numerico_recusa_com_exit_1(tmp_path, capsys):
    """TF (`DM-15`): `--tokens-k abc` sai exit **1** com `tokens_k: 'abc' não é numérico` — a
    regra concorrente (`argparse` `type=float`) saía exit **2** com o bloco de `usage`; é esta
    linha que tranca a remoção do `type=`."""
    rdo = _load_rdo()

    exit_code = rdo.main(_argv_close(tmp_path, **{"--tokens-k": "abc"}))

    assert exit_code == 1
    saida = capsys.readouterr()
    assert "rdo: FALHOU - tokens_k: 'abc' não é numérico" in saida.err
    assert [p for p in tmp_path.glob("*.md")] == []


def test_tf_close_duracao_s_decimal_aceita_e_grava_uma_casa(tmp_path):
    """TF (`DM-15`, `DM-11`): sobre o plano de fixture que os testes de `close` já usam,
    `--duracao-s 1020.6` — o literal que o hook `SubagentStop` emite — fecha o RDO normalmente e
    o documento contém `1020.6`. A regra concorrente (`argparse` `type=int`) saía exit 2,
    `invalid int value: '1020.6'`."""
    rdo = _load_rdo()

    exit_code = rdo.main(_argv_close(tmp_path, **{"--duracao-s": "1020.6"}))

    assert exit_code == 0
    gerados = [p for p in tmp_path.glob("*.md") if p.name != "INDEX.md"]
    conteudo = gerados[0].read_text(encoding="utf-8")
    assert "1020.6" in conteudo


def test_tr_close_consumo_valido_segue_igual(tmp_path):
    """TR: o caminho feliz de hoje (`--tool-uses 5 --tokens-k 80 --duracao-s 300`) continua
    fechando o RDO, com `80.0` e `300` legíveis no documento — uma guarda escrita com `>` no
    lugar de `>=` derrubaria o zero e quebraria este caminho."""
    rdo = _load_rdo()

    exit_code = rdo.main(
        _argv_close(tmp_path, **{"--tool-uses": "5", "--tokens-k": "80", "--duracao-s": "300"})
    )

    assert exit_code == 0
    gerados = [p for p in tmp_path.glob("*.md") if p.name != "INDEX.md"]
    conteudo = gerados[0].read_text(encoding="utf-8")
    assert "80.0" in conteudo
    assert "300" in conteudo


def _escrever_plano_sintetico(caminho: Path, cabecalho: str) -> None:
    caminho.write_text(
        "# Plano de teste\n\n"
        f"{cabecalho}\n"
        "- **Objetivo:** validar a gramática do cabeçalho.\n"
        "- **Arquivos-alvo:** `arquivo.py`.\n"
        "- **Verificação:** bateria do §3.\n"
        "- **Pronto quando:** o teste passa.\n",
        encoding="utf-8",
    )


def test_tf_extrair_dossie_cabecalho_gramatica_nova_sem_teto(tmp_path):
    """TF da CTX-T1d (`DX-15`): o cabeçalho na gramática nova — `[<modelo> · classe <classe>]`,
    sem segmento de teto — parseia sem flag nenhuma, com `modelo`/`classe` corretos."""
    rdo = _load_rdo()
    plano = tmp_path / "plano.md"
    _escrever_plano_sintetico(plano, "### T1 — Tarefa sintética [Sonnet · classe implementacao]")

    dossie = rdo.extrair_dossie(
        plano, "T1", esquema_legado=False, modelo_legado=None, classe_legado=None,
    )

    assert dossie.modelo == "Sonnet"
    assert dossie.classe == "implementacao"
    assert dossie.esquema == "padrao"
    assert not hasattr(dossie, "teto")


def test_tr_extrair_dossie_cabecalho_historico_com_teto_e_aceito_e_descartado(tmp_path):
    """TR (`DX-15`): o cabeçalho histórico com ` · teto <N>` continua parseando — mesmos
    `titulo`/`classe` do cabeçalho novo —, e o número é descartado: `close` sobre esse cabeçalho
    gera um RDO sem a palavra 'Teto' em lugar nenhum."""
    rdo = _load_rdo()
    plano = tmp_path / "plano.md"
    _escrever_plano_sintetico(
        plano, "### T1 — Tarefa sintética [Sonnet · classe implementacao · teto 40]"
    )

    dossie = rdo.extrair_dossie(
        plano, "T1", esquema_legado=False, modelo_legado=None, classe_legado=None,
    )
    assert dossie.titulo == "Tarefa sintética"
    assert dossie.classe == "implementacao"

    rdo_dir = tmp_path / "rdo"
    exit_code = rdo.main(
        [
            "close", "--plano", str(plano), "--tarefa", "T1",
            "--tool-uses", "5", "--tokens-k", "10", "--duracao-s", "60",
            "--veredito", "aprovado", "--percentual", "100", "--bloqueante", "nenhuma",
            "--recomendacao", "seguir", "--pendencia-laudo", "nenhuma",
            "--rdo-dir", str(rdo_dir),
        ]
    )

    assert exit_code == 0
    conteudo = next(p for p in rdo_dir.glob("*.md") if p.name != "INDEX.md").read_text(
        encoding="utf-8"
    )
    assert "Teto" not in conteudo


@pytest.mark.parametrize(
    "flag",
    ["--veredito", "--percentual", "--bloqueante", "--recomendacao", "--pendencia-laudo"],
)
def test_tr_close_recusa_cada_campo_do_pacote_ausente(tmp_path, flag):
    """TR: os cinco argumentos do `pacote` (`DP-H` item 4) são obrigatórios — omitir qualquer um
    deles falha ruidosamente pelo próprio `argparse` (exit != 0), sem chegar a `cmd_close` nem
    escrever nada."""
    rdo = _load_rdo()

    with pytest.raises(SystemExit) as exc:
        rdo.main(_argv_close(tmp_path, omit=(flag,)))
    assert exc.value.code not in (0, None)
    assert [p for p in tmp_path.glob("*.md")] == []


def test_tr_close_recusa_veredito_fora_do_dominio(tmp_path):
    """TR: `--veredito` tem domínio fechado `{aprovado, ressalva}` (`choices`) — a premissa de
    escopo (`DP-F`) torna `reprovado`/`bloqueado` inalcançáveis por `close`. Passar qualquer outro
    valor falha pelo `argparse`, exit != 0, nada escrito."""
    rdo = _load_rdo()

    with pytest.raises(SystemExit) as exc:
        rdo.main(_argv_close(tmp_path, **{"--veredito": "reprovado"}))
    assert exc.value.code not in (0, None)
    assert [p for p in tmp_path.glob("*.md")] == []


def test_tr_close_recusa_percentual_fora_de_0_100(tmp_path):
    """TR: `--percentual` é inteiro em `0..100` — `101` é recusado pelo `argparse`, exit != 0,
    nada escrito."""
    rdo = _load_rdo()

    with pytest.raises(SystemExit) as exc:
        rdo.main(_argv_close(tmp_path, **{"--percentual": "101"}))
    assert exc.value.code not in (0, None)
    assert [p for p in tmp_path.glob("*.md")] == []


def test_tf_close_regenera_indice_com_mais_de_um_rdo(tmp_path):
    """TF: fechar duas tarefas reais distintas (`T7`, `T8a`) no mesmo `--rdo-dir` regenera
    `docs/RDO/INDEX.md` por varredura do diretório, listando os dois documentos e ignorando um
    `.gitkeep` presente no meio do caminho."""
    rdo = _load_rdo()
    (tmp_path / ".gitkeep").write_text("placeholder\n", encoding="utf-8")

    assert rdo.main(_argv_close(tmp_path, tarefa="T7")) == 0
    assert rdo.main(_argv_close(tmp_path, tarefa="T8a")) == 0

    indice = (tmp_path / "INDEX.md").read_text(encoding="utf-8")
    gerados = [p.name for p in tmp_path.glob("*.md") if p.name != "INDEX.md"]
    assert len(gerados) == 2
    for nome in gerados:
        assert nome in indice
    assert ".gitkeep" not in indice


def test_tr_close_recusa_new_e_laudos_dir_fora_da_cli(tmp_path):
    """TR: o subcomando `new` não existe mais (`rdo.py --help` não o oferece) e `close` não aceita
    `--laudos-dir` (o comando não lê laudo nenhum) — as duas chamadas falham pelo `argparse`."""
    rdo = _load_rdo()

    with pytest.raises(SystemExit) as exc_new:
        rdo.main(["new", "--plano", str(_PLANO_REAL), "--tarefa", "T7", "--rdo-dir", str(tmp_path)])
    assert exc_new.value.code not in (0, None)

    with pytest.raises(SystemExit) as exc_laudos_dir:
        rdo.main(_argv_close(tmp_path, **{"--laudos-dir": str(tmp_path)}))
    assert exc_laudos_dir.value.code not in (0, None)


def test_tf_close_calcula_desdobramento_por_veredito_sem_ramificar_por_consumo(tmp_path):
    """TF do item (c), reescrito pela `DP-Q` (§21 do `P-0734`): o desdobramento é tabela de dois
    ramos só por veredito (`ressalva` -> `aprovado com ressalva`; `aprovado` -> `aprovado`) — o
    terceiro ramo por estouro de teto caiu, porque nenhum teto numérico governa fluxo. `--tool-uses`
    alto não abre um ramo novo: o consumo continua medido e registrado no documento
    (`TOOL_USES`), só o veredito decide o desdobramento; o campo `teto` do cabeçalho da `T7`
    (`DX-15`) é aceito e ignorado, sem sobreviver no documento."""
    rdo = _load_rdo()

    assert rdo.calcular_desdobramento("aprovado") == "aprovado"
    assert rdo.calcular_desdobramento("ressalva") == "aprovado com ressalva"

    exit_code = rdo.main(_argv_close(tmp_path, **{"--tool-uses": "41"}))
    assert exit_code == 0
    conteudo = next(p for p in tmp_path.glob("*.md") if p.name != "INDEX.md").read_text(
        encoding="utf-8"
    )
    # consumo acima do teto do cabeçalho continua medido e registrado, sem abrir ramo de
    # desdobramento e sem que o número de teto sobreviva no documento
    assert "41 tool uses" in conteudo
    assert "Teto" not in conteudo
    assert "**Desdobramento:** aprovado" in conteudo
    assert "estouro" not in conteudo.lower()


@pytest.mark.parametrize(
    "pendencia,pendencia_laudo,esperado",
    [
        (None, "nenhuma", ["nenhuma"]),
        (None, "laudo aponta requisito ambíguo", ["laudo: laudo aponta requisito ambíguo"]),
        ("executor precisa de decisão sobre X", "nenhuma",
         ["executor: executor precisa de decisão sobre X"]),
        ("executor precisa de decisão sobre X", "laudo aponta requisito ambíguo",
         ["executor: executor precisa de decisão sobre X",
          "laudo: laudo aponta requisito ambíguo"]),
    ],
)
def test_tf_close_compoe_pendencia_para_o_dono_pelas_quatro_linhas_da_tabela(
    tmp_path, pendencia, pendencia_laudo, esperado
):
    """TF do item (d): as quatro combinações de `--pendencia`/`--pendencia-laudo` compõem o campo
    `Pendência para o dono` exatamente pela tabela — `ausente`/`nenhuma` -> `nenhuma`;
    `ausente`/`<Y>` -> `laudo: <Y>`; `<X>`/`nenhuma` -> `executor: <X>`; `<X>`/`<Y>` -> as duas
    linhas, nesta ordem."""
    rdo = _load_rdo()
    overrides = {"--pendencia-laudo": pendencia_laudo}
    if pendencia is not None:
        overrides["--pendencia"] = pendencia

    exit_code = rdo.main(_argv_close(tmp_path, tarefa="T7", **overrides))

    assert exit_code == 0
    conteudo = next(p for p in tmp_path.glob("*.md") if p.name != "INDEX.md").read_text(
        encoding="utf-8"
    )
    linha_pendencia = "\n".join(esperado)
    assert linha_pendencia in conteudo


def test_tr_close_recusa_pendencia_de_duas_linhas(tmp_path):
    """TR: `--pendencia` aceita uma linha — passar duas (`\\n` embutido) é recusado por
    `_contar_linhas`, exit != 0, nada escrito."""
    rdo = _load_rdo()

    exit_code = rdo.main(
        _argv_close(tmp_path, **{"--pendencia": "linha 1\nlinha 2"})
    )

    assert exit_code != 0
    assert [p for p in tmp_path.glob("*.md")] == []


def test_tf_close_transcreve_card_licoes_aprendidas_quando_fornecido(tmp_path):
    """TF da EXA-T52 (`DP-Q` §21 item 3): `close` **transcreve** — sem decidir o que fazer com ele
    (isso é a `T30`) — o card "Lições aprendidas na tarefa" para o RDO persistido, no mesmo padrão
    do resto do `pacote`."""
    rdo = _load_rdo()

    exit_code = rdo.main(
        _argv_close(tmp_path, **{"--licoes-aprendidas": "achado fora de escopo: X"})
    )

    assert exit_code == 0
    conteudo = next(p for p in tmp_path.glob("*.md") if p.name != "INDEX.md").read_text(
        encoding="utf-8"
    )
    assert "## Lições aprendidas na tarefa" in conteudo
    assert "achado fora de escopo: X" in conteudo


def test_tr_close_card_licoes_aprendidas_ausente_nao_e_obrigatorio(tmp_path):
    """TR: `--licoes-aprendidas` não integra o `pacote` obrigatório (discricionário, `DP-Q` §21 item
    3) — omiti-lo não falha `close`, o card continua presente no RDO (heading materializado) e
    nenhum placeholder é forçado no lugar do texto ausente; todo `{{...}}` do template segue
    substituído."""
    rdo = _load_rdo()

    exit_code = rdo.main(_argv_close(tmp_path))

    assert exit_code == 0
    conteudo = next(p for p in tmp_path.glob("*.md") if p.name != "INDEX.md").read_text(
        encoding="utf-8"
    )
    assert "## Lições aprendidas na tarefa" in conteudo
    assert "{{" not in conteudo


def test_tr_close_recusa_fechar_a_mesma_tarefa_duas_vezes(tmp_path, capsys):
    """TR: uma segunda chamada de `close` para a mesma `plano_id`/`tarefa`/`título` mira o mesmo
    caminho de destino, que já existe — falha ruidosa (substitui a antiga checagem de 'RDO já
    aberto/fechado'), exit != 0, arquivo original intocado."""
    rdo = _load_rdo()
    assert rdo.main(_argv_close(tmp_path)) == 0
    caminho = next(p for p in tmp_path.glob("*.md") if p.name != "INDEX.md")
    original = caminho.read_text(encoding="utf-8")

    exit_code = rdo.main(_argv_close(tmp_path))

    assert exit_code != 0
    saida = capsys.readouterr()
    assert "já existe" in saida.err
    assert caminho.read_text(encoding="utf-8") == original


def test_tr_laudo_recusa_plano_e_tarefa_em_forma_de_caminho(tmp_path, capsys):
    """TR (disciplina de instrumento, `GOVERNANCA.md` §3, 2026-09-16): `--plano` e `--tarefa` são
    identificadores, não caminhos — `--plano docs/plans/P-0739-....md` quase gravou um laudo em
    `docs/RDO/laudos/docs/plans/...`. Recusa com exit != 0, flag nomeado em stderr, nada escrito."""
    rdo = _load_rdo()
    laudos_dir = tmp_path / "laudos"

    exit_code = rdo.main(
        _argv_laudo(laudos_dir, plano="docs/plans/P-0739-backlog-instrumento.md", tarefa="T2")
    )

    assert exit_code != 0
    assert "--plano" in capsys.readouterr().err
    assert not laudos_dir.exists() or list(laudos_dir.glob("*.md")) == []


def test_tf_extrair_dossie_id_prefixado(tmp_path):
    """TF da BKL-T2a (`DB-22`): ID de tarefa com prefixo de plano (`BKL-T2`) é localizado pelo
    cabeçalho e casado por igualdade exata, prefixo incluído."""
    rdo = _load_rdo()
    plano = tmp_path / "plano.md"
    _escrever_plano_sintetico(plano, "### BKL-T2 — Tarefa sintética [Sonnet · classe implementacao]")

    dossie = rdo.extrair_dossie(
        plano, "BKL-T2", esquema_legado=False, modelo_legado=None, classe_legado=None,
    )

    assert dossie.tarefa_id == "BKL-T2"
    assert dossie.modelo == "Sonnet"
    assert dossie.classe == "implementacao"
    assert dossie.esquema == "padrao"


def test_tf_extrair_dossie_id_prefixado_com_letra_e_teto_legado(tmp_path):
    """TF da BKL-T2a (`DB-22`): ID prefixado com letra de subtarefa (`CTX-T1d`) e segmento de
    teto histórico (`· teto 30`), aceito e descartado."""
    rdo = _load_rdo()
    plano = tmp_path / "plano.md"
    _escrever_plano_sintetico(plano, "### CTX-T1d — Tarefa sintética [Opus · classe redacao · teto 30]")

    dossie = rdo.extrair_dossie(
        plano, "CTX-T1d", esquema_legado=False, modelo_legado=None, classe_legado=None,
    )

    assert dossie.tarefa_id == "CTX-T1d"
    assert dossie.classe == "redacao"
    assert dossie.esquema == "padrao"


def test_tf_extrair_dossie_bracket_com_aceite_do_dono(tmp_path):
    """TF da BKL-T2a (`DB-20`): segmento ` + dono` no bracket é aceito e descartado."""
    rdo = _load_rdo()
    plano = tmp_path / "plano.md"
    _escrever_plano_sintetico(plano, "### BKL-T9 — Tarefa sintética [Opus + dono · classe redacao]")

    dossie = rdo.extrair_dossie(
        plano, "BKL-T9", esquema_legado=False, modelo_legado=None, classe_legado=None,
    )

    assert dossie.modelo == "Opus"
    assert dossie.classe == "redacao"
    assert dossie.esquema == "padrao"


def test_tr_extrair_dossie_id_casa_por_igualdade_exata(tmp_path):
    """TR da BKL-T2a: prefixo nunca casa por sufixo nem por ID parcial — `T1` não encontra
    `BKL-T1`, e `BKL-T2` não encontra `BKL-T1`."""
    rdo = _load_rdo()
    plano = tmp_path / "plano.md"
    _escrever_plano_sintetico(plano, "### BKL-T1 — Tarefa sintética [Sonnet · classe redacao]")

    with pytest.raises(rdo.RdoValidationError):
        rdo.extrair_dossie(
            plano, "T1", esquema_legado=False, modelo_legado=None, classe_legado=None,
        )

    with pytest.raises(rdo.RdoValidationError):
        rdo.extrair_dossie(
            plano, "BKL-T2", esquema_legado=False, modelo_legado=None, classe_legado=None,
        )


def test_id_header_re_aceita_tk_subtarefa_e_recusa_nivel_dois():
    """TK-62a (`DB-17`): `_ID_HEADER_RE` passa a reconhecer a forma `TK-<n><letra>` de subtarefa
    de tíquete, além da gramática `(?:[A-Z0-9]+-)?T[0-9]+[a-z]?` já aceita — e continua recusando
    o cabeçalho de nível 2 do tíquete-pai (`##`, sem bracket), que não é ID de tarefa."""
    rdo = _load_rdo()

    assert rdo._ID_HEADER_RE.match("### TK-57a — Título").group(1) == "TK-57a"
    assert rdo._ID_HEADER_RE.match("### TK-62a — Título").group(1) == "TK-62a"
    assert rdo._ID_HEADER_RE.match("### TK-54b — Título").group(1) == "TK-54b"
    assert rdo._ID_HEADER_RE.match("### TK-57 — Título").group(1) == "TK-57"
    assert rdo._ID_HEADER_RE.match("## TK-62 — Título") is None


def test_header_bracket_re_aceita_tk_e_recusa_id_fora_da_gramatica():
    """TK-62a (`DB-17`): `_HEADER_BRACKET_RE` reconhece `TK-<n><letra>` no grupo `id` e continua
    recusando cabeçalho cujo texto não é ID de tarefa (`2.5`, `Achados`)."""
    rdo = _load_rdo()

    aceito = rdo._HEADER_BRACKET_RE.match(
        "### TK-62a — Título [Sonnet · classe implementacao]"
    )
    recusado_numeral = rdo._HEADER_BRACKET_RE.match(
        "### 2.5 — Título [Sonnet · classe implementacao]"
    )
    recusado_achados = rdo._HEADER_BRACKET_RE.match(
        "### Achados — Título [Sonnet · classe implementacao]"
    )

    assert aceito is not None
    assert aceito.group("id") == "TK-62a"
    assert recusado_numeral is None
    assert recusado_achados is None


# --- laudo · achado de processo (BKL-T2d, RUBRICA_DE_REVISAO.md §6) ------------------------------


def test_tf_laudo_achado_de_processo_grava_secao_com_os_tres_alvos(tmp_path):
    """TF da BKL-T2d: `--achado-processo` repetível grava a seção `## Achado de processo` com uma
    linha de tabela por alvo."""
    rdo = _load_rdo()
    laudos_dir = tmp_path / "laudos"

    exit_code = rdo.main(
        _argv_laudo(laudos_dir)
        + [
            "--achado-processo", "dossie", "criterio de pronto exige registro fora dos alvos",
            "--achado-processo", "doutrina", "sem guardrail de atribuicao por tarefa",
        ]
    )

    assert exit_code == 0
    conteudo = (laudos_dir / "P-TESTE-T1.md").read_text(encoding="utf-8")
    assert "## Achado de processo" in conteudo
    assert "| dossiê | criterio de pronto exige registro fora dos alvos |" in conteudo
    assert "| doutrina | sem guardrail de atribuicao por tarefa |" in conteudo


def test_tr_laudo_achado_de_processo_nao_muda_veredito_nem_recomendacao(tmp_path):
    """TR da BKL-T2d: com um achado de processo, veredito, pendência e percentual são os mesmos do
    laudo gerado sem achado — invariante 1 de `docs/RUBRICA_DE_REVISAO.md` §6."""
    rdo = _load_rdo()
    laudos_dir_com = tmp_path / "com-achado"
    laudos_dir_sem = tmp_path / "sem-achado"

    exit_com = rdo.main(
        _argv_laudo(laudos_dir_com)
        + ["--achado-processo", "rubrica", "invariante 1 poderia ser mais explicita"]
    )
    exit_sem = rdo.main(_argv_laudo(laudos_dir_sem))

    assert exit_com == 0
    assert exit_sem == 0
    conteudo_com = (laudos_dir_com / "P-TESTE-T1.md").read_text(encoding="utf-8")
    conteudo_sem = (laudos_dir_sem / "P-TESTE-T1.md").read_text(encoding="utf-8")
    assert "**Recomendação:** seguir" in conteudo_com
    assert "**Pendência:** nenhuma" in conteudo_com
    linha_percentual_com = next(l for l in conteudo_com.splitlines() if l.startswith("**Percentual:**"))
    linha_percentual_sem = next(l for l in conteudo_sem.splitlines() if l.startswith("**Percentual:**"))
    assert linha_percentual_com == linha_percentual_sem


def test_tr_laudo_secao_achado_de_processo_existe_com_nenhum_sem_a_flag(tmp_path):
    """TR da BKL-T2d: sem `--achado-processo`, a seção existe sempre, com corpo `nenhum`."""
    rdo = _load_rdo()
    laudos_dir = tmp_path / "laudos"

    exit_code = rdo.main(_argv_laudo(laudos_dir))

    assert exit_code == 0
    conteudo = (laudos_dir / "P-TESTE-T1.md").read_text(encoding="utf-8")
    assert "## Achado de processo" in conteudo
    assert "nenhum" in conteudo


def test_tr_laudo_recusa_alvo_fora_dos_tres_e_linha_com_pipe(tmp_path):
    """TR da BKL-T2d: alvo fora de `dossie`/`doutrina`/`rubrica` e linha com `|` são recusados, sem
    escrever laudo nenhum."""
    rdo = _load_rdo()

    laudos_dir_alvo = tmp_path / "alvo-invalido"
    exit_alvo = rdo.main(
        _argv_laudo(laudos_dir_alvo) + ["--achado-processo", "escopo", "x"]
    )
    assert exit_alvo != 0
    assert not laudos_dir_alvo.exists() or list(laudos_dir_alvo.glob("*.md")) == []

    laudos_dir_pipe = tmp_path / "linha-com-pipe"
    exit_pipe = rdo.main(
        _argv_laudo(laudos_dir_pipe) + ["--achado-processo", "dossie", "a | b"]
    )
    assert exit_pipe != 0
    assert not laudos_dir_pipe.exists() or list(laudos_dir_pipe.glob("*.md")) == []


def test_tf_rdo_3campos():
    """TF da LM-T4a: `_HEADER_BRACKET_RE` aceita o cabeçalho de três campos (`DM-5`), com o campo
    `esforço` opcional entre modelo e classe. Concorrente: com a gramática de hoje o match é
    `None`, e é esse `None` que leva `extrair_dossie` ao ramo legado e produz o exit 1 do `AE-5`."""
    rdo = _load_rdo()

    match = rdo._HEADER_BRACKET_RE.match(
        "### XX-T1 — Título [Sonnet · esforço medium · classe implementacao]"
    )

    assert match is not None
    assert match.group("modelo") == "Sonnet"
    assert match.group("classe") == "implementacao"


def test_tr_rdo_2campos():
    """TR da LM-T4a: `_HEADER_BRACKET_RE` continua aceitando o cabeçalho de dois campos (sem
    `esforço`) — o corpus inteiro de planos vivos está nessa forma. Concorrente: com o campo
    `esforço` implementado como obrigatório, esta linha passaria a dar `None`."""
    rdo = _load_rdo()

    match = rdo._HEADER_BRACKET_RE.match(
        "### XX-T2 — Título [Opus + dono · classe investigacao]"
    )

    assert match is not None
    assert match.group("modelo") == "Opus"
    assert match.group("classe") == "investigacao"


# --- _parsear_campos: bullet de topo encerra o campo (LM-T3b, AE-27 item 2) ---------------------

_REVIEW_EVIDENCE_PATH = _ROOT / ".claude" / "tools" / "review_evidence.py"


def _load_review_evidence():
    spec = importlib.util.spec_from_file_location("review_evidence", _REVIEW_EVIDENCE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_tf_campo_termina_em_bullet_de_prosa():
    """TF da LM-T3b (`AE-27` item 2): um bullet de topo cujo rótulo não termina em `:**` — logo
    não casa `_CAMPO_RE` — encerra o campo corrente do mesmo jeito que um campo canônico
    encerraria. Concorrente: o código de hoje só encerra campo em bullet que case `_CAMPO_RE`,
    então as linhas indentadas sob o bullet de prosa (aqui, uma tabela com `251.1` e
    `message.id` entre crases) continuam anexadas a `arquivos-alvo`, e `extrair_arquivos_alvo`
    devolveria os dois caminhos **mais** esses dois literais que `_eh_caminho` aceita por
    terem 'extensão'."""
    rdo = _load_rdo()
    review_evidence = _load_review_evidence()

    linhas = [
        "- **Arquivos-alvo:**",
        "  - `.claude/tools/rdo.py`",
        "  - `tests/test_rdo.py`",
        "- **A calibração medida no `ESC-3` (2026-09-18) — residência única desta tabela.**",
        "  | campo | valor |",
        "  | --- | --- |",
        "  | `251.1` | `message.id` |",
    ]

    campos, _ = rdo._parsear_campos(linhas)

    assert review_evidence.extrair_arquivos_alvo(campos) == [
        ".claude/tools/rdo.py",
        "tests/test_rdo.py",
    ]


def test_tr_campo_multilinha_continua_valendo():
    """TR da LM-T3b: campo canônico seguido de vários sub-bullets indentados continua sendo lido
    por inteiro — o reparo encerra o campo em bullet de topo, não em qualquer linha nova.
    Concorrente: encerrar o campo em qualquer linha nova quebraria a lista de `Arquivos-alvo` de
    todo card do plano, que é multilinha."""
    rdo = _load_rdo()
    review_evidence = _load_review_evidence()

    linhas = [
        "- **Arquivos-alvo:**",
        "  - `.claude/tools/rdo.py`",
        "  - `tests/test_rdo.py`",
        "  - `.claude/tools/review_evidence.py`",
    ]

    campos, _ = rdo._parsear_campos(linhas)

    assert review_evidence.extrair_arquivos_alvo(campos) == [
        ".claude/tools/rdo.py",
        "tests/test_rdo.py",
        ".claude/tools/review_evidence.py",
    ]
