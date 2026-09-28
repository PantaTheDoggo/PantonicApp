# Evidência de revisão — P-0753 AF-T15

## Diff (`git diff --stat`)
```
docs/DIARIO_DE_OBRAS.md                            |   4 +-
 docs/plans/P-0753-auditoria-estagio-1/estado.tsv   |   2 +-
 .../evidencia/P-0753-AF-T15-medida.json            |  43 +++++++
 docs/telemetria.tsv                                |   1 +
 tests/conformance/test_camadas_do_kit.py           |  47 ++++++++
 tests/piso_comportamental.txt                      | 125 +++++++++++++++++++++
 6 files changed, 219 insertions(+), 3 deletions(-)
```

## Arquivos tocados
- `docs/DIARIO_DE_OBRAS.md` — atribuição: alheio; estado git: ` M`
- `docs/plans/P-0753-auditoria-estagio-1/estado.tsv` — atribuição: alheio; estado git: `??`
- `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T15-medida.json` — atribuição: alheio; estado git: `??`
- `docs/telemetria.tsv` — atribuição: alheio; estado git: ` M`
- `tests/conformance/test_camadas_do_kit.py` — atribuição: da entrega; estado git: `??`
- `tests/piso_comportamental.txt` — atribuição: da entrega; estado git: `??`

## Escopo
- Recorte: desde `fe6f469ffbac7afa1d9c679284529364d9e7fc2d`
- Arquivos-alvo declarados: `tests/piso_comportamental.txt`, `tests/conformance/test_camadas_do_kit.py`
- Arquivos tocados: `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T15-medida.json`, `docs/telemetria.tsv`, `tests/conformance/test_camadas_do_kit.py`, `tests/piso_comportamental.txt`
- Registro da orquestração (não atribuível a tarefa): `docs/DIARIO_DE_OBRAS.md`, `docs/plans/P-0753-auditoria-estagio-1/estado.tsv`, `docs/plans/P-0753-auditoria-estagio-1/evidencia/P-0753-AF-T15-medida.json`, `docs/telemetria.tsv`
- Veredito mecânico: conforme

## Trechos de diff dos arquivos-alvo (teto 4000 caracteres)

### `tests/piso_comportamental.txt`
```
# Piso comportamental do hub — um comportamento trancado por linha (GOVERNANCA.md §4.4); gerado pela AF-T15 do P-0753.
tests/conformance/test_camadas_do_kit.py::test_tr_camada_acusa_import_de_tests_e_de_caminhos — camada acusa import de tests e de caminhos
tests/test_backlog.py::test_tr_c10_contador_do_inbox_aponta_para_id_livre_nao_dispara — c10 contador do inbox aponta para id livre nao dispara
tests/test_backlog.py::test_tr_check_esqueleto_com_linha_de_tarefa_segue_acusando_c10 — check esqueleto com linha de tarefa segue acusando c10
tests/test_backlog.py::test_tr_check_plano_legado_blocked_no_contador_segue_acusando_c10 — check plano legado blocked no contador segue acusando c10
tests/test_backlog.py::test_tr_c12_depende_de_com_ids_de_tarefa_nao_dispara — c12 depende de com ids de tarefa nao dispara
tests/test_backlog.py::test_tr_resolver_citacao_secao_nao_casa_por_substring — resolver citacao secao nao casa por substring
tests/test_backlog.py::test_tr_resolver_citacao_secao_item5_arquivo_ausente_ou_ambiguo_devolve_none — resolver citacao secao item5 arquivo ausente ou ambiguo devolve none
tests/test_backlog.py::test_tr_resolver_citacao_secao_dominio_um_nivel — resolver citacao secao dominio um nivel
tests/test_backlog.py::test_tr_show_de_tiquete_nao_muda — show de tiquete nao muda
tests/test_backlog.py::test_tr_carregar_nunca_abre_historico — carregar nunca abre historico
tests/test_backlog.py::test_tr_saida_do_next_cabe_no_teto — saida do next cabe no teto
tests/test_backlog.py::test_tr_card_inteiro_notas_de_execucao_seguem_com_teto — card inteiro notas de execucao seguem com teto
tests/test_backlog.py::test_tr_linha_dos_tres_contadores_segue_identica — linha dos tres contadores segue identica
tests/test_backlog.py::test_tr_bloco_fila_nao_cresce_com_plano_terminal — bloco fila nao cresce com plano terminal
tests/test_backlog.py::test_tr_diretiva_sem_id_descartado_mensagem_igual_a_hoje — diretiva sem id descartado mensagem igual a hoje
tests/test_backlog.py::test_tr_bkl_grupos_posicionais — bkl grupos posicionais
tests/test_backlog.py::test_tr_status_canonico_continua_lido — status canonico continua lido
tests/test_backlog.py::test_tr_round_trip_blocked_ready_preserva_a_cauda — round trip blocked ready preserva a cauda
tests/test_backlog.py::test_tr_historico_do_inbox_so_cresce — historico do inbox so cresce
tests/test_backlog.py::test_tr_main_reconfigure_apos_parse_args_falha_no_ambiente_hostil — main reconfigure apos parse args falha no ambiente hostil
tests/test_backlog.py::test_tr_tk88_plano_com_tarefa_aberta_nao_fecha_e_tarefa_segue_a_tabela — tk88 plano com tarefa aberta nao fecha e tarefa segue a tabela
tests/test_backlog.py::test_tr_despachar_recusa_no_primeiro_gate_sem_escrever — despachar recusa no primeiro gate sem escrever
tests/test_card_check.py::test_tr_card_integro_sai_zero — card integro sai zero
tests/test_card_check.py::test_tr_pipe_dentro_de_argumento_citado_executa — pipe dentro de argumento citado executa
tests/test_card_check.py::test_tr_card_sem_ancora_nao_muda — card sem ancora nao muda
tests/test_card_check.py::test_tr_estado_tsv_ready_compara_antes — estado tsv ready compara antes
tests/test_crenca_hook.py::test_tr_payload_invalido_sai_zero — payload invalido sai zero
tests/test_dead_code.py::test_tr_orphan_symbol_is_flagged — orphan symbol is flagged
tests/test_dead_code.py::test_tr_undeclared_framework_virtual_is_flagged — undeclared framework virtual is flagged
tests/test_encerrar.py::test_tr_achado_do_laudo_repetido_nao_duplica — achado do laudo repetido nao duplica
tests/test_encerrar.py::test_tr_nao_medido_com_medida_na_serie_recusa — nao medido com medida na serie recusa
tests/test_encerrar.py::test_tr_nao_medido_com_trio_recusa — nao medido com trio recusa
tests/test_encerrar.py::test_tr_tarefa_trio_repetido_recusa_sem_escrever — tarefa trio repetido recusa sem escrever
tests/test_encerrar.py::test_tr_tarefa_recusa_sem_escrever[status-nao-review] — tarefa recusa sem escrever
tests/test_e
```
[truncado em 4000 caracteres]

