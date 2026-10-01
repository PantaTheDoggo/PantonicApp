# RDO — P-0755 · RAF-T19

# Humano

Tarefa "A conferência do modelo julga só a versão vigente quando pedida" concluída em 2026-09-29.
A conferência do modelo passa a poder julgar só a versão vigente quando pedida.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 30/51 tarefas concluídas; próxima: "O despacho pede à conferência do modelo só a versão vigente".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T19` — A conferência do modelo julga só a versão vigente quando pedida
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz a conferência do modelo julgar só a versão vigente quando pedida assim, deixando a versão pendente para o marco.

**Arquivos-alvo:** - `.claude/tools/modelo.py` - `tests/test_modelo.py`

**Verificação:** 1. `python -m pytest tests/test_modelo.py -q -k so_vigente` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - conferência do modelo.versões julgadas — pode julgar só a vigente quando pedida assim; sem o pedido, continua julgando as duas — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-1`, `DRF-14`, `DRF-37`; `F-19` (com a pendente presente, o `check` valida a `## 1A` e prefixa as violações com `1A: `; o `V1` da operação sem card vale em qualquer bloco); relatório `R-04` (auditoria reg. 31 e 32).
- **Depende de:** `RAF-T18`
- **Operação do modelo:** `OP-19` - OP-19: Quem executa faz a conferência do modelo julgar só a versão vigente quando pedida assim, deixando a versão pendente para o marco. - precisa de: escolhas do dono sobre o roteiro — Ninguém altera: fixam a rota das operações que dependem delas.; despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/modelo.py`, só biblioteca padrão; carrega o `backlog.py` da raiz dada por `--root` (`_load_backlog`) e chama `backlog._parse_plano`, que exige o plano sob essa raiz. Primeira tarefa da etapa C: nasce `blocked` até o `go` do Marco 3 (`DRF-5`). O `check` sem a flag nova segue julgando as duas versões; quem passa a pedir a flag é o despacho (`RAF-T20`). O contrato do objeto é: "Quem implementa acrescenta à conferência o que cada operação pede, sem mudar o que ela já julga quando chamada como hoje."
- **Contratos/classes:** `validar(modelo: Modelo, plano, modelo_pendente: Modelo | None = None, *, pendente: bool = False, so_vigente: bool = False) -> list[str]` (parâmetro novo `so_vigente`) e `verbo_check(args) -> int`. Quatro regras: 1. O subparser `check` de `main` ganha a opção `--so-vigente` (`action="store_true"`, ajuda `Julga só a '## 1' (versão vigente); a '## 1A' fica para o marco (R-04).`). 2. `verbo_check`, com `--so-vigente`: chama `validar(modelo, plano, modelo_pendente, so_vigente=True)` e **não** acrescenta as violações `1A: ` da pendente; sem a flag, tudo como hoje. 3. `validar`, com `so_vigente=True`: a violação `V20` (pendente fora de sequência) não se emite; as demais, como hoje. 4. `validar`, violação `V4` (`V4 <ID> — operação inexistente OP-<n>`), com ou sem a flag (`DRF-37`): conjunto novo `numeros_pendente` = os números das operações de `modelo_pendente` (vazio sem pendente), e `V4` só se emite quando o número citado não está em `numeros_operacoes` nem em `numeros_pendente`. O comentário acima do conjunto cita `DRF-37` do `P-0755`.
- **Passos:** 1. Acrescentar ao fim de `tests/test_modelo.py`, nesta ordem: o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo deste card e começa na coluna 0); o helper `_raiz_modelo_pendente(tmp_path: Path, tarefas_op2: str = "", card_op2: bool = False, texto_op1: str = "Primeira operação da fixture.", texto_op2: str = "Segunda operação, nova na versão pendente.", op_card2: str = "OP-2") -> tuple[Path, Path]`, que cria `tmp_path/raiz/.claude/tools/` com cópias de `backlog.py` e `caminhos.py` do repositório (`shutil.copy2` a partir de `_ROOT`), grava em `tmp_path/raiz/docs/plans/P-0999-pendente.md` o `_MODELO_PENDENTE_TEXTO` com `@TAREFAS_OP2@` trocado por `tarefas_op2` e `@TEXTO_OP1@` por `texto_op1`, seguido, com `card_op2`, do `_CARD_OP2_TEXTO` com `@OP_CARD2@` trocado por `op_card2` e `@TEXTO_OP2@` por `texto_op2`, e devolve `(raiz, plano)`; e os quatro testes da seção `Testes`. ```python _MODELO_PENDENTE_TEXTO = """# P-0999 — Plano com versão pendente **Prefixo das tarefas no diário:** `EX-T<n>` ## 1. Modelo conceitual **Estado do modelo:** versão 1 · 2026-09-10 · autor: modelador · 1 operações · 2 propriedades · situação: vigente ### 1.1 Objetos | objeto | o que é | propriedades | contrato | origem | lastro | |---|---|---|---|---|---| | insumo | dado de entrada | status | um registro por rodada | externo | lastro da fixture | | produto | o produto da primeira operação | status | um registro validado | OP-1 | lastro da fixture | ### 1.2 Fluxo de operações - **OP-1** — Primeira operação da fixture. - `precisa de: insumo` · `altera: produto.status` · `tarefas: EX-T1` ### 1.3 Estado inicial e estado final | propriedade | estado inicial | estado final | |---|---|---| | insumo.status | lido | lido | | produto.status | rascunho | validado | ### 1.4 Registro de versões | versão | data | situação | por | |---|---|---|---| | 1 | 2026-09-10 | vigente | modelador | | 2 | 2026-09-21 | pendente | modelador, emenda | ## 1A. Modelo conceitual — versão pendente de validação **Estado do modelo:** versão 2 · 2026-09-21 · autor: modelador · 2 operações · 3 propriedades · situação: pendente ### 1.1 Objetos | objeto | o que é | propriedades | contrato | origem | lastro | |---|---|---|---|---|---| | insumo | dado de entrada | status | um registro por rodada | externo | lastro da fixture | | produto | o produto da primeira operação | status | um registro validado | OP-1 | lastro da fixture | | resultado | o produto da segunda operação | nível | um relatório derivado | OP-2 | lastro da fixture | ### 1.2 Fluxo de operações - **OP-1** — Primeira operação da fixture. - `precisa de: insumo` · `altera: produto.status` · `tarefas: EX-T1` - **OP-2** — Segunda operação, nova na versão pendente. - `precisa de: produto` · `altera: resultado.nível` · `tarefas: @TAREFAS_OP2@` ### 1.3 Estado inicial e estado final | propriedade | estado inicial | estado final | |---|---|---| | insumo.status | lido | lido | | produto.status | rascunho | validado | | resultado.nível | inicial | alto | ## 5. Tarefas ### EX-T1 — Um [Sonnet · classe mecanica] - **Operação do modelo:** `OP-1` - OP-1: @TEXTO_OP1@ - precisa de: insumo — um registro por rodada """ _CARD_OP2_TEXTO = """ ### EX-T2 — Dois [Sonnet · classe mecanica] - **Operação do modelo:** `@OP_CARD2@` - @OP_CARD2@: @TEXTO_OP2@ - precisa de: produto — um registro validado """ ``` 2. Rodar `python -m pytest tests/test_modelo.py -q -k so_vigente` e conferir que os três testes que passam `--so-vigente` falham (a flag não existe) e o `test_tr_sem_so_vigente_julga_as_duas_versoes` passa. 3. Aplicar as quatro regras de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 4 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - O `check` sem `--so-vigente` continua saindo como hoje sobre as fixtures de `tests/fixtures/modelo/`, exceto a linha `V4 EX-T2 — operação inexistente OP-2` de `fluxo-pendente.md`, que sai pela regra 4; nenhum teste existente afirma essa linha. - Nenhuma linha que já existia em `tests/test_modelo.py` sai ou muda: o card só acrescenta ao fim do arquivo; as fixtures de `tests/fixtures/modelo/` não mudam. - Os testes gravam só em `tmp_path`. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não editar `.claude/tools/backlog.py` (o despacho passa a pedir a flag na `RAF-T20`); não acrescentar violação nova ao vocabulário (a `V22` é da `RAF-T21`); não mexer em `_diff_fluxo` nem em `_diff_estado` (`RAF-T22`); não mudar a saída `modelo: OK — …` nem a `modelo: FALHOU — …`.
- **Contingências:** - se um teste que já existia em `tests/test_modelo.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_so_vigente_ignora_a_versao_pendente` — `tarefas_op2` vazio (a `OP-2` da `## 1A` sem card): `check --so-vigente --root <raiz>` sai 0 com `modelo: OK — 1 operações` no stdout e sem `1A:` no stderr (hoje o argparse recusa a flag e sai 2). TR `test_tr_sem_so_vigente_julga_as_duas_versoes` — o mesmo plano, sem a flag: sai 1 com `1A: V1 OP-2 — operação sem tarefa` no stderr (a regra concorrente, julgar sempre só a vigente, sairia 0). TF `test_tf_so_vigente_card_da_operacao_nova_nao_e_v4` — `tarefas_op2="EX-T2"` e o card `EX-T2` citando a `OP-2`: `check` sai 0 sem a flag e sai 0 com ela (hoje sai 1 com `V4 EX-T2 — operação inexistente OP-2`). TR `test_tr_so_vigente_operacao_ausente_das_duas_segue_v4` — o card `EX-T2` cita `OP-9`: `check --so-vigente` sai 1 com `V4 EX-T2 — operação inexistente OP-9`. Suíte `tests/test_modelo.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** o despacho com a flag (`RAF-T20`); a violação do texto copiado divergente (`RAF-T21`); a diferença entre versões (`RAF-T22`); a promoção no marco (`RAF-T23`).
- **Handover:** 2026-09-29 · para `RAF-T20` - **Entregue:** modelo.py check --so-vigente julga só a versão vigente (sem V20 e sem as violações 1A:); V4 aceita operação presente só na pendente (DRF-37), com ou sem a flag; 4 testes novos, suíte 586 - **Contrato:** sem a flag o check segue julgando as duas versões, exceto o V4 de operação só da pendente (versão 3 pendente do modelo acerta o contrato) - **Não refazer:** --so-vigente, numeros_pendente e os testes - **Pendente:** nenhum

