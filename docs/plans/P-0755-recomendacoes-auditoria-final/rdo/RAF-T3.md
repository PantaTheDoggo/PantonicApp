# RDO — P-0755 · RAF-T3

# Humano

Tarefa "O despacho grava o pacote da tarefa e imprime só o recado ao executor" concluída em 2026-09-28.
O despacho passa a gravar o card da tarefa num arquivo e a mostrar a quem conduz só o recado pronto ao executor.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 4/41 tarefas concluídas; próxima: "Quem conduz repassa o texto pronto do despacho e não reconfere âncora".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T3` — O despacho grava o pacote da tarefa e imprime só o recado ao executor
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o despacho de tarefa entregar ao executor, num arquivo próprio, o card com as âncoras já conferidas, deixando na tela de quem conduz só o texto pronto do despacho.

**Arquivos-alvo:** - `.claude/tools/backlog.py` - `.claude/tools/caminhos.py` - `.gitignore` - `tests/test_backlog.py`

**Verificação:** 1. `python -m pytest tests/test_backlog.py -q -k pacote` → `exit 0` — antes `exit 5`, depois `exit 0` 2. `python -m pytest tests/test_backlog.py -q -k texto_pronto` → `exit 0` — antes `exit 5`, depois `exit 0` 3. `python -m pytest tests/test_backlog.py -q -k confere_as_ancoras` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - despacho de tarefa.lugar do card despachado — o pacote da tarefa é gravado num arquivo da pasta do plano, fora do versionamento, que se regenera a cada despacho — Verificação 1 - despacho de tarefa.texto pronto ao executor — o despacho imprime o recado pronto: a linha que declara plano e tarefa, o caminho do pacote e a forma da resposta esperada — Verificação 2 - despacho de tarefa.âncoras conferidas — o pacote traz cada linha citada com o número atual e o texto dela, e marca como ausente o texto que não está mais no arquivo — Verificação 3

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-7`, `DRF-8`, `DRF-35`; `F-6` (3,06k por despacho na tela de quem conduz; 0,72k com o card por arquivo; 23 turnos de âncora à mão), `F-9`, `F-10`; relatório `R-02`, `R-03`.
- **Depende de:** `RAF-T1`
- **Operação do modelo:** `OP-3` - OP-3: Quem executa faz o despacho de tarefa entregar ao executor, num arquivo próprio, o card com as âncoras já conferidas, deixando na tela de quem conduz só o texto pronto do despacho. - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit — `.claude/tools/backlog.py` (verbo `despachar`) e a residência dos caminhos `.claude/tools/caminhos.py`, só biblioteca padrão; `backlog.py` carrega `caminhos.py` por caminho (`_caminhos`), nunca por `import` de pacote; `modelo.py`, `card_check.py` e `review_evidence.py` seguem chamados por subprocesso, sem mudança. O pacote gravado é projeção regenerável do card: fica fora do versionamento pelo `.gitignore`. O contrato do objeto é: "Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor."
- **Contratos/classes:** 1. `caminhos.py`, função nova antes de `def main(argv: list[str] | None = None) -> int:` — `destino_despacho(raiz: Path, plano_path: Path, tarefa: str) -> Path`: plano em pasta (`pasta_do_plano(plano_path)` não `None`) → `<pasta>/despacho/<tarefa>.md`; senão → `<raiz>/docs/RDO/despacho/<tarefa>.md`. 2. `backlog.py`, funções novas antes de `def despachar(`: `_campos_do_card(texto: str) -> dict[str, str]` — cada linha que casa `^- \*\*(?P<rotulo>[^*]+):\*\*` abre o campo `<rotulo>` (sem espaços nas pontas), cujo texto vai do resto da linha até a linha anterior ao próximo campo; e `conferir_ancoras_do_card(repo: Path, texto_card: str) -> list[str]`, com esta regra fechada (`DRF-8`, `DRF-35`): (a) alvos = cada trecho entre crases do campo `Arquivos-alvo` que, sem espaços nas pontas, é arquivo existente sob `repo`, na ordem do card e sem repetição; (b) para cada trecho entre crases (`` `[^`\n]+` ``) dos campos `Passos` e, depois, `Contratos/classes`, sem espaços nas pontas, pula o trecho com menos de 4 caracteres, o já visto e o que é um dos alvos; (c) trecho na forma `<caminho>:<n>` ou `<caminho>:<n>-<m>` (regex `^(?P<caminho>[^:\s]+\.[A-Za-z0-9]+):(?P<linha>\d+)(?:-\d+)?$`) com `<caminho>` arquivo existente e `1 <= n <= número de linhas` → `- <caminho>:<n> — <linha n sem espaços nas pontas>`; (d) outro trecho → a primeira linha, do primeiro alvo em ordem, que contém o trecho → `- <caminho>:<linha> — <texto da linha sem espaços nas pontas>`; (e) sem linha → `- âncora ausente: <trecho>`; (f) item repetido não se repete; lista vazia → `["- nenhuma âncora citada"]`. Arquivos se leem em UTF-8 com `errors="replace"`. 3. `despachar(repo: Path, id_: str, mundo: str | None = None) -> ResultadoStatus` — assinatura, gates, ordem das conferências, recusa e gravação de `.claude/estado/tarefa-corrente.json` (com `ref`) inalterados. No lugar das quatro impressões de hoje (o bloco que começa em `print(f"=== DESPACHO: {id_} — {alvo.titulo}")` e termina em `print(f"ref={ref}")`), grava o pacote em `_caminhos.destino_despacho(repo, repo / pai.arquivo, id_)` (cria a pasta; sobrescreve o que houver; UTF-8, quebra `\n`), com estas partes, nesta ordem, unidas por quebra de linha: `# Despacho <ID> — <título>`, linha vazia, `despacho: <P-id> <ID>` (o `<P-id>` é `pai.id`), `ref=<ref>`, linha vazia, `## Card`, linha vazia, o texto de `show(modelo, id_)`, linha vazia, `## Handovers`, linha vazia, cada handover de `handovers_para(pai, tipo_pai, alvo)` como hoje (`=== HANDOVER DE {autor.id} — {autor.titulo} ({autor.status}; {autor.arquivo})`, o texto, linha vazia) ou `- nenhum` e linha vazia quando não há, `## Âncoras conferidas`, linha vazia, as linhas de `conferir_ancoras_do_card(repo, alvo.texto)` e uma linha vazia. Depois imprime no stdout exatamente estas linhas, nesta ordem (as quebras são as do bloco; `<rel>` é o caminho do pacote relativo a `repo`, com `/`): ```text === DESPACHO: <ID> — <título> despacho: <P-id> <ID> Execute a tarefa <ID>: o card, os handovers e as âncoras conferidas estão em <rel>. Devolva uma única linha, numa destas formas: <ID> review <ID> review pendencia=<uma linha> <ID> blocked motivo=<dependencia|premissa|ferramenta> <uma linha de razão> ref=<ref> ``` 4. `.gitignore`: logo depois da linha `!.claude/estado/.gitkeep`, uma linha vazia e o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card): ```text # Pacote do despacho (`R-02`, `P-0755`): projeção regenerável do card, gravada por # `backlog.py despachar` a cada despacho — nunca se versiona. docs/plans/*/despacho/ docs/RDO/despacho/ ```
- **Passos:** 1. Acrescentar ao fim de `tests/test_backlog.py` os cinco testes da seção `Testes`, no molde de `test_tf_despachar_grava_estado_e_imprime_ref` (fixture `_montar_repo_despachar`, `backlog.main(["despachar", ...])`). 2. Rodar `python -m pytest tests/test_backlog.py -q -k "pacote or texto_pronto or confere_as_ancoras"` e conferir que os testes falham. 3. Aplicar os itens 1 a 4 de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 5 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5); `destino_despacho` e as duas funções novas de `backlog.py` têm chamador de produção em `despachar`. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Os testes montam o repositório em `tmp_path` com `_montar_repo_despachar`; o único teste que lê a árvore real é o do `.gitignore`, por `git check-ignore -q`, sem escrever nada. - Nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar os gates de `despachar` nem a ordem deles; não mudar `next` nem `show`; não mudar o `modelo.py check` chamado pelo despacho (o `--so-vigente` é da `RAF-T20`); não editar a skill `scrum-master` (a doutrina dos Passos 3 e 4 é da `RAF-T4`); não criar pasta `despacho/` versionada nem `.gitkeep` nela.
- **Contingências:** - se um teste de `despachar` que já existia em `tests/test_backlog.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se `git check-ignore -q docs/plans/P-0755-recomendacoes-auditoria-final/despacho/RAF-T1.md` sair 1 depois do item 4 → parar e sinalizar `blocked` razão `premissa`, colando a saída de `git check-ignore -v` para o mesmo caminho.
- **Testes:** TF `test_tf_despachar_grava_o_pacote_na_pasta_do_plano` — `despachar GAM-T1` sai 0 e `docs/plans/P-0-gama/despacho/GAM-T1.md` tem as linhas `### GAM-T1 — Primeira tarefa [Sonnet · classe implementacao]`, `despacho: P-0 GAM-T1` e `## Âncoras conferidas` (a regra de hoje não grava arquivo). TR `test_tr_despachar_recusado_nao_grava_o_pacote` — `despachar GAM-T2` sai 1 e a pasta `docs/plans/P-0-gama/despacho` não existe. TF `test_tf_gitignore_ignora_o_pacote_do_despacho` — na raiz real, `git check-ignore -q` sai 0 para `docs/plans/P-0755-recomendacoes-auditoria-final/despacho/RAF-T1.md` e para `docs/RDO/despacho/TK-1.md` (hoje sai 1). TF `test_tf_despachar_imprime_o_texto_pronto_ao_executor` — a primeira linha do stdout é `=== DESPACHO: GAM-T1 — Primeira tarefa`, a segunda é `despacho: P-0 GAM-T1`, a terceira contém `docs/plans/P-0-gama/despacho/GAM-T1.md`, o stdout tem as três linhas da gramática de retorno com `GAM-T1`, a última começa por `ref=`, e o stdout não contém `- **Objetivo:** fixture.` (hoje o card inteiro sai na tela). TF `test_tf_despachar_confere_as_ancoras_do_card` — o card `GAM-T1` da fixture ganha `- **Arquivos-alvo:**` com `src/alvo.py` (no lugar do `Entregável`) e `- **Passos:**` com `` 1. Editar `src/alvo.py:1` — `x = 1`. `` e `` 2. Trocar `return 1` e `texto que sumiu`. ``; `src/alvo.py` tem as linhas `x = 1`, `def alvo():` e `    return 1`; o pacote tem as linhas `- src/alvo.py:1 — x = 1`, `- src/alvo.py:3 — return 1` e `- âncora ausente: texto que sumiu` (a regra de hoje não confere âncora). Suíte `tests/test_backlog.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** a doutrina do Passo 3 e do Passo 4 da skill `scrum-master` (`RAF-T4`); o despacho com `--so-vigente` (`RAF-T20`); a linha `despacho:` lida pelos hooks de telemetria e de progresso (`RAF-T31`, `RAF-T32`).
- **Handover:** 2026-09-28 · para `RAF-T4` - **Entregue:** backlog.py despachar grava o pacote (card, handovers, âncoras conferidas) em <pasta do plano>/despacho/<ID>.md via caminhos.destino_despacho e imprime só o recado de 8 linhas (=== DESPACHO, despacho: <P-id> <ID>, caminho do pacote, gramática de retorno, ref=); .gitignore ignora docs/plans/*/despacho/ e docs/RDO/despacho/; 5 testes novos, suíte 530 passed - **Contrato:** a linha 'despacho: <P-id> <ID>' sai na 2ª linha do stdout e no pacote; o pacote se regenera a cada despacho e nunca se versiona; gates e ordem de despachar inalterados - **Não refazer:** destino_despacho, _campos_do_card, conferir_ancoras_do_card e os 5 testes - **Pendente:** a regra de conferir_ancoras_do_card gera âncora ausente falsa (AE do laudo), em triagem do consultor antes da RAF-T4

## Execução

**Consumo:** 39 tool uses, 119.2 k tokens, 613.8 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Os cinco testes da RAF-T3 so exercitam a fixture sintetica, cujo card cita ancoras limpas; o comportamento da regra sobre cards reais (ruido de ancora ausente) so apareceu ao rodar conferir_ancoras_do_card em leitura sobre o proprio plano. Card que fecha regra de parser sobre texto de card ganha em trazer um caso medido sobre card real no aceite.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "O medidor de custo da sessão vira comando do kit" e vai pegar a tarefa "O despacho grava o pacote da tarefa e imprime só o recado ao executor".
Tarefa "O despacho grava o pacote da tarefa e imprime só o recado ao executor". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O despacho grava o pacote da tarefa e imprime só o recado ao executor" e vai executar: Quem executa faz o despacho de tarefa entregar ao executor, num arquivo próprio, o card com as âncoras já conferidas, deixando na tela de quem conduz só o texto pronto do despacho.
Agente executor devolveu a tarefa "O despacho grava o pacote da tarefa e imprime só o recado ao executor": review — sem pendência.
Tarefa "O despacho grava o pacote da tarefa e imprime só o recado ao executor": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O despacho grava o pacote da tarefa e imprime só o recado ao executor" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O despacho grava o pacote da tarefa e imprime só o recado ao executor": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O despacho grava o pacote da tarefa e imprime só o recado ao executor" como done: registrar estado, RDO e telemetria.
