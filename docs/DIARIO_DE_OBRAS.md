# Diário de Obras — PantonicApp (hub de governança Pantonic*)
**Diretiva do dono (2026-09-26, vigente até o fechamento da auditoria final):** *"Execute em loop as tarefas abertas."* (1) O objetivo é **esgotar os tíquetes e planos abertos hoje**, para desbloquear o plano de auditoria final; (2) **nenhum card nem tíquete novo por ajuste**: achado novo vira `AE-<n>` com rota "auditoria final"; (3) tíquete ou card que o dono não abriu **fecha pelo condutor**, sem pedir o veredito do dono.

**Diretiva de priorização:** Priorize `P-0755` — o plano sucessor da auditoria final (as 31 recomendações do relatório, 40 cards em cinco etapas); Marco 1 com go do dono em 2026-09-28 ("Marcar como aceito, e colocar o plano no topo da fila para próxima janela"). O loop abre em janela nova, com o plano como único insumo (recomendação R-01 em prática), e para ao fim de cada etapa, nos Marcos 2 a 6. Fora da fila, atos do dono: o veredito do Marco 3 do plano P-0754 (documento de validação pronto na pasta dele), o commit do WIP e a projeção da camada global em ~/.claude (materializar.py apply).

**`P-0753` — FECHADO `done` 21/21 em 2026-09-28, pelo aceite do dono** (*"Conclua o que estiver pendente, e me entregue o plano concluído"*). Entrega: `docs/plans/P-0753-auditoria-estagio-1/entrega.md` · validação: `docs/plans/P-0753-auditoria-estagio-1/operacoes.md`.

**`P-0742` — CANCELADO `cancelled` 0/8 em 2026-09-27, no-go do dono no Marco 1.** O loop não sai do LLM: o `scrum-master` fica no loop. A mecanização das ações mecânicas dele e a otimização das rotinas vão à auditoria final:
- **AE-95** (`P-0742`, Marco 1, 2026-09-27) — matéria de avaliação herdada do `P-0742` cancelado: o `scrum-master` **continua** no loop, porque a orquestração de vários agentes ainda pede julgamento em casos não padronizados; o que se avalia é **mecanizar as ações mecânicas** do `scrum-master` (os passos que já são materialização por instrumento — apurar a fila, capturar o `<ref>`, coletar a evidência, gravar telemetria, fechar a tarefa) e **otimizar as rotinas dele**, sem tirar o agente do loop. Insumos: o problema medido na `## 0` do `P-0742` (orquestrar uma tarefa custa $2–6, 7–13 turnos do orquestrador por despacho) e os fatos `F-*` e o roteamento da `## 12` de `docs/plans/P-0742-loop-fora-do-llm.md`. Veredito do dono, verbatim: *"Eu não concordo em tirar o agente scrum-master do loop, acho que é necessário algum nível de julgamento no processo, pois a orquestração de multiplos agentes eventualmente requer tratar diversos casos  não padronizados ainda. O que eu concordo é que pode existir potencial para ganhor mecanizado ações mecânicas do scrum-master ou otimizar as rotinas dele. Mas essas tarefas podem ser herdadas no plano de auditoria. Deixe registrado na spec do plano de auditoria essa matéria de avaliação, e encerre este plano"* **Rota:** auditoria final — entra na spec do plano de auditoria final como item de avaliação.

**`P-0752` — FECHADO `done` 17/17 em 2026-09-27, pelo aceite do dono** (*"Marcar como concluído o que estiver esperando validação."*). Entrega: `docs/plans/_ENTREGA-P-0752.md` · validação: `docs/OPERACOES_AS_IS_P-0752.md`.

**`P-0751` — FECHADO `done` 16/16 em 2026-09-26, pelo aceite do dono** (*"Rode o revisor, considere o veredito do 0751 aceito e encerre."*). Entrega: `docs/plans/_ENTREGA-P-0751.md` · validação: `docs/OPERACOES_AS_IS_P-0751.md`.

**`P-0750` — FECHADO `done` 6/6 em 2026-09-25, pelo aceite do dono** (*"continue executando as tarefas em aberto. O desejo é esgotar o backlog para priorizar os testes em projetos reais. No que depender de aceite, considerar aceito."*). Regra da mensagem legível ao dono em `GOVERNANCA.md` §4.2 com eco na Regra 9 de `.claude/global/CLAUDE.md`, glossário das famílias de sigla no `README.md`, `docs/FALHAS_COMUNICACAO.tsv` com as 3 falhas medidas, skill `mensagem-ao-dono`, e os textos que mandavam citar sigla ao dono passam a mandar o título. 6 aprovados 100%, 9 achados (`AE-1`..`AE-9`), todos com rota. Modelo versão 1 vigente, `modelo check` 0. Documento de validação: `docs/OPERACOES_AS_IS_P-0750.md`. Pendência com efeito fora do repositório: o `apply` do regulamento global em `~/.claude/` (ato do dono, `TK-68`). **Nada commitado.**

**`P-0749` — FECHADO `done` 10/10 em 2026-09-25, pelo aceite do dono** (*"conclua o plano atual 749 e inicie o 750 nesta mesma janela logo em sequencia"*), com o veredito sobre as trocas `M1`..`M6` do `README.md` incluso. 7 achados (`AE-1`..`AE-7`), todos com rota. Modelo na versão 1 vigente, `modelo check` 0. Documento de validação: `docs/OPERACOES_AS_IS_P-0749.md`. **Nada commitado.** O instrumento recusa `ready → done` para plano (tabela de §2.7 do `backlog.py`); o fechamento foi escrito à mão, como nos planos anteriores.

**`P-0746` e `P-0741` — FECHADOS em 2026-09-24, pelo aceite do dono** (*"Aceite os planos, revise os tiquetes para ver quais são pertinentes ainda para enfileira-los na sequencia"*). `P-0746` `done` 7/7: Marcos 2 e 3 fechados, modelo promovido à **versão 4 vigente** (a 3 obsoleta, bloco `## 1A` retirado), documento de validação `docs/OPERACOES_AS_IS_P-0746.md`; a pendência `AE-18` (critério de ator inédito) **não** foi decidida no ato e segue no `TK-73` Pacote 2. `P-0741` `done` 8/8: `MC-T5` `review` → `done` com o veredito do Marco 2, RDO gerado. Revisão de pertinência dos 17 tíquetes `ready`: 3 fechados (`TK-69` absorvido pelo `P-0746`, `TK-48` caducou, `TK-80` absorvido pelo `TK-72`), 14 enfileirados na diretiva acima. Instrumentos: `backlog check` 0 · `modelo check` 0 no `P-0746`. **Nada commitado.**

**`P-0748` — FECHADO `done` 17/17 em 2026-09-24, com o aceite do dono no Marco 3.** Veredito verbatim: *"Vamos aprovar esse plano e ver ele ocorrendo na prática."* e *"Aceite os planos, revise os tiquetes para ver quais são pertinentes ainda para enfileira-los na sequencia"*. O painel do gerente passa a ser gerado pelo gancho `.claude/tools/progresso_hook.py` a partir do evento de cada transição do loop, com o título da tarefa no lugar da sigla, em `.claude/estado/progresso.txt` (aberto por `Get-Content -Path .claude/estado/progresso.txt -Wait -Tail 30 -Encoding utf8`). Na primeira leitura do Marco 3 o dono aceitou a forma e recusou a confiabilidade (`DTG-42`); os corretivos `TLG-T3c`..`TLG-T3h` e `TLG-T5a` fecharam cada linha que se perdia ou afirmava o que não aconteceu. Modelo na **versão 4 vigente**. Instrumentos: `backlog check` 0 · `modelo check` 0 · `313 passed`. Documento de validação: `docs/OPERACOES_AS_IS_P-0748.md`. **Nada commitado.** Pendências com rota: `TK-79` (prosa depois da linha de retorno do executor), `TK-80` (régua de autoria: `AE-13` e `AE-1`), `TK-81` (propagação aos derivados), `TK-55` (ponteiro para `AE-4`/`AE-5`/`AE-11`), `AE-28` (registro, sem efeito funcional). **Próxima janela: a diretiva acima, em contexto novo.**

**`P-0747` — FECHADO `done` 19/19 em 2026-09-23, com `go` do dono no marco de fechamento.** Veredito verbatim: *"pode fechar esse plano, irei iniciar um plano novo na próxima janela"*. O consultor virou papel de doutrina (linha *Consultoria* da matriz de `GOVERNANCA.md` §3), triagem de toda parada de executor, forma efêmera com cenário persistido **adotada** no piloto ($2,8 equivalente-Opus por acionamento contra $3,7 da prontidão; amostras em Fable, declarado na spec §11). 8 cards de autoria e 11 corretivos, 18 aprovados 100% e `CON-T8` com ressalva 93; zero reprovações e zero perguntas ao dono na execução. Modelo em **versão 2 vigente**, promovida no fechamento (inclui a recusa de impedimento improcedente, `DCS-35`). Instrumentos: `backlog check` 0 · `modelo check` 0 · `277 passed` · frontmatters YAML ok. Documento de validação: `docs/OPERACOES_AS_IS_P-0747.md` — **cobre 17 das 19 tarefas**: as seções de `CON-T2b`/`CON-T3d` e a nova validação do consultor sobre a v2 emendada foram dispensadas pelo fechamento. **Nada commitado** (commit é ato do dono, `DCS-16`). Pendências herdadas, com rota: `AE-24` (passo 8 sem saída para o redespacho), `AE-17`/`AE-18`/`AE-23` (redação), `TK-72`, `TK-77`, `TK-66`, `TK-55`, e a cópia do dono em `~/.claude/CLAUDE.md` com a Regra 8 antiga. Nesta janela também fechou o `TK-76`. **Próxima janela: plano novo, por decisão do dono.**

**`P-0745` — FECHADO `done` 10/10 em 2026-09-22, com `go` do dono no Marco 3.** Veredito verbatim:
*"Pode concluir o plano"*. Documento de validação: `docs/OPERACOES_AS_IS_P-0745.md` (563 linhas,
cobertura 10/10 conferida por comando). O plano nasceu com 7 cards e ganhou **3 corretivos**
(`PLN-T4a`, `PLN-T5a`, `PLN-T7a`), somados às operações que reparam. Vereditos: 7 × `aprovado` 100%,
3 × `ressalva` (88%, 94%, 83%), **dimensão bloqueante em nenhum**. Modelo em **versão 4 vigente**
(`go` do Marco 2 no mesmo dia), `estágio atual: concluído`. Estado dos instrumentos no fechamento:
`backlog.py check` exit 0 · `modelo.py check` exit 0 · `277 passed`. Os **26 achados** (`AE-1`..`AE-26`)
estão triados, todos com `**Rota:**` explícita.

**O QUE A PRÓXIMA JANELA PRECISA SABER — planejamento do consultor (decisão do dono, 2026-09-22).**

1. **As diretivas do dono já estão gravadas** em `docs/consultant-spec.md` §3, subseção *Ato do dono
   de 2026-09-22*: `DC-1` (questão não correlata ao modelo é tática, e tática é do consultor, não
   sobe ao dono) · `DC-2` (a guarda é o drift do modelo; havendo drift, para e pede decisão do dono)
   · `DC-3` (decisão técnica ou tática do consultor não passa por validação do dono) · `DC-4` (o
   consultor é o ponto de triagem de **toda** parada de executor, e decide entre model designer,
   planejador ou resolver). A §2, classe 1 de gatilho, foi estendida aos três motivos.
2. **`TK-75` NÃO se abre — a matéria virou o `P-0747`** (`docs/plans/P-0747-consultor-de-plano.md`,
   `DCS-1`), registrado em 2026-09-22 pelo `pantonic-planner` sob o protocolo novo (SAÍDA 3 +
   autoria do `pantonic-model-designer`, três dossiês antes do primeiro card): 8 cards `CON-T1`..
   `CON-T8`, um por operação, `modelo.py check` e `backlog.py check` exit 0, **`blocked` até o `go`
   do dono no Marco 1** sobre a versão 1 do modelo. Linha no `_INBOX.md` por drenar. O veredito da
   sessão sobre os procedimentos do `P-0743`/`P-0745`/`P-0746`, com o custo medido, está em
   `docs/plans/_VEREDITO-procedimentos-2026-09-22.md`. O registro original da lacuna segue: três
   residências do kit **contradizem** a spec do consultor e não foram tocadas de propósito, por
   decisão do dono de fechar o `P-0745` antes: **(a)** `.claude/skills/scrum-master/SKILL.md` —
   regras `A3a`/`A3b`/`A3c` do bloco A, o passo 8 e a lista *O que obriga parada*, que roteiam a
   parada de executor **em volta** do consultor; **(b)** `GOVERNANCA.md` §3 (matriz de
   responsabilidades) e §7 (`G-REPLAN` item 17, `G-NOASK` item 18); **(c)**
   `.claude/agents/pantonic-consultant.md`, conduta e estatuto. **Regra de precedência vigente,
   fixada pelo dono e escrita na spec:** enquanto o bloco A não for reescrito, **a spec prevalece**.
   Causa medida da lacuna: o bloco A tem fonte no `P-0734`, que abriu em 2026-08-08; o consultor foi
   criado em 2026-09-18, e a palavra *consultor* **não ocorre nenhuma vez** naquele plano.
3. **Insumo medido para esse planejamento, colhido nesta janela:** o consultor foi acionado **sete
   vezes** e resolveu **todas** como tática, sem escalar nada ao dono — incluindo criar três cards
   corretivos e devolver três dossiês `Ato de modelo` de lastro. Duas paradas idênticas de executor
   tiveram desfechos opostos: a `PLN-T2` (manhã, antes da `DC-4`) encerrou a janela e chegou ao dono
   como três opções táticas; a `PLN-T5` (tarde, sob a `DC-4`) foi triada, reparada e devolvida ao
   loop sem round-trip. Custo em `docs/telemetria.tsv`, linhas `*-consultor-*` de 2026-09-22.
4. **Pendências herdadas, com texto pronto:** `TK-72` recebe **quatro** emendas à régua de autoria de
   card, todas redigidas verbatim nos achados do `P-0745` (`AE-16` de quem é o número; `AE-17` que
   pergunta o comando responde; `AE-24` varredura pelo conceito aposentado; `AE-25` guarda de
   invariante afere contagem, não pertinência) — custo de redação zero. `TK-66`/`TK-74` recebem as
   facetas de instrumento (`AE-3`, `AE-9`, `AE-11`, `AE-18`, `AE-21`, `AE-23`). `TK-68` ganha um
   segundo caso: a cópia global do dono está correta e **sem guarda executável**.
5. **Estado da árvore:** nada commitado. Convivem o WIP do `P-0746` (7/7, **sem fechamento**) e as
   dez entregas do `P-0745`. Enquanto não commitar, `review_evidence.py --desde <ref>` não isola a
   entrega e toda revisão exige aviso à mão mais reconciliação por hunk e mtime.

<!-- fila:gerada -->
**Fila corrente:** nada delegável — 0 elegível(is) · blocked 0
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
| P-0737-AUT | Loop autônomo — o plano que consolida a `EXECUCAO-AUTONOMA`: 10 tarefas (`AUT-T1..T10`), decisões `DU-1..DU-13`, absorve as 8 tarefas abertas do `P-0734` e 11 tíquetes, poda 10 e encaminha 2;… | superseded *(sucedido pelo `P-0740-loop-de-modulos` em 2026-09-18, `DM-1` — a condição do bloqueio (`P-0738` fechar) foi satisfeita e a razão de fundo (custo fixo de contexto) caiu com a correção do denominador de janela para 1M; as 7 tarefas abertas foram absorvidas e reagrupadas em módulos, e **entregues** — o `P-0740` fechou `done 35/35`, com o piloto do §8(a) cumprido na `LM-T6` e **veredito do dono APROVADO** em 2026-09-19. Condensado para o histórico em 2026-09-21)* | docs/DIARIO_HISTORICO.md#p-0737--loop-autônomo |
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
| TK-38 | **Comunicação entre agente e humano — skill própria e requisitos mínimos.** Aberto por decisão do dono em 2026-08-13. O framework nomeia objetos de projeto por prefixo abreviado (`DP-`, `DR-`,… | cancelled | docs/DIARIO_DE_OBRAS.md#tk-38--comunicação-entre-agente-e-humano--skill-própria-e-requisitos-mínimos |
| TK-48 | `~/.claude/settings.json` **perdeu a chave `hooks` inteira silenciosamente**, sem ação intencional do dono, entre a `RPC-T4` e a escolha da `RPC-T5` — os 4 hooks registrados (premissa da `T5`) somem sem rastro. | cancelled | docs/DIARIO_DE_OBRAS.md#tk-48--~/claude/settingsjson-perdeu-a-chave-hooks-inteira-silenciosamente |
| TK-53 | O que mudou no corte da `95db6421…` que desloca o custo opaco de abertura de janela para as 6 janelas pós-corte inteiras (mediana 46.070 vs. 34.347 do grupo `antes`) — decisão do dono em 2026-08-24 sobre o achado do `TK-51`, causa ainda não investigada. Bloqueia `P-0737`. | done *(**desfecho negativo, decisão do dono em 2026-08-31** — a `TK-53a` mediu que não há degrau no corte: os dois regimes (`cache_read` 18.084 e 26.695) coexistem **antes e depois** dele, então a causa procurada não existe. `TK-53b` **cancelada por absorção** (seu insumo único, o bracket temporal, perdeu o objeto). A pergunta viva migrou para `TK-54`: não *o que mudou*, mas *do que o custo é feito*)* | docs/DIARIO_DE_OBRAS.md#tk-53--causa-do-deslocamento-de-custo-nas-janelas-pós-corte |
| TK-54 | **Extrato do custo de abertura de uma janela principal.** O 1º `usage` decompõe-se em uma linha por fonte carregada, com tamanho medido, origem (nossa ou do harness) e classificação em *válido / necessário / dispensável / economizável* — o detalhamento sem o qual o dono não decide corte nenhum. Substitui o objetivo morto da `TK-53`. Bloqueia `P-0737`. | cancelled 2/2 | docs/DIARIO_DE_OBRAS.md#tk-54--extrato-do-custo-de-abertura-de-uma-janela-principal |
| TK-55 | **Confiabilidade de agente e de instrumento.** Acumulador dos casos em que um **derivado** (comando de aceite, piso de regressão, linha de telemetria, achado de lint, linha de índice) erra sem sinal porque nada o confronta com a fonte — `AE-19`, `AE-18`, `AE-3`, `AE-1` e a projeção de índice desatualizada por um dia inteiro em 2026-09-19. Não é erro de execução de tarefa: a janela que os produziu fechou oito tarefas com zero reprovações. | cancelled | docs/DIARIO_DE_OBRAS.md#tk-55--confiabilidade-de-agente-e-de-instrumento |
| P-0741-MC | O modelo conceitual do plano: a interface entre o dono e o loop | done 8/8 | docs/plans/P-0741-modelo-conceitual.md |
| TK-56 | **Propagar o reparo de codificação de `stdin` aos três pontos de carga restantes.** `ocupacao.py:141`, `telemetria_hook.py:213` e `modelo_por_fase_userpromptsubmit.py:101` leem `sys.stdin.read()` e decodificam na codificação do host; em Windows sem `PYTHONUTF8` isso é `cp1252`. O terceiro é **global** e roda a cada prompt em todos os projetos — vem degradando em silêncio para prompt acentuado. Regra de reparo pronta na `DB-53` do `P-0739`. Depende do `TK-57`. | done 2/2 | `docs/DIARIO_DE_OBRAS.md` › `## TK-56` |
| TK-57 | **Fixar o ambiente no teste por subprocesso do hook.** `test_tf_hook_executavel_*` em `tests/test_backlog.py` herda o ambiente do `pytest`: em host com `PYTHONUTF8=1` passa com ou sem o reparo, deixando de discriminar. Aplicar as três cláusulas da `DB-53` — roda o processo, fixa `env=` explícito, afirma a invariância entre os dois mundos. **Pré-requisito do `TK-56`.** | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-57` |
| TK-58 | **Fechar a metade `usage_1` da medida de pickup.** O método `DC-4` tem duas metades; a de caracteres está publicada (26.760, −65,5%), e a do primeiro `usage` de uma sessão nova ficou **declarada sem valor** na `## 14` de `docs/CUSTO_DO_PICKUP.md` por não ser observável de dentro de um subagente. Exige abrir uma janela principal nova e ler o primeiro `usage`. | done 4/4 | `docs/DIARIO_DE_OBRAS.md` › `## TK-58` |
| TK-59 | **Guarda para o contador de id do inbox.** `**Próximo id de plano:**` é recalculado por `max(id visto) + 1` sobre o que passou pelo inbox; plano criado sem linha de inbox fica invisível e o contador aponta para id já usado. Ocorreu com o `P-0742` e foi corrigido à mão para `P-0743`. Falta um verificador que confronte o contador com `docs/plans/`. | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-59` |
| TK-60 | **Verificador de citação de seção.** O kit resolve caminho de arquivo (`Test-Path`) e identificador de tarefa (`review_evidence`), mas **nada** resolve *“§X.Y publicada em Z”*. Um ponteiro para seção inexistente atravessou autoria, transcrição aprovada em 100%, duas varreduras e um despacho, e só caiu quando um executor foi abrir o arquivo para editar. | done 3/3 | `docs/DIARIO_DE_OBRAS.md` › `## TK-60` |
| TK-61 | **Implementar o rodapé de “candidato a fechamento” (`DB-4`).** A norma está publicada na `## 3` do `P-0739` **sem implementação e sem teste**: a expressão não existe em `.claude/tools/backlog.py`, e o rodapé de `next` imprime só `inbox de planos`, `fila de memória` e `blocked`. Efeito hoje: pai cujos filhos ficaram todos terminais deveria aparecer no rodapé, e nada o mostra. | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-61` |
| TK-62 | **A gramática de ID de `rdo.py` não reconhece subtarefa de tíquete.** `_ID_HEADER_RE` e `_HEADER_BRACKET_RE` exigem `T` seguido de dígitos; `TK-<n><letra>` nunca casa. Bloqueia o dossiê de evidência e o `rdo.py close` de **toda** subtarefa de tíquete. A `DB-17` justificou a forma com *“já leem essa forma”* — cláusula falsa, nunca verificada. | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-62` |
| TK-63 | **O mundo hostil dos testes de executável é herdado do host, não construído.** Os dois sítios que discriminam hoje o fazem por acidente de plataforma: o mundo “sem `PYTHONUTF8`” só é hostil porque este host é Windows-cp1252. Medido: `PYTHONIOENCODING` prevalece sobre `PYTHONUTF8`, e é ele que constrói o mundo hostil portátil. | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-63` |
| TK-64 | **O `check-drift` está vermelho por linha de skill que nenhuma tarefa aberta possui.** `.claude/README.md` não tem a linha da skill `entrega-de-encerramento`, entrega do `TK-51a` (fechado). O vermelho chega sem dono a toda revisão desta janela e já obrigou três reconciliações manuais. | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-64` |
| TK-65 | **Três defeitos medidos de `backlog.py` na abertura da janela do `P-0741`.** O `check` aprova plano estruturalmente inselecionável (`Depende de:` com id que não é item); o `--help` e todo erro de argparse morrem com `UnicodeEncodeError` em console cp1252; o verbo `diretiva` descarta em silêncio os ids escritos depois do travessão. | done 5/5 | `docs/DIARIO_DE_OBRAS.md` › `## TK-65` |
| TK-66 | **O atribuidor de `review_evidence.py` fabrica autoria com tarefa nunca despachada.** `--atribuir` casa caminho contra os `Arquivos-alvo` de **qualquer** tarefa do plano sem olhar o `status` dela: na janela do `P-0743` rotulou quatorze arquivos como `alvo-de-outra-tarefa (DOM-T3/T4/T5)` — tarefas em `ready`, que nada produziram —, quando eram entrega de uma janela paralela. No regime de commit por marco, é a atribuição que separa uma entrega da outra, e as duas revisões da janela tiveram de desmentir a evidência mecânica por injeção manual. | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-66` |
| TK-67 | **A rodada de revisão de guardrails está pendente desde 2026-08-08.** `GOVERNANCA.md` §7.1 pendura a revisão no fechamento de cada plano; a última rodada registrada é a do `P-0731` (2026-08-08) e **sete** planos fecharam `done` depois dela (`P-0732`, `P-0735`, `P-0736`, `P-0738`, `P-0739`, `P-0740`, `P-0743`). §7 passou de 14 guardrails naquela rodada para **20** hoje. A skill `checar-versao-kit` reportou a pendência ao criar o `P-0745` em 2026-09-21; ela não executa a revisão — a revisão é tarefa nomeada, e é este tíquete. | cancelled | `docs/DIARIO_DE_OBRAS.md` § `## TK-67` |
| TK-68 | **A cópia do kit das regras globais divergiu do arquivo que o dono carrega.** `.claude/global/CLAUDE.md` não tem os **Controles 1.1 e 1.2** da Regra 1 (28 linhas) que o `CLAUDE.md` global do dono carrega desde 2026-09-04, e `.claude/sync-kit.ps1` não projeta `.claude/global/` — as duas cópias se mantêm à mão e nada afere a diferença. Medido em 2026-09-21 na abertura do `P-0745`. | done 1/1 | `docs/DIARIO_DE_OBRAS.md` § `## TK-68` |
| TK-69 | **O lastro obrigatório do modelo conceitual, e o modelo como contrato bilateral.** Ato do dono em 2026-09-21, na validação **prática** do `P-0741`: todo objeto, operação e propriedade do modelo tem de ter lastro direto no enunciado do problema e no prompt de origem; elemento sem lastro é requisito secundário, executável mas **fora do modelo**, e de responsabilidade inteira do agente. Segunda doutrina no mesmo ato: o modelo só vigora validado pelo cliente/gerente — *"contrato onde só um dos atores estabelece as condições não é contrato, é imposição"* —, o que torna a autoria do modelo **etapa assistida** e abre exceção declarada ao loop desassistido. Seis classes de defeito tipificadas sobre o modelo do `P-0745` (exemplos, não avaliação exaustiva), mais a leitura correta do enunciado dele e o defeito de gate do Marco 1. | cancelled | `docs/DIARIO_DE_OBRAS.md` › `## TK-69` |
| TK-70 | **A vigência bilateral do modelo e a conduta de drift do loop.** Recorte do `P-0746` na versão 3 do modelo dele: ao aceitar o modelo, o dono apontou que a restrição de atualização *"foge um pouco do escopo de lastro"* — o trecho do enunciado que a sustentava é conversação, não pedido de trabalho — e que o conteúdo *"já deve estar abrangido por outra ferramenta"*. Dois pacotes, com os dossiês da ex-`LST-T2` e da ex-`LST-T4` preservados inteiros: a vigência bilateral do modelo em `GOVERNANCA.md` §3.2 (mais a correção do `TK-69` §2 pela `DLS-3`), e a conduta de drift do loop na skill `scrum-master` e em `GOVERNANCA.md` §4.5. **Antes de executar, confirmar a suposição do dono** — a medição de 2026-09-21 diz que nenhuma das duas está coberta hoje (`drift`: 0 ocorrências na skill; `só vigora`: 0 em `GOVERNANCA.md`); pacote já coberto fecha por obsolescência. | cancelled | `docs/DIARIO_DE_OBRAS.md` › `## TK-70` |
| TK-71 | **A `V2` e a tarefa que não materializa operação.** Recorte do `P-0746` em 2026-09-22 (`AE-15`, `DLS-18`): a `V2` do `check` acusa toda tarefa sem o campo `Operação do modelo`, e o modelo daquele plano pedia que ela reconhecesse a tarefa que **declara** não materializar operação por ser requisito não fundamental — mas a forma textual dessa declaração nunca foi publicada (`requisito não fundamental`: **0** ocorrências na skill `diario-de-obras` e **0** em `GOVERNANCA.md`, medido em 2026-09-22), e o enunciado do `P-0746` não a pede: ele fala de **elemento** sem lastro, que já reside na seção nomeada do plano. Dois pacotes, nesta ordem: **(1)** decidir se a categoria existe — uma tarefa pode entregar requisito secundário sem materializar operação? hoje nenhum plano vivo tem o caso, e a `LST-T0` que o teria foi dissolvida (`DLS-10`); pacote sem caso fecha por obsolescência; **(2)** se existir, publicar a forma do campo na gramática e só então ensinar a `V2` a reconhecê-la — gramática antes do parser, nunca o contrário (`F-17` do `P-0746`). | cancelled | `docs/DIARIO_DE_OBRAS.md` › `## TK-71` |
| TK-72 | **A régua de autoria de card do kit.** Quatro achados medidos da janela do `P-0746`, todos sobre como se escreve um card para executor frio: aceite de card de `redacao` é recorte de literal e não contagem de palavra (`DLS-14` — a linha da `LST-T1` sairia verde com três menções decorativas); card que recebe rota de achado declara-a no próprio dossiê (`AE-11` — a `LST-T8` herdou rota que o card dela punha fora de escopo); `Arquivos-alvo` fecha o efeito colateral obrigatório (`AE-19` — reautorar o modelo obrigava a reescrever o campo de operação dos sete cards); e verificação sem valor esperado não é verificação (`AE-20`, família do `DM-12`). Residência: `GOVERNANCA.md` §3 e a gramática do card na skill `diario-de-obras`. | cancelled | `docs/DIARIO_DE_OBRAS.md` › `## TK-72` |
| TK-73 | **A oração da operação: recorte e sujeito.** A `OP-5` do `P-0746` tinha três orações com lastros diferentes, e as duas defeituosas só apareceram na implementação, a dois executores frios e cinco escalonamentos do Marco 1. Pacote 1: operação com mais de uma oração é operação mal recortada. Pacote 2, **bloqueado na decisão do dono** (`AE-18`): o critério de *ator inédito na operação*, que ele tipificou como integralmente mecânico, acusa 6 dos 7 atores do `P-0743` que ele aceitou, 4 dos 4 do `P-0746` e 5 dos 5 do `P-0745` reautorado — reprova o acervo inteiro ao pé da letra. | cancelled | `docs/DIARIO_DE_OBRAS.md` › `## TK-73` |
| TK-74 | **`review_evidence.py` não expande alvo terminado em barra.** `tests/fixtures/modelo/`, prescrito no reparo da `LST-T5`, chegou ao revisor da tarefa seguinte como falso `sem-atribuicao` para **10** fixtures; o revisor reconciliou à mão. Decide se o alvo de diretório se expande no instrumento ou se a gramática do card passa a exigir enumeração. Origem: `AE-22` do `P-0746`, por `I-4`. | done 2/2 | `docs/DIARIO_DE_OBRAS.md` › `## TK-74` |
| TK-76 | **As tabelas do modelo se escrevem para o dono.** Ato do dono de 2026-09-23 ao ler o modelo do `P-0747`: as três tabelas do modelo conceitual (objetos, operações, estados) passam a ser escritas *human-friendly*, em frases curtas e ilustrativas do conteúdo real — a coluna de contrato do `P-0747` ficou cheia de indireções difíceis de compreender —, e a especificidade que o executor precisa vai para as seções *machine-friendly* do plano. Vale para os próximos atos do modelador; o `P-0747` não se toca. Um card, `TK-76a`. | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-76` |
| TK-77 | **`kit_check` não recusa frontmatter de agente que não é YAML válido.** Medido no `P-0747` (`AE-20` iii): uma `description` com `: ` sem aspas quebrou o YAML de `.claude/agents/pantonic-consultant.md`, e o `validate` e o check-drift saíram `0`; o harness pode deixar de carregar o agente. O corretivo `CON-T8a` reparou o arquivo; a guarda segue sem pegar a classe. | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-77` |
| TK-78 | **As pendências da janela de 2026-09-24 do `P-0748`, antes de voltar a ele.** Ordem do dono: o loop deixa de parar para rebaixar o modelo — só para para subir a um melhor (`TK-78a`), a régua do card aprende rótulo, contingência de permissão e verificação por delta (`TK-78b`), e o gerador de evidência mede só o que mudou desde o despacho (`TK-78c`). | done 4/4 | `docs/DIARIO_DE_OBRAS.md` › `## TK-78` |
| TK-79 | **O executor devolve a linha de retorno seguida de prosa.** Medido em três despachos seguidos do `P-0748` (`TLG-T5`, `TLG-T3e`, `TLG-T3f`), o último com a proibição escrita no próprio despacho. A `A2` da `scrum-master` tipifica prosa **no lugar** da linha, não prosa **depois** dela; o loop e o gancho do painel leem só a primeira linha, e o resto se perde calado. | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-79` |
| TK-80 | **A régua de autoria do card: valor de aceite não viaja em `pendencia=`, e o rótulo do card de investigação que o parser não conhece.** Duas lições do `P-0748` sem residência: o `AE-13` (a Verificação 5 da `TLG-T4a` mandou colar valor medido na linha de retorno, e o `B1` escalou uma pendência que não existia) e o `AE-1` (o `pantonic-planner` manda o card de investigação trocar *Pronto quando* por um rótulo que o `rdo.py` recusa). O `TK-78`, destino previsto, fechou sem elas. | cancelled | `docs/DIARIO_DE_OBRAS.md` › `## TK-80` |
| TK-81 | **Propagar o painel do gerente aos cinco kits derivados.** O `P-0748` alterou só o hub (`DTG-8`): o gancho `.claude/tools/progresso_hook.py`, a declaração dele em `.claude/projecoes.json`/`settings.json`, a seção *Repertório de mensagens ao gerente* e o guardrail do painel na `scrum-master`, e o trecho do `README.md`. Nenhum derivado tem o gancho. | cancelled | `docs/DIARIO_DE_OBRAS.md` › `## TK-81` |
| TK-82 | **`rdo.py` imprime em cp1252 no pipe do Windows.** O `--help` de `rdo.py` (e toda saída dele) sai com `Diret\xf3rio`/`t\xedquete` quando redirecionado, porque o `rdo.py` não reconfigura `stdout` para UTF-8 como o `review_evidence.py` já faz. Achado do laudo da `SAN-T3a` do `P-0749`. | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-82` |
| TK-83 | **O tíquete nasce executável.** Ato do dono de 2026-09-25: problema identificado entra no fluxo já como trabalho, e só fica fora da fila por bloqueio real. A doutrina foi publicada na sessão; o card fecha a guarda no `backlog.py check`. | cancelled | `docs/DIARIO_DE_OBRAS.md` › `## TK-83` |
| TK-84 | **`review_evidence.py --desde` lista não rastreado anterior ao despacho.** Na evidência da `EBK-T5` do `P-0751`, 19 arquivos não rastreados anteriores ao commit do despacho saíram como "sem atribuição" e o reviewer os reconciliou à mão pela data de modificação. | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-84` |
| TK-85 | **O `rdo.py laudo` não tem onde pôr o motivo da dimensão, e recusa o alvo `dossiê`.** Achado do laudo da `EBK-T5` do `P-0751`: o motivo de dimensão fora de `conforme` foi parar no card de lições. | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-85` |
| TK-86 | **O piso do `C-11` mora no código do `backlog.py` e acusa `C-17` em todo outro repositório.** O subcomando `check` liga a constante do piso deste repositório para qualquer `--repo`: uma cópia sem alteração da fixture `verde` sai `C-17`, e o mesmo esperaria cada derivado depois da publicação do kit. Achado do fechamento do `P-0751` (`AE-6`). | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-86` |
| TK-87 | **O dossiê do último card de um plano leva as seções seguintes do plano.** O `backlog.py show`/`next` do `EBK-T14` imprimiu as seções `## 6`..`## 8` do `P-0751` como parte do card: o item só termina no próximo cabeçalho de item. Achado do fechamento do `P-0751` (`AE-6`). | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-87` |
| TK-88 | **O encerramento de tarefa e de plano era uma sequência de comandos e prosa à mão.** Fechar uma tarefa eram quatro comandos em turnos separados, com o pacote do laudo redigitado; fechar um plano era inteiramente manual, porque o instrumento recusava `ready → done` para plano (diário, 2026-09-25). Pedido do dono em 2026-09-26: tornar mecânicos os dois fechamentos, com relatório em três seções (humana, máquina, histórico), e um verbo `handover` que registra no card o que a sucessora espera da tarefa. | done 4/4 | `docs/DIARIO_DE_OBRAS.md` › `## TK-88` |
| TK-89 | **O gate do card religado deixou atrás o leitor de alvos e a doutrina.** A `FPU-T2` do `P-0752` religou o `card_check` como gate de despacho; o laudo dela achou o `review_evidence.py` sem ler a entrada `caminho:linha — <literal>` de `Arquivos-alvo` (3 de 4 alvos fora), o `scrum-master` com "sete itens" e o `B3` sem o `card_check`, e a rubrica `### 8.1` com a comparação de literal antiga (`AE-38`, `AE-40`, `AE-41` do plano). | done 2/2 | `docs/DIARIO_DE_OBRAS.md` › `## TK-89` |
| TK-90 | **O `P-0742` está fora do índice do diário, `blocked` com a condição já satisfeita.** Achado na varredura do gate do card pelo consultor do `P-0752`: o plano "O loop sai do LLM" nunca entrou no índice (o caso do `TK-59`), espera o `P-0739`, que já fechou, e os oito cards dele não passam no gate. Registro no índice pelo `TK-90a`; o dono decidiu *"Retomar"* (2026-09-26), e o `TK-90b` é a rodada de replanejamento `RP-1` do plano. | done 2/2 | `docs/DIARIO_DE_OBRAS.md` › `## TK-90` |
| TK-91 | **O modelador não tem o ato que promove ou elimina a versão pendente no marco.** Achado pelo consultor do `P-0752` ao validar a versão 2 do modelo: a `GOVERNANCA.md` §3.2 diz o desfecho do marco e dá ao modelador todo ato sobre o modelo, e o arquivo do agente só diz, na emenda, que a `## 1` vigente não se toca. Correção no `TK-91a`. | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-91` |
| TK-92 | **A medida do executor de card de tíquete grava onde o `review_evidence.py` não procura.** A doutrina fixa o nome do arquivo de medida pelo id do plano, que card de tíquete do diário não tem: o executor do `TK-86a` gravou com o id `P-0751`, e a evidência deu a medida como ausente. O destino passa a ser uma função só, usada pelos dois instrumentos (`AE-77`). | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-92` |
| TK-93 | **A evidência não mostra o que mudou em arquivo não rastreado, e o redespacho perde a primeira execução.** O `<ref>` do despacho vem de `git stash create`, que ignora não rastreado: a evidência do `TK-86a` trouxe `encerrar.py` inteiro, truncado antes da linha editada, e o `<ref>` recapturado no redespacho deixou fora a primeira execução (`AE-78`). | done 1/1 | `docs/DIARIO_DE_OBRAS.md` › `## TK-93` |
| P-0743-DOM | O modelo conceitual vira modelo de domínio — **aceito pelo dono em 2026-09-21**. As 18 tarefas fecharam aprovadas; a norma, a gramática, o instrumento `modelo.py` e o agente `pantonic-model-designer` publicam o modelo de domínio em objetos com propriedades, fluxo de operações, estado inicial × estado final e registro de versões, e o próprio plano é o primeiro do acervo escrito na forma nova. O Marco 3 foi **dispensado** por ato do dono, que moveu a validação para o as-is. **Entrega validada: `docs/Entregas Aceitas/Entregas - P-0743.md`** (875 linhas, cobre também o `P-0741`), onde vivem as oito pendências abertas — três com efeito fora deste plano (`AE-25` telemetria, `TK-66` atribuição de evidência, `AE-24` residência de prova). Vinte e cinco achados (`AE-1`..`AE-25`), dez escalonamentos ao consultor, uma rodada de replanejamento (`RP-1`). Nada commitado. | done 18/18 | docs/plans/P-0743-modelo-de-dominio.md |
| P-0744-PLS | A especificação do agente de planejamento — substituído por: `P-0745` (2026-09-21, `DPN-1`) | superseded | docs/plans/P-0744-spec-do-planejador.md |
| P-0745-PLN | O planejador diante do modelo: uma operação, um card | done 10/10 | docs/plans/P-0745-planejador-modelo-operacao.md |
| P-0746-LST | **O lastro do modelo: o contrato se escreve do enunciado.** Institui o lastro obrigatório (todo objeto, operação e propriedade derivado do enunciado e do prompt de origem; elemento sem lastro vira requisito secundário, fora do contrato e de responsabilidade inteira do agente), a vigência bilateral do modelo, as duas vias de leitura do enunciado (estado × operação) e a conduta de drift do loop (carrega até o marco; o marco adjudica; recusa retroage as tarefas). 7 tarefas (`LST-T1`, `LST-T7`, `LST-T3`, `LST-T8`, `LST-T9`, `LST-T5`, `LST-T6`), `DLS-1..DLS-15`, 3 marcos. A `LST-T6` reaplica o conceito ao modelo do `P-0745` para nova medição do dono. **Modelo na versão 3** (2026-09-21), depois de duas rodadas de Marco 1: a versão 1 foi reprovada — quatro propriedades escritas como objetos — e reautorada sob a leitura do dono (um objeto, as restrições; tudo o mais é propriedade dele); a versão 2 foi aceita com uma correção — a restrição de atualização não tem lastro e saiu do modelo (`DLS-11`), levando a `LST-T2` e a `LST-T4` para o `TK-70`. Efeitos medidos: `modelo.py check` sobre o plano saiu de `1` para `0` **sem tocar o instrumento** (a `V9` era sintoma de modelo mal decomposto, não defeito da gramática), a `LST-T0` foi dissolvida (`DLS-10`) e a exceção de gate da `DLS-8` revogada; a `LST-T7` nasceu para a restrição de decomposição. **Marco 1 fechado em 2026-09-21** com o `go` do dono sobre a versão 3: o modelo vigora e o plano está publicado. Execução em janela própria, por decisão do dono. Origem: `TK-69`. **Aceito pelo dono em 2026-09-24** (Marcos 2 e 3): modelo na versão 4 vigente; documento de validação `docs/OPERACOES_AS_IS_P-0746.md`; `AE-18` segue no `TK-73` Pacote 2. | done 7/7 | docs/plans/P-0746-lastro-do-modelo.md |
| P-0747-CON | O consultor de plano: a figura, a triagem de toda parada e a fronteira com o planejador | done 19/19 | docs/plans/P-0747-consultor-de-plano.md |
| P-0748-TLG | A tela do gerente: o fluxo da execução em linguagem humana | done 17/17 | docs/plans/P-0748-tela-do-gerente.md |
| P-0749-SAN | Saneamento de artefatos: pasta por plano, máquina em TSV, humano mínimo | done 10/10 | docs/plans/P-0749-saneamento-artefatos.md |
| P-0750-CAH | Comunicação agente↔humano: a mensagem ao dono se entende sozinha | done 6/6 | docs/plans/P-0750-comunicacao-agente-humano.md |
| P-0751-EBK | Esgotar o backlog antes da publicação do kit | done 16/16 | docs/plans/P-0751-esgotar-backlog.md |
| P-0752-FPU | Fato no ponto de uso: os mecanismos contra o esquecimento e a assunção | done 17/17 | docs/plans/P-0752-fato-no-ponto-de-uso.md |
| P-0742-LF | O loop sai do LLM | cancelled | docs/plans/P-0742-loop-fora-do-llm.md |
| P-0753-AF | Auditoria de encerramento do estágio 1: as dezoito recomendações e os dois tíquetes do consultor | done 21/21 | docs/plans/P-0753-auditoria-estagio-1/plano.md |
| P-0754-AUF | Auditoria final do kit: os herdados e o relatório de auditoria nova | ready 16/16 | docs/plans/P-0754-auditoria-final/plano.md |
| P-0755-RAF | Aplicação das recomendações da auditoria final do kit | ready 64/64 | docs/plans/P-0755-recomendacoes-auditoria-final/plano.md |

---

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

- **Status:** `cancelled` · 2026-09-25

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
- **Notas de execução:**
  - 2026-09-25 `cancelled` — absorvido pelo P-0750 (comunicação agente↔humano)

## TK-48 — `~/.claude/settings.json` **perdeu a chave `hooks` inteira silenciosamente**

- **Status:** `cancelled` · 2026-09-24

`~/.claude/settings.json` **perdeu a chave `hooks` inteira silenciosamente**, sem ação intencional do dono, entre a `RPC-T4` e a escolha da `RPC-T5` — os 4 hooks registrados (premissa da `T5`) somem sem rastro. Causa não investigada por decisão do dono (foco em proteção, não em achar culpado); a `T5` não depende do estado atual do arquivo (reconstrói o registro pela tabela já transcrita no dossiê) e segue delegável. Vulnerabilidade a considerar: `settings.json` global pode perder chave inteira sem sinal

*(Âncora original do índice, preservada:* `docs/plans/P-0735-residencia-e-ponto-de-carga.md` seção "Achados da execução" (2026-08-17) *)*

- 2026-09-19 — *(**dono mandou resolver em 2026-09-19**. Estado medido no mesmo dia: a chave `hooks` **existe** — global com `PreToolUse` e `UserPromptSubmit`, projeto com `PreToolUse` e `SubagentStop` —, portanto **não há perda ativa a reparar**; o que falta é a **proteção**, que era o foco declarado do dono desde a abertura (proteger, não achar culpado). Não entra no `P-0740` por `DM-30` — cruza o tema; entra na fila logo depois do marco)*

---
- **Notas de execução:**
  - 2026-09-24 `cancelled` — caducou (revisão de pertinência de 2026-09-24): a proteção pedida existe — o alvo usuario de .claude/projecoes.json declara as chaves hooks do settings.json global, e python .claude/tools/materializar.py drift --alvo usuario acusa a entrada ausente ou divergente (apply a restaura). Disparo automático do drift é a classe do TK-55

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
registrada em `docs/DIARIO_HISTORICO.md` › `## P-0737` (nova razão do `blocked`) e no tíquete novo `TK-53` (investigação do que
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

**Bloqueia:** `P-0737` (ver seção `docs/DIARIO_HISTORICO.md` › `## P-0737` — a premissa de custo fixo de abrir janela que o loop
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

- **Status:** `cancelled` · 2026-09-21 · obsoleto por decisão do dono, 2026-09-21

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

**Bloqueia:** `P-0737` (razão vigente na seção `docs/DIARIO_HISTORICO.md` › `## P-0737`).

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
- **Notas de execução:**
  - 2026-09-21 `cancelled` — ENCERRADO POR OBSOLESCÊNCIA, NÃO POR DESCARTE. As duas sub-tarefas entregaram e ficam done: o extrato (## 13 de docs/CUSTO_DO_PICKUP.md, ratificado pelo dono em 2026-09-19) e o descarte medido do candidato da bimodalidade (## 16, TK-54b aprovada com ressalva 92%). O que o cancelamento mata é só a pergunta residual da bimodalidade, rota (c) do AE-4. Razão do dono: tíquete exclusivo de custo, e custo deixou de ser critério (DM-30 do P-0740, 2026-09-19); o foco passou a ser incrementar o framework. O estado é cancelled e não done porque de ready a tabela de transições de §2.7 só admite cancelled; não houve review do tíquete como um todo. Reabre por tíquete novo, e só pela rota (a), instrumento fora de banda, se o custo voltar a ser critério.

### TK-54a — O extrato [Sonnet · classe investigacao]

- **Status:** `done` · 2026-09-18 — executada inline pela orquestração em 2026-09-18; `## 13` publicada em `docs/CUSTO_DO_PICKUP.md:404-431`

Reaberta no mesmo dia pela rodada `RP-TK54-1`, rota **A**. A coluna de
classificação vem **fixada neste card**: o executor **transcreve** o valor e a justificativa da
tabela `B` abaixo, não avalia e não propõe classificação própria.

- **Objetivo:** publicar a seção `## 13` de `docs/CUSTO_DO_PICKUP.md` — uma linha por fonte
  carregada, com `chars` medidos, estrato, regime, participação nos três regimes de `usage_1` e a
  classificação já fixada — e registrar a seção em `docs/DOC_MAP.md`. **Não corta nada e não propõe
  rota de corte.**
- **Fundamento:** decisões 1..7 de `## TK-54` (copiadas inline no que vinculam), a
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

- **Status:** `done` · 2026-09-21
- **Objetivo:** identificar **qual fonte liga e desliga** entre os dois regimes que a `## 12` mediu
  — `cache_read` exatamente 18.084 vs 26.695 (Δ **8.611 tok**), `cache_creation` ~16,5k vs ~19,4k,
  **preâmbulo visível idêntico** (~11.684 chars) nos dois.
- **Candidato nomeado, a confirmar ou descartar por sonda (não por argumento):** o mecanismo de
  *deferred tools* — em algumas janelas um conjunto de ferramentas chega só como nome, em outras
  com o schema completo, e a ordem de grandeza bate. Descartado o candidato, publica-se o que foi
  descartado e como.
- **Arquivos-alvo:** `docs/CUSTO_DO_PICKUP.md` (a seção nova, ao fim do portador),
  `docs/DOC_MAP.md` (contagem de linhas do portador + bullet da seção nova) e
  `docs/DIARIO_DE_OBRAS.md` (este card: `Status` e bullet de fechamento). A sonda é de scratchpad,
  descartável e **fora do repo** — decisão 4 de `## TK-54`, não mexer no que se mede.
- **Verificação:** `Select-String -Path docs\CUSTO_DO_PICKUP.md -Pattern '^## 16 ' -List` imprime
  uma linha (a seção começa em 520) · `(Get-Content docs\CUSTO_DO_PICKUP.md).Count` imprime 631,
  igual à contagem que o `DOC_MAP` publica para o portador ·
  `Select-String -Path docs\CUSTO_DO_PICKUP.md -Pattern 'As quatro can','Veredito: não identificada'`
  imprime duas linhas (527, o gate das quatro canônicas da `## 12`; 620, o veredito) ·
  `Select-String -Path docs\DOC_MAP.md -Pattern '^## docs/CUSTO_DO_PICKUP.md','## 16 A fonte'`
  imprime duas linhas (104 e 137). Os quatro rodam a partir de `D:\workspaces\PantonicApp` e
  foram medidos nesta forma em 2026-09-21.
- **Pronto quando:** a seção do `docs/CUSTO_DO_PICKUP.md` nomeia a fonte com evidência, ou publica
  `não identificada` com a lista do que foi descartado e por quê; e `docs/DOC_MAP.md` registra a
  seção com a contagem de linhas do portador atualizada.
- **Reparo de forma (2026-09-21, `AE-3`):** o card nasceu em 2026-08-31, antes do `rdo.py` atual, e
  não declarava `Verificação`, `Pronto quando` nem `Arquivos-alvo` — o gerador de evidência recusava
  a tarefa **depois** de ela estar entregue. Os três campos acima são **transcrição** do que foi
  despachado e medido, não escopo novo: `Pronto quando` é o texto literal do antigo *Critério de
  pronto*, com o número da seção substituído por *a seção do portador* — `## 14` e `## 15` foram
  ocupadas em 2026-09-20 por outra frente, depois de este card ser escrito, e a entrega saiu na
  `## 16`; o portador é único (`DX-3`), então a identidade do entregável não mudou.
- **Fecha apontando para:** `## 16` publicada em `docs/CUSTO_DO_PICKUP.md:520-631`.

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

- **`AE-3` (2026-09-21) — card anterior ao `rdo.py` atual é um `B3` silencioso: o defeito de forma
  só aparece depois do despacho, com a entrega já feita.** Fato medido nesta execução, com a
  `TK-54b` já em `review`:
  `python .claude/tools/review_evidence.py --plano docs/DIARIO_DE_OBRAS.md --tarefa TK-54b --desde d75e7a6 --out ...`
  → `review_evidence: FALHOU - campo obrigatório ausente em 'TK-54b': 'verificacao'` (exit 1). Causa
  em `.claude/tools/rdo.py:309-320`: todo dossiê exige `objetivo`, `verificacao` e `pronto-quando`,
  mais **exatamente um** entre `arquivos-alvo` e `entregavel`; e `_CAMPO_RE` (`rdo.py:97`) só
  reconhece campo em **bullet de topo** (`- **Rótulo:**`). O card foi escrito em 2026-08-31, antes
  desses instrumentos, e trazia `Critério de pronto` — rótulo que o parser não mapeia — sem
  `Verificação` e sem `Arquivos-alvo`. Como `rdo.py close` usa o mesmo parser, o defeito trava
  **julgamento e arquivamento** da mesma entrega.
  - **O defeito é de classe, não deste card.** `extrair_dossie` sobre a irmã `TK-54a` falha com a
    **mesma** mensagem, e por motivo pior: ela **tem** `Verificação` e `Pronto quando`, mas como
    **parágrafo em negrito** (`docs/DIARIO_DE_OBRAS.md:1546,1556`), não como bullet — o parser não
    os enxerga, e falta-lhe também `Arquivos-alvo`. Escapou só porque foi executada inline pela
    orquestração, sem passar pelo gerador. Todo card do acervo anterior ao `rdo.py` atual está
    nessa condição.
  - **Efeito de segunda ordem, medido na leitura do código.**
    `review_evidence.mapear_alvos_de_outras_tarefas` engole `RdoValidationError` e **pula** o card
    defeituoso: um card mal-formado desaparece em silêncio do balde *alvo de outra tarefa* da
    `confrontar_escopo`, e a atribuição de escopo de toda tarefa irmã degrada sem aviso. Nesta
    execução o efeito foi **nulo** — os alvos da `TK-54a` são os mesmos da `TK-54b`, cobertos com
    precedência maior pelos alvos do próprio card.
  - **Por que os gates do passo 3 não pegaram.** `G-PLANREADY`, o gate de delegação e
    `modelo.py check` **não exercitam o parser de dossiê**; nenhum deles lê os campos obrigatórios.
    O `B3` era detectável antes do despacho por um único comando — `extrair_dossie` sobre o card —
    que o loop não roda em lugar nenhum.
  - **Consequência para o kit (insumo do planejador, não ato desta rodada).** Duas matérias, nesta
    ordem: (i) **gate ausente** — falta rodar `extrair_dossie` no card **antes** do despacho, seja
    dentro do `G-PLANREADY`, seja como subcomando `rdo.py check <tarefa>`; (ii) **gramática do
    acervo** — decidir se o parser aprende o rótulo em parágrafo negrito e o alias
    `Critério de pronto` → `pronto-quando`, ou se o acervo antigo é migrado; alargar a gramática é
    ato de plano, não de rodada de desbloqueio.
  - **Rota escolhida (A) e o que ela editou.** Card `TK-54b` reparado **no lugar**, por
    transcrição do que foi despachado e medido: `Arquivos-alvo` (os três arquivos que a entrega
    tocou), `Verificação` (quatro comandos rodados em 2026-09-21, saídas conferidas) e
    `Pronto quando` (texto literal do antigo *Critério de pronto*). Reparo de **forma**, declarado
    como tal no próprio card. **`TK-54a` foi deixada como está**: é `done`, não volta a passar pelo
    gerador e o efeito vivo do seu defeito foi medido como nulo — reescrever campo de card aceito
    seria retro-justificação sem contrapartida. Classificação da mudança: **técnica/tática**; nada
    escalado ao dono.

- **`AE-4` (2026-09-21) — a pergunta da `TK-54` é não observável pelo instrumento que a `TK-54`
  usa; decisão de rota pendente, classificada ESTRATÉGICA e escalada ao dono.** Fato medido duas
  vezes, de forma independente: a entrega da `TK-54b` (`## 16`, `docs/CUSTO_DO_PICKUP.md:520-631`)
  descartou o candidato *deferred tools* por identidade byte-a-byte no par 18.084/26.695, e a
  revisão reproduziu de fora, por **enumeração exaustiva de chaves sobre 299 transcripts de raiz**,
  que **nenhuma versão do formato loga `system` nem `tools` do request**. Continuar sondando
  transcript não pode responder à pergunta — não é falta de esforço, é ausência de referente no
  corpus. **Três rotas, e o que cada uma implica:** (a) **instrumentar fora de banda** (proxy/OTEL
  sobre o request real) — é a única que observa o objeto, custa instrumento novo, fora do que
  qualquer tarefa desta fila financia, e mexe no que se mede (tensiona a decisão 4 de `## TK-54`);
  (b) **experimento pareado controlado** — mais barato, mas só mede *correlação* entre configuração
  e `cache_read`, nunca o conteúdo do `system`/`tools`, então responde "o que alterna" e não "do que
  é feito"; (c) **encerrar a pergunta como não observável** e fechar o `TK-54` com o extrato que já
  tem, mais esta linha de base. **`registrar e não agir` é a forma mínima de (c)** e é a
  **recomendação**, pelo motivo medido: o gatilho que dava urgência à pergunta caiu — `DM-30` do
  `P-0740` tirou o custo do posto de critério (dono, 2026-09-19), e a condição de destravamento do
  `P-0737` escrita na sua própria seção (*"até a `TK-54` publicar o extrato do custo e o dono
  ratificar a classificação"*) está **satisfeita** desde 2026-09-19 — a bimodalidade **não** é
  condição de liberação. **O que fica bloqueado sem resposta: nada nesta fila.** O que se perde em
  (c) é a explicação de um Δ de 8.611 tok que hoje não decide nada; se o custo voltar a ser
  critério, a pergunta reabre por tíquete novo, com (a) como única rota que a responde.
  - **Rota do achado de processo (i) do laudo — `sem ação` na `## 16`.** O reviewer apontou que o
    achado de método sai em prosa, sem rota e sem dizer o que *seria* preciso. A lacuna é real e
    está preenchida **aqui**, não lá: a seção é entrega **aceita** de tarefa `done`, e o que falta
    é decisão de rota, que não mora no portador de medição. Residência única do que seria preciso:
    este `AE-4`.
  - **DECISÃO DO DONO (2026-09-21) — rota (c), `registrar e não agir`.** Literal: *"Se for a
    questão de custo, essa já está vencida a algumas sprints. No momento, o foco é em incrementar o
    framework. Se o plano for exclusivo de custo, pode encerrá-lo por ser obsoleto."* O `TK-54` é
    exclusivo de custo, então **fecha `done` por obsolescência do que restava**, não por
    esgotamento da pergunta: as duas sub-tarefas entregaram (2/2) e o extrato foi ratificado em
    2026-09-19; o que morre aqui é só a pergunta da bimodalidade. Reabertura, se o custo voltar a
    ser critério, é por **tíquete novo** e só pela rota (a) — nenhuma outra observa o objeto.

- **`AE-5` (2026-09-21) — `B0` do laudo: a `pendencia=` do executor era da orquestração, não da
  entrega.** A linha de retorno da `TK-54b` apontava `docs/plans/_INBOX.md`,
  `docs/plans/_INBOX_HISTORICO.md` e `docs/telemetria.tsv` como tocados fora dos `Arquivos-alvo`.
  Atribuição medida e conferida: `_INBOX.md`/`_INBOX_HISTORICO.md` vêm da **drenagem do inbox** que
  o próprio `backlog.py check` executa (rodado pela orquestração antes do despacho) e
  `telemetria.tsv` da apensação de consumo no fechamento — **nenhum dos três foi tocado pelo
  executor**. Confirmado mecanicamente pelo gerador depois do reparo do `AE-3`: os três caem no
  balde *registro da orquestração (não atribuível a tarefa)* e o veredito de escopo sai `conforme`
  (`docs/RDO/evidencia/TK-54-TK-54b.md`). Sem efeito sobre a entrega. **Consequência de classe,
  sem ação aqui:** um comando de **verificação** do loop (`backlog.py check`) tem efeito colateral
  de **escrita** versionada — quem confere não deveria escrever; insumo para a rodada que revisar
  os instrumentos do loop.

- **Rota do achado de processo (ii) do laudo — encaminhado ao `TK-55`, sem tíquete novo.** O
  reviewer reproduziu o método descrito pela `## 16` e obteve `cache_read=18.084` com **n=116**
  (corpus 299) contra os **n=120** publicados (corpus 303), sem regra de enumeração publicada que
  permita reconciliar. Não altera conclusão nenhuma — o veredito repousa na identidade byte-a-byte
  do blob, não no `n`. É exatamente a classe do `TK-55` (derivado publicado que nada confronta com
  a fonte), e abrir tíquete próprio fragmentaria o acumulador que o dono criou para isso.

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
na seção `docs/DIARIO_HISTORICO.md` › `## P-0737`); investigação do que mudou no corte aberta como `TK-53`, **já desenhada**
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

- **Status:** `cancelled` · 2026-09-25 — gated pelo encerramento do `P-0740` (ato do dono, 2026-09-19).
- **Casos do `P-0748` (2026-09-24), ponteiro:** `AE-4`, `AE-5` e `AE-11` de `docs/plans/P-0748-tela-do-gerente.md` `## 9` — o `review_evidence.py` com `--desde <ref>` lista como tocados os não rastreados que já existiam antes do despacho, e mostra alvo não rastreado como arquivo inteiro truncado, sem diff; recorreu em todos os laudos da janela (`TLG-T3b`..`TLG-T3h`, `TLG-T5`, `TLG-T5a`), sempre reconciliado à mão por mtime.

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

**Caso novo (2026-09-21, `TK-54b`) — o `n` publicado que nada reconcilia com o corpus.** A `## 16`
do `docs/CUSTO_DO_PICKUP.md` publica `cache_read=18.084` com `n=120` sobre 303 janelas; a revisão,
reproduzindo o método **descrito pela própria seção**, obteve `n=116` sobre 299. A seção não publica
a **regra de enumeração** do corpus (o que conta como janela principal, o que descarta), então a
diferença não é reconciliável de fora e nenhuma das duas contagens é verificável. Conclusão
intacta — o veredito repousa em identidade byte-a-byte, não no `n`. Mesma classe dos cinco acima:
derivado publicado sem confronto com a fonte. Encaminhado por rota do consultor (`AE-4`/`AE-5` de
`## TK-54`), sem tíquete próprio.

**Rodada de planejamento (2026-09-25), por ato do dono ao instituir *Tíquete nasce executável*.**
O acumulador deixa de acumular: cada caso acima foi re-medido e saiu com rota, e casos novos da
classe abrem tíquete próprio, já com card. O tíquete fecha quando os cards abaixo fecharem.

| caso | medido em 2026-09-25 | rota |
|---|---|---|
| comando de aceite que não discrimina (`AE-19`), aceite que conta a si mesmo, aceite inatingível (`AE-23`) | regra publicada: `pantonic-planner` Fase 4, itens 11 e 12 (v) | sem ação |
| número de aceite que nasce vencido (`AE-18`), número citado de outra data | regra publicada: `pantonic-planner` Fase 4, item 12 (iv) | sem ação; a extensão à premissa vai ao `TK-72a` |
| hook de telemetria inflado e sem disparo na retomada (`AE-3`) | primeira metade corrigida (`LM-T2b`); a segunda é conduta do loop, `scrum-master` passo 9 | sem ação |
| `check` casa toda tabela como índice (`AE-1`) | corrigido: `_parse_indice` lê só a tabela sob `## Índice` | sem ação |
| projeção do índice que não se regenera | corrigido: `backlog.py status` regenera a célula | sem ação |
| `check` varrendo planos fechados, `next` mudo com fila cheia, `status` apagando a fila, citação de seção sem resolução, contador de id | corrigidos no `P-0739` e no `TK-60a` (`C-10`, `C-11`) | sem ação |
| três entrypoints lendo `stdin` sem UTF-8 (`AE-36`) | corrigidos: `ocupacao.py:142`, `telemetria_hook.py:214`, `modelo_por_fase_userpromptsubmit.py:104` | sem ação |
| teste de executável que herda o ambiente (`ESC-10`, `DB-53` cláusula 3) | os testes usam `env=_ambiente_hostil()`; a regra corrigida não tem residência na doutrina | `TK-55g` |
| fixture com nome de descoberta do harness | 0 arquivos hoje sob `tests/fixtures/`; nada impede a volta | `TK-55f` |
| piso de `C-11` como esconderijo de defeito | `_PISO_C11` tem 2 entradas; nada acusa entrada que não casa ocorrência | `TK-55a` |
| `check` aprova card que o `rdo.py` recusa | persiste; caso novo no `TK-68a` — literal com `### ` na coluna 0 cortou o card para o `rdo.py`, e o `check` saiu OK | `TK-55a` |
| `rdo.py close` não confere o estado da tarefa | persiste: `rdo.py:14` declara que o `close` não lê `status` | `TK-55b` |
| ` + dono` descartado na projeção do `next` | persiste, e o esforço também cai: `backlog.py:1250` monta `[<modelo> · classe <classe>]` | `TK-55c` |
| relatório do `kit_check` que corrompe o console | acentuação corrigida (`É` e `—` chegam íntegros); a contagem ainda soma cabeçalho e detalhe: uma divergência de README com 2 linhas contou 3 problemas | `TK-55d` |
| menção vira uso; número que o instrumento calcula; premissa medida; o card fixa a propriedade | regra sem residência | `TK-72a` |
| asserção de magnitude; teste que lê estado vivo | regra sem residência | `TK-55g` |
| rótulo errado; efeito abaixo do ruído do controle; `n` sem regra de enumeração | regra sem residência | `TK-55g` |
| `review_evidence.py --desde` lista não rastreado anterior ao despacho | na evidência do `TK-68a`, 3 arquivos, todos com atribuição `alheio`, sem rebaixar a entrega (regra `B0`) | sem ação — ruído sem efeito no veredito |
- **Notas de execução:**
  - 2026-09-25 `cancelled` — absorvido pelo P-0751 — Esgotar o backlog antes da publicação do kit (DEB-2)

### TK-55a — O `check` confronta o card com o `rdo.py` e o piso com o corpus [Sonnet · esforço medium · classe implementacao]

- **Status:** `cancelled` · 2026-09-25
- **Objetivo:** `python .claude/tools/backlog.py check` passa a emitir `C-16` para toda tarefa de
  plano e toda subtarefa de tíquete com status `ready`, `in-progress` ou `review` que a leitura de
  dossiê do `rdo.py` recusa, com a mensagem dessa leitura no texto da violação; e `C-17` para toda
  entrada de `_PISO_C11` que não casa nenhuma ocorrência de citação quebrada no corpus corrente.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
  - `.claude/skills/diario-de-obras/SKILL.md`
- **Propriedades:**
  1. A leitura que decide `C-16` é a mesma que `rdo.py close` usa para o dossiê — um card que o
     `close` recusaria sai acusado, e um que ele aceita não sai. A gramática não é reimplementada
     no `backlog.py`.
  2. Card `done`, `cancelled` ou `blocked` não é lido para `C-16`.
  3. `C-17` nomeia a entrada órfã; entrada órfã no corpus vivo sai de `_PISO_C11` neste card.
  4. As menções `C-1..C-14` do módulo e da skill passam a `C-1..C-17`.
- **Texto atual 1** (`.claude/skills/diario-de-obras/SKILL.md`, uma ocorrência):

  ~~~~
  mesmo ato do card corretivo que ele já escreve.
  ~~~~

- **Texto novo 1** (sem quebra nova):

  ~~~~
  mesmo ato do card corretivo que ele já escreve. Card vivo que o `rdo.py` não lê é `C-16` no `backlog.py check`.
  ~~~~

- **Casos medidos que motivaram (2026-09-20 e 2026-09-25):** seis cards de tíquete sem
  `Arquivos-alvo`, `Verificação` e `Pronto quando` passaram no `check` e só falharam no
  `rdo.py close`; o `TK-68a` passou no `check` e o `review_evidence.py` recusou com `campo
  obrigatório ausente em 'TK-68a': 'verificacao'`, porque o literal do card tinha uma linha
  `### Controle 1.1 — …` na coluna 0.
- **Testes (novos, em `tests/test_backlog.py`):**
  - TF par sobre cópia da fixture `verde`: card `ready` íntegro → nenhum `C-16`; o mesmo card sem
    a linha `- **Verificação:**` → um `C-16` com o id; o mesmo card com uma linha `### X` na coluna
    0 antes da `Verificação` → um `C-16` com o id.
  - TF: o mesmo card defeituoso com status `done` → nenhum `C-16`.
  - TF par para `C-17`: piso com uma entrada que casa ocorrência da fixture → nenhum `C-17`;
    acrescida uma entrada que não casa nada → um `C-17` que a nomeia.
- **Verificação:**
  1. `python -m pytest tests/test_backlog.py -q` → verde, com os testes acima.
  2. `python .claude/tools/backlog.py check` na árvore → `check: OK — nenhuma violação.`
  3. `(Select-String -Path .claude/skills/diario-de-obras/SKILL.md -SimpleMatch 'Card vivo que o').Count` — antes `0`, depois `1`.
  4. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho mais os testes novos
     (referência medida na autoria: `360 passed`, 2026-09-25).
- **Pronto quando:** o `check` acusa card vivo que o `rdo.py` recusa e entrada de piso órfã, cada
  um com par em teste, e sai `OK` sobre a árvore.
- **Não fazer:** não mudar a gramática aceita pelo `rdo.py`; não corrigir card de plano fechado;
  não tocar `rdo.py`.
- **Contingências:**
  - se o Verificação 2 acusar `C-16` em card vivo da árvore → parar e sinalizar `blocked`
    razão `premissa`, colando as violações (o card acusado é defeito de autoria, de outro dono).
  - se `C-17` acusar entrada órfã no corpus vivo → remover a entrada de `_PISO_C11` e seguir
    (propriedade 3).
- **Notas de execução:**
  - 2026-09-25 `cancelled` — absorvido pelo P-0751 como EBK-T2 (DEB-2)

### TK-55b — `rdo.py close` recusa tarefa que não está `done` [Sonnet · esforço medium · classe implementacao]

- **Status:** `cancelled` · 2026-09-25
- **Objetivo:** `rdo.py close` sai com código diferente de `0`, sem escrever arquivo, quando o
  status corrente da tarefa não é `done` — lido na mesma fonte que o `backlog.py status` escreve:
  bullet `- **Status:**` no plano legado e no diário, linha da tarefa em `estado.tsv` no plano em
  pasta. A mensagem nomeia a tarefa, o status encontrado e o exigido.
- **Arquivos-alvo:**
  - `.claude/tools/rdo.py`
  - `tests/test_rdo.py`
  - fixtures sob `tests/fixtures/` usadas por testes de `close` — só a linha de status da tarefa
    fechada, e só quando o teste existente passar a falhar por causa desta regra
- **Caso medido que motivou (2026-09-20):** o `close` escreveu RDO para uma tarefa `in-progress`
  um comando depois de o `backlog.py status` ter recusado `in-progress → done`. Hoje `rdo.py:14`
  declara: *"`close` não tem `--status` e não lê `status` de lugar nenhum"*.
- **Testes:** TF par — tarefa `in-progress` → exit diferente de `0` e nenhum RDO no destino; a
  mesma tarefa `done` → exit `0` e o RDO escrito. Um par no plano legado e um no plano em pasta.
- **Verificação:**
  1. `python -m pytest tests/test_rdo.py -q` → verde, com os pares acima.
  2. `(Select-String -Path .claude/tools/rdo.py -SimpleMatch 'de lugar nenhum').Count` — antes `1`, depois `0`.
  3. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho mais os testes novos.
- **Pronto quando:** o `close` só escreve RDO de tarefa `done`, provado pelos dois pares, e a
  docstring do módulo diz que ele lê o status.
- **Não fazer:** não acrescentar flag `--status`; não mudar o pacote de campos do `close`; não
  tocar `backlog.py`.
- **Contingências:**
  - se um teste existente de `close` falhar porque a tarefa da fixture não está `done` → mudar
    só a linha de status dessa tarefa na fixture para `done`; se outra asserção do teste mudar de
    resultado com isso → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Notas de execução:**
  - 2026-09-25 `cancelled` — absorvido pelo P-0751 como EBK-T4 (DEB-2)

### TK-55c — O `next` projeta o colchete do cabeçalho inteiro [Sonnet · esforço low · classe implementacao]

- **Status:** `cancelled` · 2026-09-25
- **Objetivo:** a primeira linha de `backlog.py next` reproduz o colchete do cabeçalho do card como
  ele está no plano — com ` + dono` e ` · esforço <e>` quando o cabeçalho os tem.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
- **Caso medido (2026-09-25):** o card `TK-68a` tinha o cabeçalho `[Sonnet · esforço low · classe
  redacao]` e o `next` imprimiu `[Sonnet · classe redacao]`; em 2026-09-20 o `TK-58a` perdeu o
  ` + dono`, que é a marca de tarefa não delegável. A linha é montada em `backlog.py:1250` como
  `[{item.modelo} · classe {item.classe}]`.
- **Testes:** TF par sobre cópia da fixture `verde` — card `[Sonnet · classe mecanica]` → primeira
  linha termina em `[Sonnet · classe mecanica]`; card `[Opus + dono · esforço high · classe
  investigacao]` → termina em `[Opus + dono · esforço high · classe investigacao]`.
- **Verificação:**
  1. `python -m pytest tests/test_backlog.py -q` → verde, com o par acima.
  2. `python -m pytest tests/test_progresso_hook.py -q` → verde (o gancho do painel lê essa linha).
  3. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho mais os testes novos.
- **Pronto quando:** o colchete do `next` é o do cabeçalho, provado pelo par.
- **Não fazer:** não mudar o formato do resto da saída de `next`; não tocar `progresso_hook.py`.
- **Notas de execução:**
  - 2026-09-25 `cancelled` — absorvido pelo P-0751 como EBK-T3 (DEB-2)

### TK-55d — O `kit_check` conta defeito, não linha [Sonnet · esforço low · classe implementacao]

- **Status:** `cancelled` · 2026-09-25
- **Objetivo:** o número em `kit_check: check-drift FALHOU (<n> problema(s))` e em
  `kit_check: FALHOU (<n> problema(s))` passa a ser o número de defeitos: uma divergência de
  README conta `1`, e as linhas `[regenerado]`/`[versionado]` que a detalham continuam impressas
  sem entrar na contagem.
- **Arquivos-alvo:**
  - `.claude/checks/kit_check.ps1`
  - `tests/test_kit_check.py` (novo, ou o arquivo de teste do `kit_check` que já existir)
- **Caso medido (2026-09-25):** cópia de `.claude/` em diretório temporário, com uma frase
  acrescentada a uma linha da região gerada de `.claude/README.md` → a saída listou
  `README.md diverge do regenerado (2 linha(s) diferente(s)):` mais as duas linhas de detalhe
  como três itens `- ` da mesma lista, todos contados.
- **Testes:** TF sobre cópia do kit sob `tmp_path` (pular se `pwsh` não estiver no `PATH`): uma
  divergência de README com duas linhas diferentes → a contagem de problemas atribuída ao README
  é `1` e as duas linhas de detalhe aparecem na saída.
- **Verificação:**
  1. `python -m pytest <arquivo de teste do kit_check> -q` → verde, com o teste acima.
  2. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` na árvore → exit `0`.
  3. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho mais os testes novos.
- **Pronto quando:** uma divergência conta um problema, provado pelo teste, e o check segue verde
  na árvore.
- **Não fazer:** não mudar o que o `kit_check` considera divergência; não mexer na codificação do
  console (já correta).
- **Notas de execução:**
  - 2026-09-25 `cancelled` — absorvido pelo P-0751 como EBK-T5 (DEB-2)

### TK-55f — Nenhuma fixture carrega nome que o harness descobre [Sonnet · esforço low · classe mecanica]

- **Status:** `cancelled` · 2026-09-25
- **Objetivo:** um teste falha, nomeando o arquivo, quando existe sob `tests/fixtures/` um arquivo
  chamado `SKILL.md`, `CLAUDE.md`, `AGENTS.md`, `settings.json` ou `settings.local.json`.
- **Arquivos-alvo:**
  - `tests/test_fixtures_higiene.py` (novo)
- **Caso medido (2026-09-20):** uma fixture do `TK-60a` continha `SKILL.md`, e o harness passou a
  listá-la como skill invocável real. Hoje há `0` arquivos com esses nomes sob `tests/fixtures/`
  (medido em 2026-09-25).
- **Testes:** função pura `nomes_de_descoberta(raiz: Path) -> list[Path]`; TF par — diretório sob
  `tmp_path` com `a/SKILL.md` → 1 caminho; sem ele → 0; TR — `tests/fixtures/` real → 0.
- **Verificação:**
  1. `python -m pytest tests/test_fixtures_higiene.py -q` → verde.
  2. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho mais os testes novos.
- **Pronto quando:** o TR acusa fixture com nome de descoberta, provado pelo par.
- **Notas de execução:**
  - 2026-09-25 `cancelled` — absorvido pelo P-0751 como EBK-T6 (DEB-2)

### TK-55g — A doutrina do teste que discrimina e da medida publicada [Sonnet · esforço low · classe redacao]

- **Status:** `cancelled` · 2026-09-25
- **Objetivo:** `GOVERNANCA.md` §4.4 passa a carregar as quatro regras do teste que discrimina, e a
  *Disciplina de instrumento* de §3 passa de cinco para oito regras, com as três da medida
  publicada. A regra corrigida da `DB-53` do `P-0739` ganha residência aqui, e o plano fechado não
  é editado.
- **Arquivos-alvo:**
  - `GOVERNANCA.md`
- **Passos:** substituir cada **Texto atual** pelo **Texto novo** de mesmo número; rodar as
  Verificações.
- **Texto atual 1** (§4.4, uma ocorrência):

  ~~~~
  nunca a cada micro-edição; tier superior só no fechamento (`.claude/global/CLAUDE.md` Regra 7;
  skill `test-tiers`).
  ~~~~

- **Texto novo 1** (as quebras são as do bloco):

  ~~~~
  nunca a cada micro-edição; tier superior só no fechamento (`.claude/global/CLAUDE.md` Regra 7;
  skill `test-tiers`).

  **Teste que discrimina.** Teste verde só prova algo se ficaria vermelho sem o que ele protege.
  Quatro regras, cada uma com caso medido de teste que passou pelo motivo errado:

  1. **Asserção afirma relação, nunca magnitude.** O teste compara mundos: o produto certo dá a
     mesma saída nos dois, o produto revertido dá saídas diferentes, e a saída do mundo hostil não
     é vazia. A magnitude medida vai para o docstring, com a data e o mundo da medida.
  2. **Executável que lê `stdin` se testa em mundo hostil construído, não herdado.** Os mundos são
     ambiente mínimo com `PYTHONIOENCODING` de byte único e ambiente mínimo com `PYTHONUTF8=1`. O
     payload acentuado tem de chegar a um canal observável — a saída, ou o efeito colateral do
     executável silencioso —; sem canal que o carregue, o fato se declara e o teste não se escreve.
     O par negativo é o próprio produto revertido por substituição textual da fonte, nunca um stub.
  3. **Teste de instrumento roda sobre fixture copiada, nunca sobre o diário ou os planos vivos** —
     o estado vivo torna o teste instável e leva conteúdo alheio ao contexto de quem roda a suíte.
  4. **Fixture não carrega nome que o harness descobre** — `SKILL.md`, `CLAUDE.md`, `AGENTS.md`,
     `settings.json`, `settings.local.json` —, porque o harness passa a tratá-la como artefato real.
  ~~~~

- **Texto atual 2** (§3, uma ocorrência):

  ~~~~
  - **Disciplina de instrumento** — cinco regras de método, medidas na janela de 2026-09-16
  ~~~~

- **Texto novo 2** (sem quebra nova):

  ~~~~
  - **Disciplina de instrumento** — oito regras de método, as cinco primeiras medidas na janela de 2026-09-16
  ~~~~

- **Texto atual 3** (§3, uma ocorrência):

  ~~~~
    só se ele produzir; protocolo lido antes de evidência que não veio é leitura paga sem uso.
  ~~~~

- **Texto novo 3** (as quebras são as do bloco):

  ~~~~
    só se ele produzir; protocolo lido antes de evidência que não veio é leitura paga sem uso.
    **(f)** Medida publicada nomeia o objeto medido — registro, texto renderizado e texto-fonte do
    mesmo artefato têm comprimentos diferentes, e o rótulo errado sobrevive à recontagem. **(g)**
    Contagem publicada traz a regra de enumeração do corpus — o que conta e o que se descarta —,
    sem a qual o `n` não se reconcilia por quem refaz a medida. **(h)** Efeito publicado vem com a
    dispersão do controle pareado — sessão gêmea, mesmo dia, mesma árvore —, e efeito dentro da
    faixa do controle não é efeito.
  ~~~~

- **Verificação:** no PowerShell, na raiz; **antes** medido em 2026-09-25.
  1. `(Select-String -Path GOVERNANCA.md -SimpleMatch '**Teste que discrimina.**').Count` — antes `0`, depois `1`
  2. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'cinco regras de método').Count` — antes `1`, depois `0`
  3. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'efeito dentro da').Count` — antes `0`, depois `1`
  4. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho.
- **Pronto quando:** as três contagens saem nos valores de depois.
- **Não fazer:** não editar `docs/plans/P-0739-backlog-instrumento.md`; não tocar outro parágrafo de §4.4.
- **Contingências:**
  - se um **Texto atual** não for encontrado exatamente uma vez → parar e sinalizar `blocked`
    razão `premissa`, citando o número do bloco.
- **Notas de execução:**
  - 2026-09-25 `cancelled` — absorvido pelo P-0751 como EBK-T7 (DEB-2)

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

- **Status:** `done` · 2026-09-25 — aberto pelo consultor de plano do `P-0741` no escalonamento
  `ESC-1`; os três achados são `AE-2`, `AE-3` e `AE-4` de `docs/plans/P-0741-modelo-conceitual.md`
  (seção `## Achados da execução`), atribuídos a `.claude/tools/backlog.py` e vedados ao plano
  pelo invariante `I-3` dele.

**Por que um tíquete e não cards do `P-0741`:** o plano proíbe, no `I-3`, que qualquer card edite
`backlog.py`; e os três defeitos são do instrumento de fila, não do modelo conceitual. O que o
`ESC-1` reparou foi o **plano** (`DMC-19`: `Depende de` só com id de item, proveniência no campo
novo `Fundamento`) — o instrumento continua aceitando calado a forma que trava a janela.

**Ordem sugerida:** `TK-65b` (o mais barato e o que mais atrapalha o diagnóstico dos outros dois),
depois `TK-65a`, depois `TK-65c`. Nenhum depende do outro.
- **Notas de execução:**
  - 2026-09-25 `done` — 5/5 cards done (TK-65a..e); fechado na apuracao da fila de 2026-09-25

### TK-65a — `check` recusa id de `Depende de:` que não é item [Sonnet · classe implementacao]

- **Status:** `done` · 2026-09-24
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
- **Notas de execução:**
  - 2026-09-24 `review` — C-12 no check (_depende_checks); 4 TF/TR em tests/test_backlog.py, 84 verdes. Arvore viva: 3 C-12 em itens done (TK-54a:1310 prosa + id "## TK-54"; TK-78c:3882 prosa) - fora dos alvos do card, reportados ao dono

### TK-65b — O ponto de carga escreve em utf-8 antes de argparse abrir a boca [Sonnet · classe implementacao]

- **Status:** `done` · 2026-09-24
- **Objetivo:** mover a reconfiguração de encoding de `main()` para antes de `parse_args`, de modo
  que `--help` e toda mensagem de erro de argparse — que imprimem o `usage` com `→` — saiam sem
  `UnicodeEncodeError` em console cp1252.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py` (`main()`, hoje: `reconfigure` em `:1415`, `parse_args` em `:1411`)
  - `tests/test_backlog.py`
- **Verificação:** par presença-ausência por subprocesso com o ambiente hostil explícito
  (`PYTHONIOENCODING` vazio, `-X utf8=0`): `backlog.py --help` sai **exit 0** e imprime o `usage`;
  hoje o mesmo comando sai em traceback. `python -m pytest tests/test_backlog.py` verde.
- **Pronto quando:** em `main()` a reconfiguração de encoding precede `parse_args`; sob o ambiente
  hostil explícito, `backlog.py --help` sai exit 0 com o `usage` inteiro, `→` incluído; o teste é
  par presença-ausência por subprocesso, falhando sobre o `main()` anterior e passando sobre o novo.
  (Campo acrescido pelo consultor, acionamento 1 do `TK-65`, `CT65-1`: o `review_evidence.py`
  recusava o card sem ele; o critério é o da Verificação, sem escopo novo.)
- **Caso medido que motivou (2026-09-20):**
  `PYTHONIOENCODING= python -X utf8=0 .claude/tools/backlog.py --help` →
  `UnicodeEncodeError: 'charmap' codec can't encode character '→' in position 611`.
  É a metade de **escrita** do defeito que o `TK-56a` fechou na leitura.
- **Não fazer:** não trocar o `→` do texto de ajuda por ASCII — o defeito é do ponto de carga, não
  do texto; não tocar os outros pontos de carga já fechados pelo `TK-56a`.

### TK-65c — O verbo `diretiva` não descarta id em silêncio [Sonnet · classe implementacao]

- **Status:** `done` · 2026-09-24 — ramo acusar/recusar fechado em **acusar** pelo consultor
  (acionamento 2 do `TK-65`, `CT65-2`).
- **Objetivo:** `diretiva` passa a **acusar** — escreve a linha e avisa, exit 0 — o texto em que há
  id de item entre crases **depois** do ` — `, que o `next` não lê; o aviso diz quantos ids reconheceu
  antes do ` — ` e nomeia cada id descartado. Recusar a escrita está fora: a diretiva viva do dono
  (linha 2 do diário, 2026-09-24) usa a cauda de propósito para a sequência completa, e medida em
  2026-09-24 ela tem 3 ids reconhecidos e 19 ids de item na cauda — recusar a tornaria ingravável.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py` (`transacionar_diretiva`, `:1474`; `_parse_diretiva`, `:351`, só leitura)
  - `tests/test_backlog.py`
- **Id descartado, definição única:** texto entre crases na cauda (depois do primeiro ` — `) que está
  em `_ids_da_arvore(modelo)` (`:518`) e **não** está entre os ids que `_parse_diretiva` devolve; sem
  repetição, na ordem em que aparece. Crase que não é id de item (`done`, `next`, nome de arquivo)
  não é descartado e não entra no aviso.
- **Verificação:** par presença-ausência por `transacionar_diretiva` sobre fixture cuja árvore tem os
  ids citados — diretiva ``Priorize `A` — e depois `B`, `C` `` (os três ids de item): `exit_code == 0`,
  a linha é escrita, e `mensagem` contém `B` e `C` e a contagem 1 de reconhecidos; diretiva
  ``Priorize `A` — texto com `done` `` : `mensagem` idêntica à de hoje para a mesma árvore (nenhum
  aviso de descarte). `python -m pytest tests/test_backlog.py` verde (86 passed em 2026-09-24).
- **Pronto quando:** `transacionar_diretiva` segue escrevendo e saindo `exit_code 0` em toda forma; com
  id descartado, o aviso nomeia cada um e a contagem de reconhecidos, e chega ao console pela via que
  `main()` já usa (`print(resultado.mensagem)`, `:1706`), concatenado por quebra de linha ao aviso de
  `_regenerar_bloco_fila` quando os dois existem; sem id descartado, `mensagem` é a de hoje; o conjunto
  que `_parse_diretiva` devolve não muda; o teste é par presença-ausência sobre as duas formas.
- **Caso medido que motivou (2026-09-20):** `_parse_diretiva` sobre
  ``**Diretiva de priorização:** Priorize `P-0741` — e depois `TK-57`, `TK-56` `` devolve
  `['P-0741']`: os tíquetes que a própria diretiva do dono manda priorizar saem da fila sem aviso.
  Na janela do `P-0741` isso produziu uma fila filtrada a um único item e uma inversão de
  prioridade que só a leitura do código explicou.
- **Não fazer:** não passar a colher ids da cauda livre — a cauda é para humanos por gramática
  publicada (skill `diario-de-obras`, *Cabeçalho do diário*); o reparo é tornar o descarte
  **audível**, não mudar o que o campo significa.

### TK-65d — Os dois `Depende de` do diário voltam à gramática [Sonnet · classe mecanica]

- **Status:** `done` · 2026-09-24 — aberto pelo loop no fechamento do `TK-65a` (laudo ressalva 94%,
  achado de processo roteado a subitem do `TK-65`).
- **Objetivo:** devolver `python .claude/tools/backlog.py check` a exit 0 saneando os dois campos
  `- **Depende de:**` do diário que a violação `C-12` do `TK-65a` acusa, sem perder texto.
- **Arquivos-alvo:**
  - `docs/DIARIO_DE_OBRAS.md` (só as duas linhas abaixo, localizadas por conteúdo)
- **Reparo, por linha:**
  1. No `### TK-54a`, o bullet `- **Depende de:** decisões 1..7 de `` `## TK-54` `` (copiadas inline
     no que vinculam), a` e a continuação recuada logo abaixo: trocar só o rótulo
     `**Depende de:**` por `**Fundamento:**`, texto e continuação verbatim — é proveniência, não
     dependência de item (mesma convenção do `DMC-19` do `P-0741`).
  2. No `### TK-78c`, o bullet `` - **Depende de:** `TK-78a` (as duas editam a skill scrum-master, em
     trechos distintos) ``: reduzir a `` - **Depende de:** `TK-78a` `` e apensar ao fim do bullet
     `- **Fundamento:**` do mesmo card a frase
     `` Depende do `TK-78a` porque as duas editam a skill scrum-master, em trechos distintos. ``
- **Verificação:** antes, `python .claude/tools/backlog.py check` sai exit 1 com exatamente as três
  `C-12` (`TK-54a` ×2, `TK-78c` ×1); depois, exit 0 com `check: OK — nenhuma violação.`
- **Pronto quando:** os dois bullets estão na forma do Reparo, sem palavra perdida (a proveniência
  mora em `Fundamento`, e o `Depende de` do `TK-78c` lista só `` `TK-78a` ``); `backlog.py check`
  sai exit 0 com `check: OK — nenhuma violação.`
- **Não fazer:** não tocar `.claude/tools/backlog.py` — piso de dívida ou isenção de item terminal
  para `C-12` não foram adotados; o reparo é do corpus, não do lint.

### TK-65e — O ramo concatenado do aviso de `diretiva` ganha teste [Sonnet · classe mecanica]

- **Status:** `done` · 2026-09-24 — aberto pelo loop no fechamento do `TK-65c` (laudo aprovado
  100%, achado de processo: o `Pronto quando` do `TK-65c` exige a concatenação e nenhum teste a tranca).
- **Objetivo:** trancar por teste o ramo em que `transacionar_diretiva` devolve, na mesma `mensagem`,
  o aviso de id descartado **e** o aviso de `_regenerar_bloco_fila`, unidos por quebra de linha.
- **Arquivos-alvo:**
  - `tests/test_backlog.py` (junto de `test_tf_diretiva_acusa_id_descartado_na_cauda`)
- **Verificação:** um teste sobre cópia da fixture `next_tk90` **sem** `_inserir_bloco_gerado` (sem o
  marcador `<!-- fila:gerada -->`, o que faz `_regenerar_bloco_fila` avisar), com a diretiva
  ``Priorize `TK-90a` — e depois `TK-90b`, `FFO-T1` ``: `exit_code == 0` e `mensagem` com duas linhas —
  a 1ª nomeia `TK-90b` e `FFO-T1`, a 2ª é o aviso do bloco gerado. `python -m pytest tests/test_backlog.py`
  verde.
- **Pronto quando:** o teste existe, passa sobre o `backlog.py` vigente e falharia se a concatenação
  deixasse cair qualquer um dos dois avisos.
- **Não fazer:** não tocar `.claude/tools/backlog.py` — a entrega do `TK-65c` já produz as duas
  linhas (exercitado ponta a ponta na revisão dele); falta só a trava.

## TK-66 — O atribuidor de `review_evidence.py` fabrica autoria com tarefa nunca despachada

- **Status:** `done` · 2026-09-25 — aberto pela janela de orquestração do `P-0743` ao fechar a
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

**Decisão do planejamento (2026-09-25).**

- **`DT-1` — rota 1.** Só casa tarefa com `status` `in-progress`, `review` ou `done`. A rota 1 ataca
  a causa medida (o casamento não consulta `status`). A rota 2 mantém a previsão dentro do mapa de
  autoria, só que com outro nome. A rota 3 depende do `--desde`, que este tíquete declara fora de
  escopo, e o recorte por instantâneo do despacho já é do `TK-78c`. Arquivo que deixa de casar cai
  em `sem-atribuicao`, que é o balde honesto: o instrumento não sabe o autor, e quem decide a rota é
  a `B0`. `blocked` e `cancelled` também não casam: não dá para distinguir `blocked` vindo de
  `ready` de `blocked` vindo de `in-progress`, e atribuir sem saber é o defeito que se corrige aqui.
- **`DT-2` — o `status` vem do dossiê que o `rdo.py` já extrai.** A linha `- **Status:**` do card
  cai em `dossie.extras` (rótulo fora de `_CAMPOS_CANONICOS`); o estado é o primeiro literal entre
  crases do conteúdo. Não se carrega `backlog.py` (seria carregador novo e cópia nova no ajudante
  `_init_repo_com_baseline`, âncora da `SAN-T1` do `P-0749`). Tarefa sem linha de status não casa.
- **Achado roteado ao `P-0749`, não reparado aqui:** plano em pasta (`SAN-T2`) guarda o estado em
  `estado.tsv` e não tem linha `**Status:**` — nele nenhuma outra tarefa casará, e todo arquivo
  alheio sairá `sem-atribuicao`. É o lado seguro, mas a `SAN-T3` (evidência na pasta do plano) é o
  lugar de ensinar o atribuidor a ler o `estado.tsv`.

### TK-66a — O atribuidor só casa tarefa já despachada [Sonnet · esforço medium · classe implementacao]

- **Status:** `done` · 2026-09-25
- **Depende de:** `TK-74a`
- **Objetivo:** `mapear_alvos_de_outras_tarefas` passa a pular toda tarefa cujo `status` não seja
  `in-progress`, `review` ou `done`; alvo de tarefa não despachada deixa de virar
  `alvo-de-outra-tarefa`.
- **Fundamento:** `AE-3` do `P-0743` (14 arquivos de janela paralela rotulados
  `alvo-de-outra-tarefa (DOM-T3/T4/T5)`, tarefas em `ready`); `DT-1` e `DT-2` acima. Depende da
  `TK-74a` porque as duas editam a atribuição a outra tarefa em `review_evidence.py`, e o TF dela usa
  o ajudante que este card altera.
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
- **Contratos/classes:**
  - constante nova, junto de `_BACKTICK_RE`: `_STATUS_DESPACHADO = frozenset({"in-progress", "review", "done"})`.
  - função nova `_status_do_dossie(dossie) -> str | None`, logo antes de
    `mapear_alvos_de_outras_tarefas`: percorre `dossie.extras` (lista de pares `[rotulo, conteudo]`);
    no primeiro par cujo `rotulo.strip().lower() == "status"`, devolve o primeiro literal entre
    crases de `conteudo` (`_BACKTICK_RE.search`), sem espaços em volta, ou `None` se não houver
    literal; sem o par → `None`.
  - em `mapear_alvos_de_outras_tarefas`, logo depois do `try/except` que extrai o dossiê:
    `if _status_do_dossie(dossie) not in _STATUS_DESPACHADO:` → `continue`. Assinatura e retorno
    inalterados. A docstring ganha uma frase: tarefa não despachada (`status` fora de
    `in-progress`/`review`/`done`, ou ausente) é pulada, porque alvo declarado sem despacho é
    previsão, não autoria (`TK-66`).
  - em `tests/test_review_evidence.py`, `_escrever_plano_duas_tarefas` ganha o parâmetro
    `status_t2: str | None = "done"`: não sendo `None`, escreve
    ``f"- **Status:** `{status_t2}` · 2026-09-25\n"`` como primeira linha depois do heading de T2;
    `None` omite a linha. O default `"done"` mantém verdes os nove usos existentes.
- **Passos:**
  1. Altere o ajudante e escreva o TF abaixo; rode-o e veja falharem os casos `ready`, `blocked`,
     `cancelled` e `None`.
  2. Implemente os contratos; rode o arquivo de teste inteiro.
  3. Rode as Verificações.
- **Testes:**
  - TF `test_tf_atribuir_so_tarefa_despachada_casa` parametrizado em `status_t2` com os sete casos
    `in-progress`, `review`, `done` (esperado `atribuicao: src/a.py -> alvo-de-outra-tarefa (T2)`) e
    `ready`, `blocked`, `cancelled`, `None` (esperado `atribuicao: src/a.py -> sem-atribuicao`):
    repositório de `_init_repo_com_baseline`; plano de
    `` _escrever_plano_duas_tarefas(plano, "edita `src/b.py`.", "cria `src/a.py`.", status_t2=<caso>) ``;
    `src/a.py` criado no repositório; `main([... "--atribuir"])` devolve `0` e a saída contém a linha
    esperada.
  - TR: `tests/test_review_evidence.py` inteiro verde, inclusive os dois TF da `TK-74a`.
- **Restrições desta tarefa:**
  - Não renomear nem mudar a assinatura de `mapear_alvos_de_outras_tarefas`, `confrontar_escopo`,
    `formatar_atribuicoes` e `_init_repo_com_baseline` (âncoras da `SAN-T1` do `P-0749`).
  - Não carregar `backlog.py` nem criar carregador novo.
  - Não commitar.
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho
    sobe em exatamente `7`.
- **Não fazer:** não criar balde novo de atribuição; não usar `--desde` na decisão; não ler
  `estado.tsv`.
- **Contingências:**
  - se `dossie.extras` não trouxer o par de rótulo `Status` para um card que tem a linha
    `- **Status:**` → parar e sinalizar `blocked` razão `premissa`, colando o `extras` impresso
  - se algum teste preexistente de `tests/test_review_evidence.py` ficar vermelho com o default
    `"done"` → parar e sinalizar `blocked` razão `premissa`, colando o nome do teste
- **Verificação:** no PowerShell, na raiz do repositório.
  1. `python -m pytest tests/test_review_evidence.py -q` — depois, o medido no despacho `+ 7`,
     `0 failed`
  2. `python -m pytest -q` — total de `passed` = o medido no despacho `+ 7`, `0 failed`
  3. `(Select-String -Path .claude/tools/review_evidence.py -SimpleMatch '_STATUS_DESPACHADO').Count`
     — antes `0`, depois `2`
- **Pronto quando:** tarefa em `ready`, `blocked`, `cancelled` ou sem status não recebe atribuição, e
  tarefa em `in-progress`, `review` ou `done` segue recebendo — Verificações 1 a 3.
- **Fora do escopo desta tarefa:** a leitura do `estado.tsv` de plano em pasta (`SAN-T3` do
  `P-0749`, achado acima); o alvo-diretório (`TK-74a`).
- **Notas de execução:**
  - 2026-09-25 `review` — V1 51 passed (44+7); V2 333 passed (326+7); V3 2

## TK-67 — A rodada de revisão de guardrails está pendente desde 2026-08-08

- **Status:** `cancelled` · 2026-09-25 — aberto pela sessão de planejamento do `P-0745`, quando a skill
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

**Insumo do veredito dos procedimentos, roteado pelo consultor do `P-0747` em 2026-09-23.** Fonte:
`docs/plans/_VEREDITO-procedimentos-2026-09-22.md`, roteado por `DCS-25` do `P-0747`. Três
matérias de doutrina que não são guardrail novo — são ajuste de regra existente, saída legítima da
rodada:

1. **A forma da devolução do `pantonic-model-designer` está errada em dois pontos** (veredito
   §3.5). A regra manda devolver *"a seção inteira e literal … nenhuma prosa fora da seção"*;
   medido no `P-0747`, o modelador desviou duas vezes e acertou as duas: não recopiou 94 linhas já
   na árvore (devolveu ponteiro, cabeçalho de estado, linha da versão e saída do `check`) e
   devolveu **fora da seção** o achado mais útil da primeira autoria (quatro linhas de
   `GOVERNANCA.md` e do próprio arquivo dele fora da `F-4`). Texto a publicar no agente: a
   devolução é ponteiro + cabeçalho de estado + linha da versão + saída literal do `check` + um
   campo nomeado `Achados fora da seção`, que quem conduz roteia ao planejador.
2. **O enunciado composto de atos registrados é forma legítima e frequente** (veredito §3.6).
   `GOVERNANCA.md` §3.2 fala em *"enunciado do problema ou prompt de origem"*; no `P-0747` o
   enunciado foi uma frase do dono mais oito atos registrados em datas diferentes, transcritos
   pelo condutor na `## 0`, e o lastro funcionou. Texto a publicar em §3.2 (*Lastro no enunciado*):
   o enunciado pode ser composto de atos do dono registrados, cada um com **data e ponteiro**,
   transcritos na `## 0`.
3. **Ruído do harness** (veredito §5): o hook `UserPromptSubmit` injetou a *PRÓXIMA TAREFA* de
   outra iniciativa numa sessão de planejamento (Regra 2, coesão), e o gate `modelo-por-fase`
   pediu Opus numa sessão que o dono abriu em Fable — a matriz admite Fable *"só sob solicitação
   explícita do dono"*, e a escolha do modelo na sessão é essa solicitação. Os dois são de
   `modelo-por-fase` e do hook; a rodada os avalia pela pergunta única e ajusta, sem guardrail
   novo.

**Cards (2026-09-25, *Tíquete nasce executável*).** A rodada é o `TK-67a`; os três ajustes de regra
existente, com o texto já dado acima, são o `TK-67b`. Do item 3, só o aviso de modelo entra: o
`backlog_hook.py` injeta a próxima tarefa apenas quando o prompt contém a expressão literal
*próximo passo* (`_GATILHO`, `backlog_hook.py:33`), o que é o contrato dele — sem ação.
- **Notas de execução:**
  - 2026-09-25 `cancelled` — absorvido pelo P-0751 — Esgotar o backlog antes da publicação do kit (DEB-2)

### TK-67a — A rodada de revisão de guardrails pendente desde 2026-08-08 [Opus · esforço high · classe investigacao]

- **Status:** `cancelled` · 2026-09-25
- **Objetivo:** registrar em `GOVERNANCA.md` §7.1, *Registro das rodadas*, a rodada disparada
  pelos planos fechados depois da rodada `P-0731`, aplicando o procedimento de §7.1 às guardrails
  em escopo, e marcar `OBSOLETA desde <rodada>` a que ficar sem caso citável.
- **Arquivos-alvo:**
  - `GOVERNANCA.md`
- **Método de sondagem:**
  1. **Rótulo e gatilho.** A rodada se rotula pelo plano fechado mais recente, `P-0750`, e pela data
     da execução: `P-0750 — <AAAA-MM-DD>`. Os planos que a disparam são os `done` do índice de
     `docs/DIARIO_DE_OBRAS.md` fechados depois de 2026-08-08: `P-0732`, `P-0735`, `P-0736`,
     `P-0738`, `P-0739`, `P-0740`, `P-0741`, `P-0743`, `P-0745`, `P-0746`, `P-0747`, `P-0748`,
     `P-0749` e `P-0750` (medido em 2026-09-25).
  2. **Escopo.** O registro ainda não tem duas rodadas do regime por plano, então a `1.4.0` segue
     como penúltima e o escopo é o mesmo da rodada `P-0731`: treze guardrails, por nome — regra de
     dependência, ACL, egress G6, namespace de estado, gate de conformance, allowlist de
     subcomandos destrutivos, piso de regressão, disciplina de contexto, `G-DEADCODE`,
     `G-PLANFIDELITY`, `G-PREMISE`, `G-PLANREADY` e `G-EXECREADY`. Fora por idade: `G-README`,
     `G-SCOPE`, `G-SURFACE`, `G-REPLAN`, `G-NOASK`, `G-MODULO` e `G-TOOLDENY`.
  3. **Isenção, re-confirmada e não herdada.** Para cada uma das seis isentas na rodada `P-0731`,
     rodar hoje o check que a isentou e registrar a linha de sumário: em
     `D:\workspaces\PantonicVideo`, `python -m pytest tests/conformance/test_layer_imports.py
     tests/conformance/test_acl_no_external_in_plugins.py tests/conformance/test_filesystem_egress.py
     tests/boundary/test_state_writer_namespacing.py -q -rs`; no hub, `python -m pytest -q`; e a
     contagem de `permissions.deny` em `.claude/settings.json`. Check que não roda, que sai com
     `skip`/`xfail` no alvo ou cuja lista cobre tudo **não isenta**: a guardrail vai para o passo 4
     e o check morto entra na entrada como achado.
  4. **Pergunta única**, para cada guardrail em escopo e não isenta: *"Esta regra mudou algum
     comportamento desde a penúltima rodada registrada? Cite o caso."* Caso citável é ocorrência
     **registrada** entre 2026-08-08 e a data da execução — em `docs/DIARIO_DE_OBRAS.md`,
     `docs/DIARIO_HISTORICO.md`, `docs/plans/`, `docs/RDO/`, `docs/Entregas Aceitas/` ou no diário de
     `D:\workspaces\PantonicVideo` — em que a regra bloqueou algo, forçou correção ou embasou
     decisão. Suíte verde não é caso; lembrança sem registro não é caso. O caso se cita por
     arquivo e identificador (`AE-`, `DB-`, id de tarefa).
  5. **Resultado.** Guardrail sem caso citável recebe, no próprio item de §7, a marca
     `OBSOLETA desde P-0750` — permanece em vigor por uma rodada, e a remoção é tarefa da rodada
     seguinte. Zero marcações é resultado legítimo.
- **Pronto quando (o fato que tem de existir ao final):** a entrada `P-0750 — <data>` no *Registro
  das rodadas* de §7.1, com os planos que a dispararam, as treze em escopo, as sete fora por
  idade, cada isenta com o check e a linha de sumário de hoje, e cada uma das demais com o caso
  citável (arquivo e identificador) ou com a marca aplicada no item de §7.
- **Verificação:**
  1. Contagem da entrada nova:

     ```
     (Select-String -Path GOVERNANCA.md -Pattern '^- \*\*.P-0750. — 2026-').Count
     ```

     antes `0` (medido em 2026-09-25), depois `1`.
  2. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho.
- **Não fazer:** não criar guardrail; não remover guardrail (remoção é da rodada seguinte); não
  editar plano fechado; não tocar as matérias do `TK-67b`.
- **Contingências:**
  - se `D:\workspaces\PantonicVideo` ou um dos quatro arquivos de teste não existir → a guardrail
    daquele check vai para o passo 4, e a entrada registra `check ausente: <caminho>`.
- **Notas de execução:**
  - 2026-09-25 `cancelled` — absorvido pelo P-0751 como EBK-T14 (DEB-2)

### TK-67b — Três ajustes de regra existente: a devolução do modelador, o enunciado composto e o aviso de modelo [Sonnet · esforço medium · classe redacao]

- **Status:** `cancelled` · 2026-09-25
- **Objetivo:** o `pantonic-model-designer` passa a devolver ponteiro, cabeçalho, linha da versão,
  saída do `check` e o campo `Achados fora da seção` — em vez de recopiar a seção —, com
  `GOVERNANCA.md` §3 e §3.2 dizendo o mesmo; §3.2 reconhece o enunciado composto de atos do dono
  registrados; e o aviso da fase intelectual do hook de modelo deixa de mandar parar quem está em
  Fable.
- **Fundamento:** itens 1, 2 e 3 do insumo do veredito dos procedimentos, acima, com os casos
  medidos no `P-0747`.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-model-designer.md`
  - `GOVERNANCA.md`
  - `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`
- **Passos:** substituir cada **Texto atual** pelo **Texto novo** de mesmo número, no arquivo
  indicado; rodar `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate`; rodar as
  Verificações.
- **Texto atual 1** (`.claude/agents/pantonic-model-designer.md`, uma ocorrência):

  ~~~~
  Todo ato devolve exatamente duas coisas, e nada além delas:

  1. A seção **inteira e literal** — a `## 1. Modelo conceitual` na autoria; a
     `## 1A. Modelo conceitual — versão pendente de validação` em todo ato que versiona. Não um
     trecho, não um resumo do que mudou.
  2. A linha da versão do ato, registrada em `### 1.4 Registro de versões` dentro da própria seção,
     com a situação que o ato produz.

  Nenhuma prosa fora da seção, nenhum comentário sobre a qualidade do plano, nenhuma recomendação.
  ~~~~

- **Texto novo 1** (as quebras são as do bloco):

  ~~~~
  Todo ato devolve quatro coisas, e nada além delas:

  1. O **ponteiro** para a seção que o ato escreveu na árvore — a `## 1. Modelo conceitual` na
     autoria; a `## 1A. Modelo conceitual — versão pendente de validação` em todo ato que
     versiona —, com a linha `**Estado do modelo:**` copiada. A seção já está no arquivo: não a
     recopie.
  2. A linha da versão do ato, registrada em `### 1.4 Registro de versões` dentro da própria seção,
     com a situação que o ato produz.
  3. A saída literal de `python .claude/tools/modelo.py check --plano <plano>` depois do ato.
  4. O campo `Achados fora da seção:` — o que você viu fora da seção e que afeta o plano, um por
     linha, com arquivo, linha e fato —, ou `nenhum`. Quem conduz a sessão o roteia ao planejador.

  Nenhum comentário sobre a qualidade do plano e nenhuma recomendação fora do campo 4.
  ~~~~

- **Texto atual 2** (`GOVERNANCA.md` §3, matriz, linha *Modelagem*; sem quebra nova):

  ~~~~
  devolve a seção literal e a linha do registro de versões que registra o ato (`pantonic-model-designer`)
  ~~~~

- **Texto novo 2:**

  ~~~~
  devolve o ponteiro da seção, a linha do registro de versões que registra o ato, a saída do `check` e os achados fora da seção (`pantonic-model-designer`)
  ~~~~

- **Texto atual 3** (`GOVERNANCA.md` §3.2, tabela de papéis, linha *modelador*; sem quebra nova):

  ~~~~
  devolve a seção literal e a linha do ato em `### 1.4 Registro de versões`;
  ~~~~

- **Texto novo 3:**

  ~~~~
  devolve o ponteiro da seção, a linha do ato em `### 1.4 Registro de versões`, a saída do `check` e os achados fora da seção;
  ~~~~

- **Texto atual 4** (`GOVERNANCA.md` §3.2, *Lastro no enunciado*; sem quebra nova e sem refluxo):

  ~~~~
  o que o modelador imaginou. E o
  ~~~~

- **Texto novo 4:**

  ~~~~
  o que o modelador imaginou. O enunciado pode ser composto — uma frase do dono mais atos dele registrados em datas diferentes, transcritos na `## 0`, cada ato com a data e o ponteiro ao registro —, e o lastro vale igual para cada parte. E o
  ~~~~

- **Texto atual 5** (`.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`, uma ocorrência):

  ~~~~
          "Se o modelo ativo NAO for Opus, PARE e peca ao dono `/model opus` antes de "
          "prosseguir (anuncie a troca — Regra 5). Se ja estiver em Opus, ignore.",
  ~~~~

- **Texto novo 5:**

  ~~~~
          "Se o modelo ativo for Sonnet ou Haiku, PARE e peca ao dono `/model opus` antes de "
          "prosseguir (anuncie a troca — Regra 5). Em Opus ou Fable, ignore: o modelo "
          "da sessao e escolha do dono.",
  ~~~~

- **Verificação:** no PowerShell, na raiz; **antes** medido em 2026-09-25.
  1. `(Select-String -Path .claude/agents/pantonic-model-designer.md -SimpleMatch 'Achados fora da seção:').Count` — antes `0`, depois `1`
  2. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'devolve a seção literal').Count` — antes `2`, depois `0`
  3. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'O enunciado pode ser composto').Count` — antes `0`, depois `1`
  4. `(Select-String -Path .claude/global/hooks/modelo_por_fase_userpromptsubmit.py -SimpleMatch 'Em Opus ou Fable, ignore').Count` — antes `0`, depois `1`
  5. `python -m py_compile .claude/global/hooks/modelo_por_fase_userpromptsubmit.py` → exit `0`
  6. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate` e `-Mode check-drift` → exit `0`
  7. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho.
- **Pronto quando:** as quatro contagens saem nos valores de depois, o hook compila e o kit segue
  sem drift interno.
- **Não fazer:** não rodar `materializar.py apply` nem escrever em `C:\Users\panta\.claude\` — a
  cópia do hook no ponto de carga é do dono, e o relatório de encerramento a pede; não tocar o
  aviso da fase de execução nem o `systemMessage` da fase intelectual.
- **Contingências:**
  - se um **Texto atual** não for encontrado exatamente uma vez → parar e sinalizar `blocked`
    razão `premissa`, citando o número do bloco.
- **Notas de execução:**
  - 2026-09-25 `cancelled` — absorvido pelo P-0751 como EBK-T12 (DEB-2)

## TK-68 — A cópia do kit das regras globais divergiu do arquivo que o dono carrega

- **Status:** `done` · 2026-09-25 — aberto pela sessão de planejamento do `P-0745`, ao confrontar
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

**Estado medido na revisão de pertinência (2026-09-24).** A segunda metade do defeito ("nada afere
a diferença") caiu: `.claude/projecoes.json` declara `global/CLAUDE.md` no alvo `usuario`, e
`python .claude/tools/materializar.py drift --alvo usuario` sai **1** acusando três arquivos com
conteúdo diferente no destino — `~/.claude/CLAUDE.md` (a cópia do kit segue sem os Controles 1.1
e 1.2: `grep -c "Controle 1.1"` → **0** no kit, **2** no global), `~/.claude/docs/GOVERNANCA_MEMORIAS.md`
e `~/.claude/hooks/modelo_por_fase_userpromptsubmit.py`. Resta a reconciliação do conteúdo, arquivo
a arquivo, e só então o `apply` — que escreve em `~/.claude/` e por isso é ato do dono.

**Autorização do dono (2026-09-25), verbatim:** *"pode aplicar no fim do TK-68"*. O `apply` deixa de
ser ato do dono e passa a ser o **último passo do fechamento deste tíquete**, executado pelo
condutor, nesta ordem e só com todas as condições satisfeitas:
1. `Select-String -Path .claude/global/CLAUDE.md -Pattern "Controle 1.1","Controle 1.2"` acha os dois
   — sem isso o `apply` apaga os Controles do arquivo do dono; falhou, **não aplica** e reporta.
2. Cópia de segurança dos três destinos em `~/.claude/` com sufixo `.bak` (`CLAUDE.md`,
   `docs/GOVERNANCA_MEMORIAS.md`, `hooks/modelo_por_fase_userpromptsubmit.py`).
3. `python .claude/tools/materializar.py apply --alvo usuario`.
4. `python .claude/tools/materializar.py drift --alvo usuario` sem `FALHOU`; falhou, restaura os `.bak`
   e reporta.
5. O relatório ao dono diz que foi aplicado e que a regra nova só vale depois de fechar e reabrir o
   Claude Code.

**Reconciliação arquivo a arquivo (2026-09-25, medida na autoria do card).** A rota já está
decidida: `docs/RESIDENCIA_DOUTRINA.md` (linha da classe `global`) e `GOVERNANCA.md` (tabela de
residência) fazem de `.claude/global/` o canônico e de `~/.claude/` a projeção. Diff de
`~/.claude/<arquivo>` contra `.claude/global/<arquivo>`, ignorando `\r`:

| Arquivo | Diferença | Quem é mais novo | Destino |
|---|---|---|---|
| `CLAUDE.md` | (a) Controles 1.1 e 1.2 da Regra 1, 28 linhas só no do dono; (b) Regra 8 com *"devolve `blocked` à triagem do plano"* e Regra 9 inteira (*"A mensagem ao dono se entende sozinha"*, `P-0750`) só no kit | (a) dono, (b) kit | (a) entra no kit pelo `TK-68a`; (b) chega ao dono pelo `apply` |
| `docs/GOVERNANCA_MEMORIAS.md` | 1 linha: *"a skill `proximo-passo` drena"* no dono × *"a skill `scrum-master` drena"* no kit | kit (`proximo-passo` não existe mais no hub) | chega ao dono pelo `apply`; nenhuma edição |
| `hooks/modelo_por_fase_userpromptsubmit.py` | nudge de execução *"Gate … recomende `/model sonnet`"* no dono × *"Nota … NAO pare"* no kit (`TK-78a`); leitura do `stdin` em UTF-8 só no kit | kit | chega ao dono pelo `apply`; nenhuma edição |

Fechado o `TK-68a`, o kit é superconjunto do arquivo do dono nos três arquivos, e o `apply` da
autorização acima não apaga nada que só o dono tenha.

**Estado em 2026-09-25, depois do `TK-68a` `done` (aprovado 100%).** A condição 1 da autorização
está satisfeita, mas o `apply` **não rodou**: o classificador de permissão do modo automático do
Claude Code recusou o comando (cópia `.bak` + `apply`) como *Self-Modification*, antes de qualquer
escrita — `~/.claude/` está intocado e o `drift --alvo usuario` segue saindo `1` nos três arquivos.
O tíquete fica aberto só por esse passo; ele fecha quando o dono rodar os passos 2–4 da autorização
(ou liberar a regra de permissão e mandar o condutor rodá-los).

**Fechamento (2026-09-25).** O dono rodou os passos 2–4 (cópias `.bak` + `apply`), sem falha; o
condutor re-mediu `python .claude/tools/materializar.py drift --alvo usuario` → `OK - sem drift`,
exit `0`. Tíquete `done` 1/1. As regras novas (Controles 1.1/1.2 já vigentes; Regra 8 revisada e
Regra 9 novas no arquivo do dono) valem a partir da próxima abertura do Claude Code.

### TK-68a — Os Controles 1.1 e 1.2 da Regra 1 entram na cópia canônica do kit [Sonnet · esforço low · classe redacao]

- **Status:** `done` · 2026-09-25
- **Objetivo:** `.claude/global/CLAUDE.md` passa a carregar, sob a Regra 1 e antes da Regra 2, os
  Controles 1.1 e 1.2 com o texto exato do arquivo do dono. É o que torna seguro o `apply` do
  fechamento do tíquete: sem os controles no kit, o `apply` os apaga de `~/.claude/CLAUDE.md`.
- **Fundamento:** tabela de reconciliação acima, linha `CLAUDE.md` (a).
- **Arquivos-alvo:**
  - `.claude/global/CLAUDE.md`
  - `tests/test_global_claude.py` (novo)
- **Passos:**
  1. Em `.claude/global/CLAUDE.md`, substitua o **Texto atual 1** pelo **Texto novo 1**.
  2. Crie `tests/test_global_claude.py` com o teste descrito em **Testes**.
  3. Rode as Verificações.
- **Texto atual 1** (uma ocorrência, linhas 16–18 hoje):

  ~~~~
  prossiga com a implementação em uma nova mensagem/turno iniciada pelo usuário.

  ## Regra 2 — Integridade do contexto
  ~~~~

- **Texto novo 1:**

  ~~~~
  prossiga com a implementação em uma nova mensagem/turno iniciada pelo usuário.

  ### Controle 1.1 — Persistir o plano **é** encerramento do planejamento, não execução

  Ao sair do Plan Mode com plano aprovado, **grave o plano no repositório antes de encerrar o
  turno**: em projeto Pantonic*, `docs/plans/P-<MMDD>-<slug>.md` + uma linha apensada a
  `docs/plans/_INBOX.md`. Isso **não** é execução e a Regra 1 **não** o proíbe — o que a Regra 1
  proíbe é começar a implementar. Só depois de gravado o turno encerra.

  **Motivo:** em Plan Mode o agente não pode escrever arquivo; depois da aprovação a Regra 1 manda
  parar. Lido literalmente, o arquivamento não tem onde morar, e o plano só existe no contexto da
  sessão — que o `/clear` seguinte destrói. Defeito medido em 2026-09-04 (PantonicVideo): dois
  planos aprovados no mesmo dia, nenhum gravado em `docs/plans/`, nenhum no `_INBOX.md`; a retomada
  seguinte de backlog encontrou fila vazia e reportou "nada a fazer" com dois planos aprovados
  pendurados. O harness salva uma cópia em `~/.claude/plans/<slug-aleatório>.md`, mas esse nome não
  é rastreável a partir do backlog — não substitui o arquivamento canônico.

  ### Controle 1.2 — Não abrir sessão de planejamento sobre alvo que já tem plano aprovado

  Antes de entrar em Plan Mode para um tíquete/iniciativa, verifique se ele já tem plano vivo
  (`docs/plans/`, `_INBOX.md`, índice do diário). Se já tiver, **não replaneje**: ou executa o que
  está aprovado, ou emenda o plano existente por decisão explícita do dono. Planejar duas vezes o
  mesmo alvo produz dois planos vivos disputando a mesma rota — que é exatamente o que a regra de
  convergência de uma iniciativa proíbe (skill `diario-de-obras`, "Planos derivados").

  **Motivo:** mesmo incidente de 2026-09-04 — a segunda sessão custou um contexto inteiro de Opus e
  produziu um artefato descartado pelo dono. A causa dela foi o Controle 1.1: como o primeiro plano
  não estava gravado em lugar nenhum rastreável, a sessão seguinte não tinha como saber que ele
  existia.

  ## Regra 2 — Integridade do contexto
  ~~~~

- **Restrições desta tarefa:**
  - A edição é substituição literal; o texto novo entra exatamente como está no bloco, sem
    reescrita editorial (o arquivo do dono é a fonte do literal, e o `apply` o sobrescreve com
    esta cópia). O arquivo tem final de linha LF: preserve.
  - Não commitar.
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho
    não diminui.
- **Não fazer:** não rodar `materializar.py apply` nem escrever em `C:\Users\panta\.claude\` — o
  `apply` é o último passo do fechamento do tíquete, do condutor, nas condições da autorização
  acima; não tocar a Regra 8 nem a Regra 9 do kit (são a versão mais nova); não editar
  `.claude/global/docs/GOVERNANCA_MEMORIAS.md` nem `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`
  (a versão do kit prevalece, tabela acima); não tocar `.claude/sync-kit.ps1`.
- **Contingências:**
  - se o **Texto atual 1** não for encontrado **exatamente uma vez** → parar e sinalizar `blocked`
    razão `premissa`, colando a contagem
  - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com
    qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** TR novo em `tests/test_global_claude.py`, lendo `.claude/global/CLAUDE.md` em UTF-8:
  `### Controle 1.1 —` e `### Controle 1.2 —` aparecem uma vez cada, nessa ordem, depois de
  `## Regra 1 —` e antes de `## Regra 2 —`. Falha sobre o arquivo anterior, passa sobre o novo — é
  a guarda de que o canônico não volta a perder os controles, que o `apply` apagaria do dono.
- **Verificação:** no PowerShell, na raiz do repositório; **antes** medido em 2026-09-25.
  1. `(Select-String -Path .claude/global/CLAUDE.md -Pattern "^### Controle 1\.[12] ").Count` —
     antes `0`, depois `2`
  2. `(Get-Content .claude/global/CLAUDE.md -Encoding utf8).Count` — antes `182`, depois `210`
  3. `git diff --no-index --ignore-cr-at-eol --numstat "$env:USERPROFILE/.claude/CLAUDE.md" .claude/global/CLAUDE.md` —
     antes `17	29`, depois `17	1` (sobra só a Regra 8/9, que é do kit)
  4. `python -m pytest tests/test_global_claude.py -q` → verde
  5. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho mais o teste novo
- **Pronto quando:** o canônico do kit carrega os Controles 1.1 e 1.2 com o literal do arquivo do
  dono, o diff contra `~/.claude/CLAUDE.md` se reduz às linhas em que o kit é o mais novo, e o TR
  guarda a presença dos dois controles.

## TK-69 — O lastro obrigatório do modelo conceitual, e o modelo como contrato bilateral

- **Status:** `cancelled` · 2026-09-24 — aberto por ato do dono na validação prática do `P-0741`,
  medindo o modelo do `P-0745` como primeiro caso real da forma publicada.

**Origem.** O dono validou o mecanismo do modelo conceitual **na prática**, e não pela leitura da
documentação: leu o modelo do `P-0745` — o primeiro plano nascido inteiro sob a forma publicada pelo
`P-0741`/`P-0743` — e o reprovou. A reprovação não é do plano nem de quem o escreveu: é do
**conceito de modelo**, que admite elemento sem lastro no enunciado. Os casos citados pelo dono são
**exemplos, não avaliação exaustiva**.

### 1. A restrição de lastro (doutrina)

**Todo objeto, operação e propriedade do modelo tem lastro direto no enunciado do problema e no
prompt de origem do plano.** Elemento sem esse lastro é **requisito secundário** e **não participa
do modelo**.

Não é proibição de executar. O elemento sem lastro pode existir e ser entregue — mas é
**responsabilidade inteira do agente** ideá-lo, executá-lo e garantir que não prejudique o modelo.
Nas palavras do dono: *"Qualquer entrega que não tiver lastro nesses textos são entregas que o
agente supôs que o cliente quer."* O modelo é o contrato com o dono; o resto é meio, e meio é
transparente para o cliente/gerente.

### 2. O modelo é contrato bilateral (doutrina)

**O modelo sempre precisa ser validado pelo cliente/gerente antes de vigorar.** Ato do dono,
2026-09-21: *"Um contrato onde só um dos atores estabelece as condições não é contrato, é
imposição."* Consequência sobre a rota do loop autônomo: a **autoria do modelo não é etapa
desassistida**, e o dono declarou que não acredita ser calibrável agenticamente. É exceção
declarada ao objetivo de execução sem round-trip humano, e a única — vale para o ato de modelo,
não para a execução das tarefas que dele derivam.

### 3. As classes de defeito medidas no modelo do `P-0745`

Tipificação dos exemplos dados pelo dono. Servem de base para violações de `modelo.py check`, e
**não esgotam** a matéria.

| classe | exemplos citados pelo dono |
|---|---|
| sem lastro no enunciado | `guarda da forma antiga`, `documentação pública do kit`, `agregado medido do planejador`, `citações históricas de medida` |
| propriedade promovida a objeto | `norma da unidade de trabalho` (é propriedade de *tarefa*), `gramática do card` (de *card*), `protocolo do planejador` e `especificação do planejador` (de *planejador*) |
| resultado de operação promovido a objeto | `corpus medido da atuação do planejador` |
| conceito promovido a objeto | `modelo de domínio e o papel que o escreve` |
| ator inédito na operação | o fluxo 1.2 faz agir *investigador*, *mantenedor*, *redator da norma*, *autor de papéis* e *redator da especificação* — **nenhum dos cinco existe em 1.1** |
| dosimetria de estado final | 21 estados finais para um enunciado que especificou poucos: *"são os agentes tentarem estipular uma entrega que o cliente nunca pediu"* |

A classe **ator inédito** é integralmente mecânica: todo ator citado em 1.2 tem de existir em 1.1.
Medição de 2026-09-21 sobre o `P-0745`: **zero de cinco**.

### 4. A leitura correta do enunciado do `P-0745` (dono, 2026-09-21)

Registro de uma interpretação que o agente errou nesta sessão, e que o dono corrigiu. O trecho do
prompt de origem — *"agora com o conceito de modelo e do agente model designer estabelecido, assim
como a revisão dos limites de janela e a mudança da orientação de granularidade de tarefa, que não
mais serão atividades atômicas, mas atividades de escopo maior, mantendo a coesão e coerência do
objeto trabalhado"* — **é tudo propriedade**, e descreve **estado**, não pedido de trabalho.

| eixo | estado inicial do framework (antes dos planos citados) | estado final do framework (hoje) |
|---|---|---|
| modelo | sem assistência do model designer e sem o conceito de modelo | existe modelo e existe um model designer |
| janela | restrição de 200k por janela | janela de 1M tokens; tanta restrição deixou de ser relevante |
| granularidade | tarefas atômicas | tarefas maiores, desde que coesas e coerentes |

**O que o plano responde:** como as instruções contidas nesses agentes/skills respondem a essa
mudança de estados — que **já ocorreu**. O plano não produz a mudança; ele faz os instrumentos
alcançá-la.

- **Critério de sucesso:** os instrumentos se utilizam do novo aparato construído.
- **Critério de fracasso:** os instrumentos ainda utilizam os conceitos obsoletos.

Nota de coerência: a *guarda da forma antiga*, rejeitada como objeto por falta de lastro, tem
residência legítima como **aceite** — é a aferição do critério de fracasso, não uma coisa que o
plano trabalha. A regra do dono não perde a guarda; apenas a tira do modelo.

### 5. Consequências a rotear (não decididas aqui)

1. **Revisar o conceito de modelo** e reaplicá-lo ao modelo do `P-0745`, para nova medição do dono.
   Ordem fixada por ele: revisar primeiro, reaplicar depois.
2. **Residências afetadas pela revisão:** `GOVERNANCA.md` §3.2 (norma), a subseção *Modelo de
   domínio (seção do plano)* da skill `diario-de-obras` (gramática), `.claude/tools/modelo.py`
   (violações novas), `.claude/agents/pantonic-model-designer.md` (gate de autoria) e `README.md`
   §8.1 (descrição pública do mecanismo).
3. **Defeito de gate medido no `P-0745`.** O Marco 1 do plano prevê dois desfechos — `go` (sai de
   `blocked`) e `no-go` (`cancelled`, e o `P-0744` volta a `blocked`). O desfecho real foi um
   **terceiro**: modelo reprovado, plano **não** cancelado, modelo a ser reautorado. O gate não
   tem esse ramo; o plano segue `blocked` e o ramo não se inventa na execução (Regra 8).

**Não é escopo deste tíquete:** reescrever o modelo do `P-0745` — todo ato sobre a seção *Modelo
conceitual* é exclusivo do `pantonic-model-designer`.
- **Notas de execução:**
  - 2026-09-24 `cancelled` — absorvido pelo P-0746 (done 7/7, aceito pelo dono em 2026-09-24): lastro obrigatório (LST-T1, LST-T8, LST-T9), decomposição objeto × propriedade (LST-T7), requisitos secundários (LST-T3), V21 no check (LST-T5) e reautoria do P-0745 com o ramo no-go do Marco 1 (LST-T6). O modelo como contrato bilateral segue no TK-70. Resíduo medido: README.md §8.1 tem 0 menções a lastro — roteado ao TK-70

## TK-70 — A vigência bilateral do modelo e a conduta de drift do loop

- **Status:** `cancelled` · 2026-09-25 — aberto no recorte do `P-0746` na versão 3 do modelo dele
  (`F-13`, `DLS-11`).

**Origem:** recorte do `P-0746` na versão 3 do modelo dele (`F-13`, `DLS-11`) · **Decisões que o
vinculam:** `DLS-3` e `DLS-4` do `P-0746`, que deixaram de vincular aquele plano e passaram a
vincular este tíquete.

### 1. Por que está aqui e não no `P-0746`

Ao aceitar a versão 2 do modelo do `P-0746`, o dono fez uma correção: a restrição de atualização
*"foge um pouco do escopo de lastro (…) foi mencionado do enunciado, mas a título de conversação"*,
e o conteúdo dela *"já deve estar abrangido por outra ferramenta"*. O trecho da `## 0` daquele plano
que a sustentava descreve **como a coisa funciona**, não pede trabalho — e portanto não é lastro,
pelo critério que o próprio plano institui.

Pela `DLS-2` do `P-0746`, elemento sem lastro não fica proibido de existir: fica proibido de
participar **daquele** contrato. Pelo invariante `I-4`, achado fora de escopo vira tíquete, nunca
tarefa do plano. Daí este tíquete, com os dois dossiês preservados inteiros.

### 2. A suposição a confirmar antes de executar

O dono supôs que o conteúdo já está abrangido por outra ferramenta. **A medição de 2026-09-21 diz
que não está**, e quem pegar este tíquete confirma antes de escrever qualquer linha:

- `drift` tem **0** ocorrências em `.claude/skills/scrum-master/SKILL.md` (`F-7` do `P-0746`).
- `GOVERNANCA.md:372-375` **define** drift como a variação do modelo em si, distinta de medição, mas
  nenhum texto diz o que acontece com o drift acumulado quando o marco chega.
- `lastro`, `só vigora` e `vigora validado` têm **0** ocorrências em `GOVERNANCA.md` (`F-9`).

Se a confirmação mostrar que outra ferramenta já cobre um dos dois pacotes, **esse pacote fecha por
obsolescência** em vez de entrar na fila — é o desfecho que o dono previu.

### 3. Pacote A — a vigência bilateral do modelo (dossiê da ex-`LST-T2`)

- **Objetivo:** a norma passa a declarar que o modelo só vigora validado pelo cliente ou gerente, e
  que antes do primeiro aceite ele é rascunho substituível no lugar; o `TK-69` §2 é corrigido pela
  `DLS-3`, que revoga a leitura de *"exceção declarada ao objetivo da `EXECUCAO-AUTONOMA`"*.
- **Fundamento:** `DLS-3`; fatos `F-8`, `F-9` do `P-0746`.
- **Camada e fronteira:** doutrina, mais uma correção de registro no diário. Nenhum instrumento,
  nenhum agente.
- **Domínio:** *vigência* — a condição a partir da qual o texto do modelo obriga as partes.
  *Rascunho* — o modelo antes do primeiro aceite: substitui-se no lugar, sem bloco irmão e sem linha
  nova em `### 1.4`.
- **Caso medido acrescentado em 2026-09-22 (`AE-21` do `P-0746`, roteado pelo revisor e confirmado
  pelo consultor):** a norma não tem ramo para **primeira versão recusada e reautorada**, e a
  divergência apareceu **dentro de uma janela, no mesmo papel e no mesmo dia** — a `## 1A` do
  `P-0746` está `pendente` aguardando o Marco 2, e a `## 1` do `P-0745`, reautorada da versão 1
  recusada, está `vigente` aguardando o Marco 3. Mesmo estado de fato, valores opostos no
  cabeçalho. O pacote fecha os dois: o que é rascunho substituível, o que é pendente com bloco
  irmão, e qual valor de `situação` cada um carrega antes do primeiro aceite.
- **Arquivos-alvo:** `GOVERNANCA.md` §3.2 — parágrafo novo antes de **Versão vigente, pendente e
  obsoleta**; `docs/DIARIO_DE_OBRAS.md` › `## TK-69` §2 (correção pela `DLS-3`).
- **Verificação:**
  1. ```
     grep -ci 'só vigora\|vigora validado' GOVERNANCA.md
     ```
     → **≥ 1**. **Medido antes: 0**.
  2. ```
     grep -c 'exceção declarada ao objetivo' docs/DIARIO_DE_OBRAS.md
     ```
     → **0**. **Medido antes: 1** (texto do `TK-69` §2, a revogar).
  3. ```
     python -m pytest tests -q
     ```
     → **≥ 262 passed**.
- **Pronto quando:** as três verificações saem nos valores declarados.

### 4. Pacote B — o drift, o loop e o marco (dossiê da ex-`LST-T4`)

- **Objetivo:** a skill `scrum-master` declara que o loop **carrega** o drift até o marco em vez de
  parar nele ou decidir sobre ele; `GOVERNANCA.md` §4.5 declara que o marco revisa o modelo e
  adjudica o drift — validado, o plano segue; recusado, as tarefas retroagem ao ponto do drift.
- **Fundamento:** `DLS-4`; fatos `F-7`, `F-9` do `P-0746`.
- **Camada e fronteira:** doutrina de marco e skill de orquestração. **Não** redefine o conceito de
  drift, que já existe em `GOVERNANCA.md:372-375` — acrescenta conduta e desfecho.
- **Domínio:** *drift* — a variação do modelo em si, distinta de medição (norma vigente).
  *Retroagir* — as tarefas posteriores ao ponto do drift voltam a `ready`; o plano **não** é
  cancelado.
- **Arquivos-alvo:** `.claude/skills/scrum-master/SKILL.md` — conduta do loop diante de drift;
  `GOVERNANCA.md` §4.5 — o que o marco revisa e os dois desfechos do drift.
- **Verificação:**
  1. ```
     grep -ci 'drift' .claude/skills/scrum-master/SKILL.md
     ```
     → **≥ 2**. **Medido antes: 0**.
  2. ```
     grep -ci 'retroage\|retroagem' GOVERNANCA.md
     ```
     → **≥ 1**. **Medido antes: 0**.
  3. Par presença-ausência: a skill diz que o loop **não** para no drift e **não** decide sobre ele,
     e o texto do marco nomeia os **dois** desfechos.
  4. ```
     python -m pytest tests -q
     ```
     → **≥ 262 passed**.
- **Pronto quando:** as quatro verificações saem nos valores declarados.

### 5. O que este tíquete não faz

- Não toca o modelo do `P-0746` nem o do `P-0745` — a matéria de lastro é daquele plano.
- Não redefine o conceito de drift, que já é norma vigente.
- Não entra na fila do `P-0746`: quem o executa é uma janela própria, depois da confirmação da §2.

**Resíduo recebido do `TK-69` (revisão de pertinência, 2026-09-24).** O `TK-69` fechou absorvido pelo
`P-0746`; a descrição pública do mecanismo em `README.md` §8.1 ficou sem a regra de lastro
(`grep -ci lastro README.md` → **0**). Entra aqui porque este tíquete já reescreve a descrição do
contrato do modelo; a redação pública passa pela skill `redacao-doc`.

**Confirmação da §2, medida em 2026-09-25 na autoria do card.** Metade do tíquete já está coberta
por planos posteriores e fecha por obsolescência, como a §2 previa:

- **Pacote A** — `GOVERNANCA.md` §3.2 já tem *Rascunho antes do Marco 1* (substituição no lugar,
  sem bloco irmão). Falta dizer que o modelo só vigora validado e qual `situação` o rascunho
  carrega (caso `AE-21`). A correção do `TK-69` §2 caiu: o literal *exceção declarada ao
  objetivo* não existe mais fora desta seção.
- **Pacote B** — a conduta do loop já está publicada: `scrum-master` passo 8, rota `modelador` — a
  versão pendente coexiste com a vigente até o marco, sem parar a janela. Falta o desfecho da
  recusa: `retroag` tem `0` ocorrências em `GOVERNANCA.md`.
- **Resíduo do `TK-69`** — `lastro` tem `0` ocorrências em `README.md`.
- **Notas de execução:**
  - 2026-09-25 `cancelled` — absorvido pelo P-0751 — Esgotar o backlog antes da publicação do kit (DEB-2)

### TK-70a — A vigência do modelo, o desfecho do drift recusado e o lastro na descrição pública [Sonnet · esforço low · classe redacao]

- **Status:** `cancelled` · 2026-09-25
- **Objetivo:** `GOVERNANCA.md` §3.2 passa a dizer que o modelo só vigora depois de validado pelo
  dono — o rascunho carrega `situação: vigente` por forma, não por vigência — e o que acontece com o
  que foi entregue sob uma versão pendente recusada; `README.md` §8.1 passa a dizer ao leitor que
  todo elemento do modelo tem lastro no pedido.
- **Fundamento:** `DLS-3` e `DLS-4` do `P-0746`; `AE-21` daquele plano; confirmação acima.
- **Arquivos-alvo:**
  - `GOVERNANCA.md`
  - `README.md`
- **Passos:** substituir cada **Texto atual** pelo **Texto novo** de mesmo número; rodar as
  Verificações.
- **Texto atual 1** (`GOVERNANCA.md` §3.2, *Rascunho antes do Marco 1*, uma ocorrência):

  ~~~~
  a versão 1 **no lugar**, sem bloco irmão e sem linha nova no registro. Versionar só começa no
  Marco 1.
  ~~~~

- **Texto novo 1** (as quebras são as do bloco):

  ~~~~
  a versão 1 **no lugar**, sem bloco irmão e sem linha nova no registro. Versionar só começa no
  Marco 1. O rascunho carrega `situação: vigente` porque essa é a forma da `## 1`, não porque
  vigore: **o modelo só vigora depois de validado pelo dono**, e antes disso não obriga nenhuma das
  partes. Rascunho recusado e reescrito continua rascunho — substitui-se no lugar —, e
  `situação: pendente` só existe na `## 1A`, depois do Marco 1.
  ~~~~

- **Texto atual 2** (`GOVERNANCA.md` §3.2, *Versão vigente, pendente e obsoleta*, uma ocorrência):

  ~~~~
  registra qual versão ficou obsoleta, quando e por aceite de qual versão. Recusada, a pendente é
  **eliminada** e a vigente permanece, sem marca.
  ~~~~

- **Texto novo 2** (as quebras são as do bloco):

  ~~~~
  registra qual versão ficou obsoleta, quando e por aceite de qual versão. Recusada, a pendente é
  **eliminada** e a vigente permanece, sem marca — e o plano **retroage ao ponto do drift**: o que
  foi entregue sob a versão recusada é refeito, sob a vigente, por card corretivo da operação
  afetada, porque `done` é terminal e não se reabre. O plano não é cancelado.
  ~~~~

- **Texto atual 3** (`README.md` §8.1, uma ocorrência):

  ~~~~
  O modelo **versiona, não se reescreve**: quando uma decisão muda o que o plano entrega, a versão
  ~~~~

- **Texto novo 3** (as quebras são as do bloco; a linha em branco separa parágrafos):

  ~~~~
  Todo elemento do modelo tem **lastro** no pedido: um trecho do enunciado que o justifica. O que o
  pedido não traz não entra no modelo — se o agente o julga necessário, entrega-o como requisito
  secundário, declarado numa seção à parte e sob a responsabilidade inteira dele.

  O modelo **versiona, não se reescreve**: quando uma decisão muda o que o plano entrega, a versão
  ~~~~

- **Verificação:** no PowerShell, na raiz; **antes** medido em 2026-09-25.
  1. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'o modelo só vigora depois de validado pelo dono').Count` — antes `0`, depois `1`
  2. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'retroage ao ponto do drift').Count` — antes `0`, depois `1`
  3. `(Select-String -Path README.md -SimpleMatch 'Todo elemento do modelo tem **lastro** no pedido').Count` — antes `0`, depois `1`
  4. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho.
- **Pronto quando:** as três contagens saem nos valores de depois e a suíte segue verde.
- **Não fazer:** não tocar `.claude/skills/scrum-master/SKILL.md` (o Pacote B já está lá); não
  editar modelo de plano nenhum; não editar a seção do `TK-69`.
- **Contingências:**
  - se um **Texto atual** não for encontrado exatamente uma vez → parar e sinalizar `blocked`
    razão `premissa`, citando o número do bloco.
- **Notas de execução:**
  - 2026-09-25 `cancelled` — absorvido pelo P-0751 como EBK-T8 (DEB-2)

## TK-71 — A `V2` e a tarefa que não materializa operação

- **Status:** `cancelled` · 2026-09-25 — aberto pelo consultor de plano do `P-0746` no quinto
  escalonamento da janela (`AE-15`, `DLS-18`), para que a rota do recorte não fique órfã.

**Origem:** recorte do `P-0746` em 2026-09-22 · **Decisão que o vincula:** `DLS-18` do `P-0746`.

### 1. Por que está aqui e não no `P-0746`

O modelo do `P-0746` pedia, na `OP-5`, que a conferência automática *"reconheça a tarefa que declara
não materializar operação por ser requisito não fundamental"*. Dois executores frios independentes
pararam na `LST-T5` sob `G-NOASK` — o segundo exatamente aqui — porque **o referente não existe**:
a gramática publicada define uma única forma para o campo `Operação do modelo` do card, e nenhuma
forma alternativa de declaração. Medido em 2026-09-22: `requisito não fundamental` tem **0**
ocorrências em `.claude/skills/diario-de-obras/SKILL.md` e **0** em `GOVERNANCA.md`.

Pela regra que o próprio `P-0746` institui, a cláusula não podia estar no modelo: o enunciado
(`## 0` daquele plano) fala de **elemento** sem lastro — *"podem entrar como requisitos
não-fundamentais, mas são de responsabilidade inteira do agente idear, executar e garantir"* —, que
é o lastro da `OP-4` e se materializou na seção nomeada do plano (`LST-T3`). A metade `V2` desce do
`F-10`, que é **medição do instrumento**, e medição de instrumento não é âncora. Saiu do modelo por
emenda acumulada na versão 4 pendente, que o Marco 2 adjudica.

### 2. Pacote 1 — a categoria existe?

Antes de construir qualquer coisa, decidir: **uma tarefa pode entregar requisito secundário sem
materializar operação do modelo?** Hoje nenhum plano vivo tem o caso — a `LST-T0` do `P-0746`, que
o teria, foi dissolvida (`DLS-10` daquele plano), e a seção `## 2` dele lista quatro requisitos
secundários, nenhum deles um card. **Pacote sem caso fecha por obsolescência**, como o `TK-70`
prevê para si.

### 3. Pacote 2 — se existir, a ordem é gramática, depois parser

Publicar a forma do campo na subseção *Modelo de domínio (seção do plano)* da skill
`diario-de-obras` — o rótulo pelo qual um card se declara não fundamental — e **só então** ensinar
a `V2` a reconhecê-la, com par presença-ausência sobre fixture: acusa quem omite o campo, não acusa
quem o declara. A ordem inversa é o defeito que o `F-17` do `P-0746` mediu: forma nova antes de o
parser aprender passa em silêncio.

### 4. O que este tíquete não faz

- Não reabre a `LST-T5` do `P-0746`, que entrega a `V21` e nada mais.
- Não toca o modelo do `P-0746` — a emenda que retira a cláusula já foi devolvida ao modelador.
- Não altera a `V2` existente, que segue acusando tarefa sem o campo `Operação do modelo`.
- **Notas de execução:**
  - 2026-09-25 `cancelled` — cancelado por obsolescência, pelo critério do próprio tíquete (§2): nenhum plano vivo tem o caso — medido em 2026-09-25, todos os planos do índice em estado terminal

## TK-72 — A régua de autoria de card do kit

- **Status:** `cancelled` · 2026-09-25 — aberto pelo consultor de plano do `P-0746` no escalonamento de
  consolidação da janela, com quatro achados medidos da mesma família.

**Origem:** janela do `P-0746` (2026-09-21/22) · **Achados:** `AE-2`/`DLS-14`, `AE-11`, `AE-19`,
`AE-20` daquele plano.

### 1. O que este tíquete decide

Como se escreve um card para um executor frio que **não decide, não pergunta e não muda a rota**.
Quatro pacotes, todos com caso medido na mesma janela, e todos na mesma residência: `GOVERNANCA.md`
§3 (planejamento) e a gramática do card na skill `diario-de-obras`.

### 2. Pacote 1 — aceite de card de `redacao` é recorte de literal, não contagem

`DLS-14` do `P-0746`. Caso medido: a linha de aceite da `LST-T1` era `grep -ci 'lastro' ≥ 3` e
sairia **verde com três menções decorativas**; o laudo aprovou com ressalva 88% e apontou o defeito
de régua, não de texto. A forma que funcionou nas quatro tarefas seguintes: o card **fixa o literal
verbatim**, a verificação é `grep -cF`, e onde há texto a substituir, o par presença-ausência mede
o desaparecimento do literal antigo.

### 3. Pacote 2 — card que recebe rota de achado declara-a no próprio dossiê

`AE-11` do `P-0746`. Caso medido: o `AE-9` roteava para a `LST-T8`, cujo card declarava a matéria
**fora do escopo**; a tarefa fechou sem fechar a rota, e o vão só apareceu no laudo seguinte. Regra
a publicar: rota de achado só se declara para card que a aceite no dossiê — e rota que sai do plano
precisa de tíquete aberto no mesmo ato, não de promessa no relatório.

### 4. Pacote 3 — `Arquivos-alvo` fecha o efeito colateral obrigatório

`AE-19` do `P-0746`. Caso medido: a `LST-T6` mandava reautorar o modelo do `P-0745` e listava só o
arquivo do plano; reautorar obriga a reescrever o campo `Operação do modelo` dos **sete** cards, ou
a `V4`/`V14` disparam. O executor absorveu e declarou — mas o card obrigava a decidir. Regra:
entrega cujo efeito colateral é mecânico e previsível tem esse efeito **no `Arquivos-alvo`**.

### 5. Pacote 4 — verificação sem valor esperado não é verificação

`AE-20` do `P-0746`, mesma família do `DM-12` do `P-0740` (*comando de aceite não se deduz, se
roda*). Caso medido: a Verificação 4 da `LST-T6` era `grep -c 'cancelled'` **sem número**; a única
leitura inequívoca era `0`, e o executor teve de inferi-la. Regra: toda verificação carrega o valor
esperado **e** o medido antes.

### 6. O que este tíquete não faz

- Não reabre card algum do `P-0746`, que fechou `7/7`.
- Não muda a rubrica de revisão: o que se corrige é a autoria, não o julgamento.

### 7. Insumo do veredito dos procedimentos, roteado pelo consultor do `P-0747` em 2026-09-23

Fonte: `docs/plans/_VEREDITO-procedimentos-2026-09-22.md`, roteado por `DCS-25` do `P-0747`. Quatro
pacotes novos, todos com caso medido na sessão de planejamento do `P-0747`; nenhum abre card
naquele plano (capacidade, não término — spec do consultor §2).

- **Pacote 5 — o contrato copiado no card se limita ao que este card precisa** (veredito §3.4).
  Caso medido: o contrato do objeto de escopo do `P-0747` tem ~600 palavras — a partição de 47
  residências entre oito operações, as exclusões e os intocados — e foi copiado em sete cards ao
  lado dos contratos dos outros quatro objetos: 3.761 caracteres por card, e a `CON-T3` com 259
  linhas para 11 substituições literais. Regra a publicar em `GOVERNANCA.md` §3.2 (*O contrato
  chega ao card*) e na gramática do card: `precisa de:` copia o contrato do objeto **sem a
  partição alheia** — só o que a operação do card usa —, e toda lista de residências vive por
  **ponteiro** ao fato da `## 2` que é a residência única dela. Medido em 2026-09-23:
  `modelo.py check` afere em `V14` só a presença do sub-bullet do contrato, não o texto — a regra
  não exige mudança de instrumento.
- **Pacote 6 — censo de superfície é grep literal com padrão e contagem, e o planejador pode
  re-rodá-lo** (veredito §3.1). Caso medido: a pergunta semântica aos scouts devolveu 22
  residências; o grep do próprio planejador achou 43; a partição por linha, 47 — duas das três
  reautorias do modelo nasceram desse buraco. Regra a publicar no `pantonic-planner`: (i) para
  toda lista de residências, o scout devolve o **padrão de grep e a contagem** que rodou, e o fato
  da `## 2` publica os dois; (ii) a regra de uso único do `Bash` ganha a exceção nomeada *grep de
  verificação de superfície, com o padrão publicado no fato* — foi esse grep que salvou o plano.
- **Pacote 7 — o ensaio dos cards em árvore temporária é o modo normal da Fase 4** (veredito
  §3.8). Caso medido: primeira sessão em que todo literal de aceite publicado foi rodado antes e
  depois, inclusive o gate de drift ficando vermelho no meio da `CON-T8` e verde depois; 333k
  tokens e 38 min. Regra a publicar no `pantonic-planner`: a Fase 4 aplica os cards em sequência
  numa cópia da árvore e mede cada linha de `Verificação` antes e depois; o número publicado é o
  medido. É o `DM-12` do `P-0740` levado à autoria, não só à execução.
- **Pacote 8 — medida a fazer antes de a doutrina escolher entre retomada por mensagem e
  invocação fria** (veredito §3.7). O planejador foi retomado quatro vezes por mensagem com o
  contexto intacto, mas os intervalos passaram de 5 minutos e o cache de subagente expirou — o
  custo em dólares não foi medido. A sonda da `CON-T7` do `P-0747` (`%TEMP%\claude\sonda_p0747.py`,
  filtro por `argv[1]`) serve à medida trocando o `agentType` e o filtro da primeira linha.

### 8. Pacotes 9 e 10 — absorvidos do `TK-80` (revisão de pertinência, 2026-09-24)

Mesma família (régua de autoria de card), residência vizinha (`.claude/agents/pantonic-planner.md`
e a rubrica de criação de tarefa). O enunciado e os casos medidos ficam na seção `## TK-80`, que
segue como registro: **Pacote 9** — valor medido de aceite nunca viaja em `pendencia=` (`AE-13` do
`P-0748`); **Pacote 10** — o rótulo do card de investigação é um que o parser conhece (`AE-1` do
`P-0748`, parte de doutrina).

### 9. Pacotes 11 e 12 — roteados pelo consultor do `P-0749` (acionamento 4, 2026-09-25)

Fonte: `AE-5` (a) e (c) do `P-0749`, laudo da `SAN-T6` (ressalva 88).

- **Pacote 11 — o veredito do dono é gate do marco, não critério de pronto.** Caso medido: o
  *Pronto quando* da `SAN-T6` citava a Verificação 4 (veredito do dono, aferição manual), que o
  revisor não pode aferir no ato; a revisão saiu `criterio-de-pronto=parcial` com a entrega fiel.
  Regra: card que precisa do veredito do dono o devolve no passo final e o leva ao relatório de
  encerramento; o *Pronto quando* só cita verificação que o revisor roda.
- **Pacote 12 — troca literal de redação declara a quebra de linha do texto novo.** Caso medido: a
  `M1` da `SAN-T6` publicou ~200 colunas numa linha sem dizer se o parágrafo reflui, e o executor
  refluiu três linhas por conta própria. Regra: o literal marca a quebra (`↵`) ou declara "sem
  quebra nova e sem refluxo".

### 10. Reconciliação e cards (2026-09-25, *Tíquete nasce executável*)

A residência que funciona para as regras de autoria é a Fase 4 do `pantonic-planner`, itens 1 a 12,
que já carrega parte dos pacotes; o que falta entra ali como item 13, e o consultor passa a
aplicá-la. Medido na autoria:

| pacote | estado em 2026-09-25 | card |
|---|---|---|
| 1, 3, 9, 11, 12, e as regras de autoria do `TK-55` (premissa medida, propriedade e não técnica, instrumento calcula, menção não colhível) | sem residência | `TK-72a` |
| 2 | metade publicada: rota que sai do plano abre tíquete com card (skill `diario-de-obras`, "Tíquete nasce executável"); falta a metade do card que aceita a rota | `TK-72a` |
| 4 | publicado: `pantonic-planner` Fase 4, item 12 (v) — os dois valores, antes e depois | sem ação |
| 5 | sem residência (`GOVERNANCA.md` §3.2, *O contrato chega ao card*) | `TK-72a` |
| 6, 7 | sem residência | `TK-72b` |
| 8 | medida não feita; a sonda existe (`%TEMP%\claude\sonda_p0747.py`, medido em 2026-09-25) | `TK-72c` |
| 10 | publicado: `pantonic-planner`, rótulo `Pronto quando (o fato que tem de existir ao final)` do card de investigação | sem ação |
| caso do `TK-68a`: literal com `### ` na coluna 0 cortou o card | sem residência | `TK-72a` |
- **Notas de execução:**
  - 2026-09-25 `cancelled` — absorvido pelo P-0751 — Esgotar o backlog antes da publicação do kit (DEB-2)

### TK-72a — A régua de autoria do card, segunda leva [Sonnet · esforço medium · classe redacao]

- **Status:** `cancelled` · 2026-09-25
- **Objetivo:** a Fase 4 do `pantonic-planner` ganha o item 13 com os dez critérios de autoria que
  faltam; o `pantonic-consultant` passa a aplicar os itens 11 a 13 a todo card que escreve; e
  `GOVERNANCA.md` §3.2 limita o contrato copiado no card ao que a operação dele usa.
- **Fundamento:** pacotes 1, 2, 3, 5, 9, 11 e 12 deste tíquete; itens nomeados do `TK-55`
  (escalonamentos 3 a 6 de 2026-09-20); caso do `TK-68a` (2026-09-25).
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-planner.md`
  - `.claude/agents/pantonic-consultant.md`
  - `GOVERNANCA.md`
- **Passos:** substituir cada **Texto atual** pelo **Texto novo** de mesmo número, no arquivo
  indicado; rodar as Verificações.
- **Texto atual 1** (`.claude/agents/pantonic-planner.md`, fim do item 12 da Fase 4, uma ocorrência):

  ~~~~
     construção (2026-09-19, `AE-19`).
  ~~~~

- **Texto novo 1** (as quebras são as do bloco; a linha em branco separa os itens):

  ~~~~
     construção (2026-09-19, `AE-19`).

  13. **Régua de autoria, segunda leva** — dez critérios medidos em janelas de execução de
     2026-09-20 a 2026-09-25; valem para todo card, de plano ou de tíquete, e para o
     `pantonic-consultant` quando ele escreve card:
     (i) **O card fixa a propriedade e a medida; a técnica é do executor** — o card diz o que tem de
     ser verdade ao final e o comando que o prova, e só prescreve o *como* quando o como é a própria
     propriedade.
     (ii) **Premissa citada se mede, e pelo instrumento quando ele sabe medir** — gramática,
     domínio, população e contagem citados no card se medem antes de publicar; número que um
     instrumento do kit calcula vem do instrumento, nunca de varredura que conte outra coisa
     (`grep -c` conta linha, não ocorrência).
     (iii) **Aceite de redação é recorte de literal** — o card fixa o texto verbatim e a verificação
     conta o literal (`Select-String -SimpleMatch`); onde há texto a substituir, conta também o
     literal antigo sumir. Contar palavra solta aprova menção decorativa.
     (iv) **O literal declara a quebra de linha** — cada bloco diz "as quebras são as do bloco" ou
     "sem quebra nova e sem refluxo".
     (v) **Literal com cabeçalho markdown entra recuado** — linha que começa com `## ` ou `### ` na
     coluna 0 encerra o card para o `rdo.py` e o `review_evidence.py`; todo bloco literal do card
     vai recuado dois espaços.
     (vi) **`Arquivos-alvo` fecha o efeito colateral mecânico** — entrega cujo efeito em outro
     arquivo é obrigatório e previsível lista esse arquivo; o executor não decide absorvê-lo.
     (vii) **Rota de achado só vai para card que a aceita** — o achado roteado a um card está no
     dossiê dele; rota que sai do plano abre tíquete no mesmo ato, já com o card (skill
     `diario-de-obras`, "Tíquete nasce executável").
     (viii) **Valor medido de aceite nunca viaja na linha de retorno** — `pendencia=` é só para
     pendência; a medida vai para a evidência que o revisor gera.
     (ix) **O veredito do dono é gate do marco, não critério de pronto** — `Pronto quando` só cita
     verificação que o revisor roda; card que precisa do veredito do dono o leva ao relatório de
     encerramento.
     (x) **Menção de referência quebrada vai em forma que o lint não colhe** — reproduzir a citação
     quebrada na forma colhível, para falar dela, cria mais uma ocorrência.
  ~~~~

- **Texto atual 2** (`.claude/agents/pantonic-consultant.md`, uma ocorrência; sem quebra nova):

  ~~~~
  no caso que a skill `diario-de-obras` determina em "Tíquete nasce executável".
  ~~~~

- **Texto novo 2:**

  ~~~~
  no caso que a skill `diario-de-obras` determina em "Tíquete nasce executável". Todo card que você escreve passa pelos itens 11 a 13 da Fase 4 do `pantonic-planner` (`.claude/agents/pantonic-planner.md`).
  ~~~~

- **Texto atual 3** (`GOVERNANCA.md` §3.2, *O contrato chega ao card*, uma ocorrência):

  ~~~~
  estágio está e do que precisa.
  ~~~~

- **Texto novo 3** (as quebras são as do bloco):

  ~~~~
  estágio está e do que precisa. O contrato copiado se limita ao que **esta** operação usa: a
  partição que é de outra operação fica fora, e lista de residências entra por ponteiro ao fato da
  `## 2` que é a residência única dela, nunca copiada card a card.
  ~~~~

- **Verificação:** no PowerShell, na raiz; **antes** medido em 2026-09-25.
  1. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'Régua de autoria, segunda leva').Count` — antes `0`, depois `1`
  2. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'Literal com cabeçalho markdown entra recuado').Count` — antes `0`, depois `1`
  3. `(Select-String -Path .claude/agents/pantonic-consultant.md -SimpleMatch 'itens 11 a 13 da Fase 4').Count` — antes `0`, depois `1`
  4. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'O contrato copiado se limita ao que').Count` — antes `0`, depois `1`
  5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate` e `-Mode check-drift` → exit `0`
  6. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho.
- **Pronto quando:** as quatro contagens saem nos valores de depois e o kit segue válido e sem drift.
- **Não fazer:** não renumerar nem reescrever os itens 1 a 12 da Fase 4; não tocar
  `docs/RUBRICA_DE_REVISAO.md`.
- **Contingências:**
  - se um **Texto atual** não for encontrado exatamente uma vez → parar e sinalizar `blocked`
    razão `premissa`, citando o número do bloco.
- **Notas de execução:**
  - 2026-09-25 `cancelled` — absorvido pelo P-0751 como EBK-T10 (DEB-2)

### TK-72b — O planejador publica o grep da superfície e ensaia os cards antes de gravar [Sonnet · esforço low · classe redacao]

- **Status:** `cancelled` · 2026-09-25
- **Depende de:** `TK-72a`
- **Objetivo:** o `pantonic-planner` passa a ter dois usos para o `Bash` — o comando de aceite e o
  grep de verificação de superfície, publicado com padrão e contagem —, e a Fase 4 ganha o item 14,
  o ensaio dos cards numa cópia da árvore.
- **Fundamento:** pacotes 6 e 7 deste tíquete.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-planner.md`
- **Passos:** substituir cada **Texto atual** pelo **Texto novo** de mesmo número; rodar as
  Verificações.
- **Texto atual 1** (uma ocorrência):

  ~~~~
  única matéria-prima é decisão; seu único produto é plano fechado. Você **tem `Bash`**, e ele
  serve a **um** uso: rodar o comando de aceite que você mesmo vai publicar num card, antes de
  publicá-lo — não é licença para levantamento próprio.
  ~~~~

- **Texto novo 1** (as quebras são as do bloco):

  ~~~~
  única matéria-prima é decisão; seu único produto é plano fechado. Você **tem `Bash`**, e ele
  serve a **dois** usos: rodar o comando de aceite que você mesmo vai publicar num card, antes de
  publicá-lo, e re-rodar o **grep de verificação de superfície** que um fato da `## 2` publica — não
  é licença para levantamento próprio. Toda lista de residências que um fato publica traz o padrão
  de grep que a produziu e a contagem que ele deu: peça ao `pantonic-scout` o padrão e a contagem,
  não só a lista, e re-rode o padrão antes de gravar.
  ~~~~

- **Texto atual 2** (fim do item 13 da Fase 4, escrito pelo `TK-72a`; uma ocorrência):

  ~~~~
     quebrada na forma colhível, para falar dela, cria mais uma ocorrência.
  ~~~~

- **Texto novo 2** (as quebras são as do bloco; a linha em branco separa os itens):

  ~~~~
     quebrada na forma colhível, para falar dela, cria mais uma ocorrência.

  14. **Ensaio dos cards em árvore temporária** — antes de gravar, aplique os cards em sequência
     numa cópia da árvore fora do repositório e rode cada linha de `Verificação` antes e depois de
     cada card; o valor publicado é o medido no ensaio. Linha que dá o mesmo valor antes e depois
     não discrimina e volta à autoria.
  ~~~~

- **Verificação:** no PowerShell, na raiz; **antes** medido em 2026-09-25 (itens 1 e 2) e depois do
  `TK-72a` (item 3).
  1. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'serve a **dois** usos').Count` — antes `0`, depois `1`
  2. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'serve a **um** uso').Count` — antes `1`, depois `0`
  3. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'Ensaio dos cards em árvore temporária').Count` — antes `0`, depois `1`
  4. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate` → exit `0`
  5. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho.
- **Pronto quando:** as três contagens saem nos valores de depois e o kit segue válido.
- **Não fazer:** não tocar `.claude/agents/pantonic-scout.md`; não renumerar itens da Fase 4.
- **Contingências:**
  - se um **Texto atual** não for encontrado exatamente uma vez → parar e sinalizar `blocked`
    razão `premissa`, citando o número do bloco.
- **Notas de execução:**
  - 2026-09-25 `cancelled` — absorvido pelo P-0751 como EBK-T11 (DEB-2)

### TK-72c — Quanto custa retomar o planejador por mensagem [Sonnet · esforço high · classe investigacao]

- **Status:** `cancelled` · 2026-09-25
- **Objetivo:** medir, nos transcripts do `pantonic-planner` da sessão de planejamento do `P-0747`,
  o custo de cada retomada por mensagem e o de cada invocação fria do mesmo papel; publicar a
  medida em `docs/CUSTO_DO_PICKUP.md` e aplicar a `GOVERNANCA.md` a regra que o resultado determina.
- **Fundamento:** pacote 8 deste tíquete.
- **Arquivos-alvo:**
  - `docs/CUSTO_DO_PICKUP.md`
  - `GOVERNANCA.md`
- **Método de sondagem:**
  1. **Corpus fechado:** os arquivos `agent-*.meta.json` sob
     `C:\Users\panta\.claude\projects\d--workspaces-PantonicApp\*\subagents\` com `agentType` igual
     a `pantonic-planner` e cujo `.jsonl` irmão cita `P-0747` na primeira linha.
  2. **Segmento:** cada trecho do `.jsonl` que começa numa mensagem do tipo `user` vinda de fora do
     agente (a invocação ou uma retomada por mensagem) e vai até a próxima. O primeiro segmento de
     cada agente é a **invocação fria**; os seguintes são **retomadas**.
  3. **Métrica por segmento:** soma de `input_tokens`, `output_tokens`, `cache_read_input_tokens` e
     `cache_creation_input_tokens` das mensagens `assistant` com `message.id` distinto, e o custo
     com os preços da sonda `%TEMP%\claude\sonda_p0747.py` (5, 25, 0,5 e 6,25 dólares por milhão, na
     ordem); mais o intervalo, em minutos, desde o fim do segmento anterior. Adaptar a sonda
     trocando `pantonic-consultant` por `pantonic-planner`, o filtro por `P-0747` e somando por
     segmento. Nenhum texto de mensagem entra no contexto: só chaves, contagens e datas.
  4. **Agregado que volta:** no máximo 20 linhas — por grupo (fria, retomada): `n`, média, mínimo e
     máximo do custo, e o intervalo de cada retomada.
  5. **O que cada resultado dispara:** média das retomadas **menor** que a das invocações frias →
     entra em `GOVERNANCA.md` o **Texto novo A**; **igual ou maior** → o **Texto novo B**; nenhuma
     retomada no corpus → nenhum dos dois, e a seção publica "não mensurável neste corpus".
- **Texto atual 1** (`GOVERNANCA.md` §3, uma ocorrência):

  ~~~~
    execução inline a abrir um subagente.
  ~~~~

- **Texto novo A** (as quebras são as do bloco):

  ~~~~
    execução inline a abrir um subagente.
  - **Rodada de replanejamento retoma o mesmo planejador por mensagem**, sem abrir instância fria:
    a retomada custou menos que a invocação fria do mesmo papel (`docs/CUSTO_DO_PICKUP.md`, seção
    *Retomada do planejador por mensagem*).
  ~~~~

- **Texto novo B** (as quebras são as do bloco):

  ~~~~
    execução inline a abrir um subagente.
  - **Rodada de replanejamento abre instância fria do planejador**, sem retomá-lo por mensagem: a
    retomada custou o mesmo ou mais que a invocação fria do mesmo papel, porque o cache do
    subagente expira entre as rodadas (`docs/CUSTO_DO_PICKUP.md`, seção *Retomada do planejador
    por mensagem*).
  ~~~~

- **Pronto quando (o fato que tem de existir ao final):** `docs/CUSTO_DO_PICKUP.md` tem uma seção
  nova, com o próximo número da sequência, titulada `Retomada do planejador por mensagem × invocação
  fria`, com a data, o corpus, a regra de enumeração dos segmentos, o agregado do passo 4 e o
  desfecho do passo 5; e `GOVERNANCA.md` carrega exatamente o texto que o desfecho determinou.
- **Verificação:**
  1. `(Select-String -Path docs/CUSTO_DO_PICKUP.md -SimpleMatch 'Retomada do planejador por mensagem × invocação fria').Count` — antes `0`, depois `1`
  2. `(Select-String -Path GOVERNANCA.md -Pattern 'Rodada de replanejamento (retoma|abre instância fria)').Count` — antes `0`, depois `1` (ou `0`, com o desfecho "não mensurável" publicado)
  3. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho.
- **Não fazer:** não ler conteúdo de mensagem dos transcripts; não medir outro papel; não mudar o
  `pantonic-planner`.
- **Contingências:**
  - se a sonda não existir no despacho → escrever a soma direto sobre o corpus do passo 1, com as
    mesmas chaves e preços.
- **Notas de execução:**
  - 2026-09-25 `cancelled` — absorvido pelo P-0751 como EBK-T13 (DEB-2)

## TK-73 — A oração da operação: recorte e sujeito

- **Status:** `cancelled` · 2026-09-25 — aberto pelo consultor de plano do `P-0746`. **O Pacote 2 não se
  executa sem a resposta do dono à pendência `AE-18`**, que vai ao relatório de encerramento
  daquela janela.

**Origem:** janela do `P-0746` (2026-09-21/22) · **Achados:** `AE-4`, `AE-15`, `AE-18`; fatos `F-14`,
`F-19`, decisões `DLS-13`, `DLS-18` daquele plano.

### 1. Por que existe

A `OP-5` do `P-0746` foi escrita com **três orações** e cada uma tinha lastro próprio: acusar
elemento sem lastro (tem), acusar ator inédito (inexequível, `F-14`), reconhecer tarefa não
fundamental (sem lastro, `F-19`). As duas defeituosas **só apareceram na implementação** — a dois
executores frios e cinco escalonamentos de distância do Marco 1, que é onde deveriam ter sido
apanhadas. Custo medido da janela: cinco escalonamentos `B1`, dois `blocked motivo=premissa` no
mesmo card.

### 2. Pacote 1 — uma oração por operação

Publicar em `GOVERNANCA.md` §3.2 e na gramática: **operação com mais de uma oração é operação mal
recortada** — cada oração tem lastro próprio e, portanto, é operação própria, com a sua propriedade
e o seu card. Guarda: o Marco 1 lê operação a operação contra a `## 0`; e avaliar se o `check` pode
acusar mecanicamente a oração composta (conjunção coordenada no texto da operação) sem produzir
falso positivo.

### 3. Pacote 2 — o sujeito da operação, e o critério de ator inédito

**Bloqueado na decisão do dono (`AE-18`).** O dono tipificou *"ator inédito na operação"* no
`TK-69` §3 como classe **integralmente mecânica** e mediu 0 de 5 no `P-0745`. Medido depois, no
`P-0746`: a regra ao pé da letra acusa **6 dos 7** atores do `P-0743` — modelo que ele **aceitou** —
e **4 dos 4** do `P-0746`; o modelo reautorado do `P-0745` tem **5 de 5**. Ou seja, ela reprova todo
o acervo, inclusive o que passou. Caminhos a avaliar quando a decisão vier:
**(a)** manter a dispensa — o vínculo entre fluxo e tabela já é aferido pela `V5`/`V16` (objeto e
propriedade citados em `precisa de:`/`altera:` existem) e pelo lastro por elemento;
**(b)** proibir **sujeito-ator** no texto da operação — a operação passa a dizer o que muda, não
quem age, o que é mecanicamente aferível e vale para o acervo inteiro, ao custo de reescrever os
modelos vivos;
**(c)** outra formulação que discrimine, se a medição mostrar uma.

### 4. O que este tíquete não faz

- Não reabre o modelo do `P-0745` nem o do `P-0746` antes dos Marcos 2 e 3.
- Não decide sozinho o Pacote 2: a classe é do dono, e foi ele quem a nomeou.

### 5. Medido na autoria dos cards (2026-09-25)

- **Guarda mecânica do Pacote 1:** das **52** operações `- **OP-<n>** — …` do acervo
  (`docs/plans/*.md` e `docs/plans/*/plano.md`), **50** contêm ` e `. Uma guarda por conjunção
  acusaria quase todas: fica o Marco 1 como guarda, e o `check` não muda.
- **Custo da opção (b) do Pacote 2:** nenhum plano do índice está vivo — todos terminais —, e a
  doutrina não migra plano terminal (`GOVERNANCA.md` §3.2, *Retroatividade*). Proibir sujeito-ator
  já não obriga a reescrever modelo nenhum: vale para os planos que nascerem.
- **Notas de execução:**
  - 2026-09-25 `cancelled` — absorvido pelo P-0751 — Esgotar o backlog antes da publicação do kit (DEB-2)

### TK-73a — Uma operação, uma oração [Sonnet · esforço low · classe redacao]

- **Status:** `cancelled` · 2026-09-25
- **Objetivo:** `GOVERNANCA.md` §3.2 e a skill `diario-de-obras` passam a dizer que operação escrita
  com mais de uma oração é operação mal recortada, que cada oração vira operação própria, e que a
  guarda é o marco.
- **Fundamento:** Pacote 1 deste tíquete; medição da §5.
- **Arquivos-alvo:**
  - `GOVERNANCA.md`
  - `.claude/skills/diario-de-obras/SKILL.md`
- **Passos:** substituir cada **Texto atual** pelo **Texto novo** de mesmo número; rodar as
  Verificações.
- **Texto atual 1** (`GOVERNANCA.md` §3.2, *Objeto, operação e propriedade*, uma ocorrência):

  ~~~~
  identificam-se as propriedades, e deles caem por decomposição — não por intuição.
  ~~~~

- **Texto novo 1** (as quebras são as do bloco):

  ~~~~
  identificam-se as propriedades, e deles caem por decomposição — não por intuição.
  **Uma operação, uma oração.** Operação escrita com mais de uma oração — cada uma com o seu verbo
  e o seu lastro — é operação mal recortada: cada oração vira operação própria, com a sua
  propriedade e o seu card. A guarda é o Marco 1, que lê operação a operação contra a `## 0`;
  nenhuma validação a apanha, porque a conjunção também aparece dentro de uma oração só.
  ~~~~

- **Texto atual 2** (`.claude/skills/diario-de-obras/SKILL.md`, *Objeto e propriedade, na
  decomposição*, uma ocorrência; sem quebra nova):

  ~~~~
  marco.
  ~~~~

- **Texto novo 2:**

  ~~~~
  marco. Operação escrita com mais de uma oração é operação mal recortada: cada oração vira operação própria, e a guarda também é o marco.
  ~~~~

- **Verificação:** no PowerShell, na raiz; **antes** medido em 2026-09-25.
  1. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'Uma operação, uma oração.').Count` — antes `0`, depois `1`
  2. `(Select-String -Path .claude/skills/diario-de-obras/SKILL.md -SimpleMatch 'Operação escrita com mais de uma oração').Count` — antes `0`, depois `1`
  3. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate` → exit `0`
  4. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho.
- **Pronto quando:** as duas contagens saem nos valores de depois.
- **Não fazer:** não mudar `modelo.py` nem o `check`; não editar modelo de plano nenhum.
- **Contingências:**
  - se um **Texto atual** não for encontrado exatamente uma vez → parar e sinalizar `blocked`
    razão `premissa`, citando o número do bloco (o **Texto atual 2** é a linha que termina o
    parágrafo *Objeto e propriedade, na decomposição*, que hoje é exatamente `marco.`).

### 6. Ato do dono (2026-09-25) — o Pacote 2 não existe

Verbatim: *"Essa regra não existe. É uma regra inferida de exemplo. Não é uma regra geral. Eu não
tenho nada a decidir sobre uma regra mal interpretada."* Os casos da §3 do `TK-69` são **exemplos**
do que o dono leu no modelo do `P-0745` em 2026-09-21 — a própria §3 diz que *"não esgotam a
matéria"* —; o nome *ator inédito na operação* e a afirmação de que a classe é *"integralmente
mecânica"* foram generalização de quem registrou, atribuída ao dono. Não há critério a manter nem
a dispensar, e a pendência `AE-18` do `P-0746` se encerra por este ato. O `TK-73b` é cancelado.
- **Notas de execução:**
  - 2026-09-25 `cancelled` — absorvido pelo P-0751 como EBK-T9 (DEB-2)

### TK-73b — O sujeito da operação e o critério de ator inédito [Sonnet · esforço low · classe redacao]

- **Status:** `cancelled` · 2026-09-25 — decisão do dono sobre o `AE-18` do `P-0746`
- **Objetivo:** fixar na doutrina o que o texto de uma operação pode dizer sobre quem age, na forma
  que o dono escolher.
- **A decisão pendente (vai ao dono no relatório):** o critério *ator inédito na operação*, que o
  dono tipificou como mecânico, acusa 6 de 7 atores do `P-0743` (aceito), 4 de 4 do `P-0746` e 5 de
  5 do `P-0745` reautorado — reprova o acervo inteiro ao pé da letra.
  - **(a) Manter a dispensa** — quem age não é aferido; o vínculo entre fluxo e tabela se afere
    pelos objetos e propriedades citados (`V5`, `V16`) e pelo lastro. Implica: uma frase em
    `GOVERNANCA.md` §3.2, nada mais.
  - **(b) Proibir sujeito-ator** — a operação diz o que muda, não quem age. Implica: reescrever a
    descrição da operação em `GOVERNANCA.md` §3.2 e `README.md` §8.1 (hoje *"nomeando quem age"* e
    *"dizem quem age"*); nenhum modelo vivo a reescrever (§5).
  - **(c) Outra formulação** — exige nova medição e volta ao planejamento.
- **Arquivos-alvo:**
  - `GOVERNANCA.md`
  - `README.md` — só na opção (b)
- **Texto atual 1** (`GOVERNANCA.md` §3.2, *O que é*, uma ocorrência; sem quebra nova):

  ~~~~
  (`### 1.2 Fluxo de operações`), numeradas `OP-<n>`, cada uma nomeando quem age, o que faz, de que
  ~~~~

- **Texto novo 1(a):**

  ~~~~
  (`### 1.2 Fluxo de operações`), numeradas `OP-<n>`, cada uma nomeando quem age — o que não se afere: o vínculo entre fluxo e tabela é o dos objetos e propriedades citados —, o que faz, de que
  ~~~~

- **Texto novo 1(b):**

  ~~~~
  (`### 1.2 Fluxo de operações`), numeradas `OP-<n>`, cada uma dizendo o que muda — nunca quem age —, de que
  ~~~~

- **Texto atual 2** (`README.md` §8.1, uma ocorrência; só na opção (b); sem quebra nova):

  ~~~~
  operações** encadeadas, que dizem quem age, o que faz, de que objetos precisa e que propriedades
  ~~~~

- **Texto novo 2(b):**

  ~~~~
  operações** encadeadas, que dizem o que muda, de que objetos precisa e que propriedades
  ~~~~

- **Verificação:** no PowerShell, na raiz; **antes** medido em 2026-09-25.
  1. opção (a): `(Select-String -Path GOVERNANCA.md -SimpleMatch 'o que não se afere: o vínculo entre fluxo e tabela').Count` — antes `0`, depois `1`
  2. opção (b): `(Select-String -Path GOVERNANCA.md -SimpleMatch 'nunca quem age').Count` — antes `0`, depois `1`; `(Select-String -Path README.md -SimpleMatch 'que dizem quem age').Count` — antes `1`, depois `0`
  3. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho.
- **Pronto quando:** as contagens da opção decidida saem nos valores de depois.
- **Ao destravar:** quem registrar a decisão do dono apaga do card a opção não escolhida e a
  palavra "opção" das verificações, e passa o card a `ready`; a opção (c) devolve o card ao
  planejamento.
- **Notas de execução:**
  - 2026-09-25 `cancelled` — ato do dono de 2026-09-25: a regra não existe, foi inferida de exemplo; nada a decidir (§6 do tíquete)

## TK-74 — `review_evidence.py` não expande alvo terminado em barra

- **Status:** `done` · 2026-09-25 — aberto pelo consultor de plano do `P-0746` por `I-4` (achado
  fora de escopo vira tíquete).

**Origem:** `AE-22` do `P-0746`, medido no laudo da `LST-T6`.

### 1. Defeito medido

`Arquivos-alvo` que termina em barra — `tests/fixtures/modelo/`, prescrito pelo consultor no reparo
da `LST-T5` (`DLS-17`) — não é expandido pelo instrumento: as **10** fixtures tocadas chegaram ao
revisor da tarefa seguinte como falso `sem-atribuicao`. O laudo não foi rebaixado porque o revisor
reconciliou à mão, mas a reconciliação manual é exatamente o que o instrumento existe para evitar.

### 2. O que decide

Se o alvo de diretório se expande no instrumento (todo arquivo sob o prefixo é atribuído à tarefa)
ou se a gramática do card passa a proibir alvo de diretório, exigindo enumeração. Par
presença-ausência sobre fixture nos dois casos: alvo com barra atribui, alvo inexistente não.

### 3. O que este tíquete não faz

- Não altera laudo algum já emitido.
- Não toca `backlog.py`, cujos defeitos medidos são o `TK-65`.

### 4. Decisão do planejamento (2026-09-25)

- **`DT-1` — expande no instrumento; a gramática não muda.** A gramática já aceita alvo de
  diretório (`DB-27`: `_eh_caminho` aceita barra final, e `tests/fixtures/backlog/` é o exemplo
  da docstring), e o alvo-diretório **do próprio card** já casa por prefixo (`AUT-T5b`, em
  `confrontar_escopo`). O defeito é a assimetria: o mapa de **outra** tarefa casa só por caminho
  exato. Proibir alvo de diretório invalidaria cards já aceitos e o ajudante que já o reconhece.
- **`DT-2` — precedência:** caminho exato vence; sem caminho exato, vence o alvo-diretório de
  prefixo mais longo. Arquivo sob nenhum alvo continua `sem-atribuicao`.
- **`DT-3` — o `AE-2` do `TK-78` entra aqui como `TK-74b`.** Ele foi roteado a `TK-66`/`TK-74`
  (*facetas de instrumento*) e segue vivo em 2026-09-25: `python .claude/tools/modelo.py check
  --plano TK-74` termina em `FileNotFoundError` com traceback. O loop roda esse comando no passo 3
  de todo despacho, inclusive o da `TK-74a`.
- **Âncoras do `P-0749` preservadas (`DSA-16`):** os cards não renomeiam `mapear_alvos_de_outras_tarefas`,
  `confrontar_escopo`, `formatar_atribuicoes`, `_init_repo_com_baseline` nem as linhas
  `plano_id_match` — a `SAN-T1` depende deste tíquete e ancora nesses nomes.

### TK-74a — O alvo-diretório de outra tarefa casa por prefixo [Sonnet · esforço medium · classe implementacao]

- **Status:** `done` · 2026-09-25
- **Objetivo:** arquivo tocado sob um alvo-diretório declarado por **outra** tarefa do mesmo plano
  sai `alvo-de-outra-tarefa (<ID>)`, como já sai `alvo-do-card` o arquivo sob o alvo-diretório do
  próprio card.
- **Fundamento:** `AE-22` do `P-0746` (10 fixtures sob `tests/fixtures/modelo/`, alvo da
  `LST-T5`, chegaram à revisão da `LST-T6` como `sem-atribuicao`); `DT-1` e `DT-2` acima.
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
- **Contratos/classes:**
  - função nova `_tarefa_dona(tocado_norm: str, outros: dict[str, str], root: Path) -> str | None`,
    logo antes de `confrontar_escopo`: se `tocado_norm` é chave de `outros` → devolve o valor;
    senão, entre as chaves `chave` de `outros` com `_eh_alvo_diretorio(root, chave)` verdadeiro e
    `tocado_norm.startswith(_normalizar_separador(chave).rstrip("/") + "/")`, devolve o valor da de
    prefixo mais longo; nenhuma → `None`.
  - em `confrontar_escopo`, o ramo `if tocado_norm in outros:` / `de_outra_tarefa[tocado] =
    outros[tocado_norm]` passa a ser `dona = _tarefa_dona(tocado_norm, outros, root)` /
    `if dona is not None:` / `de_outra_tarefa[tocado] = dona`. Os demais ramos e a ordem de
    precedência dos baldes não mudam.
  - na docstring de `confrontar_escopo`, o trecho `a atribuição a outra tarefa casa por caminho
    exato, depois de normalizar` passa a dizer que ela casa por caminho exato e, sem ele, pelo
    alvo-diretório de prefixo mais longo (`TK-74`), depois de normalizar.
- **Passos:**
  1. Escreva os dois TF abaixo em `tests/test_review_evidence.py`, reusando `_load_review_evidence`,
     `_init_repo_com_baseline` e `_escrever_plano_duas_tarefas`; rode-os e veja-os falhar.
  2. Implemente os contratos; rode o arquivo de teste inteiro.
  3. Rode as Verificações.
- **Testes:**
  - TF `test_tf_atribuir_alvo_diretorio_de_outra_tarefa_casa_por_prefixo(tmp_path, capsys)` — par
    presença-ausência: repositório de `_init_repo_com_baseline`; plano de
    `` _escrever_plano_duas_tarefas(plano, "edita `src/b.py`.", "cria `tests/fixtures/modelo/`.") ``;
    cria `tests/fixtures/modelo/a.md` e `tests/fixtures/outro/b.md` no repositório;
    `main(["--plano", str(plano), "--tarefa", "T1", "--root", str(repo), "--atribuir"])` devolve `0`
    e a saída contém `atribuicao: tests/fixtures/modelo/a.md -> alvo-de-outra-tarefa (T2)` **e**
    `atribuicao: tests/fixtures/outro/b.md -> sem-atribuicao`.
  - TF `test_tf_tarefa_dona_exato_vence_e_prefixo_mais_longo_desempata(tmp_path)` —
    `confrontar_escopo(["tests/fixtures/modelo/a.md", "tests/fixtures/modelo/c.md", "tests/x.md"],
    [], tmp_path, {"tests/": "T2", "tests/fixtures/modelo/": "T3", "tests/fixtures/modelo/a.md": "T4"})["de_outra_tarefa"]`
    é igual a `{"tests/fixtures/modelo/a.md": "T4", "tests/fixtures/modelo/c.md": "T3", "tests/x.md": "T2"}`.
  - TR: `tests/test_review_evidence.py` inteiro verde, inclusive
    `test_tf_arquivo_alvo_de_outra_tarefa_sai_atribuido_e_nao_pesa_no_veredito` e
    `test_tf_atribuir_alvo_diretorio_casa_por_prefixo`.
- **Restrições desta tarefa:**
  - Não renomear nem mudar a assinatura de `mapear_alvos_de_outras_tarefas`, `confrontar_escopo`,
    `formatar_atribuicoes` e `_init_repo_com_baseline` (âncoras da `SAN-T1` do `P-0749`).
  - Não filtrar por `status` — é a `TK-66a`.
  - Não commitar.
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho
    sobe em exatamente `2`.
- **Não fazer:** não mudar a gramática de caminho da `DB-27`; não mudar os baldes
  `registro-da-orquestracao` e `ato-do-dono`.
- **Contingências:**
  - se `confrontar_escopo` não tiver exatamente uma ocorrência de `if tocado_norm in outros:` →
    parar e sinalizar `blocked` razão `premissa`, colando a linha encontrada
  - se algum teste preexistente de `tests/test_review_evidence.py` ficar vermelho → parar e
    sinalizar `blocked` razão `premissa`, colando o nome do teste
- **Verificação:** no PowerShell, na raiz do repositório; **antes** medido em 2026-09-25.
  1. `python -m pytest tests/test_review_evidence.py -q` — antes `42 passed`; depois `44 passed`,
     `0 failed`
  2. `python -m pytest -q` — total de `passed` = o medido no despacho `+ 2`, `0 failed`
  3. `(Select-String -Path .claude/tools/review_evidence.py -SimpleMatch '_tarefa_dona(').Count` —
     antes `0`, depois `2`
  4. `(Select-String -Path .claude/tools/review_evidence.py -SimpleMatch 'if tocado_norm in outros:').Count`
     — antes `1`, depois `0`
- **Pronto quando:** arquivo sob alvo-diretório de outra tarefa sai atribuído a ela e arquivo sob
  nenhum alvo segue `sem-atribuicao` — Verificações 1 a 4.
- **Fora do escopo desta tarefa:** o filtro por `status` (`TK-66a`); o `modelo.py` (`TK-74b`).
- **Notas de execução:**
  - 2026-09-25 `review` — V1 44 passed; V2 324 passed (322+2); V3 2; V4 0

### TK-74b — `modelo.py` recusa limpo o alvo que não é arquivo de plano [Sonnet · esforço low · classe implementacao]

- **Status:** `done` · 2026-09-25
- **Objetivo:** `modelo.py check` e `modelo.py show` com `--plano` que não é arquivo saem com uma
  linha e exit `2`, sem traceback.
- **Fundamento:** `AE-2` do `TK-78` e `DT-3` acima. Exit `2` porque é o código que o passo 9 da
  skill `scrum-master` já lê como *sem modelo a julgar — materializa e fecha*, o mesmo que
  `_checar_forma` devolve a plano sem a seção do modelo; o tíquete do diário é esse caso.
- **Arquivos-alvo:**
  - `.claude/tools/modelo.py`
  - `tests/test_modelo.py`
- **Contratos/classes:**
  - constante nova, junto das demais `_MSG_*`: `_MSG_PLANO_AUSENTE = "modelo: plano não encontrado
    '{}' — sem modelo a julgar"`.
  - em `verbo_check` e em `verbo_show`, logo depois de `plano_path = _resolver_plano(args)`:
    `if not plano_path.is_file():` → `print(_MSG_PLANO_AUSENTE.format(args.plano))` e `return 2`.
    Mesmo canal (`print` em stdout) das mensagens de `_checar_forma`.
- **Passos:**
  1. Escreva os dois TF abaixo em `tests/test_modelo.py`, reusando `_load_modelo`; rode-os e
     veja-os falhar.
  2. Implemente os contratos; rode o arquivo de teste inteiro.
  3. Rode as Verificações.
- **Testes:**
  - TF `test_tf_check_plano_inexistente_sai_2_sem_traceback(tmp_path, capsys)`:
    `_load_modelo().main(["check", "--plano", "TK-74", "--root", str(tmp_path)])` devolve `2` e a
    saída padrão contém `modelo: plano não encontrado 'TK-74'`.
  - TF `test_tf_show_plano_inexistente_sai_2_sem_traceback(tmp_path, capsys)`: o mesmo com
    `["show", "--plano", "TK-74", "--root", str(tmp_path)]`.
  - TR: `tests/test_modelo.py` inteiro verde.
- **Restrições desta tarefa:**
  - Não mudar exit nem mensagem de nenhum caminho em que o plano existe.
  - Não commitar.
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho
    sobe em exatamente `2`.
- **Não fazer:** não ensinar o `modelo.py` a ler tíquete do diário; não tocar `backlog.py`.
- **Contingências:**
  - se `verbo_check` ou `verbo_show` não tiver exatamente uma linha `plano_path = _resolver_plano(args)`
    → parar e sinalizar `blocked` razão `premissa`, colando o que encontrou
- **Verificação:** no PowerShell, na raiz do repositório; **antes** medido em 2026-09-25.
  1. `python .claude/tools/modelo.py check --plano TK-74; $LASTEXITCODE` — antes traceback
     `FileNotFoundError`; depois a linha `modelo: plano não encontrado 'TK-74' — sem modelo a julgar`
     e `2`
  2. `python -m pytest tests/test_modelo.py -q` — os dois TF novos verdes, `0 failed`
  3. `python -m pytest -q` — total de `passed` = o medido no despacho `+ 2`, `0 failed`
- **Pronto quando:** alvo que não é arquivo sai em uma linha com exit `2` nos dois verbos —
  Verificações 1 a 3.
- **Fora do escopo desta tarefa:** o `review_evidence.py` (`TK-74a`, `TK-66a`).
- **Notas de execução:**
  - 2026-09-25 `review` — V1 linha + exit 2 (check e show); V2 32 passed; V3 326 passed (324+2)

## TK-76 — As tabelas do modelo se escrevem para o dono

- **Status:** `done` · 2026-09-23 — aberto por ato do dono, ao ler o modelo do `P-0747`.

**Ato do dono, 2026-09-23, verbatim:**

> A definição de objetos no modelo ficou bom, mas gostaria que fizesse um tíquete avulso para ajustar
> na matéria de modelo que, pelo menos no que será apresentado ao cliente/dono/domain expert, evite ter
> tanta especificidade nos campos descritivos. Por exemplo, na coluna "Contratos", aparecem muitas
> indireções que é difícil de compreender.
> Não faça nade neste plano, mas nos próximos acionamentos do model-designer, que a tabela inteira dos
> elementos de modelo seja "human-friendly", com frases curtas e ilustrativas do conteudo real.
> Nas demais seções, que são "machine-friendly", pode ser feito o descritivo adequado.

**Caso medido:** o contrato do objeto de escopo do `P-0747` (`consultor`) passou de 600 palavras,
feitas de caminhos, números de linha, itens de `F-4` e ids de decisão; o veredito de 2026-09-22 (§3.4)
já registrava que essa especificidade, copiada nos oito cards, não serve ao executor.

**Fronteira:** o `P-0747` não se toca (ato do dono). O instrumento não se estende: a `V12` continua
aferindo só crase e barra no texto da operação — estender a aferição às três tabelas reprovaria os
modelos vigentes do acervo, e gramática nova vem antes do parser (`F-17` do `P-0746`). O pacote 5 do
`TK-72` §7 (contrato sem a partição alheia) fica absorvido por este card, que resolve a mesma matéria
na origem.

### TK-76a — As tabelas do modelo em frases curtas para o dono [Sonnet · esforço low · classe redacao]

- **Status:** `done` · 2026-09-23
- **Objetivo:** fixar, na norma e nas duas definições de conduta, que as três tabelas do modelo
  conceitual — objetos, texto das operações, estados — são escritas para o dono em frases curtas e
  ilustrativas, e que a especificidade que o executor precisa mora nas seções do plano escritas para
  a máquina.
- **Fundamento:** ato do dono de 2026-09-23 (acima); veredito `docs/plans/_VEREDITO-procedimentos-2026-09-22.md` §3.4.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-model-designer.md`
  - `GOVERNANCA.md`
  - `.claude/agents/pantonic-planner.md`
- **Passos:**
  1. Em `.claude/agents/pantonic-model-designer.md`, insira o bloco **Texto novo 1** imediatamente
     antes da linha `## Os quatro atos`, separado por uma linha em branco antes e depois.
  2. Em `GOVERNANCA.md`, substitua o bloco **Texto atual 2** pelo bloco **Texto novo 2**.
  3. Em `.claude/agents/pantonic-planner.md`, substitua o bloco **Texto atual 3** pelo bloco
     **Texto novo 3**.

- **Restrições desta tarefa:**
  - Toda edição é substituição ou inserção literal: o texto novo entra exatamente como está no bloco.
  - Não tocar `docs/plans/P-0747-consultor-de-plano.md` nem nenhum outro plano (ato do dono).
  - Não tocar `.claude/tools/modelo.py`, seus testes nem suas fixtures.
  - Não commitar.
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (medido em 2026-09-23: `277 passed`, referência histórica).
- **Não fazer:** não alterar a `description` do frontmatter de nenhum agente (mudaria a região gerada
  de `.claude/README.md` e deixaria o check-drift vermelho); não reescrever as tabelas de plano
  nenhum para a forma nova.
- **Contingências:**
  - se um bloco **Texto atual** não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco
  - se a linha `## Os quatro atos` não existir exatamente uma vez em `.claude/agents/pantonic-model-designer.md` → parar e sinalizar `blocked` razão `premissa`
  - se o valor **antes** de qualquer linha de `Verificação` diferir do publicado → parar e sinalizar `blocked` razão `premissa`, citando a linha e o valor medido
  - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina. A guarda é a suíte inteira, que inclui `tests/test_doutrina_unidade.py` (prende literais de `GOVERNANCA.md` e de `.claude/agents/pantonic-planner.md`).
- **Verificação:** no PowerShell, na raiz do repositório; **antes** medido em 2026-09-23.
  1. `(Select-String -Path .claude/agents/pantonic-model-designer.md -SimpleMatch 'As tabelas do modelo se escrevem para o dono').Count` — antes `0`, depois `1`
  2. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'human-friendly').Count` — antes `0`, depois `1`
  3. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'escrito para o dono').Count` — antes `0`, depois `1`
  4. `python .claude/tools/modelo.py check --plano docs/plans/P-0747-consultor-de-plano.md` — antes e depois `modelo: OK — 8 operações, 5 objetos, 12 propriedades, 8 tarefas, versão 1`, exit `0`
  5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` — antes e depois exit `0`
  6. `python -m pytest -q` — total de `passed` igual ao medido no despacho, `0 failed`
- **Pronto quando:** a regra *tabelas do modelo human-friendly, especificidade nas seções machine-friendly* está escrita nas três residências — Verificações 1, 2 e 3 —, o `P-0747` segue intocado e verde — Verificação 4 —, e nenhum gate regrediu — Verificações 5 e 6.
- **Fora do escopo desta tarefa:** estender a `V12` às tabelas; reescrever modelo de plano existente; o restante do `TK-72` §7.

### Achados da execução (TK-76)

- **`AE-1` (2026-09-23, laudo da `TK-76a`, alvo `dossiê`)** — os blocos literais foram autorados no meio do card e o gerador de evidência deixou de achar `Verificação`; o loop os moveu para o fim. Regra: bloco cercado de card vai depois do último campo. **Rota:** `TK-72`.
- **`AE-2` (idem)** — o `Pronto quando` exige o `P-0747` intocado, mas a verificação só afere que o modelo segue válido; arquivo não rastreado não tem diff. Regra: card que prende arquivo não rastreado publica hash antes e depois. **Rota:** `TK-72`.
- **`AE-3` (idem)** — atribuição de evidência por arquivo sobre árvore com WIP de outras frentes exigiu reconciliação manual. **Rota:** sem ação nova — já roteado à atribuição por hunk (`TK-66`).

**Texto novo 1** — `.claude/agents/pantonic-model-designer.md`:

~~~~
## As tabelas do modelo se escrevem para o dono

As três tabelas da seção — `### 1.1 Objetos`, o texto de cada operação em `### 1.2 Fluxo de
operações` e `### 1.3 Estado inicial e estado final` — são o que o dono, o cliente e o domain expert
leem no Marco 1. Escreva-as **human-friendly**: frases curtas, em linguagem corrente, que ilustram o
conteúdo real — o que a coisa é, o que muda nela e como se vê que mudou. Nas células descritivas
(`o que é`, `propriedades`, `contrato`, os dois estados) não entram caminho de arquivo, número de
linha, identificador de decisão, fato ou item, nome de instrumento nem remissão a outra seção. O
contrato de um objeto diz, em uma ou duas frases, o que quem implementa recebe nas mãos — não
enumera onde isso mora. A especificidade que o executor precisa — residências, partição de arquivos
entre operações, exclusões, comandos — pertence às seções **machine-friendly** do plano, que são do
planejador: `## 2. Fatos estabelecidos`, `## 3. Decisões` e os campos do card. As linhas entre
crases do fluxo (`precisa de:`, `altera:`, `tarefas:`, `lastro:`) e a coluna de lastro continuam na
forma que o instrumento lê. Caso medido: o contrato do objeto de escopo do `P-0747` passou de 600
palavras de indireções, e o dono o achou difícil de compreender (`TK-76`, 2026-09-23).
~~~~

**Texto atual 2** — `GOVERNANCA.md`:

~~~~
instrumento recusa crase e barra (`V12`); o resto é dever de autoria. Máximo de 40 operações por
plano.
~~~~

**Texto novo 2** — `GOVERNANCA.md`:

~~~~
instrumento recusa crase e barra (`V12`); o resto é dever de autoria. Máximo de 40 operações por
plano. O mesmo vale para as células descritivas das três tabelas — objetos, estados e o contrato de
cada objeto: são escritas **human-friendly**, em frases curtas e ilustrativas do conteúdo real, e a
especificidade que o executor precisa (residências, arquivos, exclusões, comandos) mora nas seções
do plano escritas para a máquina — fatos, decisões e os campos do card (`TK-76`, ato do dono de
2026-09-23). A aferição é do marco, não do instrumento.
~~~~

**Texto atual 3** — `.claude/agents/pantonic-planner.md`:

~~~~
a `Camada e fronteira` transcreve o contrato dos objetos de que ela precisa.
~~~~

**Texto novo 3** — `.claude/agents/pantonic-planner.md`:

~~~~
a `Camada e fronteira` transcreve o contrato dos objetos de que ela precisa e acrescenta, da `## 2`,
as residências e os arquivos que o contrato — escrito para o dono — não enumera.
~~~~

## TK-77 — `kit_check` não recusa frontmatter de agente que não é YAML válido

- **Status:** `done` · 2026-09-25 — aberto pela orquestração do `P-0747`, rota do `AE-20` (iii) daquele plano.

**Caso medido (2026-09-23):** a `CON-T8` do `P-0747` gravou na `description` de `.claude/agents/pantonic-consultant.md` a sequência `Efêmero: cada acionamento`; o `: ` num valor sem aspas faz `yaml.safe_load` falhar (*"mapping values are not allowed here"*), e o harness pode deixar de carregar o agente. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate` saiu `0` com o arquivo nesse estado, o check-drift também, e a revisão só pegou o defeito por leitura. O corretivo `CON-T8a` reparou o arquivo; a guarda continua sem pegar a classe.

**O que decide:** o `validate` passa a recusar todo `.claude/agents/*.md` cujo frontmatter um parser YAML estrito recusa, com a mensagem nomeando o arquivo. Par presença-ausência sobre fixture: `description` com `: ` sem aspas → exit diferente de 0; a mesma com ` - ` → exit 0.
- **Notas de execução:**
  - 2026-09-25 `done` — 1/1 card done (TK-77a); o validate recusa frontmatter que o yaml.safe_load recusa

### TK-77a — O `validate` recusa frontmatter de agente ou skill que o YAML estrito recusa [Sonnet · esforço medium · classe implementacao]

- **Status:** `done` · 2026-09-25
- **Objetivo:** o `kit_check.ps1 -Mode validate` passa a falhar, nomeando o arquivo, quando o frontmatter de um `.claude/agents/*.md` ou de um `.claude/skills/*/SKILL.md` não é YAML válido para `yaml.safe_load` ou não carrega um mapeamento. A classe é a mesma nas duas famílias (o harness lê as duas pelo frontmatter), e o leitor de frontmatter do script já é um só (`Get-Frontmatter`).
- **Arquivos-alvo:**
  - `.claude/checks/frontmatter_yaml.py` (novo)
  - `.claude/checks/kit_check.ps1`
  - `tests/test_frontmatter_yaml.py` (novo)
- **Desenho:**
  1. `frontmatter_yaml.py` — função pura `problemas(caminhos: list[Path]) -> list[str]`: para cada arquivo, lê em UTF-8, recorta o bloco entre a primeira linha `---` e a seguinte `---` (arquivo sem o bloco não é problema deste script: o `validate` já o acusa), aplica `yaml.safe_load` e devolve `"<caminho>: <primeira linha da mensagem do erro YAML>"` quando o parser levanta, ou `"<caminho>: frontmatter não é mapeamento"` quando o resultado não é `dict`. CLI: `python .claude/checks/frontmatter_yaml.py <arquivo>...` imprime um problema por linha e sai `1` se houver algum, `0` se nenhum; sem PyYAML importável imprime `frontmatter_yaml: PyYAML ausente` e sai `2`. Força UTF-8 em `stdout`/`stderr` antes de imprimir (mesma forma do `_forcar_utf8` de `.claude/tools/review_evidence.py`).
  2. `kit_check.ps1`, bloco `validate` — logo antes da linha `# --- 3. Paridade de versão: VERSION (raiz) == .claude/KIT_VERSION --------`, uma seção `# --- 2b. Frontmatter é YAML válido` que chama o script com os caminhos de `$agentFiles` e dos `SKILL.md` existentes de `$skillDirs`, no mesmo padrão da chamada do `materializar.py` (seção 4): exit `1` → cada linha vira `$errors.Add("frontmatter YAML: $line")`; exit diferente de `0` e `1` → `$errors.Add("frontmatter YAML: saida nao interpretavel (exit N): ...")`.
- **Caso medido que motivou (2026-09-25, re-medido no ato da autoria):** cópia de `.claude/` + `VERSION` num diretório temporário, com `Efêmero - cada acionamento` trocado por `Efêmero: cada acionamento` na `description` de `agents/pantonic-consultant.md` → `kit_check.ps1 -Mode validate -KitRoot <cópia>/.claude` sai `kit_check: OK - 10 agente(s), 12 skill(s) …` exit `0`. `yaml.safe_load('description: Efêmero: cada acionamento')` levanta `ScannerError`; com ` - ` devolve o mapeamento. Hoje os 10 agentes e as 12 skills da árvore passam no `safe_load`.
- **Testes (novos, em `tests/test_frontmatter_yaml.py`):**
  - TF par presença-ausência sobre a função: arquivo com `description: A: b` → 1 problema com o nome do arquivo; o mesmo com `description: A - b` → 0 problemas.
  - TF: frontmatter que carrega lista ou escalar (não mapeamento) → 1 problema.
  - TF par presença-ausência ponta a ponta: cópia de `.claude/` + `VERSION` sob `tmp_path` (`shutil.copytree`, ignorando `__pycache__`), `pwsh -NoProfile -File <cópia>/.claude/checks/kit_check.ps1 -Mode validate -KitRoot <cópia>/.claude` → exit `0`; com a troca acima no `pantonic-consultant.md` da cópia → exit diferente de `0` e a saída contém `pantonic-consultant.md`. Pular (`pytest.skip`) se `pwsh` não estiver no `PATH`.
- **Verificação:**
  1. `python -m pytest tests/test_frontmatter_yaml.py -q` → verde, com os três testes acima.
  2. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate` na árvore → exit `0` (os 22 frontmatters atuais passam).
  3. `python -m pytest tests -q` → nenhuma falha; total = o da referência do despacho mais os testes novos (referência medida na autoria: `353 passed`, re-derivada no despacho).
- **Pronto quando:** o `validate` recusa, com o nome do arquivo na saída, o frontmatter de agente ou skill que o `yaml.safe_load` recusa, e aceita o mesmo arquivo com ` - ` no lugar de `: `; o par está em teste ponta a ponta sobre cópia do kit, falhando sobre o `kit_check.ps1` anterior e passando sobre o novo.
- **Não fazer:** não reescrever `Get-Frontmatter`/`Get-FieldValue` nem as checagens de campo existentes; não tocar os agentes e skills da árvore (todos passam); não acrescentar PyYAML a arquivo de dependências.
- **Contingências:**
  1. se algum frontmatter da árvore falhar no `safe_load` no ato da execução → parar e sinalizar `blocked motivo=premissa` com o arquivo e a mensagem do parser, sem consertá-lo.

## TK-78 — As pendências da janela de 2026-09-24 do `P-0748`

- **Status:** `done` · 2026-09-24 — aberto pela orquestração do `P-0748` por ordem do dono, com prioridade sobre o plano: *"Queria resolver essas pendências primeiro logo na próxima janela, então crie um card extra prioritário para o próximo contexto, e depois desse card, volte a esse plano."*

**Origem:** janela de 2026-09-24 do `P-0748` (`TLG-T1`, `TLG-T2`) · **Achados:** `AE-1`, `AE-2` (ii, iii) e `AE-3` do `P-0748`, mais a ordem do dono na abertura da mesma janela: *"Não dá para você ficar interrompendo a execução para isso. [...] Continue com Opus e páre de interromper o trabalho para isso"* (candidato `nao-interromper-por-troca-de-modelo` na fila de memória, cujo lar é a doutrina, não a memória).

**Caso medido:** na abertura da janela o loop parou duas vezes seguidas em sentidos opostos — o hook `UserPromptSubmit` mandou pedir `/model opus`, o passo 1 da `scrum-master` mandou pedir `/model sonnet` — sem nenhum trabalho entre as duas paradas. Depois, o gerador de evidência recusou o card de investigação (`AE-1`), recolheu a árvore suja inteira como diff da entrega e truncou o trecho do alvo antes de chegar à seção entregue (`AE-3` ii), e a verificação por `numstat` da `TLG-T2` só foi aferível relida como delta (`AE-3` i).

**O que decide:** três cards, em sequência, cada um numa superfície: o loop deixa de parar para rebaixar o modelo e só para para subir a um melhor (`TK-78a`, emendado pelo adendo do dono abaixo); a régua de autoria do card aprende as três lições da janela (`TK-78b`); o gerador de evidência passa a medir só o que mudou desde o despacho (`TK-78c`). Fechado o `TK-78`, a diretiva volta ao `P-0748`.

**Adendo do dono na abertura da execução (2026-09-24), verbatim:** *"como a tela principal é só o orquestrado, nunca parar para rebaixar o modelo, apenas para escolher um melhor"*. Materializado como emenda do `TK-78a` antes do despacho: modelo ativo **acima** do indicado segue e anota uma linha; modelo ativo **abaixo** do indicado para e pede ao dono o `/model` do melhor. O Texto 8 (nudge da fase intelectual, que já só manda subir a Opus) saiu do card.

**Relação:** o `TK-72` (régua de autoria, quatro pacotes do `P-0746`) e o `TK-66` (atribuidor que ignora `status`) seguem abertos e não são absorvidos — o `TK-78b` escreve na mesma família de regra, em residência vizinha, sem tocar os pacotes deles.

### TK-78a — O loop não para para rebaixar o modelo [Sonnet · esforço medium · classe redacao]

- **Status:** `done` · 2026-09-24
- **Objetivo:** tirar da skill do loop, da skill `modelo-por-fase`, da matriz de `GOVERNANCA.md` §3 e do hook de nudge a instrução de parar para **rebaixar** o modelo: o contexto principal só orquestra, o modelo de cada tarefa viaja no despacho, e modelo ativo acima do indicado vira uma linha de nota, nunca parada. A única parada que sobra é a de subir: modelo ativo abaixo do que a fase exige para e pede ao dono o `/model` do melhor.
- **Fundamento:** ordem do dono de 2026-09-24 e adendo do dono na abertura da execução (acima); caso medido acima.
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md`
  - `.claude/skills/modelo-por-fase/SKILL.md`
  - `GOVERNANCA.md`
  - `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`
  - `README.md`
  - `.claude/README.md` (regenerado pelo gerador do kit, nunca à mão)
- **Passos:**
  1. Em `.claude/skills/scrum-master/SKILL.md`, substitua o **Texto atual 1** pelo **Texto novo 1** e o **Texto atual 2** pelo **Texto novo 2**.
  2. Em `.claude/skills/modelo-por-fase/SKILL.md`, substitua os **Textos atuais 3, 4 e 5** pelos **Textos novos 3, 4 e 5**.
  3. Em `GOVERNANCA.md`, substitua o **Texto atual 6** pelo **Texto novo 6**.
  4. Em `README.md`, substitua o **Texto atual 7** pelo **Texto novo 7**.
  5. Em `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`, substitua o **Texto atual 9** pelo **Texto novo 9** (não há Texto 8: o nudge da fase intelectual fica intacto).
  6. Rode `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` (a `description` da `modelo-por-fase` muda a região gerada de `.claude/README.md`).
  7. Rode as Verificações.
- **Restrições desta tarefa:**
  - Toda edição é substituição literal; o texto novo entra exatamente como está no bloco. Os arquivos `.md` da skill têm final de linha CRLF na cópia de trabalho: compare ignorando `\r` e preserve o final de linha existente.
  - Não editar nada fora do repositório: a projeção do hook para `~/.claude/hooks/` é ato do dono (Fora do escopo).
  - Não tocar a Regra 5 (anúncio de troca efetivada) nem a seção `## Convenção de anúncio` da `modelo-por-fase`.
  - Não commitar.
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (referência histórica: `277 passed`, 2026-09-24).
- **Não fazer:** não mudar a tabela de modelo por fase (quem roda em que modelo); não remover a skill `modelo-por-fase`; não tocar `_NUDGE["intellectual"]` nem as `systemMessage` do hook (a parada para subir é a que o adendo preserva); não editar `C:\Users\panta\.claude\`.
- **Contingências:**
  - se um bloco **Texto atual** não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco
  - se `kit_check.ps1 -Mode generate` ou `-Mode check-drift` sair diferente de `0` → parar e sinalizar `blocked` razão `ferramenta`, colando a última linha da saída
  - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina e texto de nudge. TR: a suíte inteira; `py_compile` do hook.
- **Verificação:** no PowerShell, na raiz do repositório; **antes** medido em 2026-09-24.
  1. `(Select-String -Path .claude/skills/scrum-master/SKILL.md -SimpleMatch 'PARA e pede `/model` ao dono').Count` — antes `1`, depois `0`
  2. `(Select-String -Path .claude/skills/scrum-master/SKILL.md -SimpleMatch 'O loop nunca para para rebaixar o modelo').Count` — antes `0`, depois `1`
  3. `(Select-String -Path .claude/skills/scrum-master/SKILL.md -SimpleMatch '--desde <data de abertura da janela>').Count` — antes `1`, depois `0`
  4. `(Select-String -Path .claude/skills/modelo-por-fase/SKILL.md -SimpleMatch 'Gate de parada').Count` — antes `2`, depois `0`; `(Select-String -Path .claude/skills/modelo-por-fase/SKILL.md -SimpleMatch '## Gate de subida').Count` — antes `0`, depois `1`
  5. `(Select-String -Path GOVERNANCA.md -SimpleMatch '**para para pedir `/model`**').Count` — antes `1`, depois `0`; `(Select-String -Path GOVERNANCA.md -SimpleMatch '**nunca para para rebaixar o modelo**').Count` — antes `0`, depois `1`
  6. `(Select-String -Path README.md -SimpleMatch 'e para para pedir o correto').Count` — antes `1`, depois `0`
  7. `(Select-String -Path .claude/global/hooks/modelo_por_fase_userpromptsubmit.py -SimpleMatch 'recomende ao dono `/model sonnet`').Count` — antes `1`, depois `0`; `(Select-String -Path .claude/global/hooks/modelo_por_fase_userpromptsubmit.py -SimpleMatch 'NAO pare e NAO peca').Count` — antes `0`, depois `1`; `(Select-String -Path .claude/global/hooks/modelo_por_fase_userpromptsubmit.py -SimpleMatch 'PARE e peca').Count` — antes e depois `1`
  8. `python -m py_compile .claude/global/hooks/modelo_por_fase_userpromptsubmit.py; $LASTEXITCODE` — `0`
  9. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift; $LASTEXITCODE` — depois `0`
  10. `python -m pytest -q` — total de `passed` ≥ o medido no despacho, `0 failed`
- **Pronto quando:** nenhuma das quatro superfícies manda parar para rebaixar o modelo, e as quatro dizem a mesma coisa — acima do indicado segue no modelo ativo e anota a divergência, abaixo do indicado para e pede o `/model` do melhor, o modelo da tarefa viaja no despacho — Verificações 1 a 7; o relatório de encerramento chama `modelo.py show` na forma que a ferramenta aceita — Verificação 3; nenhum gate regrediu — Verificações 8 a 10.
- **Fora do escopo desta tarefa:** projetar o hook no ponto de carga — ato do dono, depois do fechamento: `Copy-Item .claude/global/hooks/modelo_por_fase_userpromptsubmit.py $HOME/.claude/hooks/ -Force` (a cópia do kit é superconjunto da carregada: a única diferença medida em 2026-09-24 é a leitura de stdin em UTF-8, que o kit já tem); a Regra 7 do `~/.claude/CLAUDE.md` do dono.

**Texto atual 1** — `.claude/skills/scrum-master/SKILL.md` (passo 1):

~~~~
- **Ação:** rodar `.claude/skills/modelo-por-fase/SKILL.md` (fase **orquestração**, matriz
  `GOVERNANCA.md` §3). Modelo diferente do exigido: **PARA e pede `/model` ao dono**.
- **Saída:** modelo conferido, ou parada com o `/model` pedido.
~~~~

**Texto novo 1:**

~~~~
- **Ação:** rodar `.claude/skills/modelo-por-fase/SKILL.md` (fase **orquestração**, matriz
  `GOVERNANCA.md` §3). Modelo ativo **acima** do exigido: **segue** nele — o contexto principal
  só orquestra, e o modelo de cada tarefa viaja no despacho (passo 4) — e anota a divergência em
  uma linha do relatório de encerramento. O loop nunca para para rebaixar o modelo. Modelo ativo
  **abaixo** do exigido: **PARA e pede ao dono o `/model` do modelo melhor** — a única parada do
  gate.
- **Saída:** modelo conferido, com a divergência anotada quando houver, ou parada com o `/model`
  do modelo melhor pedido.
~~~~

**Texto atual 2** — `.claude/skills/scrum-master/SKILL.md` (relatório de encerramento):

~~~~
.claude/tools/modelo.py show --plano <plano> --desde <data de abertura da janela>` — a
~~~~

**Texto novo 2:**

~~~~
.claude/tools/modelo.py show --plano <plano>` — a
~~~~

**Texto atual 3** — `.claude/skills/modelo-por-fase/SKILL.md` (frontmatter, trecho da `description`):

~~~~
confere o modelo ativo contra a tabela vinculante e para para pedir o /model correto ao dono.
~~~~

**Texto novo 3:**

~~~~
confere o modelo ativo contra a tabela vinculante; acima do exigido segue e anota a divergência, e só abaixo do exigido para para pedir o /model melhor ao dono.
~~~~

**Texto atual 4** — `.claude/skills/modelo-por-fase/SKILL.md` (linha 35, trecho):

~~~~
(passo "Gate de parada" abaixo)
~~~~

**Texto novo 4:**

~~~~
(passo "Gate de subida" abaixo)
~~~~

**Texto atual 5** — `.claude/skills/modelo-por-fase/SKILL.md`:

~~~~
## Gate de parada

Se o modelo ativo **não bate** com a fase:

- **Pare** — não prossiga a fase com o modelo errado (não decida sozinho, não assuma que "dessa
  vez tanto faz").
- **Peça** ao dono, de forma explícita, o comando `/model <opus|sonnet|haiku>` correspondente.
- Só o dono decide inverter a tabela para um agente de **execução** (custo caro em execução
  exige OK explícito e registrado — `GOVERNANCA.md` §3, penúltimo bullet). Para as demais fases
  não há inversão silenciosa possível: preferência genérica de memória não decide isso.
- Se o modelo já bate com a fase, siga sem ruído — o gate não é anúncio a cada turno.
~~~~

**Texto novo 5:**

~~~~
## Gate de subida

Se o modelo ativo **não bate** com a fase (ordem: Haiku < Sonnet < Opus):

- **Acima do indicado** (ex.: Opus numa fase de Sonnet): **não pare** e não peça `/model` ao
  dono — siga no modelo ativo. O contexto principal só orquestra: o modelo de cada tarefa
  delegada viaja no despacho (`model` do cabeçalho do card), e rebaixar a tela principal nunca
  justifica interromper o trabalho. **Anote** a divergência em uma linha, no fim da resposta —
  uma vez por fase, não a cada turno; no loop de execução a nota vai ao relatório de
  encerramento (`scrum-master`, passo 1).
- **Abaixo do indicado** (ex.: Sonnet numa fase de Opus): **pare** e peça ao dono, de forma
  explícita, o `/model <opus|sonnet>` do modelo melhor — a única parada do gate. Não prossiga a
  fase com o modelo mais fraco nem assuma que "dessa vez tanto faz".
- Só o dono decide inverter a tabela para um agente de **execução** (custo caro em execução
  exige OK explícito e registrado — `GOVERNANCA.md` §3, penúltimo bullet); a inversão se
  materializa no `model` do despacho, nunca numa parada do contexto principal.
- Se o modelo já bate com a fase, siga sem ruído — o gate não é anúncio a cada turno.
~~~~

**Texto atual 6** — `GOVERNANCA.md` (§3, linha *Orquestração*, trecho):

~~~~
e **para para pedir `/model`** quando a fase exige outro modelo
~~~~

**Texto novo 6:**

~~~~
e **nunca para para rebaixar o modelo**, porque só orquestra e o modelo de cada tarefa viaja no despacho; para para pedir `/model` só quando o modelo ativo está abaixo do que a fase exige
~~~~

**Texto atual 7** — `README.md` (tabela de skills, linha `modelo-por-fase`, trecho):

~~~~
confere o modelo ativo contra a tabela vinculante e para para pedir o correto.
~~~~

**Texto novo 7:**

~~~~
confere o modelo ativo contra a tabela vinculante; acima do exigido segue e anota, e só abaixo do exigido para para pedir o melhor.
~~~~

**Texto 8** — suprimido pelo adendo do dono: `_NUDGE["intellectual"]` só manda parar para subir a Opus, que é a parada que o adendo preserva.

**Texto atual 9** — `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` (`_NUDGE["execution"]`, segunda string):

~~~~
        "Gate modelo-por-fase: este prompt e execucao mecanica (Regra 7). Se o modelo "
        "ativo for Opus, recomende ao dono `/model sonnet` antes de implementar "
        "(anuncie — Regra 5), salvo tarefa de alto risco com racional registrado.",
~~~~

**Texto novo 9:**

~~~~
        "Nota modelo-por-fase: este prompt e execucao mecanica (Regra 7); o modelo "
        "indicado e Sonnet. Se o ativo for Opus, NAO pare e NAO peca `/model` ao dono "
        "(rebaixar a tela principal nunca interrompe o trabalho): siga e anote a "
        "divergencia em uma linha no fim da resposta. So pare para pedir "
        "`/model sonnet` se o ativo for Haiku.",
~~~~

### TK-78d — A doutrina e o README deixam de mandar parar para rebaixar o modelo [Sonnet · esforço low · classe redacao]

- **Status:** `done` · 2026-09-24
- **Depende de:** `TK-78a`
- **Objetivo:** corretivo da `TK-78a` (`AE-1` abaixo): os dois trechos que os Textos 1-9 da `TK-78a` não cobriram — `GOVERNANCA.md` §3, bullet *Gatilho operacional do modelo por fase*, e `README.md` §4, frase do gatilho e parágrafo *Onde o gerente intervém* — passam a dizer o mesmo que a skill do loop, a `modelo-por-fase` e o hook já dizem: modelo ativo **acima** do indicado segue e anota a divergência em uma linha; **abaixo** do indicado para e pede ao dono o `/model` do modelo melhor.
- **Fundamento:** adendo do dono de 2026-09-24 (cabeçalho do `## TK-78`); `AE-1`; triagem do consultor de 2026-09-24 (`docs/plans/_CENARIO-TK-78.md`, `CT-1`).
- **Arquivos-alvo:**
  - `GOVERNANCA.md`
  - `README.md`
- **Passos:**
  1. Em `GOVERNANCA.md`, substitua o **Texto atual 1** pelo **Texto novo 1**.
  2. Em `README.md`, substitua o **Texto atual 2** pelo **Texto novo 2** e o **Texto atual 3** pelo **Texto novo 3**.
  3. Rode as Verificações.
- **Restrições desta tarefa:**
  - Toda edição é substituição literal de linhas inteiras; o texto novo entra exatamente como está no bloco. Os dois arquivos têm final de linha LF.
  - Não tocar as outras superfícies já conformes (`.claude/skills/scrum-master/SKILL.md`, `.claude/skills/modelo-por-fase/SKILL.md`, o hook), nem a linha *Orquestração* da matriz de `GOVERNANCA.md` §3, nem o parágrafo *Por quê* do `README.md` §4.
  - Não commitar.
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (medido pelo consultor em 2026-09-24: `277 passed`).
- **Não fazer:** não mudar a tabela de modelo por fase; não editar `CHANGELOG.md` (registro histórico); não editar `C:\Users\panta\.claude\`.
- **Contingências:**
  - se um bloco **Texto atual** não for encontrado **exatamente uma vez** no arquivo indicado → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco
  - se `kit_check.ps1 -Mode check-drift` ou `check-readme.ps1` sair diferente de `0` → parar e sinalizar `blocked` razão `ferramenta`, colando a última linha da saída
  - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina e espelho; nenhum teste prende os literais trocados (medido em 2026-09-24). TR: a suíte inteira.
- **Verificação:** no PowerShell 7 (`pwsh`), na raiz do repositório; **antes** medido em 2026-09-24, **depois** medido pelo consultor sobre cópia com as três substituições aplicadas.
  1. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'e o modelo ativo, **para** e pede o `/model` correto ao dono').Count` — antes `1`, depois `0`
  2. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'exige, **para** e pede ao dono o `/model` do modelo melhor').Count` — antes `0`, depois `1`
  3. `(Select-String -Path GOVERNANCA.md -SimpleMatch '**nunca para para rebaixar o modelo**').Count` — antes `1`, depois `2`
  4. `(Select-String -Path README.md -SimpleMatch 'confere contra o modelo ativo e **para** para pedir o `/model` correto').Count` — antes `1`, depois `0`; `(Select-String -Path README.md -SimpleMatch '**abaixo** do exigido **para** para pedir o `/model` do modelo melhor').Count` — antes `0`, depois `1`
  5. `(Select-String -Path README.md -SimpleMatch 'Quando o gate dispara, ele para e pede uma').Count` — antes `1`, depois `0`; `(Select-String -Path README.md -SimpleMatch 'decidir sozinho e seguir').Count` — antes `1`, depois `0`
  6. `(Select-String -Path README.md -SimpleMatch 'agente seguir sozinho num modelo mais fraco').Count` — antes `0`, depois `1`; `(Select-String -Path README.md -SimpleMatch 'orquestra, nunca interrompe o trabalho').Count` — antes `0`, depois `1`
  7. Discriminante das cinco superfícies: `(Select-String -Path GOVERNANCA.md,README.md,.claude/skills/scrum-master/SKILL.md,.claude/skills/modelo-por-fase/SKILL.md,.claude/global/hooks/modelo_por_fase_userpromptsubmit.py -SimpleMatch '`/model` correto').Count` — antes `2`, depois `0`
  8. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift; $LASTEXITCODE` — antes e depois `0`
  9. `pwsh -NoProfile -File .claude/checks/check-readme.ps1; $LASTEXITCODE` — antes e depois `0`
  10. `python -m pytest -q` — total de `passed` ≥ o medido no despacho, `0 failed`
- **Pronto quando:** nenhuma superfície do kit manda parar para rebaixar o modelo nem pede o `/model` "correto" em qualquer divergência, e `GOVERNANCA.md` e `README.md` dizem o mesmo que a skill do loop, a `modelo-por-fase` e o hook — acima do indicado segue e anota, abaixo do indicado para e pede o melhor — Verificações 1 a 7; nenhum gate regrediu — Verificações 8 a 10. Fechada esta tarefa, o `Pronto quando` da `TK-78a` fica verdadeiro.
- **Fora do escopo desta tarefa:** as `systemMessage` do hook (`considere /model sonnet|haiku`), que sugerem ao dono sem mandar parar e que a `TK-78a` proibiu tocar; o `CHANGELOG.md`, que registra o gate de parada como história.

**Texto atual 1** — `GOVERNANCA.md` (§3, bullet *Gatilho operacional do modelo por fase*, linha única):

~~~~
  detecta a fase da tarefa e o modelo ativo, **para** e pede o `/model` correto ao dono (fato
~~~~

**Texto novo 1:**

~~~~
  detecta a fase da tarefa e o modelo ativo e, só quando o ativo está **abaixo** do que a fase
  exige, **para** e pede ao dono o `/model` do modelo melhor — acima do exigido segue e anota a
  divergência em uma linha, porque o contexto principal só orquestra e o modelo de cada tarefa
  viaja no despacho (linha *Orquestração* acima); o gate **nunca para para rebaixar o modelo** (fato
~~~~

**Texto atual 2** — `README.md` (§4, frase do gatilho operacional, linha única):

~~~~
da tarefa, confere contra o modelo ativo e **para** para pedir o `/model` correto. A correção fica com
~~~~

**Texto novo 2:**

~~~~
da tarefa e confere contra o modelo ativo: **acima** do exigido segue e anota a divergência em uma
linha — o contexto principal só orquestra, e o modelo de cada tarefa viaja no despacho —, e só
**abaixo** do exigido **para** para pedir o `/model` do modelo melhor. A correção fica com
~~~~

**Texto atual 3** — `README.md` (§4, parágrafo *Onde o gerente intervém* do modelo por fase, cinco linhas):

~~~~
**Onde o gerente intervém.** Quando o gate dispara, ele para e pede uma ação humana: trocar o modelo
com `/model` e confirmar. Três respostas são legítimas — trocar (o caso normal), autorizar
explicitamente a exceção (que fica registrada, com motivo, no plano ou no diário), ou reclassificar a
fase se o gate errou a classificação. O que **não** é legítimo é o agente decidir sozinho e seguir:
uma exceção não registrada vira precedente silencioso e a tabela deixa de valer na prática.
~~~~

**Texto novo 3:**

~~~~
**Onde o gerente intervém.** Só quando o modelo ativo está **abaixo** do que a fase exige: aí o gate
para e pede uma ação humana — subir o modelo com `/model` e confirmar. Três respostas são
legítimas — trocar (o caso normal), autorizar explicitamente a exceção (que fica registrada, com
motivo, no plano ou no diário), ou reclassificar a fase se o gate errou a classificação. O que
**não** é legítimo é o agente seguir sozinho num modelo mais fraco que o exigido: uma exceção não
registrada vira precedente silencioso e a tabela deixa de valer na prática. Modelo ativo **acima**
do exigido não dispara intervenção: o agente segue e anota a divergência em uma linha — rebaixar a
tela principal, que só orquestra, nunca interrompe o trabalho (ordem do dono de 2026-09-24).
~~~~

### TK-78b — A régua do card aprende as três lições da janela [Sonnet · esforço low · classe redacao]

- **Status:** `done` · 2026-09-24
- **Depende de:** `TK-78a`, `TK-78d`
- **Objetivo:** fixar na definição do planejador que card de investigação mantém o rótulo `Pronto quando`, que card que edita a configuração do harness declara a contingência de permissão recusada, e que verificação por total de diff sobre arquivo com alteração alheia mede delta contra a base do despacho.
- **Fundamento:** `AE-1`, `AE-2` (ii) e `AE-3` (i) do `P-0748`.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-planner.md`
- **Passos:**
  1. Em `.claude/agents/pantonic-planner.md`, substitua o **Texto atual 1** pelo **Texto novo 1**.
  2. Rode as Verificações.
- **Restrições desta tarefa:**
  - Substituição literal; o texto novo entra exatamente como está no bloco.
  - Não alterar a `description` do frontmatter (mudaria a região gerada de `.claude/README.md`).
  - Não tocar `.claude/tools/rdo.py` nem `review_evidence.py` — o rótulo se acerta na doutrina, não no parser.
  - Não reescrever card de plano nenhum para a forma nova.
  - Não commitar.
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui.
- **Não fazer:** não tocar os pacotes do `TK-72` nem `GOVERNANCA.md`.
- **Contingências:**
  - se o **Texto atual 1** não for encontrado **exatamente uma vez** → parar e sinalizar `blocked` razão `premissa`
  - se `python -m pytest -q` sair com total de `passed` menor que o medido no despacho, ou com qualquer `failed` → parar e sinalizar `blocked` razão `premissa`, colando a linha de sumário
- **Testes:** nenhum TF novo — o card edita doutrina. A guarda é a suíte inteira, que inclui `tests/test_doutrina_unidade.py` (prende literais de `.claude/agents/pantonic-planner.md`).
- **Verificação:** no PowerShell, na raiz do repositório; **antes** medido em 2026-09-24.
  1. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'por **o número ou fato que tem de existir ao final**').Count` — antes `1`, depois `0`
  2. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'Pronto quando (o fato que tem de existir ao final)').Count` — antes `0`, depois `1`
  3. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'o dono cola o bloco literal do card').Count` — antes `0`, depois `1`
  4. `(Select-String -Path .claude/agents/pantonic-planner.md -SimpleMatch 'contra a base re-medida no despacho').Count` — antes `0`, depois `1`
  5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift; $LASTEXITCODE` — antes e depois `0`
  6. `python -m pytest -q` — total de `passed` ≥ o medido no despacho, `0 failed`
- **Pronto quando:** as três regras estão escritas na definição do planejador — Verificações 1 a 4 —, e nenhum gate regrediu — Verificações 5 e 6.
- **Fora do escopo desta tarefa:** os pacotes do `TK-72`; ensinar ao parser um rótulo novo.

**Texto atual 1** — `.claude/agents/pantonic-planner.md`:

~~~~
Tarefa de `classe investigacao` troca "Passos" por **Método de sondagem** (corpus fechado, métricas,
formato e teto de linhas do agregado que volta — nenhum dado bruto entra em contexto) e "Pronto
quando" por **o número ou fato que tem de existir ao final**.
~~~~

**Texto novo 1:**

~~~~
Tarefa de `classe investigacao` troca "Passos" por **Método de sondagem** (corpus fechado, métricas,
formato e teto de linhas do agregado que volta — nenhum dado bruto entra em contexto) e mantém o
rótulo **Pronto quando**, escrito `- **Pronto quando (o fato que tem de existir ao final):**`: o
critério é o número ou fato que tem de existir ao final, e o rótulo é o que `rdo.py` e
`review_evidence.py` leem — rótulo trocado faz o gerador de evidência recusar o card.

Card que edita a configuração do harness (`.claude/settings*.json`, hooks) declara a contingência
de permissão: *se o modo de permissão recusar a edição → o dono cola o bloco literal do card e o
agente confere `json ok`*. O agente não contorna a recusa.

Verificação por total de diff (`git diff --numstat` ou equivalente) sobre arquivo que pode ter
alteração não commitada de outra frente mede o **delta** contra a base re-medida no despacho —
nunca o total contra `HEAD`, que outras entregas movem. Forma: base medida no despacho `<a> <r>`;
depois, removidas `= <r>` e adicionadas `≥ <a> + <n>`.
~~~~

### TK-78c — A evidência mede só o que mudou desde o despacho [Sonnet · esforço high · classe implementacao]

- **Status:** `done` · 2026-09-24
- **Depende de:** `TK-78a`
- **Objetivo:** o dossiê de evidência passa a mostrar, para cada arquivo-alvo, só o diff desde um instantâneo da árvore tirado no despacho — sem os hunks que outras frentes já tinham deixado —, e reconhece como caminho o alvo declarado com sufixo de seção (`<arquivo> §<n>`).
- **Fundamento:** `AE-1` (inconclusivo: `--desde` recolhe a árvore suja), `AE-2` (iii) e `AE-3` (ii) do `P-0748`. Medido em 2026-09-24: com `--desde d75e7a6` sobre árvore com 40+ arquivos modificados de outros planos, o trecho da skill-alvo da `TLG-T2` truncou em 4000 caracteres dentro de hunks do `P-0747` sem chegar à seção entregue; e `docs/plans/P-0748-tela-do-gerente.md §2.1` saiu como literal descartado, não como alvo. Depende do `TK-78a` porque as duas editam a skill scrum-master, em trechos distintos.
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
  - `.claude/skills/scrum-master/SKILL.md`
- **Contratos/classes:**
  - `review_evidence.py`: constante nova `_SECAO_REF_RE = re.compile(r"\s+§\S*$")`, aplicada em `_classificar_campo_alvos` **antes** de `_LINHA_REF_RE`: `candidato = _LINHA_REF_RE.sub("", _SECAO_REF_RE.sub("", bruto))`.
  - `_diff_para_arquivo(root: Path, caminho_rel: str, desde: str | None = None) -> str`: sem `desde`, comportamento atual intacto. Com `desde`: texto = `git diff <desde> -- <caminho_rel>`; não vazio → devolve; vazio e o caminho existe na árvore do `<desde>` (`git cat-file -e <desde>:<caminho_rel>` com exit `0`) → devolve a linha `(sem alteração desde <desde>)`, com `<desde>` entre crases; vazio e não existe no `<desde>` → o fallback atual (conteúdo integral do arquivo novo, ou a mensagem de ausente).
  - `montar_trechos(root, arquivos_alvo, teto_chars, tocados=None, desde=None)`: repassa `desde` às duas chamadas de `_diff_para_arquivo`; `montar_documento` passa o seu `desde` a `montar_trechos`.
  - `scrum-master` passo 4: a `<ref>` passa a ser a saída de `git stash create` (instantâneo dos arquivos rastreados, que não altera árvore, índice nem a lista de stash), ou `git rev-parse HEAD` quando a saída vem vazia (árvore limpa) — **Texto atual 1** → **Texto novo 1**.
- **Passos:**
  1. Escreva os três TF abaixo em `tests/test_review_evidence.py`, reusando os ajudantes do arquivo (`_load_review_evidence`, `_init_repo_com_baseline`, `_run_git`); rode-os e veja-os falhar.
  2. Implemente os contratos em `.claude/tools/review_evidence.py`; rode o arquivo de teste inteiro.
  3. Em `.claude/skills/scrum-master/SKILL.md`, substitua o **Texto atual 1** pelo **Texto novo 1**.
  4. Rode as Verificações.
- **Testes:**
  - TF `test_tf_alvo_com_sufixo_de_secao_e_caminho`: `extrair_arquivos_alvo` sobre um campo `arquivos-alvo` cujo único literal entre crases é `docs/x.md §2.1` devolve `["docs/x.md"]`.
  - TF `test_tf_trecho_desde_instantaneo_mostra_so_o_delta`: repositório com `a.md` commitado; edita `a.md` acrescentando a linha `linha-velha`; `snap = git stash create`; edita de novo acrescentando `linha-nova`; `montar_trechos(repo, ["a.md"], 4000, desde=snap)["a.md"]["texto"]` contém `+linha-nova` e não contém `+linha-velha`.
  - TF `test_tf_trecho_desde_sem_alteracao_nao_despeja_o_arquivo`: mesmo arranjo, sem a segunda edição; o texto é exatamente a linha `(sem alteração desde <snap>)`, com `<snap>` entre crases.
  - TR: o arquivo inteiro `tests/test_review_evidence.py` verde, inclusive `test_tr_sem_desde_nada_muda`; a suíte inteira.
- **Restrições desta tarefa:**
  - Sem `--desde`, a saída do gerador é byte a byte a de antes (TR `test_tr_sem_desde_nada_muda`).
  - `git stash create` só lê: nenhum passo roda `git stash push`, `git stash apply` nem altera a lista de stash.
  - Não tocar `coletar_arquivos_tocados` nem `coletar_estado_git` (já aceitam `desde`), nem o atribuidor `--atribuir` (`TK-66`).
  - Não commitar.
  - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho sobe em exatamente `3`.
- **Não fazer:** não mudar o teto de 4000 caracteres; não mudar a gramática de caminho da `DB-27` além do sufixo de seção.
- **Contingências:**
  - se o **Texto atual 1** não for encontrado **exatamente uma vez** → parar e sinalizar `blocked` razão `premissa`
  - se `git stash create` sair diferente de `0` numa árvore suja → parar e sinalizar `blocked` razão `ferramenta`, colando a linha de erro
  - se algum teste preexistente de `tests/test_review_evidence.py` ficar vermelho → parar e sinalizar `blocked` razão `premissa`, colando o nome do teste
- **Verificação:** no PowerShell, na raiz do repositório; **antes** medido em 2026-09-24.
  1. `python -m pytest tests/test_review_evidence.py -q` — depois, os três TF novos verdes e `0 failed`
  2. `python -m pytest -q` — total de `passed` = o medido no despacho `+ 3`, `0 failed`
  3. `(Select-String -Path .claude/skills/scrum-master/SKILL.md -SimpleMatch 'git stash create').Count` — antes `0`, depois `1`
  4. `(Select-String -Path .claude/skills/scrum-master/SKILL.md -SimpleMatch 'Capturar `git rev-parse HEAD` como `<ref>`').Count` — antes `1`, depois `0`
- **Pronto quando:** o trecho de diff de um arquivo-alvo mostra só o que mudou desde o instantâneo do despacho, e alvo com sufixo de seção é caminho — Verificações 1 e 2; o loop captura o instantâneo no passo 4 — Verificações 3 e 4.
- **Fora do escopo desta tarefa:** a atribuição por `status` do `--atribuir` (`TK-66`); a atribuição por hunk.

**Texto atual 1** — `.claude/skills/scrum-master/SKILL.md` (passo 4):

~~~~
  `docs/telemetria.tsv`. Capturar `git rev-parse HEAD` como `<ref>` (schema `DP-S`), usada no
  passo 6 (`AUT-T5b`).
~~~~

**Texto novo 1:**

~~~~
  `docs/telemetria.tsv`. Capturar como `<ref>` (schema `DP-S`) a saída de `git stash create` —
  instantâneo dos arquivos rastreados no despacho, que não altera árvore, índice nem a lista de
  stash —, ou `git rev-parse HEAD` quando ela vier vazia (árvore limpa); usada no passo 6
  (`AUT-T5b`), onde o trecho de cada alvo passa a mostrar só o que mudou desde o despacho.
~~~~

### Achados da execução (TK-78)

- **`AE-1` (2026-09-24, laudo da `TK-78a`, `ressalva` 91, recomendação `escalar`, alvo `dossiê`)** — o `Pronto quando` da `TK-78a` segue falso: `GOVERNANCA.md` §3, bullet *Gatilho operacional do modelo por fase* (~linha 121, "para e pede o `/model` correto ao dono"), e `README.md` §4 (~linha 343, "**para** para pedir o `/model` correto"; e o parágrafo *Onde o gerente intervém*, ~linhas 353-358, que declara ilegítimo "o agente decidir sozinho e seguir") ainda mandam parar em qualquer divergência, inclusive para rebaixar. Os blocos Texto atual 1-9 não cobriram esses trechos, e as Verificações 5 e 6 contam só o literal substituído. **Rota:** `B1` → triagem do consultor. **Absorvido** (consultor, 2026-09-24, `rota=resolve`): card corretivo `TK-78d`, antes da `TK-78b` (`docs/plans/_CENARIO-TK-78.md`, `CT-1`).
- **`AE-2` (2026-09-24, orquestração, passo 3)** — `python .claude/tools/modelo.py check --plano TK-78` termina em `FileNotFoundError` com traceback, em vez de recusa limpa com exit `2`, quando o alvo é tíquete do diário (sem arquivo de plano nem modelo de domínio). O loop registrou a nota "sem modelo". **Rota:** `TK-66`/`TK-74` (facetas de instrumento).
- **`AE-3` (2026-09-24, orquestração, passo 2)** — `backlog.py next` devolveu *nada delegável* com a `TK-78c` `ready` e a dependência `done`: `_extrair_depende` lê todo literal entre crases do bullet **Depende de**, e o parêntese da `TK-78c` citava o caminho da skill `scrum-master` entre crases, que virou dependência inexistente. Reparo de forma pelo loop (crases tiradas do parêntese, conteúdo intacto). **Rota:** `TK-72` (regra de autoria: o bullet **Depende de** leva só ids entre crases) e `TK-66`/`TK-74` (o instrumento deveria aceitar só ids de tarefa, ou o `check` recusar dependência que não resolve).

## TK-79 — O executor devolve a linha de retorno seguida de prosa

- **Status:** `done` · 2026-09-25 — aberto no fechamento do `P-0748`, rota do `AE-23` daquele plano.

**Caso medido (2026-09-24):** os executores de `TLG-T5`, `TLG-T3e` e `TLG-T3f` devolveram a linha de retorno válida (`<ID> review`) seguida de parágrafos de relatório; o de `TLG-T3f` o fez com o despacho dizendo, por escrito, *"sem nenhuma prosa depois da linha"*. O loop leu a primeira linha e seguiu; o gancho do painel (`progresso_hook.py`) lê só a primeira linha não vazia do hand-back, então o painel não foi afetado. O que vier depois se perde sem registro.

**O que decide:** a forma do retorno do executor deixa de depender de o agente obedecer ao texto do despacho — ou a `A2` da `scrum-master` tipifica prosa depois da linha (reenvio de formato, ou descarte declarado), ou a definição do `pantonic-executor` fecha o retorno com guarda verificável. Par presença-ausência sobre a linha de retorno com e sem prosa.
- **Notas de execução:**
  - 2026-09-25 `done` — 1/1 card done (TK-79a); prosa depois da linha de retorno vira descarte declarado

### TK-79a — A prosa depois da linha de retorno é descartada por regra, não por sorte [Sonnet · esforço low · classe redacao]

- **Status:** `done` · 2026-09-25
- **Objetivo:** o retorno do executor com a linha válida seguida de prosa passa a ter tratamento escrito nas duas pontas: a definição do `pantonic-executor` diz que a última mensagem é só a linha, e que o que precisa chegar ao loop vai em `pendencia=`; a `scrum-master` tipifica, no passo 5 e na `A2`, que a linha válida seguida de prosa vale pela primeira linha não vazia (a mesma que o gancho do painel lê), com a prosa descartada sem reenvio e o descarte anotado no relatório — o resto deixa de se perder calado.
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md`
  - `.claude/agents/pantonic-executor.md`
- **Texto novo, literal** (antigo → novo):

  ```text
  [S1] .claude/skills/scrum-master/SKILL.md
  ou prosa no lugar da linha: **retorno inválido**, regra `A2`.
  → ou prosa no lugar da linha: **retorno inválido**, regra `A2`. Linha válida seguida de prosa **não** é retorno inválido: vale a primeira linha não vazia — a mesma que o gancho do painel lê —, a prosa depois dela é descartada sem reenvio de formato, e o descarte se anota numa linha do relatório de encerramento.

  [S2] .claude/skills/scrum-master/SKILL.md
  | `A2` | retorno ausente ou inválido (campo faltando, teto de campo estourado, linha fora da gramática) |
  → | `A2` | retorno ausente ou inválido (campo faltando, teto de campo estourado, linha fora da gramática, prosa no lugar da linha); prosa **depois** de linha válida não casa aqui — o passo 5 a descarta |

  [E1] .claude/agents/pantonic-executor.md
  6. **Encerramento**: sinalize `review` e encerre.
  → 6. **Encerramento**: sinalize `review` e encerre. A sua última mensagem é **só** a linha de retorno do despacho, sem nada antes nem depois: o loop lê a primeira linha não vazia e descarta o resto sem ler; o que precisa chegar a ele vai em `pendencia=`, numa linha.
  ```
- **Caso medido que motivou (2026-09-24 e 2026-09-25):** os retornos de `TLG-T5`, `TLG-T3e` e `TLG-T3f` do `P-0748`, e o da `CAH-T2` do `P-0750` (`AE-4`, anexo), trouxeram a linha válida seguida de parágrafos; o de `TLG-T3f` com a proibição escrita no despacho.
- **Passos:**
  1. Rodar a Verificação 1 e conferir os valores "antes".
  2. Aplicar `S1`, `S2`, `E1` com `Edit`.
  3. Rodar a Verificação 1 e 2.
- **Não fazer:** não tocar as demais linhas das tabelas dos blocos A e B, a gramática do passo 4, o `progresso_hook.py` nem o repertório `M-*`.
- **Contingências:**
  1. se algum texto antigo não aparecer exatamente uma vez no arquivo → parar e sinalizar `blocked motivo=dependencia`, devolvendo o código da troca.
- **Testes:** nenhum novo (redação); a suíte inteira roda como TR.
- **Verificação:**
  1. ```
     pwsh -NoProfile -Command '$s = ".claude/skills/scrum-master/SKILL.md"; $e = ".claude/agents/pantonic-executor.md"; "S1=" + @(Select-String -LiteralPath $s -SimpleMatch -Pattern "Linha válida seguida de prosa").Count + " S2=" + @(Select-String -LiteralPath $s -SimpleMatch -Pattern "prosa **depois** de linha válida").Count + " E1=" + @(Select-String -LiteralPath $e -SimpleMatch -Pattern "**só** a linha de retorno").Count'
     ```
     → **S1=1 S2=1 E1=1**. **Medido na autoria: S1=0 S2=0 E1=0**.
  2. `python -m pytest tests -q` → nenhuma falha, total igual ao da referência do despacho.
- **Pronto quando:** o passo 5 e a `A2` da `scrum-master` distinguem prosa **no lugar** da linha (inválido, reenvio) de prosa **depois** dela (descarte declarado), e a definição do executor fecha a última mensagem na linha — Verificação 1.

## TK-80 — A régua de autoria do card: valor de aceite fora de `pendencia=` e rótulo de investigação que o parser conhece

- **Status:** `cancelled` · 2026-09-24 — aberto no fechamento do `P-0748`, rota do `AE-13` e da parte de doutrina do `AE-1` daquele plano (o `TK-78`, destino previsto, fechou `done` sem elas).

**Casos medidos (2026-09-24):** (i) `AE-13` — a Verificação 5 da `TLG-T4a` mandou colar os valores medidos na linha de retorno, cujo único campo livre é `pendencia=`; a regra `B1` da `scrum-master` leu isso como pendência substantiva e escalou ao consultor, que recusou a escalada como improcedente (`DTG-40`). (ii) `AE-1` — `.claude/agents/pantonic-planner.md` manda o card de `classe investigacao` trocar *Pronto quando* por *"o número ou fato que tem de existir ao final"*, e o `rdo.py`/`review_evidence.py` exigem `pronto-quando`: todo card de investigação escrito ao pé da letra é recusado pelo gerador de evidência.

**O que decide:** a régua de autoria do card (residência do `pantonic-planner` e a rubrica de criação de tarefa) passa a dizer que valor medido de aceite nunca viaja em `pendencia=`, e o rótulo do card de investigação passa a ser um que o parser aceita (ou o parser passa a aceitar o rótulo da doutrina) — uma residência, sem duas redações do mesmo fato. Relação: vizinho do `TK-72` (régua de autoria, pacotes do `P-0746`), sem absorvê-lo.
- **Notas de execução:**
  - 2026-09-24 `cancelled` — absorvido pelo TK-72 (revisão de pertinência de 2026-09-24): mesma família — régua de autoria de card — e residência vizinha; os dois casos (AE-13 e AE-1 do P-0748) viram os Pacotes 9 e 10 do TK-72

## TK-81 — Propagar o painel do gerente aos cinco kits derivados

- **Status:** `cancelled` · 2026-09-26 — aberto no fechamento do `P-0748` (`DTG-8`: a propagação é ato de sincronização próprio, fora do plano).

**O que o hub tem e os derivados não:** o gancho `.claude/tools/progresso_hook.py` (eventos `PreToolUse`, `PostToolUse`, `UserPromptSubmit` e `Stop`) com `tests/test_progresso_hook.py`; a declaração dele em `.claude/projecoes.json`, materializada em `.claude/settings.json`; na `scrum-master`, a seção *Repertório de mensagens ao gerente* (24 frases) e o guardrail do painel; o trecho do `README.md` que ensina a abrir o painel (`Get-Content -Path .claude/estado/progresso.txt -Wait -Tail 30 -Encoding utf8`). Documento de validação: `docs/OPERACOES_AS_IS_P-0748.md`.

**O que decide:** cada derivado passa a gerar o painel nas próprias janelas de execução, preservando as divergências por linha que cada kit já carrega (a linha container tem divergências de transporte a preservar). Aceite por derivado: o painel mostra a abertura de janela e o ciclo de uma tarefa real com o título no lugar da sigla.

**Premissa medida na autoria do card (2026-09-25) — caiu.** Os cinco derivados (`PantonicContainerForAWS`, `PantonicContainer`, `PantonicMonitor`, `PantonicScanlator`, `PantonicPatom`, em `D:\workspaces\`) não têm o loop de execução em que o painel se apoia: nenhum tem `.claude/tools/`, `.claude/settings.json`, `.claude/KIT_VERSION` nem `.claude/sync-kit.ps1`; quatro têm só as skills `audit-sweep`, `bootstrap-pantonic`, `diario-de-obras`, `guardrails-check`, `handover`, `integrar-poc` e `proximo-passo` — sem `scrum-master` —, e o `PantonicMonitor` não tem skill nenhuma; só o `PantonicScanlator` é repositório git. O painel é gerado pelos eventos do loop (`backlog.py next`/`status`, despacho de agente); levar só o gancho produz painel vazio. A rota é decisão do dono.
- **Notas de execução:**
  - 2026-09-25 `blocked` — o card TK-81a espera a decisão do dono sobre como os derivados recebem o kit (premissa medida em 2026-09-25)
  - 2026-09-26 `cancelled` — dono, 2026-09-26: a publicação do kit aos derivados será feita por plano, não por tarefa; subtarefa TK-81a cancelada

### TK-81a — Levar o kit atual, e com ele o painel, aos derivados [Sonnet · esforço medium · classe implementacao]

- **Status:** `cancelled` · 2026-09-26 — parte do plano de publicação do kit; o dono o pauta no momento apropriado
- **Objetivo:** cada derivado passa a gerar o painel do gerente nas próprias janelas de execução,
  pela rota que o dono escolher.
- **A decisão pendente (vai ao dono no relatório):**
  - **(a) Atualizar cada derivado ao kit atual inteiro** — skills, agentes, `tools/`, projeções e
    `settings.json` —, preservando as divergências de cada linha (a linha container não tem
    PySide6 e fala em fronteira de transporte). O painel vem junto. Implica um card por derivado,
    escrito no ato da decisão, cada um com aceite pelo painel de uma tarefa real.
  - **(b) Adotar nos derivados o consumo por `git subtree` e `sync-kit.ps1`** (`GOVERNANCA.md`
    §10). Implica tornar repositório git os quatro que não são, antes de qualquer sincronização.
  - **(c) Cancelar** — os derivados ficam no kit antigo até um teste em projeto real pedir a
    atualização.
- **Arquivos-alvo:**
  - `.claude/` de cada derivado escolhido — na opção (a) ou (b)
- **Verificação:** por derivado, depois da rota escolhida:
  1. `Test-Path <derivado>\.claude\tools\progresso_hook.py` — antes `False`, depois `True`
  2. `python -m pytest tests/test_progresso_hook.py -q`, na raiz do derivado → verde
- **Pronto quando:** cada derivado da rota escolhida tem o loop e o gancho do painel, com a suíte
  do gancho verde nele.
- **Ao destravar:** a opção (a) abre um card por derivado neste tíquete, na forma de *Formato de
  uma tarefa*; a (b), um card de preparação git por derivado antes; a (c) cancela o tíquete.
- **Notas de execução:**
  - 2026-09-26 `cancelled` — dono, 2026-09-26: a publicação do kit aos derivados será feita por plano, não por tarefa

## TK-82 — `rdo.py` imprime em cp1252 no pipe do Windows

- **Status:** `done` · 2026-09-25 — aberto pelo `scrum-master` na janela do `P-0749`, rota do achado de processo do laudo da `SAN-T3a` (regra `A9`, sem reabrir a tarefa).

**Caso medido (2026-09-25):** a Verificação 4 da `SAN-T3a` mede só o exit 0 do `--help`; o texto reescrito sai, no pipe do Windows, em cp1252 (`Diret\xf3rio`, `t\xedquete`). O `review_evidence.py` reconfigura `stdout` para UTF-8 (`.claude/tools/review_evidence.py`, linhas 158-161); o `rdo.py` não. Defeito anterior à `SAN-T3a`, fora dos alvos dela.

**O que decide:** o `rdo.py` força UTF-8 na saída como o `review_evidence.py`, uma forma só entre os instrumentos do kit. Par presença-ausência: `python .claude/tools/rdo.py close --help` redirecionado a arquivo contém `Diretório` em UTF-8 com a mudança e não contém sem ela.
- **Notas de execução:**
  - 2026-09-25 `done` — 1/1 card done (TK-82a); rdo.py escreve em UTF-8 antes do argparse

### TK-82a — `rdo.py` escreve em UTF-8 antes de argparse abrir a boca [Sonnet · esforço low · classe implementacao]

- **Status:** `done` · 2026-09-25
- **Objetivo:** `main()` de `.claude/tools/rdo.py` reconfigura `sys.stdout` e `sys.stderr` para UTF-8 antes de `parser.parse_args(argv)`, pela mesma forma de `.claude/tools/review_evidence.py` (`_forcar_utf8`: `reconfigure(encoding="utf-8", errors="replace")` quando o stream tem `reconfigure`), de modo que `--help`, mensagens de erro e as linhas `rdo: …` saiam em UTF-8 no pipe do Windows.
- **Arquivos-alvo:**
  - `.claude/tools/rdo.py`
  - `tests/test_rdo.py`
- **Caso medido que motivou (2026-09-25, re-medido no ato da autoria):** `PYTHONIOENCODING= python -X utf8=0 .claude/tools/rdo.py close --help > h.tmp` → exit `0`, e os bytes de `h.tmp` contêm `Diretório` em cp1252 (`b"Diret\xf3rio"`) e **não** em UTF-8.
- **Testes (novo, em `tests/test_rdo.py`):** TF par presença-ausência por subprocesso com ambiente hostil explícito (`PYTHONIOENCODING` vazio no `env`, `-X utf8=0`, `stdout=subprocess.PIPE`): `rdo.py close --help` sai exit `0` e os bytes da saída contêm `"Diretório".encode("utf-8")` e não contêm `"Diretório".encode("cp1252")`. Sobre o `main()` anterior o teste falha no Windows (medido acima).
- **Verificação:**
  1. `python -m pytest tests/test_rdo.py -q` → verde, com o teste novo.
  2. `python -m pytest tests -q` → nenhuma falha; total = o da referência do despacho mais 1.
- **Pronto quando:** em `main()` a reconfiguração precede `parse_args`; sob o ambiente hostil explícito, `rdo.py close --help` redirecionado sai em UTF-8; o teste é par presença-ausência por subprocesso.
- **Não fazer:** não importar `review_evidence.py` de dentro do `rdo.py` (copiar a função de 4 linhas, como os demais pontos de carga); não trocar acentos do texto de ajuda por ASCII.

## TK-83 — O tíquete nasce executável

- **Status:** `cancelled` · 2026-09-25 — aberto por ato do dono.

**Ato do dono (2026-09-25), verbatim:** *"Eu acho que não deveria haver a separação, e na hora em
que for identifcado o problema, ele já deveria ser de algum modo inserido no fluxo de trabalho.
Tenho tentado esgotar o backglo, a prioridade é essa, mas esses tíquetes tem frustrado esse
objetivo, sendo trabalho a ser realizado, mas não podendo ser realizado. Ajuste essa governança,
não vejo ganho, só perdas nessa sistemática."*

**Caso medido (2026-09-25):** oito tíquetes `ready` no índice e `backlog.py next` respondendo
`nada delegável — 0 elegível(is)` — nenhum tinha card.

**Doutrina publicada na mesma sessão, fora de card:** skill `diario-de-obras` — seção nova
*Tíquete nasce executável*, significado de `ready`, estados do tíquete (sem `triage`), a linha do
tíquete na tabela de residência e a operação 6, *Abrir tíquete*; `GOVERNANCA.md` §4.2; regra `A8`
da `scrum-master`; passo 3 do `pantonic-consultant`. No mesmo ato, os tíquetes abertos ganharam
card: `TK-55`, `TK-67`, `TK-70`, `TK-72`, `TK-73` e `TK-81`; o `TK-71` fechou por obsolescência.

**O que falta:** a guarda — nada no kit acusa tíquete vivo sem card.
- **Notas de execução:**
  - 2026-09-25 `cancelled` — absorvido pelo P-0751 — Esgotar o backlog antes da publicação do kit (DEB-2)

### TK-83a — O `check` acusa tíquete vivo sem card [Sonnet · esforço medium · classe implementacao]

- **Status:** `cancelled` · 2026-09-25
- **Objetivo:** `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo
  tíquete `## TK-<n>` cujo status não é `done`, `cancelled` nem `superseded` e que não tem nenhuma
  subtarefa `### TK-<n><letra>`; a skill `diario-de-obras` nomeia o código.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
  - `.claude/skills/diario-de-obras/SKILL.md`
  - `tests/fixtures/backlog/candidato_a_fechamento/docs/DIARIO_DE_OBRAS.md`,
    `tests/fixtures/backlog/contador_inbox/docs/DIARIO_DE_OBRAS.md`,
    `tests/fixtures/backlog/corpus/docs/DIARIO_DE_OBRAS.md` e
    `tests/fixtures/backlog/vermelho/docs/DIARIO_DE_OBRAS.md` — só pela contingência abaixo
- **Propriedades:**
  1. O `C-15` sai uma vez por tíquete vivo sem subtarefa, nomeando o tíquete.
  2. Tíquete terminal sem subtarefa não é acusado.
  3. As menções `C-1..C-14` do módulo passam a `C-1..C-15` (ou ao maior código vigente, se o
     `TK-55a` já tiver fechado).
- **Texto atual 1** (`.claude/skills/diario-de-obras/SKILL.md`, uma ocorrência):

  ~~~~
  aberto. No loop, achado com rota `tíquete` vai ao consultor, que abre o tíquete já com o card — o
  ~~~~

- **Texto novo 1** (as quebras são as do bloco):

  ~~~~
  aberto — o `backlog.py check` o acusa como `C-15`. No loop, achado com rota `tíquete` vai ao
  consultor, que abre o tíquete já com o card — o
  ~~~~

- **Medido na autoria (2026-09-25):** quatro fixtures têm tíquete vivo sem subtarefa —
  `candidato_a_fechamento` (`TK-4`), `contador_inbox` (`TK-1`), `corpus` (`TK-1`) e `vermelho`
  (`TK-2`); a fixture `verde` tem `TK-1` com `TK-1a`.
- **Testes (novos, em `tests/test_backlog.py`):**
  - TF par sobre cópia da fixture `verde`: como está → nenhum `C-15`; com a subtarefa `TK-1a`
    removida → um `C-15` que nomeia `TK-1`.
  - TF: a mesma cópia sem `TK-1a` e com `TK-1` em `cancelled` (seção e índice) → nenhum `C-15`.
- **Verificação:**
  1. `python -m pytest tests/test_backlog.py -q` → verde, com os testes acima.
  2. `python .claude/tools/backlog.py check` na árvore → `check: OK — nenhuma violação.`
  3. `(Select-String -Path .claude/skills/diario-de-obras/SKILL.md -SimpleMatch 'o acusa como').Count` — antes `0`, depois `1`.
  4. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho mais os testes novos
     (referência medida na autoria: `360 passed`, 2026-09-25).
- **Pronto quando:** o `check` acusa tíquete vivo sem card, com par em teste, e sai `OK` sobre a
  árvore.
- **Não fazer:** não mudar outro código de violação; não tocar `next`.
- **Contingências:**
  - se um teste existente ficar vermelho só por causa do `C-15` numa das quatro fixtures → acrescentar
    ao tíquete acusado dessa fixture uma subtarefa mínima `### TK-<n>a — Card de fixture [Sonnet ·
    classe mecanica]` com o mesmo status do tíquete; se, com isso, outra asserção do mesmo teste
    mudar de resultado → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
  - se a Verificação 2 acusar `C-15` na árvore → parar e sinalizar `blocked` razão `premissa`,
    colando as violações.
- **Notas de execução:**
  - 2026-09-25 `cancelled` — absorvido pelo P-0751 como EBK-T1 (DEB-2)

## TK-84 — `review_evidence.py --desde` lista não rastreado anterior ao despacho

- **Status:** `done` · 2026-09-26 — aberto pelo consultor do `P-0751` (acionamento 4, `DEB-9`), rota do achado (3) do laudo da `EBK-T5` (`AE-2` do plano).

**Caso medido (2026-09-26):** a evidência da `EBK-T5` (`--desde 671e4b1`, commit de 2026-09-25 23:41:37) listou 19 arquivos não rastreados como "fora dos alvos e sem atribuição", todos anteriores ao commit; o reviewer os reconciliou à mão pela data de modificação. Na árvore, 228 não rastreados: 223 com data de modificação anterior ao `671e4b1` e 5 posteriores, todos da janela da `EBK-T5`. O `coletar_arquivos_tocados` põe todo `??` do `git status` na lista, com ou sem `desde`. Mesmo defeito recorreu em todos os laudos do `P-0748` (`## TK-55`, ponteiro para `AE-4`/`AE-5`/`AE-11`); a rodada de planejamento de 2026-09-25 do `TK-55` o deu por "sem ação" com 3 arquivos no `TK-68a`, e o caso de 19 com reconciliação refeita em cada laudo o supera.

**O que decide:** com `desde`, não rastreado cuja data de modificação é anterior à data do commit de `desde` sai da lista de tocados; o posterior fica. Correção conhecida, card `ready`.
- **Notas de execução:**
  - 2026-09-26 `ready` — aberto com o card TK-84a (consultor P-0751, acionamento 4)
- **AE-82** (`TK-84a`, fechamento, 2026-09-26) — execução inline pelo condutor sem ref capturada nem medida do executor; a doutrina não previa o caminho **Rota:** TK-88b (fechado: --nao-medido e captura de ref fora do loop em GOVERNANCA.md §4.2)
- **AE-83** (`TK-84a`, fechamento, 2026-09-26) — card do TK-84a promete o ramo de caminho ausente com escape octal sem Verificação nem teste que o exercite (RUBRICA 8 (xvii)); exercitado pelo revisor e conforme **Rota:** auditoria final



### TK-84a — Com `--desde`, o não rastreado anterior ao ref sai dos tocados [Sonnet · esforço low · classe implementacao]

- **Status:** `done` · 2026-09-26
- **Objetivo:** em `coletar_arquivos_tocados` de `.claude/tools/review_evidence.py`, com `desde`
  informado, cada entrada `??` do `git status` cujo arquivo tem data de modificação (`st_mtime`)
  menor que a data de commit de `desde` (`git show -s --format=%ct <desde>`, em segundos) deixa de
  entrar na lista; a de data igual ou maior entra como hoje. Caminho que não existe no disco como
  veio do `git status` (nome entre aspas com escape octal, por exemplo) entra como hoje, sem erro.
  Sem `desde`, nada muda. A docstring da função deixa de dizer que o não rastreado "entra sempre".
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
- **Caso medido que motivou:** ver `## TK-84`.
- **Reparo medido (protótipo do consultor, 2026-09-26, cópia da árvore já apagada):** ler `%ct` de
  `desde` uma vez com o `_git` do módulo e, no laço das entradas `??`, pular a que tem
  `(root / caminho).stat().st_mtime < corte`. Com ele, `tests/test_review_evidence.py` inteiro
  verde e suíte sem falha; o teste abaixo falha sobre o `review_evidence.py` de hoje.
- **Testes (novo, em `tests/test_review_evidence.py`, nome começado por `test_coletar_nao_rastreado_anterior_ao_desde`):** TF par sobre `_init_repo_com_baseline`:
  `ref` = `HEAD`, `ct` = `%ct` de `ref`; `src/velho.py` criado com `os.utime` em `ct - 60` e
  `src/novo.py` com `os.utime` em `ct + 60` → `coletar_arquivos_tocados(repo, desde=ref)` contém
  `src/novo.py` e não contém `src/velho.py`; `coletar_arquivos_tocados(repo)` (sem `desde`) contém
  `src/velho.py`.
- **Verificação:**
  1. `python -m pytest tests/test_review_evidence.py -q -k nao_rastreado_anterior_ao_desde` → o teste novo verde — antes `exit 5`, depois `exit 0` (antes nenhum teste selecionado).
  2. `python -m pytest tests/test_review_evidence.py -q` → verde — antes `exit 0`, depois `exit 0`.
  3. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`.
- **Pronto quando:** com `desde`, não rastreado anterior ao commit de `desde` não aparece entre os
  tocados, provado pelo par, e sem `desde` a lista não muda.
- **Não fazer:** não mudar `coletar_estado_git` nem os baldes de `confrontar_escopo`; não trocar a
  data de commit pela data de autor; não ler data de modificação de arquivo rastreado.
- **Contingências:**
  - se um teste existente de `desde` cair com o reparo → parar e sinalizar `blocked` razão
    `premissa`, nomeando o teste (medido no protótipo: nenhum cai).
- **Notas de execução:**
  - 2026-09-26 `review` — corte por %ct de desde no laço ?? de coletar_arquivos_tocados; TF novo verde (vermelho sem o reparo); test_review_evidence 55 passed; suíte 421 passed
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-84a-com-desde-o-nao-rastreado-anterior-ao-ref-sai-dos-tocados.md`, veredito ressalva 94%

## TK-85 — O `rdo.py laudo` não tem onde pôr o motivo da dimensão, e recusa o alvo `dossiê`

- **Status:** `done` · 2026-09-27 — aberto pelo consultor do `P-0751` (acionamento 4, `DEB-9`), rota do achado (4) do laudo da `EBK-T5` (`AE-2` do plano).

**Caso medido (2026-09-26):** o `pantonic-reviewer` manda que o motivo de cada dimensão fora de `conforme` fique no laudo, e o `rdo.py laudo` não tem campo para ele; na revisão da `EBK-T5` o motivo de `criterio-de-pronto parcial` foi para o card *Lições aprendidas na tarefa*, que a rubrica reserva ao registro qualitativo de consumo. De passagem: a definição do agente grafa o alvo de achado `dossiê`, e o `--achado-processo` só aceita `dossie` (`_ALVOS_ACHADO` do `rdo.py`), embora imprima `dossiê` na tabela.

**O que decide:** o `rdo.py laudo` ganha `--motivo <dimensão> "<uma linha>"`, e o laudo, uma seção própria para ele; o `--achado-processo` aceita `dossiê` como sinônimo de `dossie`; a definição do reviewer nomeia a flag. Descartado nomear o card de lições como residência (mistura o motivo com o registro de consumo que a rubrica pôs ali). Correção conhecida, card `ready`.
- **Notas de execução:**
  - 2026-09-26 `ready` — aberto com o card TK-85a (consultor P-0751, acionamento 4)
- **AE-90** (`TK-85a`, fechamento, 2026-09-27) — execução fora do loop sem ref de despacho nem medida do executor: evidência sem recorte e sem consumo medido **Rota:** TK-88b (fechado: --nao-medido e captura de ref fora do loop em GOVERNANCA.md §4.2)


### TK-85a — `rdo.py laudo --motivo` e o alvo `dossiê` [Sonnet · esforço low · classe implementacao]

- **Status:** `done` · 2026-09-27
- **Objetivo:** em `.claude/tools/rdo.py`, subcomando `laudo`:
  1. flag nova `--motivo DIMENSAO LINHA`, repetível (`nargs=2`, `action="append"`), com recusa
     (`RdoValidationError`, exit diferente de `0`, nenhum laudo escrito) quando a dimensão não é
     uma das sete, quando o nível dela é `conforme`, ou quando a linha é vazia, tem `|` ou quebra de
     linha;
  2. o documento do laudo ganha, entre a tabela de níveis e `## Achado de processo`, a seção
     `## Motivo das dimensões fora de conforme`, com a tabela `| dimensão | nível | motivo |` (uma
     linha por `--motivo`, na ordem dada) ou o corpo `nenhum` sem a flag — a seção existe sempre,
     como a de achado;
  3. `--achado-processo` aceita `dossiê` como sinônimo de `dossie` (normalizado antes da
     validação; a tabela segue imprimindo `dossiê`).
  Em `.claude/agents/pantonic-reviewer.md`, a frase que começa por `O motivo de cada dimensão fora
  de` passa a nomear a flag `--motivo` do `rdo.py laudo` como o lugar do motivo, e diz que ele não
  vai ao card *Lições aprendidas na tarefa*.
- **Arquivos-alvo:**
  - `.claude/tools/rdo.py`
  - `tests/test_rdo.py`
  - `.claude/agents/pantonic-reviewer.md`
- **Caso medido que motivou:** ver `## TK-85`.
- **Reparo medido (protótipo do consultor, 2026-09-26, cópia da árvore já apagada):** os três itens
  acima em `cmd_laudo` e no `laudo_parser`; com eles, `tests/test_rdo.py` inteiro verde (nenhuma
  asserção existente depende da ordem das seções do laudo) e suíte sem falha; os dois testes abaixo
  falham sobre o `rdo.py` de hoje. Âncora no agente medida: a frase aparece uma vez no arquivo.
- **Testes (novos, em `tests/test_rdo.py`, com `_argv_laudo` e `rdo.main`; os do item 1 com nome começado por `test_laudo_motivo_`, o do item 2 `test_laudo_achado_dossie_acentuado`):**
  1. TF: `_argv_laudo(d, **{"criterio-de-pronto": "parcial"})` mais
     `--motivo criterio-de-pronto "falta o modo validate"` → exit `0` e o laudo contém
     `## Motivo das dimensões fora de conforme` e
     `| criterio-de-pronto | parcial | falta o modo validate |`; TR: `--motivo escopo "x"` com
     `escopo` `conforme` → exit diferente de `0`; sem `--motivo`, o laudo contém a seção com o corpo
     `nenhum`.
  2. TF: `--achado-processo dossiê "linha do achado"` → exit `0` e o laudo contém
     `| dossiê | linha do achado |`.
- **Verificação:**
  1. `python -m pytest tests/test_rdo.py -q -k "laudo_motivo or laudo_achado_dossie_acentuado"` → os testes novos verdes — antes `exit 5`, depois `exit 0` (antes nenhum teste selecionado).
  2. `python -c "from pathlib import Path;print(Path('.claude/agents/pantonic-reviewer.md').read_text(encoding='utf-8').count('--motivo')>=1)"` → `True` — antes `False`, depois `True`.
  3. `python -m pytest tests/test_rdo.py -q` → verde — antes `exit 0`, depois `exit 0`.
  4. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`.
- **Pronto quando:** o motivo de dimensão tem campo e seção própria no laudo, com recusa para
  dimensão `conforme`; `dossiê` é aceito como alvo; a definição do reviewer nomeia a flag.
- **Não fazer:** não mudar `calcular_laudo` nem o `close`; não tornar `--motivo` obrigatório; não
  mudar a tabela de níveis nem o card *Lições aprendidas na tarefa*.
- **Notas de execução:**
  - 2026-09-26 `review` — rdo.py laudo --motivo + alvo dossiê + reviewer nomeia a flag; 5 testes novos; test_rdo 66 verdes; suíte 426 verdes
  - 2026-09-27 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-85a-rdo-py-laudo-motivo-e-o-alvo-dossie.md`, veredito ressalva 94%

## TK-86 — O piso do `C-11` mora no código do `backlog.py` e acusa `C-17` em todo outro repositório

- **Status:** `done` · 2026-09-26 — aberto pelo consultor do `P-0751` (acionamento 8, `DEB-13`), rota do achado (1) do fechamento do plano (`AE-6` do plano).

**Caso medido (2026-09-26):** numa cópia de `tests/fixtures/backlog/verde`, sem alteração, `python .claude/tools/backlog.py check --repo <cópia>` sai `1` com `C-17 GOVERNANCA.md:1 — piso_c11 nomeia entrada órfã` (além do `C-16` do `TK-1a`, esperado: os cards da fixture não têm campos). O subcomando `check` passa a constante `_PISO_C11` do módulo para qualquer `--repo`, e a única entrada dela (`GOVERNANCA.md`, seção `1.1`, dívida medida neste repositório no `TK-60a`) não casa citação quebrada em outro corpus. O `backlog.py` vai aos derivados com a publicação do kit (`TK-81a`): lá o `check` nasceria vermelho sem defeito do derivado. Na árvore do hub, sem o piso, o `check` acusa 10 `C-11` dessa dívida.

**O que decide:** o piso é dado do corpus, não regra do instrumento — sai da constante e vai para `docs/PISO_C11.tsv`, versionado no repositório que tem a dívida; arquivo ausente é o estado normal de repositório sem dívida (nenhum piso, `C-11` julga tudo, nenhum `C-17`), no mesmo desenho do `tests/piso_comportamental.txt` do `ratchet_piso.py`. `docs/` não é projetado pelo `.claude/projecoes.json`, então o piso do hub não viaja. Supera, no `DEB-7` do `P-0751`, a parte "só o `main` liga o piso": o `main` liga o piso lido do `--repo`, e o `fechar_plano` do `.claude/tools/encerrar.py` (segundo consumidor, nascido no `TK-88`) liga o piso lido do repositório que fecha (`PC-1`, triagem do consultor, acionamento 1, `docs/plans/_CENARIO-TK-86.md`). Correção conhecida, card `ready`.
- **Notas de execução:**
  - 2026-09-26 `ready` — aberto com o card TK-86a (consultor P-0751, acionamento 8)
  - 2026-09-26 triagem do consultor (acionamento 1, `rota=resolve`, `PC-1`): o `TK-86a` parou `blocked` `premissa` porque o card omitiu o consumidor `encerrar.py:681` da constante; card emendado com o item 4 e devolvido a `ready`.
  - 2026-09-26 `done` — tíquete fechado pelo condutor: TK-86a done (aprovado com ressalva 94%); achados AE-77/AE-78 roteados a TK-92/TK-93
- **AE-77** (`TK-86a`, fechamento, 2026-09-26) — Doutrina: pantonic-executor.md item 5a e scrum-master Passo 5 fixam <P-n> = id do plano, forma que não cobre card de tíquete do diário; o executor gravou a medida como docs/RDO/evidencia/P-0751-TK-86a-medida.json e o review_evidence.py (id = stem DIARIO_DE_OBRAS, :787) não a achou (registro parcial no laudo). **Rota:** tíquete `TK-92` (card `TK-92a`: destino da medida numa função de `caminhos.py`, gravado pelo `card_check --gravar` sem caminho), aberto pelo consultor do `TK-86`, acionamento 2 (`PC-2`); o arquivo `P-0751-TK-86a-medida.json` fica com o nome que tem, citado pelos registros fechados do `TK-86a`
- **AE-78** (`TK-86a`, fechamento, 2026-09-26) — Dossiê de evidência: review_evidence.py não mostra hunk de arquivo untracked (.claude/tools/encerrar.py, trecho truncado em 4000 caracteres sem as linhas 680-683), e o --desde do redespacho deixa os itens da primeira execução fora da evidência. **Rota:** tíquete `TK-93` (card `TK-93a`: `<ref>` do despacho com os não rastreados e diff por conteúdo; o redespacho reusa o `<ref>` do primeiro despacho), aberto pelo consultor do `TK-86`, acionamento 2 (`PC-3`); descartado o recorte pelas âncoras do card



### TK-86a — O piso do `C-11` vem de `docs/PISO_C11.tsv` do repositório checado [Sonnet · esforço low · classe implementacao]

- **Status:** `done` · 2026-09-26
- **Objetivo:** em `.claude/tools/backlog.py`:
  1. a constante `_PISO_C11` sai; entram `_PISO_C11_ARQUIVO = "docs/PISO_C11.tsv"`,
     `_PISO_C11_CABECALHO = "arquivo\tsecao\torigem"` e a função pública
     `ler_piso_c11(repo: Path) -> tuple[set[tuple[str, str]] | None, list[Violacao]]`: arquivo
     ausente → `(None, [])`; primeira linha diferente do cabeçalho → `(set(), [Violacao("C-17",
     "docs/PISO_C11.tsv", 1, "cabeçalho fora do esquema")])`; linha não vazia com número de campos
     (separados por tabulação) diferente de 3, `arquivo` vazio ou `secao` fora de
     `^\d+(?:\.\d+)*$` → `Violacao("C-17", "docs/PISO_C11.tsv", <n>, "linha fora do esquema")` e a
     linha não entra no piso; as demais linhas entram como `(arquivo, secao)`;
  2. no `main`, subcomando `check`, as violações de `ler_piso_c11(repo)` vêm primeiro, seguidas das
     de `check(...)` com `piso_c11=` o conjunto lido (e não mais a constante); `check()` não muda
     de assinatura nem de comportamento;
  3. o comentário de origem da constante (medida de 2026-09-20, `TK-60a`) vai para a docstring de
     `ler_piso_c11`, e o comentário do `C-17` em `check` passa a dizer que o piso vem do arquivo do
     repositório checado;
  4. em `.claude/tools/encerrar.py`, `fechar_plano`: a chamada `_backlog.check(...)` do gate deixa
     de ler `_backlog._PISO_C11`; antes dela, `piso_c11, violacoes = _backlog.ler_piso_c11(repo)`, e
     as violações de `check(...)`, com `piso_c11=piso_c11`, somam-se a essas (`violacoes += ...`),
     na mesma ordem do `main`.
  Na raiz, o arquivo novo `docs/PISO_C11.tsv`, em UTF-8 com fim de linha LF, com o cabeçalho e a
  linha `GOVERNANCA.md<TAB>1.1<TAB>TK-60a, medido em 2026-09-20`.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
  - `docs/PISO_C11.tsv` (novo; `git check-ignore` sai `1`, medido: não é ignorado)
  - `.claude/tools/encerrar.py` (só a chamada do item 4, linhas 680-682 de hoje; o arquivo é do `TK-88`, cujos cards `TK-88b`..`TK-88d` também o tocam)
- **Caso medido que motivou:** ver `## TK-86`.
- **Reparo medido (protótipo do consultor, 2026-09-26, cópia da árvore já apagada):** os itens 1 e 2
  acima e o arquivo novo. Com eles: `check` da árvore OK exit `0`; cópia da `verde` só com o
  `C-16` do `TK-1a`; arquivo removido da árvore → 10 `C-11` e nenhum `C-17`; arquivo com uma
  entrada `GOVERNANCA.md`/`3.2` e uma linha `lixo` → `C-17 docs/PISO_C11.tsv:4 — linha fora do
  esquema` e o `C-17` da entrada órfã; suíte `376 passed`. Os dois testes abaixo falham sobre o
  `backlog.py` de hoje e passam com o protótipo.
- **Estado da árvore na retomada (medido pelo consultor, 2026-09-26, acionamento 1 do `TK-86`):**
  os itens 1 a 3, o arquivo novo e os dois testes já estão aplicados pela primeira execução
  (Verificação 1 exit `0`, 2 → `0`, 3 → `2 passed`, 4 → `114 passed`); falta só o item 4. Suíte
  com eles e sem o item 4: `427 passed, 1 failed`
  (`tests/test_encerrar.py::test_tf_plano_fecha_status_entrega_tres_secoes_e_linha_do_diario`,
  `AttributeError` em `_backlog._PISO_C11`). Item 4 ensaiado na árvore e revertido:
  `tests/test_encerrar.py` `15 passed`, suíte `428 passed`. Varredura de consumidores
  (`_PISO_C11` sem sufixo em `.claude`, `tests`, `docs`, `*.py`): só `encerrar.py:681`.
- **Testes (novos, em `tests/test_backlog.py`, com `_load_backlog`, `_copiar_fixture` e `capsys`; nome de cada um começado por `test_piso_c11_tsv_`):**
  1. TF: cópia de `_FIXTURE_VERDE` em `tmp_path / "repo"`; `backlog.main(["check", "--repo",
     str(repo)])` → a saída padrão não contém `C-17`.
  2. TR: na mesma montagem, `docs/PISO_C11.tsv` escrito com o cabeçalho, a linha
     `GOVERNANCA.md\t9.9\tteste` e a linha `lixo` → `main` devolve `1`; a saída contém
     `piso_c11 nomeia entrada órfã` com `9.9`, e `C-17 docs/PISO_C11.tsv:3 — linha fora do esquema`.
- **Verificação:**
  1. `python .claude/tools/backlog.py check` → `check: OK — nenhuma violação.` — antes `exit 0`, depois `exit 0`.
  2. `python -c "from pathlib import Path;t=Path('.claude/tools/backlog.py').read_text(encoding='utf-8');print(t.count('_PISO_C11')-t.count('_PISO_C11_'))"` → `0` (a constante `_PISO_C11` sem sufixo) — antes `0`, depois `0` (o antes é a árvore de hoje, com o item 1 já aplicado; antes da primeira execução era `2`).
  3. `python -m pytest tests/test_backlog.py -q -k piso_c11_tsv` → os testes novos verdes — antes `exit 0`, depois `exit 0` (o antes é a árvore de hoje, com os testes já aplicados; antes da primeira execução era `exit 5`).
  4. `python -m pytest tests/test_backlog.py -q` → verde — antes `exit 0`, depois `exit 0`.
  5. `python -m pytest -q` → nenhuma falha — antes `exit 1`, depois `exit 0` (antes `427 passed, 1 failed`, o teste do `encerrar.py`; depois `428 passed`).
  6. `python -c "from pathlib import Path;t=Path('.claude/tools/encerrar.py').read_text(encoding='utf-8');print(t.count('_PISO_C11')-t.count('_PISO_C11_'))"` → `0` (o `encerrar.py` não lê mais a constante) — antes `1`, depois `0`.
- **Pronto quando:** o `check` de um repositório sem `docs/PISO_C11.tsv` não acusa `C-17`, o do hub
  segue OK com o piso lido do arquivo, e linha malformada do arquivo sai `C-17` com a linha dela.
- **Não fazer:** não quitar a dívida do piso (tíquete próprio); não mudar `check()`, o `C-11` nem o
  `C-16`; não declarar o arquivo em `.claude/projecoes.json`; no `encerrar.py`, não tocar nada além
  da chamada do item 4 (o resto do arquivo é dos cards do `TK-88`); não desfazer os itens 1 a 3 já
  aplicados.
- **Contingências:**
  - se a Verificação 1 acusar `C-11` ou `C-17` na árvore → parar e sinalizar `blocked` razão
    `premissa`, colando as violações (medido no protótipo: nenhuma).
  - se `_PISO_C11` sem sufixo aparecer num arquivo fora dos Arquivos-alvo → parar e sinalizar
    `blocked` razão `premissa`, nomeando arquivo e linha (medido na retomada: nenhum além do
    `encerrar.py`).
- **Handover:** 2026-09-26 · para quem vier depois
  - **Entregue:** ler_piso_c11(repo) em .claude/tools/backlog.py:906 lê docs/PISO_C11.tsv do repo checado; main do check (backlog.py:2049) e gate de fechar_plano (.claude/tools/encerrar.py:680) usam o piso lido; a constante _PISO_C11 não existe mais
  - **Contrato:** repo sem docs/PISO_C11.tsv = sem piso e sem C-17; linha malformada do TSV sai C-17 com o número dela; check() inalterado de assinatura e comportamento
  - **Não refazer:** migração do piso para o TSV e os testes test_piso_c11_tsv_* (tests/test_backlog.py)
  - **Pendente:** quitar a dívida do piso (entrada GOVERNANCA.md 1.1) é tíquete próprio
- **Notas de execução:**
  - 2026-09-26 `blocked` — Verificação 5 vermelha: .claude/tools/encerrar.py:681 lê _backlog._PISO_C11 (consumidor fora dos Arquivos-alvo; a suíte do protótipo era 376, hoje 428) → AttributeError em tests/test_encerrar.py::test_tf_plano_fecha_status_entrega_tres_secoes_e_linha_do_diario. V1-V4 verdes. Diff do card aplicado e mantido na árvore (backlog.py, tests/test_backlog.py, docs/PISO_C11.tsv).
  - 2026-09-26 `ready` — consultor (acionamento 1 do `TK-86`, `PC-1`, `rota=resolve`): premissa procedente, defeito de autoria do card (consumidor da constante fora dos Arquivos-alvo; protótipo medido sobre a suíte de 376, antes do `encerrar.py`). Card emendado: item 4, `encerrar.py` nos Arquivos-alvo, estado da árvore na retomada, Verificações 2/3/5 com o antes de hoje e Verificação 6 nova. Resta só o item 4.
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-86a-o-piso-do-c-11-vem-de-docs-piso-c11-tsv-do-repositorio-checa.md`, veredito ressalva 94%

## TK-87 — O dossiê do último card de um plano leva as seções seguintes do plano

- **Status:** `done` · 2026-09-26 — aberto pelo consultor do `P-0751` (acionamento 8, `DEB-13`), rota do achado (2) do fechamento do plano (`AE-6` do plano).

**Caso medido (2026-09-26):** `python .claude/tools/backlog.py show EBK-T14` imprime, depois do card, as seções `## 6. Ordem de execução`, `## 7. Fora de escopo` e `## 8. Achados da execução` do `P-0751` (3 cabeçalhos `## ` no dossiê); o `next` imprimiu o mesmo no despacho. Em `_scan_items`, o item termina só no próximo cabeçalho de item (`HEADING_RE`, que exige ` — `), e `## 6. Ordem de execução` não é um. O `rdo.py` já corta no cabeçalho seguinte (`_SECTION_BREAK_RE`). No corpus de hoje (diário e todo `docs/plans/P-*.md`), 492 itens: 29 mudam de fim com o reparo, nenhum muda status, `Depende de` ou `Tipo`; dois vivos entre eles (`LF-T8` do `P-0742` e `PLS-T3` do `P-0744`), ambos com o mesmo defeito. Remedido pelo consultor do `P-0752` (acionamento 10): o dossiê de `show FPU-T10`, último card do `P-0752`, traz 3 linhas `## ` (as seções 6 a 8 do plano) — o mesmo defeito, e o `TK-87a` o cobre.

**O que decide:** o item termina também na primeira linha de cabeçalho de nível 1 ou 2 (`NIVEL_1_OU_2_RE`, já no módulo) fora de cerca de código. Descartado usar a fronteira do `rdo.py` (`^#{2,3} `): cortaria mais itens nas subseções `### ` dos tíquetes do diário (`TK-69`..`TK-74`, por exemplo), mudando o `show` e a posição das notas deles. A cerca importa: `TK-76a` e `TK-78a` citam, dentro de `~~~~`, textos que começam por `## `. Correção conhecida, card `ready`.
- **Notas de execução:**
  - 2026-09-26 `ready` — aberto com o card TK-87a (consultor P-0751, acionamento 8)

### TK-87a — O item do `backlog.py` termina no cabeçalho de nível 1 ou 2 seguinte [Sonnet · esforço low · classe implementacao]

- **Status:** `done` · 2026-09-26
- **Objetivo:** em `_scan_items` de `.claude/tools/backlog.py`, o fim do item (`fim_idx`) passa a
  ser o menor entre o de hoje (linha antes do próximo cabeçalho de item, ou a última do arquivo) e
  a linha antes da primeira linha, depois do cabeçalho do item, que casa `NIVEL_1_OU_2_RE` fora de
  cerca de código. Uma linha que começa por três crases ou por `~~~` abre ou fecha a cerca. O
  `texto`, o `linha_fim` e as extrações de status, `Depende de` e `Tipo` do item passam a ler só
  essa faixa. A regra vive numa função auxiliar, chamada uma vez em `_scan_items`.
- **Arquivos-alvo:**
  - `.claude/tools/backlog.py`
  - `tests/test_backlog.py`
- **Caso medido que motivou:** ver `## TK-87`.
- **Reparo medido (protótipo do consultor, 2026-09-26, cópia da árvore já apagada):** a auxiliar
  `_fim_na_secao(linhas, inicio_idx, fim_idx)` percorre de `inicio_idx + 1` a `fim_idx`,
  alternando a cerca, e devolve `j - 1` na primeira `NIVEL_1_OU_2_RE` fora dela. Com ela:
  `show EBK-T14` sem nenhuma linha `## `, `show TK-76a` ainda com o texto cercado, `check` da
  árvore OK, suíte `376 passed`. O teste abaixo falha sobre o `backlog.py` de hoje.
- **Testes (novo, em `tests/test_backlog.py`, com `_load_backlog`, nome começado por `test_scan_items_corta_no_nivel_2`):** TF sobre
  `backlog._scan_items(linhas, "p.md")`, com `linhas` = `# P-0999 — Plano`, vazia, `## 5. Tarefas`,
  vazia, `### X-T1 — Um [Sonnet · esforço low · classe implementacao]`, vazia,
  ``- **Status:** `ready` ``, vazia, `~~~~`, `## Dentro da cerca`, `~~~~`, vazia,
  `## 6. Ordem de execução`, vazia, `` `X-T1` ``, vazia, `## 8. Achados`, vazia, `- achado` → o
  item `X-T1` tem `linha_fim == 12`, o `texto` dele contém `## Dentro da cerca` e não contém
  `## 6. Ordem de execução`.
- **Verificação:**
  1. `python -c "import subprocess,sys;o=subprocess.run([sys.executable,'.claude/tools/backlog.py','show','EBK-T14'],capture_output=True,text=True,encoding='utf-8').stdout;print(sum(1 for l in o.splitlines() if l.startswith('## ')))"` → `0` (linhas `## ` no dossiê do último card do `P-0751`) — antes `3`, depois `0`.
  2. `python .claude/tools/backlog.py check` → `check: OK — nenhuma violação.` — antes `exit 0`, depois `exit 0`.
  3. `python -m pytest tests/test_backlog.py -q -k scan_items_corta_no_nivel_2` → o teste novo verde — antes `exit 5`, depois `exit 0` (antes nenhum teste selecionado).
  4. `python -m pytest tests/test_backlog.py -q` → verde — antes `exit 0`, depois `exit 0`.
  5. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`.
- **Pronto quando:** o dossiê do último card de um plano para no cabeçalho de nível 1 ou 2
  seguinte, e cabeçalho dentro de cerca não corta o item.
- **Não fazer:** não mudar `HEADING_RE` nem o `rdo.py`; não cortar em `### ` (tíquetes do diário têm
  subseções `### ` que são corpo); não mudar o teto `DB-7` de `_truncar`.
- **Contingências:**
  - se um teste existente cair com o reparo → parar e sinalizar `blocked` razão `premissa`,
    nomeando o teste (medido no protótipo: nenhum cai).
- **Handover:** 2026-09-26 · para quem vier depois
  - **Entregue:** _fim_na_secao em .claude/tools/backlog.py:303, chamada uma vez em _scan_items (.claude/tools/backlog.py:350); teste test_scan_items_corta_no_nivel_2 em tests/test_backlog.py:145
  - **Contrato:** o item de _scan_items termina antes do primeiro cabeçalho # ou ## fora de cerca de código (três crases ou ~~~); texto, linha_fim, status, Depende de e Tipo leem só essa faixa; ### continua sendo corpo
  - **Não refazer:** o corte em nível 1/2 com respeito à cerca já está coberto por teste; show EBK-T14 sai sem linhas ##
  - **Pendente:** nenhum
- **Notas de execução:**
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-87a-o-item-do-backlog-py-termina-no-cabecalho-de-nivel-1-ou-2-se.md`, veredito aprovado 100%

## TK-88 — O encerramento de tarefa e de plano vira um comando, com relatório em três seções e handover no card

- **Status:** `done` · 2026-09-26 — aberto pelo dono ("Torne mecânicos os encerramentos de tarefas e planos"), entregue na mesma sessão; aguarda a revisão.

**Caso medido (2026-09-26, fechamentos de `P-0745`..`P-0751`):** fechar uma tarefa eram quatro comandos em turnos separados — `modelo.py check`, `backlog.py status <ID> done`, `rdo.py close` com o pacote do laudo **redigitado** a partir do arquivo que `rdo.py laudo` já tinha gravado, e `telemetria.py append` conferindo a linha do hook — mais o achado `AE-<n>` editado no plano à mão. Fechar um plano era inteiramente manual: o instrumento recusava `ready → done` para plano (registrado no cabeçalho do diário em 2026-09-25, no fechamento do `P-0749`), e o parágrafo de fechamento, a linha do índice e a triagem dos achados eram escritos pelo condutor. O RDO só tinha a leitura de máquina; o que o dono lia era prosa redigida no cabeçalho do diário, sem forma fixa.

**O que decide:** um instrumento, `.claude/tools/encerrar.py`, com três verbos que compõem os instrumentos existentes sem reimplementar regra: `tarefa` (status → RDO → telemetria → achados, tudo depois de todas as checagens) e `plano` (status → relatório de entrega → linha do diário) **reportam** resultado e histórico; `handover` **entrega** — registra no próprio card, como campo `- **Handover:**` de máquina (`Entregue`, `Contrato`, `Não refazer`, `Pendente`, `para`), o que quem vem depois espera da tarefa, e o `backlog.py next` devolve esse campo à sucessora sob `=== HANDOVER DE <ID>`, junto com o dossiê dela (pedido do dono na mesma sessão). O RDO e o relatório de entrega ganham três seções de nível 1: `# Humano` (linguagem corrente, título no lugar da sigla, ≤ 8 linhas), `# Máquina` (dossiê verbatim, pacote transcrito do laudo, consumo, desdobramento) e `# Histórico` (as linhas do painel do gerente para a tarefa ou o plano). O `backlog.py` aceita `done` de plano quando toda tarefa é terminal. O gancho do painel reconhece o comando novo (`M-10` pela detecção de `encerrar.py tarefa`; `M-18` nova para o plano).

**Triagem do consultor (acionamento 1, 2026-09-26; laudo da `TK-88a` `ressalva 85`, bloqueante nenhuma, cenário em `docs/plans/_CENARIO-TK-88.md`):**
- **CT-1** — A pendência do laudo é defeito desta entrega e mais velho que ela: o gancho do painel lê `--tarefa`/`--plano`/`--atribuir` na linha de comando inteira e casa `encerrar.py`, `review_evidence.py` e `backlog.py status` em texto de argumento; com `telemetria.py append --tarefa <ID>-revisao` encadeado antes do `encerrar.py`, 14 frases `M-10` e 13 `M-11` saíram com o id `-revisao` no lugar do título, e as `M-11` foram copiadas ao `# Histórico` de 12 RDO; o `rdo.py close` grava o caminho do plano como o recebe, e o `encerrar.py` o passa com barra invertida (16 RDO). Corretivo `TK-88c`, que também conserta as RDO publicadas. A linha `M-10` que o defeito rotulou errado não se reconstrói nas RDO (omissão, não afirmação falsa), e `.claude/estado/progresso.txt` (estado local, fora do git) não se reescreve. Até o `TK-88c` fechar, o condutor roda `encerrar.py` sozinho na linha de comando, sem outro comando encadeado, e sem citar os nomes dos instrumentos em texto de `--achado`/`--resumo`.
- **CT-2** — A `TK-88a` não fecha agora. A linha de `docs/telemetria.tsv` com tarefa `TK-88a` e fonte `usage` (60 tool uses, 186.4 k tokens, 464.1 s) é a rodada do **revisor**: o hook `SubagentStop` a gravou porque `.claude/estado/tarefa-corrente.json` nomeava `TK-88a` no despacho do revisor, e ela repete a linha `TK-88a-revisao` logo abaixo (60, 186.4, 464.3). O `encerrar.py tarefa` de hoje a leria como consumo do executor — número de outra execução, que não fecha tarefa. Desfecho: tarefa sem `<usage>` fecha com `nao_medido` declarado e razão, pelo corretivo `TK-88b` (`--nao-medido`), que também tira da série a linha do revisor, restringe o hook ao executor e escreve a doutrina. Depois do `done` da `TK-88b`, o condutor fecha a `TK-88a` pelo comando registrado na nota dela.
- **CT-3** — Achado de processo "evidência sem `--desde`" (tarefa executada fora do loop): a doutrina da `TK-88b` manda capturar a ref do ponto de partida antes da primeira edição e gravar a medida do executor (`card_check --gravar`), e grava `tarefa-corrente.json` só no despacho do executor.
- **CT-4** — Achado de processo "pré-checagens duplicadas": `rdo.py` e `backlog.py` expõem a checagem sem escrita e o `encerrar.py` a chama — corretivo `TK-88d`, com a linha `FECHADO` contando como o índice e o stdout concordando em gênero. Descartado: declarar a duplicação na doutrina — a linha `FECHADO` (1/2 com uma `cancelled`) já diverge do índice (1/1), que é a cópia da regra divergindo.
- **Fila:** `TK-88b` → fechamento da `TK-88a` pelo condutor → `TK-88c` → `TK-88d`. A `FPU-T7` do `P-0752` segue dependendo só da `TK-88a`: não toca `encerrar.py` nem os alvos dos corretivos, e a `TK-88a` só fecha depois da `TK-88b`. A diretiva passa a incluir o `TK-88`.

- **Notas de execução:**
  - 2026-09-26 `review` — entregue: `encerrar.py` (2 verbos), template do RDO em 3 seções, regra de plano no `backlog.py`, `M-18` no gancho, doutrina em `GOVERNANCA.md` §4.2, skills `diario-de-obras`/`passagem-de-bastao`/`scrum-master`, README §9 e §11; testes `tests/test_encerrar.py` + 4 novos nas suítes tocadas; verbo `handover` e bloco `=== HANDOVER DE` do `next` acrescentados no mesmo dia, a pedido do dono.
  - 2026-09-26 `in-progress` — triagem do consultor (acionamento 1): corretivos TK-88b, TK-88c e TK-88d abertos; a TK-88a fecha depois do done da TK-88b (CT-1..CT-4)
- **AE-79** (`TK-88a`, fechamento, 2026-09-26) — painel do gerente: o gancho lê o argumento de tarefa e de plano na linha de comando inteira, e o RDO grava o caminho do plano com barra invertida **Rota:** TK-88c
- **AE-80** (`TK-88a`, fechamento, 2026-09-26) — tarefa executada fora do loop: evidência sem ponto de partida e fechamento sem medida **Rota:** TK-88b
- **AE-81** (`TK-88a`, fechamento, 2026-09-26) — pré-checagens de rdo e backlog copiadas no instrumento de fechamento **Rota:** TK-88d
- **AE-84** (`TK-88c`, fechamento, 2026-09-26) — review_evidence.py não expande glob dos Arquivos-alvo nem marca alvo não rastreado sem antes; a evidência da TK-88c saiu sem diff das 21 RDO **Rota:** auditoria final
- **AE-85** (`TK-88c`, fechamento, 2026-09-26) — variante publicada do painel com o id do tíquete no lugar do título do card fechado (RDO de TK-84a e TK-87a: 'concluiu a tarefa "TK-91"' e '"TK-86"') **Rota:** auditoria final
- **AE-86** (`TK-88d`, fechamento, 2026-09-26) — stdout do encerrar.py tarefa ainda diz 'tarefa fechado' (encerrar.py:958, 'encerrar: OK - {args.comando} fechado'); o item do Objetivo do TK-88d não entrou em Pronto quando nem em teste **Rota:** auditoria final
- **AE-87** (`TK-88d`, fechamento, 2026-09-26) — o card delegou à execução a escolha da recusa exercitada pelo TR (colisão de destino); escolha coerente, a regra de autoria já cobre o caso **Rota:** sem ação








### TK-88a — O fechamento de tarefa e de plano é um comando cada, com RDO e entrega em três seções e handover no card [Opus · esforço high · classe implementacao]

- **Status:** `done` · 2026-09-26
- **Objetivo:** `python .claude/tools/encerrar.py tarefa --plano <plano> --tarefa <ID> [--resumo] [--pendencia] [--achado TEXTO ROTA]... [--tool-uses --tokens-k --duracao-s]` leva a tarefa de `review` a `done` num ato só — gate do modelo, `backlog.transacionar_status` com a nota de fechamento, `rdo.cmd_close` com o pacote **transcrito do laudo** e as seções `# Humano`/`# Histórico` preenchidas, linha de telemetria (da série ou do trio do `<usage>`), `AE-<n>` com `**Rota:**` por achado —, e `python .claude/tools/encerrar.py plano --plano <plano> --veredito "<frase do dono>"` leva o plano a `done` — só sem tarefa aberta, com RDO de toda tarefa `done`, achado sem rota nenhum e documento de validação presente —, escreve `entrega.md`/`docs/plans/_ENTREGA-<id>.md` nas três seções e uma linha no cabeçalho do diário. Ambos recusam sem escrever quando falta insumo. O terceiro verbo, `python .claude/tools/encerrar.py handover --plano <plano> --tarefa <ID> --entregue "…" --contrato "…" [--nao-refazer] [--pendente] [--para <ID>]...`, escreve ou substitui o campo `- **Handover:**` no card (status `in-progress`/`review`/`done`/`blocked`), e `backlog.py next` imprime, sob `=== HANDOVER DE <ID>`, o handover de todo irmão que nomeia a próxima tarefa em `para` ou, sem nenhum, o da antecessora imediata.
- **Arquivos-alvo:**
  - `.claude/tools/encerrar.py` (novo)
  - `.claude/tools/rdo.py` — `cmd_close` ganha `HUMANO`/`HISTORICO` (`--humano`, `--historico`)
  - `.claude/tools/rdo_template.md` — as três seções `# Humano` / `# Máquina` / `# Histórico`
  - `.claude/tools/backlog.py` — `transacionar_status`: plano → `done` com toda tarefa terminal; `extrair_handover`/`handovers_para` e o bloco `=== HANDOVER DE` em `renderizar_next`
  - `.claude/tools/caminhos.py` — `destino_operacoes`, `destino_entrega`
  - `.claude/tools/progresso_hook.py` — detecção de `encerrar.py tarefa` (`M-10`) e `M-18`
  - `GOVERNANCA.md` §4.2 (*Fronteira de registro*, *Fechamento enxuto*); `README.md` §9 e §11
  - `.claude/skills/diario-de-obras/SKILL.md` (transição de plano, operação 7); `.claude/skills/passagem-de-bastao/SKILL.md` (Parte 3, itens 2-3); `.claude/skills/scrum-master/SKILL.md` (Passo 9, fechamento do plano, repertório `M-10`/`M-18`)
  - `tests/test_encerrar.py` (novo); `tests/test_rdo.py`, `tests/test_backlog.py`, `tests/test_progresso_hook.py`
- **Testes:** TF `tests/test_encerrar.py` — fechamento de tarefa escreve status, RDO em três seções (humano com título e revisão em palavras; máquina com pacote do laudo e consumo da série; histórico só com as linhas do título) e achado com rota; consumo por argumento apensa a série; fechamento de plano escreve status, entrega em três seções e linha do diário. TR — cada checagem recusa sem escrever (status ≠ `review`, laudo ausente, `reprovado`, consumo ausente; tarefa aberta, sem documento de validação, achado sem rota, `done` sem RDO). TF handover em `test_encerrar.py` (campo no card antes de `Notas`, substituição, transcrição no RDO; recusa em `ready`) e em `test_backlog.py` (`next` devolve o da antecessora; o endereçado em `para` vence). TF/TR em `test_backlog.py` (plano `ready → done`), `test_rdo.py` (três seções e mínimo honesto), `test_progresso_hook.py` (`M-10` pelo instrumento, `M-18`).
- **Verificação:**
  1. `python -m pytest tests/test_encerrar.py tests/test_rdo.py tests/test_backlog.py tests/test_progresso_hook.py tests/test_caminhos.py -q` → verde.
  2. `python .claude/tools/backlog.py check` → `check: OK — nenhuma violação.`, exit `0`.
  3. `python -m pytest -q` → nenhuma falha; `passed` ≥ 376 + os testes novos.
- **Pronto quando:** os dois verbos fecham tarefa e plano num comando cada, com as três seções, recusando sem escrever quando falta insumo, e as residências da doutrina (GOVERNANCA §4.2, as três skills, README) descrevem o instrumento como a forma canônica.
- **Não fazer:** não reimplementar regra de `backlog.py`/`rdo.py`/`telemetria.py` dentro do `encerrar.py`; não inventar número de consumo; não apagar o laudo.
- **Notas de execução:**
  - 2026-09-26 `review` — entrega na árvore; o próprio card se fecha por `python .claude/tools/encerrar.py tarefa --plano docs/DIARIO_DE_OBRAS.md --tarefa TK-88a --laudo <laudo>` depois do laudo do revisor.
  - 2026-09-26 `review` — laudo `ressalva 85`, bloqueante nenhuma, recomendação `escalar` (`docs/RDO/laudos/DIARIO_DE_OBRAS-TK-88a.md`); triagem do consultor em `CT-1`..`CT-4` do `## TK-88`. **Não fechar antes do `done` da `TK-88b`:** a única linha medida desta tarefa na série é a rodada do revisor (`CT-2`), e o `encerrar.py` de hoje a tomaria como consumo do executor. Depois dela, o condutor fecha esta tarefa com o comando abaixo, sozinho na linha de comando (`CT-1`); o laudo é o padrão (`docs/RDO/laudos/DIARIO_DE_OBRAS-TK-88a.md`):
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-88a-o-fechamento-de-tarefa-e-de-plano-e-um-comando-cada-com-rdo.md`, veredito ressalva 85%

    ```
    python .claude/tools/encerrar.py tarefa --plano docs/DIARIO_DE_OBRAS.md --tarefa TK-88a --nao-medido "executada na sessão principal, fora do loop: sem SubagentStop nem bloco de uso" --achado "painel do gerente: o gancho lê o argumento de tarefa e de plano na linha de comando inteira, e o RDO grava o caminho do plano com barra invertida" "TK-88c" --achado "tarefa executada fora do loop: evidência sem ponto de partida e fechamento sem medida" "TK-88b" --achado "pré-checagens de rdo e backlog copiadas no instrumento de fechamento" "TK-88d"
    ```

### TK-88b — A tarefa sem medida fecha declarando a ausência, e a rodada do revisor deixa de valer pela do executor [Sonnet · esforço high · classe implementacao]

- **Status:** `done` · 2026-09-26
- **Objetivo:** `python .claude/tools/encerrar.py tarefa --plano <plano> --tarefa <ID> --nao-medido "<razão>"` fecha a tarefa em `review` sem consumo medido: não procura linha na série, apensa a `docs/telemetria.tsv` a linha da tarefa com `fonte` `nao_medido` e as três células de consumo vazias, e o RDO traz `**Consumo:** não medido — <razão>` no lugar dos números. Recusa sem escrever quando vem junto do trio `--tool-uses/--tokens-k/--duracao-s`, quando a razão é vazia ou tem mais de uma linha, e quando a série já tem linha medida da tarefa (medida existente não se descarta). `rdo.py close` aceita o mesmo `--nao-medido "<razão>"` no lugar do trio, e exige exatamente um dos dois. O hook `SubagentStop` (`telemetria_hook.processar`) só grava e consome o estado quando o `agent_type` é `pantonic-executor` — o estado `tarefa-corrente.json` é do despacho do executor (skill `scrum-master`, Passo 4); outro papel do kit é silêncio, com o estado preservado. A série perde a linha com tarefa `TK-88a` e fonte `usage` (60 tool uses, 186.4 k tokens, 464.1 s), a rodada do revisor gravada sob o id do executor (`CT-2` do `## TK-88`); as demais linhas ficam intactas. A doutrina diz o desfecho (texto abaixo).
- **Arquivos-alvo:**
  - `.claude/tools/encerrar.py` — `fechar_tarefa`, `main` (flag `--nao-medido` do verbo `tarefa`)
  - `.claude/tools/rdo.py` — `cmd_close` e o parser do `close` (o trio deixa de ser obrigatório no argparse e passa a ser exigido por `cmd_close` quando falta `--nao-medido`)
  - `.claude/tools/rdo_template.md` — a linha `**Consumo:**`
  - `.claude/tools/telemetria_hook.py` — `processar` e a docstring do módulo (parágrafo *Filtro*)
  - `docs/telemetria.tsv` — só a linha da rodada do revisor sob `TK-88a`
  - `GOVERNANCA.md` §4.2 — fim do bullet *Fonte única da série*
  - `.claude/skills/scrum-master/SKILL.md` — Passo 9: o bloco do comando `encerrar.py tarefa` e o item (4) da telemetria
  - `.claude/skills/passagem-de-bastao/SKILL.md` — Parte 3, item 3 (*Telemetria pós-notificação*)
  - `tests/test_encerrar.py`, `tests/test_rdo.py`, `tests/test_telemetria_hook.py`
- **Contratos/classes:** `fechar_tarefa(..., nao_medido: str | None = None)`, recusa com o prefixo `consumo:` do módulo; `cmd_close` lê `args.nao_medido` (`str | None`); com medida, a linha `**Consumo:**` do RDO sai idêntica à de hoje.
- **Texto da doutrina** (sem quebra obrigatória: o executor reflui no parágrafo, na largura do arquivo):
  - `GOVERNANCA.md` §4.2, ao fim do bullet *Fonte única da série*: `**Tarefa sem medida fecha declarando a ausência:** tarefa sem <usage> — executada na sessão principal, fora do loop — fecha com encerrar.py tarefa --nao-medido "<razão>", que apensa à série a linha nao_medido com as células de consumo vazias e escreve no RDO "não medido — <razão>"; número estimado nunca entra, e medida existente não se descarta (o instrumento recusa --nao-medido quando a série já mede a tarefa). Quem executa fora do loop captura a ref do ponto de partida (git stash create, ou git rev-parse HEAD com a árvore limpa) antes da primeira edição e grava a medida do executor (card_check --gravar), para a evidência do revisor sair com --desde. O .claude/estado/tarefa-corrente.json se grava só no despacho do executor, e o hook SubagentStop só grava a linha do pantonic-executor; a rodada de outro papel gravada sob o id da tarefa (caso medido, 2026-09-26: a do revisor da TK-88a) sai da série por card corretivo que a cita.` — com crases nos nomes de flag, arquivo e instrumento, como no resto do parágrafo.
  - `scrum-master`, Passo 9: no bloco do comando, a linha `[--tool-uses <N> --tokens-k <tokens_k> --duracao-s <N> | --nao-medido "<razão>"]` no lugar da linha do trio; no item (4), logo depois de "número inventado não fecha tarefa.": `Tarefa sem <usage> — executada fora do loop — fecha com --nao-medido "<razão>" (GOVERNANCA.md §4.2): a série registra a ausência, nunca um número.`
  - `passagem-de-bastao`, Parte 3, item 3, logo depois de "sem contagem, `nao_medido`)": `; no fechamento, encerrar.py tarefa --nao-medido "<razão>"`.
- **Testes (novos):** TF `test_tf_tarefa_nao_medido_fecha_com_linha_nao_medido` (`test_encerrar.py`) — tarefa em `review` sem linha na série, `--nao-medido "x"` → `done`, RDO com `**Consumo:** não medido — x`, uma linha nova `nao_medido` com as três células vazias; TR `test_tr_nao_medido_com_medida_na_serie_recusa` — série com linha `usage` da tarefa → recusa, status `review`, sem RDO, série byte a byte igual; TR `test_tr_nao_medido_com_trio_recusa`; TF/TR `test_tf_close_nao_medido_sem_trio` e `test_tr_close_sem_trio_nem_nao_medido_recusa` (`test_rdo.py`); TR `test_tr_hook_so_executor_consome_estado` (`test_telemetria_hook.py`) — `agent_type` `pantonic-reviewer` com estado e transcript presentes → `False`, estado preservado, nada apensado.
- **Verificação:**
  1. `python -m pytest tests/test_encerrar.py tests/test_rdo.py tests/test_telemetria_hook.py -q -k "nao_medido or so_executor"` → verde — antes `exit 5`, depois `exit 0` (antes nenhum teste selecionado).
  2. `python -c "from pathlib import Path;print(sum(1 for l in Path('docs/telemetria.tsv').read_text(encoding='utf-8').splitlines() if l.split(chr(9))[2:3]==['TK-88a'] and l.endswith(chr(9)+'usage')))"` → `0` — antes `1`, depois `0`.
  3. `python -c "from pathlib import Path;print(all('--nao-medido' in Path(f).read_text(encoding='utf-8') for f in ('GOVERNANCA.md','.claude/skills/scrum-master/SKILL.md','.claude/tools/encerrar.py','.claude/tools/rdo.py')))"` → `True` — antes `False`, depois `True`.
  4. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0` (piso re-medido no despacho; referência: `420 passed` em 2026-09-26, antes deste card).
- **Pronto quando:** a tarefa sem `<usage>` fecha com a ausência declarada e recusa quando há medida (Verificação 1), a rodada do revisor sumiu da série sob o id do executor (Verificação 2) e a doutrina diz o desfecho (Verificação 3).
- **Não fazer:** não inventar, estimar nem copiar número de consumo; não tocar outra linha de `docs/telemetria.tsv` nem reordenar a série; não fechar a `TK-88a` (é ato do condutor, depois do `done` deste card); não tocar `telemetria.py` (a `FPU-T7` do `P-0752` é dona dele); não mudar o texto de `**Consumo:**` com medida.
- **Contingências:**
  - se teste existente de `test_rdo.py` ou `test_encerrar.py` fixar o trio como obrigatório no argparse ou o texto do template → o teste que fixa o comportamento antigo é alvo da tarefa (`DM-33` do `P-0740`): ajustar e nomear no retorno.
  - se teste existente de `test_telemetria_hook.py` fizer papel do kit diferente de `pantonic-executor` gravar linha → idem, nomeando o teste.
- **Handover:** 2026-09-26 · para `TK-88a`
  - **Entregue:** encerrar.py tarefa --nao-medido (.claude/tools/encerrar.py:328,380); rdo.py close --nao-medido (.claude/tools/rdo.py:768); hook grava só pantonic-executor (.claude/tools/telemetria_hook.py:51); linha TK-88a usage removida de docs/telemetria.tsv
  - **Contrato:** Tarefa sem <usage> fecha com encerrar.py tarefa --nao-medido "<razão>"; recusa se a série já mede a tarefa ou se vier com o trio
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum
- **Notas de execução:**
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-88b-a-tarefa-sem-medida-fecha-declarando-a-ausencia-e-a-rodada-d.md`, veredito aprovado 100%

### TK-88c — O painel lê cada argumento da própria invocação, e o RDO publicado diz o plano e a tarefa certos [Sonnet · esforço high · classe implementacao]

- **Status:** `done` · 2026-09-26
- **Depende de:** `TK-88b`
- **Objetivo:** no ramo `PreToolUse` · `Bash` de `evento` em `.claude/tools/progresso_hook.py`, a linha de comando se lê por invocação: as frases de `backlog.py status` (`M-2`, `M-10`, `M-10b`), de `encerrar.py tarefa` (`M-10`), de `encerrar.py plano` (`M-18`) e de `review_evidence.py` (`M-5`, `M-13`) só saem quando o script é o programa de uma invocação — `python` (ou `python3`/`py`, com ou sem caminho e opções) seguido do caminho que termina no script e, onde há verbo, do verbo —, e `--tarefa`, `--plano` e `--atribuir` se leem só nos argumentos dessa invocação. Invocações se separam por `&&`, `||`, `;`, `|` e quebra de linha fora de aspas. Texto de argumento que cite o script (mensagem de commit, `--resumo`, `--achado`) não gera frase. `rdo.py close` grava a linha `**Plano:**` com barra normal, venha o caminho como vier. As RDO publicadas se corrigem: em todo `docs/**/*.md`, a frase do painel com `a tarefa "<ID>-revisao"` passa a `a tarefa "<título do card <ID>>"` (título do backlog), e a linha `**Plano:**` com barra invertida passa a barra normal (`CT-1` do `## TK-88`).
- **Arquivos-alvo:**
  - `.claude/tools/progresso_hook.py` — `evento`, ramo `PreToolUse` · `Bash`
  - `.claude/tools/rdo.py` — `cmd_close`, valor de `PLANO_PATH`
  - `.claude/skills/scrum-master/SKILL.md` — repertório do painel, linhas `M-2`, `M-5`, `M-10`, `M-13` e `M-18`: o gatilho passa a dizer que o script e os argumentos se leem na própria invocação
  - `docs/RDO/P-0752-FPU-*.md`, `docs/RDO/DIARIO_DE_OBRAS-TK-91a-*.md` e toda RDO que a regra acima achar em `docs/**/*.md` quando a tarefa rodar
  - `tests/test_progresso_hook.py`, `tests/test_rdo.py`
- **Testes (novos):** TF `test_tf_m10_da_propria_invocacao_em_comando_encadeado` — `evento` sobre `python .claude/tools/telemetria.py append --tarefa X-revisao …; python .claude/tools/encerrar.py tarefa --plano <p> --tarefa X` → `M-10` com o título de `X` e `tarefa_fechada` = `X` (hoje sai o título `X-revisao`, reproduzido pelo revisor com `FPU-T8`); TR `test_tr_literal_em_argumento_nao_e_propria_invocacao` — `git commit -m "… encerrar.py plano …"` não gera `M-18`, e um `--resumo "encerrar.py tarefa --tarefa Y"` noutro comando não gera `M-10`; TF `test_tf_review_evidence_da_propria_invocacao` — o `--tarefa` de um comando anterior na linha não muda o título da `M-5`; TF `test_tf_close_grava_plano_em_barra` (`test_rdo.py`) — `cmd_close` com o caminho do plano em barra invertida grava a linha `**Plano:**` sem barra invertida.
- **Verificação:**
  1. `python -m pytest tests/test_progresso_hook.py tests/test_rdo.py -q -k "propria_invocacao or plano_em_barra"` → verde — antes `exit 5`, depois `exit 0` (antes nenhum teste selecionado).
  2. `python -c "import re;from pathlib import Path;print(sum(len(re.findall('a tarefa '+chr(34)+'[A-Z][A-Za-z0-9-]*-revisao'+chr(34),p.read_text(encoding='utf-8'))) for p in Path('docs').rglob('*.md'))>0)"` → `False` — antes `True`, depois `False`.
  3. `python -c "from pathlib import Path;print(sum(1 for p in Path('docs').rglob('*.md') for l in p.read_text(encoding='utf-8').splitlines() if l.startswith(chr(42)*2+'Plano:') and chr(92) in l)>0)"` → `False` — antes `True`, depois `False`.
  4. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0` (piso re-medido no despacho).
- **Pronto quando:** comando encadeado e script citado em argumento não trocam o título nem inventam frase no painel (Verificação 1), e nenhuma RDO publicada traz o id `-revisao` em frase do painel nem o caminho do plano com barra invertida (Verificações 2 e 3).
- **Não fazer:** não tocar `encerrar.py` (o `**Plano:**` se corrige no `rdo.py`, que serve também o `rdo.py close` direto); não reescrever `.claude/estado/progresso.txt`; não reconstruir nas RDO a linha `M-10` que o defeito rotulou com o id `-revisao` (`CT-1`); não mudar o texto de `FRASES`; nas RDO, não tocar nada além das duas correções.
- **Contingências:**
  - se teste existente de `test_progresso_hook.py` fixar a detecção por substring (script citado em argumento gerando frase) → o teste que fixa o comportamento antigo é alvo da tarefa (`DM-33` do `P-0740`): ajustar e nomear no retorno.
  - se uma RDO trouxer `<ID>-revisao` cujo `<ID>` o backlog não conhece → parar e sinalizar `blocked` razão `premissa`, nomeando o arquivo.
- **Handover:** 2026-09-26 · para `TK-88d`
  - **Entregue:** progresso_hook.py lê script e argumentos por invocação (_dividir_invocacoes :248, _programa :293); rdo.py cmd_close grava **Plano:** em barra normal; 21 RDO corrigidas (-revisao → título; Plano: barra normal)
  - **Contrato:** comando encadeado ou script citado em argumento não troca o título nem gera frase no painel
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum
- **Notas de execução:**
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-88c-o-painel-le-cada-argumento-da-propria-invocacao-e-o-rdo-publ.md`, veredito aprovado 100%

### TK-88d — O fechamento pergunta ao `rdo.py` e ao `backlog.py` se pode escrever, em vez de copiar a regra deles [Sonnet · esforço high · classe implementacao]

- **Status:** `done` · 2026-09-26
- **Depende de:** `TK-88b`, `TK-88c`
- **Objetivo:** `rdo.py` expõe a checagem do `close` sem escrita e `backlog.py` a regra de transição de `transacionar_status` sem escrita; `encerrar.py tarefa` e `encerrar.py plano` chamam as duas antes da primeira escrita e deixam de ter cópia própria delas (destino e existência do RDO; regra de plano `done`). Toda recusa que hoje só o `rdo.py close` faz sai antes do `done`, e a janela "status `done` sem RDO" fica só para falha de E/S. A linha `FECHADO` que o `encerrar.py plano` escreve no diário conta as tarefas como o índice (`_done_total`, que tira as `cancelled` do total), e o stdout do fechamento diz `tarefa fechada` e `plano fechado` (`CT-4` do `## TK-88`).
- **Arquivos-alvo:**
  - `.claude/tools/rdo.py` — `cmd_close`
  - `.claude/tools/backlog.py` — `transacionar_status`
  - `.claude/tools/encerrar.py` — `fechar_tarefa`, `fechar_plano`, `main`
  - `tests/test_rdo.py`, `tests/test_backlog.py`, `tests/test_encerrar.py`
- **Contratos/classes:** `rdo.checar_close(args, status_exigido: str = "done") -> Path` — as checagens do `cmd_close`, sem escrita, devolvendo o destino; `cmd_close` a chama com `"done"`. `backlog.checar_transicao(modelo, id_, estado, razao=None) -> ResultadoStatus | None` — `None` quando a transição pode; `transacionar_status` a chama antes de escrever. As mensagens de recusa não mudam.
- **Testes (novos):** TR `test_tr_checar_close_recusa_antes_do_done` (`test_encerrar.py`) — uma recusa que hoje só o `rdo.py close` faz (o executor escolhe qual e a nomeia no retorno) sai do `encerrar.py tarefa` com a tarefa ainda em `review` e sem RDO; TF `test_tf_checar_transicao_sem_escrita` (`test_backlog.py`) — mesmo resultado de `transacionar_status` para plano com tarefa aberta, arquivos intactos; TF `test_tf_fechado_conta_como_o_indice` (`test_encerrar.py`) — plano com uma `done` e uma `cancelled` → linha `FECHADO` com `1/1` e stdout `plano fechado`.
- **Verificação:**
  1. `python -m pytest tests/test_encerrar.py tests/test_rdo.py tests/test_backlog.py -q -k "checar_close or checar_transicao or fechado_conta"` → verde — antes `exit 5`, depois `exit 0` (antes nenhum teste selecionado).
  2. `python -c "from pathlib import Path;t=Path('.claude/tools/encerrar.py').read_text(encoding='utf-8');print(t.count('tarefa já fechada'),t.count('não terminal(is)'))"` → `0 0` — antes `1 1`, depois `0 0`.
  3. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0` (piso re-medido no despacho).
- **Pronto quando:** a recusa do `rdo.py` sai antes do `done` (Verificação 1), o `encerrar.py` não guarda cópia das duas regras (Verificação 2) e a linha `FECHADO` diz o que o índice diz (Verificação 1).
- **Não fazer:** não mudar mensagem de recusa de `rdo.py` nem de `backlog.py`; não mudar a ordem das escritas do `encerrar.py` (status → RDO → telemetria → achados); não tocar `progresso_hook.py`; não reescrever a linha `FECHADO` já publicada no diário.
- **Contingências:**
  - se alguma checagem do `close` depender do status já `done` por outra razão que não a própria exigência de status → parar e sinalizar `blocked` razão `premissa`, nomeando a checagem.
- **Handover:** 2026-09-26 · para quem vier depois
  - **Entregue:** rdo.checar_close (rdo.py) e backlog.checar_transicao (backlog.py) sem escrita; encerrar.py chama as duas antes da primeira escrita e não copia mais as regras; linha FECHADO conta por _done_total
  - **Contrato:** recusa do rdo.py close sai do encerrar.py tarefa antes do done; FECHADO diz o que o índice diz
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum
- **Notas de execução:**
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-88d-o-fechamento-pergunta-ao-rdo-py-e-ao-backlog-py-se-pode-escr.md`, veredito ressalva 91%

## TK-89 — O gate do card religado deixou atrás o leitor de alvos e a doutrina

- **Status:** `done` · 2026-09-26 — aberto pelo consultor do `P-0752` (acionamento 6, `DFP-18`), rota dos achados `AE-38`, `AE-40` e `AE-41` do laudo da `FPU-T2`.

**Caso medido (2026-09-26):** (1) `review_evidence._classificar_campo_alvos` varre o campo `Arquivos-alvo` achatado por pares de crases; a entrada `` `<caminho>:<linha>` — `<literal>` `` da `DFP-16` traz crase escapada (`\``) dentro do literal, o par se desalinha e só o primeiro caminho sobrevive: sobre a `FPU-T2`, 1 alvo de 5, e 8 literais descartados. Protótipo do consultor (em memória, sem tocar o módulo): cortar o literal logo depois da âncora antes da varredura dá os 5 alvos e 0 descartados na `FPU-T2`, e muda o resultado de 5 dos 314 cards do acervo (`docs/plans/**` e o diário), todos do `P-0752`. (2) `.claude/skills/scrum-master/SKILL.md:62` diz "sete itens" do Gate de delegação da `passagem-de-bastao`, que tem oito desde a `FPU-T2` (o 8º é `card_check` exit 0), e a linha `B3` do bloco B não cita o `card_check` como gatilho, embora o Passo 3 mande o exit 1 dele para `B3`. (3) `docs/RUBRICA_DE_REVISAO.md` `### 8.1` diz que o literal da âncora é "comparado por `strip()` contra a linha citada"; a `DFP-16` do `P-0752` e o instrumento conferem o literal **contido** em alguma linha (`strip()`) da faixa `linha..fim`.

**O que decide:** correção conhecida nos três; dois cards `ready`, um por natureza (instrumento; redação). Descartado: um card só (mistura classe `implementacao` e `redacao`).
- **Notas de execução:**
  - 2026-09-26 `ready` — aberto com os cards TK-89a e TK-89b (consultor P-0752, acionamento 6)

### TK-89a — O leitor de alvos da evidência corta o literal da âncora antes de varrer as crases [Sonnet · esforço low · classe implementacao]

- **Status:** `done` · 2026-09-26
- **Objetivo:** em `_classificar_campo_alvos` de `.claude/tools/review_evidence.py`, antes da varredura por `_BACKTICK_RE`, o texto do campo (`arquivos-alvo` ou `entregavel`) troca cada âncora seguida de literal pela âncora só; o resto da função não muda. Com isso a entrada `` `<caminho>:<linha>` — `<literal>` `` vira um alvo, com ou sem crase escapada no literal, e o literal não vai aos descartados.
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
- **Contratos/classes:** constante de módulo `_LITERAL_APOS_ANCORA_RE = re.compile(r"(`[^`\s]+:\d+(?:-\d+)?`)\s*(?:—|:)\s*`(?:\\`|[^`\\])+`")`, aplicada com `.sub(r"\1", texto)`; mesma leitura de literal da `DFP-16` do `P-0752` (`card_check._LITERAL_APOS_ANCORA_RE`), duplicada aqui, sem import cruzado.
- **Caso medido que motivou:** ver `## TK-89`, item (1).
- **Testes (novos, em `tests/test_review_evidence.py`):** TF `test_tf_alvo_ancorado_com_literal_e_um_alvo` — o campo `- \`a/b.md:3\` — \`x \\\` y\` - \`c/d.py\`` (literal com crase escapada) → `_classificar_campo_alvos` devolve `(["a/b.md", "c/d.py"], [])`; hoje devolve `(["a/b.md"], [...])` (medido no protótipo). TR `test_tr_alvo_sem_ancora_nao_muda` — campo só com caminhos entre crases e um literal não caminho → mesmo resultado de hoje.
- **Teste existente que muda (um só, `CT89-1`):** em `test_tr_extrair_literais_nao_caminho_lista_o_descartado`, a entrada `` `.claude/tools/rdo.py:79` — `_ID_HEADER_RE = re.compile(x)` `` perde o `:79` e fica `` `.claude/tools/rdo.py` — `_ID_HEADER_RE = re.compile(x)` ``. Razão: com linha, o par é âncora da `DFP-16` e o literal é dela (conferido pelo `card_check`), não literal descartado — o corte o tira dos descartados por decisão (Objetivo); sem linha, o `re.compile` continua literal não caminho e o teste segue provando o que prova (a `DB-27` lista o descartado). Os dois `assert` ficam como estão. Medido pelo consultor (protótipo na árvore, revertido): com o corte e essa troca, `tests/test_review_evidence.py` 55 passed, suíte 442 passed, `FPU-T2` 5 alvos e 0 descartados, o campo do TF → `(['a/b.md', 'c/d.py'], [])`.
- **Verificação:**
  1. `python -c "import sys;sys.path.insert(0,'.claude/tools');import review_evidence as r,rdo;from pathlib import Path;d=rdo.extrair_dossie(Path('docs/plans/P-0752-fato-no-ponto-de-uso.md'),'FPU-T2',esquema_legado=False,modelo_legado=None,classe_legado=None);print(len(r.extrair_arquivos_alvo(d.campos)))"` → `5` — antes `1`, depois `5`.
  2. `python -m pytest tests/test_review_evidence.py -q -k alvo_ancorado_com_literal` → verde — antes `exit 5`, depois `exit 0` (antes nenhum teste selecionado).
  3. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`.
  4. `python -m pytest tests/test_review_evidence.py -q -k literais_nao_caminho_lista` → verde — antes `exit 0`, depois `exit 0` (o teste de `CT89-1`, com a entrada trocada).
- **Pronto quando:** a entrada de `Arquivos-alvo` com âncora e literal conta como um alvo na evidência, provado pelo TF e pela `FPU-T2` do `P-0752` (5 alvos).
- **Não fazer:** não mudar `_eh_caminho`, `_LINHA_REF_RE` nem `_SECAO_REF_RE`; não importar `card_check`; não tocar `rdo.py`; não mudar os `assert` de `test_tr_extrair_literais_nao_caminho_lista_o_descartado` nem a entrada de `test_tf_extrair_arquivos_alvo_aceita_arquivo_de_raiz_e_recusa_literal_de_regex` (a mesma, que segue verde com `:79`); não aplicar o corte só aos alvos (descartados lidos do texto sem corte voltam a desalinhar na crase escapada).
- **Contingências:**
  - se cair um teste existente de `_classificar_campo_alvos` ou de `extrair_literais_nao_caminho` **outro que** `test_tr_extrair_literais_nao_caminho_lista_o_descartado` (tratado em `CT89-1`) → parar e sinalizar `blocked` razão `premissa`, nomeando o teste (no protótipo, o corte só muda cards do `P-0752` e só esse teste cai).
- **Handover:** 2026-09-26 · para `TK-89b`
  - **Entregue:** review_evidence.py: _LITERAL_APOS_ANCORA_RE corta o literal da âncora em _classificar_campo_alvos antes de _BACKTICK_RE; FPU-T2 do P-0752 conta 5 alvos
  - **Contrato:** entrada de Arquivos-alvo 'caminho:linha — literal' é um alvo, e o literal não vai aos descartados
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum
- **Notas de execução:**
  - 2026-09-26 `ready` — consultor TK-89 acionamento 1 (CT89-1): corte mantido nos alvos e nos descartados; test_tr_extrair_literais_nao_caminho_lista_o_descartado troca a entrada rdo.py:79 por rdo.py (asserts intactos); protótipo medido 442 passed
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-89a-o-leitor-de-alvos-da-evidencia-corta-o-literal-da-ancora-ant.md`, veredito aprovado 100%

### TK-89b — A doutrina do gate do card conta oito itens, cita o `card_check` no `B3` e confere o literal contido na faixa [Sonnet · esforço low · classe redacao]

- **Status:** `done` · 2026-09-26
- **Objetivo:** o `scrum-master` diz "oito itens" do Gate de delegação e cita o `card_check` do passo 3 na linha `B3`; a rubrica `### 8.1` diz que o literal da âncora confere quando está contido em alguma linha da faixa `linha..fim`, como a `DFP-16` do `P-0752` e o `card_check`.
- **Arquivos-alvo:**
  - `.claude/skills/scrum-master/SKILL.md:62` — `seção "Gate de delegação", sete itens`
  - `.claude/skills/scrum-master/SKILL.md:285` — `pelo gate de delegação ou pelo`
  - `docs/RUBRICA_DE_REVISAO.md:340-341` — `contra a linha citada`
  - `.claude/README.md` (projeção regenerada, se o gerador do kit a reescrever)
- **Caso medido que motivou:** ver `## TK-89`, itens (2) e (3).
- **Passos:**
  1. `.claude/skills/scrum-master/SKILL.md:62`: `sete itens` → `oito itens`.
  2. `.claude/skills/scrum-master/SKILL.md:285`: `pelo gate de delegação ou pelo \`modelo.py check\` do passo 3` → `pelo gate de delegação, pelo \`modelo.py check\` ou pelo \`card_check\` do passo 3`.
  3. Rubrica, na âncora do alvo (o trecho quebra entre as duas linhas): `desescapado e comparado por` + `strip()` + `contra a linha citada` → `desescapado e com \`strip()\`, e confere quando está contido em alguma linha (\`strip()\`) da faixa \`linha..fim\``.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print(t.count('sete itens'),t.count('oito itens'))"` → `0 1` — antes `1 0`, depois `0 1`.
  2. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print(sum(1 for l in t.splitlines() if l.startswith('| ') and 'B3' in l[:8] and 'card_check' in l))"` → `1` — antes `0`, depois `1`.
  3. `python -c "from pathlib import Path;print(Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8').count('contra a linha citada'))"` → `0` — antes `1`, depois `0`.
  4. `pwsh .claude/checks/kit_check.ps1` → exit 0 — antes `exit 0`, depois `exit 0` (trava).
- **Pronto quando:** as três frases da doutrina do gate batem com o gate que roda — Verificações 1 a 3.
- **Não fazer:** não tocar o bloco A do `scrum-master`; não mudar a ordem nem o texto dos gates do Passo 3; não tocar a `passagem-de-bastao`.
- **Contingências:**
  - se a linha `B3` ou a frase da rubrica tiver mudado de texto antes do despacho (o gate de âncora acusa) → aplicar a mesma troca de sentido sobre o texto novo e registrar em `pendencia=`.
- **Handover:** 2026-09-26 · para quem vier depois
  - **Entregue:** scrum-master/SKILL.md:62 'oito itens'; :285 B3 cita card_check; RUBRICA_DE_REVISAO.md §8.1 literal contido na faixa linha..fim
  - **Contrato:** a doutrina do gate do card bate com o gate que roda
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum
- **Notas de execução:**
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-89b-a-doutrina-do-gate-do-card-conta-oito-itens-cita-o-card-chec.md`, veredito aprovado 100%

## TK-90 — O `P-0742` está fora do índice do diário, `blocked` com a condição já satisfeita

- **Status:** `done` · 2026-09-27 — aberto pelo consultor do `P-0752` (acionamento 10), na varredura do gate do card sobre todo card não terminal, por ordem do dono de 2026-09-26 (erro inequívoco não se adia).

**Caso medido (2026-09-26):** `docs/plans/P-0742-loop-fora-do-llm.md` existe com status `blocked` no cabeçalho e oito cards `ready` (`LF-T1`..`LF-T8`), e nenhuma linha do índice de `docs/DIARIO_DE_OBRAS.md` começa por `| P-0742-` (0 linhas, medido); nem `docs/plans/_INBOX.md` nem o histórico do inbox o citam — é o plano do `TK-59`, criado sem linha de inbox. A condição de destravamento escrita no cabeçalho (`P-0739` `done`) já está satisfeita. Os oito cards saem `card_check` exit 1 com `nenhum item reconhecido (comando em bloco cercado ausente)`: foram escritos antes do gate e cairão em `B3` no despacho. Numa cópia da árvore, uma linha de inbox mais `backlog.py drain` grava `| P-0742-LF | O loop sai do LLM | blocked | docs/plans/P-0742-loop-fora-do-llm.md |`, mas recalcula o contador do inbox pelo maior id do próprio inbox e o põe em `P-0743` (`check` sai `C-10`); com o contador reposto, `check` OK.

**O que decide:** o registro no índice é correção conhecida (card `TK-90a`, `ready`). O destino do plano — retomar ou encerrar — era decisão do dono, tomada em 2026-09-26: *"Retomar"* (card `TK-90b`, que passa a ser a rodada `RP-1` do `P-0742`, ao planejador); a reescrita dos oito cards para o gate pertence à rodada de replanejamento do próprio plano, se ele retomar, e não a este tíquete (card vivo de outro plano não se reescreve para caber no instrumento, `I-3` do `P-0752`).
- **Notas de execução:**
  - 2026-09-26 `ready` — aberto com os cards TK-90a e TK-90b (consultor P-0752, acionamento 10)
- **AE-88** (`TK-90b`, fechamento, 2026-09-27) — rodada de replanejamento despachada ao planejador não tem canal de medida gravada (card_check --gravar); o verde só se confirmou por re-execução do revisor **Rota:** auditoria final
- **AE-89** (`TK-90b`, fechamento, 2026-09-27) — LF-T2..LF-T5 do P-0742 passam do teto DB-7 de backlog.py show (8.000 caracteres) e saem truncados; a Fase 4 do planejador não confronta o tamanho do card com o teto **Rota:** auditoria final · **Desfecho (P-0754, AUF-T14, 2026-09-28):** encerrado sem mudança no kit — a premissa caiu: o card de tarefa é isento do teto do `backlog.py show`, e os oito cards do `P-0742` saem inteiros, sem marca de truncado.



### TK-90a — O `P-0742` entra no índice do diário como `blocked` [Sonnet · esforço low · classe mecanica]

- **Status:** `done` · 2026-09-26
- **Objetivo:** o índice de `docs/DIARIO_DE_OBRAS.md` ganha a linha do `P-0742`, com o status do cabeçalho do plano, pelo caminho canônico do inbox, sem mexer no contador de id de plano.
- **Arquivos-alvo:**
  - `docs/plans/_INBOX.md`
  - `docs/DIARIO_DE_OBRAS.md` (índice e bloco `Fila corrente`, reescritos pelo `drain`)
  - `docs/plans/_INBOX_HISTORICO.md` (apenso do `drain`)
- **Passos:**
  1. Anotar o valor do contador `**Próximo id de plano: P-NNNN.**` de `docs/plans/_INBOX.md`.
  2. Apensar ao fim de `docs/plans/_INBOX.md` a linha ``- 2026-09-19 · `docs/plans/P-0742-loop-fora-do-llm.md` · O loop sai do LLM — registro tardio no índice (`TK-90a`).``
  3. Rodar `python .claude/tools/backlog.py drain`.
  4. Repor no contador o valor anotado no passo 1 (o `drain` o recalcula pelo maior id do inbox e o põe em `P-0743`, medido).
- **Verificação:**
  1. `python -c "from pathlib import Path;print(sum(1 for l in Path('docs/DIARIO_DE_OBRAS.md').read_text(encoding='utf-8').splitlines() if l.startswith('| P-0742-')))"` → `1` — antes `0`, depois `1`.
  2. `python .claude/tools/backlog.py check` → `check: OK — nenhuma violação.` — antes `exit 0`, depois `exit 0` (trava: o `C-10` acusa contador que o `drain` deixou para trás).
- **Pronto quando:** o índice tem uma linha do `P-0742` com o status do cabeçalho do plano, e o contador de id de plano é o de antes do `drain`.
- **Não fazer:** não mudar o status nem o texto do `P-0742`; não tocar os cards `LF-T*`; não mudar o `backlog.py`.
- **Contingências:**
  - se o `drain` sair diferente de `0` ou tocar outra linha de índice além da do `P-0742` → parar e sinalizar `blocked` razão `premissa`, colando a saída.
- **Handover:** 2026-09-26 · para `TK-90b`
  - **Entregue:** índice do diário com | P-0742-LF | O loop sai do LLM | blocked | (docs/DIARIO_DE_OBRAS.md:308); contador do inbox mantido em P-0753
  - **Contrato:** o P-0742 é visível ao backlog; a rodada RP-1 do planejador parte dele
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum
- **Notas de execução:**
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-90a-o-p-0742-entra-no-indice-do-diario-como-blocked.md`, veredito aprovado 100%

### TK-90b — A rodada de replanejamento `RP-1` do `P-0742`: os oito cards passam no gate do card [Opus · esforço high · classe redacao]

- **Status:** `done` · 2026-09-27 — decisão do dono *"Retomar"*; espera o `TK-90a`
- **Depende de:** `TK-90a`
- **Decisão do dono (2026-09-26):** *"Retomar"* — a opção (a) que este card levava ao dono; a (b), encerrar o plano, fica descartada.
- **Despacho:** ao `pantonic-planner`, em instância fria — é a rodada de replanejamento `RP-1` do `P-0742` (`GOVERNANCA.md` §7 item 17, `G-REPLAN`), não card de executor. O dossiê `Ato de modelo` de `autoria` que o planejador devolver, quem conduz a sessão despacha ao `pantonic-model-designer` (`GOVERNANCA.md` §3.2), e a rodada segue com a seção escrita.
- **Objetivo:** o `P-0742` ("O loop sai do LLM") volta à fila: a rodada `RP-1` escreve o que o plano não tem — a seção `## 1. Modelo conceitual`, pelo modelador — e reescreve os oito cards `LF-T1`..`LF-T8`, um por operação, com a `Verificação` na forma que o gate do card lê, e o plano sai de `blocked` para `ready`.
- **Entrada da rodada:** o caso medido do `TK-90`, acima — cabeçalho `blocked` à espera do `P-0739` `done`, condição já satisfeita; os oito cards saem `card_check` exit 1 com `nenhum item reconhecido (comando em bloco cercado ausente)`; `modelo.py check` sai exit 2 com `plano anterior à doutrina`; `## Achados da execução` do `P-0742` vazio.
- **Arquivos-alvo:**
  - `docs/plans/P-0742-loop-fora-do-llm.md` — cabeçalho, seção do modelo (do modelador), os cards `LF-T*` e `## Achados da execução` (entrada `RP-1`)
  - `docs/DIARIO_DE_OBRAS.md` (linha de índice do `P-0742`, escrita pelo `backlog.py status`)
- **Passos:**
  1. Seguir a seção "Rodada de replanejamento" de `.claude/agents/pantonic-planner.md`; como o plano não tem a seção do modelo, devolver primeiro o dossiê `Ato de modelo` de `autoria` (Fase 3a) e reescrever os cards só com a seção na árvore (Fase 3b), um card por operação, com o campo `Operação do modelo`.
  2. Cada card reescrito passa pelos itens 11 a 13 da Fase 4 do planejador e sai `python .claude/tools/card_check.py --plano docs/plans/P-0742-loop-fora-do-llm.md --tarefa <ID>` exit 0 antes de gravado.
  3. Gravar a entrada `RP-1` em `## Achados da execução` do `P-0742`, com a classificação da mudança e a decisão do dono (*"Retomar"*, 2026-09-26, `TK-90b`).
  4. Rodar `python .claude/tools/backlog.py status P-0742 ready --nota "rodada RP-1 fechada (TK-90b)"`.
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('docs/plans/P-0742-loop-fora-do-llm.md').read_text(encoding='utf-8');print(('**Status:** '+chr(96)+'ready') in t.split('**Prefixo')[0])"` → `True` (o cabeçalho do plano diz `ready`) — antes `False`, depois `True`.
  2. `python -c "import sys;sys.path.insert(0,'.claude/tools');import backlog,subprocess;from pathlib import Path;p=[x for x in backlog.carregar(Path('.')).planos if x.id=='P-0742'][0];ids=[t.id for t in p.tarefas if t.status!='cancelled'];print(len(ids)>0 and all(subprocess.run([sys.executable,'.claude/tools/card_check.py','--plano','docs/plans/P-0742-loop-fora-do-llm.md','--tarefa',i],capture_output=True).returncode==0 for i in ids))"` → `True` (todo card não cancelado do plano fecha no gate) — antes `False`, depois `True`.
  3. `python .claude/tools/modelo.py check --plano docs/plans/P-0742-loop-fora-do-llm.md` → `modelo: OK` — antes `exit 2`, depois `exit 0`.
  4. `python .claude/tools/backlog.py check` → `check: OK — nenhuma violação.` — antes `exit 0`, depois `exit 0`.
- **Pronto quando:** o cabeçalho e a linha de índice do `P-0742` dizem `ready`; o plano tem a seção do modelo com `modelo.py check` exit 0; todo card não cancelado dele sai `card_check` exit 0; a entrada `RP-1` está em `## Achados da execução` do plano.
- **Não fazer:** não executar card do `P-0742`; não mudar o objetivo do plano nem decisão `DLF-*` do dono — o que for estratégico ou de escopo vai ao dono numa rodada de decisões, uma só (`G-REPLAN`); não estender `card_check.py`, `backlog.py` nem `modelo.py` para caber os cards; o `ready` do plano não o põe na janela, porque a diretiva de priorização é ato do dono.
- **Contingências:**
  - se uma decisão `DLF-*` do plano cair diante do `P-0739` entregue (verbo de `backlog.py` que o driver consome e que não existe mais) → decisão nova com id na tabela de decisões do plano, pela rodada, e o card que dela depende reescrito no mesmo ato; se a queda mudar o objetivo do plano → rodada de decisões ao dono e o card fica `blocked` razão `dependencia`, nomeando a decisão.
  - se uma operação do modelo não couber num card coeso → o planejador devolve novo dossiê de `autoria` e o modelador substitui a seção no lugar (`GOVERNANCA.md` §3.2, "Rascunho antes do Marco 1"); a Verificação 2 lê os cards que existirem ao fim, e não uma lista fixa.
- **Handover:** 2026-09-27 · para quem vier depois
  - **Entregue:** P-0742 com ## 1 Modelo conceitual versão 1 (8 operações), cards LF-T1..LF-T8 reescritos um por operação com card_check exit 0, RP-1 em Achados, status ready 0/8
  - **Contrato:** P-0742 ready e fora da janela até o Marco 1 (leitura da ## 1 pelo dono); a priorização é ato do dono
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum
- **Notas de execução:**
  - 2026-09-26 `ready` — decisão do dono "Retomar" (2026-09-26): o card vira a rodada de replanejamento RP-1 do P-0742, ao pantonic-planner, depois do TK-90a (consultor P-0752, acionamento 11)
  - 2026-09-27 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-90b-a-rodada-de-replanejamento-rp-1-do-p-0742-os-oito-cards-pass.md`, veredito aprovado 100%

## TK-91 — O modelador não tem o ato que promove ou elimina a versão pendente no marco

- **Status:** `done` · 2026-09-26 — aberto pelo consultor do `P-0752` (acionamento 11), ao validar a versão 2 do modelo do plano no marco.

**Caso medido (2026-09-26):** `GOVERNANCA.md` §3.2 (*Versão vigente, pendente e obsoleta*) diz o que acontece no marco — aceita, a pendente passa a vigente e a anterior a obsoleta, e o plano guarda só a linha que registra a obsolescência; recusada, a pendente é eliminada — e dá ao modelador todo ato sobre o modelo. `.claude/agents/pantonic-model-designer.md`, seção `## Os quatro atos`, não tem esse desfecho: `grep -n -i "aceit" .claude/agents/pantonic-model-designer.md` sai vazio, e o bullet **Emenda** manda *"A `## 1` vigente **não se toca**"*. Um modelador frio que recebe o dossiê da promoção lê instrução contrária à tarefa; a promoção já foi feita em `P-0747` e `P-0748` (registro de versões: *"Caiu pelo aceite da versão 2"*) sem que o arquivo do agente a descrevesse.

**O que decide:** correção conhecida — o bullet **Emenda** ganha o desfecho do marco, sem ato novo nem valor novo no campo `Ato` (card `TK-91a`, `ready`).
- **Notas de execução:**
  - 2026-09-26 `ready` — aberto com o card TK-91a (consultor P-0752, acionamento 11)
  - 2026-09-26 `in-progress` — tíquete fechado: único card TK-91a done, laudo aprovado 100 (docs/RDO/laudos/DIARIO_DE_OBRAS-TK-91a.md)
  - 2026-09-26 `review` — tíquete fechado: único card TK-91a done, laudo aprovado 100 (docs/RDO/laudos/DIARIO_DE_OBRAS-TK-91a.md)
  - 2026-09-26 `done` — tíquete fechado: único card TK-91a done, laudo aprovado 100 (docs/RDO/laudos/DIARIO_DE_OBRAS-TK-91a.md)
- **AE-76** (`TK-91a`, fechamento, 2026-09-26) — Revisor: a secao 'A forma da devolucao' de .claude/agents/pantonic-model-designer.md (itens 1 e 2) nao cobria o desfecho do marco - o item 1 mandava apontar a '## 1A', que sai do plano no aceite, e o item 2 mandava devolver 'a linha da versao do ato', que o marco nao cria. **Rota:** corrigido no ato pelo condutor (regra do dono: erro inequivoco nao se adia): itens 1 e 2 ganharam o caso do marco, sem mudar a contagem de linhas; kit_check validate e check-drift OK


### TK-91a — O bullet Emenda do modelador diz o que fazer no marco [Sonnet · esforço low · classe redacao]

- **Status:** `done` · 2026-09-26
- **Objetivo:** o arquivo do modelador descreve o desfecho da versão pendente no marco, aceita ou recusada, na forma da `GOVERNANCA.md` §3.2, dentro do ato `emenda`.
- **Arquivos-alvo:**
  - `.claude/agents/pantonic-model-designer.md:88` — `toca**: quem decide entre as duas é o marco, nunca você.`
- **Passos:**
  1. Logo depois da linha 88 de `.claude/agents/pantonic-model-designer.md`, dentro do bullet **Emenda**, inserir as seis linhas do bloco abaixo, cada uma com dois espaços de recuo no arquivo, como as linhas vizinhas do bullet, sem mudar outra linha do arquivo:

     ```text
     **No marco**, o desfecho da pendente chega em novo dossiê `Ato: emenda`, com a validação do
     consultor e o ato do dono em `Motivo`. Aceita: o conteúdo da `## 1A` passa à `## 1`, com o
     cabeçalho em `situação: vigente`; a `## 1A` sai do plano; no registro de versões a pendente passa
     a `vigente` e a anterior a `obsoleta`, com a frase `Caiu pelo aceite da versão <N> em <data>` —
     a linha fica, o conteúdo da obsoleta não. Recusada: a `## 1A` e a linha dela saem, e a vigente
     fica sem marca (`GOVERNANCA.md` §3.2, *Versão vigente, pendente e obsoleta*).
     ```
- **Verificação:**
  1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-model-designer.md').read_text(encoding='utf-8');print('Caiu pelo aceite da versão' in t)"` → `True` — antes `False`, depois `True`.
  2. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate` → `kit_check: OK` — antes `exit 0`, depois `exit 0`.
  3. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `kit_check: check-drift OK` — antes `exit 0`, depois `exit 0`.
- **Pronto quando:** o bullet **Emenda** do modelador diz o desfecho da pendente no marco, aceita e recusada, e os dois modos do `kit_check` seguem exit 0 (medido em protótipo sobre a árvore, revertido, em 2026-09-26).
- **Não fazer:** não criar ato novo nem valor novo no campo `Ato` (a gramática de seis campos é da `GOVERNANCA.md` §3.2); não tocar a `GOVERNANCA.md`; não mudar o título `## Os quatro atos`.
- **Contingências:**
  - se a linha 88 não trouxer o literal ancorado (o gate de âncora acusa) → inserir as seis linhas logo depois da linha que termina o bullet **Emenda** com `quem decide entre as duas é o marco, nunca você.`, e registrar a linha em `pendencia=`.
- **Handover:** 2026-09-26 · para `pantonic-model-designer`
  - **Entregue:** .claude/agents/pantonic-model-designer.md: bullet Emenda (apos a linha 88) descreve o desfecho da pendente no marco, aceita e recusada; secao 'A forma da devolucao' itens 1 e 2 cobrem o marco (corrigido pelo condutor no ato, achado do revisor)
  - **Contrato:** o modelador promove ou elimina a versao pendente no marco pelo ato emenda; kit_check validate e check-drift OK
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum
- **Notas de execução:**
  - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-91a-o-bullet-emenda-do-modelador-diz-o-que-fazer-no-marco.md`, veredito aprovado 100%


## TK-92 — A medida do executor de card de tíquete grava onde o `review_evidence.py` não procura

- **Status:** `done` · 2026-09-27 — aberto pelo consultor do `TK-86` (acionamento 2, `PC-2`), rota do achado `AE-77` do fechamento do `TK-86a`.

**Caso medido (2026-09-26):** o item 5a do `pantonic-executor.md` e a Saída do Passo 5 do `scrum-master` mandam gravar a medida em `<evidencia>/<P-n>-<ID>-medida.json`, com `<P-n>` "o id do plano" — forma que não cobre card de tíquete do diário. O executor do `TK-86a` gravou `docs/RDO/evidencia/P-0751-TK-86a-medida.json` (o id do plano de onde o tíquete nasceu); o `review_evidence.py` procura `DIARIO_DE_OBRAS-TK-86a-medida.json` (`id_do_plano(...) or plano_path.stem`, em `montar_documento`), deu a medida como `ausente`, e o laudo deu `registro` parcial. O executor do `TK-91a`, na mesma janela, acertou o nome. A regra do destino vive em três lugares: na prosa de dois arquivos de doutrina e em `montar_documento`.

**O que decide:** correção conhecida — o destino passa a ser uma função de `.claude/tools/caminhos.py`, chamada pelo `review_evidence.py` para procurar e pelo `card_check.py --gravar` sem caminho para gravar; a doutrina manda rodar `--gravar` sem caminho e deixa de ensinar a regra. Card `TK-92a`, `ready`. O arquivo `docs/RDO/evidencia/P-0751-TK-86a-medida.json` fica com o nome que tem: o laudo e a evidência do `TK-86a`, registros fechados, o citam por esse nome, e ele é o caso medido deste tíquete. Descartado: só emendar a prosa com o id derivado (a regra seguiria em três lugares).
- **Notas de execução:**
  - 2026-09-26 `ready` — aberto com o card TK-92a (consultor TK-86, acionamento 2)
- **AE-91** (`TK-92a`, fechamento, 2026-09-27) — evidência de card não rastreado sai inteira (caminhos.py, test_caminhos.py) **Rota:** TK-93a
- **AE-92** (`TK-92a`, fechamento, 2026-09-27) — review_evidence no modo diário atribui escritas da orquestração (status no diário, linha de telemetria) a tíquetes que não as fizeram (TK-54b, TK-88b) **Rota:** auditoria final



### TK-92a — O destino da medida do executor sai de uma função só, e o `card_check --gravar` sem caminho grava nele [Sonnet · esforço medium · classe implementacao]

- **Status:** `done` · 2026-09-27
- **Objetivo:**
  1. `.claude/tools/caminhos.py` ganha `destino_medida(raiz, plano_path, tarefa)`: plano em pasta → `<pasta>/evidencia/<id>-<tarefa>-medida.json`; qualquer outro (plano legado, `docs/DIARIO_DE_OBRAS.md`) → `<raiz>/docs/RDO/evidencia/<id ou stem>-<tarefa>-medida.json`, com `<id ou stem>` = `id_do_plano(plano_path) or Path(plano_path).stem`, a regra que `montar_documento` usa hoje;
  2. `montar_documento` de `.claude/tools/review_evidence.py` procura a medida em `destino_medida(root, plano_path, <tarefa>)`; com `dir_evidencia` informado, no mesmo nome de arquivo dentro de `dir_evidencia`, como hoje;
  3. `--gravar` de `.claude/tools/card_check.py` aceita vir sem caminho e então grava em `destino_medida(<--root>, <--plano>, <tarefa>)`; com caminho, igual a hoje; ausente, não grava;
  4. a doutrina manda rodar `--gravar` sem caminho (os dois trechos de `Passos`).
- **Arquivos-alvo:**
  - `.claude/tools/caminhos.py`
  - `.claude/tools/review_evidence.py`
  - `.claude/tools/card_check.py`
  - `.claude/agents/pantonic-executor.md`
  - `.claude/skills/scrum-master/SKILL.md`
  - `tests/test_caminhos.py`
  - `tests/test_card_check.py`
- **Passos:**
  1. Em `.claude/agents/pantonic-executor.md`, item 5a, o trecho depois de `antigo:` vira o trecho depois de `novo:` (sem quebra nova e sem refluxo; o rótulo não entra no arquivo):

     ```text
     antigo: --mundo depois --gravar <evidencia>/<P-n>-<ID>-medida.json`, com `<P-n>` o id do plano (`P-0752`, nunca o caminho) e `<evidencia>` = `docs/RDO/evidencia` no plano legado ou `<pasta>/evidencia` no plano em pasta — a pasta em que `review_evidence.py` procura a medida; exit 1
     novo: --mundo depois --gravar`, sem caminho — o destino é o de `caminhos.destino_medida`, o mesmo em que `review_evidence.py` procura a medida, em plano legado, plano em pasta e tíquete do diário; exit 1
     ```
  2. Em `.claude/skills/scrum-master/SKILL.md`, Passo 5, Saída, idem (o trecho antigo está numa linha só do arquivo):

     ```text
     antigo: `<evidencia>/<P-n>-<ID>-medida.json` (`<P-n>` o id do plano; `<evidencia>` = `docs/RDO/evidencia` no legado, `<pasta>/evidencia` no plano em pasta), cuja ausência
     novo: o destino de `caminhos.destino_medida` (o `card_check.py --gravar` sem caminho grava ali e o `review_evidence.py` procura ali), cuja ausência
     ```
- **Contratos/classes:** `caminhos.destino_medida(raiz: Path, plano_path: Path, tarefa: str) -> Path`. O `card_check.py` carrega `caminhos.py` do diretório do próprio módulo, como o `review_evidence.py` já faz. O JSON gravado não muda.
- **Caso medido que motivou:** ver `## TK-92`.
- **Testes (novos):** TF `test_tf_destino_medida_tres_residencias` (`tests/test_caminhos.py`) — `docs/DIARIO_DE_OBRAS.md` e `TK-1a` → `<raiz>/docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-1a-medida.json`; `docs/plans/P-0001-x.md` e `T1` → `<raiz>/docs/RDO/evidencia/P-0001-T1-medida.json`; `docs/plans/P-0002-y/plano.md` e `T2` → `docs/plans/P-0002-y/evidencia/P-0002-T2-medida.json`. TF `test_tf_gravar_sem_caminho_grava_no_destino_derivado` (`tests/test_card_check.py`) — raiz temporária com o `plano-corpus.md` da fixture copiado como `docs/DIARIO_DE_OBRAS.md`, `--gravar` sem valor → exit `0` e `docs/RDO/evidencia/DIARIO_DE_OBRAS-CX-T1-medida.json` gravado na raiz temporária (nada gravado no repositório).
- **Verificação:**
  1. `python -c "import sys;sys.path.insert(0,'.claude/tools');import caminhos as c;from pathlib import Path;print(c.destino_medida(Path('.'),Path('docs/DIARIO_DE_OBRAS.md'),'TK-86a').as_posix())"` → `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-86a-medida.json` — antes `exit 1`, depois `docs/RDO/evidencia/DIARIO_DE_OBRAS-TK-86a-medida.json`.
  2. `python -c "from pathlib import Path;fs=['.claude/agents/pantonic-executor.md','.claude/skills/scrum-master/SKILL.md'];print(sum(Path(f).read_text(encoding='utf-8').count('<P-n>-<ID>-medida.json') for f in fs))"` → `0` — antes `2`, depois `0`.
  3. `python -c "from pathlib import Path;fs=['.claude/agents/pantonic-executor.md','.claude/skills/scrum-master/SKILL.md'];print(sum(Path(f).read_text(encoding='utf-8').count('caminhos.destino_medida') for f in fs))"` → `2` — antes `0`, depois `2`.
  4. `python -m pytest tests/test_caminhos.py tests/test_card_check.py -q -k "destino_medida or gravar_sem_caminho"` → verde — antes `exit 5`, depois `exit 0`.
  5. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`.
  6. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `kit_check: check-drift OK` — antes `exit 0`, depois `exit 0`.
- **Pronto quando:** a medida de card de tíquete, de plano legado e de plano em pasta é gravada e procurada no mesmo caminho, dado por uma função só (Verificação 1 e 4), e a doutrina manda o `--gravar` sem caminho (Verificação 2 e 3). Medido em protótipo do consultor sobre cópia da árvore, apagada, em 2026-09-26: suíte `428 passed` → `430 passed`, `check-drift` OK.
- **Não fazer:** não mudar o JSON gravado nem o nome que o `review_evidence.py` procura hoje em plano legado e em pasta; não renomear nem apagar `docs/RDO/evidencia/P-0751-TK-86a-medida.json`; não tocar `.claude/skills/fatos-frescos/SKILL.md` (o `--gravar <caminho>` que ele ensina segue válido); não tocar `_classificar_campo_alvos` (é do `TK-89a`).
- **Contingências:**
  - se um teste existente de `tests/test_review_evidence.py` sobre a seção de medida do executor cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste (no protótipo, nenhum caiu).
- **Handover:** 2026-09-27 · para `TK-93a`
  - **Entregue:** caminhos.destino_medida (.claude/tools/caminhos.py:110) usado por review_evidence para procurar e por card_check --gravar sem caminho para gravar; doutrina do executor e do scrum-master manda --gravar sem caminho
  - **Contrato:** a medida do executor grava e é achada pelo mesmo caminho, em plano legado, em pasta e no diário
  - **Não refazer:** nada a declarar
  - **Pendente:** nenhum
- **Notas de execução:**
  - 2026-09-27 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-92a-o-destino-da-medida-do-executor-sai-de-uma-funcao-so-e-o-car.md`, veredito aprovado 100%

## TK-93 — A evidência não mostra o que mudou em arquivo não rastreado, e o redespacho perde a primeira execução

- **Status:** `done` · 2026-09-27 — aberto pelo consultor do `TK-86` (acionamento 2, `PC-3`), rota do achado `AE-78` do fechamento do `TK-86a`.

**Caso medido (2026-09-26):** (1) o `<ref>` do despacho é a saída de `git stash create` (Passo 4 do `scrum-master`), que não carrega arquivo não rastreado (armadilha já registrada em `docs/ARMADILHAS_DE_FERRAMENTA.md`, `AE-3` do `P-0750`). Para alvo não rastreado, `_diff_para_arquivo` do `review_evidence.py` devolve o arquivo inteiro, cortado no teto de 4000 caracteres: no `TK-86a`, `.claude/tools/encerrar.py` (não rastreado, 45974 bytes) saiu truncado antes das linhas 680-683, as editadas. (2) O redespacho do `TK-86a`, depois da triagem, capturou `<ref>` novo, e o `--desde` dele deixou fora da evidência os itens 1 a 3 da primeira execução. Protótipo do consultor (cópia da árvore, apagada): um `<ref>` que é commit, com pai `HEAD`, da árvore de trabalho inteira, gravado por índice temporário, mais a comparação de conteúdo do não rastreado presente no `<ref>`, dá na evidência do `TK-86a` só `encerrar.py` nos tocados e o hunk `@@ -679,6 +679,7 @@` da edição, sem mudar árvore, índice nem a lista de stash; suíte verde.

**O que decide:** correção conhecida — `review_evidence.py --capturar-ref` captura o `<ref>` com os não rastreados, e o `--desde` julga pelo conteúdo o não rastreado presente no `<ref>`; o Passo 4 manda capturar assim e manda o redespacho da mesma tarefa reusar o `<ref>` do primeiro despacho. Card `TK-93a`, `ready`, depois do `TK-92a` (os dois tocam `review_evidence.py` e o `scrum-master`). Descartado: recortar o não rastreado pelas âncoras do card (depende de o card escrever âncora de linha, e a linha anda com a edição); levar ao revisor dois `--desde` (o do primeiro despacho já cobre as duas execuções).
- **Notas de execução:**
  - 2026-09-26 `ready` — aberto com o card TK-93a (consultor TK-86, acionamento 2)
- **AE-93** (`TK-93a`, fechamento, 2026-09-27) — regressão: capturar_ref usa git add -A em índice vazio e deixa fora do <ref> o arquivo rastreado que casa com o .gitignore (git ls-files -ci), que o git stash create carregava; latente no PantonicApp (0 arquivos), vivo no PantonicVideo (4, egg-info) **Rota:** auditoria final
- **AE-94** (`TK-93a`, fechamento, 2026-09-27) — não rastreado binário ou não-UTF-8 intocado desde o <ref> entra em tocados em toda evidência (_nao_rastreado_mudou_desde_ref devolve True quando o texto não decodifica); o card não fechou a classe **Rota:** auditoria final



### TK-93a — O `<ref>` do despacho carrega o não rastreado, e o redespacho reusa o do primeiro despacho [Sonnet · esforço high · classe implementacao]

- **Status:** `done` · 2026-09-27
- **Depende de:** `TK-92a`
- **Objetivo:** em `.claude/tools/review_evidence.py`:
  1. `capturar_ref(root)` e a flag `--capturar-ref`, que imprime o `<ref>` e sai `0` sem exigir `--plano` nem `--tarefa` (sem a flag, os dois seguem obrigatórios): o `<ref>` é um commit cujo pai é `HEAD` (sem pai em repositório sem commit) e cuja árvore é a árvore de trabalho inteira — rastreados e não rastreados não ignorados —, gravado por índice temporário; árvore de trabalho, índice e lista de stash saem como entraram;
  2. com `--desde <ref>`, o arquivo hoje não rastreado e presente no `<ref>` é julgado pelo conteúdo, comparado linha a linha com o fim de linha normalizado: entra nos tocados só se mudou, e o trecho dele é o diff unificado entre o conteúdo no `<ref>` e o atual, ou `(sem alteração desde <ref>)` quando igual; ele não entra nos tocados pela saída de `git diff <ref> --name-only` (que o dá como apagado) e o estado dele na evidência segue `??`. Com `<ref>` de `git stash create` (sem não rastreados), o resultado é o de hoje;
  3. o Passo 4 do `scrum-master` manda capturar o `<ref>` pela flag e reusar o do primeiro despacho no redespacho (texto em `Passos`).
- **Arquivos-alvo:**
  - `.claude/tools/review_evidence.py`
  - `tests/test_review_evidence.py`
  - `.claude/skills/scrum-master/SKILL.md`
- **Passos:**
  1. Em `.claude/skills/scrum-master/SKILL.md`, Passo 4, as quatro linhas depois de `antigo:` viram as seis depois de `novo:` (as quebras são as do bloco; os rótulos não entram no arquivo; cada linha leva no arquivo os dois espaços de recuo que tem no bloco):

     ```text
     antigo:
       `docs/telemetria.tsv`. Capturar como `<ref>` (schema `DP-S`) a saída de `git stash create` —
       instantâneo dos arquivos rastreados no despacho, que não altera árvore, índice nem a lista de
       stash —, ou `git rev-parse HEAD` quando ela vier vazia (árvore limpa); usada no passo 6
       (`AUT-T5b`), onde o trecho de cada alvo passa a mostrar só o que mudou desde o despacho.
     novo:
       `docs/telemetria.tsv`. Capturar como `<ref>` (schema `DP-S`) a saída de
       `python .claude/tools/review_evidence.py --capturar-ref` — instantâneo da árvore de trabalho
       inteira no despacho, rastreados e não rastreados, que não altera árvore, índice nem a lista de
       stash; usada no passo 6 (`AUT-T5b`), onde o trecho de cada alvo passa a mostrar só o que mudou
       desde o despacho. No redespacho da mesma tarefa (retomada depois de `blocked`, ou retentativa),
       o `<ref>` não se recaptura: vale o do primeiro despacho, para a evidência cobrir as duas execuções.
     ```
- **Contratos/classes:** `capturar_ref(root: Path) -> str` (o SHA do commit); `--capturar-ref` é `store_true`, com `--root` opcional como hoje. As assinaturas de `coletar_arquivos_tocados`, `coletar_estado_git`, `montar_trechos` e `montar_documento` não mudam.
- **Caso medido que motivou:** ver `## TK-93`.
- **Testes (novos, em `tests/test_review_evidence.py`):** TF `test_tf_capturar_ref_carrega_nao_rastreado` — repositório temporário com um não rastreado: `git show <ref>:<arquivo>` devolve o conteúdo dele, e `git status --porcelain=v1 --untracked-files=all` e `git stash list` saem iguais aos de antes da captura. TF `test_tf_nao_rastreado_no_ref_mostra_so_o_hunk` — não rastreado de 400 linhas no `<ref>`, uma linha editada depois: o trecho traz a linha nova com `+` e não é truncado no teto de 4000, e `coletar_arquivos_tocados(repo, ref)` devolve só ele (outro não rastreado, sem mudança, fica de fora). Os TF da `TK-78c` (`<ref>` de `git stash create`) seguem verdes sem mudança.
- **Verificação:**
  1. `python .claude/tools/review_evidence.py --capturar-ref` → verde — antes `exit 2`, depois `exit 0`.
  2. `python -m pytest tests/test_review_evidence.py -q -k "capturar_ref or nao_rastreado_no_ref"` → verde — antes `exit 5`, depois `exit 0`.
  3. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print(t.count('git stash create'),t.count('review_evidence.py --capturar-ref'),t.count('vale o do primeiro despacho'))"` → `0 1 1` — antes `1 0 0`, depois `0 1 1`.
  4. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`.
  5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `kit_check: check-drift OK` — antes `exit 0`, depois `exit 0`.
- **Pronto quando:** a evidência de tarefa que edita arquivo não rastreado mostra o hunk da edição, e só o não rastreado que mudou entra nos tocados (Verificação 2); a captura existe e não mexe na árvore (Verificação 1 e 2); o Passo 4 manda capturar pela flag e reusar o primeiro `<ref>` (Verificação 3). Medido em protótipo do consultor sobre cópia da árvore com o `TK-92a` aplicado, apagada, em 2026-09-26: suíte `430 passed` → `432 passed`, `check-drift` OK.
- **Não fazer:** não mudar o teto de 4000 caracteres nem o recorte por data (`st_mtime`) do não rastreado ausente do `<ref>`; não tocar `_classificar_campo_alvos` (é do `TK-89a`) nem o destino da medida (é do `TK-92a`); não mudar `pantonic-reviewer.md`, que cita o `<ref>` do passo 4 e segue certo; não usar `git stash push` nem nada que mexa na árvore, no índice real ou na lista de stash.
- **Contingências:**
  - se um teste existente de `tests/test_review_evidence.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste (no protótipo, nenhum caiu).
- **Handover:** 2026-09-27 · para quem vier depois
  - **Entregue:** review_evidence.py --capturar-ref (capturar_ref: índice temporário com a árvore de trabalho) e julgamento por conteúdo do não rastreado presente no <ref>; scrum-master Passo 4 manda capturar assim e reusar o <ref> no redespacho
  - **Contrato:** a evidência mostra só o hunk do não rastreado que mudou desde o despacho
  - **Não refazer:** nada a declarar
  - **Pendente:** rastreado-e-ignorado sai do <ref> (git add -A em índice vazio); binário ou não-UTF-8 intocado entra sempre em tocados — AE com rota auditoria final
- **Notas de execução:**
  - 2026-09-27 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-93a-o-ref-do-despacho-carrega-o-nao-rastreado-e-o-redespacho-reu.md`, veredito ressalva 91%
