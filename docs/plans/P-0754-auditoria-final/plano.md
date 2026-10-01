# P-0754 — Auditoria final do kit: os herdados e o relatório de auditoria nova

**Data de origem:** 2026-09-28 · **Origem:** pedido do dono de 2026-09-28 em três atos (transcritos na §0) e
diretivas de 2026-09-26 (`docs/DIARIO_DE_OBRAS.md:2` e `:4`) · **Plano de origem:** nenhum (herda achados
de `P-0753`, `P-0752`, `P-0742` e dos tíquetes `TK-84`, `TK-86`, `TK-88`, `TK-93`; inventário na §2.1) ·
**Classe do plano:** ferramentaria · **Prefixo das tarefas no diário:** `AUF-T<n>` (lastro `tarefas: AUF-T<n>` para
`OP-<n>`) · **Prefixo das decisões:** `DAU-<n>` · **Prefixo dos fatos:** `F-<n>` ·
**Checagem de versão do kit:** modo hub — congelada em `0.0.0` (`GOVERNANCA.md` §10) ·
**Branch de trabalho:** `plan/planner-modelo-escopo` (HEAD `2513964`, árvore limpa salvo
`docs/telemetria.tsv`, escrito pelo hook de telemetria) · **Estado:** linha `plano` de `estado.tsv`, nesta
pasta.

**Marcos de validação pelo dono:**

| marco | o que o dono lê | veredito |
|---|---|---|
| **Marco 1** | `python .claude/tools/modelo.py show --plano docs/plans/P-0754-auditoria-final/plano.md` (a §1 escrita pelo modelador) e a §3 deste plano | go · 2026-09-28 — "Pode iniciar agora esse plano" |
| **Marco 2** | os herdados fechados e o `README.md` revisado; a instrução do dono abre o card da auditoria nova (o loop para antes dele, `DAU-3`) | go · 2026-09-28 — "pode  iniciar a auditoria neste contexto" |
| **Marco 3** | o relatório novo em `docs/audits/` e a entrega do plano | pendente |

## 0. O problema, verbatim

**Ato 1 — pedido (2026-09-28):** *"execute oplano de auditoria final"*.

**Ato 2 — respostas do dono às duas perguntas de quem conduz (2026-09-28):**

1. "Quer que eu comece o planejamento agora?" → **"Planejar agora (Recomendado)"** — *"Abro a sessão de
   planejamento. O agente planejador grava a estrutura do plano e o modelador escreve o modelo. Paro no
   Marco 1 para você validar, sem executar nada."*
2. "O que a auditoria final deve cobrir?" → **"Herdado + auditoria nova"** — *"Tudo o que foi herdado mais
   uma varredura nova do kit, que gera um relatório de auditoria, no formato usado na auditoria de
   encerramento do estágio 1 (P-0753)."* (A alternativa recusada: "Só o herdado".)

**Ato 3 — resposta do dono à rodada de decisões do planejador (2026-09-28):**

Pergunta: "O planejador precisa de uma decisão sua para gravar o plano: quem conduz a auditoria nova? No
estágio 1, ela foi feita pelo agente que conduzia a sessão. Ele executou um plano fictício de ponta a ponta
e acionou os outros agentes: planejador, modelador, executor e revisor. Uma tarefa comum do plano não faz
isso, porque quem a executa é um subagente, e subagente não aciona outro agente."

Resposta: **"Quem conduz (Recomendado)"** — *"A auditoria é a última tarefa do plano, executada pela sessão
principal, como no estágio 1. O loop para antes dela e só a abre quando você mandar. Isso abre uma exceção
à matriz de papéis, válida só para essa tarefa. A tarefa passa pela revisão. A avaliação do scrum-master
que você pediu é medida no loop real, com o custo real de orquestrar."*

**Atos anteriores do dono que definem este plano:**

- `docs/DIARIO_DE_OBRAS.md:2` — **Diretiva do dono (2026-09-26, vigente até o fechamento da auditoria
  final):** *"Execute em loop as tarefas abertas."* (1) esgotar tíquetes e planos abertos para desbloquear o
  plano de auditoria final; (2) nenhum card nem tíquete novo por ajuste: achado novo vira `AE-<n>` com rota
  "auditoria final"; (3) tíquete ou card que o dono não abriu fecha pelo condutor.
- `docs/DIARIO_DE_OBRAS.md:4` — **Diretiva de priorização:** o plano de auditoria final é o próximo, em
  contexto novo; a sessão de planejamento o escreve herdando os `AE-<n>` com rota "auditoria final".
  Fora da fila, atos do dono: a projeção da camada global em `~/.claude` (`materializar.py apply`).
- `AE-95` (`docs/DIARIO_DE_OBRAS.md:9`), veredito do dono no Marco 1 do `P-0742`: *"Eu não concordo em
  tirar o agente scrum-master do loop, [...] O que eu concordo é que pode existir potencial para ganhor
  mecanizado ações mecânicas do scrum-master ou otimizar as rotinas dele. Mas essas tarefas podem ser
  herdadas no plano de auditoria. Deixe registrado na spec do plano de auditoria essa matéria de avaliação,
  e encerre este plano"*.

**Pré-voo do pedido** (`python .claude/tools/prevoo.py`, colado por quem conduz):

| citado | existe | onde |
|---|---|---|
| docs/audits/AUDITORIA_ENCERRAMENTO_ESTAGIO1_2026-09-27.md | sim | docs/audits/AUDITORIA_ENCERRAMENTO_ESTAGIO1_2026-09-27.md |

**O que o plano entrega quando termina:** os itens herdados com rota "auditoria final" (§2.1)
fechados — absorvidos por mudança no kit ou registrados como não-ação com a prova —, o guia de entrada
(`README.md`) revisado para descrever o kit com eles fechados, e um relatório novo
de auditoria do kit em `docs/audits/`, no formato da auditoria de encerramento do estágio 1, produzido pela
sessão principal executando um plano fictício ponta a ponta contra o kit já com os herdados fechados, com
a avaliação das ações mecânicas do scrum-master (`AE-95`) medida no loop real.

**Marco 1, 2026-09-28 — veredito do dono (go):**

> Pode iniciar agora esse plano

**Marco 2, 2026-09-28 — veredito do dono (go):**

> pode  iniciar a auditoria neste contexto

## 1. Modelo conceitual

**Estado do modelo:** versão 1 · 2026-09-28 · autor: modelador · 16 operações · 23 propriedades · situação: vigente

### 1.1 Objetos

| objeto | o que é | propriedades | contrato | origem | lastro na §0 ou no inventário | tipo |
|---|---|---|---|---|---|---|
| dossiê de evidência | o que o revisor recebe mostrando o que a entrega mudou, para julgar cada tarefa | arquivo novo depois do recorte, caminho com acento, leitura dos alvos do card, atribuição das escritas da condução, arquivo versionado e ignorado, arquivo novo que não é texto | Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório. | OP-1 | §0, ato 2: *"Tudo o que foi herdado"* · §2.1 H-10, H-12, H-13, H-18, H-19, H-20 | escopo |
| painel do gerente | a tela de progresso que acompanha o que o loop está fazendo | título do tíquete | Quem implementa faz o painel achar o título também quando o trabalho em curso é um tíquete, e não só um card de plano. | OP-7 | §0, ato 2: *"Tudo o que foi herdado"* · §2.1 H-14 | escopo |
| fechamento de tarefa | o comando que encerra uma tarefa revisada e diz, ao fim, o que fez | mensagem de conclusão | Quem implementa troca só a frase final por uma que sirva a todos os comandos, e acerta os testes que esperavam a antiga. | OP-8 | §0, ato 2: *"Tudo o que foi herdado"* · §2.1 H-15 | escopo |
| planejador | o agente que transforma o pedido do dono em plano e escreve os cards | contingência do card, pontos de parada do teste de interrupção, restrição que cita o estado do plano, pergunta sobre o impedimento do papel | Quem implementa recebe o roteiro de fases do agente e acrescenta só a regra que a operação pede, deixando as demais como estão. | OP-9 | §0, ato 2: *"Tudo o que foi herdado"* · §2.1 H-1 a H-5, H-8, H-9 | escopo |
| rubrica de revisão | a régua pela qual o revisor julga cada entrega | critério de contingência | Quem implementa acrescenta um critério que confere a contingência do card pela mesma regra que o planejador passa a seguir. | OP-10 | §0, ato 2: *"Tudo o que foi herdado"* · §2.1 H-1, H-8 | escopo |
| herdados que não pedem mudança | quatro achados deixados para a auditoria final que, conferidos hoje, não pedem mudança nenhuma no kit | desfecho | Quem implementa registra o encerramento de cada um com a prova já levantada, sem mudar nada no kit. | OP-14 | §0, o que o plano entrega quando termina: *"registrados como não-ação com a prova"* · §2.1 H-6, H-7, H-11, H-17 | escopo |
| guia de entrada do kit | o documento que apresenta o kit a quem chega | aderência ao kit entregue | Quem implementa revisa o guia contra o kit como ele fica depois dos herdados fechados. | OP-15 | §0, o que o plano entrega quando termina: *"contra o kit já com os herdados fechados"* · prompt do planejador: o guia se revisa ao fim de toda etapa que muda o kit | escopo |
| relatório de auditoria nova | o relatório da varredura do kit depois dos herdados, que o dono lê para decidir o plano seguinte | cobertura do kit, avaliação das ações mecânicas do gerente, medida no replanejamento, recomendações | Quem conduz a sessão recebe o formato do primeiro estágio e o kit já fechado, audita-o executando de ponta a ponta um plano fictício que depois descarta, e grava o relatório. As recomendações dele não se aplicam neste plano. | OP-16 | §0, ato 2: *"uma varredura nova do kit, que gera um relatório de auditoria, no formato usado na auditoria de encerramento do estágio 1"* · §0, ato 3 | escopo |
| levantamento dos herdados | a lista dos vinte e um achados deixados para a auditoria final, com o defeito de cada um e a prova de como ele está hoje | itens e provas | Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha. | externo | §0, ato 2: *"Tudo o que foi herdado"* · §2.1 | externo |
| relatório do primeiro estágio | a auditoria de encerramento do primeiro estágio, cujo formato o relatório novo segue | formato | Ninguém altera: é o molde do relatório novo, seção por seção. | externo | §0, ato 2: *"no formato usado na auditoria de encerramento do estágio 1"* | externo |
| instrução do dono no segundo marco | a ordem do dono que abre a auditoria nova, depois de ele ver os herdados fechados | abertura da auditoria | Ninguém altera: a auditoria espera por ela, e o loop não a abre sozinho. | externo | §0, ato 3: *"O loop para antes dela e só a abre quando você mandar"* | externo |
| gerente do loop | a rotina de quem conduz a sessão, que despacha, revisa e fecha cada tarefa | passos do loop | Ninguém altera: ele fica no loop, e é nele que se mede, durante o plano fictício, quanto das suas ações é mecânico e quanto custa. | externo | §0, veredito do dono sobre o gerente: *"Eu não concordo em tirar o agente scrum-master do loop"* · §0, ato 3: *"medida no loop real, com o custo real de orquestrar"* | medição |

### 1.2 Fluxo de operações

**A. O que o revisor recebe como evidência**

- **OP-1** — Quem executa faz o instrumento de evidência mostrar como diferença, e não como conteúdo inteiro, o arquivo novo criado depois do recorte do despacho.
  - `precisa de: levantamento dos herdados` · `altera: dossiê de evidência.arquivo novo depois do recorte` · `tarefas: AUF-T1` · `lastro: §0, ato 2, Tudo o que foi herdado; §2.1 H-10`
- **OP-2** — Quem executa cobre com teste o trecho do instrumento de evidência que lê o caminho com acento devolvido em código pelo versionador.
  - `precisa de: levantamento dos herdados, dossiê de evidência` · `altera: dossiê de evidência.caminho com acento` · `tarefas: AUF-T2` · `lastro: §0, ato 2, Tudo o que foi herdado; §2.1 H-12`
- **OP-3** — Quem executa faz o instrumento de evidência reconhecer, entre os alvos do card, o nome escrito com curinga e o arquivo que ainda não existia.
  - `precisa de: levantamento dos herdados, dossiê de evidência` · `altera: dossiê de evidência.leitura dos alvos do card` · `tarefas: AUF-T3` · `lastro: §0, ato 2, Tudo o que foi herdado; §2.1 H-13`
- **OP-4** — Quem executa faz o instrumento de evidência atribuir à condução, e não a um tíquete, o que quem conduz escreve nos próprios registros.
  - `precisa de: levantamento dos herdados, dossiê de evidência` · `altera: dossiê de evidência.atribuição das escritas da condução` · `tarefas: AUF-T4` · `lastro: §0, ato 2, Tudo o que foi herdado; §2.1 H-18`
- **OP-5** — Quem executa faz o instrumento de evidência incluir no recorte o arquivo já versionado que a lista de ignorados também cobre.
  - `precisa de: levantamento dos herdados, dossiê de evidência` · `altera: dossiê de evidência.arquivo versionado e ignorado` · `tarefas: AUF-T5` · `lastro: §0, ato 2, Tudo o que foi herdado; §2.1 H-19`
- **OP-6** — Quem executa faz o instrumento de evidência comparar pelo conteúdo bruto o arquivo novo que não é texto, em vez de dá-lo sempre por tocado.
  - `precisa de: levantamento dos herdados, dossiê de evidência` · `altera: dossiê de evidência.arquivo novo que não é texto` · `tarefas: AUF-T6` · `lastro: §0, ato 2, Tudo o que foi herdado; §2.1 H-20`

**B. O painel e o fechamento**

- **OP-7** — Quem executa faz o painel do gerente mostrar o título do tíquete em curso, e não só o identificador dele.
  - `precisa de: levantamento dos herdados, dossiê de evidência` · `altera: painel do gerente.título do tíquete` · `tarefas: AUF-T7` · `lastro: §0, ato 2, Tudo o que foi herdado; §2.1 H-14`
- **OP-8** — Quem executa troca a frase final do fechamento de tarefa por uma sem erro de concordância com o nome de nenhum comando.
  - `precisa de: levantamento dos herdados, dossiê de evidência` · `altera: fechamento de tarefa.mensagem de conclusão` · `tarefas: AUF-T8` · `lastro: §0, ato 2, Tudo o que foi herdado; §2.1 H-15`

**C. O planejador e a régua do revisor**

- **OP-9** — Quem executa ensina o planejador a tratar cada contingência do card como parte ensaiada dele, sem contrariar as restrições do card e com os arquivos que ela escreve declarados.
  - `precisa de: levantamento dos herdados, dossiê de evidência` · `altera: planejador.contingência do card` · `tarefas: AUF-T9` · `lastro: §0, ato 2, Tudo o que foi herdado; §2.1 H-1, H-8`
- **OP-10** — Quem executa acrescenta à rubrica de revisão o critério que cobra da contingência do card a regra que o planejador passou a seguir.
  - `precisa de: levantamento dos herdados, dossiê de evidência, planejador` · `altera: rubrica de revisão.critério de contingência` · `tarefas: AUF-T10` · `lastro: §0, ato 2, Tudo o que foi herdado; §2.1 H-1, H-8`
- **OP-11** — Quem executa acrescenta ao teste de interrupção do planejador os três casos medidos em que o card deveria ter parado e não parou.
  - `precisa de: levantamento dos herdados, dossiê de evidência, planejador` · `altera: planejador.pontos de parada do teste de interrupção` · `tarefas: AUF-T11` · `lastro: §0, ato 2, Tudo o que foi herdado; §2.1 H-2, H-3, H-4`
- **OP-12** — Quem executa faz o planejador reconferir a restrição de card que cita o estado do plano sempre que o modelador grava uma versão pendente.
  - `precisa de: levantamento dos herdados, dossiê de evidência, planejador` · `altera: planejador.restrição que cita o estado do plano` · `tarefas: AUF-T12` · `lastro: §0, ato 2, Tudo o que foi herdado; §2.1 H-5`
- **OP-13** — Quem executa faz o planejador perguntar, diante de um papel que não consegue algo, se o impedimento é ajuste do kit ou limite da plataforma.
  - `precisa de: levantamento dos herdados, dossiê de evidência, planejador` · `altera: planejador.pergunta sobre o impedimento do papel` · `tarefas: AUF-T13` · `lastro: §0, ato 2, Tudo o que foi herdado; §2.1 H-9`

**D. O fecho da etapa dos herdados**

- **OP-14** — Quem executa registra o encerramento dos quatro herdados que não pedem mudança no kit, cada um com a prova já levantada.
  - `precisa de: levantamento dos herdados, dossiê de evidência` · `altera: herdados que não pedem mudança.desfecho` · `tarefas: AUF-T14` · `lastro: §0, o que o plano entrega quando termina, registrados como não-ação com a prova; §2.1 H-6, H-7, H-11, H-17`
- **OP-15** — Quem executa revisa o guia de entrada do kit para que ele descreva o kit como fica depois dos herdados fechados.
  - `precisa de: dossiê de evidência, painel do gerente, fechamento de tarefa, planejador, rubrica de revisão` · `altera: guia de entrada do kit.aderência ao kit entregue` · `tarefas: AUF-T15` · `lastro: §0, o que o plano entrega quando termina, contra o kit já com os herdados fechados`

**E. A auditoria nova, aberta pelo dono no segundo marco**

- **OP-16** — Quem conduz a sessão, por instrução do dono, grava o relatório de auditoria nova, medido num plano fictício que ela executa de ponta a ponta sobre o kit já fechado.
  - `precisa de: instrução do dono no segundo marco, guia de entrada do kit, herdados que não pedem mudança, dossiê de evidência, relatório do primeiro estágio, gerente do loop, levantamento dos herdados` · `altera: relatório de auditoria nova.cobertura do kit, relatório de auditoria nova.avaliação das ações mecânicas do gerente, relatório de auditoria nova.medida no replanejamento, relatório de auditoria nova.recomendações` · `tarefas: AUF-T16` · `lastro: §0, ato 2, Herdado + auditoria nova; §0, ato 3, Quem conduz; §0, veredito do dono sobre o gerente; §2.1 H-16, H-21`

### 1.3 Estado inicial e estado final

