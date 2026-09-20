# RDO — DIARIO_DE_OBRAS · TK-56b

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-56b` — Os dois testes sem poder discriminante passam a observar o produto
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** reparar `test_tf_hook_executavel_stdin_utf8_nao_falha_e_preserva_invariancia` (`tests/test_telemetria_hook.py`) e `test_tf_hook_modelo_por_fase_executavel_stdin_utf8_classifica_a_fase` (`tests/test_materializar.py`), que hoje ficam **verdes com o reparo de `stdin` revertido** (medido na revisão do `TK-56a`). Causa: o par negativo é um **stub** escrito à mão — discrimina o stub, não o produto — e o payload acentuado nunca chega ao observável.

**Arquivos-alvo:** - `tests/test_telemetria_hook.py` - `tests/test_materializar.py`

**Verificação:** `python -m pytest tests/test_telemetria_hook.py tests/test_materializar.py` verde, coletando **≥30**; `python -m pytest` verde, sem queda do piso de **230**. O RDO registra a assinatura medida das duas variantes (reparada e revertida) nos dois mundos.

**Pronto quando:** os dois testes satisfazem as quatro condições abaixo, e cada uma é conferível no arquivo de teste: 1. **Mundo hostil construído, não herdado:** os dois mundos são `env` mínimo + `PYTHONIOENCODING=cp1252` (hostil) e `env` mínimo + `PYTHONUTF8=1` (seguro). O mundo "host sem a variável" deixa de ser o hostil — ele mede o host. Medido em 2026-09-20: `PYTHONIOENCODING` prevalece sobre `PYTHONUTF8`. 2. **Canal discriminante:** o payload acentuado chega ao observável. - `modelo_por_fase`: prompt cujo **único** gatilho de classificação é acentuado — `{"prompt": "me dê sua análise disso"}`. Medido: reparado **470 B** nos dois mundos; revertido **2 B** (`{}`) no hostil e 470 B no seguro. O payload entregue hoje (`"faça uma análise arquitetural do módulo"`) dá 470 B em todas as combinações, porque `arquitet` casa sem acento. - `telemetria_hook`: o `stdout` é `b""` e `rc=0` em **todas** as combinações — o canal é o **efeito colateral**. O teste monta uma raiz falsa em `tmp_path` (`.claude/tools/telemetria_hook.py` copiado do arquivo real, `.claude/tools/telemetria.py` copiado, `.claude/estado/tarefa-corrente.json` válido, `docs/`) e usa `agent_transcript_path` apontando para um arquivo de **nome acentuado**. A relocação é obrigatória e não é conveniência: sem ela, `main` apagaria o `.claude/estado/tarefa-corrente.json` **real**. Medido: reparado → estado consumido e TSV com uma linha `2026-09-20 PantonicApp EXA-T55 sonnet 0 0.0 0.0 usage` (separado por TAB); revertido no mundo hostil → estado **sobrevive** e o TSV não é criado. 3. **Par negativo é o produto revertido, nunca um stub:** a variante quebrada nasce de `Path(<arquivo real>).read_text(encoding="utf-8").replace(<bloco do reparo>, "raw = sys.stdin.read()")`, precedida de `assert <bloco do reparo> in fonte` — se o reparo mudar de forma, o teste cai ruidosamente em vez de virar verde vazio. O bloco é o literal de 4 linhas (`try: raw = sys.stdin.buffer.read().decode("utf-8", errors="replace")` / `except AttributeError:` / `raw = sys.stdin.read()`), idêntico nos quatro entrypoints — conferido em 2026-09-20. Os dois `stub = tmp_path / "hook_quebrado.py"` existentes são **removidos**. 4. **Asserções:** (i) produto reparado dá a **mesma** saída observada nos dois mundos; (ii) produto **revertido** dá saídas **diferentes** entre os dois mundos; (iii) o valor acentuado chega íntegro ao observável no mundo hostil. A comparação é de **bytes** — vale porque os dois executáveis imprimem `json.dumps` com `ensure_ascii` default (`stdout` ASCII puro).

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20
- **Não fazer:** não editar `.claude/tools/telemetria_hook.py`, `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` nem nenhum arquivo de produto — o reparo de `stdin` deles está correto e aprovado; não tocar `tests/test_backlog.py` nem `tests/test_ocupacao.py` (matéria do `TK-63`); não editar `docs/plans/P-0739-backlog-instrumento.md` (`DB-23`); não escrever em `.claude/estado/`, `docs/telemetria.tsv` ou qualquer caminho real durante o teste.

## Execução

**Consumo:** 30 tool uses, 120.0 k tokens, 385.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: Vermelho de guarda sem dono na arvore: kit_check check-drift exit 1 por README.md divergir do regenerado; obriga reconciliacao manual a cada revisao desta janela.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
