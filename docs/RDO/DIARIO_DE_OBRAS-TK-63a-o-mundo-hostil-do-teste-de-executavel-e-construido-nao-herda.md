# RDO — DIARIO_DE_OBRAS · TK-63a

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-63a` — O mundo hostil do teste de executável é construído, não herdado do host
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** os dois sítios que discriminam **por acidente de plataforma** — o mundo "sem `PYTHONUTF8`" só é hostil porque este host é Windows-cp1252 — passam a usar o mundo hostil **construído**. Em host que exporte `PYTHONUTF8=1`, ou em plataforma cujo default seja UTF-8, os dois param de discriminar hoje.

**Arquivos-alvo:** - `tests/test_backlog.py` - `tests/test_ocupacao.py`

**Verificação:** `python -m pytest tests/test_backlog.py tests/test_ocupacao.py` verde, coletando **>=91**; `python -m pytest` verde, sem queda do piso de **238**. Nenhum teste lê `docs/DIARIO_DE_OBRAS.md`, `docs/plans/*` ou `.claude/tools/backlog.py` **no lugar**.

**Pronto quando:** 1. **Mundo hostil construído.** Os dois mundos são `env` mínimo + `PYTHONIOENCODING=cp1252` (hostil) e `env` mínimo + `PYTHONUTF8=1` (seguro). O mundo "host sem a variável" deixa de ser o hostil — ele mede o host. Medido: `PYTHONIOENCODING` prevalece sobre `PYTHONUTF8`, então o mundo hostil é hostil até em host que exporte a variável. 2. **`backlog_hook`: raiz relocada, sem shim.** O teste monta em `tmp_path` uma raiz falsa a partir de `tests/fixtures/backlog/next_tk90/` e copia para `<raiz>/.claude/tools/` **os dois** arquivos reais — `backlog_hook.py` e `backlog.py` — com `shutil.copy2`. Isso basta: o hook resolve `backlog.py` como irmão de `__file__` e a raiz a partir do `backlog.py`, de modo que todo o acoplamento se fecha **dentro** da raiz falsa. **Nenhum shim, nenhum `exec(compile(...))`, nenhum `__file__` apontando para a árvore viva.** Mesma técnica do `telemetria_hook` no `TK-56b` (aprovado 100%). 3. **Par negativo é o produto revertido**, materializado por substituição textual sobre a fonte real (`assert <bloco do reparo> in fonte` antes), copiado para dentro da raiz falsa como o positivo. O `stub = tmp_path / "hook_quebrado.py"` **sai** dos testes que ainda o têm. 4. **`ocupacao.py`: cópia simples em `tmp_path`** — não tem acoplamento por `__file__`; medido. 5. **As asserções afirmam relação, nunca magnitude.** Três, e nenhuma envelhece: (i) **invariância** — o produto correto dá a mesma saída nos dois mundos; (ii) **divergência** — o produto revertido dá saídas diferentes entre eles; (iii) **não-vazio** — a saída do produto correto no mundo hostil é `!= b""`. **Nenhum `assert` cita número de bytes.** 6. **A magnitude vive no docstring, com data e mundo, como registro — não como aceite.** Medidas de 2026-09-20, a reproduzir: `backlog_hook` em raiz relocada sobre `next_tk90` → **737 B** idênticos nos quatro mundos, revertido **0 B** no hostil; `ocupacao` → **323 B** idênticos nos quatro mundos, revertido **335 B** no hostil.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20 — **reescrito** após devolução `blocked` razão `premissa`, por conduta correta do executor: o card prescrevia shim com `__file__` preservado, e preservar `__file__` faz o TF ler o `backlog.py` e o **diário reais**, acoplando o teste a estado vivo escrito por outra janela de orquestração. A prescrição do shim **cai**; entra raiz relocada.
- **Não fazer:** não ler o diário real, nenhum arquivo de `docs/plans/` e nenhum estado vivo em teste — foi o acoplamento que devolveu este card; não editar `.claude/tools/backlog_hook.py`, `.claude/tools/backlog.py` nem `.claude/tools/ocupacao.py` (os reparos estão corretos e aprovados); não reabrir `TK-57a` nem `TK-56a`; não tocar `docs/plans/P-0741-modelo-conceitual.md`.

## Execução

**Consumo:** 30 tool uses, 97.8 k tokens, 286.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