| propriedade | estado inicial | estado final | lastro na §0 ou no inventário |
|---|---|---|---|
| dossiê de evidência.arquivo novo depois do recorte | um arquivo criado depois do recorte chegava ao revisor inteiro, sem diferença; o recorte já foi refeito desde então, sem registro de que isso resolveu | o arquivo novo chega ao revisor como diferença contra o recorte, com um teste que o prova; se já chegava assim, o item fecha como resolvido antes e o teste fica de guarda | §2.1 H-10 |
| dossiê de evidência.caminho com acento | o trecho que traduz o caminho com acento devolvido em código pelo versionador existe e nenhum teste o exercita | um teste exercita o trecho com um caminho acentuado de verdade | §2.1 H-12 |
| dossiê de evidência.leitura dos alvos do card | só alvo que é pasta se expande; alvo escrito com curinga não casa com nada, e o alvo que ainda não existia chega sem aviso de que é novo | o alvo com curinga casa com os arquivos da árvore, e o alvo que não existia antes chega marcado como novo | §2.1 H-13 |
| dossiê de evidência.atribuição das escritas da condução | o que quem conduz escreve no diário e nos próprios registros é atribuído a um tíquete que não o escreveu | essa escrita conta como registro da condução antes de se procurar um tíquete dono | §2.1 H-18 |
| dossiê de evidência.arquivo versionado e ignorado | o arquivo já versionado que a lista de ignorados também cobre fica fora do recorte, e a mudança nele some da evidência | o recorte parte de tudo o que já está versionado, e esse arquivo entra como qualquer outro | §2.1 H-19 |
| dossiê de evidência.arquivo novo que não é texto | um arquivo novo que não é texto entra sempre entre os tocados, mesmo que ninguém tenha mexido nele | ele entra só quando o conteúdo mudou desde o recorte | §2.1 H-20 |
| painel do gerente.título do tíquete | durante um tíquete, o painel mostra o identificador dele no lugar do título | o painel mostra o título do tíquete, como já faz com o card | §2.1 H-14 |
| fechamento de tarefa.mensagem de conclusão | ao fechar uma tarefa, a frase final diz "tarefa fechado" | a frase final diz que o comando foi concluído, correta para todos os comandos | §2.1 H-15 |
| planejador.contingência do card | o planejador ensaia os valores das verificações e não ensaia a contingência; ela já saiu contrariando a restrição do próprio card e escrevendo em arquivo que o card não declarava | cada contingência é ensaiada como o resto do card, não contraria nenhuma restrição dele, e o arquivo que ela escreve aparece entre os alvos, marcado como condicional | §2.1 H-1, H-8 |
| planejador.pontos de parada do teste de interrupção | o teste pergunta, em termos gerais, se o executor teria de parar; três casos medidos passaram por ele: objetivo que diz "se" contra contrato que manda sempre, caminho sem dizer se é relativo ou absoluto, e argumento sem a limpeza e as recusas fechadas | os três casos entram no teste pelo nome, como pontos em que o card tem de ser fechado antes de sair | §2.1 H-2, H-3, H-4 |
| planejador.restrição que cita o estado do plano | uma restrição de card afirmou um estado do plano que o modelador mudou depois, e ninguém a reconferiu | quando o modelador grava uma versão pendente, o planejador reconfere toda restrição de card que cita o estado do plano | §2.1 H-5 |
| planejador.pergunta sobre o impedimento do papel | diante de "esse papel não consegue fazer isso", o planejador aceita o impedimento como dado | antes de contornar, o planejador pergunta se o impedimento é ajuste do kit, que se corrige, ou limite da plataforma | §2.1 H-9 |
| rubrica de revisão.critério de contingência | a rubrica não diz nada sobre a contingência do card | a rubrica cobra da contingência a mesma regra que o planejador segue ao escrevê-la | §2.1 H-1, H-8 |
| herdados que não pedem mudança.desfecho | quatro achados seguem abertos com a rota da auditoria final, embora a premissa de dois tenha caído e a regra dos outros dois já exista | os quatro estão encerrados, cada um com a prova de que não pede mudança no kit | §0, o que o plano entrega quando termina: *"registrados como não-ação com a prova"* · §2.1 H-6, H-7, H-11, H-17 |
| guia de entrada do kit.aderência ao kit entregue | descreve o kit de antes dos herdados fechados | descreve o kit como ele fica depois dos herdados fechados | §0, o que o plano entrega quando termina: *"contra o kit já com os herdados fechados"* |
| relatório de auditoria nova.cobertura do kit | não há relatório de auditoria depois do primeiro estágio | cada regra do kit que se pode testar tem o seu teste no plano fictício, a medição registrada e a conclusão por dimensão, no formato do primeiro estágio; o plano fictício foi descartado e nada dele ficou | §0, ato 2: *"uma varredura nova do kit, que gera um relatório de auditoria"* · §0, ato 3 |
| relatório de auditoria nova.avaliação das ações mecânicas do gerente | as ações mecânicas do gerente do loop nunca foram avaliadas no loop real; o custo conhecido vem de planos anteriores, de sete a treze turnos por despacho | cada passo do loop diz se é mecânico, que instrumento já o cobre e quanto custou no plano fictício, com uma recomendação para cada ação que se possa mecanizar | §0, veredito do dono sobre o gerente: *"pode existir potencial para ganhor mecanizado ações mecânicas do scrum-master"* · §0, ato 3: *"medida no loop real, com o custo real de orquestrar"* · §2.1 H-21 |
| relatório de auditoria nova.medida no replanejamento | não se sabe onde a rodada de replanejamento grava a medida dos cards que reescreve | o relatório diz onde essa medida deve morar e recomenda o remédio | §2.1 H-16 |
| relatório de auditoria nova.recomendações | nenhuma recomendação nova | uma recomendação por registro inadequado ou oportunidade de melhoria, a aplicar em plano seguinte que o dono abre depois de ler o relatório | §0, ato 2: *"no formato usado na auditoria de encerramento do estágio 1"* |
| levantamento dos herdados.itens e provas | vinte e um itens, cada um com o defeito e a prova de como ele está hoje | os mesmos vinte e um; o levantamento não muda | §2.1 |
| relatório do primeiro estágio.formato | modelo, regras testadas, registro de cada medição, conclusão por oito dimensões, recomendações, custo do plano fictício e o que ficou | o mesmo; o relatório do primeiro estágio não muda | §0, ato 2 |
| instrução do dono no segundo marco.abertura da auditoria | não dada: o loop para antes da auditoria nova | dada pelo dono no segundo marco, e só então quem conduz a sessão abre a auditoria | §0, ato 3: *"O loop para antes dela e só a abre quando você mandar"* |
| gerente do loop.passos do loop | dez passos, metade apoiada em instrumento e metade feita à mão por quem conduz | os mesmos dez passos; nenhum removido, fundido ou substituído | §0, veredito do dono sobre o gerente: *"Eu não concordo em tirar o agente scrum-master do loop"* |

### 1.4 Registro de versões

| versão | data | situação | por |
|---|---|---|---|
| 1 | 2026-09-28 | vigente | modelador, autoria sobre o dossiê do planejador |

## 2. Fatos estabelecidos

Fontes: dossiês do `pantonic-scout`, rodadas 1 (Q1..Q7) e 2 (S1..S7), 2026-09-28, sobre HEAD `2513964`;
greps de superfície re-rodados pelo planejador no mesmo HEAD (marcados *re-rodado*).

### 2.1 Inventário dos herdados (residência única desta lista)

Esta subseção é a **residência única** da lista de herdados. Decisões e cards remetem a ela pelo id da
linha (`H-<n>`); nenhum outro lugar do plano reenuncia a lista. Padrões que a produziram:
`grep -rn -i "auditoria final" docs .claude --include=*.md --include=*.tsv` = 84 linhas (fora da pasta do
`P-0753`: 27 linhas, 12 itens canônicos, 2 cópias em `docs/plans/_ENTREGA-P-0752.md:66-67`, 13 só menção);
na pasta do `P-0753`: `plano.md` 20 linhas, `operacoes.md` 3, `cenario.md` 11. *Re-rodado:*
`grep -rn "AE-<n>\b" .claude tests --exclude-dir=__pycache__` = 0 para cada um de AE-50, 51, 83, 84, 85, 86,
88, 89, 92, 93, 94, 95.

| H | item | origem | residência | defeito, em uma frase | estado em HEAD `2513964` |
|---|---|---|---|---|---|
| H-1 | pendência 1 | `P-0753` | `docs/plans/P-0753-auditoria-estagio-1/operacoes.md:533` | classe "card publicado com contingência ou valor não ensaiado" (DAF-37, 38, 39, 41, 47 do `P-0753`, `plano.md:273-283`) | aberto: o valor não ensaiado é coberto por `card_check.py` e pelo item 14 da Fase 4 do planejador; contingência não é coberta — `conting[eê]ncia` = 0 em `.claude/agents/pantonic-planner.md` e em `docs/RUBRICA_DE_REVISAO.md` |
| H-2 | AE-8 | `P-0753` | `plano.md:1740` | Objetivo da AF-T7 condicional contra Contratos que mandam ler sempre | aberto; card `done`; regra específica ausente |
| H-3 | AE-13 | `P-0753` | `plano.md:1745` | o card AF-T10 não fixou se `--plano` é relativo ou absoluto | aberto; card `done`; regra específica ausente (genérica: `pantonic-planner.md:329`, item 8) |
| H-4 | AE-18 (parte não resolvida) | `P-0753` | `plano.md:1750` | o card AF-T12 não fechou a forma de `<plano>` no dossiê (caminho relativo), o `strip()` da frase nem as duas recusas a mais (plano sem id no nome, plano fora do backlog) | aberto; o AF-T12a prometido não existe (DAF-43) |
| H-5 | AE-20 | `P-0753` | `plano.md:1752` | o parêntese "(o plano não tem ## 1A)" da restrição da AF-T14 é falso | aberto; remédio do laudo: "card cuja restrição cita estado do plano re-confere o parêntese quando o modelador grava versão pendente" (`laudos/AF-T14.md:27`); regra ausente |
| H-6 | AE-21 | `P-0753` | `plano.md:1753` | o dossiê truncou o diff do `modelo.py` em 4000 caracteres | laudo: "sem ação — teto conhecido do instrumento" (`laudos/AF-T14.md:28`) |
| H-7 | AE-22 | `P-0753` | `plano.md:1754` | Verificações da AF-T16 "esperado, não ensaiado" | regra existe: `pantonic-planner.md:433-438` (item 14) e `docs/RUBRICA_DE_REVISAO.md:305` (xii)(b) |
| H-8 | AE-24 | `P-0753` | `plano.md:1756` | contingência escreve em arquivo fora dos Arquivos-alvo | aberto; remédio do laudo: "card com contingencia que escreve em arquivo o lista em Arquivos-alvo como condicional" (`laudos/AF-T17.md:31`); regra ausente |
| H-9 | RP-1 | `P-0753` | `plano.md:1758` (remissão `:1573`) | a Fase 1 do planejador não pergunta "o impedimento do papel é configuração do kit?" | aberto; `configura[çc][ãa]o do (pr[óo]prio )?kit\|impedimento` = 0 em `pantonic-planner.md` |
| H-10 | AE-50 do `P-0752` | `P-0752` | `docs/plans/P-0752-fato-no-ponto-de-uso.md:840` | ref de despacho por `git stash create` não carrega não rastreado; evidência sai inteira, sem diff | a verificar: `capturar_ref` (`review_evidence.py:207`) usa hoje índice temporário + `git add -A` (`:213-219`, trabalho do `TK-93a`), sem registro de absorção; fallback de conteúdo integral em `_diff_para_arquivo` `:581`, `:606-614` |
| H-11 | AE-51 do `P-0752` | `P-0752` | `P-0752…:841` | `docs/ACIONAMENTOS_CONSULTOR.tsv` fora do git: evidência cola o arquivo sem baseline | premissa caiu (*re-rodado*): `git ls-files --error-unmatch docs/ACIONAMENTOS_CONSULTOR.tsv` exit 0, adicionado em `2513964`; `git check-ignore -q` exit 1; o caminho está em `_REGISTRO_ORQUESTRACAO` (`review_evidence.py:403-410`) |
| H-12 | AE-83 | `TK-84` | `docs/DIARIO_DE_OBRAS.md:5592` | o card do TK-84a promete ramo de escape octal sem Verificação nem teste | aberto: ramo em `coletar_arquivos_tocados` `review_evidence.py:349-352`; `grep -rn -i "octal" tests` = 0 |
| H-13 | AE-84 | `TK-86` | `DIARIO:5865` | `review_evidence` não expande glob dos alvos nem marca alvo não rastreado sem "antes" | aberto: `montar_trechos` `:618-650` só expande alvo-diretório (`_eh_alvo_diretorio` `:395`); `glob\|fnmatch` = 0 |
| H-14 | AE-85 | `TK-86` | `DIARIO:5866` | o painel publica id do tíquete no lugar do título do card | aberto: `localizar_card` `progresso_hook.py:143`, padrão `:148` só casa `^### <id> — `; tíquete cai no fallback `:179`; casos nos RDO `TK-84a:67`, `TK-87a:68` |
| H-15 | AE-86 | `TK-86` | `DIARIO:5867` | stdout de `encerrar.py tarefa` diz "tarefa fechado" | aberto (*re-rodado*): `encerrar.py:1293` `print(f"encerrar: OK - {args.comando} fechado; relatório em '{destino}'.")` |
| H-16 | AE-88 | `TK-88` | `DIARIO:6082` | rodada de replanejamento sem canal de medida gravada | residência não apurada: `card_check.py --gravar` (`:524-549`) exige `--tarefa` (`:508`) e grava em `caminhos.destino_medida` (`caminhos.py:110-116`); o planejador exige `card_check` exit 0 sem `--gravar` (`pantonic-planner.md:435-436`, `:443`) |
| H-17 | AE-89 | `TK-88` | `DIARIO:6083` | cards do `P-0742` passam do teto DB-7 do `show` e a Fase 4 não confronta | premissa caiu: `backlog.py:8` isenta o card de tarefa do teto (`_TETO_CHARS = 8000`, `_TETO_LINHAS = 120`, `:138-139`); os 8 cards LF-T1..LF-T8 saem de `backlog.py show` com 0 marcas `truncado (` (maior: LF-T5, 130 linhas, 22979 caracteres) |
| H-18 | AE-92 | `TK-93` | `DIARIO:6209` | o modo diário atribui escritas da orquestração a tíquetes que não as fizeram | aberto: `confrontar_escopo` `:496`, precedência `:534-538` testa `_tarefa_dona` antes de `_eh_registro_orquestracao` |
| H-19 | AE-93 | `TK-93` | `DIARIO:6273` | `git add -A` em índice temporário vazio deixa de fora arquivo rastreado que casa com `.gitignore` | aberto: `capturar_ref` `:207`, `add -A` `:219`, `GIT_INDEX_FILE` temporário `:213-217`; nenhum `ls-files` no arquivo |
| H-20 | AE-94 | `TK-93` | `DIARIO:6274` | não rastreado binário ou não-UTF-8 intocado entra sempre em tocados | aberto: `_nao_rastreado_mudou_desde_ref` `:300`, `:304-306` devolve `True` quando `_texto_do_disco` (`:293-297`) dá `None` por `UnicodeDecodeError` |
| H-21 | AE-95 | `P-0742` | `DIARIO:9` | mecanizar ou otimizar as ações mecânicas do scrum-master sem tirá-lo do loop | matéria de avaliação (veredito na §0) |

Nota de contagem: a tabela tem 21 linhas `H-`. `H-1` é a classe da pendência 1 do `P-0753`; `H-2..H-8` são as
notas que a pendência 2 lhe dá como insumo, cada uma com linha própria porque cada uma fecha por decisão
própria (§3).

Fora do inventário, com rota diferente de "auditoria final": pendências 3, 4 e 5 do `P-0753`
(`operacoes.md:535-537`: dono, plano próprio, rodada de revisão da doutrina); AE-87, AE-90, AE-91
(`DIARIO:5868`, `:5642`, `:6208`: rotas "sem ação", `TK-88b`, `TK-93a`). Os ids `AE-50`/`AE-51` repetem no
`P-0740`: neste plano valem sempre qualificados "do `P-0752`".

### 2.2 Fatos do kit

