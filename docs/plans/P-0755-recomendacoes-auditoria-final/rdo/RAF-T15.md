# RDO — P-0755 · RAF-T15

# Humano

Tarefa "A medida gravada fica na pasta do plano da árvore medida, com o momento no nome" concluída em 2026-09-29.
A medida gravada pela conferência do card passa a ficar na pasta do plano da árvore medida, com o momento no nome.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 26/51 tarefas concluídas; próxima: "O planejador mede o antes do card dependente na cópia com os anteriores aplicados".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T15` — A medida gravada fica na pasta do plano da árvore medida, com o momento no nome
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz a medida gravada do card ficar na pasta do plano da árvore medida, com o momento da medida no nome, onde o dossiê de evidência a encontra.

**Arquivos-alvo:** - `.claude/tools/caminhos.py` - `.claude/tools/card_check.py` - `.claude/tools/review_evidence.py` - `tests/test_caminhos.py` - `tests/test_card_check.py` - `tests/test_review_evidence.py`

**Verificação:** 1. `python -m pytest tests/test_caminhos.py -q -k destino_medida_na_raiz` → `exit 0` — antes `exit 5`, depois `exit 0` 2. `python -m pytest tests/test_card_check.py -q -k medida_gravada_com_o_mundo` → `exit 0` — antes `exit 5`, depois `exit 0` 3. `python -m pytest tests/test_review_evidence.py -q -k medida_com_mundo` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - medida gravada do card.pasta em que é gravada — a medida fica na pasta do plano dentro da árvore que foi medida — Verificação 1 - medida gravada do card.momento no nome — o nome diz o momento, e as duas convivem — Verificação 2 - medida gravada do card.leitura pelo revisor — o revisor lê a de depois, na falta dela a de antes, e por último as vinte já gravadas com o nome antigo — Verificação 3

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-30`; `F-15` (hoje a pasta vem do `--plano`; 20 medidas versionadas com o nome sem mundo em `docs/plans/P-0753-auditoria-estagio-1/evidencia/`); relatório `R-05` (auditoria reg. 35).
- **Depende de:** `RAF-T11a`, `RAF-T14`, `RAF-T12a`
- **Operação do modelo:** `OP-15` - OP-15: Quem executa faz a medida gravada do card ficar na pasta do plano da árvore medida, com o momento da medida no nome, onde o dossiê de evidência a encontra. - precisa de: conferência de verificação do card — Quem implementa amplia o que a conferência aceita sem deixar de ler os cards já escritos na forma antiga.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumentos do kit — a residência dos caminhos `.claude/tools/caminhos.py` (a regra mora só em `destino_medida`), o escritor `.claude/tools/card_check.py` (`--gravar` sem caminho) e o leitor `.claude/tools/review_evidence.py` (`montar_documento`); só biblioteca padrão; os dois instrumentos carregam `caminhos.py` por caminho. As 20 medidas antigas do `P-0753` ficam como estão e seguem legíveis pelo nome sem mundo. O contrato do objeto é: "Quem implementa muda onde e com que nome a medida se grava, e faz o revisor achar tanto a nova quanto as vinte já gravadas com o nome antigo."
- **Contratos/classes:** três regras: 1. `caminhos.destino_medida(raiz: Path, plano_path: Path, tarefa: str, mundo: str | None = None) -> Path` — plano em pasta (`pasta_do_plano(plano_path)` não `None`): `planos_dir(raiz) / <nome da pasta do plano> / "evidencia" / "<P-id>-<tarefa>-medida<sufixo>.json"`; plano legado ou tíquete: `<raiz>/docs/RDO/evidencia/<id ou stem>-<tarefa>-medida<sufixo>.json` (a regra de `<id ou stem>` de hoje); `<sufixo>` é `-<mundo>` quando `mundo` é dado e vazio quando é `None`. O comentário acima da função passa a descrever a regra nova. 2. `card_check.py`, `main`: `--gravar` sem caminho grava em `_caminhos.destino_medida(args.root, args.plano, args.tarefa, medida["mundo"])` — o mundo efetivo da medida (o de `--mundo` ou o derivado do status); o texto de ajuda do `--gravar` cita `<mundo>`. Com caminho dado, nada muda. 3. `review_evidence.py`, `montar_documento`: a medida lida é a primeira que existe desta lista, nesta ordem — com `dir_evidencia` dado: `<dir>/<plano_id>-<ID>-medida-depois.json`, `-medida-antes.json`, `-medida.json`; e, sempre depois: `destino_medida(root, plano_path, <ID>, "depois")`, `(…, "antes")`, `(…, None)`; sem nenhuma, o primeiro da lista vai para `secao_medida_do_executor`, que já imprime `ausente`. O bloco da `RAF-T7` (medida ao lado do `--out`, e na falta dela `destino_medida`) é substituído por esta lista, que o mantém: a do lado do `--out` vence.
- **Passos:** 1. Em `tests/test_caminhos.py`, no teste `test_tf_destino_medida_tres_residencias`, trocar o valor esperado da terceira asserção, `Path("docs/plans/P-0002-y") / "evidencia" / "P-0002-T2-medida.json"`, por `raiz / "docs" / "plans" / "P-0002-y" / "evidencia" / "P-0002-T2-medida.json"`, e o docstring do teste pelas três linhas do bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os quatro espaços do corpo da função) — o significado mudou pela `R-05`, e a asserção se reescreve, não se remove. ```text """`TK-92a` — `destino_medida` cobre as três residências pela mesma função: tíquete do diário e plano legado caem em `<raiz>/docs/RDO/evidencia`, plano em pasta grava na pasta do plano sob a raiz, em `<raiz>/docs/plans/<pasta>/evidencia` (`R-05`, RAF-T15).""" ``` 2. Em `tests/test_card_check.py`, no teste `test_tf_gravar_sem_caminho_grava_no_destino_derivado`, trocar o nome `DIARIO_DE_OBRAS-CX-T1-medida.json` por `DIARIO_DE_OBRAS-CX-T1-medida-antes.json` na linha `destino = ...` e no docstring, acrescentando ao docstring que o nome leva o mundo desde a RAF-T15 (`R-05`) — o card `CX-T1` da fixture compara o mundo `antes`. 3. Acrescentar ao fim de `tests/test_caminhos.py`, `tests/test_card_check.py` e `tests/test_review_evidence.py` os testes da seção `Testes` (em `tests/test_review_evidence.py`, com o helper `_gravar_medida(caminho: Path, exit_medido: int) -> None`, reusando `_plano_em_pasta_com_medida` da `RAF-T7`). 4. Rodar `python -m pytest tests/test_caminhos.py tests/test_card_check.py tests/test_review_evidence.py -q -k "destino_medida or medida_gravada_com_o_mundo or medida_com_mundo or gravar_sem_caminho"` e conferir que os três TF e os dois testes reescritos falham e o TR passa. 5. Aplicar as três regras de `Contratos/classes`. 6. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 4 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Nos três arquivos de teste, as únicas linhas que já existiam e mudam são as dos passos 1 e 2; o resto só se acrescenta ao fim. - Os testes gravam só em `tmp_path`; nenhum grava em `docs/`. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/` (inclusive as 20 medidas com o nome antigo, que não se renomeiam), `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não renomear nem mover medida já gravada; não mudar `destino_evidencia`, `destino_rdo` nem `destino_laudo`; não mudar a forma da seção `## Medida do executor`; não editar a doutrina do planejador (a gravação dos dois mundos na rodada é da `RAF-T18`).
- **Contingências:** - se um teste que já existia na suíte, fora os reescritos nos passos 1 e 2, cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_destino_medida_na_raiz_com_o_mundo` (em `tests/test_caminhos.py`) — raiz `/copia`, plano `/real/docs/plans/P-0002-y/plano.md`, tarefa `T2`, mundo `depois`: `/copia/docs/plans/P-0002-y/evidencia/P-0002-T2-medida-depois.json`; plano legado `/real/docs/plans/P-0001-x.md`, `T1`, `antes`: `/copia/docs/RDO/evidencia/P-0001-T1-medida-antes.json` (hoje a função não aceita o mundo e a pasta vem de `/real`). TF `test_tf_medida_gravada_com_o_mundo_na_pasta_da_raiz` (em `tests/test_card_check.py`) — plano em pasta `P-0007-z` numa árvore `real`, `--root` numa árvore `copia` com `rdo.py` e `caminhos.py`, `--gravar` sem caminho rodado com `--mundo antes` e com `--mundo depois`: a pasta `copia/docs/plans/P-0007-z/evidencia/` tem exatamente `P-0007-RX-T1-medida-antes.json` e `P-0007-RX-T1-medida-depois.json`, e `real/docs/plans/P-0007-z/evidencia` não existe (hoje grava um arquivo só, sem mundo, na árvore `real`). TF `test_tf_medida_com_mundo_lida_na_ordem` (em `tests/test_review_evidence.py`) — plano `P-0999-teste` com a medida sem mundo de `exit` 7; com `-medida-antes.json` de `exit` 5, o documento traz a linha com `5`; com `-medida-depois.json` de `exit` 6 também, traz a linha com `6` (hoje traz `7` nos dois). TR `test_tr_medida_com_mundo_sem_mundo_ainda_lida` — só a medida sem mundo: o documento traz a linha com `7`. Suítes `tests/test_caminhos.py`, `tests/test_card_check.py`, `tests/test_review_evidence.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** a regra do planejador de gravar os dois mundos na rodada de replanejamento (`RAF-T18`); a árvore em que o card dependente mede o `antes` (`RAF-T16`).
- **Handover:** 2026-09-29 · para quem vier depois - **Entregue:** card_check/caminhos/review_evidence: a medida gravada fica na pasta do plano da árvore medida, com o momento no nome (P-<n>-<ID>-medida-<antes|depois>.json), e o leitor do review_evidence a encontra ali (ver RDO RAF-T15) - **Contrato:** medida de antes e de depois coexistem sem se sobrescrever, no plano da árvore medida - **Não refazer:** o destino da medida e o leitor - **Pendente:** nenhum

