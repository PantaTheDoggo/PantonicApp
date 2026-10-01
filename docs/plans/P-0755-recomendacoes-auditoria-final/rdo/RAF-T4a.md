# RDO — P-0755 · RAF-T4a

# Humano

Tarefa "O gate de delegação e a entrada do Passo 4 deixam de mandar re-derivar e copiar" concluída em 2026-09-28.
O gate de delegação e a entrada do Passo 4 deixam de mandar reconferir âncoras e copiar o card na tarefa de plano.
Revisão: aprovada com ressalva (88%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 7/43 tarefas concluídas; próxima: "O gatilho do próximo passo responde só ao dono".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T4a` — O gate de delegação e a entrada do Passo 4 deixam de mandar re-derivar e copiar
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa fecha a regra da `RAF-T4` nos dois pontos que ela não alcançou: o item 3 do Gate de delegação da skill `passagem-de-bastao`, que o Passo 3 da `scrum-master` manda rodar antes do `despachar`, deixa de mandar colar âncoras re-derivadas na tarefa de plano; e a `Entrada` do Passo 4 da `scrum-master` deixa de ser o dossiê copiado do plano.

**Arquivos-alvo:** - `.claude/skills/passagem-de-bastao/SKILL.md` - `.claude/skills/scrum-master/SKILL.md`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/skills/passagem-de-bastao/SKILL.md').read_text(encoding='utf-8');print('gate=%d-%d'%(t.count('Junto dos números vão as'),t.count('e não se re-derivam à mão; só o')))"` → `gate=0-1` — antes `gate=1-0`, depois `gate=0-1` 2. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print('entrada=%d-%d'%(t.count('dossiê da tarefa copiado do plano'),t.count('(tíquete: dossiê à mão); modelo do cabeçalho')))"` → `entrada=0-1` — antes `entrada=1-0`, depois `entrada=0-1` 3. `python -c "from pathlib import Path;a=Path('.claude/skills/passagem-de-bastao/SKILL.md');b=Path('.claude/skills/scrum-master/SKILL.md');print('linhas=%d-%d cr=%d-%d'%(len(a.read_text(encoding='utf-8').splitlines()),len(b.read_text(encoding='utf-8').splitlines()),a.read_bytes().count(bytes([13])),b.read_bytes().count(bytes([13]))))"` → `linhas=306-445 cr=0-0` — antes `linhas=306-445 cr=0-445`, depois `linhas=306-445 cr=0-0`

**Pronto quando:** - gerente do loop.conferência das âncoras — o gate que roda antes do despacho não manda re-derivar a âncora da tarefa de plano: ela chega conferida no pacote — Verificação 1 - gerente do loop.entrega do despacho ao executor — a entrada do Passo 4 é o texto pronto do `despachar`, não o dossiê copiado do plano — Verificação 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-46`; `AE-126` (laudo da `RAF-T4`, ressalva 88); `DRF-7`, `DRF-8`, `DRF-45`; relatório `R-02`, `R-03`.
- **Depende de:** `RAF-T4`
- **Operação do modelo:** `OP-4` - OP-4: Quem executa ensina o gerente do loop a repassar ao executor o texto pronto do despacho, sem reconferir à mão as âncoras do card. - precisa de: despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.
- **Camada e fronteira:** doutrina do kit — o item 3 do Gate de delegação da skill `passagem-de-bastao` (residência única do gate) e o campo `Entrada` do Passo 4 da skill `scrum-master`; nenhum código muda. A `RAF-T4` trocou os Passos 3 e 4 da `scrum-master`, mas o gate que o Passo 3 manda rodar antes do `despachar` seguia mandando colar as âncoras "re-derivadas no ato", e a `Entrada` do Passo 4 seguia "dossiê da tarefa copiado do plano". O card de tíquete segue pelos passos à mão (Passo 3 da `scrum-master`) e não tem pacote: para ele o gate conserva a re-derivação. O número de linhas dos dois arquivos não muda. A árvore tem a `scrum-master` com fim de linha CRLF nas 445 linhas, contra o `eol=lf` que o `.gitattributes` declara e o índice guarda em LF (medido pelo consultor, 2026-09-28, `git ls-files --eol`: `i/lf w/crlf`); o arquivo volta a LF no mesmo ato, sem mudar conteúdo.
- **Passos:** 1. Em `.claude/skills/passagem-de-bastao/SKILL.md`, na seção `**Gate de delegação — residência única, roda ANTES de despachar o executor:**`, item 3, trocar as quatro linhas do texto antigo pelas quatro do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os três espaços iniciais que já tem no arquivo). Texto antigo: ```text silêncio. Junto dos números vão as **âncoras** (arquivo, linha e texto do ponto a editar) re-derivadas no ato e, quando a tarefa fecha em plano em andamento, o **range de linhas do bullet de fechamento anterior**: sem isso o dossiê não é autossuficiente e quem executa precisa redescobrir a localização — trabalho que a tarefa não pediu. ``` Texto novo: ```text silêncio. As **âncoras** (arquivo, linha e texto do ponto a editar) da tarefa de plano chegam conferidas no pacote do `despachar` (`scrum-master`, passo 3) e não se re-derivam à mão; só o card de tíquete, despachado à mão, as leva re-derivadas no ato. Tarefa que fecha em plano em andamento leva ainda o **range de linhas do bullet de fechamento anterior** (`scrum-master`, passo 4). ``` 2. Em `.claude/skills/scrum-master/SKILL.md`, no `### Passo 4 — Despacho do executor`, trocar a linha do texto antigo pela do texto novo (sem quebra nova e sem refluxo; a linha começa na coluna 0). Texto antigo: ```text - **Entrada:** dossiê da tarefa copiado do plano; modelo declarado no cabeçalho. ``` Texto novo: ```text - **Entrada:** texto pronto impresso pelo `despachar` (tíquete: dossiê à mão); modelo do cabeçalho. ``` 3. Gravar `.claude/skills/scrum-master/SKILL.md` com fim de linha LF em todas as linhas, sem mudar outro byte além dos do passo 2. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `533 passed`, 2026-09-28, entrega da `RAF-T3a`). `tests/test_progresso_hook.py` lê a skill `scrum-master` (tabela do repertório `M-0`..`M-18`), que os passos não tocam. - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0 (medido 0 antes, 2026-09-28). - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar os itens 1, 2 e 4 a 8 do Gate de delegação nem o começo do item 3 (números de aceite e string de assert); não mexer nos Passos 3 e 4 da `scrum-master` além do campo `Entrada` do Passo 4 (o resto é da `RAF-T4`); não mexer no Passo 1 (`RAF-T1`, `RAF-T1a`).
- **Contingências:** - se o texto antigo do passo 1 ou do passo 2 não existir verbatim → parar e sinalizar `blocked` razão `premissa`, nomeando o passo. - se a Verificação 3 já imprimir `cr=0-0` antes da edição → o passo 3 não tem efeito e a tarefa segue.
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_progresso_hook.py` lê a skill `scrum-master`.
- **Fora do escopo desta tarefa:** a linha do `README.md` que ainda descreve o despacho imprimindo o card (`RAF-T40`); a menção a âncoras re-derivadas como precedente já pago, na herança de contexto da mesma skill `passagem-de-bastao` (não manda re-derivar); o parágrafo das âncoras do Passo 4 da `scrum-master` (`RAF-T4`).
- **Handover:** 2026-09-28 · para quem vier depois - **Entregue:** passagem-de-bastao Gate de delegação item 3 dispensa re-derivar âncora na tarefa de plano (tíquete segue à mão); Entrada do Passo 4 da scrum-master = texto pronto impresso pelo despachar; scrum-master/SKILL.md de volta a LF - **Contrato:** a regra 'repassar o texto pronto, sem copiar card nem reconferir âncora' vale nos Passos 3 e 4 e no gate de delegação - **Não refazer:** as três trocas de prosa e a normalização LF - **Pendente:** nenhum

## Execução

**Consumo:** 16 tool uses, 55.6 k tokens, 140.3 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 88%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "Quem conduz repassa o texto pronto do despacho e não reconfere âncora" e vai pegar a tarefa "O gate de delegação e a entrada do Passo 4 deixam de mandar re-derivar e copiar".
Tarefa "O gate de delegação e a entrada do Passo 4 deixam de mandar re-derivar e copiar". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O gate de delegação e a entrada do Passo 4 deixam de mandar re-derivar e copiar" e vai executar: Quem executa fecha a regra da `RAF-T4` nos dois pontos que ela não alcançou: o item 3 do Gate de delegação da skill `passagem-de-bastao`, que o Passo 3 da `scrum-master` manda rodar antes do `despachar`, deixa de mandar colar âncoras re-de…
Agente executor devolveu a tarefa "O gate de delegação e a entrada do Passo 4 deixam de mandar re-derivar e copiar": review — sem pendência.
Tarefa "O gate de delegação e a entrada do Passo 4 deixam de mandar re-derivar e copiar": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O gate de delegação e a entrada do Passo 4 deixam de mandar re-derivar e copiar" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O gate de delegação e a entrada do Passo 4 deixam de mandar re-derivar e copiar": ressalva 88%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O gate de delegação e a entrada do Passo 4 deixam de mandar re-derivar e copiar" como done: registrar estado, RDO e telemetria.
