# RDO — P-0753 · AF-T1

# Humano

Tarefa "Com `--desde`, o resumo de diferenças do dossiê sai do recorte dos tocados" concluída em 2026-09-27.
O dossiê de evidência passa a resumir as diferenças só pelos arquivos que a tarefa tocou desde o despacho, sem o trabalho em andamento de fora.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria de encerramento do estágio 1: as dezoito recomendações e os dois tíquetes do consultor": 1/21 tarefas concluídas; próxima: "O relatório de auditoria de quem conduz entra no balde de registro da orquestração".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achado registrado no plano, com rota: 1 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/plans/P-0753-auditoria-estagio-1/plano.md`
**Tarefa:** `AF-T1` — Com `--desde`, o resumo de diferenças do dossiê sai do recorte dos tocados
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O instrumento de evidência passa a resumir as diferenças da entrega pelo mesmo recorte da lista de arquivos tocados, sem o trabalho em andamento de fora da tarefa.

**Arquivos-alvo:** - `.claude/tools/review_evidence.py` - `tests/test_review_evidence.py`

**Verificação:** 1. `python -m pytest tests/test_review_evidence.py -q -k "diff_stat_desde"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado) 2. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava) 3. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)

**Pronto quando:** - dossiê de evidência.recorte do resumo de diferenças — com recorte informado, o resumo lista exatamente os arquivos tocados desde o recorte, os novos inclusive; sem recorte, nada muda — Verificação 1 (e a suíte segue verde, Verificação 2)

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAF-3` (o card do Apêndice A do relatório, `TK-94a`, é a fonte; `antes` re-medidos), `F-24`, `F-26`; `DAF-24` (primeiro item: o instrumento corrigido julga as tarefas seguintes).
- **Operação do modelo:** `OP-1` - OP-1: O instrumento de evidência passa a resumir as diferenças da entrega pelo mesmo recorte da lista de arquivos tocados, sem o trabalho em andamento de fora da tarefa. - precisa de: relatório de auditoria — Ninguém altera: é a fonte de cada item que o plano aplica.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/` (ferramentaria do hub). Carrega módulo irmão por caminho (`importlib.util.spec_from_file_location`), nunca por `import`; não importa de `tests/`.
- **Caso medido que motivou:** no dossiê de evidência de duas tarefas do plano fictício da auditoria (2026-09-27), o bloco `## Diff (git diff --stat)` listou os 59 arquivos do trabalho não commitado da árvore contra `HEAD`, nenhum da entrega, e deixou fora os alvos entregues não rastreados; só `## Arquivos tocados` respeitou o `--desde`. Causa: `coletar_diff_stat(root)` roda `git diff HEAD --stat` e não recebe o `desde` que `montar_documento` já tem. O protótipo do consultor (fora da árvore) gravou a árvore de trabalho num índice temporário, como `capturar_ref` faz, e rodou `git diff --stat <ref> <árvore> -- <tocados>`: deu os mesmos 10 arquivos de `## Arquivos tocados`, o não rastreado incluído.
- **Contratos/classes:** `coletar_diff_stat(root: Path, desde: str | None = None) -> str`; `montar_documento` repassa o `desde` que já recebe. Com `desde`, o bloco `## Diff (git diff --stat)` lista exatamente os arquivos da seção `## Arquivos tocados` do mesmo recorte — rastreados e não rastreados —, cada um com as linhas mudadas desde `<ref>`; sem arquivo tocado, o bloco traz `(sem diferenças)`. Com lista de tocados vazia, o `git diff` não roda sem caminho (sem caminho ele devolveria a árvore inteira). Árvore de trabalho, índice real e lista de stash saem como entraram. O cabeçalho do bloco não muda. Sem `desde`, o bloco é o de hoje (`git diff HEAD --stat`).
- **Passos:** 1. Em `coletar_diff_stat`, acrescentar o parâmetro `desde`; com `desde`, gravar a árvore de trabalho num índice temporário (variável `GIT_INDEX_FILE` apontando para arquivo em diretório temporário, como `capturar_ref` faz) e rodar `git diff --stat <desde> <árvore> -- <tocados>`, com `<tocados>` = a lista que `coletar_arquivos_tocados` devolve para o mesmo `desde`. 2. Em `montar_documento`, passar `desde` a `coletar_diff_stat`. 3. Escrever os dois testes da seção `Testes`.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 2 testes novos (referência datada: `452 passed`, 2026-09-27). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; o trabalho não commitado da árvore fora deles não se toca, não se reverte e não se commita; nenhum commit. - Nenhum tíquete novo no diário; achado vai à linha de retorno.
- **Não fazer:** não mudar `coletar_arquivos_tocados` nem `capturar_ref`; não tocar `_REGISTRO_ORQUESTRACAO` (é da `AF-T2`); não mudar o cabeçalho do bloco nem o teto de caracteres dos trechos; não usar `git stash push` nem nada que escreva na árvore, no índice real ou na lista de stash.
- **Contingências:** - se um teste existente de `tests/test_review_evidence.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_diff_stat_desde_recorta_como_os_tocados` — repositório temporário com baseline commitado; um rastreado alterado antes da captura (trabalho alheio); `<ref>` por `capturar_ref`; depois, um rastreado alterado e um não rastreado criado: o bloco `## Diff` de `montar_documento(..., desde=<ref>)` cita os dois arquivos da entrega e não cita o trabalho alheio (a regra antiga, `git diff HEAD --stat`, citaria o alheio e não citaria o não rastreado). TR `test_tr_diff_stat_desde_sem_tocados_sai_sem_diferencas` — `<ref>` capturado e nada mudado depois: o bloco traz `(sem diferenças)`. Suítes: `tests/test_review_evidence.py`, depois a suíte inteira.
- **Fora do escopo desta tarefa:** o balde de registro da orquestração para `docs/audits/` (`AF-T2`).
- **Handover:** 2026-09-27 · para `AF-T2` - **Entregue:** coletar_diff_stat(root, desde=None) em .claude/tools/review_evidence.py:232 recorta o bloco ## Diff pelos tocados desde <ref> (indice temporario, rastreados e nao rastreados); montar_documento repassa desde; testes em tests/test_review_evidence.py:1206 e :1238 - **Contrato:** com --desde, o bloco ## Diff do dossie de evidencia lista exatamente os arquivos de ## Arquivos tocados; sem tocados sai (sem diferencas); sem --desde nada muda - **Não refazer:** o recorte do resumo de diferencas; a guarda de tocados vazio ja existe por inspecao - **Pendente:** nenhum