| F | fato | fonte |
|---|---|---|
| F-1 | Fila vazia: `python .claude/tools/backlog.py next` → `nada delegável — 0 elegível(is) · blocked 0`, exit 2; `_INBOX.md` sem linha de plano; índice do diário (`DIARIO_DE_OBRAS.md:227`) com 80 linhas, todas terminais (done 56, cancelled 17, superseded 7). A precondição da diretiva de 2026-09-26 está cumprida. | Q5 |
| F-2 | Próximo id de plano: `_INBOX.md:5` "**Próximo id de plano: P-0754.**". Prefixos `AUF-T` e `DAU-` com 0 ocorrências em `docs`. | Q5, S7, *re-rodado* |
| F-3 | Só o contexto principal despacha subagentes; subagente não aciona outro agente (limite da plataforma, não configuração do kit). A matriz de `GOVERNANCA.md` §3 é por papel (`:88`); card de qualquer classe é da linha **Execução** (`:94`, Sonnet, subagente); a skill `scrum-master` roda no contexto principal (`SKILL.md:8`, `GOVERNANCA.md:93`); nenhuma cláusula prevê card executado pela sessão principal. | S6 |
| F-4 | Estados de `estado.tsv`: `razao` ∈ {`-`, `dependencia`, `premissa`} (skill `diario-de-obras`, `SKILL.md:205`); `backlog.py next` só seleciona `ready`; o sufixo ` + dono` do cabeçalho é lido por `backlog.py:98-106` e **não** filtra a seleção. | *re-rodado* |
| F-5 | Método da auditoria do estágio 1 (`docs/audits/AUDITORIA_ENCERRAMENTO_ESTAGIO1_2026-09-27.md`, 367 linhas): conduzida pela sessão principal (`:5`), sem id de plano próprio; §1 modelo com fluxo "OP-1 enumerar as cláusulas → OP-2 autorar o plano fictício que as cobre → OP-3 executar cada teste e registrar a medição na tabela → OP-4 concluir por dimensão → OP-5 emitir as recomendações → OP-6 descartar o plano fictício" (`:11-22`); §2 cláusulas `\| id \| cláusula (mecanismo) \| residência \| teste \|` (36 K-n; cláusula sem passagem no plano fictício marcada `sonda`, `:26`); §3 registros `\| # \| cláusula \| teste \| medido \| dimensões \| avaliação \|` (58 linhas; legenda `:69` L lacuna · E erro de execução · C pouca confiabilidade · $ custo evitável · Q qualidade da entrega · M mecanização · F fluxo; avaliação adequado/inadequado/oportunidade); §4 oito dimensões (Integração ponta a ponta, L, E, C, $, Q, M, F) com `dimensão \| veredito \| fundamento` e veredito geral; §5 18 R-n (`### R-01`..`### R-18`); §6 custo do plano fictício; §7 o que ficou e o que foi descartado; plano fictício em `docs/plans/P-0753-sonda-fantasma/`, removido sem commit, 3 cards. | Q4, S6 |
| F-6 | Corpus das cláusulas do estágio 1: `.claude/tools/*.py` (backlog, encerrar, modelo, materializar, rdo, review_evidence, telemetria_hook, progresso_hook, crenca_hook, ocupacao, uow), `.claude/agents/pantonic-{planner,model-designer,executor,reviewer,scout}.md`, skills `scrum-master`, `diario-de-obras`, `passagem-de-bastao`, `guardrails-check`, `entrega-de-encerramento`, `checar-versao-kit`, `modelo-por-fase`, `.claude/checks/`, `.claude/global/hooks/`, `GOVERNANCA.md`. | Q4 |
| F-7 | Loop do scrum-master (`.claude/skills/scrum-master/SKILL.md`, 435 linhas; não há agente scrum-master em `.claude/agents/`): passos com instrumento — P2 `backlog.py next` (`:50`); P3 `modelo.py check` (`:65`), `card_check.py` (`:70`), `backlog.py despachar` (`:77`); P4 `review_evidence.py --capturar-ref` (`:98`); P6 `review_evidence.py --plano --tarefa` (`:151`); P9 `encerrar.py handover` (`:203`), `encerrar.py tarefa` (`:214`); fora do fluxo `review_evidence.py --atribuir` (`:299`), `encerrar.py plano` (`:365`). Passos sem instrumento: P1 (`:33`), P5 (`:124`), P7 (`:163`), P8 (`:178`), P10 (`:252`). Custo medido no `P-0742` §0 (`docs/plans/P-0742-loop-fora-do-llm.md:19-26`): 7-13 turnos por despacho, $2-6 por tarefa orquestrada, $139,7 em sete sessões; fatos F-4..F-9 e F-13 do `P-0742` (`:98-107`); tabela de roteamento na §12 (`:749` ao fim, 21 linhas). | Q3, S5 |
| F-8 | `docs/telemetria.tsv`, cabeçalho `data	projeto	tarefa	modelo	tool_uses	tokens_k	duracao_s	fonte`: sem coluna de papel; papel só como sufixo manual em `tarefa` (`-revisao`, `-consultor`, `-modelador`; `ORQ` 1 linha); a orquestração praticamente não tem linha própria. | S5 |
| F-9 | `review_evidence.py` `_REGISTRO_ORQUESTRACAO` (`:403-410`) contém `docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/plans/`, `docs/RDO/`, `docs/audits/` — o relatório novo em `docs/audits/` é tratado pelo instrumento como registro de orquestração. | *re-rodado* |
| F-10 | Instrumentos do gate (todos existem e saem 0 em HEAD): `card_check.py --help` (`--plano PLANO --tarefa TAREFA [--root ROOT] [--mundo {antes,depois}] [--gravar [GRAVAR]]`); `modelo.py check --plano docs/plans/P-0753-auditoria-estagio-1/plano.md` → `modelo: OK — 21 operações, 21 objetos, 30 propriedades, 22 tarefas, versão 3`; `backlog.py check` → `check: OK — nenhuma violação.`; `pwsh .claude/checks/check-readme.ps1` → `check-readme: OK - 10 agente(s), 13 skill(s), 20 guardrail(s), …`. `git check-ignore -q` sai 1 para `docs/audits/<novo>.md` e para `docs/plans/P-<n>-x/plano.md` (não ignorados). | Q7 |
| F-11 | Configuração dos papéis (RP-1 aplicado a este plano): frontmatter — executor `sonnet` sem linha `tools:`; planner `Read,Glob,Grep,Write,Edit,Bash`; model-designer `Read,Glob,Grep,Bash,Edit`; reviewer e scout `Read,Glob,Grep,Bash`; consultant `Read,Glob,Grep,Bash,Write,Edit`. `.claude/settings.json` allow: Edit em `/.claude/skills/scrum-master/**`, `/.claude/skills/diario-de-obras/**`, `/.claude/agents/**`, Write em `/.claude/agents/**`; deny: `git push -f/--force`, `reset --hard`, `branch -D`, `clean -fdx`, `gh repo delete`. Nenhuma regra afeta Write em `docs/` nem `python .claude/tools/*`. `.claude/settings.local.json` ausente. | S6/Q6 |
| F-12 | `card_check.py` emite 17 violações (`falhas(_forma)?\.append`): fora da forma da 8.1 (`:212`), âncora sem literal (`:309`), alvo inexistente (`:314`), literal fora da linha (`:324`), nenhum item reconhecido (`:376`), marcador 'Aferição: manual' rejeitado (`:393`, `:441`), comando em bloco cercado ausente (`:400`), `→` ausente (`:404`), Medido antes ausente (`:406`), comando recusado (`:416`, `:470`), divergência Medido antes (`:425`), divergência valor do mundo (`:479`), sem valor antes (`:450`), sem valor esperado (`:456`), esperado sem literal (`:460`). Nenhuma olha o campo **Contingências**. | S1 |
| F-13 | Ensaio da Fase 4 (2026-09-28): cópia de HEAD `2513964` fora do repositório (`%TEMP%\ensaio-p0754`), cards aplicados em sequência. Os TF de `H-10`, `H-13`, `H-14`, `H-15`, `H-18`, `H-19` e `H-20` falham em HEAD e passam com a mudança do card — nenhum dos três itens do primeiro risco da §8 foi absorvido antes; o TF de `H-12` passa sem mudança de código (cobre o comportamento de hoje). Com os 16 cards aplicados: `python -m pytest -q` 505 → 521 passed; `dead_code.py`, `ratchet_piso.py`, `kit_check -Mode validate`, `kit_check -Mode check-drift` e `check-readme.ps1` saem 0. Os valores `antes`/`depois` das Verificações da §5 são os medidos nesse ensaio. | ensaio do planejador |
| F-14 | `review_evidence.py`: `_CAMINHO_RE` (`^[A-Za-z0-9_.][A-Za-z0-9_./\\-]*$`) recusa `*`, e o alvo com curinga cai hoje nos literais descartados de `_classificar_campo_alvos`; `coletar_diff_stat` grava a árvore de trabalho pelo mesmo molde de `capturar_ref` (índice temporário vazio + `git add -A`), e por isso tem o mesmo defeito de `H-19`. | *re-rodado*, ensaio |
| F-15 | `tests/test_encerrar.py`, teste `test_tf_fechado_conta_como_o_indice`, afirma `"plano fechado" in capsys.readouterr().out` — o texto antigo da linha de `H-15`; `grep -rn "fechado; relat" tests` = 0 linhas. | *re-rodado* |
| F-16 | O tíquete do diário tem cabeçalho `## TK-<n> — <título>`, sem sufixo `[` (`DIARIO_DE_OBRAS.md:6150`, `## TK-91 — O modelador não tem o ato…`); o card de tíquete tem `### TK-<n>a — <título> [` (`:5596`, `### TK-84a — …`). O caso do `AE-85` (`concluiu a tarefa "TK-91"`) é o fechamento de um tíquete sem card. | *re-rodado* |
| F-17 | `README.md`: nenhuma ocorrência de `review_evidence`; o painel é descrito na §6 ("com o título da tarefa no lugar da sigla"); a condição 4 da §8 é `4. **Linear.**`; o `README.md` não cita a frase final do `encerrar.py`. | *re-rodado* |

## 3. Decisões

| id | valor | razão |
|---|---|---|
| DAU-1 | O plano entrega o fechamento dos herdados da §2.1 e o relatório novo; **aplicar as R-n do relatório novo fica fora**, para plano sucessor que o dono abre depois de ler o relatório. | Opção do dono "uma varredura nova do kit, que gera um relatório de auditoria" (§0, ato 2); precedente do estágio 1: auditoria (2026-09-27) e aplicação (`P-0753`) foram atos separados. |
| DAU-2 | Ordem: todos os herdados, depois a revisão do `README.md` (fecha a etapa dos herdados), depois — no Marco 2 — a auditoria nova, que é a última tarefa do plano. | Ato 3 do dono: "A auditoria é a última tarefa do plano"; G-README dever 2: a etapa que muda o kit termina com a revisão do `README.md`; a varredura mede o kit com os herdados fechados e o `README.md` revisado; o relatório novo não muda o `README.md` (DAU-1: as R-n não se aplicam aqui). |
| DAU-3 | A auditoria nova é um card do plano **executado pela sessão principal** (quem conduz a sessão, papel de auditor), com modelo Opus; exceção à matriz de papéis válida só para esse card. O loop não o despacha: a linha do card nasce em `estado.tsv` como `blocked`, razão `dependencia`, nota "Marco 2: executado pela sessão principal por instrução do dono"; só quem conduz a sessão a passa a `in-progress`, e só por instrução do dono. O card passa pela revisão (`pantonic-reviewer`) como os demais. | Ato 3 do dono (§0); F-3 (subagente não despacha); F-4 (`+ dono` não filtra `next`, `blocked` filtra). |
| DAU-4 | Método e forma do relatório novo: os do estágio 1 (F-5), cláusula por cláusula — modelo em seis operações, cláusulas K-n com residência e teste, registros com a legenda L/E/C/$/Q/M/F, conclusão pelas oito dimensões, R-n, custo do plano fictício, o que ficou e o que foi descartado. Corpus das cláusulas: o de F-6 acrescido do que os herdados mudaram. Plano fictício numa pasta de rascunho removida no fim, sem commit. | Ato 2 do dono ("no formato usado na auditoria de encerramento do estágio 1"); F-5. |
| DAU-5 | `H-21` (AE-95): avaliação sem implementação. O relatório novo traz uma seção própria que, por passo P1..P10 do loop (F-7), dá: se a ação é mecânica, qual instrumento já a cobre, o custo medido no loop real do plano fictício; e R-n para cada ação mecanizável. O scrum-master fica no loop. | Veredito do dono (§0, AE-95: "matéria de avaliação"); ato 3 ("medida no loop real, com o custo real de orquestrar"); DAU-1. |
| DAU-6 | `H-16` (AE-88): vira cláusula K-n da auditoria nova ("rodada de replanejamento grava medida"), com diagnóstico de residência e R-n. | Residência não apurada em duas rodadas de levantamento (§2.1 H-16); o que sobra desconhecido é investigação, e a investigação cabível é a própria auditoria; DAU-1. |
| DAU-7 | Fecham **sem mudança no kit**, com a prova da §2.1 como registro: `H-6` (AE-21, teto conhecido do instrumento), `H-7` (AE-22, regra existente), `H-11` (AE-51 do `P-0752`, premissa caída), `H-17` (AE-89, premissa caída). | Provas em §2.1; diretiva (2) de 2026-09-26: nenhum card por ajuste. |
| DAU-8 | `H-1` + `H-8` (pendência 1 e AE-24, com DAF-47 do `P-0753`), doutrina em `.claude/agents/pantonic-planner.md` e `docs/RUBRICA_DE_REVISAO.md`: (i) o item 14 da Fase 4 ensaia também cada contingência — a ação aplicada na cópia e as Verificações re-rodadas; (ii) regra nova: a ação da contingência não contradiz nenhuma Restrição do mesmo card, e arquivo que ela escreve entra nos Arquivos-alvo marcado "(condicional: contingência <n>)"; (iii) critério correspondente na rubrica. Mecanizar (ii) no `card_check.py` fica como candidato a R-n do relatório novo. | F-12 (nenhuma checagem sobre Contingências); remédio do laudo AE-24 (§2.1 H-8); DAU-1. |
| DAU-9 | `H-2`, `H-3`, `H-4` (AE-8, AE-13, AE-18 parte): os três casos concretos entram no item 8 (teste de interrupção) da Fase 4 de `pantonic-planner.md` como pontos de parada nomeados — Objetivo condicional contra Contratos incondicionais; argumento de caminho sem forma fixada (relativo ou absoluto); normalização e recusas do argumento não fechadas no card. | Genérico já existe (`pantonic-planner.md:329`); os casos medidos são o que o genérico não pegou. |
| DAU-10 | `H-5` (AE-20): regra nova na Rodada de replanejamento de `pantonic-planner.md`: restrição de card que cita estado do plano é re-conferida quando o modelador grava versão pendente. | Remédio do laudo (§2.1 H-5). |
| DAU-11 | `H-9` (RP-1): a Fase 1 de `pantonic-planner.md` ganha a verificação "diante de 'o papel X não consegue Y', perguntar primeiro se o impedimento é configuração do kit (frontmatter `tools:`, `settings*.json`) ou limite da plataforma". | RP-1 do `P-0753` (`plano.md:1758`). |
| DAU-12 | `H-10` (AE-50 do `P-0752`): TF de arquivo não rastreado criado depois do ref, que tem de sair com diff e não com conteúdo integral; se o TF passa em HEAD antes de qualquer mudança, o item fecha como absorvido pelo `TK-93a` e o teste fica como TR. | §2.1 H-10 (`capturar_ref` já usa índice temporário). |
| DAU-13 | `H-12` (AE-83): TF do ramo de caminho ausente em `coletar_arquivos_tocados` (`review_evidence.py:349-352`) com caminho não-ASCII que o git devolve com escape octal. | §2.1 H-12. |
| DAU-14 | `H-13` (AE-84): `montar_trechos` expande bullet de Arquivos-alvo que contém `*` contra os arquivos da árvore, e marca alvo não rastreado sem "antes" como novo. | §2.1 H-13. |
| DAU-15 | `H-14` (AE-85): `localizar_card` (`progresso_hook.py:143`) casa também o cabeçalho de tíquete `## <id> — ` e devolve o título dele. | §2.1 H-14. |
| DAU-16 | `H-15` (AE-86): a linha de `encerrar.py:1293` passa a `print(f"encerrar: OK - comando '{args.comando}' concluído; relatório em '{destino}'.")` — forma sem concordância de gênero com o nome do subcomando. | §2.1 H-15. |
| DAU-17 | `H-18` (AE-92): em `confrontar_escopo` (`review_evidence.py:534-538`), `_eh_registro_orquestracao` é testado antes de `_tarefa_dona`. | §2.1 H-18. |
| DAU-18 | `H-19` (AE-93): `capturar_ref` semeia o índice temporário com `git read-tree HEAD` antes do `git add -A`. | §2.1 H-19. |
| DAU-19 | `H-20` (AE-94): `_nao_rastreado_mudou_desde_ref` compara bytes quando a decodificação UTF-8 falha, em vez de devolver `True`. | §2.1 H-20. |
| DAU-20 | Achado novo durante a execução deste plano vira `AE-<n>` na §9 e entra no relatório novo como registro; nenhum card corretivo nem tíquete por ajuste. | Diretiva (2) de 2026-09-26 (§0). |
| DAU-21 | O card da auditoria declara o relatório em `docs/audits/` nos Arquivos-alvo sabendo que `review_evidence.py` classifica `docs/audits/` como registro de orquestração (F-9); a Verificação do card mede o relatório por conteúdo no arquivo (literais de seção e contagens), não pelo trecho de diff da evidência. | F-9; F-10. |
| DAU-22 | `H-13`, curinga: `_CAMINHO_RE` aceita `*`; o alvo com `*` casa por `fnmatch.fnmatchcase`, com separador normalizado, contra os **tocados** — o mesmo conjunto contra o qual o alvo-diretório já se expande — em `montar_trechos` (um trecho por tocado que casa; sem casamento, uma entrada com o texto `(nenhum arquivo tocado casa com o curinga)`) e na cobertura de `confrontar_escopo`; a atribuição a outra tarefa (`_tarefa_dona`) não muda. | F-14; "os arquivos da árvore" da `DAU-14` lidos como os tocados, porque o trecho de arquivo não tocado seria `(sem alteração)` e não informa ao revisor; a operação fala dos alvos **do card**. |
| DAU-23 | `H-13`, alvo novo: o trecho de alvo não rastreado ausente da base abre com a linha `(arquivo novo — ausente em <base>)`, a base entre crases — `<ref>` com `--desde`, `HEAD` sem ele. | Literal fixo, testável, e que não depende da forma do diff. |
| DAU-24 | `H-10`, forma: com `--desde`, o não rastreado ausente de `<ref>` sai como `difflib.unified_diff` contra o vazio, com `fromfile=f"{caminho}@{desde}"`, no molde do ramo do `TK-93a`. | F-13 (o TF falha em HEAD); mesmo molde do ramo vizinho. |
| DAU-25 | `H-19`, residência única: função nova `_gravar_arvore_de_trabalho(root) -> str`, que semeia o índice temporário com `git read-tree HEAD` quando há `HEAD`; `capturar_ref` e `coletar_diff_stat` a chamam. | F-14 (o irmão tem a mesma matéria e o mesmo defeito); a correção de um é o momento de o outro sair auditável (Fase 4 item 7, `RP-7`). |
| DAU-26 | `H-14`: o tíquete (`## <id> — <título>`) devolve `(título, "", "")` — objetivo e título de plano vazios; o card de tíquete segue como hoje. | F-16; o tíquete não mora dentro de um plano, e título de plano vazio não gera a frase de abertura de plano no painel. |
| DAU-27 | `H-15`: a asserção de `test_tf_fechado_conta_como_o_indice` passa ao texto novo no mesmo card. | F-15; resposta pré-decidida do segundo risco da §8. |
| DAU-28 | `H-6`, `H-7`, `H-11`, `H-17`: o desfecho se registra na própria linha do `AE-<n>` de origem, como sufixo ` · **Desfecho (P-0754, AUF-T14, 2026-09-28):** encerrado sem mudança no kit — <prova da §2.1>`. | A linha de origem é onde a rota "auditoria final" foi escrita e onde a busca por ela chega; DAU-7. |
| DAU-29 | `README.md`: três passagens — o painel (§6) passa a dizer card de plano ou tíquete; um bullet novo de `review_evidence.py` na §11; a condição 4 da §8 ganha a frase da contingência. As regras de `H-2..H-5`, `H-9` e o critério novo da rubrica não vão ao guia. | F-17; o guia descreve o que quem chega usa, e as regras internas do planejador e do revisor já moram nos próprios arquivos. |
| DAU-30 | Relatório novo em `docs/audits/AUDITORIA_FINAL_KIT.md`, data de execução no cabeçalho, com as seções 0 a 7 do estágio 1 e a §8 das ações mecânicas do gerente (`DAU-5`); plano fictício em `docs/plans/P-<n>-sonda-auditoria-final/`, `<n>` o próximo id do `_INBOX.md` no retrato inicial; retrato e limpeza no molde do estágio 1 (F-5). | Nome fixo torna o card executável sem escolha; F-5; DAU-4. |
| DAU-31 | Residências da doutrina em `.claude/agents/pantonic-planner.md`: `DAU-8` (ii) no item 3 da Fase 4 (vale para toda classe de plano) e (i) no item 14 (dosado pela classe); `DAU-9` no item 8; `DAU-10` no passo 4 da Rodada de replanejamento; `DAU-11` como bullet da Fase 1. `DAU-8` (iii) é a linha `(xix)` da tabela da §8 de `docs/RUBRICA_DE_REVISAO.md`. | A tabela de dosagem da Fase 4 aplica o item 14 só com arquivo compartilhado; a regra (ii) tem de valer sempre. |
| DAU-32 | `AE-97` (a `AUF-T2` apagou `assert "+linha-1" not in texto` do TR da `AUF-T1`): o consultor repõe a linha no ato, fora de card, como reparo de instrumento que nenhum card cobre; a `AUF-T2` fecha com a ressalva sanada, sem card corretivo e sem redespacho. Medido depois do reparo: `git diff 3be2450 --numstat -- tests/test_review_evidence.py` = `20 0`; `-k "arquivo_novo_sem_desde or caminho_acentuado"` exit 0; suíte `508 passed`. | Laudo `laudos/AUF-T2.md` (testes parcial); regra A8 do loop (erro inequívoco não se adia); `DAU-20` (nenhum card corretivo por ajuste). |
| DAU-33 | Laudo da `AUF-T16` (`criterio-de-pronto` parcial, ressalva 90%): o consultor corrige no ato o relatório `docs/audits/AUDITORIA_FINAL_KIT.md`, fora de card — seis `R-<nn>` novas (`R-26`..`R-31`) para os reg. 13, 14, 17, 18, 27 e 28; linhas `K-39`..`K-43` para `.claude/checks/` e as skills `guardrails-check`, `diario-de-obras`, `passagem-de-bastao` e `checar-versao-kit`, e `GOVERNANCA.md` §3.2 na residência da `K-16`; reg. 49..54 para `K-39`..`K-42`, `K-22` e `K-33` (medidos: checks rodados na árvore, as 5 evidências do `P-0755`, o painel `.claude/estado/progresso.txt`), `K-09` citada no reg. 9 e `K-43` no reg. 15; reg. 41 e `R-16` corrigidos (o planejador da SAÍDA 1 está na série como `P-0754-planejador`, atribuído pelo id da primeira mensagem, `telemetria_hook.py:338-339`); reg. 27 cita `AE-104` e não `AE-103`; "20/20 aprovadas" vira 19 aprovadas e 1 ressalva. Os defeitos em herdado fechado dos reg. 23, 24 e 36 entram como `AE-114`..`AE-116` (contingência 2). A `AUF-T16` fecha com a ressalva sanada, sem redespacho. Medido: Verificações 1 a 6 da `AUF-T16` = `[9]`, `[8]`, `[10]`, `[1]`, `[1-1]`, `[1]`; 0 registro `inadequado`/`oportunidade` sem `Origem:` na §5; 0 `K` da §2 sem registro na §3; 0 item do corpus do passo 3 sem linha `K`; 307 linhas (teto 450). | Laudo `laudos/AUF-T16.md`; regra A8 do loop; `DAU-20`; precedente `DAU-32`. |

## 4. Invariantes de execução

Valem para todos os cards; cada card repete, inline, a parte que o vincula.

