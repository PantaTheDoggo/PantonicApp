# RDO — P-0755 · RAF-T29

# Humano

Tarefa "O controle do backlog recusa o prefixo de decisão que outro plano já declarou" concluída em 2026-09-29.
O controle do backlog passou a recusar o prefixo de decisão que outro plano já declarou.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 46/57 tarefas concluídas; próxima: "O fechamento de tarefa registra o achado pela linha de origem e avisa a falha de instrumento".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T29` — O controle do backlog recusa o prefixo de decisão que outro plano já declarou
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o controle do backlog recusar o plano que declara o mesmo prefixo de decisão que outro já declarou, nomeando o plano dono do prefixo.

**Arquivos-alvo:** - `.claude/tools/backlog.py` - `tests/test_backlog.py`

**Verificação:** 1. `python -m pytest tests/test_backlog.py -q -k prefixo_de_decisao` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - controle do backlog.prefixo de decisão repetido — a conferência recusa o segundo, nomeando o plano dono; citar o prefixo de outro plano continua permitido — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-29`; `F-23` (`PREFIXO_CAMPO_RE` lê só o prefixo das tarefas), `F-24` (34 planos, 17 declaram `**Prefixo das decisões:**`, nenhuma colisão de declaração; citar prefixo de outro plano é comum e legítimo); relatório `R-28` (auditoria reg. 17).
- **Depende de:** `RAF-T28`
- **Operação do modelo:** `OP-29` - OP-29: Quem executa faz o controle do backlog recusar o plano que declara o mesmo prefixo de decisão que outro já declarou, nomeando o plano dono do prefixo. - precisa de: controle do backlog — Quem implementa acrescenta um aviso ao tirar o plano da fila e uma recusa ao conferir, sem mudar o resultado do primeiro.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/backlog.py`, parser do cabeçalho do plano (`_parse_plano`) e verbo `check`; só biblioteca padrão. O vocabulário do `check` vai hoje de `C-1` a `C-17`; a violação nova é `C-18`. Sobre a árvore de 2026-09-28 a regra não acusa nada (medido no ensaio: nenhuma linha `C-18` no `check` do repositório). O contrato do objeto é: "Quem implementa acrescenta um aviso ao tirar o plano da fila e uma recusa ao conferir, sem mudar o resultado do primeiro."
- **Contratos/classes:** `Plano` ganha os campos `prefixo_decisoes: str | None = None` e `prefixo_decisoes_linha: int | None = None` (depois de `status_no_texto`); funções novas `_prefixo_decisoes_checks(modelo: Modelo, violacoes: list[Violacao]) -> None` e `_numero_do_plano(plano: Plano) -> tuple[int, str]`, logo antes de `check`. Quatro regras: 1. Constante nova, logo depois de `PREFIXO_CAMPO_RE`: `PREFIXO_DECISOES_RE`, que casa `**Prefixo das decisões:**`, espaço e, entre crases, `<letras e dígitos>-<n>`, capturando as letras e dígitos; comentário acima cita `R-28` e `DRF-29` do `P-0755`. 2. `_parse_plano`: no mesmo laço das 20 primeiras linhas que já lê `Status` e o prefixo das tarefas (pulando bullets), a primeira linha que casa `PREFIXO_DECISOES_RE` dá `prefixo_decisoes` e `prefixo_decisoes_linha` (número da linha, a contar de 1); os dois valores entram no construtor `Plano(...)`, logo depois de `prefixo=prefixo`. 3. `_numero_do_plano`: `(int(<dígitos de P-<n>>), plano.id)` quando o id começa por `P-` e dígitos; senão `(10**9, plano.id)`. `_prefixo_decisoes_checks`: agrupa os planos de `modelo.planos` que declaram prefixo; em cada grupo de dois ou mais, o dono é o de menor `_numero_do_plano`; para cada outro plano do grupo que não é `fora_do_corpus`, `Violacao("C-18", plano.arquivo, plano.prefixo_decisoes_linha or plano.linha_header, f"{plano.id}: prefixo de decisão '{prefixo}' já declarado por {dono.id}")`. Docstring cita `C-18`, `R-28` e `DRF-29` do `P-0755` e diz que citar não é declarar. 4. `check`: chama `_prefixo_decisoes_checks(modelo, violacoes)` logo depois do laço dos planos e antes do laço `for tiquete in modelo.tiquetes:`.
- **Passos:** 1. Acrescentar ao fim de `tests/test_backlog.py` o helper `_repo_prefixos_de_decisao(tmp_path: Path, prefixo_beta: str, texto_beta: str = "") -> Path` — copia a fixture `verde` (`_copiar_fixture(_FIXTURE_VERDE, tmp_path / "repo")`) e grava em `docs/plans/` da cópia dois planos: `P-0800-alfa.md` e `P-0801-beta.md`, cada um com a linha 1 `# <id> — Plano <nome do arquivo>`, a linha 2 vazia e a linha 3 com `**Status:**` `ready`, `**Prefixo das tarefas no diário:**` (`ALF-T<n>` e `BET-T<n>`) e `**Prefixo das decisões:**` (`DSA-<n>` e `<prefixo_beta>-<n>`), separados por ` · `, cada valor entre crases; depois uma linha vazia e `texto_beta` no `P-0801` — e os dois testes da seção `Testes`, pelo `backlog.main(["check", "--repo", <repo>])`. 2. Rodar `python -m pytest tests/test_backlog.py -q -k prefixo_de_decisao` e conferir que o TF falha e o TR passa. 3. Aplicar as quatro regras de `Contratos/classes`. 4. Rodar `python .claude/tools/backlog.py check` na raiz do repositório e conferir que nenhuma linha começa por `C-18`. 5. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Nenhuma linha que já existia em `tests/test_backlog.py` sai ou muda: o card só acrescenta ao fim do arquivo; as fixtures de `tests/fixtures/backlog/` não mudam. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não contar ocorrência de prefixo no corpo do plano (citar não é declarar); não acusar prefixo de plano legado sem o campo declarado; não mudar os códigos `C-1`..`C-17` nem a forma da linha de violação; não mexer no aviso do `drain` (`RAF-T28`).
- **Contingências:** - se um teste que já existia em `tests/test_backlog.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o passo 4 imprimir linha que começa por `C-18` → parar e sinalizar `blocked` razão `premissa`, colando a linha. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_check_prefixo_de_decisao_repetido_recusa` — `prefixo_beta="DSA"`: `check` sai 1 e há uma linha que começa por `C-18 docs/plans/P-0801-beta.md:3 — ` e contém `P-0801: prefixo de decisão 'DSA' já declarado por P-0800`; nenhuma linha `C-18 docs/plans/P-0800-alfa.md` (hoje nenhuma linha `C-18`). TR `test_tr_check_prefixo_de_decisao_citado_nao_e_colisao` — `prefixo_beta="DSB"` e o corpo do `P-0801` com `` Aplica a `DSA-3` do P-0800. ``: nenhuma linha contém `C-18` (a regra concorrente, contar ocorrências, acusaria). Suíte `tests/test_backlog.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** o aviso da diretiva no `drain` (`RAF-T28`); a colisão de prefixo próprio dos planos legados sem declaração (`DC`, `DM`, `DP`, `F-24`), que a regra não alcança por construção.
- **Handover:** 2026-09-29 · para quem vier depois - **Entregue:** .claude/tools/backlog.py: campos prefixo_decisoes/prefixo_decisoes_linha em Plano e a violação C-18 (prefixo de decisão declarado por dois planos, nomeando o dono); testes em tests/test_backlog.py - **Contrato:** C-1..C-17 inalterados; citar prefixo de outro plano segue permitido; plano legado sem o campo não é acusado - **Não refazer:** nada a declarar - **Pendente:** docstring do módulo backlog.py (linhas 3 e 7) e o comentário da linha 592 ainda dizem C-1..C-17 (achado do laudo, ao consultor)

## Execução

**Consumo:** 45 tool uses, 97.7 k tokens, 655.6 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Exercicio ponta a ponta em copias fora do repositorio confirmou a regra alem dos dois testes: tres planos com o mesmo prefixo acusam os dois nao-donos nomeando o de menor numero independente da ordem de arquivo; plano em pasta (plano.md) colide com plano plano; linha de bullet com o campo e ignorada; sobre a arvore real 15 de 35 planos declaram prefixo e nenhum repete. A assercao de exit 1 do TF nao discrimina sozinha - a fixture verde com os dois planos novos ja sai 1 por C-16/C-10 alheios -; quem discrimina e a assercao da linha C-18, que o teste tambem faz.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Tarefa "O controle do backlog recusa o prefixo de decisão que outro plano já declarou": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O controle do backlog recusa o prefixo de decisão que outro plano já declarou" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O controle do backlog recusa o prefixo de decisão que outro plano já declarou": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O controle do backlog recusa o prefixo de decisão que outro plano já declarou" como done: registrar estado, RDO e telemetria.
