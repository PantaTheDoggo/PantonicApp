# RDO — DIARIO_DE_OBRAS · TK-65e

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-65e` — O ramo concatenado do aviso de `diretiva` ganha teste
**Modelo:** Sonnet · **Classe:** mecanica
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** trancar por teste o ramo em que `transacionar_diretiva` devolve, na mesma `mensagem`, o aviso de id descartado **e** o aviso de `_regenerar_bloco_fila`, unidos por quebra de linha.

**Arquivos-alvo:** - `tests/test_backlog.py` (junto de `test_tf_diretiva_acusa_id_descartado_na_cauda`)

**Verificação:** um teste sobre cópia da fixture `next_tk90` **sem** `_inserir_bloco_gerado` (sem o marcador `<!-- fila:gerada -->`, o que faz `_regenerar_bloco_fila` avisar), com a diretiva ``Priorize `TK-90a` — e depois `TK-90b`, `FFO-T1` ``: `exit_code == 0` e `mensagem` com duas linhas — a 1ª nomeia `TK-90b` e `FFO-T1`, a 2ª é o aviso do bloco gerado. `python -m pytest tests/test_backlog.py` verde.

**Pronto quando:** o teste existe, passa sobre o `backlog.py` vigente e falharia se a concatenação deixasse cair qualquer um dos dois avisos.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-24 — aberto pelo loop no fechamento do `TK-65c` (laudo aprovado 100%, achado de processo: o `Pronto quando` do `TK-65c` exige a concatenação e nenhum teste a tranca).
- **Não fazer:** não tocar `.claude/tools/backlog.py` — a entrega do `TK-65c` já produz as duas linhas (exercitado ponta a ponta na revisão dele); falta só a trava.

## Execução

**Consumo:** 9 tool uses, 57.3 k tokens, 41.6 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

Discriminacao provada por mutacao em memoria: _regenerar_bloco_fila -> None, _ids_descartados_diretiva -> [], join por ' | ' -> teste FALHA nos tres; vigente PASSA. Achado roteado: nao rastreados pre-despacho no dossie -> TK-55.

## Fechamento

**Desdobramento:** aprovado
