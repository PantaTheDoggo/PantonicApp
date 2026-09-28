# RDO — P-0751 · EBK-T3

**Plano:** `docs/plans/P-0751-esgotar-backlog.md`
**Tarefa:** `EBK-T3` — O `next` projeta o colchete do cabeçalho inteiro
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** a primeira linha de `backlog.py next` reproduz o colchete do cabeçalho do card como ele está no plano — com ` + dono` e ` · esforço <e>` quando o cabeçalho os tem.

**Arquivos-alvo:** - `.claude/tools/backlog.py` - `tests/test_backlog.py`

**Verificação:** 1. `python -m pytest tests/test_backlog.py -q` → verde, com o par acima. 2. `python -m pytest tests/test_progresso_hook.py -q` → verde (o gancho do painel lê essa linha). 3. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho mais os testes novos.

**Pronto quando:** o colchete do `next` é o do cabeçalho, provado pelo par.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Origem:** card `TK-55c` do diário de obras, seção `## TK-55`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-3` - OP-3: O card que faz a escolha da próxima tarefa mostrar o cabeçalho inteiro do card sai de pronto para concluído, sobre o backlog que a operação anterior deixou. - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Caso medido (2026-09-25):** o card `TK-68a` tinha o cabeçalho `[Sonnet · esforço low · classe redacao]` e o `next` imprimiu `[Sonnet · classe redacao]`; em 2026-09-20 o `TK-58a` perdeu o ` + dono`, que é a marca de tarefa não delegável. A linha é montada em `backlog.py:1250` como `[{item.modelo} · classe {item.classe}]`.
- **Testes:** TF par sobre cópia da fixture `verde` — card `[Sonnet · classe mecanica]` → primeira linha termina em `[Sonnet · classe mecanica]`; card `[Opus + dono · esforço high · classe investigacao]` → termina em `[Opus + dono · esforço high · classe investigacao]`.
- **Não fazer:** não mudar o formato do resto da saída de `next`; não tocar `progresso_hook.py`.

## Execução

**Consumo:** 38 tool uses, 88.8 k tokens, 367.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