## Execução

**Consumo:** 42 tool uses, 111.9 k tokens, 485.4 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Exercicio ponta a ponta fora do repo (arvore real com plano em pasta e plano legado, --root numa copia com rdo.py/caminhos.py da entrega): card_check --gravar sem caminho grava na pasta do plano sob a copia com -antes/-depois no nome (mundo de --mundo ou derivado do status), plano legado cai em copia/docs/RDO/evidencia com -antes, --gravar com caminho segue inalterado, e a arvore real nao ganha pasta de evidencia; montar_documento le a de depois, na falta dela a de antes, e a medida sem mundo ao lado do --out vence a da raiz, como o contrato 3 manda; as 20 medidas sem mundo do P-0753 seguem resolvidas por destino_medida(..., None) (20 de 20). O proprio dossie desta revisao ja leu P-0755-RAF-T15-medida-depois.json pelo caminho novo. Nota fora do card: em plano em pasta sem estado.tsv o mundo derivado e antes mesmo com bullet Status done (rdo._status_atual le o estado.tsv da arvore do --plano, nao da --root) - comportamento anterior, nao tocado pela entrega.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "A conferência do card roda o git de leitura contra o recorte do despacho" e vai pegar a tarefa "A medida gravada fica na pasta do plano da árvore medida, com o momento no nome".
Tarefa "A medida gravada fica na pasta do plano da árvore medida, com o momento no nome". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "A medida gravada fica na pasta do plano da árvore medida, com o momento no nome" e vai executar: Quem executa faz a medida gravada do card ficar na pasta do plano da árvore medida, com o momento da medida no nome, onde o dossiê de evidência a encontra.
Agente executor devolveu a tarefa "A medida gravada fica na pasta do plano da árvore medida, com o momento no nome": review — sem pendência.
Tarefa "A medida gravada fica na pasta do plano da árvore medida, com o momento no nome": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A medida gravada fica na pasta do plano da árvore medida, com o momento no nome" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A medida gravada fica na pasta do plano da árvore medida, com o momento no nome": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "A medida gravada fica na pasta do plano da árvore medida, com o momento no nome" como done: registrar estado, RDO e telemetria.
