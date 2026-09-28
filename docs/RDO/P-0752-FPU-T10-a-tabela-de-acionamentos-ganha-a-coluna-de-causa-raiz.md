# RDO — P-0752 · FPU-T10

# Humano

Tarefa "A tabela de acionamentos ganha a coluna de causa raiz" concluída em 2026-09-27.
A tabela de acionamentos do consultor ganhou a coluna de causa raiz, com seis classes e, para cada uma, o que a pega.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Fato no ponto de uso: os mecanismos contra o esquecimento e a assunção": 17/17 tarefas concluídas; nenhuma tarefa pronta na fila dele.
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achado registrado no plano, com rota: 1 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/plans/P-0752-fato-no-ponto-de-uso.md`
**Tarefa:** `FPU-T10` — A tabela de acionamentos ganha a coluna de causa raiz
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `docs/ACIONAMENTOS_CONSULTOR.tsv` ganha a décima coluna `causa_raiz`; todas as linhas de dados existentes recebem `-` (DFP-9; eram 40 na autoria, 50 depois do acionamento 6 do consultor, e crescem uma por acionamento); o consultor (`pantonic-consultant.md:38`) preenche a coluna com um dos seis tokens `valor-reutilizado`, `premissa-nao-sondada`, `auto-relato`, `regra-esquecida`, `semantica-de-ferramenta`, `contexto-presumido` ou `-`; `GOVERNANCA.md` §3, na linha *Consultoria* da tabela de modelo por fase (linha 92), aponta a subseção nova `Vocabulário de causa raiz`, que diz, para cada token, o que o pega: nos quatro primeiros, uma conferência da régua executável; em `semantica-de-ferramenta` e `contexto-presumido`, nenhuma conferência da régua — a lista de armadilhas e o checklist da `mensagem-ao-dono` ficam fora dela (DFP-21, DFP-22).

**Arquivos-alvo:** - `docs/ACIONAMENTOS_CONSULTOR.tsv` — linha 1 (cabeçalho de nove campos) e todas as linhas de dados - `.claude/agents/pantonic-consultant.md:38` — `5. **Apensa uma linha de estatística por acionamento** a \`docs/ACIONAMENTOS_CONSULTOR.tsv\`` - `GOVERNANCA.md` — nova subseção `### 3.3 Vocabulário de causa raiz` depois da `### 3.2` (antes de `## 4`), e a linha 92 da tabela - `.claude/README.md` (projeção regenerada, se o gerador do kit a reescrever)

**Verificação:** 1. `python -c "import csv;from pathlib import Path;r=list(csv.reader(Path('docs/ACIONAMENTOS_CONSULTOR.tsv').open(encoding='utf-8',newline=''),delimiter='\t'));print(len(r[0]),r[0][-1],all(len(l)==len(r[0]) for l in r[1:]))"` → `10 causa_raiz True` — antes `9 inconclusivo True`, depois `10 causa_raiz True` (toda linha de dados com o número de campos do cabeçalho). 2. `python -c "from pathlib import Path;c=chr(96);t=Path('.claude/agents/pantonic-consultant.md').read_text(encoding='utf-8').splitlines();p=[('valor-reutilizado','valor reutilizado em vez de medido;'),('premissa-nao-sondada','premissa não sondada na autoria;'),('auto-relato','auto-relato aceito;'),('regra-esquecida','regra ou precedente esquecido;'),('semantica-de-ferramenta','semântica de ferramenta;'),('contexto-presumido','contexto presumido com o dono.')];print(t[38:44]==['   - '+c+k+c+' — '+v for k,v in p],(c+'inconclusivo'+c+', '+c+'causa_raiz'+c+'.') in t[37] and t[37].endswith('o critério de cada classe:'),t[44]=='')"` → `True True True` — antes `False False False`, depois `True True True` (os seis sub-itens na ordem, a linha 38 com a lista e a frase nova, a linha em branco depois deles). 3. `python -c "from pathlib import Path;print(Path('GOVERNANCA.md').read_text(encoding='utf-8').count('Vocabulário de causa raiz')>=1)"` → `True` — antes `False`, depois `True`. 4. `python .claude/tools/backlog.py check` → `check: OK — nenhuma violação.` — antes `OK`, depois `OK` (trava: a subseção nova não cria citação órfã). 5. `python -c "from pathlib import Path;print(Path('GOVERNANCA.md').read_text(encoding='utf-8').count('nenhuma conferência da régua'))"` → `2` (as duas classes que a régua não pega) — antes `0`, depois `2`. 6. `python -c "from pathlib import Path;c=chr(96);t=Path('GOVERNANCA.md').read_text(encoding='utf-8');print(sum(t.count('| '+c+k+c+' | ')==1 for k in 'valor-reutilizado premissa-nao-sondada auto-relato regra-esquecida semantica-de-ferramenta contexto-presumido'.split()),t.count('por plano fechado é a medida deste vocabulário; linha de base: 25 de 40 acionamentos em 2026-09-26 ('+c+'P-0752'+c+' F-10).'),t.count(c+'docs/ACIONAMENTOS_CONSULTOR.tsv'+c+'; causa raiz pelo vocabulário da §3.3 | '))"` → `6 1 1` — antes `0 0 0`, depois `6 1 1` (as seis linhas da tabela, a frase da medida e a linha 92).

