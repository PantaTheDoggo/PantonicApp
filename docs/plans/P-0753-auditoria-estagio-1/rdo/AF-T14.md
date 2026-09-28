# RDO — P-0753 · AF-T14

# Humano

Tarefa "A conferência do modelo julga a versão pendente, e a comparação mostra o contrato" concluída em 2026-09-27.
A conferência do modelo passa a julgar também a versão pendente, e a comparação entre versões mostra o contrato alterado.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria de encerramento do estágio 1: as dezoito recomendações e os dois tíquetes do consultor": 14/21 tarefas concluídas; próxima: "O piso comportamental e o teste de camadas passam a existir no hub".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achado registrado no plano, com rota: 1 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/plans/P-0753-auditoria-estagio-1/plano.md`
**Tarefa:** `AF-T14` — A conferência do modelo julga a versão pendente, e a comparação mostra o contrato
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** A conferência do modelo passa a julgar a versão pendente pelas mesmas regras da vigente e a mostrar, na comparação entre as duas, o contrato que mudou.

**Arquivos-alvo:** - `.claude/tools/modelo.py` - `tests/test_modelo.py` - `tests/fixtures/modelo/fluxo-pendente-contrato.md`

**Verificação:** 1. `python -m pytest tests/test_modelo.py -q -k "pendente_roda_o_vocabulario or drift_mostra_contrato"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado) 2. `python .claude/tools/modelo.py check --plano tests/fixtures/modelo/fluxo-pendente-contrato.md` → `exit 1` — antes `exit 2`, depois `exit 1` (esperado, não ensaiado) 3. `python .claude/tools/modelo.py show --plano tests/fixtures/modelo/fluxo-pendente-contrato.md --drift` → `[~] resultado um — contrato: um registro validado => um registro validado e datado` — antes `exit 2`, depois `[~] resultado um — contrato: um registro validado => um registro validado e datado` (esperado, não ensaiado) 4. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava) 5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)

**Pronto quando:** - conferência do modelo.versão pendente conferida — a versão pendente passa pelas mesmas regras da vigente, com as violações marcadas como dela — Verificações 1 e 2 - conferência do modelo.comparação de contratos — a comparação mostra também o contrato e a propriedade de objeto que mudaram — Verificações 1 e 3

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAF-21`, `DAF-28`, `F-20`, `F-31`.
- **Operação do modelo:** `OP-14` - OP-14: A conferência do modelo passa a julgar a versão pendente pelas mesmas regras da vigente e a mostrar, na comparação entre as duas, o contrato que mudou. - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.
- **Camada e fronteira:** instrumento do kit `.claude/tools/modelo.py` (verbos `check` e `show`); carrega `backlog.py` por caminho, como hoje; não importa de `tests/`.
- **Contratos/classes:** - `validar(modelo, plano, modelo_pendente=None, *, pendente=False) -> list[str]` — com `pendente=True`, pula `V2`, `V4` e `V14` (os cards citam a vigente), `V19` e `V20`, e o `V13` só exige cabeçalho, tabela de objetos e tabela de estado (a `## 1A` não tem registro de versões). `verbo_check`, quando a `## 1A` existe, roda também `validar(modelo_pendente, plano, pendente=True)` e soma as violações dela com o prefixo `1A: ` (ex.: `1A: V5 OP-3 — objeto inexistente objeto fantasma`); exit e mensagem final como hoje, contando as duas. - `_diff_objetos(vigente, pendente)` acrescenta, para objeto presente nas duas versões com `contrato` diferente, a linha `[~] <objeto> — contrato: <contrato vigente> => <contrato pendente>`, depois das linhas de propriedade de hoje.
- **Passos:** 1. Acrescentar o parâmetro `pendente` a `validar` e a chamada sobre a `## 1A` em `verbo_check`, pela regra de `Contratos/classes`. 2. Acrescentar a comparação de contrato em `_diff_objetos`. 3. Criar `tests/fixtures/modelo/fluxo-pendente-contrato.md`: cópia de `tests/fixtures/modelo/fluxo-valido.md` com, entre a tabela de `### 1.4 Registro de versões` e o heading seguinte, o bloco `## 1A. Modelo conceitual — versão pendente de validação` com o cabeçalho `**Estado do modelo:** versão 2 · 2026-09-27 · autor: modelador · 3 operações · 4 propriedades · situação: pendente` e cópias de `### 1.1`, `### 1.2` e `### 1.3` da vigente, com duas diferenças: na tabela de objetos, o contrato de `resultado um` é `um registro validado e datado`; na `OP-3`, o `precisa de:` é `resultado dois, registro auxiliar, objeto fantasma`. 4. Escrever os dois testes da seção `Testes`.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 2 testes novos (referência datada: `452 passed`, 2026-09-27). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - `python .claude/tools/modelo.py check --plano docs/plans/P-0753-auditoria-estagio-1/plano.md` segue saindo 0 (o plano não tem `## 1A`).
- **Não fazer:** não mudar a gramática lida (`_localizar_secao`, `extrair_modelo`); não mudar `V1`..`V21` sobre a vigente; não editar `tests/fixtures/modelo/fluxo-pendente.md` (os testes de `show` o usam).
- **Contingências:** - se `check` sobre a fixture nova acusar, além de `1A: V5 OP-3 — objeto inexistente objeto fantasma`, outra violação → a cópia da vigente divergiu de `fluxo-valido.md`: refazer a cópia pelo passo 3 e seguir; se persistir, parar e sinalizar `blocked` razão `premissa`, colando a saída. - se um teste existente de `tests/test_modelo.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_check_pendente_roda_o_vocabulario` — `check` sobre a fixture nova sai 1 e o stderr tem a linha `1A: V5 OP-3 — objeto inexistente objeto fantasma` (a regra de hoje sai 0). TF `test_tf_drift_mostra_contrato_alterado` — `show --drift` sobre a fixture nova tem a linha `[~] resultado um — contrato: um registro validado => um registro validado e datado` (a regra de hoje não imprime linha de objeto, porque as propriedades não mudaram).
- **Fora do escopo desta tarefa:** o dossiê de versão no marco (`AF-T12`).
- **Handover:** 2026-09-27 · para quem vier depois - **Entregue:** modelo.py: validar(pendente=True) roda o vocabulário sobre o bloco ## 1A e verbo_check soma as violações com prefixo '1A: '; _diff_objetos mostra '[~] <objeto> — contrato: <v> => <p>'; fixture tests/fixtures/modelo/fluxo-pendente-contrato.md; 2 TF em tests/test_modelo.py - **Contrato:** modelo.py check julga também a versão pendente; show --drift mostra contrato alterado; check sobre o P-0753 (com ## 1A v2) sai 0 - **Não refazer:** o check da versão pendente e o drift de contrato - **Pendente:** nenhum

## Execução

**Consumo:** 43 tool uses, 106.1 k tokens, 442.2 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

Discriminação confirmada nos dois mundos: o modelo.py de f824f75 sobre a fixture nova dá check exit 0 e show 'sem drift'; o atual dá exit 1 com '1A: V5 OP-3 — objeto inexistente objeto fantasma' e a linha de contrato. Ponta a ponta: fluxo-pendente.md segue exit 1 (agora com '1A: V17 ...' somado), P-0753 real com ## 1A segue exit 0; validar tem um único chamador de produção (verbo_check).

## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master vai fechar a tarefa "A conferência do modelo julga a versão pendente, e a comparação mostra o contrato" como done: registrar estado, RDO e telemetria.
