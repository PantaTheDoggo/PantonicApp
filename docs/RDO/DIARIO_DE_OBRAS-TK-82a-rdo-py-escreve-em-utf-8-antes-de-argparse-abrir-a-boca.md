# RDO — DIARIO_DE_OBRAS · TK-82a

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-82a` — `rdo.py` escreve em UTF-8 antes de argparse abrir a boca
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `main()` de `.claude/tools/rdo.py` reconfigura `sys.stdout` e `sys.stderr` para UTF-8 antes de `parser.parse_args(argv)`, pela mesma forma de `.claude/tools/review_evidence.py` (`_forcar_utf8`: `reconfigure(encoding="utf-8", errors="replace")` quando o stream tem `reconfigure`), de modo que `--help`, mensagens de erro e as linhas `rdo: …` saiam em UTF-8 no pipe do Windows.

**Arquivos-alvo:** - `.claude/tools/rdo.py` - `tests/test_rdo.py`

**Verificação:** 1. `python -m pytest tests/test_rdo.py -q` → verde, com o teste novo. 2. `python -m pytest tests -q` → nenhuma falha; total = o da referência do despacho mais 1.

**Pronto quando:** em `main()` a reconfiguração precede `parse_args`; sob o ambiente hostil explícito, `rdo.py close --help` redirecionado sai em UTF-8; o teste é par presença-ausência por subprocesso.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Caso medido que motivou (2026-09-25, re-medido no ato da autoria):** `PYTHONIOENCODING= python -X utf8=0 .claude/tools/rdo.py close --help > h.tmp` → exit `0`, e os bytes de `h.tmp` contêm `Diretório` em cp1252 (`b"Diret\xf3rio"`) e **não** em UTF-8.
- **Testes (novo, em `tests/test_rdo.py`):** TF par presença-ausência por subprocesso com ambiente hostil explícito (`PYTHONIOENCODING` vazio no `env`, `-X utf8=0`, `stdout=subprocess.PIPE`): `rdo.py close --help` sai exit `0` e os bytes da saída contêm `"Diretório".encode("utf-8")` e não contêm `"Diretório".encode("cp1252")`. Sobre o `main()` anterior o teste falha no Windows (medido acima).
- **Não fazer:** não importar `review_evidence.py` de dentro do `rdo.py` (copiar a função de 4 linhas, como os demais pontos de carga); não trocar acentos do texto de ajuda por ASCII.

## Execução

**Consumo:** 21 tool uses, 59.4 k tokens, 160.2 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
