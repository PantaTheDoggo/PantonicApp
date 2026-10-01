# RDO — P-0754 · AUF-T15

# Humano

Tarefa "O guia de entrada descreve o kit com os herdados fechados" concluída em 2026-09-28.
O README passou a descrever o kit como ficou depois dos itens herdados fechados: a evidência do revisor, o título do tíquete no painel e o plano de contingência das tarefas.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: veredito do dono sobre o README revisado, no Marco 2.
Plano "Auditoria final do kit: os herdados e o relatório de auditoria nova": 15/16 tarefas concluídas; nenhuma tarefa pronta na fila dele.
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0754-auditoria-final/plano.md`
**Tarefa:** `AUF-T15` — O guia de entrada descreve o kit com os herdados fechados
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa revisa o guia de entrada do kit para que ele descreva o kit como fica depois dos herdados fechados.

**Arquivos-alvo:** - `README.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('README.md').read_text(encoding='utf-8');print('[%d-%d-%d]'%(t.count('do card de plano ou do tíquete do diário'),t.count('a evidência que o revisor recebe de cada tarefa'),t.count('A contingência do card faz parte dele')))"` → `[1-1-1]` — antes `[0-0-0]`, depois `[1-1-1]`

**Pronto quando:** - guia de entrada do kit.aderência ao kit entregue — descreve o kit como ele fica depois dos herdados fechados — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAU-2` (revisão do `README.md` ao fim da etapa dos herdados, G-README dever 2), `DAU-29`; `F-17`; as mudanças descritas vêm das `AUF-T1`, `AUF-T3` a `AUF-T7` e `AUF-T9`.
- **Depende de:** `AUF-T1`, `AUF-T2`, `AUF-T3`, `AUF-T4`, `AUF-T5`, `AUF-T6`, `AUF-T7`, `AUF-T8`, `AUF-T9`, `AUF-T10`, `AUF-T11`, `AUF-T12`, `AUF-T13`, `AUF-T14`
- **Operação do modelo:** `OP-15` - OP-15: Quem executa revisa o guia de entrada do kit para que ele descreva o kit como fica depois dos herdados fechados. - precisa de: dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.; painel do gerente — Quem implementa faz o painel achar o título também quando o trabalho em curso é um tíquete, e não só um card de plano.; fechamento de tarefa — Quem implementa troca só a frase final por uma que sirva a todos os comandos, e acerta os testes que esperavam a antiga.; planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta só a regra que a operação pede, deixando as demais como estão.; rubrica de revisão — Quem implementa acrescenta um critério que confere a contingência do card pela mesma regra que o planejador passa a seguir.
- **Camada e fronteira:** documentação pública do hub (`README.md`); `.claude/README.md` é derivado e não se edita à mão.
- **Passos:** 1. Seção `## 6. O loop de execução`, na linha que contém `cada transição do loop, com o título da tarefa no lugar da sigla e sem nenhuma saída de`, trocar `com o título da tarefa no lugar da sigla` por `com o título da tarefa — do card de plano ou do tíquete do diário — no lugar da sigla`, sem quebra nova e sem refluxo. 2. Seção `## 11. Anatomia do kit`, logo depois da linha `  nas mesmas três seções e uma linha no diário. Os cinco recusam sem escrever quando falta insumo.` (fim do bullet de `.claude/tools/encerrar.py`) e antes da linha que começa por ``- `.claude/tools/prevoo.py` ``, inserir o bullet abaixo (as quebras são as do bloco; cada linha perde o recuo da cerca do bloco, e os dois espaços que sobram nas linhas de continuação entram no arquivo): ```text - `.claude/tools/review_evidence.py` — a evidência que o revisor recebe de cada tarefa: a partir do ponto de partida gravado no despacho (`--capturar-ref`), mostra como diferença contra ele o que a entrega mudou — o arquivo criado depois dele, marcado como novo; o versionado que a lista de ignorados também cobre; o que não é texto, comparado pelo conteúdo bruto —, expande o alvo do card escrito com curinga e conta como registro da condução o que quem conduz escreve nos próprios registros, antes de procurar outra tarefa que o tenha declarado. ``` 3. Seção `## 8. Planos: o que é um plano fechado`, condição 4 (a linha que começa por `4. **Linear.**`), trocar a linha `   lê de cima a baixo e sabe o que fazer sem inferir.` pelas três linhas abaixo (as quebras são as do bloco; cada linha perde o recuo da cerca do bloco, e os três espaços que sobram entram no arquivo): ```text lê de cima a baixo e sabe o que fazer sem inferir. A contingência do card faz parte dele: tem a ação fechada, não contraria as restrições do próprio card e declara entre os alvos o arquivo que escreve. ``` 4. Rodar a Verificação e `pwsh -NoProfile -File .claude/checks/check-readme.ps1`.
- **Restrições desta tarefa:** - `pwsh -NoProfile -File .claude/checks/check-readme.ps1` sai 0 e `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho). - Só o `README.md` se edita; nada fora dele se toca, se reverte ou se commita; nenhum commit. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não editar `.claude/README.md` (derivado); não reescrever seção fora das três dos passos; não descrever no guia as regras das `AUF-T11` a `AUF-T13` nem o critério da `AUF-T10`, que são doutrina interna do planejador e do revisor sem superfície no guia (`DAU-29`); não descrever a auditoria nova (`AUF-T16`), que ainda não rodou.
- **Contingências:** - se o texto âncora de um passo não existir verbatim no `README.md` → parar e sinalizar `blocked` razão `premissa`, nomeando o passo. - se `check-readme.ps1` sair diferente de 0 → parar e sinalizar `blocked` razão `premissa`, colando a saída.
- **Testes:** nenhum teste novo; `pwsh -NoProfile -File .claude/checks/check-readme.ps1` e a suíte inteira.
- **Fora do escopo desta tarefa:** o veredito do dono sobre o `README.md` revisado — gate do Marco 2, não critério de pronto deste card.
- **Handover:** 2026-09-28 · para `AUF-T16` - **Entregue:** README.md revisado: §6 (:472, título do card ou do tíquete no painel), §8 condição 4 (a contingência faz parte do card), §11 bullet novo de review_evidence.py (:929); check-readme exit 0 - **Contrato:** o guia descreve o kit depois dos herdados fechados; a auditoria nova ainda não está descrita - **Não refazer:** as três revisões do README - **Pendente:** veredito do dono sobre o README revisado (Marco 2)

## Execução

**Consumo:** 18 tool uses, 52.4 k tokens, 106.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: veredito do dono sobre o README revisado, no Marco 2

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master concluiu a tarefa "Os quatro herdados sem mudança fecham com a prova" e vai pegar a tarefa "O guia de entrada descreve o kit com os herdados fechados".
Tarefa "O guia de entrada descreve o kit com os herdados fechados". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O guia de entrada descreve o kit com os herdados fechados" e vai executar: Quem executa revisa o guia de entrada do kit para que ele descreva o kit como fica depois dos herdados fechados.
Agente executor devolveu a tarefa "O guia de entrada descreve o kit com os herdados fechados": review — sem pendência.
Tarefa "O guia de entrada descreve o kit com os herdados fechados": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O guia de entrada descreve o kit com os herdados fechados" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O guia de entrada descreve o kit com os herdados fechados": aprovado 100%, bloqueante nenhuma, recomendação seguir.
Scrum master vai fechar a tarefa "O guia de entrada descreve o kit com os herdados fechados" como done: registrar estado, RDO e telemetria.
