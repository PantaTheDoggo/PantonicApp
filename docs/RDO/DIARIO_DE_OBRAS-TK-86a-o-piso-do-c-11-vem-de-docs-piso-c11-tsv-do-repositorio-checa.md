# RDO — DIARIO_DE_OBRAS · TK-86a

# Humano

Tarefa "O piso do `C-11` vem de `docs/PISO_C11.tsv` do repositório checado" concluída em 2026-09-26.
O backlog.py e o encerrar.py agora leem a lista de citações quebradas já conhecidas de um arquivo do próprio repositório, e deixam de acusar falso C-17 nos projetos derivados.
Revisão: aprovada com ressalva (94%).
Pendência para o dono: nenhuma.
Tíquete "O piso do `C-11` mora no código do `backlog.py` e acusa `C-17` em todo outro repositório": 1/1 tarefas concluídas; nenhuma tarefa pronta na fila dele.
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achados registrados no plano, com rota: 2 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-86a` — O piso do `C-11` vem de `docs/PISO_C11.tsv` do repositório checado
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** em `.claude/tools/backlog.py`: 1. a constante `_PISO_C11` sai; entram `_PISO_C11_ARQUIVO = "docs/PISO_C11.tsv"`, `_PISO_C11_CABECALHO = "arquivo\tsecao\torigem"` e a função pública `ler_piso_c11(repo: Path) -> tuple[set[tuple[str, str]] | None, list[Violacao]]`: arquivo ausente → `(None, [])`; primeira linha diferente do cabeçalho → `(set(), [Violacao("C-17", "docs/PISO_C11.tsv", 1, "cabeçalho fora do esquema")])`; linha não vazia com número de campos (separados por tabulação) diferente de 3, `arquivo` vazio ou `secao` fora de `^\d+(?:\.\d+)*$` → `Violacao("C-17", "docs/PISO_C11.tsv", <n>, "linha fora do esquema")` e a linha não entra no piso; as demais linhas entram como `(arquivo, secao)`; 2. no `main`, subcomando `check`, as violações de `ler_piso_c11(repo)` vêm primeiro, seguidas das de `check(...)` com `piso_c11=` o conjunto lido (e não mais a constante); `check()` não muda de assinatura nem de comportamento; 3. o comentário de origem da constante (medida de 2026-09-20, `TK-60a`) vai para a docstring de `ler_piso_c11`, e o comentário do `C-17` em `check` passa a dizer que o piso vem do arquivo do repositório checado; 4. em `.claude/tools/encerrar.py`, `fechar_plano`: a chamada `_backlog.check(...)` do gate deixa de ler `_backlog._PISO_C11`; antes dela, `piso_c11, violacoes = _backlog.ler_piso_c11(repo)`, e as violações de `check(...)`, com `piso_c11=piso_c11`, somam-se a essas (`violacoes += ...`), na mesma ordem do `main`. Na raiz, o arquivo novo `docs/PISO_C11.tsv`, em UTF-8 com fim de linha LF, com o cabeçalho e a linha `GOVERNANCA.md<TAB>1.1<TAB>TK-60a, medido em 2026-09-20`.

**Arquivos-alvo:** - `.claude/tools/backlog.py` - `tests/test_backlog.py` - `docs/PISO_C11.tsv` (novo; `git check-ignore` sai `1`, medido: não é ignorado) - `.claude/tools/encerrar.py` (só a chamada do item 4, linhas 680-682 de hoje; o arquivo é do `TK-88`, cujos cards `TK-88b`..`TK-88d` também o tocam)

**Verificação:** 1. `python .claude/tools/backlog.py check` → `check: OK — nenhuma violação.` — antes `exit 0`, depois `exit 0`. 2. `python -c "from pathlib import Path;t=Path('.claude/tools/backlog.py').read_text(encoding='utf-8');print(t.count('_PISO_C11')-t.count('_PISO_C11_'))"` → `0` (a constante `_PISO_C11` sem sufixo) — antes `0`, depois `0` (o antes é a árvore de hoje, com o item 1 já aplicado; antes da primeira execução era `2`). 3. `python -m pytest tests/test_backlog.py -q -k piso_c11_tsv` → os testes novos verdes — antes `exit 0`, depois `exit 0` (o antes é a árvore de hoje, com os testes já aplicados; antes da primeira execução era `exit 5`). 4. `python -m pytest tests/test_backlog.py -q` → verde — antes `exit 0`, depois `exit 0`. 5. `python -m pytest -q` → nenhuma falha — antes `exit 1`, depois `exit 0` (antes `427 passed, 1 failed`, o teste do `encerrar.py`; depois `428 passed`). 6. `python -c "from pathlib import Path;t=Path('.claude/tools/encerrar.py').read_text(encoding='utf-8');print(t.count('_PISO_C11')-t.count('_PISO_C11_'))"` → `0` (o `encerrar.py` não lê mais a constante) — antes `1`, depois `0`.

**Pronto quando:** o `check` de um repositório sem `docs/PISO_C11.tsv` não acusa `C-17`, o do hub segue OK com o piso lido do arquivo, e linha malformada do arquivo sai `C-17` com a linha dela.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Caso medido que motivou:** ver `## TK-86`.
- **Reparo medido (protótipo do consultor, 2026-09-26, cópia da árvore já apagada):** os itens 1 e 2 acima e o arquivo novo. Com eles: `check` da árvore OK exit `0`; cópia da `verde` só com o `C-16` do `TK-1a`; arquivo removido da árvore → 10 `C-11` e nenhum `C-17`; arquivo com uma entrada `GOVERNANCA.md`/`3.2` e uma linha `lixo` → `C-17 docs/PISO_C11.tsv:4 — linha fora do esquema` e o `C-17` da entrada órfã; suíte `376 passed`. Os dois testes abaixo falham sobre o `backlog.py` de hoje e passam com o protótipo.
- **Estado da árvore na retomada (medido pelo consultor, 2026-09-26, acionamento 1 do `TK-86`):** os itens 1 a 3, o arquivo novo e os dois testes já estão aplicados pela primeira execução (Verificação 1 exit `0`, 2 → `0`, 3 → `2 passed`, 4 → `114 passed`); falta só o item 4. Suíte com eles e sem o item 4: `427 passed, 1 failed` (`tests/test_encerrar.py::test_tf_plano_fecha_status_entrega_tres_secoes_e_linha_do_diario`, `AttributeError` em `_backlog._PISO_C11`). Item 4 ensaiado na árvore e revertido: `tests/test_encerrar.py` `15 passed`, suíte `428 passed`. Varredura de consumidores (`_PISO_C11` sem sufixo em `.claude`, `tests`, `docs`, `*.py`): só `encerrar.py:681`.
- **Testes (novos, em `tests/test_backlog.py`, com `_load_backlog`, `_copiar_fixture` e `capsys`; nome de cada um começado por `test_piso_c11_tsv_`):** 1. TF: cópia de `_FIXTURE_VERDE` em `tmp_path / "repo"`; `backlog.main(["check", "--repo", str(repo)])` → a saída padrão não contém `C-17`. 2. TR: na mesma montagem, `docs/PISO_C11.tsv` escrito com o cabeçalho, a linha `GOVERNANCA.md\t9.9\tteste` e a linha `lixo` → `main` devolve `1`; a saída contém `piso_c11 nomeia entrada órfã` com `9.9`, e `C-17 docs/PISO_C11.tsv:3 — linha fora do esquema`.
- **Não fazer:** não quitar a dívida do piso (tíquete próprio); não mudar `check()`, o `C-11` nem o `C-16`; não declarar o arquivo em `.claude/projecoes.json`; no `encerrar.py`, não tocar nada além da chamada do item 4 (o resto do arquivo é dos cards do `TK-88`); não desfazer os itens 1 a 3 já aplicados.
- **Contingências:** - se a Verificação 1 acusar `C-11` ou `C-17` na árvore → parar e sinalizar `blocked` razão `premissa`, colando as violações (medido no protótipo: nenhuma). - se `_PISO_C11` sem sufixo aparecer num arquivo fora dos Arquivos-alvo → parar e sinalizar `blocked` razão `premissa`, nomeando arquivo e linha (medido na retomada: nenhum além do `encerrar.py`).
- **Handover:** 2026-09-26 · para quem vier depois - **Entregue:** ler_piso_c11(repo) em .claude/tools/backlog.py:906 lê docs/PISO_C11.tsv do repo checado; main do check (backlog.py:2049) e gate de fechar_plano (.claude/tools/encerrar.py:680) usam o piso lido; a constante _PISO_C11 não existe mais - **Contrato:** repo sem docs/PISO_C11.tsv = sem piso e sem C-17; linha malformada do TSV sai C-17 com o número dela; check() inalterado de assinatura e comportamento - **Não refazer:** migração do piso para o TSV e os testes test_piso_c11_tsv_* (tests/test_backlog.py) - **Pendente:** quitar a dívida do piso (entrada GOVERNANCA.md 1.1) é tíquete próprio
- **Notas de execução:** - 2026-09-26 `blocked` — Verificação 5 vermelha: .claude/tools/encerrar.py:681 lê _backlog._PISO_C11 (consumidor fora dos Arquivos-alvo; a suíte do protótipo era 376, hoje 428) → AttributeError em tests/test_encerrar.py::test_tf_plano_fecha_status_entrega_tres_secoes_e_linha_do_diario. V1-V4 verdes. Diff do card aplicado e mantido na árvore (backlog.py, tests/test_backlog.py, docs/PISO_C11.tsv). - 2026-09-26 `ready` — consultor (acionamento 1 do `TK-86`, `PC-1`, `rota=resolve`): premissa procedente, defeito de autoria do card (consumidor da constante fora dos Arquivos-alvo; protótipo medido sobre a suíte de 376, antes do `encerrar.py`). Card emendado: item 4, `encerrar.py` nos Arquivos-alvo, estado da árvore na retomada, Verificações 2/3/5 com o antes de hoje e Verificação 6 nova. Resta só o item 4. - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-86a-o-piso-do-c-11-vem-de-docs-piso-c11-tsv-do-repositorio-checa.md`, veredito ressalva 94%

## Execução

**Consumo:** 20 tool uses, 56.1 k tokens, 208.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 94%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Retomada apos blocked com ref --desde do redespacho: a evidencia mecanica cobre so o delta da retomada (item 4), e os itens 1-3 da primeira execucao so aparecem contra HEAD. Em card com retomada, o despacho do reviewer precisa das duas refs.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Tarefa "O piso do `C-11` vem de `docs/PISO_C11.tsv` do repositório checado". Passo: conferir os gates e preparar o despacho.
Scrum master vai marcar a tarefa "O piso do `C-11` vem de `docs/PISO_C11.tsv` do repositório checado" como blocked, sem RDO.
Agente consultor recebe a tarefa "O piso do `C-11` vem de `docs/PISO_C11.tsv` do repositório checado" e vai triar.
Agente consultor devolveu a tarefa "O piso do `C-11` vem de `docs/PISO_C11.tsv` do repositório checado": rota resolve.
Tarefa "O piso do `C-11` vem de `docs/PISO_C11.tsv` do repositório checado". Passo: conferir os gates e preparar o despacho.
Tarefa "O piso do `C-11` vem de `docs/PISO_C11.tsv` do repositório checado": gates aprovados; vou materializar in-progress e gravar o ponto de partida.
Agente executor recebe a tarefa "O piso do `C-11` vem de `docs/PISO_C11.tsv` do repositório checado" e vai executar: em `.claude/tools/backlog.py`:
Agente executor devolveu a tarefa "O piso do `C-11` vem de `docs/PISO_C11.tsv` do repositório checado": review — sem pendência.
Tarefa "O piso do `C-11` vem de `docs/PISO_C11.tsv` do repositório checado": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O piso do `C-11` vem de `docs/PISO_C11.tsv` do repositório checado" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O piso do `C-11` vem de `docs/PISO_C11.tsv` do repositório checado": ressalva 94%, bloqueante nenhuma.
Scrum master vai fechar a tarefa "O piso do `C-11` vem de `docs/PISO_C11.tsv` do repositório checado" como done: registrar estado, RDO e telemetria.
Tarefa "O piso do `C-11` vem de `docs/PISO_C11.tsv` do repositório checado": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
