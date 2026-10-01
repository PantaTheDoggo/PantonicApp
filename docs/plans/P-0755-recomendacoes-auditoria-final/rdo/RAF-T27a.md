# RDO — P-0755 · RAF-T27a

# Humano

Tarefa "O docstring do módulo do pré-voo diz o que conta como caminho e quando o caminho sai a criar" concluída em 2026-09-29.
A documentação do pré-voo passou a descrever o que conta como caminho e quando ele sai como 'criar'.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 44/57 tarefas concluídas; próxima: "O controle do backlog avisa, ao drenar, a diretiva que não cita nada vivo".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T27a` — O docstring do módulo do pré-voo diz o que conta como caminho e quando o caminho sai a criar
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o docstring do módulo do pré-voo do pedido dizer as três regras que a `RAF-T27` entregou: o que conta como caminho, o valor `criar` pelo verbo na mesma frase e o exit que ele não derruba.

**Arquivos-alvo:** - `.claude/tools/prevoo.py`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/tools/prevoo.py').read_text(encoding='utf-8');print('docstring=%d-%d-%d linhas=%d'%(t.count('ou terminado em'),t.count('de 1 a 5 letras ou dígitos'),t.count('não derruba o exit 0'),len(t.splitlines())))"` → `docstring=0-1-1 linhas=227` — antes `docstring=1-0-0 linhas=222`, depois `docstring=0-1-1 linhas=227`

**Pronto quando:** - pré-voo do pedido.o que conta como caminho — o docstring do módulo diz a barra final, a pasta com extensão curta e o nome solto com uma das nove extensões que não começa por ponto — Verificação 1 - pré-voo do pedido.caminho a criar — o docstring do módulo diz o valor criar pelo verbo na mesma frase, que não derruba o exit 0 — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-66`; `AE-183` (laudo da `RAF-T27`, ressalva 91); `DRF-19`; relatório `R-17`.
- **Depende de:** `RAF-T27`
- **Operação do modelo:** `OP-27` - OP-27: Quem executa faz o pré-voo do pedido separar o caminho que o pedido manda criar do caminho que já devia existir, sem tomar extensão solta por caminho. - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta ou troca só a regra que a operação pede, deixando as demais como estão.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** texto do instrumento `.claude/tools/prevoo.py` — o item `caminhos` do docstring do módulo (linhas 13-15); nenhum comportamento muda. A `RAF-T27` trocou só o docstring de `_e_caminho` e escreveu o de `_caminhos_a_criar` (as regras do card nomearam só eles); o docstring do módulo seguiu dizendo que caminho é o token terminado numa das nove extensões ou em `/`, sem o valor `criar`.
- **Passos:** 1. No docstring do módulo de `.claude/tools/prevoo.py`, trocar as três linhas do texto antigo pelas oito do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card, e os dois espaços que sobram no começo das linhas de continuação entram no arquivo). Texto antigo: ```text - **caminhos** — token terminado em `.py`, `.md`, `.ps1`, `.json`, `.tsv`, `.txt`, `.yml`, `.yaml` ou `.toml`, ou terminado em `/`; existe quando `(<root> / <token>)` existe; `onde` é o próprio caminho. ``` Texto novo: ```text - **caminhos** — token terminado em `/`; ou com `/` e o último segmento terminado numa extensão de 1 a 5 letras ou dígitos; ou, sem `/`, terminado em `.py`, `.md`, `.ps1`, `.json`, `.tsv`, `.txt`, `.yml`, `.yaml` ou `.toml` e não começado por `.` (`R-17` e `DRF-19` do `P-0755`); existe (`sim`) quando `(<root> / <token>)` existe, e `onde` é o próprio caminho; o que não existe sai `criar` quando a mesma frase (texto entre `. ` ou quebra de linha) o traz depois de um verbo de criação (`crie`, `criar`, `grave`, `gravar`, `escreva`, `escrever`, `gere`, `gerar`, sem distinção de caixa), e `criar` não derruba o exit 0; o que não existe e o pedido não manda criar sai `não` e, como o símbolo e a flag ausentes, faz o exit ser 1. ``` 2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Em `.claude/tools/prevoo.py` só mudam as três linhas do texto antigo: nenhum código, nome, regex, constante nem outro docstring muda; o fim de linha do arquivo não muda (hoje CRLF na árvore; o git normaliza no `add`, `eol=lf`). - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar os docstrings de `_e_caminho` e de `_caminhos_a_criar` (a `RAF-T27` já os escreveu); não mudar os itens `símbolos` e `flags` nem o parágrafo da normalização; não tocar `tests/test_prevoo.py`.
- **Contingências:** - se o texto antigo do passo 1 não existir verbatim → parar e sinalizar `blocked` razão `premissa`, nomeando o passo. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo (nenhum teste lê o docstring do módulo); `tests/test_prevoo.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** o texto da `RAF-T27` (`done`), que fica como executado; a doutrina do planejador sobre o pré-voo.
- **Handover:** 2026-09-29 · para quem vier depois - **Entregue:** .claude/tools/prevoo.py docstring do módulo, item caminhos: as três regras de caminho, o valor criar (verbo de criação antes, na mesma frase, sem derrubar o exit 0) e o nao que faz exit 1; fim de linha CRLF preservado - **Contrato:** o cabeçalho do prevoo.py descreve o comportamento entregue pela RAF-T27 - **Não refazer:** nada a declarar - **Pendente:** nenhum

## Execução

**Consumo:** 16 tool uses, 57.3 k tokens, 337.8 s (fonte: `<usage>` do encerramento)

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

Tarefa "O docstring do módulo do pré-voo diz o que conta como caminho e quando o caminho sai a criar": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O docstring do módulo do pré-voo diz o que conta como caminho e quando o caminho sai a criar" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O docstring do módulo do pré-voo diz o que conta como caminho e quando o caminho sai a criar": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O docstring do módulo do pré-voo diz o que conta como caminho e quando o caminho sai a criar" como done: registrar estado, RDO e telemetria.