## Execução

**Consumo:** 1 tool uses, 0.4 k tokens, 11.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

A linha de retorno do executor so saiu no formato fixo depois de um reenvio (a primeira resposta trouxe prosa antes da linha); a telemetria carrega tres linhas usage para a tarefa. Informativo, sem efeito na marcacao.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Tarefa "A conferência do modelo julga só a versão vigente quando pedida". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "A conferência do modelo julga só a versão vigente quando pedida" e vai executar: Quem executa faz a conferência do modelo julgar só a versão vigente quando pedida assim, deixando a versão pendente para o marco.
Agente executor devolveu a tarefa "A conferência do modelo julga só a versão vigente quando pedida": RAF-T19 entregue..
Tarefa "A conferência do modelo julga só a versão vigente quando pedida": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A conferência do modelo julga só a versão vigente quando pedida" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A conferência do modelo julga só a versão vigente quando pedida": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Agente modelador recebe a tarefa "A conferência do modelo julga só a versão vigente quando pedida" e vai fazer conflito no modelo.
Agente modelador devolveu a tarefa "A conferência do modelo julga só a versão vigente quando pedida": Ato de conflito concluído. O texto do modelo passa a acompanhar a entrega, numa versão pendente nova (versão 3). A entrega da RAF-T19 não vira drift, porque exe….
Scrum master vai fechar a tarefa "A conferência do modelo julga só a versão vigente quando pedida" como done: registrar estado, RDO e telemetria.
