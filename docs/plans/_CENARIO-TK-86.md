# Cenário do TK-86 — autoridade sobre o tíquete para o que cobre

Teto: 15k tokens. Escrito só pelo `pantonic-consultant`, com `Edit` mínimo, a cada acionamento. Residência do tíquete: `docs/DIARIO_DE_OBRAS.md`, `## TK-86` (tíquete avulso, sem modelo de domínio: nenhum dossiê `Ato de modelo` cabe aqui). Origem: `DEB-13` do `P-0751` (acionamento 8, `docs/plans/_CENARIO-P-0751.md`), achado `AE-6` do fechamento daquele plano.

## Decisões vivas

- Herdada do `DEB-13`: o piso do `C-11` é dado do corpus — sai da constante `_PISO_C11` do `backlog.py` para `docs/PISO_C11.tsv` do repositório checado; arquivo ausente = sem piso, sem `C-17`. Texto no `## TK-86`, parágrafo *O que decide*.
- `PC-1` (acionamento 1, gatilho 1, `TK-86a` `blocked` `premissa`): `rota=resolve`, sem `estrategico=`. Premissa procedente, defeito de autoria do card: o `fechar_plano` de `.claude/tools/encerrar.py` (linha 681, nascido no `TK-88` depois do protótipo, medido sobre a suíte de 376) é o segundo consumidor de `_backlog._PISO_C11` e ficou fora dos Arquivos-alvo. Reparo: item 4 no Objetivo do `TK-86a` — o gate do `fechar_plano` lê o piso por `_backlog.ler_piso_c11(repo)` e soma as violações dele antes das do `check(...)`, na mesma ordem do `main`. O `DEB-7`/`DEB-13` ("o `main` liga o piso") estende-se ao `fechar_plano`. Descartado: restaurar a constante como alias (reintroduz o piso do hub em todo repositório que fecha plano).
- `PC-2` (acionamento 2, gatilho 2, `AE-77`): `rota=resolve`. Nenhum card vivo cobre (`TK-88b`..`TK-88d` mexem em `encerrar.py`/`progresso_hook.py`/`rdo.py`; o card do `P-0752` que fixou `<P-n>` já é `done`). Abre `TK-92`/`TK-92a`: `caminhos.destino_medida(raiz, plano_path, tarefa)` é a regra única, usada pelo `review_evidence.py` e pelo `card_check.py --gravar` sem caminho; a doutrina (executor 5a, scrum-master Passo 5) manda `--gravar` sem caminho. `docs/RDO/evidencia/P-0751-TK-86a-medida.json` fica com o nome: laudo e evidência do `TK-86a` (fechados) o citam. Descartado: só emendar a prosa.
- `PC-3` (acionamento 2, gatilho 2, `AE-78`): `rota=resolve`. Abre `TK-93`/`TK-93a`: `review_evidence.py --capturar-ref` (commit da árvore inteira por índice temporário, pai `HEAD`), `--desde` julga pelo conteúdo o não rastreado presente no `<ref>`; Passo 4 do `scrum-master` captura pela flag e o redespacho reusa o `<ref>` do primeiro despacho. Descartado: recorte pelas âncoras do card; dois `--desde`.
- Medido em 2026-09-26 (acionamento 2), protótipos em cópias da árvore, apagadas: `TK-92a` suíte `428` → `430 passed`; `TK-93a` sobre o `TK-92a`, `430` → `432 passed`, evidência do `TK-86a` com só `encerrar.py` nos tocados e o hunk `@@ -679,6 +679,7 @@`; `check-drift` OK nos dois. `card_check` exit `0` nos dois cards, mundo antes na árvore e depois nos protótipos; `backlog.py check` OK.
- Medido na árvore em 2026-09-26 (acionamento 1): itens 1 a 3, o arquivo novo e os dois testes do `TK-86a` já aplicados pela primeira execução e mantidos; suíte `427 passed, 1 failed`. Item 4 ensaiado na árvore e revertido: `tests/test_encerrar.py` `15 passed`, suíte `428 passed`. Varredura: `_PISO_C11` sem sufixo só em `encerrar.py:681`. `card_check` exit `0` no `TK-86a` emendado; `backlog.py check` OK; `status TK-86a ready`; `next` → `TK-86a`.

## Fila

- `TK-86a` `done` (ressalva 94, `registro` parcial). Nada do `TK-86` na fila; o fechamento do tíquete (`ready 1/1` no índice) é ato do condutor.
- Abertos neste acionamento, fora do tíquete: `TK-92a` (`ready`) → `TK-93a` (`ready`, `Depende de: TK-92a`). `next` medido: `TK-87a`.

## Achados abertos

- Nenhum. `AE-77` e `AE-78` (fechamento do `TK-86a`) saíram com rota aos tíquetes `TK-92` e `TK-93`; a linha **Rota:** de cada um foi reescrita.

## Matéria inconclusiva

- Insumo de régua, sem card: card que remove símbolo de módulo varre os consumidores na emissão e remede a suíte quando o protótipo envelhece (o `TK-87a` também traz "suíte `376 passed`" do mesmo protótipo; registro histórico, não reescrito).
- `encerrar.py` é tocado também por `TK-88b`..`TK-88d`: o item 4 do `TK-86a` ancora pela chamada, não pela linha; não ensaiado sobre o `encerrar.py` depois do `TK-88b`.
- O `<ref>` do primeiro despacho não tem residência durável: se o contexto do condutor for trocado entre despacho e redespacho, ele se perde (o `TK-93a` só manda reusá-lo).
- `review_evidence.py` é tocado por `TK-89a`, `TK-92a` e `TK-93a` em funções diferentes; ensaiados `TK-92a` → `TK-93a`, não sobre o `TK-89a`.

## Acionamentos

1. 2026-09-26 · `TK-86a` `blocked` `premissa` (V5 vermelha, `encerrar.py:681`) · gatilho 1 · `rota=resolve` · `PC-1`; card emendado (item 4, `encerrar.py` nos alvos, estado na retomada, V2/V3/V5 com o antes de hoje, V6 nova), `ready`; não estratégico.
2. 2026-09-26 · laudo do `TK-86a` (ressalva 94) com `AE-77`, `AE-78` de rota tíquete · gatilho 2 · `rota=resolve` · `PC-2`, `PC-3`; abertos `TK-92a` e `TK-93a` (`ready`, `card_check` 0), linhas **Rota:** reescritas; não estratégico.
