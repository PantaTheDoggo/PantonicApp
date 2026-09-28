# RDO — P-0749 · SAN-T3

**Plano:** `docs/plans/P-0749-saneamento-artefatos.md`
**Tarefa:** `SAN-T3` — Relato, laudo e evidência nascem na pasta do plano
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O mantenedor do registro faz os instrumentos de relato e de evidência gravarem o relato, o laudo e a evidência de cada tarefa de plano novo dentro da pasta do plano; tíquete e plano antigo seguem gravando onde gravam hoje.

**Arquivos-alvo:** - `.claude/tools/caminhos.py` - `.claude/tools/rdo.py` - `.claude/tools/review_evidence.py` - `tests/test_rdo.py` - `tests/test_review_evidence.py` - `tests/test_caminhos.py`

**Verificação:** 1. ``` python -m pytest tests/test_rdo.py tests/test_review_evidence.py -q -k tf_san ``` → **3 passed**. **Medido antes: exit 5** (nenhum teste selecionado). 2. ``` pwsh -NoProfile -Command 'if (Test-Path .claude/tools/caminhos.py) { @(Select-String -LiteralPath .claude/tools/caminhos.py -SimpleMatch -Pattern "def destino_").Count } else { "ausente" }' ``` → **3**. **Medido antes: 0** (2026-09-25, `caminhos.py` da entrega de `AE-1`; ausente em 2026-09-24). 3. ``` python -m pytest tests/test_rdo.py tests/test_review_evidence.py -q ``` → **o total destes dois arquivos no despacho + 3, nenhuma falha**. **Medido antes: 104 passed** (2026-09-25; 95 em 2026-09-24). 4. ``` python -m pytest tests -q ``` → **o total anotado no passo 1 + 4, nenhuma falha** (três TF e o TF 4). **Medido antes: 339 passed** (2026-09-25, com a entrega de `AE-1`; 313 em 2026-09-24). 5. ``` python .claude/checks/dead_code.py ``` → **exit 0**. **Medido antes: exit 1** (2026-09-25, 8 achados em `caminhos.py`; exit 0 depois da `SAN-T1` redespachada).

**Pronto quando:** - kit.onde se gravam os registros da tarefa — dentro da pasta do plano; tíquete e plano antigo seguem na pasta comum — Verificação 1, 2, 3

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Fundamento:** DSA-9, DSA-16, DSA-17, DSA-18; §3.1; F-11; I-2.
- **Depende de:** `SAN-T2`
- **Operação do modelo:** `OP-3` - OP-3: O mantenedor do registro faz os instrumentos de relato e de evidência gravarem o relato, o laudo e a evidência de cada tarefa de plano novo dentro da pasta do plano; tíquete e plano antigo seguem gravando onde gravam hoje. - precisa de: kit — Quem implementa recebe essas ferramentas e esses textos. O que já está gravado continua sendo lido como hoje.; acervo existente — Quem implementa não o toca. Ele prova que nada do que existe se perdeu.
- **Camada e fronteira:** kit, `.claude/tools/rdo.py`, `.claude/tools/review_evidence.py`, `.claude/tools/caminhos.py` e três arquivos de teste. Flag explícita (`--rdo-dir`, `--laudos-dir`, `--out`) sempre vence; o destino novo vale só sem a flag e só para plano em pasta.
- **Texto novo, literal:** - em `caminhos.py`, imediatamente antes de `def main(` (`pasta_por_id` nasce com o chamador do `laudo`, `DSA-18`): ```python def pasta_por_id(raiz: Path, plano_id: str) -> Path | None: achadas = [p.parent for p in planos_dir(raiz).glob(plano_id + "-*/" + NOME_PLANO_PASTA) if p.is_file()] return achadas[0] if len(achadas) == 1 else None def destino_rdo(pasta: Path, tarefa: str) -> Path: return Path(pasta) / "rdo" / f"{tarefa}.md" def destino_laudo(pasta: Path, tarefa: str) -> Path: return Path(pasta) / "laudos" / f"{tarefa}.md" def destino_evidencia(pasta: Path, tarefa: str) -> Path: return Path(pasta) / "evidencia" / f"{tarefa}.md" ``` - `rdo.py`, no `close`, as duas linhas `rdo_dir = Path(args.rdo_dir) if args.rdo_dir is not None else _default_rdo_dir()` e `destino = rdo_dir / nome_arquivo` → ```python pasta_plano = _caminhos.pasta_do_plano(plano_path) if args.rdo_dir is None and pasta_plano is not None: destino = _caminhos.destino_rdo(pasta_plano, dossie.tarefa_id) rdo_dir = destino.parent else: rdo_dir = Path(args.rdo_dir) if args.rdo_dir is not None else _default_rdo_dir() destino = rdo_dir / nome_arquivo ``` e a linha `    _regenerar_indice(rdo_dir)` do `close` → `    if pasta_plano is None:` seguida de `        _regenerar_indice(rdo_dir)`. - `rdo.py`, no `laudo`, as duas linhas `laudos_dir = Path(args.laudos_dir) if args.laudos_dir is not None else _default_laudos_dir()` e `destino = laudos_dir / f"{args.plano}-{args.tarefa}.md"` → ```python pasta_plano = _caminhos.pasta_por_id(_default_root(), args.plano) if args.laudos_dir is None else None if pasta_plano is not None: destino = _caminhos.destino_laudo(pasta_plano, args.tarefa) laudos_dir = destino.parent else: laudos_dir = Path(args.laudos_dir) if args.laudos_dir is not None else _default_laudos_dir() destino = laudos_dir / f"{args.plano}-{args.tarefa}.md" ``` - `review_evidence.py` `main`, imediatamente antes da linha única `    if args.out is not None:`: ```python if args.out is None: pasta_plano = _caminhos.pasta_do_plano(args.plano) if pasta_plano is not None: args.out = _caminhos.destino_evidencia(pasta_plano, args.tarefa) ``` - em `tests/test_caminhos.py`, o TF `test_tf_san_4_pasta_por_id_sem_colisao_de_prefixo` — com `P-1-a/plano.md` e `P-12-b/plano.md`: `P-1` → pasta `P-1-a`, `P-12` → pasta `P-12-b`, `P-9` → `None` (glob por prefixo `P-1*` acha as duas).
- **Passos:** 1. Rodar `python -m pytest tests -q`; anotar o total. 2. Aplicar os blocos de `Texto novo, literal`. 3. Escrever os três TF de `Testes`. 4. Rodar a Verificação 1 a 5.
- **Restrições desta tarefa:** I-2 — com flag explícita, e para plano legado ou tíquete, destino e `INDEX.md` como hoje; nenhum teste grava no `docs/` real (todo TF isola o destino legado em `tmp_path`).
- **Não fazer:** não mover RDO, laudo ou evidência existente; não mudar o nome do RDO legado; não tocar `backlog.py` nem a doutrina.
- **Contingências:** 1. se uma das linhas a trocar não existir literal (renomeada por `TK-66`/`TK-74`) → parar e sinalizar `blocked` razão `premissa`, devolvendo a linha; 2. se `_regenerar_indice(rdo_dir)` aparecer mais de uma vez em `rdo.py` → aplicar a troca só à chamada dentro do `close` e seguir.
- **Fora do escopo desta tarefa:** a doutrina que cita os destinos (`SAN-T4`).

## Execução

**Consumo:** 39 tool uses, 88.2 k tokens, 272.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: nenhuma; testes=parcial (TF 15 inserido no meio do TR TK-62a em tests/test_review_evidence.py:227, amputando a recusa); achados de processo com rota em AE-3 do P-0749

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
