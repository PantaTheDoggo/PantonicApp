# RDO — P-0755 · RAF-T27

# Humano

Tarefa "O pré-voo separa o caminho a criar do que já devia existir e não toma extensão solta por caminho" concluída em 2026-09-29.
O pré-voo passou a marcar como 'criar' o caminho que o pedido manda criar e deixou de tomar extensão solta por caminho.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 43/56 tarefas concluídas; próxima: "O controle do backlog avisa, ao drenar, a diretiva que não cita nada vivo".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T27` — O pré-voo separa o caminho a criar do que já devia existir e não toma extensão solta por caminho
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o pré-voo do pedido separar o caminho que o pedido manda criar do caminho que já devia existir, sem tomar extensão solta por caminho.

**Arquivos-alvo:** - `.claude/tools/prevoo.py` - `tests/test_prevoo.py`

**Verificação:** 1. `python -m pytest tests/test_prevoo.py -q -k conta_como_caminho` → `exit 0` — antes `exit 5`, depois `exit 0` 2. `python -m pytest tests/test_prevoo.py -q -k caminho_a_criar` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - pré-voo do pedido.o que conta como caminho — conta o que termina em barra, o que tem pasta e extensão curta, e o nome solto com uma das extensões conhecidas — Verificação 1 - pré-voo do pedido.caminho a criar — ele sai como a criar, sem derrubar o resultado; o pedido medido passa com seis linhas a criar — Verificação 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-19`; `F-22` (nove extensões; `_e_caminho` = termina numa delas ou em `/`; sobre o pedido do plano fictício, seis linhas `não`, uma delas `.txt`, e o `c.bin` ausente, exit 1); relatório `R-17` (auditoria reg. 2).
- **Depende de:** `RAF-T24`, `RAF-T24a`, `RAF-T25`, `RAF-T26`, `RAF-T26a`
- **Operação do modelo:** `OP-27` - OP-27: Quem executa faz o pré-voo do pedido separar o caminho que o pedido manda criar do caminho que já devia existir, sem tomar extensão solta por caminho. - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/prevoo.py`, só biblioteca padrão, sem import de `tests` nem de `caminhos` (`tests/conformance/test_camadas_do_kit.py`). Primeira tarefa da etapa D: nasce `blocked` até o `go` do Marco 4 (`DRF-5`), e depende dos três cards que fecham a etapa C. A saída continua `citado | existe | onde`, uma linha por item; o valor novo da coluna `existe` é `criar`, que não derruba o exit 0. O pedido é do planejador, que roda o pré-voo na Fase 0. O contrato do objeto é: "Quem implementa muda só a leitura do que é caminho e a classificação do que falta, com os testes que a provam."
- **Contratos/classes:** `_e_caminho(token: str) -> bool` (regra nova) e função nova `_caminhos_a_criar(texto: str) -> set[str]`; `main` muda só no laço dos caminhos. Três regras: 1. `_e_caminho`, com docstring que cita `R-17` e `DRF-19` do `P-0755`: verdadeiro quando o token termina em `/`; ou quando contém `/` e o último segmento (depois da última `/`) casa `\.[A-Za-z0-9]{1,5}$` (constante nova `_RE_EXTENSAO_CURTA`); ou quando não contém `/`, termina numa das nove `_EXTENSOES_CAMINHO` e não começa por `.`. 2. `_caminhos_a_criar`: constantes novas `_VERBOS_DE_CRIACAO = {"crie", "criar", "grave", "gravar", "escreva", "escrever", "gere", "gerar"}` e `_RE_FIM_DE_FRASE` = regex de `. ` (ponto e espaço) ou quebra de linha; o texto se divide em frases por essa regex; em cada frase, os tokens separados por espaço em branco passam por `_normalizar`; depois do primeiro token cujo `lower()` é um dos verbos, todo token que é caminho por `_e_caminho` entra no conjunto. 3. `main`, laço dos caminhos: caminho que existe sob a raiz sai `<caminho> | sim | <caminho>`; que não existe e está em `_caminhos_a_criar(args.texto)` sai `<caminho> | criar | —` e **não** muda o exit; que não existe e não está no conjunto sai `<caminho> | não | —` e faz o exit ser 1, como hoje. Símbolos e flags não mudam.
- **Passos:** 1. Acrescentar ao fim de `tests/test_prevoo.py` a constante `_PEDIDO_MEDIDO_R17` com o pedido do plano fictício, verbatim, em uma string só: `Crie em scratch_sonda/ duas coisas: (1) as amostras scratch_sonda/amostras/a.txt, scratch_sonda/amostras/b.txt e o binário scratch_sonda/amostras/c.bin; (2) o utilitário scratch_sonda/contar.py, que recebe caminhos de arquivo e imprime, por arquivo .txt, o número de linhas, recusando com mensagem o caminho que não existe, com os testes em tests/test_sonda_auditoria_final.py. Tudo só com biblioteca padrão.` — e os quatro testes da seção `Testes`, com `_load_prevoo` e `--root` em `tmp_path`. 2. Rodar `python -m pytest tests/test_prevoo.py -q -k "conta_como_caminho or caminho_a_criar"` e conferir que os dois TF falham e os dois TR passam. 3. Aplicar as três regras de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 4 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). Os seis testes que já existem em `tests/test_prevoo.py` continuam passando sem mudança. - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Nenhuma linha que já existia em `tests/test_prevoo.py` sai ou muda: o card só acrescenta ao fim do arquivo. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `_normalizar`, `_e_flag`, `_simbolo_de`, `_achar_simbolo` nem `_achar_flag`; não acrescentar extensão às nove de `_EXTENSOES_CAMINHO`; não mudar o cabeçalho `citado | existe | onde`; não editar a doutrina do planejador.
- **Contingências:** - se um teste que já existia em `tests/test_prevoo.py` ou em `tests/conformance/` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_prevoo_conta_como_caminho_sem_extensao_solta` — texto `leia, por arquivo .txt, o binário dados/c.bin`, raiz vazia: exit 1 e a saída exatamente `citado | existe | onde` e `dados/c.bin | não | —` (hoje: `.txt | não | —` e nenhuma linha de `dados/c.bin`). TR `test_tr_prevoo_conta_como_caminho_nome_solto_conhecido` — `notas.md` na raiz, texto `leia notas.md antes`: exit 0 e `notas.md | sim | notas.md` (a regra concorrente, exigir `/`, o perderia). TF `test_tf_prevoo_caminho_a_criar_no_pedido_medido` — `_PEDIDO_MEDIDO_R17`, raiz vazia: exit 0 e a saída exatamente o cabeçalho e as seis linhas `scratch_sonda/ | criar | —`, `scratch_sonda/amostras/a.txt | criar | —`, `scratch_sonda/amostras/b.txt | criar | —`, `scratch_sonda/amostras/c.bin | criar | —`, `scratch_sonda/contar.py | criar | —` e `tests/test_sonda_auditoria_final.py | criar | —`, nesta ordem (hoje: seis linhas `não` e exit 1). TR `test_tr_prevoo_caminho_a_criar_so_na_mesma_frase` — texto `Crie o módulo novo. Leia docs/x.md depois`: exit 1 e `docs/x.md | não | —` (a regra concorrente, verbo em qualquer ponto do texto, daria `criar`). Suíte `tests/test_prevoo.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** a doutrina do planejador sobre o pré-voo (a Fase 0 já manda rodar e colar a tabela; a linha `criar` não volta ao dono porque não é premissa ausente).
- **Handover:** 2026-09-29 · para quem vier depois - **Entregue:** .claude/tools/prevoo.py:60 (_e_caminho: extensão curta só com '/', nome solto só começando por '.'), :114-118 (_VERBOS_DE_CRIACAO, _caminhos_a_criar), :199-200 (coluna existe = criar); tests/test_prevoo.py com os TF/TR do card - **Contrato:** prevoo.py segue citado | existe | onde, uma linha por item; 'criar' não derruba o exit 0; só a biblioteca padrão - **Não refazer:** nada a declarar - **Pendente:** a docstring do módulo (prevoo.py:13-15) ainda descreve a regra antiga de caminho e só sim/nao (achado do laudo, ao consultor)

## Execução

**Consumo:** 19 tool uses, 86.0 k tokens, 378.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Exercicio ponta a ponta pela CLI, na raiz real: 'Crie .claude/tools/novo.py ... leia .claude/tools/prevoo.py. Grave docs/y.md; ... README.md' deu novo.py e y.md como criar, prevoo.py e README.md como sim, simbolo e flag inalterados, exit 1 so pelo simbolo ausente - as tres colunas e a tabela de exit seguem coerentes. Discriminacao conferida contra o prevoo.py da ref 643d75d: os dois TF saem como o card diz (.txt | nao e exit 1; seis linhas nao, com .txt no lugar de c.bin, e exit 1), e o TR da mesma frase ja passava. Bordas fieis a letra das regras, sem defeito de entrega, que o planejador pode querer ver: quebra de linha entre o verbo e o caminho tira o caminho do conjunto (gerar\ndocs/z.md sai nao); ponto sem espaco nao fecha frase (docs/a.md.Leia vira caminho a criar); o conjunto nao guarda posicao, entao 'leia docs/c.md e crie docs/c.md' sai criar; URL com extensao no ultimo segmento (https://x.com/a.html) conta como caminho.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Tarefa "O pré-voo separa o caminho a criar do que já devia existir e não toma extensão solta por caminho". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O pré-voo separa o caminho a criar do que já devia existir e não toma extensão solta por caminho" e vai executar: Quem executa faz o pré-voo do pedido separar o caminho que o pedido manda criar do caminho que já devia existir, sem tomar extensão solta por caminho.
Agente executor devolveu a tarefa "O pré-voo separa o caminho a criar do que já devia existir e não toma extensão solta por caminho": review — sem pendência.
Tarefa "O pré-voo separa o caminho a criar do que já devia existir e não toma extensão solta por caminho": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O pré-voo separa o caminho a criar do que já devia existir e não toma extensão solta por caminho" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O pré-voo separa o caminho a criar do que já devia existir e não toma extensão solta por caminho": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O pré-voo separa o caminho a criar do que já devia existir e não toma extensão solta por caminho" como done: registrar estado, RDO e telemetria.