## Execução

**Consumo:** 22 tool uses, 87.4 k tokens, 474.4 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

O proprio dossie de evidencia desta tarefa ja saiu pelo codigo entregue: o bloco Diff lista os mesmos 6 arquivos de Arquivos tocados, os 2 nao rastreados inclusive, contra os 59 do caso medido. Exercicio ponta a ponta em repositorio temporario (trabalho alheio antes do <ref>, rastreado alterado e nao rastreado criado depois): Diff = tocados, sem-desde inalterado, indice real, lista de stash e status da arvore identicos antes e depois. Observacao sem rota: o --stat abrevia caminho longo com '.../' (visto no bloco desta tarefa), efeito da largura padrao do git que o card prescreveu.

## Fechamento

**Desdobramento:** aprovado

# Histórico

Tarefa "Com `--desde`, o resumo de diferenças do dossiê sai do recorte dos tocados". Passo: conferir os gates e preparar o despacho.
Tarefa "Com `--desde`, o resumo de diferenças do dossiê sai do recorte dos tocados": gates aprovados; vou materializar in-progress e gravar o ponto de partida.
Agente executor recebe a tarefa "Com `--desde`, o resumo de diferenças do dossiê sai do recorte dos tocados" e vai executar: O instrumento de evidência passa a resumir as diferenças da entrega pelo mesmo recorte da lista de arquivos tocados, sem o trabalho em andamento de fora da tarefa.
Agente executor devolveu a tarefa "Com `--desde`, o resumo de diferenças do dossiê sai do recorte dos tocados": review — sem pendência.
Tarefa "Com `--desde`, o resumo de diferenças do dossiê sai do recorte dos tocados": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "Com `--desde`, o resumo de diferenças do dossiê sai do recorte dos tocados" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "Com `--desde`, o resumo de diferenças do dossiê sai do recorte dos tocados": aprovado 100%, bloqueante nenhuma.
Scrum master vai fechar a tarefa "Com `--desde`, o resumo de diferenças do dossiê sai do recorte dos tocados" como done: registrar estado, RDO e telemetria.
