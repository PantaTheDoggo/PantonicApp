# RDO — P-0753 · AF-T18

# Humano

Tarefa "O guia de entrada descreve o kit como ele fica" concluída em 2026-09-27.
O README passa a descrever o kit como a janela o deixou: os verbos novos, o pré-voo, a versão pendente do modelo e a telemetria gravada pelo gancho.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria de encerramento do estágio 1: as dezoito recomendações e os dois tíquetes do consultor": 18/21 tarefas concluídas; próxima: "`uow.py` sai do kit".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0753-auditoria-estagio-1/plano.md`
**Tarefa:** `AF-T18` — O guia de entrada descreve o kit como ele fica
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa revisa o guia de entrada do kit para que ele descreva o kit como fica depois das mudanças deste plano.

**Arquivos-alvo:** - `README.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('README.md').read_text(encoding='utf-8');print(t.count('em sete verbos'),t.count('em oito verbos'),t.count('em cinco verbos'),t.count('prevoo.py'),t.count('Quem escreve a linha é o hook'))"` → `0 1 1 1 1` — antes `1 0 0 0 0`, depois `0 1 1 1 1` (esperado, não ensaiado) 2. `pwsh -NoProfile -File .claude/checks/check-readme.ps1` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava) 3. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava) 4. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)

