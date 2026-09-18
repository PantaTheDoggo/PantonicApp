# RDO — P-0739 · BKL-T2d

**Plano:** `docs/plans/P-0739-backlog-instrumento.md`
**Tarefa:** `BKL-T2d` — `rdo.py laudo`: o campo de achado de processo com os três alvos
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `rdo.py laudo` grava a seção `## Achado de processo` a partir de `--achado-processo <alvo> "<uma linha>"`, sem alterar percentual, veredito, dimensão bloqueante nem recomendação.

**Arquivos-alvo:** - `.claude/tools/rdo.py:24` — início do parágrafo do docstring que hoje diz "`laudo` (EXA-T8b/T18) não é tocado por esta rodada:". - `.claude/tools/rdo.py:450-488` — corpo de `cmd_laudo` até a linha `)` que fecha `conteudo_final`. - `.claude/tools/rdo.py:698-705` — bloco `laudo_parser.add_argument("--escalar", …)`. - `tests/test_rdo.py` — apenso de 4 testes ao final do arquivo. - `CHANGELOG.md` — uma linha sob `## [Não lançado]`, por `DB-13`.

**Verificação:** 1. `python -m pytest tests/test_rdo.py -q` → verde, com os 4 testes novos entre os coletados. 2. `python -m pytest tests/ -q` → verde. 3. `git status --short` → exatamente três caminhos: `.claude/tools/rdo.py`, `tests/test_rdo.py`, `CHANGELOG.md`.

