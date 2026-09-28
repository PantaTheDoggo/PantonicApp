# RDO — P-0753 · AF-T10

# Humano

Tarefa "Um verbo `despachar` roda as conferências do despacho e recusa pela primeira que falhar" concluída em 2026-09-27.
Um verbo despachar passa a rodar de uma vez as conferências do despacho e a preparar a tarefa; ficou uma ressalva sobre a codificação das mensagens de recusa.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Auditoria de encerramento do estágio 1: as dezoito recomendações e os dois tíquetes do consultor": 10/21 tarefas concluídas; próxima: "O consultor lê só as três entradas, e `estrategico=` é uma frase".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achado registrado no plano, com rota: 1 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/plans/P-0753-auditoria-estagio-1/plano.md`
**Tarefa:** `AF-T10` — Um verbo `despachar` roda as conferências do despacho e recusa pela primeira que falhar
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem conduz passa a despachar a tarefa por um comando único, que roda as conferências do despacho e recusa pela primeira que falhar.

**Arquivos-alvo:** - `.claude/tools/backlog.py` - `tests/test_backlog.py` - `.claude/skills/scrum-master/SKILL.md`

**Verificação:** 1. `python .claude/tools/backlog.py despachar --help` → `exit 0` — antes `exit 2`, depois `exit 0` (antes medido pelo consultor, `DAF-41`; depois esperado) 2. `python -m pytest tests/test_backlog.py -q -k "despachar"` → `exit 0` — antes `exit 5`, depois `exit 0` (antes medido pelo consultor, `DAF-41`; depois esperado) 3. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print(t.count('backlog.py despachar'),t.count('Despachada pelo verbo'))"` → `1 1` — antes `0 0`, depois `1 1` (antes medido pelo consultor, `DAF-41`; âncoras do passo 3 e do passo 4 conferidas, uma ocorrência cada) 4. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (antes medido pelo consultor, `475 passed`, `DAF-41`; trava) 5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (antes medido pelo consultor, `DAF-41`; trava)

