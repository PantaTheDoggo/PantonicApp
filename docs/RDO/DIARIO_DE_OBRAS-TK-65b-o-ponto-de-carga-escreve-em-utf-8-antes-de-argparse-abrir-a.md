# RDO — DIARIO_DE_OBRAS · TK-65b

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-65b` — O ponto de carga escreve em utf-8 antes de argparse abrir a boca
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** mover a reconfiguração de encoding de `main()` para antes de `parse_args`, de modo que `--help` e toda mensagem de erro de argparse — que imprimem o `usage` com `→` — saiam sem `UnicodeEncodeError` em console cp1252.

**Arquivos-alvo:** - `.claude/tools/backlog.py` (`main()`, hoje: `reconfigure` em `:1415`, `parse_args` em `:1411`) - `tests/test_backlog.py`

**Verificação:** par presença-ausência por subprocesso com o ambiente hostil explícito (`PYTHONIOENCODING` vazio, `-X utf8=0`): `backlog.py --help` sai **exit 0** e imprime o `usage`; hoje o mesmo comando sai em traceback. `python -m pytest tests/test_backlog.py` verde.

**Pronto quando:** em `main()` a reconfiguração de encoding precede `parse_args`; sob o ambiente hostil explícito, `backlog.py --help` sai exit 0 com o `usage` inteiro, `→` incluído; o teste é par presença-ausência por subprocesso, falhando sobre o `main()` anterior e passando sobre o novo. (Campo acrescido pelo consultor, acionamento 1 do `TK-65`, `CT65-1`: o `review_evidence.py` recusava o card sem ele; o critério é o da Verificação, sem escopo novo.)

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-24
- **Caso medido que motivou (2026-09-20):** `PYTHONIOENCODING= python -X utf8=0 .claude/tools/backlog.py --help` → `UnicodeEncodeError: 'charmap' codec can't encode character '→' in position 611`. É a metade de **escrita** do defeito que o `TK-56a` fechou na leitura.
- **Não fazer:** não trocar o `→` do texto de ajuda por ASCII — o defeito é do ponto de carga, não do texto; não tocar os outros pontos de carga já fechados pelo `TK-56a`.

## Execução

**Consumo:** 27 tool uses, 75.0 k tokens, 140.4 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

Verificacao reproduzida nos dois mundos sob o ambiente hostil exato do card: arvore revisada '--help' exit 0 com usage e U+2192; instantaneo 2362c3f exit 1 com UnicodeEncodeError. O par TF/TR tambem tranca o 'Nao fazer': se o U+2192 virasse ASCII, o TR cairia. Achados de processo roteados: nao rastreados anteriores ao despacho no dossie -> TK-55 (caso ja registrado do P-0748); ancoras envelhecidas e Pronto quando ausente -> sem acao (CT65-1 acresceu o campo; ancoras re-derivadas no despacho).

## Fechamento

**Desdobramento:** aprovado
