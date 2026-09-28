# RDO — P-0751 · EBK-T4

**Plano:** `docs/plans/P-0751-esgotar-backlog.md`
**Tarefa:** `EBK-T4` — `rdo.py close` recusa tarefa que não está `done`
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `rdo.py close` sai com código diferente de `0`, sem escrever arquivo, quando o status corrente da tarefa não é `done` — lido na mesma fonte que o `backlog.py status` escreve: bullet `- **Status:**` no plano legado e no diário, linha da tarefa em `estado.tsv` no plano em pasta. A mensagem nomeia a tarefa, o status encontrado e o exigido. Status ausente (card sem o bullet, tarefa sem linha no `estado.tsv`, `estado.tsv` inexistente) não é `done`: recusa, e a mensagem diz `ausente` (`DEB-8`).

**Arquivos-alvo:** - `.claude/tools/rdo.py` - `tests/test_rdo.py` — e só ele do lado dos testes: nenhum arquivo sob `tests/fixtures/` e nenhum plano sob `docs/plans/` muda (`DEB-8`)

**Verificação:** 1. `python -m pytest tests/test_rdo.py -q` → verde, com os pares acima. 2. `(Select-String -Path .claude/tools/rdo.py -SimpleMatch 'de lugar nenhum').Count` — antes `1`, depois `0`. 3. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho mais os testes novos.

**Pronto quando:** o `close` só escreve RDO de tarefa `done`, provado pelos dois pares, e a docstring do módulo diz que ele lê o status.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Origem:** card `TK-55b` do diário de obras, seção `## TK-55`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-4` - OP-4: O card que faz o fechamento de tarefa recusar a que não foi concluída sai de pronto para concluído, sobre o backlog que a operação anterior deixou. - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Montagem dos testes existentes:** `DEB-8`, medida pelo consultor numa cópia da árvore com a regra mínima no `close` — sem a montagem, 17 dos 57 testes do `test_rdo.py` caem; com ela, `57 passed` e suíte `367 passed`. - `_argv_close` deixa de apontar `--plano` para `_PLANO_REAL`: aponta uma cópia dele em `tmp_path / "plano-real" / _PLANO_REAL.name` (subpasta, porque vários testes contam os `.md` de `tmp_path` como RDO), com a linha `` - **Status:** `done` · 2026-09-25 `` inserida logo abaixo de cada linha que começa por `### T7 — ` e por `### T8a — `; o plano real não é tocado. - `_escrever_plano_sintetico` ganha parâmetro opcional `status` (padrão sem linha de status, e os testes de `extrair_dossie` seguem como estão); o teste do cabeçalho histórico com teto que chama `close` passa `status="done"`. - Os dois testes de `close` sobre plano em pasta (`test_tf_san_13_…` e `test_tr_san_19_…`) gravam `plano.parent / "estado.tsv"` com o cabeçalho de `caminhos.CABECALHO_ESTADO` e a linha `T1`, `tarefa`, `done`, `-`, `2026-09-25`, `-`, separada por tabulação. - Em `test_tf_close_gera_rdo_completo_a_partir_do_plano_pacote_e_consumo`, a asserção de que a palavra `status` não aparece no RDO passa a excluir a linha transcrita do plano: `assert "status" not in conteudo.replace("- **Status:** `done` · 2026-09-25", "").lower()`. O RDO transcreve o bullet de status do card como campo extra, e isso já acontece em produção: o RDO do `EBK-T3` em `docs/RDO/` traz a linha. A intenção da asserção fica de pé: o `close` não produz status por conta própria.
- **Caso medido que motivou (2026-09-20):** o `close` escreveu RDO para uma tarefa `in-progress` um comando depois de o `backlog.py status` ter recusado `in-progress → done`. Hoje `rdo.py:14` declara: *"`close` não tem `--status` e não lê `status` de lugar nenhum"*.
- **Testes:** TF par — tarefa `in-progress` → exit diferente de `0` e nenhum RDO no destino; a mesma tarefa `done` → exit `0` e o RDO escrito. Um par no plano legado e um no plano em pasta.
- **Não fazer:** não acrescentar flag `--status`; não mudar o pacote de campos do `close`; não tocar `backlog.py`.
- **Contingências:** - se, com a montagem acima, outro teste existente de `close` além dos 17 medidos cair, ou outra asserção deles além da da palavra `status` mudar de resultado → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Notas de execução:** - 2026-09-25 `ready` — DEB-8: status ausente recusa; testes de close sobre copia do plano real em tmp_path; montagem medida (367 passed)

## Execução

**Consumo:** 58 tool uses, 130.0 k tokens, 461.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