### `tests/conformance/test_camadas_do_kit.py`
```
"""Teste de camadas do kit — instrumentos do kit não importam de `tests` nem de
`caminhos` por `import`/`from ... import ...` (`caminhos` é carregado por
`importlib.util.spec_from_file_location`, nunca por `import`).

AF-T15 (`docs/plans/P-0753-auditoria-estagio-1/plano.md`)."""
from __future__ import annotations

import ast
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent

MODULOS_PROIBIDOS = {"tests", "caminhos"}


def violacoes_de_camada(arquivos: list[Path]) -> list[str]:
    """Para cada arquivo, faz `ast.parse` e devolve uma linha
    `<arquivo>:<linha> importa <módulo>` para todo `Import`/`ImportFrom` cujo primeiro
    componente do módulo importado é `tests` ou `caminhos`."""
    achados: list[str] = []
    for arquivo in arquivos:
        arvore = ast.parse(arquivo.read_text(encoding="utf-8"), filename=str(arquivo))
        for node in ast.walk(arvore):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    primeiro = alias.name.split(".")[0]
                    if primeiro in MODULOS_PROIBIDOS:
                        achados.append(f"{arquivo}:{node.lineno} importa {alias.name}")
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    primeiro = node.module.split(".")[0]
                    if primeiro in MODULOS_PROIBIDOS:
                        achados.append(f"{arquivo}:{node.lineno} importa {node.module}")
    return achados


def test_tf_instrumentos_do_kit_nao_importam_tests_nem_caminhos():
    arquivos = sorted((RAIZ / ".claude" / "tools").glob("*.py")) + sorted(
        (RAIZ / ".claude" / "checks").glob("*.py")
    )
    assert violacoes_de_camada(arquivos) == []


def test_tr_camada_acusa_import_de_tests_e_de_caminhos(tmp_path):
    arquivo = tmp_path / "exemplo.py"
    arquivo.write_text("from tests import x\nimport caminhos\n", encoding="utf-8")
    assert len(violacoes_de_camada([arquivo])) == 2

```

## Medida do executor
- Arquivo: docs\plans\P-0753-auditoria-estagio-1\evidencia\P-0753-AF-T15-medida.json; mundo: depois; gerado em: 2026-09-27T16:14:52+00:00

| item | comando | exit | bate |
|---|---|---|---|
| 1 | `python .claude/checks/ratchet_piso.py` | 0 | true |
| 2 | `python -m pytest tests/conformance -q` | 0 | true |
| 3 | `python -c "import subprocess,sys;from pathlib import Path;p=Path('tests/piso_comportamental.txt');c=subprocess.run([sys.executable,'-m','pytest','--co','-q'],capture_output=True,text=True).stdout.splitlines();tr=sorted(x.strip() for x in c if '::test_tr_' in x);print('ausente' if not p.exists() else ('iguais' if sorted(l.split(' — ')[0].strip() for l in p.read_text(encoding='utf-8').splitlines() if l.strip() and not l.startswith('#'))==tr else 'diferentes'))"` | 0 | true |
| 4 | `python -m pytest -q` | 0 | true |
| 5 | `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` | 0 | true |

## Guardas (bateria de `GOVERNANCA.md` §3)
- `pytest` (`python -m pytest -q`): exit 0
- `dead_code` (`python .claude/checks/dead_code.py`): exit 0
- `ratchet_piso` (`python .claude/checks/ratchet_piso.py`): exit 0
- `kit_check_validate` (`pwsh .claude/checks/kit_check.ps1 -Mode validate`): exit 0
- `kit_check_check_drift` (`pwsh .claude/checks/kit_check.ps1 -Mode check-drift`): exit 0
- `check_readme` (`pwsh .claude/checks/check-readme.ps1`): exit 0
- Veredito mecânico (`guardas`): conforme
- Veredito mecânico (`testes`): conforme
