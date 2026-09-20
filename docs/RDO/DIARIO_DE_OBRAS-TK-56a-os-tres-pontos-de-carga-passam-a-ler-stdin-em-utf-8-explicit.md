# RDO — DIARIO_DE_OBRAS · TK-56a

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-56a` — Os três pontos de carga passam a ler `stdin` em UTF-8 explícito
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** aplicar as três cláusulas da `DB-53` do `P-0739` a `.claude/tools/ocupacao.py:141`, `.claude/tools/telemetria_hook.py:213` e `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py:101`, cada um com teste por subprocesso e ambiente fixo. O terceiro é global: o reparo dele vale para todos os projetos.

**Arquivos-alvo:** - `.claude/tools/ocupacao.py` - `.claude/tools/telemetria_hook.py` - `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` - `tests/test_ocupacao.py` - `tests/test_telemetria_hook.py` - `tests/test_materializar.py`

**Verificação:** `python -m pytest tests/test_ocupacao.py tests/test_telemetria_hook.py tests/test_materializar.py` verde, e a bateria completa `python -m pytest` sem queda de piso. Cada um dos três executáveis rodado por `subprocess.run` com `env=` mínimo, nos dois mundos da variável `PYTHONUTF8`, devolvendo a **mesma** saída.

**Pronto quando:** as três cláusulas da `DB-53` estão aplicadas aos três pontos de carga — (1) o teste roda o processo com entrada em bytes; (2) fixa `env=` explícito de dicionário mínimo, nunca copiado de `os.environ`; (3) afirma a invariância do executável correto e a divergência do quebrado —, e o terceiro arquivo, que é hook **global**, passa a ler `stdin` em UTF-8 explícito para todos os projetos.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20
- **Depende de:** `TK-57a`
- **Razão da dependência (`DB-50` do `P-0739`; a linha acima só carrega IDs):** a regra de teste tem de estar completa antes de ser propagada, senão multiplica por três um teste que não discrimina.

## Execução

**Consumo:** 51 tool uses, 99.1 k tokens, 379.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: Emendar a clausula 3 da DB-53 (P-0739) e reparar os dois testes sem poder discriminante (telemetria_hook, modelo_por_fase): hoje eles ficam verdes com o reparo de stdin revertido.

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
