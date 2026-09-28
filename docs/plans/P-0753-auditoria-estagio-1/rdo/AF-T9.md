# RDO — P-0753 · AF-T9

# Humano

Tarefa "O `next` e o `show` entregam o card inteiro" concluída em 2026-09-27.
O next e o show passam a entregar o card inteiro da tarefa, sem cortá-lo no teto.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria de encerramento do estágio 1: as dezoito recomendações e os dois tíquetes do consultor": 9/21 tarefas concluídas; próxima: "Um verbo `despachar` roda as conferências do despacho e recusa pela primeira que falhar".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achados registrados no plano, com rota: 2 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/plans/P-0753-auditoria-estagio-1/plano.md`
**Tarefa:** `AF-T9` — O `next` e o `show` entregam o card inteiro
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O backlog passa a entregar a quem conduz o card inteiro no despacho, sem corte no meio.

**Arquivos-alvo:** - `.claude/tools/backlog.py` - `tests/test_backlog.py` - `.claude/skills/passagem-de-bastao/SKILL.md`

**Verificação:** 1. `python -m pytest tests/test_backlog.py -q -k "card_inteiro"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado) 2. `python -c "from pathlib import Path;print(Path('.claude/skills/passagem-de-bastao/SKILL.md').read_text(encoding='utf-8').count('O card chega inteiro.'))"` → `1` — antes `0`, depois `1` (esperado, não ensaiado) 3. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava) 4. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)

**Pronto quando:** - despacho de tarefa.card entregue inteiro — o card chega inteiro; só os achados e as notas de execução têm teto — Verificações 1 e 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAF-11`, `DAF-33`, `F-9`.
- **Depende de:** `AF-T8`
- **Operação do modelo:** `OP-9` - OP-9: O backlog passa a entregar a quem conduz o card inteiro no despacho, sem corte no meio. - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; conferência do backlog — Quem implementa faz a conferência aceitar o plano recém-esboçado que já tem o estado registrado e ainda não entrou na fila.
- **Camada e fronteira:** instrumento do kit `.claude/tools/backlog.py` (verbos `next` e `show`, somente leitura) e a skill `passagem-de-bastao`; não importa de `tests/`.
- **Contratos/classes:** `_truncar(texto, arquivo, linha_header, linha_fim) -> str` não muda. Regra nova: no `next` (`renderizar_next`) e no `show` de tarefa ou de card de tíquete (`Item`), o texto do card sai inteiro até a linha anterior a `- **Notas de execução:**`; o trecho que começa nessa linha (quando existe) e o bloco `_bloco_achados` passam por `_truncar`. O `show` de um plano (`Plano`) continua inteiro por `_truncar`, como hoje. O rótulo `--- dossiê (verbatim, teto DB-7) ---` do `next` vira `--- dossiê (verbatim, card inteiro) ---`.
- **Passos:** 1. Escrever a função `_card_inteiro(item: Item) -> str` com a regra de `Contratos/classes` e usá-la no `next` e no `show` de `Item`. 2. Trocar o rótulo do dossiê no `next`; na docstring do módulo, a linha depois de `antigo:` vira a linha depois de `novo:` (sem quebra nova e sem refluxo das linhas vizinhas; os rótulos não entram no arquivo): ```text antigo: truncado ao teto `DB-7` (8.000 chars / 120 linhas, com ponteiro `arquivo:l1-l2` quando corta). novo: inteiro no card de tarefa; o teto `DB-7` (8.000 chars / 120 linhas, com ponteiro `arquivo:l1-l2` quando corta) vale para plano, notas de execução e achados. ``` 3. Escrever os dois testes da seção `Testes`. 4. Em `.claude/skills/passagem-de-bastao/SKILL.md`, Parte 2, inserir antes da linha que começa por `**Fonte do contexto, em ordem de preferência:**` o parágrafo abaixo, seguido de uma linha vazia (as quebras são as do bloco; o recuo de dois espaços não entra no arquivo): ```text **O card chega inteiro.** `backlog.py next` e `backlog.py show <ID>` imprimem o card inteiro, sem corte; o teto `DB-7` (8.000 caracteres ou 120 linhas, com o ponteiro `arquivo:l1-l2` de onde cortou) vale só para o bloco de achados roteados ao card e para as notas de execução do plano legado. O dossiê se copia da saída do instrumento, sem reler o plano. ```
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 2 testes novos (referência datada: `452 passed`, 2026-09-27). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - `next` e `show` seguem somente leitura: nenhuma escrita em arquivo.
- **Não fazer:** não mudar `_TETO_CHARS` nem `_TETO_LINHAS`; não mudar a seleção do `next`; não mudar o `show` de plano (`test_tf_show_trunca_em_8000_chars_120_linhas_com_ponteiro` segue verde).
- **Contingências:** - se `test_tr_saida_do_next_cabe_no_teto` cair porque o card da fixture `next_tk90` passou do teto → parar e sinalizar `blocked` razão `premissa`, colando o tamanho medido da saída. - se outro teste existente de `tests/test_backlog.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_card_inteiro_no_next_e_no_show` — plano temporário com um card de 150 linhas: a saída do `next` e a do `show <ID>` contêm a linha 150 do card e não contêm `… truncado (` (a regra de hoje corta na linha 120). TR `test_tr_card_inteiro_notas_de_execucao_seguem_com_teto` — card de plano legado com 200 linhas de notas de execução: a saída do `show` contém `… truncado (`.
- **Fora do escopo desta tarefa:** o verbo `despachar`, que imprime o card pelo mesmo caminho (`AF-T10`).
- **Handover:** 2026-09-27 · para quem vier depois - **Entregue:** _card_inteiro em .claude/tools/backlog.py:1121, usada por renderizar_next e pelo show de Item: card inteiro ate '- **Notas de execucao:**', notas e achados com teto; rotulo '--- dossiê (verbatim, card inteiro) ---'; paragrafo 'O card chega inteiro.' na skill passagem-de-bastao; testes tests/test_backlog.py:1142 e :1196 - **Contrato:** o next e o show de tarefa entregam o card inteiro; show de plano segue truncado - **Não refazer:** o card inteiro no next/show - **Pendente:** nenhum

## Execução

**Consumo:** 39 tool uses, 102.6 k tokens, 479.1 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master vai fechar a tarefa "O `next` e o `show` entregam o card inteiro" como done: registrar estado, RDO e telemetria.