**Pronto quando:** - despacho de tarefa.conferências do despacho — um comando roda as conferências, marca a tarefa em curso e recusa pela primeira que falhar — Verificações 1 a 3

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAF-20`, `DAF-30`, `F-19`.
- **Depende de:** `AF-T6`, `AF-T7`, `AF-T9`
- **Operação do modelo:** `OP-10` - OP-10: Quem conduz passa a despachar a tarefa por um comando único, que roda as conferências do despacho e recusa pela primeira que falhar. - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; despacho de tarefa — Quem implementa faz o despacho entregar o card sem corte e rodar num comando só as conferências que hoje se repetem à mão, recusando pela primeira que falhar.; conferência do card — Quem implementa faz a conferência ler a situação da tarefa no estado do plano quando o card não a traz.; tarefa do loop — Ninguém altera: é nela que se vê, antes e depois, quanto de cada ciclo ainda depende da mão e da memória de quem conduz.
- **Camada e fronteira:** instrumento do kit `.claude/tools/backlog.py`; roda `modelo.py`, `card_check.py` e `review_evidence.py` como subprocessos (`sys.executable` + caminho do irmão em `Path(__file__).parent`), nunca por `import`; não importa de `tests/`.
- **Contratos/classes:** subcomando `despachar <ID> [--repo <caminho>]` (raiz padrão: a do próprio `backlog.py`, como os demais verbos). Ordem, parando na primeira recusa, com a linha `despachar: recusado — <gate>: <razão>` no stderr, exit `1` e **nada escrito**: - `tarefa` — `<ID>` é tarefa de plano (`Item` com `tipo == "tarefa"`) com status `ready`; senão a razão é `<ID> não é tarefa de plano` ou `<ID> está <status>, não ready`. - `modelo` — `python .claude/tools/modelo.py check --plano <plano> --root <repo>` sai `0` ou `2`; senão a razão é a última linha do stderr. - `card_check` — `python .claude/tools/card_check.py --plano <plano> --tarefa <ID> --root <repo>` sai `0`; senão a razão é a última linha do stderr. - `pytest --co` — `python -m pytest --co -q`, com `cwd = <repo>`, sai `0` ou `5`; senão a razão é `exit <n>`. - `ref` — se `<repo>/.claude/estado/tarefa-corrente.json` existe, é da mesma `tarefa` e tem `ref` não vazio, reaproveita esse `ref` (redespacho); senão `python .claude/tools/review_evidence.py --capturar-ref --root <repo>` sai `0` e o `ref` é a última linha não vazia do stdout; senão a razão é a última linha do stderr. - `status` — `transacionar_status(repo, modelo, <ID>, "in-progress", nota="despachada por backlog.py despachar")` com `exit_code == 0`; senão a razão é a `mensagem`. Depois do `status`: grava `<repo>/.claude/estado/tarefa-corrente.json` (criando o diretório) com `tarefa`, `projeto` (nome da pasta de `<repo>`), `modelo` (o do cabeçalho do card), `plano` (caminho do plano relativo a `<repo>`, com `/`), `despachado_em` (ISO 8601, UTC) e `ref`; e imprime, nesta ordem: `=== DESPACHO: <ID> — <título>`, os blocos `=== HANDOVER DE ...` que `handovers_para` devolve, o card como o `show <ID>` o imprime e a linha `ref=<sha>`. Exit `0`.
- **Passos:** 1. Escrever a função `despachar(repo: Path, id_: str) -> ResultadoStatus` com a ordem de `Contratos/classes` e o subcomando no `main`. 2. Escrever os três testes da seção `Testes`, sobre cópia temporária (`tmp_path`) de `tests/fixtures/backlog/pasta/` montada nesta ordem (`DAF-41`): (a) copiar a fixture; (b) copiar do repositório `.claude/tools/rdo.py` e `.claude/tools/caminhos.py` para `.claude/tools/` da cópia — o `card_check` carrega `rdo.py` de `<root>/.claude/tools/` e `rdo.py` carrega `caminhos.py` ao lado; sem eles o gate `card_check` recusa com `rdo.py: módulo não encontrado`; (c) sobrescrever `docs/plans/P-0-gama/plano.md` da cópia com o conteúdo abaixo (as quebras são as do bloco; o recuo de dois espaços não entra no arquivo) — `rdo.extrair_dossie` exige em todo card `Objetivo`, `Verificação`, `Pronto quando` e exatamente um entre `Arquivos-alvo` e `Entregável`; `GAM-T1` o `card_check` aceita e `GAM-T2` recusa (`antes` `z` contra a saída `a`); (d) `git init` e um commit inicial com tudo. A fixture do repositório não muda. Ensaiado pelo consultor na cópia assim montada: `modelo.py check` exit 2 (`ausente`), `card_check` `GAM-T1` exit 0 e `GAM-T2` exit 1, `pytest --co -q` exit 5, `review_evidence.py --capturar-ref` exit 0. ```text # P-0 — Plano gama **Prefixo das tarefas no diário:** `GAM-T<n>` ### GAM-T1 — Primeira tarefa [Sonnet · classe implementacao] - **Objetivo:** fixture. - **Entregável:** nenhum — fixture sintética, não é card vivo de plano. - **Verificação:** 1. `python -c "print('a')"` → `b` — antes `a`, depois `b` - **Pronto quando:** fixture existe. ### GAM-T2 — Segunda tarefa [Sonnet · classe implementacao] - **Objetivo:** fixture. - **Entregável:** nenhum — fixture sintética, não é card vivo de plano. - **Verificação:** 1. `python -c "print('a')"` → `b` — antes `z`, depois `b` - **Pronto quando:** fixture existe. ``` 3. Em `.claude/skills/scrum-master/SKILL.md`, Passo 3, inserir depois do parágrafo que começa por `Aprovados os quatro,` (e antes de `- **Saída:**`) o parágrafo abaixo, precedido de uma linha vazia (as quebras são as do bloco; o recuo de dois espaços entra no arquivo, como o dos parágrafos vizinhos do passo): ```text **Por comando** (`R-15`): `python .claude/tools/backlog.py despachar <ID>` roda, nesta ordem, o terceiro gate, o quarto e a coleta da suíte (`python -m pytest --co -q`), materializa `in-progress`, grava `.claude/estado/tarefa-corrente.json` com o `<ref>` e imprime o card inteiro, o bloco `HANDOVER` e a linha `ref=<sha>`. Recusa pelo primeiro gate que falhar, sem escrever nada: exit `1` **não delega**, e a linha de recusa vai à razão de `B3`. `G-PLANREADY` e o Gate de delegação continuam com quem conduz, antes do verbo; card de tíquete segue pelos passos à mão. ``` 4. No Passo 4, inserir antes do parágrafo que começa por `Invocar ` + `` `pantonic-executor` `` o parágrafo abaixo, seguido de uma linha vazia (as quebras são as do bloco; o recuo de dois espaços entra no arquivo, como o dos parágrafos vizinhos do passo): ```text Despachada pelo verbo `despachar` do passo 3, a tarefa já tem o arquivo gravado e o `<ref>` na linha `ref=<sha>` da saída: este passo só invoca o executor. ```
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 3 testes novos (referência datada: `475 passed`, medido pelo consultor em 2026-09-27, `DAF-41`; piso `478`). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Os testes rodam o verbo só sobre cópia temporária (`tmp_path`), nunca sobre o repositório real; o `pytest --co` do teste roda com `cwd` na cópia.
- **Não fazer:** não mudar `next`, `status` nem `start`; não mudar `card_check.py`, `modelo.py` nem `review_evidence.py`; não rodar o verbo sobre o repositório real para testar.
- **Contingências:** - se o `pytest --co` dentro do teste, com `cwd` na cópia temporária, sair com código fora de `0` e `5` → parar e sinalizar `blocked` razão `premissa`, colando a saída. - se um teste existente de `tests/test_backlog.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_despachar_grava_estado_e_imprime_ref` — `despachar GAM-T1` na cópia sai 0, a saída tem a linha que começa por `ref=`, o `estado.tsv` da cópia tem `GAM-T1` em `in-progress` e `tarefa-corrente.json` tem `tarefa == "GAM-T1"` e `ref` igual ao da saída. TR `test_tr_despachar_recusa_no_primeiro_gate_sem_escrever` — `GAM-T2` com `Verificação` que o `card_check` recusa: exit 1, stderr com `despachar: recusado — card_check:`, `estado.tsv` e `tarefa-corrente.json` intocados (a regra concorrente, "materializa e depois confere", deixaria `in-progress`). TF `test_tf_despachar_redespacho_reaproveita_ref` — `tarefa-corrente.json` já de `GAM-T1` com `ref` `abc`, tarefa de volta a `ready`: a saída traz `ref=abc`.
- **Fora do escopo desta tarefa:** o molde do despacho do consultor (`AF-T11`, que também edita a skill `scrum-master`).
- **Handover:** 2026-09-27 · para quem vier depois - **Entregue:** verbo 'backlog.py despachar <ID>' roda modelo check, card_check, materializa in-progress, grava tarefa-corrente.json, captura o ref e imprime DESPACHO/HANDOVER/card/ref=; recusa pela primeira conferência que falhar, sem escrever; Passos 3 e 4 do scrum-master citam o verbo - **Contrato:** o condutor despacha com um comando; redespacho reaproveita o ref; a decodificação do stderr dos irmãos ainda não é UTF-8 (ressalva do laudo, com o consultor) - **Não refazer:** nada a declarar - **Pendente:** subprocess.run do despachar sem encoding='utf-8': razão com mojibake e traceback em byte indefinido (ressalva do laudo)

## Execução

**Consumo:** 72 tool uses, 180.3 k tokens, 872.6 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

O defeito so apareceu rodando o verbo pela CLI numa copia da fixture: os tres testes chamam main() em processo e o TR confere so o prefixo da recusa, entao a decodificacao do stderr dos filhos nunca foi olhada. Verbo que orquestra irmaos por subprocess precisa de ao menos um aceite sobre o texto que atravessa a fronteira do processo.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master vai marcar a tarefa "Um verbo `despachar` roda as conferências do despacho e recusa pela primeira que falhar" como blocked, sem RDO.
Scrum master vai fechar a tarefa "Um verbo `despachar` roda as conferências do despacho e recusa pela primeira que falhar" como done: registrar estado, RDO e telemetria.
