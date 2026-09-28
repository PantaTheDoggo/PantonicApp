# Cenário do P-0749 — consultor

Plano: `docs/plans/P-0749-saneamento-artefatos.md` (legado, não rastreado). Modelo `## 1` versão 1, vigente, 6 operações; nenhum dossiê de emenda pendente.

## Decisões vivas (do consultor)

- `DSA-18` — função de `caminhos.py` nasce com o primeiro chamador de produção: `pasta_do_plano` na `SAN-T1` (chamada por `backlog._parse_plano`), `formatar_id` (+ `estado_tsv`) na `SAN-T2`, `pasta_por_id` (+ `destino_*`) na `SAN-T3`. Os blocos das T2/T3 entram "imediatamente antes de `def main(`".
- `DSA-19` — `caminhos.py` tem CLI `main` (lista `<id><TAB><caminho>`) e guarda `__main__`: é o que o torna semente do `dead_code.py`; `I-6` intacto (nada em `.claude/checks`).
- `DSA-20` — `I-2` se mede comparando, na mesma árvore e no mesmo instante, cópia de referência em `$env:TEMP` (`san-t1a-ref`, `san-t2-ref`) × código editado; nunca saída gravada.
- Códigos novos de `check` são `C-13`/`C-14` (`C-12` já é do `TK-65`); `DSA-12`, `SAN-T2` e `SAN-T4` alinhados.
- `DSA-21` — flag explícita vence também no `INDEX.md` (`close` regenera sempre que grava no legado); corretivo `SAN-T3a` (`OP-3`, na lista `tarefas:` da operação) antes da `SAN-T4`, que passou a depender dele.
- `DSA-22` — `C-10` só com plano presente: sem plano, todo contador vale (`P-0` inclusive); com plano, regra e mensagem inalteradas (TF 12 segue). Corretivo `SAN-T2a` (`OP-2`, na lista `tarefas:`) antes da `SAN-T5`.
- `DSA-23` — glossário do `README.md`: "contador monotônico do repositório" (troca `M5`). Corretivo `SAN-T6a` (`OP-6`, na lista `tarefas:`) depois da `SAN-T6`; veredito do dono sobre `M1`..`M5` é gate do marco, sobe no relatório de encerramento, fora do *Pronto quando*.
- `DSA-24` — o `README.md` inteiro deixa de dizer o contador "global": §14 → "contador sequencial do repositório" (troca `M6`). Corretivo `SAN-T6b` (`OP-6`, na lista `tarefas:`) depois da `SAN-T6a`; `M6` sobe com `M1`..`M5` no relatório de encerramento. `contador sequencial` sem "global" (`README.md:624`, `GOVERNANCA.md:867`) fica.

## Fila

`SAN-T1`..`SAN-T6a` `done` (9/10) → `SAN-T6b` `ready` (retentativas 0), última. `backlog.py check` exit 0, `next` aponta `SAN-T6b`, `modelo.py check --plano` OK 10 tarefas (medido, acionamento 5). O dossiê do `next` da última tarefa arrasta `## 6`..`## 9` (truncado no teto DB-7) — já era assim na `SAN-T6`.
Totais da suíte: 353 (T2a, medido). `M5` medido numa cópia (`check-readme -Root`, apagada): exit 0, contagens `0 / 1`. `dead_code` exit 0. Filtros `-k tf_san` contam TF de cards anteriores (`AE-2`): `test_backlog.py` 7 → 8. Próximo TF livre: `san_21`.

## Achados

- `AE-1` — absorvido (acionamento 1). Reparo medido numa cópia da árvore: Verificações 1-8 da `SAN-T1` conferem; TF 17/18 falham sem o reparo.
- `AE-1` (c) — fora do plano: `review_evidence.py` não mostra os arquivos não rastreados de antes do despacho (`git stash create`); recorrência já registrada no `TK-55`. Espere o mesmo ruído no laudo do redespacho (os 12 arquivos não rastreados de antes; `progresso_hook.py` inteiro, sem diff).

- `AE-2` — sem ação (número esperado do filtro no card).
- `AE-3` — absorvido (acionamento 2): ressalva (TF 15 amputou a cauda do teste `TK-62a`), (a) índice com `--rdo-dir` e (b) help da CLI → `SAN-T3a`; (c) → fora do plano, terceira recorrência do `TK-55`/`TK-78c`.
- `AE-4` — absorvido (acionamento 3): `C-10` falso no estado de bootstrap → defeito da `SAN-T2` (`OP-2`), `DSA-22` + `SAN-T2a`.
- `AE-5` — absorvido (acionamento 4): (b) glossário "global" → `DSA-23` + `SAN-T6a`; ressalva (veredito manual de `M1`..`M4`) → relatório de encerramento, sem card; (a) e (c) → `TK-72` §9, Pacotes 11 e 12, já aplicados ao card `SAN-T6a`.
- `AE-6` — absorvido (acionamento 5): §14 "contador sequencial global" → `DSA-24` + `SAN-T6b`; `M6` medido numa cópia (`check-readme -Root`, apagada): exit 0, contagens `0 / 0 / 1`. Varredura do loop: último resíduo da família no `README.md`.

## Inconclusivo

- A instância poluída (descartada) editou o plano antes de o reparo ser validado. Esta instância conferiu e manteve tudo: `DSA-18`..`20`, reescrita da `SAN-T1`, blocos movidos para as T2/T3, `C-13`/`C-14`, "Medido antes" com 339. Tirou só a nota de execução `ready` que ela tinha escrito.

## Acionamentos

1. 2026-09-25 · `SAN-T1` · A6a (reprovado 68, guardas) · `rota=resolve` · reexecução `A1` em contexto limpo.
2. 2026-09-25 · `SAN-T3` · A8 (ressalva 91, laudo `AE-3`) · `rota=resolve` · corretivo `SAN-T3a` antes da `SAN-T4`.
3. 2026-09-25 · `SAN-T4` · A9 (aprovado 100, achado `AE-4`) · `rota=resolve` · corretivo `SAN-T2a` antes da `SAN-T5`.
4. 2026-09-25 · `SAN-T6` · A8 (ressalva 88, laudo `AE-5`) · `rota=resolve` · corretivo `SAN-T6a` depois da `SAN-T6`; (a)/(c) ao `TK-72`.
5. 2026-09-25 · `SAN-T6a` · A9 (aprovado 100, achado `AE-6`) · `rota=resolve` · corretivo `SAN-T6b` depois da `SAN-T6a`.
