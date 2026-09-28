# RDO — P-0752 · FPU-T5

# Humano

Tarefa "O executor devolve a medida como arquivo, e a evidência a incorpora" concluída em 2026-09-26.
O verificador de cards agora grava o resultado de cada verificação num arquivo, e o dossiê do revisor passa a mostrar esse arquivo em vez de depender do relato do executor.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Fato no ponto de uso: os mecanismos contra o esquecimento e a assunção": 3/11 tarefas concluídas; próxima: "O gate do card roda no ensaio do planejador e no despacho do loop".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achado registrado no plano, com rota: 1 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/plans/P-0752-fato-no-ponto-de-uso.md`
**Tarefa:** `FPU-T5` — O executor devolve a medida como arquivo, e a evidência a incorpora
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `card_check.py --gravar <caminho.json>` roda os itens no mundo pedido e grava um JSON com um registro por item (DFP-6), sem mudar o exit; `review_evidence.py` incorpora o JSON como seção `## Medida do executor` quando `<dir da evidência>/<plano>-<ID>-medida.json` existe (DFP-17; plano legado sem `--out`: `docs/RDO/evidencia/`), e escreve `## Medida do executor` com `ausente` quando não.

**Arquivos-alvo:** - `.claude/tools/card_check.py` — `verificar_tarefa` (devolver também os registros) e `main` (`--gravar`) - `.claude/tools/review_evidence.py` — ponto onde o dossiê é montado antes de `--out` (função que escreve a saída; localizar por `--out` em `main`) - `tests/test_card_check.py`, `tests/test_review_evidence.py`

**Verificação:** 1. `python -m pytest tests/test_card_check.py tests/test_review_evidence.py -q` → verde — antes `68 passed`, depois `71 passed` (16 + 52 após `FPU-T1` e `FPU-T3`; medidos no acionamento 5). 2. `python -c "from pathlib import Path;print(Path('.claude/tools/review_evidence.py').read_text(encoding='utf-8').count('Medida do executor')>=1)"` → `True` — antes `False`, depois `True`. 3. `python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-corpus.md --tarefa CX-T1 --gravar scratchpad/medida-CX-T1.json` → exit 0 — antes `exit 2`, depois `exit 0` (flag inexistente antes; `scratchpad/` é ignorado pelo `.gitignore` e o `--gravar` cria a pasta). 4. `python -c "import json;print(json.load(open('scratchpad/medida-CX-T1.json',encoding='utf-8'))['itens'][0]['bate'])"` → `True` — antes `exit 1`, depois `True` (roda depois do item 3). 5. `python -m pytest -q` → nenhuma falha — antes `406 passed`, depois `409 passed`.

