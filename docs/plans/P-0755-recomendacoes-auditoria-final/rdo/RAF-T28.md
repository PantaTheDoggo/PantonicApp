# RDO — P-0755 · RAF-T28

# Humano

Tarefa "O controle do backlog avisa, ao drenar, a diretiva que não cita nada vivo" concluída em 2026-09-29.
O controle do backlog passou a avisar, ao drenar, quando a diretiva de prioridade não cita nenhum plano ou tarefa ainda viva.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 45/57 tarefas concluídas; próxima: "O controle do backlog recusa o prefixo de decisão que outro plano já declarou".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T28` — O controle do backlog avisa, ao drenar, a diretiva que não cita nada vivo
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o controle do backlog avisar, ao tirar um plano da fila, que a diretiva de priorização não cita nada vivo nem o plano que saiu.

**Arquivos-alvo:** - `.claude/tools/backlog.py` - `tests/test_backlog.py`

**Verificação:** 1. `python -m pytest tests/test_backlog.py -q -k aviso_diretiva` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - controle do backlog.aviso de diretiva desatualizada — um aviso diz que a diretiva não cita nada vivo nem o plano que saiu; o resultado do comando não muda — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-20`; `F-23` (`DIRETIVA_RE`; `_parse_diretiva` lê os ids entre crases antes de ` — `; `transacionar_drain`, chamado pelas skills `passagem-de-bastao` e `diario-de-obras`); relatório `R-18` (auditoria reg. 16: a diretiva seguiu apontando o plano que já tinha saído).
- **Depende de:** `RAF-T27`
- **Operação do modelo:** `OP-28` - OP-28: Quem executa faz o controle do backlog avisar, ao tirar um plano da fila, que a diretiva de priorização não cita nada vivo nem o plano que saiu. - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/backlog.py`, função `transacionar_drain` (verbo `drain`); só biblioteca padrão. O aviso é só texto no stderr: o `drain` continua escrevendo o diário, o inbox e o histórico como hoje, com o mesmo exit e a mesma saída no stdout. A reescrita da diretiva continua ato de quem conduz (`backlog.py diretiva`). O contrato do objeto é: "Quem implementa acrescenta um aviso ao tirar o plano da fila e uma recusa ao conferir, sem mudar o resultado do primeiro."
- **Contratos/classes:** `transacionar_drain(repo: Path, modelo: Modelo, inbox_planos: Path, historico: Path, data: str | None = None) -> ResultadoStatus` — assinatura inalterada; função nova `_id_vivo(modelo: Modelo, id_: str) -> bool`, logo antes de `_localizar`. Duas regras: 1. `_id_vivo`: `_localizar(modelo, id_)`; `None` → `False`; senão, vivo quando o primeiro termo do `status` (texto até o primeiro espaço) não é `done`, `cancelled` nem `superseded` (status vazio conta como vivo). Docstring cita `DRF-20` do `P-0755`. 2. `transacionar_drain`, logo depois das três chamadas a `_escrever_atomico` e antes do cálculo de `arquivos`: quando o diário (as `diario_linhas` já com as linhas de índice novas) tem a linha da diretiva (`DIRETIVA_RE`) e nenhum id de `modelo.diretiva_ids` é vivo por `_id_vivo`, para cada plano drenado, na ordem do inbox, cujo id não está em `modelo.diretiva_ids`, imprime no stderr `drain: aviso — a diretiva de priorização não cita nenhum id vivo nem <P-id>`. Sem linha de diretiva, nenhum aviso. O comentário acima do bloco cita `R-18` e `DRF-20` do `P-0755`.
- **Passos:** 1. Acrescentar ao fim de `tests/test_backlog.py` o helper `_repo_drain_com_diretiva(tmp_path: Path, ids_da_diretiva: str) -> Path` — copia a fixture `next_tk90` (`_copiar_fixture(_FIXTURE_NEXT_TK90, tmp_path / "repo")`), grava o plano `P-0800-alfa.md` com `_escrever_plano(repo, "P-0800-alfa.md", "P-0800", "Plano alfa de teste", "ALF", "ready")`, põe no inbox a linha `- docs/plans/P-0800-alfa.md — plano alfa de teste` (`_inbox_com_linhas`), chama `_inserir_bloco_gerado(repo)` e insere no diário, como segunda linha, `**Diretiva de priorização:** <ids_da_diretiva> — texto da fixture.` — e os dois testes da seção `Testes`, pelo `backlog.main(["drain", "--repo", <repo>, "--data", "2026-09-28"])`. 2. Rodar `python -m pytest tests/test_backlog.py -q -k aviso_diretiva` e conferir que o TF falha e o TR passa. 3. Aplicar as duas regras de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). Os testes de `drain` que já existem (fixture sem linha de diretiva) continuam passando sem mudança. - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Nenhuma linha que já existia em `tests/test_backlog.py` sai ou muda: o card só acrescenta ao fim do arquivo; as fixtures de `tests/fixtures/backlog/` não mudam (só a cópia em `tmp_path`). - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não reescrever a diretiva no `drain`; não mudar o exit, o stdout nem os arquivos que o `drain` escreve; não mexer em `transacionar_diretiva` nem em `_parse_diretiva`; não acrescentar a recusa do prefixo de decisão (é da `RAF-T29`).
- **Contingências:** - se um teste que já existia em `tests/test_backlog.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_drain_aviso_diretiva_sem_id_vivo` — diretiva `` `P-0001` `` (id que não existe na fixture): `drain` sai 0 e o stderr contém `drain: aviso — a diretiva de priorização não cita nenhum id vivo nem P-0800` (hoje sai 0 sem aviso). TR `test_tr_drain_aviso_diretiva_com_id_vivo_ou_drenado_cala` — diretiva `` `P-0090` `` (plano `ready` da fixture) e, em outra cópia, `` `P-0800` `` (o drenado): os dois saem 0 e nenhum stderr contém `drain: aviso` (a regra concorrente, avisar a cada drenagem, avisaria). Suíte `tests/test_backlog.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** a recusa do prefixo de decisão repetido (`RAF-T29`); a reescrita da diretiva, ato de quem conduz.
- **Handover:** 2026-09-29 · para quem vier depois - **Entregue:** .claude/tools/backlog.py:1044 (_id_vivo) e o aviso de diretiva sem id vivo em transacionar_drain (:1978); testes em tests/test_backlog.py - **Contrato:** transacionar_drain com assinatura inalterada; o aviso não muda o exit do drain - **Não refazer:** nada a declarar - **Pendente:** nenhum

## Execução

**Consumo:** 35 tool uses, 90.9 k tokens, 430.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Tarefa "O controle do backlog avisa, ao drenar, a diretiva que não cita nada vivo": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O controle do backlog avisa, ao drenar, a diretiva que não cita nada vivo" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O controle do backlog avisa, ao drenar, a diretiva que não cita nada vivo": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O controle do backlog avisa, ao drenar, a diretiva que não cita nada vivo" como done: registrar estado, RDO e telemetria.