**Pronto quando:** tabela de acionamentos.causa raiz por linha — coluna presente, vocabulário fechado de seis classes, preenchida a cada acionamento — Verificações 1 a 3, 5 e 6.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-27
- **Depende de:** `FPU-T2`, `FPU-T6`, `FPU-T7`
- **Operação do modelo:** `OP-10` - OP-10: A tabela de acionamentos ganha a coluna de causa raiz com o vocabulário fechado de classes, cada uma nomeando o que a pega: a conferência da régua ou, onde a régua não tem, nenhuma conferência e o que a pega fora dela. - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; tabela de acionamentos — Quem implementa acrescenta a coluna com vocabulário fechado; linha anterior recebe o valor vazio.; ocorrência de erro por crença — Ninguém altera: a coluna da tabela de acionamentos é o que a mede.
- **Fundamento:** DFP-9, DFP-22, DFP-25, F-7, F-10; a métrica da §0.
- **Passos:** 1. TSV: apensar `\tcausa_raiz` ao cabeçalho e `\t-` a cada linha de dados, por script Python que lê e reescreve em UTF-8 com `\n`, sem tocar nenhum outro byte das linhas. O arquivo tem hoje terminador CRLF em todas as linhas (medido, DFP-25): o script separa as linhas com `splitlines()` e grava cada uma terminada em LF, o canônico do `.gitattributes`; o terminador é a única outra mudança de byte, e não é desvio. 2. `.claude/agents/pantonic-consultant.md`: a linha 38 inteira (item 5) é substituída pelas sete linhas do bloco abaixo, nesta ordem, transcritas sem mudar nenhum caractere (DFP-25). A primeira é a linha 38 com `causa_raiz` depois de `inconclusivo` na lista de campos e uma frase nova no fim; as seis seguintes são os sub-itens do item 5 e, no arquivo, começam com três espaços, como os sub-itens do item 3; a linha em branco que precede `## O que você não faz` fica depois delas. O texto depois do travessão de cada sub-item é a coluna `o que é` do Passo 3. ~~~~ 5. **Apensa uma linha de estatística por acionamento** a `docs/ACIONAMENTOS_CONSULTOR.tsv`, com os campos separados por tabulação, na ordem `data`, `plano`, `acionamento`, `tarefa`, `gatilho`, `motivo`, `classe_impedimento`, `rota`, `inconclusivo`, `causa_raiz`. `gatilho` é a classe 1-4 da §2 de `docs/consultant-spec.md` (1 card `blocked`; 2 laudo com pendência substantiva; 3 impedimento de instrumento que nenhum card cobre; 4 ato do dono no marco); `acionamento` é o número de ordem no plano; `inconclusivo` é o que a decisão deliberadamente não fechou, ou `-`. O consumidor é o `TK-55`, acumulador da spec de robustez. `causa_raiz` é a classe do erro por crença que originou o acionamento, do vocabulário fechado da §3.3 de `GOVERNANCA.md`, onde está também o que pega cada classe, ou `-` quando nenhuma das seis o explica; o critério de cada classe: - `valor-reutilizado` — valor reutilizado em vez de medido; - `premissa-nao-sondada` — premissa não sondada na autoria; - `auto-relato` — auto-relato aceito; - `regra-esquecida` — regra ou precedente esquecido; - `semantica-de-ferramenta` — semântica de ferramenta; - `contexto-presumido` — contexto presumido com o dono. ~~~~ 3. `GOVERNANCA.md`, duas edições, com o texto literal dos blocos abaixo (células da DFP-22, tokens entre crases; DFP-25). (a) Subseção nova inserida antes de `GOVERNANCA.md:477` — `## 4. Fluxo de desenvolvimento`: o título `### 3.3 Vocabulário de causa raiz`, uma linha em branco, a tabela e a frase do bloco, e uma linha em branco antes do `## 4`; a linha em branco que hoje precede o `## 4` fica antes do título. ~~~~ | token | o que é | o que o pega | |---|---|---| | `valor-reutilizado` | valor reutilizado em vez de medido | conferência da régua: o literal da âncora no card_check e o aviso de número gravado sem comando | | `premissa-nao-sondada` | premissa não sondada na autoria | conferência da régua: o card_check no ensaio da autoria e no despacho | | `auto-relato` | auto-relato aceito | conferência da régua: o arquivo de medida do executor, lido pela evidência | | `regra-esquecida` | regra ou precedente esquecido | conferência da régua: os achados roteados ao card, colados no dossiê de despacho | | `semantica-de-ferramenta` | semântica de ferramenta | nenhuma conferência da régua: a lista docs/ARMADILHAS_DE_FERRAMENTA.md, consultada no ponto de uso | | `contexto-presumido` | contexto presumido com o dono | nenhuma conferência da régua: o checklist da mensagem-ao-dono, que chama a skill fatos-frescos, medida em prosa | A parcela de linhas com causa fora de `-` por plano fechado é a medida deste vocabulário; linha de base: 25 de 40 acionamentos em 2026-09-26 (`P-0752` F-10). ~~~~ (b) Na linha 92 (linha *Consultoria* da tabela de modelo por fase), o trecho da primeira linha do bloco (ocorrência única no arquivo) passa a ser o da segunda. ~~~~ `docs/ACIONAMENTOS_CONSULTOR.tsv` | Não reabre `docs/ACIONAMENTOS_CONSULTOR.tsv`; causa raiz pelo vocabulário da §3.3 | Não reabre ~~~~
- **Não fazer:** não classificar as linhas anteriores (DFP-9); não mudar nenhum outro campo do TSV; não tocar `docs/consultant-spec.md`.
- **Contingências:** - se alguma linha de dados do TSV tiver número de campos diferente de nove antes da edição → parar e sinalizar `blocked` razão `premissa`, nomeando a linha.
- **Handover:** 2026-09-27 · para `pantonic-consultant` - **Entregue:** docs/ACIONAMENTOS_CONSULTOR.tsv com a 10ª coluna causa_raiz (linhas anteriores '-'), pantonic-consultant.md:38 com os seis tokens, GOVERNANCA.md ### 3.3 Vocabulário de causa raiz e linha 92 apontando para ela - **Contrato:** cada acionamento do consultor preenche causa_raiz com um dos seis tokens ou '-' - **Não refazer:** nada a declarar - **Pendente:** nenhum
- **Notas de execução:** - 2026-09-27 `ready` — DFP-25: Passos 1-3 com o literal em bloco cercado; V2 e V6 travam o texto - 2026-09-27 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T10-a-tabela-de-acionamentos-ganha-a-coluna-de-causa-raiz.md`, veredito aprovado 100%

## Execução

**Consumo:** 23 tool uses, 87.5 k tokens, 281.8 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master concluiu a tarefa "O escritor da telemetria recusa a linha repetida da mesma rodada" e vai pegar a tarefa "A tabela de acionamentos ganha a coluna de causa raiz".
Tarefa "A tabela de acionamentos ganha a coluna de causa raiz". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "A tabela de acionamentos ganha a coluna de causa raiz" e vai executar: `docs/ACIONAMENTOS_CONSULTOR.tsv` ganha a décima coluna `causa_raiz`; todas as linhas de dados existentes recebem `-` (DFP-9; eram 40 na autoria, 50 depois do acionamento 6 do consultor, e crescem uma por acionamento); o consultor (`panton…
Agente executor devolveu a tarefa "A tabela de acionamentos ganha a coluna de causa raiz": blocked — motivo premissa: defeito=decisao: Passo 2 do card ("Consultor, item 5: acrescentar `causa_raiz` ao fim da lista de campos e a frase com os seis tokens e o critério de cada um (uma linha por token)") não fornece o texto literal da frase a inserir em `.claude/agents/pantonic-consultant.md:38` — ao contrário do Passo 3 (GOVERNANCA.md §3.3), que ancora explicitamente "com o texto de cada célula como está (DFP-22)" e cuja Verificação 5 trava o literal, a Verificação 2 deste passo só checa `count('causa_raiz')>=1`, não fixando conteúdo nem forma; compor a redação das seis linhas (conector, pontuação, se reaproveita literalmente o texto "o que o pega" do Passo 3 ou resume) é escolha entre alternativas que o card não fecha — não performei nenhuma edição..
Scrum master vai marcar a tarefa "A tabela de acionamentos ganha a coluna de causa raiz" como blocked, sem RDO.
Agente consultor recebe a tarefa "A tabela de acionamentos ganha a coluna de causa raiz" e vai triar.
Agente consultor devolveu a tarefa "A tabela de acionamentos ganha a coluna de causa raiz": rota resolve.
Agente executor recebe a tarefa "A tabela de acionamentos ganha a coluna de causa raiz" e vai executar: `docs/ACIONAMENTOS_CONSULTOR.tsv` ganha a décima coluna `causa_raiz`; todas as linhas de dados existentes recebem `-` (DFP-9; eram 40 na autoria, 50 depois do acionamento 6 do consultor, e crescem uma por acionamento); o consultor (`panton…
Agente executor devolveu a tarefa "A tabela de acionamentos ganha a coluna de causa raiz": review — sem pendência.
Agente revisor recebe a tarefa "A tabela de acionamentos ganha a coluna de causa raiz" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A tabela de acionamentos ganha a coluna de causa raiz": aprovado 100%, bloqueante nenhuma.
Scrum master vai fechar a tarefa "A tabela de acionamentos ganha a coluna de causa raiz" como done: registrar estado, RDO e telemetria.
