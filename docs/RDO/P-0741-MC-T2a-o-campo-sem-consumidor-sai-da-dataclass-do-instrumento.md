# RDO — P-0741 · MC-T2a

**Plano:** `docs/plans/P-0741-modelo-conceitual.md`
**Tarefa:** `MC-T2a` — O campo sem consumidor sai da dataclass do instrumento
**Modelo:** Sonnet · **Classe:** mecanica
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `.claude/tools/modelo.py` não declara nem atribui o campo `linha` da dataclass `Oracao`, e a suíte segue verde sem reduzir o total.

**Arquivos-alvo:** - `.claude/tools/modelo.py` — a dataclass `Oracao` e a construção dela em `_extrair_oracoes`

**Verificação:** 1. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/tools/modelo.py -Pattern 'linha: int' -SimpleMatch | Measure-Object).Count" ``` → **0**. **Medido antes: 1**. 2. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/tools/modelo.py -Pattern 'linha=offset' -SimpleMatch | Measure-Object).Count" ``` → **0**. **Medido antes: 1**. 3. ``` python -m pytest tests -q -p no:cacheprovider ``` → **exit 0**. **Medido antes: exit 0**. Piso: total coletado ≥ 245 (`I-2`). 4. ``` python .claude/tools/modelo.py check --plano docs/plans/P-0741-modelo-conceitual.md ``` → **exit 0**. **Medido antes: exit 0**. (invariância: a limpeza não quebra o corpus real.) 5. ``` pwsh -NoProfile -Command "python .claude/tools/review_evidence.py --plano docs/plans/P-0741-modelo-conceitual.md --tarefa MC-T2a --desde HEAD --atribuir | Select-String -Pattern '0 sem atribuicao' -SimpleMatch | Measure-Object | Select-Object -ExpandProperty Count" ``` → **1**. **Medido antes: 1**. (invariância de escopo, `DMC-22`.)

**Pronto quando:** as cinco linhas acima devolvem o esperado.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20
- **Fundamento:** `AE-13` item 3 e a decisão `DMC-26` do `ESC-3`; a §6 deste plano, que congela a forma de saída dos dois verbos e não pede posição de linha em lugar nenhum.
- **Depende de:** `MC-T2`
- **Oração do modelo:** `M-17` - M-17: Um instrumento confere o modelo: toda oração tem tarefa, toda tarefa tem oração, todo estado é válido, nenhuma oração está confirmada com tarefa que ainda não foi entregue para revisão, e nenhuma oração carrega nome de arquivo ou literal técnico.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/`; só `modelo.py`. Nenhum teste muda de expectativa — se algum precisar mudar, a premissa caiu (contingência 1).
- **Contratos/classes:** `Oracao` passa a ter `id`, `texto`, `estado`, `estado_data`, `estado_ref` e `tarefas` — e nada mais.
- **Passos:** 1. Apagar a linha `linha: int = 0` da dataclass `Oracao` (`.claude/tools/modelo.py:61` em 2026-09-20). 2. Apagar o argumento `linha=offset + i + 1` da construção de `Oracao` em `_extrair_oracoes` (`.claude/tools/modelo.py:150` em 2026-09-20), preservando os demais argumentos. 3. Rodar a suíte inteira e o `check` sobre o corpus real.
- **Restrições desta tarefa:** nenhum outro símbolo de `modelo.py` muda; nenhum arquivo de teste muda; `backlog.py`, `review_evidence.py` e `card_check.py` intocados (`I-3`).
- **Não fazer:** não aproveitar a passagem para refatorar `modelo.py`; não criar consumidor para o campo — a `DMC-26` decidiu o contrário, e inventar leitor para justificar símbolo é o avesso do achado.
- **Contingências:** 1. se a busca por leitura de `.linha` encontrar consumidor em qualquer arquivo do repositório → a premissa da `DMC-26` caiu: parar e sinalizar `blocked` razão `premissa`, com a linha encontrada na razão.
- **Testes:** `TR`: `tests/test_modelo.py` e a suíte inteira seguem verdes, sem redução de total (`I-2`; piso medido em 245 no fechamento da `MC-T2`).
- **Fora do escopo desta tarefa:** qualquer outra limpeza de `modelo.py`; os papéis (`MC-T3`).

## Execução

**Consumo:** 10 tool uses, 47.0 k tokens, 92.4 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
