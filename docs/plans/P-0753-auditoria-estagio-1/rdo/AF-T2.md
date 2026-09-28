# RDO — P-0753 · AF-T2

# Humano

Tarefa "O relatório de auditoria de quem conduz entra no balde de registro da orquestração" concluída em 2026-09-27.
O relatório de auditoria que quem conduz grava em docs/audits/ passa a contar como registro da condução, sem pesar no veredito da tarefa.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria de encerramento do estágio 1: as dezoito recomendações e os dois tíquetes do consultor": 2/21 tarefas concluídas; próxima: "O painel do gerente reconhece o programa depois das opções do interpretador".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0753-auditoria-estagio-1/plano.md`
**Tarefa:** `AF-T2` — O relatório de auditoria de quem conduz entra no balde de registro da orquestração
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O instrumento de evidência passa a contar o relatório de auditoria de quem conduz como registro da condução, e não como entrega fora do alvo da tarefa.

**Arquivos-alvo:** - `.claude/tools/review_evidence.py` - `tests/test_review_evidence.py`

**Verificação:** 1. `python -c "import importlib.util as u;from pathlib import Path;s=u.spec_from_file_location('r',Path('.claude/tools/review_evidence.py'));m=u.module_from_spec(s);s.loader.exec_module(m);print(m._eh_registro_orquestracao('docs/audits/AUDITORIA_X.md'))"` → `True` — antes `False`, depois `True` (esperado, não ensaiado) 2. `python -c "from pathlib import Path;c=chr(96);t=Path('.claude/tools/review_evidence.py').read_text(encoding='utf-8');print(t.count(c+'docs/RDO/'+c+')'),t.count(c+'docs/RDO/'+c+', '+c+'docs/audits/'+c+')'),t.count('plano, RDO, relatório de auditoria'))"` → `0 1 1` — antes `1 0 0`, depois `0 1 1` (esperado, não ensaiado) 3. `python -m pytest tests/test_review_evidence.py -q -k "auditoria"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado) 4. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava) 5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)

**Pronto quando:** - dossiê de evidência.atribuição do relatório de auditoria — cai como registro da condução e não pesa no veredito; quando é alvo do card, segue coberto — Verificações 1 e 3 (as duas docstrings nomeiam a pasta, Verificação 2)

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAF-3` (o card do Apêndice A do relatório, `TK-95a`, é a fonte; `antes` re-medidos), `F-24`.
- **Depende de:** `AF-T1`
- **Operação do modelo:** `OP-2` - OP-2: O instrumento de evidência passa a contar o relatório de auditoria de quem conduz como registro da condução, e não como entrega fora do alvo da tarefa. - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/`; carrega módulo irmão por caminho; não importa de `tests/`.
- **Caso medido que motivou:** a evidência de uma tarefa do plano fictício da auditoria (`--desde a1bea86`, 2026-09-27) deu `docs/audits/AUDITORIA_ENCERRAMENTO_ESTAGIO1_2026-09-27.md` como "fora dos alvos e sem atribuição" e deixou o veredito mecânico aberto: o arquivo era o relatório que quem conduz escrevia na janela, não entrega do card. `_REGISTRO_ORQUESTRACAO` tem `docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, `docs/plans/` e `docs/RDO/`, e não `docs/audits/`, onde a orquestração grava auditoria. Com `docs/audits/` no balde, a mesma evidência sai `conforme`.
- **Contratos/classes:** `_eh_registro_orquestracao(caminho: str) -> bool` devolve `True` para caminho sob `docs/audits/`; a precedência de `confrontar_escopo` não muda: arquivo de `docs/audits/` que é alvo do card segue coberto (`da entrega`). O balde vale no dossiê, em `confrontar_escopo` e no `--atribuir`.
- **Passos:** 1. Acrescentar `docs/audits/` à tupla `_REGISTRO_ORQUESTRACAO`. 2. Na docstring do módulo, o trecho depois de `antigo:` vira o trecho depois de `novo:` (sem quebra nova e sem refluxo; o rótulo não entra no arquivo): ```text antigo: `docs/plans/`, `docs/RDO/`); ato do dono fora novo: `docs/plans/`, `docs/RDO/`, `docs/audits/`); ato do dono fora ``` 3. Na docstring de `_eh_registro_orquestracao`, o trecho depois de `antigo:` vira o trecho depois de `novo:` (sem quebra nova e sem refluxo; o rótulo não entra no arquivo): ```text antigo: telemetria, plano, RDO. Não é atribuível novo: telemetria, plano, RDO, relatório de auditoria. Não é atribuível ``` 4. Escrever os dois testes da seção `Testes`.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 2 testes novos (referência datada: `452 passed`, 2026-09-27). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Nenhum tíquete novo no diário.
- **Não fazer:** não mudar a precedência de `confrontar_escopo`; não criar declaração de trabalho em andamento da orquestração no despacho (rota descartada pelo consultor: ainda dependeria de quem conduz lembrar); não tocar `coletar_diff_stat` (é da `AF-T1`).
- **Contingências:** - se um teste existente de `tests/test_review_evidence.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_relatorio_de_auditoria_sai_como_registro_da_orquestracao` — `docs/audits/AUDITORIA_X.md` tocado fora dos alvos de `T1`: o documento traz `Registro da orquestração (não atribuível a tarefa)` e `Veredito mecânico: conforme`. TR `test_tr_relatorio_de_auditoria_alvo_do_card_segue_coberto` — card cujo alvo é `docs/audits/AUDITORIA_X.md`: a atribuição do arquivo é `da entrega` (a regra concorrente, "tudo em `docs/audits/` é registro", daria registro da orquestração).
- **Fora do escopo desta tarefa:** edição de quem conduz fora de `docs/audits/` na janela segue para a reconciliação do revisor, como hoje.
- **Handover:** 2026-09-27 · para quem vier depois - **Entregue:** docs/audits/ na tupla _REGISTRO_ORQUESTRACAO (.claude/tools/review_evidence.py:407); docstrings do modulo (:51) e de _eh_registro_orquestracao atualizadas; testes em tests/test_review_evidence.py:597 e :618 - **Contrato:** arquivo tocado sob docs/audits/ fora dos alvos sai como 'Registro da orquestracao' e nao pesa no veredito mecanico; alvo do card em docs/audits/ segue 'da entrega' - **Não refazer:** o balde de docs/audits/; o recorte do ## Diff (AF-T1) - **Pendente:** nenhum

## Execução

**Consumo:** 20 tool uses, 84.0 k tokens, 338.6 s (fonte: `<usage>` do encerramento)

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

Scrum master concluiu a tarefa "Com `--desde`, o resumo de diferenças do dossiê sai do recorte dos tocados" e vai pegar a tarefa "O relatório de auditoria de quem conduz entra no balde de registro da orquestração".
Tarefa "O relatório de auditoria de quem conduz entra no balde de registro da orquestração". Passo: conferir os gates e preparar o despacho.
Tarefa "O relatório de auditoria de quem conduz entra no balde de registro da orquestração": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O relatório de auditoria de quem conduz entra no balde de registro da orquestração" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O relatório de auditoria de quem conduz entra no balde de registro da orquestração": aprovado 100%, bloqueante nenhuma.
Scrum master vai fechar a tarefa "O relatório de auditoria de quem conduz entra no balde de registro da orquestração" como done: registrar estado, RDO e telemetria.
