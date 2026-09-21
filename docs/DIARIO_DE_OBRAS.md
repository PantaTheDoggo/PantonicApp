# Diário de Obras — PantonicApp (hub de governança Pantonic*)

**Diretiva de priorização:** sem alvo fixo — a priorização volta a ser do agente (default), porque o alvo fixado foi entregue. O `P-0743` foi **aceito pelo dono em 2026-09-21**, fechou `done` 18/18, e a entrega validada está em `docs/Entregas Aceitas/Entregas - P-0743.md` — o as-is saiu de `docs/OPERACOES_AS_IS.md`, que volta a ficar livre para o próximo plano a produzir um. Fila viva: `TK-54`, `P-0741` (`MC-T5` em `review`), `TK-65`, `TK-66`, `TK-55`; `P-0744` segue `blocked`. Oito pendências do `P-0743` estão listadas na entrega aceita, três delas com efeito fora daquele plano.
<!-- fila:gerada -->
**Fila corrente:** `TK-54` — Extrato do custo de abertura de uma janela principal (`docs/DIARIO_DE_OBRAS.md:1286-1770`) · fila: — · ready 15 · blocked 0 · in-progress 0
- `TK-54` (`ready`, 1/2): próxima `TK-54b`
- `P-0741` (`ready`, 7/8): próxima —
- `TK-65` (`ready`, 0/3): próxima `TK-65a`
- `P-0744` (`blocked`, 0/3): próxima —
<!-- /fila:gerada -->

> **⏹ Os quatro blocos de diretiva abaixo são HISTÓRICO — o `P-0743` fechou `done` 18/18 e foi
> aceito pelo dono em 2026-09-21.** Não são instruções vivas, e nenhuma janela nova deve tentar
> executá-las: foi diretiva velha tratada como viva que travou o pickup de 2026-09-21. O verbatim
> das decisões vive no plano (`D-24` em diante) e a entrega validada, em
> `docs/Entregas Aceitas/Entregas - P-0743.md`.
>
> **Duas cláusulas sobrevivem ao plano e seguem vinculantes:**
> 1. **Relatório tem apêndice, e matéria tática mora nele** (`D-46`, item 10 da diretiva de
>    desenho) — vinculante para a orquestração em qualquer plano, não só neste.
> 2. **O critério de admissão de matéria nova é coesão, não custo** (ato do dono de 2026-09-19,
>    materializado como `DM-30` no `P-0740`).
>
> **Uma cláusula CADUCOU no fechamento:** a exceção que punha o `scrum-master` em Opus era
> *limitada a este plano* (item 1 da diretiva de execução). Com o `P-0743` fechado, a orquestração
> **volta a Sonnet** pela matriz de `GOVERNANCA.md` §3, salvo novo ato do dono.
>
> A condensação destes blocos para uma seção de histórico segue **pendente** — decisão do dono.

**Diretiva de desenho do `P-0743` (dono, 2026-09-20, sobre o as-is reescrito em 100 linhas):** o
terceiro estágio do modelo. Oito decisões, vinculantes até o dono as revogar. O verbatim integral e
as decisões formais (`D-24` em diante) vivem em `docs/plans/P-0743-modelo-de-dominio.md`; aqui fica
o ponteiro e a essência, para sobreviver a troca de contexto.

1. **`Mudanças` sai do modelo.** Mudança é **evento**, e evento não é estado. O estado do modelo é
   definido por **duas variáveis**: os objetos trabalhados e o fluxo de operações em que esses
   objetos participam.

2. **No lugar entra `Propriedades`.** Os objetos entram com propriedades iniciais; o fluxo de
   operações as altera; as propriedades finais são o estado **desejável** do modelo.

3. **O aceite do plano passa a ser modelável.** O plano só teve sucesso se o estado final for o
   especificado no modelo. A validação da mecânica é a **confrontação do estado final real contra o
   estado final conceitual**, e é essa diferença que tem valor para o cliente.

4. **Tarefa fora do modelo não é tarefa proibida.** Significa que não tem interesse para o
   usuário, o gerente de projeto ou o domain expert; deve ser realizada, e mantida de forma
   **transparente**. Contradiz a regra vigente de que toda tarefa cita operação (`V2` do
   `modelo.py`), e a forma de materializar a contradição é matéria do replanejamento.

5. **O teste do desenho é este plano.** O modelo dele seria `agente model designer` e `modelo`, com
   a operação *"construir o modelo"* devolvendo `modelo` no padrão esperado — testável e ajustável.
   Começa-se por este "modelo de um modelo"; outra forma, se a necessidade exigir, fica para depois.

6. **A construção do modelo vira mecânica**, com entrada de dados declarada: **objetos, operações,
   estado inicial e estado final**.

7. **Versionamento, e nada de rewrite.** Emenda ao modelo original **versiona**, não reescreve. O
   drift é apresentado no marco seguinte e avaliado ali; **validado**, aí cabe o merge das versões.
   *"Modelos são seres vivos que podem se alterar com base na evolução do projeto, mas um rewrite
   não é adequado."*

9. **O terceiro estágio fica no `P-0743`** (dono, 2026-09-20: *"Manter plano."*). A recomendação
   de abrir plano novo foi apresentada e recusada; o plano segue sendo um só.

10. **Relatório tem apêndice, e matéria tática mora nele** (dono, 2026-09-20: *"você pode migrar
    questões táticas para apendice do relatorio"*). Vinculante para a orquestração, a partir de já:
    o **corpo** de todo relatório e de todo marco carrega o que tem **lastro no modelo**; o que é
    tático **desce para apêndice** — não some e não sobe. A `V2` **não se toca**: nenhuma regra do
    instrumento afrouxa, e a distinção tática/estratégia é de **apresentação**, não de mecanismo.

**Diretiva de validação do `P-0743` (dono, 2026-09-21):** uma decisão, que substitui o gate do
Marco 3. Verbatim: *"Eu somente vou validar com base no AS-IS. Continuar para a conclusão do plano,
e depois eu valido."*

1. **O Marco 3 não recebe veredito na forma prevista.** A saída de `modelo.py show` foi apresentada
   ao dono em 2026-09-21 e ele **dispensou** o veredito sobre ela: não é por ali que ele valida.
   A régua da `D-43` — marco é detector de desvio — **não cai**; o que muda é **qual artefato** é o
   detector, e o dono nomeou o **as-is**.
2. **A `DOM-T6` está destravada.** Ela era a única tarefa aberta e estava retida por ser card do
   Marco 5. A janela de 2026-09-21 havia encerrado por `B3` exatamente por isso; o ato do dono
   remove a trava, e o plano segue até **18/18**.
3. **O artefato de validação é o `docs/OPERACOES_AS_IS.md`**, produzido pela skill
   `entrega-de-encerramento` depois da última tarefa e **antes** de pedir o veredito. Ele cobre o
   `P-0741` e o `P-0743` numa leitura só, e o documento hoje na árvore está na forma anterior
   (datado de 2026-09-20): descreve três blocos com `Mudanças`, quatorze regras onde hoje são
   vinte, e o gate do modelador antes da emenda da `D-53`. **Ele é reescrito, não apensado.**
4. **Os Marcos 4 e 5 seguem sem cards novos.** O ato do dono move a validação, não abre escopo.
   A matéria de replanejamento acumulada (`AE-20`, `AE-24`, `AE-25`) desce para a seção de
   pendências do as-is, que é onde o dono a lê no veredito.

**Ponto de partida do próximo contexto — é o VEREDITO DO MARCO 3, e ele é do dono.**
A janela de 2026-09-21 fechou por `B3`: a próxima tarefa da fila (`DOM-T6`) pertence ao **Marco 5**,
e a `D-43` a trava até o Marco 3 receber `go`. Não abrir janela de execução sobre o `P-0743` antes
da resposta.

- **O que o dono lê, e é a entrega do Marco 3:**
  `python .claude/tools/modelo.py show --plano docs/plans/P-0743-modelo-de-dominio.md`
  — sai `0`, abre por `estágio atual: OP-13`, traz 9 objetos com propriedades, 13 operações
  (12 `[concluída]`, 1 `[prevista]`) e a tabela de estado inicial × estado final das 21
  propriedades. `go` = os Marcos 4 e 5 ganham cards; `no-go` = o desenho falhou no meio do caminho,
  que é exatamente o serviço do marco.
- **Estado do plano:** `in-progress` **17/18**, `modelo.py check` sai `0`
  (`13 operações, 9 objetos, 21 propriedades, 18 tarefas, versão 1`), `backlog.py check` sai `0`.
  **Nada commitado** — a árvore carrega o plano inteiro.
- **Fechado na janela de 2026-09-21:** `DOM-T9c` (`aprovado 100%`, via rodada `RP-1`/`D-54`, que
  absorveu o `AE-23`) e `DOM-T10` (`aprovado 100%`, card de dois atos com o ato do
  `pantonic-model-designer` no meio — primeira autoria do modelador no acervo).
- **Matéria de replanejamento acumulada, sem ação:** `AE-20` (fixture das seis violações novas),
  `AE-24` (residência das provas de proveniência de card de dois atos) e `AE-25` (rótulo de
  telemetria por ato). Todas dependem do `go`.
- **Conduta vinculante:** relatório tem **apêndice**, e matéria tática mora nele (`D-46`).

8. **A resolução de conflito sai do modelador e volta ao consultor.** O modelador **guarda** a
   informação recebida e a **versiona**; quem tem o cenário decide a pertinência. Ato do dono:
   *"Não quero que o model designer seja mais um controle do processo. Sua função é ver o modelo, e
   não o projeto, por isso ele não tem o cenário completo para inferir se uma mudança é pertinente
   ou não."*

**Diretiva de execução do `P-0743` (dono, 2026-09-20, no gate de modelo da abertura da janela):** uma decisão, vinculante para esta janela.

1. **O `scrum-master` roda em Opus durante o `P-0743`.** Não é o modelo que a matriz de `GOVERNANCA.md` §3 atribui à Orquestração (Sonnet): é **exceção temporária, limitada a este plano**, concedida por ato do dono no Passo 1 do loop, depois de a janela ter parado no gate e nomeado a matriz. Precedente de forma: a exceção idêntica concedida ao `P-0739` (item 2 da diretiva daquele plano), que caducou com o fechamento dele em `18/18`. Ao fim do `P-0743` esta exceção caduca e a orquestração volta a Sonnet, salvo novo ato do dono. O modelo de cada tarefa continua sendo o do cabeçalho do card — as seis tarefas do `P-0743` são Sonnet e são despachadas assim; a exceção vale para o contexto principal que conduz, não para quem executa.

**Diretiva de execução do `P-0740` (dono, 2026-09-18, ao fim da janela que fechou a `LM-T1`):** quatro decisões, todas vinculantes para a próxima janela e para as seguintes, até o dono as revogar.

1. **Figura nova — o consultor de plano, instanciado ad-hoc.** A execução de um plano passa a instanciar **uma** vez o agente `pantonic-consultant` (`.claude/agents/pantonic-consultant.md`, criado neste ato), que **não é efêmero**: fica de standby com o cenário inteiro no contexto e é acionado **a cada escalonamento** para desbloquear impedimento vindo de executor e reparar o modelo funcional do plano. Motivo medido nesta janela: as quatro rodadas de replanejamento custaram **423,7k tk** contra 134,8k de execução real porque **cada uma nasceu fria** e redescobriu o mesmo cenário. O dono declarou que vai **detalhar esta figura e as fronteiras dela com o `pantonic-planner` em plano próprio**; até lá o agente é provisório, não é doutrina de `GOVERNANCA.md` §3 e não se cita como fonte normativa. Nesta transição o `scrum-master` aciona o consultor no lugar de abrir rodada fria de planejador.

2. **A janela vai até o marco validável, não até a primeira tarefa.** O loop deve rodar **todas as tarefas do plano que conseguir**, em sequência, e só entregar ao dono **no marco de validação pelo cliente**. Regra de parada por tarefa fechada (`B1` como está redigida) deixa de ser o critério de encerramento desta execução: pendência substantiva vira escalonamento **ao consultor**, e a janela segue. Encerram a janela: o marco validável, a poluição de contexto (`CLAUDE.md` global, Regra 2) ou impedimento que o consultor classifique como **estratégico**.

3. **Commit acontece no marco, não por tarefa.** Nada de commit a cada entrega. No marco de validação, o loop commita o conjunto. Consequência operacional: o recorte de evidência (`--desde <ref>`) continua sendo o último commit real, e o dossiê do reviewer seguirá misturando entregas — até a `LM-T3` fechar a atribuição, a injeção manual do contexto de árvore no despacho do reviewer é obrigatória.

4. **A ordem da fila é do `scrum-master`.** O dono abriu mão da ordem: *"o scrum-master pode executar os cards na melhor ordem, só me interessa a entrega validável"*. A fila da `DM-13` deixa de ser vinculante como sequência; as **dependências declaradas nos cards** continuam sendo. Fica autorizado, nominalmente, antecipar a `LM-T5` (auditoria de criação de card) se o loop julgar que ela evita repetir o defeito que custou 423,7k nesta janela.

5. **Impedimento `AE-7` — resolvido por decisão do dono, a executar na próxima tarefa.** O `pantonic-planner` **precisa de ferramenta de execução**: a `DM-12` ("comando de aceite não se deduz, se roda") é hoje inexequível pelo papel a que se dirige. A próxima tarefa do `P-0740` deve incluir a **adequação de toolset**, com o alinhamento explícito pedido pelo dono: *planner e executor acessando a mesma ferramenta de validação*. O `pantonic-reviewer` já tem `Bash`; o `pantonic-executor` tem toolset aberto; o `pantonic-planner` tem `Read, Glob, Grep, Write, Edit` e é o único sem execução. O `pantonic-consultant` já nasce com `Bash` por este motivo.

6. **Técnica ainda não projetada se executa *ad-hoc* — e o ad-hoc é insumo, não precedente.** Ato do dono, 2026-09-19: *"sempre que a tarefa demandar uma técnica ainda a ser projetada, faça ad-hoc. Execução ad-hoc vira insights para planejamento da técnica a ser materializada em sequência"*. O loop **não para** para desenhar a técnica que falta: faz, entrega, e registra a lição no acumulador do plano que vai materializá-la. O inverso é que está proibido — tratar o ad-hoc como doutrina por ter funcionado uma vez. Enquanto a técnica não for planejada e publicada, ela não é fonte normativa e não se cita como tal. Materializado como `DM-28` no `P-0740`, com residência em `## 9` do plano (`I-1`..`I-8`) e o card `LM-T9` (`docs/consultant-spec.md`) como penúltima tarefa (`DM-29`).

7. **O critério de admissão de matéria nova é coesão, não custo.** Ato do dono, 2026-09-19: *"já resolvemos a questão de custo. Com os limites expandidos, nossa preocupação agora é a coesão e coerência do contexto ao invés de uso"*. Consequências aplicadas no mesmo ato: a rodada de corte que a `TK-54a` habilitava **não se abre**; a `TK-54b` fica despriorizada; o `_CARD-mapa-de-custo-da-janela.md` foi eliminado por perda de objeto; e matéria de coerência que **cruze o tema** de um plano vivo continua fora dele (`DM-4`) — vai para a fila pós-plano, como `TK-38` e `TK-55`. Materializado como `DM-30` no `P-0740`.

8. **Consultor que atinge o limite faz handover; o loop descomissiona e provisiona outro.** Ato do dono, 2026-09-19, motivado pelo `ESC-22`: o `pantonic-consultant` caiu por *session limit* **sem devolver** as alocações abertas, e o contexto acumulado de 14 passagens morreu junto. **Ao perceber que se aproxima do próprio limite, o consultor promove handover** — estado do cenário, escalonamentos abertos, o que estava em curso — e o **`scrum-master` descomissiona a instância e provisiona outra**, repassando esse handover. A **forma de comunicação é ad-hoc** neste plano (`DM-28`) e entra na **spec do consultor** (`LM-T9`) para resolução no plano próprio; enquanto não for projetada, o ad-hoc **não é fonte normativa**. Materializado como `DM-45` (iii) no `P-0740`.

9. **O consultor coleta estatística do próprio acionamento.** Ato do dono, 2026-09-19. Responsabilidade nova: registrar, a cada acionamento, **o que o motivou, que classe de impedimento era e o que ficou inconclusivo**, produzindo o **panorama dos pontos inconclusivos** que serve de insumo à **spec de robustez**. Base medida: nesta janela foram **14 acionamentos** e **63%** do consumo total (`3.802,2k` de `6.004,3k`), sem nenhum registro estruturado de **causa** — `docs/telemetria.tsv` mede custo, não motivo. Sem o panorama, a spec de robustez seria autorada sobre impressão. Materializado como `DM-45` (iv) no `P-0740`, com residência na `LM-T9`.

**Diretiva de execução do `P-0739` (dono, 2026-09-19, sobre o relatório de encerramento do `P-0740`):** cinco decisões, vinculantes para a retomada e para as janelas seguintes, até o dono as revogar.

1. **Retomar o `P-0739`, e o `P-0740` é a medida do entregável.** O plano volta à fila; a régua do que é entrega boa aqui é o que o `P-0740` produziu — módulo coeso, card com `Verificação` que discrimina, achado com rota, e as cinco formas de aceite que a janela de 2026-09-19 mediu (presença; par presença-ausência; invariância; conferência contra a fonte; token com leitura de referente).

2. **O `scrum-master` roda em Opus durante o plano inteiro.** Não é o modelo da tabela de `GOVERNANCA.md` §3 para orquestração (Sonnet): é **exceção temporária, limitada a este plano**, porque o papel recebe responsabilidade nova — **avaliar carências e lacunas**. Ao fim do `P-0739` a exceção caduca e a orquestração volta a Sonnet, salvo novo ato do dono.

3. **O `scrum-master` preenche lacuna que identificar no plano, e registra a pendência.** Responsabilidade nova e temporária: onde o plano não cobre algo que a execução exige — exemplo dado pelo dono: **operacionalizar uma comunicação ainda não implementada** —, o loop **preenche** em vez de parar, e **registra a pendência** no acumulador. Isto **não** revoga a Regra 8 (o executor não decide, não pergunta e não muda rota) nem o `G-NOASK`: o que muda é que a **lacuna de plano** deixa de ser só motivo de escalonamento e passa a ser matéria que a orquestração pode fechar, sempre com registro.

4. **O consultor segue ad-hoc — a figura ainda não foi criada.** A `docs/consultant-spec.md` é insumo, não criação: enquanto o agente não for materializado por plano próprio, o `pantonic-consultant` permanece provisório, não é doutrina de `GOVERNANCA.md` §3 e não se cita como fonte normativa.

5. **O consultor coleta estatística para as DUAS specs.** São duas, e não se confundem: a **spec do consultor** (`docs/consultant-spec.md`, que existe) e a **spec de robustez** (que ainda não tem arquivo; o `TK-55` é o acumulador dela). A cada acionamento o consultor registra o que o motivou, que classe de impedimento era e o que ficou inconclusivo — alimentando a primeira; e todo caso de **derivado que erra sem sinal** alimenta a segunda. **Ato do dono neste ponto:** as imprecisões de contagem medidas na janela de 2026-09-19 (`AE-49`, `AE-51`, `AE-52`, `AE-57`, `AE-59`, `AE-61`, `AE-70`, `AE-71`, `AE-73`, `AE-75`) entram como **estatística na spec de robustez** — não como correção da spec do consultor.

> Este diário é o kanban do backlog de **governança comum** dos projetos Pantonic*. Os planos
> completos vivem em `docs/plans/P-*.md`; aqui ficam o índice, o status e o ponteiro. Entrada de
> planos novos: `docs/plans/_INBOX.md` (append-only), drenado por quem abrir a skill
> `proximo-passo`.

## Índice

| ID | Título | Status | Âncora |
|---|---|---|---|
| SPRINT-PANTONICV2 | Consolidação do framework em V2 — 7 estágios encadeados (5 `done`, 2 `superseded`; encerrada pelo aceite do dono ao `README.md` na `V2P-T10`) | done | `docs/DIARIO_HISTORICO.md#sprint-pantonicv2--consolidação-do-framework-em-v2` |
| P-0729-V2B | Estágio 1 — benchmarking de 21 frameworks públicos (T1..T9) | done | `docs/plans/P-0729-v2-benchmarking.md` |
| P-0729-V2C | Estágio 2 — confronto, diagnóstico e autoria do plano 3B (T1..T6) | done | `docs/plans/P-0729-v2-confronto.md` |
| P-0729-V2M | Estágio 3A — doutrina herdada do P-0722 (T1..T5 completos, 5/5) | done | `docs/plans/P-0729-v2-melhoria.md` |
| P-0729-V2K | Estágio 3B — mudanças adotadas do benchmarking (T1..T19, com `T12` partida em `T12a`/`T12b`; 20/20) | done | `docs/plans/P-0729-v2-melhoria-candidatos.md` |
| P-0729-V2D | Estágio 4 — README espelho, fechamento 2.0.0 e distribuição (T1..T4 entregues; `T5` reprovada, `T6` cancelada por absorção) | superseded | substituído por `docs/plans/P-0730-v2-identidade.md` |
| P-0730-V2I | Estágio 5 — identidade do framework: agnosticismo a stack/plataforma, CA+DDD, perfis e o README como contrato canônico (`T1..T11c` entregues; `T12` reprovou por identidade e derrubou a `DR-2`;… | superseded | docs/DIARIO_HISTORICO.md#p-0730-v2i--estágio-5 |
| P-0731-V2E | Estágio 6 — extração da camada de modalidade: o conceito de perfil sai do hub, desktop e container viram ramificações próprias, fechamento pelo **congelamento da versão em `0.0.0`** (`DE-7`,… | done | docs/DIARIO_HISTORICO.md#p-0731-v2e--estágio-6 |
| P-0732-V2P | Estágio 7 — as portas do core e a camada de casos de uso: contrato de porta para as 8 portas de runtime + superfície de entrada e execução assíncrona, residência do caso de uso… | done | docs/DIARIO_HISTORICO.md#p-0732-v2p--estágio-7 |
| P-0733-DHB | Quitação da dívida de doutrina e de kit do hub — os 12 tíquetes vivos do índice em 13 tarefas (`DHB-T1..T13`): doutrina decidida e não executada (`TK-15`, `TK-17`, `TK-21`, `TK-22`), resíduo de… | cancelled *(corte seco pelo `P-0737` em 2026-08-22, decisão do dono — a dívida que ele quitava não é caminho para o objetivo da `EXECUCAO-AUTONOMA`; tíquetes podados pelo critério de `docs/plans/P-0737-loop-autonomo.md` §5)* | docs/DIARIO_HISTORICO.md#p-0733--quitação-da-dívida-de-doutrina-e-de-kit-do-hub |
| P-0734-EXA | Execução autônoma — o backlog deixa de custar um round-trip humano por tarefa: papel de orquestração (skill `scrum-master`), papel de revisão (agente `pantonic-reviewer`) e documental gerado por… | superseded *(rebase de classificação (B) pelo `P-0737` em 2026-08-22 — as 52 entregues ficam como registro, as 8 abertas são absorvidas uma a uma e a `T16` é cancelada por absorção no plano recomendado do piloto; mapa em `docs/plans/P-0737-loop-autonomo.md` §4. Histórico: destravado em 2026-08-19 pelo fechamento do `P-0735`; retomado pela `T14`, que fechou no mesmo dia em **ramo B** — o `SubagentStop` expõe o consumo do subagente, mas não a identidade da tarefa, e o terceiro ramo — um contrato que a carregue até o hook — subiu ao dono como decisão; a `T15` fechou o enxugamento dos prompts com −1 linha líquida, medindo que o texto de formato coberto por instrumento já não vivia nos prompts declarados; a `T55` fechou a automação da série — o `scrum-master` grava a tarefa corrente e o hook de `SubagentStop` apende a linha sem gastar turno, com dedupe por `message.id` achado na calibração obrigatória; denominador 60 → 61 pela `DP-S`; 52/61)* | docs/DIARIO_HISTORICO.md#p-0734--execução-autônoma |
| P-0735-RPC | Residência e ponto de carga — o pacote materializa o que a doutrina invoca: a régua de residência deixa de responder *onde mora* com uma resposta só e separa **autoridade** de **ponto de carga** em… | done | docs/DIARIO_HISTORICO.md#p-0735--residência-e-ponto-de-carga |
| P-0736-CPK | Custo do pickup — mede por fonte o que uma retomada ingere, ranqueia e lista rotas candidatas; termina antes da decisão da rota (nível 2). 5 tarefas `CPK-T1..T5`, 3 executadas; `T4`/`T5`… | done | docs/DIARIO_HISTORICO.md#p-0736--custo-do-pickup |
| P-0737-AUT | Loop autônomo — o plano que consolida a `EXECUCAO-AUTONOMA`: 10 tarefas (`AUT-T1..T10`), decisões `DU-1..DU-13`, absorve as 8 tarefas abertas do `P-0734` e 11 tíquetes, poda 10 e encaminha 2;… | superseded *(sucedido pelo `P-0740-loop-de-modulos` em 2026-09-18, `DM-1` — a condição do bloqueio (`P-0738` fechar) foi satisfeita e a razão de fundo (custo fixo de contexto) caiu com a correção do denominador de janela para 1M; as 7 tarefas abertas foram absorvidas e reagrupadas em módulos)* | docs/DIARIO_DE_OBRAS.md#p-0737--loop-autônomo |
| P-0738-CTX | Contexto esgotado na partida — medir por que uma janela nasce cara e parar de repagar o custo fixo; Estágio C autorado pela charneira em 7 cards; `CTX-T10` mediu **regressão** (DX-5 subiu 34%, não caiu); 17/17 | done | `docs/plans/P-0738-contexto-esgotado.md` |
| P-0739-BKL | O pickup vira instrumento — `backlog.py` (`next`/`status`/`drain`/`check`), gramática legível por máquina e hook `UserPromptSubmit`; 16 tarefas (`BKL-T1`..`T9` + `T2a`..`T2e` + `T3a` + `T3b`). **11 fechadas:** `T1`, `T2`, `T2a`..`T2e`, `T3`, `T3a`, `T3b` e `T4` — a `BKL-T4` fechou `done` em 2026-09-18 com ressalva 85%, bloqueante `nenhuma`, ressalva roteada como `AE-10`. Rodadas `RP-1`..`RP-7` fechadas. **DESESTACIONADO em 2026-09-19**: a condição do dono (*não volta à fila enquanto o `P-0740` não encerrar*) foi **satisfeita** — o `P-0740` fechou em `35/35`, marco 3 commitado em `13ce6a3` —, e o plano é a **próxima janela**, sob a *Diretiva de execução do `P-0739`* (dono, 2026-09-19). O `DM-9` caduca com o encerramento do `P-0740`. **Primeiro ato da retomada: transcrever `BKL-T10`..`BKL-T12`**, cuja partição e mapa de herança já estão decididos pela `LM-T5a` do `P-0740` (`AE-63`, `AE-65`, `AE-67`) — o executor transcreve, não re-decide. As 5 tarefas restantes (`T5`..`T9`) **não** voltam uma a uma — a `LM-T5` as reagrupa em módulos coesos e o plano fecha em rodada única na `LM-T6`. O `AE-10` não abre rodada própria (absorvido pela `LM-T5`); o `AE-9` foi resolvido pelo dono em 2026-09-18 (seguir sem `RP-8`). | done 18/18 | docs/plans/P-0739-backlog-instrumento.md |
| P-0740-LM | O loop de módulos — a convergência da `EXECUCAO-AUTONOMA` sob a janela real de 1M: sucede o `P-0737` (`DM-1`), troca a tarefa atômica pelo **módulo coeso** (`DM-2`..`DM-5`) e corrige os seis defeitos medidos no run de aferição do `scrum-master` sobre a `BKL-T4`. **35 tarefas, 35 fechadas** (a `LM-T2e` nasceu no `ESC-9` desta janela; `LM-T4b`, `LM-T2f` e `LM-T3b` no `ESC-12`), decisões `DM-1`..`DM-50`. Marco 1 **commitado em `6eebccd`** (2026-09-19, oito entregas + `BKL-T4`, suíte 165 verde); recorte de evidência passa a `--desde 6eebccd`. Rodadas `RP-1`..`RP-5` e escalonamentos `ESC-1`..`ESC-26` fechados — os oito últimos pelo `pantonic-consultant`, figura ad-hoc instanciada uma vez e acionada em 9 passagens sem reler o plano. Atos do dono de 2026-09-19 (`DM-27`..`DM-30`): permissão de `.claude/agents/` concedida (`LM-T8` sai de `blocked`), técnica não projetada se executa ad-hoc com a lição registrada em `## 9` (`I-1`..`I-8`), card novo `LM-T9` (`consultant-spec`) como penúltima, e o critério de admissão de matéria nova passa a ser **coesão, não custo**. Fila: `LM-T6` (medida publicada, aguarda veredito do dono) → `LM-T9`, com `LM-T4c`, `LM-T5d`, `LM-T5a` fora do caminho crítico e `LM-T8` `blocked` por permissão (`AE-42`). | done 35/35 | docs/plans/P-0740-loop-de-modulos.md |
| TK-51 | `CTX-T10` mediu que a rodada Estágio C (`CTX-T6a..T9`) **não** reduziu o custo fixo de abrir uma janela de orquestração — 1º `usage` subiu de ~34-46k para 46.071 tok, +34% vs. mediana anterior. Nenhum card do Estágio C tocou o que compõe esse número (candidato apontado pela própria `CTX-T4`: superfície de ferramentas registrada). Decisão do dono sobre causa/próxima rota é pré-requisito antes de nova rodada. | done *(medido em 2026-08-24 — `docs/CUSTO_DO_PICKUP.md` `## 11`: o Δ de +11.779 tok é carregado pelo componente **opaco** (Δ+11.781 tok), o **visível** (chars do preâmbulo) ficou estável (Δ≈0); dispersão do grupo `antes` (n=233) já continha janela mais cara (46.429) — 46.071 no percentil 94,8, dentro do intervalo. Não corta, não propõe rota)* | docs/DIARIO_DE_OBRAS.md#tk-51--composição-do-1º-usage-de-uma-janela-de-orquestração |
| TK-52 | `GOVERNANCA.md` §4.3 (bullet *"Contexto acabando sem plano de parada"*, linhas 416-420) ainda atribui ao **executor** gravar o checkpoint intermediário e afirma que *"o mesmo checkpoint responde ao sinal de poluição"*. As duas afirmações são contraditas pelos **dois bullets acima, na mesma seção** (Capacidade: *"nunca interrompe tarefa em curso"*; encerramento: *"ato da orquestração, entre tarefas — nunca dentro de uma tarefa, nunca do executor"*) e pelo bloco *"Dois casos que NÃO são checkpoint"* de `.claude/skills/handover/SKILL.md`, que nomeia esses dois casos como **não**-checkpoint. Resíduo não varrido pela `CTX-T1`. Corrigir o bullet e conferir se `.claude/global/CLAUDE.md` Regra 2 carrega o mesmo resíduo. | done *(aceito pelo dono em 2026-08-24 — §4.3 partida em dois bullets e Regra 2 em dois ramos; a Regra 2 **carregava** o resíduo. No mesmo ato, por decisão do dono: correção **propagada** para a cópia implantada em `~/.claude/CLAUDE.md` e cláusula pendurada de `uow.py:23` **dispensada**)* | docs/plans/P-0738-contexto-esgotado.md#9-achados-da-execução |
| P-0722 | Guardrails de doutrina anti-saga (G-DEADCODE, G-PLANFIDELITY, G-PREMISE, G-PLANREADY, G-EXECREADY) | superseded | mesclado em `P-0729-v2-melhoria.md` §1 |
| P-0721 | Governança single-source: PantonicApp como referência | done | `docs/plans/P-0721-governanca-single-source.md` |
| P-0725-3C | Governança em três camadas condicionais | superseded | substituído por `P-0725-governanca-hub-unico.md` |
| P-0725-HU | Hub único: PantonicApp canônico, PantonicVideo como prova | done | `docs/plans/P-0725-governanca-hub-unico.md` |
| TK-23 | A variante (b) do proxy de ocupação de contexto — contador de tarefas por janela calibrado pela série de `docs/telemetria.tsv` — não foi medida pela `EXA-T1` (orçamento esgotado). A variante (a),… | cancelled *(achado da `EXA-T1`)* *(encaminhado ao plano de contexto recomendado pelo P-0737 §8; **absorvido pelo P-0738 em 2026-08-22**, §4 — mede na CTX-T3, rota na CTX-T4)* | docs/DIARIO_DE_OBRAS.md#tk-23--a-variante-b-do-proxy-de-ocupação-de-contexto |
| TK-32 | **Uso e teto: medida agregada ou porteiro de tarefa.** O teto por tarefa vem sendo cruzado com regularidade sem produzir a consequência que a doutrina prescreve — `EXA-T31` consumiu os 15 do teto… | cancelled — a parte interina foi **absorvida pela `DP-Q` em 2026-08-13** e deixou de ser interina: teto numérico não governa fluxo em lugar nenhum do framework, e custo/consumo são informação de agregado, com residência do qualitativo no card "Lições aprendidas na tarefa" do laudo (materializado pelo bloco `EXA-T49`..`T52`). O restante da matéria segue para plano próprio (`T17` item 4), com a `EXA-T34` cancelada por absorção *(achado do fechamento da `EXA-T31`)* *(encaminhado ao plano de contexto recomendado pelo P-0737 §8; **absorvido pelo P-0738 em 2026-08-22**, §4 — mede na CTX-T3, rota na CTX-T4)* | docs/DIARIO_DE_OBRAS.md#tk-32--uso-e-teto-medida-agregada-ou-porteiro-de-tarefa |
| TK-38 | **Comunicação entre agente e humano — skill própria e requisitos mínimos.** Aberto por decisão do dono em 2026-08-13. O framework nomeia objetos de projeto por prefixo abreviado (`DP-`, `DR-`,… | ready | docs/DIARIO_DE_OBRAS.md#tk-38--comunicação-entre-agente-e-humano--skill-própria-e-requisitos-mínimos |
| TK-48 | `~/.claude/settings.json` **perdeu a chave `hooks` inteira silenciosamente**, sem ação intencional do dono, entre a `RPC-T4` e a escolha da `RPC-T5` — os 4 hooks registrados (premissa da `T5`) somem sem rastro. | ready | docs/DIARIO_DE_OBRAS.md#tk-48--~/claude/settingsjson-perdeu-a-chave-hooks-inteira-silenciosamente |
| TK-53 | O que mudou no corte da `95db6421…` que desloca o custo opaco de abertura de janela para as 6 janelas pós-corte inteiras (mediana 46.070 vs. 34.347 do grupo `antes`) — decisão do dono em 2026-08-24 sobre o achado do `TK-51`, causa ainda não investigada. Bloqueia `P-0737`. | done *(**desfecho negativo, decisão do dono em 2026-08-31** — a `TK-53a` mediu que não há degrau no corte: os dois regimes (`cache_read` 18.084 e 26.695) coexistem **antes e depois** dele, então a causa procurada não existe. `TK-53b` **cancelada por absorção** (seu insumo único, o bracket temporal, perdeu o objeto). A pergunta viva migrou para `TK-54`: não *o que mudou*, mas *do que o custo é feito*)* | docs/DIARIO_DE_OBRAS.md#tk-53--causa-do-deslocamento-de-custo-nas-janelas-pós-corte |
| TK-54 | **Extrato do custo de abertura de uma janela principal.** O 1º `usage` decompõe-se em uma linha por fonte carregada, com tamanho medido, origem (nossa ou do harness) e classificação em *válido / necessário / dispensável / economizável* — o detalhamento sem o qual o dono não decide corte nenhum. Substitui o objetivo morto da `TK-53`. Bloqueia `P-0737`. | ready | docs/DIARIO_DE_OBRAS.md#tk-54--extrato-do-custo-de-abertura-de-uma-janela-principal |
| TK-55 | **Confiabilidade de agente e de instrumento.** Acumulador dos casos em que um **derivado** (comando de aceite, piso de regressão, linha de telemetria, achado de lint, linha de índice) erra sem sinal porque nada o confronta com a fonte — `AE-19`, `AE-18`, `AE-3`, `AE-1` e a projeção de índice desatualizada por um dia inteiro em 2026-09-19. Não é erro de execução de tarefa: a janela que os produziu fechou oito tarefas com zero reprovações. | ready | docs/DIARIO_DE_OBRAS.md#tk-55--confiabilidade-de-agente-e-de-instrumento |
| P-0741-MC | O modelo conceitual do plano: a interface entre o dono e o loop | ready 7/8 | docs/plans/P-0741-modelo-conceitual.md |
| TK-56 | **Propagar o reparo de codificação de `stdin` aos três pontos de carga restantes.** `ocupacao.py:141`, `telemetria_hook.py:213` e `modelo_por_fase_userpromptsubmit.py:101` leem `sys.stdin.read()` e decodificam na codificação do host; em Windows sem `PYTHONUTF8` isso é `cp1252`. O terceiro é **global** e roda a cada prompt em todos os projetos — vem degradando em silêncio para prompt acentuado. Regra de reparo pronta na `DB-53` do `P-0739`. Depende do `TK-57`. | done 2/2 | `docs/DIARIO_DE_OBRAS.md` › `## TK-56` |
| TK-57 | **Fixar o ambiente no teste por subprocesso do hook.** `test_tf_hook_executavel_*` em `tests/test_backlog.py` herda o ambiente do `pytest`: em host com `PYTHONUTF8=1` passa com ou sem o reparo, deixando de discriminar. Aplicar as três cláusulas da `DB-53` — roda o processo, fixa `env=` explícito, afirma a invariância entre os dois mundos. **Pré-requisito do `TK-56`.** | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-57` |
| TK-58 | **Fechar a metade `usage_1` da medida de pickup.** O método `DC-4` tem duas metades; a de caracteres está publicada (26.760, −65,5%), e a do primeiro `usage` de uma sessão nova ficou **declarada sem valor** na `## 14` de `docs/CUSTO_DO_PICKUP.md` por não ser observável de dentro de um subagente. Exige abrir uma janela principal nova e ler o primeiro `usage`. | done 4/4 | `docs/DIARIO_DE_OBRAS.md` › `## TK-58` |
| TK-59 | **Guarda para o contador de id do inbox.** `**Próximo id de plano:**` é recalculado por `max(id visto) + 1` sobre o que passou pelo inbox; plano criado sem linha de inbox fica invisível e o contador aponta para id já usado. Ocorreu com o `P-0742` e foi corrigido à mão para `P-0743`. Falta um verificador que confronte o contador com `docs/plans/`. | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-59` |
| TK-60 | **Verificador de citação de seção.** O kit resolve caminho de arquivo (`Test-Path`) e identificador de tarefa (`review_evidence`), mas **nada** resolve *“§X.Y publicada em Z”*. Um ponteiro para seção inexistente atravessou autoria, transcrição aprovada em 100%, duas varreduras e um despacho, e só caiu quando um executor foi abrir o arquivo para editar. | done 3/3 | `docs/DIARIO_DE_OBRAS.md` › `## TK-60` |
| TK-61 | **Implementar o rodapé de “candidato a fechamento” (`DB-4`).** A norma está publicada na `## 3` do `P-0739` **sem implementação e sem teste**: a expressão não existe em `.claude/tools/backlog.py`, e o rodapé de `next` imprime só `inbox de planos`, `fila de memória` e `blocked`. Efeito hoje: pai cujos filhos ficaram todos terminais deveria aparecer no rodapé, e nada o mostra. | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-61` |
| TK-62 | **A gramática de ID de `rdo.py` não reconhece subtarefa de tíquete.** `_ID_HEADER_RE` e `_HEADER_BRACKET_RE` exigem `T` seguido de dígitos; `TK-<n><letra>` nunca casa. Bloqueia o dossiê de evidência e o `rdo.py close` de **toda** subtarefa de tíquete. A `DB-17` justificou a forma com *“já leem essa forma”* — cláusula falsa, nunca verificada. | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-62` |
| TK-63 | **O mundo hostil dos testes de executável é herdado do host, não construído.** Os dois sítios que discriminam hoje o fazem por acidente de plataforma: o mundo “sem `PYTHONUTF8`” só é hostil porque este host é Windows-cp1252. Medido: `PYTHONIOENCODING` prevalece sobre `PYTHONUTF8`, e é ele que constrói o mundo hostil portátil. | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-63` |
| TK-64 | **O `check-drift` está vermelho por linha de skill que nenhuma tarefa aberta possui.** `.claude/README.md` não tem a linha da skill `entrega-de-encerramento`, entrega do `TK-51a` (fechado). O vermelho chega sem dono a toda revisão desta janela e já obrigou três reconciliações manuais. | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-64` |
| TK-65 | **Três defeitos medidos de `backlog.py` na abertura da janela do `P-0741`.** O `check` aprova plano estruturalmente inselecionável (`Depende de:` com id que não é item); o `--help` e todo erro de argparse morrem com `UnicodeEncodeError` em console cp1252; o verbo `diretiva` descarta em silêncio os ids escritos depois do travessão. | ready 0/3 | `docs/DIARIO_DE_OBRAS.md` › `## TK-65` |
| TK-66 | **O atribuidor de `review_evidence.py` fabrica autoria com tarefa nunca despachada.** `--atribuir` casa caminho contra os `Arquivos-alvo` de **qualquer** tarefa do plano sem olhar o `status` dela: na janela do `P-0743` rotulou quatorze arquivos como `alvo-de-outra-tarefa (DOM-T3/T4/T5)` — tarefas em `ready`, que nada produziram —, quando eram entrega de uma janela paralela. No regime de commit por marco, é a atribuição que separa uma entrega da outra, e as duas revisões da janela tiveram de desmentir a evidência mecânica por injeção manual. | ready | `docs/DIARIO_DE_OBRAS.md` › `## TK-66` |
| TK-67 | **A rodada de revisão de guardrails está pendente desde 2026-08-08.** `GOVERNANCA.md` §7.1 pendura a revisão no fechamento de cada plano; a última rodada registrada é a do `P-0731` (2026-08-08) e **sete** planos fecharam `done` depois dela (`P-0732`, `P-0735`, `P-0736`, `P-0738`, `P-0739`, `P-0740`, `P-0743`). §7 passou de 14 guardrails naquela rodada para **20** hoje. A skill `checar-versao-kit` reportou a pendência ao criar o `P-0745` em 2026-09-21; ela não executa a revisão — a revisão é tarefa nomeada, e é este tíquete. | ready | `docs/DIARIO_DE_OBRAS.md` § `## TK-67` |
| TK-68 | **A cópia do kit das regras globais divergiu do arquivo que o dono carrega.** `.claude/global/CLAUDE.md` não tem os **Controles 1.1 e 1.2** da Regra 1 (28 linhas) que o `CLAUDE.md` global do dono carrega desde 2026-09-04, e `.claude/sync-kit.ps1` não projeta `.claude/global/` — as duas cópias se mantêm à mão e nada afere a diferença. Medido em 2026-09-21 na abertura do `P-0745`. | ready | `docs/DIARIO_DE_OBRAS.md` § `## TK-68` |
| P-0743-DOM | O modelo conceitual vira modelo de domínio — **aceito pelo dono em 2026-09-21**. As 18 tarefas fecharam aprovadas; a norma, a gramática, o instrumento `modelo.py` e o agente `pantonic-model-designer` publicam o modelo de domínio em objetos com propriedades, fluxo de operações, estado inicial × estado final e registro de versões, e o próprio plano é o primeiro do acervo escrito na forma nova. O Marco 3 foi **dispensado** por ato do dono, que moveu a validação para o as-is. **Entrega validada: `docs/Entregas Aceitas/Entregas - P-0743.md`** (875 linhas, cobre também o `P-0741`), onde vivem as oito pendências abertas — três com efeito fora deste plano (`AE-25` telemetria, `TK-66` atribuição de evidência, `AE-24` residência de prova). Vinte e cinco achados (`AE-1`..`AE-25`), dez escalonamentos ao consultor, uma rodada de replanejamento (`RP-1`). Nada commitado. | done 18/18 | docs/plans/P-0743-modelo-de-dominio.md |
| P-0744-PLS | A especificação do agente de planejamento — substituído por: `P-0745` (2026-09-21, `DPN-1`) | superseded | docs/plans/P-0744-spec-do-planejador.md |

---

## P-0737 — Loop autônomo

> **Índice (texto integral do campo Título, migrado da tabela ativa em 2026-08-23):** Loop autônomo — o plano que consolida a `EXECUCAO-AUTONOMA`: 10 tarefas (`AUT-T1..T10`), decisões `DU-1..DU-13`, absorve as 8 tarefas abertas do `P-0734` e 11 tíquetes, poda 10 e encaminha 2; `AUT-T5` partida em `T5a`/`T5b`/`T5c` por orçamento no gate de delegação (3/12). **`blocked` em 2026-08-22 — paralisado por decisão do dono** enquanto o `P-0738` não fecha; a razão é o custo fixo de contexto, não defeito do plano
>
> *(Âncora original do índice, preservada:* `docs/plans/P-0737-loop-autonomo.md` *)*

**Objetivo (herdado verbatim da diretiva do dono, 2026-08-22):** transformar o trabalho de
`proximo-passo` num agente autônomo, capaz de rodar sozinho todas as delegações e ajustes de modelo e
entregar ao cliente o entregável do plano, sem delegar ao humano tarefa rotineira e mecânica. O plano
existe para desfazer o drift medido — instrumento, papel e doutrina em volume, e o loop nunca rodando.

**Plano:** `docs/plans/P-0737-loop-autonomo.md` — **10 tarefas** (`AUT-T1..T10`), decisões
`DU-1..DU-13` fechadas no ato do planejamento (cinco do dono, oito de planejamento). Absorve as **8**
tarefas abertas do `P-0734` e **11** tíquetes; **10** tíquetes são podados e **2** encaminhados ao
plano de contexto recomendado; `TK-38` e `TK-48` seguem vivos, sem toque. Sem bump e sem tag
(`DE-7`). **Checagem de versão do kit:** modo hub — congelada em `0.0.0`, nada a comparar.

**Ordem de execução (§7 do plano, e não a numeração):** `AUT-T1` → `AUT-T5` → `AUT-T4` → `AUT-T2` →
`AUT-T3` → **[ratificação em lote do dono, `DU-12`]** → `AUT-T6` → `AUT-T7` → `AUT-T8` → `AUT-T9` →
`AUT-T10`.

**Próxima tarefa:** **nenhuma — plano `blocked`**. A razão vigente até 2026-08-24 (esperar o `TK-51`
devolver a medida) foi **satisfeita e fechada com ressalva** — `TK-51` mediu o número, mas a linha de
fecho não discriminava ruído de deslocamento (laudo `docs/RDO/laudos/DIARIO-TK-51.md`, Achado 3).
**Decisão do dono (2026-08-24): deslocamento real** — as 6 janelas pós-corte formam um padrão, não
ruído isolado. **Razão do `blocked` substituída de novo em 2026-08-31, por decisão do dono:** a `TK-53` fechou com
desfecho negativo (não houve mudança no corte — os dois regimes de custo coexistem dos dois lados
dele), o que **não** destrava este plano: a premissa que o loop constrói continua contradita, agora
por um motivo melhor definido — o custo de abrir janela **não é fixo, é bimodal**, com ~11,7k tok de
diferença entre os dois regimes e nenhuma explicação de qual fonte alterna. Não sai tarefa deste
plano até a `TK-54` publicar o extrato do custo e o dono ratificar a classificação. O custo fixo de abrir janela
é premissa direta do loop que este plano constrói; destravar sobre uma premissa já contradita
repetiria o erro que reprovou o critério (a) do `P-0738` — agir sem entender a causa. **Não destravar
por heurística:** as razões anteriores (`P-0738`, `TK-52`, `TK-51`) não valem mais como gatilho. A
razão do `blocked` segue externa ao plano: nenhum defeito do `P-0737` foi apontado, e nada aqui é
reaberto ou reescrito.
**Ao destravar, a fila retoma exatamente em `AUT-T5c`** — frente (c) do dossiê `### AUT-T5` (mede o
`TK-27`: se o `tools:` do frontmatter de agente aceita especificador de `Bash` escopado; **para**
para a ratificação em lote da `DU-12`; nenhuma edição em `pantonic-reviewer.md`), e depois segue a
ordem do §7 (`AUT-T4` → `AUT-T2` → `AUT-T3` → [ratificação `DU-12`] → `T6`..`T10`).

- **Paralisação por decisão do dono — 2026-08-22.** Registrada no ato da análise crítica do pickup da
  `AUT-T5b`. Fato medido que a originou: a tarefa consumiu **três janelas de orquestração** — (A)
  pickup pago, teto cruzado no gate de delegação **sem delegar**; (B) pickup pago, delegação
  despachada e teto cruzado **antes do retorno**, deixando o ato de fechamento órfão; (C) pickup pago
  integralmente para verificar entrega já pronta e escrever 2 edits. O trabalho real coube num único
  subagente em background. Cada janela repagou os **77.457 chars (~19.364 tokens)** que a `CPK-T2`
  mediu como pickup típico, dos quais **43,8% são custo fixo de entrada**. Diagnóstico preliminar
  levado à linha do `_INBOX.md` **sem ratificar rota**: o gate de delegação orça o teto do executor e
  não o saldo do orquestrador; o custo fixo não amortiza entre tarefas; e a verificação foi feita à
  mão, no contexto mais caro, existindo `review_evidence.py` e `pantonic-reviewer` para isso. A
  **Diretiva** deste diário foi condensada de 20 para 15 linhas no mesmo ato — o conteúdo retirado
  (drift da `EXECUCAO-AUTONOMA`, reconciliação `P-0734`/`P-0733`, recomendações do §8) não foi
  apagado: vive na linha `P-0737-loop-autonomo` do `_INBOX.md` e nesta seção.

**`AUT-T5` partida em `T5a`/`T5b`/`T5c` por orçamento — 2026-08-22, no gate de delegação.** Medidos
~12-14 write-clusters contra o limite de 8, com duas das três frentes comportamentais (mudam
contrato de CLI e assinatura de renderização). **Sem mudança de rota ou de escopo**: a partição segue
as três frentes já publicadas no dossiê, que permanece intocado, e o corte é o mesmo precedente da
`RPC-T7` do `P-0735`. Fatias: **`T5a`** = frente (a), sentinela de métrica ausente
(`.claude/tools/telemetria.py`, `docs/telemetria.tsv:50`, `tests/test_telemetria.py`), classe
`implementacao`, Sonnet, teto 40; **`T5b`** = frente (b), escopo do dossiê de evidência
(`.claude/tools/review_evidence.py`, `tests/test_review_evidence.py` e a conciliação de
`.claude/skills/scrum-master/SKILL.md:143`, que o *Conteúdo* do dossiê manda tocar e o campo
*Arquivos-alvo* omitiu), classe `implementacao`, Sonnet, teto 40; **`T5c`** = frente (c), medição do
`TK-27` e o achado no §9 do plano, **tarefa-investigação** que mede e **para** para a ratificação em
lote da `DU-12`, teto 15. O denominador do plano passa de 10 para 12.

**Notas de execução:**

- **`AUT-T5b` — done, confirmado em contexto novo — 2026-08-22.** Achado no pickup: o trabalho já
  estava materializado no working tree (agente em background da rodada anterior concluiu antes do
  retorno chegar a esta sessão — contexto anterior encerrado por capacidade sem consumir a
  notificação). Verificado, não redelegado: diff de `review_evidence.py`/`test_review_evidence.py`/
  `scrum-master/SKILL.md:143` bate exatamente com as duas frentes do dossiê (alvo-diretório por
  prefixo, `--desde <ref>`); suíte **83 passed** (piso `AUT-T5a` era 80, +3 testes novos da `T5b`).
  Consumo: ver `docs/telemetria.tsv` (`nao_medido` — notificação da sessão anterior perdida no
  `<usage>`, mesmo padrão da `RPC-T11`).
- **Checkpoint de janela — `AUT-T5b` delegada, aguardando retorno — 2026-08-22.** Dossiê montado com
  design já resolvido (alvo-diretório por prefixo, `--desde <ref>` sem tocar `DP-S`/`tarefa-corrente.json`)
  e despachado ao `pantonic-executor` em background (agentId `adb71e11660fbf127`). Contexto encerrado
  por capacidade antes do retorno. **Próximo passo:** aguardar a notificação de conclusão, fechar o
  registro (bullet + `docs/telemetria.tsv`) e seguir a ordem do §7 (`AUT-T4` depois).

- **Checkpoint de janela — pickup da `AUT-T5b` encerrado por capacidade, sem delegação — 2026-08-22.**
  Janela cruzou o teto no gate de delegação, depois do levantamento das âncoras. **Âncoras
  re-derivadas nesta rodada, para o contexto novo não repagar:** `review_evidence.py` 413 linhas —
  comparação literal de escopo em `confrontar_escopo:129-138` (`t not in alvo_set`), fallback
  "arquivo ausente na árvore de trabalho" em `_diff_para_arquivo:141-151`, recorte da árvore inteira
  em `coletar_arquivos_tocados:111-126` (`git status --porcelain=v1 --untracked-files=all`), bloco
  `argparse` em `main:362-384` (sem `--desde`), seção `## Escopo` do render em `_renderizar:272-285`
  (onde entra a declaração de recorte), chamada em `montar_documento:336`;
  `tests/test_review_evidence.py` 277 linhas; conciliação da skill em
  `.claude/skills/scrum-master/SKILL.md:143-145` (comando) — o `.claude/estado/tarefa-corrente.json`
  do passo 4 (`:88-94`) **não** tem campo de ref de git, então de onde sai o `<ref>` do `--desde` é
  ponto a fechar no dossiê. Piso da suíte (80 passed, `AUT-T5a`) **não** re-medido — a suíte não
  chegou a rodar.

- **`AUT-T5a` — done em 2026-08-22.** A célula vazia passou a ser a sentinela única de métrica
  ausente: `_validar_inteiro_nao_negativo` e `_validar_numero_nao_negativo` ganharam `permite_vazio`,
  e `build_row` valida `fonte` primeiro para propagá-lo às três colunas numéricas — com
  `fonte = usage` o vazio continua falha ruidosa, porque ali a medida é perdida, não ausente. A
  única linha histórica com traço literal (`docs/telemetria.tsv` L50, `V2I-T3`) foi normalizada, com
  o Grep de reconferência medindo 1 match antes e 0 depois e o resto do arquivo preservado. Ordem TDD
  demonstrada por `git stash` do fix: os dois testes de aceitação falharam sem ele e passaram com
  ele; o de recusa por `fonte = usage` já passava. Bateria do §3 inteira em exit 0; suíte em **80
  passed** (piso era 77 — subiu). **Reconciliação de série feita pelo orquestrador no fechamento:** a
  prova ponta a ponta exigida pela *Verificação* apende uma linha real pelo instrumento, e essa
  linha nasce auto-relatada (`fonte = contado`), o que colidiria com a linha medida da mesma tarefa;
  a célula `tarefa` da linha de prova passou a `AUT-T5a-prova-instrumento` — correção de
  identificador, não de número — e a linha canônica da tarefa foi apendada do bloco `<usage>` com
  `fonte = usage`. Nenhum achado fora de escopo. Consumo: ver `docs/telemetria.tsv`.

- **Registro do plano — 2026-08-22.** Plano autorado em contexto novo, a partir do inventário e das
  decisões que a rodada de consolidação do mesmo dia deixou na linha `P-0737-loop-autonomo` do
  `docs/plans/_INBOX.md` (agora `[drenado]`). Reconciliação de planos derivados aplicada no mesmo
  ato: `P-0734` → `superseded` (classificação B), `P-0733` → `cancelled` (`DU-1`) — a iniciativa
  volta a ter **um** plano vivo. Nenhuma questão precisou subir ao dono na autoria: as duas que
  ameaçavam abrir ramo — o portador do checkpoint de contexto (`TK-37`) e a fronteira de ferramenta
  do `pantonic-reviewer` (`TK-27`) — foram fechadas, a primeira por derivação do já ratificado
  (`DU-8`) e a segunda como medição que **para** para a ratificação em lote (`DU-12`). O agente de
  planejamento caiu por **limite de sessão da API** depois de publicar o plano e antes de fechar o
  registro no diário; retomado pelo mesmo `agentId` com o delta, sem re-delegação a frio. Consumo:
  ver `docs/telemetria.tsv` — a fatia anterior à queda não traz bloco `<usage>` e está **PARCIAL,
  não medida**.
- **Acréscimo de escopo por decisão do dono — 2026-08-22.** Achado de fronteira levantado no
  fechamento da autoria: o `P-0737` nasceu com 574 linhas, acima do gatilho de 500 do
  `docs/DOC_MAP.md`, que hoje indexa três planos grandes e não este. O dono decidiu acrescentar a
  entrada ao dossiê da `AUT-T1` (frente **(e)**) em vez de abrir tíquete ou ignorar — a `T1` já
  edita o kanban, o custo marginal é zero, e plano desse porte fora do mapa reintroduz o custo de
  navegação que o `P-0736` mediu. Único ponto do plano publicado alterado depois da publicação;
  `Arquivos-alvo`, `Invariantes`, `Verificação` e `Pronto quando` da `AUT-T1` atualizados no mesmo
  ato. Teto da tarefa mantido em 20.
- **`AUT-T1` — done em 2026-08-22.** O kanban passou a dizer a verdade do dia: as 23 células de
  tíquete do índice receberam rota única — 10 `cancelled` por poda, 11 com a nota de absorção e a
  `AUT-T<n>` que as fecha, 2 encaminhadas ao plano de contexto recomendado —, e `TK-38`/`TK-48`
  ficaram intocados. O `TK-18` teve a razão do `blocked` amarrada à `AUT-T9`. O
  `P-0734-execucao-autonoma.md` ganhou a seção `## 24. Rebase pelo P-0737` como acréscimo no fim do
  arquivo, com a tabela das 8 absorvidas e a `T16` cancelada por absorção; nenhum dossiê, bullet ou
  decision record anterior foi tocado. A frente **(e)** indexou o plano no `docs/DOC_MAP.md` com o
  porte re-derivado no ato (**586 linhas**, e não as 574 que o dossiê supunha) e padrão de acesso
  `^### AUT-T5 ` conferido por execução. As 23 anotações foram aplicadas num único passo
  programático, com guarda de 6 campos por linha da tabela — 23 edições linha a linha estourariam o
  teto da classe `mecanica`. Bateria do §3 inteira em exit 0; suíte em **77 passed**. Nenhum achado
  fora de escopo. Consumo: ver `docs/telemetria.tsv`.

- **2026-08-23 (`CTX-T6a`, item 4):** os 11 tíquetes absorvidos por este plano fecham `cancelled` no índice (preservando o ponteiro `fecha na AUT-T<n>` de cada célula) e migram para `docs/DIARIO_HISTORICO.md`: `TK-04` (fecha na `AUT-T9`), `TK-18` (fecha na `AUT-T10`), `TK-26` (fecha na `AUT-T5`), `TK-27` (fecha na `AUT-T5`), `TK-30` (fecha na `AUT-T8`), `TK-44` (fecha na `AUT-T5`), `TK-36` (fecha na `AUT-T6`), `TK-37` (fecha na `AUT-T6`), `TK-42` (fecha na `AUT-T9`), `TK-46` (fecha na `AUT-T10`), `TK-50` (fecha na `AUT-T5`).
## P-0738 — Contexto esgotado na partida

**Objetivo:** parar de repagar, a cada janela, o custo fixo que faz um contexto nascer esgotado. A
`AUT-T5b` consumiu três janelas de orquestração para uma tarefa atômica cujo trabalho real coube num
único subagente; cada janela repagou os **77.457 chars (~19.364 tokens)** do pickup medido pela
`CPK-T2`, dos quais **43,8% são custo fixo de entrada**. O plano vai da medida à execução: mede a
ocupação real de uma janela pelo transcript, ratifica causas raízes com o dono e executa as ações no
mesmo plano — não termina no diagnóstico.

**Plano:** `docs/plans/P-0738-contexto-esgotado.md` — **17 tarefas** (`CTX-T1`, `CTX-T1b`,
`CTX-T1c`, `CTX-T1d`, `CTX-T2`..`CTX-T5`, os **7 cards do Estágio C** autorados pela charneira —
`CTX-T6a`, `CTX-T6b`, `CTX-T7`, `CTX-T8a`, `CTX-T8b`, `CTX-T8c`, `CTX-T9` —, `CTX-T10`,
`CTX-T11`); decisões `DX-1`..`DX-15`. Absorve as recomendações **(b)** e
**(c)** do `P-0737` §8 e os tíquetes **`TK-23`** e **`TK-32`**; **não** absorve a recomendação (a), o
piloto. Relatório em `docs/CUSTO_DO_PICKUP.md` (`## 7`..`## 10`). Sem bump e sem tag (`DE-7`).
**Checagem de versão do kit:** modo hub — congelada em `0.0.0`, nada a comparar.

**Ordem de execução (§6 do plano):** `CTX-T1` → `CTX-T1b` → `CTX-T1c` → `CTX-T1d` → `CTX-T2` →
`CTX-T3` → `CTX-T4` → `CTX-T5` → `CTX-T6a` → `CTX-T6b` → `CTX-T7` → `CTX-T8a` → `CTX-T8b` →
`CTX-T8c` → `CTX-T9` → `CTX-T10` → `CTX-T11`.

**Próxima tarefa:** **nenhuma — plano concluído `17/17` em 2026-08-24**, com a `CTX-T11` aceita pelo
dono. Duas pendências saem daqui e **não** são tarefa deste plano: o `TK-51` (a `CTX-T10` mediu
regressão — critério (a) reprovado) e o achado da `CTX-T11` sobre `GOVERNANCA.md` §4.3, ambos
dependentes de decisão do dono.

- **`CTX-T9` — a skill de orquestração encolhe sem perder ato — `done` em 2026-08-24.**
  `.claude/skills/scrum-master/SKILL.md` condensada de 15.131 para **14.980 chars** (4 cortes de
  prosa: justificativa/exemplo viraram ponteiro ou caíram); 19 cabeçalhos preservados na mesma
  ordem, nenhum passo/gate/contador/roteamento mudou. A 7ª âncora `G-SURFACE` (linha 119, herdada
  da `CTX-T1c`) morreu — a `G-SURFACE` daquela decisão fecha 7/7 e a `CTX-T1e` deixa de ser
  necessária. `CHANGELOG.md` ganhou a linha única `(CTX-T9)` sob `## [Não lançado]`.
  `git status --short` acusa só os dois arquivos-alvo.
- **`CTX-T8c` — a verificação de entrega sai do contexto caro — `done` em 2026-08-23.** A linha de
  invocação de `.claude/tools/review_evidence.py` passou a ser publicada nos **dois** pontos onde é
  consumida, idêntica em ambos: `.claude/skills/scrum-master/SKILL.md` (Passo 6, linha 149) já a
  trazia e ganhou a declaração de que o instrumento **se executa** — abrir o fonte para entender a
  chamada é sinal de documentação insuficiente, não caminho normal —; `.claude/agents/pantonic-reviewer.md`
  recebeu bullet novo (após a linha 32) com o **mesmo** comando e a mesma declaração, fechando o
  ponto onde antes só se citava o instrumento sem dizer como chamá-lo. Causa `C5` atacada; ganho
  esperado ~3.700 tok por fechamento. **Nenhuma responsabilidade mudou:** o ato segue do
  `pantonic-reviewer` pela matriz. **Fronteira `DX-9` respeitada** — só texto e ponteiro, nenhum
  passo criado; os cabeçalhos `### Passo 1..10` do `scrum-master` seguem na mesma ordem. Nenhum
  `.py`, teste ou `CHANGELOG.md` tocado (a invariante "instrumento nasce com teste" não se aplica);
  o delta acrescentou à árvore apenas `.claude/agents/pantonic-reviewer.md`.
  Consumo: ver `docs/telemetria.tsv`.

- **`CTX-T8b` — a janela de orquestração amortiza o custo fixo — `done` em 2026-08-23.** A §4.3 do
  `GOVERNANCA.md` deixou de ser ambígua sobre o que fecha ao fim de uma tarefa: o parágrafo do
  fechamento (linhas 398-402) passou a dizer que o contexto encerrado por tarefa concluída é o **do
  executor** — um por tarefa —, e que a **janela de orquestração é outra coisa e não fecha junto**,
  seguindo a regra do bullet anterior (atravessa as tarefas atômicas do mesmo plano, encerra na
  troca de plano/iniciativa ou, de forma planejada, na ocupação). O restante da §4.3 **não foi
  reescrito**: as linhas 390-397 já enunciavam a amortização e o contrato ali já estava satisfeito —
  a tarefa foi de desambiguação do resíduo, não de reautoria. Causa `C2` atacada; ganho esperado
  ~8.400 tok da segunda tarefa da janela em diante. **`DX-14` item 3 preservada e instrumento
  intacto:** `Grep "ocupacao.py" GOVERNANCA.md` segue com 1 match (linha 394), texto idêntico ao
  baseline; `.claude/tools/ocupacao.py` não foi tocado. **Fronteira `DX-9` respeitada** — nada
  materializado em passo, contador ou tabela de roteamento do `scrum-master` (matéria da `AUT-T6`);
  `## 9. Achados` não recebeu linha. `CHANGELOG.md` ganhou o bullet de topo sob `## [Não lançado]`.
  Consumo: ver `docs/telemetria.tsv`.

- **`CTX-T8a` — a varredura sai do papel caro — `done` em 2026-08-23.** O passo 4 da skill
  `proximo-passo` deixou de acionar o papel barato por gatilho condicional (*"se entender o estado
  atual exigir ler mais de ~1-2 arquivos de código-fonte integrais"*) e passou a acioná-lo por
  **regra de precedência**: toda coleta que não seja Read de âncora já conhecida (arquivo + range de
  linhas) ou Grep de string exata vai para `pantonic-scout` (ou `context-scout` via `context-prep`
  fora do projeto), e **ler no contexto caro virou exceção declarada no ato, com o motivo escrito na
  delegação** — nunca o default. O item (4) da *"Fonte do contexto"* seguiu a mesma inversão: de
  "leitura direta só para ≤1-2 arquivos pequenos já conhecidos" para "exceção declarada no ato…
  qualquer outra coleta é (3)". As **duas** ocorrências de `1-2 arquivos` saíram (o dossiê previa a
  verificação, mas só a do bloco 1 era óbvia; a segunda estava no item (4) do bloco 2). Causa `C1`
  atacada; ganho esperado ~25.700 tok por varredura movida (executor 34.016 tok, n=149, contra
  `pantonic-scout` 8.340, n=10 — 4,1×). **Fronteira `DX-9` não tocada:** mudou o critério de
  acionamento de um ato que já era do passo 4; nenhum passo, gate, contador ou linha de roteamento
  nasceu, e `## 9. Achados` não recebeu linha. **Âncoras:** as do dossiê (71-77 / 78-86) estavam
  defasadas; reais 72-79 e 81-88, re-derivadas no gate antes da delegação. Consumo: ver
  `docs/telemetria.tsv`.

- **`CTX-T7` — a fila corrente e o dossiê viram ponteiro — `done` em 2026-08-23.** O cabeçalho do
  diário ganhou, logo abaixo da Diretiva, a linha única `**Fila corrente:**` — projeção que carrega
  plano, ID da tarefa, caminho do dossiê **com o range de linhas** e a fila restante. Uma retomada
  passa a saber qual é a tarefa e onde está o dossiê dela lendo `offset:1 limit:15`, em vez de
  reconstruir a fila por varredura (39 matches históricos de `Próxima tarefa` no kanban). O bloco é
  **projeção, não fonte nova**: a linha `Próxima tarefa` da seção do plano continua existindo e
  continua sendo a prosa do fechamento; as três skills que já a escrevem — `diario-de-obras` (bullet
  "Sprints multi-tarefa"), `scrum-master` (bullet de parada) — passaram a mandar reescrever o bloco
  **no mesmo ato, pelo mesmo autor**, e o passo 3 do `proximo-passo` trocou o `Grep "Próxima tarefa
  da sprint"` pelo `Read offset:1 limit:15` (o Grep antigo não retorna mais nada na skill). Causas
  `C6` e `C7` fechadas; ganho projetado ~6.000–6.900 tok por janela. **Fronteira `DX-9` não tocada:**
  nenhum passo, gate, contador ou linha de roteamento nasceu — mudou onde se lê e o que a linha
  carrega. **Âncora corrigida no ato:** o dossiê apontava `proximo-passo/SKILL.md:54`, real 55.
  **Achado de verificação, sem conserto:** `git status --short` não isola os quatro arquivos-alvo
  porque o working tree já vinha sujo de sessões anteriores (~20 arquivos `M`/`??` pré-existentes,
  nenhum deles tocado por esta tarefa). Consumo: ver `docs/telemetria.tsv`.

- **`CTX-T6b` — o inbox de planos sai do pickup — `done` em 2026-08-23.** O `docs/plans/_INBOX.md`
  caiu de **292 linhas / 27.381 chars para 12 linhas / 844 chars** (−96,9%): o pickup deixa de
  reingerir 283 linhas de bullets já drenados para drenar zero. As **18** entradas `[drenado]` e os
  **2** bullets de correção de 2026-07-29 migraram verbatim, na ordem original, para
  `docs/plans/_INBOX_HISTORICO.md` (novo, 291 linhas / 27.229 chars, com cabeçalho próprio que o
  declara destino de arquivamento e nunca de reescrita). Nada se perdeu: as 283 linhas de corpo
  estão inteiras do outro lado, e a linha **Próximo id de plano** sobreviveu literal no arquivo
  vivo. As duas skills passaram a citar o arquivo vivo como única fonte da drenagem
  (`proximo-passo` item 1; `diario-de-obras` item 5, onde drenar agora **move** a linha em vez de
  só marcá-la in-place). **Bloqueio no meio da execução, resolvido sem subir ao dono:** o executor
  parou porque "manter o cabeçalho" e o aceite `Grep "\[drenado\]"` sem retorno não fechavam juntos
  — a linha 8 citava o token em prosa. Não era contradição de rota: o contrato já exigia um ponteiro
  novo no cabeçalho, logo ele mudava de qualquer forma; a frase foi reescrita para descrever o
  arranjo de dois arquivos sem emitir o token, e a residência canônica da convenção do marcador
  continua sendo `.claude/skills/diario-de-obras/SKILL.md`. O mesmo defeito de leitura explicou o
  número errado do dossiê (**19** bullets veio de um grep sobre o arquivo inteiro, que casava a
  prosa do cabeçalho; corpo real = **18**). Verificação conferida pelo orquestrador contra o disco:
  `[drenado]` devolve **0** no arquivo vivo e **18** no histórico, `12 ≤ 40`, soma `12 + 291 = 303 ≥
  292`, e `git status --short` acusa exatamente os quatro alvos. **Fora de escopo, indexado sem
  conserto:** a linha 230 do `diario-de-obras` (apensar plano novo ao inbox) não foi tocada — apensar
  continua indo ao arquivo vivo, e a citação não é de drenagem. Consumo: ver `docs/telemetria.tsv`.

- **`CTX-T6a` — o diário para de ser lido inteiro — `done` em 2026-08-23.** O kanban ativo caiu de
  **3.016 linhas / 349.153 chars para 539 linhas / 57.119 chars** (−83,6%), e a tabela do índice, de
  **86.579 para 7.363 chars** (alvo ≤ 8.000), com a maior célula *Título* em **199 chars** contra as
  54 que passavam de 200 na entrada. Os números herdados do dossiê estavam vencidos (2.935/341.964) e
  foram re-derivados no gate. Nada foi descartado: a soma dos dois arquivos subiu de **621.227 para
  625.977 chars**, porque o texto que saiu das células passou a viver em blockquote ou em seção — as
  4 seções terminais (`P-0733`/`P-0734`/`P-0735`/`P-0736`) migraram verbatim para o histórico, os 3
  planos terminais sem seção ativa ganharam container próprio lá, e os itens **vivos** (`P-0737-AUT`,
  `TK-23`, `TK-32`, `TK-38`, `TK-48`) ficaram no diário como hook + âncora para seção do próprio
  arquivo, pela regra 3-B da `DX-16`. O item 4 fechou os 11 tíquetes absorvidos com o ponteiro
  `AUT-T<n>` extraído verbatim por regex de cada célula, nunca redigitado, e o bullet datado na seção
  `## P-0737` mantém a matéria visível a partir do plano vivo que a carrega. Todo o corte saiu de uma
  sonda programática única no scratchpad, com parse por pipe não-escapado — as 3 células com `\|`
  eram a armadilha medida no gate — e escrita só depois de as 6 verificações passarem em dry-run.
  Verificação conferida pelo orquestrador contra o disco: `^## P-07` devolve exatamente duas seções,
  os 11 `TK-*` flipados estão fora do índice ativo e presentes no histórico, a linha `Próxima tarefa`
  sobreviveu intacta e `git status --short` acusa só os dois arquivos-alvo. **Achado fora de escopo,
  indexado sem conserto:** a transição `## P-0737` → `## P-0738` não tem o separador em branco que as
  demais transições de seção usam (defeito pré-existente). Consumo: ver `docs/telemetria.tsv`.

- **Rodada de replanejamento por decisão do dono — 2026-08-23 — `DX-16`.** A premissa falsa que
  bloqueou a `CTX-T6a` foi levada ao dono no pickup seguinte e fechada em duas decisões, transcritas
  pelo planejamento sem reabrir mérito. **(1)** O texto longo de linha **viva** do índice passa a ter
  residência: **seção `## <ID>` no próprio diário ativo**, com a célula virando hook ≤ 200 chars +
  âncora — a mesma forma dos planos vivos. Recusadas as alternativas de criar um arquivo próprio de
  tíquetes vivos (terceira residência, arrastaria a skill `diario-de-obras`) e de relaxar o teto de
  200 chars (deixaria a causa `C3` intacta na tabela que todo pickup lê). **(2)** Autorizado o
  **flip** dos **11 tíquetes** que a poda de 2026-08-22 já declarara absorvidos pelo `P-0737`
  (`TK-04`, `TK-18`, `TK-26`, `TK-27`, `TK-30`, `TK-36`, `TK-37`, `TK-42`, `TK-44`, `TK-46`,
  `TK-50`): viram `cancelled *(absorvido pelo P-0737, fecha na AUT-T<n>)*` dentro da própria
  `CTX-T6a`, com o ponteiro `AUT-T<n>` preservado verbatim e a lista replicada num bullet da seção
  `## P-0737` — a execução do flip estava alocada à `AUT-T1` de um plano que **este** plano
  paralisou, e trocar marcador de status não cria passo, ramo nem roteamento (carve-out declarado à
  `DX-9`). Com o flip, as 16 linhas sem destino caem para **5** (`P-0737-AUT`, `TK-23`, `TK-32`,
  `TK-38`, `TK-48`). **Consequência sobre o aceite:** o critério **"≤ 450 linhas" caiu** — texto que
  sai da tabela e fica no mesmo arquivo não reduz linha; mede-se agora **a tabela do índice
  (≤ 8.000 chars)** e o teto por célula. Editado: `## 2` (linha `DX-16`) e o card `### CTX-T6a`
  (contrato, verificação, pronto quando) do plano. Nenhuma questão nova ao dono; a `Q1` segue aberta
  e independente.

- **`CTX-T6a` — 2026-08-23 — `blocked`, razão `premissa`.** Nenhum arquivo tocado; nenhuma edição em
  `docs/DIARIO_DE_OBRAS.md` ou `docs/DIARIO_HISTORICO.md`. Medido por sonda: diário em **357.008
  bytes / 2.982 linhas**; 4 seções terminais a migrar (`P-0733` cancelled, `P-0734` superseded,
  `P-0735` done, `P-0736` done), 2 a ficar (`P-0737` blocked, `P-0738` in-progress) — essa parte do
  contrato é executável. **A premissa falsa:** o item 3 exige coluna *Título* ≤ 200 chars **sem
  exceção**, mas o item 1 só autoriza migrar texto de linha **terminal** — e **16 linhas
  não-terminais** passam de 200 chars com conteúdo substantivo e sem destino autorizado:
  `P-0737-AUT` (421) e os tíquetes vivos `TK-04` (240), `TK-18` (1084), `TK-23` (517), `TK-26`
  (3015), `TK-27` (800), `TK-30` (2016), `TK-32` (2170), `TK-36` (2447), `TK-37` (2113), `TK-38`
  (2743), `TK-42` (890), `TK-44` (896), `TK-46` (621), `TK-48` (508), `TK-50` (1064). Hipótese de
  que o excedente fosse anotação de rastreio cortável foi testada e **refutada**. As três saídas que
  o executor recusou por não serem dele: destino fora de `Arquivos-alvo`, descarte de conteúdo
  (viola invariante 8) ou arquivar item aberto no histórico (misrepresenta trabalho vivo como
  fechado). Consumo: ver `docs/telemetria.tsv`.

- **`CTX-T5` — charneira: o Estágio C autorado e fechado — 2026-08-23 — `done`.** As nove causas
  ratificadas da `## 9` viraram **7 cards** na faixa reservada, partidos por letra (regra 6) para
  manter cada um numa matéria só: `T6a` (`C3`, condensar o diário) · `T6b` (`C4`, inbox ao
  histórico) · `T7` (`C6`+`C7`, ponteiro único da fila e do dossiê) · `T8a` (`C1`, a varredura sai
  do papel caro) · `T8b` (`C2`, a janela amortiza o custo fixo) · `T8c` (`C5`, a verificação sai do
  contexto caro) · `T9` (`C8`, condensação do `scrum-master`). **`C9` é a única sem card**, por ter
  rota ratificada `manter` e ganho 0. Ordem por grandeza e ganho (regra 7): as três mecânicas
  abrem, as três comportamentais seguem por ganho, a condensação fecha. Todos os cabeçalhos na
  gramática da `DX-15` (`[<modelo> · classe <classe>]`, sem teto) e o dimensionamento exercido no
  planejamento **sem ser publicado no card**. Dois achados abertos foram **absorvidos sem card
  novo**: a 7ª âncora da `G-SURFACE` da `DX-13` (`scrum-master:119`) entra na `CTX-T9`, o que fecha
  o achado da `CTX-T1d` e **torna a `CTX-T1e` desnecessária**; e a lição do critério de grep
  negativo (citar a string exata, nunca o radical) foi aplicada em todas as sete linhas de
  *Verificação*. Denominador do plano fechado em **17** (a previsão de `n/14` supunha quatro
  cards). Nenhuma rota nova foi inventada, nenhum card altera responsabilidade, passo, gate,
  contador ou tabela de roteamento — a fronteira `DX-9` está declarada card a card, com a
  instrução de parar e registrar em `## 9. Achados` se a materialização exigir fluxo.
  Consumo: ver `docs/telemetria.tsv`.

- **`CTX-T4` — causas raízes, rotas e o round-trip único do dono — 2026-08-23 — `done`.** A seção
  `## 9 Causas raízes e veredito do dono (2026-08-23)` entrou em `docs/CUSTO_DO_PICKUP.md` com **37
  linhas** (teto de 40; arquivo em 278 de 320). **Nove causas**, cada uma com número colado da `## 7`
  ou da `## 8`, artefato-alvo com caminho exato, rota do conjunto fechado da `DX-6` e ganho estimado,
  ranqueadas por ganho: `C1` papel caro lendo (`delegar`, ~25.700 tok por varredura) · `C2` custo
  fixo não amortizado (`amortizar`, ~8.400) · `C3` diário relido na própria janela (`condensar`,
  7.800–15.252) · `C4` `_INBOX.md` integral (`mover-ao-historico`, ~6.600) · `C5` verificação à mão
  (`delegar`, ~3.700) · `C6` fila sem ponteiro (`ponteiro`, ~3.500) · `C7` dossiê do plano integral
  (`ponteiro`, 2.500–3.400) · `C8` `scrum-master` (`condensar`, ~2.800) · `C9` `TK-23`(b) (`manter`,
  0 — o tíquete fecha por medida, sem instrumento novo). Os **três diagnósticos preliminares** do §0
  saem **`confirmado`**, cada um com o número que o sustenta. **Round-trip único cumprido** (`DC-9`):
  causas e rotas **ratificadas na forma proposta**; o **alvo foi recusado** pelo dono — *"não aceito
  valores sem respaldo teórico; se é um número mágico, ignorar"* —, o que derruba tanto o default de
  40.000 chars / 10.000 tok da `DX-11` quanto a proposta de 1º `usage` ≤ 25.000 tok, deixa o
  50%/60% da `DX-13` como o único número com proveniência e faz a aferição da `CTX-T10` passar a
  **relativa e sem constante**, contra o antes já registrado. Um achado **com** número ficou fora da
  tabela por `DX-9` e foi para o `## 9. Achados` do plano: o custo de abrir um papel é dominado pela
  **superfície de ferramentas registrada**, não pelo prompt (arquivo do executor = 4.685c = **3,4%**
  dos 34.016 tok de abertura; scout de três ferramentas abre em 8.340) — insumo obrigatório da
  `AUT-T6`/`AUT-T9` do `P-0737`. Bateria de fechamento 5/5 em exit 0, suíte **85 passed**.
  **Desvio declarado:** o dossiê fixava "nenhum outro arquivo", mas a regra dele mesmo manda causa
  sem rota na tabela para o `## 9. Achados` do plano, e o dono ratificou essa colocação no
  round-trip — daí a segunda edição, em `docs/plans/P-0738-contexto-esgotado.md`.
  Consumo: ver `docs/telemetria.tsv`.

- **`CTX-T3` — 2026-08-23 — `done`.** A série saiu do caso e virou número, nos quatro blocos do
  dossiê, publicados em `docs/CUSTO_DO_PICKUP.md` `## 8 A série: custo por papel e custo do
  controle` (38 linhas, dentro do teto de 50). **(1) Custo fixo por papel** — mediana do 1º `usage`
  de janela de subagente por `agentType`: `pantonic-executor` n=149 · 34.016 tok;
  `pantonic-planner` n=15 · 13.980; `pantonic-reviewer` n=1 · 13.995; `pantonic-benchmarker` n=16 ·
  10.352; `context-scout` n=13 · 9.150; `pantonic-scout` n=10 · 8.340 — abrir um papel Opus custa
  ~4× abrir um scout Haiku, **antes de qualquer ato**. **(2) Janelas por tarefa atômica** — pela
  contagem corrigida por dia de execução (a bruta infla por releitura de diário), a `AUT-T5b`
  consome **5** janelas e **não é caso isolado**: `AUT-T1` 8, `RPC-T2`/`RPC-T3` 13 cada, `RPC-T4`
  12, `RPC-T5` 11 — padrão, não exceção. **(3) Os três números do `TK-32`**, como leitura histórica
  do regime anterior (`DX-13`): (i) cruzamentos por classe — `redacao` 13/40, `implementacao` 6/23,
  `mecanica` **3/3**, `investigacao` 1/2, excedente médio ~6,5 por tarefa cruzada; (ii) **0
  ocorrências em 4 arquivos** de a consequência antes prescrita ter disparado em qualquer dos 23
  cruzamentos; (iii) o próprio controle custou **198 tool uses** (n=5). **(4) `TK-23`(b)** — não
  medível só pela série (`telemetria.tsv` não tem coluna de sessão/janela), medível pelos
  transcripts: as 3 janelas da `AUT-T5b` citam **8, 15 e 14** marcadores de tarefa distintos, ou
  seja, várias tarefas atômicas dividem uma janela. Verificação: quatro entregas com número e `n`,
  `## 8` em 38/50 linhas, nenhum arquivo além do alvo tocado (sonda `sonda_janela.py` só no
  scratchpad). **Achado fora de escopo registrado pelo executor:** a função
  `entrega2_janelas_por_tarefa` da `CTX-T2` superestima janelas de tarefa apenas *citada* depois no
  diário; a variante `_v2` (usada aqui) corrige — vale para quem reusar a sonda, e os números
  publicados na `## 7` não dependem dela. **Custo de condução, para a própria matéria do plano:**
  a tarefa consumiu **3 janelas de orquestração** — a 1ª encerrou no gate de delegação por
  capacidade, a 2ª delegou e o subagente caiu por limite de sessão da API (não defeito da tarefa,
  sem nenhuma escrita antes da queda, telemetria `PARCIAL — trecho pré-queda não medido`), a 3ª
  entregou; este fechamento é a 4ª. Consumo: ver `docs/telemetria.tsv`.

- **`CTX-T2` — 2026-08-23 — `review`.** Medido o custo fixo de abrir uma janela de orquestração sem
  agir: primeiro `usage` das 3 janelas da `AUT-T5b` (2026-08-22) em 34.260–45.872 tokens
  (17,1%–22,9% dos 200k nominais) **antes do turno 1**. Atribuição do crescimento até o
  cruzamento de 100k: releitura do mesmo arquivo dentro da própria janela
  (`DIARIO_DE_OBRAS.md`, `_INBOX.md`, `P-0737-loop-autonomo.md`), não ingestão de fonte nova —
  reforça `H1`/`H2` já registradas na `## 4`. Publicado em `docs/CUSTO_DO_PICKUP.md` `## 7
  Anatomia de uma janela de orquestração` (39 linhas; arquivo em 202/320) com as sete métricas
  por janela e o número do primeiro `usage` em destaque; `docs/DOC_MAP.md` corrigido (a entrada
  prometia `## 7 Veredito do dono`, que nunca existiu — a `CPK-T4` ficou sem objeto). Sonda
  (`sonda_janela.py`/`.md`) só no scratchpad, fora do repo. Verificação: script exit 0, agregado
  66/120 linhas, `git status --short` restrito aos dois arquivos-alvo. Nenhum achado fora de
  escopo. Consumo: ver `docs/telemetria.tsv`.

- **`CTX-T1d` — 2026-08-23 — `review`.** A gramática da `DX-15` passou a ser a que o parser da `DP-C`
  fala: `### <ID> — <título> [<modelo> · classe <classe>]`, com ` · teto <N>` histórico **aceito e
  descartado** por segmento opcional e **anônimo** da regex. Remoção de campo, não fluxo novo —
  nenhum passo, ramo, contador ou linha de roteamento nasceu. Em `rdo.py`: o parâmetro/atributo
  `teto` saiu de `DossieTarefa`; `extrair_dossie` perdeu o kwarg `teto_legado`, os **dois** blocos de
  validação `teto != default_teto`, o `("--teto", teto_legado)` da lista `faltando` e o
  `int(teto_legado)` com o erro de "não é inteiro", e a mensagem de plano legado passou a
  **"não declara modelo/classe"**; o CLI perdeu `--teto` e o `help` do `--esquema-legado` foi
  reescrito; a docstring redefiniu legado como **cabeçalho sem colchete algum**; e a entrada
  `"TETO"` saiu do mapping. `_CLASSE_TETO_DEFAULT` **permanece com nome e valores**, com o
  comentário agora declarando o que ele é — o **conjunto normativo de classes** para mensagens de
  erro, cujos números são régua do planejador em `GOVERNANCA.md` §3 e **não são mais lidos por este
  módulo**. `rdo_template.md` perdeu `{{TETO}}` nas duas linhas (identificação e consumo): o número
  **deixa de existir no RDO**, sem derivação substituta. `review_evidence.py` perdeu só o
  `teto_legado=None` — os 22 `teto_diff_chars`/`teto_chars` são homônimo de truncamento e ficaram
  intactos. `classe`, `_CLASSE_ALIASES`, `_normalizar_classe` e `_ID_HEADER_RE` não foram tocados
  (`Q1` aberta; `DX-2`). Testes: fixtures migradas, o teste do erro "teto diferente do default"
  **caiu** com o erro, e **dois novos** cobrem a gramática nova e o cabeçalho histórico com
  ` · teto 40` parseando com o número ignorado e o RDO gerado sem a palavra `Teto`. Verificação em
  exit 0 nos cinco critérios; suíte **85 passed** (piso re-derivado no gate era **83**; subiu pelos
  dois testes novos, não desceu). **Dois achados do gate de delegação, registrados aqui:** (a) a
  linha de verificação do dossiê exigia `Grep "TETO" path:.claude/tools/` **sem retorno**, o que
  contradiz o item 4 do mesmo dossiê (que preserva `_CLASSE_TETO_DEFAULT`, 5 ocorrências medidas) —
  critério **impossível de cumprir como publicado**; prevaleceu o corpo do dossiê e o critério foi
  corrigido para `{{TETO}}`/`"TETO"`, que fecha sem retorno; (b) **~14 sítios de escrita contra o
  limite de 8** do item 5 do gate, **sem partição** — é a remoção de um único campo com acoplamento
  total (tirar `teto_legado` de `extrair_dossie` quebra `review_evidence.py` no mesmo instante;
  tirar `"TETO"` do mapping sem o template deixa `{{TETO}}` literal no RDO), e qualquer partição
  deixaria a suíte vermelha entre as fatias, violando o piso de regressão. Medido e reportado, não
  decomposto (`DP-Q`: teto é alarme, nunca bloqueio). Nenhum achado fora de escopo pelo executor;
  nada escalado ao dono. Consumo: ver `docs/telemetria.tsv`.

- **`CTX-T1c` — 2026-08-22 — `review`.** A `G-SURFACE` fechada no **kit executável**: nenhum artefato
  de fluxo manda mais quem executa parar por número. Na skill `proximo-passo`, o item 5 do gate virou
  **"Decomposição por volume — dimensionamento do planejador (`GOVERNANCA.md` §3), nunca instrução de
  parada a quem executa"**, preservando os dois critérios de decomposição (>8 write-clusters; ≥3
  camadas com padrão sem precedente) e perdendo o `"PARE e reporte ao atingir N"`, o teto por ramo, as
  faixas de tool uses e a série que os sustentava; o item 6 manteve o **método de sondagem prescrito**
  e perdeu o teto numérico por padrão (`DX-15`); e as duas justificativas por "excedente de teto do
  executor" (item 3 do gate, item 1 do escopamento) passaram a se apoiar em **autossuficiência de
  contexto da tarefa**. No `scrum-master`, as seis âncoras: a gramática virou
  `### <ID> — <título> [<modelo> · classe <classe>]` nos dois pontos, com a rota de `B3` justificada
  **só pelo modelo** — sem ele não há como instanciar o executor adequado; a linha do teto de tool
  uses **saiu inteira**; o consumo virou **medida e registro, nunca critério de rota** (`DP-Q`); `B2` e
  "parada legítima" receberam a consequência **não graciosa** (nada produzido depois do sinal de
  poluição se aproveita), sem ramo nem valor novo; e entrou a linha de ponteiro de que o
  `scrum-master` **não revisa plano**. A âncora homônima `A2` (`teto de campo estourado`) não foi
  tocada. No `diario-de-obras`, uma linha sem valor novo: revisão de plano pedida por quem executa ou
  orquestra é `blocked` **de plano**, e a razão tipada da tarefa correspondente é `premissa`. Em
  `ocupacao.py`, só texto — o proxy é **aviso informativo à orquestração entre tarefas** sob §3, com
  `LIMIAR`, hook e `MENSAGEM_AVISO` intactos. Confirmações sem edição: `telemetria.py` sem objeto (0
  matches de `teto|orçamento`), `pantonic-reviewer.md` já conforme. As quatro verificações do dossiê
  conferem — `"PARE e reporte"` sem match no kit, nenhuma das 11 linhas com `teto` prescrevendo número
  a quem executa ou orquestra, as duas linhas de gramática sem ` · teto` — e a suíte em **83 passed**,
  exit 0. **Dois achados apendidos ao `## 9` do plano:** `scrum-master:119` carrega a **sétima**
  ocorrência da justificativa falsa, fora do conjunto fechado de seis âncoras e gêmea exata do item 3
  do gate, com rota nomeada de emenda de uma linha pelo planejador (`CTX-T1d` ou `CTX-T1e`); e
  `MENSAGEM_AVISO` (`ocupacao.py:57`) conserva tom imperativo mais forte que o estatuto novo, vedada
  aqui por ser comportamento de `.py`, com rota na `AUT-T6` do `P-0737`. Nada de passo, ramo, contador,
  status ou razão tipada criado. Consumo: ver `docs/telemetria.tsv`.

- **`CTX-T1b` — 2026-08-22 — `review`.** A superfície de **papéis** reconciliada com a `DX-13`
  (`G-SURFACE`), com a matriz de responsabilidades de `GOVERNANCA.md` §3 como fonte única e os três
  artefatos que a exercem apenas apontando. **Planejamento** / *Responde por* ganha o dimensionamento
  de cada tarefa sob a diretriz de §3 e a **exclusividade da revisão de plano**; **Execução** /
  *Responde por* passa a **executar a tarefa como responsabilidade única** (entrega correta e sinal
  viram o conteúdo dessa responsabilidade, não responsabilidades paralelas) e / *Não faz* ganha
  **não se ocupa de teto nem de orçamento** — nem de turnos nem de contexto — e **não revisa plano**;
  **Orquestração** / *Não faz* ganha **não revisa plano** (roteia a escalada, não replaneja);
  **Revisão** confirmada sem edição. Parágrafo novo **"Escada de revisão de plano"** logo abaixo da
  matriz: quem suspeita marca `blocked` com a razão **`premissa`** já existente, o planejador é o
  único destinatário e decide o técnico-tático, e sobe ao dono o **estratégico ou o que altera
  escopo** — nenhuma sigla nova e nenhuma razão tipada nova. §4 reaponta a linha *Item de backlog* e
  o parágrafo das duas práticas para a diretriz de §3, nomeando o **planejador** como quem dimensiona
  e afirmando que o executor não a observa. No `pantonic-planner.md`, item novo com o dimensionamento
  e a `DX-15` — dimensionamento **exercido, não publicado**, cabeçalho sem teto e `<modelo>`
  justificado pelo consumidor `scrum-master`. No `pantonic-executor.md`, o trecho de orçamento **sai
  inteiro** (a palavra não aparece mais no arquivo); a disciplina de economia de turnos permanece
  requalificada como **método de trabalho, não teto**, e o estouro passa a se registrar no corpo da
  tarefa como insumo do planejador. Na skill `handover`, o checkpoint é rescopado ao **encerramento
  planejado da janela de orquestração** e ganha o bloco **"Dois casos que NÃO são checkpoint"** —
  poluição vira retorno **não gracioso** sem ponteiro de retomada, e contexto acabando dentro de uma
  tarefa vira **sintoma de tarefa mal dimensionada**, devolvido ao planejamento sem retomada parcial
  (o custo dobrado que a `DX-13` proíbe). Mais uma linha no `CHANGELOG.md`. Verificações do dossiê
  conferem: `revisa plano` em `GOVERNANCA.md` sai de **0 para 3** ocorrências, `orçamento` no agente
  executor devolve **nada**, `tolerância` no planner devolve o item novo. Bateria de fechamento em
  exit 0 nos quatro comandos (o `check-drift` não precisou regravar o `.claude/README.md`), suíte
  **83 passed**. Delta de `git status` restrito aos cinco alvos. Nenhum achado fora de escopo.
  Consumo: ver `docs/telemetria.tsv`.

- **`CTX-T1` — 2026-08-22 — `review`.** As duas normas da `DX-13` publicadas como permanentes, cada
  uma na residência da régua de §3.1. **Poluição** é regra final: o bullet *Coesão* da **Regra 2** do
  `.claude/global/CLAUDE.md` passa a exigir parada não graciosa, descarte do que se produziu depois
  do sinal e retorno demandando **contexto limpo para a reexecução**; mesma consequência em texto
  operacional no `GOVERNANCA.md` §4.3 e no guardrail §7 item 7, que passa a enunciar **só** a
  poluição. **Capacidade** deixa de ser regra de execução e vira **diretriz de dimensionamento do
  planejador**, canônica em `GOVERNANCA.md` §3 em subtítulo próprio (três critérios, 50% com
  tolerância a 60%, proveniência na literatura de decaimento por enchimento de contexto e cláusula de
  revisão); §4.3 fica com uma linha de ponteiro declarando que **capacidade nunca interrompe tarefa
  em curso**, e o encerramento planejado de janela é requalificado como ato da orquestração **entre
  tarefas**, com `ocupacao.py` reclassificado de condição de execução para **aviso informativo** (o
  arquivo não foi tocado). Pela `DX-15`, a tabela de classes vira a **única** residência de número de
  teto: a célula *Comportamental* troca "teto por ramo no dossiê" por critério de **partição**, a
  célula *Investigação* deixa no dossiê só o **método de sondagem**, e o `≤50` do replanejamento saiu
  da prosa para linha própria da tabela. Mais uma linha no `CHANGELOG.md` e a linha de ponteiro no
  `P-0737` §3, invariante 5 — registro, sem reabrir aquele plano. **`G-SURFACE` aplicado na mesma
  tarefa:** o achado do executor — a linha de *Motivo* da Regra 2 ainda dizia que duas condições
  encerram um contexto — foi reconciliado dentro da `CTX-T1` em vez de virar tíquete, porque é
  superfície da mesma norma. Bateria de fechamento em exit 0 nos cinco comandos, suíte **83 passed**,
  piso mantido; os três Greps de verificação conferem (`tolerância` só em §3). Nenhum achado fora de
  escopo remanescente. Consumo: ver `docs/telemetria.tsv`.

- **Registro do plano — 2026-08-22.** Autorado em contexto de planejamento a partir da linha
  `P-0738-contexto-esgotado` do `docs/plans/_INBOX.md` (já `[drenado]`). A tensão que o inbox
  atribuiu à autoria — investigação medida antes da rota **e** execução no mesmo plano, sem violar o
  gate de publicação do `G-PLANREADY` item 5 — foi fechada pela **`DX-1`**: três estágios num arquivo
  só, com a `CTX-T5` como charneira que autora o estágio de execução já fechado (precedente da
  `V2C-T6`). Dividir em dois planos foi recusado por custo: um plano novo repagaria o pickup que este
  existe para eliminar. **Nenhuma questão subiu ao dono na autoria** — as decisões que são dele estão
  concentradas na `CTX-T4`, round-trip único, e nenhuma tarefa publicada assume o resultado dela.
  Aplicado no mesmo ato, não repetir: linha do índice encurtada e apontando para o plano
  (`backlog` → `ready`), Diretiva de priorização condensada de 15 para 7 linhas, e as células
  `TK-23`/`TK-32` marcadas como absorvidas por este plano. Dois achados colhidos na autoria, já
  embutidos nos dossiês e não usados como premissa: o `docs/DOC_MAP.md` promete uma seção
  `## 7 Veredito do dono` em `docs/CUSTO_DO_PICKUP.md` que não existe (a `CPK-T4` ficou sem objeto),
  corrigido pela `CTX-T2`; e o hook de ocupação **está** registrado no `.claude/settings.json` —
  a hipótese de hook ausente caiu na verificação. Consumo: ver `docs/telemetria.tsv`.
- **Revisão do plano por adendo do dono — 2026-08-22.** Decisão do dono chegada **depois** da autoria
  e **antes** de a `CTX-T1` ser executada, registrada como **`DX-13`**: o enunciado único que a
  `CTX-T1` publicaria fundia duas regras de naturezas diferentes, e elas se separam — **poluição** é
  regra **final** (vale 100% do tempo, parada não graciosa, nada se aproveita depois do sinal,
  reexecução em contexto limpo); **capacidade** deixa de ser regra de execução e de guardrail e vira
  **diretriz do planejador** para dimensionar tarefa (coesa, autossuficiente em contexto, ~50% de
  ocupação com tolerância a 60%, número com proveniência na literatura de decaimento de desempenho
  por enchimento de contexto e **revisável**). Decorrem: teto e orçamento **saem** do horizonte do
  executor, cuja única responsabilidade é executar; estouro se **registra no corpo da tarefa** como
  insumo de revisão do plano e de eventual reexecução; e **nem executor nem `scrum-master` revisam
  plano** — indício de revisão leva o plano a `blocked` e escala ao **planejador**, que decide o
  técnico e o tático e sobe ao dono o estratégico ou o que altere escopo. Fato medido que motivou o
  adendo: a regra de capacidade vinha interrompendo tarefas à força, com retomada parcial em contexto
  novo e **custo fixo pago em dobro** — o defeito que este plano existe para eliminar. As residências
  e o que o adendo arrasta de superfície estão na **`DX-14`**: a varredura achou **20 pontos de
  contato**, distribuídos entre a `CTX-T1` (doutrina canônica, reescrita), a nova **`CTX-T1b`**
  (matriz de responsabilidades, `pantonic-planner`, `pantonic-executor`, `handover`) e a nova
  **`CTX-T1c`** (`proximo-passo`, `scrum-master`, `diario-de-obras`, `ocupacao.py`, mais quatro
  confirmações sem edição). Reconciliadas no mesmo ato, não repetir: invariante 1 do §3 do plano,
  metade normativa do diagnóstico `(i)` do §0, entrega 3 da `CTX-T3` (passa a leitura histórica),
  round-trip da `CTX-T4` (o que a `DX-13` já decidiu **não** volta ao dono) e regra 8 da charneira
  `CTX-T5` (dimensiona os cards do Estágio C sob a diretriz). **Nenhuma questão subiu ao dono**: as
  duas consequências candidatas a estratégicas — o `LIMIAR` de `ocupacao.py` e o roteamento do
  retorno de poluição — foram resolvidas por `manter` e por encaminhamento ao `P-0737` (`DX-9`).
  Consumo: ver `docs/telemetria.tsv`.
- **Segunda revisão por decisão do dono — 2026-08-22.** Decisão chegada logo depois da `DX-13`/`DX-14`
  e ainda antes de qualquer tarefa executar, registrada como **`DX-15`**: **o campo `teto` cai do
  cabeçalho de tarefa**. Palavra do dono — *"todas as tarefas respeitarão a regra de contexto,
  aplicável apenas ao planejador no dimensionamento de escopo; como somente o planejador tem
  autoridade para revisar o escopo, uma informação de teto é poluição"*. A `DX-15` **revoga**, com
  marca datada e sem apagar o texto anterior, a parte do **item 5 da `DX-14`** que mantinha o campo
  com o nome que tem, apenas mudando de destinatário: ele não muda de destinatário, **deixa de
  existir**. **`Modelo` fica**, e agora com consumidor nomeado pelo dono — é por ele que o
  `scrum-master` instancia o executor adequado. **Gramática nova, decidida pelo planejamento:**
  `### <ID> — <título> [<modelo> · classe <classe>]`; o segmento ` · teto <N>` vira **opcional e
  descartado** na regex do `rdo.py`, de modo que nenhum plano fechado se reescreve e o `P-0737`
  (`blocked`) não se toca; só os **9 cabeçalhos do próprio `P-0738`** migraram, no ato. Confirmação
  medida que fechou o mérito: o campo já era **redundante** — `rdo.py` recusava qualquer teto
  diferente do default da classe. Consequência de `G-SURFACE`: os 20 pontos da `DX-14` **mudaram de
  natureza** (de "reendereçar ao planejador" para **deleção**) e foram reconciliados nos dossiês da
  `CTX-T1` (duas células da tabela de classes de `GOVERNANCA.md` §3 que prescreviam teto "no
  dossiê"), `CTX-T1b` (o planejador **exerce** o dimensionamento, não o publica), `CTX-T1c` (o
  `scrum-master` passa de quatro para **seis** âncoras, com as duas linhas de gramática) e `CTX-T5`
  (regra 1 e regra 8 da charneira); a varredura complementar acrescentou os **instrumentos**, que
  saíram das "confirmações sem edição" e viraram a tarefa nova **`CTX-T1d`** (`rdo.py`,
  `rdo_template.md`, `review_evidence.py` e os dois arquivos de teste). **Uma questão subiu ao dono**,
  a primeira deste plano: **`Q1` — que informação o campo `classe` carrega**, aberta pelo próprio dono;
  o levantamento por Grep confirmou que a `classe` era lida **só** para localizar o teto, e que quem
  roteia o executor é o `Modelo` — caindo o teto, ela perde o único consumidor funcional. Três
  destinos com custo estão no bloco `## Questões ao dono` do plano (cair · sobreviver como rótulo com
  consumidor declarado · função nova, que é `DX-9`); enquanto a questão correr, **`classe` fica
  congelada como está** e nenhuma tarefa publicada depende do desfecho — o plano segue fechado pelo
  `G-PLANREADY` item 5. Achado registrado na `## 9` do plano, sem virar tarefa: `rdo.py` **não
  localiza identificador prefixado** (`CTX-T*`, `AUT-T*`) por causa de `_ID_HEADER_RE` — defeito
  pré-existente, nunca exercitado, encaminhado à `AUT-T4` do `P-0737`. Consumo: ver
  `docs/telemetria.tsv`.

---

## P-0739 — O pickup vira instrumento

- 2026-09-19 — **Fila corrente:** **`P-0740` FECHADO em 35/35, marco 3 commitado em `13ce6a3` (2026-09-19).** Janela de 2026-09-19 (a terceira do dia): **quinze tarefas fechadas, zero reprovações, zero retentativas consumidas**, três devoluções `blocked` razão `premissa` todas por conduta correta de `G-EXECREADY` (nenhum arquivo tocado em nenhuma). Consumo da janela: **6.729,2k tk / 819 tool uses / 3,54 h** em 41 linhas de `docs/telemetria.tsv` — execução 19%, revisão 15%, **consultor 67%**. Suíte **187 → 201**; `tests/test_backlog.py` 41 → 49. Achados `AE-47`..`AE-75`; escalonamentos `ESC-27`..`ESC-40`, **catorze, todos ao consultor instanciado uma vez, nenhum ao dono**. **PRÓXIMA JANELA: retomada do `P-0739`**, sob a *Diretiva de execução do `P-0739`* acima (dono, 2026-09-19). **Primeira tarefa: transcrever os três módulos `BKL-T10`..`BKL-T12`** em `docs/plans/P-0739-backlog-instrumento.md` — a partição, o mapa de herança das superfícies mortas e a regra de re-derivação do número **já estão decididos e registrados** pela `LM-T5a` (`AE-63`, `AE-65`, `AE-67`): `BKL-T10` absorve `BKL-T5` (`drain`) + `BKL-T6` (migração), `BKL-T11` absorve `BKL-T7` (hook) + `BKL-T8` (skills), `BKL-T12` absorve `BKL-T9` sozinha; ordem `BKL-T10` → `BKL-T11` → `BKL-T12`. Os cinco cards antigos ficam no arquivo como `cancelled` **por absorção** (autoridade: `AE-13` do `P-0739`, com o produto (c) da `LM-T5a` do `P-0740`; a citação anterior a `DM-33` (iii) era ponteiro quebrado — o `DM-33` trata de teste pré-existente, e a correção está registrada no `AE-14` (ii) do `P-0739`), nada se apaga. **Herança já decidida:** `passagem-de-bastao` herda a matéria de skill da `BKL-T8` (as skills `proximo-passo` e `handover` foram removidas pela `LM-T4` em `f1afbd3`); o `scrum-master` fica com a condução do loop; o número `≥ 3` do aceite herdado **não se transcreve** — escreve-se a regra (*toda skill que invoca o instrumento o cita*) e re-deriva-se no despacho (mede **1** em 2026-09-19). **`AE-10` encerrado** pelo reparo `AE-47`: a dependência de ordem que ele nomeava deixou de existir quando `transacionar_status` ganhou a guarda que declara a ausência dos marcadores em vez de estourar. **Estado medido do `P-0739` em 2026-09-19:** `11/16` — `ready 5` (`BKL-T5`..`BKL-T9`), `done 11`, e a nota `AE-13` **da série local do `P-0739`** (as séries `AE-<n>` são **por plano**; citação de achado de outro plano leva sempre o qualificador `AE-<n>` **do** `<plano>` — `AE-67`). **Números de aceite a re-derivar no despacho:** suíte **201 passed**, `tests/test_backlog.py` **49**, `- **Objetivo:**` no `P-0739` **18**. **Recorte de evidência da próxima rodada: `--desde 13ce6a3`** (as quinze entregas do marco 3 foram commitadas ali; o recorte volta a tamanho proporcional à entrega). **Matéria pós-plano, sem card e sem rodada:** o `TK-55` acumulou seis evidências novas nesta janela e é o acumulador da **spec de robustez**; o teto de saturação do `AE-60`/`AE-63` cobre `.claude/checks/check-readme.ps1`, `docs/RUBRICA_DE_REVISAO.md` e `.claude/tools/review_evidence.py`; o teto prospectivo do `AE-74` fecha `docs/consultant-spec.md` — **achado novo sobre esses arquivos não abre card**, registra-se e vai à spec correspondente. **Fila corrente anterior (texto do marco 2, 2026-09-19):** migra para `## P-0740` na condensação.
- `P-0739` (`in-progress`, 11/16): `RP-2` fechou em 2026-09-16 (`pantonic-planner`, sobre o `AE-2`) — decisão técnica/tática, não escalada: `DB-21..DB-24` em `docs/plans/P-0739-backlog-instrumento.md` §1, rota = corrigir a gramática de ID em `rdo.py` (`_ID_HEADER_RE`/`_HEADER_BRACKET_RE`, ponto único) mais regressão em `tests/test_rdo.py`, sem retroação e sem tocar `P-0737`. Card novo `BKL-T2a` (`ready`, próxima tarefa). `BKL-T2` passou de `blocked` para `review` (entrega verde; `review` porque a rodada de revisão do `pantonic-reviewer` só roda depois que `BKL-T2a` destravar o dossiê de evidência — quem leva a `done` é o `scrum-master`). Pendência de doutrina **resolvida em 2026-09-16, por ordem do dono**: a lição da `RP-2` foi aplicada em `.claude/agents/pantonic-planner.md` fase 1 (último bullet: plano que introduz convenção de ID/caminho/nome de artefato verifica na fase 1 que os instrumentos do gate de aceite a aceitam; se não aceitam, corrigir o instrumento é tarefa do plano), com linha em `CHANGELOG.md` sob `## [Não lançado]`. Registro da pendência original (texto no parágrafo "Lição para o planejador" de `docs/plans/P-0739-backlog-instrumento.md`, seção `### RP-2`) — só o dono altera arquivo de definição de agente. Consumo: ver `docs/telemetria.tsv` (`BKL-RP2`). Revisão crítica do procedimento desta janela (7 achados, insumo §7.1): `docs/plans/_CARD-revisao-critica-pickup-opus.md`. **`BKL-T2a` entregue em 2026-09-16** (`pantonic-executor`, `review`): `_ID_HEADER_RE`/`_HEADER_BRACKET_RE` de `.claude/tools/rdo.py` passam a aceitar ID prefixado (`(?:[A-Z0-9]+-)?T[0-9]+[a-z]?`) e bracket com ` + dono`; 4 testes novos em `tests/test_rdo.py`, suíte `98 passed`, `review_evidence.py --tarefa BKL-T2` sai `OK` — o `AE-2` está fechado e a rodada de revisão da `BKL-T2`+`BKL-T2a` é a próxima tarefa. Entrega não commitada: `.claude/tools/rdo.py`, `tests/test_rdo.py`, `CHANGELOG.md`. Consumo: ver `docs/telemetria.tsv` (`BKL-T2a`). **Rodada de revisão fechada em 2026-09-16** (`pantonic-reviewer`, um laudo por tarefa): `BKL-T2` → `done` com **ressalva** (94%, bloqueante nenhuma, única dimensão fora de `conforme`: `registro` `parcial`; laudo `docs/RDO/laudos/P-0739-BKL-T2.md`) e `BKL-T2a` → `done` **aprovado** (100%, bloqueante nenhuma; laudo `docs/RDO/laudos/P-0739-BKL-T2a.md`). Evidência mecânica verde nas duas (`guardas` e `testes` `conforme`), recorte por base distinta — `--desde 1a9645a` para a `BKL-T2` (entrega já em `6d7433c`) e `--desde 6d7433c` para a `BKL-T2a` (árvore de trabalho); dossiês em `docs/RDO/evidencia/`. Os dois laudos escalaram o **mesmo achado de processo**, registrado como `AE-3` (`docs/plans/P-0739-backlog-instrumento.md:729-767`), sem retroação sobre as entregas: a rodada `RP-3` é a próxima tarefa. Consumo: ver `docs/telemetria.tsv` (`BKL-T2-revisao`, `BKL-T2a-revisao`). **Rodada `RP-3` fechada em 2026-09-16** (`pantonic-planner`, sobre o `AE-3`) — decisão técnica/tática, **nada escalado ao dono**: `DB-25`..`DB-29` em `docs/plans/P-0739-backlog-instrumento.md` §1 (linhas 52-84), rodada em `docs/plans/P-0739-backlog-instrumento.md:1394-1466`, `AE-3` absorvido. Rotas: (1) atribuição de arquivo a tarefa é **do instrumento**, não doutrina — `review_evidence.py` classifica cada arquivo tocado em 4 baldes (alvo do card · alvo de outra tarefa do mesmo plano · registro da orquestração, lista fechada · fora sem atribuição) e só o último pesa no veredito (`DB-25`); commit isolado por tarefa descartado porque o registro da orquestração é escrito depois da entrega e antes da revisão; (2) forma canônica de `Arquivos-alvo` fixada — um caminho por bullet, nenhum outro caminho entre crases (`DB-26`), com leitura mecânica **por literal, não por linha** (`DB-27`, fato que manda: `rdo.py:151-183` junta as linhas do campo com espaço); a migração dos cards vivos foi feita na própria autoria (`BKL-T8` reescrito, `BKL-T9` com `Arquivos-alvo` reposto — estava ausente e `extrair_dossie` recusaria a tarefa); (3) `rdo.py laudo` ganha `--achado-processo <alvo> "<linha>"` (alvos `dossie`|`doutrina`|`rubrica`) fora de `calcular_laudo`, devolvendo `--escalar` a só pendência de arquitetura/requisito (`DB-28`); (4) a observação de card do laudo da `BKL-T2` virou regra de autoria (`DB-29`): `Pronto quando`/`Verificação` só citam efeito nos arquivos-alvo do card e comandos do executor; (5) o `UnicodeEncodeError` de `stdout` cp1252 entrou como `_forcar_utf8` no card `BKL-T2b` (o `→` que a `BKL-T2c` imprime depende dele — daí a ordem). Três cards novos `ready`: `BKL-T2b` (`docs/plans/P-0739-backlog-instrumento.md:407-584`), `BKL-T2c` (`:585-834`), `BKL-T2d` (`:835-994`); ordem `BKL-T2b` → `BKL-T2c` → `BKL-T2d` → `BKL-T3`; §6 riscos com 4 linhas novas. **Pendência que é ato do dono, não decisão** (mesmo precedente da `RP-1`/`RP-2`): publicar em `.claude/agents/pantonic-planner.md` as três lições da `RP-3` — fase 1, instrumento de gate cuja saída nunca foi inspecionada contra corpus real; fase 4, campo de card lido por máquina autorado como prosa; fase 4, critério de pronto sem poder discriminante. O `P-0739` **não** depende dessa edição: os três cards estão despacháveis desde já. Consumo: ver `docs/telemetria.tsv` (`BKL-RP3`). **`BKL-T2b` entregue em 2026-09-16** (`pantonic-executor`, `review`): `extrair_arquivos_alvo` de `.claude/tools/review_evidence.py` passa a ler o campo por **gramática de caminho** (`DB-27`) — `_eh_caminho` + `_classificar_campo_alvos`, com `extrair_literais_nao_caminho` alimentando a linha "Literais não reconhecidos como caminho" da seção `## Escopo`, e `_forcar_utf8` em `stdout`/`stderr` no `main`. Arquivo de raiz (`CHANGELOG.md`) volta a ser alvo e literal de regex deixa de ser; 4 testes novos em `tests/test_review_evidence.py` (`13 passed` → `17 passed`), suíte `102 passed` (piso 98), nenhuma contingência acionada. Entrega não commitada: `.claude/tools/review_evidence.py`, `tests/test_review_evidence.py`, `CHANGELOG.md`. Consumo: ver `docs/telemetria.tsv` (`BKL-T2b`). **Correção de registro no mesmo ato:** os campos `**Status:**` de `BKL-T2` e `BKL-T2a` no plano ainda diziam `review` depois da rodada de revisão ter fechado as duas como `done` — divergência entre a residência do item e a projeção do índice (`DB-2`), corrigida com o veredito e o ponteiro do laudo de cada uma. **`BKL-T2c` entregue em 2026-09-16** (`pantonic-executor`, `review`): `confrontar_escopo` de `.claude/tools/review_evidence.py` passa a classificar o arquivo tocado nos quatro baldes da `DB-25` (coberto pelos alvos do card · alvo de outra tarefa do mesmo plano · registro da orquestração · fora sem atribuição), com `_REGISTRO_ORQUESTRACAO` + `_eh_registro_orquestracao` e `mapear_alvos_de_outras_tarefas` lendo a gramática de ID por `rdo._ID_HEADER_RE` (residência única, `DB-22`); só o quarto balde resolve o veredito, e a seção `## Escopo` nomeia os outros dois baldes em linha própria. 4 testes novos em `tests/test_review_evidence.py` (`17 passed` → `21 passed`), suíte `106 passed` (piso 102 preservado). **Contingência 2 do card acionada** (prevista no dossiê, não é desvio): `test_escopo_violado_gera_fato_sem_inventar_parcial` quebrou porque a frase do fato virou "fora dos alvos e sem atribuição" — só essa asserção foi ajustada. Entrega não commitada: `.claude/tools/review_evidence.py`, `tests/test_review_evidence.py`, `CHANGELOG.md`. Consumo: ver `docs/telemetria.tsv` (`BKL-T2c`). **Âncoras do card re-derivadas no despacho** (fato de orquestração a reaproveitar na `BKL-T2d`, não achado de execução): os números de linha que a `RP-3` escreveu nos cards de instrumento envelheceram dentro da própria sprint — o card da `BKL-T2c` apontava `review_evidence.py:172-197`/`:360-368`/`:420` e os blocos reais estavam em `:214-239`/`:409-417`/`:470`, deslocados pela entrega não commitada da `BKL-T2b`; o item 3 do gate de delegação pegou antes do despacho e o dossiê seguiu com âncora fresca, sem acionar contingência `premissa`. **Rodada de revisão de `BKL-T2b`+`BKL-T2c` fechada em 2026-09-16** (`pantonic-reviewer`, um laudo por tarefa, mesmo protocolo da rodada anterior): as duas **aprovadas 100%**, bloqueante nenhuma, as sete dimensões `conforme` em ambas — `BKL-T2b` → `done` (laudo `docs/RDO/laudos/P-0739-BKL-T2b.md`) e `BKL-T2c` → `done` (laudo `docs/RDO/laudos/P-0739-BKL-T2c.md`). Evidência mecânica verde nas duas (`guardas` e `testes` `conforme`, bateria de 6 guardas toda exit 0), recorte `--desde 6d7433c` para ambas — as entregas estão todas não commitadas sobre `HEAD`, e quem as separou foi a atribuição por tarefa que a própria `BKL-T2c` instalou (`DB-25`): dossiês em `docs/RDO/evidencia/P-0739-BKL-T2b.md` e `...-BKL-T2c.md`. A contingência 2 acionada na `BKL-T2c` estava prevista no card, logo `rota` `conforme`. **Nada escalado ao dono** (sem `--escalar`: nenhuma pendência de arquitetura ou requisito). Os dois laudos escalaram achados de processo convergentes, registrados como `AE-4` (`docs/plans/P-0739-backlog-instrumento.md:1483-1513`), sem retroação sobre as entregas: residência do registro de contingência acionada, e a falta de balde para ato do dono no confronto de escopo (reincidente — já observado no laudo da `BKL-T2a`). A rodada `RP-4` é o próximo passo recomendado; ela não bloqueia a `BKL-T2d`. Consumo: ver `docs/telemetria.tsv` (`BKL-T2bc-revisao` — uma linha, porque a rodada foi um único despacho cobrindo as duas tarefas). **Rodada `RP-4` fechada em 2026-09-16** (`pantonic-planner`, sobre o `AE-4`) — decisão técnica/tática, **nada escalado ao dono**: `DB-30`..`DB-32` em `docs/plans/P-0739-backlog-instrumento.md` §1 (linhas 85-87), rodada em `docs/plans/P-0739-backlog-instrumento.md:1717`-fim, `AE-4` absorvido (`:1711-1712`). Veredito por defeito: (1) **residência do registro de contingência acionada — não gera tarefa** (`DB-30`/`DB-31`): contingência acionada volta na linha de retorno da entrega (`contingência <n> acionada: <o que mudou>`) e é a **orquestração** que a materializa na linha `- **Status:**` do card; os três canais já existiam (`DB-15`, `DB-16`, `--nota` da `BKL-T4`), então nenhum artefato novo — rotas descartadas: artefato "nota de execução" próprio, executor escrevendo a linha `Status`, diff como registro; (2) **balde do ato do dono — gera tarefa** (`DB-32`): card novo `BKL-T2e` (`ready`, `docs/plans/P-0739-backlog-instrumento.md:1020-1205`), quinto balde em `review_evidence.py` para arquivo tocado por ato do dono fora do ciclo da tarefa — rotas descartadas: manter a atribuição externa como insumo do despacho, jogar `.claude/agents/` dentro de `_REGISTRO_ORQUESTRACAO`, branch/stash do dono, filtro por autoria do `git`; nada da entrega da `BKL-T2c` é desfeito. Card `BKL-T2d` ajustado (`Depende de` em `:859-861`; duas contingências na forma da `DB-30` em `:1000-1006`) e **segue despachável, sem depender da `BKL-T2e`**; cabeçalho do plano em 14 tarefas com a ordem `BKL-T2d` → `BKL-T2e` → `BKL-T3` (`:4-19`); §6 riscos com três linhas novas (`:1338-1340`). **Pendência que é ato do dono, não decisão** (mesmo precedente da `RP-1`/`RP-2`/`RP-3`): publicar em `.claude/agents/pantonic-planner.md` as duas lições da `RP-4` (`docs/plans/P-0739-backlog-instrumento.md:1776`) — classe nova *ação de contingência sem residência nomeada* (fase 4, item 3) e reforço de *classificação de vocabulário fechado sem destino para toda forma do inventário* (fase 4, item 7); somam-se às três da `RP-3` (`:1655`) na mesma superfície, numa única edição. O `P-0739` **não** depende dela. Consumo: ver `docs/telemetria.tsv` (`BKL-RP4`). **`BKL-T2d` entregue em 2026-09-16** (`pantonic-executor`, `review`): `rdo.py laudo` ganha `--achado-processo <alvo> "<linha>"` (repetível; alvos `dossie`|`doutrina`|`rubrica`) gravando a seção `## Achado de processo` fora de `calcular_laudo` — percentual, veredito, bloqueante e recomendação intactos (invariante 1 da `RUBRICA_DE_REVISAO.md` §6), com `_ALVOS_ACHADO`/`_formatar_achados_processo`, validação de alvo/linha vazia/`|` em `cmd_laudo` e a seção existindo sempre (`nenhum` sem a flag); `--escalar` volta a ser só pendência de arquitetura ou de requisito (`DB-28`). 4 testes novos em `tests/test_rdo.py` (`38 passed`), suíte `110 passed` (piso 106), **nenhuma das quatro contingências acionada** e nenhuma asserção pré-existente ajustada. Entrega não commitada: `.claude/tools/rdo.py`, `tests/test_rdo.py`, `CHANGELOG.md`. Âncoras do card re-derivadas no despacho e **sem deriva desta vez** (`rdo.py:24`, `:450-488`, `:698-705` idênticas ao literal transcrito pela `RP-3`) — a `BKL-T2d` não tocava os arquivos que a entrega não commitada da `BKL-T2b`/`BKL-T2c` deslocou. Achado da execução registrado como `AE-5` (`docs/plans/P-0739-backlog-instrumento.md:1802-1825`), sem retroação: a Verificação 3 do card afirma estado da **árvore inteira** (`git status --short` → exatamente três caminhos) e a própria sprint torna isso insatisfazível — contraria a `DB-29` do mesmo plano, e a forma correta (recorte por pathspec) já está no card da `BKL-T2e`, autorado pela `RP-4`; cards vivos ainda com a forma velha: `BKL-T3` e `BKL-T4`. Consumo: ver `docs/telemetria.tsv` (`BKL-T2d`). **Rodada de revisão de `BKL-T2d` fechada em 2026-09-17** (`pantonic-reviewer`, mesmo protocolo): **aprovada 100%**, bloqueante nenhuma, as sete dimensões `conforme` — `BKL-T2d` → `done` (RDO `docs/RDO/P-0739-BKL-T2d-rdo-py-laudo-o-campo-de-achado-de-processo-com-os-tres-alvos.md`; laudo consumido e apagado, `DP-H`). Evidência mecânica verde (`docs/RDO/evidencia/P-0739-BKL-T2d.md`, `--desde 6d7433c`). **Nada escalado ao dono:** o achado de processo do laudo repete o mesmo fato já registrado como `AE-5` (Verificação 3 do card não discrimina estado alheio na árvore compartilhada), com rota já aberta ali (emenda de `BKL-T3`/`BKL-T4`) — sem ação nova, sem retroação (`DB-23`). Consumo: ver `docs/telemetria.tsv` (`BKL-T2d-revisao`). **`BKL-T2e` entregue e revisada em 2026-09-17** (`pantonic-executor` → `pantonic-reviewer`, mesmo protocolo): os seis textos literais do quinto balde (`ato do dono`, `.claude/agents/`) aplicados em `.claude/tools/review_evidence.py` ao pé da letra, 4 testes novos em `tests/test_review_evidence.py` (`21 passed` → `25 passed`), suíte inteira `114 passed` (piso 110), nenhuma contingência acionada. Dossiê de evidência (`docs/RDO/evidencia/P-0739-BKL-T2e.md`, `--desde 6d7433c`) com `guardas`/`testes`/`escopo` `conforme` — `.claude/agents/pantonic-planner.md` sai nomeado no balde novo `ato do dono`, sem peso no veredito mecânico, fechando o caso real que motivou a `DB-32`. Laudo **aprovado 100%**, bloqueante nenhuma, sete dimensões `conforme` → `BKL-T2e` → `done` (RDO `docs/RDO/P-0739-BKL-T2e-review-evidence-py-o-balde-do-ato-do-dono-no-confronto-de-es.md`; laudo consumido e apagado, `DP-H`). **Nada escalado ao dono:** único achado é um nit de precisão sem rota e sem efeito em dimensão (docstring do módulo credita os cinco baldes à `DB-25`; o quinto é da `DB-32`), registrado no laudo. Consumo: ver `docs/telemetria.tsv` (`BKL-T2e`, `BKL-T2e-revisao`). **Janela encerrada por ocupação de contexto (`B2`, `GOVERNANCA.md` §4.3)** logo após o fechamento — `BKL-T3` segue `ready` e delegável, não despachada nesta janela. **`BKL-T3` despachada e devolvida defeituosa em 2026-09-17** (`pantonic-executor`, `blocked` razão `premissa`): a triagem parou no primeiro sinal e **nenhuma linha** de `.claude/tools/backlog.py` ou `tests/test_backlog.py` foi tocada — §2.6 fixa uma única linha de contexto do pai, com rótulo literal `plano:` e campos `P-NNNN`/`<done>/<total>`, mas §2.5 regra 4 faixa (b) faz vencer subtarefa de **tíquete**, e o TF obrigatório "bug antes de FIFO" do card só é satisfazível instanciando esse caso; quatro formas candidatas levantadas sem preferência, a escolha é do planejador. Registrado como `AE-6` (`docs/plans/P-0739-backlog-instrumento.md:1833-1865`), **nada escalado ao dono** (forma de saída de instrumento interno, não é arquitetura nem requisito). Âncoras do card re-derivadas no despacho e **sem deriva** (`backlog.py` intocado pelas entregas da `BKL-T2b`..`BKL-T2e`), números de aceite re-medidos na janela (`tests/test_backlog.py` `8 passed`, suíte `114 passed`). A rodada `RP-5` (`pantonic-planner`) é a próxima tarefa e absorve, sem custo de decisão, a emenda mecânica pendente do `AE-5` — que incide nos mesmos dois cards vivos (`BKL-T3`, `BKL-T4`). Consumo: ver `docs/telemetria.tsv` (`BKL-T3-devolvida`). **Rodada `RP-5` fechada em 2026-09-17** (`pantonic-planner`, sobre o `AE-6`) — decisão técnica/tática, **nada escalado ao dono**: `DB-33`..`DB-36` em `docs/plans/P-0739-backlog-instrumento.md:93-96`, rodada em `:2060-2135`, `AE-6` absorvido (`:2053-2058`). Rota escolhida para §2.6: a alternativa (1) do `AE-6` — mesmo conjunto de campos, **rótulo escolhido pelo tipo de pai** (`plano:` / `tíquete:`), porque §2.1/§2.2 já garantem título, residência, âncora de índice e par `<done>/<total>` também para tíquete e nenhum campo precisa de substituto; as outras três alternativas e mais duas variantes foram despachadas com motivo na `DB-33`. §2.6 reescrita (`:177-249`) com esqueleto, duas formas da linha 2, tabela campo a campo (sem remissão, `DB-18`) e dois worked examples (pai-plano com antecessora; pai-tíquete sem ela). **Vãos vizinhos fechados no mesmo ato**, sem os quais a `BKL-T3` pararia de novo: §2.3 (`:133-152`, um bullet por pai, token `P-NNNN` ou `TK-<n>`), §2.5 regra 4 (`:169-176`, três faixas sobre **itens elegíveis**; a faixa de bug casa `Tipo: bug` do próprio card ou do tíquete-pai; FIFO pela linha do pai no índice) e §3 (`:266-270`, fórmula única do par). `BKL-T3` reaberta `ready` (`:1296-1369`) com `Restrições desta tarefa`, `Não fazer`, quatro contingências fechadas e cinco testes novos; `BKL-T4` **também** precisava de emenda (`:1371-1407`) — o bullet do bloco `Fila corrente` carregava o mesmo vício, e o `Pronto quando` perdeu o "`check` verde", que depende da migração da `BKL-T6` (`DB-29`). **Nenhum card novo:** o plano segue com 14 tarefas e nada fechado foi reaberto (`DB-23`). **Correção de registro no mesmo ato:** a premissa do `AE-5` sobre *quais* cards vivos carregavam a `Verificação` por árvore inteira estava **errada** — `BKL-T3` e `BKL-T4` nunca a tiveram (as duas verificavam só `pytest verde`); os cards vivos afetados eram a `BKL-T6` e a `BKL-T9`, agora ambas por pathspec (`:1424-1430`, `:1489-1494`), com a correção apensada ao próprio `AE-5` (`:2004-2016`). O fato foi medido pela **orquestração** no gate de delegação (grep das 11 ocorrências de `git status --short`, conferidas uma a uma) e descarregado no dossiê antes do despacho, pelo item 2 do gate — a rodada não gastou contexto redescobrindo, e o achado de execução se confirmou como **indício**, não como fato apurado. **Pendência que é ato do dono, não decisão** (precedente `RP-1`/`RP-2`/`RP-3`/`RP-4`): publicar as três lições da `RP-5` em `.claude/agents/pantonic-planner.md`, com linha em `CHANGELOG.md`; o `P-0739` **não** depende dela. Consumo: ver `docs/telemetria.tsv` (`BKL-RP5`). **`BKL-T3` entregue e revisada em 2026-09-17** (`pantonic-executor` → `pantonic-reviewer`, mesmo protocolo): o verbo somente-leitura `next` implementado em `.claude/tools/backlog.py` — `selecionar_next` (§2.5, regras 1-5), `renderizar_next` (§2.6: formas pai-plano e pai-tíquete da `DB-33`, linha `antecessora` da `DB-34`, par `<done>/<total>` da `DB-36`), dataclasses `Candidato`/`SelecaoNext`, subcomando CLI `next`, mais os campos de suporte `Item.campo_tipo`, `LinhaIndice.ancora`, `Modelo.diario_linhas`/`diretiva_ids`. 13 testes novos em `tests/test_backlog.py` (`8 passed` → `21 passed`), suíte inteira `127 passed` (piso 114) e duas fixtures novas em disco (`tests/fixtures/backlog/next_tk90/` e `...next_tk90_sem_indice/`), **nenhuma contingência acionada**. Dossiê de evidência (`docs/RDO/evidencia/P-0739-BKL-T3.md`, `--desde 6d7433c`) com `guardas`/`testes`/`escopo` `conforme` — o balde `ato do dono` da `BKL-T2e` absorveu `.claude/agents/pantonic-planner.md` e os baldes de outra tarefa absorveram as entregas não commitadas das `BKL-T2a`..`BKL-T2e`, deixando o quarto balde vazio. Laudo **ressalva 94%**, bloqueante nenhuma, seis dimensões `conforme` e `rota` `parcial` → `BKL-T3` → `done` (RDO `docs/RDO/P-0739-BKL-T3-next-a-selecao-deterministica.md`; laudo consumido e apagado, `DP-H`). **Nada escalado ao dono:** os três achados de processo são alvo `dossiê`, registrados como `AE-7` (`docs/plans/P-0739-backlog-instrumento.md:2172-2215`), sem retroação sobre a entrega (`DB-23`) — e quem moveu `rota` foi o achado 3 (rodapé de §2.6 sem TF discriminante, com desvio medido no contador do inbox de planos), não o achado 1 que o executor relatou. A rodada `RP-6` é a próxima tarefa e vem **antes** da `BKL-T4`. Consumo: ver `docs/telemetria.tsv` (`BKL-T3`, `BKL-T3-revisao`). **Pendência de doutrina das `RP-3`/`RP-4`/`RP-5` encerrada em 2026-09-17, por ordem do dono** ("publicar é consequência do plano, não pergunta — o plano foi iniciado exatamente para modificar"): as lições da `RP-3` e da `RP-4` já estavam em `.claude/agents/pantonic-planner.md` (fase 1 saída real do instrumento de gate; fase 4 itens 2, 3, 7 e 9), e as três da `RP-5` foram publicadas no mesmo ato — fase 4 item 7 (worked example por caso que as regras do próprio plano admitem), fase 4 item 4 (coerência entre decisões do mesmo plano) e passo 1 da rodada de replanejamento (fato de achado é indício, re-derivar por busca antes de emendar) —, com a linha correspondente em `CHANGELOG.md` sob `## [Não lançado]`. `kit_check -Mode validate` e `check-readme.ps1` exit 0 depois da edição. **Rodada `RP-6` fechada em 2026-09-18** (`pantonic-planner`, sobre o `AE-7`) — decisão técnica/tática, **nada escalado ao dono**: `DB-37`..`DB-39` em `docs/plans/P-0739-backlog-instrumento.md:101-103`, rodada em `:2477-2564`, `AE-7` absorvido (`:2416-2476`). Rotas, por achado: (1) a lista de condições de exit 3 de `next` passa a ter **três** condições (`E-1`/`E-2`/`E-3`), cada uma com substring obrigatória de mensagem e fronteira explícita contra o lint — `linha de índice fora da gramática` deixa de ser condição de `next` (cai em `E-3` quando é linha de pai elegível; lint é `C-4`/`C-9`) e `plano vivo sem prefixo` é `C-7` + exit 3 do `drain` (`DB-37`); (2) **residência única em §2.5 item 6** (`:173-210`), com a `DB-6` mantendo o princípio e **deixando de enumerar** (emendada na própria célula, `:70`) e a cópia inline do card `done` rebaixada a registro — fecha a divergência que a `DB-2` proíbe; (3) uma gramática de linha viva **por arquivo de inbox** (`DB-38`, §2.4 em `:161-172`) mais TF que afirma o valor impresso sobre corpus onde as regras concorrentes discordam (1 vs. 3), com a correção de `_contar_pendentes_inbox` partida em dois contadores. **Card novo `BKL-T3a`** (`ready`, `:1429-1549`, `DB-39`) — residência da correção, **antes** da `BKL-T4`; plano passa a **15** tarefas. **Cards emendados no mesmo ato:** `BKL-T4` (`:1550-1623`) ganhou `Restrições desta tarefa`, `Não fazer`, `Contingências` e um TF — **não tinha nenhum desses campos**, ao contrário do que o `AE-7` supunha; e `BKL-T5` (`:1624-1653`) ganhou gramática inline, TF novo, `Arquivos-alvo` por bullet e `Pronto quando` discriminante (o anterior era satisfeito por inbox vazio). `BKL-T3` **intocada** (`DB-23`, sem retroação); §6 com três linhas de risco novas (`:1752-1771`). **Lição da rodada publicada no mesmo ato, como ato da orquestração** (precedente do dono, 2026-09-17 — publicar é consequência do plano, não pergunta): fase 4 item 4 de `.claude/agents/pantonic-planner.md` passa a exigir **residência única declarada para lista normativa copiada inline** (seção normativa do plano, nunca célula da tabela de decisões), e o item 7 passa a exigir, por **condição de erro** enumerada, a substring literal da mensagem + o TF que a afirma + a fronteira contra o instrumento vizinho, mais o valor que a **regra concorrente** daria sobre a mesma fixture; linha correspondente em `CHANGELOG.md` sob `## [Não lançado]`. Consumo: ver `docs/telemetria.tsv` (`BKL-RP6`). **`BKL-T3a` entregue em 2026-09-18** (`pantonic-executor`, `review`): as três condições de exit 3 de `next` em `.claude/tools/backlog.py` passam a imprimir as substrings obrigatórias de §2.5 item 6 — E-1 virou `dois ou mais itens in-progress: ` com os IDs **ordenados alfabeticamente** (antes `dois in-progress: `, sem ordem), E-2 virou `linha de status ausente para <ID>` (antes `item sem linha de Status: <ids>`) e E-3 ficou **intocada** por já estar conforme; `_contar_pendentes_inbox` partida em `_contar_inbox_planos` (regex nova `_CAMINHO_PLANO_INBOX_RE`, gramática de §2.4) e `_contar_inbox_memoria` (gramática preservada), com `renderizar_next` ligando cada campo do rodapé ao seu contador — até aqui o campo `inbox de planos:` contava pela gramática do inbox de memória (`DB-38`). Fixture nova `tests/fixtures/backlog/inbox_planos/_INBOX.md` com o texto literal do card (1 linha viva pela gramática de §2.4 contra 3 pela do inbox de memória — é essa diferença que dá poder discriminante ao TF), 3 testes novos em `tests/test_backlog.py` (`21 passed` → `24 passed`), suíte inteira `130 passed` (piso 127), **nenhuma das cinco contingências acionada** e nenhuma asserção pré-existente ajustada. Âncoras do card re-derivadas no despacho e **sem deriva** (`selecionar_next:655-696`, `_contar_pendentes_inbox:767-781`, `renderizar_next:784-839`) — o card não cita linha de código, e o gate de delegação ainda descartou as contingências 1 e 2 por verificação barata antes do despacho (função existe com o nome exato; `renderizar_next` já recebia os dois caminhos por parâmetro), o que o executor confirmou. Entrega não commitada: `.claude/tools/backlog.py`, `tests/test_backlog.py`, `tests/fixtures/backlog/inbox_planos/_INBOX.md`. **Nenhum achado de execução** — o executor não reportou nada fora do escopo do card. **Janela encerrada por ocupação de contexto (`B2`, `GOVERNANCA.md` §4.3)** logo após a entrega: a rodada de revisão da `BKL-T3a` **não** foi despachada nesta janela e é a próxima tarefa. Consumo: ver `docs/telemetria.tsv` (`BKL-T3a`). **Rodada `RP-7` fechada em 2026-09-18** (`pantonic-planner`, sobre o `AE-8`) — decisão técnica/tática, **nada escalado ao dono**: `DB-40`..`DB-42` em `docs/plans/P-0739-backlog-instrumento.md:107-109`, rodada em `:2807`-fim, `AE-8` absorvido (`:2773-2805`). Rotas, por achado: (1) **E-2 corre sobre a união item ∪ pai** — a norma de §2.5 item 6 sempre teve o sujeito composto ("item candidato **ou pai de candidato**") e o que faltava era o código cobrir a segunda metade mais a norma fechar os dois casos que só a segunda metade cria: pai compartilhado por dois candidatos (uma ocorrência por **ID distinto**) e item + pai os dois sem a linha (ordem **alfabética crescente**, separador `, `), com a ordem de avaliação entregue (E-2 antes de E-1 e E-3) ratificada e a fronteira contra o lint escrita na própria tabela (ausência de `Status` é `C-2`/`C-8` no `check`; em `next` é E-2, que recusa e não classifica) — `DB-40`; (2) **prefixo `- ` do contador de fila de memória** (`DB-41`): não há norma nova — §2.6 e `GOVERNANCA_MEMORIAS.md` §8 já escreviam o espaço —, o código é que testava `s.startswith("-")` e contava a régua `---` como candidato; a célula de §2.6 passa a dizer que o espaço faz parte do prefixo e que **nenhuma outra exclusão** entra no contador, e o TF obrigatório roda sobre corpus em que as duas leituras discordam (2 contra 3); filtro de indentação foi descartado por falta de forma real apurada (gramática autorada de memória é o defeito da `RP-1`). **Card novo `BKL-T3b`** (`ready`, `:1569-1704`, `DB-42`) — um card só para os dois defeitos (mesmo verbo, mesmo módulo, mesmo arquivo de teste, mesma família de fixture, pelo raciocínio da `DB-39`) e **antes** da `BKL-T4`, porque a `BKL-T4` aplica E-2 ao item alvo **e ao pai dele** antes de escrever e reusa a função que a `BKL-T3b` normaliza — despachada primeiro, ela criaria segunda residência para a mesma regra. Plano passa a **16** tarefas. **Cards emendados no mesmo ato:** `BKL-T4` (`:1705-1786`) ganhou `BKL-T3b` no `Depende de`, a forma da mensagem de E-2 nas `Restrições` com a instrução de **reusar** a função em vez de reescrever a regra, e o `Não fazer` atualizado. `BKL-T3a` **intocada** (`DB-23`, sem retroação); §6 com duas linhas de risco novas. **Fato re-derivado no passo 1** (achado é indício, não apuração): com os dois pais da fixture sem a linha, a seleção de hoje sai exit 2 (`nada delegável`), não exit 0 — o exit 0 elegendo `FFO-T2` que o `AE-8` relata ocorre quando **só** o tíquete perde a linha; as duas leituras entraram no card, e o TF afirma exit 3 nos dois casos. **Lição da rodada publicada no mesmo ato, como ato da orquestração** (precedente do dono, 2026-09-17): fase 4 item 7 de `.claude/agents/pantonic-planner.md` passa a exigir **um TF por termo de sujeito composto** de regra normativa, mais o fechamento na norma dos casos que o sujeito composto cria (referente repetido, dois termos falhando juntos), e o confronto do **instrumento irmão** com a mesma gramática quando um card corrige um de um par; linha correspondente em `CHANGELOG.md` sob `## [Não lançado]`. Consumo: ver `docs/telemetria.tsv` (`BKL-RP7`). **`BKL-T3b` entregue em 2026-09-18** (`pantonic-executor`, `review`): em `.claude/tools/backlog.py`, a condição **E-2** de `next` passa a correr sobre a **união item ∪ pai** (`DB-40`) — a lista `sem_status` virou `ids_sem_status`, união ordenada por `sorted` do `item.id` de cada candidato com `item.status is None` com o `pai.id` de cada candidato com `pai.status is None`, uma ocorrência de `linha de status ausente para <ID>` por **ID distinto**, mesma posição no fluxo (antes da contagem de `in-progress`); e `_contar_inbox_memoria` passa a testar o prefixo `- ` (hífen **e** espaço) em vez de `-` (`DB-41`), deixando de contar a régua markdown `---` como candidato, **sem** nenhum outro filtro novo. 2 testes novos em `tests/test_backlog.py` (`24 passed` → `26 passed`), suíte inteira `132 passed` (piso 130), **nenhuma das quatro contingências acionada**, nenhuma asserção pré-existente ajustada e **nenhum achado de execução** — as duas linhas literais da fixture transcritas pela `RP-7` bateram exatamente (contingência 1 descartada por verificação do próprio executor) e nenhum nome de teste colidiu (contingência 2 descartada). Âncoras e números de aceite re-derivados no despacho pelo item 3 do gate de delegação e **sem deriva** (`tests/test_backlog.py` `24`, suíte `130`, idênticos ao piso que a `BKL-T3a` mediu). Entrega não commitada: `.claude/tools/backlog.py`, `tests/test_backlog.py`. **Janela encerrada por ocupação de contexto (`B2`, `GOVERNANCA.md` §4.3)** logo após a entrega: a rodada de revisão da `BKL-T3b` **não** foi despachada nesta janela e é a próxima tarefa. Consumo: ver `docs/telemetria.tsv` (`BKL-T3b`). **`BKL-T3b` revisada e fechada em 2026-09-18** (`pantonic-reviewer`, mesmo protocolo): **aprovada 100%**, bloqueante nenhuma, as sete dimensões `conforme` → `BKL-T3b` → `done` (RDO `docs/RDO/P-0739-BKL-T3b-e-2-sobre-o-pai-do-candidato-e-o-prefixo-do-contador-de-memo.md`; laudo consumido e apagado, `DP-H`). O reviewer re-rodou a `Verificação` do card por conta própria (`tests/test_backlog.py` `26 passed`, os dois nomes de TF no `--collect-only`, coleta global `132`, `tests/ -q` `132 passed`) e conferiu o diff: E-2 virou conjunto de **IDs distintos** ordenado (união do `item.id` com o `pai.id` de cada candidato sem a linha de `Status`), na posição em que já estava, e `_contar_inbox_memoria` passou a testar `startswith("- ")`, com `_contar_inbox_planos` **intocado**, como o card exige. Evidência mecânica (`docs/RDO/evidencia/P-0739-BKL-T3b.md`, `--desde 6d7433c`) com `guardas`/`testes` `conforme`; o veredito de `escopo` saiu **aberto** na mecânica e o reviewer o fechou como `conforme` por datação de `mtime` — os 5 arquivos de `tests/fixtures/backlog/next_tk90*/` são de 2026-09-17 19:52 (`BKL-T3`) contra 2026-09-18 04:16 dos dois alvos. **Nada escalado ao dono pelo laudo** (recomendação `seguir`, pendência `nenhuma`, sem `--escalar`): o único achado de processo é alvo `dossiê` e está registrado como `AE-9` (`docs/plans/P-0739-backlog-instrumento.md:2920`-fim) — a atribuição cruzada de `review_evidence.py` casa só por caminho exato, com rota de card próprio e **sem** bloquear a `BKL-T4`. As duas decisões do dono pendentes (abrir `RP-8` antes da `BKL-T4` ou não; commitar as 7 entregas acumuladas ou não) estão no bloco `Fila corrente`, nenhuma despachada. Consumo: ver `docs/telemetria.tsv` (`BKL-T3b-revisao`).

- 2026-09-18 — **Fila corrente anterior (texto de 2026-09-18, janela da `BKL-T4`; migra para `## P-0739` na condensação):** nada em execução. **A `BKL-T3b` fechou `done` em 2026-09-18** — **aprovada 100%**, bloqueante nenhuma, as sete dimensões `conforme`, recomendação `seguir`, sem `--escalar` (RDO `docs/RDO/P-0739-BKL-T3b-e-2-sobre-o-pai-do-candidato-e-o-prefixo-do-contador-de-memo.md`; laudo consumido e apagado, `DP-H`). Plano em **10/16**. O único achado do laudo (alvo `dossiê`) está registrado como `AE-9` (`docs/plans/P-0739-backlog-instrumento.md:2920`-fim), **sem retroação** (`DB-23`) e **sem bloquear a `BKL-T4`**: `review_evidence.py:295-320` atribui arquivo tocado a outra tarefa do mesmo plano só por **caminho exato**, então alvo-diretório declarado por outra tarefa (o `tests/fixtures/backlog/` da `BKL-T3`) nunca casa — nesta rodada isso deixou o veredito mecânico de `escopo` **aberto** e obrigou o reviewer a datar `mtime` para provar que a `BKL-T3b` não tocou os 5 arquivos de `tests/fixtures/backlog/next_tk90*/`. **Decisão do dono sobre o `AE-9` (2026-09-18, contexto novo):** seguir para a `BKL-T4` e deixar o `AE-9` registrado **sem agir** — não abrir `RP-8` (seria o terceiro adiamento seguido da `BKL-T4`; `AE-9` é achado de dossiê e não bloqueia). **Decisão de commit já satisfeita antes desta pergunta ser feita:** o dono commitou as 7 entregas em `428246c` (2026-09-18 17:57:52, "fecha BKL-T2a..T3b do P-0739") entre o encerramento da janela anterior e a abertura desta — o texto abaixo que descrevia a árvore como "não commitada" estava desatualizado, não a árvore; `git status` confirma limpo. Ordem do plano a partir daqui: `BKL-T4` → `BKL-T5` → `BKL-T6` → `BKL-T7` → `BKL-T8` → `BKL-T9` · ready 6 · blocked 0 · in-progress 0 · review 0 · done 10 · total 16. **Âncoras** (re-derivadas em 2026-09-18, re-derivar de novo no despacho): card `BKL-T4` em `docs/plans/P-0739-backlog-instrumento.md:1710-1791`, `BKL-T5` em `:1792-1821`, `AE-9` em `:2920`-fim. **Números de aceite (medidos em 2026-09-18, na revisão da `BKL-T3b`):** `tests/test_backlog.py` `26`, suíte inteira `132` (piso 130). Base de recorte da evidência para a próxima rodada: `--desde 428246c` (as entregas das `BKL-T2a`..`BKL-T3b` foram commitadas em `428246c`; recorte volta a tamanho proporcional à entrega). Consumo: ver `docs/telemetria.tsv` (`BKL-T3b-revisao`). **Achado de orquestração sem ação nova** (o mesmo das cinco janelas anteriores): `python .claude/tools/backlog.py check` segue vermelho no repo por desenho até a migração da `BKL-T6`. **Próxima tarefa delegável: `TK-54a`** (diretiva de emergência de 2026-09-18, acima — vem antes da `BKL-T4` e de tudo no `P-0739`). Ela voltou `blocked` razão `premissa` na triagem de 2026-09-18 (`AE-1`: a coluna de classificação não tinha critério) e a rodada `RP-TK54-1` a fechou e devolveu a `ready` no mesmo dia, rota A — rubrica das quatro categorias e coluna já preenchidas no card, executor transcreve e não avalia; rodada técnica/tática, nada escalado ao dono. Card fechado em `docs/DIARIO_DE_OBRAS.md` › `### TK-54a — O extrato [Sonnet · classe investigacao]`; registro da rodada em `## TK-54` › `### Achados da execução (TK-54)`. **RUN DE AFERIÇÃO DO `scrum-master` (2026-09-18):** a `BKL-T4` foi conduzida pelo loop de ponta a ponta como caso-teste — `done`, `ressalva` 85%, bloqueante `nenhuma`, RDO `docs/RDO/P-0739-BKL-T4-status-start-diretiva-transicao-e-projecoes.md`; suíte 132→142 verdes. Loop encerrado pela regra `B1` (pendência + ressalva com rota). Ressalva roteada como `AE-10` (dependência de ordem: `transacionar_status` chama `.index('<!-- fila:gerada -->')` sem guarda e os marcadores só entram na `BKL-T6` item (a)) — **o `P-0739` fica PARADO** (`DM-9` do `P-0740`): nem a `BKL-T5`, nem rodada de replanejamento sobre o `AE-10`. O plano espera a baseline do `scrum-master` fechar (`LM-T1`..`LM-T4` do `P-0740`), é reagrupado em módulos coesos pela `LM-T5` — que absorve o `AE-10` — e fecha em **rodada única** na `LM-T6`. Cinco defeitos do próprio loop em `AE-11` e no relatório de janela. `P-0739` passa a 11/16. **`LM-T1` do `P-0740` despachada e devolvida `blocked` razão `premissa` em 2026-09-18** (10 tool uses / 61,8k tk, nenhum arquivo tocado — conduta correta de `G-EXECREADY`): o entregável (a) mandava versionar `.claude/estado/` e o `.gitignore` excluía o diretório inteiro (`AE-2`). **Rodada `RP-1` fechada em 2026-09-18** (`pantonic-planner`, `G-REPLAN`) — decisão **técnica**, **nada escalado ao dono**: `DM-10` (o diretório é canônico do framework e viaja com `.gitkeep`; o conteúdo de sessão continua ignorado — `.gitignore` passa a `.claude/estado/*` + `!.claude/estado/.gitkeep`) e `DM-11` (`rdo.py close --tokens-k` vira `float` com uma casa decimal, a mesma forma que o hook já emite), em `docs/plans/P-0740-loop-de-modulos.md` §4; rodada registrada em `### RP-1` sob `## Achados da execução` do mesmo plano, `AE-2` absorvido. `LM-T1` reescrita (com `.gitignore` nominalmente nos `Arquivos-alvo`, três textos literais, quatro contingências e verificação por `git check-ignore`, que discrimina — o TF velho passava versionado ou não) e de volta a `ready`; `LM-T2` ganhou só o fato de contorno, `LM-T3` intocada, `LM-T5` ganhou o critério (vi) da rubrica com o `AE-2` como caso medido. Plano de volta a `in-progress`. **Lição publicada no mesmo ato** em `.claude/agents/pantonic-planner.md` (fase 4, item 10 — classe nova: entregável que versiona, cria ou apaga arquivo confrontado com a regra de versionamento vigente antes de publicar), com linha em `CHANGELOG.md`. **`LM-T1` despachada de novo em 2026-09-18 e devolvida `blocked` razão `premissa` pela SEGUNDA vez — mas com a entrega INTEIRA produzida e verde** (145 testes; `.gitignore:11-12` na ordem prescrita; `.gitkeep` criado; `rdo.py`, `scrum-master/SKILL.md` e os dois arquivos de teste editados): a contingência 1 do card disparou porque as **verificações 3 e 5 eram insatisfazíveis por desenho do git** — `git check-ignore -v` reporta o padrão decisivo mesmo quando é a negação (imprime `.gitignore:12:!.claude/estado/.gitkeep`, exit 0) e `git status --porcelain` sem `-uall` colapsa o diretório não rastreado. Registrado como `AE-4`. **Rodada `RP-2` fechada em 2026-09-18** (`pantonic-planner`, `G-REPLAN`) — decisão **técnica**, **nada escalado ao dono**: `DM-12` em `docs/plans/P-0740-loop-de-modulos.md` §4, rodada em `### RP-2` sob `## Achados da execução`, `AE-4` absorvido. **Veredito sobre a cláusula do segundo bloqueio: NÃO se aplica** — a premissa não caiu, a rota de `DM-10`/`DM-11` saiu **confirmada** pelo fato medido; o plano **não** vira `superseded`. A cláusula, que contava bloqueios em vez de olhar o objeto do bloqueio, foi **emendada** em `GOVERNANCA.md` §7 item 17: o teste passa a ser "existe entrega que satisfaz o entregável do card sob as decisões vigentes?" (não existe → bloqueio de rota → `superseded`; existe → bloqueio **de aceite** → a rodada corrige a redação), com dois tetos anti-abuso (terceiro bloqueio `premissa` na mesma tarefa; segundo bloqueio de aceite sobre a mesma verificação já reescrita). A saída (c) do `G-REPLAN` ganhou o ramo **`review`**, e a transição `blocked` → `review` (autoria do planejador, **gatilho 1**) foi publicada na tabela de transições de `.claude/skills/diario-de-obras/SKILL.md` — o loop não improvisa status. Cards reescritos: `LM-T1` (verificações 2/3/4/5 e contingência 1, com saída **medida**; `Status` → `review` com nota de atribuição para quem revisa), `LM-T2` e `LM-T3` (piso de suíte 142 → 145), `LM-T4` (aceite `backlog.py check` verde **removido** — insatisfazível pelos 315 achados pré-existentes do `AE-1` em arquivos que a tarefa não toca; no lugar, `kit_check -Mode check-drift` exit 0, piso 145 e varredura da régua antiga pelo literal `>8 write-clusters`, hoje com uma ocorrência em `.claude/skills/proximo-passo/SKILL.md:126`), `LM-T5` (critério (vii) da rubrica e o `AE-4` como quarto insumo medido). **Lição publicada no mesmo ato** em `.claude/agents/pantonic-planner.md` (fase 4, item 11 — classe nova: saída esperada de comando é fato **observado**, nunca deduzida da ferramenta; pergunta binária usa flag binária + exit code; nenhum card exige "verde" de instrumento que a tarefa não pode deixar verde — mais o gatilho correspondente na fase 1), com linha em `CHANGELOG.md`. Plano de volta a `in-progress`. **Próximo passo do `P-0740`: a rodada de REVISÃO da `LM-T1`** (`pantonic-reviewer` sobre a entrega que já está na árvore, não commitada, contra o dossiê corrigido) — **não** é despacho de executor e a `LM-T1` **não** se refaz. Depois dela, `LM-T2`. **O Passo 6 dessa revisão falhou em 2026-09-18 e a rodada `RP-3` o destravou** (`pantonic-planner`, `G-REPLAN`, decisão **tática**, **nada escalado ao dono**): `review_evidence.py` saía exit 1 em `LM-T1` porque o cabeçalho de três campos da `DM-5` (`[<modelo> · esforço <e> · classe <c>]`) não casa a gramática de **nenhum** dos dois parsers do kit — `rdo.py:85-89` (`_HEADER_BRACKET_RE`, compartilhada com o `review_evidence.py`, que fixa `esquema_legado=False` e não tem escotilha) nem `backlog.py:51` (`_BRACKET`, que faz o card sair `header_valido=False`) —, e `esforço` não existia em nenhum lugar da árvore `.claude/` (`F-7`). `DM-13` (`docs/plans/P-0740-loop-de-modulos.md` §4; rodada em `### RP-3`, `AE-5` absorvido) recua os **seis** cabeçalhos para a forma de dois campos com `- **Esforço:** <valor>` como campo do corpo — nenhuma linha de código tocada, nenhum executor despachado — e aloca a gramática de três campos, com o campo **opcional** e grupo **não capturante**, à tarefa nova **`LM-T4a`** (`Sonnet · classe implementacao`, esforço `low`), ordenada **antes** da `LM-T4`: a ordem é parser → doutrina → cards. Fila do plano: `LM-T1` → `LM-T2` → `LM-T3` → `LM-T4a` → `LM-T4` → `LM-T5` → `LM-T6`, 7 tarefas. `LM-T1` **segue em `review`**, intocada. **Lição: classe já conhecida** (dependência de ordem, mesma do `AE-10`, já coberta pelo bullet da fase 1 do `pantonic-planner` publicado em 2026-09-16) — `.claude/agents/pantonic-planner.md` **não** foi editado. Ao regerar o dossiê, use o comando já medido: `python .claude/tools/review_evidence.py --plano docs/plans/P-0740-loop-de-modulos.md --tarefa LM-T1 --desde 428246c --out docs/RDO/evidencia/P-0740-LM-T1.md`.

---

## TK-23 — A variante (b) do proxy de ocupação de contexto

- **Status:** `cancelled` · 2026-08-24

A variante (b) do proxy de ocupação de contexto — contador de tarefas por janela calibrado pela série de `docs/telemetria.tsv` — não foi medida pela `EXA-T1` (orçamento esgotado). A variante (a), hook lendo o `transcript_path` exposto no payload de `PreToolUse`, tem viabilidade técnica confirmada com evidência colada. Decidir entre as duas é escopo da `EXA-T13`; se (b) continuar viva quando a `T13` chegar, ela precisa de sonda dedicada antes da escolha — nenhuma decisão pode se apoiar em (b) como se fosse medida

*(Âncora original do índice, preservada:* `docs/audits/SPIKE_HARNESS_EXECUCAO_AUTONOMA.md` §"Nota de escopo" *)*

---

## TK-32 — Uso e teto: medida agregada ou porteiro de tarefa

- **Status:** `cancelled` · 2026-08-13

**Uso e teto: medida agregada ou porteiro de tarefa.** O teto por tarefa vem sendo cruzado com regularidade sem produzir a consequência que a doutrina prescreve — `EXA-T31` consumiu os 15 do teto exatamente no fechamento e deixou a verificação órfã (coberta pelo orquestrador na mesma rodada), `EXA-T19` fechou em 41 contra 40, e a série `UXROUND3` registrou 56/35, 61/40 e 112/50. **Enunciado do dono (2026-08-11):** a questão é de **conceito de framework**, não de desenvolvimento deste projeto; uso e teto são medidas de **agregado** e não de indivíduo — avaliadas tarefa a tarefa medem ruído; o portador entre tarefas é o card **"Lições aprendidas na tarefa"** (metainformação **da tarefa**, nunca do entregável), acumulando até o **fecho do plano**, onde os números são lidos em conjunto. **Hipótese a confrontar com a série, não premissa:** o uso atual desse controle é mais poluição do que valor ou economia efetiva. **Regime interino, com efeito imediato:** até a posição final o teto é **alarme, nunca bloqueio** — nenhuma tarefa para, é impedida ou fica incompleta por cruzar o número, e quem delega não escreve cláusula de parada dura por teto; a medição em `docs/telemetria.tsv` continua obrigatória, porque é a série que decide. Execução: `EXA-T34`, que fecha a `DP-L` e para para ratificação em lote com `DP-I` e `DP-J`; a materialização em `GOVERNANCA.md` §3 é card autorado depois do aceite. **Encaminhamento do dono, 2026-08-12:** a matéria de consumo se revê **inteira e em plano próprio**, aberto depois que o `P-0734` fechar — o desdobramento está registrado na tarefa de fechamento (`### T17`, item 4), e a hipótese a confrontar com a série é que tanto alarme de teto não paga o que custa, já que todo cruzamento acaba justificado. **A `EXA-T34` foi cancelada por absorção na mesma decisão** e nenhuma `DP-L` se forma no `P-0734`: formar a posição ali decidiria agora o que o plano seguinte revê por inteiro. O corpo daquele card permanece como material absorvido — o insumo do dono (§15), a medição obrigatória de três números e o conteúdo que a decisão precisa cobrir —, e é dele que o plano novo parte. Até lá, o regime interino continua em vigor

*(Âncora original do índice, preservada:* `docs/plans/P-0734-execucao-autonoma.md` §15, `### T34` e `### T17`; `GOVERNANCA.md` §3 (tabela de tetos por classe) *)*

---

## TK-38 — Comunicação entre agente e humano — skill própria e requisitos mínimos

- **Status:** `ready` · 2026-08-13

**Comunicação entre agente e humano — skill própria e requisitos mínimos.** Aberto por decisão do dono em 2026-08-13. O framework nomeia objetos de projeto por prefixo abreviado (`DP-`, `DR-`, `DE-`, `DI-`, `DH-`, `DA-`, `TK-`, `EXA-T<n>`, `G-*`) e os agentes carregam esses tokens **crus** para dentro da conversa com o humano, que não participou do ato que os criou. **Fato medido nesta mesma rodada:** o relatório de handover da `EXA-T25` citou `DP-F`, `DP-I`, `DP-J` e `DP-L` sem expandir nenhum, o dono precisou gastar **um prompt inteiro** perguntando onde essas descrições moravam, e a expansão que ele inferiu (*"Decisão Pendente"*) **está errada** — `README.md:172` define o prefixo como *decision record* (decisão já ratificada) e **não expande as letras `D` e `P` em lugar nenhum do repositório**, de modo que a sigla é ilegível a partir do artefato até para quem a usa. Agravante declarado pelo dono: o framework almeja público de **outros idiomas**, para quem uma abreviação em português nunca fará sentido. **Recorte:** a nomenclatura abreviada **permanece** nos artefatos (é compacta e greppável); o que muda é a **superfície de conversa** — toda ocorrência em texto dirigido ao humano vem acompanhada do significado inline, na forma `DP-7 (<expansão> #7)`. **Golden rule a trabalhar no tíquete, enunciada pelo dono:** *"toda comunicação que demandar que o humano leia um documento extra, ou crie um novo prompt, é comunicação ineficiente, e deve ser registrada como lição aprendida para melhoria da skill de comunicação"*. **Escopo a cobrir:** (a) skill de comunicação agente↔humano, com os requisitos mínimos do corpo da mensagem para acelerar a tomada de decisão; (b) proibição de exigir leitura de artefato extra ou prompt de esclarecimento como caminho normal — o token gasto em pergunta de esclarecimento é desperdício mensurável; (c) tabela de expansão dos prefixos e termos intrínsecos do framework, **incluindo o que `DP-` e os demais de fato significam**, hoje inexistente; (d) alcance multilíngue; (e) o registro das falhas de comunicação como lição aprendida, ligando ao portador de metainformação de tarefa da `TK-32`. Área de superfície ampla — atinge kit executável, doutrina e espelho, e por isso nasce como tíquete, não como correção de rodada. **Fronteira declarada contra o `TK-36`** (dono, 2026-08-13, `P-0734` §19): este tíquete governa **exclusivamente** a superfície **agente↔humano**; a unificação `handover` + `proximo-passo` é maquinário **agente↔agente**, transparente ao gerente, e **não** recebe requisito de comunicação humana — arrastá-lo para lá acrescentaria custo a toda iteração do loop autônomo. Os dois eixos não se misturam e nenhum planejamento derivado pode tratá-los como a mesma matéria

**Segunda ocorrência medida (2026-09-19):** sobre o relatório de encerramento da janela do `P-0740`,
o dono gastou um prompt próprio pedindo *"um glossário das várias siglas usadas para referenciar as
tarefas (`A10`, `B6`, etc)"* — e dois dos tokens que ele citou (`A10`, `B6`) **não existem**: as
tabelas de roteamento do `scrum-master` vão até `A9` (com `A6a` e `A8a`) e até `B4`. O artefato não
só é ilegível a partir de fora do ato que o criou; ele induz o leitor a inventar identificadores
plausíveis. A classe é a mesma da `EXA-T25`, agora com o **dono** como leitor afetado, e não um
agente. **Não entra no `P-0740`** (`DM-30` (ii)): é matéria de coerência, portanto pertinente ao
critério novo, mas cruza o tema do plano e `DM-4` proíbe a absorção oportunista. Fila pós-plano.

*(Âncora original do índice, preservada:* `README.md:172` (glossário, entrada `DR-`/`DP-`); `.claude/skills/` (skill nova a autorar); `GOVERNANCA.md` §3.1 *)*

- 2026-09-19 — *(decisão do dono, 2026-08-13; evidência medida no handover da `EXA-T25`)*

---

## TK-48 — `~/.claude/settings.json` **perdeu a chave `hooks` inteira silenciosamente**

- **Status:** `ready` · 2026-09-19

`~/.claude/settings.json` **perdeu a chave `hooks` inteira silenciosamente**, sem ação intencional do dono, entre a `RPC-T4` e a escolha da `RPC-T5` — os 4 hooks registrados (premissa da `T5`) somem sem rastro. Causa não investigada por decisão do dono (foco em proteção, não em achar culpado); a `T5` não depende do estado atual do arquivo (reconstrói o registro pela tabela já transcrita no dossiê) e segue delegável. Vulnerabilidade a considerar: `settings.json` global pode perder chave inteira sem sinal

*(Âncora original do índice, preservada:* `docs/plans/P-0735-residencia-e-ponto-de-carga.md` seção "Achados da execução" (2026-08-17) *)*

- 2026-09-19 — *(**dono mandou resolver em 2026-09-19**. Estado medido no mesmo dia: a chave `hooks` **existe** — global com `PreToolUse` e `UserPromptSubmit`, projeto com `PreToolUse` e `SubagentStop` —, portanto **não há perda ativa a reparar**; o que falta é a **proteção**, que era o foco declarado do dono desde a abertura (proteger, não achar culpado). Não entra no `P-0740` por `DM-30` — cruza o tema; entra na fila logo depois do marco)*

---

## TK-51 — Composição do 1º usage de uma janela de orquestração

- **Status:** `done` · 2026-08-24

**Origem:** achado da `CTX-T10` (`docs/plans/P-0738-contexto-esgotado.md` `## 9`, 2026-08-24) — a
rodada Estágio C não reduziu o custo fixo de abrir uma janela: 1º `usage` = **46.071 tok** contra
34.260 / 34.292 / 45.872 antes (+34,4% vs. mediana). **Rota decidida pelo dono em 2026-08-24:** (i)
investigar **medindo**; **proibido cortar antes de medir** — cortar sem medir é o que produziu a
regressão. **Escopamento (planejador, 2026-08-24):** o que faltava não era a rota, era o **método de
sondagem**; decidido abaixo, com baseline e formato do achado, e o tíquete vira uma tarefa atômica
fechada.

**Decisões do escopamento (fechadas aqui, o executor não as reabre):**

1. **O 1º `usage` parte em duas metades, uma visível e uma opaca.** Visível: tudo que o transcript
   mostra antes da primeira entrada `assistant` — o primeiro turno `user`, que carrega CLAUDE.md
   global, CLAUDE.md de projeto, índice e arquivos de memória, `gitStatus`, `env` e o texto do
   pedido; mede-se direto, em chars. Opaca: system prompt do produto, **esquemas das ferramentas
   registradas** e skills anunciadas; não está no transcript e **só se mede por diferença**.
2. **A metade opaca se precifica por regressão, não por adivinhação de payload.** Ajustar
   `usage_1 ~ chars_preambulo` (mínimos quadrados, duas variáveis) sobre muitas sessões do mesmo
   `agentType`: a **inclinação** dá o câmbio chars→token do conteúdo e o **intercepto** dá o custo
   com preâmbulo zero, que é exatamente a superfície opaca. Comparar interceptos entre papéis
   precifica a superfície de ferramentas (é a pista da `CTX-T4`: executor com toolset completo ×
   `pantonic-scout` com três, 34.016 × 8.340 tok); comparar o intercepto da janela **principal**
   antes × depois responde se o Estágio C a mexeu.
3. **A dispersão da baseline se mede antes de qualquer atribuição de causa.** As três janelas do
   controle já variam 34.260 → 45.872 no **mesmo dia** (+33,9%) — a mesma grandeza da regressão
   declarada (+34,4%). Enquanto n=3 × n=1, "subiu 34%" e "sempre variou 34%" são indistinguíveis;
   por isso a primeira medida é a distribuição com n grande, e "o número está dentro da dispersão
   pré-existente" é **desfecho legítimo**, não fracasso da sondagem.
4. **Baseline canônica:** as três janelas registradas em `docs/CUSTO_DO_PICKUP.md` `## 7`/`## 9` —
   `08a29a54…` (34.260), `a7432333…` (34.292), `29dd40a9…` (45.872), 2026-08-22 —, porque são as do
   registro e é contra elas que a regressão foi declarada. **Ponto tratado:**
   `95db6421-3bbd-4938-b97d-f60a28435084.jsonl` (46.071). **Baseline estendida** (contexto de
   variância, não substitui a canônica): **todas** as janelas principais do diretório do projeto com
   início anterior ao início da `95db6421…`. **Corte antes/depois:** o timestamp da primeira entrada
   da `95db6421…` — sem arqueologia de data, sem lista de commits.
5. **Instrumento novo, descartável.** A `sonda_janela.py` da `CTX-T2` vivia no scratchpad de outra
   sessão e não é recuperável; a sonda desta tarefa se **reescreve**, roda no scratchpad da sessão e
   **não entra no repo** (`DX-4`). Desenho fixado no card — o executor implementa, não projeta.
6. **Não é sprint e não abre plano** (`P-0739` segue livre): uma tarefa, três arquivos de registro,
   nenhuma superfície de `.claude/` tocada.

### TK-51a — Do que é feito o 1º usage: preâmbulo visível × superfície opaca [Sonnet · classe investigacao]

- **Status:** `done` · 2026-08-24
- **Objetivo:** devolver, em número medido, **de que é feito** o 1º `usage` de uma janela de
  orquestração e **qual componente** carrega o Δ de +11.779 tok que a `CTX-T10` mediu — ou registrar,
  também em número, que o Δ está dentro da dispersão que a série sempre teve. A tarefa **mede e
  publica**; não corta, não propõe corte e não escolhe rota.
- **Arquivos-alvo:**
  - `<scratchpad da sessão>/sonda_dx5.py` — **novo**, stdlib apenas (sem `numpy`/`pandas`),
    descartável, fora do repo.
  - `<scratchpad da sessão>/serie_dx5.tsv` e `<scratchpad>/blocos_dx5.tsv` — saídas da sonda.
  - `d:\workspaces\PantonicApp\docs\CUSTO_DO_PICKUP.md` — acrescenta `## 11 Composição do 1º usage
    (<data>)`, **≤ 55 linhas**, ao fim do arquivo.
  - `d:\workspaces\PantonicApp\docs\DOC_MAP.md` — na entrada `## docs/CUSTO_DO_PICKUP.md`,
    acrescentar a linha da `## 11` na lista de seções (mesmo formato das linhas `## 9`/`## 10`) e
    atualizar o `(~306 linhas)` do cabeçalho para a contagem nova (`(Get-Content f).Count`).
  - `d:\workspaces\PantonicApp\docs\DIARIO_DE_OBRAS.md` — linha `TK-51` do índice (status → `done`)
    e bloco **Resultado** ao fim desta seção.
  - `README.md` **só se** `Grep pattern:"CUSTO_DO_PICKUP" path:README.md -n` mostrar que o espelho
    **enumera seções** desse relatório; se ele só nomeia o arquivo, `README.md` **não se toca**.
- **Corpus:** `C:\Users\panta\.claude\projects\d--workspaces-PantonicApp\*.jsonl`. Janela
  **principal** = arquivo sem campo `agentType` nas entradas lidas; janela de subagente = o valor do
  `agentType` (é por esse campo que a `CTX-T3`/`CTX-T4` agregou `pantonic-executor` n=149,
  `pantonic-scout` n=10 etc.).
- **Sonda `sonda_dx5.py` — desenho fechado:** para cada `.jsonl`, ler **linha a linha** e **parar na
  primeira entrada `assistant` que traga `usage`** (o arquivo inteiro nunca é carregado). Coletar:
  1. `arquivo`, `ts_inicio` (timestamp da 1ª entrada), `agent` (`agentType` ou `principal`);
  2. `usage_1` = `input_tokens + cache_creation_input_tokens + cache_read_input_tokens` do primeiro
     `usage` (fórmula candidata — ver **Calibração**), com os três campos também gravados soltos;
  3. `chars_preambulo` = soma dos chars de todo texto das entradas anteriores à primeira `assistant`;
  4. **blocos nomeados** do preâmbulo, segmentados por marcador literal, na ordem em que ocorrerem:
     cada `<system-reminder>…</system-reminder>` (rotulado pela primeira linha `# <nome>` interna
     quando houver — ex. `# claudeMd`, `# currentDate`), `gitStatus:`, `<env>…</env>`, e o restante
     como `pedido`; o que não casar vai para `outros`.
  **Saída:** `serie_dx5.tsv` (uma linha por sessão) e `blocos_dx5.tsv` (uma linha por sessão × bloco,
  só `arquivo`, `bloco`, `chars`). **Proibido imprimir conteúdo bruto de transcript** — o `stdout` da
  sonda traz **apenas** as três agregações abaixo, em ≤ 40 linhas.
- **As três medidas que a sonda imprime:**
  - **M1 — dispersão.** Para as janelas **principais**, por grupo (`antes` / `depois` do corte da
    decisão 4): `n`, mediana, mín, máx, p25, p75 de `usage_1`; e em que percentil do grupo `antes`
    cai o valor 46.071.
  - **M2 — visível × opaco nas 4 janelas canônicas.** Para `08a29a54…`, `a7432333…`, `29dd40a9…` e
    `95db6421…` (casar por prefixo do nome do arquivo): `usage_1`, `chars_preambulo`, tokens visíveis
    (chars ÷ câmbio da M3), resíduo opaco = `usage_1` − visíveis; e a tabela de blocos por janela,
    com Δ de cada bloco entre a `95db6421…` e a mediana das três de 2026-08-22.
  - **M3 — regressão.** `usage_1 ~ chars_preambulo` por `agentType` (e, para `principal`, também
    separado em `antes` / `depois`): `n`, intercepto (tok), inclinação (tok/char e o recíproco
    chars/tok), `r²`. Mínimos quadrados em Python puro, fórmula fechada.
- **Calibração (gate — antes de qualquer interpretação):** a sonda tem de **reproduzir os quatro
  números do registro** — 34.260 / 34.292 / 45.872 / 46.071. Se a soma dos três campos não
  reproduzir, testar **nesta ordem e só nesta**: (a) `input_tokens` isolado; (b)
  `input_tokens + cache_read_input_tokens`. Adotar a primeira que reproduza os quatro e **declarar
  qual foi** na `## 11`. Se **nenhuma** das três reproduzir, a tarefa **para**, não publica análise e
  devolve `blocked` razão `premissa` ao planejamento: número de registro não reproduzível é achado
  maior que esta investigação.
- **Formato do achado — `## 11`, estrutura fixa:** (1) sonda, corpus e **fórmula calibrada** do
  `usage_1`, com os quatro números reproduzidos; (2) **Tabela A** (M1); (3) **Tabela B** (M2, visível
  × opaco e blocos com Δ); (4) **Tabela C** (M3, intercepto por papel e `principal` antes × depois);
  (5) bloco **Veredito**, vocabulário fechado, uma linha por componente medido —
  `subiu <N> tok` · `desceu <N> tok` · `estável (|Δ| < 500 tok)` · `não isolado`; (6) **duas linhas
  de fecho obrigatórias**: *"O Δ de +11.779 tok vs. mediana é carregado por `<componente>`"* ou
  *"não isolado — falta medir `<o quê>`"*, e *"Dispersão: 46.071 está **dentro** / **fora** do
  intervalo [mín, máx] da baseline estendida (n=`<n>`)"*. Nenhuma célula com número sem proveniência
  medida; nenhuma constante nova (o dono já recusou número mágico, `## 9`).
- **Proibido:** propor, recomendar ou executar qualquer corte; editar qualquer arquivo sob
  `.claude/`; alterar prompt, agente, skill ou superfície de ferramenta; versionar a sonda ou os
  TSVs; retificar `docs/telemetria.tsv` (`DX-12`); reabrir `docs/plans/P-0738-contexto-esgotado.md`,
  que está `done`.
- **Verificação:** os quatro números canônicos aparecem reproduzidos na `## 11`; as tabelas A, B e C
  e as duas linhas de fecho existem; `## 11` ≤ 55 linhas (`(Get-Content docs/CUSTO_DO_PICKUP.md).Count`
  antes e depois); `git status --short` acusa **apenas** `docs/CUSTO_DO_PICKUP.md`,
  `docs/DOC_MAP.md`, `docs/DIARIO_DE_OBRAS.md` — e `README.md` se e só se o espelho enumerar seções —
  e **nenhum arquivo novo** (a sonda vive no scratchpad).
- **Pronto quando:** a `## 11` publica a decomposição visível × opaco das quatro janelas canônicas, a
  dispersão da baseline estendida e o intercepto por papel, com veredito nomeando o componente que
  carrega o Δ — ou `não isolado` com o que falta medir —, e o `TK-51` está fechado no índice.

**Resultado:** Medido em `docs/CUSTO_DO_PICKUP.md` `## 11 Composição do 1º usage (2026-08-24)`.
Sonda `sonda_dx5.py` (scratchpad) calibrou `usage_1 = input_tokens + cache_creation_input_tokens +
cache_read_input_tokens` reproduzindo os quatro números do registro. **M1 (dispersão):** grupo
`antes` (n=233) já continha janela mais cara que a tratada — máx 46.429 > 46.071 (percentil 94,8).
**M2 (visível × opaco, 4 janelas canônicas):** o texto do preâmbulo armazenado é quase idêntico nas
quatro (Δ ≈ 0 tok); o resíduo opaco sobe de mediana 14.504 tok (3 janelas de controle) para 26.285
tok em `95db6421` (Δ +11.781 tok). **M3 (regressão por papel):** intercepto `principal` global
17.155 tok, r²=0,030 — fraco; `principal/depois` (n=6) não dá regressão confiável, fica **não
isolado**. **Veredito:** o Δ de +11.779 tok vs. mediana é carregado pelo componente **opaco**
(superfície fora do transcript — não o texto do preâmbulo); dentro da dispersão pré-existente da
baseline estendida (percentil 94,8, não excede o máximo histórico). Tarefa mede e publica — não
corta, não propõe rota; decisão sobre causa/próxima rota segue pendente do dono.

**Revisão:** laudo `docs/RDO/laudos/DIARIO-TK-51.md` — 92%, veredito **ressalva**, nenhuma dimensão
bloqueante, recomendação **escalar**: o teste "dentro do intervalo [mín,máx]" não distingue ruído de
deslocamento — a Tabela A mostra o grupo `depois` (n=6) com mediana 46.070 contra 34.347 do grupo
`antes` (n=233), isto é, as 6 janelas pós-corte agrupadas no topo da faixa histórica, não só a
janela tratada. Decisão do dono sobre causa/rota é pré-requisito, ver "Diretiva de priorização".

**Decisão do dono (2026-08-24):** causa é **deslocamento real**, não ruído — o padrão das 6 janelas
pós-corte pesa mais que "dentro do intervalo [mín,máx]" da baseline (Achado 3). Consequência
registrada em `## P-0737` (nova razão do `blocked`) e no tíquete novo `TK-53` (investigação do que
mudou no corte). Ressalva resolvida; `TK-51` permanece `done`, sem reabertura.
Consumo: ver `docs/telemetria.tsv`.

## TK-53 — Causa do deslocamento de custo nas janelas pós-corte

- **Status:** `done` · 2026-08-31

**Origem:** decisão do dono em 2026-08-24 sobre o Achado 3 do laudo `docs/RDO/laudos/DIARIO-TK-51.md`
— a ressalva do `TK-51` (teste "dentro do intervalo [mín,máx]" não distingue ruído de deslocamento)
foi resolvida como **deslocamento real**: a Tabela A mostra as 6 janelas pós-corte (grupo `depois`,
mediana 46.070) agrupadas acima do grupo `antes` (mediana 34.347, n=233), não apenas a janela
tratada isolada.

**Objetivo:** identificar o que mudou no corte da `95db6421…` que desloca o componente **opaco** do
1º `usage` (achado da `TK-51`, `docs/CUSTO_DO_PICKUP.md` `## 11`) para as 6 janelas pós-corte
inteiras — não decidir corte nem rota, só a causa.

**Bloqueia:** `P-0737` (ver seção `## P-0737` — a premissa de custo fixo de abrir janela que o loop
constrói está contradita, não confirmada como estável).

**Escopamento (planejador, 2026-08-24):** o que faltava não era a rota, era o **método de
discriminação**. O opaco não é observável — só se mede por diferença (decisão 1 da `TK-51`) —, então
a investigação **não tenta reconstruir o payload**: ela localiza o degrau em três eixos
independentes (*quando*, *em que tipo de janela*, *em que projeto/máquina*) e só depois filtra
candidatos de superfície pela janela temporal medida. Sai em **duas** tarefas atômicas em ordem
dura, `TK-53a → TK-53b`; a primeira entrega valor sozinha (diz se o degrau é do produto, da máquina
ou do projeto), a segunda só é despachável com o insumo que a primeira publica.

**Fatos de corpus verificados no escopamento (o executor não os redescobre):**

1. **`95db6421…` é janela, não commit.** É o transcript
   `C:\Users\panta\.claude\projects\d--workspaces-PantonicApp\95db6421-3bbd-4938-b97d-f60a28435084.jsonl`.
   Não existe commit com esse sha e **não há arqueologia de git por ele**: o corte é o timestamp da
   1ª entrada desse arquivo (regra da `TK-51`, decisão 4), como já foi.
2. **Campos disponíveis por entrada do `.jsonl`** (lidos, não presumidos): `version` (versão do
   cliente), `cwd`, `gitBranch`, `sessionId`. Papel de janela de subagente **só** existe no sidecar
   `<sessão>/subagents/agent-*.meta.json` — `agentType` não é campo top-level (achado da `TK-51`).
3. **Bump de versão do cliente está descartado na fronteira:** `version` = **2.1.220** tanto na 1ª
   entrada da `08a29a54…` (controle, antes) quanto na da `95db6421…` (tratada, depois). A hipótese
   mais óbvia já está morta antes de custar turno; `version` segue como **co-variável publicada**,
   nunca como hipótese-mãe.
4. **Controle externo é provavelmente vazio:** os 14 `.jsonl` mais recentes de **todos** os
   diretórios de `C:\Users\panta\.claude\projects\` são do `d--workspaces-PantonicApp` — nenhum
   outro projeto tem janela no período pós-corte. Mede-se assim mesmo (é barato), mas nenhuma
   conclusão se apoia nele.

**Decisões do escopamento (fechadas aqui, o executor não as reabre):**

1. **Discriminar camada, não adivinhar payload.** Cada um dos três eixos descarta ou mantém
   **famílias inteiras** de candidatos: o eixo *tipo de janela* separa causa comum à máquina de
   causa que só a janela principal carrega; o eixo *projeto* separa global de local; o eixo
   *tempo* dá o filtro que torna o inventário de superfícies finito.
2. **Unidade, fórmula e corte não se remedem.** `usage_1 = input_tokens +
   cache_creation_input_tokens + cache_read_input_tokens` (calibrada pela `TK-51`), corpus e regra
   de corte idênticos. **Gate de calibração:** reproduzir os quatro números canônicos
   (34.260 / 34.292 / 45.872 / 46.071) **e** o grupo `antes` da Tabela A (`n=233`, mediana 34.347,
   máx 46.429). Não reproduziu → `blocked` razão `premissa`, sem publicar análise.
3. **O corpus é vivo e o `n` do grupo `depois` cresceu — isso é ganho, não divergência.** A `## 11`
   fechou `principal/depois` como **não isolado** por `n=6`; desde então novas janelas entraram. A
   `TK-53a` publica o `n_depois` **medido na data**, e a diferença para o 6 da `## 11` **não se
   retifica nem se explica**: é o próprio tempo dando à investigação o `n` que faltava. As janelas
   geradas pela própria investigação contam no corpus e o registro declara isso.
4. **Com `n` pequeno, publica-se linha a linha, não quantil.** A Tabela A mostra `depois` com mín
   34.644 e p25 37.500: o deslocamento **não é uniforme** nas 6. Quantil sobre `n` de um dígito
   esconde o formato do degrau.
5. **O discriminador principal é a janela de subagente.** Ela abre com outra superfície e sem o
   preâmbulo `/clear` da principal, na mesma máquina e no mesmo intervalo, e é o único controle com
   `n` suficiente (`pantonic-executor` n=161). Subiu junto → causa comum (cliente/máquina); não
   subiu → causa está no que a **principal** carrega.
6. **Câmbio chars→tok não sustenta conclusão.** O 0,590 chars/tok da `## 11` tem r²=0,030; ele entra
   só para continuidade de leitura com a Tabela B. Toda conclusão desta investigação se apoia em
   `usage_1` e `chars_preambulo` **brutos**.
7. **Candidato de causa se filtra por data, não por mérito.** A `TK-53b` só examina superfície cuja
   alteração cai dentro do bracket temporal que a `TK-53a` publica; fora do bracket é
   `descartado (fora da janela temporal)`, sem discussão. Superfície sem histórico (o que está em
   `C:\Users\panta\.claude\` e não está sob git) tem veredito máximo `não datável` — e publicar isso
   é resultado, não fracasso (herda a decisão 3 da `TK-51`: desfecho negativo é desfecho).
8. **Uma seção por tarefa, no relatório que já é o portador durável.** `## 12` é da `TK-53a`, `## 13`
   é da `TK-53b`, ambas em `docs/CUSTO_DO_PICKUP.md` (`DX-3`: o arquivo não se renomeia nem se
   duplica). Nenhuma das duas edita a seção da outra.
9. **Instrumento novo, descartável, desenho fixado no card** (`DX-4`, decisão 5 da `TK-51`): roda no
   scratchpad da sessão e não entra no repo. O executor implementa, não projeta.
10. **Medir não pode mexer no que se mede.** Nenhuma das duas tarefas altera prompt, agente, skill,
    memória, settings ou superfície de ferramenta: uma edição dessas durante a medição corrompe a
    série da `TK-53a` e a baseline futura.
11. **Não é sprint e não abre plano** (`P-0739` segue livre): duas tarefas de medição, três arquivos
    de registro, nenhuma superfície de `.claude/` tocada. **Reafirmado na revisão de plano de
    2026-08-24:** abrir um `docs/plans/P-0739-*.md` para esta matéria criaria um **segundo artefato
    vivo** disputando a mesma investigação, contra a *Regra de convergência* da skill
    `diario-de-obras` ("uma iniciativa tem no máximo UM plano vivo"). O desenho vive nesta seção,
    como o do `TK-51` viveu na dele; `P-0739` **não é alocado** e o `_INBOX.md` não é tocado.
12. **Nenhuma das duas tarefas escreve `status` no índice.** O `status` é **materializado** pelo
    `scrum-master` e só por ele; ao executor cabe **autorar** `review` ou `blocked` na linha de
    retorno (skill `diario-de-obras`, "Status — residência única"). Cada card edita **apenas** o seu
    bloco **Resultado** ao fim desta seção. O `TK-53` fecha quando o `scrum-master` materializa
    `done` após o laudo da `TK-53b` — não é ato do executor nem critério de pronto dele. (Corrige
    três defeitos do escopamento original: a célula `doing`, que **não é estado válido** da lista
    canônica — `triage`/`ready`/`blocked`/`in-progress`/`review`/`done`/`cancelled` —, e as duas
    cláusulas que punham o executor escrevendo a coluna `Status`.)

### TK-53a — Onde e quando o degrau do 1º usage acontece [Sonnet · classe investigacao]

- **Status:** `done` · 2026-08-31
- **Objetivo:** publicar, em número, **três discriminações** sobre o degrau do componente opaco:
  (i) a **janela temporal** em que ele aparece na série de janelas principais; (ii) se ele atinge
  **também** janelas de subagente; (iii) se ele atinge **outros projetos** da mesma máquina. A
  tarefa mede e publica; **não nomeia causa**, não propõe corte e não escolhe rota.
- **Arquivos-alvo:**
  - `<scratchpad da sessão>/sonda_dx6.py` — **novo**, stdlib apenas (sem `numpy`/`pandas`),
    descartável, fora do repo.
  - `<scratchpad da sessão>/serie_dx6.tsv` — saída da sonda, uma linha por janela.
  - `d:\workspaces\PantonicApp\docs\CUSTO_DO_PICKUP.md` — acrescenta `## 12 Onde e quando o degrau
    do 1º usage acontece (<data>)`, **≤ 50 linhas**, ao fim do arquivo.
  - `d:\workspaces\PantonicApp\docs\DOC_MAP.md` — na entrada `## docs/CUSTO_DO_PICKUP.md`,
    acrescentar a linha da `## 12` na lista de seções (mesmo formato das linhas `## 9`/`## 10`/
    `## 11`) e atualizar o `(~351 linhas)` do cabeçalho por `(Get-Content f).Count`.
  - `d:\workspaces\PantonicApp\docs\DIARIO_DE_OBRAS.md` — bloco **Resultado da `TK-53a`** ao fim
    desta seção, e **nada mais**: a linha `TK-53` do índice não se toca (decisão 12).
- **Corpus:** `C:\Users\panta\.claude\projects\` inteiro. Janela **principal** = `*.jsonl` na raiz de
  um diretório de projeto; janela de **subagente** = `<sessão>/subagents/agent-*.jsonl`, papel lido
  do sidecar `agent-*.meta.json` (único lugar onde o papel existe). **Corte:** timestamp da 1ª
  entrada de `d--workspaces-PantonicApp\95db6421-3bbd-4938-b97d-f60a28435084.jsonl` — mesmo corte da
  `TK-51`, sem arqueologia de data.
- **Sonda `sonda_dx6.py` — desenho fechado:** para cada `.jsonl`, ler **linha a linha** e **parar na
  primeira entrada `assistant` que traga `usage`** (nunca carregar o arquivo inteiro). Uma linha de
  `serie_dx6.tsv` por janela, com: `projeto` (nome do diretório), `arquivo`, `ts_inicio`, `escopo`
  (`principal` ou `subagente:<papel>`), `input_tokens`, `cache_creation_input_tokens`,
  `cache_read_input_tokens`, `usage_1` (a soma), `chars_preambulo` (soma dos chars de todo texto
  anterior à 1ª `assistant`), `version`, `gitBranch`. **Proibido imprimir conteúdo bruto de
  transcript** — `stdout` traz **apenas** as agregações abaixo, em ≤ 40 linhas.
- **As três medidas que a sonda imprime:**
  - **M-A — quando.** (a) Série **diária** das janelas principais do `d--workspaces-PantonicApp` nos
    7 dias que terminam na janela mais recente: `dia`, `n`, `mediana`, `n com usage_1 ≥ 40.000`.
    (b) As janelas principais do grupo `depois` **linha a linha** e as **5** imediatamente anteriores
    ao corte: `ts_inicio`, `usage_1`, os três componentes, `chars_preambulo`, `version`. (c) Duas
    linhas de contexto: `janelas ≥ 40.000 tok no grupo antes: <n> de 233; ts da mais recente: <ts>`.
    O limiar 40.000 é **rótulo operacional** desta tabela (cai entre as duas medianas do registro,
    34.347 e 46.070), não constante nova de produto — declarar assim na seção.
  - **M-B — em que tipo de janela.** Para cada papel de subagente com `n_total ≥ 10`: `n_antes`,
    `mediana_antes`, `n_depois`, `mediana_depois`, `Δ mediana`. Se **nenhum** papel tiver
    `n_depois ≥ 3`, imprimir `controle interno insuficiente (n_depois máx = <n>)` e não concluir
    nada sobre camada.
  - **M-C — em que projeto.** Para **cada** diretório de `C:\Users\panta\.claude\projects\` com ao
    menos uma janela principal: `projeto`, `n_antes` (14 dias antes do corte), `mediana_antes`,
    `n_depois`, `mediana_depois`. Se todo projeto ≠ `d--workspaces-PantonicApp` fechar com
    `n_depois = 0`, imprimir `controle externo ausente`.
- **Gate de calibração (antes de qualquer interpretação):** a sonda tem de reproduzir os quatro
  números do registro (34.260 / 34.292 / 45.872 / 46.071) **e** o grupo `antes` da Tabela A da
  `## 11` (`n=233`, mediana 34.347, máx 46.429). Se qualquer um não reproduzir, a tarefa **para**,
  não publica análise e devolve `blocked` razão `premissa`. O `n_depois` **não** faz parte do gate
  (decisão 3).
- **Formato do achado — `## 12`, estrutura fixa:** (1) sonda, corpus, corte e fórmula herdados, com o
  gate declarado e o `n_depois` medido na data; (2) **Tabela A** (M-A a: série diária); (3)
  **Tabela B** (M-A b: janelas linha a linha) + as duas linhas de contexto (M-A c); (4) **Tabela C**
  (M-B: papéis antes × depois); (5) **Tabela D** (M-C: projetos); (6) **Veredito**, vocabulário
  fechado, **uma linha por eixo** — eixo tempo: `degrau em <ts_a> → <ts_b>` · `sem degrau (oscilação
  pré-existente)`; eixo janela: `também em subagente` · `só na principal` · `não isolado (n
  insuficiente)`; eixo projeto: `também fora do projeto` · `só no projeto` · `controle externo
  ausente`; (7) **linha de fecho obrigatória**, literalmente rotulada
  `Janela temporal do degrau: <ts_a> → <ts_b>` (ou `indefinida`), onde `ts_a` = `ts_inicio` da última
  janela principal com `usage_1 < 40.000` anterior à `95db6421…` e `ts_b` = `ts_inicio` da
  `95db6421…`. Essa linha é o **insumo único** da `TK-53b`. Nenhuma célula com número sem
  proveniência medida; nenhuma constante nova (o dono já recusou número mágico, `## 9`).
- **Proibido:** nomear causa ou candidato de causa (é matéria da `TK-53b`); propor, recomendar ou
  executar qualquer corte; editar qualquer arquivo sob `.claude/`; alterar prompt, agente, skill,
  memória ou superfície de ferramenta (decisão 10); versionar a sonda ou o TSV; retificar
  `docs/telemetria.tsv` (`DX-12`); reabrir `docs/plans/P-0738-contexto-esgotado.md`, que está `done`.
- **Verificação:** o gate aparece declarado com os quatro números e as três estatísticas do grupo
  `antes`; as quatro tabelas, as linhas de veredito por eixo e a linha `Janela temporal do degrau:`
  existem; `## 12` ≤ 50 linhas (`(Get-Content docs/CUSTO_DO_PICKUP.md).Count` antes e depois, ambos
  registrados no bloco Resultado); `git status --short` acusa **apenas**
  `docs/CUSTO_DO_PICKUP.md`, `docs/DOC_MAP.md`, `docs/DIARIO_DE_OBRAS.md` e **nenhum arquivo novo**.
- **Pronto quando:** a `## 12` publica os três eixos com número e `n`, o veredito traz uma linha por
  eixo no vocabulário fechado, e a linha `Janela temporal do degrau:` está fechada — com dois
  timestamps ou com `indefinida`.

### TK-53b — Que superfície mudou dentro da janela do degrau [Sonnet · classe investigacao]

- **Status:** `cancelled` · 2026-08-31
- **Insumo obrigatório (pré-condição de despacho, verificada pelo `scrum-master`):** a linha
  `Janela temporal do degrau: <ts_a> → <ts_b>` da `## 12`. Se a `TK-53a` publicar `indefinida`, esta
  tarefa **não é despachada** e o tíquete volta ao planejamento — não é ramo dentro da tarefa.
- **Objetivo:** para cada superfície que entra no prompt e **não** no transcript, dizer se ela mudou
  **dentro do bracket** e por quanto (chars e tok), fechando cada item com veredito de vocabulário
  fixo, e publicar a **conta de fechamento** (quanto do degrau os candidatos datáveis explicam). A
  tarefa mede e publica; não escolhe rota, não propõe corte e não altera nenhuma superfície.
- **Arquivos-alvo:**
  - `d:\workspaces\PantonicApp\docs\CUSTO_DO_PICKUP.md` — acrescenta `## 13 Que superfície mudou
    dentro da janela do degrau (<data>)`, **≤ 45 linhas**, ao fim do arquivo.
  - `d:\workspaces\PantonicApp\docs\DOC_MAP.md` — linha da `## 13` na lista de seções + contagem do
    cabeçalho atualizada.
  - `d:\workspaces\PantonicApp\docs\DIARIO_DE_OBRAS.md` — bloco **Resultado da `TK-53b`** ao fim
    desta seção, e **nada mais**: a linha `TK-53` do índice não se toca (decisão 12).
- **Inventário fechado — o executor não acrescenta itens; o que aparecer fora da lista vira linha de
  achado, não linha de tabela:**
  - **Camada repo (datável por git):** `d:\workspaces\PantonicApp\CLAUDE.md` (se existir),
    `.claude/agents/*.md`, `.claude/skills/*/SKILL.md`, `.claude/global/CLAUDE.md`,
    `.claude/settings.json`, `.claude/settings.local.json`, `.mcp.json`, `.claude/plugins/**` e
    `.claude/hooks/**` (se existirem).
  - **Camada máquina (datável só por `LastWriteTime`):** `C:\Users\panta\.claude\CLAUDE.md`,
    `C:\Users\panta\.claude\settings.json`, `C:\Users\panta\.claude\agents\*.md`,
    `C:\Users\panta\.claude\skills\**\SKILL.md`,
    `C:\Users\panta\.claude\projects\d--workspaces-PantonicApp\memory\*.md`,
    `C:\Users\panta\.claude\plugins\**`, e as chaves de superfície de `C:\Users\panta\.claude.json`
    (`mcpServers` e as de plugin habilitado).
- **Método, fixado:**
  1. **Repo:** `git log --since=<ts_a> --until=<ts_b> --name-only --pretty=format:"%h|%ad" -- <paths
     do inventário>`; para cada arquivo tocado, Δ chars entre `git show <sha_antes>:<path>` e
     `git show <sha_depois>:<path>`. **Nunca** `git checkout`/`stash`/`restore` e nunca escrever na
     árvore. Mudança **não commitada** de item do inventário conta com a data de `LastWriteTime`, e
     a seção marca a linha como `(não commitada)`.
  2. **Máquina:** `Get-ChildItem -Recurse` dos caminhos acima, projetando só `Name`, `Length`,
     `LastWriteTime`; entram na tabela apenas os itens com `LastWriteTime` dentro do bracket. Para
     `SKILL.md` e `*.md` de agente, medir **frontmatter e corpo separados** — só o frontmatter entra
     no catálogo anunciado.
  3. **`C:\Users\panta\.claude.json` é caso especial:** o arquivo tem churn de estado de sessão, logo
     `LastWriteTime` dele **não é evidência**. Mede-se o tamanho em chars **apenas** das chaves de
     superfície, hoje, e o veredito máximo é `não datável`. **Proibido despejar o arquivo** ou
     qualquer trecho dele no registro.
  4. Conversão chars→tok: mesma da `## 11`, declarada com a ressalva de r²=0,030; a comparação com o
     degrau é de **ordem de grandeza**, e a seção diz isso.
- **Veredito por item, vocabulário fechado:** `descartado (fora da janela temporal)` ·
  `descartado (Δ < 500 tok)` · `compatível (Δ = <N> tok, dentro da janela)` ·
  `não datável (sem histórico; tamanho atual <N> tok)`.
- **Conta de fechamento (obrigatória, uma linha):** `soma dos Δ compatíveis = <N> tok; degrau medido
  = <M> tok (## 11/## 12); explicado = <N/M>%`. E a **linha de fecho**: *"O degrau é **compatível
  com** `<item(ns)>`"* ou *"**não isolado** — os candidatos datáveis explicam `<pct>`% do degrau; o
  restante está em superfície não datável (`<lista>`)"*.
- **Proibido:** **alterar qualquer superfície do inventário** — medir é ler, e uma edição aqui
  corrompe a série da `TK-53a` e a baseline futura (decisão 10); propor, recomendar ou executar
  corte; decidir rota; `git checkout`/`stash`/`restore`; copiar conteúdo de memória, de `CLAUDE.md`
  ou de `.claude.json` para o registro (só medida agregada); retificar `docs/telemetria.tsv`;
  reabrir `P-0738`.
- **Verificação:** todo item do inventário aparece na tabela com um dos quatro vereditos; a conta de
  fechamento traz numerador, denominador e percentual; `## 13` ≤ 45 linhas (contagem antes e depois
  registrada no bloco Resultado); `git status --short` acusa **apenas** os três arquivos de registro
  e **nenhum arquivo novo**.
- **Pronto quando:** cada superfície do inventário tem veredito com número, a conta de fechamento e a
  linha de fecho estão publicadas — nomeando o(s) item(ns) compatível(is) ou declarando
  `não isolado` com o que ficou sem histórico. O fecho do `TK-53` no índice **não** é critério de
  pronto desta tarefa (decisão 12).

**Ordem e dependência dura:** `TK-53a → TK-53b`, linear, sem ramo. A `TK-53b` consome **uma** linha
da `## 12` (a `Janela temporal do degrau:`) e nada mais — nenhuma das duas depende do scratchpad da
outra, e trocar de contexto entre elas não custa remedição (`DC-5`). A `TK-53a` entrega valor
sozinha: mesmo que a `TK-53b` nunca rode, o dono já sabe se o degrau é do produto, da máquina ou do
projeto — e o `P-0737` já pode ser reavaliado com isso.

**Nota ao dono (registrada no escopamento, não decidida aqui):**

1. **Não vira plano formal, e `P-0739` segue livre.** A matéria destas duas tarefas é **medição**:
   nenhuma altera arquitetura do loop. Se a `TK-53b` fechar `compatível` com uma superfície de
   `.claude/` cuja mudança altere **responsabilidade** de papel, a **rota** é matéria do `P-0737`
   (a `DX-9` já pôs superfície de ferramenta fora do `P-0738`) — não de um plano novo.
2. **A hipótese mais óbvia já está descartada de graça:** o cliente era `2.1.220` dos dois lados da
   fronteira (fato de corpus 3). Quem revisar não deve cobrar essa via.
3. **Revisão cai no buraco do Achado 1 do laudo `DIARIO-TK-51.md`:** `review_evidence.py` não aceita
   tíquete residente no diário, então a metade mecânica terá de ser reproduzida à mão enquanto o
   tíquete do `_INBOX.md` não fechar. Não é bloqueio de despacho.
4. **Teto do arquivo estourado, sem rota decidida:** `docs/CUSTO_DO_PICKUP.md` já está em 351 linhas
   contra as 320 da `DX-3` (orçamento do `P-0738`, `done`), e as duas seções novas o levam a ~440.
   Nenhuma das tarefas renomeia nem parte o arquivo (`DX-3`); partir/arquivar é decisão do dono.

**Resultado da `TK-53a`:** Medido em `docs/CUSTO_DO_PICKUP.md` `## 12 Onde e quando o degrau do 1º
usage acontece (2026-08-24)`. Sonda `sonda_dx6.py` (scratchpad) reproduziu o gate: as 4 canônicas
(34.260/34.292/45.872/46.071) e o grupo `antes` da Tabela A da `## 11` (n=233, mediana 34.347, máx
46.429) — **PASS**. `n_depois` medido hoje (`d--workspaces-PantonicApp`): **9** (cresceu do `n=6`
da `## 11`, decisão 3). **Eixo tempo:** sem degrau (oscilação pré-existente) — `08-20` já tinha
mediana 46.349 (acima de `08-24`) e 45/233 janelas `antes` já cruzavam 40.000; o grupo `depois`
mistura 2 valores em ~34.644 com o restante em ~46k. **Eixo janela:** só na principal —
`pantonic-executor` (n_depois=4) sobe +1.183 tok (+3,4%) e `pantonic-planner` (n_depois=3) cai
−360 tok, ambos muito abaixo do salto de ~+11.700 tok (+34%) da principal. **Eixo projeto:**
controle externo ausente — nenhum projeto ≠ `d--workspaces-PantonicApp` tem janela `depois` do
corte. Tarefa mede e publica — não nomeia causa, não propõe corte, não escolhe rota.

`docs/CUSTO_DO_PICKUP.md`: 351 → 402 linhas (`## 12` = 50 linhas, dentro do limite). `git status
--short` acusa apenas `docs/CUSTO_DO_PICKUP.md`, `docs/DOC_MAP.md`, `docs/DIARIO_DE_OBRAS.md` —
nenhum arquivo novo (a sonda e o `serie_dx6.tsv` vivem no scratchpad da sessão).

**Janela temporal do degrau:** `2026-08-24T06:50:09.164Z → 2026-08-24T07:18:55.063Z` — insumo
único da `TK-53b`.

**Ressalva do orquestrador (2026-08-24):** o eixo tempo fechou `sem degrau (oscilação
pré-existente)`, que **contradiz a premissa** com que o `TK-53` foi aberto (decisão do dono de
2026-08-24: "deslocamento real, não ruído"). A decisão sobre o que fazer com essa contradição é do
dono e **precede** o despacho da `TK-53b`. Consumo: ver `docs/telemetria.tsv`.

**Decisão do dono sobre a ressalva — 2026-08-31:** a contradição fecha o `TK-53` com **desfecho
negativo** e `TK-53b` **cancelada por absorção**. Nenhuma das três rotas apresentadas foi aceita,
porque todas terminavam num número: *"não consigo tomar uma decisão só com esse número, sem um
detalhamento se o custo é válido, necessário, dispensável ou possível de economizar. Enquanto eu
não tiver essa visão desse custo, não vamos seguir adiante, pois todo esse plano se iniciou na
percepção minha de que cada tarefa deste projeto estava esgotando muito rapidamente os recursos."*
A pergunta viva deixa de ser *o que mudou* e passa a ser *do que o custo é feito* — `## TK-54`.

---

## TK-54 — Extrato do custo de abertura de uma janela principal

- **Status:** `ready` · 2026-08-31

**Origem:** diretiva do dono, 2026-08-31 (citada acima), no ato de fechar a `TK-53`.

**Diretiva de priorização vigente de 2026-08-31 a 2026-09-15 (movida verbatim em 2026-09-15, registro do `P-0739`, `DB-11`):**

> **Diretiva de priorização:** (dono, 2026-08-31) **o extrato do custo de abertura de janela vem
> antes de tudo.** Nenhuma outra iniciativa avança — nem a `P-0737`, nem a `TK-38` — enquanto não
> houver o detalhamento do custo por fonte, classificado em *válido / necessário / dispensável /
> economizável*. Número agregado não decide nada; o plano inteiro nasceu da percepção de que cada
> tarefa esgota os recursos rápido demais, e é essa percepção que o extrato tem que atender.
> Âncora: `## TK-54`.

**Objetivo:** publicar o **extrato** do 1º `usage` de uma janela principal deste projeto — **uma
linha por fonte carregada**, com tamanho medido, estrato de origem e **classificação proposta** em
*válido / necessário / dispensável / economizável*. A tarefa mede, ranqueia e propõe; **a
ratificação da classificação é do dono** e nenhum corte acontece nesta rodada.

**Bloqueia:** `P-0737` (razão vigente na seção `## P-0737`).

**Fato que torna a tarefa viável (verificado no escopamento, 2026-08-31 — o executor não
redescobre):** o obstáculo da `TK-51` — *"o componente opaco só se mede por diferença"* — era sobre
**reconstruir o payload a partir do transcript**. O extrato não faz isso: ele **enumera as fontes em
disco** que o harness carrega e mede cada uma direto no arquivo. Censo de viabilidade já rodado:

| fonte | chars |
|---|---|
| `C:\Users\panta\.claude\CLAUDE.md` (cópia implantada) | 10.751 |
| `MEMORY.md` do projeto | 837 |
| `SKILL.md` locais **inteiros** (n=17, projeto + global) | 120.523 |
| `agents/*.md` locais **inteiros** (n=9) | 39.572 |
| linhas `description:` das 17 skills (o que de fato vai para a listagem) | 5.677 |

Os dois números de "arquivo inteiro" são **teto, não medida da janela principal**: a listagem
carrega `name` + `description`, e o corpo do `SKILL.md` só entra quando a skill é invocada.
Distinguir *carregado sempre* de *carregado sob demanda* é parte do entregável, não premissa.

**Decisões do escopamento (fechadas aqui; o executor não as reabre):**

1. **Medir em chars; não converter para tokens.** O câmbio 0,590 chars/tok da `## 11` tem r²=0,030
   e a decisão 6 da `TK-53` já o proibiu como base de conclusão. O extrato ranqueia por chars — que
   é o que responde *"vale a pena cortar?"*. A reconciliação com o `usage_1` medido entra como
   **faixa**, com a incerteza declarada, nunca como número fechado.
2. **Três estratos, nesta ordem.** **E1 — fontes nossas** (editáveis por nós): `CLAUDE.md` global,
   `MEMORY.md` + memórias recuperadas, listagem de skills (`name`+`description`), listagem de
   agentes, bloco `gitStatus` (status + commits recentes), bloco de environment (a lista de
   diretórios de trabalho adicionais), hooks de `settings.json`. **E2 — fontes do harness** (não
   editáveis por nós): system prompt do Claude Code, schemas das ferramentas carregadas, skills
   embutidas. **E3 — residual:** `usage_1` medido − (E1 + E2).
3. **E2 e E3 dimensionam-se por diferença, não por adivinhação.** Nada em `.claude/` produz o
   system prompt do harness; ele entra como bloco único, classificado `fixo — fora do nosso
   alcance`. Residual grande publica-se como `não atribuído` — desfecho negativo é desfecho
   (decisão 3 da `TK-51`).
4. **Não mexer no que se mede** (herda decisão 10 da `TK-53`): a tarefa **não** edita skill,
   agente, memória, `CLAUDE.md` ou settings. Cortar é rodada seguinte, depois da ratificação.
5. **Portador:** `docs/CUSTO_DO_PICKUP.md` (`DX-3`: não se renomeia nem se duplica) —
   `## 13` para a `TK-54a`, `## 14` para a `TK-54b`. `docs/DOC_MAP.md` atualizado por tarefa.
   Bloco **Resultado** ao fim desta seção. A linha do índice não se toca.
6. **Duas tarefas independentes, uma por contexto** — o extrato (`TK-54a`) e a fonte da
   bimodalidade (`TK-54b`) são perguntas separadas e nenhuma é insumo da outra; separá-las evita o
   alvo duplo que o gate de delegação proíbe. `TK-54a` primeiro, por ser a que o dono pediu.
7. **Não abre plano** (`P-0739` segue livre) — mesma razão da decisão 11 da `TK-53`.

### TK-54a — O extrato [Sonnet · classe investigacao]

- **Status:** `done` · 2026-09-18 — executada inline pela orquestração em 2026-09-18; `## 13` publicada em `docs/CUSTO_DO_PICKUP.md:404-431`

Reaberta no mesmo dia pela rodada `RP-TK54-1`, rota **A**. A coluna de
classificação vem **fixada neste card**: o executor **transcreve** o valor e a justificativa da
tabela `B` abaixo, não avalia e não propõe classificação própria.

- **Objetivo:** publicar a seção `## 13` de `docs/CUSTO_DO_PICKUP.md` — uma linha por fonte
  carregada, com `chars` medidos, estrato, regime, participação nos três regimes de `usage_1` e a
  classificação já fixada — e registrar a seção em `docs/DOC_MAP.md`. **Não corta nada e não propõe
  rota de corte.**
- **Depende de:** decisões 1..7 de `## TK-54` (copiadas inline no que vinculam), a
  `### Medição de 2026-09-18` da mesma seção e a rodada `RP-TK54-1` (`AE-1`).

**Vocabulário fechado (termos usados nas células, com a definição que vale aqui):**
`usage_1` = `input`+`cache_read`+`cache_creation` da 1ª entrada `assistant` de uma janela
principal · `E1` = fonte nossa, editável por nós · `E2` = fonte do harness, não editável por nós ·
`E3` = residual (`usage_1` − E1 − E2) · regime `sempre` = entra no preâmbulo de toda janela ·
regime `sob demanda` = só entra quando invocada, e o `chars` publicado é **teto**, não custo da
janela.

**A. Rubrica das quatro categorias — residência única.** Esta lista é a **única** enunciação da
rubrica no projeto; nada a repete em outro lugar. Cada categoria nomeia **o que a rodada de corte
faz com aquela linha**, e as quatro são exaustivas e mutuamente exclusivas sob esta ordem:

1. `dispensável` — a fonte sai da janela e não precisa voltar (é re-derivável por comando quando
   alguém precisar dela).
2. `necessário` — o conteúdo tem de continuar **alcançável**, mas não **carregado**: já está, ou
   pode passar a estar, atrás de um ponteiro que o traz sob demanda.
3. `economizável` — continua carregado sempre, e a **mesma** informação cabe em menos chars
   (condensar, deduplicar, encurtar campo). Nada sai da janela.
4. `válido` — continua carregado sempre e **já está na forma mínima**: a rodada de corte não mexe.

Fora de E1 valem dois rótulos fixos (decisão 3 de `## TK-54`): E2 recebe
`fixo — fora do nosso alcance`; E3 recebe `não atribuído`. E vale a regra **R0**: linha cujo custo
na janela não é observável ou cuja fonte não existe em disco recebe `—` (sem classificação), com a
justificativa literal que a contingência correspondente prescreve.

**B. Inventário fechado de E1 e a classificação fixada.** São **dez** linhas, derivadas da decisão
2 de `## TK-54` (a enumeração de E1), do censo de 2026-08-31 e da `### Medição de 2026-09-18`. O
executor mede o `chars` de cada uma pela receita da coluna *medida* e copia `classificação` e
*justificativa* como estão. Onde a justificativa cita um número medido, ele substitui pelo valor
que a sonda mediu, sem trocar o resto da frase.

| # | fonte e medida | regime | classificação | justificativa (literal, uma linha) |
|---|---|---|---|---|
| 1 | `C:\Users\panta\.claude\CLAUDE.md` — `len` do arquivo | sempre | `economizável` | Norma que o agente aplica sem ser mandado buscá-la, então não vira ponteiro; mas cresceu 1.563 ch desde 2026-08-31 e carrega blocos de motivo e narrativa de incidente que não mudam o que o agente faz. |
| 2 | `C:\Users\panta\.claude\projects\d--workspaces-PantonicApp\memory\MEMORY.md` — `len` do arquivo | sempre | `economizável` | Índice insubstituível (é o ponteiro de toda memória do projeto), mas suas 5 linhas-hook somam 817 ch, acima do teto de 120 ch por linha que a Regra 4 do `CLAUDE.md` global prescreve — a folga é de forma. |
| 3 | `…\memory\*.md` exceto `MEMORY.md` e `_INBOX.md` — soma dos `len` | sob demanda | `necessário` | Conteúdo que só entra quando alguém o puxa pelo índice; já está no regime que a rodada de corte buscaria, e o número publicado é teto, não custo de janela. |
| 4 | linhas `name:` + `description:` dos `SKILL.md` (n=17, projeto + global) — soma dos `len` | sempre | `economizável` | É a única porta de invocação de skill (não sai da janela e não vira ponteiro), mas 5.984 ch em 17 descrições é forma: encurtar `description` não retira skill nenhuma. |
| 5 | `SKILL.md` **inteiros** (n=17, projeto + global) — soma dos `len` | sob demanda | `necessário` | O corpo da skill só entra quando ela é invocada; o teto de 120.523 ch mede o que a listagem evita carregar, e é esse arranjo que a rodada de corte preserva. |
| 6 | frontmatter dos `agents/*.md` (n=9, projeto + global) — soma dos `len` do bloco entre as duas linhas `---` | sempre | `economizável` | É o que torna cada agente selecionável (não sai e não vira ponteiro), mas 3.104 ch em 9 frontmatters é forma, não capacidade. |
| 7 | `agents/*.md` **inteiros** (n=9) — soma dos `len` | sob demanda | `necessário` | O corpo do agente entra na janela dele, não na principal; o teto de 39.572 ch mede o que o frontmatter evita carregar. |
| 8 | bloco `gitStatus` — `len` da saída de `git status` mais a de `git log -5 --oneline`, rodadas em `D:\workspaces\PantonicApp` | sempre | `dispensável` | Dado re-derivável por dois comandos de uma linha no instante em que alguém precisar dele; carregá-lo em toda janela paga adiantado por informação que a janela pode buscar. |
| 9 | bloco de environment, diretórios de trabalho adicionais — soma dos comprimentos dos caminhos da chave `additionalDirectories` mais 4 chars por entrada | sempre | `economizável` | Projeção literal de uma chave de config nossa: o tamanho é escolha de configuração, editável sem tocar em artefato nenhum do projeto. |
| 10 | hooks de `settings.json` — `len` do JSON serializado da chave `hooks` de `C:\Users\panta\.claude\settings.json` | não observável por sonda em disco | `—` | A sonda mede o teto em disco; se este bloco entra ou não no preâmbulo da janela principal não é observável de dentro de um subagente, e sem o regime observado não há custo de janela a classificar. |

**Nota literal a publicar logo abaixo da tabela em `## 13`:** `válido` não tem ocorrência neste
extrato — nenhuma fonte de E1 carregada sempre está na forma mínima. A ausência é resultado
medido, não omissão.

**C. Forma da tabela de `## 13`.** Colunas, nesta ordem: `# | fonte | caminho ou comando medido |
chars | estrato | regime | %34.600 | %46.100 | %60.472 | classificação | justificativa`. Linhas: as
dez de E1, na ordem da tabela `B`, mais a linha de E2 e a de E3. Células `%` de linha `sob demanda`
vão **entre parênteses** (é teto, não custo fixo). Exemplos trabalhados, um por caso que as regras
deste card admitem — o executor reproduz a forma, com os números que mediu:

| # | fonte | caminho ou comando medido | chars | estrato | regime | %34.600 | %46.100 | %60.472 | classificação | justificativa |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `CLAUDE.md` global | `C:\Users\panta\.claude\CLAUDE.md` | 12.314 | E1 | sempre | 8,9% | 6,7% | 5,1% | `economizável` | Norma que o agente aplica sem ser mandado buscá-la… |
| 5 | corpos dos `SKILL.md` (n=17) | `…\.claude\skills\*\SKILL.md` | 120.523 | E1 | sob demanda | (87,1%) | (65,4%) | (49,8%) | `necessário` | O corpo da skill só entra quando ela é invocada… |
| 10 | hooks de `settings.json` | chave `hooks` de `C:\Users\panta\.claude\settings.json` | *(medido)* | E1 | não observável | — | — | — | `—` | A sonda mede o teto em disco… |
| 11 | fontes do harness (bloco único) | não produzido por nada em `.claude/` | não medido | E2 | sempre | — | — | — | `fixo — fora do nosso alcance` | Nada em `.claude/` produz o system prompt do harness, os schemas de ferramenta ou as skills embutidas; e esta rodada não separa E2 de E3. |
| 12 | residual | `usage_1` − E1 | — | E3 | sempre | 78,6%–86,6% | 83,9%–90,4% | 87,8%–92,6% | `não atribuído` | Inclui o E2 inteiro: separar E2 de E3 exige medida que esta rodada não tem. |

**D. Fórmulas (as únicas conversões permitidas; decisão 1 de `## TK-54` proíbe o câmbio 0,590 da
`## 11` e exige faixa na reconciliação):**
- **F1** `E1_ch` = soma da coluna `chars` das linhas de E1 com regime `sempre`. Linhas `sob
  demanda`, `—` e `não medido` **não** entram na soma.
- **F2** faixa de tokens: `E1_tok_min` = arredondar(`E1_ch` / 5) · `E1_tok_max` =
  arredondar(`E1_ch` / 3). O divisor central 4 é o que a `### Medição de 2026-09-18` usou
  (22.219 ch ≈ 5.554 tk); a faixa ±25% em torno dele é a incerteza declarada.
- **F3** para cada regime `R` ∈ {34.600, 46.100, 60.472}: `E3_min` = `R` − `E1_tok_max` ·
  `E3_max` = `R` − `E1_tok_min`; a célula `%` do E3 publica `E3_min/R` – `E3_max/R`.
- **F4** célula `%R` de uma linha comum = arredondar(`chars`/4) ÷ `R`, com uma casa decimal. O
  divisor 4 vale só para ranquear; nenhuma conclusão deste extrato se apoia nele.

**E. Frase de consequência — a publicar em `## 13` logo após as tabelas.** Primeiro parágrafo,
recalculado com os números medidos pelas fórmulas F1–F3. O exemplo trabalhado abaixo usa o `E1_ch`
de 2026-09-18 (22.219 ch), que somava só as quatro fontes medidas naquele dia — as linhas 1, 2, 4 e
6; o `E1_ch` desta tarefa soma também as linhas 8 e 9, e por isso **não** tem de reproduzir 22.219: *"Zerar todo o E1 — apagar o `CLAUDE.md` global, as 17 skills, os 9 agentes
e a memória do projeto — levaria o `usage_1` de 60.472 tk (30,2% de uma janela de 200k) para algo
entre 53.066 e 56.028 tk, isto é, entre 26,5% e 28,0%."* Segundo parágrafo, **literal, copiado sem
recálculo**: *"A meta de <10% é inatingível por qualquer corte em fonte nossa: mesmo que o E1
medido fosse o triplo do que é, zerá-lo inteiro deixaria 38.253 tk — 19,1%. O alvo obrigatório é o
E2: schemas de ferramenta, skills embutidas e system prompt do harness."*

**F. Notas de honestidade — literais, a publicar ao fim de `## 13`:** *"A linha de E3 fecha os três
regimes por construção, porque é a diferença; o que este extrato afirma com medida é a participação
de E1."* · *"E1 é medido em 2026-09-18; os regimes 34.600 e 46.100 são de 2026-08-24, quando o
`CLAUDE.md` global tinha 10.751 ch — a reconciliação nesses dois regimes é aproximada, e é por isso
que ela sai como faixa."* · *"As linhas 8, 9 e 10 são medidas por proxy em disco ou por comando, não
por leitura do preâmbulo de uma janela principal."*

**Arquivos-alvo:**
- `docs/CUSTO_DO_PICKUP.md:402` — última linha do arquivo,
  `Janela temporal do degrau: 2026-08-24T06:50:09.164Z → 2026-08-24T07:18:55.063Z`; a seção nova é
  apensada **depois** dela, com o heading literal
  `## 13 Extrato do custo de abertura de uma janela principal (2026-09-18, TK-54a)`.
- `docs/DOC_MAP.md:104` — `## docs/CUSTO_DO_PICKUP.md (~402 linhas)`.
- `docs/DOC_MAP.md:128` — último bullet da lista de seções (`## 12 Onde e quando o degrau…`); o
  bullet novo entra depois dele e antes de `**Acesso:**` (linha 129).

**Método de sondagem:** sonda descartável em
`C:\Users\panta\AppData\Local\Temp\claude\d--workspaces-PantonicApp\<sessão>\scratchpad`, Python
stdlib apenas, fora do repo, apagada ao fim. Corpus fechado: as dez linhas da tabela `B`. Métrica
única: `chars` = `len(texto)` do arquivo ou do bloco, sem normalizar. Nenhum conteúdo de arquivo
entra em contexto — o que volta é a tabela pronta.

**Passos:**
1. Escrever a sonda no scratchpad, com uma função por linha do inventário `B`.
2. Rodar a sonda e coletar os dez valores de `chars`.
3. Calcular `E1_ch` (F1), a faixa de tokens (F2), as células `%` (F4) e a linha de E3 (F3).
4. Apensar a seção `## 13` ao fim de `docs/CUSTO_DO_PICKUP.md`, com as tabelas da forma `C`, a nota
   do `válido` vazio, a frase de consequência `E` e as notas `F`.
5. Em `docs/DOC_MAP.md:104`, trocar `(~402 linhas)` pelo valor de
   `(Get-Content docs\CUSTO_DO_PICKUP.md).Count` arredondado; depois da linha 128, inserir o bullet
   `` - `## 13 Extrato do custo de abertura de uma janela principal (2026-09-18)` — uma linha por fonte carregada, com chars medidos, estrato E1/E2/E3, regime e a classificação que o dono ratifica ``.
6. Apagar a sonda do scratchpad.
7. Devolver a linha de retorno: caminho e range de linhas de `## 13`, `E1_ch` medido, e uma linha
   `contingência <n> acionada: <o que mudou>` por contingência disparada.

**Restrições desta tarefa (copiadas inline; não há ponteiro a seguir):**
- Medir em chars. Converter para token só pelas fórmulas F2–F4; o câmbio 0,590 chars/tok da `## 11`
  é proibido como base de qualquer conclusão (r²=0,030).
- Não mexer no que se mede: a tarefa **não** edita `CLAUDE.md`, skill, agente, memória nem
  `settings.json`. Cortar é rodada seguinte, depois da ratificação do dono.
- O portador é `docs/CUSTO_DO_PICKUP.md` e não se renomeia nem se duplica (`DX-3`); nenhuma seção
  existente dele é reordenada, renomeada ou reescrita, e a linha do índice não se toca.
- Desfecho negativo é desfecho: residual grande publica-se como `não atribuído`, e linha sem custo
  observável publica-se com `—`.

**Não fazer:**
- Não escrever em `docs/DIARIO_DE_OBRAS.md` — o bloco **Resultado** ao fim de `## TK-54` é ato da
  orquestração, não desta tarefa.
- Não classificar por conta própria, não acrescentar categoria nova e não reescrever nenhuma
  justificativa da tabela `B` além da substituição de número medido.
- Não propor rota de corte, não dizer como desligar a linha 8 e não estimar ganho de corte.
- Não tocar `docs/plans/P-0739-backlog-instrumento.md` nem qualquer tarefa `BKL-`.

**Contingências** (vale a **primeira** que casar, nesta ordem):
1. Se uma fonte do inventário não existir no caminho indicado → seguir com a linha publicada com
   `chars` `0`, regime `ausente em disco`, classificação `—` e a justificativa literal *"fonte do
   inventário não existe no caminho medido nesta data"*; reportar `contingência 1 acionada: linha <#>`.
2. Se o `n` medido divergir do inventário (17 skills, 9 agentes) → seguir, publicando o `n` medido
   na célula `fonte`; reportar `contingência 2 acionada: linha <#>, n=<medido>`.
3. Se a sonda encontrar fonte nossa que não casa nenhuma das dez linhas → seguir, publicando linha
   extra com `chars` e regime medidos, classificação `—` e a justificativa literal *"fonte fora do
   inventário fechado da rodada RP-TK54-1; classificação pendente de rodada de planejamento"*;
   reportar `contingência 3 acionada: <fonte>`.
4. Se a chave `additionalDirectories` não existir em `C:\Users\panta\.claude\settings.json` → medir
   em `D:\workspaces\PantonicApp\.claude\settings.local.json`; ausente nos dois, seguir com a linha
   9 publicada com `chars` `não medido`, classificação `—` e a justificativa literal *"chave de
   config ausente nos dois caminhos medidos"*; reportar `contingência 4 acionada`.
5. Se a chave `hooks` não existir em `C:\Users\panta\.claude\settings.json` → seguir com a linha 10
   publicada com `chars` `0` e a justificativa literal *"chave `hooks` ausente no settings global
   nesta data (a `TK-48` registra perda silenciosa dessa chave)"*; reportar
   `contingência 5 acionada`.
6. Se `## 13` fechar com mais de 60 linhas → seguir e publicar assim mesmo; reportar
   `contingência 6 acionada: ## 13 com <n> linhas`.
7. Se `git status` ou `git log -5 --oneline` falhar em `D:\workspaces\PantonicApp` → parar e
   sinalizar `blocked` razão `dependencia`.

**Verificação (comandos exatos, executáveis como estão, a partir de `D:\workspaces\PantonicApp`):**
- `Select-String -Path docs\CUSTO_DO_PICKUP.md -Pattern '^## 13 ' -List` — imprime uma linha, com o
  número da linha inicial da seção.
- `(Get-Content docs\CUSTO_DO_PICKUP.md).Count` — total de linhas do portador; o tamanho de `## 13`
  é esse total menos a linha inicial mais 1, e a meta é ≤ 60.
- `Select-String -Path docs\CUSTO_DO_PICKUP.md -Pattern 'não atribuído','fixo — fora do nosso alcance'`
  — as duas linhas fixas de E2 e E3 aparecem.
- `Select-String -Path docs\DOC_MAP.md -Pattern '^## docs/CUSTO_DO_PICKUP.md','## 13 Extrato'` —
  duas linhas, a contagem atualizada e o bullet novo.

**Pronto quando:** `docs/CUSTO_DO_PICKUP.md` termina com a seção `## 13`, que contém as doze linhas
(dez de E1 na ordem da tabela `B`, mais E2 e E3), cada célula `classificação` igual ao valor fixado
na tabela `B` ou a `—` por regra R0/contingência, a nota do `válido` vazio, os dois parágrafos da
frase de consequência `E` e as três notas `F`; e `docs/DOC_MAP.md` tem o bullet de `## 13` com a
contagem de linhas do portador atualizada.

**Fora do escopo desta tarefa:** a fonte da bimodalidade de 8.611 tok (`TK-54b`); a rodada de corte
e qualquer edição em fonte medida (rodada posterior à ratificação do dono); a separação de E2 e E3
(pede medida que esta rodada não tem); o corte do bloco `Fila corrente` do diário (achado de
processo registrado na `### Medição de 2026-09-18`).

### TK-54b — A fonte da bimodalidade [Sonnet · classe investigacao]

- **Status:** `ready` · 2026-08-31
- **Objetivo:** identificar **qual fonte liga e desliga** entre os dois regimes que a `## 12` mediu
  — `cache_read` exatamente 18.084 vs 26.695 (Δ **8.611 tok**), `cache_creation` ~16,5k vs ~19,4k,
  **preâmbulo visível idêntico** (~11.684 chars) nos dois.
- **Candidato nomeado, a confirmar ou descartar por sonda (não por argumento):** o mecanismo de
  *deferred tools* — em algumas janelas um conjunto de ferramentas chega só como nome, em outras
  com o schema completo, e a ordem de grandeza bate. Descartado o candidato, publica-se o que foi
  descartado e como.
- **Critério de pronto:** `## 14` nomeia a fonte com evidência, ou publica `não identificada` com a
  lista do que foi descartado e por quê.

### Medição de 2026-09-18 (orquestração, apensada à `TK-54` — insumo da `TK-54a`, não a substitui)

Fatos medidos numa janela principal real (transcript `4f46cd5b…`, sessão de pickup que encerrou
por teto de ocupação sem executar tarefa). **A `TK-54a` não os redescobre; reconcilia e classifica.**

- **`usage_1` = 60.472 tk** (`input`+`cache_read`+`cache_creation` da 1ª entrada `assistant`).
  É um **terceiro regime**, acima dos dois que a `## 12` mediu (34.6k e 46.1k) — o extrato passa a
  ter de fechar em **três** colunas, não duas. Emenda a decisão 2 da `TK-54a` só no número de
  colunas; método inalterado.
- **E1 medido em disco, em chars:** `CLAUDE.md` global **12.314** (era 10.751 no censo de
  2026-08-31 — cresceu 1.563), `MEMORY.md` **817**, `description:` de 17 skills **5.984** (era
  5.677), frontmatter de 9 agentes **3.104**. **Subtotal E1 ≈ 22.219 ch ≈ 5.554 tk.**
- **E2+E3 por diferença ≈ 54.918 tk — 91% do `usage_1`.** Consequência que a `TK-54a` tem de
  publicar explicitamente: **zerar todo o E1** (apagar `CLAUDE.md`, as 17 skills, os 9 agentes e a
  memória) levaria a ocupação inicial de **30,2% para 27,5%** — a meta de <10% é **inatingível por
  qualquer corte em fonte nossa**. O alvo obrigatório é E2 (schemas de ferramenta, skills
  embutidas, system prompt do harness).
- **Insumo direto para a `TK-54b`:** o mecanismo de *deferred tools* — candidato nomeado da
  bimodalidade — está **ativo** nesta janela: 18 ferramentas chegaram só como nome
  (`CronCreate`…`WebSearch`), enquanto outras (`Artifact`, `Agent`, `PowerShell`) chegaram com
  schema completo. O candidato **não está descartado**; está confirmado como presente e
  seletivo — falta medir o delta que ele explica.
- **Custo marginal medido na mesma janela** (para dimensionar o que sobra depois do preâmbulo):
  skill `proximo-passo` +7.660 tk · leitura do bloco `Fila corrente` deste diário **+20.511 tk** ·
  skill `handover` +5.383 tk.
- **Achado de processo, sem ação nesta janela:** o gatilho de condensação do diário é "bullet >
  ~30 linhas"; o bloco `Fila corrente` tem **1 linha de ~42.000 chars** e nunca o disparou —
  cresceu em largura, não em altura. Rota (corte) pertence à rodada pós-ratificação, não aqui
  (decisão 4 da `TK-54`: não mexer no que se mede).

### Achados da execução (`TK-54`)

- **`AE-1` (2026-09-18) — a coluna de classificação da `TK-54a` não tem critério fechado; card
  devolvido `blocked` razão `premissa` na triagem, antes de qualquer edição ou sonda.** O card
  pede, por linha de E1, "classificação proposta (*válido / necessário / dispensável /
  economizável*) com justificativa de uma linha" — e as sete decisões do escopamento fecham
  objetivamente todo o resto da tabela (caminhos, chars, estrato, `sempre`/`sob demanda`, fórmulas,
  a frase de consequência do <10%, o rótulo `fixo — fora do nosso alcance` de E2 e o `não
  atribuído` do residual), mas **não** esta coluna: não há definição que distinga as quatro
  categorias, nenhuma linha de E1 já classificada como exemplo, e nenhuma régua mecânica derivável
  dos fatos medidos (chars, estrato, regime de carga) que produza a categoria sem juízo de valor
  sobre a utilidade do conteúdo. Como a coluna é o núcleo do entregável — é ela que o dono
  ratifica antes da rodada de corte —, o executor não podia nem preenchê-la nem omiti-la.
  Leituras alternativas levantadas na devolução, **sem preferência indicada**: (a) a classificação
  segue régua mecânica sobre `sempre`/`sob demanda` + natureza da fonte; (b) "válido" é rótulo de
  qualidade da **medição** (fonte bem atribuída, sem dupla contagem), não de utilidade do
  conteúdo, e então falta distinguir operacionalmente "válido" de "necessário"; (c) a classificação
  é do dono/planejador e falta transcrevê-la no card. Nenhum referente ausente — âncoras batem.
  **Consequência:** abre a rodada de replanejamento `RP-TK54-1` (`G-REPLAN`), que fecha o critério
  de classificação (ou remove a coluna do escopo da `TK-54a`) antes de a execução reabrir.
  **Absorvido em 2026-09-18 pela `RP-TK54-1` (abaixo), rota A.**

- **`RP-TK54-1` (2026-09-18) — rodada de replanejamento sobre o `AE-1`. Classificação da mudança:
  técnica/tática; nada escalado ao dono.** Rota escolhida: **(A) fechar o critério**, na forma
  reforçada — o card não só publica a rubrica como **já traz a coluna preenchida**, porque o
  inventário de E1 é fechado e conhecido **hoje** (decisão 2 de `## TK-54` enumera as fontes; o
  censo de 2026-08-31 e a `### Medição de 2026-09-18` dão os tamanhos). Classificar é **decidir**, e
  decidir é ato de planejamento: com corpus fechado, a decisão cabe na rodada e o executor passa a
  **transcrever** dez valores fixos. A rubrica, o inventário e a coluna moram na seção `A`/`B` do
  card `TK-54a`, que é a **residência única** delas no projeto.
  - **O que a rodada decidiu, ponto a ponto.** (i) As quatro categorias nomeiam **o que a rodada de
    corte faz com a linha**, ordenadas e mutuamente exclusivas: `dispensável` (sai e não volta) →
    `necessário` (sai da carga fixa, volta sob demanda) → `economizável` (fica, encolhe por forma) →
    `válido` (fica como está). (ii) Regra **R0**: custo não observável ou fonte ausente recebe `—`,
    nunca uma das quatro palavras. (iii) A distribuição resultante instancia três das quatro
    categorias e deixa `válido` **vazio** — resultado medido, publicado como tal: nenhuma fonte
    nossa carregada sempre está na forma mínima.
  - **Leituras alternativas do `AE-1`, todas descartadas com razão.** **(a) régua mecânica sobre
    `sempre`/`sob demanda` + natureza da fonte:** sem poder discriminante — sete das dez linhas de
    E1 são `sempre`, e a coluna viraria reenunciação de uma coluna que a tabela já tem.
    **(b) `válido` como qualidade da medição:** descartada porque a qualidade da medição já tem
    instrumentos próprios no card (rastreabilidade de cada linha a um caminho ou comando, residual
    publicado como `não atribuído`, notas de proxy), e porque a diretriz do dono de 2026-08-31 amarra
    as quatro palavras à **decisão de corte** ("é essa percepção que o extrato tem que atender"),
    não à auditoria do número. **(c) a classificação é do dono, falta transcrevê-la:** descartada
    porque o objetivo já fechado da `TK-54` reparte o ato — *"a tarefa mede, ranqueia e **propõe**;
    a ratificação da classificação é do dono"*. A proposta é nossa; o gate de ratificação segue
    intacto e passa a incluir a rubrica.
  - **Rota (B) — remover a coluna do escopo — descartada.** Ela parte a `TK-54a` em duas e insere
    uma tarefa de planejamento **entre** a medição e a ratificação do dono, adiando o único
    entregável que a diretiva de emergência de 2026-09-18 pôs à frente de tudo — sem ganho: o que
    (B) faria depois, esta rodada fez agora, com o mesmo insumo.
  - **Efeito colateral fechado na mesma rodada, sem reabrir decisão.** A emenda das três colunas de
    regime (34.6k / 46.1k / 60.472) dizia *que* elas existem, não *o que cada célula carrega* —
    ponto de interrupção certo para um executor frio. A rodada fixou a **forma** (participação da
    linha no `usage_1` de cada regime, divisor declarado, célula entre parênteses quando o regime é
    `sob demanda`) sem tocar a identidade dos três regimes. Também fixou a reconciliação como
    **faixa** (fórmulas F2/F3), que é o que a decisão 1 já exigia e o card não instanciava.
  - **Causa-raiz na autoria.** Fase 4 item 7 do protocolo de planejamento: a exigência de que *cada
    forma real do inventário case exatamente um item da classificação, com exemplo trabalhado* foi
    lida como regra de **instrumento** (parser, lint) e não foi aplicada a uma tabela de
    classificação cujo aplicador é o **executor**. Classe de erro já coberta pela `RP-4` do
    `P-0739`; o que faltava era a leitura de que "instrumento" inclui um agente executando um card.
  - **Verificação que teria evitado o bloqueio.** Ao autorar um card cujo entregável contém coluna
    de classificação, escrever a classificação de **todas** as linhas do inventário durante a
    autoria: se o corpus é fechado, a coluna sai pronta e não há o que o executor decida; se não
    sai, a coluna não é executável e a tarefa está mal partida. Promover essa verificação ao
    protocolo do papel de planejamento **não** foi feito nesta rodada: o arquivo do agente é uma das
    fontes que a `TK-54a` mede, e a decisão 4 de `## TK-54` proíbe editá-la antes da ratificação —
    fica como ato da rodada pós-ratificação, junto com o corte.
  - **Estado após a rodada:** `TK-54a` de `blocked` para **`ready`**, card reescrito e fechado
    (`docs/DIARIO_DE_OBRAS.md`, seção `### TK-54a`); `TK-54` segue `ready`; `TK-54b` intacta;
    decisões 1..7 intactas; nenhum plano formal aberto (`P-0739` segue livre).
  - **Consumo:** ver `docs/telemetria.tsv` (linhas `TK-54a-triagem-blocked` e `RP-TK54-1`,
    2026-09-18 — telemetria medida por notificação, `fonte: usage`).

### Resultado da `TK-54` (parcial — `TK-54a`)

- **`TK-54a` `done` em 2026-09-18.** `## 13 Extrato do custo de abertura de uma janela principal`
  publicada em `docs/CUSTO_DO_PICKUP.md:404-431` (28 linhas, dentro do teto de 60);
  `docs/DOC_MAP.md` atualizado (heading `~431 linhas` + bullet da `## 13`). Sonda descartável
  rodada no scratchpad e apagada. Executada **inline pela orquestração**, não delegada — decisão
  do dono nesta janela, depois de a delegação ter consumido 150,4k tk de subagente sem produzir
  entregável.
- **E1 carregado sempre = 22.334 ch (4.467–7.445 tk).** Residual não atribuído: 87,7%–92,6% do
  `usage_1` de 60.472. Classificações fixadas pela `RP-TK54-1`: `economizável` 4 · `necessário` 3 ·
  `dispensável` 1 · `—` 2 · `válido` 0.
- **Veredito que a seção publica:** a meta de <10% é **inatingível por qualquer corte em fonte
  nossa**. O alvo obrigatório é o E2 (schemas de ferramenta, skills embutidas, system prompt do
  harness). A rodada de corte só faz sentido depois da ratificação desta classificação pelo dono.
- **`AE-2` (achado de medição, sem ação nesta tarefa):**
  `D:\workspaces\PantonicApp\.claude\global\{skills,agents}\` **espelha**
  `C:\Users\panta\.claude\{skills,agents}\` — 6 `SKILL.md` e 1 `agents/*.md` duplicados. A
  enumeração bruta dá 23 skills e 10 agentes; deduplicado, 17 e 9. Sem deduplicar, a listagem de
  skills mediria 8.033 ch em vez de 5.984 e a de agentes 3.104 em vez de 2.740 — ou seja, a
  medição de 2026-09-18 contou o frontmatter de **10** arquivos e o rotulou "9 agentes". Se o
  espelho é intencional (kit propagado) ou resíduo, e se o harness carrega os dois, é decisão que
  esta tarefa não toma (decisão 4: não mexer no que se mede).
- **Consumo:** ver `docs/telemetria.tsv` (linha `TK-54a-inline`, 2026-09-18, `fonte: nao_medido` —
  execução inline sem bloco `<usage>` a ler; `tool_uses` contado no transcript).
- **Ratificado pelo dono em 2026-09-19.** A classificação das 10 linhas está aceita. A rodada de
  corte que ela habilitava **não se abre**: `DM-30` do `P-0740` tira o custo do posto de critério
  (*"com os limites expandidos, nossa preocupação agora é a coesão e coerência do contexto ao invés
  de uso"*, dono, 2026-09-19). O extrato fica como **linha de base medida**, não como gatilho.

- 2026-08-31 — **Fila corrente anterior (texto de 2026-08-31; migra para `## TK-54`/`## TK-53` na `BKL-T6`):** nada em execução. **`TK-54a` é a próxima tarefa delegável** (escopada em
2026-08-31, sem pré-condição). **`TK-53` fechada em 2026-08-31 por decisão do dono, com desfecho
negativo:** a `TK-53a` mediu o eixo tempo como `sem degrau (oscilação pré-existente)`,
contradizendo a premissa que abriu o tíquete — não há causa a achar no corte da `95db6421…`
porque não houve mudança no corte. **`TK-53b` cancelada por absorção:** seu insumo único era o
bracket temporal, que perdeu o objeto junto com a premissa. **Decisão do dono no mesmo ato:** o
número agregado não sustenta decisão nenhuma — o que falta é o **extrato** do custo por fonte,
classificado em *válido / necessário / dispensável / economizável*; aberto como `TK-54`. **Decisão do dono sobre a
ressalva do `TK-51`
(2026-08-24): causa é deslocamento real, não ruído** — a Tabela A do laudo
(`docs/RDO/laudos/DIARIO-TK-51.md`, Achado 3) mostra as 6 janelas pós-corte agrupadas com mediana
46.070 (grupo `depois`) contra 34.347 (grupo `antes`, n=233), e o teste "dentro do intervalo
[mín,máx]" não discrimina isso. **Consequência:** `P-0737` segue `blocked` — a premissa de custo
fixo de abrir janela que o loop constrói está contradita, não confirmada como estável (nova razão
na seção `## P-0737`); investigação do que mudou no corte aberta como `TK-53`, **já desenhada**
(2026-08-24) em duas tarefas de medição na própria seção — **`TK-53a` é a próxima tarefa
delegável**, sem pré-condição; `TK-53b` só é despachada com a linha `Janela temporal do degrau:`
que a `TK-53a` publica. Não abre plano formal: `P-0739` segue livre. Os 2 achados de processo do
mesmo laudo (itens 1 e 2 —
`review_evidence.py` não aceita tarefa residente no diário; desenho de sonda fixou fato de corpus
não verificado) seguem sem tíquete, para rodada futura.
A regra escalonada de 2026-08-21 e o `G-PLANREADY` continuam valendo.
- `TK-52` **done** (2026-08-24, aceito pelo dono): resíduo do checkpoint corrigido nas duas superfícies vivas.
  `GOVERNANCA.md` §4.3 — o bullet *"Contexto acabando sem plano de parada"* (que atribuía ao
  **executor** gravar o checkpoint e dizia que *"o mesmo checkpoint responde ao sinal de poluição"*)
  virou dois bullets: *Checkpoint intermediário* como ato da **orquestração**, e *Dois casos que não
  são checkpoint* (contexto acabando dentro da tarefa = dimensionamento errado, volta ao planejamento;
  sinal de poluição = sem ponteiro de retomada). `.claude/global/CLAUDE.md` Regra 2 **carregava o mesmo
  resíduo** e teve o "Como aplicar" reescrito para enunciar a poluição como **único** critério de
  parada de execução, com parada não graciosa e sem ponteiro de retomada. **Regressão detectada e
  revertida no mesmo dia, pelo dono:** o dossiê da tarefa mandou o executor escrever um segundo ramo
  ("capacidade cruzada → orquestração grava checkpoint"), que é exatamente a cláusula que a `CTX-T1a`
  removeu por decisão do `P-0738` (`DX-13`/`DX-14`, dossiê `## CTX-T1a`: *"O parágrafo Como aplicar
  perde 'ao cruzar a capacidade, grave um checkpoint' como caminho de interrupção de tarefa"*),
  ratificada no guardrail 7 (`GOVERNANCA.md:586-592`: ocupação não é matéria de parada, é diretriz de
  dimensionamento de §3). O erro foi de **autoria de dossiê**, não do executor, que cumpriu o
  prescrito. Autoridade seguida: `.claude/skills/handover/SKILL.md:88-121`, espelhada em
  `README.md:674-688` (já correto pela `CTX-T11`, não tocado). Verificação: 3 greps negativos +
  `check-readme.ps1` exit 0 (8 agentes, 11 skills, 16 guardrails, 14 seções) + `git status --short` sem
  arquivo novo. **Achado fora de escopo (1) — resolvido em 2026-08-24:** `.claude/tools/uow.py:23`
  (arquivo ainda untracked) citava *"o checkpoint de interrupção da Regra 2"*, referente que a
  correção eliminou — a parada por poluição não gera ponteiro. Rota do dono: **dispensar a cláusula**,
  já que o checkpoint da orquestração não nasce dentro da UoW de uma tarefa e a exclusão de escopo
  perdeu o objeto; a menção saiu do docstring. **Achado fora de escopo (2) — resolvido em
  2026-08-24:** a cópia **implantada** em `C:\Users\panta\.claude\CLAUDE.md` estava **defasada do
  kit** e carregava o resíduo em forma pior — *"ao detectar sinal de poluição, **ou ao cruzar a
  capacidade**, grave um checkpoint… **faça handover**"*, na voz do executor. `Compare-Object` provou
  que o bloco da Regra 2 era a **única** divergência entre kit e cópia; com autorização do dono o
  arquivo foi copiado inteiro (165 linhas, diff vazio depois). **Achado colateral, sem tíquete por
  decisão do dono:** o `CLAUDE.md` global **não tem ponto de carga** — o `materializar.py` projeta só
  `.claude/settings.json` —, então correção de kit nesse arquivo fica sem efeito até ser copiada à
  mão. Consumo: ver `docs/telemetria.tsv`.
- `CTX-T11` **done** (2026-08-24): espelho do `README.md` revisado e **aprovado pelo dono** —
  `check-readme.ps1` exit 0 antes e depois (o guarda não vê nada do que mudou). Sete correções de
  sentido: verbete "Contexto" e guardrail 7 (capacidade deixa de encerrar contexto e de morar no
  guardrail), duas células da tabela de classes (teto sai do dossiê), linha própria da *Rodada de
  replanejamento*, "quem executa registra o consumo" (contradizia o §12 do próprio README), §9 do
  checkpoint (era do executor, é da orquestração) e ponteiro novo para `docs/CUSTO_DO_PICKUP.md`.
  `docs/DOC_MAP.md`: entrada do relatório de ~202→~306 linhas, seções 8-10. Achado registrado em
  `P-0738` `## 9`: `GOVERNANCA.md` §4.3:416-420 ainda atribui o checkpoint ao executor, contra os
  dois bullets acima dele e contra a skill `handover` — resíduo não varrido pela `CTX-T1`, fora dos
  arquivos-alvo, **a corrigir em tíquete próprio**. Estouro de orçamento: 52 tool uses contra ≤30 da
  classe `redacao` — a varredura achou 4 âncoras além das 3 pré-localizadas no dossiê; insumo de
  dimensionamento, não bloqueio. Consumo: ver `docs/telemetria.tsv`.
- `CTX-T10` **done** (2026-08-24): aferição publicada em `docs/CUSTO_DO_PICKUP.md` `## 10`. 1º
  `usage` da 1ª janela pós-`CTX-T9` = **46.071 tok**, contra 34.260/34.292/45.872 antes — **subiu**
  34,4%–34,5%. Critério (a) da iniciativa **reprovado**; (b) aprovado (abre/delega/fecha/telemetria
  numa janela). Achado registrado em `P-0738` `## 9. Achados da execução` + `TK-51` aberto — decisão
  do dono é pré-requisito antes de qualquer nova rodada. `git status --short` acusa só os dois
  arquivos do plano/relatório. Consumo: ver `docs/telemetria.tsv`.

- 2026-09-19 — *(**escopado em 2026-08-31** — 2 tarefas independentes: `TK-54a` (extrato, delegável agora) e `TK-54b` (fonte da bimodalidade de 8.611 tok). **Não abre plano formal — `P-0739` segue livre**. **`TK-54a` voltou `blocked` razão `premissa` em 2026-09-18 (`AE-1`) e a rodada `RP-TK54-1` a devolveu a `ready` no mesmo dia, rota A: a rubrica das quatro categorias e a coluna de classificação já vêm preenchidas no card — o executor transcreve, não avalia. Rodada técnica/tática, nada escalado ao dono**)*

- 2026-09-19 — **`TK-54a` fechou `done` em 2026-09-18, executada inline pela orquestração: `## 13` em `docs/CUSTO_DO_PICKUP.md:404-431`. A classificação das quatro categorias foi **ratificada pelo dono em 2026-09-19** — a `TK-54` fecha com isso. A `TK-54b` fica **despriorizada** por `DM-30` (`P-0740`): com os limites expandidos, o critério deixou de ser custo e passou a ser coesão/coerência de contexto; ela não é cancelada, apenas sai da fila sem previsão. A rodada de corte que a `TK-54a` habilitava **não se abre** pelo mesmo motivo. `AE-2` aberto (espelho `.claude/global/` duplica 6 skills e 1 agente).**

---

## TK-55 — Confiabilidade de agente e de instrumento

- **Status:** `ready` · 2026-09-19 — gated pelo encerramento do `P-0740` (ato do dono, 2026-09-19).

**Aberto por ato do dono em 2026-09-19**, sobre o relatório de encerramento da janela do `P-0740`:
*"vejo alguns casos de erros de agente com alguma frequência. No futuro (após terminar esse plano)
faremos esse planejamento"*. Não é plano e não entra no `P-0740` (`DM-30`): é o **acumulador** dos
casos, aberto agora para que a evidência não se perca até a rodada de planejamento, que acontece
**depois** que o `P-0740` encerrar.

**O recorte:** não é erro de *execução* de tarefa — a janela de 2026-09-18/19 fechou oito tarefas
com zero reprovações. É o erro que o **instrumento** ou o **artefato derivado** comete e que passa
sem sinal, porque nada o confronta com o mundo.

**Casos medidos até agora, todos com identificador rastreável:**

- **`AE-19` — comando de aceite que não discrimina mundo nenhum.** A `Verificação` 1 da `LM-T2`
  procurava a célula do `B0` com crase **dupla**, artefato de escape de markdown: devolve **0 antes
  e 0 depois**. O item 3 do mesmo card procurava uma palavra em negrito que nunca existiu no
  arquivo. **Reincidência medida no mesmo dia:** a autoria da `LM-T9` (2026-09-19) publicou um
  terceiro comando desta classe, que casou **a própria linha em que estava publicado** e nenhum dos
  oito insumos — pego antes do despacho **só porque foi rodado** (`DM-24`).
- **`AE-18` — número de aceite que nasce vencido.** Cinco correções manuais de piso de regressão em
  **sete** despachos, sobre uma suíte que andou 145 → 153 → 156 → 161 → 165 dentro da mesma janela.
  Mitigado por `DM-23` (piso vira relação re-medida), não eliminado.
- **`AE-3` — hook que mente e hook que não dispara.** O `SubagentStop` gravou o `tokens_k` inflado
  em **todas** as passagens, até **37×**, e **não dispara** quando o subagente é retomado por
  `SendMessage`: nenhuma das nove passagens do consultor gerou linha. A série da janela inteira foi
  mantida à mão. A `LM-T2b` fecha a primeira metade; a segunda não tem conserto de instrumento.
- **`AE-1` — lint cujo sinal está afogado no próprio ruído.** `backlog.py check` casa qualquer
  `| <algo> |` como linha de índice: 35 achados novos, **todos falsos positivos**, vindos de tabelas
  de exemplo. Um `C-3` verdadeiro passa despercebido no meio deles.
- **Projeção derivada que não se regenera** (2026-09-19, sem `AE-` porque não veio de laudo). A
  linha de índice do `P-0739` no diário dizia `in-progress 10/16` e *"a próxima é a `BKL-T4`"* por
  **um dia inteiro** depois de a `BKL-T4` ter fechado `done` com RDO na árvore. Ninguém detectou; o
  dono descobriu ao pedir um recap. A mesma linha do `P-0740` dizia `0/7` com nove tarefas fechadas.
  O instrumento que deveria regenerar essa projeção (`backlog.py status`, `BKL-T4`) **existe e está
  entregue**, mas não roda contra o diário vivo — é exatamente o `AE-10`.

**Padrão que os cinco compartilham, e que é a pergunta do planejamento futuro:** em todos, existe um
**derivado** (comando de aceite, piso, linha de telemetria, achado de lint, linha de índice) que
ninguém confronta com a fonte. O que a rodada tem de decidir é *quem* faz esse confronto e *quando*
— não *quem* errou.


- 2026-09-19 — *(aberto por ato do dono em 2026-09-19. O gate caiu: o `P-0740` fechou em `35/35`. **Ato do dono, 2026-09-19:** este tíquete é o **acumulador da spec de robustez**, que ainda não tem arquivo, e as **imprecisões de contagem** medidas na janela do marco 3 entram nele como **estatística** — não como correção da `docs/consultant-spec.md`. Casos novos acumulados: `AE-49` (constante de corpus congelada pelo gate), `AE-51`/`AE-57`/`AE-61` (frase que conta envelhece sozinha e nenhum instrumento a lê), `AE-52`/`AE-59` (irmão não enumerado), `AE-70` (invariância é do recorte, não do valor), `AE-71` (rótulo ordinal que o recenseamento renumera), `AE-73` (o instrumento do aceite não vê soft-wrap), `AE-75` (o número que o próprio ato de medi-lo falsifica). Segue acumulando durante a retomada do `P-0739`; a rodada de planejamento é posterior)*

**Evidências da janela do `P-0739` (2026-09-20) — oito ocorrências da mesma classe, *o derivado
cala onde deveria falar*:**

- **`check` varria 20 planos** enquanto a norma falava de 3, porque decidia *vivo* por um campo que
  a `DB-15` proíbe em plano fechado. O único sinal era um **número grande de achados**, que se lê
  como dívida, não como defeito de escopo do instrumento (`AE-15` do `P-0739`).
- **Aceite que conta a si mesmo:** itens de `Verificação` fazendo `Select-String` sobre o arquivo
  que contém o próprio padrão escrito (`AE-15`).
- **Aceite inatingível sem que nada o diga:** o `BKL-T10` passou por revisão de autoria aprovada
  em 100%, duas reautorias de consultor e três conferências de despacho afirmando `check exit 0` —
  e em nenhum desses momentos alguém **rodou** o aceite; todos o leram (`AE-23`).
- **`next` respondeu “nada delegável” com a fila cheia**, por um literal entre crases numa linha
  de prosa que o parser leu como id de dependência. Sem exit 3, sem violação, sem mensagem —
  indistinguível de backlog legitimamente vazio (`ESC-7`, `DB-50`).
- **Verbo destrutivo com `exit 0`:** `status` apagava a linha `**Fila corrente:**` e devolvia
  sucesso, sem aviso. A perda só aparece para quem comparar o arquivo antes e depois (`AE-27`).
- **Citação de seção é a única referência do kit que ninguém resolve:** caminho tem `Test-Path`,
  id de tarefa tem `review_evidence`, literal tem `Select-String` — mas *“§2.5 publicada na skill
  X”* atravessou autoria, transcrição aprovada em 100%, duas varreduras e um despacho, e só caiu
  quando um executor foi **abrir o arquivo para editar** (`AE-33`).
- **O hook devolvia 0 bytes com `exit 0`** no ponto de carga real (`stdin` em `cp1252`), e a tarefa
  seguinte publicaria esse zero como **medida** de redução do pickup — a mais cara da série,
  porque o silêncio viraria número (`AE-35`). **Três entrypoints seguem com a mesma lacuna**, um
  deles **global**: `.claude/tools/ocupacao.py:141`, `.claude/tools/telemetria_hook.py:213` e
  `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py:101` (`AE-36`).
- **Teste que passa pelo motivo errado:** TF por subprocesso que **herda** o ambiente do `pytest`
  deixa de discriminar em host com `PYTHONUTF8=1`. Primeira da série em que o silêncio previsto é
  de um **teste**, não de um instrumento (`AE-37`).
- **Contador de id que ignora o que nunca passou pelo inbox:** `**Próximo id de plano:**` apontava
  para um id **já usado**; nada confronta o contador com `docs/plans/` (`AE-39`).

**Pendência com pré-requisito, deixada pelo `ESC-10`:**

> `P-0739`/`ESC-10` — emendar `test_tf_hook_executavel_*` em `tests/test_backlog.py` para fixar
> `env=` (regra completa em `DB-53` do `P-0739`); hoje herda o ambiente e deixa de discriminar em
> host com `PYTHONUTF8=1`. **Pré-requisito de propagar a regra** a `ocupacao.py:141`,
> `telemetria_hook.py:213` e `modelo_por_fase_userpromptsubmit.py:101` (global).

**O contraste que resume a série (medido no `ESC-9`):** dos cinco entrypoints do kit que leem
`stdin`, os **dois** que acertam a codificação são exatamente os dois que **não têm teste** —
escritos por quem já tinha se queimado. O acerto veio de **cicatriz, não de norma**, e cicatriz
não se propaga: morre com quem a tem.

**Item nomeado (escalonamento 1 da janela dos seis tíquetes, 2026-09-20) — a cláusula 3 da `DB-53`
(`P-0739`) é satisfazível sem poder discriminante.**
Medido na revisão do `TK-56a`: dois dos três testes propagados seguem **verdes com o reparo de
`stdin` revertido**. A norma publicada manda construir o par negativo com "um executável
deliberadamente quebrado escrito em `tmp_path`" — e um stub discrimina o **stub**, não o produto. No
precedente `TK-57a` a regra funcionou por acidente feliz: lá o acento estava na frase-gatilho e
atravessava até a saída observada. A emenda tem quatro partes, todas medidas:

1. **Mundo hostil construído, não herdado.** Os dois mundos são `env` mínimo +
   `PYTHONIOENCODING=<codec de byte único>` e `env` mínimo + `PYTHONUTF8=1`. "O host sem a variável"
   mede o host, não o código — é o mesmo defeito do `TK-57` uma camada abaixo. Medido:
   `PYTHONIOENCODING` **prevalece** sobre `PYTHONUTF8` para `stdin`, então o mundo hostil é hostil
   até em host que exporte a variável.
2. **Canal discriminante obrigatório.** O teste só vale se o payload acentuado **viaja até o
   observável**. Preferência: (i) `stdout`, quando o valor sai nele; (ii) **efeito colateral**
   (arquivo escrito, estado consumido), quando o executável é silencioso por contrato — caso do
   `telemetria_hook.py`, cujo `stdout` é `b""` e `rc=0` em todos os mundos e cuja leitura exige
   relocar a raiz para `tmp_path`; (iii) se nenhum canal carrega, o entrypoint **não é testável por
   esta regra** e o fato se declara, em vez de se escrever um teste verde sem poder.
3. **O par negativo é o próprio produto revertido.** Nasce da fonte real por substituição textual,
   com `assert <literal do reparo> in fonte` antes. Stub escrito à mão fica **vedado**. Para
   executável que resolve caminho por `__file__`, a cópia em `tmp_path` quebra: usa-se shim com
   `exec(compile(src, str(alvo), "exec"), {"__name__": "__main__", "__file__": str(alvo)})`.
4. **Condição de validade da invariância em bytes:** vale enquanto a saída for ASCII pura
   (`json.dumps` com `ensure_ascii` default, caso dos quatro hooks). Executável que imprima não-ASCII
   cru tem a saída legitimamente alterada pelo mundo hostil — aí compara-se o **texto decodificado**.

A `DB-53` **publicada** segue com a cláusula 3 defeituosa: `docs/plans/P-0739-backlog-instrumento.md`
não é editado (`DB-23`, e a própria `DB-53` já recusou matéria nova a 17/18). O apenso à decisão é
**ato do dono**, não do loop. Rota executável já materializada: `TK-56b` e `TK-63a`.

**Estatística da classe:** esta é *o derivado cala onde deveria falar* na variante **teste**, com
agravante nova — o derivado não só calou, **a norma autorizava o silêncio**. Atravessou o autor
(`TK-56a`), o gate de delegação e a própria decisão que a criou; quem a pegou foi o `reviewer`,
executando a reversão à mão. A generalização — *toda norma que exige "o quebrado dá saída diferente"
tem de dizer **qual** quebrado e **por qual canal*** — não tem instrumento que a cheque.

**Item nomeado (escalonamento 3, 2026-09-20) — dado de teste vaza para o namespace de produção.**
A fixture criada pela primeira entrega do `TK-60a` continha uma folha chamada `SKILL.md`, e o
harness passou a **listá-la como skill invocável real** (`tests/fixtures/backlog/citacao_secao:diario-de-obras`).
Nada avisou. Regra que a classe pede: **fixture não pode conter arquivo cujo nome seja convenção de
descoberta do harness ou do agente** — `SKILL.md`, `CLAUDE.md`, `AGENTS.md`, `settings.json`. Não
varrido: se há outras convenções descobríveis dentro de `tests/fixtures/`.

**Item nomeado (escalonamento 3, 2026-09-20) — premissa citada em card também se mede, não se
deduz.** Medido nesta janela: um card fixou como gramática de citação uma forma com **1** ocorrência
no repositório, enquanto a forma real tem **1.017**; e fixou domínio de dois níveis quando **772**
das citações reais são de um nível — reprovando 76% do universo. O executor implementou
corretamente a gramática inventada, e o defeito só apareceu no laudo. Dos sete achados que
motivaram escalonamento nesta janela, **quatro foram defeitos de card**, todos da mesma classe:
campo obrigatório preenchido por dedução em vez de varredura. A regra é a extensão do `DM-12`
(*comando de aceite não se deduz, se roda*) do **comando** para a **premissa**: gramática, domínio e
contagem citados num card medem-se antes de publicar.

**Item nomeado (escalonamento 4, 2026-09-20) — piso/allowlist como esconderijo de defeito.**
Um mecanismo criado para **declarar dívida aceita** absorveu silenciosamente um falso positivo do
colhedor, e o número inflado virou documentação oficial: o piso do `C-11` nasceu com 5 entradas,
das quais **3** eram artefato de um item de card não implementado. O guarda contra isso é mecânico
e barato, e nada no kit o exige hoje: **toda entrada de piso tem de acusar quando removida** — a
entrada que some sem o lint reclamar nunca foi dívida, era defeito de gramática escondido no piso.

**Item nomeado (escalonamento 4, 2026-09-20) — menção vira uso, e a contagem que o instrumento sabe
fazer não se faz à mão.** Duas medidas da mesma rodada:
(i) escrever uma citação quebrada dentro de um documento do corpus **para falar sobre ela** é
indistinguível, para o colhedor, de **usá-la** — medido: o item que nomeava a dívida virou a 15ª
ocorrência dela. Quem documenta ponteiro quebrado usa forma não-colhível, e quitar o piso exige
**desarmar as menções antes**, senão o lint fica vermelho por causa dos próprios cards que o
criaram.
(ii) o número "13 ocorrências" publicado num card saiu de `grep -c`, que conta **linhas**, e não do
instrumento, que conta **ocorrências**; nada confrontou um com o outro. É a definição do `TK-55`
— derivado que erra sem sinal porque nada o confronta com a fonte — cometida por quem escreve os
cards do `TK-55`. Regra que impõe: **número que vai para dentro de um card e que o instrumento sabe
calcular é calculado pelo instrumento**, nunca por varredura ad-hoc.

**Item nomeado (escalonamento 5, 2026-09-20) — caso de aferição citado em card é derivado, não
fato, e aceite ancorado em população viva é o pior deles.** Medido nesta janela: **quatro** números
de aceite envelhecidos, três pegos pelo gate antes do despacho e um só no laudo —
(i) `7.123` bytes que eram **1.237** (`TK-57`); (ii) *"as 301 linhas não contêm o literal `2.5`"*,
que contêm, em prosa (`TK-60`); (iii) *"casos vivos: `TK-51` e `TK-53`"*, ambos `done` desde a
autoria, com a população do fenômeno **zerada** pela própria condução da janela (`TK-61`); (iv)
`13` ocorrências de dívida que o instrumento conta como **15**.

Forma única do vício: **o card cita medida real feita em outra data, e nada no kit confronta a
medida com a data**. A regra que destila é mais forte que a do escalonamento 4: todo número, literal
ou população citado como **caso de aferição** num card carrega a data da medida e é **re-derivado
pelo instrumento no despacho**. Aceite ancorado em população viva é o pior caso, porque a própria
execução do plano a extingue — o `TK-61a` mediria hoje o **oposto** do que o card mandava.

**Item nomeado (escalonamento 6, 2026-09-20) — asserção de magnitude é dívida com juros.**
Quatro números de aceite envelhecidos nesta janela, e o quarto foi **prescrito uma rodada depois**
de a regra contra isso ser enunciada. A correção é de forma, não de disciplina: **asserção afirma
relação, nunca magnitude** — (i) invariância: o produto correto dá a mesma saída nos dois mundos;
(ii) divergência: o produto revertido dá saídas diferentes entre eles; (iii) não-vazio: a saída
observada no mundo hostil difere de vazio, que é o que prova que o canal carrega. A magnitude vira
**documentação datada no docstring**, com o mundo em que foi medida, e nunca entra num `assert`. O
que discrimina no caso medido é **737 contra 0**, não o 737.

**Item nomeado (escalonamento 6, 2026-09-20) — teste que lê estado vivo é canal de contaminação,
não só de instabilidade.** O dano medido não foi teste intermitente: foi **dossiê de plano alheio
entrando no contexto de um executor** pela saída do `pytest`, obrigando a descartar aquele contexto
e a refazer o trabalho. Isolamento de teste tem valor de **contenção de contexto**, não só de
determinismo — e é argumento independente do de reprodutibilidade.

**Item nomeado (escalonamento 6, 2026-09-20) — o card fixa a propriedade, o executor escolhe a
técnica.** Dos oito acionamentos de consultor desta janela, **cinco** foram defeitos de card, todos
da mesma classe: o card **prescreveu o *como*** onde devia fixar o ***quê***. Shim com `__file__`
preservado em vez de *"o teste não lê estado vivo"*; registro no RDO em vez de *"a assinatura fica
em artefato do executor"*; gramática autorada em vez de *"a gramática é a que o corpus usa"*. Nos
cinco o executor cumpriu a prescrição à risca e o defeito estava na premissa. Regra: do card são a
**propriedade a satisfazer** e a **medida que a comprova**; a técnica é do executor.

**Item nomeado (encerramento da janela dos tíquetes, 2026-09-20) — duas fontes do mesmo fato
divergem sem sinal: `check` aprova o que `rdo.py` recusa.** Medido: os seis cards de tíquete abertos
no encerramento do `P-0739` não tinham `Arquivos-alvo`, `Verificação` nem `Pronto quando` — três dos
quatro campos que `rdo.py close` exige para fechar uma tarefa. O `backlog.py check` saiu **OK** sobre
todos eles. Os dois instrumentos leem o **mesmo corpus** e discordam sobre o que é card válido, e
nada confronta um com o outro: o defeito só aparece no fim, quando o fechamento falha e a tarefa já
foi executada. Classe: *dois derivados do mesmo fato divergem, e o desacordo é invisível até o
último passo*.

**Item nomeado (encerramento da janela, 2026-09-20) — `rdo.py close` não confere o estado da
tarefa.** Medido: o `close` escreveu RDO para uma tarefa que o kanban dava como `in-progress`. A
transição `in-progress → done` havia sido **corretamente recusada** por `backlog.py status` um
comando antes; o `close` não olhou. A doutrina diz que o RDO só nasce na transição `review → done`,
e nada a impõe. Classe: *norma publicada sem guarda, num ponto em que o instrumento vizinho já tem
a guarda certa*.

**Item nomeado (encerramento da janela, 2026-09-20) — o marcador ` + dono` é descartado em silêncio
na projeção do dossiê.** Medido: o card `TK-58a` tem cabeçalho `[Opus + dono · classe investigacao]`
e `backlog.py next` projetou `[Opus · classe investigacao]`. O token que some é **exatamente** o que
declara que a tarefa não é delegável a agente nenhum — e o card em questão manda **não estimar**. Um
loop que confiasse na projeção despacharia a um executor um card cuja única saída honesta é o ato do
dono. É a classe *o derivado cala onde deveria falar*, na variante mais perigosa: o silêncio recai
sobre a marca de participação humana.

**Item nomeado (encerramento da janela, 2026-09-20) — relatório de guarda que mente no console e
não no arquivo, e conta 1 defeito como 2.** Medido em `kit_check.ps1 -Mode check-drift`: o
`Write-Host` degrada `—` para `-` e `É` para caractere de substituição, enquanto o arquivo
regenerado está íntegro no byte; e o relatório soma cabeçalho e linha de detalhe na mesma lista,
reportando **2 problema(s)** para **1** defeito. Um agente que decida pelo console abre card de
defeito inexistente — risco agravado por este kit ter acabado de fechar quatro cards consertando
leitura de UTF-8. Classe: *o canal de apresentação do derivado corrompe o dado que o derivado
apurou corretamente*.

**Item nomeado (escalonamento 7, 2026-09-20) — rótulo errado é pior que número errado, porque
sobrevive à conferência.** Medido: uma seção publicou *"o `additionalContext` do hook (16.459
bytes)"*. O **número estava certo** — é o comprimento exato da linha JSONL — e o **objeto estava
errado**: o texto efetivamente injetado eram 7.867 chars. O rótulo casa com o arquivo e resiste a
qualquer recontagem; o que não casa é o que ele nomeia. Consequência medida: a suspeita **correta**
de que as duas metades do método não fechavam produziu um recálculo (36.140) tão errado quanto o
original, porque a aritmética se apoiou no rótulo. Há três comprimentos distintos para o mesmo
objeto — registro, texto renderizado e texto-fonte — e nenhum instrumento do kit os distingue.

**Item nomeado (escalonamento 7, 2026-09-20) — efeito abaixo do ruído do próprio controle,
publicado como medida.** Medido: `usage_1` de **39.650 tk** publicado como resultado, com a linha de
base sem tratamento — **36.023 · 36.262 · 48.171 · 49.533** — impressa **na mesma seção**. O valor
cai dentro da faixa do controle: o efeito buscado é menor que a dispersão dele. Nenhum guarda do kit
confronta um valor medido com a dispersão do controle que o acompanha, embora os dois estejam
publicados lado a lado. A correção de método é o **controle pareado**: sessão gêmea, mesmo dia e
mesma árvore, diferindo só no tratamento.

**Nota de técnica (escalonamento 7, 2026-09-20) — medir não é ler.** O transcript auditado nesta
rodada carrega dossiê de plano de **outra janela**, e ainda assim foi auditado sem poluir o
contexto: mediram-se **apenas estrutura, chaves e comprimentos**, com sonda booleana para confirmar
a presença dos marcadores, sem nunca extrair valores. A contenção entre janelas não obriga a
renunciar à evidência — obriga a extrair dela apenas a **forma**.

## TK-56 — Propagar o reparo de codificação de `stdin` aos três pontos de carga restantes

- **Status:** `done` · 2026-09-20 — aberto no encerramento do `P-0739`, pendência 1 de
  `docs/Entregas Aceitas/Entregas - P-0739.md`.

**O defeito, medido:** três entrypoints leem `sys.stdin.read()` e decodificam na codificação do
host. Em Windows sem `PYTHONUTF8` isso é `cp1252`, e payload UTF-8 chega mis-decodificado:

| arquivo | gatilho | efeito hoje |
|---|---|---|
| `.claude/tools/ocupacao.py:141` | `PreToolUse`, matcher `.*` — roda a cada ferramenta | recebe mojibake sem falhar |
| `.claude/tools/telemetria_hook.py:213` | `SubagentStop` | recebe mojibake sem falhar |
| `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py:101` | `UserPromptSubmit`, **global** | normaliza acento mas lê `stdin` do modo inseguro; **degrada em silêncio** para prompt acentuado, em todos os projetos |

**Por que é o mais urgente dos seis:** é o único com efeito **fora** deste projeto. O gate de
modelo-por-fase roda a cada prompt em toda a família Pantonic*.

**O que fecha:** aplicar as três cláusulas da `DB-53` do `P-0739` aos três arquivos.

**Depende de `TK-57`** — propagar a regra com o teste incompleto multiplicaria por três um teste
que não discrimina.

### TK-56a — Os três pontos de carga passam a ler `stdin` em UTF-8 explícito [Sonnet · classe implementacao]

- **Status:** `done` · 2026-09-20
- **Depende de:** `TK-57a`
- **Razão da dependência (`DB-50` do `P-0739`; a linha acima só carrega IDs):** a regra de teste tem
  de estar completa antes de ser propagada, senão multiplica por três um teste que não discrimina.
- **Objetivo:** aplicar as três cláusulas da `DB-53` do `P-0739` a `.claude/tools/ocupacao.py:141`,
  `.claude/tools/telemetria_hook.py:213` e
  `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py:101`, cada um com teste por subprocesso
  e ambiente fixo. O terceiro é global: o reparo dele vale para todos os projetos.
- **Arquivos-alvo:**
  - `.claude/tools/ocupacao.py`
  - `.claude/tools/telemetria_hook.py`
  - `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`
  - `tests/test_ocupacao.py`
  - `tests/test_telemetria_hook.py`
  - `tests/test_materializar.py`
- **Verificação:** `python -m pytest tests/test_ocupacao.py tests/test_telemetria_hook.py tests/test_materializar.py` verde, e a bateria completa `python -m pytest` sem queda de piso. Cada um dos três executáveis rodado por `subprocess.run` com `env=` mínimo, nos dois mundos da variável `PYTHONUTF8`, devolvendo a **mesma** saída.
- **Pronto quando:** as três cláusulas da `DB-53` estão aplicadas aos três pontos de carga — (1) o teste roda o processo com entrada em bytes; (2) fixa `env=` explícito de dicionário mínimo, nunca copiado de `os.environ`; (3) afirma a invariância do executável correto e a divergência do quebrado —, e o terceiro arquivo, que é hook **global**, passa a ler `stdin` em UTF-8 explícito para todos os projetos.

### TK-56b — Os dois testes sem poder discriminante passam a observar o produto [Sonnet · classe implementacao]

- **Status:** `done` · 2026-09-20
- **Objetivo:** reparar `test_tf_hook_executavel_stdin_utf8_nao_falha_e_preserva_invariancia`
  (`tests/test_telemetria_hook.py`) e `test_tf_hook_modelo_por_fase_executavel_stdin_utf8_classifica_a_fase`
  (`tests/test_materializar.py`), que hoje ficam **verdes com o reparo de `stdin` revertido** (medido
  na revisão do `TK-56a`). Causa: o par negativo é um **stub** escrito à mão — discrimina o stub, não
  o produto — e o payload acentuado nunca chega ao observável.
- **Arquivos-alvo:**
  - `tests/test_telemetria_hook.py`
  - `tests/test_materializar.py`
- **Verificação:** `python -m pytest tests/test_telemetria_hook.py tests/test_materializar.py` verde,
  coletando **≥30**; `python -m pytest` verde, sem queda do piso de **230**. O RDO registra a
  assinatura medida das duas variantes (reparada e revertida) nos dois mundos.
- **Pronto quando:** os dois testes satisfazem as quatro condições abaixo, e cada uma é conferível no
  arquivo de teste:
  1. **Mundo hostil construído, não herdado:** os dois mundos são `env` mínimo + `PYTHONIOENCODING=cp1252`
     (hostil) e `env` mínimo + `PYTHONUTF8=1` (seguro). O mundo "host sem a variável" deixa de ser o
     hostil — ele mede o host. Medido em 2026-09-20: `PYTHONIOENCODING` prevalece sobre `PYTHONUTF8`.
  2. **Canal discriminante:** o payload acentuado chega ao observável.
     - `modelo_por_fase`: prompt cujo **único** gatilho de classificação é acentuado — `{"prompt": "me dê sua análise disso"}`.
       Medido: reparado **470 B** nos dois mundos; revertido **2 B** (`{}`) no hostil e 470 B no seguro.
       O payload entregue hoje (`"faça uma análise arquitetural do módulo"`) dá 470 B em todas as
       combinações, porque `arquitet` casa sem acento.
     - `telemetria_hook`: o `stdout` é `b""` e `rc=0` em **todas** as combinações — o canal é o
       **efeito colateral**. O teste monta uma raiz falsa em `tmp_path`
       (`.claude/tools/telemetria_hook.py` copiado do arquivo real, `.claude/tools/telemetria.py`
       copiado, `.claude/estado/tarefa-corrente.json` válido, `docs/`) e usa `agent_transcript_path`
       apontando para um arquivo de **nome acentuado**. A relocação é obrigatória e não é conveniência:
       sem ela, `main` apagaria o `.claude/estado/tarefa-corrente.json` **real**.
       Medido: reparado → estado consumido e TSV com uma linha
       `2026-09-20 PantonicApp EXA-T55 sonnet 0 0.0 0.0 usage` (separado por TAB); revertido no mundo
       hostil → estado **sobrevive** e o TSV não é criado.
  3. **Par negativo é o produto revertido, nunca um stub:** a variante quebrada nasce de
     `Path(<arquivo real>).read_text(encoding="utf-8").replace(<bloco do reparo>, "raw = sys.stdin.read()")`,
     precedida de `assert <bloco do reparo> in fonte` — se o reparo mudar de forma, o teste cai
     ruidosamente em vez de virar verde vazio. O bloco é o literal de 4 linhas
     (`try: raw = sys.stdin.buffer.read().decode("utf-8", errors="replace")` / `except AttributeError:` /
     `raw = sys.stdin.read()`), idêntico nos quatro entrypoints — conferido em 2026-09-20.
     Os dois `stub = tmp_path / "hook_quebrado.py"` existentes são **removidos**.
  4. **Asserções:** (i) produto reparado dá a **mesma** saída observada nos dois mundos; (ii) produto
     **revertido** dá saídas **diferentes** entre os dois mundos; (iii) o valor acentuado chega íntegro
     ao observável no mundo hostil. A comparação é de **bytes** — vale porque os dois executáveis
     imprimem `json.dumps` com `ensure_ascii` default (`stdout` ASCII puro).
- **Não fazer:** não editar `.claude/tools/telemetria_hook.py`, `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`
  nem nenhum arquivo de produto — o reparo de `stdin` deles está correto e aprovado; não tocar
  `tests/test_backlog.py` nem `tests/test_ocupacao.py` (matéria do `TK-63`); não editar
  `docs/plans/P-0739-backlog-instrumento.md` (`DB-23`); não escrever em `.claude/estado/`,
  `docs/telemetria.tsv` ou qualquer caminho real durante o teste.

## TK-57 — Fixar o ambiente no teste por subprocesso do hook

- **Status:** `done` · 2026-09-20 — aberto no encerramento do `P-0739`, pendência 2 de
  `docs/Entregas Aceitas/Entregas - P-0739.md`.

**O defeito, medido:** `test_tf_hook_executavel_*` em `tests/test_backlog.py` roda o executável por
`subprocess.run`, o que é correto — mas **herda o ambiente do `pytest`**. Em host que exporte
`PYTHONUTF8=1`, o teste passa **com ou sem** o reparo: deixa de discriminar. Medido ao autorar a
`DB-53`: hook pré-reparo devolve **0** bytes com `env={SYSTEMROOT, PATH}` e **59** com
`PYTHONUTF8=1` acrescido.

**O que fecha:** as três cláusulas da `DB-53` — (1) roda o processo, entrada em bytes; (2) **fixa
`env=` explícito**, montado de dicionário mínimo e nunca copiado de `os.environ`; (3) **afirma a
invariância** — o executável correto dá a mesma saída nos dois mundos, o quebrado dá saídas
diferentes.

**Armadilha conferida:** em Windows o subprocesso sobe com `env={}` e com `{SYSTEMROOT, PATH}`; é a
cópia preguiçosa de `os.environ` que reintroduz o problema.

**É pré-requisito do `TK-56`.**

### TK-57a — O teste do hook fixa o ambiente e afirma a invariância [Sonnet · classe implementacao]

- **Status:** `done` · 2026-09-20
- **Objetivo:** emendar `test_tf_hook_executavel_*` em `tests/test_backlog.py` para montar `env=`
  explícito de dicionário mínimo — nunca copiado de `os.environ` — e afirmar que o executável
  correto devolve a **mesma** saída com e sem `PYTHONUTF8`, enquanto o quebrado devolve saídas
  diferentes. Referência medida: pré-reparo dá **0** bytes com `env={SYSTEMROOT, PATH}` e **59**
  com `PYTHONUTF8=1`.
- **Arquivos-alvo:**
  - `tests/test_backlog.py`
- **Verificação:** `python -m pytest tests/test_backlog.py` verde, coletando **≥72** testes; `python -m pytest` verde, coletando **≥224**.
- **Pronto quando:** os dois `test_tf_hook_executavel_*` montam `env=` explícito de dicionário mínimo (ler `SYSTEMROOT`/`PATH` individualmente é permitido; `dict(os.environ)` ou `os.environ.copy()` é o que fica vedado); existe asserção de **invariância** do executável correto — mesma saída sem e com `PYTHONUTF8=1` —; e existe o **par negativo**, um executável deliberadamente quebrado escrito em `tmp_path` que devolve saídas diferentes nos dois mundos.

## TK-58 — Fechar a metade `usage_1` da medida de pickup

- **Status:** `done` · 2026-09-20 — aberto no encerramento do `P-0739`, pendência 3 de
  `docs/Entregas Aceitas/Entregas - P-0739.md`.

**Estado:** o método `DC-4` tem duas metades. A de **caracteres** está publicada — pickup composto
de **26.760 chars**, **−65,5%** contra os 77.457 da `## 3` e 66,9% do alvo de 40.000 da `## 6`. A
do **primeiro `usage` de uma sessão nova** ficou **declarada sem valor** na `## 14` de
`docs/CUSTO_DO_PICKUP.md`, porque não é observável de dentro de um subagente.

**O que fecha:** abrir uma janela principal nova, ler o primeiro `usage` e publicar o par completo.
Ato manual; nenhum agente o resolve sozinho.

**Não estimar.** A lacuna foi deixada sem valor de propósito: número inventado ali seria publicado
como fato num documento usado para decidir custo.

### TK-58a — Medir o `usage_1` em janela nova e fechar o método `DC-4` [Opus + dono · classe investigacao]

- **Status:** `done` · 2026-09-20
- **Objetivo:** abrir uma janela principal nova, ler o **primeiro `usage`** dela e publicar o par
  completo na `## 15` de `docs/CUSTO_DO_PICKUP.md`, substituindo a lacuna declarada na `## 14`. A
  metade em caracteres já está publicada: **26.760**, **−65,5%** contra 77.457. **Não estimar** — o
  valor ou é medido em sessão nova, ou a lacuna continua declarada.
- **Arquivos-alvo:**
  - `docs/CUSTO_DO_PICKUP.md`
- **Verificação:** a `## 15` de `docs/CUSTO_DO_PICKUP.md` passa a conter o par completo, e a lacuna declarada na `## 14` é substituída por remissão a ele. O valor de `usage_1` é **lido** do primeiro `usage` de uma janela principal nova, não derivado de nenhuma outra medida do documento.
- **Pronto quando:** o par (**caracteres** e **`usage_1`**) está publicado com as duas medidas ancoradas em observação, a metade em caracteres preservando os números já publicados (**26.760**, **−65,5%** contra 77.457), e a `## 14` não declara mais lacuna. **Não estimar:** sem sessão nova que produza o número, a tarefa devolve `blocked motivo=premissa` e a lacuna continua declarada — número inventado aqui seria publicado como fato num documento usado para decidir custo.

### TK-58b — A `## 15` corrige o rótulo, declara a fronteira e o `DC-4` ganha emenda [Sonnet · classe redacao]

- **Status:** `done` · 2026-09-20 — pendência do laudo do `TK-58a` (ressalva 88%), roteada pelo
  `A8a` e resolvida pelo consultor no escalonamento 7. **Nada aqui é remedição:** tudo o que corrige
  já está no transcript em disco.
- **Objetivo:** a `## 15` de `docs/CUSTO_DO_PICKUP.md` deixa de sustentar *"o pickup custa 39.650
  tk"* e passa a sustentar *"abrir janela com pickup custou 39.650 tk, dentro da faixa de abertura
  sem pickup do mesmo dia"*; o método `DC-4` ganha as três cláusulas que o caso mediu; e a `## 14`
  recebe um `a apurar` na composição dela.
- **Arquivos-alvo:**
  - `docs/CUSTO_DO_PICKUP.md`
- **Verificação:**
  - A `## 15` **não** contém mais a frase `o additionalContext do hook (**16.459 bytes**)`.
  - A `## 15` contém os literais `7.867` e `Fronteira do que esta medida sustenta`.
  - A `## 14` contém o literal `a apurar`.
  - `python -m pytest` verde, coletando **238** — não pode cair.
- **Pronto quando:** os três fatos medidos no transcript da sessão `8760907f` estão publicados, e
  cada um com o objeto corretamente nomeado:
  1. **Correção de rótulo.** `16.458` é o comprimento da **linha JSONL** do registro do hook, com
     envelope e escapes. O texto efetivamente injetado é **7.867 chars** (`rendered[0].content`),
     contra **7.079** na `## 14`: os dois pickups diferem **~11%**, não em ordem de grandeza. O
     recálculo de 36.140 que a pendência propunha era aritmética sobre o rótulo errado e **não** se
     publica.
  2. **Fronteira declarada.** Os 39.650 tk **não isolam o pickup**: o registro do pickup é ~16% dos
     ~48,5 mil chars renderizados que precedem o primeiro `usage` — o resto é listagem de agentes
     (6.141), listagem de skills (11.948), arquivos anexados (13.605), `session_context` (3.377),
     MCP (2.053) e ambiente (1.718). E 39.650 cai **dentro** da linha de base sem pickup do mesmo
     dia (36.023 · 36.262 · 48.171 · 49.533): o efeito buscado é menor que a dispersão do controle.
     A seção publica o custo de **abertura de janela que fez pickup**, comparável aos regimes da
     `## 12` e da `## 13`, e **não** o custo do pickup. Isolar o pickup exige **controle pareado**
     (sessão gêmea, mesmo dia e mesma árvore, sem o gatilho); enquanto não houver, o par do `DC-4`
     fica **aberto por declaração**, não fechado por medida.
  3. **A sessão nomeia o dossiê que o pickup projetou:** `MC-T1`, do plano `P-0741`. Medida de
     pickup sem a tarefa declarada não é interpretável.
  4. **Emenda ao `DC-4`, três cláusulas:** (i) o pickup é **função da tarefa**, não constante, e
     toda medida nomeia o dossiê que projetou — duas medidas de tarefas diferentes **não formam
     par**; (ii) a metade `usage_1` só vale se **isolar** o pickup, e sem controle pareado a metade
     se declara aberta; (iii) **todo número publicado nomeia o objeto medido** — comprimento de
     registro, de texto renderizado e de texto-fonte são três objetos distintos.
  5. **`a apurar` na `## 14`.** Recomposta para a sessão `8760907f` pelo mesmo método, a metade em
     chars dá **20.996** (`CLAUDE.md` 12.313 + `MEMORY.md` 816 + hook 7.867). A divergência contra
     os 26.760 não é só de dossiê: a `## 14` publica `CLAUDE.md` em **10.376** (medido **12.313**
     nesta data) e soma **8.488** chars de memórias indexadas que **não aparecem** entre os anexos
     da primeira requisição daquela sessão. Isso se registra como **`a apurar`**, não como defeito,
     e é pré-requisito de qualquer republicação da `## 14`.
- **Não fazer:** não republicar os 26.760 nem os 36.140; não alterar a metade em chars nem a
  redução de **−65,5%**, que nunca dependeu do `usage_1` e segue de pé; não abrir
  `docs/plans/P-0741-modelo-conceitual.md`; não tocar `GOVERNANCA.md`,
  `docs/RUBRICA_DE_REVISAO.md` nem `.claude/skills/diario-de-obras/SKILL.md` — a outra janela de
  orquestração está editando os três **agora**.

### TK-58c — O título e o lead da `## 15` dizem o que a seção mede [Sonnet · classe redacao]

- **Status:** `done` · 2026-09-20 — pendência do laudo do `TK-58b` (ressalva 88%), roteada pelo
  `A8a`. Sem decisão de rota: o corpo da seção já está aprovado e dita o conteúdo.
- **Objetivo:** alinhar o **cabeçalho** da `## 15` de `docs/CUSTO_DO_PICKUP.md` ao **corpo** dela. O
  título diz *"Par completo do método `DC-4`"* e o lead diz *"Fecha a aferição da `## 14`"* e *"as
  duas estão medidas"* — mas o próprio corpo, três parágrafos abaixo, declara que a metade
  `usage_1` **não isola o pickup** e que o par fica **aberto por declaração**. O cabeçalho promete o
  que o texto desmente, e é o cabeçalho que se lê primeiro.
- **Arquivos-alvo:**
  - `docs/CUSTO_DO_PICKUP.md`
- **Verificação:**
  - A `## 15` **não** contém mais os literais `Par completo`, `Fecha a aferição` nem
    `as duas estão medidas`.
  - O título da `## 15` nomeia **abertura de janela com pickup**, não *par completo*.
  - O lead declara, em uma frase, que a metade em chars está medida e que a metade `usage_1`
    **fica aberta** à espera de controle pareado.
  - O **corpo** da seção não muda: os parágrafos de proveniência, correção de rótulo, fronteira,
    pickups distintos e emenda ao `DC-4` ficam **byte a byte** como estão.
  - `python -m pytest` verde, coletando **238**.
- **Pronto quando:** quem lê só o título e o lead da `## 15` chega à mesma conclusão de quem lê a
  seção inteira — que a redução de **−65,5%** em chars está medida e de pé, e que o custo do pickup
  **não** foi isolado. É o critério inteiro desta tarefa.
- **Não fazer:** não alterar nenhum número; não tocar a `## 14`; não abrir
  `docs/plans/P-0741-modelo-conceitual.md`; não tocar `GOVERNANCA.md`,
  `docs/RUBRICA_DE_REVISAO.md` nem `.claude/skills/diario-de-obras/SKILL.md` — a outra janela de
  orquestração está editando os três agora.

### TK-58d — Nenhum lugar do corpus afirma que o par do `DC-4` está fechado [Sonnet · classe redacao]

- **Status:** `done` · 2026-09-20 — pendência do laudo do `TK-58c` (aprovado 100%, recomendação
  `escalar`), roteada pelo `A8a`. **Escopo por afirmação, não por local** — é a correção do defeito
  que produziu três rodadas seguidas de rastro: `TK-58b` e `TK-58c` foram escopados por arquivo e
  por seção, então cada um corrigiu uma instância e deixou as outras vivas.
- **Objetivo:** a afirmação aposentada — *o par do `DC-4` está fechado / as duas metades estão
  medidas* — deixa de existir em **todo** o corpus vivo. Ela sobrevive em dois lugares medidos, e
  os dois são lidos **antes** da `## 15`.
- **Arquivos-alvo:**
  - `docs/CUSTO_DO_PICKUP.md`
  - `docs/DOC_MAP.md`
- **Verificação:**
  - `grep -rn "par completo\|Par completo\|as duas metades do" docs/CUSTO_DO_PICKUP.md docs/DOC_MAP.md`
    → **nenhuma** ocorrência.
  - `docs/CUSTO_DO_PICKUP.md` não contém mais o literal `fecha o par`.
  - A entrada da `## 15` no `DOC_MAP` traz o **título atual** da seção, que começa com
    `Abertura de janela com pickup`.
  - `python -m pytest` verde, coletando **238**.
- **Pronto quando:** as duas ocorrências medidas em 2026-09-20 estão corrigidas, e cada uma passa a
  dizer o que a `## 15` de fato sustenta — metade em chars medida e de pé (**−65,5%**), metade
  `usage_1` medindo **abertura de janela com pickup**, sem isolar o pickup, **aberta** à espera de
  controle pareado:
  1. **Fecho da `## 14`** (parágrafo `**Metade em \`usage_1\`: medida.**`): hoje afirma que a
     `## 15` *"fecha o par do `DC-4`"*. Passa a remeter à `## 15` dizendo que a metade foi **medida**
     e que o **par segue aberto**, pelo motivo que a `## 15` declara.
  2. **Entradas do `DOC_MAP`** (linhas 131-135): a da `## 14` diz `a metade usage_1 declarada não
     medida` — defasada, o número existe desde 2026-09-20. A da `## 15` repete o **título antigo**
     (`Par completo do método DC-4…`) e afirma `as duas metades do DC-4 medidas`. As duas passam a
     descrever o estado atual, e a da `## 15` cita o título vigente.
- **Não fazer:** não alterar nenhum número; não editar o **corpo** da `## 15`, aprovado em
  `TK-58b`/`TK-58c`; não editar o texto histórico dos cards `TK-58`/`TK-58a` no diário — card
  fechado não retroage (`DB-23`); não abrir `docs/plans/P-0741-modelo-conceitual.md`; não tocar
  `GOVERNANCA.md`, `docs/RUBRICA_DE_REVISAO.md` nem `.claude/skills/diario-de-obras/SKILL.md` — a
  outra janela de orquestração está editando os três agora.

## TK-59 — Guarda para o contador de id do inbox

- **Status:** `done` · 2026-09-20 — aberto no encerramento do `P-0739`, pendência 4 de
  `docs/Entregas Aceitas/Entregas - P-0739.md`.

**O defeito, medido:** `drain` recalcula `**Próximo id de plano:**` por `max(id visto) + 1` sobre o
que **passou pelo inbox**. Plano criado sem linha de inbox é invisível para essa conta. Ocorreu:
o contador ficou em `P-0742` enquanto `docs/plans/P-0742-loop-fora-do-llm.md` já existia — o
próximo plano colidiria. **`check` não acusa.**

**Já corrigido à mão** nesta execução, para `P-0743`, depois de conferir o maior id da árvore por
varredura de `docs/plans/P-*.md` (**742**). O que falta é a **guarda**.

**O que fecha:** um verificador que confronte o contador com `docs/plans/` e acuse divergência.

### TK-59a — Verificador do contador de id do inbox contra `docs/plans/` [Sonnet · classe implementacao]

- **Status:** `done` · 2026-09-20
- **Objetivo:** acrescentar ao `check` uma violação que confronte
  `**Próximo id de plano: P-NNNN.**` de `docs/plans/_INBOX.md` com o maior id presente em
  `docs/plans/P-*.md`, acusando quando o contador aponta para id **já usado**. Caso medido que a
  motivou: contador em `P-0742` com `P-0742-loop-fora-do-llm.md` já na árvore.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
- **Verificação:** `python .claude/tools/backlog.py check` acusa a divergência sobre fixture em que o contador de `docs/plans/_INBOX.md` aponta para id já presente em `docs/plans/P-*.md`, e **não** acusa sobre fixture em que o contador aponta para id livre. `python -m pytest tests/test_backlog.py` verde.
- **Pronto quando:** `check` tem uma violação nova, de vocabulário fechado como as demais (`C-*`), que confronta `**Próximo id de plano: P-NNNN.**` com o maior id presente em `docs/plans/P-*.md`; e o teste é **par presença-ausência**, sobre corpus em que as duas leituras dariam resultados diferentes. Caso medido que motivou: contador em `P-0742` com `docs/plans/P-0742-loop-fora-do-llm.md` já na árvore.

## TK-60 — Verificador de citação de seção

- **Status:** `done` · 2026-09-20 — aberto no encerramento do `P-0739`, pendência 5 de
  `docs/Entregas Aceitas/Entregas - P-0739.md`.

**A lacuna:** o kit resolve dois dos três tipos de referência que usa — caminho de arquivo tem
`Test-Path`, identificador de tarefa tem `review_evidence`, literal de aceite tem `Select-String`
nos dois mundos. **Citação de seção não tem nada.**

**Custo medido da ausência:** o ponteiro *"§2.5 publicada na skill `diario-de-obras`"* atravessou a
autoria de um card, uma transcrição **aprovada em 100%**, duas varreduras de consultor e um
despacho — e só caiu quando um executor foi **abrir o arquivo para editar**. O que ele mediu, e é o
que dá o critério do verbo: das 301 linhas, **nenhuma é heading numerado**, e o literal `2.5`
aparece **uma vez, em prosa**, na linha 42 (`~2.5k para ~5k chars`). Por isso o casamento é por
**heading**, nunca por substring. A redação anterior desta linha — *"as 301 linhas não contêm o
literal `2.5`"* — era **falsa**; corrigida em 2026-09-20 pelo laudo do `TK-60a`.

**Agravante:** o mundo que o card cria não resolve o caso — a seção não passaria a existir por
efeito de passo nenhum, então nem o método da `DB-47` (rodar o aceite em cópia) o alcançaria.

**O que fecha:** um verbo que resolva `§X.Y publicada em Z` contra o arquivo citado.

### TK-60a — `check` resolve citação de seção e emite `C-11` [Sonnet · classe implementacao]

- **Status:** `done` · 2026-09-20 — **reescrito** após reprovação 56% (bloqueante `guardas`).
  A reprovação foi de **autoria do card**, não de conduta do executor: a `Verificação` anterior
  exigia superfície de CLI e fixava uma gramática de citação que **não existe no corpus**.
  Retentativa não consumida.
- **Objetivo:** `check` passa a resolver as citações de seção do corpus contra o arquivo citado e a
  emitir `C-11` quando a seção citada não existe nele. Fecha o terceiro resolvedor de referência do
  kit — caminho de arquivo tem `Test-Path`, identificador de tarefa tem `review_evidence`, citação
  de seção passa a ter este.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
  - `tests/fixtures/backlog/citacao_secao/`
- **Verificação:**
  - `python .claude/checks/dead_code.py` sai **exit 0** — hoje sai `FALHOU - 1 achado(s)`, nomeando
    `.claude/tools/backlog.py:638: resolver_citacao_secao - sem chamador de producao alcancavel`.
  - `python .claude/tools/backlog.py check` sai **exit 0**. Se sair 1, o **piso do item 7 está
    errado** — não o corpus.
  - `python -m pytest tests/test_backlog.py` verde; `python -m pytest` verde, sem queda do piso de
    **234** (medido em 2026-09-20, com a entrega anterior na árvore).
- **Pronto quando:** os oito itens abaixo valem, e cada um é conferível no arquivo entregue.
  1. **Gramática de colheita — a observada, não a inventada.** A citação real do kit é
     `` `<arquivo>.md` §<N>[.<N>]* `` (literal entre crases, espaço, `§`). Medido em 2026-09-20:
     **1.017** ocorrências dessa forma contra **1** da forma `§X.Y publicada em <arquivo>` que o card
     anterior fixava — e essa 1 é o texto do próprio tíquete. A `_REF_SECAO_RE` entregue **sai**.
  2. **Domínio — um nível e N níveis.** Medido: **772** citações de um nível (`§3`, `§7`, `§10`)
     contra **240** de dois ou mais. A gramática anterior exigia `\d+(?:\.\d+)+` e reprovava as 772.
  3. **Casamento por heading numerado, nunca substring** — `^#{1,6}\s+<N>(\.<N>)*\b`. O núcleo
     entregue está **correto e fica**: é o que faz o caso motivador sair `C-11` apesar de o literal
     existir (`.claude/skills/diario-de-obras/SKILL.md` tem `2.5` em prosa na linha 42 e **zero**
     headings numerados nas suas 301 linhas).
  4. **Resolução de caminho: raiz do repo, com queda para basename único no corpus.** Medido: **56**
     ocorrências / 20 distintas falhariam só por a citação omitir o prefixo — `` `RUBRICA_DE_REVISAO.md`
     §8 `` (9 ocorrências) com o arquivo em `docs/`. Sem essa queda o lint vira ruído.
  5. **Fronteira declarada, e é silêncio nos dois casos:** arquivo que não existe nem por basename
     **não** é `C-11` — resolver caminho é do `Test-Path` (`DB-2`, uma residência por regra); e `§`
     seguido de **três ou mais** componentes numéricos é **versão**, não seção (medido:
     `` `CHANGELOG.md` §3.0.0 ``, 3 ocorrências).
  6. **O chamador de produção é `check`.** Nenhum subcomando novo, nenhum segundo ponto de entrada.
  7. **Piso, para o lint não nascer vermelho.** `check` não tem severidade: violação implica exit 1.
     O corpus vivo já carrega dívida — medido: **duas** seções citadas que não existem,
     `` `GOVERNANCA.md` §1.1 `` e `` §3.2 ``, em **13** ocorrências (`docs/DIARIO_HISTORICO.md` 5,
     `docs/plans/P-0741-modelo-conceitual.md` 6, `P-0730` 1, `P-0731` 1). `C-11` nasce com um piso
     dessas **duas** entradas, inline no módulo, cada uma com origem e data da medida — mesma trava
     do `.claude/checks/ratchet_piso.py`. O lint falha no **próximo** ponteiro quebrado, que é o
     defeito que o `TK-60` existe para pegar. Quitar o piso é tíquete próprio, não deste card.
  8. **O mundo do teste é declarado.** A fixture `tests/fixtures/backlog/citacao_secao/` **fica** —
     é a convenção do módulo e blinda o teste das edições da outra janela —, e a folha
     `.claude/skills/diario-de-obras/SKILL.md` dentro dela é **renomeada para `SKILL.fixture.md`**,
     preservando o diretório-espelho. Razão medida: com o nome real, o harness passou a listar a
     fixture como **skill invocável** (`tests/fixtures/backlog/citacao_secao:diario-de-obras`).
  E o **par de regressão do domínio**, que é o defeito medido nesta rodada, entra como teste:
  `§3` contra `GOVERNANCA.md`, `§8` contra `docs/RUBRICA_DE_REVISAO.md` e `§9` contra
  `docs/consultant-spec.md` resolvem (`None`); hoje os três saem `C-11`.
- **Não fazer:** não editar `docs/plans/P-0741-modelo-conceitual.md` — é plano **vivo de outra janela
  de orquestração ativa neste mesmo repositório**; as 6 ocorrências dele entram no piso, são
  reportadas e **não** corrigidas. Não corrigir nenhuma das 13 ocorrências. Não criar subcomando de
  CLI. Não editar `GOVERNANCA.md`, `.claude/tools/rdo.py`, `review_evidence.py` nem
  `.claude/estado/tarefa-corrente.json`.

### TK-60b — Item 5 implementado e piso devolvido à dívida real [Sonnet · classe implementacao]

- **Status:** `done` · 2026-09-20
- **Objetivo:** implementar o item 5 do `TK-60a` **como ele já está escrito** — arquivo citado que
  não resolve nem por basename devolve `None` em silêncio — e devolver `_PISO_C11` às duas entradas
  de dívida real. Hoje `resolver_citacao_secao` devolve `C-11` quando `_resolver_arquivo_citado`
  devolve `None`, **contra o próprio docstring**, e as 3 entradas extras do piso são artefato desse
  defeito. Nenhuma rota nova: o estado final está medido.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
- **Verificação:**
  - `python .claude/tools/backlog.py check` sai **exit 0** com `check: OK` e nenhuma violação
    (medido em cópia patchada contra o repo real, 2026-09-20).
  - `python .claude/checks/dead_code.py` sai **exit 0**.
  - `python -m pytest` verde, sem queda do piso de **235**.
- **Pronto quando:**
  1. `resolver_citacao_secao` devolve `None` quando `_resolver_arquivo_citado` devolve `None` — um
     `if caminho is None: return None` antes do laço de headings. **Nenhuma outra** mudança de
     comportamento: gramática de colheita, domínio, casamento por heading, chamador em `check` e
     fixture estão aprovados e não se tocam.
  2. `_PISO_C11` tem **exatamente duas** entradas, as de dívida real em `GOVERNANCA.md`. As três
     saem: duas citam doc de **outro repositório** (PantonicVideo) e uma é **nota de diff**, não
     citação. As três são falso positivo do colhedor, que o item 5 silencia sozinho.
     **O princípio que isso destila, e que vale para toda autoria desta família:** *piso absorve
     dívida real, nunca falso positivo do colhedor*. O teste é mecânico — com o colhedor correto,
     **remover** uma entrada do piso tem de fazer o lint **acusar**; a entrada que some sem acusar
     nunca foi dívida, era defeito de gramática escondido dentro do piso.
  3. **Teste que tranca a regra** (é o que impede a reincidência): par presença-ausência sobre o
     ramo do item 5 — citação a arquivo que não existe, e a arquivo de basename ambíguo, saem
     `None`; citação a arquivo existente com seção ausente sai `C-11`.
  4. **Número de dívida corrigido no comentário de origem do piso: 15 ocorrências, não 13.** Medido
     pelo próprio instrumento com `_PISO_C11` vazio, em cópia: 15 violações, todas das duas seções
     ausentes, nenhuma das três espúrias reaparecendo. O 13 do `TK-60a` era contagem de **linhas**
     (`grep -c`) e não contava a ocorrência que o próprio card criou.
- **Não fazer:** não corrigir nenhuma das 15 ocorrências; não editar
  `docs/plans/P-0741-modelo-conceitual.md` — plano vivo de outra janela; não editar `GOVERNANCA.md`;
  não mexer em `_REF_SECAO_RE`, `_CITACAO_SECAO_HARVEST_RE`, `_HEADING_NUMERADO_RE`, na chamada
  dentro de `check` nem na fixture.

### TK-60c — A decomposição por arquivo do piso bate com o total que ela declara [Sonnet · classe implementacao]

- **Status:** `done` · 2026-09-20 — pendência do laudo do `TK-60b` (ressalva 91%), roteada pelo
  `A8a`.
- **Objetivo:** corrigir o comentário de origem de `_PISO_C11` em `.claude/tools/backlog.py`, cuja
  decomposição por arquivo soma **13** sob um cabeçalho que declara **15** — o comentário contradiz
  a si mesmo dentro do próprio guarda que existe para pegar derivado que erra sem sinal.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
- **Verificação:** a soma das parcelas da decomposição é **15**, igual ao total do cabeçalho da
  mesma frase. `python .claude/tools/backlog.py check` sai **exit 0**; `python -m pytest` verde, sem
  queda do piso de **236**.
- **Pronto quando:** a decomposição lista os cinco arquivos com as contagens **medidas pelo próprio
  instrumento** em 2026-09-20 (`check` com `_PISO_C11` vazio, em processo, sem tocar a árvore):
  `docs/plans/P-0741-modelo-conceitual.md` **6**, `docs/DIARIO_HISTORICO.md` **6**,
  `docs/DIARIO_DE_OBRAS.md` **1**, `docs/plans/P-0730-v2-identidade.md` **1**,
  `docs/plans/P-0731-v2-extracao-modalidade.md` **1**. A redação anterior omitia
  `docs/DIARIO_DE_OBRAS.md` e contava 5 em vez de 6 no histórico. **Só o comentário muda** —
  nenhuma linha de código, nenhuma entrada do piso, nenhum teste.
- **Não fazer:** não corrigir nenhuma das 15 ocorrências de dívida; não alterar as duas entradas de
  `_PISO_C11`; não editar `docs/plans/P-0741-modelo-conceitual.md`, plano vivo de outra janela de
  orquestração ativa neste repositório.

## TK-61 — Implementar o rodapé de "candidato a fechamento" (`DB-4`)

- **Status:** `done` · 2026-09-20 — aberto no encerramento do `P-0739`, pendência 6 de
  `docs/Entregas Aceitas/Entregas - P-0739.md`.

**O defeito, medido:** a `DB-4` está publicada na `## 3` do `P-0739` como norma — pai cujos filhos
diretos ficaram todos terminais entra no rodapé de `next` como *candidato a fechamento*. A
expressão **não existe** em `.claude/tools/backlog.py`, e o rodapé imprime só `inbox de planos`,
`fila de memória` e `blocked`. **Norma publicada sem implementação e sem teste.**

**Efeito hoje:** com a migração feita, `TK-51` (**1/1**) e `TK-53` (**1/1**) têm todos os filhos
terminais e *deveriam* aparecer no rodapé. Nada os mostra.

**Por que ficou fora dos módulos do `P-0739`:** não é corpus nem migração — seria matéria
transversal, vedada pelo critério (ii) da rubrica de criação de tarefa.

**O que fecha:** implementar o rodapé que a norma descreve, com teste que discrimine pai com filhos
todos terminais de pai com filho vivo.


### TK-61a — O rodapé de `next` imprime candidato a fechamento [Sonnet · classe implementacao]

- **Status:** `done` · 2026-09-20 — **reescrito** no gate, antes do despacho: o aceite anterior
  citava `TK-51` e `TK-53` como casos vivos e ambos estão `done` desde então. Re-derivado em
  2026-09-20 pelo instrumento, não por varredura.
- **Objetivo:** implementar a `DB-4` do `P-0739` na metade que falta — a expressão *candidato a
  fechamento* não existe em `.claude/tools/backlog.py` e o rodapé de `next` imprime só os três
  contadores mecânicos.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
  - `tests/fixtures/backlog/`
- **Verificação:** `python .claude/tools/backlog.py next` sai **exit 0** e o rodapé traz **duas**
  linhas: a dos três contadores, **byte a byte como hoje**, e a nova, que sobre o corpus vivo
  imprime `candidato a fechamento: nenhum` (população medida em 2026-09-20: **zero**).
  `python .claude/tools/backlog.py check` exit 0; `python .claude/checks/dead_code.py` exit 0;
  `python -m pytest` verde, sem queda do piso de **236**.
- **Pronto quando:**
  1. **Definição, quatro cláusulas conjuntas.** Candidato a fechamento é pai (plano **ou** tíquete)
     que: (a) está no corpus da §2.0 (`DB-43`); (b) tem **>= 1 filho direto**; (c) tem **todos** os
     filhos diretos terminais — `done` ou `cancelled`, o vocabulário da §2.5 (`superseded` não entra:
     só plano o tem e plano não é filho); (d) **não é ele próprio terminal**
     (`done`/`cancelled`/`superseded`).
     **Medido em 2026-09-20, e é o que justifica (b) e (d):** sem (d) o rodapé carregaria **8**
     entradas permanentes, todas de pai já `done` (`TK-51`, `TK-53`, `TK-56`, `TK-57`, `TK-59`,
     `TK-60`, `TK-62`, `TK-64`); sem (b), mais **5** por verdade vacuosa, três delas de tíquete
     aberto sem subtarefa (`TK-38`, `TK-48`, `TK-55`).
     **A cláusula (d) é leitura declarada, não texto publicado:** a §2.5 não fala do status do pai.
     Ela deriva do enunciado do `DB-4` — o rodapé é lista de **decisão pendente**, e pai fechado não
     tem decisão pendente. Registrada assim para o dono poder derrubá-la sabendo o custo (as 8).
  2. **Linha própria, e a linha dos três contadores não se toca.** A `DB-38` fixa aquela linha em
     *"três campos ... sempre os três"*: acrescentar um quarto campo contradiria norma publicada. O
     campo novo sai em **linha própria**, sob o mesmo `--- pendências mecânicas ---`, que é o
     *"uma linha cada"* do `DB-4`. Literal: `candidato a fechamento: <ID> (<done>/<total>), ...`, IDs
     em **ordem alfabética crescente** (`DB-37` E-1), `<done>/<total>` pela `DB-36`; sem população,
     o literal exato `candidato a fechamento: nenhum` (espelha `blocked: nenhum`).
  3. **Mundo do teste: fixture, quatro casos.** Nada de aferir contra o diário vivo — ele muda por
     ato desta janela **e da outra janela de orquestração ativa**. A fixture traz: (i) pai vivo com
     >=1 filho, todos terminais → **aparece**; (ii) pai vivo com filho vivo → **não aparece**;
     (iii) pai já terminal com todos os filhos terminais → **não aparece**; (iv) pai com zero
     filhos → **não aparece**. Os quatro num corpus só, para que a asserção seja sobre a **linha
     inteira** e não sobre presença de substring.
  4. **Regressão da linha antiga:** teste que afirma que a linha dos três contadores segue idêntica,
     com os três campos e os mesmos literais.
- **Não fazer:** não alterar a linha `inbox de planos: ... · fila de memória: ... · blocked: ...`; não
  tocar `selecionar_next` nem a eleição de candidato a **despacho** (`_candidatos`, `_eh_elegivel`) —
  este card só acrescenta projeção de rodapé, não muda o que `next` elege; não aferir contra
  `docs/DIARIO_DE_OBRAS.md` nem contra `docs/plans/P-0741-modelo-conceitual.md`; não fechar nenhum
  pai (fechar é juízo do agente com o dono, que é o que a `DB-4` diz).

## TK-62 — A gramática de ID de `rdo.py` não reconhece subtarefa de tíquete

- **Status:** `done` · 2026-09-20 — aberto pelo `scrum-master` na abertura da janela dos seis
  tíquetes, por lacuna medida que bloqueia os seis (diretiva de execução do `P-0739`, item 3).

**O defeito, medido:** `_ID_HEADER_RE` (`.claude/tools/rdo.py:84`) é
`^### ((?:[A-Z0-9]+-)?T[0-9]+[a-z]?)(?=[\s—])` e `_HEADER_BRACKET_RE` (`.claude/tools/rdo.py:86-90`)
repete a mesma classe de ID. Ambas exigem `T` **seguido de dígitos**. O ID de subtarefa de tíquete é
`TK-<n><letra>` — prefixo `TK-`, depois dígitos: **nenhuma das duas leituras casa**. Medido nesta
janela: `review_evidence.py --plano docs/DIARIO_DE_OBRAS.md --tarefa TK-57a` sai
`FALHOU - tarefa: 'TK-57a' não encontrada em 'docs\DIARIO_DE_OBRAS.md'`, com o cabeçalho presente em
`docs/DIARIO_DE_OBRAS.md:1819`.

**A premissa que caiu:** a `DB-17` do `P-0739` publicou a forma `### TK-<n><letra> — <título>
[<modelo> · classe <classe>]` justificando-a com *"porque a subtarefa é executada como tarefa e
`rdo.py`/`review_evidence.py` já leem essa forma"*. Essa cláusula é **falsa**, e nunca foi
verificada: a `DB-22`, que fixou a gramática de ID, escreveu `(?:[A-Z0-9]+-)?T[0-9]+[a-z]?` — que
cobre `BKL-T2a` e **estruturalmente não pode** cobrir `TK-57a`.

**Alcance:** bloqueia o Passo 6 (dossiê de evidência) e o Passo 9 (`rdo.py close`) do
`scrum-master` para **toda** subtarefa de tíquete — os seis tíquetes desta fila, e todo tíquete
futuro.

**A rota já é doutrina publicada**, não decisão nova: `DB-21` — *"Limitação de instrumento não
dispensa gate — conserta-se o instrumento"* — e `DB-22` — *"a gramática de ID mora num ponto só, em
`rdo.py`"*.

**Para a spec de robustez (`TK-55`):** classe *o derivado cala onde deveria falar*, na variante mais
cara — aqui o derivado **não** calou, falhou ruidosamente; o que calou foi a **autoria**, que
publicou como fato conferido (*"já leem essa forma"*) uma afirmação que um comando de uma linha
teria derrubado. É o mesmo defeito que o `TK-60` combate em citação de seção, aplicado a citação de
**comportamento de código**.

### TK-62a — `rdo.py` reconhece `TK-<n><letra>` como ID de tarefa [Sonnet · classe implementacao]

- **Status:** `done` · 2026-09-20
- **Objetivo:** alargar `_ID_HEADER_RE` e `_HEADER_BRACKET_RE` em `.claude/tools/rdo.py` para
  reconhecer, além do `(?:[A-Z0-9]+-)?T[0-9]+[a-z]?` atual, a forma `TK-[0-9]+[a-z]?` da `DB-17`,
  sem alargar para nada além dessas duas. Regressão em `tests/test_rdo.py` e
  `tests/test_review_evidence.py` que discrimine ID de tíquete aceito de ID fora da gramática
  recusado. Caso medido que motivou: `TK-57a` em `docs/DIARIO_DE_OBRAS.md:1819`.
- **Arquivos-alvo:**
  - `.claude/tools/rdo.py`
  - `tests/test_rdo.py`
  - `tests/test_review_evidence.py`
- **Verificação:** `python .claude/tools/review_evidence.py --plano docs/DIARIO_DE_OBRAS.md --tarefa TK-57a --desde <ref> --out docs/RDO/evidencia/TK-57-TK-57a.md` sai **exit 0** e grava o arquivo — hoje sai exit 1 com `tarefa: 'TK-57a' não encontrada`. `python -m pytest` verde, sem queda do piso de **224**.
- **Pronto quando:** `_ID_HEADER_RE` e `_HEADER_BRACKET_RE` aceitam `TK-<n>` e `TK-<n><letra>` além do `(?:[A-Z0-9]+-)?T[0-9]+[a-z]?` atual, e **nada além dessas duas** — `## TK-62 — …` (nível 2, tíquete-pai) continua não sendo reconhecido como tarefa, e `### 2.5 — …` continua fora. Regressão **par presença-ausência** nos dois arquivos de teste.


## TK-63 — O mundo hostil dos testes de executável é herdado do host, não construído

- **Status:** `done` · 2026-09-20 — aberto pelo `scrum-master` no escalonamento 1 desta janela, por
  decisão do consultor de plano sobre a ressalva do `TK-56a`.

**Por que é tíquete próprio, e não card do `TK-57`:** a matéria é a continuação do `TK-57`, mas o
`TK-57` está `done` e a tabela de transições de §2.7 **não tem rota de reabertura** — `done` não é
origem de nenhuma transição. A `DB-23` também veda retroação em entrega fechada. O tíquete novo é a
residência correta; o `TK-57` permanece fechado como foi entregue e aprovado.

**O defeito, medido pelo consultor em 2026-09-20:** os dois sítios que **já** discriminam neste host
o fazem **por acidente de plataforma** — o mundo "sem `PYTHONUTF8`" só é hostil porque este host é
Windows-cp1252. Em host que exporte `PYTHONUTF8=1`, ou em plataforma cujo default já seja UTF-8, os
dois param de discriminar. É exatamente o defeito que abriu o `TK-57`, uma camada abaixo.

**Medida que fecha a questão:** `PYTHONIOENCODING` **prevalece** sobre `PYTHONUTF8` para `stdin`.
Logo o mundo hostil **construído** (`PYTHONIOENCODING=cp1252`) é hostil em qualquer host e em
qualquer plataforma — que é a metade que a `DB-53` não cobre.

### TK-63a — O mundo hostil do teste de executável é construído, não herdado do host [Sonnet · classe implementacao]

- **Status:** `done` · 2026-09-20 — **reescrito** após devolução `blocked` razão `premissa`, por
  conduta correta do executor: o card prescrevia shim com `__file__` preservado, e preservar
  `__file__` faz o TF ler o `backlog.py` e o **diário reais**, acoplando o teste a estado vivo
  escrito por outra janela de orquestração. A prescrição do shim **cai**; entra raiz relocada.
- **Objetivo:** os dois sítios que discriminam **por acidente de plataforma** — o mundo "sem
  `PYTHONUTF8`" só é hostil porque este host é Windows-cp1252 — passam a usar o mundo hostil
  **construído**. Em host que exporte `PYTHONUTF8=1`, ou em plataforma cujo default seja UTF-8, os
  dois param de discriminar hoje.
- **Arquivos-alvo:**
  - `tests/test_backlog.py`
  - `tests/test_ocupacao.py`
- **Verificação:** `python -m pytest tests/test_backlog.py tests/test_ocupacao.py` verde, coletando
  **>=91**; `python -m pytest` verde, sem queda do piso de **238**. Nenhum teste lê
  `docs/DIARIO_DE_OBRAS.md`, `docs/plans/*` ou `.claude/tools/backlog.py` **no lugar**.
- **Pronto quando:**
  1. **Mundo hostil construído.** Os dois mundos são `env` mínimo + `PYTHONIOENCODING=cp1252`
     (hostil) e `env` mínimo + `PYTHONUTF8=1` (seguro). O mundo "host sem a variável" deixa de ser o
     hostil — ele mede o host. Medido: `PYTHONIOENCODING` prevalece sobre `PYTHONUTF8`, então o
     mundo hostil é hostil até em host que exporte a variável.
  2. **`backlog_hook`: raiz relocada, sem shim.** O teste monta em `tmp_path` uma raiz falsa a
     partir de `tests/fixtures/backlog/next_tk90/` e copia para `<raiz>/.claude/tools/` **os dois**
     arquivos reais — `backlog_hook.py` e `backlog.py` — com `shutil.copy2`. Isso basta: o hook
     resolve `backlog.py` como irmão de `__file__` e a raiz a partir do `backlog.py`, de modo que
     todo o acoplamento se fecha **dentro** da raiz falsa. **Nenhum shim, nenhum `exec(compile(...))`,
     nenhum `__file__` apontando para a árvore viva.** Mesma técnica do `telemetria_hook` no `TK-56b`
     (aprovado 100%).
  3. **Par negativo é o produto revertido**, materializado por substituição textual sobre a fonte
     real (`assert <bloco do reparo> in fonte` antes), copiado para dentro da raiz falsa como o
     positivo. O `stub = tmp_path / "hook_quebrado.py"` **sai** dos testes que ainda o têm.
  4. **`ocupacao.py`: cópia simples em `tmp_path`** — não tem acoplamento por `__file__`; medido.
  5. **As asserções afirmam relação, nunca magnitude.** Três, e nenhuma envelhece: (i) **invariância**
     — o produto correto dá a mesma saída nos dois mundos; (ii) **divergência** — o produto revertido
     dá saídas diferentes entre eles; (iii) **não-vazio** — a saída do produto correto no mundo
     hostil é `!= b""`. **Nenhum `assert` cita número de bytes.**
  6. **A magnitude vive no docstring, com data e mundo, como registro — não como aceite.** Medidas de
     2026-09-20, a reproduzir: `backlog_hook` em raiz relocada sobre `next_tk90` → **737 B**
     idênticos nos quatro mundos, revertido **0 B** no hostil; `ocupacao` → **323 B** idênticos nos
     quatro mundos, revertido **335 B** no hostil.
- **Não fazer:** não ler o diário real, nenhum arquivo de `docs/plans/` e nenhum estado vivo em
  teste — foi o acoplamento que devolveu este card; não editar `.claude/tools/backlog_hook.py`,
  `.claude/tools/backlog.py` nem `.claude/tools/ocupacao.py` (os reparos estão corretos e aprovados);
  não reabrir `TK-57a` nem `TK-56a`; não tocar `docs/plans/P-0741-modelo-conceitual.md`.

## TK-64 — O `check-drift` está vermelho por linha de skill que nenhuma tarefa aberta possui

- **Status:** `done` · 2026-09-20 — aberto pelo loop na janela dos tíquetes do `P-0739`, por decisão
  do consultor de plano no escalonamento 2.

**O defeito, medido em 2026-09-20:** `pwsh .claude/checks/kit_check.ps1 -Mode check-drift` sai
**exit 1** porque `.claude/README.md` não tem a linha da skill `entrega-de-encerramento`. A skill é
entrega do `TK-51a`, **fechado** — o vermelho chega a esta janela sem dono e obrigou o reviewer a
reconciliar à mão em **três** revisões (`TK-62a`, `TK-56a`, `TK-56b`).

**Metade verde do guarda:** `materializar drift --alvo projeto` sai exit 0. Os "2 problema(s)" do
relatório são o cabeçalho e a linha de detalhe do **mesmo** defeito — contagem inflada, item já
roteado à spec de robustez (`TK-55`).

**Por que card e não ato direto do loop:** regenerar sem card põe uma edição de `.claude/README.md`
sem dono no recorte de evidência de toda revisão seguinte — falso positivo de escopo, classe do
`AE-4` do `P-0739`. O que apaga o vermelho é a atribuição, não o comando. O `TK-51a` não reabre
(`DB-23` do `P-0739`); o reparo nasce em card próprio, como `BKL-T2a`..`BKL-T3b` nasceram.

### TK-64a — Regenerar `.claude/README.md` pelo gerador do kit [Sonnet · classe implementacao]

- **Status:** `done` · 2026-09-20
- **Objetivo:** pôr `.claude/README.md` em dia com `.claude/skills/` rodando o gerador do próprio
  kit, para que o guarda pare de chegar vermelho a revisões que não o causaram.
- **Arquivos-alvo:**
  - `.claude/README.md`
- **Verificação:** `pwsh .claude/checks/kit_check.ps1 -Mode generate` sai **exit 0**;
  em seguida `pwsh .claude/checks/kit_check.ps1 -Mode check-drift` sai **exit 0** (hoje: exit 1);
  e `git diff --numstat .claude/README.md` devolve **`1	0`** — uma linha acrescida, nenhuma removida.
- **Pronto quando:** a única mudança na árvore é a linha nova da skill `entrega-de-encerramento` na
  região `<!-- kit:skills:begin -->`…`<!-- kit:skills:end -->` de `.claude/README.md`, escrita **pelo
  gerador** e não à mão; a linha traz a `description` do `SKILL.md` **íntegra**, com travessão `—` e
  acentuação (`É o artefato pelo qual o dono valida o plano`) — medido em cópia via `-KitRoot` em
  2026-09-20: 9 agentes, 11 skills, `52a53`, delta de exatamente uma linha.
- **Não fazer:** não editar `.claude/skills/entrega-de-encerramento/SKILL.md` — a `description` é a
  **fonte**, e é entrega fechada do `TK-51a`; não editar `.claude/README.md` à mão nem fora da região
  marcada; não tocar `.claude/checks/kit_check.ps1` (o `-` e o caractere de substituição vistos no
  console são renderização do `Write-Host`, não conteúdo — não há defeito de codificação a corrigir);
  não reabrir o `TK-51a`.
## TK-65 — Três defeitos medidos de `backlog.py` na abertura da janela do `P-0741`

- **Status:** `ready` · 2026-09-20 — aberto pelo consultor de plano do `P-0741` no escalonamento
  `ESC-1`; os três achados são `AE-2`, `AE-3` e `AE-4` de `docs/plans/P-0741-modelo-conceitual.md`
  (seção `## Achados da execução`), atribuídos a `.claude/tools/backlog.py` e vedados ao plano
  pelo invariante `I-3` dele.

**Por que um tíquete e não cards do `P-0741`:** o plano proíbe, no `I-3`, que qualquer card edite
`backlog.py`; e os três defeitos são do instrumento de fila, não do modelo conceitual. O que o
`ESC-1` reparou foi o **plano** (`DMC-19`: `Depende de` só com id de item, proveniência no campo
novo `Fundamento`) — o instrumento continua aceitando calado a forma que trava a janela.

**Ordem sugerida:** `TK-65b` (o mais barato e o que mais atrapalha o diagnóstico dos outros dois),
depois `TK-65a`, depois `TK-65c`. Nenhum depende do outro.

### TK-65a — `check` recusa id de `Depende de:` que não é item [Sonnet · classe implementacao]

- **Status:** `ready` · 2026-09-20
- **Objetivo:** acrescentar ao `check` uma violação de vocabulário fechado (`C-*`, como as demais)
  que acuse `- **Depende de:**` citando id sem item correspondente na árvore, e prosa no campo.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
- **Verificação:** par presença-ausência sobre fixture — `check` acusa a violação sobre um plano
  cujo card cita em `Depende de:` um id que não é item (ex.: `` `DMC-1` ``), e **não** acusa sobre
  o mesmo plano com o campo em ids de tarefa; `python -m pytest tests/test_backlog.py` verde.
- **Pronto quando:** a violação nova existe, é nomeada no vocabulário fechado do `check`, e o
  teste é par presença-ausência sobre corpus em que as duas leituras dariam resultados diferentes.
- **Caso medido que motivou (2026-09-20):** `check` devolveu `check: OK — nenhuma violação` sobre
  a árvore em que as cinco tarefas do `P-0741` estavam inselecionáveis, e `next` devolveu
  `nada delegável — 0 elegível(is) · blocked 0`. O lint aprovou um plano que o seletor não
  consegue percorrer; o defeito só apareceu no gate de despacho, com a janela já aberta.
- **Não fazer:** não mexer em `_eh_elegivel` nem na semântica de `next` — o campo é lista de ids
  de item por gramática publicada (skill `diario-de-obras`, *Item e residência*); o que falta é o
  lint recusar quem desvia, não o seletor tolerar.

### TK-65b — O ponto de carga escreve em utf-8 antes de argparse abrir a boca [Sonnet · classe implementacao]

- **Status:** `ready` · 2026-09-20
- **Objetivo:** mover a reconfiguração de encoding de `main()` para antes de `parse_args`, de modo
  que `--help` e toda mensagem de erro de argparse — que imprimem o `usage` com `→` — saiam sem
  `UnicodeEncodeError` em console cp1252.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py` (`main()`, hoje: `reconfigure` em `:1415`, `parse_args` em `:1411`)
  - `tests/test_backlog.py`
- **Verificação:** par presença-ausência por subprocesso com o ambiente hostil explícito
  (`PYTHONIOENCODING` vazio, `-X utf8=0`): `backlog.py --help` sai **exit 0** e imprime o `usage`;
  hoje o mesmo comando sai em traceback. `python -m pytest tests/test_backlog.py` verde.
- **Caso medido que motivou (2026-09-20):**
  `PYTHONIOENCODING= python -X utf8=0 .claude/tools/backlog.py --help` →
  `UnicodeEncodeError: 'charmap' codec can't encode character '→' in position 611`.
  É a metade de **escrita** do defeito que o `TK-56a` fechou na leitura.
- **Não fazer:** não trocar o `→` do texto de ajuda por ASCII — o defeito é do ponto de carga, não
  do texto; não tocar os outros pontos de carga já fechados pelo `TK-56a`.

### TK-65c — O verbo `diretiva` não descarta id em silêncio [Sonnet · classe implementacao]

- **Status:** `ready` · 2026-09-20
- **Objetivo:** `diretiva` passa a reportar quantos ids reconheceu e a recusar (ou a acusar) o
  texto em que há id entre crases **depois** do ` — `, que hoje é cortado e perdido.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py` (`_parse_diretiva`, `:326`)
  - `tests/test_backlog.py`
- **Verificação:** par presença-ausência — a escrita de uma diretiva com ids depois do travessão
  produz saída que nomeia os ids descartados (ou recusa a escrita), e a escrita de uma diretiva
  bem-formada segue silenciosa; `python -m pytest tests/test_backlog.py` verde.
- **Caso medido que motivou (2026-09-20):** `_parse_diretiva` sobre
  ``**Diretiva de priorização:** Priorize `P-0741` — e depois `TK-57`, `TK-56` `` devolve
  `['P-0741']`: os tíquetes que a própria diretiva do dono manda priorizar saem da fila sem aviso.
  Na janela do `P-0741` isso produziu uma fila filtrada a um único item e uma inversão de
  prioridade que só a leitura do código explicou.
- **Não fazer:** não passar a colher ids da cauda livre — a cauda é para humanos por gramática
  publicada (skill `diario-de-obras`, *Cabeçalho do diário*); o reparo é tornar o descarte
  **audível**, não mudar o que o campo significa.

## TK-66 — O atribuidor de `review_evidence.py` fabrica autoria com tarefa nunca despachada

- **Status:** `ready` · 2026-09-20 — aberto pela janela de orquestração do `P-0743` ao fechar a
  `DOM-T2`; o achado é o `AE-3` de `docs/plans/P-0743-modelo-de-dominio.md` (seção
  `## Achados da execução`), atribuído a `.claude/tools/review_evidence.py` e vedado ao plano pelo
  invariante `I-1` dele, que proíbe qualquer card de editar o instrumento.

**Fato medido (2026-09-20, janela do `P-0743`).** Ao montar a evidência das tarefas `DOM-T1` e
`DOM-T2`, `python .claude/tools/review_evidence.py --plano docs/plans/P-0743-modelo-de-dominio.md
--tarefa <ID> --desde e0efcf6 --atribuir` devolveu **quatorze** arquivos rotulados
`alvo-de-outra-tarefa (DOM-T3)`, `(DOM-T4)` e `(DOM-T5)`. Nenhuma dessas três tarefas havia sido
despachada — todas em `ready`, com zero entrega. Os arquivos (`.claude/agents/pantonic-*.md`,
`.claude/tools/modelo.py`, `.claude/tools/rdo.py`, `README.md`, `.claude/README.md`,
`tests/fixtures/modelo/*`, `tests/test_modelo.py`, entre outros) eram entrega **não commitada** da
janela paralela que conduz o `P-0741`.

**Por que importa.** A diretiva de execução do `P-0740`, item 3, trocou commit por tarefa por
**commit no marco**. Nesse regime o recorte `--desde <ref>` sempre mistura entregas, e a atribuição
é o **único** mecanismo que diz de quem é cada arquivo — é exatamente onde a `B0` do `scrum-master`
decide se um vermelho rebaixa a entrega ou vira achado de outro dono. Um atribuidor que inventa
autor não é ruído: ele contamina a decisão de rota com a aparência de medida. Nas duas revisões
desta janela o despacho teve de **desmentir por escrito a evidência mecânica** que ele próprio
gerou.

**Causa provável.** O casamento caminho → tarefa percorre os `Arquivos-alvo` declarados de todas as
tarefas do plano e não consulta o `status` de nenhuma. Uma tarefa `ready` tem alvos declarados e
zero autoria; o instrumento trata as duas coisas como a mesma.

**Rotas candidatas (o tíquete não decide qual — é do planejamento).**

1. Filtrar a atribuição pelas tarefas cujo `status` seja `in-progress`, `review` ou `done` — as
  únicas que podem ter escrito algo. Tarefa `ready` deixa de casar.
2. Manter o casamento e criar categoria própria — `alvo-de-tarefa-nao-despachada` —, separada de
  `alvo-de-outra-tarefa`, para que quem lê veja que aquilo é **previsão**, não autoria.
3. Cruzar com o recorte temporal: se o arquivo já estava modificado na árvore **antes** do
  `--desde` do despacho, rotular como `anterior-ao-recorte`, seja qual for o alvo declarado.

**Não é escopo deste tíquete:** o `--desde` em si, nem a decisão de commitar por tarefa — essa é
ato do dono e está fechada na diretiva do `P-0740`.

## TK-67 — A rodada de revisão de guardrails está pendente desde 2026-08-08

- **Status:** `ready` · 2026-09-21 — aberto pela sessão de planejamento do `P-0745`, quando a skill
  `checar-versao-kit` armou o gatilho de `GOVERNANCA.md` §7.1 na criação do plano.

**Fato medido (2026-09-21).** O **registro das rodadas** de `GOVERNANCA.md` §7.1 tem duas entradas:
`1.4.0` (2026-08-01, primeira aplicação) e `P-0731` (2026-08-08, primeira rodada do regime por
fechamento de plano). Desde então **sete** planos foram a `done` no índice deste diário — `P-0732`,
`P-0735`, `P-0736`, `P-0738`, `P-0739`, `P-0740` e `P-0743` — e **nenhuma** rodada foi registrada.
No mesmo intervalo §7 passou de **14** guardrails para **20**: nasceram `G-SCOPE`, `G-SURFACE`,
`G-REPLAN`, `G-NOASK`, `G-MODULO` e `G-TOOLDENY`.

**Por que é tíquete e não ato da skill.** §7.1 é explícito: a skill *arma* o gatilho e reporta, mas
*"não executa a revisão — ela é tarefa nomeada, com registro próprio no diário"*. Este é o registro.

**O que a rodada faz, quando for despachada.** Aplica a **pergunta única** de §7.1 — *"esta regra
mudou algum comportamento desde a penúltima rodada registrada? Cite o caso."* — a cada guardrail
**em escopo e não isenta**:

1. **Escopo** — só guardrail com ≥2 rodadas de idade, isto é, a que já constava de §7 na penúltima
   rodada registrada. Enquanto o registro não tiver duas rodadas **deste regime**, a `1.4.0` faz as
   vezes de penúltima (ressalva escrita na própria entrada do `P-0731`): entram as **13** que
   existiam em 2026-08-01, pelo nome e não pelo número — a numeração deslocou duas vezes desde
   então. Os seis nascidos depois ficam **fora por idade**.
2. **Isenção por enforcement executável** — guardrail verificado por check ativo não entra na
   pergunta, e quem a invoca **nomeia o check e confirma que ele roda hoje**. Na rodada do `P-0731`
   foram seis isentos, com os checks confirmados no consumidor `PantonicVideo`; a rodada nova
   re-confirma, não herda.
3. **Caso citável** é ocorrência **registrada** no intervalo — diário do hub ou de um consumidor,
   `CHANGELOG.md`, nota de fechamento, decision record. Suíte verde não é caso; lembrança sem
   registro não é caso.
4. **Saída** — a entrada nova no *Registro das rodadas* de §7.1, com o plano que a disparou, as
   guardrails avaliadas, as fora por idade, as isentas com o check nomeado e o resultado item a
   item; mais a deprecação do que não passar.

**Insumo farto, e é o motivo de a rodada valer agora.** O intervalo carrega sete planos, os achados
`AE-*` de `P-0739`, `P-0740`, `P-0741` e `P-0743` e a entrega aceita em
`docs/Entregas Aceitas/Entregas - P-0743.md` — material medido que não existia na rodada anterior.

**Não é escopo deste tíquete:** criar guardrail novo. A porta de §7.1 é de **saída**.

## TK-68 — A cópia do kit das regras globais divergiu do arquivo que o dono carrega

- **Status:** `ready` · 2026-09-21 — aberto pela sessão de planejamento do `P-0745`, ao confrontar
  as duas cópias antes de decidir quem edita o quê na `PLN-T2`.

**Fato medido (2026-09-21).** `C:/Users/panta/.claude/CLAUDE.md` (12.752 bytes, 2026-09-04) e
`.claude/global/CLAUDE.md` (10.751 bytes, 2026-08-24) **diferem**. A diferença é de uma direção só:
o arquivo do dono carrega, sob a Regra 1, os **Controles 1.1** (*persistir o plano é encerramento do
planejamento, não execução*) e **1.2** (*não abrir sessão de planejamento sobre alvo que já tem
plano aprovado*) — 28 linhas nascidas do incidente medido de 2026-09-04 no `PantonicVideo` — e a
cópia do kit não os tem. Nenhuma outra região diverge: em especial, o bullet *Capacidade* da Regra 2
e o bullet *Orçamento por tarefa atômica* da Regra 7 são **idênticos byte a byte** nas duas — é o que
permite à `PLN-T2` do `P-0745` editar as duas com o mesmo literal.

**Por que importa.** `.claude/sync-kit.ps1` **não projeta** `.claude/global/` — busca por `global` no
script não retorna ocorrência. As duas cópias se mantêm à mão, nada as afere, e a do kit é a que
viaja para os projetos derivados. Consequência prática: um projeto Pantonic* que receba o kit hoje
herda regras globais **sem** os dois controles, e a sessão seguinte pode repetir exatamente o defeito
que eles existem para impedir — planejar duas vezes o mesmo alvo, ou aprovar plano que nunca é
gravado.

**Rotas candidatas (a decidir na execução, não aqui).**

1. Trazer os Controles 1.1 e 1.2 para `.claude/global/CLAUDE.md` e declarar o arquivo do dono como
   fonte, com um check que compare as duas.
2. Fazer `sync-kit.ps1` projetar `.claude/global/`, transformando a cópia em projeção de verdade.
3. Declarar as duas cópias como residências distintas por desenho — o que exige dizer, em
   `docs/RESIDENCIA_DOUTRINA.md`, o que cabe em cada uma.

**Não é escopo deste tíquete:** o percentual de ocupação e a tabela de tetos, que as duas cópias
carregam hoje e que a `PLN-T2` do `P-0745` reescreve **nas duas** (`DPN-12`).