**Pronto quando:** - guia de entrada do kit.aderência ao kit entregue — descreve o kit com as mudanças deste plano — Verificações 1 e 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAF-2` (revisão do `README.md` ao fim, G-README dever 2), `DAF-24`; as mudanças descritas vêm das `AF-T5`, `AF-T8`, `AF-T9`, `AF-T10`, `AF-T12`, `AF-T13`, `AF-T14` e `AF-T17`.
- **Depende de:** `AF-T1`, `AF-T2`, `AF-T3`, `AF-T4`, `AF-T5`, `AF-T6`, `AF-T7`, `AF-T8`, `AF-T9`, `AF-T10`, `AF-T11`, `AF-T12`, `AF-T13`, `AF-T14`, `AF-T15`, `AF-T16`, `AF-T17`
- **Operação do modelo:** `OP-18` - OP-18: Quem executa revisa o guia de entrada do kit para que ele descreva o kit como fica depois das mudanças deste plano. - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; série de telemetria — Quem implementa faz o gancho gravar toda rodada de agente do kit, com o papel no identificador, e a soma do plano contar todas elas.; linha de retorno do revisor — Quem implementa acrescenta a recomendação à linha e faz todos os que a leem aceitarem a forma nova no mesmo ato.; despacho de tarefa — Quem implementa faz o despacho entregar o card sem corte e rodar num comando só as conferências que hoje se repetem à mão, recusando pela primeira que falhar.; marco de validação — Quem implementa faz um comando receber o resultado do dono como escolha explícita e gravá-lo em todos os lugares onde o marco aparece, sem interpretar a frase do dono.; relatório de operações — Quem implementa faz um comando gerar o esqueleto do relato a partir das tarefas do plano e conferir a cobertura dele.; conferência do modelo — Quem implementa faz a conferência julgar a versão pendente pelas mesmas regras da vigente, e a comparação mostrar o contrato e a propriedade que mudaram.; planejador — Quem implementa recebe o roteiro de fases do agente e muda só a fase que a recomendação aponta, deixando as demais como estão.
- **Camada e fronteira:** documentação pública do hub (`README.md`); `.claude/README.md` é derivado e não se edita à mão.
- **Passos:** 1. Seção *Anatomia do kit*, o bullet de `.claude/tools/backlog.py` (cinco linhas, de `- `` `.claude/tools/backlog.py` `` — o instrumento do diário de obras, em sete verbos` até `a linha de priorização.`) vira o bloco abaixo (as quebras são as do bloco; o recuo de dois espaços não entra no arquivo): ```text - `.claude/tools/backlog.py` — o instrumento do diário de obras, em oito verbos: `next` seleciona a próxima tarefa de forma determinística e imprime o card inteiro, `show` devolve o card inteiro de um item, `check` faz o lint da gramática do diário e dos planos — o plano recém-esboçado, com o estado registrado e ainda fora da fila, inclusive —, `status` e `start` transicionam uma tarefa e projetam a mudança nos registros derivados, `despachar` roda os gates do despacho, materializa `in-progress`, grava a tarefa corrente com o ponto de partida e imprime o card, `drain` leva o inbox de planos ao índice, e `diretiva` reescreve a linha de priorização. ``` 2. Mesma seção, o bullet de `.claude/tools/encerrar.py` (sete linhas, de `- `` `.claude/tools/encerrar.py` `` — o instrumento de fechamento, em três verbos` até `Os três recusam sem escrever quando falta insumo.`) vira o bloco abaixo, seguido do bullet novo do `prevoo.py` (as quebras são as do bloco; o recuo de dois espaços não entra no arquivo): ```text - `.claude/tools/encerrar.py` — o instrumento de fechamento, em cinco verbos: `handover` registra no próprio card, de máquina, o que quem vem depois espera da tarefa (o que foi entregue, com o que se pode contar, o que não refazer, o que fica pendente), e é esse campo que a seleção da próxima tarefa devolve à sucessora; `tarefa` leva a tarefa em revisão a concluída num ato só — confere o modelo do plano, projeta o estado, escreve o registro da tarefa em três seções (humano, máquina, histórico) com o pacote transcrito do laudo, garante a linha de telemetria e registra com rota os achados, inclusive cada achado de processo do laudo; `marco` grava o resultado que o dono deu num marco em todos os lugares onde o marco aparece; `operacoes` gera o esqueleto do relatório de operações e confere a cobertura dele; `plano` fecha o plano sem tarefa aberta — estado, relatório de entrega nas mesmas três seções e uma linha no diário. Os cinco recusam sem escrever quando falta insumo. - `.claude/tools/prevoo.py` — o pré-voo do pedido: confere cada caminho, símbolo e flag que o texto do dono cita e imprime a tabela `citado | existe | onde`, que abre o plano antes de qualquer campanha. ``` 3. Seção *O modelo de domínio do plano*, as duas linhas depois de `antigo:` viram as três depois de `novo:` (as quebras são as do bloco; os rótulos não entram no arquivo): ```text antigo: a sessão o despacha. O instrumento `.claude/tools/modelo.py` confere a seção (`check`) e gera a leitura do dono (`show`), que abre pelo estágio atual. Planos escritos antes desta doutrina não são novo: a sessão o despacha. O instrumento `.claude/tools/modelo.py` confere a seção vigente e a versão pendente (`check`) e gera a leitura do dono (`show`), que abre pelo estágio atual e, com `--drift`, mostra o que muda entre as duas versões, contratos inclusive. Planos escritos antes desta doutrina não são ``` 4. Seção *Memória e telemetria*, as duas linhas depois de `antigo:` viram as quatro depois de `novo:` (as quebras são as do bloco; os rótulos não entram no arquivo): ```text antigo: com a sessão). Quem escreve a linha é **o orquestrador**, nos dois pontos de fechamento — ao fechar cada tarefa e ao encerrar a janela. O valor registrado sai do dado medido da novo: com a sessão). Quem escreve a linha é o hook `SubagentStop`, a cada rodada de agente do kit, com o papel no identificador da tarefa (`<ID>`, `<ID>-revisao`, `<ID>-consultor-<n>`, `<P-n>-planejador`, `<P-n>-modelador`, `<P-n>-scout`); **o orquestrador** só a escreve no fechamento, quando o hook não disparou. O valor registrado sai do dado medido da ``` 5. Rodar `pwsh -NoProfile -File .claude/checks/check-readme.ps1` e conferir exit 0.
- **Restrições desta tarefa:** - `pwsh -NoProfile -File .claude/checks/check-readme.ps1` sai 0 e `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho). - Só o `README.md` se edita; nada fora dele se toca, se reverte ou se commita; nenhum commit.
- **Não fazer:** não editar `.claude/README.md` (derivado); não reescrever seção fora das quatro dos passos; não acrescentar descrição das `AF-T19`, `AF-T20` e `AF-T21`, que esperam o veredito do dono.
- **Contingências:** - se o trecho `antigo:` de um passo não existir verbatim no `README.md` → parar e sinalizar `blocked` razão `premissa`, nomeando o passo. - se `check-readme.ps1` sair diferente de 0 → parar e sinalizar `blocked` razão `premissa`, colando a saída.
- **Testes:** nenhum teste novo; `pwsh -NoProfile -File .claude/checks/check-readme.ps1` e a suíte inteira.
- **Fora do escopo desta tarefa:** o veredito do dono sobre o `README.md` revisado — gate do Marco 2, não critério de pronto deste card.
- **Handover:** 2026-09-27 · para quem vier depois - **Entregue:** README.md: backlog.py em oito verbos com despachar (:906), encerrar.py em cinco verbos com marco e operacoes (:916), bullet novo de prevoo.py (:926), modelo.py check/show --drift sobre a versão pendente (~:695), telemetria gravada pelo hook SubagentStop (~:989) - **Contrato:** o guia de entrada descreve os instrumentos como a janela os deixou; check-readme.ps1 sai 0 - **Não refazer:** nada a declarar - **Pendente:** nenhum

## Execução

**Consumo:** 23 tool uses, 85.7 k tokens, 316.5 s (fonte: `<usage>` do encerramento)

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

Scrum master vai fechar a tarefa "O guia de entrada descreve o kit como ele fica" como done: registrar estado, RDO e telemetria.
