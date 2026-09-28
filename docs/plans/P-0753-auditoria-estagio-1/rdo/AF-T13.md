# RDO — P-0753 · AF-T13

# Humano

Tarefa "O esqueleto do relatório de operações sai por comando" concluída em 2026-09-27.
O esqueleto do relatório de operações do fechamento passa a sair por comando, com uma conferência de cobertura.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria de encerramento do estágio 1: as dezoito recomendações e os dois tíquetes do consultor": 13/21 tarefas concluídas; próxima: "A conferência do modelo julga a versão pendente, e a comparação mostra o contrato".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0753-auditoria-estagio-1/plano.md`
**Tarefa:** `AF-T13` — O esqueleto do relatório de operações sai por comando
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem conduz passa a gerar por comando o esqueleto do relatório de operações, em vez de reescrevê-lo de memória a cada plano.

**Arquivos-alvo:** - `.claude/tools/encerrar.py` - `tests/test_encerrar.py` - `.claude/skills/entrega-de-encerramento/SKILL.md`

**Verificação:** 1. `python .claude/tools/encerrar.py operacoes --help` → `exit 0` — antes `exit 2`, depois `exit 0` (esperado, não ensaiado) 2. `python -m pytest tests/test_encerrar.py -q -k "esqueleto_de_operacoes"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado) 3. `python -c "from pathlib import Path;t=Path('.claude/skills/entrega-de-encerramento/SKILL.md').read_text(encoding='utf-8');print(t.count('encerrar.py operacoes --plano'),t.count('citados = set(re.findall'))"` → `2 0` — antes `0 1`, depois `2 0` (esperado, não ensaiado) 4. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava) 5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)

**Pronto quando:** - relatório de operações.esqueleto — gerado por comando a partir das tarefas do plano, com a cobertura conferida — Verificações 1 a 3

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAF-22`, `DAF-34`, `F-21`.
- **Depende de:** `AF-T12`
- **Operação do modelo:** `OP-13` - OP-13: Quem conduz passa a gerar por comando o esqueleto do relatório de operações, em vez de reescrevê-lo de memória a cada plano. - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; fechamento de tarefa — Quem implementa faz o fechamento copiar cada achado de processo do laudo para os achados do plano, com a rota, sem repetir achado igual.
- **Camada e fronteira:** instrumento do kit `.claude/tools/encerrar.py` e a skill `entrega-de-encerramento`; `encerrar.py` carrega `backlog.py` e `caminhos.py` por caminho; não importa de `tests/`.
- **Contratos/classes:** subcomando `operacoes`, com `parents=[comuns]` (o analisador comum de hoje, que já traz `--plano` e `--repo`) e mais a opção `--checar`. Sem `--checar`: grava em `caminhos.destino_operacoes(repo, plano)` o esqueleto abaixo; arquivo já existente é recusa (`operacoes: já existe <caminho>`, exit `1`, nada escrito). Com `--checar`: não escreve; lê o arquivo de `destino_operacoes` e imprime duas linhas, `nao citados: <ids separados por vírgula e espaço, ou nenhum>` (todo `### <ID> ` de card do plano que não aparece no documento como `` `<ID>` ``) e `sem os quatro blocos: <ids, ou nenhum>` (toda seção `## `` `<ID>` `` sem uma das quatro linhas de bloco); exit `0` quando as duas dizem `nenhum`, senão `1`; arquivo ausente é recusa (`operacoes: arquivo ausente <caminho>`, exit `1`). Tarefas lidas de `_backlog._parse_plano(plano, repo).tarefas` (`id`, `titulo`, `status`); tarefa `cancelled` entra na tabela do arco e não ganha seção.
- **Passos:** 1. Escrever o subcomando com a regra de `Contratos/classes`. O esqueleto é, nesta ordem (as quebras são as do bloco; o recuo de dois espaços não entra no arquivo; `<título do plano>`, e em cada linha de tarefa `<ID>`, `<título>` e `<status>`, se substituem; a seção `## `` `<ID>` `` se repete por tarefa não `cancelled`, na ordem do plano): ```text # Operações — <título do plano> ## Abertura **O problema:** **A solução, em uma frase:** | termo | o que é | |---|---| ## O arco | estrato | pergunta que responde | tarefas | |---|---|---| | tarefa | título | status | |---|---|---| | `<ID>` | <título> | <status> | ## `<ID>` — <título> **Contexto que a motivou:** **O que é o artefato:** **Como funciona na prática:** **Protege contra:** ## O que vale além deste plano | regra | o que resolve | residência | |---|---|---| ## Os ganhos, medidos | medida | antes | depois | |---|---|---| ## O padrão que a execução revelou ## Pendências abertas ao fim do plano | pendência | por que ficou aberta | o que a fecha | bloqueia algo? | |---|---|---|---| ``` 2. Escrever os três testes da seção `Testes`, sobre o repositório temporário de `_montar_repo` (plano legado `P-0001-alfa.md`, destino `docs/OPERACOES_AS_IS_P-0001.md`). 3. Em `.claude/skills/entrega-de-encerramento/SKILL.md`, seção *Procedimento*: o item `4.` passa a ser a linha `4. **Escreva as seções por tarefa** sobre o esqueleto que `` `python .claude/tools/encerrar.py operacoes --plano <plano>` `` gera (uma seção por tarefa viva, com os quatro blocos vazios), aplicando os três testes da regra de leitura.`; o item `6.` inteiro, com o bloco de código dele, e o item `7.` saem, e entra no lugar deles o item abaixo; o item `8.` passa a `7.` (as quebras são as do bloco; o recuo de dois espaços não entra no arquivo): ```text 6. **Verifique a cobertura e a estrutura por comando**, não por leitura — todo card do plano citado no documento e toda seção de tarefa com os quatro blocos obrigatórios: `python .claude/tools/encerrar.py operacoes --plano <plano> --checar`, exit `0` com as linhas `nao citados: nenhum` e `sem os quatro blocos: nenhum`. ```
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 3 testes novos (referência datada: `452 passed`, 2026-09-27). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0 (a skill muda no corpo, não no frontmatter). - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
- **Não fazer:** não preencher os blocos do esqueleto (a redação é do relato, pela skill); não mudar `caminhos.destino_operacoes`; não mudar os demais verbos de `encerrar.py`.
- **Contingências:** - se um teste existente de `tests/test_encerrar.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_esqueleto_de_operacoes_uma_secao_por_card` — `operacoes --plano P-0001-alfa.md` grava o arquivo com exatamente uma linha que começa por `` ## `ALF-T1` `` e nenhuma de `ALF-T2` (`cancelled`), e a tabela do arco cita as duas. TR `test_tr_esqueleto_de_operacoes_nao_sobrescreve` — arquivo já existente: exit 1 e conteúdo intocado. TF `test_tf_esqueleto_de_operacoes_checar_cobertura` — sobre o esqueleto recém-gerado, `--checar` sai 0 com `nao citados: nenhum` e `sem os quatro blocos: nenhum`; com a linha `**Protege contra:**` apagada, sai 1 com `sem os quatro blocos: ALF-T1`.
- **Fora do escopo desta tarefa:** a redação do relatório de operações deste plano (ato de encerramento).
- **Handover:** 2026-09-27 · para quem vier depois - **Entregue:** subcomando 'encerrar.py operacoes' grava o esqueleto do relatório de operações em caminhos.destino_operacoes (recusa se já existe) e, com --checar, lista 'nao citados' e 'sem os quatro blocos'; skill entrega-de-encerramento (Procedimento itens 4 e 6) cita o comando; 3 testes em tests/test_encerrar.py - **Contrato:** o relato do fechamento parte do esqueleto por comando e confere a cobertura com --checar; --checar ainda não acusa seção inteira ausente (achado do laudo, com o consultor) - **Não refazer:** nada a declarar - **Pendente:** nenhum

## Execução

**Consumo:** 49 tool uses, 138.6 k tokens, 671.6 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

Entrega fiel ao contrato do card, e o furo mora no contrato: a checagem de cobertura cruza o ID contra o documento inteiro, e o esqueleto gerado pelo mesmo verbo cita todo ID na tabela do arco — a checagem passa a ser verdadeira por construção. O exercício que o revela é apagar a seção inteira, não uma linha dela; o TF do card só apaga uma linha.

## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master vai fechar a tarefa "O esqueleto do relatório de operações sai por comando" como done: registrar estado, RDO e telemetria.