1. **Nenhuma mudança fora do inventário.** Um card só altera o que a sua operação declara e o item `H-<n>` da
   §2.1 que ela fecha. Achado novo → `AE-<n>` na §9 deste plano (DAU-20), nunca edição extra.
2. **O scrum-master fica no loop.** Nenhum card remove, funde ou substitui passo de
   `.claude/skills/scrum-master/SKILL.md`; a matéria do `AE-95` é avaliação (DAU-5).
3. **As R-n do relatório novo não se aplicam neste plano** (DAU-1).
4. **Exceção de papel única.** Só o card da auditoria nova é executado pela sessão principal (DAU-3); todo
   outro card é executado por subagente executor, uma tarefa por contexto.
5. **Nada escreve no índice real, na lista de stash nem na árvore fora dos Arquivos-alvo.** Proibido
   `git stash push`, `git add` sobre o índice real, `git reset --hard`, `git clean`. Testes de
   `review_evidence.py` rodam em repositório temporário (`tmp_path`).
6. **Piso de regressão é relação.** A entrega não reduz o total da suíte re-medido no despacho e soma os TF
   novos; nenhum total de suíte entra como número de aceite.
7. **Literal de aceite.** `Select-String` de aceite leva `-SimpleMatch`; comando com crase, asterisco ou
   barra invertida vai em bloco cercado; bloco literal com cabeçalho markdown entra recuado dois espaços;
   toda Verificação por efeito em arquivo publica os valores antes e depois.
8. **O plano fictício da auditoria nova** vive numa pasta de rascunho, é removido no fim e nada dele é
   commitado (DAU-4).
9. **Regra de dependência** `infracore ← contracts ← services ← plugins`, nunca no inverso; os instrumentos
   de `.claude/tools/` não importam código de projeto consumidor.

## 5. Tarefas

Um card por operação da §1, na ordem das operações; `AUF-T<n>` materializa `OP-<n>`. Os valores `antes` e `depois` das
Verificações foram medidos no ensaio da Fase 4 (cópia de HEAD `2513964` fora do repositório, 2026-09-28, `F-13`).

### AUF-T1 — O arquivo criado depois do recorte chega ao revisor como diferença [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa faz o instrumento de evidência mostrar como diferença, e não como conteúdo inteiro, o arquivo novo criado depois do recorte do despacho.
- **Fundamento:** `DAU-12`, `DAU-24`; `H-10` (§2.1); `F-13` (o TF falha em HEAD: o item não foi absorvido pelo `TK-93a`).
- **Operação do modelo:** `OP-1`
  - OP-1: Quem executa faz o instrumento de evidência mostrar como diferença, e não como conteúdo inteiro, o arquivo novo criado depois do recorte do despacho.
  - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; não importa de `tests/` nem de projeto consumidor; roda `git` por `subprocess` sem escrever no índice real, na lista de stash nem na árvore de trabalho.
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
- **Contratos/classes:** `_diff_para_arquivo(root: Path, caminho_rel: str, desde: str | None = None) -> str` — assinatura inalterada. Regra nova, dentro do ramo `if desde is not None:`, depois do bloco do `TK-93a` (o que começa em `if _eh_nao_rastreado(root, caminho_rel) and _existe_no_ref(root, desde, caminho_rel):`) e antes da chamada `_git(["diff", desde, "--", caminho_rel], root)`: arquivo com `_eh_nao_rastreado(root, caminho_rel)` verdadeiro — ali ele já é ausente de `<ref>`, porque o bloco anterior devolveu o presente — tem o texto lido por `_texto_do_disco(root, caminho_rel)`; texto `None` devolve a linha que o bloco do `TK-93a` já usa, `(arquivo binário ou não-UTF-8 — trecho omitido)`; texto lido devolve o diff unificado contra o vazio, no molde do bloco do `TK-93a`: `difflib.unified_diff([], texto_atual.splitlines(), fromfile=f"{caminho_rel}@{desde}", tofile=caminho_rel, lineterm="")`, linhas unidas por quebra de linha e uma quebra final. Sem `desde`, nada muda.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_review_evidence.py` os dois testes da seção `Testes`, no molde de `test_tf_nao_rastreado_no_ref_mostra_so_o_hunk` (fixture `_init_repo_com_baseline`, `review_evidence.capturar_ref`, `review_evidence.montar_trechos`).
  2. Rodar `python -m pytest tests/test_review_evidence.py -q -k "arquivo_novo_depois_do_recorte"` e conferir que o TF falha.
  3. Acrescentar em `_diff_para_arquivo` o ramo de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `505 passed`, 2026-09-28, HEAD `2513964`).
  - `python .claude/checks/dead_code.py` sai 0 e `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`; os testes criam o próprio repositório em `tmp_path` com `_init_repo_com_baseline`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar o bloco do `TK-93a` nem o caminho sem `desde` de `_diff_para_arquivo`; não mudar `coletar_arquivos_tocados`, `capturar_ref` nem `montar_trechos`; não acrescentar marca de arquivo novo ao trecho (é da `AUF-T3`).
- **Contingências:**
  - se o TF `test_tf_arquivo_novo_depois_do_recorte_sai_como_diferenca` passar no passo 2, antes de qualquer mudança em `.claude/tools/review_evidence.py` → seguir sem o passo 3, com o TF como guarda, e devolver `contingência 1 acionada: absorvido em HEAD`.
  - se um teste que já existia em `tests/test_review_evidence.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_arquivo_novo_depois_do_recorte_sai_como_diferenca` — repositório de `_init_repo_com_baseline`, `ref = review_evidence.capturar_ref(repo)`, depois `novo.md` criado com as linhas `linha-1` e `linha-2`; o texto de `montar_trechos(repo, ["novo.md"], 4000, desde=ref)["novo.md"]` contém `+linha-1` e `+linha-2` (a regra antiga devolve o conteúdo integral, sem `+`). TR `test_tr_arquivo_novo_sem_desde_segue_com_conteudo_integral` — o mesmo arquivo, sem `ref` e sem `desde`: o texto contém as duas linhas seguidas, com a quebra de cada uma, e não contém `+linha-1`. Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_review_evidence.py -q -k "arquivo_novo_depois_do_recorte or arquivo_novo_sem_desde"` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - dossiê de evidência.arquivo novo depois do recorte — o arquivo novo chega ao revisor como diferença contra o recorte, com um teste que o prova; se já chegava assim, o item fecha como resolvido antes e o teste fica de guarda — Verificação 1
- **Fora do escopo desta tarefa:** a marca de arquivo novo e o alvo com curinga (`AUF-T3`); o arquivo versionado e ignorado (`AUF-T5`); o arquivo que não é texto (`AUF-T6`).
- **Handover:** 2026-09-28 · para `AUF-T2`, `AUF-T3`
  - **Entregue:** ramo novo em _diff_para_arquivo (.claude/tools/review_evidence.py:601-614): não rastreado ausente do <ref> sai como diff unificado contra o vazio; TF test_tf_arquivo_novo_depois_do_recorte_sai_como_diferenca (tests/test_review_evidence.py:1403) e TR test_tr_arquivo_novo_sem_desde_segue_com_conteudo_integral (:1422)
  - **Contrato:** com desde, arquivo novo depois do recorte chega ao revisor com linhas '+'; sem desde, conteúdo integral como antes; bloco do TK-93a e assinatura intactos
  - **Não refazer:** o ramo de arquivo novo em _diff_para_arquivo
  - **Pendente:** arquivo novo VAZIO sai como bloco em branco (achado do laudo, a fechar com a marca de arquivo novo da AUF-T3)

### AUF-T2 — Um teste exercita o caminho com acento que o versionador devolve em código [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa cobre com teste o trecho do instrumento de evidência que lê o caminho com acento devolvido em código pelo versionador.
- **Fundamento:** `DAU-13`; `H-12` (§2.1); `F-13`.
- **Depende de:** `AUF-T1`
- **Operação do modelo:** `OP-2`
  - OP-2: Quem executa cobre com teste o trecho do instrumento de evidência que lê o caminho com acento devolvido em código pelo versionador.
  - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.
- **Camada e fronteira:** suíte do kit (`tests/`); o instrumento `.claude/tools/review_evidence.py` não muda nesta tarefa.
- **Arquivos-alvo:**
  - `tests/test_review_evidence.py`
- **Contratos/classes:** o trecho coberto é o de `coletar_arquivos_tocados(root: Path, desde: str | None = None) -> list[str]`, com `desde`: a linha `??` do `git status` cujo caminho, lido por `_extrair_caminho_status` (que tira as aspas e não decodifica o escape octal), não existe no disco entra nos tocados, porque o salto `if arquivo.exists() and arquivo.stat().st_mtime < corte: continue` não dispara. Com `core.quotepath` ligado, o `git status` devolve `ação.txt` como `"a\303\247\303\243o.txt"`; o caminho que entra nos tocados é `a\303\247\303\243o.txt` — em Python, a string `"a\\303\\247\\303\\243o.txt"`.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_review_evidence.py` o teste da seção `Testes`: repositório de `_init_repo_com_baseline`, `_run_git(["config", "core.quotepath", "true"], repo)`, `ref = review_evidence.capturar_ref(repo)`, depois `(repo / "ação.txt")` criado com uma linha de texto.
  2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma o 1 teste novo (referência datada: `505 passed`, 2026-09-28, HEAD `2513964`).
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`; o teste cria o próprio repositório em `tmp_path` com `_init_repo_com_baseline`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `.claude/tools/review_evidence.py` — nem para decodificar o escape octal: o card cobre o comportamento de hoje; não depender da configuração global do `git` (o teste liga `core.quotepath` no próprio repositório).
- **Contingências:**
  - se, com `core.quotepath` ligado no repositório do teste, a lista devolvida não for exatamente `["a\\303\\247\\303\\243o.txt"]` → parar e sinalizar `blocked` razão `premissa`, colando a lista devolvida e a saída de `git status --porcelain=v1 --untracked-files=all` do repositório do teste.