**Pronto quando:** os quatro testes novos passam e `python -m pytest tests/ -q` está verde.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `review` · entregue 2026-09-16 (`pantonic-executor`), **nenhuma contingência acionada**; `tests/test_rdo.py` 38 passed, suíte 110 passed (piso 106). Achado de execução sobre a Verificação 3 registrado como `AE-5`. Consumo: ver `docs/telemetria.tsv` (`BKL-T2d`).
- **Depende de:** `DB-13`, `DB-28` (`RP-3`), `DB-30`/`DB-31` (`RP-4`, forma do campo `Contingências`). Nenhuma tarefa é insumo: esta tarefa não lê nem edita o que a `BKL-T2b`/`BKL-T2c` produzem.
- **Camada e fronteira:** camada de instrumento (`.claude/tools/`), fora das camadas de produto. A tarefa toca **três** arquivos e nenhum outro: `.claude/tools/rdo.py`, `tests/test_rdo.py`, `CHANGELOG.md`. Não edita `review_evidence.py`, `backlog.py`, `rdo_template.md`, `docs/RUBRICA_DE_REVISAO.md`, plano, diário nem inbox.
- **Fatos verificados na `RP-3` (não re-apurar, não re-grepar):** - `docs/RUBRICA_DE_REVISAO.md:239-246` define o campo e os três alvos (`dossiê`, `doutrina`, `rubrica`); a invariante 1 (`:249-251`) proíbe o achado de rebaixar dimensão de entrega, e a invariante 2 (`:252-254`) exige rota (tíquete, replanejamento ou emenda), que é ato da orquestração, não do gerador. - `calcular_laudo` (`rdo.py:386`) decide percentual, veredito, bloqueante e recomendação; o achado **não** passa por ela e a assinatura dela não muda. - `conteudo_final` é montado em `rdo.py:476-488`, com `## Lições aprendidas na tarefa` por último; `licoes_aprendidas` (`rdo.py:474`) é o precedente de campo discricionário com corpo vazio legítimo. - `_argv_laudo(laudos_dir, plano="P-TESTE", tarefa="T1", escalar=None, **overrides)` (`tests/test_rdo.py:48-70`) monta o argv completo do subcomando `laudo` com as sete dimensões; `rdo.main(...)` devolve exit code e os testes de recusa afirmam `not laudos_dir.exists() or list(laudos_dir.glob("*.md")) == []`. `rdo.py:450`): ```python _ALVOS_ACHADO = {"dossie": "dossiê", "doutrina": "doutrina", "rubrica": "rubrica"} def _formatar_achados_processo(pares: list[list[str]] | None) -> str: """`docs/RUBRICA_DE_REVISAO.md` §6: campo próprio, três alvos. Invariante 1 — o achado não rebaixa dimensão de entrega e não muda recomendação; por isso nada disto passa por `calcular_laudo`. Sem achado, o corpo é `nenhum` (a seção existe sempre).""" if not pares: return "nenhum" linhas = ["| alvo | achado |", "|---|---|"] for alvo, texto in pares: linhas.append(f"| {_ALVOS_ACHADO[alvo]} | {texto.strip()} |") return "\n".join(linhas) ``` `for flag, valor in (("--plano", args.plano), ("--tarefa", args.tarefa)):` e antes de `niveis = {...}`): ```python for alvo, texto in (args.achado_processo or []): if alvo not in _ALVOS_ACHADO: raise RdoValidationError( f"--achado-processo: alvo '{alvo}' fora de {sorted(_ALVOS_ACHADO)} " "(RUBRICA_DE_REVISAO.md §6)" ) if not texto.strip(): raise RdoValidationError("--achado-processo: a linha do achado não pode ser vazia") if "|" in texto or "\n" in texto: raise RdoValidationError( "--achado-processo: uma linha, sem '|' — a tabela do laudo quebraria" ) ``` `f"{tabela_niveis}\n\n"` e `"## Lições aprendidas na tarefa\n\n"`): ```python "## Achado de processo\n\n" f"{_formatar_achados_processo(args.achado_processo)}\n\n" ``` `laudo_parser.add_argument("--escalar", …)`): ```python laudo_parser.add_argument( "--achado-processo", dest="achado_processo", nargs=2, action="append", metavar=("ALVO", "LINHA"), default=None, help=( "Achado de processo (repetivel): ALVO e dossie, doutrina ou rubrica, seguido de uma " "linha. Nao altera percentual, veredito, bloqueante nem recomendacao (RUBRICA §6)." ), ) ```
- **Passos:** 1. Substituir, em `rdo.py:24`, o trecho "`laudo` (EXA-T8b/T18) não é tocado por esta rodada:" por "`laudo` (EXA-T8b/T18, estendido pela `BKL-T2d` do `P-0739`):". 2. Apensar ao final desse mesmo parágrafo do docstring (depois de "…que a regra `B1` consome.") a frase: ``--achado-processo <alvo> "<uma linha>"` (repetível; alvo em `dossie`, `doutrina` ou `rubrica`) grava a seção `## Achado de processo` e **não** altera percentual, veredito, bloqueante nem recomendação — invariante 1 de `docs/RUBRICA_DE_REVISAO.md` §6; `--escalar` fica reservado ao achado que invalida a rota (decisão de arquitetura ou de requisito).` 3. Inserir a constante `_ALVOS_ACHADO` e a função `_formatar_achados_processo` imediatamente acima de `def cmd_laudo(`. 4. Inserir em `cmd_laudo` o bloco de validação literal acima. 5. Inserir em `conteudo_final` as duas linhas literais acima, entre a tabela de níveis e `## Lições aprendidas na tarefa`. 6. Inserir o `add_argument` literal acima depois do bloco do `--escalar`. 7. Apensar ao final de `tests/test_rdo.py` os quatro testes da seção **Testes**. 8. Rodar as verificações 1 e 2. 9. Apensar a linha do `CHANGELOG.md` sob `## [Não lançado]`: ``- `rdo.py laudo`: campo `--achado-processo <alvo> "<linha>"` com os três alvos da `RUBRICA_DE_REVISAO.md` §6, sem mexer em percentual, veredito nem recomendação — `--escalar` volta a ser só pendência de arquitetura ou de requisito (`P-0739` `BKL-T2d`, `DB-28`).`` - `test_tf_laudo_achado_de_processo_grava_secao_com_os_tres_alvos` — TF: `rdo.main(_argv_laudo(laudos_dir) + ["--achado-processo", "dossie", "criterio de pronto exige registro fora dos alvos", "--achado-processo", "doutrina", "sem guardrail de atribuicao por tarefa"])`; afirma exit 0, `"## Achado de processo"` no arquivo gravado, e as duas linhas `| dossiê | …` e `| doutrina | …`. - `test_tr_laudo_achado_de_processo_nao_muda_veredito_nem_recomendacao` — TR: mesmo comando com **um** achado e todas as dimensões no default de `_argv_laudo`; afirma que o arquivo contém `"**Recomendação:** seguir"`, `"**Pendência:** nenhuma"` e o mesmo `"**Percentual:**"` do laudo gerado sem o achado (dois laudos, comparação da linha). - `test_tr_laudo_secao_achado_de_processo_existe_com_nenhum_sem_a_flag` — TR: `rdo.main(_argv_laudo(laudos_dir))`; afirma `"## Achado de processo"` e a linha `nenhum` no arquivo. - `test_tr_laudo_recusa_alvo_fora_dos_tres_e_linha_com_pipe` — TR: dois casos, cada um em seu `laudos_dir`: `["--achado-processo", "escopo", "x"]` e `["--achado-processo", "dossie", "a | b"]`; cada um afirma exit != 0 e `not laudos_dir.exists() or list(laudos_dir.glob("*.md")) == []`.
- **Restrições desta tarefa (copiadas inline):** - Não alterar `calcular_laudo`, `LaudoResultado`, `_RECOMENDACOES_VALIDAS`, `_DIMENSOES_ORDEM`, `_PESO`, `_VALOR_NIVEL` nem a semântica de `--escalar` e `--vermelho-mecanico`. - Não tocar `cmd_close`, `calcular_desdobramento`, `.claude/tools/rdo_template.md` nem `docs/RUBRICA_DE_REVISAO.md`: o achado é gravado no laudo, e o laudo é consumido e descartado pelo `scrum-master` (`DP-H`). - Nenhum caractere fora de cp1252 no texto de `help` do `add_argument` (o `--help` é impresso no console do Windows): a seta `→` e o símbolo de pertinência ficam fora. - `.claude/tools/` não está na lista `ask` de `.claude/settings.json`: editar por `Edit` direto, **sem** abrir UoW (`uow.py`). - Sem bump de versão e sem tag; nenhum projeto derivado é tocado (`DB-13`).
- **Não fazer:** não fazer o achado entrar em `calcular_laudo` nem alterar dimensão, percentual ou recomendação (invariante 1 da §6); não acrescentar alvo fora dos três; não gerar nem regerar laudo de tarefa já fechada (`DB-23`); não editar `docs/RDO/laudos/*`, `docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, `docs/plans/*`.
- **Contingências:** - se o texto de `rdo.py:450-488` ou do bloco do `--escalar` não for literalmente o transcrito → parar e sinalizar `blocked` razão `premissa`, citando o texto encontrado. - se `argparse` recusar `metavar=("ALVO", "LINHA")` com `nargs=2` → seguir com `metavar="ALVO LINHA"` e devolver na linha de retorno da entrega a frase `contingência 2 acionada: metavar trocada para "ALVO LINHA"` (`DB-30`). - se um teste já existente de `laudo` falhar por causa da seção nova → seguir com o ajuste das asserções desse teste (a seção `## Achado de processo` passa a existir sempre) e devolver na linha de retorno da entrega a frase `contingência 3 acionada: asserções de <nome do teste> ajustadas à seção nova` (`DB-30`). - se um teste já existente falhar sem citar `cmd_laudo`, `laudo` ou `conteudo_final` → parar e sinalizar `blocked` razão `dependencia`, nomeando o teste e a mensagem.
- **Fora do escopo desta tarefa:** a rota do achado (tíquete, replanejamento ou emenda da rubrica) é ato da orquestração, não do gerador; a seção `## Escopo` do dossiê de evidência (é a `BKL-T2b` e a `BKL-T2c`); qualquer mudança em `.claude/tools/backlog.py` (é a `BKL-T3`).

## Execução

**Consumo:** 23 tool uses, 83 k tokens, 202 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