**Pronto quando:** retorno do executor.evidência de verificação — arquivo de medida gerado por comando, lido pela evidência — Verificações 1 a 4; régua executável.conferências — a medida do executor é registro, não prosa — Verificações 3 e 4.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Depende de:** `FPU-T1`
- **Operação do modelo:** `OP-5` - OP-5: O executor devolve a verificação como arquivo de medida gerado por comando, e o revisor e o loop leem o arquivo. - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; retorno do executor — Quem implementa faz o loop e o revisor lerem o arquivo de medida; prosa não conta como verde.
- **Fundamento:** DFP-6, DFP-17, F-6, causa 3 de F-10.
- **Contratos/classes:** JSON: `{"plano": str, "tarefa": str, "mundo": "antes"|"depois", "gerado_em": ISO-8601, "itens": [{"indice": int, "comando": str|null, "exit": int|null, "saida": str (≤400 chars), "bate": bool}]}`. `review_evidence` lê o arquivo por caminho derivado (`<dir da evidência>/<plano>-<ID>-medida.json`) e o transcreve como tabela `| item | comando | exit | bate |` sob `## Medida do executor`. `verificar_tarefa(plano, tarefa_id, root, mundo=None) -> tuple[bool, list[str], dict]` (DFP-17): o terceiro elemento é `medida = {"plano": plano_path.as_posix(), "tarefa": dossie.tarefa_id, "mundo": <mundo já resolvido>, "itens": registros}` — o JSON inteiro menos `gerado_em`, que `main` acrescenta ao gravar (`datetime.now(timezone.utc).isoformat(timespec="seconds")`). Registro: um por elemento de `itens` de `_parsear_itens` (item `fora da forma` não entra em `itens`, não tem registro e segue só como falha), criado no início da iteração com `exit: None`, `saida: ""`, `bate: False` e atualizado só no ramo que chama `_rodar_comando`: `exit` = returncode, `saida` = `saida.strip()[:400]`, `bate` = o `_bate_com_medido` daquele ramo; item manual, recusado ou sem valor fica com os valores iniciais. Caminho do JSON (DFP-17): `<dir da evidência>` = pai do `--out` depois da resolução que `main` já faz (plano em pasta sem `--out`: `<pasta>/evidencia`); plano legado sem `--out`: `<root>/docs/RDO/evidencia`. `<plano>` = `_caminhos.id_do_plano(plano_path) or plano_path.stem` (o `plano_id` que `montar_documento` já calcula); `<ID>` = `dossie.tarefa_id`. `secao_medida_do_executor(caminho_json: Path) -> list[str]`: primeira linha `## Medida do executor`; arquivo ausente → `- ausente: <caminho> não existe`; JSON ilegível ou sem as chaves (`ValueError`, `KeyError`, `TypeError`) → `- ilegível: <caminho> (<erro>)`, sem exceção; presente → `- Arquivo: <caminho>; mundo: <mundo>; gerado em: <gerado_em>`, linha vazia, `| item | comando | exit | bate |`, `|---|---|---|---|` e uma linha por item `| <indice> | <comando entre crases> | <exit> | <true ou false> |` (`comando` ou `exit` nulo → `-`; `|` dentro do comando sai escapado, `replace("|", "\\|")`).
- **Passos:** 1. `card_check`, `verificar_tarefa`: devolve `(ok, falhas, medida)` (Contratos); o mundo resolvido em `.claude/tools/card_check.py:344` — `if mundo is None:` chega a `main` dentro de `medida`, sem repetir a extração do dossiê. Único chamador: `.claude/tools/card_check.py:484` — `ok, falhas = verificar_tarefa(args.plano, args.tarefa, args.root, mundo=args.mundo)`; nenhum teste chama `verificar_tarefa` direto (todos passam por `main`). 2. `card_check`, `main`: `--gravar` (`type=Path`, default `None`). Quando vem, grava `medida` + `gerado_em` depois que `verificar_tarefa` retorna, **ok ou não**, com `json.dumps(..., ensure_ascii=False, indent=2)`, `parent.mkdir(parents=True, exist_ok=True)` e escrita atômica pelo padrão de `.claude/tools/review_evidence.py:837` — `fd, tmp_path = tempfile.mkstemp(` (temporário no mesmo diretório + `os.replace`); `CardCheckValidationError` sai exit 1 sem gravar. Exit, stdout e stderr ficam os de hoje. 3. `review_evidence`: `secao_medida_do_executor` (Contratos). `_renderizar` ganha o kwarg `linhas_medida: list[str] | None = None`, estendido (seguido de linha vazia) logo antes da seção `## Guardas`, isto é, antes de `.claude/tools/review_evidence.py:682` — `linhas.extend(`; `montar_documento` ganha o kwarg `dir_evidencia: Path | None = None` e passa `linhas_medida=secao_medida_do_executor(<caminho do JSON>)`, com o `plano_id` de `.claude/tools/review_evidence.py:728` — `plano_id = _caminhos.id_do_plano(plano_path) or plano_path.stem`. Em `main`, o bloco de `.claude/tools/review_evidence.py:830` — `if args.out is None:` (resolução do destino de plano em pasta) sobe para antes da chamada de `montar_documento`, que recebe `dir_evidencia=args.out.parent if args.out is not None else None`. 4. Testes (3; `68` → `71`): TF `test_tf_gravar_escreve_um_registro_por_item` em `tests/test_card_check.py` — `card_check.main(["--plano", str(_PLANO_CORPUS), "--tarefa", "CX-T1", "--root", str(_ROOT), "--gravar", str(tmp_path / "medida.json")])` → `0`; o JSON tem `mundo == "antes"`, `tarefa == "CX-T1"`, 1 item com `exit == 0` e `bate is True`. TF `test_tf_evidencia_incorpora_medida` em `tests/test_review_evidence.py` — padrão de `test_cli_main_ok_e_falhou` (`_init_repo_com_baseline`, `plano = tmp_path / "plano.md"` com `_escrever_plano`, `review_evidence.BATERIA_GUARDAS = _BATERIA_FAKE_VERDE`); JSON com o item `{"indice": 1, "comando": "python -c \"print('a')\"", "exit": 0, "saida": "a", "bate": true}` em `tmp_path / "ev" / "plano-T1-medida.json"` (plano sem id → stem `plano`); `main` com `--out tmp_path / "ev" / "plano-T1.md"` → `0`, e o arquivo gravado contém `## Medida do executor` e a linha ``| 1 | `python -c "print('a')"` | 0 | true |``. TR `test_tr_evidencia_sem_medida_diz_ausente` — `montar_documento(plano, "T1", repo, comandos_guardas=_BATERIA_FAKE_VERDE)` sem JSON → a seção `## Medida do executor` diz `ausente`.
- **Não fazer:** não tocar `encerrar.py` (I-4); não mudar o exit do `card_check` por causa de `--gravar`; não mudar o nome nem o caminho do dossiê de evidência; não mudar a assinatura de `montar_documento` e `_renderizar` além dos dois kwargs com default `None`; não versionar o JSON de `scratchpad/`.
- **Contingências:** - a montagem da saída são três pontos, e o Passo 3 diz o que cada um recebe: `main` (resolve o destino), `montar_documento` (deriva o caminho do JSON), `_renderizar` (escreve a seção) — não é bifurcação (DFP-17). - se `dead_code.py` acusar `secao_medida_do_executor` ou um kwarg novo → ambos têm chamador de produção (`montar_documento`); a acusação significa que só os testes os chamam: corrigir a chamada, nunca isentar (DFP-15). Medido no acionamento 5, em cópia com o reparo: `dead_code`, `ratchet_piso`, `kit_check` validate e `check-readme` exit 0.
- **Handover:** 2026-09-26 · para `FPU-T5a`, `FPU-T2` - **Entregue:** card_check: verificar_tarefa (.claude/tools/card_check.py:320) devolve (ok, falhas, medida) com medida = {plano, tarefa, mundo resolvido, itens}; main --gravar <json> (:511) acrescenta gerado_em e grava atomico, sem mudar exit; review_evidence: secao_medida_do_executor(caminho_json) em .claude/tools/review_evidence.py:588, montar_documento(..., dir_evidencia=) (:737) e _renderizar(..., linhas_medida=) (:629) poem '## Medida do executor' antes de '## Guardas' - **Contrato:** JSON de medida em <dir da evidencia>/<id do plano>-<ID>-medida.json (legado sem --out: docs/RDO/evidencia); evidencia sem o arquivo escreve linha 'ausente', JSON ilegivel 'ilegivel', sem excecao; tabela | item | comando | exit | bate |; suite 409 passed - **Não refazer:** --gravar e a secao da evidencia ja pagos; main de review_evidence ja resolve --out antes de montar_documento - **Pendente:** saida no JSON guarda a cabeca (strip()[:400]); em item de pytest o sumario 'N passed' fica fora - achado com rota de replanejamento
- **Notas de execução:** - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T5-o-executor-devolve-a-medida-como-arquivo-e-a-evidencia-a-inc.md`, veredito aprovado 100%

## Execução

**Consumo:** 60 tool uses, 130.9 k tokens, 631.6 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master concluiu a tarefa "Toda âncora de arquivo e linha do card leva o literal, e o gate confere a linha hoje" e vai pegar a tarefa "O executor devolve a medida como arquivo, e a evidência a incorpora".
Tarefa "O executor devolve a medida como arquivo, e a evidência a incorpora". Passo: conferir os gates e preparar o despacho.
Tarefa "O executor devolve a medida como arquivo, e a evidência a incorpora": gates aprovados; vou materializar in-progress e gravar o ponto de partida.
Agente executor recebe a tarefa "O executor devolve a medida como arquivo, e a evidência a incorpora" e vai executar: `card_check.py --gravar <caminho.json>` roda os itens no mundo pedido e grava um JSON com um registro por item (DFP-6), sem mudar o exit; `review_evidence.py` incorpora o JSON como seção `## Medida do executor` quando `docs/RDO/evidencia/<…
Agente executor devolveu a tarefa "O executor devolve a medida como arquivo, e a evidência a incorpora": blocked — motivo premissa: defeito=ambiguidade: Passo 1 do card fixa "verificar_tarefa passa a devolver (ok, falhas, registros) [...] os chamadores existentes (testes) recebem a tupla de três", mas Contratos/classes exige que o JSON gravado por `--gravar` tenha o campo top-level `"mundo": "antes"|"depois"` (tipo não-nulo, só dois literais) — e a resolução desse mundo (quando `--mundo` vem ausente) hoje só existe dentro de `verificar_tarefa` (`.claude/tools/card_check.py:344-350`: deriva de `rdo._status_atual(plano_path, dossie.tarefa_id, dossie, None)` sobre o `dossie` já extraído ali) e não é devolvida pela tupla de três. Isso concilia mal com o próprio exemplo do card (Verificação 3: `python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-corpus.md --tarefa CX-T1 --gravar ...` sem `--mundo`), que exercita exatamente o caminho em que `main` precisaria desse valor resolvido para escrever o JSON..
Scrum master vai marcar a tarefa "O executor devolve a medida como arquivo, e a evidência a incorpora" como blocked, sem RDO.
Agente consultor recebe a tarefa "O executor devolve a medida como arquivo, e a evidência a incorpora" e vai triar.
Agente consultor devolveu a tarefa "O executor devolve a medida como arquivo, e a evidência a incorpora": rota resolve.
Tarefa "O executor devolve a medida como arquivo, e a evidência a incorpora". Passo: conferir os gates e preparar o despacho.
Tarefa "O executor devolve a medida como arquivo, e a evidência a incorpora": gates aprovados; vou materializar in-progress e gravar o ponto de partida.
Agente executor recebe a tarefa "O executor devolve a medida como arquivo, e a evidência a incorpora" e vai executar: `card_check.py --gravar <caminho.json>` roda os itens no mundo pedido e grava um JSON com um registro por item (DFP-6), sem mudar o exit; `review_evidence.py` incorpora o JSON como seção `## Medida do executor` quando `<dir da evidência>/<…
Agente executor devolveu a tarefa "O executor devolve a medida como arquivo, e a evidência a incorpora": review — sem pendência.
Tarefa "O executor devolve a medida como arquivo, e a evidência a incorpora": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O executor devolve a medida como arquivo, e a evidência a incorpora" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O executor devolve a medida como arquivo, e a evidência a incorpora": aprovado 100%, bloqueante nenhuma.