- **Testes:** TF `test_tf_caminho_acentuado_do_status_entra_nos_tocados_pelo_ramo_de_caminho_ausente` — `review_evidence.coletar_arquivos_tocados(repo, desde=ref)` devolve exatamente `["a\\303\\247\\303\\243o.txt"]` (a regra concorrente, que pulasse o caminho ausente do disco, devolveria `[]`). Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_review_evidence.py -q -k "caminho_acentuado"` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - dossiê de evidência.caminho com acento — um teste exercita o trecho com um caminho acentuado de verdade — Verificação 1
- **Fora do escopo desta tarefa:** decodificar o escape octal do `git status` (não pedido pela operação; se a revisão o julgar defeito, vira `AE-<n>` na §9).
- **Handover:** 2026-09-28 · para `AUF-T3`
  - **Entregue:** TF test_tf_caminho_acentuado_do_status_entra_nos_tocados_pelo_ramo_de_caminho_ausente em tests/test_review_evidence.py (fim do arquivo); assert '+linha-1' do TR da AUF-T1 reposto pelo consultor (DAU-32)
  - **Contrato:** coletar_arquivos_tocados com core.quotepath devolve o caminho com escape octal cru; comportamento de hoje coberto, instrumento intocado
  - **Não refazer:** nada a declarar
  - **Pendente:** caminho com escape octal chega a montar_trechos como arquivo ausente (AE-99, à AUF-T16)

### AUF-T3 — O alvo com curinga casa, e o alvo que não existia chega marcado como novo [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** Quem executa faz o instrumento de evidência reconhecer, entre os alvos do card, o nome escrito com curinga e o arquivo que ainda não existia.
- **Fundamento:** `DAU-14`, `DAU-22`, `DAU-23`; `H-13` (§2.1); `F-13`, `F-14`.
- **Depende de:** `AUF-T2`
- **Operação do modelo:** `OP-3`
  - OP-3: Quem executa faz o instrumento de evidência reconhecer, entre os alvos do card, o nome escrito com curinga e o arquivo que ainda não existia.
  - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão (`fnmatch` entra no `import`); não importa de `tests/` nem de projeto consumidor; roda `git` por `subprocess` sem escrever no índice real, na lista de stash nem na árvore de trabalho.
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
- **Contratos/classes:** assinaturas públicas inalteradas. Cinco regras:
  1. `_CAMINHO_RE` aceita `*` nas duas classes de caractere: `re.compile(r"^[A-Za-z0-9_.*][A-Za-z0-9_./\\*-]*$")`; o resto de `_eh_caminho` não muda.
  2. Função nova `_eh_alvo_curinga(alvo: str) -> bool` — verdadeiro quando o alvo contém `*`.
  3. `montar_trechos(root, arquivos_alvo, teto_chars, tocados=None, desde=None)`: alvo com curinga, testado antes do alvo-diretório, casa por `fnmatch.fnmatchcase(_normalizar_separador(arquivo), _normalizar_separador(alvo))` contra cada item de `tocados` (lista vazia quando `tocados` é `None`); cada tocado que casa ganha a própria entrada, com o texto de `_diff_para_arquivo(root, arquivo, desde)` e o mesmo truncamento das demais; curinga sem tocado que case ganha uma entrada só, com a chave igual ao próprio alvo, `truncado` falso e o texto exato `(nenhum arquivo tocado casa com o curinga)`.
  4. `confrontar_escopo`: a função interna `coberto` dá por coberto também o tocado que, com separador normalizado, casa por `fnmatch.fnmatchcase` com algum alvo com curinga do card; a atribuição a outra tarefa (`_tarefa_dona`) não muda.
  5. `_diff_para_arquivo`: o trecho de arquivo não rastreado (`_eh_nao_rastreado`) ausente da base abre com uma linha de marca e a quebra dela, antes do resto do texto. Com `desde`, no ramo da `AUF-T1`, a base é `<ref>`; sem `desde`, no ramo final que lê o conteúdo integral do arquivo que existe na árvore, a base é `HEAD`, e a marca só entra quando o arquivo é não rastreado — o rastreado sem diferença segue como hoje. As duas linhas de marca, exatas (as quebras são as do bloco; cada linha perde o recuo da cerca do bloco; `<ref>` é o valor de `desde`):

     ```text
     (arquivo novo — ausente em `<ref>`)
     (arquivo novo — ausente em `HEAD`)
     ```
- **Passos:**
  1. Acrescentar ao fim de `tests/test_review_evidence.py` os quatro testes da seção `Testes`, no molde de `test_tf_nao_rastreado_no_ref_mostra_so_o_hunk`.
  2. Rodar `python -m pytest tests/test_review_evidence.py -q -k "curinga or marcado_como_novo"` e conferir que os três primeiros falham.
  3. Aplicar em `.claude/tools/review_evidence.py` as cinco regras de `Contratos/classes`, com `import fnmatch` na lista de imports.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 4 testes novos (referência datada: `505 passed`, 2026-09-28, HEAD `2513964`).
  - `python .claude/checks/dead_code.py` sai 0 e `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`; os testes criam o próprio repositório em `tmp_path` com `_init_repo_com_baseline`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não expandir o curinga contra a árvore inteira (só contra os tocados, `DAU-22`); não mudar `_tarefa_dona` nem `mapear_alvos_de_outras_tarefas`; não mudar o ramo do `TK-93a`; não marcar como novo o arquivo rastreado.
- **Contingências:**
  - se um teste que já existia em `tests/test_review_evidence.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_alvo_com_curinga_casa_os_tocados` — `ref = capturar_ref(repo)`, depois `relatorios/a.md` e `relatorios/b.md` criados; `` extrair_arquivos_alvo({"arquivos-alvo": "- `relatorios/*.md`"}) `` devolve `["relatorios/*.md"]`; com `tocados = coletar_arquivos_tocados(repo, desde=ref)`, as chaves de `montar_trechos(repo, alvos, 4000, tocados, desde=ref)` são exatamente `relatorios/a.md` e `relatorios/b.md`, e `confrontar_escopo(tocados, alvos, repo)["fora_dos_alvos"]` é `[]` (a regra antiga descartava o literal, dava uma entrada só com a chave do padrão e punha os dois arquivos fora dos alvos). TR `test_tr_alvo_com_curinga_sem_tocado_diz_que_nada_casa` — `montar_trechos(repo, ["relatorios/*.md"], 4000, [], desde=ref)` é exatamente o dicionário de uma entrada, chave `relatorios/*.md`, texto `(nenhum arquivo tocado casa com o curinga)`, `truncado` falso. TF `test_tf_alvo_nao_rastreado_sem_antes_sai_marcado_como_novo` — `novo.md` criado depois do `ref`: o texto com `desde=ref` começa pela marca de `<ref>` com o valor do `ref` e a quebra; sem `desde`, começa pela marca de `HEAD` e a quebra. TR `test_tr_alvo_rastreado_alterado_nao_leva_a_marca_de_novo` — `src/b.py` alterado depois do `ref`: o texto com `desde=ref` traz a linha nova com `+` e não contém `(arquivo novo`. Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_review_evidence.py -q -k "curinga or marcado_como_novo or marca_de_novo"` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - dossiê de evidência.leitura dos alvos do card — o alvo com curinga casa com os arquivos da árvore, e o alvo que não existia antes chega marcado como novo — Verificação 1
- **Fora do escopo desta tarefa:** o curinga no alvo de outra tarefa do mesmo plano (`_tarefa_dona`, não pedido pela operação); a diferença do arquivo novo contra o recorte (`AUF-T1`, já entregue).
- **Handover:** 2026-09-28 · para `AUF-T4`, `AUF-T5`, `AUF-T6`
  - **Entregue:** review_evidence.py: _CAMINHO_RE aceita '*'; _eh_alvo_curinga (:404); montar_trechos casa curinga contra os tocados, com '(nenhum arquivo tocado casa com o curinga)' (:674); confrontar_escopo.coberto aceita curinga; marca '(arquivo novo — ausente em <ref>/HEAD)' em _diff_para_arquivo (:626, :643); 4 testes em tests/test_review_evidence.py:1458-1518+
  - **Contrato:** alvo com curinga casa só contra os tocados (fnmatchcase: '*' atravessa '/'); não rastreado ausente da base abre com a linha de marca; rastreado não leva marca
  - **Não refazer:** curinga em montar_trechos/confrontar_escopo e a marca de arquivo novo
  - **Pendente:** nenhum

### AUF-T4 — O que quem conduz escreve nos próprios registros conta como registro da condução [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa faz o instrumento de evidência atribuir à condução, e não a um tíquete, o que quem conduz escreve nos próprios registros.
- **Fundamento:** `DAU-17`; `H-18` (§2.1); `F-9`, `F-13`.
- **Depende de:** `AUF-T3`
- **Operação do modelo:** `OP-4`
  - OP-4: Quem executa faz o instrumento de evidência atribuir à condução, e não a um tíquete, o que quem conduz escreve nos próprios registros.
  - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; não importa de `tests/` nem de projeto consumidor.
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
- **Contratos/classes:** `confrontar_escopo(tocados, arquivos_alvo, root, alvos_de_outras_tarefas=None) -> dict` — assinatura e chaves do dicionário inalteradas. No laço sobre os tocados não cobertos, `_eh_registro_orquestracao(tocado)` se testa **antes** de `_tarefa_dona(tocado_norm, outros, root)`: o tocado que é registro da condução vai para `registro_orquestracao` e não chega à busca de tarefa dona. A precedência nova, que a docstring de `confrontar_escopo` passa a enunciar no lugar da antiga: coberto pelos alvos do card > registro da orquestração > alvo de outra tarefa do mesmo plano > ato do dono fora do ciclo de tarefa > fora dos alvos sem atribuição. `_REGISTRO_ORQUESTRACAO` não muda: `docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, `docs/ACIONAMENTOS_CONSULTOR.tsv`, `docs/plans/`, `docs/RDO/`, `docs/audits/`.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_review_evidence.py` os dois testes da seção `Testes`.
  2. Rodar `python -m pytest tests/test_review_evidence.py -q -k "escrita_da_conducao"` e conferir que o TF falha.
  3. Trocar a ordem dos dois testes em `confrontar_escopo` e a frase de precedência da docstring, pela regra de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `505 passed`, 2026-09-28, HEAD `2513964`).
  - `python .claude/checks/dead_code.py` sai 0 e `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`; os testes criam o próprio repositório em `tmp_path` com `_init_repo_com_baseline`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `_REGISTRO_ORQUESTRACAO`, `_tarefa_dona`, `formatar_atribuicoes` nem a cobertura pelos alvos do próprio card, que segue em primeiro.
- **Contingências:**
  - se um teste que já existia em `tests/test_review_evidence.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_escrita_da_conducao_vence_o_alvo_de_outra_tarefa` — `confrontar_escopo(["docs/DIARIO_DE_OBRAS.md"], ["src/b.py"], repo, {"docs/DIARIO_DE_OBRAS.md": "TK-1a"})` devolve `registro_orquestracao == ["docs/DIARIO_DE_OBRAS.md"]` e `de_outra_tarefa == {}` (a regra antiga devolve `{"docs/DIARIO_DE_OBRAS.md": "TK-1a"}` e `[]`). TR `test_tr_alvo_de_outra_tarefa_fora_do_registro_segue_atribuido` — `confrontar_escopo(["src/c.py"], ["src/b.py"], repo, {"src/c.py": "TK-1a"})` devolve `de_outra_tarefa == {"src/c.py": "TK-1a"}` e `registro_orquestracao == []`. Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_review_evidence.py -q -k "escrita_da_conducao or fora_do_registro_segue"` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - dossiê de evidência.atribuição das escritas da condução — essa escrita conta como registro da condução antes de se procurar um tíquete dono — Verificação 1
- **Fora do escopo desta tarefa:** o recorte do arquivo versionado e ignorado (`AUF-T5`).
- **Handover:** 2026-09-28 · para `AUF-T5`
  - **Entregue:** confrontar_escopo testa _eh_registro_orquestracao antes de _tarefa_dona (.claude/tools/review_evidence.py, laço de confrontar_escopo) e a docstring enuncia a precedência nova; TF/TR test_tf_escrita_da_conducao_vence_o_alvo_de_outra_tarefa e test_tr_alvo_de_outra_tarefa_fora_do_registro_segue_atribuido no fim de tests/test_review_evidence.py
  - **Contrato:** precedência: coberto pelos alvos > registro da orquestração > alvo de outra tarefa > ato do dono > fora dos alvos
  - **Não refazer:** a ordem registro-antes-de-tarefa-dona
  - **Pendente:** nenhum

### AUF-T5 — O recorte parte de tudo o que já está versionado [Sonnet · esforço medium · classe implementacao]
- **Objetivo:** Quem executa faz o instrumento de evidência incluir no recorte o arquivo já versionado que a lista de ignorados também cobre.
- **Fundamento:** `DAU-18`, `DAU-25`; `H-19` (§2.1); `F-13`, `F-14` (o resumo de diferenças grava a árvore pelo mesmo molde e tem o mesmo defeito).
- **Depende de:** `AUF-T4`
- **Operação do modelo:** `OP-5`
  - OP-5: Quem executa faz o instrumento de evidência incluir no recorte o arquivo já versionado que a lista de ignorados também cobre.
  - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; roda `git` por `subprocess` com índice temporário (`GIT_INDEX_FILE`), sem escrever no índice real, na lista de stash nem na árvore de trabalho.
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
- **Contratos/classes:** função nova `_gravar_arvore_de_trabalho(root: Path) -> str` — residência única da gravação da árvore de trabalho: cria o índice temporário como `capturar_ref` já cria (arquivo de `tempfile.mkstemp`, apagado antes do uso e no `finally`), e, quando `git rev-parse --verify HEAD` sai 0, roda `git read-tree HEAD` nesse índice antes do `git add -A`; sem commit ainda, o índice parte vazio como hoje; devolve o hash de `git write-tree`. `capturar_ref(root: Path) -> str` e `coletar_diff_stat(root: Path, desde: str | None = None) -> str` passam a obter a árvore só por `_gravar_arvore_de_trabalho(root)` — o bloco de índice temporário de cada uma sai —, e o resto delas não muda (pai, `commit-tree`, mensagem, `git diff --stat`). Docstring da função nova diz que ela é chamada pelas duas.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_review_evidence.py` o auxiliar e os dois testes da seção `Testes`.
  2. Rodar `python -m pytest tests/test_review_evidence.py -q -k "versionado"` e conferir que os dois falham.
  3. Criar `_gravar_arvore_de_trabalho` e fazer `capturar_ref` e `coletar_diff_stat` a chamarem, pela regra de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `505 passed`, 2026-09-28, HEAD `2513964`).
  - `python .claude/checks/dead_code.py` sai 0 e `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`; os testes criam o próprio repositório em `tmp_path` com `_init_repo_com_baseline`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não usar `git stash create` nem o índice real; não mudar `coletar_arquivos_tocados`, que passa a acertar pelo `<ref>` novo sem mudança própria.
- **Contingências:**
  - se um teste que já existia em `tests/test_review_evidence.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** auxiliar `_repo_com_versionado_ignorado(tmp_path: Path) -> Path` — repositório de `_init_repo_com_baseline`; `.gitignore` reescrito com `__pycache__/` e `versionado.log`; `versionado.log` criado com `v1`, adicionado com `git add -f` e commitado junto do `.gitignore`. TF `test_tf_capturar_ref_inclui_versionado_que_o_gitignore_cobre` — `versionado.log` reescrito com `v2`; depois de `ref = capturar_ref(repo)`, `git show <ref>:versionado.log` sai 0 com a saída `v2` e a quebra (a regra antiga sai diferente de 0: o `<ref>` não tem o arquivo). TF `test_tf_versionado_ignorado_intocado_fica_fora_dos_tocados_e_alterado_entra` — logo depois do `ref`, `coletar_arquivos_tocados(repo, desde=ref)` é `[]` (a regra antiga devolve `["versionado.log"]`); com o arquivo reescrito com `v3`, é `["versionado.log"]` e `coletar_diff_stat(repo, desde=ref)` contém `versionado.log` (a regra antiga devolve o resumo vazio). Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_review_evidence.py -q -k "versionado"` → `exit 0` — antes `exit 5`, depois `exit 0`
  2. `python -c "from pathlib import Path;t=Path('.claude/tools/review_evidence.py').read_text(encoding='utf-8');print('[%d-%d-%d]'%(t.count('def _gravar_arvore_de_trabalho'),t.count('_gravar_arvore_de_trabalho(root)'),t.count(chr(34)+'read-tree'+chr(34))))"` → `[1-2-1]` — antes `[0-0-0]`, depois `[1-2-1]`
- **Pronto quando:**
  - dossiê de evidência.arquivo versionado e ignorado — o recorte parte de tudo o que já está versionado, e esse arquivo entra como qualquer outro — Verificações 1 e 2
- **Fora do escopo desta tarefa:** o arquivo que não é texto (`AUF-T6`).
- **Handover:** 2026-09-28 · para `AUF-T6`
  - **Entregue:** _gravar_arvore_de_trabalho em .claude/tools/review_evidence.py (read-tree HEAD antes do add -A no índice temporário), chamada por capturar_ref e coletar_diff_stat; auxiliar _repo_com_versionado_ignorado e 2 TF no fim de tests/test_review_evidence.py
  - **Contrato:** o <ref> e o resumo de diferenças partem de tudo o que está versionado; versionado que o .gitignore cobre entra como qualquer outro
  - **Não refazer:** a gravação da árvore em função única
  - **Pendente:** nenhum

### AUF-T6 — O arquivo novo que não é texto se julga pelo conteúdo bruto [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa faz o instrumento de evidência comparar pelo conteúdo bruto o arquivo novo que não é texto, em vez de dá-lo sempre por tocado.
- **Fundamento:** `DAU-19`; `H-20` (§2.1); `F-13`.
- **Depende de:** `AUF-T5`
- **Operação do modelo:** `OP-6`
  - OP-6: Quem executa faz o instrumento de evidência comparar pelo conteúdo bruto o arquivo novo que não é texto, em vez de dá-lo sempre por tocado.
  - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; roda `git` por `subprocess` sem escrever no índice real, na lista de stash nem na árvore de trabalho.
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
- **Contratos/classes:** `_nao_rastreado_mudou_desde_ref(root: Path, ref: str, caminho: str) -> bool` — assinatura inalterada. Quando `_texto_do_disco(root, caminho)` devolve `None`: lê os bytes de `root / caminho`; `FileNotFoundError` devolve `True`, como hoje; senão devolve se os bytes diferem do conteúdo bruto de `<ref>:<caminho>`, obtido por `git show <ref>:<caminho>` rodado com `subprocess.run(..., cwd=str(root), capture_output=True)` sem decodificar a saída, numa função nova `_bytes_do_ref(root: Path, ref: str, caminho: str) -> bytes`. O julgamento do arquivo que se lê como texto não muda.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_review_evidence.py` os dois testes da seção `Testes`.
  2. Rodar `python -m pytest tests/test_review_evidence.py -q -k "binario"` e conferir que o TF falha.
  3. Criar `_bytes_do_ref` e mudar o ramo `None` de `_nao_rastreado_mudou_desde_ref`, pela regra de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `505 passed`, 2026-09-28, HEAD `2513964`).
  - `python .claude/checks/dead_code.py` sai 0 e `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`; os testes criam o próprio repositório em `tmp_path` com `_init_repo_com_baseline`.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar a linha `(arquivo binário ou não-UTF-8 — trecho omitido)` de `_diff_para_arquivo` (o trecho do alvo não é a propriedade desta operação); não mudar `_texto_do_disco`.
- **Contingências:**
  - se um teste que já existia em `tests/test_review_evidence.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_nao_rastreado_binario_intocado_fica_fora_dos_tocados` — `imagem.bin` gravado com os bytes `FF FE 00 81` antes do `ref = capturar_ref(repo)` e não tocado depois: `coletar_arquivos_tocados(repo, desde=ref)` é `[]` (a regra antiga devolve `["imagem.bin"]`). TR `test_tr_nao_rastreado_binario_alterado_entra_nos_tocados` — o mesmo arquivo regravado com `FF FE 00 82` depois do `ref`: a lista é `["imagem.bin"]`. Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_review_evidence.py -q -k "binario"` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - dossiê de evidência.arquivo novo que não é texto — ele entra só quando o conteúdo mudou desde o recorte — Verificação 1
- **Fora do escopo desta tarefa:** o painel do gerente (`AUF-T7`).
- **Handover:** 2026-09-28 · para `AUF-T15`
  - **Entregue:** _bytes_do_ref em .claude/tools/review_evidence.py (git show <ref>:<caminho> sem decodificar) e o ramo None de _nao_rastreado_mudou_desde_ref compara bytes; TF/TR de binário no fim de tests/test_review_evidence.py
  - **Contrato:** não rastreado que não é texto entra nos tocados só quando os bytes mudaram desde o <ref>
  - **Não refazer:** a comparação por bytes
  - **Pendente:** nenhum

### AUF-T7 — O painel mostra o título do tíquete em curso [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa faz o painel do gerente mostrar o título do tíquete em curso, e não só o identificador dele.
- **Fundamento:** `DAU-15`, `DAU-26`; `H-14` (§2.1); `F-13`, `F-16`.
- **Operação do modelo:** `OP-7`
  - OP-7: Quem executa faz o painel do gerente mostrar o título do tíquete em curso, e não só o identificador dele.
  - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.
- **Camada e fronteira:** gancho do kit em `.claude/tools/progresso_hook.py` (roda em `PreToolUse`, `PostToolUse` e `Stop`); falha aberta, sem bloquear a chamada; não importa de `tests/`.
- **Arquivos-alvo:**
  - `.claude/tools/progresso_hook.py`
  - `tests/test_progresso_hook.py`
- **Contratos/classes:** `localizar_card(id_tarefa: str, raiz: Path) -> tuple[str, str, str]` — assinatura inalterada. Padrão novo, ao lado do de card (`^### <id> — (.+?) \[`): o de tíquete, `^## <id> — (.+?)\s*$`, com o id escapado por `re.escape`. Na varredura linha a linha, a linha que casa o padrão de tíquete devolve na hora `(título, "", "")` — título com `strip()`, objetivo vazio e título de plano vazio, porque o tíquete não mora dentro de um plano. O card (`### <id> — … [`), inclusive o card de tíquete, segue como hoje, e o fallback `(id_tarefa, "", "")` também.
- **Passos:**
  1. Acrescentar ao fim de `tests/test_progresso_hook.py` os dois testes da seção `Testes`, no molde de `test_tf_san_18_titulo_do_plano_em_pasta` (`tmp_path` como raiz, diário em `docs/DIARIO_DE_OBRAS.md`).
  2. Rodar `python -m pytest tests/test_progresso_hook.py -q -k "tiquete"` e conferir que o TF falha.
  3. Acrescentar o padrão de tíquete a `localizar_card`, pela regra de `Contratos/classes`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `505 passed`, 2026-09-28, HEAD `2513964`).
  - `python .claude/checks/dead_code.py` sai 0 e `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - O gancho segue em falha aberta: exceção dentro dele nunca bloqueia a chamada.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `FRASES` nem as frases do painel; não mudar `.claude/skills/scrum-master/SKILL.md`, `.claude/settings.json` nem `.claude/projecoes.json`.
- **Contingências:**
  - se um teste que já existia em `tests/test_progresso_hook.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_titulo_do_tiquete_em_curso` — diário com as linhas `# Diário`, vazia, `## TK-9 — Um tíquete de teste`, vazia e `Corpo do tíquete.`: `localizar_card("TK-9", tmp_path)` devolve `("Um tíquete de teste", "", "")` (a regra antiga devolve `("TK-9", "", "")`). TR `test_tr_card_de_tiquete_segue_com_o_titulo_do_card` — diário com `## TK-9 — Um tíquete de teste`, vazia, `### TK-9a — O card do tíquete [Sonnet · classe implementacao]` e `- **Objetivo:** fixture.`: `localizar_card("TK-9a", tmp_path)` devolve `("O card do tíquete", "fixture.", "Um tíquete de teste")`. Suíte `tests/test_progresso_hook.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_progresso_hook.py -q -k "tiquete"` → `exit 0` — antes `exit 5`, depois `exit 0`
- **Pronto quando:**
  - painel do gerente.título do tíquete — o painel mostra o título do tíquete, como já faz com o card — Verificação 1
- **Fora do escopo desta tarefa:** a frase final do fechamento (`AUF-T8`).
- **Handover:** 2026-09-28 · para `AUF-T15`
  - **Entregue:** localizar_card em .claude/tools/progresso_hook.py:143 casa também o cabeçalho de tíquete '## <id> — <título>' e devolve (título, '', ''); TF/TR no fim de tests/test_progresso_hook.py
  - **Contrato:** o painel mostra o título do tíquete em curso; card de tíquete e fallback inalterados
  - **Não refazer:** o padrão de tíquete em localizar_card
  - **Pendente:** nenhum

### AUF-T8 — A frase final do fechamento serve a todos os comandos [Sonnet · esforço low · classe implementacao]
- **Objetivo:** Quem executa troca a frase final do fechamento de tarefa por uma sem erro de concordância com o nome de nenhum comando.
- **Fundamento:** `DAU-16`, `DAU-27`; `H-15` (§2.1); `F-13`, `F-15`.
- **Operação do modelo:** `OP-8`
  - OP-8: Quem executa troca a frase final do fechamento de tarefa por uma sem erro de concordância com o nome de nenhum comando.
  - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/encerrar.py`; só a linha final de sucesso de `main` muda.
- **Arquivos-alvo:**
  - `.claude/tools/encerrar.py`
  - `tests/test_encerrar.py`
- **Contratos/classes:** a linha de sucesso de `main` em `.claude/tools/encerrar.py`, hoje `print(f"encerrar: OK - {args.comando} fechado; relatório em '{destino}'.")`, passa a ser, exata (as quebras são as do bloco: uma linha só; ela perde o recuo da cerca do bloco, e os quatro espaços que sobram entram no arquivo):

  ```python
      print(f"encerrar: OK - comando '{args.comando}' concluído; relatório em '{destino}'.")
  ```
- **Passos:**
  1. Em `tests/test_encerrar.py`, no teste `test_tf_fechado_conta_como_o_indice`, trocar a asserção `assert "plano fechado" in capsys.readouterr().out` por `assert "encerrar: OK - comando 'plano' concluído;" in capsys.readouterr().out`, e, na docstring do mesmo teste, o trecho `` diz `plano fechado` `` por `` diz `comando 'plano' concluído` ``.
  2. Acrescentar ao fim de `tests/test_encerrar.py` o TF da seção `Testes`, no molde de `test_tf_tarefa_fecha_num_ato_status_rdo_tres_secoes_e_achado` (`_montar_repo`, `_argv_tarefa`).
  3. Trocar a linha de `Contratos/classes` em `.claude/tools/encerrar.py`.
  4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma o 1 teste novo (referência datada: `505 passed`, 2026-09-28, HEAD `2513964`).
  - `python .claude/checks/dead_code.py` sai 0 e `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar as outras linhas `encerrar: OK - …` de `main` (handover, operações), a mensagem `marco:` nem o texto humano dos relatórios (`Plano "…" fechado em …`).
- **Contingências:**
  - se `tests/test_encerrar.py` tiver, além da asserção do passo 1, outra asserção sobre o texto `fechado; relatório` ou `<comando> fechado` → seguir trocando-a pelo texto novo, no mesmo molde do passo 1, e devolver `contingência 1 acionada: <nome do teste>`.
  - se um teste que já existia em `tests/test_encerrar.py` cair depois do passo 3 → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_conclusao_da_tarefa_sem_erro_de_concordancia` — `encerrar.main(_argv_tarefa(repo, **{"--resumo": "A primeira coisa está entregue.", "--pendencia": "nomear a função"}))` sai 0, e o stdout contém `encerrar: OK - comando 'tarefa' concluído;` e não contém `tarefa fechado` (a regra antiga imprime `encerrar: OK - tarefa fechado;`). Suíte `tests/test_encerrar.py` e a suíte inteira.
- **Verificação:**
  1. `python -m pytest tests/test_encerrar.py -q -k "conclusao_da_tarefa"` → `exit 0` — antes `exit 5`, depois `exit 0`
  2. `python -c "from pathlib import Path;t=Path('.claude/tools/encerrar.py').read_text(encoding='utf-8');print('[%d-%d]'%(t.count('concluído; relatório em'),t.count('fechado; relatório em')))"` → `[1-0]` — antes `[0-1]`, depois `[1-0]`
- **Pronto quando:**
  - fechamento de tarefa.mensagem de conclusão — a frase final diz que o comando foi concluído, correta para todos os comandos — Verificações 1 e 2
- **Fora do escopo desta tarefa:** o guia de entrada (`AUF-T15`), que não cita a frase.
- **Handover:** 2026-09-28 · para `AUF-T15`
  - **Entregue:** linha de sucesso de main em .claude/tools/encerrar.py:1293 passa a "encerrar: OK - comando '<comando>' concluído; relatório em '<destino>'."; asserção de test_tf_fechado_conta_como_o_indice atualizada e TF test_tf_conclusao_da_tarefa_sem_erro_de_concordancia no fim de tests/test_encerrar.py
  - **Contrato:** a frase final do fechamento serve a todos os comandos
  - **Não refazer:** a frase final de main
  - **Pendente:** nenhum

### AUF-T9 — O planejador ensaia a contingência e a faz caber no card [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa ensina o planejador a tratar cada contingência do card como parte ensaiada dele, sem contrariar as restrições do card e com os arquivos que ela escreve declarados.
- **Fundamento:** `DAU-8` (i) e (ii), `DAU-31`; `H-1`, `H-8` (§2.1); `F-12`.
- **Operação do modelo:** `OP-9`
  - OP-9: Quem executa ensina o planejador a tratar cada contingência do card como parte ensaiada dele, sem contrariar as restrições do card e com os arquivos que ela escreve declarados.
  - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.
- **Camada e fronteira:** doutrina do kit — definição do agente planejador; nenhum código muda.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-planner.md`
- **Passos:**
  1. Na Fase 4, item 3 (o que começa por `3. **Léxico proibido no card**`), logo depois da linha que termina em `` (plano legado: na linha `**Status:**` do card) (2026-09-16, `RP-4`). `` e antes da linha que começa por `4. **Rastreabilidade**`, inserir o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo da cerca do bloco, e os três espaços que sobram entram no arquivo):

     ```text
        **A contingência não contradiz o card:** a ação `seguir com <X>` de uma contingência não
        contraria nenhuma `Restrição` do mesmo card, e todo arquivo que ela escreve entra nos
        `Arquivos-alvo`, no próprio bullet, seguido de `(condicional: contingência <n>)`, com `<n>` a
        posição do bullet em `Contingências` (2026-09-27, `AE-24` do `P-0753`).
     ```
  2. Na Fase 4, item 14 (o que começa por `14. **Ensaio dos cards em árvore temporária**`), logo depois da linha `   volta à autoria.` e antes da linha `### Fase 5 — Registro e parada`, inserir o bloco abaixo, mantendo a linha vazia que já separa o item 14 do cabeçalho da Fase 5 (as quebras são as do bloco; cada linha perde o recuo da cerca do bloco, e os três espaços que sobram entram no arquivo):

     ```text
        **A contingência se ensaia:** cada contingência de ação `seguir com <X>` se aplica na cópia
        como passo do card, e as linhas de `Verificação` se re-rodam depois dela; linha cujo valor ela
        muda publica, na própria contingência, o valor medido com ela aplicada (2026-09-27, pendência 1
        do `P-0753`).
     ```
  3. Rodar a Verificação.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `505 passed`, 2026-09-28).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não reescrever outra frase dos itens 3 e 14; não mexer na tabela de dosagem da Fase 4 (`| 14 (ensaio em cópia) |`); não editar a Anatomia do card nem o `docs/RUBRICA_DE_REVISAO.md` (é da `AUF-T10`).
- **Contingências:**
  - se a linha âncora de um dos passos não existir verbatim em `.claude/agents/pantonic-planner.md` → parar e sinalizar `blocked` razão `premissa`, nomeando o passo.
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê `.claude/agents/pantonic-planner.md`.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('[%d-%d]'%(t.count('A contingência não contradiz o card'),t.count('A contingência se ensaia')))"` → `[1-1]` — antes `[0-0]`, depois `[1-1]`
- **Pronto quando:**
  - planejador.contingência do card — cada contingência é ensaiada como o resto do card, não contraria nenhuma restrição dele, e o arquivo que ela escreve aparece entre os alvos, marcado como condicional — Verificação 1
- **Fora do escopo desta tarefa:** o critério da rubrica (`AUF-T10`); mecanizar a regra no `card_check.py` (candidata a recomendação do relatório novo, `DAU-8`).
- **Handover:** 2026-09-28 · para `AUF-T10`, `AUF-T11`
  - **Entregue:** duas regras novas em .claude/agents/pantonic-planner.md: 'A contingência não contradiz o card' (Fase 4 item 3, :271) e 'A contingência se ensaia' (Fase 4 item 14, :443)
  - **Contrato:** a contingência não contraria Restrição do card, o arquivo que ela escreve entra nos Arquivos-alvo com '(condicional: contingência <n>)', e ela se ensaia na cópia como passo do card
  - **Não refazer:** as duas regras de contingência do planejador
  - **Pendente:** nenhum

### AUF-T10 — A rubrica cobra a contingência pela regra do planejador [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa acrescenta à rubrica de revisão o critério que cobra da contingência do card a regra que o planejador passou a seguir.
- **Fundamento:** `DAU-8` (iii), `DAU-31`; `H-1`, `H-8` (§2.1); `F-12`.
- **Depende de:** `AUF-T9`
- **Operação do modelo:** `OP-10`
  - OP-10: Quem executa acrescenta à rubrica de revisão o critério que cobra da contingência do card a regra que o planejador passou a seguir.
  - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.; planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta só a regra que a operação pede, deixando as demais como estão.
- **Camada e fronteira:** doutrina do kit — régua de revisão; nenhum código muda.
- **Arquivos-alvo:**
  - `docs/RUBRICA_DE_REVISAO.md`
- **Passos:**
  1. Na `## 8. Rubrica de criação de tarefa`, na tabela `| # | o card passa quando | caso medido |`, logo depois da linha que começa por `| (xviii) |` e antes da linha vazia que fecha a tabela, inserir a linha abaixo (as quebras são as do bloco: uma linha só, sem o recuo da cerca do bloco):

     ```text
     | (xix) | **a contingência é parte ensaiada do card, e não o contradiz.** A ação `seguir com <X>` de cada contingência foi aplicada no ensaio, quando o plano ensaia, e as linhas de `Verificação` re-rodadas depois dela; ela não contraria nenhuma `Restrição` do mesmo card; e todo arquivo que ela escreve está nos `Arquivos-alvo`, seguido de `(condicional: contingência <n>)` | pendência 1 e `AE-24` do `P-0753` |
     ```
  2. Rodar a Verificação.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `505 passed`, 2026-09-28).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar as linhas `(i)`..`(xviii)`; não mudar a frase `dezoito critérios em vigor` da `### 8.1` — ela registra a medida de uma data e não conta a tabela.
- **Contingências:**
  - se a linha `| (xviii) |` não existir em `docs/RUBRICA_DE_REVISAO.md` ou já existir uma linha `| (xix) |` → parar e sinalizar `blocked` razão `premissa`, colando a linha encontrada.
- **Testes:** nenhum teste novo; a suíte inteira.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8');print('[%d-%d]'%(t.count('a contingência é parte ensaiada do card, e não o contradiz'),t.count('| (xix) |')))"` → `[1-1]` — antes `[0-0]`, depois `[1-1]`
- **Pronto quando:**
  - rubrica de revisão.critério de contingência — a rubrica cobra da contingência a mesma regra que o planejador segue ao escrevê-la — Verificação 1
- **Fora do escopo desta tarefa:** o texto do planejador (`AUF-T9`, já entregue).
- **Handover:** 2026-09-28 · para `AUF-T15`
  - **Entregue:** critério (xix) na tabela da ## 8 de docs/RUBRICA_DE_REVISAO.md:312 — a contingência é parte ensaiada do card e não o contradiz
  - **Contrato:** o revisor cobra da contingência a regra do planejador (AUF-T9)
  - **Não refazer:** o critério (xix)
  - **Pendente:** nenhum

### AUF-T11 — O teste de interrupção nomeia os três casos que passaram por ele [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa acrescenta ao teste de interrupção do planejador os três casos medidos em que o card deveria ter parado e não parou.
- **Fundamento:** `DAU-9`, `DAU-31`; `H-2`, `H-3`, `H-4` (§2.1).
- **Depende de:** `AUF-T9`
- **Operação do modelo:** `OP-11`
  - OP-11: Quem executa acrescenta ao teste de interrupção do planejador os três casos medidos em que o card deveria ter parado e não parou.
  - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.; planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta só a regra que a operação pede, deixando as demais como estão.
- **Camada e fronteira:** doutrina do kit — definição do agente planejador; nenhum código muda.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-planner.md`
- **Passos:**
  1. Na Fase 4, item 8 (o que começa por `8. **Teste de interrupção**`), logo depois da linha `   falha sua, não do executor.` e antes da linha que começa por `9. **Campo de card lido por máquina`, inserir o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo da cerca do bloco, e os três espaços que sobram entram no arquivo):

     ```text
        Três pontos de parada medidos que o enunciado geral deixou passar, e que se conferem pelo nome
        em todo card: (a) **Objetivo condicional contra contrato incondicional** — o `Objetivo` diz "se"
        enquanto `Contratos/classes` ou `Passos` mandam fazer sempre (`AE-8` do `P-0753`); (b) **caminho
        sem forma fixada** — argumento ou campo de caminho sem dizer se é relativo à raiz do repositório
        ou absoluto (`AE-13` do `P-0753`); (c) **argumento sem limpeza nem recusas fechadas** — argumento
        de texto sem a normalização aplicada antes do uso (`strip()`, separador) e sem a lista fechada
        das entradas que ele recusa, cada uma com a mensagem (`AE-18` do `P-0753`).
     ```
  2. Rodar a Verificação.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `505 passed`, 2026-09-28).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não reescrever o enunciado geral do item 8; não editar outro item da Fase 4.
- **Contingências:**
  - se a linha âncora do passo 1 não existir verbatim em `.claude/agents/pantonic-planner.md` → parar e sinalizar `blocked` razão `premissa`, colando as linhas do item 8.
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê `.claude/agents/pantonic-planner.md`.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('[%d-%d-%d]'%(t.count('Objetivo condicional contra contrato incondicional'),t.count('sem forma fixada'),t.count('argumento sem limpeza nem recusas fechadas')))"` → `[1-1-1]` — antes `[0-0-0]`, depois `[1-1-1]`
- **Pronto quando:**
  - planejador.pontos de parada do teste de interrupção — os três casos entram no teste pelo nome, como pontos em que o card tem de ser fechado antes de sair — Verificação 1
- **Fora do escopo desta tarefa:** reabrir os cards `AF-T7`, `AF-T10` e `AF-T12` do `P-0753` (já `done`).
- **Handover:** 2026-09-28 · para `AUF-T12`
  - **Entregue:** três pontos de parada nomeados no item 8 (Teste de interrupção) da Fase 4 de .claude/agents/pantonic-planner.md:341 — Objetivo condicional contra contrato incondicional; caminho sem forma fixada; argumento sem limpeza nem recusas fechadas
  - **Contrato:** o teste de interrupção confere os três casos pelo nome em todo card
  - **Não refazer:** o bloco dos três pontos de parada
  - **Pendente:** nenhum

### AUF-T12 — A versão pendente do modelo reconfere a restrição que cita o estado do plano [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa faz o planejador reconferir a restrição de card que cita o estado do plano sempre que o modelador grava uma versão pendente.
- **Fundamento:** `DAU-10`, `DAU-31`; `H-5` (§2.1).
- **Depende de:** `AUF-T11`
- **Operação do modelo:** `OP-12`
  - OP-12: Quem executa faz o planejador reconferir a restrição de card que cita o estado do plano sempre que o modelador grava uma versão pendente.
  - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.; planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta só a regra que a operação pede, deixando as demais como estão.
- **Camada e fronteira:** doutrina do kit — definição do agente planejador; nenhum código muda.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-planner.md`
- **Passos:**
  1. Na `## Rodada de replanejamento`, passo 4 (o que começa por `4. **Reescrever os cards**`), logo depois da linha que termina em `` dossiê `Ato de modelo` de `emenda`. `` e antes da linha que começa por `5. **Fechar o estado**`, inserir o bloco abaixo (as quebras são as do bloco; cada linha perde o recuo da cerca do bloco, e os três espaços que sobram entram no arquivo):

     ```text
        **Versão pendente reconfere a restrição que cita o estado do plano:** quando o modelador grava
        uma versão pendente do modelo, toda `Restrição` de card que afirma estado do plano — seção que
        existe ou não, versão vigente, operação presente — se reconfere contra o plano gravado, no mesmo
        ato, e a que ficou falsa se reescreve (2026-09-27, `AE-20` do `P-0753`).
     ```
  2. Rodar a Verificação.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `505 passed`, 2026-09-28).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não reescrever outra frase do passo 4 nem dos passos 1 a 3, 5 e 6 da rodada.
- **Contingências:**
  - se a linha âncora do passo 1 não existir verbatim em `.claude/agents/pantonic-planner.md` → parar e sinalizar `blocked` razão `premissa`, colando as linhas do passo 4 da rodada.
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê `.claude/agents/pantonic-planner.md`.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('[%d]'%t.count('Versão pendente reconfere a restrição que cita o estado do plano'))"` → `[1]` — antes `[0]`, depois `[1]`
- **Pronto quando:**
  - planejador.restrição que cita o estado do plano — quando o modelador grava uma versão pendente, o planejador reconfere toda restrição de card que cita o estado do plano — Verificação 1
- **Fora do escopo desta tarefa:** corrigir o parêntese da restrição da `AF-T14` do `P-0753` (card `done`).
- **Handover:** 2026-09-28 · para `AUF-T13`
  - **Entregue:** regra 'Versão pendente reconfere a restrição que cita o estado do plano' no passo 4 da Rodada de replanejamento de .claude/agents/pantonic-planner.md:539
  - **Contrato:** versão pendente do modelo dispara a reconferência das Restrições de card que afirmam estado do plano
  - **Não refazer:** a regra da versão pendente
  - **Pendente:** nenhum

### AUF-T13 — O planejador pergunta se o impedimento do papel é ajuste do kit [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa faz o planejador perguntar, diante de um papel que não consegue algo, se o impedimento é ajuste do kit ou limite da plataforma.
- **Fundamento:** `DAU-11`, `DAU-31`; `H-9` (§2.1); `F-11`.
- **Depende de:** `AUF-T12`
- **Operação do modelo:** `OP-13`
  - OP-13: Quem executa faz o planejador perguntar, diante de um papel que não consegue algo, se o impedimento é ajuste do kit ou limite da plataforma.
  - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.; planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta só a regra que a operação pede, deixando as demais como estão.
- **Camada e fronteira:** doutrina do kit — definição do agente planejador; nenhum código muda.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-planner.md`
- **Passos:**
  1. Na `### Fase 1 — Levantamento delegado (nunca próprio)`, logo depois da linha que termina em `` de memória (2026-09-18, `RP-2`). `` (fim do bullet que começa por `` - **Todo comando que vai aparecer numa linha de `Verificação` ``) e antes da linha vazia que precede `Orçamento: no máximo **duas** rodadas`, inserir o bullet abaixo (as quebras são as do bloco; cada linha perde o recuo da cerca do bloco, e os dois espaços que sobram nas linhas de continuação entram no arquivo):

     ```text
     - **Impedimento de papel é pergunta antes de ser dado**: diante de "o papel X não consegue Y", a
       campanha pergunta primeiro se o impedimento é **configuração do kit** — frontmatter `tools:` do
       agente, `.claude/settings*.json` — ou **limite da plataforma**. Configuração do kit se corrige
       como tarefa do plano; só o limite da plataforma se contorna, com a razão registrada na §2
       (2026-09-27, `RP-1` do `P-0753`).
     ```
  2. Rodar a Verificação.
- **Restrições desta tarefa:**
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `505 passed`, 2026-09-28).
  - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar a linha `Orçamento: no máximo **duas** rodadas de levantamento.` nem outro bullet da Fase 1; não editar o frontmatter do agente.
- **Contingências:**
  - se a linha âncora do passo 1 não existir verbatim em `.claude/agents/pantonic-planner.md` → parar e sinalizar `blocked` razão `premissa`, colando as linhas finais da Fase 1.
- **Testes:** nenhum teste novo; a suíte inteira, porque `tests/test_doutrina_unidade.py` lê `.claude/agents/pantonic-planner.md`.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print('[%d]'%t.count('Impedimento de papel é pergunta antes de ser dado'))"` → `[1]` — antes `[0]`, depois `[1]`
- **Pronto quando:**
  - planejador.pergunta sobre o impedimento do papel — antes de contornar, o planejador pergunta se o impedimento é ajuste do kit, que se corrige, ou limite da plataforma — Verificação 1
- **Fora do escopo desta tarefa:** mudar a configuração de qualquer papel (nenhuma operação a pede).
- **Handover:** 2026-09-28 · para `AUF-T15`
  - **Entregue:** bullet 'Impedimento de papel é pergunta antes de ser dado' na Fase 1 de .claude/agents/pantonic-planner.md:137
  - **Contrato:** diante de 'o papel X não consegue Y', a campanha pergunta primeiro se é configuração do kit (tools:, settings) ou limite da plataforma
  - **Não refazer:** o bullet do impedimento de papel
  - **Pendente:** nenhum

### AUF-T14 — Os quatro herdados sem mudança fecham com a prova [Sonnet · esforço low · classe mecanica]
- **Objetivo:** Quem executa registra o encerramento dos quatro herdados que não pedem mudança no kit, cada um com a prova já levantada.
- **Fundamento:** `DAU-7`, `DAU-28`; `H-6`, `H-7`, `H-11`, `H-17` (§2.1).
- **Operação do modelo:** `OP-14`
  - OP-14: Quem executa registra o encerramento dos quatro herdados que não pedem mudança no kit, cada um com a prova já levantada.
  - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.
- **Camada e fronteira:** registros de achado de planos fechados e do diário; nenhum código nem doutrina muda.
- **Arquivos-alvo:**
  - `docs/plans/P-0753-auditoria-estagio-1/plano.md`
  - `docs/plans/P-0752-fato-no-ponto-de-uso.md`
  - `docs/DIARIO_DE_OBRAS.md`
- **Passos:** cada passo acrescenta um sufixo ao **fim** de uma linha que já existe — a linha que começa pelo prefixo dado —, sem quebra nova e sem refluxo; cada linha de bloco perde o recuo da cerca, e o sufixo abre com um espaço.
  1. Em `docs/plans/P-0753-auditoria-estagio-1/plano.md`, na linha que começa por ``- **AE-21** (`AF-T14`, fechamento, 2026-09-27)``, acrescentar:

     ```text
      · **Desfecho (P-0754, AUF-T14, 2026-09-28):** encerrado sem mudança no kit — o teto de 4000 caracteres do trecho é conhecido do instrumento e sai marcado na evidência, como o laudo da `AF-T14` registrou.
     ```
  2. No mesmo arquivo, na linha que começa por ``- **AE-22** (`AF-T16`, fechamento, 2026-09-27)``, acrescentar:

     ```text
      · **Desfecho (P-0754, AUF-T14, 2026-09-28):** encerrado sem mudança no kit — a regra já existe: o ensaio dos cards em cópia, item 14 da Fase 4 de `.claude/agents/pantonic-planner.md`, e o critério (xii)(b) de `docs/RUBRICA_DE_REVISAO.md`.
     ```
  3. Em `docs/plans/P-0752-fato-no-ponto-de-uso.md`, na linha que começa por ``- **AE-51** (`FPU-T10`, fechamento, 2026-09-27)``, acrescentar:

     ```text
      · **Desfecho (P-0754, AUF-T14, 2026-09-28):** encerrado sem mudança no kit — a premissa caiu: `docs/ACIONAMENTOS_CONSULTOR.tsv` é versionado desde o commit `2513964`, e `review_evidence.py` o trata como registro da condução.
     ```
  4. Em `docs/DIARIO_DE_OBRAS.md`, na linha que começa por ``- **AE-89** (`TK-90b`, fechamento, 2026-09-27)``, acrescentar:

     ```text
      · **Desfecho (P-0754, AUF-T14, 2026-09-28):** encerrado sem mudança no kit — a premissa caiu: o card de tarefa é isento do teto do `backlog.py show`, e os oito cards do `P-0742` saem inteiros, sem marca de truncado.
     ```
  5. Rodar a Verificação e `python .claude/tools/backlog.py check`.
- **Restrições desta tarefa:**
  - `python .claude/tools/backlog.py check` sai 0 ao fim.
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `505 passed`, 2026-09-28).
  - Só os `Arquivos-alvo` se editam, e neles só as quatro linhas dos passos; nada fora deles se toca, se reverte ou se commita; nenhum commit.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar a `**Rota:**` já escrita nas quatro linhas; não mexer no cabeçalho gerado do diário (entre `<!-- fila:gerada -->` e `<!-- /fila:gerada -->`); não mudar o `AE-50` nem o `AE-51` do `P-0740`, que repetem os ids.
- **Contingências:**
  - se o prefixo de um passo não casar exatamente uma linha do arquivo → parar e sinalizar `blocked` razão `premissa`, nomeando o passo e colando as linhas que casam.
- **Testes:** nenhum teste novo; a suíte inteira.
- **Verificação:**
  1. `python -c "from pathlib import Path;c=[('docs/plans/P-0753-auditoria-estagio-1/plano.md','AE-21'),('docs/plans/P-0753-auditoria-estagio-1/plano.md','AE-22'),('docs/plans/P-0752-fato-no-ponto-de-uso.md','AE-51'),('docs/DIARIO_DE_OBRAS.md','AE-89')];print('[%s]'%'-'.join(str(sum(1 for l in Path(a).read_text(encoding='utf-8').splitlines() if l[4:9]==n and not l[9].isdigit() and 'Desfecho (P-0754, AUF-T14, 2026-09-28)' in l)) for a,n in c))"` → `[1-1-1-1]` — antes `[0-0-0-0]`, depois `[1-1-1-1]`
- **Pronto quando:**
  - herdados que não pedem mudança.desfecho — os quatro estão encerrados, cada um com a prova de que não pede mudança no kit — Verificação 1
- **Fora do escopo desta tarefa:** o desfecho dos herdados que outros cards fecham com mudança no kit — eles fecham pela entrega do próprio card, e a §2.1 deste plano é a residência que os liga.
- **Handover:** 2026-09-28 · para `AUF-T15`, `AUF-T16`
  - **Entregue:** sufixo 'Desfecho (P-0754, AUF-T14, 2026-09-28)' nas linhas AE-21 e AE-22 de docs/plans/P-0753-auditoria-estagio-1/plano.md, AE-51 de docs/plans/P-0752-fato-no-ponto-de-uso.md e AE-89 de docs/DIARIO_DE_OBRAS.md
  - **Contrato:** os quatro herdados sem mudança estão encerrados na origem, cada um com a prova
  - **Não refazer:** os quatro desfechos
  - **Pendente:** nenhum

### AUF-T15 — O guia de entrada descreve o kit com os herdados fechados [Sonnet · esforço low · classe redacao]
- **Objetivo:** Quem executa revisa o guia de entrada do kit para que ele descreva o kit como fica depois dos herdados fechados.
- **Fundamento:** `DAU-2` (revisão do `README.md` ao fim da etapa dos herdados, G-README dever 2), `DAU-29`; `F-17`; as mudanças descritas vêm das `AUF-T1`, `AUF-T3` a `AUF-T7` e `AUF-T9`.
- **Depende de:** `AUF-T1`, `AUF-T2`, `AUF-T3`, `AUF-T4`, `AUF-T5`, `AUF-T6`, `AUF-T7`, `AUF-T8`, `AUF-T9`, `AUF-T10`, `AUF-T11`, `AUF-T12`, `AUF-T13`, `AUF-T14`
- **Operação do modelo:** `OP-15`
  - OP-15: Quem executa revisa o guia de entrada do kit para que ele descreva o kit como fica depois dos herdados fechados.
  - precisa de: dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.; painel do gerente — Quem implementa faz o painel achar o título também quando o trabalho em curso é um tíquete, e não só um card de plano.; fechamento de tarefa — Quem implementa troca só a frase final por uma que sirva a todos os comandos, e acerta os testes que esperavam a antiga.; planejador — Quem implementa recebe o roteiro de fases do agente e acrescenta só a regra que a operação pede, deixando as demais como estão.; rubrica de revisão — Quem implementa acrescenta um critério que confere a contingência do card pela mesma regra que o planejador passa a seguir.
- **Camada e fronteira:** documentação pública do hub (`README.md`); `.claude/README.md` é derivado e não se edita à mão.
- **Arquivos-alvo:**
  - `README.md`
- **Passos:**
  1. Seção `## 6. O loop de execução`, na linha que contém `cada transição do loop, com o título da tarefa no lugar da sigla e sem nenhuma saída de`, trocar `com o título da tarefa no lugar da sigla` por `com o título da tarefa — do card de plano ou do tíquete do diário — no lugar da sigla`, sem quebra nova e sem refluxo.
  2. Seção `## 11. Anatomia do kit`, logo depois da linha `  nas mesmas três seções e uma linha no diário. Os cinco recusam sem escrever quando falta insumo.` (fim do bullet de `.claude/tools/encerrar.py`) e antes da linha que começa por ``- `.claude/tools/prevoo.py` ``, inserir o bullet abaixo (as quebras são as do bloco; cada linha perde o recuo da cerca do bloco, e os dois espaços que sobram nas linhas de continuação entram no arquivo):

     ```text
     - `.claude/tools/review_evidence.py` — a evidência que o revisor recebe de cada tarefa: a partir do
       ponto de partida gravado no despacho (`--capturar-ref`), mostra como diferença contra ele o que a
       entrega mudou — o arquivo criado depois dele, marcado como novo; o versionado que a lista de
       ignorados também cobre; o que não é texto, comparado pelo conteúdo bruto —, expande o alvo do card
       escrito com curinga e conta como registro da condução o que quem conduz escreve nos próprios
       registros, antes de procurar outra tarefa que o tenha declarado.
     ```
  3. Seção `## 8. Planos: o que é um plano fechado`, condição 4 (a linha que começa por `4. **Linear.**`), trocar a linha `   lê de cima a baixo e sabe o que fazer sem inferir.` pelas três linhas abaixo (as quebras são as do bloco; cada linha perde o recuo da cerca do bloco, e os três espaços que sobram entram no arquivo):

     ```text
        lê de cima a baixo e sabe o que fazer sem inferir. A contingência do card faz parte dele: tem a
        ação fechada, não contraria as restrições do próprio card e declara entre os alvos o arquivo que
        escreve.
     ```
  4. Rodar a Verificação e `pwsh -NoProfile -File .claude/checks/check-readme.ps1`.
- **Restrições desta tarefa:**
  - `pwsh -NoProfile -File .claude/checks/check-readme.ps1` sai 0 e `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0.
  - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho).
  - Só o `README.md` se edita; nada fora dele se toca, se reverte ou se commita; nenhum commit.
  - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não editar `.claude/README.md` (derivado); não reescrever seção fora das três dos passos; não descrever no guia as regras das `AUF-T11` a `AUF-T13` nem o critério da `AUF-T10`, que são doutrina interna do planejador e do revisor sem superfície no guia (`DAU-29`); não descrever a auditoria nova (`AUF-T16`), que ainda não rodou.
- **Contingências:**
  - se o texto âncora de um passo não existir verbatim no `README.md` → parar e sinalizar `blocked` razão `premissa`, nomeando o passo.
  - se `check-readme.ps1` sair diferente de 0 → parar e sinalizar `blocked` razão `premissa`, colando a saída.
- **Testes:** nenhum teste novo; `pwsh -NoProfile -File .claude/checks/check-readme.ps1` e a suíte inteira.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('README.md').read_text(encoding='utf-8');print('[%d-%d-%d]'%(t.count('do card de plano ou do tíquete do diário'),t.count('a evidência que o revisor recebe de cada tarefa'),t.count('A contingência do card faz parte dele')))"` → `[1-1-1]` — antes `[0-0-0]`, depois `[1-1-1]`
- **Pronto quando:**
  - guia de entrada do kit.aderência ao kit entregue — descreve o kit como ele fica depois dos herdados fechados — Verificação 1
- **Fora do escopo desta tarefa:** o veredito do dono sobre o `README.md` revisado — gate do Marco 2, não critério de pronto deste card.
- **Handover:** 2026-09-28 · para `AUF-T16`
  - **Entregue:** README.md revisado: §6 (:472, título do card ou do tíquete no painel), §8 condição 4 (a contingência faz parte do card), §11 bullet novo de review_evidence.py (:929); check-readme exit 0
  - **Contrato:** o guia descreve o kit depois dos herdados fechados; a auditoria nova ainda não está descrita
  - **Não refazer:** as três revisões do README
  - **Pendente:** veredito do dono sobre o README revisado (Marco 2)

### AUF-T16 — A auditoria nova do kit, medida num plano fictício de ponta a ponta [Opus + dono · esforço high · classe investigacao]
- **Objetivo:** Quem conduz a sessão, por instrução do dono, grava o relatório de auditoria nova, medido num plano fictício que ela executa de ponta a ponta sobre o kit já fechado.
- **Fundamento:** `DAU-1`, `DAU-3`, `DAU-4`, `DAU-5`, `DAU-6`, `DAU-20`, `DAU-21`, `DAU-30`; `H-16`, `H-21` (§2.1); `F-3`, `F-5`, `F-6`, `F-7`, `F-8`, `F-9`.
- **Depende de:** `AUF-T1`, `AUF-T2`, `AUF-T3`, `AUF-T4`, `AUF-T5`, `AUF-T6`, `AUF-T7`, `AUF-T8`, `AUF-T9`, `AUF-T10`, `AUF-T11`, `AUF-T12`, `AUF-T13`, `AUF-T14`, `AUF-T15`
- **Operação do modelo:** `OP-16`
  - OP-16: Quem conduz a sessão, por instrução do dono, grava o relatório de auditoria nova, medido num plano fictício que ela executa de ponta a ponta sobre o kit já fechado.
  - precisa de: instrução do dono no segundo marco — Ninguém altera: a auditoria espera por ela, e o loop não a abre sozinho.; guia de entrada do kit — Quem implementa revisa o guia contra o kit como ele fica depois dos herdados fechados.; herdados que não pedem mudança — Quem implementa registra o encerramento de cada um com a prova já levantada, sem mudar nada no kit.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.; relatório do primeiro estágio — Ninguém altera: é o molde do relatório novo, seção por seção.; gerente do loop — Ninguém altera: ele fica no loop, e é nele que se mede, durante o plano fictício, quanto das suas ações é mecânico e quanto custa.; levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.
- **Camada e fronteira:** executado pela **sessão principal** — quem conduz a sessão, no papel de auditor —, exceção à matriz de papéis válida só para este card (ato do dono de 2026-09-28, §0 ato 3: *"A auditoria é a última tarefa do plano, executada pela sessão principal, como no estágio 1. O loop para antes dela e só a abre quando você mandar. Isso abre uma exceção à matriz de papéis, válida só para essa tarefa. A tarefa passa pela revisão."*). Só a sessão principal despacha subagente; o plano fictício aciona planejador, modelador, executor, revisor e consultor pelo procedimento que o kit prescreve. O card passa pela revisão (`pantonic-reviewer`) como os demais; `review_evidence.py` trata `docs/audits/` como registro da condução, e a revisão mede o relatório pelo conteúdo no arquivo (`DAU-21`).
- **Arquivos-alvo:**
  - `docs/audits/AUDITORIA_FINAL_KIT.md` (novo)
  - `docs/plans/P-0754-auditoria-final/plano.md` (condicional: contingência 2)
- **Método de sondagem:**
  1. **Abertura.** Só com a instrução do dono no Marco 2: a sessão principal passa a linha `AUF-T16` de `estado.tsv` a `ready` e, no ato seguinte, a `in-progress`, por `python .claude/tools/backlog.py status AUF-T16 ready` e `python .claude/tools/backlog.py status AUF-T16 in-progress` (a tabela de transições recusa `blocked` → `in-progress` direto); o loop nunca a despacha.
  2. **Retrato inicial**, antes do primeiro ato da sonda: copiar para `%TEMP%\claude\auditoria\p0754_retrato\` a saída de `git status --porcelain=v1 --untracked-files=all` e os arquivos `docs/plans/_INBOX.md`, `docs/plans/_INBOX_HISTORICO.md`, `docs/DIARIO_DE_OBRAS.md`, `docs/telemetria.tsv`, `docs/ACIONAMENTOS_CONSULTOR.tsv` e `docs/RDO/INDEX.md`.
  3. **Corpus das cláusulas** (`DAU-4`, `F-6`): `.claude/tools/*.py`; `.claude/agents/pantonic-{planner,model-designer,executor,reviewer,scout,consultant}.md`; as skills `scrum-master`, `diario-de-obras`, `passagem-de-bastao`, `guardrails-check`, `entrega-de-encerramento`, `checar-versao-kit` e `modelo-por-fase`; `.claude/checks/`; `.claude/global/hooks/`; `GOVERNANCA.md`; e, como cláusulas novas, o que as `AUF-T1` a `AUF-T13` mudaram. Uma linha `K-<nn>` por mecanismo testável, com residência e teste; cláusula sem passagem no plano fictício marcada `sonda`. Uma das linhas é a cláusula cujo texto contém `rodada de replanejamento grava a medida` (`H-16`, `DAU-6`), com o diagnóstico de onde essa medida deve morar.
  4. **Plano fictício**: pasta `docs/plans/P-<n>-sonda-auditoria-final/`, com `<n>` o id que o `_INBOX.md` declara como próximo no retrato inicial; ele cobre as cláusulas da §2 do relatório e atravessa planejador → modelador → decomposição → loop do `scrum-master` → revisão → fechamento, com pelo menos uma rodada de replanejamento; cada passagem vira um registro da §3 do relatório.
  5. **Métricas por registro**: as dimensões do estágio 1 — `L` lacuna, `E` erro de execução, `C` pouca confiabilidade, `$` custo evitável, `Q` qualidade da entrega, `M` mecanização, `F` fluxo —, com avaliação `adequado`, `inadequado` ou `oportunidade`. Custo por papel sai do bloco `<usage>` da notificação de conclusão de cada subagente; papel sem medida entra como `nao_medido`, com a razão.
  6. **Ações mecânicas do gerente do loop** (`H-21`, `DAU-5`): durante o loop do plano fictício, medir cada passo `P1` a `P10` da skill `scrum-master` — se a ação é mecânica, que instrumento já a cobre e quanto custou (turnos e tokens da sessão principal naquele passo) — e emitir uma `R-<nn>` por ação mecanizável. Nenhum passo se remove, funde ou substitui.
  7. **Relatório** em `docs/audits/AUDITORIA_FINAL_KIT.md`, com a data de execução no cabeçalho e as seções abaixo, cada cabeçalho exato numa linha própria, nesta ordem, na coluna 0 do relatório (cada linha perde o recuo da cerca do bloco):

     ```text
     ## 0. O pedido, verbatim
     ## 1. Modelo conceitual da auditoria
     ## 2. Cláusulas do kit exercitadas
     ## 3. Registros — um por teste
     ## 4. Conclusão por dimensão
     ## 5. Recomendações — um tíquete por registro viável
     ## 6. Custo medido da execução do plano fictício
     ## 7. O que ficou na árvore e o que foi descartado
     ## 8. As ações mecânicas do gerente do loop
     ```

     A §2 é a tabela `| id | cláusula (mecanismo) | residência | teste |`; a §3, a tabela `| # | cláusula | teste | medido | dimensões | avaliação |`; a §4, a tabela `| dimensão | veredito | fundamento (registros da §3) |` com uma linha por dimensão — `Integração ponta a ponta`, `Lacunas (L)`, `Erros de execução (E)`, `Confiabilidade (C)`, `Custo evitável ($)`, `Qualidade da entrega (Q)`, `Mecanização (M)`, `Fluxo (F)` — e o veredito geral; a §5, uma `### R-<nn> — <título>` por recomendação e a frase exata `As recomendações deste relatório não se aplicam no P-0754.`; a §7 nomeia a pasta do plano fictício e o que foi descartado; a §8, a tabela `| passo | ação | mecânica | instrumento que a cobre | custo medido no plano fictício | recomendação |` com uma linha por passo, cada uma começando por `| P<n> |`. Teto do relatório: 450 linhas.
  8. **Limpeza**: copiar os artefatos do plano fictício para `%TEMP%\claude\auditoria\p0754_artefatos\`, restaurar do retrato inicial os arquivos do passo 2 e remover a pasta do plano fictício e tudo o que ela criou fora dela, sem commit; conferir que `git status --porcelain=v1 --untracked-files=all` é o do retrato inicial mais o relatório e os registros deste card.
- **Restrições desta tarefa:**
  - As recomendações do relatório não se aplicam neste plano (`DAU-1`); nenhum card corretivo nem tíquete nasce da auditoria (`DAU-20`).
  - O `scrum-master` fica no loop: nenhum passo de `.claude/skills/scrum-master/SKILL.md` se remove, funde ou substitui.
  - Nada do plano fictício é commitado; ao fim, `docs/plans/` não tem pasta `*-sonda-auditoria-final`.
  - Nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`; nenhum commit.
  - A árvore fora dos `Arquivos-alvo` volta ao retrato inicial.
- **Não fazer:** não despachar este card a subagente; não abrir o card sem a instrução do dono no Marco 2; não aplicar recomendação no kit durante a auditoria; não editar `README.md`, `.claude/` nem `GOVERNANCA.md` fora do que o plano fictício faz e a limpeza desfaz.
- **Contingências:**
  - se um papel não tiver medida de custo no `<usage>` nem em `docs/telemetria.tsv` → seguir com `nao_medido` e a razão na §6 do relatório, e uma `R-<nn>` para a lacuna.
  - se a auditoria encontrar defeito num herdado já fechado por este plano → seguir registrando-o na §3 do relatório e como `AE-<n>` em `## 9. Achados da execução` de `docs/plans/P-0754-auditoria-final/plano.md`, rota "plano sucessor"; nenhum card corretivo.
  - se, depois da limpeza, `git status --porcelain=v1 --untracked-files=all` diferir do retrato inicial em algo além do relatório e dos registros deste card → parar e sinalizar `blocked` razão `premissa`, colando a diferença.
- **Testes:** nenhum teste novo no kit; os testes do plano fictício saem com ele.
- **Verificação:**
  1. `python -c "from pathlib import Path;p=Path('docs/audits/AUDITORIA_FINAL_KIT.md');L=p.read_text(encoding='utf-8').splitlines() if p.exists() else None;H=['## 0. O pedido, verbatim','## 1. Modelo conceitual da auditoria','## 2. Cláusulas do kit exercitadas','## 3. Registros — um por teste','## 4. Conclusão por dimensão','## 5. Recomendações — um tíquete por registro viável','## 6. Custo medido da execução do plano fictício','## 7. O que ficou na árvore e o que foi descartado','## 8. As ações mecânicas do gerente do loop'];print('ausente' if L is None else '[%d]'%sum(1 for h in H if h in L))"` → `[9]` — antes `ausente`, depois `[9]`
  2. `python -c "from pathlib import Path;p=Path('docs/audits/AUDITORIA_FINAL_KIT.md');L=p.read_text(encoding='utf-8').splitlines() if p.exists() else None;D=['Integração ponta a ponta','Lacunas (L)','Erros de execução (E)','Confiabilidade (C)','Custo evitável','Qualidade da entrega (Q)','Mecanização (M)','Fluxo (F)'];print('ausente' if L is None else '[%d]'%sum(1 for d in D if any(l.startswith('| ') and d in l for l in L)))"` → `[8]` — antes `ausente`, depois `[8]`
  3. `python -c "from pathlib import Path;p=Path('docs/audits/AUDITORIA_FINAL_KIT.md');L=p.read_text(encoding='utf-8').splitlines() if p.exists() else None;print('ausente' if L is None else '[%d]'%sum(1 for n in range(1,11) if any(l.startswith('| P%d |'%n) for l in L)))"` → `[10]` — antes `ausente`, depois `[10]`
  4. `python -c "from pathlib import Path;p=Path('docs/audits/AUDITORIA_FINAL_KIT.md');L=p.read_text(encoding='utf-8').splitlines() if p.exists() else None;print('ausente' if L is None else '[%d]'%sum(1 for l in L if l.startswith('| K-') and 'rodada de replanejamento grava a medida' in l))"` → `[1]` — antes `ausente`, depois `[1]`
  5. `python -c "from pathlib import Path;p=Path('docs/audits/AUDITORIA_FINAL_KIT.md');t=p.read_text(encoding='utf-8') if p.exists() else None;print('ausente' if t is None else '[%d-%d]'%(t.count('As recomendações deste relatório não se aplicam no P-0754'),min(1,t.count('### R-'))))"` → `[1-1]` — antes `ausente`, depois `[1-1]`
  6. `python -c "from pathlib import Path;p=Path('docs/audits/AUDITORIA_FINAL_KIT.md');t=p.read_text(encoding='utf-8') if p.exists() else None;print('ausente' if t is None else '[%d]'%min(1,t.count('-sonda-auditoria-final')))"` → `[1]` — antes `ausente`, depois `[1]`
- **Pronto quando (o fato que tem de existir ao final):**
  - relatório de auditoria nova.cobertura do kit — cada regra do kit que se pode testar tem o seu teste no plano fictício, a medição registrada e a conclusão por dimensão, no formato do primeiro estágio; o plano fictício foi descartado e nada dele ficou — Verificações 1, 2 e 6
  - relatório de auditoria nova.avaliação das ações mecânicas do gerente — cada passo do loop diz se é mecânico, que instrumento já o cobre e quanto custou no plano fictício, com uma recomendação para cada ação que se possa mecanizar — Verificação 3
  - relatório de auditoria nova.medida no replanejamento — o relatório diz onde essa medida deve morar e recomenda o remédio — Verificação 4
  - relatório de auditoria nova.recomendações — uma recomendação por registro inadequado ou oportunidade de melhoria, a aplicar em plano seguinte que o dono abre depois de ler o relatório — Verificação 5
- **Fora do escopo desta tarefa:** aplicar as recomendações (plano sucessor que o dono abre depois de ler o relatório, `DAU-1`); o veredito do dono sobre o relatório — gate do Marco 3, não critério de pronto deste card.
- **Handover:** 2026-09-28 · para `dono`
  - **Entregue:** docs/audits/AUDITORIA_FINAL_KIT.md: 43 cláusulas, 54 registros, 31 recomendações, custo por papel, avaliação P1..P10 do gerente do loop; plano fictício P-0755 descartado, árvore igual ao retrato
  - **Contrato:** relatório para o dono ler no Marco 3; as recomendações vão a plano sucessor
  - **Não refazer:** nada a declarar
  - **Pendente:** veredito do dono sobre o relatório (Marco 3)


## 6. Ordem de execução

Grafo (cada seta é um `Depende de:` do card da direita):

- `AUF-T1` → `AUF-T2` → `AUF-T3` → `AUF-T4` → `AUF-T5` → `AUF-T6` — em série: todos editam `tests/test_review_evidence.py`, e todos salvo a `AUF-T2` editam `.claude/tools/review_evidence.py`.
- `AUF-T9` → `AUF-T10`; `AUF-T9` → `AUF-T11` → `AUF-T12` → `AUF-T13` — em série no `.claude/agents/pantonic-planner.md`; a `AUF-T10` lê a regra que a `AUF-T9` escreve.
- `AUF-T7`, `AUF-T8` e `AUF-T14` não dependem de nada e rodam em paralelo às séries acima (arquivos disjuntos).
- `AUF-T15` depende de `AUF-T1` a `AUF-T14` (fecha a etapa dos herdados, `DAU-2`).
- `AUF-T16` depende de `AUF-T1` a `AUF-T15` e nasce `blocked` (razão `dependencia`): só a sessão principal a abre, e só por instrução do dono no Marco 2 (`DAU-3`).

## 7. Fora de escopo (explícito)

- Aplicar as R-n do relatório novo — plano sucessor aberto pelo dono (DAU-1).
- Implementar a mecanização de ações do scrum-master — candidata a R-n do relatório novo (DAU-5).
- Mecanizar no `card_check.py` a checagem de contingência — candidata a R-n (DAU-8).
- A projeção da camada global em `~/.claude` (`materializar.py apply`) — ato do dono (`DIARIO_DE_OBRAS.md:4`).
- A propagação aos projetos derivados — plano próprio.
- Pendências 3, 4 e 5 do `P-0753` (`operacoes.md:535-537`) e AE-87, AE-90, AE-91 — rotas próprias (§2.1).
- Coluna de papel em `docs/telemetria.tsv` — se a auditoria a julgar necessária, vira R-n.

## 8. Riscos

| risco | resposta pré-decidida |
|---|---|
| O TF de `H-10`, `H-13` ou `H-18` passa em HEAD antes da mudança (correção parcial em `2513964` não descartada pelo levantamento) | o item fecha como absorvido pelo commit `2513964` (ou `TK-93a` para `H-10`), o TF fica como TR, e a entrega devolve `contingência <n> acionada: absorvido em HEAD` |
| Testes existentes afirmam o texto antigo de `encerrar.py:1293` (`H-15`) | medido (F-15): um teste, `test_tf_fechado_conta_como_o_indice`; a `AUF-T8` o lista nos Arquivos-alvo e o atualiza ao texto novo (`DAU-27`), com contingência para outro que apareça |
| `backlog.py next` selecionaria o card da auditoria | a linha nasce `blocked` razão `dependencia` (DAU-3); só quem conduz a sessão a desbloqueia, por instrução do dono |
| O custo da orquestração não tem medida na telemetria (F-8) | o relatório registra o custo como `nao_medido`, com a razão, e emite R-n; a seção do `AE-95` usa turnos e tokens medidos pela sessão principal durante o loop do plano fictício |
| A auditoria nova encontra defeito em herdado já fechado neste plano | `AE-<n>` na §9 e registro no relatório (DAU-20); nenhum card corretivo |
| `review_evidence.py` não mostra o relatório novo como diff por estar em `docs/audits/` (F-9) | a Verificação do card mede o relatório por conteúdo no arquivo (DAU-21) |

## 9. Achados da execução

(Vazio; apensado por quem executa ou orquestra.)
- **AE-96** (`AUF-T1`, fechamento, 2026-09-28) — achado de processo (dossiê): O contrato da AUF-T1 nao fechou o arquivo novo VAZIO depois do recorte: unified_diff([], []) nao gera linha e o trecho sai so uma quebra de linha (bloco vazio, sem cabecalho nem aviso), enquanto o stat mostra 'vazio.md 0' - exercido em repo temporario; nao e regressao (antes saia string vazia). **Rota:** item de replanejamento, registrar como AE-<n> na secao 9 do plano e fechar junto com a marca de arquivo novo da AUF-T3.
- **AE-97** (`AUF-T2`, revisão, 2026-09-28) — a entrega da `AUF-T2` apagou a última linha do TR `test_tr_arquivo_novo_sem_desde_segue_com_conteudo_integral` da `AUF-T1` (`assert "+linha-1" not in texto`), sem causa: a asserção segue verdadeira. **Desfecho:** reposta pelo consultor no ato (`DAU-32`); diff do arquivo contra o ref do despacho sem linha removida.
- **AE-98** (`AUF-T2`, revisão, 2026-09-28) — achado de processo (dossiê): a Verificação por `-k` e o piso de suíte por contagem não discriminam o enfraquecimento de teste vizinho no mesmo arquivo-alvo; a remoção do `AE-97` passou verde por construção. Remédio proposto pelo laudo: card que acrescenta a arquivo de teste existente verifica que o diff do arquivo-alvo contra o ref do despacho não tem linha removida (`git diff <ref> --numstat` com deleções = 0). **Rota:** auditoria final (`AUF-T16`), `DAU-20`.
- **AE-99** (`AUF-T2`, revisão, 2026-09-28) — achado de processo (dossiê): o caminho com escape octal que `coletar_arquivos_tocados` devolve segue a `montar_trechos` como `(sem diferença coletável - arquivo ausente na árvore de trabalho)`: não rastreado com acento de verdade chega ao revisor sem diff. Comportamento de hoje, fora do escopo da `AUF-T2` por decisão do card. **Rota:** auditoria final (`AUF-T16`), `DAU-20`.
- **AE-100** (`AUF-T2`, fechamento, 2026-09-28) — achado de processo (dossiê): A Verificacao do card (-k caminho_acentuado) e a restricao de suite por contagem (505/508 passed) nao discriminam o enfraquecimento de um teste vizinho no mesmo arquivo-alvo: a remocao de uma assercao da AUF-T1 passou verde por construcao. **Rota:** item de replanejamento na secao 9 do plano (AE-<n>) - card de acrescimo a arquivo de teste existente precisa de verificacao de que o diff do arquivo-alvo nao tem linha removida (ex.: git diff --numstat com delecoes = 0).
- **AE-101** (`AUF-T2`, fechamento, 2026-09-28) — achado de processo (dossiê): Exercicio ponta a ponta (3b): o caminho com escape octal que coletar_arquivos_tocados devolve segue para montar_trechos como '(sem diferenca coletavel - arquivo ausente na arvore de trabalho)', isto e, arquivo nao versionado com acento de verdade chega ao revisor sem diff. Comportamento de hoje, fora do escopo do card por decisao do plano; rota: AE-<n> na secao 9 do plano, como o proprio card preve. **Rota:** não declarada no laudo
- **AE-102** (`AUF-T2`, condução, 2026-09-28) — achado de processo (instrumento): `encerrar.py tarefa` registrou `AE-100` e `AE-101` como achados novos, mas eles repetem o `AE-98` e o `AE-99` que o consultor já tinha gravado sobre as mesmas duas linhas do laudo da `AUF-T2`; a dedupe do passo (5) do fechamento compara o texto literal, e o consultor tinha reescrito o texto. **Rota:** auditoria final — matéria da `AUF-T16` (diretiva do dono de 2026-09-26: nenhum card nem tíquete novo por ajuste); `AE-100` e `AE-101` ficam como duplicatas de `AE-98` e `AE-99`.
- **AE-103** (`AUF-T3`, fechamento, 2026-09-28) — O AE-96 (arquivo novo vazio saía como bloco em branco) fica fechado por esta entrega: a marca de arquivo novo abre o trecho, medido pelo revisor no laudo da AUF-T3. **Rota:** sem ação — fecha o AE-96
- **AE-104** (`AUF-T3`, fechamento, 2026-09-28) — achado de processo (dossiê): Regra 3 da AUF-T3 fixou fnmatch.fnmatchcase sem fechar se o * atravessa '/': exercido em repo temporario, relatorios/*.md casa tambem relatorios/sub/x.md (semantica fnmatch, nao de glob de shell); a entrega seguiu o contrato literal. **Rota:** item de replanejamento na secao 9 do plano (AE-<n>) - card futuro que declarar curinga em Arquivos-alvo fecha a semantica de diretorio ou aceita a do fnmatch por escrito.
- **AE-105** (`AUF-T5`, fechamento, 2026-09-28) — achado de processo (dossiê): Exercicio ponta a ponta (passo 3b) achou defeito anterior a esta entrega e fora de todo card do P-0754: 'review_evidence.py --atribuir' sem .claude/tools/rdo.py na raiz sai com traceback cru (exit 1), enquanto o caminho do dossie sai 'review_evidence: FALHOU - rdo.py: modulo nao encontrado' - contrato de erro divergente entre verbos do mesmo instrumento; rota: AE-<n> na secao 9 do plano, candidato a card de contrato de erro do instrumento **Rota:** não declarada no laudo
- **AE-106** (`AUF-T6`, fechamento, 2026-09-28) — achado de processo (dossiê): Caso simetrico fora do cerco do card: nao rastreado que era binario em <ref> (FF FE 00 81) e hoje se le como texto ('ola') derruba coletar_arquivos_tocados com AttributeError ('NoneType' object has no attribute 'splitlines'), porque _texto_do_ref decodifica como UTF-8 e devolve None; defeito anterior (o review_evidence.py de 55123364 falha igual) e o card fechou o ramo texto como 'nao muda', entao a entrega esta fiel. **Rota:** a conducao registra como AE-<n> na secao 9 do P-0754 e o leva como item de replanejamento (o ramo texto tambem compara pelo conteudo bruto quando o <ref> nao decodifica).
- **AE-107** (`AUF-T10`, fechamento, 2026-09-28) — achado de processo (dossiê): O literal (xix) fixado pelo card AUF-T10 cobre ensaio, re-execucao da Verificacao, nao-contradicao com Restricao e marca (condicional: contingencia <n>), mas omite a clausula do planejador (.claude/agents/pantonic-planner.md:444-445) 'linha cujo valor a contingencia muda publica, na propria contingencia, o valor medido com ela aplicada': card que ensaia sem publicar o valor passa no (xix). **Rota:** item de replanejamento do P-0754 (AE-<n> na §9) para emendar a linha (xix) da RUBRICA_DE_REVISAO.md §8.
- **AE-108** (`AUF-T12`, fechamento, 2026-09-28) — achado de processo (dossiê): AUF-T12 passo 1 nao definiu se o bloco entra colado a linha 'dossie Ato de modelo de emenda.' (continuacao do paragrafo, como os bolds dos passos 1 e 3 da rodada) ou como paragrafo proprio; a entrega escolheu inserir uma linha em branco antes do bloco (5a linha do numstat 5 0) sem declarar a escolha. Escolha de detalhe, reversivel, compativel com o precedente da linha 83 do mesmo arquivo. **Rota:** item de replanejamento do P-0754 (sec. 9, AE-<n>): card de insercao em lista numerada nomeia a linha separadora
- **AE-109** (`AUF-T14`, fechamento, 2026-09-28) — achado de processo (dossiê): A evidência marca docs/DIARIO_DE_OBRAS.md inteiro como da entrega, mas 2 das 3 linhas trocadas são o bloco <!-- fila:gerada --> que o backlog.py status (_regenerar_bloco_fila) regenerou ao materializar in-progress/review, registro da condução; reconciliado pelo contexto injetado no despacho, o escopo segue conforme e a entrega mudou só a linha AE-89. **Rota:** sem ação — a lacuna de atribuição por hunk já é a nota de 2026-09-19 na RUBRICA §3; registrado para o agregado.
- **AE-110** (`AUF-T14`, fechamento, 2026-09-28) — achado de processo (dossiê): O trecho do diff de P-0753/plano.md saiu truncado em 4000 caracteres antes das linhas + do AE-21/AE-22 (o mesmo teto que o AE-21 registra); a leitura exigiu git diff no repositório, que confirmou sufixo puro, igual ao texto do card, nas duas linhas. **Rota:** sem ação — teto conhecido do instrumento, que o próprio desfecho do AE-21 fecha sem mudança no kit; registrado para o agregado.
- **AE-111** (`AUF-T16`, revisão, 2026-09-28) — achado de processo (dossiê): as Verificações da `AUF-T16` contam cabeçalhos, linhas e a presença de `### R-`; nenhuma discrimina "uma recomendação por registro inadequado ou oportunidade" nem "cada regra testável tem teste", e os seis registros sem `R-<nn>` e o corpus sem linha `K` passaram verdes. Remédio do laudo: card de relatório com cobertura enumerada verifica por comando que cada registro diferente de `adequado` está citado numa `Origem:` e que cada item do corpus do método tem linha `K`. **Rota:** plano sucessor (`DAU-20`).
- **AE-112** (`AUF-T16`, revisão, 2026-09-28) — achado de processo (dossiê): a contingência 2 da `AUF-T16` manda registrar como `AE-<n>` cada defeito em herdado já fechado, mas a §3 do relatório não tem marca de "defeito em herdado fechado por este plano", e o conjunto de `AE` ficou a juízo de quem fecha (reparado pela `DAU-33` com `AE-114`..`AE-116`). Remédio: a contingência que escreve em residência do fechamento nomeia a coluna ou a marca que a dispara. **Rota:** plano sucessor.
- **AE-113** (`AUF-T16`, revisão, 2026-09-28) — achado de processo (dossiê): o loop fictício despachou o executor com o card por arquivo em vez de colado (`K-18`, reg. 22), variante do Passo 4 do `scrum-master` que o método não previa — decisão da entrega que o card não fechou (`G-NOASK`), declarada no relatório e base da `R-02`. Remédio: card de sondagem que admite variante de procedimento a nomeia. **Rota:** plano sucessor.
- **AE-114** (`AUF-T16`, contingência 2, 2026-09-28) — defeito em herdado fechado (`AUF-T3`, reg. 23 do relatório): o binário novo depois do `<ref>` sai só `(arquivo binário…)`, sem a marca de arquivo novo. Remédio: `R-14`. **Rota:** plano sucessor.
- **AE-115** (`AUF-T16`, contingência 2, 2026-09-28) — defeito em herdado fechado (`AUF-T4`, reg. 24): o resumo da evidência dá o registro da condução como tal, e a lista por arquivo rotula os mesmos arquivos `atribuição: alheio`. Remédio: `R-14`. **Rota:** plano sucessor.
- **AE-116** (`AUF-T16`, contingência 2, 2026-09-28) — defeito em herdado fechado (`AUF-T12`, reg. 36): a reconferência da versão pendente não cobre o campo `Operação do modelo` — `SA-T5` e `SA-T4` citaram `OP-4` com textos diferentes e `modelo.py check` aprovou. Remédio: `R-06`. **Rota:** plano sucessor.
- **AE-117** (`AUF-T16`, fechamento, 2026-09-28) — achado de processo (dossiê): A Verificacao 5 so conta a frase e min(1, '### R-'), e as 1, 2 e 6 contam cabecalhos e linhas: nenhuma discrimina 'uma recomendacao por registro inadequado ou oportunidade' nem 'cada regra testavel tem teste'; os 6 registros sem R e o corpus sem linha K passaram verdes. Remedio: card de relatorio com cobertura enumerada verifica por comando (cada registro da §3 com avaliacao diferente de adequado citado em alguma 'Origem:' da §5; cada item do corpus do metodo com linha K). **Rota:** AE-<n> na §9 do P-0754, plano sucessor (DAU-20).
- **AE-118** (`AUF-T16`, fechamento, 2026-09-28) — achado de processo (dossiê): A contingencia 2 manda registrar como AE-<n> na §9 do plano cada defeito em herdado ja fechado, mas o formato do relatorio (§3) nao tem marca de 'defeito em herdado fechado por este plano': plano.md segue sem alteracao desde o <ref> e o conjunto de AE fica a juizo de quem fecha (candidatos pela §3: reg. 23 e 24, AUF-T3/AUF-T4; reg. 36, AUF-T12; reg. 25 e 26 ja sao AE-105/AE-106). **Rota:** AE-<n> na §9 do P-0754, plano sucessor - a contingencia que escreve em residencia do fechamento nomeia a coluna ou a marca que a dispara.
- **AE-119** (`AUF-T16`, fechamento, 2026-09-28) — achado de processo (dossiê): Decisao tomada pela entrega que o card nao fechou (G-NOASK): o loop ficticio despachou o executor com o card por arquivo em vez de colado (K-18, reg. 22), variante do Passo 4 do scrum-master que o metodo nao previa; declarada no relatorio e base da R-02. **Rota:** AE-<n> na §9 do P-0754, plano sucessor (card de sondagem que admite variante de procedimento a nomeia).
