# Diário de Obras — PantonicApp (hub de governança Pantonic*)

**Diretiva de priorização:** Priorize a **residência e a distribuição de artefatos** (`TK-45` —
plano a autorar): decisão do dono de 2026-08-15, *"vamos parar por algumas tarefas e resolver isso
globalmente"*, com o alcance ratificado no mesmo ato — **o pacote passa a materializar também o
`~/.claude`**. A iniciativa `EXECUCAO-AUTONOMA` (`P-0734`) fica **suspensa em 49/60**, com a `T53` e
a `T54` **retidas** por resolverem o sub-caso do hook antes da regra geral (`G-SURFACE`); retoma
quando o plano de residência fechar. A quitação da dívida do hub (`P-0733`, parcial) vem depois.

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
| P-0730-V2I | Estágio 5 — identidade do framework: agnosticismo a stack/plataforma, CA+DDD, perfis e o README como contrato canônico (`T1..T11c` entregues; `T12` reprovou por identidade e derrubou a `DR-2`; `T13..T16` absorvidas) | superseded | substituído por `docs/plans/P-0731-v2-extracao-modalidade.md` |
| P-0731-V2E | Estágio 6 — extração da camada de modalidade: o conceito de perfil sai do hub, desktop e container viram ramificações próprias, fechamento pelo **congelamento da versão em `0.0.0`** (`DE-7`, 2026-08-07 — a `DE-4`/`3.0.0` foi revogada) (`V2E-T1..T11`, com `T3` partida em `T3a`/`T3b`/`T3c` e `T4` em `T4a`/`T4b`/`T4c` e `T6` em `T6a`/`T6b` por orçamento, `T5` em `T5a`/`T5b` por plano não-pronto e `T9` em `T9a`..`T9e` na reescrita do dossiê; 21/21) | done | `docs/plans/P-0731-v2-extracao-modalidade.md` |
| P-0732-V2P | Estágio 7 — as portas do core e a camada de casos de uso: contrato de porta para as 8 portas de runtime + superfície de entrada e execução assíncrona, residência do caso de uso (`plugins/<nome>/use_case.py` + campo `use_case` no manifesto) e as duas declarações de aderência "não auditado" fechadas com o medido (`V2P-T1..T10`; `DI-1..DI-8` todas de planejamento; 10/10) | done | `docs/plans/P-0732-v2-portas-do-core.md` |
| P-0733-DHB | Quitação da dívida de doutrina e de kit do hub — os 12 tíquetes vivos do índice em 13 tarefas (`DHB-T1..T13`): doutrina decidida e não executada (`TK-15`, `TK-17`, `TK-21`, `TK-22`), resíduo de vocabulário do kit (`TK-04`, `TK-12`, `TK-20`), guarda e navegação desalinhadas (`TK-06`, `TK-07`, `TK-10`), a não-promoção de "estágio" (`TK-08`) e a revisão final do espelho (`TK-18`); `DH-1..DH-7` fechadas no ato (1/13) | in progress | `docs/plans/P-0733-divida-do-hub.md` |
| P-0734-EXA | Execução autônoma — o backlog deixa de custar um round-trip humano por tarefa: papel de orquestração (skill `scrum-master`), papel de revisão (agente `pantonic-reviewer`) e documental gerado por função (telemetria/RDO/evidência), com o registro canônico da tarefa migrando do diário para `docs/RDO/` (`EXA-T1..T17`; `DA-1..DA-10` fechadas no ato, três desenhos postergados viram `T2`/`T3`/`T4`; alcance = hub primeiro, medir, depois propagar; `DA-9` revogada pelo dono em 2026-08-08 e substituída pela `DA-11` — Regra 2 passa a governar integridade de contexto, com a `T6` partida em `T6a`/`T6b`, a `T8` em `T8a`/`T8b`/`T8c` e a `T9` em `T9a`/`T9b` por orçamento; **`DP-D` ratificada em 2026-08-10** — o pacote de retorno de 8 campos deixa de existir, o RDO passa a ser gerado no fechamento e a retentativa vira agente novo em contexto novo, com `T18`..`T21` novas; **`DP-E` ratificada em 2026-08-11** — o `status` é característica da tarefa e quem o gerencia é o `scrum-master`, o laudo perde o campo, *inspetor* é abolido em favor de `pantonic-reviewer`, e os sete estados enunciados pelo dono viram objeto de avaliação própria antes de virar norma, com `T22`..`T27` novas e `T19`/`T20`/`T21` marcadas pendentes de reescrita; **`DP-F` fechada pela `T22` e ratificada pelo dono em 2026-08-11** — os sete estados avaliados como suficientes, com `backlog`→`ready`, `in progress`→`in-progress` e `superseded` fora do vocabulário de tarefa; destrava `T23`..`T27` e a reescrita de `T19`/`T20`/`T21`; `T23` partida em `T23a`/`T23b` por orçamento; **`DP-G` ratificada pelo dono em 2026-08-11** — a fronteira de `status` separa **autoria** (executor é autor de `review` e `blocked`, e de mais nada) de **materialização** (só o `scrum-master` grava, em qualquer estado), o `blocked` do executor é canal único com **razão tipada** (`dependencia` reordena a fila e segue; `premissa` para e escala), e daí a `T21` partida em `T21a`/`T21b` por orçamento mais a `T28` nova de sanitização; `T19`/`T20`/`T21` reescritos na mesma rodada e a fila reordenada para que a conformidade suceda o loop; **`DP-H` fechada em 2026-08-11**, por derivação do insumo do dono (`§12`) e sem decisão nova — a fronteira **conceito do framework × desenvolvimento do framework** escopa cada orientação, a regra de recência vale só dentro dos planos de desenvolvimento e não entra em artefato publicado, dossiê de tarefa executada é orientação e se concilia enquanto o que narra o ocorrido permanece intocado, o laudo é consumido e **descartado** pelo `scrum-master` e o `pacote` existe **dentro do laudo** (não é objeto devolvido pelo executor), com `T29` (artefato **tarefa**), `T30` (**utilidade**) e `T31` (resíduo de `pacote de retorno`) novas, `T19`/`T20`/`T21a`/`T21b`/`T23a`/`T26` e os achados do `§9` reconciliados, `TK-31` fechado e a fila reaberta pela `T19`; **`DP-K` fechada em 2026-08-11**, por ratificação do dono dos três pontos que a `DP-H` devolveu — a ambiguidade no framework **escala ao dono** (desempate que estava declarado não decidido, agora com residência no `GOVERNANCA.md` §3.1), `reviewer` vira **termo único** e abole também a forma *revisor* no texto vivo, e os **quatro artefatos canônicos** ganham hierarquia (plano → tarefa → laudo → RDO: a tarefa é a comunicação **entre agentes** e a verdade da tarefa em execução, o laudo é **efêmero** e move para `done` ou devolve para `in-progress`, o RDO é a comunicação com o **dono** e pressupõe tarefa finalizada, e **nenhum substitui o outro**), com `T32` (desempate) e `T33` (`reviewer`) novas e `T29`/`T30`/`T21a`/`T21b`/`T31` reconciliadas) **`TK-32` aberto em 2026-08-11** — uso e teto passam a ser medida de agregado, com regime interino de teto não-bloqueante e a `T34` nova, que decide e para junto de `DP-I`/`DP-J`; **`DP-M` ratificada em 2026-08-11** — o laudo se padroniza por função e vira mínimo e suficiente (`--observacoes` sai), e no lugar de coibir papel a papel entra a golden rule de escopo de agente como guardrail 15 do `GOVERNANCA.md` §7, com espelho em lockstep; a matriz de responsabilidades passa a ser autoridade exaustiva, o que torna a auditoria de completude precondição, e as tarefas `T35`..`T39` novas materializam a decisão; **`DP-N` ratificada em 2026-08-12** — o executor **sinaliza `review` ou `blocked` e nada mais**: não marca `in-progress`, não escreve bullet, não invoca `handover` e não grava consumo, e o achado fora de escopo vira uma linha do sinal que o `scrum-master` indexa; a verificação **fica** com ele, como responsabilidade de entregar tecnicamente correto, não de aferir aceitação; o `reviewer` não muda (dossiê + evidência + diff já são a coleta descrita), o `TK-35` fecha na `T40` e a reorganização da passagem de bastão vira o `TK-36`, com `T40`/`T41` novas; **`DP-O` fechada em 2026-08-12** — a matriz de responsabilidades é o **limitador exaustivo** de todo agente e o texto que atribui ato não endossado (ou papel sequer citado) é **não-conformidade grave, que para e regulariza**, com a régua já publicada no guardrail 15 e a resposta na descoberta entrando nele, mais a varredura dos dois universos fechados do framework e a lacuna da matriz subindo ao dono, materializadas em `T42`/`T43`/`T44`; **`T34` cancelada por absorção em 2026-08-12** — a matéria de uso e teto se revê inteira em plano próprio, aberto depois deste, o desdobramento é o item 4 da `T17` e nenhuma `DP-L` se forma aqui, de modo que a ratificação em lote fica com `DP-I` e `DP-J`; **bloco da `DP-O` encerrado em 2026-08-12 pela `T44`** — kit executável e doutrina varridos contra a matriz, com as duas ocorrências de classe (c) apontando para a lacuna já encaminhada ao `TK-36`; **`T25` fechada em 2026-08-13** — o espelho e os índices passam a falar a lista final da `DP-F` e a apontar para a residência única; **`T45` aberta em 2026-08-13** como card prioritário do `TK-39` — o critério de aceitação do §19 deixa de ser contagem de acionamentos do gerente; **fechada em 2026-08-13** — a aceitação passa a classificar cada acionamento pela causa (causa do gerente é legítima e ilimitada; caminho feliz é defeito), com residência na doutrina (`GOVERNANCA.md` §4.3) e na skill que conduz o loop, e o achado da tabela de riscos do §6 aberto como `TK-40`; **`DP-P` ratificada em 2026-08-13** — a golden rule do dono vira o guardrail 16 (`G-SURFACE`: mudança de decisão estruturante regulariza a superfície de contato inteira, no ato) e a consolidação é executada de imediato em dois universos fechados, com `T46` (a régua), `T47` (o plano) e `T48` (os artefatos publicados) novas, todas fechadas no mesmo dia — o `TK-40` quitado dentro da `T47`, o `TK-42` aberto com o resíduo fora dos universos declarados, e **duas ocorrências de classe (c) subindo ao dono como `TK-41`**, que bloqueia a `T16` e a `T17`; **`DP-Q` fechada em 2026-08-13** pela decisão do dono sobre o `TK-41` — teto numérico não governa fluxo (caem o roteamento por estouro `A4`, os dois números do fim de janela `B2`, o proxy operante de capacidade, o gatilho de checkpoint por 2/3 do teto e a ramificação por consumo no gerador), custo e consumo passam a ser informação de agregado com residência do qualitativo no card "Lições aprendidas na tarefa", e a matéria de limites vai inteira para plano próprio; primeira aplicação real do `G-SURFACE`, com `T49`, `T50`, `T51a`, `T51b` e `T52` novas e todas fechadas no mesmo dia, e a `T13` repositionada à frente da `T29` por virar o único critério de capacidade; **`T13` fechada em 2026-08-15** com laudo `aprovado` 100% e recomendação `escalar`, que sobe o `TK-43` ao dono; **`DP-R` fechada em 2026-08-15** — o *quê* por decisão do dono (hook canônico ganha **residência versionada própria**, com materialização no `settings.json` local; recusado o proxy só-do-hub, porque a capacidade do `GOVERNANCA.md` §4.3 vincula todo Pantonic\* e viraria regra sem meio de cumprimento no consumidor) e as **derivações de planejamento** fechadas na rodada do mesmo dia, sem decisão nova de arquitetura: residência em `.claude/hooks/hooks.json` com o comando portável por `{KIT_ROOT}`, materializador idempotente `.claude/tools/hooks_sync.py` (`apply`/`check`/`drift`) que preserva `permissions.deny` e todo hook não-kit, `kit_check` cobrando o canônico no `-Mode validate` e a materialização no `-Mode check-drift` (inclusive hook de kit registrado direto no arquivo local, que é a regressão do próprio `TK-43`), `sync-kit.ps1` inalterado e nenhum derivado tocado (`DA-3`; `docs/CONSUMIDORES.md` registra 0/6 com `.claude/kit/`), com `T53`/`T54` novas entrando **em bloco** logo depois da `T13` e antes da `T29`, o dossiê da `T14` reescrito (a rota por `settings.json` caiu; a tarefa passa a depender da `T53`) e o campo *Arquivos-alvo* do `### T13` conciliado com nota datada (`scrum-master` e `GOVERNANCA.md` §4.3, tocadas por consequência obrigatória); questão adjacente **fechada pela `DL-7`** (decisão do plano `P-0735`: `permissions.deny` é canônico, vira chave declarada do alvo `projeto`, `permissions.allow` e demais subchaves de `permissions` intocadas) — o `permissions.deny` do guardrail 13 tinha o mesmo defeito de distribuição; **rebaseado pelo `P-0735` em 2026-08-15** — classificação **(A)** da convenção de planos derivados: a premissa da iniciativa continua de pé, mas a matéria de residência e distribuição passa a ser resolvida em forma geral no plano novo, e o plano de origem fica **suspenso em 49/60** até ele fechar; `T53` e `T54` **canceladas por absorção** (o desenho da `T53` sobrevive integral na `RPC-T2`/`RPC-T3` e só a residência particular `.claude/hooks/hooks.json` desaparece; o item da `T54` que mandava preservar o bullet do hook global do `modelo-por-fase` é **revogado** pela régua nova), e a dependência declarada da `T14` passa da `T53` para a `RPC-T2` (49/60) | in-progress *(destravado em 2026-08-19 pelo fechamento do `P-0735`; retomado pela `T14`, que fechou no mesmo dia em **ramo B** — o `SubagentStop` expõe o consumo do subagente, mas não a identidade da tarefa, e o terceiro ramo — um contrato que a carregue até o hook — subiu ao dono como decisão; a `T15` fechou o enxugamento dos prompts com −1 linha líquida, medindo que o texto de formato coberto por instrumento já não vivia nos prompts declarados; a `T55` fechou a automação da série — o `scrum-master` grava a tarefa corrente e o hook de `SubagentStop` apende a linha sem gastar turno, com dedupe por `message.id` achado na calibração obrigatória; denominador 60 → 61 pela `DP-S`; 52/61)* | `docs/plans/P-0734-execucao-autonoma.md` |
| P-0735-RPC | Residência e ponto de carga — o pacote materializa o que a doutrina invoca: a régua de residência deixa de responder *onde mora* com uma resposta só e separa **autoridade** de **ponto de carga** em três classes (canônico · ponto de carga · local de máquina), com **pergunta zero** antes das quatro e o `Prec-2` promovido a **invariante** (*nada canônico mora só num ponto de carga*). Constrói o manifesto único `.claude/projecoes.json` e o materializador `.claude/tools/materializar.py` (`apply`/`check`/`drift`, alvos `projeto` e `usuario`), promove ao kit os **13 artefatos** que hoje só existem em `~/.claude/` (4 hooks registrados, 6 skills, 1 agente, 2 docs de doutrina) mais o `CLAUDE.md` global, declara por exaustão o que é **local de máquina** e faz o `kit_check` cobrar o canônico (`-Mode validate`) e a materialização do alvo `projeto` (`-Mode check-drift`). **9 tarefas** (`RPC-T1..T9`), decisões `DL-1..DL-9` fechadas no ato, todas de planejamento. Absorve `TK-45`, `TK-43` e o `permissions.deny` do `DP-R` §22.5, destrava o `DR-B`, e **não** absorve o `TK-21` (rota já decidida na `DH-4`, executável no `P-0733` `T10`). Alcance: hub primeiro, medir, depois propagar (`DA-3` mantida, 0/6 consumidores), alvo `usuario` **opt-in**, `sync-kit.ps1` inalterado. Sem bump e sem tag (`DE-7`). **`DL-10` decidida pelo dono em 2026-08-17** sobre o `TK-47` (achado da `RPC-T4`): `apply` passa a ser byte-idempotente sob equivalência semântica — recusada a alternativa de aceitar a normalização e afrouxar o critério da `T5` —, com a `T10` nova autorada fechada e entrando entre a `T4` e a `T5`; **`TK-49` (achado da `T5`, decidido pelo dono no mesmo dia) vira a `T11`**, autorada fechada logo depois da `T5` — `{KIT_ROOT}` passa a resolver para caminho absoluto; a `T6` foi executada em 2026-08-17 fora de ordem, à frente da `T11`, e a `T11` fechou em 2026-08-18, restabelecendo a ordem do §5; a `T7` foi **partida em `T7a`/`T7b`/`T7c` por orçamento** no gate de delegação (14 write-clusters medidos contra o limite de 8 na primeira partição; 10 na re-derivação da fatia do kit executável, que forçou a segunda; sem mudança de rota ou escopo em nenhuma das duas) (13/13 — `T1`, `T2`, `T3`, `T4`, `T10`, `T5`, `T6`, `T11`, `T7a`, `T7b`, `T7c`, `T8`, com a `T7` inteira fechada; `T8` fecha `.gitignore`/`CHANGELOG.md`/`TK-43`/`TK-45`/`permissions.deny` (`DL-7`), bateria de fechamento em exit 0, suíte 71 passed; `T9` fecha o espelho com veredito **aprovado** do dono: `check-readme.ps1` em exit 0 e dois trechos de estado anterior corrigidos (§4, que descrevia o hook como fora do kit, contra `GOVERNANCA.md` §3, onde ele é canônico e projetado; §1 e §11, que listavam permissões em bloco como configuração do operador, contra a `DL-7`, que tornou `permissions.deny` chave canônica do alvo `projeto`), com o §11 mantido sem enumerar `.claude/tools/` por decisão do dono — os cinco instrumentos restantes são entregáveis do `P-0734` e entram quando aquela iniciativa fechar. Consumo: ver `docs/telemetria.tsv`) | done | `docs/plans/P-0735-residencia-e-ponto-de-carga.md` |
| P-0722 | Guardrails de doutrina anti-saga (G-DEADCODE, G-PLANFIDELITY, G-PREMISE, G-PLANREADY, G-EXECREADY) | superseded | mesclado em `P-0729-v2-melhoria.md` §1 |
| P-0721 | Governança single-source: PantonicApp como referência | done | `docs/plans/P-0721-governanca-single-source.md` |
| P-0725-3C | Governança em três camadas condicionais | superseded | substituído por `P-0725-governanca-hub-unico.md` |
| P-0725-HU | Hub único: PantonicApp canônico, PantonicVideo como prova | done | `docs/plans/P-0725-governanca-hub-unico.md` |
| TK-01 | Corrigir residência de `modelo-por-fase` em `GOVERNANCA.md` §3 e no bullet `V2M-T1` do `CHANGELOG.md` (ainda apontam `~/.claude/skills/`, superado por `DM-7`) | done *(absorvido pela `V2M-T3`)* | `docs/DIARIO_HISTORICO.md#tíquetes-avulsos--condensado-em-2026-08-01` |
| TK-02 | `.claude/sync-kit.ps1`: `Get-ExcludedKeys`/`Test-Excluded` quebram sem `kit-exclude.txt` presente (achado pré-existente, `V2K-T11`) | done | docs/DIARIO_HISTORICO.md#tíquetes-avulsos--2ª-condensação-2026-08-01
| TK-05 | Skill `checar-versao-kit`: o gatilho de revisão de doutrina (`GOVERNANCA.md` §7.1) compara só o componente MINOR e fica cego ao atravessar um MAJOR (local `2.0.0` × última rodada `1.4.0` ⇒ "sem pendência" indevido). **Resolvido por remoção do mecanismo** (`DE-8`, 2026-08-07): o gatilho de revisão deixa de pender de versão e passa a pender do fechamento de um plano, então a comparação de MINOR — e com ela a cegueira ao atravessar um MAJOR — sai do procedimento. Execução na `V2E-T9c`; a distinção MAJOR × MINOR/PATCH da checagem de **versão**, que é outra coisa, permanece intacta | done *(achado do planejamento do `P-0730`; fechado pela `DE-8`, execução na `V2E-T9c`)* | `docs/plans/P-0731-v2-extracao-modalidade.md` §8 |
| TK-06 | `docs/DOC_MAP.md` lista `GOVERNANCA.md` entre os "docs abaixo de 500 linhas (Read direto)", mas o arquivo já está em **644 linhas** — o mapa manda ler integralmente um doc que passou do limite e não tem entrada de âncoras. Drift pré-existente (já >500 antes da `V2I-T5`); corrigir criando a entrada de navegação da GOVERNANCA no DOC_MAP | backlog *(achado da `V2I-T5`)* | `docs/DOC_MAP.md:7-9` |
| TK-04 | `.claude/agents/pantonic-executor.md:20` hardcoda "orçamento esperado ~≤40 tool uses" — diverge de `DR-C`/`V2K-T16` (o kit, `GOVERNANCA.md` §3, já é a única autoridade numérica, tabela de tetos por classe; o global perdeu o número na `T17`) | backlog *(achado da `V2K-T17`)* | `.claude/agents/pantonic-executor.md:20` |
| TK-07 | `check-readme.ps1` só indexa seções que casam `^## (\d+)\. ` — seção `##` **não numerada** (o glossário da `V2I-T11b`) fica invisível às cinco checagens, inclusive à exigência de `> Fonte da verdade:`; decidir se o guarda passa a cobrir seção não numerada ou se a regra vale só para as numeradas | backlog *(achado da `V2I-T11b`)* | `.claude/checks/check-readme.ps1:58` |
| TK-08 | "Estágio" (subdivisão de iniciativa) estrutura toda a `PANTONIC-V2` mas não tem residência normativa — não está em `GOVERNANCA.md` nem em skill; decidir se vira conceito com regra de abertura/fechamento ou permanece convenção do diário | backlog *(achado da `V2I-T11b`)* | `docs/DIARIO_HISTORICO.md#sprint-pantonicv2--consolidação-do-framework-em-v2` (bullet `V2I-T11b`) |
| TK-10 | `docs/DIARIO_DE_OBRAS.md` em 937 linhas, muito além do gatilho de ~500 da operação "Condensar" — as seções dos estágios 1 a 4, todas terminais, deveriam estar em `docs/DIARIO_HISTORICO.md` | done *(fecha na `DHB-T1`: seção terminal migrada para o histórico, diário em 78 linhas)* | `docs/plans/P-0733-divida-do-hub.md` `### T1` |
| TK-09 | Skill de redação de documentação — todo doc publicado que a IA escreve vem contaminado por **narrativa de proveniência**: relato das conversas com o dono, episódio que motivou cada procedimento, ID de tarefa/estágio no corpo do texto. Vício de escrita, não defeito de um documento; precisa de critério reexecutável | done *(skill `redacao-doc` autorada em 2026-08-06; aplicação ao README é a `V2I-T11c`)* | `.claude/skills/redacao-doc/SKILL.md` |
| TK-11 | `ARQUITETURA_PANTONICA.md` §9 ("Condições de POC integrável"), bullet do TaskRunner, cita "(§10)" apontando para a seção MVVM/Threading que a `V2E-T3a` extraiu para a doutrina; a renumeração das seções seguintes fez `§10` existir de novo (agora "Operações de OS e IN/OUT", conteúdo não relacionado), então a referência aponta para um número válido mas semanticamente errado. Resolvido pelo orquestrador na mesma rodada: o ponteiro de seção foi removido (`sempre TaskRunner;`) — a doutrina extraída vive em pasta fora do versionamento e não pode ser destino de referência do hub, e a regra se sustenta afirmada inline. A frase "UI thread" do mesmo bullet é escopo da `V2E-T3b` | done *(achado da `V2E-T3a`, fechado em 2026-08-06)* | `ARQUITETURA_PANTONICA.md` §9, bullet TaskRunner |
| TK-12 | `.claude/skills/audit-sweep/SKILL.md`, `description` do frontmatter, ainda cita "pyside6" como um dos tipos de varredura ("arch, pyside6, cleancode, fora-da-caixa") — residual fora dos blocos `ARCH-mvvm`/`DDD-pureza`/`PYSIDE` que a `V2E-T4b` já havia extraído; a `V2E-T4c` mediu ao verificar o total do kit (Grep caiu de 9 para **1**, não para 0) e não o tocou por estar fora dos três arquivos-alvo daquela fatia | done *(fechado pela `EXA-T43` em 2026-08-12: a `description` passou a citar a frente **DDD** no lugar de "pyside6", como ocorrência de classe (b) da sanitização contra a matriz)* | `.claude/skills/audit-sweep/SKILL.md:3` |
| TK-13 | Carregar `.claude/checks/dead_code.py` por caminho via `importlib.util.spec_from_file_location`/`exec_module` (padrão exigido pela `T5a` porque `.claude/checks/` tem ponto no nome e não é pacote importável) grava bytecode em `.claude/checks/__pycache__/`; `.gitignore` não tem entrada para `__pycache__/`, então o diretório aparece como untracked em todo `git status` após rodar `python -m pytest` — adicionar o padrão ao `.gitignore` | done *(fechado pelo orquestrador na mesma rodada, 2026-08-06: `__pycache__/` + `*.pyc` no `.gitignore` — consequência mecânica da suíte recém-criada, edição de risco zero)* | `.gitignore` |
| TK-14 | O framework nunca foi lançado em público: não existe `V0`/`V1`/`V2`, e todo o trabalho até aqui é o desenvolvimento da **primeira** versão (veredito do dono na `V2E-T8`). A consequência para o `README.md` já foi aplicada (§15 removida), mas a premissa atinge a `T9` do `P-0731`, cujo dossiê manda escrever `CHANGELOG.md` §3.0.0 com instrução de migração: decidir se o registro de histórico de alterações se mantém como artefato de distribuição (5 consumidores materializam o kit por versão) ou se cai junto com a numeração de versões. **Decidido pelo dono em 2026-08-07:** o número de versão **fica** como artefato, congelado em **`0.0.0`** até que ele decida publicar — antes do lançamento a numeração não tem valor, e só passa a ter depois; o `CHANGELOG.md` permanece (ver `TK-15`). A `T9` deixa de fechar `3.0.0` e passa a fechar o congelamento. Superfícies a reconciliar, medidas: `VERSION` e `.claude/KIT_VERSION` (paridade checada por `kit_check.ps1 -Mode validate` e pela checagem 3 do `check-readme.ps1`); `README.md:3` e `README.md:829`, as duas linhas que o guarda exige; `README.md` §13, onde o bump obrigatório a cada mudança canônica, a tag `kit-v<versão>` (colide com número congelado) e os quatro desfechos da checagem de versão perdem função; `GOVERNANCA.md` §9, fonte da verdade do §13; a skill `checar-versao-kit`, que passa a reportar sempre "versões iguais" — e torna o `TK-05` sem objeto enquanto durar o congelamento; `docs/CONSUMIDORES.md` e os 5 consumidores, para quem a deriva deixa de ser detectável por versão e passa a depender de `-Mode check-drift`. Ponto que o replanejamento precisa fechar antes de a `T9` ser performável: o que acontece com o que já foi numerado — as entradas `§1.x`..`§2.0.0` do `CHANGELOG.md` e as tags `kit-v*` já publicadas — sob um número que volta a `0.0.0`. **Fechado em 2026-08-07 pela reescrita do dossiê da `T9`:** a `DE-4` (fechamento em `3.0.0`) foi revogada, entrou a `DE-7` — o número congela em `0.0.0` e o que já foi numerado **permanece** como histórico de desenvolvimento pré-lançamento (as 8 tags `kit-v*` não são tocadas, as seções `1.0.0`..`2.0.0` do `CHANGELOG.md` não são reescritas, e `[Não lançado]` vira a única seção viva) —, e a `T9` virou `T9a`..`T9d` | done *(achado da `V2E-T8`; consumido pela reescrita do dossiê, 2026-08-07)* | `docs/plans/P-0731-v2-extracao-modalidade.md` `### T9` |
| TK-15 | `.claude/skills/redacao-doc/SKILL.md` §5 abre a classe **"Seção histórica declarada"** — uma seção do doc publicado cujo assunto *é* a mudança entre versões, com o vício `V7` liberado. Essa isenção é o que manteve a §15 do `README.md` viva por três rodadas de redação: a varredura mecânica do §6 não acusa nada nela (medido na `V2E-T8`: 0 ocorrências de `V1`,`V2`,`V4`,`V6`,`V7`,`V8`,`V10` no README antes e depois do corte). Decidir se a classe sai da skill ou se ganha condição de existência explícita. **Decidido pelo dono em 2026-08-07:** a classe **sai**. O histórico ganha residência num documento de finalidade estrita, e esse documento é o **`CHANGELOG.md`** que já existe, isento das restrições de redação do agente. Doc publicado não é lugar de histórico, e as restrições de padronização de escrita valem nele **sem exceção** — o `README.md` inclusive. A skill perde a linha do meio da tabela do §5 (a classe passa a ter duas entradas: **publicado**, com `V1..V10` proibidos, e **registro**, isento) e o §4 continua apontando "o que mudou entre versões → `CHANGELOG.md`" | **decidido** *(achado da `V2E-T8`; execução pendente de tarefa própria)* | `.claude/skills/redacao-doc/SKILL.md` §5 |
| TK-16 | A porta de saída de guardrail (`GOVERNANCA.md` §7.1) pendura o gatilho de revisão no **fechamento de um MINOR do kit**. Com a versão congelada em `0.0.0` (`DE-7`) nenhum MINOR fecha e o gatilho não dispara — a `V2E-T9a` declara a suspensão no próprio §7.1 —, de modo que enquanto durar o congelamento o framework **só adiciona regra** e nenhuma pode sair: exatamente o apodrecimento que a §7.1 existe para impedir. Escolher o gatilho substituto é decisão de doutrina do dono. **Decidido pelo dono em 2026-08-07 (`DE-8`):** o gatilho deixa de pender do fechamento de um MINOR e passa a pender do **fechamento de um plano** (`P-NNNN` → `done` no índice deste diário) — preserva a intenção original (revisão atrelada a marco real de evolução, nunca a calendário) sem depender de um número que deixou de andar, apoiada num evento que já existe, já é registrado no índice e teve historicamente a mesma cadência dos MINORs. Recusadas: cadência por contagem de tarefas concluídas (mede volume, não marco) e suspender a revisão até o lançamento (é o apodrecimento que a §7.1 existe para impedir, e o congelamento não tem prazo). Escopo, janela da pergunta e transição passam a ser contados em **rodadas**. Execução: `V2E-T9b` (doutrina §7.1), `V2E-T9c` (procedimento da skill) e `V2E-T9e` (espelho no README). **Fechado em 2026-08-07 pela `V2E-T9b`:** a §7.1 passou a pender do fechamento de plano, com escopo, janela da pergunta, transição e registro contados em rodadas — o gatilho volta a disparar sob número congelado, que é o objeto do tíquete; o espelho (`T9e`) e o mecanismo executável (`T9c`) seguem como fatias do `P-0731` | done *(achado da reescrita do dossiê da `V2E-T9`, 2026-08-07; decidido e executado no mesmo dia)* | `docs/plans/P-0731-v2-extracao-modalidade.md` §8 |
| TK-17 | `GOVERNANCA.md` é doc da classe **publicado** (`redacao-doc` §5), onde `V3` (id de processo) e `V7` (datação viva) são proibidos com piso de aceite zero, mas o corpo fora da §10 concentra 25+ ocorrências: datas explícitas em §3 (L106, L118, L137-144), ids de tarefa e plano em §7 (L459, L474-476, L498, L511, L520, L523), §7.1 (L546, L577, L585-592) e §9 (L619-624, L630). Parte é razão legítima enunciada como fato medido (`redacao-doc` §3 — a evidência que sustenta o limiar), parte é proveniência pura. A §10 foi saneada na `V2E-T9a` e serve de referência de forma. **Decidido pelo dono em 2026-08-07: limpar tudo** — nenhuma ocorrência de `V3`/`V7` sobrevive no arquivo, nem as que enunciam razão como fato medido; a regra que a medição sustentava é afirmada inline, sem ponteiro de proveniência (padrão do `TK-11`), e a medição continua registrada onde é histórico (plano, diário, `CHANGELOG.md`). Piso de aceite da varredura do §6 sobre o arquivo inteiro passa a **zero**; a §10 é a referência de forma. Recusada a alternativa de preservar caso a caso o fato medido: o critério por seção era o próprio custo a evitar. **Precondição decidida em 2026-08-08:** o bloco *Registro das rodadas* da §7.1 é registro por desenho — o rótulo `<P-NNNN> — <AAAA-MM-DD>` é o mecanismo, não proveniência — e esta limpeza o apagaria; ele sai da `GOVERNANCA.md` primeiro (`TK-22`), e só depois o piso zero de `V3`/`V7` vale para o arquivo inteiro **sem exceção**, como decidido. Sem essa ordem, a limpeza precisaria de uma isenção por bloco — exatamente o que o `TK-15` acabou de remover da skill | **decidido** — execução pendente de tarefa própria, depois do `TK-22` *(achado da `V2E-T9a`)* | `docs/plans/P-0731-v2-extracao-modalidade.md` `## Achados da execução` |
| TK-18 | **Revisão final do espelho do `README.md`.** O `check-readme.ps1` verifica que cada seção declara uma `> Fonte da verdade:` existente, mas não compara o **texto** do espelho com o da fonte — a fidelidade do conteúdo é responsabilidade de quem executa a tarefa, e um par fiel hoje pode divergir em silêncio numa edição futura. Medido na `V2E-T9e`: o parágrafo do apodrecimento em `README.md` §10 espelha `GOVERNANCA.md` §7.1 e foi conferido à mão, sem guarda executável; o dossiê daquela fatia já previa a ausência de guarda e atribuiu a conferência à execução. Escopo: varrer o espelho inteiro (as 14 seções com `Fonte da verdade` declarada) contra as fontes correspondentes, e decidir o que fica sob guarda executável e o que permanece sob conferência humana. Achado de mesma natureza descoberto durante a construção acumula neste tíquete em vez de abrir tíquete novo. **Decidido pelo dono em 2026-08-07:** é revisão **final** — executa só ao término das operações de construção, nunca no meio delas; revisar espelho enquanto as fontes ainda mudam é conferir duas vezes o mesmo texto | blocked — *validação postergada* (destrava quando as operações de construção terminarem) *(achado da `V2E-T9e`)* | `.claude/checks/check-readme.ps1`; `README.md` §10 |
| TK-19 | Teto de bullet do diário na skill `handover` (gatilho de condensação) estava em ~10 linhas e era estourado por 100% dos bullets da sprint (`V2E-*` em 20-30 linhas; `V2P-T1` em ~30) — regra nunca cumprida é regra errada, não prática errada. **Decidido pelo dono em 2026-08-07: ajustar o teto ao real**; recusadas "manter e cumprir" (desloca o detalhe de fechamento para fora do kanban sem impedir o crescimento) e "deixar como está" (teto nominal ignorado). O gatilho de ~500 linhas do diário inteiro permanece intacto e continua sendo o controle de tamanho, junto do `TK-10` | done *(achado da `V2P-T1`; fechado pelo orquestrador na mesma rodada — edição de 1 linha em skill)* | `.claude/skills/handover/SKILL.md:41` |
| TK-20 | `.claude/skills/integrar-poc/SKILL.md:23` nomeia a **implementação de referência como se fosse a regra** — "estado via `PathsService`; trabalho pesado via `TaskRunner`" —, resíduo da mesma classe que a `V2P-T2` removeu dos outros artefatos do kit, mas fora dos três arquivos-alvo daquele dossiê. Não tem "UI thread" (por isso escapou da varredura da `T2`); o desvio é citar nome de componente do case onde a doutrina deveria citar a porta (raiz de dados e execução assíncrona). Corrigir para o vocabulário de portas da `ARQUITETURA_PANTONICA.md` §4 | backlog *(achado da `V2P-T2`)* | `.claude/skills/integrar-poc/SKILL.md:23` |
| TK-21 | O ratchet do **piso comportamental** roda **sem alvo em toda parte**: no hub, `ratchet_piso.py` entra na bateria de fechamento de toda tarefa mas reporta sempre `exit 0 — nenhum piso declarado`, porque `tests/piso_comportamental.txt` nunca foi criado (nem depois de a `V2E-T5a` dar suíte ao hub); nos consumidores, `.claude/checks/` não existe (`0/6` materializam o kit — medido em `docs/CONSUMIDORES.md`, confirmado por `Test-Path` no `PantonicVideo`). O guardrail do piso (`GOVERNANCA.md` §7 item 6) foi **retido com caso citável de registro**, não pelo check — o check é vacuidade, e a §7.1 diz que check neutralizado não isenta. Decidir se o hub declara piso próprio para a suíte que já tem, se o ratchet passa a rodar contra o consumidor por `--root`, ou se o piso é reconhecido como regra procedimental sem enforcement executável. **Decidido pelo dono em 2026-08-08:** o ratchet passa a rodar **contra o consumidor**, por `--root` — é onde o piso tem objeto, porque o hub não tem código de produção. Recusadas: declarar piso próprio no hub (protegeria 3 asserções de um repositório sem produção — cobre o lugar errado) e reconhecer o piso como regra procedimental sem enforcement (deixaria o item 6 de §7 dependente de caso citável em toda rodada futura, marcável por ausência de atividade no consumidor e não por morte da regra). O que a execução precisa resolver, medido nesta rodada: `tests/piso_comportamental.txt` **não existe** no `PantonicVideo` (o piso comportamental do consumidor ainda precisa ser autorado, uma frase por comportamento), e falta fixar onde a invocação com `--root` mora — bateria de fechamento do hub, skill `guardrails-check` ou fechamento de tarefa do próprio consumidor | **decidido** — execução pendente de tarefa própria *(achado da `V2P-T7`)* | `.claude/checks/ratchet_piso.py`; `GOVERNANCA.md` §7 item 6 |
| TK-23 | A variante (b) do proxy de ocupação de contexto — contador de tarefas por janela calibrado pela série de `docs/telemetria.tsv` — não foi medida pela `EXA-T1` (orçamento esgotado). A variante (a), hook lendo o `transcript_path` exposto no payload de `PreToolUse`, tem viabilidade técnica confirmada com evidência colada. Decidir entre as duas é escopo da `EXA-T13`; se (b) continuar viva quando a `T13` chegar, ela precisa de sonda dedicada antes da escolha — nenhuma decisão pode se apoiar em (b) como se fosse medida | backlog *(achado da `EXA-T1`)* | `docs/audits/SPIKE_HARNESS_EXECUCAO_AUTONOMA.md` §"Nota de escopo" |
| TK-24 | `P-0733` tem **12 tarefas não iniciadas** cujo cabeçalho (`[Opus]`/`[Sonnet]`) não carrega `classe` nem `teto`, e portanto fica fora do esquema fixado pela `DP-C`. Retrofit é **ato de planejamento**, não de execução — a classe é escolhida no dossiê antes de delegar (`GOVERNANCA.md` §3) —, e a `EXA-T4` não edita outro plano. Escopo: completar os 12 cabeçalhos para `### <ID> — <título> [<modelo> · classe <slug> · teto <N>]`, com `<slug>` no conjunto de cinco e `<N>` igual ao teto da classe. Não bloqueia nada: `rdo.py` (`EXA-T8`) nasce com o caminho de plano legado por desenho | backlog *(achado da `EXA-T4`)* | `docs/plans/P-0733-divida-do-hub.md`; `docs/plans/P-0734-execucao-autonoma.md` `### DP-C` |
| TK-22 | O bloco *Registro das rodadas* (`GOVERNANCA.md` §7.1) ganha **residência própria**, num documento de finalidade estrita isento das restrições de redação, e a §7.1 passa a apontar para ele. **Reuso do `CHANGELOG.md` verificado e recusado em 2026-08-08**, por três medidas: (1) `CHANGELOG.md:3` declara como objeto as **mudanças notáveis** do framework, e o resultado normal de uma rodada é **0 marcações** — não-mudança que a §7.1 exige registrar mesmo assim ("revisão sem registro não aconteceu"); registro cujo caso comum é "nada mudou" não cabe num changelog; (2) a chave de organização do `CHANGELOG.md` é a **versão** e a do registro é o **fechamento de plano** — sob o congelamento tudo cai em `[Não lançado]`, e quando o congelamento acabar essa seção vira uma versão numerada, fatiando o registro entre seções de versão de forma permanente, quando o mecanismo precisa de lista contígua onde "última" e "penúltima rodada" sejam localizáveis; (3) o registro é **lido por mecanismo** — `.claude/skills/checar-versao-kit/SKILL.md:83-84` faz Grep por `Registro das rodadas` em `GOVERNANCA.md` §7.1 e confronta a última rodada com o índice deste diário. O `CHANGELOG.md` continua ganhando entrada quando a rodada **produzir** mudança (guardrail marcado ou removido) — aí sim é mudança notável. Superfícies medidas para a execução: `GOVERNANCA.md` §7.1 (o bloco mais a prosa que diz "a lista abaixo", L558 e L600) e a skill `checar-versao-kit` (L83-84); `README.md` **não** referencia o bloco (L701 espelha só o parágrafo do apodrecimento) e `docs/DOC_MAP.md` ganha o doc novo. **Bloqueia o `TK-17`** | **decidido** — execução pendente de tarefa própria *(achado da `V2P-T7`)* | `GOVERNANCA.md` §7.1; `.claude/skills/checar-versao-kit/SKILL.md:83-84` |
| TK-25 | `docs/RESIDENCIA_DOUTRINA.md:89` (seção **Regra 3**, item 3.5) aponta "§7 item 8 ('docs grandes via índice')" quando esse conteúdo é do **item 7** — o mesmo drift de numeração que a `EXA-T6b` corrigiu na nota da seção "Regra 2", mas em seção fora dos alvos daquele dossiê, por isso não corrigido junto. Escopo: trocar a referência para "§7 item 7" e conferir se as demais faixas de linha citadas pelo documento acompanharam as edições que já ocorreram em `~/.claude/CLAUDE.md` | backlog *(achado da `EXA-T6b`)* | `docs/plans/P-0734-execucao-autonoma.md` `## Achados da execução`; `docs/RESIDENCIA_DOUTRINA.md:89` |
| TK-26 | `docs/telemetria.tsv` usa duas formas distintas de sentinela para "métrica não medida" nas 3 linhas com `fonte=nao_medido` medidas na `EXA-T7`: célula vazia (`V2K-T17`, `V2K-T19`) e traço literal `-` (uma linha com `fonte=contado`, `V2I-T3`) — sem convenção fixa entre as duas. `.claude/tools/telemetria.py` (`EXA-T7`) exige número válido em `tool_uses`/`tokens_k`/`duracao_s` em toda chamada `append` e não aceita nenhuma das duas formas — decisão deliberada de escopo mínimo (dossiê da `T7` só cobre linha válida/`fonte` inválida/campo numérico não numérico/preservação byte a byte, nenhum teste de sentinela). Decidir a convenção única (célula vazia **ou** `-`, nunca as duas) e se `append` passa a aceitá-la é escopo de tarefa própria — sem isso, uma tarefa futura com `fonte=nao_medido` não tem como registrar consumo pelo script novo. **Decidido pelo dono em 2026-08-08:** a sentinela única é a **célula vazia**, e o `append` passa a aceitá-la nas três colunas numéricas **apenas** quando `fonte=nao_medido` — é a forma majoritária da série, é a que um leitor de TSV por `split('\t')` já trata como ausência, e o `-` obrigaria todo consumidor futuro do arquivo a conhecer uma regra extra. Recusadas: padronizar em `-` (sentinela visível, mas empurra a regra para todo leitor) e não aceitar sentinela alguma (manteria a edição manual do TSV justamente no caso que a `EXA-T7` existiu para eliminar). Escopo da execução: `telemetria.py` aceita célula vazia nas colunas numéricas; teste de regressão para aceitação e para recusa; **1** linha histórica com `-` (`docs/telemetria.tsv:50`, `V2I-T3`, `tokens_k` e `duracao_s`) normalizada para célula vazia — única exceção à regra "só apende", por ser correção de sentinela, não de número. **Medido na ratificação (2026-08-08, corrige a contagem do achado):** a célula vazia aparece em **14** linhas e o `-` em **1**; das 14, **11 têm `fonte=contado`** (`tool_uses` preenchido, `tokens_k`/`duracao_s` vazios) e só 3 têm `nao_medido` — de modo que restringir a aceitação de vazio a `fonte=nao_medido` impediria o script de reproduzir a forma dominante da própria série. **Ponto aberto fechado em 2026-08-11, por delegação do dono ao orquestrador** (questão operacional, não tática): a célula vazia é aceita nas três colunas numéricas **sempre que `fonte` ≠ `usage`**. `usage` significa que o número veio do bloco `<usage>`, que carrega os três — célula vazia ali é medida **perdida**, não medida ausente, e deve falhar ruidosamente; `contado` e `nao_medido` são exatamente os casos em que parte ou todo o número não existe. A regra reproduz a forma dominante da série (11 linhas `contado` com `tool_uses` preenchido e as outras duas vazias) sem forçá-la, e não exige que o consumidor do TSV conheça combinação nenhuma além de "vazio = ausente". **Evidência nova da mesma rodada:** a linha `EXA-DPG-replan` (`fonte=contado`) **não pôde ser apendada pelo script** e foi escrita à mão — o defeito já não é hipotético sobre `nao_medido`, é bloqueio medido no caminho comum | **decidido** — execução pendente de tarefa própria *(achado da `EXA-T7`)* | `.claude/tools/telemetria.py`; `docs/telemetria.tsv:17,40,42,50` |
| TK-27 | A independência do `pantonic-reviewer` é **parcial na lista de ferramentas**: `Write`, `Edit` e `NotebookEdit` estão fora, mas `Bash` é necessário para invocar `rdo.py laudo` e, sem escopo, permite escrita arbitrária no repositório — o "por construção" do critério de pronto da `EXA-T10` fica sustentado pela ausência das ferramentas de edição mais a proibição em prosa, não pela impossibilidade técnica plena. Não resolvido na tarefa porque escopar o comando no campo `tools:` do frontmatter é sintaxe não documentada para agentes: se o harness ignorar o especificador, o reviewer perde `Bash` inteiro e não emite laudo nenhum. Escopo: (a) confirmar empiricamente se `tools:` aceita especificador de `Bash`, ou (b) impor o escopo por regra de permissão de projeto — a escolha entre as duas é do dono | backlog *(achado da `EXA-T10`)* | `.claude/agents/pantonic-reviewer.md` (frontmatter `tools:`) |
| TK-28 | `docs/plans/P-0734-execucao-autonoma.md` `### T19` não fecha a lacuna que a própria `DP-D` (§9) deixou aberta sobre a origem do parâmetro `status` de `calcular_desdobramento` depois que o pacote de 8 campos sai (`D2`, "pacote não existe"): `D5` separa o que "passa ao laudo" (`A5`/`A6`/`A8`/`A9`) do que "permanece no loop" (`A1`/`A2`/`A4`/`A7`/`B1`-`B3`) e **omite `A3` (bloqueado)` das duas listas**, sem dizer se `close` ainda recebe algum equivalente a `--status` ou se a assinatura de `calcular_desdobramento` (reusada sem mudança declarada, `:589`) muda. Segunda lacuna do mesmo dossiê: `D1` aponta `pendencia_para_o_dono` para "retorno do executor (campo opcional) ou laudo", mas o `### T19` não lista um flag para esse canal opcional nem instrui removê-lo. Replanejar o dossiê da `T19` (fechar as duas lacunas) antes de redelegar. **Fechado em 2026-08-11 pela rodada de replanejamento**, as duas lacunas por derivação de cláusula já ratificada, sem decisão nova do dono: (1) o `status` é materializado onde a `DP-D` já o alocou — `laudo --status` obrigatório com domínio fechado grava `**Status:**` no documento de laudo, e o `close` lê de lá; `calcular_desdobramento` **não** muda assinatura nem corpo (ponteiro corrigido de `:589` para `:624`); recusada a derivação do `status` a partir do veredito, que contraria `D1` e tornaria `bloqueado` inalcançável; (2) `A3` não estava em nenhuma das duas listas do `D5` porque é o único caso com **condição** e **ação** em lados diferentes — a condição foi ao laudo por `D1`, a ação é do loop como todo o bloco A —, registrado como nota de derivação datada no §9, subordinada à `DP-D` e sem tocar o texto ratificado; (3) `close` ganha `--pendencia`, opcional, uma linha, único argumento de conteúdo, com a composição do campo fixada em tabela de 4 linhas | done *(achado do bloqueio da `EXA-T19`; fechado pelo replanejamento de 2026-08-11)* | `docs/plans/P-0734-execucao-autonoma.md` `## Achados da execução`, `### T19`, `### DP-D` (§9, `D1`/`D2`/`D5`) |
| TK-30 | Três fatos normativos sobre `superseded` ficaram **sem residência** quando a `EXA-T23a` substituiu o bullet *Status válidos* de `.claude/skills/diario-de-obras/SKILL.md` pela residência única: que ele é **terminal**, que **condensa para o histórico** e que **sai do backlog** (não é escolhível). A `DP-F` não reenuncia nenhum dos três — ela só posiciona `superseded` como estado exclusivo de plano/iniciativa, e sua máquina de transições é de tarefa, sem nenhuma aresta para `superseded`. O executor agiu certo ao não inventar a regra (a residência única enuncia só o ratificado), então os três fatos ficaram órfãos. Escopo: decidir se a `DP-F` ganha as arestas e propriedades de `superseded` no vocabulário de plano/iniciativa, ou se isso é escopo da reescrita da `T27`; a decisão precede a edição. Enquanto pendente, a regra continua afirmada nos demais pontos do arquivo que citam `superseded` (planos derivados, convergência). **Segunda ocorrência medida pela `EXA-T25`** (2026-08-13), do lado de fora do arquivo: ao espelhar a lista final no `README.md` §7, mediu-se que `superseded` consta da `### Alcance por objeto` da residência única mas está **ausente da `### Lista final` e da `### Máquina de transições`** — o único estado terminal de plano não tem gatilho de entrada nem aresta na fonte da verdade, e por isso o espelho o enuncia sem poder apontar transição. Nenhum tíquete novo: é a mesma lacuna deste tíquete, medida por outra superfície, e a decisão continua sendo a que ele já pede — arestas na `DP-F` ou escopo da reescrita da `T27`. **Decidido pelo dono em 2026-08-13:** as arestas e propriedades de `superseded` no vocabulário de plano/iniciativa são **escopo da reescrita da `T27`**, e a `DP-F` não se reabre. As arestas são de **plano**, não de tarefa, e a `DP-F` foi ratificada como decisão de tarefa: reabri-la para acrescentar um vocabulário paralelo custaria uma ratificação a mais sem destravar nada, enquanto a `T27` já passa pelo mesmo texto. A decisão precede a edição, e agora precede | ready *(achado da `EXA-T23a`; 2ª ocorrência medida pela `EXA-T25`; decidido em 2026-08-13, execução na `T27`)* | `.claude/skills/diario-de-obras/SKILL.md` `## Status — residência única`; `docs/plans/P-0734-execucao-autonoma.md` `### DP-F` |
| TK-29 | `calcular_desdobramento(status, veredito, bloqueante, orcamento_estourado)` recebe `bloqueante` e **nunca o usa** no corpo (`.claude/tools/rdo.py:624-644`) — parâmetro morto na fronteira do `G-DEADCODE`. Medido no replanejamento da `EXA-T19` e **deliberadamente não corrigido lá**: aquele dossiê declara que a assinatura não muda, e mexer nela no meio do rewire do `close` misturaria duas mudanças. **Decidido em 2026-08-11 pela rodada da `DP-G`, por derivação:** o parâmetro **sai**, e com ele sai também o `status`. A `DP-F` fixou que o RDO nasce de **uma única transição** (`review` → `done`), então tarefa bloqueada ou reprovada nunca chega ao `close` e os ramos `bloqueado`/`reprovado` ficam inalcançáveis — ramo morto testado é o que o `G-DEADCODE` proíbe. A assinatura passa a `calcular_desdobramento(veredito, orcamento_estourado)`, com dois ramos e a precedência do estouro sobre o veredito. Recusada a leitura oposta (a dominância de dimensão bloqueante deveria estar no corpo): `DA-6` já garante que `bloqueante` ≠ `nenhuma` implica `veredito=reprovado`, de modo que a informação não se perde | done *(executado na `EXA-T19`, item (c) do dossiê: assinatura encolhida para `(veredito, orcamento_estourado)`, ramos `bloqueado`/`reprovado` removidos, `dead_code.py` exit 0)* | `docs/plans/P-0734-execucao-autonoma.md` `### T19`; `.claude/tools/rdo.py:624-644` |
| TK-31 | `docs/plans/P-0734-execucao-autonoma.md:678`, dentro do **dossiê da `T23a`** (tarefa já executada), instrui "Registrar que o `status` é escrito **exclusivamente pelo `scrum-master`**" — última ocorrência afirmativa do absoluto que a `DP-G` derrubou, e a única fora das quatro superfícies que a tabela do item 5 da `DP-G` mediu. Efeito prático nulo (o artefato que aquele dossiê governa, a residência única, já foi corrigido pela `EXA-T28`), mas o texto do dossiê ficou dessincronizado da decisão vigente. Não corrigido na `T28` por desenho: os invariantes daquela tarefa proíbem tocar superfície fora das quatro e reabrir tarefa, e reescrever dossiê de tarefa fechada para acompanhar decisão posterior invalida registro (`DP-G5`). Escopo: reconciliar. **Decidido pelo dono em 2026-08-11** (`§12` do plano): no desenvolvimento do framework o último entendimento é canônico e reescreve a orientação anterior que ele contradiz — dossiê de tarefa executada é orientação, não registro, e se concilia; o que narra o ocorrido (bullet de fechamento, RDO, telemetria, histórico) permanece intacto. **Executado na rodada de replanejamento da `DP-H` (2026-08-11):** o bullet do dossiê da `T23a` passou a enunciar a fronteira da `DP-G` — o `scrum-master` é o único que **materializa** o `status`, o executor é **autor** de `review` e `blocked` —, com a conciliação datada e apontada para a `DP-H`; o artefato que aquele dossiê governa já estava corrigido pela `T28`, e nenhum registro do ocorrido foi tocado | done *(fechado por conciliação na rodada da `DP-H`; achado da `EXA-T28`)* | `docs/plans/P-0734-execucao-autonoma.md` `### T23a` |
| TK-44 | O dossiê de evidência mecânica (`.claude/tools/review_evidence.py`) **não discrimina escopo** enquanto a iniciativa inteira está sem commit: na revisão da `EXA-T13` ele leu o alvo declarado `.claude/tools/` como caminho literal ("sem diferença coletável — arquivo ausente na árvore de trabalho") e listou como *tocados* os **59** arquivos de toda a árvore não commitada do `P-0734`, produzindo "59 arquivos fora dos alvos" sem relação com a tarefa julgada. A camada declarada **autoridade sobre escopo** fica sem poder discriminante, e o conjunto real de arquivos da tarefa teve de ser reconstruído pelo `reviewer` fora do dossiê. Escopo: decidir se a atribuição de diff a tarefa passa a se apoiar em outro recorte (commit por tarefa, marco por tarefa, ou diff contra um ponto de referência gravado no despacho) e se o alvo declarado como **diretório** vira caso tratado em vez de caminho literal | backlog *(achado de processo do laudo da `EXA-T13`, alvo doutrina/instrumento)* | `.claude/tools/review_evidence.py`; `docs/RDO/evidencia/P-0734-T13.md` |
| TK-32 | **Uso e teto: medida agregada ou porteiro de tarefa.** O teto por tarefa vem sendo cruzado com regularidade sem produzir a consequência que a doutrina prescreve — `EXA-T31` consumiu os 15 do teto exatamente no fechamento e deixou a verificação órfã (coberta pelo orquestrador na mesma rodada), `EXA-T19` fechou em 41 contra 40, e a série `UXROUND3` registrou 56/35, 61/40 e 112/50. **Enunciado do dono (2026-08-11):** a questão é de **conceito de framework**, não de desenvolvimento deste projeto; uso e teto são medidas de **agregado** e não de indivíduo — avaliadas tarefa a tarefa medem ruído; o portador entre tarefas é o card **"Lições aprendidas na tarefa"** (metainformação **da tarefa**, nunca do entregável), acumulando até o **fecho do plano**, onde os números são lidos em conjunto. **Hipótese a confrontar com a série, não premissa:** o uso atual desse controle é mais poluição do que valor ou economia efetiva. **Regime interino, com efeito imediato:** até a posição final o teto é **alarme, nunca bloqueio** — nenhuma tarefa para, é impedida ou fica incompleta por cruzar o número, e quem delega não escreve cláusula de parada dura por teto; a medição em `docs/telemetria.tsv` continua obrigatória, porque é a série que decide. Execução: `EXA-T34`, que fecha a `DP-L` e para para ratificação em lote com `DP-I` e `DP-J`; a materialização em `GOVERNANCA.md` §3 é card autorado depois do aceite. **Encaminhamento do dono, 2026-08-12:** a matéria de consumo se revê **inteira e em plano próprio**, aberto depois que o `P-0734` fechar — o desdobramento está registrado na tarefa de fechamento (`### T17`, item 4), e a hipótese a confrontar com a série é que tanto alarme de teto não paga o que custa, já que todo cruzamento acaba justificado. **A `EXA-T34` foi cancelada por absorção na mesma decisão** e nenhuma `DP-L` se forma no `P-0734`: formar a posição ali decidiria agora o que o plano seguinte revê por inteiro. O corpo daquele card permanece como material absorvido — o insumo do dono (§15), a medição obrigatória de três números e o conteúdo que a decisão precisa cobrir —, e é dele que o plano novo parte. Até lá, o regime interino continua em vigor | **decidido em parte** — a parte interina foi **absorvida pela `DP-Q` em 2026-08-13** e deixou de ser interina: teto numérico não governa fluxo em lugar nenhum do framework, e custo/consumo são informação de agregado, com residência do qualitativo no card "Lições aprendidas na tarefa" do laudo (materializado pelo bloco `EXA-T49`..`T52`). O restante da matéria segue para plano próprio (`T17` item 4), com a `EXA-T34` cancelada por absorção *(achado do fechamento da `EXA-T31`)* | `docs/plans/P-0734-execucao-autonoma.md` §15, `### T34` e `### T17`; `GOVERNANCA.md` §3 (tabela de tetos por classe) |
| TK-33 | Três referências órfãs em `.claude/skills/scrum-master/SKILL.md`, todas em superfície que **nem a `T21a` nem a `T21b` podiam tocar** — os passos 1, 7, 8 e 10 foram explicitamente fencados pelo *Cuidado* da `T21a` e não estão nos arquivos-alvo da `T21b`, e a `T21b` declara `A1`/`A2`/`A7` inalterados: (1) `:153`, o gatilho do **passo 8**, cita "passo 5 concluído (regras `A1`..`A5`)" quando `A5` deixou de existir e as regras avaliadas depois do passo 5 passaram a ser `A1`, `A2`, `A3a`, `A3b` e `A4` — deveria ler `A1`..`A4`; (2) o **passo 7** (*Leitura do veredito*) extrai só `veredito`, `bloqueante` e o caminho do laudo, e **não extrai a `recomendacao`** que `A6`, `A8`, `A9` e `B1` agora leem — o campo é lido pelas tabelas sem que nenhum passo o colha; (3) a proibição *"Não abre o RDO nem o laudo"* contradiz o passo 9 entregue pela `T21a` (que extrai o `pacote` de cinco campos do laudo) e as regras `A6`/`B1` (que extraem a recomendação) — a fronteira entre "não abrir o corpo" e "extrair o pacote" precisa ser enunciada em vez de proibida. Resíduo correlato, deliberadamente preservado: `A2` ainda diz "pacote ausente ou inválido (campo faltando, teto de campo estourado)", vocabulário da era do pacote, porque o dossiê da `T21b` fixa "`A1`, `A2` e `A7` não mudam" e a `T31` cobre o resíduo de `pacote` em outros três arquivos. Escopo: reconciliar os três pontos (mais a acepção de `pacote` em `A2`) numa passada só sobre os passos 7 e 8 e a seção `## Proibições`. **Item 3 decidido pela `DP-M` (ratificada pelo dono em 2026-08-11):** não há fronteira a enunciar — a proibição **sai sem substituta**, porque com `Observações` fora do gerador (`EXA-T38`) o laudo só tem campo fechado ou calculado e não sobra nada a extrapolar; os passos 7 e 9 leem o laudo por desenho. **Item 2 fechado por derivação na mesma decisão:** a `recomendação` é campo fechado do laudo e é de lá que o passo 7 a colhe — o retorno de duas linhas do `reviewer` não muda e nenhum campo novo é criado. **Itens 1, 2 e 3, mais o resíduo de `A2`, passam a ser cobertos pela `EXA-T39`**, numa única passada no arquivo | done *(fechado pela `EXA-T39` em 2026-08-12, os três itens mais o resíduo de `A2`: (1) o gatilho do passo 8 passou a ler `A1`..`A4`; (2) o passo 7 passou a colher a `recomendação` do laudo e sua saída virou a tripla `veredito`/`bloqueante`/`recomendação`, que o passo 8 recebe, sem nada acrescentado ao retorno de duas linhas do `reviewer`; (3) o bullet "Não abre o RDO nem o laudo" saiu de `## Proibições` sem fronteira substituta, por `DP-M`; mais `A2` reenunciada como "retorno ausente ou inválido", só o termo, condição e encaminhamento idênticos; achado da `EXA-T21b`)* | `.claude/skills/scrum-master/SKILL.md:153` (passo 8), `### Passo 7`, `## Proibições`; `docs/plans/P-0734-execucao-autonoma.md` §16.4 e `### T39`; `### T21a` (*Cuidado*) e `### T21b` |
| TK-34 | O dossiê de delegação não colava as **âncoras** do ponto a editar nem o **range do bullet de fechamento anterior**, e o executor pagava a localização em tool uses. Série medida no bloco da `DP-M`: `EXA-T37` fechou em ~19/15 e `EXA-T38` em 20/15, os dois excedentes atribuídos por causa medida a localizar a bateria de verificação e o ponto de inserção no diário — não a trabalho; a `EXA-T39`, delegada com âncoras re-derivadas e o range do bullet anterior colados, fechou em **13/15**, sem cruzar o teto. Recorrência de 3 rodadas consecutivas com a correção já provada na terceira | done *(decidido pelo dono e executado pelo orquestrador na mesma rodada, 2026-08-12: o dever entrou no item 3 do gate de delegação da skill `proximo-passo` e no passo 4 da skill `scrum-master`; `kit_check` `-Mode validate` e `-Mode check-drift` em exit 0)* | `.claude/skills/proximo-passo/SKILL.md` (gate de delegação, item 3); `.claude/skills/scrum-master/SKILL.md` (`### Passo 4`) |
| TK-35 | `.claude/agents/pantonic-executor.md:60` manda o executor "atualize o diário (`review`/`done`)" — o executor **materializa `done`**, e a `DP-G` fixou que ele é **autor** de `review` e `blocked` e de mais nada, cabendo a materialização em qualquer estado só ao `scrum-master`. Não é vocabulário (a `EXA-T24` traduziu o termo e parou aí, por invariante), é **conteúdo de regra**, e nenhuma tarefa viva o cobre: a `T26` alcança `GOVERNANCA.md`/rubrica/arquitetura e a `T27` alcança kanban e planos vivos. O que a execução precisa fechar junto: **quem escreve o bullet de fechamento do diário** quando o executor deixa de escrevê-lo — hoje ele o escreve inteiro, incluindo o marcador `— done`, e as rodadas recentes já dividiam o ato (executor escreve o bullet, orquestrador escreve índice, `Próxima tarefa` e telemetria) | done *(achado da `EXA-T24`; fechado pela `DP-N` e executado na `EXA-T40`, 2026-08-12)* | `docs/plans/P-0734-execucao-autonoma.md` §17 e `### T40` |
| TK-36 | **Reorganizar a passagem de bastão.** As skills `handover` e `proximo-passo` viram **uma única skill nova**, que executa a transição de tarefas suavemente — inclusive a passagem do contexto que precise ser herdado de tarefa predecessora — e que tenha coerência com as responsabilidades do `scrum-master` **sem exigir responsabilidade nova**; se responsabilidade nova se mostrar necessária, **escalar ao dono** em vez de criá-la. Aberto por decisão do dono em 2026-08-12, ao ratificar a `DP-N`: com o executor fora da escrita, a passagem de bastão é atividade crítica e merece tíquete próprio para destrinchar colaterais, em vez de ser consequência silenciosa. Superfícies medidas que **pertencem a este tíquete** e por isso ficam fora da `T41`: `README.md` §9 inteiro (*Handover e uma tarefa por contexto*), `GOVERNANCA.md:333`/`:338`/`:341`/`:342` (§4) e `:240` (cerimônias), o *enforcement* dos itens 8 e 9 do §7 ("gate de review no handover"), e o corpo das duas skills. Entre a `T41` e este tíquete a doutrina do handover descreve um encerramento que o executor não faz mais — contradição declarada, com dono e prazo. **Anotação incorporada em 2026-08-12** (decisão do dono, ao receber o achado de classe (c) da `EXA-T43`, `TK-37`): **quem escreve o checkpoint de contexto** entra no escopo desta unificação e **não se decide antes dela**. `.claude/skills/handover/SKILL.md:96-100` atribui à **Execução** escrever até 5 linhas nas *Notas de execução* do diário ao cruzar 2/3 do teto — ato real e necessário (`~/.claude/CLAUDE.md` Regra 2) que a matriz de responsabilidades não declara para esse papel e que o domínio fechado do sinal do executor (`review`, ou `blocked` com razão tipada) não carrega. Resolver a lacuna no documento atual não tem sentido: ele está na iminência de se tornar obsoleto. A skill nova declara o portador; se isso exigir responsabilidade nova, **escala ao dono**, como este tíquete já prescreve. **Natureza da skill fixada pelo dono em 2026-08-13** (`P-0734` §19, critério de aceitação final): a skill unificada é **maquinário estrito do `scrum-master`**, na superfície **agente↔agente**, e é **transparente para o gerente do projeto** — ele não a invoca, não a lê e não a acompanha. Ela prima por **eficiência e qualidade da transição**, incluindo a herança de contexto entre tarefa predecessora e sucessora, e **não é skill de comunicação com humano**; essa superfície é do `TK-38`, e os dois eixos não se misturam | ready *(decisão do dono ao ratificar a `DP-N`; anotação do `TK-37` incorporada em 2026-08-12; natureza fixada em 2026-08-13)* | `docs/plans/P-0734-execucao-autonoma.md` §17.3; `.claude/skills/handover/SKILL.md`; `.claude/skills/proximo-passo/SKILL.md` |
| TK-37 | **Lacuna da matriz — quem escreve o checkpoint de contexto.** `.claude/skills/handover/SKILL.md:96-100` atribui à **Execução** escrever até 5 linhas nas *Notas de execução* do diário quando o consumo cruza 2/3 do teto. O ato é **real e necessário** (`~/.claude/CLAUDE.md` Regra 2: cruzada a capacidade, grava-se checkpoint de ponteiro de estado antes do handover), mas a matriz de responsabilidades (`GOVERNANCA.md` §3) nega à Execução escrever no diário, e o domínio fechado do sinal do executor (`review`, ou `blocked` com razão tipada) **não carrega o conteúdo do checkpoint** — de modo que hoje o ato não tem portador declarado. Ocorrência de **classe (c)** da `EXA-T43`, não editada por prescrição do item 15 (`G-SCOPE`): criar a responsabilidade no prompt seria a própria violação, e a falta é **da matriz**. Decisão do dono, entre (i) a matriz declarar o portador — Execução ganha o ato, ou o checkpoint passa a caber na Orquestração, que já escreve no diário —, ou (ii) o sinal do executor ganhar um canal para o conteúdo do checkpoint. **Encaminhado pelo dono em 2026-08-12, sem decidir o mérito:** a lacuna **não se resolve aqui** — vira **anotação no `TK-36`**, a unificação de `handover` + `proximo-passo`, porque resolver uma questão para um documento na iminência de se tornar obsoleto não tem sentido. A skill nova é que declara o portador do checkpoint; se isso exigir responsabilidade que a matriz não tem, aquele tíquete escala ao dono, como já prescreve. Este tíquete permanece indexado como o **registro do achado** de classe (c), não como decisão aberta. **Segunda ocorrência da mesma lacuna, medida pela `EXA-T44`** (2026-08-12): `GOVERNANCA.md:340-344` é a **fonte na doutrina** do texto que a skill repete — atribui à Execução gravar o checkpoint intermediário ao cruzar 2/3 do teto —, registrada como `#46` do §2 do relatório e **não editada** pela mesma prescrição do item 15. Nenhum tíquete novo foi aberto: é a mesma lacuna em outra superfície, e essa superfície já está dentro do recorte do `TK-36`, que lista `GOVERNANCA.md:341`/`:342` entre as suas; as duas se resolvem no mesmo ato | **encaminhado** — anotado no `TK-36` *(achado de classe (c) da `EXA-T43`; encaminhamento do dono em 2026-08-12; 2ª ocorrência medida pela `EXA-T44`)* | `.claude/skills/handover/SKILL.md:96-100`; `GOVERNANCA.md` §3 (matriz), §7 item 15 e `:340-344`; `docs/audits/CONFORMIDADE_MATRIZ_2026-08-12.md` §1 (`#27`) e §2 (`#46`) |
| TK-38 | **Comunicação entre agente e humano — skill própria e requisitos mínimos.** Aberto por decisão do dono em 2026-08-13. O framework nomeia objetos de projeto por prefixo abreviado (`DP-`, `DR-`, `DE-`, `DI-`, `DH-`, `DA-`, `TK-`, `EXA-T<n>`, `G-*`) e os agentes carregam esses tokens **crus** para dentro da conversa com o humano, que não participou do ato que os criou. **Fato medido nesta mesma rodada:** o relatório de handover da `EXA-T25` citou `DP-F`, `DP-I`, `DP-J` e `DP-L` sem expandir nenhum, o dono precisou gastar **um prompt inteiro** perguntando onde essas descrições moravam, e a expansão que ele inferiu (*"Decisão Pendente"*) **está errada** — `README.md:172` define o prefixo como *decision record* (decisão já ratificada) e **não expande as letras `D` e `P` em lugar nenhum do repositório**, de modo que a sigla é ilegível a partir do artefato até para quem a usa. Agravante declarado pelo dono: o framework almeja público de **outros idiomas**, para quem uma abreviação em português nunca fará sentido. **Recorte:** a nomenclatura abreviada **permanece** nos artefatos (é compacta e greppável); o que muda é a **superfície de conversa** — toda ocorrência em texto dirigido ao humano vem acompanhada do significado inline, na forma `DP-7 (<expansão> #7)`. **Golden rule a trabalhar no tíquete, enunciada pelo dono:** *"toda comunicação que demandar que o humano leia um documento extra, ou crie um novo prompt, é comunicação ineficiente, e deve ser registrada como lição aprendida para melhoria da skill de comunicação"*. **Escopo a cobrir:** (a) skill de comunicação agente↔humano, com os requisitos mínimos do corpo da mensagem para acelerar a tomada de decisão; (b) proibição de exigir leitura de artefato extra ou prompt de esclarecimento como caminho normal — o token gasto em pergunta de esclarecimento é desperdício mensurável; (c) tabela de expansão dos prefixos e termos intrínsecos do framework, **incluindo o que `DP-` e os demais de fato significam**, hoje inexistente; (d) alcance multilíngue; (e) o registro das falhas de comunicação como lição aprendida, ligando ao portador de metainformação de tarefa da `TK-32`. Área de superfície ampla — atinge kit executável, doutrina e espelho, e por isso nasce como tíquete, não como correção de rodada. **Fronteira declarada contra o `TK-36`** (dono, 2026-08-13, `P-0734` §19): este tíquete governa **exclusivamente** a superfície **agente↔humano**; a unificação `handover` + `proximo-passo` é maquinário **agente↔agente**, transparente ao gerente, e **não** recebe requisito de comunicação humana — arrastá-lo para lá acrescentaria custo a toda iteração do loop autônomo. Os dois eixos não se misturam e nenhum planejamento derivado pode tratá-los como a mesma matéria | ready *(decisão do dono, 2026-08-13; evidência medida no handover da `EXA-T25`)* | `README.md:172` (glossário, entrada `DR-`/`DP-`); `.claude/skills/` (skill nova a autorar); `GOVERNANCA.md` §3.1 |
| TK-39 | **O critério de aceitação não pode ser contagem de acionamentos do gerente.** Aberto por decisão do dono em 2026-08-13, corrigindo o §19 do `P-0734` autorado no mesmo dia. **Enunciado do dono:** um valor numérico de vezes que o gerente é acionado durante a execução de um plano **não tem sentido prático** — ou é sem valor, ou, virando controle, é **arbitrário**, porque não existe forma de derivar esse limite de coisa alguma. A responsabilidade do gerente **sempre** será dirimir ambiguidades e resolver conflitos, sobretudo de **requisitos** e de **aceitação**, e é **risco fatal** o agente decidir aspecto de aceitação sem estar **inequivocamente** seguro de que é a melhor solução — de modo que ele não pode ser limitado num aspecto-chave do projeto por métrica arbitrária. **Critério que entra no lugar:** é entrega **ineficiente** quando o framework solicita acionamento do gerente em **caminho feliz ou caminho natural**, sem pendência e sem demanda que seja dele. Exemplo dado pelo dono: parar para que ele limpe o contexto e invoque a tarefa seguinte — o plano corre sem problema e ele está mediando **execução normal**, que é exatamente a ineficiência que o framework existe para eliminar. A aceitação passa a classificar cada acionamento **pela causa**, nunca pelo número: causa que é do gerente é legítima e ilimitada; caminho feliz é defeito. Superfície: artefatos do framework (doutrina em `GOVERNANCA.md` §4.3, a skill que conduz o loop) mais o §19, a `T16` e a `T17` do `P-0734` | done *(decisão do dono, 2026-08-13; quitado pela `EXA-T45`, card prioritário à frente da `T29`)* | `docs/plans/P-0734-execucao-autonoma.md` `### T45` e §19; `GOVERNANCA.md` §4.3 (`:312-346`) e §3.1 (`:201`); `.claude/skills/scrum-master/SKILL.md` |
| TK-40 | **A tabela de riscos do `P-0734` ainda promete a medida que a `T16` deixou de fazer.** Achado fora de escopo da `EXA-T45`, indexado pelo orquestrador. A mitigação do risco *"o dono perder consciência situacional ao sumir o round-trip por tarefa"* (§6, `:2000`) diz que *"a `T16` mede quantos round-trips de fato desapareceram — se o custo for cegueira, o piloto mostra"*. É **mitigação viva**, não registro histórico: descreve o que uma tarefa ainda não executada vai fazer. Com a `T16` reescrita para **registrar cada acionamento pela causa**, sem contagem, a linha promete um instrumento que não existe mais, e o risco fica sem mitigação verificável. A `EXA-T45` não a corrigiu porque o dossiê declarou a tabela de riscos do §6 **fora do alvo, como história** — recorte correto para as ocorrências que narram ratificações já ocorridas, e errado para esta. **Escopo:** reescrever a mitigação para se apoiar no registro qualitativo por ocorrência (o RDO continua sendo o instrumento compensatório de `DA-5`), sem reintroduzir contagem. Edição de uma linha, sem decisão pendente | done *(achado medido na `EXA-T45`; quitado como ocorrência de classe (b) dentro da `EXA-T47`, 2026-08-13)* | `docs/plans/P-0734-execucao-autonoma.md` §6 e `### T16` |
| TK-41 | **A `DP-B` prescreve paradas que o §19 pode classificar como acionamento em caminho feliz.** Duas ocorrências de classe (c) medidas pela `EXA-T47` na consolidação do plano; nenhum dos textos envolvidos foi tocado, conforme o `G-EXECREADY`. **Decisão do dono, owner-gated.** A `DP-B` (política de autonomia, tetos e escalada, ratificada em 2026-08-08) manda o loop **parar** em duas situações, e o §19 (critério de aceitação, enunciado em 2026-08-13) diz que acionamento do gerente em caminho feliz ou natural é ineficiência da entrega, bastando **uma** ocorrência. **(1) Estouro de teto (`A4` × invariante 5 do §3 × §19):** a `A4` manda PARAR para replanejamento em todo estouro, o regime interino do §3 item 5 diz que teto é **alarme, nunca bloqueio**, e o §19 reprova parada de caminho feliz. Leitura 1 — a `A4` governa o loop depois da entrega e o invariante 5 só protege o executor, de modo que as duas convivem; leitura 2 — a `A4` é parada de caminho natural e o regime interino a esvaziou. Agrava que a matéria de uso e teto está desdobrada para plano próprio (`T17` item 4; a `DP-L` não se forma neste plano). **(2) Fim de janela (`B2` × §19):** a `B2` encerra a janela por teto e PARA, chamando isso de "encerramento normal", enquanto o §19 diz que o dono **inicia o plano e nada mais** e que a skill **cria os contextos novos** sozinha — sendo o dono invocar a continuação o caso exemplar de ineficiência. **Por que é do dono:** é conflito entre dois enunciados dele, sobre requisito e sobre aceitação, e a escolha muda o que a `T16` mede e o que a `T17` aprova. **Bloqueia `T16` e `T17`; não bloqueia `T29`/`T30`** (matéria disjunta) | done *(decidido pelo dono em 2026-08-13 — os dois itens pelo mesmo princípio: teto arbitrário não governa fluxo; materializado pela `DP-Q` (§21) e pelo bloco `EXA-T49`..`T52`)* | `docs/audits/CONSOLIDACAO_SUPERFICIE_2026-08-13.md` (classe (c), `c1`/`c2`); `docs/plans/P-0734-execucao-autonoma.md` `### DP-B`, §3 item 5 e §19; `.claude/skills/scrum-master/SKILL.md` (`A4`, `B2`) |
| TK-42 | **Resíduo de entendimento derrubado fora dos universos declarados da `DP-P`.** Dois achados da `EXA-T48`, ambos de forma classe (b) mas em artefatos que o dossiê não declarou no universo. **(1)** `tests/test_review_evidence.py`, docstring de `test_escopo_violado_gera_fato_sem_inventar_parcial`, ainda cita *"pacote de retorno"* — objeto morto desde a `DP-H`; a `T48` corrigiu as três menções vivas em `.claude/tools/review_evidence.py`, e o teste ficou de fora porque `tests/` não estava no universo. **(2)** `.claude/README.md`, nota dos auditores: *"apontamentos aceitos viram tíquetes no diário via `pantonic-planner`"* — resíduo do **eixo da matriz de responsabilidades**, não do eixo dos objetivos: a rodada de 2026-08-12 (`T43`/`T44`) corrigiu os arquivos de agente e o índice do kit ficou para trás. Edição textual nos dois casos, sem mudança de comportamento e sem decisão pendente | ready *(achados medidos na `EXA-T48`, 2026-08-13)* | `tests/test_review_evidence.py`; `.claude/README.md` (nota dos auditores) |
| TK-43 | **O hub distribui um kit cuja configuração de hook é ignorada pelo git.** `.claude/settings.json` está em `.gitignore:3`, sob o comentário "Configuração local de máquina — nunca canônica". A `EXA-T13` registrou ali o hook do proxy de ocupação porque o dossiê `### T13` nomeia esse arquivo como alvo, e o instrumento funciona na máquina do dono — mas nada dele viaja para consumidor nenhum, e `kit_check` não o vê. A `EXA-T14` (telemetria sem turno de agente) tem o mesmo alvo e herda o mesmo defeito. **Decisão do dono, owner-gated:** é arquitetura de distribuição do kit, não execução — ou hook canônico ganha residência versionada própria, com materialização no `settings.json` local, ou o proxy de ocupação é assumido como instrumento só-do-hub, e nesse caso a condição de capacidade do §4.3 não existe para consumidor. **Bloqueia `T14`; não bloqueia o laudo da `T13` nem `T29`/`T30`**. **Decidido pelo dono em 2026-08-15:** hook canônico **ganha residência versionada própria**, com materialização no `settings.json` local. O `GOVERNANCA.md` §4.3 afirma a capacidade como condição vinculante para todo Pantonic\*, não só para o hub: assumir o proxy como instrumento só-do-hub transformaria regra publicada em regra sem meio de cumprimento nos consumidores — o apodrecimento que a §7.1 existe para impedir. Recusada a alternativa (proxy só-do-hub) por esse motivo. **Replanejamento concluído em 2026-08-15, na `DP-R` (§22 do plano):** os três pontos que estavam em aberto ficaram fechados sem decisão nova de arquitetura — residência em `.claude/hooks/hooks.json` (comando portável por `{KIT_ROOT}`), materialização por `.claude/tools/hooks_sync.py apply`, idempotente e preservando `permissions.deny` e todo hook não-kit, e `kit_check` cobrando o canônico no `-Mode validate` e a materialização no `-Mode check-drift`. Execução atribuída a **`EXA-T53`** (residência, materializador, testes e guarda) e **`EXA-T54`** (a superfície publicada: `.gitignore`, `GOVERNANCA.md` §3.1, `README.md` §11 e §13, `CHANGELOG.md`), em bloco à frente da `T29`. A `T14` deixa de estar bloqueada por dossiê: o dela foi reescrito na mesma rodada e agora depende da `T53`. **Absorvido pelo `P-0735` em 2026-08-15**, junto da regra geral de que é sub-caso: `EXA-T53` e `EXA-T54` ficam **canceladas por absorção**, o desenho da `T53` sobrevive integral nas `RPC-T2`/`RPC-T3` (manifesto único, materializador `apply`/`check`/`drift`, preservação de `permissions.deny` e de hook não-kit, ancoragem hub × consumidor, guarda no `kit_check`) e só a residência particular `.claude/hooks/hooks.json` desaparece — declaração única em `.claude/projecoes.json`, porque duas declarações lado a lado seriam a duplicata que a régua proíbe. Os hooks globais, que a `T53` não alcançava, entram na `RPC-T5`; a dependência da `T14` passa para a `RPC-T2` | done *(decidido pelo dono em 2026-08-15; absorvido no mesmo dia pelo `P-0735`; fechado pelo `P-0735` — execução em `RPC-T2`/`RPC-T3`/`RPC-T5`)* | `.gitignore:3`; `.claude/settings.json`; `docs/plans/P-0734-execucao-autonoma.md` `### T53`, `### T54`, `### T14`, §22 (`DP-R`) |
| TK-45 | **Ambiguidade estrutural de residência: o framework depende de artefatos que não viajam nele.** 5ª ocorrência medida da mesma classe (`TK-01` skill `modelo-por-fase` apontada para o global; `DR-B` de `docs/RESIDENCIA_DOUTRINA.md` §5, que adiou a promoção de 6 skills globais como "iniciativa própria" nunca aberta; `TK-21` ratchet sem alvo em 0/6 consumidores; `TK-43` hook ignorado pelo git; `permissions.deny` do guardrail 13, escalado em `DP-R` §22.5). **Medido em 2026-08-15:** vivem fora do pacote, em `~/.claude/`, 4 hooks registrados no `settings.json` global (`pytest_pretooluse`, `verbose_cmd_pretooluse`, `read_cap_pretooluse`, `modelo_por_fase_userpromptsubmit`), 6 skills (`context-prep`, `doc-map`, `lean-test`, `memory-diet`, `onboard`, `test-tiers`), 1 agente (`context-scout`) e 2 docs de doutrina (`GOVERNANCA_MEMORIAS.md`, `RECOMENDACOES_CONSUMO_GLOBAL.md`) — nenhum chega a consumidor algum, e a doutrina versionada os invoca (a skill `proximo-passo` do kit cita `context-prep`/`context-scout`; o hook global é o enforcement do §3). **Raiz:** o teste de residência (`GOVERNANCA.md` §3.1) responde *onde mora* com uma resposta só, fundindo dois eixos independentes — **autoridade** (conteúdo do framework × da máquina do dono) e **ponto de carga** (onde o harness lê). Quando o ponto de carga imposto pelo harness é global ou não-versionado, a régua obriga a escolher entre residência correta e funcionamento, e o §3.1 registra o sintoma como se fosse lei ("hook não é quinta superfície (...) e não viaja"). Pelo próprio `Prec-2` ("regra que só existe no `~/.claude` do dono não é doutrina do framework"), os 13 artefatos acima não são doutrina — e a doutrina depende deles: contradição medida, e a causa direta de comportamento inconsistente entre projetos. **Decisão do dono, owner-gated:** alcance do pacote (o kit passa a materializar também o global, ou para na fronteira do projeto). Bloqueia `EXA-T53`/`EXA-T54`, que resolvem o sub-caso do hook. **Decidido pelo dono em 2026-08-15:** o pacote passa a materializar também o `~/.claude` — CLAUDE.md global e skills/agentes globais viram projeção de canônico versionado, com residência e ponto de carga separados e a materialização projetando uma na outra. **Executado no mesmo dia, na rodada de doutrina:** `GOVERNANCA.md` §3.1 reescrito para as três classes, a pergunta zero e o `Prec-2` como invariante (a afirmação de que hook não viaja saiu), e `docs/RESIDENCIA_DOUTRINA.md` ganhou a §8 de conciliação datada, que reclassifica o que a régua nova muda sem reescrever a classificação de 2026-08-03. **Execução do mecanismo atribuída ao `P-0735`** (`RPC-T1..T9`) | done *(decidido pelo dono em 2026-08-15; doutrina publicada no mesmo dia; mecanismo executado e fechado pelo `P-0735`)* | `GOVERNANCA.md` §3.1; `docs/RESIDENCIA_DOUTRINA.md` §8; `docs/plans/P-0735-residencia-e-ponto-de-carga.md` |
| TK-46 | `README.md:352-354` (§7, modelo por fase) afirma que *"o hook de aviso fica fora do kit, por ser mecanismo de enforcement de uma regra que já mora na doutrina versionada"* — contradiz `GOVERNANCA.md` §3.1, onde a **declaração do hook é canônica e versionada** e só o arquivo de configuração que o harness lê é ponto de carga. Mesma classe das 7 edições da `RPC-T1`, mas fora dos alvos daquele dossiê. Verificar se a varredura fechada da `RPC-T7` (item 4) alcança a frase: o Grep dela é por `~/\.claude` e esta frase não cita o caminho, então provavelmente **não** — nesse caso a correção entra como alvo explícito da `T7` | backlog *(achado da `RPC-T1`)* | `README.md:352-354`; `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T7` |
| TK-47 | `materializar.py apply --alvo usuario` **reescreve o `settings.json` do destino mesmo quando não há drift semântico**: o primeiro `apply` real da `RPC-T4` mudou o mtime de `~/.claude/settings.json` por normalização de serialização JSON (indentação/ordem de chaves reemitidas pelo dump), com todo o conteúdo preservado (`model`, `effortLevel`, `switchModelsOnFlag`, `statusLine`, `permissions.allow`, `additionalDirectories` intactos). Comportamento pré-existente do materializador entregue na `RPC-T2`, não introduzido pela `T4`. **Por que importa agora:** o critério de verificação da `RPC-T5` exige que o `settings.json` resultante difira do anterior **apenas** no caminho dos comandos resolvido pelo placeholder, e manda a tarefa parar em qualquer outra diferença — com a normalização em vigor, a `T5` para por um efeito que não é do escopo dela. Decidir se `apply` passa a ser byte-idempotente quando não há mudança semântica (preservar a formatação existente) ou se a normalização é aceita e o critério da `T5` é reescrito para comparar semanticamente | done *(achado da `RPC-T4`; decidido pelo dono em 2026-08-17 — `apply` byte-idempotente sob equivalência semântica; quitado pela `RPC-T10` no mesmo dia: comparação semântica em `write_settings`, 2 testes novos, suíte 65 → 67)* | `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `DL-10` e `### T10`; `.claude/tools/materializar.py:220-231` |
| TK-48 | `~/.claude/settings.json` **perdeu a chave `hooks` inteira silenciosamente**, sem ação intencional do dono, entre a `RPC-T4` e a escolha da `RPC-T5` — os 4 hooks registrados (premissa da `T5`) somem sem rastro. Causa não investigada por decisão do dono (foco em proteção, não em achar culpado); a `T5` não depende do estado atual do arquivo (reconstrói o registro pela tabela já transcrita no dossiê) e segue delegável. Vulnerabilidade a considerar: `settings.json` global pode perder chave inteira sem sinal | blocked *(owner-gated: decisão do dono sobre investigar causa/mitigar a perda silenciosa)* | `docs/plans/P-0735-residencia-e-ponto-de-carga.md` seção "Achados da execução" (2026-08-17) |
| TK-49 | **O hook do alvo `projeto` é materializado com caminho relativo e derruba a sessão inteira.** `.claude/projecoes.json` declara `python {KIT_ROOT}/tools/ocupacao.py` e o materializador resolve `{KIT_ROOT}` para o caminho **relativo** `.claude`, de modo que o `settings.json` do projeto registra `python .claude/tools/ocupacao.py`. Basta o cwd de uma chamada de ferramenta sair da raiz do repositório para o hook falhar — e hook `PreToolUse` que falha **bloqueia toda ferramenta da sessão** (Bash, PowerShell, Glob, Read, ToolSearch), inclusive a chamada que restauraria o cwd: sessão irrecuperável, só sai abrindo outra. Medido ao vivo em 2026-08-17, durante a verificação da `RPC-T5`. O mesmo campo minado viaja para todo consumidor que materializar o alvo `projeto`. **Decidido pelo dono em 2026-08-17:** corrigir na origem — `{KIT_ROOT}` resolve para caminho absoluto na escrita do `settings.json`, com TF em fixture `tmp_path`; recusada a alternativa de tratar como limitação operacional ("não mude o cwd"), que deixaria o defeito nascer propagado nos consumidores. **Dossiê autorado fechado em 2026-08-17** como `RPC-T11` do `P-0735`, logo depois da `T5`: `kit_root_placeholder` passa a devolver `kit_root.as_posix()`, a classificação de entrada de kit (`is_kit_command`) migra para um marcador relativo próprio — sem isso o `apply` preservaria a entrada relativa já instalada ao lado da nova, deixando o hook defeituoso vivo —, e a premissa foi verificada no ato: `.claude/settings.json` é gitignorado (`.gitignore:3`), então a portabilidade que o desenho original perseguia não tinha objeto | done *(fechado pela `RPC-T11` em 2026-08-18: `{KIT_ROOT}` grava caminho absoluto, TR de substituição da entrada relativa antiga, `apply`/`drift` reais em exit 0)* | `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T11` |

---

## P-0733 — Quitação da dívida de doutrina e de kit do hub

**Objetivo:** quitar os doze tíquetes que sobraram no índice quando a iniciativa anterior encerrou,
agrupados por dívida: doutrina decidida e não executada, resíduo de vocabulário do kit, e guarda e
navegação desalinhadas do que guardam. Fecha na revisão final do espelho, que era o único tíquete
postergado por decisão, e no aceite do dono sobre o `README.md`.

**Plano:** `docs/plans/P-0733-divida-do-hub.md` — 13 tarefas (`DHB-T1..T13`), ordem linear sem ramo
condicional, decisões `DH-1..DH-7` fechadas no ato do planejamento. Nenhuma questão owner-gated
pendente: `TK-07` e `TK-08` foram levadas ao dono e decididas antes da publicação.

**Tíquetes cobertos:** `TK-04`, `TK-06`, `TK-07`, `TK-08`, `TK-10`, `TK-12`, `TK-15`, `TK-17`,
`TK-18`, `TK-20`, `TK-21`, `TK-22`. Cada um fecha na tarefa que o executa; o `TK-08` fecha como
recusa registrada (não vira conceito normativo) e o `TK-18` deixa de ser `blocked` por posição na
ordem — ele é a penúltima tarefa, quando as fontes já pararam de mudar.

**Próxima tarefa:** **`DHB-T2`** — segunda rodada da porta de saída de guardrails (`DE-8`): percorrer
os 14 guardrails da lista do §7 pelo procedimento da §7.1, registrando cada resultado (marcado,
retido com caso citável, ou removido) no bloco *Registro das rodadas* com o rótulo `P-0732`. Alvos:
`GOVERNANCA.md` §7.1, `docs/DIARIO_DE_OBRAS.md`. Proibido remover guardrail sem o procedimento
completo ou contar a rodada por calendário. Verificação: bateria do §3, entrada da rodada com
resultado item a item. Dossiê em `docs/plans/P-0733-divida-do-hub.md` `### T2`.

---

## P-0734 — Execução autônoma

**Objetivo:** a execução do backlog deixa de custar um round-trip humano por tarefa atômica e passa
a ser um loop conduzido pelo próprio agente — papel de orquestração (skill `scrum-master`), papel de
revisão (agente `pantonic-reviewer`) e documental gerado por função, com o registro canônico da
tarefa migrando do diário para `docs/RDO/`.

**Plano:** `docs/plans/P-0734-execucao-autonoma.md` — **31 tarefas atômicas** (`EXA-T1..T27`, com
`T6`/`T8`/`T9` partidas em `a`/`b`/`c` por orçamento), ordem linear, decisões `DA-1..DA-10` fechadas
no ato; três desenhos postergados viram as tarefas `T2`, `T3` e `T4`. Cinco decision records
ratificados: `DP-A`..`DP-C` (2026-08-08), `DP-D` (2026-08-10, reconciliação do fluxo) e **`DP-E`
(2026-08-11, §10 — o `status` é da tarefa, não do laudo)**, que encomenda `T22`..`T27` e deixa
`T19`/`T20`/`T21` pendentes de reescrita. Alcance: hub primeiro, medir, depois propagar.

- **`EXA-T1` — spike de plataforma — `done`.** Entregável em
  `docs/audits/SPIKE_HARNESS_EXECUCAO_AUTONOMA.md`, quatro sondas com evidência colada.
  **Sonda 1 (aninhamento de subagentes): `derrubada`** — aninhamento funciona, observado até
  profundidade 3 (contexto principal → `pantonic-executor` → `general-purpose` → `context-scout`).
  **Sonda 2 (`model` da chamada vence o `model:` do arquivo do agente): `confirmada`** — arquivo do
  `pantonic-scout` fixa `haiku`, chamada passou `opus`, system prompt do subagente declarou
  `claude-opus-5`; a `DA-8` é implementável. **Sonda 3 (observabilidade de contexto): `parcial`** —
  o payload de `PreToolUse` expõe `transcript_path`, então o proxy por hook é viável; nenhum bloco
  de uso de tokens vem pronto no payload, e a variante do contador calibrado por telemetria não foi
  medida (`TK-23`). **Sonda 4 (arquivo escrito por um subagente, lido por outro): `confirmada`** —
  cenário original produzido, o transporte por arquivo da `T2` tem base.
  Executada em duas rodadas: a primeira mediu a Sonda 1 contra `context-scout`, um agente cujo
  toolset declarado não inclui `Agent`, e o resultado media a definição daquele agente em vez de um
  limite de plataforma — defeito do dossiê de delegação, não da execução. A rodada corretiva
  re-mediu as Sondas 1 e 4 e deixou nota de correção no topo do documento. Orçamento estourado por
  isso: 26 tool uses contra teto de 20 (19 + 7).
  Consumo: ver `docs/telemetria.tsv`.

**Reexame da `DA-1` — resolvido em 2026-08-08.** A `EXA-T1` derrubou a premissa em que a decisão se
apoiava (subagente não invocaria subagente). O dono reexaminou e **manteve o scrum-master como
skill no contexto principal**, com o argumento trocado de impossibilidade técnica para controle: o
loop autônomo precisa de um ponto onde o dono interrompe sem derrubar a sessão, e profundidade 3
observada numa única tentativa não sustenta mudar a arquitetura do orquestrador. Registrado no
`DA-1` e no §2 do plano; a `T2` está desbloqueada.

- **`EXA-T2` — decisão do transporte do pacote de retorno — `done`.** `DP-A` fechada como
  **transporte por arquivo** e ratificada pelo dono no ato: o executor grava o pacote no RDO e
  devolve 1 linha de confirmação; o reviewer lê o arquivo e devolve 2 linhas de veredito; o
  orquestrador nunca ingere o corpo. Medição que sustenta (29 handovers da série `V2E-*`/`V2P-*`):
  mediana 2 839 chars, p90 3 926, máximo 5 345 ⇒ ~1,6k tokens/tarefa sob (a) contra ~3,4k sob (b),
  que entra duas vezes no contexto — ~90 tarefas por janela contra ~38. Argumento decisivo além do
  número: a `DA-5` já obriga a escrita do RDO, então (b) soma uma cópia em vez de substituir.
  Entregável em `docs/plans/P-0734-execucao-autonoma.md` `## Dossiês fechados por decisão`: decision
  record, campos fixos do pacote (8 campos, teto total 44 linhas, teto por campo no template de
  `rdo.py`) e gramática fixa das 3 linhas de contexto. Dossiês dependentes: **`T10` fechado**
  integralmente; **`T8`** fecha a parte da `DP-A` e segue não delegável até `T4` e `T5`; **`T11`**
  idem até `T3`. Executada inline pelo orquestrador (decisão + ratificação não são delegáveis).
  Verificação: `kit_check -Mode validate` / `-Mode check-drift` / `check-readme.ps1` / `python -m
  pytest` — exit 0, 0, 0, 0 (`3 passed in 0.24s`). Nenhum achado fora de escopo.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T3` — decisão da política de autonomia, tetos e escalada — `done`.** `DP-B` fechada e
  ratificada pelo dono no ato: **1 retentativa** por tarefa reprovada, **10 tarefas** e **900 k
  tokens** por janela autônoma. Medição que sustenta (série de 99 tarefas em `docs/telemetria.tsv`):
  mediana 85 k tokens e 29 tool uses por tarefa, p90 159 k/52, cadência real de 10-20 tarefas por dia
  ⇒ 10 × mediana = 850 k, e o teto de consumo morde primeiro quando a janela pega tarefas mais
  pesadas que a mediana; 4 das 99 tarefas precisaram de 2ª rodada e a única que passou disso
  (`V2E-T9`) foi resolvida reescrevendo o dossiê, não repetindo a execução. Entregável em
  `docs/plans/P-0734-execucao-autonoma.md` `## Dossiês fechados por decisão`: decision record,
  domínio de saída do laudo (`veredito` ∈ {`aprovado`, `ressalva`, `reprovado`} + `bloqueante`) e
  **tabela de roteamento por precedência** — bloco A (`A1`..`A9`, o que fazer com a tarefa) e bloco B
  (`B1`..`B4`, continuar ou encerrar a janela), total sobre o produto cartesiano do domínio e sem
  nenhuma célula que peça juízo do orquestrador. Dossiês dependentes: **`T11` fechado** (não tem mais
  dossiê aberto, só precedência de ordem); adendo na `T10` com o domínio do veredito; restrição
  herdada na `T5` (a rubrica produz valores do domínio, não o amplia). Executada inline pelo
  orquestrador (decisão + ratificação não são delegáveis). Achado registrado no §"Achados da
  execução": o corpo do plano manda a `T3` fechar o dossiê da `T10`, mas a `T2` já a fechara — a
  dependência real era a `T11`. Verificação: `kit_check -Mode validate` / `-Mode check-drift` /
  `check-readme.ps1` / `python -m pytest`.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T4` — decisão do formato estruturado da tarefa no plano — `done`.** `DP-C` fechada como
  **convenção de linhas rotuladas extraída por expressão regular** (opção `b`) — ratificada, não
  inventada: a tarefa segue prosa no próprio `.md`, com gramática fixa de cabeçalho e conjunto fechado
  de valores para `classe` e `modelo`. Medição que sustenta (15 planos, 129 tarefas): **119/129 (92%)**
  dos cabeçalhos já casam a gramática, `Objetivo` e `Pronto quando` em 90%, `Arquivos-alvo` em 81%,
  `Verificação` em 72% — mas **130 rótulos distintos** depois de normalizados e duas grafias da mesma
  classe dentro de um único plano. Custo de migração zero, porque o esquema foi extraído do corpus, e
  resistência à deriva estrutural, porque não há dois lados para divergir (a mesma régua da `DP-A`).
  Entregável em `docs/plans/P-0734-execucao-autonoma.md` `## Dossiês fechados por decisão`: decision
  record, gramática de cabeçalho (`ID`, `modelo`, 5 slugs de `classe` mapeados 1:1 à tabela de tetos
  de `GOVERNANCA.md` §3, `teto` autossuficiente e travado no default da classe), gramática de campo
  com normalização de rótulo, esquema de 5 campos + `extras` livres, política de plano legado (leitura
  tolerante, autoria estrita) e instrução de autoria para a `T15`. Dois achados de desenho vindos da
  medição: a **alternância `Arquivos-alvo` × `Entregável`** (sem ela a fidelidade de escopo do laudo
  não tem âncora em tarefa de decisão) e a promoção de **`Dossiê fechado por` a campo reservado**, que
  torna mecânica a regra `B3` da `DP-B`. Dossiês dependentes: **`T8`** fecha a parte da `DP-C` e passa
  a depender só da `T5`; adendos na `T11` e insumo para a `T15`. Executada inline pelo orquestrador
  (decisão não é delegável; a `T4` é a única das três sem exigência de ratificação no dossiê).
  Achados no §"Achados da execução": `TK-24` (12 tarefas não iniciadas do `P-0733` fora do esquema) e
  a deriva de grafia de classe neste próprio plano. Verificação: `kit_check -Mode validate` /
  `-Mode check-drift` / `check-readme.ps1` / `python -m pytest` — exit 0, 0, 0, 0 (`3 passed in
  0.48s`); e o esquema aplicado à mão a `T5`/`T7`/`T9` extraiu cabeçalho e campos sem ambiguidade, com
  os quatro obrigatórios presentes e a alternância satisfeita nas três. **Estouro de teto: 34 tool
  uses contra 30 da classe `redacao`** — a varredura de 15 planos/129 tarefas (insumo medido exigido
  pelo dossiê) custou 6 chamadas de medição que uma tarefa de redação típica não tem; não é
  decomposição errada, é insumo de medição embutido numa classe de redação.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T5` — rubrica do laudo — `done`.** Entregável em `docs/RUBRICA_DE_REVISAO.md` (259 linhas,
  documento publicado): **sete dimensões** discretas (`criterio-de-pronto`, `escopo`, `testes`,
  `guardas`, `rota`, `residuo`, `registro`) — as de partida do dossiê, confirmadas, com os cinco
  campos exigidos (nome, pergunta, fonte da evidência, bloqueante, os quatro níveis). Pesos
  3/2/3/3/2/2/2 (total **17**, denominador mínimo **10**); `conforme`=1, `parcial`=0,5, `não
  conforme`=0, `não se aplica` fora de numerador **e** denominador; percentual = 100 × Σpeso×valor /
  Σpeso, metade para cima. Faixas: ≥95 `aprovado`, 70..94 `ressalva`, <70 `reprovado`. Cinco
  dimensões bloqueantes (`residuo` e `registro` não): `não conforme` em bloqueante ⇒ `reprovado` +
  `bloqueante` = a primeira em ordem canônica, qualquer que seja o percentual — `aprovado` com
  bloqueante preenchida é inalcançável por construção. Domínio de saída não ampliado. `DA-7`
  materializada na coluna de fonte: mecânica / juízo / mista, com trava explícita (vermelho mecânico
  proíbe `conforme` e o gerador recusa a marcação). **Via para achado de processo** com três alvos
  (`dossiê`, `doutrina`, `rubrica`) e três invariantes — achado de processo nunca rebaixa dimensão
  de entrega, exige rota, e defeito de dossiê que impede verificação marca `parcial` (nunca
  `conforme`); achado que invalida a rota sobe ao dono pela pendência do pacote. Propriedade
  derivada dos pesos: `aprovado` ⟺ todas as aplicáveis `conforme` (menor peso 2 sobre denominador
  máximo 17 ⇒ um `parcial` já custa 5,9 pontos). Verificação: bateria do §3, os quatro em exit 0 —
  `kit_check.ps1 -Mode validate` (0), `-Mode check-drift` (0), `check-readme.ps1` (0),
  `python -m pytest` (0); varredura da `redacao-doc` §6 com 1 correção V9 aplicada. Aplicação a mão
  a três tarefas fechadas do `P-0732` (`V2P-T3`, `V2P-T7`, `V2P-T9`): as três com `testes` e
  `residuo` em `não se aplica`, denominador 12, numerador 12 ⇒ **100%, `aprovado`,
  `bloqueante=nenhuma`** — coerente com o `done` sem ressalva que o histórico registra para as três.
  A aplicação corrigiu a dimensão `escopo`: o nível `conforme` passou a admitir o artefato cuja
  atualização a doutrina torna obrigatória como consequência mecânica da mudança nos alvos (caso do
  `DOC_MAP.md` na `V2P-T3`), que na formulação anterior cairia em `parcial` e rebaixaria a tarefa a
  `ressalva` contra o registro. Sem achado fora de escopo; nenhum arquivo da lista de fora de escopo
  tocado. Tarefa de redação de doutrina, sem TF/TR de código.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T6a` — doutrina de papéis e fronteira de registro — `done`.** Entregável em
  `GOVERNANCA.md`, duas regiões, sem nenhum outro arquivo tocado. **§3, matriz de
  responsabilidades:** de 5 para **7 linhas**, com `Orquestração` entre `Planejamento` e `Execução` e
  `Revisão` entre `Execução` e `Coleta` — a ordem da tabela passa a ser a do fluxo de uma tarefa.
  `Orquestração` responde por conduzir um plano (despachar com dossiê fechado, rotear o pacote de
  retorno nos três desfechos, registrar a telemetria medida, arquivar) e não implementa, não julga
  entrega nem decide arquitetura; `Revisão` julga **uma** entrega contra o dossiê dela e emite o
  laudo, com a escrita restrita ao caminho do laudo, e não corrige, não replaneja e não fecha tarefa.
  Coluna *Modelo* preenchida nas duas com Sonnet — **derivado, não decidido**: para a orquestração,
  `DA-8` (a célula transcreve a parada para pedir `/model`, já que o loop mora no contexto principal);
  para a revisão, paridade com `Auditoria`, o papel análogo que julga sem editar. **§4.2:** a `DA-5`
  entra como bullet novo "Fronteira de registro — três artefatos, nenhum repetindo o outro" (diário =
  kanban; RDO = registro canônico da tarefa, um arquivo por tarefa; `telemetria.tsv` = fonte única do
  número), e o bullet `Fechamento enxuto` perde a cláusula que fazia do diário o registro canônico,
  apontando agora para o RDO. Verificação: bateria do §3, os quatro em exit 0 — `kit_check.ps1 -Mode
  validate` (0), `-Mode check-drift` (0), `check-readme.ps1` (0), `python -m pytest` (0);
  `registro canônico` segue com 1 ocorrência e agora nomeia o RDO; `RDO` vai de 0 para 4 ocorrências,
  todas em §4.2; varredura da `redacao-doc` §6 sobre as regiões editadas sem achado (V3/V7/V10 zerados
  no texto novo — sem ID de processo, sem data, terceira pessoa; as negações que ficaram enunciam
  proibição, na coluna *Não faz*). Nenhum item novo em §7 (`DA-10` intacta), nenhuma menção a
  repositório derivado (`DA-3`), nada da `T6b` antecipado. O ramo condicional do dossiê foi resolvido
  pelo orquestrador antes do despacho: `docs/RESIDENCIA_DOUTRINA.md` fica fora (documento de tarefa
  concluída) e `README.md` também (espelho é escopo da `T17`). Tarefa de redação de doutrina, sem
  TF/TR de código; sem achado fora de escopo. Desvio de protocolo declarado: o status `in progress`
  não foi gravado no diário antes da execução — a linha **Próxima tarefa** já designava a tarefa e a
  gravação separada custaria um turno; o diário foi atualizado uma vez, no fechamento. A coluna
  *Modelo* das duas linhas novas, que o dossiê mandava preencher sem fixar valor, foi escalada pelo
  executor e **decidida pelo dono na mesma rodada** (`DA-12`): Orquestração em Sonnet (derivação
  confirmada) e Revisão **em Opus** (a derivação por paridade com Auditoria foi corrigida) — a célula
  da matriz foi ajustada pelo orquestrador, e a `T10` cria o `pantonic-reviewer` já com `model: opus`.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T6b` — doutrina de integridade do contexto — `done`.** Transcrição da `DA-11` nas cinco
  superfícies medidas, sem nenhuma outra tocada. `~/.claude/CLAUDE.md` **Regra 2** reescrita em texto
  íntegro (título passa a "Integridade do contexto"; L17-49): cenário coerente, as duas condições, os
  cinco sinais de poluição, a fronteira cenário × detalhe, a consequência para quem executa e para
  quem orquestra, e o checkpoint como forma de aplicar. `GOVERNANCA.md` §4.3 — o bullet "toda tarefa
  ocorre dentro de um contexto limpo" (régua de contagem) dá lugar à forma condensada `DR-A`: duas
  condições aninhadas, coesão fatal com os sinais e a fronteira cenário × detalhe, capacidade a ~50%
  com o proxy de tool uses por classe afirmado inline enquanto não houver proxy de ocupação, mais o
  bullet da consequência prática (executor inalterado; orquestrador encerra na troca de plano ou
  iniciativa, ou na capacidade); o bullet do checkpoint (2/3 do teto) ganha uma frase para o gatilho
  de poluição. `GOVERNANCA.md` §7 item 7 **reescrito**, nenhum item novo (`G-DEADCODE` intacto no
  item 8). `README.md` em duas linhas: verbete **Contexto** do glossário e linha 7 da tabela de
  guardrails do §10, que segue em **Instrução de agente**. `docs/RESIDENCIA_DOUTRINA.md` seção
  "Regra 2": título, faixa de linhas (17-49), item 2.1 e a nota de colisão, que apontava "§7 item 8"
  e agora aponta o item 7. Verificação: `.claude/checks/check-readme.ps1` em **exit 0** (7 agentes,
  10 skills, 14 guardrails, 14 seções com fonte da verdade válida); `Grep` por "tarefa por contexto"
  em `GOVERNANCA.md` e `README.md` deixa 6 ocorrências, todas legítimas — `GOVERNANCA.md` L221 e
  L519 e `README.md` L574 afirmam a forma operacional de quem executa, preservada pela `DA-11`; L313
  é o texto novo; `README.md` L27 e L613 são o título do §9, fora de escopo por dossiê. Varredura
  `redacao-doc` §6 sobre o texto novo publicado sem achado (sem ID de processo, sem data, terceira
  pessoa; as negações remanescentes enunciam limite). Tarefa de redação de doutrina, sem TF/TR de
  código. Achado fora de escopo indexado no `TK-25`. Teto da classe (30) respeitado.
  Consumo: ver `docs/telemetria.tsv`.

**Replanejamento de 2026-08-08 — a `DA-9` foi revogada pelo dono e a `T6` foi partida.** A releitura
"uma tarefa por contexto **de executor**" abria exceção por papel; o veredito do dono é que não há
exceção a abrir — conduzir um plano **é** uma tarefa, e o errado era a régua (contar tarefas), não o
alcance da regra. Entra a **`DA-11`**: a Regra 2 passa a governar **integridade de contexto**, sob
duas condições independentes — **coesão** (violação fatal e imediata: para-se ao primeiro sinal de
poluição) e **capacidade** (~50% da janela, encerramento planejado) —, com a fronteira cenário ×
detalhe limitando o gatilho fatal, "uma tarefa por contexto" preservada como forma operacional de
quem executa, e o limite do orquestrador **derivado** (a janela dele é o plano, não a tarefa).
Ratificada com o texto normativo à vista, de modo que a tarefa chega ao executor como transcrição.
A `T6` virou **`T6a`** (papéis e fronteira de registro) e **`T6b`** (integridade do contexto, cinco
superfícies) por volume medido — juntas estouravam o teto da classe. Total do plano: 17 → **18**.

- **`EXA-T7` — `telemetria.py`: a série deixa de ser editada à mão — `done`.** Cria
  `.claude/tools/telemetria.py` (subcomando `append`, um argumento nomeado por coluna do TSV —
  `data`, `projeto`, `tarefa`, `modelo`, `tool_uses`, `tokens_k`, `duracao_s`, `fonte` — mapeamento
  sempre por nome, nunca por posição) e `tests/test_telemetria.py`. Validação por coluna: `data`
  em `AAAA-MM-DD` (`datetime.date.fromisoformat`); `projeto`/`tarefa`/`modelo` não vazios e sem
  tab/newline (guarda contra corromper o TSV); `tool_uses` inteiro não negativo; `tokens_k`/
  `duracao_s` numéricos não negativos; `fonte` restrita a `usage`/`contado`/`nao_medido`. Coluna
  inválida ⇒ `TelemetriaValidationError`, `exit 1`, mensagem em stderr nomeando a coluna, nada
  escrito. Escrita atômica: conteúdo anterior lido em bytes + linha nova, gravados num arquivo
  temporário no mesmo diretório (`tempfile.mkstemp`), substituído via `os.replace` — nenhum leitor
  concorrente vê arquivo parcial, conteúdo anterior nunca tocado por conteúdo. `.claude/tools/` não
  existe antes desta tarefa (fato 2 do dossiê) e `kit_check.ps1 -Mode validate` só inventaria
  `agents/`/`skills/` (fato 1) — **`kit_check.ps1` não foi tocado**, confirmado em exit 0 depois.
  TF cobre linha válida + preservação byte a byte do conteúdo anterior na mesma asserção (`tmp_path`,
  nunca o `docs/telemetria.tsv` real); dois TR travam `fonte` inválida e campo numérico não numérico,
  ambos com exit != 0 e conteúdo anterior intacto — as 4 verificações do dossiê, sem excesso. Módulo
  carregado por caminho via `importlib.util.spec_from_file_location`/`exec_module` (`.claude/tools/`
  tem ponto no nome, não é pacote importável — mesmo padrão de `tests/test_dead_code.py`). Header
  real do TSV e as 105 linhas existentes conferidos antes de codar (fato 3) e não tocados. Achado
  fora de escopo indexado no `TK-26`: a série histórica usa célula vazia e `-` como sentinela de
  "não medido" sem convenção única, e o `append` novo não aceita nenhuma das duas — decisão
  deliberada de escopo mínimo, dossiê não pede sentinela. Sem ramo condicional a resolver, sem
  obstáculo à rota do dossiê. Teto da classe (40) respeitado.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T8a` — `rdo.py new`: o documento e o template — `done`.** Cria `.claude/tools/rdo.py`
  (subcomando `new`), `.claude/tools/rdo_template.md` e `tests/test_rdo.py`; cria o diretório
  `docs/RDO/` (`.gitkeep`, vazio até a primeira chamada). `new --plano <md> --tarefa <ID>
  [--rdo-dir <dir>]` localiza o cabeçalho da tarefa pela gramática da `DP-C`
  (`### <ID> — <título> [<modelo> · classe <classe> · teto <N>]`), extrai o dossiê (`Objetivo`,
  `Arquivos-alvo`/`Entregável` — alternância exigida —, `Verificação`, `Pronto quando`, `Dossiê
  fechado por`, demais rótulos em `extras` verbatim) e materializa o `.md` a partir do template,
  que carrega os oito campos fixos do pacote de retorno da `DP-A` com seus tetos (`tarefa`,
  `status`, `arquivos_tocados`, `desvios_do_dossie`, `verificacao`, `achados`, `orcamento`,
  `pendencia_para_o_dono`) — nenhum deles no prompt de agente algum. Achado durante a extração:
  os cabeçalhos deste próprio plano (`P-0734`) escrevem a `classe` por extenso, na grafia da
  linha de `GOVERNANCA.md` §3 (`implementação padrão`, `redação/planejamento`, `redação de
  doutrina`, `investigação`), não no slug da `DP-C` — o parser normaliza (remove acento,
  minusculiza) contra uma tabela de alias para os cinco slugs antes de validar o teto; sem isso
  nenhuma tarefa deste plano seria lida sob esquema `padrao`. Plano legado (cabeçalho sem
  `classe`/`teto`): `--esquema-legado` com `--modelo`/`--classe`/`--teto` explícitos, registrando
  `esquema=legado` no RDO, conforme a política da `DP-C`. Escrita atômica (`tempfile.mkstemp` no
  diretório de destino + `os.replace`) e falha ruidosa (`exit 1`, stderr nomeando o campo/
  identificador, nada escrito) no mesmo padrão de `.claude/tools/telemetria.py`; módulo carregado
  por caminho no teste (`.claude/tools/` não é pacote importável) — `DossieTarefa` é classe simples,
  não `@dataclass`, porque a resolução de anotações adiadas do `dataclasses` quebra sob
  `spec_from_file_location` sem registro em `sys.modules`. TF roda `new` sobre a `T7` (tarefa real,
  `done`, deste plano) e confere identidade, classe resolvida, dossiê extraído e os oito campos
  fixos no `.md`; TR roda `new` sobre identificador inexistente (`T999`) — `exit != 0`, nada
  escrito em `--rdo-dir`, identificador nomeado em stderr. `laudo`/`close` não implementados
  (fatias `T8b`/`T8c`); índice de `docs/RDO/` não gerado (`T8c`); `kit_check.ps1` não tocado.
  Sem achado fora de escopo. **Estouro de teto: 48 tool uses contra os 40 da classe** (medido na
  notificação; o auto-relato do executor dizia "teto respeitado" — a série é do orquestrador). A
  fatia já era o produto de uma partição por orçamento, e ainda assim estourou: o `new` carregou o
  parser do esquema da `DP-C` inteiro (normalização de classe, alternância de campo, ramo de plano
  legado), que é uma capacidade própria e não um acessório do subcomando.
  Consumo: ver `docs/telemetria.tsv`

- **`EXA-T8b` — `rdo.py laudo`: o veredito é calculado — `done`.** Acrescenta o subcomando `laudo`
  a `.claude/tools/rdo.py`, atualiza o texto da seção `## Laudo` do template e leva
  `tests/test_rdo.py` a 7 testes. `laudo --rdo <caminho>` recebe um flag por dimensão
  (`--criterio-de-pronto`, `--escopo`, `--testes`, `--guardas`, `--rota`, `--residuo`,
  `--registro`, cada um com `choices` nos quatro níveis), `--vermelho-mecanico <dimensão>`
  repetível e `--observacoes`/`--recomendacoes` livres; `calcular_laudo()` **copia** de
  `docs/RUBRICA_DE_REVISAO.md` §5 os pesos (3,2,3,3,2,2,2), as quatro dimensões que não admitem
  `não se aplica`, as cinco bloqueantes, a fórmula e a dominância — nada reinterpretado. Os três
  invariantes do dossiê ficaram executáveis: `--percentual`/`--veredito` **não existem** como
  flags (`DA-6` — a recusa é o erro de argumento desconhecido do argparse), `conforme` em
  dimensão declarada vermelha pela camada mecânica é recusado nomeando a dimensão (`DA-7`) e
  `não se aplica` numa das quatro que não o admitem é recusado; nos dois casos nada é escrito.
  Decisão de implementação: o arredondamento de metade para cima é feito sobre `Fraction` exata,
  nunca `round()` — o arredondamento bancário do Python levaria 0,5 para o par e desalinharia a
  fronteira de 95/70 da rubrica. A seção `## Laudo` é localizada por regex de heading (não por
  offset) e reescrita sozinha, com o mesmo padrão atômico de `cmd_new`. TF reproduz o exemplo de
  85%/`ressalva` da rubrica; os TR cobrem a dominância (`escopo` não conforme e as demais
  conforme dão 88% — `ressalva` pela faixa, `reprovado`/`bloqueante=escopo` pela dominância), a
  recusa de percentual/veredito por argumento e as duas recusas acima, ambas conferindo que o
  arquivo ficou intacto. Verificação: `13 passed` na suíte total (piso 8 + 5 novos, reconferido
  pelo orquestrador após a notificação), `dead_code.py`, `ratchet_piso.py`, `kit_check.ps1`
  (`validate` e `check-drift`) e `check-readme.ps1` todos em exit 0; `tests/conformance/` não
  existe neste repo (hub de kit, sem camadas de aplicação) — não aplicável. `close` e o índice de
  `docs/RDO/` não implementados (`T8c`); `kit_check.ps1` não tocado. Sem achado fora de escopo e
  sem pendência para o dono. **Orçamento: 26 tool uses contra o teto 40** — dentro, contra os 48
  da `T8a`: a fatia que sobrou depois de o `new` ter absorvido o parser do esquema da `DP-C`
  coube com folga, o que confirma a partição por orçamento como controle, não como formalidade.
  Consumo: ver `docs/telemetria.tsv`

- **`EXA-T8c` — `rdo.py close` e o índice gerado — `done`.** Acrescenta o subcomando `close` a
  `.claude/tools/rdo.py` e leva `tests/test_rdo.py` a 12 testes (suíte total `18 passed`, piso
  13 → 18). `close --rdo <caminho> --tarefa --status --arquivos-tocados --desvios-do-dossie
  --verificacao --achados --orcamento --pendencia-para-o-dono` grava os oito campos fixos do
  pacote de retorno (`DP-A`) na seção `## Execução` já aberta por `new` — **validando teto de
  linhas por campo** (tabela de `DP-A`: 1/1/15/8/6/8/1/4), campo ausente é `unrecognized
  arguments`/`required` do próprio argparse. Lê veredito/dimensão bloqueante já gravados por
  `laudo` na seção `## Laudo` (recusa nomeando `laudo` se ainda placeholder — `close` não
  delegável antes da `T8b`, e o CLI também impõe isso). `calcular_desdobramento()` **copia** a
  precedência do bloco A da `DP-B` (`docs/plans/P-0734-execucao-autonoma.md` `### DP-B`):
  `bloqueado` (`A3`) antes de `estouro` (`A4`, comparando `<gastos>` do próprio campo `orcamento`
  contra `<teto>`, independentemente do resto), `status=parcial` tratado como reprovação (`A5`),
  `reprovado`/`aprovado com ressalva`/`aprovado` (`A6`..`A9` — a distinção `A6`/`A7` de
  retentativa é contador do loop, fora da autoridade mecânica deste CLI, registrado como achado
  abaixo). Os cinco valores de saída são substrings literais das células "ação" da tabela — nada
  inventado. Grava `## Fechamento` (`**Desdobramento:** <valor>`) como marcador de idempotência:
  `close` sobre RDO já com essa seção falha ruidosamente nomeando o caminho, sem escrever nada.
  `_regenerar_indice()` varre `docs/RDO/*.md` (nunca `INDEX.md` a si mesmo, nunca `.gitkeep` —
  exclusão por construção do glob, não por exceção) e reescreve `docs/RDO/INDEX.md` por inteiro,
  atômico (`tempfile.mkstemp` + `os.replace`, mesmo padrão de `cmd_new`/`cmd_laudo`); `docs/RDO/`
  real permanece só com `.gitkeep` (179 bytes, intacto) — todos os RDOs de teste usam `tmp_path`.
  TF fecha um RDO-fixture pronto (laudo `aprovado`/`nenhuma`, sem estouro) com um segundo RDO
  ainda aberto e um `.gitkeep` no mesmo diretório, e confere que `INDEX.md` lista os dois `.md` e
  ignora o `.gitkeep`. TR cobrem: RDO inexistente (caminho nomeado em stderr, `INDEX.md` não
  criado), fechar RDO já fechado (conteúdo idêntico ao pós-primeiro-fechamento), campo além do
  teto (`desvios_do_dossie` com 9 linhas contra teto 8, nada escrito) e `close` sem laudo
  calculado (placeholder de `new` intacto, `laudo` nomeado em stderr, nada escrito). Verificação:
  suíte total `18 passed`; `dead_code.py`, `ratchet_piso.py` (sem piso declarado neste
  consumidor), `kit_check.ps1` (`-Mode validate` e `-Mode check-drift`) e `check-readme.ps1`
  todos exit 0; `tests/conformance/` não existe neste repo (hub de kit, sem camadas de aplicação)
  — não aplicável, mesma constatação da `T8b`. Achado fora de escopo, com rota: a distinção
  `A6`/`A7` (retentativa) e o roteamento `A1`/`A2`/`B1`..`B4` da `DP-B` seguem inteiramente fora
  deste CLI — são estado/decisão do loop, não do RDO; nenhuma ação aqui, já é o desenho esperado
  pela própria `DP-B` ("nenhuma célula pede juízo" é sobre o scrum-master, não sobre `rdo.py`) —
  cobertos quando a `T11` (skill `scrum-master`) for implementada, sem tíquete novo. Sem
  pendência para o dono. **Orçamento: 38 tool uses contra o teto 40** — dentro, mas com margem
  estreita; o auto-relato do executor dizia 31, e o número medido é o da notificação.
  Consumo: ver `docs/telemetria.tsv`

- **`EXA-T9a` — `review_evidence.py`: diff, escopo e a forma do dossiê — `done`.** Partida da
  `T9` no despacho por orçamento (a `T9` original tinha cinco guardas a invocar mais fixture de
  repositório — mesmo motivo que partiu a `T8`). Cria `.claude/tools/review_evidence.py` e
  `tests/test_review_evidence.py`; nenhum outro arquivo tocado (`rdo.py` e `.claude/README.md`
  intactos, como o dossiê exigia). Reusa `extrair_dossie` de `rdo.py:186` carregado por caminho
  (mesmo padrão de `test_rdo.py`) para obter os arquivos-alvo declarados da tarefa; coleta
  `git diff --stat HEAD` (com fallback sem `HEAD` se o repositório ainda não tem commit) e a
  lista de arquivos tocados via `git status --porcelain=v1 --untracked-files=all`; confronta
  tocados × alvos para o veredito mecânico da dimensão `escopo`
  (`docs/RUBRICA_DE_REVISAO.md:63-77`) — `conforme` quando o tocado é subconjunto do alvo; caso
  contrário só o **fato** ("N arquivo(s) fora dos alvos: ..."), veredito deixado em aberto, nunca
  resolvido para `parcial` sozinho (esse insumo mora no pacote de retorno, que este script não
  recebe). Recorta o trecho de diff de cada arquivo-alvo com teto de caracteres configurável
  (default 4000; truncamento sempre marcado na saída). Seção `## Guardas` nasce nomeada e vazia,
  marcada "não coletado", para a `T9b` preencher sem reescrever o renderizador. Dois defeitos
  reais apareceram só ao escrever o TF com repositório `git` de fixture (sem precedente na
  suíte) e foram corrigidos antes do verde: (1) `git status --porcelain=v1` sem
  `--untracked-files=all` colapsa um diretório inteiramente novo em `dir/` em vez de listar os
  arquivos dentro dele — escondia exatamente o caso "arquivo fora do escopo dentro de pasta
  nova"; (2) carregar `rdo.py` por `importlib` grava `__pycache__/` ao lado do arquivo, que
  aparecia como "tocado" nos testes porque o repositório de fixture não tinha `.gitignore` — o
  hub real já ignora `__pycache__/` (`TK-13`), então o fixture passou a espelhar isso em vez de o
  script ganhar lógica de filtro. TF cobre escopo respeitado (arquivo novo untracked + arquivo
  modificado, ambos dentro dos alvos, vereditos `conforme`); TR cobrem escopo violado (arquivo
  fora dos alvos gera o fato sem "parcial"), truncamento pelo teto (corte marcado, nunca
  silencioso), extração de arquivos-alvo (crases sem `/` ignoradas, sufixo `:N`/`:N-M` de
  referência de linha removido) e o CLI (`review_evidence: OK`/`FALHOU` com exit 0/1). Limitação
  documentada no próprio módulo (não é achado fora de escopo, é comportamento aceito pelo
  dossiê): a extração de arquivos-alvo é textual pura (todo caminho entre crases no campo
  `Arquivos-alvo` é tratado como alvo) e não interpreta prosa negativa como "não editar `x.py`" —
  quem interpreta é o reviewer (`DA-7`). Verificação: suíte total `23 passed` (piso 18 → 23);
  `dead_code.py`, `ratchet_piso.py` (sem piso declarado, `TK-21`), `kit_check.ps1` (`-Mode
  validate` e `-Mode check-drift`) e `check-readme.ps1` todos exit 0; `tests/conformance/` e
  `tests/boundary/` não existem neste repo — não aplicável, mesma constatação da `T8b`/`T8c`.
  Sem achado fora de escopo novo e sem pendência para o dono. **Orçamento: 37 tool uses contra o
  teto 40** — dentro, e a partição da `T9` se justificou: a tarefa inteira teria estourado.
  Consumo: ver `docs/telemetria.tsv`

- **`EXA-T9b` — `review_evidence.py`: a bateria de guardas — `done`.** Preenche a seção
  `## Guardas` que a `T9a` deixou nomeada e vazia (`.claude/tools/review_evidence.py`,
  `tests/test_review_evidence.py` — edita, não cria, nenhum outro arquivo tocado). Bateria de
  seis comandos lidos de `GOVERNANCA.md` §3 (via o precedente já fechado pela `T9a`, que a rodou
  e registrou no fechamento): `python -m pytest -q`, `python .claude/checks/dead_code.py`,
  `python .claude/checks/ratchet_piso.py`, `pwsh .claude/checks/kit_check.ps1 -Mode validate`,
  `pwsh .claude/checks/kit_check.ps1 -Mode check-drift`, `pwsh .claude/checks/check-readme.ps1`
  — `BATERIA_GUARDAS`, cada comando com `cwd=root`, exit code e stdout+stderr colados
  (`rodar_bateria_guardas`, injetável via `comandos_guardas` para não depender de
  `.claude/checks/*`/`pytest.ini` ausentes no repositório de fixture da suíte). Veredito mecânico
  travado (`DA-7`) das duas dimensões: `guardas` (`docs/RUBRICA_DE_REVISAO.md:94-106`, autoridade
  integral, sem faixa de juízo — qualquer comando fora de exit 0 resolve `não conforme`, nunca
  `parcial` sozinha) via `veredito_guardas`; `testes` (`:79-92`, evidência mecânica é o exit code
  do comando `pytest` da bateria) via `veredito_testes`. Seção renderizada
  (`_renderizar_guardas`) lista nome/comando/exit code de cada item, cola a saída truncada
  (teto configurável, corte sempre marcado) só quando o comando falha, e fecha com os dois
  vereditos — placeholder "não coletado" da `T9a` removido. TF cobre a bateria toda verde
  (unidade, sem subprocess) e o caminho end-to-end via `montar_documento` com bateria injetada;
  TR cobrem comando não-`pytest` vermelho travando só `guardas`, comando `pytest` vermelho
  travando as duas dimensões, e bateria sem comando `pytest` travando `testes` em `não conforme`
  por ausência de evidência (nunca silêncio) — quatro regressões novas contra a exigida mínima de
  uma. Os quatro testes pré-existentes da `T9a` foram ajustados para injetar
  `comandos_guardas`/sobrescrever `BATERIA_GUARDAS` (bateria real depende de infraestrutura
  ausente no repositório de fixture; sem isso os testes ficariam lentos e não-determinísticos) e
  para não mais afirmar o placeholder "não coletado", que deixou de existir por desenho desta
  tarefa. Verificação: suíte total `28 passed` (piso 23 → 28, +5 líquido: 10 testes em
  `test_review_evidence.py` contra 5 antes); os seis comandos da bateria rodados de fato contra o
  hub real, todos exit 0 (`pytest -q` 28 passed; `dead_code.py` 0 achados; `ratchet_piso.py` sem
  piso declarado, `TK-21`; `kit_check.ps1 -Mode validate` e `-Mode check-drift` OK; `check-readme.ps1`
  OK); `tests/conformance/` e `tests/boundary/` não existem neste repositório — não aplicável,
  mesma constatação da `T8b`/`T8c`/`T9a`. Sem achado fora de escopo novo e sem pendência para o
  dono. **Orçamento: ~35 tool uses contra o teto 40** (contagem do executor, não a medida —
  telemetria real fica com a notificação do orquestrador).
  Consumo: ver `docs/telemetria.tsv`

- **`EXA-T10` — agente `pantonic-reviewer` — `done`.** Cria `.claude/agents/pantonic-reviewer.md`
  (frontmatter `model: opus`, conforme a `DA-12`; `tools: Read, Glob, Grep, Bash` — a independência
  imposta pela lista, sem `Write`/`Edit`/`NotebookEdit`), regenera `.claude/README.md` por
  `kit_check.ps1 -Mode generate` (nenhuma edição manual da região entre marcadores) e acrescenta a
  linha do agente à tabela **Agentes** da seção "Anatomia do kit" do `README.md` da raiz. O terceiro
  alvo foi resolvido pelo orquestrador antes do despacho: a checagem 1 do `check-readme.ps1` exige
  paridade entre `.claude/agents/*.md` e aquela tabela, então a linha é consequência mecânica da
  criação do agente — não a revisão substantiva do espelho, que segue sendo a `T17` e não foi
  antecipada. Corpo do agente: papel apontando para a linha `Revisão` da matriz de `GOVERNANCA.md`
  §3 e para `docs/RUBRICA_DE_REVISAO.md` sem recopiar nenhum dos dois; fatos estáveis (ordem
  canônica das sete dimensões, as quatro grafias de nível aceitas pelo gerador, as que não admitem
  `não se aplica`, autoridade da camada mecânica, achado de processo com três alvos); protocolo em
  sete passos (dossiê → pacote de retorno → dossiê de evidência → marcação dimensão a dimensão →
  achados de processo → `rdo.py laudo` → retorno ao chamador); proibições fechando em "não julga
  mais de uma tarefa por contexto". Verificação: os seis comandos da bateria do §3 em exit 0 —
  `pytest -q` (`28 passed`, piso mantido; tarefa de doutrina, sem TF/TR de código), `dead_code.py`
  (0 achados), `ratchet_piso.py` (sem piso declarado, `TK-21`), `kit_check.ps1 -Mode validate` e
  `-Mode check-drift` (8 agentes, 10 skills), `check-readme.ps1` (8 agentes, 10 skills, 14
  guardrails, 14 seções). Varredura `redacao-doc` §6 sobre o arquivo novo sem achado, com 1 correção
  V9 aplicada; V10 mantido só na abertura ("Você é o revisor"), forma canônica dos outros sete
  arquivos de agente. **Desvio do dossiê, declarado:** a prosa que introduz a tabela
  (`README.md:726`) dizia "sete agentes" e passou a "oito" — mesma consequência mecânica da linha,
  no mesmo parágrafo, e o guarda não mede contagem em prosa. Achado fora de escopo indexado no
  `TK-27`. **Orçamento: 19 tool uses contra o teto 30** — dentro (o auto-relato dizia 11; o número
  medido é o da notificação).
  Consumo: ver `docs/telemetria.tsv`

- **`EXA-T11` — skill `scrum-master`: o loop — `done`, com o RDO impedido de fechar.** Cria
  `.claude/skills/scrum-master/SKILL.md` (255 linhas), regenera `.claude/README.md` por
  `kit_check.ps1 -Mode generate` (8 agentes, 11 skills) e acrescenta a linha da skill à tabela
  **Skills** de "Anatomia do kit" no `README.md` da raiz — terceiro alvo fora dos declarados, exigido
  pela checagem de paridade do `check-readme.ps1`, mesma consequência mecânica que a `T10` teve ao
  criar o agente. Os dez passos do fluxo saem com **gatilho, entrada, ação e saída** declarados um a
  um; `G-PLANREADY` e o gate de delegação apenas **apontados**, nunca recopiados (a deduplicação é a
  `T12`); `A1`..`A9` e `B1`..`B4` em forma operacional com `DP-A`/`DP-B` declaradas normativas;
  encerramento de janela só por teto numérico (10 tarefas / 900 k) e nunca por percepção; proibições
  explícitas — não implementa, não julga entrega, não decide arquitetura, **não abre o RDO**, não
  reescreve dossiê e não paraleliza. Verificação: os seis comandos da bateria do §3 em exit 0
  (`pytest -q` 28 passed, `dead_code.py`, `ratchet_piso.py`, `kit_check.ps1 -Mode validate` e
  `-Mode check-drift`, `check-readme.ps1` — este último vermelho na primeira passada, pela linha
  ausente na tabela de Skills, corrigido e reconferido). **Percurso a seco sobre a `DHB-T1`**
  (`P-0733`), 10/10 passos, nada executado: o passo 3 recusou a tarefa pelo **gate de delegação item
  5** (cabeçalho legado sem `classe`/`teto` ⇒ `B3`), exercitando o roteamento no primeiro alvo real.
  **Fechamento do RDO bloqueado por defeito medido em `rdo.py close`** — ver o bloco abaixo; o
  executor levantou e **não decidiu** (Regra 8), e os oito campos do pacote ficaram por gravar.
  Achados fora de escopo, com rota: `proximo-passo/SKILL.md` cita `G-PLANREADY` como item 12 quando é
  o **item 11** (rota `T12`); planos legados param em `B3` por falta de `classe`/`teto` (rota `T16`,
  e é o `TK-24`); a convenção `docs/RDO/evidencia/<plano>-<ID>.md` foi prescrita pela skill sem
  ratificação prévia (rota `T16`); o RDO não tem campo para percurso a seco (sem ação).
  **Orçamento: 32 tool uses contra o teto 30 — estourado**, por auto-relato: a execução caiu por
  limite semanal de API no meio e foi retomada por `SendMessage` ao mesmo agente, de modo que
  **PARCIAL — trecho pré-queda não medido**; só a retomada tem bloco `<usage>`.
  Consumo: ver `docs/telemetria.tsv` (linha `EXA-T11-retomada` — perna medida apenas).

**Defeito de contrato entre `DP-A` e a `T8c` — aberto, decisão do dono.** `rdo.py close`
(`.claude/tools/rdo.py:654`) faz três coisas num ato só: valida e grava os oito campos do pacote de
retorno na `## Execução` (`:697-708`, **único escritor** desses campos), **exige** a `## Laudo` já
calculada (`:678-683`) e grava o `## Fechamento`. Mas a `DP-A` põe o pacote como **entrada** da
revisão, e o laudo é **saída** dela: o pacote precisa do `close`, que precisa do laudo, que precisa
do pacote. Nenhuma tarefa fecha o ciclo — o `EXA-T11` é a primeira a percorrê-lo inteiro, porque o
loop não existia antes dela. Circularidade confirmada no código, não inferida do relato.

**A decisão foi levada ao dono em 2026-08-10 e a resposta redefine o fluxo — `P-0734` entra em
replanejamento.** Nenhuma das três opções (partir `close`, flag `--sem-laudo`, revisar a `DP-A`) foi
escolhida: o dono descreveu o processo de outra forma. Dois pontos foram **fechados na mesma rodada**
e saem da lista de divergências:

- **O scrum-master é skill** — terminologia do dono corrigida por ele próprio, depois de conferido
  que a skill entregue atende as oito responsabilidades descritas: selecionar a tarefa (passo 2),
  invocar o executor no modelo correto (passo 4), popular o contexto dele com o suficiente e
  necessário (passo 4), aguardar o retorno (passo 5), invocar o inspetor (passo 6), ler o laudo
  (passo 7), fechar a tarefa em RDO quando não há desdobramento (passo 9) e executar o desdobramento
  quando há — nova execução, correção ou escalada ao dono (blocos `A`/`B`). Nenhuma delas exige forma
  de agente; a `DA-1` permanece válida.
- **Residência e identidade do RDO** — "anexar na memória do projeto" significa a pasta própria e
  destacada, que já é `docs/RDO/`: um `.md` por tarefa, identificado pelo identificador dela, e um
  plano concluído tem tantos RDOs quantas tarefas executadas. O que existe já conforma (o nome
  carrega `<plano>-<tarefa>` com slug de título como sufixo). **Consequência medida da regra:**
  `docs/RDO/` tem **1** RDO para **15** tarefas fechadas do `P-0734` — `T1`..`T10` fecharam antes de o
  instrumento existir e têm o diário como registro canônico. O replanejamento decide se retroage ou
  se a regra vale daqui para a frente.

**Divergências de contrato que permanecem, todas com a `DP-A`/`DP-B`:** o executor devolve **"Done"**
e não a linha de 5 campos — e `status`, `tools` e `pendencia` são justamente o que as regras `A3`,
`A4` e `B1` consomem; o **pacote de retorno de 8 campos deixa de existir**; o **RDO é criado no fim**,
pelo scrum-master, e não aberto no início por `rdo.py new`; o inspetor recebe **o mesmo contexto do
executor**, não o pacote em arquivo; o **laudo carrega a recomendação**, em vez de o desdobramento
sair da tabela; e a retentativa é **agente novo em contexto novo**, não o re-despacho do mesmo
executor da regra `A6` — nesta última a descrição do dono é a mais coerente com a Regra 2, já que o
contexto de uma execução reprovada está poluído. A circularidade `close`↔`laudo` **desaparece** sob a
descrição do dono, porque o pacote de retorno deixa de existir — o defeito registrado acima é real,
mas o conserto certo depende de qual descrição é normativa.

**Replanejamento executado em 2026-08-10 (Opus, contexto novo).** O decision record está autorado
como **proposta** em `docs/plans/P-0734-execucao-autonoma.md` §9 (`DP-D`): as seis divergências
julgadas uma a uma, a realocação dos oito campos do pacote, a fronteira entre o que o loop sabe e o
que o juiz sabe, e o rebase do que sobrevive dos artefatos já construídos (`telemetria.py` e
`review_evidence.py` intactos; `rdo.py new` perde objeto; `rdo.py close`, `pantonic-reviewer` e
`scrum-master` editados, nenhum refeito). A circularidade `close` ↔ laudo desaparece com o pacote.

**`DP-D` ratificada pelo dono em 2026-08-10**, com o texto à vista, incluindo o desvio declarado no
`D1` (o executor devolve `Done` ou `Done pendencia=<uma linha>`, para que a regra `B1` não dependa de
o revisor inferir do diff uma pendência que o diff não contém). O ponto aberto foi fechado conforme a
recomendação: **o RDO não retroage** — `T1`..`T10` mantêm o diário como registro canônico.

Os quatro dossiês novos foram autorados **fechados** no mesmo ato (`G-PLANREADY` item 5). São quatro
e não três porque a `DP-C` só admite um modelo e uma classe por cabeçalho, e a fatia "revisor +
laudo" reunia código e doutrina. Duas decisões de desenho foram fechadas junto, para que nenhum
dossiê chegasse aberto ao executor: o **laudo ganha documento próprio**
(`docs/RDO/laudos/<plano>-<tarefa>.md`, com o RDO carregando campos e ponteiro, nunca a prosa) e
**`escalar` é marcado, não derivado** — as outras três recomendações saem do veredito calculado.

- **`EXA-T18` — `rdo.py laudo`: documento próprio e recomendação de domínio fechado — `done`.**
  `cmd_laudo` (`.claude/tools/rdo.py:501`, aprox.) deixa de depender de RDO aberto por `new`: grava
  em `docs/RDO/laudos/<plano>-<tarefa>.md` (`--plano`/`--tarefa`/`--laudos-dir`, default
  `docs/RDO/laudos`), criando o diretório se preciso, escrita atômica no mesmo padrão dos irmãos.
  `calcular_laudo` (`:457`, aprox.) passa a devolver também `recomendacao`/`pendencia`
  (`LaudoResultado`) pela tabela do dossiê — `aprovado`→`seguir`, `ressalva`→`seguir com ressalva`,
  `reprovado`→`refazer` — e `--escalar "<linha>"` força `recomendacao=escalar`
  **independentemente** da tabela, gravando a linha como `Pendência` (a que a regra `B1` consumirá).
  Domínio fechado nos quatro valores: nenhum flag `--recomendacao` existe — único canal é
  `--escalar` (mesma regra `DA-6` de percentual/veredito) — passar `--recomendacao`/`--percentual`/
  `--veredito` é `unrecognized arguments` (`SystemExit`), nada escrito. Removido o marcador morto
  `_LAUDO_MARCADOR_RE` (escrita na seção `## Laudo` de um RDO — rota abandonada por esta tarefa,
  `G-DEADCODE`); `rdo_template.md` `## Laudo` atualizado só na prosa, para apontar ao documento
  próprio e deixar explícito que vira campos+ponteiro na `T19` (não tocada aqui, por escopo).
  `cmd_new`/`cmd_close`/`_LAUDO_VEREDITO_RE`/`_LAUDO_BLOQUEANTE_RE` intocados, como o dossiê mandou
  (ficam temporariamente sem produtor até a `T19` rewire `close`; previsto no próprio dossiê, não é
  achado novo). Testes (`tests/test_rdo.py`): as 5 TF/TR antigas de `laudo` (interface `--rdo`)
  foram **reescritas**, não deletadas, para a interface nova — cobertura preservada (`DA-6`/`DA-7`,
  não-se-aplica, dominância de dimensão bloqueante) — mais teste novo das três derivações da tabela
  (parametrizado em um TF), da dominância de `--escalar` sobre `veredito=aprovado`, da recusa dos
  três argumentos de domínio fechado e do caminho de saída com diretório aninhado ainda
  inexistente. `test_rdo.py`: 13 testes (era 12). Achados fora de escopo: nenhum.
  Veredito — EXA-T18
  Suítes: Tier 1 (tests/test_rdo.py) — 13 passed; piso completo (`pytest -q`) — 29 passed (era 28;
    repositório ainda sem `tests/conformance/`/`tests/boundary/` — nada bloqueante a rodar ali)
  Piso: ratchet_piso.py — OK (sem piso declarado em tests/piso_comportamental.txt)
  Kit: kit_check.ps1 -Mode validate / -Mode check-drift — exit 0 (8 agentes, 11 skills, VERSION==KIT_VERSION '0.0.0')
  Espelho: check-readme.ps1 — exit 0 (8 agentes, 11 skills, 14 guardrails, 14 seções com Fonte da verdade)
  Checklist de review: ok — script CLI fora da árvore infracore/contracts/services/plugins (sem
    direção de camada a checar); sem dependência externa nova; sem trabalho pesado em thread de
    entrada; sem tipo cruzando camada; teste com significado alterado foi reescrito, não deletado;
    mudança comportamental amparada por decision record `DP-D` (§9), ratificada.
  Consumo: ver `docs/telemetria.tsv`

- **`EXA-T19` — `rdo.py`: o RDO se gera no fechamento — `blocked`.** G-EXECREADY: o dossiê do
  `### T19` não é performável sem uma decisão de arquitetura que não é do executor. O texto manda
  `cmd_close` materializar o RDO "a partir do plano, do laudo, do consumo medido e do desdobramento
  calculado" e confirma, via `9.1`/`D2` da própria `DP-D`, que "a validação dos 8 campos do pacote
  sai" (pacote de retorno deixou de existir) — mas não diz de onde `close` passa a tirar o parâmetro
  `status` (`entregue`/`parcial`/`bloqueado`) que `calcular_desdobramento` (reusada sem mudança de
  assinatura declarada, `:589`) continua exigindo. A tabela `D5` (§9) reparte o bloco A entre "passa
  ao laudo" (`A5`/`A6`/`A8`/`A9`) e "permanece no loop" (`A1`/`A2`/`A4`/`A7`/`B1`-`B3`) e **omite
  `A3` (bloqueado)** das duas listas — ramo condicional não resolvido. Segunda lacuna: `D1` põe
  `pendencia_para_o_dono` em "retorno do executor (campo opcional) ou laudo", e o `### T19` não diz
  se `close` ganha um flag para esse canal opcional. Nenhuma decisão foi tomada nesta sessão
  (G-PLANFIDELITY/Regra 8 global) — o dossiê volta ao planejamento para fechar as duas lacunas antes
  de ser redelegado. Nenhum arquivo tocado (nenhuma edição em `rdo.py`/`rdo_template.md`/
  `tests/test_rdo.py`). Achado indexado no `TK-28`.
  Consumo: ver `docs/telemetria.tsv`.

- **Replanejamento do dossiê da `EXA-T19` — `done`** (rodada de planejamento, não é tarefa do plano).
  As duas lacunas do `TK-28` foram fechadas por derivação da `DP-D` já ratificada, sem decisão nova do
  dono; detalhe da rota no `TK-28`. Escopo do `### T19` **cresceu**: além do rewire do `close`, ele
  passa a criar `laudo --status` (item mínimo, com o limite do que pode ser tocado da `T18` declarado
  no campo *Cuidado*) e a fixar a CLI final do `close` — `--plano/--tarefa/--tool-uses/--tokens-k/
  --duracao-s` mais os quatro flags de esquema legado movidos verbatim do `new`, sem os quais a `T17`
  não fecharia —, a origem do teto para `A4` (`tool_uses > dossie.teto`, sempre do cabeçalho), a
  detecção de "já fechada" e a forma seção-a-seção do template novo; os testes vão de 4 para 9.
  Achados fora de escopo: `calcular_desdobramento` recebe `bloqueante` e **nunca o usa**
  (`.claude/tools/rdo.py:624-644`, parâmetro morto, mantido porque a assinatura não muda — merece
  tíquete próprio); ramo morto `"prescrito no dossiê"` em `cmd_new:368`, que morre junto com o
  `cmd_new` na própria `T19`; `docs/RDO/laudos/` ainda não existe (a `T18` entregou o escritor, nenhum
  laudo foi produzido); o dossiê da `T20` já dizia que o revisor declara o `status` e fica consistente
  sem edição. Consumo: ver `docs/telemetria.tsv`.

- **Replanejamento `DP-E` — o `status` é da tarefa, não do laudo — `done`** (rodada de planejamento,
  não é tarefa do plano). A captura do §10 virou decisão **ratificada pelo dono em 2026-08-11**.
  Acolhidos os enunciados 1, 2, 3 e 5: `status` é característica da tarefa, o `scrum-master` é o
  único que o escreve, o laudo é escrito só pelo revisor (o `scrum-master` lê e descarta o resto), e
  o loop ganha dois gatilhos de estado — um que invoca o revisor, outro em que o RDO é escrito
  (estrutura fixada; a grafia segue a lista final). **Enunciado 4 (os sete estados) não virou norma:**
  foi deslocado para tarefa própria, que primeiro **avalia** se a lista é suficiente, exagerada ou
  insuficiente. **Nome do papel resolvido:** `pantonic-reviewer` é canônico, a prosa diz *revisor* e
  o termo *inspetor* está abolido do vocabulário. **Revogado da `DP-D`:** a linha "`status` → laudo
  do revisor" do `D1`, a célula "`status` → laudo" do `D2` e a *Nota de derivação de 2026-08-11*
  inteira (com ela caem `laudo --status`, a partição do `A3` e a leitura do `status` pelo `close`).
  **Permanecem** `D3`, `D4`, `D6`, o resto de `D1`/`D2`, o `D5` (recomendação de domínio fechado e
  partição por origem da informação), os três tetos da `DP-B`, a não-retroação do RDO e os §9.1/§9.2
  — declarados item a item no §10.3. O canal `close --pendencia` sobrevive como encomenda, sem
  derivação nova. Encomendadas **seis tarefas** (`EXA-T22..T27`): a `T22` fecha a `DP-F` (lista final,
  máquina de transições, tabela de tradução, recorte) e **para** para ratificação do dono;
  `T23`..`T26` conformam famílias disjuntas de artefatos vivos; a `T27` conforma kanban e planos
  vivos e faz a varredura de fecho. `### T19`, `### T20` e `### T21` **não foram reescritos** —
  ficam marcados como *pendentes de reescrita* no §4, com o motivo registrado. Achado medido fora de
  escopo: as ocorrências de `parcial` em `.claude/tools/review_evidence.py` são **veredito de
  rubrica**, não `status` de tarefa — a contagem bruta de ocorrências superestima a conformidade, e
  os três vocabulários (status, veredito, homônimo) estão separados no §10.2.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T22` — avaliação da lista de estados e fechamento da linguagem ubíqua — `done`; `DP-F`
  ratificada pelo dono em 2026-08-11, sem reserva.** `### DP-F` escrita em `docs/plans/P-0734-execucao-autonoma.md`
  (L1401-1560), logo após a `DP-C`; nenhum outro arquivo tocado, nenhum artefato conformado.
  **Veredito global: a lista dos sete é suficiente** — `triage`, `ready`, `blocked`, `in-progress`,
  `review`, `done` e `cancelled` têm consequência operacional observável, nenhum é exagero, nenhuma
  transição observada ficou sem nome e nenhum estado novo entra; `triage` nomeia uma insuficiência
  real (linha de `_INBOX.md` ainda não `[drenado]` não é escolhível e é avaliada, não delegada). As
  duas correções são de **grafia** e de **alcance**: `backlog` deixa de ser status e passa a nomear só
  o conjunto elegível, e `superseded` fica **fora** do vocabulário de tarefa (é exclusivo de
  plano/iniciativa; tarefa obsoleta é `cancelled`). Alcance decidido: a lista governa **todo item do
  kanban**, porque a coluna `Status` do índice é uma só e o `proximo-passo` lê essa mesma coluna, com
  tabela de aplicabilidade por objeto e residência única em `.claude/skills/diario-de-obras/SKILL.md`.
  Máquina de transições fechada com `done`/`cancelled` terminais (retrabalho vira item novo) e só as
  duas transições da `DP-E` disparando ação — `in-progress`→`review` invoca o revisor,
  `review`→`done` escreve o RDO. Tabela de tradução sem termo órfão: `entregue` e `bloqueado` morrem,
  `parcial` morre **como status** e sobrevive como veredito de rubrica. Uma correção de recorte no
  item 7: `docs/RDO/P-0734-T11-skill-scrum-master-o-loop.md` sai dos arquivos-alvo da `T27` (RDO
  emitido é registro histórico) e vira sobrevivente justificado na varredura de fecho.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T23a` — residência única do vocabulário de status no `diario-de-obras` — `done`.** A `T23`
  publicada foi **partida em `T23a`/`T23b` pelo orquestrador**, por orçamento: a contagem de
  write-clusters da tarefa inteira ficou em ~15-16, acima da linha de 8 do item 5 do gate de
  delegação; o corte é por arquivo, sem alterar nada do dossiê original. Arquivo único
  `.claude/skills/diario-de-obras/SKILL.md`: o bullet **Status válidos** virou ponteiro de duas
  linhas para a seção nova **`## Status — residência única`**, que enuncia uma única vez a lista
  final dos sete estados, a máquina de transições com os três fechamentos e a tabela de alcance por
  objeto — mais o enunciado de que o `status` é escrito exclusivamente pelo `scrum-master`. No resto
  do arquivo, só as ocorrências de tipo (i) foram traduzidas (exemplo de índice, heurística da
  diretiva de priorização, operação "Registrar plano", gatilho (c) de condensação, regra de
  convergência); prosa e homônimos ficaram intactos por classificação. Aceite re-derivado:
  `in progress|in review` de **4 → 0**; `backlog` de **8 → 3**, as três sobreviventes como
  substantivo (o conjunto), nenhuma como status. Bateria do §3 rodada pelo orquestrador no fecho —
  os quatro em exit 0, suíte em 29 passed. Achado registrado no `## Achados da execução` do plano e
  aberto como `TK-30`. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T23b` — conformidade do `proximo-passo` com a residência única — `blocked`.** **Razão do
  bloqueio (2026-08-11, decisão do dono):** o entregável existe e foi verificado, mas **não há quem
  conclua a tarefa** — a transição `review` → `done` é escrita só pelo `scrum-master`, e a skill na
  forma reescrita só passa a existir depois de `T19`/`T20`/`T21`. O executor escreve `review` e
  `blocked` e nunca `done` (captura em `docs/plans/P-0734-execucao-autonoma.md` §11, insumo ainda não
  fechado como `DP-G`). Destrava quando o loop existir. Arquivo único
  `.claude/skills/proximo-passo/SKILL.md`, cinco write-clusters. A skill que **consome** o kanban
  ganhou um parágrafo de abertura (`:15-19`) declarando que ela não define estado nenhum e apontando
  para a residência (`diario-de-obras`, `## Status — residência única`) — ponteiro, sem recopiar
  lista, máquina nem tabela de alcance. Traduzidas só as ocorrências de tipo (i) da `DP-F`: heurística
  de priorização (`:36`, `:39`, `:41-42`, `:44`), retomada de sprint (`:52`), guardrail de convergência
  (`:172`) e guardrail de diário vazio (`:182`) — `in progress`→`in-progress`, `backlog` (status)→
  `ready`. Nenhuma regra de escolha mudou de efeito: mesma ordem da heurística, mesmos filtros, mesmas
  proibições. No guardrail de `superseded` (`:167-168`) entrou o item 4 da `DP-F`: `superseded` é
  vocabulário de **plano/iniciativa**, não existe tarefa `superseded`. Tipo (ii)/(iii) intactos por
  classificação — `PARCIAL` de rubrica, `bloqueado` em prosa, `<done>/<total>` de contagem e as cinco
  ocorrências de `backlog` como substantivo (título, description, retomada, "próxima tarefa do
  backlog", "fora do backlog"). Aceite re-derivado no fecho: `in progress|in review` de **6 → 0**
  (grep vazio); `backlog` de **9 → 5**, todas substantivo. Bateria do §3:
  `check-readme.ps1`, `dead_code.py`, `kit_check.ps1`, `ratchet_piso.py` em **exit 0** e
  `python -m pytest tests -q` em **29 passed** (piso mantido, 29 × 29). Nenhum achado fora de escopo.
  Consumo: ver `docs/telemetria.tsv`.

**Fila reordenada em 2026-08-11 (decisão do dono).** A ordem anterior mandava `T24`..`T27` antes da
reescrita de `T19`/`T20`/`T21`; como nenhuma tarefa pode ser concluída antes de o loop existir, as
tarefas de conformidade passam a **suceder** o loop.

- **Replanejamento `DP-G` — a fronteira de escrita do `status` — `done`; ratificada pelo dono em
  2026-08-11, sem reserva** (rodada de planejamento, não é tarefa do plano). A captura do §11 virou
  decisão. **Fronteira fechada em dois atos que o texto vigente tratava como um só:** *autoria*
  (quem determina o valor) é do executor para `review` e `blocked`, e do `scrum-master` para todo o
  resto; *materialização* (gravar onde o kanban registra) é **exclusivamente** do `scrum-master`,
  que transcreve os dois valores do executor sem discricionariedade. A leitura literal — executor
  grava o kanban — foi **recusada por medida**: não existe hoje campo material de `status` por tarefa
  de plano (o índice só tem linha para iniciativa, plano e tíquete; a tarefa vive no bullet de
  fechamento e na ordem do §5), criá-lo é artefato novo e poria dois escritores no mesmo arquivo.
  **`E2` fechada no candidato (a)** — o `blocked` do executor é canal único com **razão tipada**:
  `motivo=dependencia` faz o `scrum-master` reordenar a fila e **seguir**; `motivo=premissa` faz
  **parar** e escalar; na dúvida, `premissa`. O previsível continua carregado pela ordem do §5, e
  nenhum campo novo entra na `DP-C`. Recusados (b) — vocabulário de retorno disjunto do `status` — e
  (c) sozinho, que não cobre dependência **descoberta em execução**, o caso do enunciado 4.
  **Consequência nas tabelas:** `A3` parte em `A3a`/`A3b` pela razão tipada, e `A5` **cai** (`parcial`
  morreu como status; entrega incompleta é veredito do revisor). Gramática de retorno nova:
  `<tarefa> review [pendencia=…]` ou `<tarefa> blocked motivo=<dependencia|premissa> …`.
  **`E1` virou a `T28`** (sanitização das quatro superfícies que afirmam o absoluto: §10.2, `DP-F`
  itens 2 e 3, e a residência única). **Três dossiês reescritos:** a `T19` perde `laudo --status` e
  encolhe `calcular_desdobramento` para `(veredito, orcamento_estourado)` — derivado de a `DP-F`
  fixar o RDO numa transição só, o que torna `bloqueado`/`reprovado` inalcançáveis e fecha o `TK-29`;
  a `T20` perde a declaração de `status` pelo revisor; a `T21` foi **partida em `T21a`/`T21b`** por
  volume (~9 write-clusters). Fila final: `T28` → `T19` → `T20` → `T21a` → `T21b` → `T23b` →
  `T24`..`T27`. Bateria do §3 no fecho: `check-readme.ps1`, `dead_code.py`, `kit_check.ps1`,
  `ratchet_piso.py` em **exit 0** e `python -m pytest tests -q` em **29 passed** (piso mantido).
  Consumo: ver `docs/telemetria.tsv`.

- **Duas questões operacionais fechadas por delegação do dono, na mesma rodada — `done`.**
  (1) **Teto da rodada de replanejamento:** `GOVERNANCA.md` §3 passa a reconhecer o caso — fechar a
  decisão e reescrever no mesmo contexto os dossiês que ela invalida — com teto **≤50**, dentro da
  classe de redação/planejamento, sem classe nova (a `DP-C` mantém os cinco slugs). Calibrado pela
  série medida dessas rodadas (19, 21, 39, 43, 48), três das cinco acima de ≤30; dividi-las entre
  contextos obrigaria a repagar a leitura da decisão em cada fatia. Espelhado no `README.md`,
  inclusive no gatilho de checkpoint por dois terços, e registrado no `CHANGELOG.md`.
  (2) **`TK-26`:** o ponto aberto foi fechado — célula vazia aceita nas três colunas numéricas
  **sempre que `fonte` ≠ `usage`**; a execução em `telemetria.py` segue pendente de tarefa própria.
  Bateria do §3 no fecho: `check-readme.ps1`, `kit_check.ps1`, `dead_code.py` em **exit 0** e
  `pytest tests -q` em **29 passed**. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T28` — sanitização do texto vigente contra a `DP-G` — `done`.** As quatro superfícies que
  afirmavam o absoluto passaram a separar **autoria** de **materialização**, cada uma com ponteiro
  para a `DP-G`: `§10.2` enunciado 2 e `DP-F` itens 2 e 3 no plano, e a residência única em
  `.claude/skills/diario-de-obras/SKILL.md`. **Cinco edições, não quatro:** a residência única
  carrega duas frases da mesma superfície — a linha *Escritor* e a abertura da máquina de transições,
  cópia normativa da frase que a edição 3 corrige no plano —, e sem a segunda a residência
  continuaria enunciando para o kit inteiro o absoluto que a `DP-G` derrubou. O aceite literal do
  dossiê (Grep vazio no plano) foi **escopado pelo orquestrador antes da delegação**: o plano cita o
  texto antigo por desenho na tabela da própria `DP-G`, no insumo `§11.2`/`§11.4` e no dossiê da
  `T28`, e os invariantes proíbem tocá-las — o critério passou a ser "nenhuma ocorrência
  **afirmativa** sobrevive". Tabelas de estados, de transições, de alcance por objeto e de tradução
  intocadas; `DP-G` na skill saiu de 0 para 2 ocorrências. Achado tiquetado, não corrigido: `TK-31`.
  Bateria do §3 no fecho: `check-readme.ps1`, `dead_code.py`, `kit_check.ps1`, `ratchet_piso.py` em
  **exit 0** e `python -m pytest tests -q` em **29 passed**. Orçamento **estourado**: 21 tool uses
  contra teto 15 da classe `redacao` — a fatia extra veio da edição 5 e da verificação escopada, que
  não estavam no volume medido quando a classe foi atribuída. Consumo: ver `docs/telemetria.tsv`.

- **Insumo do dono registrado — a fronteira conceito × desenvolvimento (`§12` do plano).** O
  levantamento de contradições aberto pelo fechamento da `T28` foi respondido com uma distinção que
  reclassifica os seis pontos: **conceito do framework** (o que ele é, reside nos artefatos
  publicados) × **desenvolvimento do framework** (como está sendo construído, reside no plano). A
  regra de recência — o último entendimento do autor é canônico e reescreve o que contradiz — é de
  **desenvolvimento** e **não** entra em artefato publicado; o critério de desempate do framework em
  si não foi decidido. O RDO fica fora da conciliação, por ter mecânica própria. Entendimentos
  canônicos confirmados: o **laudo** é emitido pelo reviewer, consumido e **descartado** pelo
  `scrum-master` (fonte de poluição de contexto), vivendo só como argumento do desdobramento; o
  **pacote** é o conjunto de informações obrigatórias **dentro do laudo**, suficientes para invocar o
  script de RDO sem falha; **`reviewer`** é o nome canônico. A definição do artefato **tarefa** —
  documento com vários autores (`scrum-master`, executor, reviewer), principal canal de comunicação
  entre as partes — sai de remendo e vira tarefa própria. Registrado como insumo, sem derivação:
  nenhuma tarefa foi autorada e nenhum dossiê reescrito nesta rodada.

- **Rodada de replanejamento — `DP-H` fechada e o `§12` consumido — `done`.** A fronteira conceito ×
  desenvolvimento virou decision record (`§13` do plano) por **derivação**, sem decisão nova: recência
  é regra de **desenvolvimento** e não entra em artefato publicado; dossiê de tarefa executada é
  **orientação** e se concilia, enquanto o que narra o ocorrido permanece intocado; o laudo é
  consumido e **descartado**; o `pacote` existe **dentro do laudo**, com suficiência declarada; o
  RDO fica fora. Consequência material nos dossiês: a `T19` perde a leitura do laudo — o `close`
  recebe os cinco campos do `pacote` por argumento, `--laudos-dir` sai da CLI e o template perde o
  ponteiro `{{LAUDO_PATH}}` —, a `T20` deixa de tratar `pacote` como objeto morto, a `T21a` ganha a
  extração do `pacote` e o **apagamento** do laudo no passo 9, a `T21b` para de repassar o caminho do
  laudo na reexecução, os achados do `§9` trocam *inspetor* por `reviewer` e param de enunciar "o
  critério não é recência", e a `T26` perde o absoluto de escritor único e passa a depender da
  `DP-I`. **Três cards novos:** `T29` (artefato **tarefa** → `DP-I`), `T30` (**utilidade** → `DP-J`)
  e `T31` (resíduo de `pacote de retorno` em `GOVERNANCA.md`, na rubrica e na residência única, que
  estava sem cobertura). `T29` e `T30` decidem e **param** para ratificação em lote — quinto
  round-trip do dono, e único ponto de parada dura da fila. `TK-31` fechado por conciliação no
  dossiê da `T23a`. Fila: `T19` → `T20` → `T31` → `T21a` → `T21b` → `T23b` → `T24` → `T25` → `T29` →
  `T30` → [ratificação] → `T26` → `T27`. Bateria do §3 **não executada** nesta rodada: o contexto de
  planejamento não dispõe de ferramenta de execução e o diff ficou restrito a `docs/` (plano e
  diário), sem tocar código, teste ou kit executável — a bateria volta no fecho da `T19`.
  Consumo: ver `docs/telemetria.tsv`.

- **Rodada de replanejamento — `DP-K` fechada: os quatro artefatos e o desempate do framework —
  `done`.** Os três pontos que a `DP-H` devolveu voltaram respondidos pelo dono e foram **registrados
  e derivados na mesma passagem** (`§14` do plano). **(1) Desempate do framework:** ambiguidade
  **escala ao dono** — o buraco que o `§12.1` e a `DP-H` declaravam explicitamente não decidido. É
  **conceito**, então ganha residência em artefato publicado: entra como **terceira regra de
  precedência** no `GOVERNANCA.md` **§3.1**, que já é a superfície que decide colisão de doutrina —
  sem seção nova, e sem que a recência (regra de desenvolvimento) vire desempate publicado. Nenhuma
  tarefa viva cobria a gravação: card **`T32`**. **(2) `reviewer` é termo único** e abole também a
  forma portuguesa *revisor*, que a `DP-H` deixara livre. Volume medido no texto vivo: **18
  ocorrências em 5 arquivos** — 11 no corpo do `SKILL.md` do `scrum-master`, que a `T21a` (7) e a
  `T21b` (4) **já reescrevem**, a custo marginal zero; as **6** restantes são linhas espelhadas
  (`description` da skill e do agente, com os espelhos em `README.md` e `.claude/README.md`) mais a
  prosa do agente e uma docstring de teste. A `T31` **não** absorveu: com 9 ocorrências em 3 arquivos
  sob teto 15, o volume medido estoura — card **`T33`**, depois da `T21b`. Registro (diário,
  histórico, RDO, telemetria) intocado; o *Revisor* do OpenSpec no benchmark é papel externo e fica.
  **(3) Hierarquia dos quatro artefatos canônicos:** plano (objetivo materializado, antecede todas as
  tarefas), tarefa (escopo localizado do plano, comunicação **entre os agentes**, verdade da tarefa em
  execução), laudo (revisão realizada, **efêmero**, move para `done` ou devolve para `in-progress`) e
  RDO (comunicação com o **dono**, verdade da entrega, pressupõe tarefa finalizada) — **nenhum
  substitui o outro**. Medido contra o texto vigente: a efemeridade **confirma** a `DP-F` e não abre
  aresta na máquina (o `review` → `blocked` da escalada não é contradito — é a mesma rota que o ponto
  1 acabou de ratificar), "em execução" lê-se *tarefa não terminal* e nenhuma grafia muda, a `DP-G`
  fica intocada (recomendar não é autorar `status`) e a `T19` é **compatível** — `close` sem leitura
  de laudo, template sem `{{LAUDO_PATH}}`. **Uma aresta real:** o laudo morre em **qualquer**
  desdobramento, e não só no fechamento — a `T21b` ganha o descarte nos ramos `A6`/`A7`/`B1` e a `T30`
  ganha o piso dos três ramos. A **`T29` foi reescrita**: sai o ramo de escalada obrigatória por
  residência (o dono já respondeu que a tarefa não substitui nada), entra a hierarquia como insumo
  fechado, e **três das cinco perguntas viram transcrição** — sobram duas a decidir (autores/escrita e
  conteúdo obrigatório, com o lugar material do `status`), que é onde a `DP-I` passa a parar. Fila:
  `T19` → `T20` → `T31` → `T32` → `T21a` → `T21b` → `T33` → `T23b` → `T24` → `T25` → `T29` → `T30` →
  [ratificação] → `T26` → `T27`. Bateria do §3 **não executada**: ato de planejamento, diff restrito a
  `docs/` (plano e diário), sem tocar código, teste ou kit executável — a bateria volta no fecho da
  `T19`. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T31` — conformidade: o resíduo de `pacote de retorno` nos artefatos publicados** (`done`).
  O objeto morto saiu do texto vigente dos três artefatos publicados. `GOVERNANCA.md` §3, linha
  *Orquestração* da matriz de responsabilidades: a orquestração passa a rotear **a linha de retorno
  do executor** e **o laudo do `reviewer`**, com o roteamento em si (aprovado segue, reprovado volta
  ao mesmo escopo, escalado sobe ao dono) inalterado. `docs/RUBRICA_DE_REVISAO.md`, 6 ocorrências:
  as fontes de evidência de `criterio-de-pronto`, `escopo`, `rota`, `residuo` e `registro` passam a
  citar **o dossiê de evidência e o diff**, onde a `D2` realocou arquivos tocados, desvios e
  verificação; e a pendência de arquitetura ou requisito sobe ao dono pelo `--escalar` do laudo.
  `.claude/skills/diario-de-obras/SKILL.md`, 2 ocorrências: o estado `review` e a transição
  `in-progress` → `review` passam a dizer que o executor devolve **a linha de retorno da `DP-G`**.
  Nenhuma regra mudou de efeito — só o objeto citado: pesos, faixas e dimensões da rubrica, lista de
  estados, máquina de transições e alcance por objeto ficaram intocados, e nada novo foi enunciado.
  Onde a leitura ficaria ambígua com dois "dossiês" na mesma frase, o da tarefa passou a aparecer
  qualificado (`dossiê da tarefa`). Tarefa de redação de doutrina, sem TF/TR de código; sem achado
  fora de escopo. Verificação: as 9 ocorrências foram substituídas por `Edit`s de âncora exata sobre
  o texto colado no dossiê, todos aceitos. O executor atingiu o teto rígido de 15 tool uses no
  fechamento e deixou a conferência pendente; ela foi **executada pelo orquestrador na mesma
  rodada**: Grep por `pacote` nos três arquivos com resultado **vazio** nos três (0 ocorrências —
  nenhum sobrevivente a justificar, nem na acepção da `DP-H` item 4), e bateria do §3 verde —
  `kit_check.ps1 -Mode validate` exit 0 (8 agentes, 11 skills, VERSION == KIT_VERSION `0.0.0`),
  `check-readme.ps1` exit 0 (14 guardrails, 14 seções com Fonte da verdade), `dead_code.py` exit 0
  (0 achados) e `python -m pytest -q` com 39 passed. Achado de calibração levantado pelo executor:
  a classe `redacao` com 9 pontos de edição em 3 arquivos não cabe em 15 tool uses somando coleta,
  registro no diário e verificação — piso realista ~18-20, ou a verificação sai do teto do
  executor. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T32` — doutrina: o desempate do framework escala ao dono** (`done` — materializado pelo
  orquestrador: este plano não executa o loop que projeta, §3 item 1, então `review` não tem
  reviewer a invocar e a bateria de fechamento abaixo é o que fecha). O buraco que o
  `§12.1` e a `DP-H` declararam não decidido — o critério de desempate do framework em si — ganhou
  residência publicada. `GOVERNANCA.md:198-204`, §3.1, bloco *Precedência, quando duas superfícies
  colidem*: entra a **regra 3 — "Sem desempate → escala ao dono"**, depois de *Empate → versionado
  vence não-versionado*. Enuncia que, exauridas as regras 1 e 2, a ambiguidade não se resolve
  embaixo (nenhum agente arbitra por palpite, antiguidade ou recência), que o desempate do framework
  é o dono, que a regra de recência governa o desenvolvimento do framework dentro dos planos e **não
  é critério de desempate de doutrina publicada** (`DP-H` item 2), e que escalar é parar e perguntar
  — a mesma rota que a Regra 8 do `~/.claude/CLAUDE.md` dá ao executor. Invariantes respeitados:
  nenhuma seção nova, teste de residência das quatro perguntas intocado, regras 1 e 2 intocadas,
  parágrafo *Colisão não se resolve com as duas cópias vivas…* no lugar (`GOVERNANCA.md:205-206`).
  Nada da mecânica do `P-0734` (laudo, RDO, `status`, `pacote`) entrou no texto, e as âncoras da
  `T31` e da `T26` não foram tocadas — um único `Edit`, um único bloco. Tarefa de redação de
  doutrina, sem TF/TR de código; sem achado fora de escopo. Verificação colada do terminal:
  `kit_check.ps1 -Mode validate` → *OK - 8 agente(s) e 11 skill(s) validados; VERSION == KIT_VERSION
  ('0.0.0')* (exit 0); `check-readme.ps1` → *OK - 8 agente(s), 11 skill(s), 14 guardrail(s), versão
  '0.0.0', 14 seção(ões) com Fonte da verdade válida* (exit 0); `dead_code.py` → *OK - 0 achado(s)*
  (exit 0); `python -m pytest -q tests` → **39 passed** (piso anterior 39, mantido). Grep de aceite
  em `GOVERNANCA.md`: o bloco de precedência tem **três** regras numeradas (linhas 191, 194, 198) e
  a regra 3 contém `escala ao dono`. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T21a` — skill `scrum-master`: os passos do loop — `done`.** Os passos foram alinhados
  ao fluxo ratificado e o loop deixou de parar no passo 9. `## Estado do loop`: além dos três
  contadores da `DP-B`, o loop passa a guardar a **fila corrente e a ordem dela**, porque `A3a` a
  reordena em execução — nada mais entra. **Passo 2** lê a fila corrente (reordenada, se `A3a` já
  agiu na janela) e não o §5 do plano. **Passo 3** ganha a materialização `ready` → `in-progress`
  antes de delegar (`DP-G` item 1, consequência 3). **Passo 4** instrui o executor a devolver uma
  das duas linhas do domínio fechado (`<tarefa> review [pendencia=…]` \| `<tarefa> blocked
  motivo=<dependencia|premissa> …`) e declara o desempate `premissa`; sai a instrução de `rdo.py
  new`. **Passo 5** (agora *Recepção do retorno do executor*) materializa o valor devolvido sem
  discricionariedade, tipifica **retorno inválido** → `A2` e ancora os `tools` no bloco `<usage>`.
  **Passo 6** (agora *Despacho do `reviewer`*) é o **gatilho 1** da `DP-E`, recebe o mesmo dossiê do
  executor + o dossiê de evidência, sem caminho de RDO, e `blocked` não passa por ele (`DP-G` item
  4). **Passo 9** é o **gatilho 2**: uma chamada de `rdo.py close` com o consumo medido e o
  **pacote** do laudo (`--veredito --percentual --bloqueante --recomendacao --pendencia-laudo`,
  `DP-H` item 4), laudo **apagado** depois de consumido (`DP-H` item 3), `cancelled`/`blocked` sem
  RDO (`DP-F` item 3, fechamento (c)); o bloco *Ponto aberto* saiu. Sete ocorrências de *revisor*
  nas seções tocadas viraram `reviewer` (`DP-K` §14.2 item 2); as cinco fora de escopo (`:3` da
  `T33`; tabelas e proibições da `T21b`) ficaram intactas. Passos 1, 7, 8 e 10 e as seções de
  tabelas/relatório/proibições/guardrails não foram tocados, salvo a troca de termo no gatilho do
  passo 7, que o dossiê enumera. Tarefa de redação, sem TF/TR de código; sem achado fora de escopo.
  Verificação colada do terminal: `kit_check.ps1 -Mode validate` → *OK - 8 agente(s) e 11 skill(s)
  validados; VERSION == KIT_VERSION ('0.0.0')* (exit 0); `kit_check.ps1 -Mode check-drift` → *OK -
  .claude/README.md == regenerado (8 agente(s), 11 skill(s))* (exit 0); `check-readme.ps1` → *OK - 8
  agente(s), 11 skill(s), 14 guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade
  válida* (exit 0); `python -m pytest` → **39 passed in 5.40s** (piso anterior 39, mantido). Grep de
  aceite em `.claude/skills/scrum-master/SKILL.md`: `pacote de retorno` → **0 ocorrências**;
  `rdo.py new` → 0; `Ponto aberto` → 0. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T21b` — skill `scrum-master`: tabelas de roteamento e vocabulário — `done`.** As duas
  tabelas passaram a refletir o estado ratificado. **Bloco A:** `A3` foi **partida** pela razão
  tipada — `A3a` (`motivo=dependencia`) reordena a fila para que a bloqueada suceda a que a bloqueia,
  materializa `blocked` com a razão, **não** despacha o `reviewer`, **não** escreve RDO, **não**
  consome retentativa, **não** incrementa o contador de tarefas fechadas e **segue**; `A3b`
  (`motivo=premissa`) materializa `blocked` e **PARA**, escalada ao dono (`DP-G` item 4). `A5`
  **saiu** da tabela (a numeração salta de `A4` para `A6`): `parcial` morreu como `status` e entrega
  incompleta é veredito do `reviewer`. `A4` passou a ler os `tools` do bloco `<usage>`; `A6`, `A8` e
  `A9` passaram a ler a **recomendação** do laudo (`refazer` / `seguir com ressalva` / `seguir`) em
  vez de derivar o desdobramento do veredito, e `A6` passou a despachar um executor **novo em
  contexto novo** com o dossiê original mais as **diretivas atualizadas**, **nunca** o caminho do
  laudo (`DP-H` item 3, `D6` reconciliado). `A1`, `A2` e `A7` ficaram intactos, e a precedência "a
  primeira que casa vence" permanece. **Bloco B:** `B1` passou a ler `pendencia=` do retorno do
  executor ou `recomendacao=escalar` do laudo; `B2`..`B4` e os três tetos da `DP-B` intactos.
  **Descarte do laudo em qualquer ramo** (`DP-K` §14.4): parágrafo próprio abaixo da tabela A —
  extraída a recomendação, o laudo é apagado na reexecução (`A6`), no fechamento (`A7`..`A9`, passo
  9) e na escalada (`B1`); nenhuma linha de tabela guarda ponteiro para ele. O bloco *O que obriga
  parada* deixou de citar os campos do pacote morto e passou a citar os canais vivos. A fonte
  normativa da seção ganhou `DP-G` item 4 e `DP-K` §14.4 ao lado de `DP-A`/`DP-B`, para que
  "divergência resolve a favor da seção" aponte para o texto ratificado. **Vocabulário:** só
  ocorrência de tipo (i) foi traduzida — `status=bloqueado` → `status=blocked` nas linhas do `A3`;
  `parcial` sobreviveu apenas onde não é `status` (`:214`, marcador literal `PARCIAL — trecho
  pré-queda não medido` do `A1`) e `bloqueado` apenas em prosa corrente (`:269`); `revisor` →
  `reviewer` no corpo (linhas do `A3`/`A4`/`A5` e a proibição *Não julga entrega*), com a
  `description` do frontmatter (`:3`) **intocada**, que é da `T33`. O frontmatter não foi editado, o
  `## Relatório de encerramento` e o `## Guardrails` não tinham termo morto nem citação do pacote e
  ficaram inalterados, e os passos entregues pela `T21a` não foram reabertos. Tarefa de redação, sem
  TF/TR de código. **Percurso a seco** (nenhum comando executado), sobre a `EXA-T32`, já fechada:
  passo 2 toma a tarefa da fila → passo 3 materializa `ready` → `in-progress` → passo 4 despacha o
  executor com o dossiê e o modelo do cabeçalho → passo 5 recebe `EXA-T32 review` (sem `pendencia=`)
  e lê os `tools` do `<usage>` → passo 6 (gatilho 1) despacha o `reviewer` → passo 7 lê `aprovado …
  bloqueante=nenhuma` + `laudo=<caminho>` → passo 8, bloco A por precedência: `A1` não (há
  `<usage>`), `A2` não (linha válida), `A3a`/`A3b` não (`status=review`), `A4` não (dentro do teto),
  `A6` não (`recomendacao=seguir`, não `refazer`), `A7` não, `A8` não, **`A9` casa** → fecha o RDO
  como `aprovado` e segue → passo 9 escreve o RDO por uma chamada de `rdo.py close`, **apaga o
  laudo** e apenda a telemetria → passo 10, bloco B: `B1` não (sem `pendencia=` e sem `escalar`),
  `B2` não (contadores abaixo dos tetos), `B3` conforme os gates da próxima, **`B4` casa** → despacha
  a próxima. Nenhuma célula do percurso exigiu juízo sobre prosa. Achado fora de escopo tiquetado,
  não corrigido: **`TK-33`** (três referências órfãs em passos e proibições que nem a `T21a` nem a
  `T21b` podiam tocar). Verificação colada do terminal: `kit_check.ps1 -Mode validate` → *OK - 8
  agente(s) e 11 skill(s) validados; VERSION == KIT_VERSION ('0.0.0')* (exit 0); `kit_check.ps1
  -Mode check-drift` → *OK - .claude/README.md == regenerado (8 agente(s), 11 skill(s))* (exit 0);
  `check-readme.ps1` → *OK - 8 agente(s), 11 skill(s), 14 guardrail(s), versão '0.0.0', 14 seção(ões)
  com Fonte da verdade válida* (exit 0); `python -m pytest` → **39 passed in 6.14s** (piso anterior
  39, mantido). Grep de aceite em `.claude/skills/scrum-master/SKILL.md`: `revisor`
  (case-insensitive) → **1 ocorrência**, `:3`, a `description` do frontmatter, que é da `T33`;
  `pacote de retorno` → **0**; `in progress|in review` → **0**; `backlog`/`entregue` como `status` →
  **0**. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T33` — Conformidade: `reviewer` nas linhas espelhadas e no resíduo fora do loop —
  `done`.** `reviewer` passa a ser o **termo único** do papel no texto vivo do kit e nos artefatos
  publicados (`DP-K` §14.2 item 2). Sete ocorrências em cinco arquivos, todas substituição
  **palavra por palavra** (`revisor`/`Revisor` → `reviewer`/`Reviewer`), sem enunciar regra nova e
  sem tocar campo, tabela, peso ou passo: os dois pares espelhados mudaram **no mesmo ato** e com
  texto idêntico caractere a caractere — `.claude/skills/scrum-master/SKILL.md:3` ↔
  `.claude/README.md:57` (`description` da skill) e `.claude/agents/pantonic-reviewer.md:3` ↔
  `.claude/README.md:19` (`description` do agente) —, mais a prosa de abertura do agente (`:8`,
  "Você é o **reviewer**"), a paráfrase da tabela do espelho em `README.md:755` (não é cópia
  verbatim da `description`: trocada só a palavra, frase preservada) e a docstring de
  `tests/test_rdo.py:122` (**só a palavra**; nenhuma asserção, nenhum comportamento). `model:` e
  `tools:` do frontmatter do `pantonic-reviewer` ficaram intocados (`TK-27`). Registro histórico
  (`docs/DIARIO_HISTORICO.md`, `docs/RDO/`, `docs/telemetria.tsv`), `docs/plans/**` e o *Revisor*
  do OpenSpec em `docs/benchmark/BM-03-fission-ai-openspec.md:26` (papel de framework externo)
  ficaram como estavam. Dois desvios do dossiê verificados na entrada e sem efeito no escopo: o
  corpo do `SKILL.md` do `scrum-master` já estava limpo pela `T21a`/`T21b` (sobrava só o
  frontmatter) e a ocorrência de `tests/test_rdo.py` migrou de `:186` para `:122` na reescrita da
  `T19`. Tarefa de redação, sem TF/TR de código. Verificação colada do terminal:
  `kit_check.ps1 -Mode validate` → *OK - 8 agente(s) e 11 skill(s) validados; VERSION == KIT_VERSION
  ('0.0.0')* (exit 0); `kit_check.ps1 -Mode check-drift` → *OK - .claude/README.md == regenerado
  (8 agente(s), 11 skill(s))* (exit 0); `check-readme.ps1` → *OK - 8 agente(s), 11 skill(s), 14
  guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade válida* (exit 0) — prova da
  paridade dos espelhos; `dead_code.py` → *OK - 0 achado(s)* (exit 0); `python -m pytest` →
  **39 passed in 8.57s** (piso anterior 39, mantido). Grep de aceite case-insensitive por `revisor`
  em `.claude/`, `README.md` e `tests/` → **0 ocorrências** nos três.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T35` — Auditoria: a matriz de responsabilidades como autoridade exaustiva — `done`.**
  Precondição da `T36` cumprida: a matriz de `GOVERNANCA.md` §3 foi medida papel vivo por papel
  vivo e fechada por **transcrição**. Universo medido: os **oito** agentes de `.claude/agents/`
  (o diretório inteiro) mais o `scrum-master`, único papel que vive numa skill. Seis agentes já
  estavam cobertos (`planner`→Planejamento, `executor`→Execução, `reviewer`→Revisão,
  `scout`→Coleta, `auditor-arch` e `auditor-cleancode` → a linha *Auditoria*, que nomeia os dois)
  e o `scrum-master` entrou pela linha *Orquestração* que já existia — papel em skill não vira
  linha nova. **Duas lacunas, ambas do tipo (a) transcrição, ambas fechadas:** `pantonic-fora-da-caixa`
  → linha **Redesenho** (Opus, do frontmatter) e `pantonic-benchmarker` → linha **Benchmarking**
  (Haiku, do frontmatter); as quatro células saíram do que o próprio prompt já publica (`## Por que
  você existe` e `## Método por alvo`; `## Guardrails do coletor` e o esquema `D1..D16`). **Nenhuma
  lacuna (b)** — nenhuma responsabilidade existia sem estar publicada, logo **nenhum tíquete novo** e
  nada a subir ao dono. Invariantes respeitados: nenhuma responsabilidade criada, nenhuma proibição
  nova na coluna *Não faz* das sete linhas preexistentes, nenhuma proibição podada (é a `T37`),
  guardrail 15 não escrito (é a `T36`), `README.md`, `.claude/**` e `docs/RDO/**` intocados. A
  medida completa, com veredito por arquivo, ficou em `docs/plans/P-0734-execucao-autonoma.md`
  `### 16.7`. Tarefa de auditoria/redação, sem TF/TR de código. Contagem da matriz re-derivada
  (Grep `^\|\s\*\*`, 11 matches no arquivo − 2 da tabela de residência do §1): **7 linhas antes,
  9 depois**. Verificação colada do terminal: `kit_check.ps1 -Mode validate` → *OK - 8 agente(s) e
  11 skill(s) validados; VERSION == KIT_VERSION ('0.0.0')* (exit 0); `kit_check.ps1 -Mode
  check-drift` → *OK - .claude/README.md == regenerado (8 agente(s), 11 skill(s))* (exit 0);
  `check-readme.ps1` → *OK - 8 agente(s), 11 skill(s), 14 guardrail(s), versão '0.0.0', 14
  seção(ões) com Fonte da verdade válida* (exit 0) — 14 guardrails inalterados, prova de que o
  guardrail 15 não foi antecipado; `dead_code.py` → *OK - 0 achado(s)* (exit 0); `python -m pytest`
  → **39 passed in 3.90s** (piso anterior 39, mantido).
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T36` — Doutrina: guardrail 15 (`G-SCOPE`) e o espelho em lockstep — `done`.** A golden
  rule de escopo de agente passa a existir na doutrina publicada: `GOVERNANCA.md` §7 ganha o **item
  15** (`G-SCOPE` — o agente se atém estritamente às responsabilidades declaradas; o que não está
  escrito é proibido), inserido entre o item 14 e o parágrafo "Esses guardrails são materializados
  em cada projeto como:", com a **matriz de responsabilidades do §3 nomeada como autoridade
  exaustiva**, a proibição de prompt criar responsabilidade por conta própria, o critério que poda
  proibição redundante (só se justifica a que restringe o exercício da **própria** responsabilidade
  declarada) e o *Enforcement* em instrução de agente/skill + gate de review sobre prompt novo ou
  alterado. O bullet "**Papéis não são intercambiáveis**" do §3 passa a **apontar** para o §7 item
  15 sem reenunciar a regra. Espelho subiu **no mesmo ato**: `README.md` §10 ganha a linha `| 15 |`
  e o numeral de abertura vira "**Quinze** regras mínimas obrigatórias". Nenhum dos 14 itens
  vigentes foi reescrito; nenhuma regra nasceu no README; nenhum prompt de agente ou skill foi
  tocado (é a `T37`); `docs/RESIDENCIA_DOUTRINA.md` intocado; sem bump de `VERSION` nem de
  `.claude/KIT_VERSION` (congelamento do §10 em vigor). **Achado — prosa de contagem do README
  (`:710`) estava divergente da tabela:** o texto vigente dizia "**Seis** … **seis**", mas a
  recontagem das três famílias **sobre a tabela** dá, com 14 linhas, **7** por teste executável
  (1–6 e 8) e **7** por gate de review/instrução (7–8, 9–12, 14), o item 8 aparecendo nas duas por
  somar as formas, mais **1** por permissão (13). Com o item 15 (instrução + gate), a contagem
  escrita passou a **sete** por teste executável e **oito** por gate/instrução, com a ressalva do
  item dual explicitada ("e por isso aparece nas duas contagens") para a aritmética fechar em 15.
  O número recontado mandou; nenhuma doutrina nova entrou por isso, e o desvio se esgota aqui (sem
  tíquete). `CHANGELOG.md` recebeu **uma** linha sob `[Não lançado]`, no formato da seção.
  Tarefa de redação, sem TF/TR de código. Verificação colada do terminal: `check-readme.ps1` →
  *OK - 8 agente(s), 11 skill(s), **15 guardrail(s)**, versão '0.0.0', 14 seção(ões) com Fonte da
  verdade válida* (exit 0) — de **14 × 14** para **15 × 15**; `kit_check.ps1 -Mode validate` →
  *OK - 8 agente(s) e 11 skill(s) validados; VERSION == KIT_VERSION ('0.0.0')* (exit 0);
  `kit_check.ps1 -Mode check-drift` → *OK - .claude/README.md == regenerado (8 agente(s),
  11 skill(s))* (exit 0); `dead_code.py` → *OK - 0 achado(s)* (exit 0); `python -m pytest` →
  **39 passed in 3.93s** (piso anterior 39, mantido). Greps de aceite: `^15\. \*\*` em
  `GOVERNANCA.md` → **1** (linha 585); `^\| 15 \|` em `README.md` → **1** (linha 709);
  `DP-M|P-0734|T36` em `GOVERNANCA.md` e `README.md` → **vazio** nos dois. Teto 30 respeitado
  (regime `TK-32`), sem estouro.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T37` — Conformidade: poda das proibições que a matriz passa a derivar — `done`.** Os dois
  prompts que mais repetiam fronteira de outro papel pararam de repeti-la: **nove** bullets saíram
  dos blocos `## Proibições`, todos derivados da matriz de `GOVERNANCA.md` §3 somada ao guardrail 15
  (`G-SCOPE`, publicado pela `T36`). **Nenhuma regra perdeu efeito** — o que saiu passou a valer por
  derivação. `.claude/skills/scrum-master/SKILL.md` foi de **6 para 2** bullets: saíram "Não
  implementa…" (linha *Execução* da matriz), "Não julga entrega…" (*Revisão*), "Não decide
  arquitetura nem requisito…" (*Planejamento* e *Dono/gerente*) e "Não reescreve dossiê…"
  (*Planejamento*); permaneceram "Não abre o RDO nem o laudo…" (**intocado — é objeto da `T39`**) e
  "Não despacha duas tarefas em paralelo…", fronteira interna do próprio loop.
  `.claude/agents/pantonic-reviewer.md` foi de **7 para 3**: saíram "A única escrita permitida é o
  laudo…", "Não corrige o que aponta…", "Não replaneja e não decide rota…", "Não declara `status` de
  tarefa…" (*Execução* e *Orquestração*, `DP-G`) e "Não julga mais de uma tarefa por contexto";
  permaneceram as três que restringem o exercício da **própria** responsabilidade ("Não marca
  `conforme` contra vermelho mecânico", "Não completa critério de pronto inverificável por conta
  própria" e "Não escreve percentual nem veredito"). Estado de entrada conferido contra o dossiê
  **antes da primeira edição**: os dois blocos batiam bullet a bullet, nenhum faltando, nada a
  reconciliar. Invariantes respeitados: nada novo enunciado nos dois arquivos, nenhum passo, tabela,
  campo, contador ou gatilho tocado, `## Guardrails` do `scrum-master` fora do escopo, nenhum
  ponteiro explicativo para o guardrail 15 acrescentado (prompt não recopia doutrina) e nenhum outro
  prompt do kit podado (`DP-M` §16.5). Tarefa de redação, sem TF/TR de código. Verificação colada do
  terminal: `kit_check.ps1 -Mode validate` → *OK - 8 agente(s) e 11 skill(s) validados; VERSION ==
  KIT_VERSION ('0.0.0')* (exit 0); `kit_check.ps1 -Mode check-drift` → *OK - .claude/README.md ==
  regenerado (8 agente(s), 11 skill(s))* (exit 0); `check-readme.ps1` → *OK - 8 agente(s), 11
  skill(s), 15 guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade válida* (exit 0);
  `python -m pytest` → **39 passed in 2.51s** (piso anterior 39, mantido). Greps de aceite: o início
  de cada um dos **nove** bullets removidos → **vazio** nos dois arquivos; "Não abre o RDO" no
  `scrum-master` → **1** ocorrência (linha 275, a `T39` a remove). **Teto de 15 (classe `redacao`)
  cruzado** — fechamento em ~19 tool uses, sob o regime `TK-32` (teto é alarme, não bloqueio). Causa
  medida, sem tarefa mal decomposta: a poda em si custou 3 chamadas (2 leituras + 3 edits em 2
  turnos); o excedente veio de **localizar a bateria de verificação** — o dossiê aponta "os quatro
  checks do §3 item 6" e o §3 lido é o de `GOVERNANCA.md`, não o do plano, o que gastou quatro
  buscas até achar `docs/plans/P-0734-execucao-autonoma.md:120-124` — e de **localizar o ponto de
  inserção no diário** (mais quatro). Recomendação ao planejamento: dossiê de tarefa de redação que
  cita "§3 item 6" nomear o arquivo do §3 e colar os quatro comandos, como já fazem outros cards do
  mesmo plano.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T38` — Laudo mínimo: `--observacoes` sai do gerador — `done`.** `.claude/tools/rdo.py`
  perdeu as três referências ao campo: o argumento `--observacoes` (linha 701), a variável
  `observacoes` (linha 479) e a linha `**Observações:** {observacoes}` do corpo do laudo (linha
  491) — `cmd_laudo` fica só com os cinco campos calculados mais a tabela de níveis.
  `.claude/agents/pantonic-reviewer.md` perdeu `--observacoes "<texto>"` do bloco de comando do
  passo 6; a prosa vizinha (linhas 67-72) já não citava observações, conferido sem edição.
  Nenhuma asserção em `tests/` citava o campo, então não houve atualização de teste. Invariantes
  respeitados: `calcular_laudo` e o cálculo de percentual, veredito, bloqueante, recomendação e
  pendência intocados; nenhum outro flag saiu; destino do laudo e escrita atômica como estavam;
  `docs/RUBRICA_DE_REVISAO.md` e `## Proibições` não tocados. Verificação: os quatro checks do §3
  item 6 do plano (`kit_check.ps1 -Mode validate`, `-Mode check-drift`, `check-readme.ps1`,
  `python -m pytest`) em exit 0; `python -m pytest` → **39 passed**, piso mantido;
  `python .claude/checks/dead_code.py` → exit 0, 0 achados; Grep `observacoes|Observações`
  (case-insensitive) em `.claude/` → **vazio**. **Teto de 15 (classe `mecanica`) cruzado** — 20 tool
  uses medidos, sob o regime `TK-32` (teto é alarme, não bloqueio). Causa medida, sem tarefa mal
  decomposta: a edição custou 3 edits + 5 verificações; o excedente veio de localizar o ponto de
  inserção no diário e o formato do bullet anterior, mais uma leitura desnecessária do índice de
  tíquetes. Recomendação ao planejamento: dossiê de tarefa `mecanica` que fecha em plano em
  andamento colar o range de linhas do bullet de fechamento anterior, como já faz para os checks.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T39` — `TK-33`: passos 7 e 8, a acepção de `pacote` em `A2` e a proibição que a `DP-M`
  dispensa — `done`.** Uma passada só em `.claude/skills/scrum-master/SKILL.md`, quatro pontos.
  (1) Gatilho do **passo 8**: "passo 5 concluído (regras `A1`..`A5`)" passou a ler `A1`..`A4` —
  `A5` não existe e as regras avaliadas depois do passo 5 são `A1`, `A2`, `A3a`, `A3b` e `A4`.
  (2) **Passo 7** (*Leitura do veredito*) passou a colher também a **recomendação**, campo fechado
  do laudo (`seguir`, `seguir com ressalva`, `refazer`, `escalar`), que `A6`, `A8`, `A9` e `B1` leem
  e que nenhum passo colhia; a saída do passo virou a tripla (`veredito`, `bloqueante`,
  `recomendação`) e a **Entrada** do passo 8 passou a recebê-la assim. O retorno de duas linhas do
  `reviewer` **não mudou** e nenhum campo novo foi criado (`DP-M` §16.4). (3) Regra `A2`: "pacote
  ausente ou inválido" passou a dizer **retorno** ausente ou inválido — `A2` julga o retorno do
  executor, e `pacote` nomeia os cinco campos do laudo (`DP-H`, item 4); só o termo mudou, condição
  e encaminhamento idênticos. (4) O bullet "Não abre o RDO nem o laudo…" saiu de `## Proibições`
  **sem fronteira substituta**: com `Observações` fora do gerador (`EXA-T38`) o laudo só tem campo
  fechado ou calculado, e os passos 7 e 9 o leem por desenho. Invariantes respeitados: nenhuma
  tabela de roteamento mudou de **efeito**; nenhum contador, teto ou gatilho novo; passo 9 intocado;
  nada acrescentado ao retorno do `reviewer`; os demais bullets de `## Proibições` como a `T37` os
  deixou; nenhum outro arquivo do kit editado. Verificação: os quatro checks do §3 item 6 do plano
  (`kit_check.ps1 -Mode validate`, `-Mode check-drift`, `check-readme.ps1`, `python -m pytest`) em
  exit 0, com **39 passed** (piso mantido); Grep `A5` no arquivo → **1** ocorrência, a que narra a
  queda de `A5` como fonte normativa (`:210`); Grep `pacote ausente` → **vazio**; Grep
  `Não abre o RDO` → **vazio**; Grep `recomenda` no bloco do passo 7 → **2** ocorrências (`:148`,
  `:151`). Teto de 15 (classe `redacao`) **não cruzado**: 13 tool uses medidos — o dossiê trouxe as
  âncoras re-derivadas e o range do bullet anterior, o que eliminou a busca de localização que
  custou o excedente da `T38`, e as quatro edições e os quatro checks couberam em três turnos.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T23b` — conformidade do `proximo-passo` com a residência única — `done`.** O entregável foi
  produzido e verificado em 2026-08-11 (bullet acima) e a tarefa ficou `blocked` por não haver quem a
  concluísse: a transição `review` → `done` é escrita só pelo `scrum-master`, que só passou a existir
  com `T19`, `T20`, `T21a` e `T21b`. As quatro estão `done`, então a razão registrada do bloqueio não
  se aplica mais — o desbloqueio é consequência mecânica do plano vigente, não decisão nova. Estado
  re-derivado no fecho sobre o arquivo **como ele está hoje** (tocado depois daquela rodada pela
  correção do `TK-34`, que acrescentou o dever de âncoras ao item 3 do gate de delegação): Grep
  `in progress|in review` em `.claude/skills/proximo-passo/SKILL.md` → **vazio**; Grep `backlog` →
  **5** ocorrências, todas substantivo (`description` do frontmatter, título, abertura, "próxima
  tarefa do backlog", "fora do backlog"); o parágrafo de vocabulário (`:15-19`) continua apontando
  para `diario-de-obras`, `## Status — residência única`, sem recopiar lista, máquina nem tabela de
  alcance; o item 4 da `DP-F` segue afirmado no guardrail de `superseded` (`:172-173`). Nenhuma
  regra de escolha mudou de efeito e **nenhuma edição de conteúdo foi necessária** — a conformidade
  entregue em 2026-08-11 sobreviveu intacta à edição do `TK-34`. Verificação: os quatro checks do §3
  item 6 de `docs/plans/P-0734-execucao-autonoma.md` (`kit_check.ps1 -Mode validate` → *8 agente(s) e
  11 skill(s) validados; VERSION == KIT_VERSION ('0.0.0')*; `-Mode check-drift` → *.claude/README.md
  == regenerado*; `check-readme.ps1` → *15 guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da
  verdade válida*; `python -m pytest`) em **exit 0**, com **39 passed** (piso mantido, 39 × 39).
  Rodada de fechamento conduzida pelo orquestrador, sem delegação: o que restava da tarefa era
  materializar `status`, ato exclusivo do `scrum-master` pela `DP-G`. Consumo: ver
  `docs/telemetria.tsv`.

- **`EXA-T24` — conformidade do restante do kit executável — `done`.** Os seis arquivos do kit que
  ainda citavam vocabulário morto de `status` foram alinhados à tabela de tradução da `DP-F`, com
  classificação por tipo de ocorrência antes de qualquer substituição. **9 edições em 4 arquivos:**
  `.claude/skills/handover/SKILL.md` (`:17` `in progress`→`in-progress`; `:20-21` `in review`→
  `review` e `in progress`→`in-progress`; `:43` ciclo do sprint `backlog`↔`in progress`↔`done` →
  `ready`↔`in-progress`↔`done`; `:109` `in progress`→`in-progress`);
  `.claude/skills/guardrails-check/SKILL.md` (`:8` `in review`→`review`; `:111` `in progress`→
  `in-progress`); `.claude/skills/bootstrap-pantonic/SKILL.md` (`:59` sprint inicial em `backlog`→
  `ready`, aqui `backlog` é status, não substantivo); `.claude/agents/pantonic-executor.md` (`:49`
  `in progress`→`in-progress`; `:60` `in review`→`review`). No `handover` `:20-21`, a enumeração dos
  quatro estados **permaneceu enumeração** — é regra do próprio handover, não recópia da lista
  canônica — e ganhou uma única linha de ponteiro para `.claude/skills/diario-de-obras/SKILL.md`,
  `## Status — residência única`. **Dois arquivos com zero edições, como previsto:**
  `.claude/skills/modelo-por-fase/SKILL.md` (`:63`, `:66`, `:67` — 3 ocorrências de `backlog`, todas
  tipo substantivo, e em `:67` string literal da lista de exclusão do hook: `pegue o backlog`;
  traduzir quebraria o casamento) e `.claude/README.md` (`:55`, substantivo dentro da região gerada
  a partir do `description` do frontmatter da `proximo-passo` — região gerada não se edita à mão).
  Invariantes respeitados: nenhuma regra mudou de efeito, nenhuma lista de estados foi recopiada em
  nenhum dos seis arquivos, nenhum gate foi reenunciado e nenhum arquivo fora dos seis foi tocado.
  Verificação (bateria do §3 item 6 de `docs/plans/P-0734-execucao-autonoma.md`, todos **exit 0**):
  `kit_check.ps1 -Mode validate` → *8 agente(s) e 11 skill(s) validados; VERSION == KIT_VERSION
  ('0.0.0')*; `-Mode check-drift` → *.claude/README.md == regenerado*; `check-readme.ps1` → *15
  guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade válida*; `python -m pytest` →
  **39 passed** (piso mantido, 39 × 39 — a tarefa não toca código). Grep `in progress|in review`
  (case-insensitive) nos seis alvos → **vazio**. Grep `backlog` nos seis → **4 sobreviventes**, todos
  legítimos: `modelo-por-fase` ×3 (substantivo/string literal do hook) e `.claude/README.md` ×1
  (substantivo em região gerada). **Achado (fora do escopo desta tarefa, que só troca termo e não
  muda conteúdo de regra):** `.claude/agents/pantonic-executor.md:60` manda o executor gravar `done`
  no diário, o que contraria a fronteira da `DP-G` — o executor é autor de `review` e `blocked` e de
  mais nada, quem materializa `done` é o `scrum-master`. Teto de 30 (classe `redacao`) **não
  cruzado**: 24 tool uses medidos — o dossiê trouxe as âncoras re-derivadas no ato, as contagens
  por arquivo corrigidas (`guardrails-check` e `pantonic-executor` tinham 2 cada, não 1) e a
  classificação dos dois arquivos de zero edição já decidida, de modo que o executor não pagou
  nem localização nem classificação. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T40` — alinhamento do executor: o prompt para de escrever e passa a sinalizar — `done`.**
  `.claude/agents/pantonic-executor.md` (arquivo único) passou a descrever o papel que a `DP-N`
  fixou. **Sete edições, uma por âncora:** a abertura ganhou a responsabilidade enunciada pelo dono
  — entregar código **funcional e conforme com as regras do projeto** (testes passando, golden rules
  cumpridas), com a aferição da aceitação declarada como ato do `reviewer`; o fato estável de
  economia de turnos trocou os dois "handover" por **sinal ao `scrum-master`**, sem tocar o número
  `~≤40` (é objeto do `TK-04`); o bullet do `Consumo:` **saiu inteiro**, porque quem não escreve no
  diário não grava placeholder nem número; o achado fora de escopo deixou de ser "tíquete indexado
  no diário" e virou **uma linha do sinal**, com a indexação atribuída ao `scrum-master`; o passo 2
  perdeu "marque `in-progress`" e ficou só em localizar a própria tarefa pelo índice; o passo 4
  passou a **sinalizar `blocked` com razão tipada** (`dependencia`/`premissa`, `DP-G`) e encerrar,
  com a declaração em prosa dos chamadores de produção removida — a alcançabilidade é medida por
  `.claude/checks/dead_code.py` e julgada na dimensão `guardas` do laudo, e `G-DEADCODE` continua
  valendo; o passo 5 virou **entrega tecnicamente correta** (suíte da área + conformance + piso) e o
  passo 6 deixou de invocar a skill `handover`, de atualizar o diário e de registrar o que foi
  feito: **sinaliza `review` e encerra**. Invariantes respeitados: nenhuma regra de execução mudou
  de efeito, o `frontmatter` não foi tocado (por isso `.claude/README.md` não precisou ser
  regenerado), nenhuma lista de estados entrou no arquivo e nada do `reviewer` ou do `scrum-master`
  foi reenunciado. Verificação (bateria do §3 item 6 de
  `docs/plans/P-0734-execucao-autonoma.md`, todos **exit 0**): `kit_check.ps1 -Mode validate` → *8
  agente(s) e 11 skill(s) validados; VERSION == KIT_VERSION ('0.0.0')*; `-Mode check-drift` →
  *.claude/README.md == regenerado*; `check-readme.ps1` → *15 guardrail(s), versão '0.0.0', 14
  seção(ões) com Fonte da verdade válida*; `python -m pytest` → **39 passed** (piso mantido,
  39 × 39 — a tarefa não toca código). Greps de aceite: `handover` → **vazio** (era 5 ocorrências);
  `diário` → **4 sobreviventes**, todas legítimas e nenhuma instrução de escrita (`:3` frontmatter,
  `:8` abertura, `:36` higiene de busca, `:48` passo 2). Teto de 15 (classe `redacao`) **não
  cruzado**: 9 tool uses medidos — o dossiê trouxe as sete âncoras coladas do arquivo, as duas
  contagens de Grep medidas no ato e a lista nominal dos quatro sobreviventes esperados, de modo que
  o executor não pagou localização nem classificação. Rodada fechada pelo orquestrador: o executor
  não editou o diário, não invocou `handover` e não gravou consumo — antecipação deliberada do
  regime que a própria tarefa institui. Consumo: ver `docs/telemetria.tsv`.
- **`EXA-T41` — as superfícies que descrevem o executor — `done`.** As cinco superfícies nomeadas
  pelo dossiê pararam de atribuir escrita ao executor, sem que nenhum princípio mudasse — **só o
  portador do ato**. `GOVERNANCA.md:93` (matriz §3, linha *Execução*): a coluna *Responde por* passa
  a declarar a entrega tecnicamente correta e o **sinal** (`review`/`blocked`), a coluna *Não faz*
  recebe que ele não escreve no diário, não registra o resultado da própria entrega e não afere a
  própria aceitação, e a cláusula final trocou "registra `blocked` no diário" por **sinaliza**;
  `GOVERNANCA.md:301-302` (§4.2): o registro do consumo é de **quem orquestra**, a partir do dado
  medido da notificação, com o desvio de 11-44% preservado como razão afirmada inline. Espelho em
  lockstep no `README.md` (o parágrafo de telemetria e a célula da tabela de preços), mesma seção,
  mesma ordem e mesma quantidade de afirmações, sem doutrina nova. Kit:
  `.claude/skills/proximo-passo/SKILL.md` perdeu a alternativa do placeholder — resta a forma única
  "o executor não edita o diário; o orquestrador escreve o bullet inteiro", com o ponteiro
  `Consumo: ver docs/telemetria.tsv` escrito direto no bullet e preservadas as regras de Edit
  pós-`Agent` e de telemetria vencida no pickup; `.claude/skills/guardrails-check/SKILL.md:8` passou
  a "obrigatório antes de sinalizar `review`", com o frontmatter intacto (índice não regenerado).
  Verificação (bateria do §3 item 6 de `docs/plans/P-0734-execucao-autonoma.md`, todos **exit 0**):
  `kit_check.ps1 -Mode validate` → *8 agente(s) e 11 skill(s) validados; VERSION == KIT_VERSION
  ('0.0.0')*; `-Mode check-drift` → *.claude/README.md == regenerado*; `check-readme.ps1` → *15
  guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade válida*; `python -m pytest` →
  **39 passed** (piso mantido, 39 × 39 — a tarefa não toca código). Greps de aceite: `handover` na
  linha 93 de `GOVERNANCA.md` → **vazio**; `executor grava` em `README.md` → **vazio** e em
  `GOVERNANCA.md` → **1 sobrevivente**. **Achado indexado pelo orquestrador:** o dossiê contava 2
  ocorrências de `executor grava` e existem 3 — a terceira (`GOVERNANCA.md:341`, checkpoint
  intermediário pela skill `handover`) está inteiramente dentro do recorte do `TK-36`, que ganhou a
  superfície na linha do índice; é a contradição declarada entre esta tarefa e aquele tíquete, não
  um desvio da entrega. Teto de 30 (classe `redacao`) **não cruzado**: 17 tool uses medidos — o
  dossiê trouxe as cinco âncoras coladas do arquivo e a contagem de cada grep de aceite. Rodada
  fechada pelo orquestrador: o executor sinalizou `review` e não tocou diário, `handover` nem
  telemetria. Consumo: ver `docs/telemetria.tsv`.
- **`EXA-T42` — a resposta na descoberta de não-conformidade de escopo — `done`.** O guardrail 15
  (`G-SCOPE`) deixou de falar só do prompt novo e passou a dizer o que se faz quando a violação é
  **encontrada em artefato existente**, sem que nenhum enunciado anterior mudasse. `GOVERNANCA.md`
  §7 item 15 ganhou duas cláusulas na sequência de "…redundante e sai": (1) **resposta na
  descoberta** — artefato do framework que atribui a um agente ato **não endossado** pela matriz, ou
  que carrega papel que ela **sequer cita**, é **não-conformidade grave**, que se para e regulariza
  em vez de enfileirar como dívida; (2) **a lacuna oposta não se resolve no ato** — ato **real e
  necessário** que a matriz não declara é falta **da matriz**, e criá-lo no prompt é exatamente a
  violação: registra-se e **sobe ao dono** (mesma regra da `DP-M`, §16.5). O *enforcement* ganhou a
  **varredura dos artefatos já existentes** ao lado do gate sobre prompt novo ou alterado. Espelho em
  lockstep na linha `| 15 |` de `README.md` §10, com as duas cláusulas condensadas na célula da regra
  e a varredura entrando como **qualificação do gate de review existente** — não como forma nova de
  enforcement —, de modo que o parágrafo de contagem (`README.md:711-713`, "**Sete**… **oito**… as
  três formas") permaneceu verdadeiro e intocado. Contagem preservada em **15 × 15**, sem guardrail
  novo e sem responsabilidade nova. Verificação (bateria do §3 item 6 de
  `docs/plans/P-0734-execucao-autonoma.md`, todos **exit 0**): `kit_check.ps1 -Mode validate` → *8
  agente(s) e 11 skill(s) validados; VERSION == KIT_VERSION ('0.0.0')*; `-Mode check-drift` →
  *.claude/README.md == regenerado*; `check-readme.ps1` → *15 guardrail(s), versão '0.0.0', 14
  seção(ões) com Fonte da verdade válida*; `python -m pytest` → **39 passed** (piso mantido,
  39 × 39 — a tarefa não toca código). Teto de 15 (classe `redacao`) **não cruzado**: 7 tool uses
  medidos — o dossiê trouxe as duas âncoras coladas na íntegra, o texto vizinho de cada uma e o
  invariante de contagem, e o executor não pagou localização. Rodada fechada pelo orquestrador: o
  executor sinalizou `review` e não tocou diário, `handover` nem telemetria. Consumo: ver
  `docs/telemetria.tsv`.
- **`EXA-T43` — sanitização do kit executável contra a matriz — `done`.** Os **19** prompts do kit
  (8 agentes + 11 skills) foram varridos contra a matriz de responsabilidades (`GOVERNANCA.md` §3)
  pelo método prescrito — uma coleta programática pelos doze verbos atributivos, **307 ocorrências
  brutas**, e leitura dirigida só das regiões apontadas. As **36** ocorrências classificadas ficaram
  em `docs/audits/CONFORMIDADE_MATRIZ_2026-08-12.md` §1, uma linha por ocorrência com arquivo,
  linha, papel, atribuição, veredito (a/b/c) e ação; a §2 nasce aberta, com cabeçalho e a nota de
  escopo da `T44`. **Doze edições, todas de classe (b)**: os dois auditores deixaram de mandar
  registrar tíquete "via `pantonic-planner`" e passaram a dizer o que a matriz declara (o
  apontamento vira item do diário, priorizado pelo dono); o `pantonic-planner` perdeu os dois
  bullets redundantes de "nunca faz", um dos quais ainda atribuía `handover` ao planejamento; a
  `guardrails-check` corrigiu quatro pontos (ponteiro para o papel inexistente
  `integration-executor`, "recomenda no handover" → sinal de retorno, "agente de refactor" →
  auditor de clean code, o bloco de veredito indo às *Notas de execução* do diário, e "registrar no
  diário" → "sinalizar `blocked` com a razão tipada"); a `diario-de-obras` perdeu duas atribuições
  de escrita no diário à Execução; a `proximo-passo` perdeu a cláusula que autorizava delegar
  execução a `clean-code`/`architect-auditor`, papéis que a matriz sequer cita; e duas
  `description` de frontmatter saíram do vocabulário morto (`audit-sweep`: frente "pyside6" →
  "DDD", o que **fecha o `TK-12`**; `integrar-poc`: "do agente integrador"), com `.claude/README.md`
  regerado por `-Mode generate`. `scrum-master`, `pantonic-reviewer` e `pantonic-executor` foram
  reconferidos e **saíram sem edição** — o que apareceu neles é (a) ou já resolvido pela `T37`/`T40`.
  Nenhuma responsabilidade nova, nenhuma proibição nova, `GOVERNANCA.md` intocado. **Um achado de
  classe (c)** — a skill `handover` atribui à Execução escrever o checkpoint de contexto nas *Notas
  de execução* do diário, ato real e necessário que a matriz não declara —, não editado por
  prescrição do item 15 e indexado como **`TK-37`**, que sobe ao dono. Verificação (bateria do §3
  item 6 de `docs/plans/P-0734-execucao-autonoma.md`, todos **exit 0**): `kit_check.ps1 -Mode
  validate` → *8 agente(s) e 11 skill(s) validados; VERSION == KIT_VERSION ('0.0.0')*;
  `-Mode check-drift` → *.claude/README.md == regenerado*; `check-readme.ps1` → *15 guardrail(s),
  versão '0.0.0', 14 seção(ões) com Fonte da verdade válida*; `python -m pytest` → **39 passed**
  (piso mantido, 39 × 39 — a tarefa não toca código). Teto de 40 (classe `redacao`) **atingido no
  limite**, 41 tool uses medidos: o volume vem do universo varrido (19 arquivos, 307 ocorrências,
  18 leituras dirigidas antes de 12 edições) e não de thrashing, e sob o regime interino do
  `TK-32` o teto é alarme — a tarefa fechou completa. Rodada fechada pelo orquestrador: o executor
  sinalizou `review` e não tocou diário, `handover` nem telemetria. Consumo: ver
  `docs/telemetria.tsv`.

- **`EXA-T44` — sanitização da doutrina, do espelho e dos índices contra a matriz — `done`.** Os
  **6** documentos do universo fechado (`GOVERNANCA.md` 839 linhas, `README.md` 933,
  `ARQUITETURA_PANTONICA.md` 513, `docs/RUBRICA_DE_REVISAO.md` 259, `docs/RESIDENCIA_DOUTRINA.md`
  188, `docs/DOC_MAP.md` 102) foram varridos contra a matriz de responsabilidades (`GOVERNANCA.md`
  §3) pelo método prescrito — uma coleta programática pelos doze verbos atributivos, **381
  ocorrências brutas**, mais uma varredura complementar por **papel que a matriz sequer cita**
  (segundo membro do `G-SCOPE`, que os verbos não pegam por construção) —, com leitura dirigida só
  das regiões apontadas e nenhum Read integral nos três docs acima de 500 linhas. As **38**
  ocorrências classificadas ficaram na §2 de `docs/audits/CONFORMIDADE_MATRIZ_2026-08-12.md`
  (`#37`..`#74`, mesma tabela da §1): **32 (a)**, **4 (b)**, **1 (c)** e uma linha declarada fora do
  escopo (§9 do `README.md`, recorte do `TK-36`). **Quatro edições, todas de classe (b)**: o estouro
  de teto deixou de se reportar "no handover" e passou ao **sinal de retorno** (`GOVERNANCA.md:139`,
  mesma correção do `#13` da `T43`); "o agente atualiza o diário de obras e faz handover"
  (`:333-334`) passou a dizer que quem executa **sinaliza** (`review`/`blocked` com razão tipada) e
  encerra o próprio contexto, cabendo o registro do fechamento e a abertura da tarefa seguinte à
  orquestração; o espelho `README.md:402-403`, que mandava "marcar `blocked` no diário e fazer
  handover", passou a "sinaliza `blocked` com a razão tipada e escala" — a **fonte já dizia isso**,
  só o espelho divergia; e "agente de integração", papel que a matriz sequer cita, saiu das duas
  ocorrências de `ARQUITETURA_PANTONICA.md` (`:155`, `:393`) para "harness de integração de POC" e
  "Pipeline de integração da POC (5 passos)". Nenhuma responsabilidade nova, nenhuma proibição nova,
  **matriz intocada** (é a régua, `#37`), registros do que aconteceu à época preservados (rodadas da
  §7.1, `RESIDENCIA_DOUTRINA.md`) e contagens do espelho intactas (15 × 15 guardrails, 14 seções com
  Fonte da verdade). **Um achado de classe (c)** — `GOVERNANCA.md:340-344` atribui à Execução gravar
  o checkpoint intermediário ao cruzar 2/3 do teto: é a **fonte na doutrina** da mesma lacuna do
  `#27` da §1, não editada pela prescrição do item 15 e **sem tíquete novo**, porque o `TK-37` já a
  registra e a superfície já está no recorte do `TK-36`. Verificação (bateria do §3 item 6 de
  `docs/plans/P-0734-execucao-autonoma.md`, todos **exit 0**): `kit_check.ps1 -Mode validate` → *8
  agente(s) e 11 skill(s) validados; VERSION == KIT_VERSION ('0.0.0')*; `-Mode check-drift` →
  *.claude/README.md == regenerado*; `check-readme.ps1` → *15 guardrail(s), versão '0.0.0', 14
  seção(ões) com Fonte da verdade válida*; `python -m pytest` → **39 passed** (piso mantido, 39 × 39
  — a tarefa não toca código). Consumo **18 tool uses** contra teto 40 da classe `redacao`, com
  folga: o método prescrito (uma coleta programática, depois leitura dirigida) é o que segurou o
  custo num universo de 381 ocorrências brutas. Rodada fechada pelo orquestrador: o executor
  sinalizou `review` e não tocou diário, `handover` nem telemetria. Consumo: ver
  `docs/telemetria.tsv`.

- **`EXA-T25` — conformidade: espelho e índices — `done`.** A porta de entrada do projeto deixou de
  ensinar vocabulário morto de `status`. `README.md`: 8 substituições de tipo (i) (`in progress` →
  `in-progress` em `:449`, `:454`, `:527`, `:626`, `:661`; `backlog` → `ready` em `:452`, `:528`;
  `in review` → `review` em `:681`) mais a reescrita do parágrafo dos estados válidos (`:533-540`),
  que agora espelha a lista final ratificada — `triage`, `ready`, `blocked`, `in-progress`,
  `review`, `done`, `cancelled` —, declara `done` e `cancelled` como os terminais de tarefa, tira
  `superseded` da lista e o enuncia como estado **exclusivo de plano e de iniciativa** (tarefa
  tornada obsoleta é `cancelled`), e **aponta** para `## Status — residência única` de
  `.claude/skills/diario-de-obras/SKILL.md` sem recopiar a máquina de transições nem o alcance por
  objeto. As 10 ocorrências de tipo (ii)/(iii) — `backlog` substantivo, `superseded` de plano,
  `bloqueado`/`parcial` em prosa — ficaram intactas, como o dossiê classificou. `CHANGELOG.md`:
  entrada nova no topo de `## [Não lançado]`, entradas históricas não reescritas. Os **dois índices
  não mudaram, com motivo medido**: `docs/DOC_MAP.md` só indexa doc acima de 500 linhas e a
  residência tem 232, de modo que indexá-la contradiria a regra do próprio mapa (o ponteiro já vive
  no `README.md` §7); `docs/RESIDENCIA_DOUTRINA.md` reconcilia as Regras 1-8 do `CLAUDE.md` global
  contra o kit e não tem entrada de residência de vocabulário — criar uma seria doutrina nascendo
  fora da residência. Desvio declarado no grep de aceite: `in progress` sobrevive **1** vez, em
  `CHANGELOG.md:22`, dentro da entrada que descreve a própria migração — registro histórico, que é
  onde o critério de pronto admite o termo. Verificação (bateria do §3 item 6, os quatro em **exit
  0**): `kit_check -Mode validate` → *8 agente(s) e 11 skill(s); VERSION == KIT_VERSION ('0.0.0')*;
  `-Mode check-drift` → *.claude/README.md == regenerado*; `check-readme.ps1` → *15 guardrail(s),
  versão '0.0.0', 14 seção(ões) com Fonte da verdade válida* (as duas contagens preservadas);
  `python -m pytest` → **39 passed** (piso 39 × 39 — a tarefa não toca código). Consumo **24 tool
  uses** contra teto 30 da classe `redacao`. **Um achado fora de escopo**, indexado como segunda
  ocorrência do `TK-30` e sem tíquete novo: na residência única, `superseded` aparece na tabela
  `### Alcance por objeto` mas está ausente da `### Lista final` e da `### Máquina de transições` —
  o único estado terminal de plano não tem gatilho de entrada na fonte da verdade. Rodada fechada
  pelo orquestrador: o executor sinalizou `review` e não tocou diário, `handover` nem telemetria.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T45` — `TK-39`: o critério de aceitação deixa de ser contagem — `done`.** O §19 do
  `P-0734` parou de aprovar a entrega por número de acionamentos do gerente e passou a classificar
  cada acionamento **pela causa**. `docs/plans/P-0734-execucao-autonoma.md`: no **§19** saiu o
  bloco-andaime que anunciava esta própria tarefa, saiu a frase *"round-trip de despacho é
  reprovação"* e entrou o bloco **"A aceitação classifica cada acionamento pela causa"**, com os
  dois ramos — causa que é do gerente (dirimir ambiguidade, conflito de requisito ou de aceitação)
  é legítima e **ilimitada**, e o risco fatal declarado é o agente decidir aceitação sem estar
  inequivocamente seguro; acionamento em **caminho feliz ou natural** é ineficiência da entrega, e
  **uma só ocorrência** basta, sem franquia — mais o ponteiro para `GOVERNANCA.md` §4.3 e §3.1
  item 3. Na **`T16`** a medida "quantos round-trips o dono precisou dar" saiu da lista, entrou o
  registro **qualitativo, por ocorrência**, e a cláusula de aceitação com o "Pronto quando" passaram
  a classificar por causa. A **`T17`** não precisou de edição: o veredito já referenciava o §19 sem
  contagem. `GOVERNANCA.md` §4.3 recebeu o bullet **"Acionamento do dono — a causa decide"**, entre
  a sinalização de fechamento e a retomada sem tarefa nomeada, com o gancho para §3.1 item 3; a
  skill `scrum-master` recebeu, na seção "O que obriga parada e o que segue com registro", o bullet
  **"Parada defeituosa"** (despachar, criar contexto e distribuir handover são execução normal do
  loop) e o parágrafo "Parada legítima não tem teto", que separa escalada de ocupação de janela
  (`B2`). Verificação (bateria do §3 item 6, os quatro em **exit 0**): `kit_check -Mode validate` →
  *8 agente(s) e 11 skill(s); VERSION == KIT_VERSION ('0.0.0')*; `-Mode check-drift` →
  *.claude/README.md == regenerado*; `check-readme.ps1` → *15 guardrail(s), versão '0.0.0', 14
  seção(ões) com Fonte da verdade válida* (as duas contagens preservadas, nenhum guardrail novo);
  `python -m pytest` → **39 passed** (piso 39 × 39 — a tarefa não toca código). Grep de aceite: as
  ocorrências remanescentes de `round-trip` são exatamente as declaradas fora do alvo — origem e
  custo, batching de decisão, ratificações ocorridas, tabela de riscos e dimensionamento de janela.
  `README.md` não tocado, por invariante do dossiê: a consolidação do espelho é da `T17`. Consumo
  **17 tool uses** contra teto 25 da classe `redacao` (âncora do §19 re-derivada pelo orquestrador
  antes da delegação: o dossiê apontava `:3652-3673`, vencido em ~57 linhas, e a seção estava em
  `:3709-3745`). **Um achado fora de escopo**, aberto como **`TK-40`**: a tabela de riscos do §6
  (`:2000`) ainda promete que a `T16` "mede quantos round-trips de fato desapareceram" — mitigação
  viva, incoerente com a `T16` reescrita, e fora do recorte que o dossiê declarou intocável. Rodada
  fechada pelo orquestrador: o executor sinalizou `review` e não tocou diário, `handover` nem
  telemetria. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T46` — doutrina: guardrail 16 (`G-SURFACE`) e o espelho em lockstep — `done`.** A golden
  rule enunciada pelo dono virou guardrail nomeado: **mudança de decisão estruturante regulariza a
  superfície de contato inteira, no ato**. O gatilho é a decisão que altera o que o trabalho *é* —
  objetivo-chave, requisito ou caso de uso —, e refinar redação, corrigir número ou trocar âncora
  **não** dispara a regra. `GOVERNANCA.md` §7 recebeu o item **16** entre o `G-SCOPE` e o parágrafo
  de materialização; o `README.md` §10 recebeu a linha 16 da tabela, mais duas correções de
  consistência na mesma seção que a linha nova tornaria falsas (a abertura, de *Quinze* para
  *Dezesseis*, e a contagem das formas de enforcement, de *oito* para *nove* dependentes de gate).
  *Enforcement* declarado: gate de planejamento — a rodada que fecha a decisão estruturante emite os
  cards de regularização no mesmo ato, e a fila não avança sem eles — somado ao gate de review.
  `check-readme.ps1` **não** foi tocado: ele conta guardrail dinamicamente, e o espelho fechou em
  **16 × 16** só por as duas listas crescerem juntas. Verificação (bateria do §3 item 6, os quatro em
  **exit 0**): `kit_check -Mode validate`; `-Mode check-drift`; `check-readme.ps1` → *16
  guardrail(s), 14 seção(ões) com Fonte da verdade válida*; `python -m pytest` → **39 passed**.
  Consumo **12 tool uses** contra teto 25 da classe `redacao`. Achado fora de escopo roteado para a
  `T48`: o `CHANGELOG.md` registrava a subida 14 → 15 e não tinha a entrada do 15 → 16. Rodada
  fechada pelo orquestrador. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T47` — consolidação, universo 1: o plano `P-0734` — `done`.** **17 ocorrências
  classificadas: 9 de classe (a), 6 de classe (b) regularizadas e 2 de classe (c) que subiram ao
  dono.** Método prescrito cumprido — sonda programática via scratchpad sobre as 3.928 linhas
  (mapa de seções, índice dos 48 cards e frequência de todo `DP-*`/`DA-*`/`DE-*`), depois leitura
  dirigida; o Grep cru do índice de decisões estourou 35 KB numa chamada e foi descartado em favor
  da sonda. Recorte de vigência aplicado e declarado: **dossiê de tarefa já executada é história**
  (é a encomenda da época), de modo que só entraram em (b) os dossiês não executados, os §1-§3, as
  mitigações do §6, o §7/§8, o §19 e o bloco `## Dossiês fechados por decisão`. As seis edições:
  **b1** quita o `TK-40` (a mitigação de risco da consciência situacional passa a se apoiar no
  registro qualitativo por ocorrência classificado pela causa, com o RDO mantido como instrumento
  compensatório da `DA-5`, sem reintroduzir contagem); **b2** e **b3** marcam a revogação parcial da
  `DP-A` e da `DP-B` no topo de cada dossiê, com o corpo intocado, dizendo o que permanece e o que
  caiu; **b4** e **b5** dão ao §9 o ponteiro da revogação da `DP-D` pela `DP-E`, que morava ~270
  linhas adiante sem marca na âncora; **b6** conserta um invariante da `T27` que enumerava
  `DP-A..DP-F` como lista fechada sete rodadas atrás — executada assim, a `T27` reescreveria
  registro. Verificação (bateria do §3 item 6, os quatro em **exit 0**): `check-readme.ps1` → *16
  guardrail(s), 14 seção(ões)*; `python -m pytest` → **39 passed**. Consumo **28 tool uses** contra
  teto 40 da classe `redacao`. Rodada fechada pelo orquestrador. Consumo: ver
  `docs/telemetria.tsv`.

- **`EXA-T48` — consolidação, universo 2: os artefatos publicados — `done`.** **28 ocorrências
  classificadas: 12 de classe (a), 13 de classe (b) regularizadas e 3 de classe (c), todas
  herdadas — nenhuma nova.** Duas medições fecharam em zero e valem como invariante conferido:
  nenhuma ocorrência viva de *revisor*/*inspetor* (`DP-H`, termo único) e nenhuma de
  `--observacoes` (`DP-M`). As edições, por arquivo: `CHANGELOG.md` ganhou a entrada 15 → 16 na
  série das subidas de guardrail, sem bump (`DE-7`); `GOVERNANCA.md` §4.2 trocou a lista morta de
  `status` (`backlog`, `in progress`, `in review`) por ponteiro à residência única, e os itens 8 e 9
  do §7 perderam o handover morto das cláusulas de *Enforcement*; `README.md` acompanhou nas linhas
  8 e 9 do espelho e reescreveu o ciclo ponta a ponta do §11, que ainda publicava *"o handover
  fecha; o gerente limpa o contexto e invoca a próxima"* — exatamente o acionamento de caminho feliz
  que o §19 reprova; `.claude/README.md` corrigiu a mesma prosa de ciclo, fora da região gerada;
  a skill `scrum-master` trocou "a rota é escrita pela execução no RDO" pelo caminho vigente (chega
  pelo laudo ou pela linha de achado do sinal, e quem fecha transcreve); e `review_evidence.py`
  perdeu as três menções vivas ao objeto morto *pacote de retorno* — docstring do módulo, docstring
  de `confrontar_escopo` e a string do veredito impressa no documento que o `reviewer` lê —, com
  mudança textual e comportamento intocado. Eixo declarado: esta varredura mede contra os
  **objetivos vigentes**, não contra a matriz de responsabilidades, que já foi varrida em 2026-08-12
  pelas `T43`/`T44`. Verificação (bateria do §3 item 6, os quatro em **exit 0**), com
  `check-drift` verde depois da edição de skill: `check-readme.ps1` → *16 guardrail(s), 14
  seção(ões)*; `python -m pytest` → **39 passed**. Consumo **46 tool uses** contra teto 40 da classe
  `redacao` — estouro de 6, registrado sem interromper a entrega (regime interino do §3 item 5); o
  sinal é de universo amplo (9 famílias de artefato), não de método ruim. Dois achados fora do
  universo declarado, indexados como **`TK-42`**. Relatório único das duas metades:
  `docs/audits/CONSOLIDACAO_SUPERFICIE_2026-08-13.md`. Rodada fechada pelo orquestrador. Consumo:
  ver `docs/telemetria.tsv`.

- **`EXA-T49` — a régua na doutrina: número arbitrário não governa fluxo — `done`.**
  `GOVERNANCA.md` §3: a tabela de tetos por classe permanece com todos os números, mas passa a ser
  declarada **referência informativa de dimensionamento, nunca gate** — não recusa entrega, não
  roteia, não encerra tarefa nem janela; caiu *"estourar o teto da classe é sinal de decomposição
  errada — replanejar, não continuar"* e entrou *"cruzar o número é alarme, nunca bloqueio"*. A
  residência do qualitativo foi nomeada ali: card **"Lições aprendidas na tarefa"** do laudo,
  preenchido quando houver o que observar; sem observação, o número isolado se desconsidera. §4.3:
  caiu a **cláusula-vício** — *"enquanto não houver proxy de ocupação disponível ao agente, o proxy
  operante é o teto de tool uses por classe"* —, e o encerramento passou a se apoiar em **coesão** e
  **capacidade**, com a medida de ocupação como instrumento e, enquanto ela não existir, a coesão e
  o fim do plano. Uma edição além das âncoras nomeadas, dentro da mesma régua: o gatilho de
  checkpoint intermediário deixou de ser *"2/3 do teto da classe"* e virou qualitativo — mantê-lo
  ressuscitaria o teto como operante logo abaixo da cláusula que o desautoriza. `README.md`
  espelhado nas 15 ocorrências varridas, com 9 preservadas por não atribuírem poder de porteiro. No
  plano, o §3 item 5 deixou de ser "regime interino" e virou o **regime deste plano**, e o topo do
  `### DP-B` recebeu marca de revogação parcial com corpo intocado. Verificação: os quatro em **exit
  0**, *16 guardrail(s), 14 seção(ões)*, **39 passed**; Grep de fecho com zero ocorrências de
  `proxy operante`, `2/3 do teto` e `replanejar, não continuar`. Consumo **38 tool uses**. Consumo:
  ver `docs/telemetria.tsv`.

- **`EXA-T50` — a regra no loop: `A4` e `B2` deixam de rotear por número — `done`.** Na skill
  `scrum-master`, a linha **`A4`** saiu da tabela do bloco A (mesmo precedente da queda de `A5` pela
  `DP-G`: sem renumeração, a lacuna fica), substituída por prosa que declara o consumo **alarme,
  nunca bloqueio** e o encaminha para a série e para o card de lições aprendidas. **`B2`** perdeu os
  dois números que o dono nomeou como vício — dez tarefas fechadas, 900 k tokens acumulados — e
  passou a medir as duas condições do §4.3, com a ressalva de que, enquanto não existir medida de
  ocupação, valem a coesão e o fim do plano. A lista "Obriga parada" perdeu os dois itens de teto e
  **manteve íntegras** as paradas de causa (`pendencia=`/`escalar`, `A3b`, `A7`, `B3`). A tabela de
  contadores trocou a coluna `teto` por `para que serve`, e a `description` do frontmatter, que
  dizia *"encerra a janela por teto numérico"*, passou a *"por coesão e ocupação de contexto"* — era
  o vício afirmado na própria superfície do alvo. Nove ocorrências de `teto` permaneceram, cada uma
  com motivo declarado, e nenhuma governa rota ou encerramento. Verificação: os quatro em **exit 0**,
  **39 passed**. Consumo **36 tool uses**. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T51a` — sanitização, o instrumento: o gerador para de decidir por consumo — `done`.** Em
  `.claude/tools/rdo.py`, `calcular_desdobramento` perdeu o parâmetro `orcamento_estourado` e o ramo
  `if orcamento_estourado: return "estouro"`; a linha `orcamento_estourado = args.tool_uses >
  dossie.teto` saiu. Os campos `TETO`/`TOOL_USES`/`TOKENS_K`/`DURACAO_S` seguem medidos, transcritos
  e impressos — a medição é o que a decisão preserva. **Achado que encolheu a superfície:** as 21
  ocorrências de `teto` em `review_evidence.py` são todas `teto_chars`/`teto_diff_chars`,
  truncamento de string, e não consumo — o arquivo não precisou de edição, nem o `rdo_template.md`.
  O teste que provava o gate foi **reescrito**, não apagado: agora fecha um RDO real com
  `--tool-uses 41` contra teto 40 e prova que o desdobramento continua `aprovado`, que os números
  aparecem no documento e que a palavra `estouro` não aparece em lugar nenhum. Verificação: os
  quatro em **exit 0**, **39 passed**. Consumo **26 tool uses**. Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T51b` — sanitização, a descrição: prompts, índices e a marca da `DA-11` — `done`.** **27
  ocorrências classificadas: 18 de classe (b), 9 de classe (a), nenhuma (c) nova.** O
  `pantonic-executor` perdeu o *"orçamento esperado ~≤40 tool uses … sinalizar ao scrum-master"* (o
  número roteava); o `pantonic-reviewer` ganhou a proibição de pontuar, reprovar ou escalar por
  consumo, mais o card de lições aprendidas nomeado como residência **discricionária**; a
  `RUBRICA_DE_REVISAO.md` passou a medir **existência e procedência** do registro de consumo, nunca
  a grandeza; a `RESIDENCIA_DOUTRINA.md` trocou *"estourar = replanejar, não continuar"* por
  referência informativa. No plano, marca de revogação parcial na **`DA-11`** e no topo do card
  `T6b`, corpo intocado nos dois. Nove famílias de ocorrências de `teto` permaneceram com motivo
  declarado — teto de **retentativa** (parada de causa, íntegra por desenho), limite de **tamanho de
  campo**, e transcrição de medida. Terceiro bloco do relatório acrescentado sem tocar os dois
  existentes. Verificação: os quatro em **exit 0**, **39 passed**. Consumo **48 tool uses**.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T52` — fecho do bloco `DP-Q`: o gatilho residual e a residência não materializada —
  `done`.** Card emitido pelo orquestrador a partir de dois resíduos vivos que a `T51b` mediu — o
  `G-SURFACE` proíbe enfileirar como dívida o que a decisão estruturante atingiu. **Parte 1:** o
  gatilho de checkpoint do `handover` foi conferido contra o §4.3 já reescrito e está transcrito
  como sinal qualitativo, sem número; o teto de 2 tool uses do próprio checkpoint e o limite de 5
  linhas permanecem, por serem prescrição de esforço do artefato. **Parte 2:** o card **"Lições
  aprendidas na tarefa"** deixou de ser residência nomeada e não materializada — `rdo.py` ganhou
  `--licoes-aprendidas` opcional em `laudo` e em `close`, e o `rdo_template.md` ganhou a seção com
  `{{LICOES_APRENDIDAS}}` entre `## Laudo` e `## Fechamento`. **Discricionário por desenho:** vazio
  é estado legítimo, sem campo obrigatório e sem validação que reprove ausência — quatro testes
  novos provam as duas metades (preenchido e vazio, em `laudo` e em `close`). Fronteira respeitada:
  materializa a residência que a `DP-Q` item 3 fixou, e **não** decide o que o `scrum-master` colhe
  do laudo, que segue com a `T30`. Verificação: os quatro em **exit 0**; **piso subiu de 39 para
  43**. Consumo **52 tool uses**. Consumo: ver `docs/telemetria.tsv`.

**Bloco da `DP-Q` encerrado em 2026-08-13** (bullets de fechamento acima) — **número arbitrário
deixou de governar fluxo em todo o framework**. A decisão do dono fechou o `TK-41` pelo mesmo
princípio nos dois itens: teto de tarefa e teto de janela são a mesma questão do limite de
round-trips, números que ninguém deriva de nada e que só geram ruído, e ação baseada em ruído é
decisão equivocada. Caíram, nominalmente, o roteamento por estouro (`A4`), os dois números de fim de
janela (`B2`), a cláusula que elegia o teto de tool uses como proxy operante de capacidade, o
gatilho de checkpoint por 2/3 do teto e a ramificação por consumo no gerador de RDO. **O que ficou
intacto por desenho:** a medição — a série `docs/telemetria.tsv` continua alimentada sem exceção,
porque é o **agregado** que a decisão declara ter valor — e toda parada de **causa**, com escalada
por ambiguidade ou conflito de requisito e de aceitação seguindo **ilimitada**. A matéria de limites
**não foi doutrinada aqui**: ela se revê inteira no plano próprio já previsto (desdobramento da
`T17` item 4), e nenhum número novo entrou no lugar dos que caíram. Consequência declarada e aceita:
até a `T13` entregar a medida de ocupação, o encerramento de janela se apoia só em coesão e no fim
do plano — por isso a `T13` saiu do fim da fila e passou a suceder o bloco. **Próxima tarefa:**
**`EXA-T13`** — proxy de ocupação de contexto. Fila registrada: **`T13`** → `T29` → `T30` →
[ratificação em lote: `DP-I` e `DP-J`] → `T26` → `T27` → `T12` → `T14` → `T15` → `T16` → `T17`
(dono).

**Bloco da `DP-P` encerrado em 2026-08-13** (bullets de fechamento acima) — **a golden rule do dono
virou guardrail e a superfície de contato foi regularizada nos dois universos**. A régua (`T46`) foi
publicada antes da varredura, o plano (`T47`) passou a enunciar o entendimento vigente uma vez só
com o texto derrubado marcado como derrubado, e os artefatos publicados (`T48`) deixaram de ensinar
o entendimento antigo — em particular o `README.md`, que descrevia como ciclo normal o gerente
limpar o contexto e invocar a próxima tarefa, que é o caso exemplar de ineficiência do §19. O
`TK-40` foi quitado dentro da `T47`. **Duas ocorrências de classe (c) pararam e subiram ao dono,
indexadas como `TK-41`** — a `DP-B` prescreve paradas (`A4`, estouro de teto; `B2`, fim de janela)
que o §19 pode classificar como acionamento em caminho feliz; nenhum dos dois textos foi tocado, e a
decisão muda o que a `T16` mede e o que a `T17` aprova. **Próxima tarefa:** a decisão do `TK-41` é o
próximo passo — enquanto ela não fecha, `T29` e `T30` seguem delegáveis (matéria disjunta), mas a
`T16` e a `T17` não. Fila registrada: [decisão do dono: `TK-41`] → **`T29`** → `T30` →
[ratificação em lote: `DP-I` e `DP-J`] → `T26` → `T27` → `T12` → `T13` → `T14` → `T15` → `T16` →
`T17` (dono).

**`EXA-T45` fechada** (bullet de fechamento acima) — **a aceitação do plano deixou de ser um número
e passou a ser uma classificação por causa**. Com ela, o `TK-39` está quitado na superfície que
declarou (o §19, a `T16`, a `T17`, a doutrina em `GOVERNANCA.md` §4.3 e a skill que conduz o loop),
e a `T16` (piloto) e a `T17` (veredito) passam a aferir o critério certo. **Próxima tarefa:**
**`EXA-T29`** — dossiê em `docs/plans/P-0734-execucao-autonoma.md` `### T29` (artefato `tarefa`:
definição, autores e canal). Em **contexto novo**. Fila registrada: **`T29`** → `T30` →
[ratificação em lote: `DP-I` e `DP-J`] → `T26` → `T27` → `T12` → `T13` → `T14` → `T15` → `T16` →
`T17` (dono).

**`EXA-T25` fechada** (bullet de fechamento acima) — **o espelho e os índices falam a lista final e
apontam para a residência, sem recopiá-la**. Com ela, a conformidade de vocabulário da `DP-F` cobre
as duas skills do kanban (`T23a`/`T23b`), o restante do kit executável (`T24`) e agora a porta de
entrada; sobram a doutrina normativa (`T26`) e o kanban mais os planos vivos (`T27`), que a fila já
posiciona depois da ratificação em lote.

**Fila reordenada em 2026-08-13 por decisão do dono** — entra o card prioritário **`EXA-T45`**
(`TK-39`), à frente da `T29`: o §19 (critério de aceitação final) foi autorado no mesmo dia apoiado
em **contagem de round-trips**, e o dono derrubou a contagem como conceito de aceitação. Enquanto o
critério estiver escrito como número, a `T16` (piloto) e a `T17` (veredito) aferem a coisa errada, e
é a aceitação da entrega final que fica em risco — por isso o card para a fila em vez de entrar no
fim dela. **Próxima tarefa:** **`EXA-T45`** — dossiê em
`docs/plans/P-0734-execucao-autonoma.md` `### T45` (o critério de aceitação deixa de ser contagem e
passa a classificar cada acionamento do gerente **pela causa**). Em **contexto novo**. Fila
registrada: **`T45`** → `T29` → `T30` → [ratificação em lote: `DP-I` e `DP-J`] → `T26` → `T27` →
`T12` → `T13` → `T14` → `T15` → `T16` → `T17` (dono).

**`EXA-T44` fechada** (bullet de fechamento acima) — **doutrina, espelho e índices só atribuem o que
a matriz endossa; o que sobrou é lacuna declarada da matriz, não improviso**. Com ela encerra o bloco
de três cards da `DP-O` (`T42`..`T44`): a régua foi publicada, o kit executável e a doutrina foram
varridos contra ela, e as duas ocorrências de classe (c) apontam para a mesma lacuna, já encaminhada
ao `TK-36`. **Próxima tarefa:** **`EXA-T25`** — dossiê em
`docs/plans/P-0734-execucao-autonoma.md` `### T25` (conformidade de **espelho e índices**: o
vocabulário de `status` da `DP-F` no `README.md` e nos índices); destravada agora, e a ordem já foi
justificada no §5 — a `T44` precede a `T25` porque as duas passam pelo mesmo `README.md`, e inverter
faria a conformidade de vocabulário rodar sobre texto que a sanitização ainda ia reescrever. Em
**contexto novo**. Fila registrada: **`T25`** → `T29` → `T30` → [ratificação em lote: `DP-I` e
`DP-J`] → `T26` → `T27` → `T12` → `T13` → `T14` → `T15` → `T16` → `T17` (dono).

**`EXA-T43` fechada** (bullet de fechamento acima) — **nenhum prompt do kit atribui mais ato que a
matriz não endossa; o que não coube nela virou `TK-37`, não improviso**. **Próxima tarefa:**
**`EXA-T44`** — dossiê em `docs/plans/P-0734-execucao-autonoma.md` `### T44` (sanitização da
**doutrina, do espelho e dos índices** contra a matriz: `GOVERNANCA.md`, `README.md`,
`ARQUITETURA_PANTONICA.md`, `docs/RUBRICA_DE_REVISAO.md`, `docs/RESIDENCIA_DOUTRINA.md`,
`docs/DOC_MAP.md`); destravada agora, por depender da `T43` `done`, e com metade das âncoras já no
relatório de conformidade, cuja §2 recebe as linhas novas. Em **contexto novo**. Fila registrada:
**`T44`** → `T25` → `T29` → `T30` → [ratificação em lote: `DP-I` e `DP-J`] → `T26` → `T27`. **A `T34`
saiu da fila em 2026-08-12**, cancelada por absorção: a matéria de uso e teto se revê inteira, em
plano próprio, aberto depois deste, e o desdobramento é o item 4 da `T17`.

**`EXA-T42` fechada** (bullet de fechamento acima) — **o `G-SCOPE` agora responde também pelo que já
está escrito: não-conformidade encontrada para e regulariza, e lacuna da matriz sobe ao dono**. A
régua que a `T43` e a `T44` aplicam está publicada. **Próxima tarefa:** **`EXA-T43`** — dossiê em
`docs/plans/P-0734-execucao-autonoma.md` `### T43` (sanitização do **kit executável** contra a
matriz de responsabilidades); destravada agora, por depender da `T42` `done`, e precede a `T44`
porque a doutrina descreve o kit e o relatório dela já traz metade das âncoras da seguinte. Em
**contexto novo**. Fila registrada: **`T43`** → `T44` → `T25` → `T29` → `T30` → `T34` →
[ratificação em lote: `DP-I`, `DP-J`, `DP-L`] → `T26` → `T27`.

**`EXA-T41` fechada** (bullet de fechamento acima) — **doutrina, espelho e a skill que delega não
mandam mais o executor escrever**. **Próxima tarefa:** **`EXA-T42`** — dossiê em
`docs/plans/P-0734-execucao-autonoma.md` `### T42` (o guardrail 15 passa a dizer o que se faz quando
a não-conformidade de escopo é encontrada em artefato existente); precede a `T43` e a `T44`, que
aplicam a régua. Em **contexto novo**. Fila registrada: **`T42`** → `T43` → `T44` → `T25` → `T29` →
`T30` → `T34` → [ratificação em lote: `DP-I`, `DP-J`, `DP-L`] → `T26` → `T27`.

**`EXA-T40` fechada** (bullet de fechamento acima) — **o prompt do executor não manda escrever em
lugar nenhum: ele entrega tecnicamente correto e sinaliza `review` ou `blocked`**. O `TK-35` está
`done`. **Próxima tarefa:** **`EXA-T41`** — dossiê em
`docs/plans/P-0734-execucao-autonoma.md` `### T41` (as superfícies que descrevem o executor:
doutrina, espelho e a skill que delega param de mandar o executor escrever); destravada agora, por
depender da `T40` `done`. Em **contexto novo**. Fila registrada: **`T41`** → `T42` → `T43` → `T44` →
`T25` → `T29` → `T30` → `T34` → [ratificação em lote: `DP-I`, `DP-J`, `DP-L`] → `T26` → `T27`.

**`EXA-T24` fechada** (bullet de fechamento acima) — **o kit executável não cita mais vocabulário
morto de `status`; o que sobrou de `backlog` é substantivo ou região gerada**. O achado dela abriu o
`TK-35` e, com ele, a rodada da **`DP-N`** (§17 do plano), ratificada pelo dono no mesmo dia: o
executor sinaliza e nada mais, a coleta do entregável é do `reviewer`, e a passagem de bastão vira
o `TK-36`. **Próxima tarefa:** **`EXA-T40`** — dossiê em
`docs/plans/P-0734-execucao-autonoma.md` `### T40` (o prompt do executor: sete pontos, arquivo
único). Em **contexto novo**. Fila registrada: **`T40`** → `T41` → `T42` → `T43` → `T44` → `T25` →
`T29` → `T30` → `T34` → [ratificação em lote: `DP-I`, `DP-J`, `DP-L`] → `T26` → `T27`.

**`EXA-T23b` fechada** (bullet de fechamento acima) — **a skill que consome o kanban fala a lista
final e aponta para a residência, sem reenunciá-la; o `blocked` da `DP-G` está quitado**. **Próxima
tarefa:** **`EXA-T24`** — dossiê em `docs/plans/P-0734-execucao-autonoma.md` `### T24` (conformidade
do restante do kit executável: seis arquivos, contagem medida em 2026-08-11). Em **contexto novo**.
Fila registrada: **`T24`** → `T25` → `T29` → `T30` → `T34` → [ratificação em lote: `DP-I`, `DP-J`,
`DP-L`] → `T26` → `T27`.

**`EXA-T39` fechada** (bullet de fechamento acima) — **as três referências órfãs do `TK-33` estão
reconciliadas e a proibição que a `DP-M` dispensa saiu; o `TK-33` está `done`**. Com ela encerra o
bloco de cinco cards da `DP-M` (`T35`..`T39`). **Próxima tarefa:** **`EXA-T23b`** — dossiê em
`docs/plans/P-0734-execucao-autonoma.md` `### T23b`. Em **contexto novo**. Fila registrada:
**`T23b`** → `T24` → `T25` → `T29` → `T30` → `T34` → [ratificação em lote: `DP-I`, `DP-J`, `DP-L`]
→ `T26` → `T27`.

**`EXA-T37` fechada** (bullet de fechamento acima) — **os dois blocos `## Proibições` só contêm
fronteira interna do próprio papel; nenhuma proibição do tipo "não faça o que é de outro papel"
sobrevive neles**.

**`EXA-T38` fechada** (bullet de fechamento acima) — **o gerador de laudo rejeita `--observacoes`;
o laudo emitido não tem prosa livre além da linha de pendência**. **Próxima tarefa:** **`EXA-T39`**
— dossiê em `docs/plans/P-0734-execucao-autonoma.md` `### T39`. Em **contexto novo**. Fila
registrada: **`T39`** → `T23b` → `T24` → `T25` → `T29` → `T30` → `T34` → [ratificação] → `T26` →
`T27`.

**`EXA-T36` fechada** (bullet de fechamento acima) — **a golden rule `G-SCOPE` existe na doutrina
publicada como guardrail 15, com o espelho em lockstep (15 × 15)**. **Próxima tarefa:** **`EXA-T37`**
— dossiê em `docs/plans/P-0734-execucao-autonoma.md` `### T37` (poda das proibições que a matriz
passa a derivar: 4 das 6 do `scrum-master`, 5 das 7 do `pantonic-reviewer`). Em **contexto novo**.
Fila registrada: **`T37` → `T38` → `T39`** → `T23b` → `T24` → `T25` → `T29` → `T30` → `T34` →
[ratificação] → `T26` → `T27` (fila da rodada de replanejamento da `DP-M`).

**`DP-M` ratificada pelo dono em 2026-08-11 — a golden rule de escopo de agente e o laudo mínimo.**
Enunciado do dono: o problema nunca foi proibir o `scrum-master` de ler o corpo do laudo — foi o
laudo ter corpo. O laudo se padroniza por função, como o RDO, e passa a ser **mínimo e suficiente**;
e no lugar de coibir papel a papel, vale uma **golden rule** para todo agente — *o agente se atém
estritamente às suas responsabilidades declaradas; o que não é escrito é proibido*. Escopo:
**conceito do framework**, não desenvolvimento dele (`DP-H`) — a regra entra em doutrina publicada,
e o plano carrega só as tarefas. Duas escolhas levadas ao dono e ratificadas: (1) a regra mora em
`GOVERNANCA.md` §7 como **guardrail 15**, com a §3 (matriz de responsabilidades) apontando para ela
— o espelho `README.md` §10 sobe para 15 linhas em lockstep, que é o que `check-readme.ps1` compara;
(2) `--observacoes` **sai** do gerador de laudo, assumido o risco de a marcação abaixo de `conforme`
ficar sem justificativa registrada.

Estado medido nesta rodada, que a rodada de replanejamento não precisa remedir: o laudo já é gerado
por função (`.claude/tools/rdo.py:481-492`), com 6 dos 8 campos fechados ou calculados; só
`Pendência` (uma linha, consumida por `B1`) e `Observações` (texto livre, sem limite, **sem
consumidor** — fora dos cinco campos do pacote) são prosa. `GOVERNANCA.md:104` já declara a matriz
como residência única do escopo de cada papel, mas **não existe** a cláusula de fechamento — nada diz
hoje que o não escrito é proibido. Sob a regra nova a matriz vira autoridade exaustiva, então
**auditar a matriz por completude é precondição**: sem isso todo agente nasce fora de conformidade.
A regra devolve linhas: 4 das 6 proibições do `scrum-master` (`:273`) e 5 das 7 do `pantonic-reviewer`
(`:83`) são do tipo "não faça o que é de outro papel" e passam a derivar da matriz. O `TK-33` item 3
(a proibição *"Não abre o RDO nem o laudo"* contra o passo 9) fica **decidido pela `DP-M`**: a
proibição some sem fronteira substituta, porque com `Observações` fora não sobra no laudo nada que o
`scrum-master` possa extrapolar lendo; os itens 1 e 2 continuam mecânicos.

**Rodada de replanejamento da `DP-M` — executada em 2026-08-11.** Autorada a seção `## 16` do
`docs/plans/P-0734-execucao-autonoma.md` (`16.1` enunciado, `16.2` as duas escolhas ratificadas,
`16.3` estado medido, `16.4` critério de sobrevivência de proibição + fechamento do `TK-33`, `16.5`
o que a `DP-M` não decide, `16.6` cards e fila; `16.7` reservada ao resultado que a `T35` escreve).
Cinco tarefas novas no §4: **`T35`** auditoria de completude da matriz de responsabilidades
[Opus · investigacao · 30], **`T36`** guardrail 15 (`G-SCOPE`) + espelho `README.md` §10 em lockstep
[Opus · redacao · 30], **`T37`** poda das proibições que a matriz passa a derivar
[Opus · redacao · 15], **`T38`** `--observacoes` sai do gerador de laudo [Sonnet · mecanica · 15] e
**`T39`** `TK-33` (passos 7 e 8, acepção de `pacote` em `A2`, proibição dispensada pela `DP-M`)
[Opus · redacao · 15]. Dois pontos fechados por derivação, sem decisão nova do dono: o **critério de
poda** (sobrevive só a proibição que restringe a própria responsabilidade) e o **`TK-33` item 2**
(a `recomendacao` é campo fechado do laudo e o passo 7 a colhe de lá — recusada a ampliação do
retorno do `reviewer`). Número de aceite re-derivado na rodada: `check-readme.ps1` compara
contagem (`| N |` do README × `^\d+\. \*\*` de `GOVERNANCA.md` §7), hoje **14 × 14** → **15 × 15**.
Fila reposicionada no §5 e linha do `TK-33` atualizada na tabela de tíquetes. A fila retoma pela
`T33`. Consumo: ver `docs/telemetria.tsv`.

**Regime interino de teto — decisão do dono, 2026-08-11 (`TK-32`); prorrogado em 2026-08-12.** O teto
do cabeçalho de cada tarefa é **alarme, nunca bloqueio**: nenhuma tarefa para, é impedida ou fica
incompleta por cruzar o número, e quem delega **não escreve cláusula de parada dura por teto** no
dossiê de delegação. A medição continua obrigatória em `docs/telemetria.tsv` — é a série que decide.
**A `DP-L` não se forma no `P-0734`:** a `EXA-T34` foi cancelada por absorção e a matéria de uso e
teto se revê inteira, em plano próprio, aberto depois deste (desdobramento na `T17`, item 4). O regime
vigora até aquela decisão. Materializado em `docs/plans/P-0734-execucao-autonoma.md` §3, item 5.

**Depois da `T20`:** `T31` → `T32` (desempate do framework no `GOVERNANCA.md` §3.1;
independente, não para) → `T21a` → `T21b` (o loop passa a existir) → `T33` (`reviewer` nas linhas
espelhadas) → `T23b` sai de `blocked` e é concluída → `T24` → `T25` → `T29` → `T30` → `T34` (uso e
teto como medida agregada; decide e para) → [ratificação em lote de `DP-I`, `DP-J` e `DP-L`, único
ponto de parada dura da fila] → `T26` → `T27`.

- **`EXA-T19` — `rdo.py`: o RDO se gera no fechamento — `done`.** `close` passa a materializar o
  RDO inteiro numa única chamada (CLI: `--plano --tarefa --tool-uses --tokens-k --duracao-s
  --veredito --percentual --bloqueante --recomendacao --pendencia-laudo [--pendencia] [--rdo-dir]
  [--template] [--esquema-legado --modelo --classe --teto]`), transcrevendo o `pacote` do laudo e o
  consumo medido por argumento — nenhuma leitura de arquivo de laudo sobrevive. Morrem `cmd_new`, o
  subparser `new`, `_CAMPOS_PACOTE_ORDEM`, `_TETO_CAMPO_PACOTE`, `_STATUS_VALIDOS`,
  `_FECHAMENTO_MARCADOR_RE`, `_EXECUCAO_CAMPO_VAZIO_RE`, `_ORCAMENTO_RE`, `_LAUDO_VEREDITO_RE` e
  `_LAUDO_BLOQUEANTE_RE` (sem consumidor vivo, confirmado por `dead_code.py` em exit 0).
  `calcular_desdobramento` encolhe para `(veredito, orcamento_estourado)`, dois ramos com
  precedência do estouro — fecha o `TK-29`. Template ganha `## Fechamento` e perde os oito bullets
  do pacote antigo e `{{LAUDO_PATH}}` (laudo é descartado pelo `scrum-master`, `DP-H`).
  `extrair_dossie` preservada (`review_evidence.py` reusa). RDOs de `T1`..`T10` e o RDO existente
  (`T11`) não tocados.
  Notas de execução:
  Arquivos: `.claude/tools/rdo.py` (reescrito), `.claude/tools/rdo_template.md` (reescrito),
    `tests/test_rdo.py` (reescrito: testes do `new` saem, 18 testes novos de `close` entram, os 6
    de `laudo` preservados intactos).
  Veredito — `EXA-T19`
  Suítes: `python -m pytest tests/test_rdo.py -q` — 23 passed; `python -m pytest -q` (suíte
    inteira) — 39 passed. `tests/conformance/` inexistente no hub (script CLI fora da árvore
    infracore/contracts/services/plugins, sem direção de camada a checar).
  Piso: `ratchet_piso.py` — OK (sem piso declarado em `tests/piso_comportamental.txt`).
  Kit: `kit_check.ps1 -Mode validate`/`-Mode check-drift` — exit 0 (8 agentes, 11 skills,
    VERSION==KIT_VERSION '0.0.0').
  Espelho: `check-readme.ps1` — exit 0 (8 agentes, 11 skills, 14 guardrails, 14 seções com Fonte
    da verdade).
  Código morto: `dead_code.py` — exit 0 (0 achados; confirma a lista de símbolos mortos acima).
  Checklist de review: ok — script CLI fora da árvore infracore/contracts/services/plugins; sem
    dependência externa nova; sem trabalho pesado em thread de entrada; sem tipo cruzando camada;
    teste com significado alterado foi reescrito, não deletado (suíte de `new` removida porque o
    comportamento morreu, não por conveniência); mudança comportamental amparada por `DP-H`/`T19`
    (ratificados) e `TK-29` (fecha aqui).
  Consumo: ver `docs/telemetria.tsv` (41 tool uses contra teto rígido 40 — estouro de 1).

- **`EXA-T20` — `pantonic-reviewer`: o revisor sem pacote — `done`.** As três entradas do
  julgamento passam a ser dossiê da tarefa + dossiê de evidência + diff, e `pacote de retorno`
  some do arquivo (0 ocorrências): o passo 2 do protocolo deixa de ler narrativa do executor e
  passa a ler a evidência mecânica; o passo 3 passa a ser o diff. O `pacote` sobrevive na acepção
  vigente — os cinco campos obrigatórios **dentro do laudo** (veredito, percentual, bloqueante,
  recomendação, pendência), com a suficiência declarada nos fatos estáveis, mais a cláusula de que
  o laudo é consumido e descartado (não é residência durável nem completa juízo por remissão). A
  saída ganha as duas linhas fixas de veredito (`<tarefa> <veredito> <percentual>
  bloqueante=<dimensão|nenhuma>` + `laudo=<caminho>`) e uma proibição nova: não declara `status` —
  nem autora, nem materializa, nem usa o vocabulário. O bloco de CLI, que documentava `--rdo` e
  `--recomendacoes` (nenhum dos dois existe no `rdo.py` vigente), passa à assinatura viva
  (`--plano --tarefa [--laudos-dir]`, sete flags de dimensão, `--vermelho-mecanico`,
  `--observacoes`, `--escalar`), com `--escalar` nomeado como o único canal de pendência do
  revisor e a recomendação declarada calculada.
  Notas de execução:
  Arquivos: `.claude/agents/pantonic-reviewer.md` (5 `Edit`s). `.claude/README.md` não regenerado —
    inventário de agentes inalterado (`check-drift` em exit 0 confirma).
  Conformidade de vocabulário (frente c): `entregue`/`bloqueado` — **0 ocorrências** antes e
    depois, nada a traduzir; `parcial` permanece nas duas ocorrências de tipo (ii) (níveis da
    rubrica, linhas 19 e 91); `pacote` remanescente em 1 linha (35), na acepção do conjunto
    obrigatório dentro do laudo.
  Veredito — `EXA-T20`
  Suítes: `python -m pytest` (raiz do hub) — 39 passed. Sem teste novo: o alvo é prompt de agente,
    sem superfície executável.
  Kit: `kit_check.ps1 -Mode validate`/`-Mode check-drift` — exit 0 (8 agentes, 11 skills,
    VERSION==KIT_VERSION '0.0.0').
  Espelho: `check-readme.ps1` — exit 0 (8 agentes, 11 skills, 14 guardrails, 14 seções com Fonte
    da verdade).
  Checklist de review: ok — `model: opus` e `tools:` intocados (escopo do `TK-27`); nenhum plano
    editado; nenhuma outra superfície tocada; redação sem narrativa de proveniência, sem citação de
    interlocutor e sem ID de processo no corpo do arquivo publicado.
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T13` — proxy de ocupação de contexto — `done`.** A condição de **capacidade** do
  `GOVERNANCA.md` §4.3 deixou de ser critério sem instrumento. Rota fechada por derivação da `T1`
  Sonda 3 (variante (a), hook lendo o `transcript_path`); a variante (b) segue descartada e o
  `TK-23` fecha sem sonda nova. Entregável: `.claude/tools/ocupacao.py` (novo) com duas funções
  puras — `calcular_ocupacao` toma a última entrada de assistant com bloco `usage` do `.jsonl` e
  soma `input_tokens` + `cache_read_input_tokens` + `cache_creation_input_tokens`, com fallback
  `soma(len)/4` marcado como fonte estimada; `avaliar` compara com `JANELA_TOKENS` (default
  200 000, sobrescrevível por ambiente) contra o limiar **0,50**, que é o "~50% da janela" já
  doutrinado e não número novo. Falha aberta total (qualquer erro ⇒ exit 0 silencioso, jamais
  bloqueia chamada de ferramenta) e filtro por `agent_type` para não avisar dentro de subagente.
  Hook `PreToolUse` registrado em `.claude/settings.json` com o bloco `permissions.deny` original
  preservado. Três superfícies de doutrina passaram a nomear o instrumento que existe, em vez da
  ausência dele: `GOVERNANCA.md` bullet *Capacidade*, e no `scrum-master` o Passo 10, a regra `B2` e
  o parágrafo de encerramento de janela. **Ramo A vencedor no primeiro mecanismo tentado**, provado
  ao vivo com hook de sonda descartável e revertido: `hookSpecificOutput.additionalContext` chega
  injetado ao turno seguinte. Ramos B e C descartados por sucesso do A, não testados.
  **Confirmação que o executor não podia produzir:** o instrumento disparou no contexto principal do
  orquestrador durante o próprio fechamento desta tarefa, o que resolve a limitação que ele
  registrou como inferida — `agent_type` é de fato ausente no contexto principal, senão o hook teria
  ficado em silêncio. Verificação: `pytest -q` **43 → 52 passed** (+9 testes novos, mínimo era 6);
  `dead_code.py`, `kit_check -Mode validate`, `-Mode check-drift` e `check-readme.ps1` todos em exit
  0, com 8 agentes, 11 skills e **16 guardrails inalterados**. Achado fora de escopo em
  `.gitignore:3` — ver bloco abaixo. **Laudo emitido em 2026-08-15: `aprovado`, 100%,
  bloqueante `nenhuma`, recomendação `escalar`** — as sete dimensões `conforme`, a pendência é o
  `TK-43` e a entrega fecha em `done`. Registro canônico da tarefa em
  `docs/RDO/P-0734-T13-proxy-de-ocupacao-de-contexto.md`; o laudo foi consumido e descartado
  (`DP-K` §14.4). Dois achados de processo do laudo saem com rota: o **`TK-44`** (o dossiê de
  evidência não discrimina escopo com a iniciativa inteira sem commit) e um **item de
  replanejamento** — o campo *Arquivos-alvo* do `### T13` não nomeia
  `.claude/skills/scrum-master/SKILL.md` nem `GOVERNANCA.md` §4.3, embora o campo *Conteúdo* exija
  o comportamento do `scrum-master`; a entrega tocou as duas superfícies por consequência
  obrigatória (`G-SURFACE`), e o escopo foi julgado contra o *Conteúdo*, sem punir a execução pelo
  campo incompleto.
  Consumo: ver `docs/telemetria.tsv`.

**Achado da `EXA-T13` — `TK-43`: o hub distribui um kit cuja configuração de hook é ignorada pelo
git.** `.claude/settings.json` está em `.gitignore:3`, sob o comentário "Configuração local de
máquina — nunca canônica". A `T13` registrou ali o hook do proxy de ocupação porque o dossiê nomeia
esse arquivo como alvo, e o instrumento funciona na máquina do dono — mas nada dele viaja para
consumidor nenhum, e `kit_check` não o vê. A `T14` (telemetria sem turno de agente) tem o mesmo
alvo e herda o mesmo defeito. É questão de arquitetura de distribuição do kit, não de execução:
decidir se hook canônico ganha residência versionada própria com materialização no `settings.json`
local, ou se o proxy de ocupação é assumido como instrumento só-do-hub. Sobe ao dono.

**Janela encerrada por escalada em 2026-08-15** — a `T13` fechou `aprovado` 100%, e a recomendação
`escalar` do laudo dispara `B1`: a pendência sobe ao dono e o loop **PARA**, mesmo com veredito
aprovado. A janela também cruzou o teto de trabalho, com o aviso disparado pelo próprio instrumento
da `T13` (`B2`) — encerramento normal, não falha. **Próxima tarefa:** a **decisão do dono sobre o
`TK-43`** — **decidida no mesmo dia**: hook canônico ganha residência versionada própria, com
materialização no `settings.json` local. A decisão fecha o *quê* e deixa o *como* em aberto (onde
mora o hook versionado, como materializar sem sobrescrever configuração de máquina do consumidor, o
que `kit_check` passa a exigir), de modo que o próximo passo é uma **rodada de replanejamento** que
autora o dossiê da correção e reescreve o da `T14`, cuja rota o achado invalida — não a delegação de
uma tarefa existente (`G-PLANREADY`). Fila registrada: [replanejamento: `TK-43` + reescrita do
dossiê da `T14`] → `T29` → `T30` → [ratificação em lote: `DP-I` e `DP-J`] → `T26` → `T27` → `T12` →
`T14` → `T15` → `T16` → `T17` (dono).

- **Rodada de replanejamento `DP-R` — `TK-43` + reescrita da `T14` — concluída em 2026-08-15.** A
  decisão do dono (hook canônico com residência versionada própria e materialização no
  `settings.json` local) ganhou residência no plano como **`DP-R`** (§22), com o bloco do dono
  separado das derivações de planejamento. Fechado, com verificação no repo: o hook canônico mora em
  `.claude/hooks/hooks.json` (chave única `hooks`, comando com placeholder `{KIT_ROOT}`); a
  materialização é do `.claude/tools/hooks_sync.py` (`apply`/`check`/`drift`), que resolve a raiz
  pelo próprio caminho, cobre as duas topologias (hub e consumidor com `.claude/kit/`), preserva
  byte a byte toda chave de topo que não seja `hooks` — inclusive o `permissions.deny` — e todo hook
  não-kit, e é idempotente; `kit_check` passa a exigir canônico válido em `-Mode validate` e
  materialização em dia em `-Mode check-drift`, com falha específica para hook de kit escrito direto
  no `settings.json` (regressão do próprio `TK-43`). `sync-kit.ps1` não muda e `DA-3` se mantém
  (0/6 consumidores com kit materializado). Dois cards novos, partidos por volume e por natureza:
  **`T53`** (residência + materializador + guarda, `[Sonnet · implementação padrão · teto 40]`, 9
  testes nomeados) e **`T54`** (superfície que diz onde hook mora e o que viaja, `[Opus · redacao ·
  teto 25]`). A **`T14`** teve o alvo trocado de `settings.json` para
  `.claude/hooks/hooks.json` + `.claude/tools/telemetria_hook.py`, ganhou dependência da `T53` e um
  invariante de residência, com a cláusula *resultado negativo é resultado* preservada e endurecida.
  A **`T13`** teve só o campo *Arquivos-alvo* conciliado (`+.claude/skills/scrum-master/SKILL.md`,
  `+GOVERNANCA.md` §4.3), com nota datada — bullet de fechamento, RDO, telemetria e histórico
  intocados (`DP-H`). Plano em **49/60**. Achado incidental prescrito dentro da `T54`: `README.md:741`
  diz "dez skills" onde disco e tabela têm onze. **Escalada ao dono, não decidida:** o
  `permissions.deny` do guardrail 13 tem o mesmo defeito de distribuição do `TK-43` — enforcement de
  regra publicada vivendo em arquivo que o git ignora —, e estender a ratificação de hook para
  permissões é requisito novo (registrado em `DP-R` §22.5, fora da `T53`/`T54`; nada da rodada
  depende da resposta). **Próxima tarefa:** **`EXA-T53`** — dossiê em
  `docs/plans/P-0734-execucao-autonoma.md` `### T53`. Fila: `T53` → `T54` → `T29` → `T30` →
  [ratificação em lote: `DP-I` e `DP-J`] → `T26` → `T27` → `T12` → `T14` → `T15` → `T16` → `T17`
  (dono).
  Consumo: ver `docs/telemetria.tsv`.

- **Iniciativa suspensa em 2026-08-15, rebase (A) — `blocked` em 49/60.** A `T53`/`T54` foram
  **retidas pelo dono** e depois **canceladas por absorção**: elas resolviam o sub-caso do hook antes
  da regra geral, e o `TK-45` mediu que o mesmo defeito de residência tem **5 ocorrências**. A
  matéria inteira migrou para o `P-0735`; corpo das duas tarefas preservado como material absorvido,
  §5 e o dossiê da `T14` conciliados com nota datada (a dependência da `T14` passa da `T53` para a
  `RPC-T2`). O ponto escalado em `DP-R` §22.5 (`permissions.deny` do guardrail 13) **fechou sem
  requisito novo** — a invariante da régua nova o decide —, com o fecho anotado no próprio §22.5.
  Destrava no fechamento do `P-0735`.

- **`EXA-T14` — Telemetria sem turno de agente — `review` (2026-08-19).** Iniciativa retomada:
  `P-0735` fechou `done` (13/13) e a razão do bloqueio deixou de se aplicar; as dependências `T7` e
  `RPC-T2` estavam satisfeitas. **Ramo B (resultado negativo) realizado**, com evidência: sonda pelo
  método da Sonda 3 (hook descartável em `SubagentStop` via `.claude/settings.local.json`, disparo
  por invocação trivial de `context-scout`, reversão confirmada) mediu que o evento **existe** e que
  `agent_transcript_path` aponta para um `.jsonl` exclusivo do subagente com `message.usage` e
  `message.model` por entrada — mesma classe de fato que `transcript_path` na Sonda 3, e mesmo padrão
  de parse que `ocupacao.py` (`T13`) já usa; `tool_uses` seria contável por blocos `tool_use` e
  `duracao_s` pela diferença de `timestamp`. **O obstáculo não é o consumo, é a identidade da
  tarefa:** `tarefa` (coluna obrigatória de `telemetria.py append`) não é campo de schema do harness —
  existe só como texto livre no prompt do subagente, e inferi-la por regex sobre prosa arrisca não
  escrever nada ou gravar linha com `tarefa` errada. Conforme o ramo: **nenhuma** entrada em
  `.claude/projecoes.json`, **nenhum** `telemetria_hook.py` e **nenhum** teste novo (`G-DEADCODE`);
  evidência registrada como **Sonda 5** em `docs/audits/SPIKE_HARNESS_EXECUCAO_AUTONOMA.md` (payload
  literal colado, veredito `parcial, insuficiente para a automação completa`) e o fluxo vigente da
  `T7` mantido. Bateria de fechamento 4/4 em exit 0, suíte **71 passed** (piso inalterado, coerente
  com o ramo). Único arquivo tocado: o documento de sondas. **Escalada ao dono, não decidida:** o
  plano enumerava dois ramos (viável / inviável) e o medido é um terceiro — o consumo está exposto e
  só falta um **contrato** que carregue a identidade da tarefa até o hook. Bifurcar a rota exige
  decision record aprovado antes (Regra 8); nada da fila depende da resposta. Plano em **50/60**.
  **Próxima tarefa:** a decisão acima; depois dela, `EXA-T15`. Fila: [decisão do dono sobre o
  contrato de identidade] → `T15` → `T16` → `T17` (dono).
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T15` — Enxugamento dos prompts absorvidos pelos instrumentos — `review` (2026-08-19).** O
  invariante 3 do §3 foi aferido nos seis artefatos declarados e a economia medida é **−1 linha
  líquida** (734 → 733): o único texto de formato coberto por instrumento que ainda vivia num prompt
  era a **enumeração das 8 colunas** do TSV em `handover/SKILL.md:32-35`, que saiu e virou ponteiro
  para `.claude/tools/telemetria.py append` (colunas, validação de tipo/domínio e escrita atômica são
  do script desde a `T7`); em `proximo-passo/SKILL.md:151-153` a mecânica do apenso, antes descrita em
  prosa sem citar instrumento, passou a apontar para o mesmo CLI, com a regra de qual `--fonte` usar
  por cenário preservada. **Três alvos fecharam com 0 linhas removidas** — `diario-de-obras/SKILL.md`,
  `pantonic-executor.md` e `pantonic-planner.md` —, confirmado por grep dedicado
  (`RDO|laudo|telemetria|colunas|dimens|campo|formato|schema`): não há ali gabarito que um CLI passou a
  garantir. As regiões MISTO (`handover:70-112`, `proximo-passo:126-149`, `diario-de-obras:44-51`)
  foram lidas e **preservadas pela regra de corte** — relatório ao dono, checkpoint e estrutura do
  diário são regra, não formato gerado por código, e o "Cuidado" do dossiê proíbe removê-las.
  `.claude/README.md` foi **regenerado por `kit_check.ps1 -Mode generate`** (nunca editado à mão) e
  reconciliou o índice com o disco: caem `pantonic-auditor-container` e `pantonic-auditor-pyside6` (já
  deletados), entra `pantonic-reviewer`, entram as skills `redacao-doc` e `scrum-master`, e quatro
  descrições desatualizadas sincronizam. Bateria do §3 item 6 inteira em exit 0 (8 agentes, 11 skills,
  20 entradas canônicas; 16 guardrails × 14 seções; `dead_code.py` com 0 achados) e suíte **71
  passed**, piso mantido — a tarefa não cria teste, por ser edição textual. **3 write-clusters** contra
  o teto de 8. **Teto de tool uses estourado:** 43 medidos contra 40 prescritos (+7,5%), sem mudança de
  rota nem de escopo — o excedente é da varredura de confirmação nos três alvos que fecharam em zero.
  Sem bump e sem tag (`DE-7`). Nenhum achado fora de escopo. Plano em **51/60**. **Próxima tarefa:** a
  decisão do dono sobre o contrato de identidade da `T14`, ainda em aberto; depois dela, `EXA-T16`.
  Fila: [decisão do dono sobre o contrato de identidade] → `T16` → `T17` (dono).
  Consumo: ver `docs/telemetria.tsv`.

- **Decisão do dono, 2026-08-19 — contrato de identidade da `T14`: rota (a) aceita.** O `scrum-master`
  grava a tarefa corrente num ponto de estado conhecido do kit no ato do despacho, e o hook de
  `SubagentStop` lê a identidade de lá — sem inferência por regex sobre a prosa do prompt, que foi o
  defeito medido. Registro é **checkpoint**: o decision record no plano e o card da tarefa nova são a
  **rodada de replanejamento** seguinte. **Próxima tarefa:** essa rodada; depois dela, `EXA-T16`.

- **Checkpoint de janela, 2026-08-19 — pickup da rodada de replanejamento, encerrado por capacidade.**
  Janela cruzou o teto de ~50% (`GOVERNANCA.md` §4.3) no levantamento, antes de qualquer edição do
  plano; nada foi iniciado depois do sinal (Regra 2). Estado derivado, para não se repagar: a rodada é
  **inline pelo orquestrador em Opus** (precedente `EXA-DP*-replan` na série, nunca delegada — Regra
  8); próximos identificadores livres **`DP-S`** (seção `## 23`, molde no `## 22` do `DP-R`) e card
  **`T55`**; o `## 5` do plano e o dossiê `### T14` são as duas superfícies a conciliar, e o
  denominador do plano passa de 60 para 61. **Próxima tarefa:** a mesma rodada, em contexto novo.

- **Checkpoint de janela, 2026-08-19 (2ª) — levantamento da rodada `DP-S` completo, encerrado por capacidade.** Teto de ~50% cruzado no levantamento; nenhuma edição iniciada (Regra 2). **Insumos já pagos:** Sonda 5 em `docs/audits/SPIKE_HARNESS_EXECUCAO_AUTONOMA.md:154-195` (payload traz `agent_id`/`agent_type`/`agent_transcript_path`, sem bloco de uso); `telemetria.py append` exige 8 flags; `.claude/projecoes.json` alvo `projeto` → `chaves.hooks` só tem `PreToolUse`→`ocupacao.py` com `{KIT_ROOT}`; `scrum-master/SKILL.md` "Estado do loop" `:20-38` e Passo 4 `:84-107`; `.gitignore:1-5`; no plano, §4 termina em `:2320` (último card `### T54`), §5 em `:2321-2334` (fila fecha em `T12 → T14 → T15 → T16 → T17`), molde da rodada em §22 `:4433-4534`, dossiê `### T14` em `:538-568`.
  **Desenho derivado, a transcrever (não repagar):** estado local de máquina `.claude/estado/tarefa-corrente.json` (gitignored) gravado pelo `scrum-master` no Passo 4; hook `SubagentStop` → `.claude/tools/telemetria_hook.py`, declarado no manifesto; filtro por `agent_type` + consumo do estado depois de escrever a linha (staleness limitada); sem estado ⇒ silêncio e exit 0, preservando o fluxo manual da `T7`; `tokens_k` somado do `agent_transcript_path` (`input+cache_creation+cache_read+output` por entrada `assistant`), calibrado contra o `<usage>` de um despacho aninhado trivial; ~6 write-clusters ⇒ **um** card `[Sonnet · implementação padrão · teto 40]`.
  **A escrever:** §23 `DP-S` + card `### T55` + `T55` na fila do §5 + nota datada no `### T14`; denominador 60 → **61** (plano em 51/61). **Próxima tarefa:** a mesma rodada, em contexto novo.

- **Rodada de replanejamento `DP-S` — contrato de identidade da telemetria — concluída em 2026-08-19.**
  A decisão do dono (o `scrum-master` grava a tarefa corrente num ponto de estado do kit no ato do
  despacho; o hook de `SubagentStop` lê a identidade de lá) ganhou residência no plano como **`DP-S`**
  (§23), com o bloco do dono separado das derivações de planejamento. Recusa registrada com a decisão:
  inferência por regex sobre a prosa do prompt — falha silenciosa que grava linha com `tarefa` errada,
  pior do que linha ausente, porque contamina a única fonte de número do framework. Derivações
  fechadas, todas de planejamento: o estado é **local de máquina** (`.claude/estado/tarefa-corrente.json`,
  no `.gitignore` — pela pergunta zero da régua, é fato de uma sessão numa máquina, não autoridade do
  framework); o autor é o **Passo 4** do `scrum-master`, sem contador novo na tabela do estado do loop;
  o hook é `SubagentStop` → `.claude/tools/telemetria_hook.py`, declarado em `.claude/projecoes.json`
  com `{KIT_ROOT}`, na mesma forma do `PreToolUse` → `ocupacao.py` já existente; filtro por
  `agent_type` e consumo do estado **depois** de escrever a linha, o que limita a staleness a uma
  janela; sem estado ⇒ silêncio e exit 0, preservando íntegro o fluxo manual da `T7`; números pelo
  `agent_transcript_path`, com calibração obrigatória contra o `<usage>` de um despacho aninhado
  trivial. **Um card**, `T55` `[Sonnet · implementação padrão · teto 40]`, 6 write-clusters contra o
  limite de 8 — sem razão de volume nem de natureza para partir. **Fila:** o card entra **depois da
  `T15` e antes da `T16`**, por duas razões declaradas: ele edita o Passo 4 do `scrum-master`, que é a
  superfície que a `T16` pilota (pilotar antes e mudar depois invalidaria a medida), e a automação
  existindo antes do piloto faz o próprio piloto se medir sozinho. A **`T14` não é reaberta** —
  fechou corretamente em ramo B — e recebeu só nota datada apontando para o §23. Denominador **60 →
  61**; plano em **51/61**. Sem guardrail novo (`DA-10`), sem bump e sem tag (`DE-7`). Nenhum ponto de
  parada e nada escalado ao dono. **Próxima tarefa:** **`EXA-T55`** — dossiê em
  `docs/plans/P-0734-execucao-autonoma.md` `### T55`. Fila: `T55` → `T16` → `T17` (dono).
  Consumo: ver `docs/telemetria.tsv`.

- **`EXA-T55` — identidade da tarefa por estado do loop: a série se alimenta sozinha — 2026-08-19.**
  A linha de `docs/telemetria.tsv` deixa de custar turno: o Passo 4 do `scrum-master` (`:88-93`) grava
  `.claude/estado/tarefa-corrente.json` antes de invocar o executor, e o hook novo
  `.claude/tools/telemetria_hook.py` lê a identidade de lá no `SubagentStop`, traduzindo o payload em
  chamada a `telemetria.py append` com as 8 flags e `--fonte usage`. A declaração entra em
  `.claude/projecoes.json` (chave `SubagentStop`, comando em `{KIT_ROOT}`, mesma forma do `PreToolUse`
  → `ocupacao.py`); o `settings.json` local continua sendo produto de `materializar.py apply`, nunca
  alvo de edição. `.gitignore:10` recebe `.claude/estado/` como local de máquina. Sem estado ⇒ silêncio
  e exit 0, com o fluxo manual da `T7` intacto. **A calibração obrigatória produziu achado e ele entrou
  no produto:** contra um despacho aninhado real, o total de `tokens_k` dobrava — entradas `assistant`
  do transcript repetem a mesma `message` com `usage` idêntico —, e o hook passou a **deduplicar por
  `message.id`**, com teste de regressão dedicado. Verificação: os quatro guardas da bateria em exit 0,
  mais `materializar.py check` em exit 0; suíte de **71 → 77 passed**. **Teto estourado:** 49 tool uses
  contra os 40 da classe (+22%), sem replanejamento nem mudança de rota — a calibração empírica com
  transcript real foi o excedente. Sem guardrail novo (`DA-10`), sem bump e sem tag (`DE-7`). Nenhum
  achado fora de escopo e nada escalado ao dono. Plano em **52/61**. **Próxima tarefa:** **`EXA-T16`**
  — dossiê em `docs/plans/P-0734-execucao-autonoma.md` `### T16` (piloto medido). Fila: `T16` → `T17`
  (dono).
  Consumo: ver `docs/telemetria.tsv`.

- **Rodada de decisão — a `EXA-T16` não é delegável e seu combustível está travado — 2026-08-20.**
  O pickup da `T16` parou no gate `G-PLANREADY`, antes de qualquer delegação, por dois fatos. (1) A
  `DA-1` põe o `scrum-master` no **contexto principal**, de modo que a `T16` **não é delegável** a
  `pantonic-executor` — conduz-se de um contexto principal; a premissa técnica original caiu na `T1`
  (aninhamento funciona), mas a decisão foi reexaminada e mantida por controle. (2) O combustível que
  a `T16` declara — tarefas ainda abertas do `P-0733` — está medido como inválido: o percurso a seco
  da `T13` já viu a `DHB-T1` ser recusada em **`B3`** por cabeçalho legado sem `classe`/`teto`, e as
  tarefas abertas (`T2`..`T12`, mais a `T13` do dono) seguem com cabeçalho só `[Opus]`/`[Sonnet]`.
  Pilotar assim mediria apenas a recusa — sem execução, laudo, RDO ou comparação com a série, que é o
  entregável da tarefa. **Duas decisões do dono nesta rodada:** (a) o **`TK-24`** — retrofit dos 12
  cabeçalhos do `P-0733` para `[<modelo> · classe <slug> · teto <N>]` — é executado **antes** do
  piloto, em tarefa própria de planejamento; recusadas rodar o piloto sobre a recusa (não mede nada) e
  afrouxar o gate `B3` (mudaria a superfície sob teste às vésperas de medi-la, o que a `T55` já
  registrou como invalidante); (b) a convenção `docs/RDO/evidencia/<plano>-<ID>.md`, prescrita pela
  skill sem ratificação prévia, é **ratificada como está**, fechando o achado que estava roteado à
  `T16`. Nada executado nesta rodada: a janela cruzou o teto de ocupação (§4.3) antes do retrofit.
  Plano em **52/61**. **Próxima tarefa:** o retrofit do `TK-24` (ato de planejamento, Opus), e só
  depois a `EXA-T16`. Fila: `TK-24` → `T16` → `T17` (dono).

---

## P-0735 — Residência e ponto de carga

- **Rodada de doutrina e autoria do plano — 2026-08-15.** Pedido do dono: *"vamos parar por algumas
  tarefas e resolver isso globalmente"*, com o alcance ratificado no mesmo ato — **o pacote passa a
  materializar também o `~/.claude`**. `GOVERNANCA.md` §3.1 deixou de responder *onde mora* com uma
  resposta só e passou a separar **autoridade** de **ponto de carga** em três classes (canônico ·
  ponto de carga · local de máquina), com **pergunta zero** antes das quatro, `Prec-2` promovido a
  **invariante** (*nada canônico mora só num ponto de carga*), a precedência 2 trocada para *canônico
  vence projeção* e a cláusula "e não viaja" do parágrafo de hook removida — era o sintoma registrado
  como lei. `docs/RESIDENCIA_DOUTRINA.md` ganhou §8 de conciliação datada, sem reescrever nenhuma
  linha das §§1-6 (`DP-H`): a classe `global` muda de residência sem mudar de alcance, `DR-A`
  sobrevive com motivo trocado, `DR-B` **destravado** depois de 12 dias parado como "iniciativa
  própria" nunca aberta. Plano `P-0735-RPC` autorado fechado, 9 tarefas (`RPC-T1..T9`), `DL-1..DL-9`
  todas de planejamento. Desenho: manifesto único `.claude/projecoes.json` (o `hooks_sync.py`/
  `hooks.json` da `T53` **não nasce** — vira chave do manifesto, `DL-2`); os 13 artefatos globais
  passam a canônicos em `.claude/global/`, **fora** de `.claude/skills/` e `.claude/agents/`, para não
  virarem skill ativa em todo projeto Pantonic nem colidir por nome com a própria projeção (`DL-6`,
  com o espelho intacto em 8 agentes e 11 skills); `check-drift` cobra só o alvo `projeto`, com o alvo
  `usuario` opt-in para não reprovar consumidor por projeção de máquina alheia (`DL-4`); `DA-3`
  mantida e `sync-kit.ps1` inalterado (`DL-8`). Ordem por valor validável, com `copiar → declarar →
  aplicar` tornando todo `apply` de promoção um **no-op verificável** — a máquina do dono não muda um
  byte e o `drift` verde é a prova de fidelidade. `TK-21` **não absorvido**, com motivo: rota já
  decidida (`DH-4`) e executável no `P-0733` `### T10`. **Próxima tarefa:** **`RPC-T1`** — dossiê em
  `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T1`.
  Consumo: ver `docs/telemetria.tsv`.
- **`RPC-T1` — espelho: o `README.md` fala a régua das três classes — 2026-08-15.** As 7 edições do
  dossiê aplicadas em `README.md`, único arquivo tocado. §12: o teste de residência ganha a **pergunta
  zero** antes das quatro e a pergunta 1 passa a apontar doutrina global **canônica no kit, projetada
  em `~/.claude/CLAUDE.md`**; a afirmação de que a governança das memórias **não viaja** cai, e a
  precedência 2 troca "versionado vence não-versionado" por **canônico vence projeção**, com a nota de
  que projeção não se edita no destino. §11: a prosa de abertura passa de "dez" para **onze** skills
  (disco e tabela já tinham onze; o guarda compara tabela × disco e não lê o número em prosa) e nomeia
  a **declaração de projeções** entre o que viaja, mais um parágrafo novo com `.claude/projecoes.json`,
  `.claude/tools/materializar.py` e `.claude/global/`; a frase das "skills instaladas fora do
  repositório" vira a régua nova — o que fica fora do kit é **configuração de quem opera a máquina**.
  §2: a frase do "não viaja no pacote distribuído" concilia com a invariante — o que não chega ao
  consumidor é o que fica **só** num ponto de carga, e a resposta é projetar, não excluir do pacote.
  Tabelas de agentes e de skills intactas (`DL-6`), nenhuma seção numerada nova, nenhuma linha
  `> Fonte da verdade:` alterada, nenhum guardrail novo, `CHANGELOG.md` não tocado (registro é da
  `T8`). Verificação: `check-readme.ps1` exit 0 (8 agentes, 11 skills, 16 guardrails, versão `0.0.0`,
  14 seções com fonte válida) e Grep de `não viaja`/`não viajam` em zero ocorrências. Achado fora de
  escopo indexado como **`TK-46`**. **Próxima tarefa:** **`RPC-T2`** — dossiê em
  `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T2`.
  Consumo: ver `docs/telemetria.tsv`.
- **`RPC-T2` — manifesto de projeções, materializador e o ponto de carga do projeto — 2026-08-17.**
  Três arquivos novos: `.claude/projecoes.json` (declaração canônica, chave única `alvos`, com o
  alvo `projeto` transcrevendo do `.claude/settings.json` real as duas chaves existentes — o
  `PreToolUse` do proxy de ocupação e as 6 entradas de `permissions.deny` do guardrail 13 — **sem
  alterar valor nenhum**, e o alvo `usuario` **declarado e vazio**, como o dossiê manda);
  `.claude/tools/materializar.py` (`apply`/`check`/`drift`, `--alvo projeto|usuario|todos` com
  default `projeto`, `--kit-root` e `--home`, ancoragem hub × consumidor decidida pelo nome do
  diretório-raiz — `kit` ⇒ destino no pai —, `{KIT_ROOT}` resolvendo para token POSIX `.claude` ou
  `.claude/kit` e `{HOME_CLAUDE}` para o `~/.claude` corrente); e `tests/test_materializar.py`, com
  os 12 casos do dossiê cobertos 1:1. O `.claude/settings.json` deixa de ser artefato editado à mão
  e passa a ser **produto** de `python .claude/tools/materializar.py apply`, com chave de topo não
  declarada, hook local não-kit e `permissions.allow` preservados por construção. Verificação
  específica do dossiê cumprida: a materialização foi desfeita à mão uma vez, o `drift` ficou
  vermelho (exit 1, dois problemas — hook canônico ausente e `permissions.deny` divergente) e o
  `apply` restaurou o arquivo, com `drift` de volta a exit 0. Bateria do §3 item 6 inteira em exit 0
  (`kit_check -Mode validate` — 8 agentes, 11 skills, paridade de versão —, `kit_check -Mode
  check-drift`, `check-readme.ps1`, `dead_code.py` com 0 achados) e suíte em **64 testes passando**
  (piso de 52 + os 12 novos). Fora de escopo e não tocados, como o dossiê fixou: `CHANGELOG.md` e
  `.gitignore` (são da `T8`), `kit_check.ps1` (é da `T3`), `~/.claude` e o preenchimento do alvo
  `usuario` (são da `T4`..`T6`). Nenhum achado fora de escopo. **Próxima tarefa:** **`RPC-T3`** —
  dossiê em `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T3`.
  Consumo: ver `docs/telemetria.tsv`.
- **`RPC-T3` — `kit_check` cobra o canônico e a materialização — 2026-08-17.** A régua deixa de
  depender de disciplina: `.claude/checks/kit_check.ps1` (único arquivo tocado, 65 linhas de delta)
  ganha dois blocos. No `-Mode validate`, **bloco 4** entre a paridade de versão e o agregador do
  modo, chamando `materializar.py check --alvo todos --kit-root <kitRoot>` e agregando a saída a
  `$errors`; a agregação é **condicionada a exit 1**, porque o contrato medido do materializador
  imprime uma linha de OK em exit 0 e agregá-la incondicionalmente reprovaria o modo para sempre —
  exit ≠ 0 e ≠ 1 vira "saída não interpretável" com a mensagem crua, de modo que nenhum dos dois
  modos passa em silêncio por não conseguir checar. A linha de OK passa a citar a contagem de
  entradas canônicas, derivada de `.claude/projecoes.json` por `ConvertFrom-Json` em tempo de
  execução (soma de entradas de hook por evento por alvo + itens de `arquivos`; valor corrente **1**)
  — nunca hardcodada. No `-Mode check-drift`, que **não tinha lista de erros** e saía no primeiro
  problema, entra `$driftErrors`: README regenerado e `materializar.py drift --alvo projeto` se
  agregam num relatório único antes de decidir o exit. Alvo `usuario` **fora** do `check-drift`
  (`DL-4`) — cobrar no guarda a projeção da máquina de quem executa quebraria consumidor que não
  optou por ela. Verificação específica do dossiê cumprida: com a chave `hooks` removida à mão do
  `.claude/settings.json`, `-Mode check-drift` ficou **vermelho** (exit 1, 2 problemas vindos do
  `drift`), e `materializar.py apply` restaurou o arquivo com os dois modos de volta a exit 0.
  Bateria do §3 item 6 inteira em exit 0 e suíte em **64 testes passando** (piso mantido — `tests/`
  não muda nesta tarefa, por desenho do dossiê). Fora de escopo e não tocados: `CHANGELOG.md` e
  `.gitignore` (são da `T8`), `.claude/projecoes.json`, `.claude/tools/materializar.py`, `README.md`,
  `.claude/README.md` e `~/.claude`. Nenhum achado fora de escopo. **Próxima tarefa:** **`RPC-T4`** —
  dossiê em `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T4`.
  Consumo: ver `docs/telemetria.tsv`.

- **`RPC-T4` — `.claude/global/`: a doutrina global vira canônica projetada — 2026-08-17.** Primeiro
  uso real do alvo `usuario`, com o conteúdo mais simples de provar: arquivos, sem hook. Os três
  documentos que só existiam no ponto de carga do dono passam a viajar no pacote —
  `.claude/global/CLAUDE.md` (156 linhas), `.claude/global/docs/GOVERNANCA_MEMORIAS.md` (161) e
  `.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md` (94) —, cada um conferido por **SHA256
  idêntico** ao original antes de qualquer outra edição, e o bloco `arquivos` do alvo `usuario` em
  `.claude/projecoes.json` deixa de ser `[]` para declarar os três pares `de`/`para`. A ordem
  obrigatória do dossiê foi cumprida (copiar → declarar → `apply`), e é ela que produz a prova: o
  `apply --alvo usuario` real foi **no-op** nos três alvos, com mtime inalterado (`CLAUDE.md`
  2026-08-08 18:25:20; `GOVERNANCA_MEMORIAS.md` 2026-08-01 18:58:22;
  `RECOMENDACOES_CONSUMO_GLOBAL.md` 2026-08-07 20:45:09) e `drift --alvo usuario` em exit 0. O teste
  novo (`tests/test_materializar.py`, TF `test_tf_drift_alvo_usuario_acusa_arquivo_ausente_e_fica_verde_apos_apply`)
  prova o ciclo contra fixture sintética com `--kit-root`/`--home` em `tmp_path`, conforme o §3 item
  3 — nunca contra o `~/.claude` real. Bateria do §3 item 6 inteira em exit 0 e suíte em **65 testes
  passando** (piso 64 → 65, sem perda). Fora de escopo e não tocados: `CHANGELOG.md` e `.gitignore`
  (são da `T8`), `.claude/tools/materializar.py` e `.claude/checks/kit_check.ps1` (`T2`/`T3`), os
  hooks e as skills globais (`T5`/`T6`). **Achado fora de escopo, indexado como `TK-47`:** o
  primeiro `apply --alvo usuario` real reescreveu `~/.claude/settings.json` por normalização de
  serialização JSON, com o conteúdo semanticamente preservado — comportamento pré-existente do
  materializador da `T2`, não introduzido aqui, mas que colide com o critério de verificação da
  `T5` ("difere do anterior **apenas** no caminho dos comandos"). **Decidido pelo dono no mesmo dia**
  (`DL-10`): `apply` passa a ser byte-idempotente sob equivalência semântica, e a `RPC-T10` nova foi
  autorada fechada entre a `T4` e a `T5`. **Próxima tarefa:** **`RPC-T10`** — dossiê em
  `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T10`.
  Consumo: ver `docs/telemetria.tsv`.

- **`RPC-T10` — `apply` não reescreve o que não mudou — 2026-08-17.** Quita o `TK-47` na origem:
  `write_settings` (`.claude/tools/materializar.py`) mantinha só a comparação de **texto** contra o
  `_dump` canônico, de modo que destino com formatação divergente era reescrito inteiro com o
  conteúdo semanticamente intacto. Entra o caminho **semântico** — `json.loads` do arquivo do
  destino comparado ao objeto a escrever; iguais ⇒ retorna `False` sem abrir o arquivo para escrita
  —, com `json.JSONDecodeError` caindo no comportamento anterior (destino ilegível ou ausente é
  escrito). `_dump` intocado: o formato de escrita **quando há mudança real** não estava em questão
  (`DL-10`), e `check`/`drift` não foram tocados porque ambos já comparam semanticamente — é por
  isso que a mudança não cria drift perpétuo. Dois testes novos em `tests/test_materializar.py`,
  ao lado do `test_tf_apply_e_idempotente`: TF — destino reescrito à mão com `indent=4` e ordem de
  chaves trocada sai do `apply` com **bytes idênticos**; regressão — destino a que falta a entrada
  de hook canônica **continua** sendo reescrito, no formato do `_dump`. Bateria do §3 item 6 inteira
  em exit 0 (`kit_check -Mode validate`, `kit_check -Mode check-drift`, `check-readme.ps1`,
  `dead_code.py` com 0 achados) e suíte em **67 testes passando** (piso 65 → 67, sem perda). Fora de
  escopo e não tocados, como o dossiê fixou: `CHANGELOG.md` e `.gitignore` (são da `T8`), `check` e
  `drift`, `_dump` e o `~/.claude` real — toda prova de comportamento novo em fixture `tmp_path` com
  `--kit-root`/`--home` (§3 item 3). Nenhum achado fora de escopo. Com isso a `T5` pode tratar
  qualquer diferença byte a byte no `settings.json` como sinal. **Próxima tarefa:** **`RPC-T5`** —
  dossiê em `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T5`.
  Consumo: ver `docs/telemetria.tsv`.
- **`RPC-T5` — os hooks globais e seus módulos viram canônicos — 2026-08-17.** Fecha o `TK-43` na
  forma geral: os quatro hooks registrados em `~/.claude/settings.json` deixam de existir só na
  máquina do dono. `.claude/global/hooks/` recebe os seis arquivos — os quatro scripts de hook
  (`pytest_pretooluse.py`, `verbose_cmd_pretooluse.py`, `read_cap_pretooluse.py`,
  `modelo_por_fase_userpromptsubmit.py`) mais os helpers `pytest_filter.py` e `tail_filter.py` — e o
  alvo `usuario` de `.claude/projecoes.json` passa a declarar os quatro registros (matchers
  `Bash|PowerShell`, `Read` e `UserPromptSubmit`, `timeout: 15`, comando por `{HOME_CLAUDE}`) mais os
  seis pares `de`/`para`. `statusline.py` e a chave `statusLine` ficaram fora, por `DL-3`. Não existe
  `statusMessage` nas entradas vivas, de modo que a cláusula de transcrição do dossiê saiu vazia.
  **A execução foi encontrada já feita** por sessão anterior do mesmo dia, encerrada antes do
  fechamento (mtime dos artefatos 20:25-20:26, posterior à última linha de telemetria da `RPC-T10`,
  18:47), sem bullet e sem consumo medido — daí a tarefa ter sido **verificada, não reexecutada**:
  seis arquivos byte-idênticos aos de `~/.claude/hooks/` (`diff -q` em todos), declaração conferida
  contra a tabela do dossiê, `~/.claude/settings.json` vivo resolvendo exatamente os quatro comandos
  declarados com as chaves de topo preservadas (`model`, `effortLevel`, `switchModelsOnFlag`,
  `statusLine`, `permissions`), `materializar.py drift --alvo usuario` em exit 0, e o teste
  `test_tf_apply_alvo_usuario_preserva_chaves_de_topo_e_grava_hooks_declarados`
  (`tests/test_materializar.py:295`) provando as cinco chaves em fixture `tmp_path` com `--home`.
  Bateria do §3 item 6 inteira em exit 0 (`kit_check -Mode validate`, `kit_check -Mode check-drift`,
  `check-readme.ps1`, `dead_code.py` com 0 achados) e suíte em **68 testes passando** (piso 67 → 68,
  sem perda). Dois dos quatro hooks se provaram vivos na própria sessão de verificação — o cap de
  Read barrou a leitura integral do diário e o de comando verboso barrou um `ls -R`. **Achado fora de
  escopo, indexado como `TK-49`:** o hook do alvo `projeto` é materializado com **caminho relativo**
  (`python .claude/tools/ocupacao.py`, de `{KIT_ROOT}/tools/ocupacao.py`), então basta o cwd de uma
  chamada de ferramenta sair da raiz do repositório para o hook falhar — e hook `PreToolUse` que
  falha **bloqueia toda ferramenta da sessão**, não só o comando. Medido ao vivo nesta sessão.
  **Decidido pelo dono no mesmo dia:** `{KIT_ROOT}` passa a ser resolvido para caminho absoluto na
  escrita do `settings.json`, em tarefa própria, para que nenhum consumidor herde o defeito.
  **Próxima tarefa:** **`RPC-T11`** (o `TK-49`) — dossiê em
  `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T11`.
  Consumo: ver `docs/telemetria.tsv` (`nao_medido` — a sessão que executou a tarefa se perdeu).

- **`RPC-T6` — as seis skills e o agente `context-scout` — 2026-08-17.** Fecha o `DR-B`, aberto desde
  2026-08-03: os artefatos executáveis que a doutrina versionada invoca deixam de existir só no ponto
  de carga. `.claude/global/skills/` recebe as seis skills (`context-prep`, `doc-map`, `lean-test`,
  `memory-diet`, `onboard`, `test-tiers`) e `.claude/global/agents/` recebe o `context-scout.md`,
  todos cópia byte a byte conferida por `diff -q`; cada diretório de origem continha só o `SKILL.md`,
  de modo que a cláusula de arquivo auxiliar do dossiê saiu vazia. O alvo `usuario` de
  `.claude/projecoes.json` passa de 9 para **16** pares `de`/`para`. O `DL-6` foi respeitado e é
  verificável: nada foi escrito em `.claude/skills/` nem em `.claude/agents/` deste repositório, e as
  contagens do kit seguem em **8 agentes e 11 skills** nos dois guardas. Teste novo
  `test_tf_apply_alvo_usuario_cria_diretorio_intermediario_e_nao_toca_irmao`
  (`tests/test_materializar.py`), que prova o `apply` criando `skills/<nome>/` inexistente no destino
  sem tocar irmão não declarado — suíte de **68 para 69**, sem perda. Ordem do ato cumprida
  (copiar → declarar → `apply --alvo usuario` **no-op**, respondendo "ja atualizado" → `drift --alvo
  usuario` em exit 0). Bateria do §3 item 6 inteira em exit 0 (`kit_check -Mode validate`,
  `kit_check -Mode check-drift`, `check-readme.ps1` com os 16 guardrails inalterados, `dead_code.py`
  com 0 achados). Sem bump, sem tag e sem linha de `CHANGELOG.md`, e nenhum ponteiro de doutrina
  tocado — as duas coisas são escopo da `T7` e da `T8`. Nenhum achado fora de escopo.
  **Desvio de fila, registrado:** o bullet da `RPC-T5` declarava a **`RPC-T11`** como próxima, e esta
  sessão despachou a `T6` por ler o `(7/11)` do índice como se a `T11` estivesse fechada, sem
  verificar. A `T11` **continua aberta** — medido nesta sessão: `kit_root_placeholder()`
  (`.claude/tools/materializar.py:70-74`) ainda devolve caminho relativo e o `.claude/settings.json`
  vivo ainda grava `python .claude/tools/ocupacao.py`, que é o defeito do `TK-49`. Sem retrabalho: a
  `T6` só acrescenta pares de arquivo sob `{HOME_CLAUDE}` e não toca comando de hook, de modo que as
  duas tarefas são ortogonais. **Próxima tarefa:** **`RPC-T11`** (o `TK-49`) — dossiê em
  `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T11`.
  Consumo: ver `docs/telemetria.tsv`.

- **`RPC-T11` — `{KIT_ROOT}` resolve para caminho absoluto — 2026-08-18.** Fecha o `TK-49` na origem:
  `kit_root_placeholder` (`.claude/tools/materializar.py`) passa a devolver `kit_root.as_posix()`, e o
  `command` gravado no `settings.json` do alvo `projeto` deixa de depender do cwd da chamada de
  ferramenta. Nome da função preservado; a docstring que afirmava "nunca o caminho físico absoluto"
  passa a afirmar o oposto, com a razão (o destino é local de máquina — `.gitignore:3` —, e o cwd não
  é garantido), e o parágrafo correspondente da docstring de módulo acompanha. A regra de topologia
  migrou para `_kit_marker_prefix(kit_root)`, privada, que devolve o marcador **relativo**
  (`.claude/kit` ou `.claude`) e passa a alimentar `is_kit_command`: sem ela a classificação por
  substring leria a entrada relativa já instalada como hook não-kit, a preservaria ao lado da nova e
  deixaria o hook defeituoso vivo. `_referenced_file`, `check`, `drift` e o alvo `usuario` intocados.
  Testes: quatro asserções migradas de literal para caminho derivado da fixture `tmp_path` — e **não
  seis**, como o dossiê previa: os dois setups em forma relativa (`hook_antigo.py`, `obsoleto.py`)
  continuam válidos justamente porque o marcador de classificação permaneceu relativo, o que os torna
  cobertura da compatibilidade retroativa e não dívida. Dois testes novos:
  `test_tf_apply_grava_command_absoluto_e_arquivo_referenciado_existe` e
  `test_tr_apply_substitui_entrada_de_kit_relativa_antiga_por_absoluta_unica` (regressão do `TK-49` —
  destino com a entrada relativa antiga sai do `apply` com **uma** entrada só, a absoluta). Suíte de
  **69 para 71**, sem perda. **Correção de número no dossiê:** ele partia de 68 → 70; o piso real era
  69, elevado pela `RPC-T6`, e o orquestrador re-derivou antes do despacho. **Correção de âncora:** o
  `obsoleto.py` estava em `:474`, não `:437`. **Ordem do ato, revista no despacho:**
  `test_tr_drift_projeto_ok_no_repositorio_real_depois_do_apply` (`tests/test_materializar.py`) chama
  `apply` contra o repositório real, de modo que rodar a suíte inteira já reescreve o `settings.json`
  vivo da sessão — a execução rodou primeiro `-k "not repositorio_real"` (18 verdes), depois provou à
  mão `python <abs>/.claude/tools/ocupacao.py` a partir de cwd fora da raiz (exit 0), e só então o
  `apply` real (`settings: atualizado`) e o `drift --alvo projeto` real (exit 0). Bateria do §3 item 6
  inteira em exit 0 (`kit_check -Mode validate`, `-Mode check-drift`, `check-readme.ps1`,
  `dead_code.py` com 0 achados). O `settings.json` resultante difere do anterior **apenas** no
  `command` do hook (`python D:/workspaces/PantonicApp/.claude/tools/ocupacao.py`). Sem bump, sem tag
  e sem linha de `CHANGELOG.md`. Nenhum achado fora de escopo. Com este fechamento a ordem do §5 está
  restabelecida. **Próxima tarefa:** **`RPC-T7`** — dossiê em
  `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T7`.
  Consumo: ver `docs/telemetria.tsv`.
- **`RPC-T7a` — os ponteiros da doutrina publicada para artefato global — 2026-08-18.** Primeira das
  duas fatias da `T7`, **partida por orçamento no gate de delegação**: a varredura `~/.claude`
  re-derivada no despacho mediu **14 write-clusters** contra o limite de 8, e o dossiê foi cortado em
  `T7a` (doutrina publicada: `GOVERNANCA.md`, `README.md`, `.claude/README.md`) e `T7b` (kit
  executável: `.claude/skills/**`, `.claude/agents/**`). Sem mudança de rota, de escopo ou de
  proibições — o texto do `### T7` continua valendo para as duas. Nesta fatia, 6 write-clusters:
  `GOVERNANCA.md` `:113` (ponteiro da auditoria de consumo), `:175` (Regra 3), `:252-254` (governança
  das memórias, que citava só "canônica no kit", sem caminho) e `:402` (Regra 7) passam a nomear o
  canônico em `.claude/global/`; `README.md:824-825` e `.claude/README.md:35-38` (o `context-scout`,
  promovido na `T6`) idem, na forma canônico + ponto de carga da `GOVERNANCA.md:211`. Quatro
  ocorrências foram **classificadas e mantidas** por serem menção legítima ao ponto de carga —
  `:116` (o ponto de carga é o contraexemplo do argumento), `:197` (a linha que define a classe),
  `:201` (o enunciado do invariante) e `:211` (já na forma correta) —, e as sete remanescentes estão
  justificadas uma a uma no relatório da tarefa: nenhuma trata `~/.claude` como residência. Bateria
  do §3 item 6 inteira em exit 0 (`kit_check -Mode validate` e `-Mode check-drift`,
  `check-readme.ps1`, `dead_code.py` com 0 achados) e suíte em **71 passed**, sem perda. Sem bump,
  sem tag e sem linha de `CHANGELOG.md` (a entrada única do plano é escopo da `T8`). Nenhum achado
  fora de escopo. **Próxima tarefa:** **`RPC-T7b`** — mesmo dossiê
  (`docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T7`), fatia do kit executável: âncoras
  vivas em `.claude/skills/scrum-master/SKILL.md:18,309`, `.claude/skills/proximo-passo/SKILL.md:10,49,145`
  (`:27` e `:31` são `~/.claude/projects/<slug>/memory/`, ponto de carga legítimo),
  `.claude/skills/handover/SKILL.md:8` e `.claude/skills/modelo-por-fase/SKILL.md:10,51` — a `:10`
  ainda declara o hook "fora deste repo", o que a `T5` derrubou; `.claude/agents/*.md` mediu 0
  ocorrências.
  Consumo: ver `docs/telemetria.tsv`.
- **`RPC-T7b` — os ponteiros da `proximo-passo` para artefato global — 2026-08-18.** Segunda das
  três fatias da `T7`. A varredura re-derivada no gate mediu **10 write-clusters** vivos contra o
  limite de 8, e a fatia do kit executável foi partida de novo, por orçamento e sem mudança de rota,
  escopo ou proibições: `T7b` = `.claude/skills/proximo-passo/SKILL.md` e `T7c` = `modelo-por-fase`,
  `handover` e `scrum-master`. A re-derivação também corrigiu duas afirmações do fechamento da
  `T7a`: a `:31` da `proximo-passo` **não** é ponto de carga de memória — é ponteiro para
  `~/.claude/docs/GOVERNANCA_MEMORIAS.md`, que tem canônico no kit —, e o item 3 do `### T7`
  (caminho canônico nas invocações de `context-prep`/`context-scout`) mora neste arquivo e não
  constava da lista. Nesta fatia, 5 write-clusters, todos textuais: `:10`, `:49` e `:145` passam a
  nomear `.claude/global/CLAUDE.md`; `:31` passa a `.claude/global/docs/GOVERNANCA_MEMORIAS.md`; e a
  **primeira** menção de `context-scout`/`context-prep` (`:70`) ganha os canônicos
  `.claude/global/agents/context-scout.md` e `.claude/global/skills/context-prep/SKILL.md` — as
  menções seguintes não repetem o caminho, porque o texto da skill é pago em todo turno de quem a
  invoca. Uma ocorrência **classificada e mantida**: `:27`, o `<memory-dir>`
  `~/.claude/projects/<slug>/memory/`, ponto de carga do harness sem canônico possível no kit.
  Nenhuma etapa do procedimento mudou. Bateria do §3 item 6 inteira em exit 0 (`kit_check -Mode
  validate` e `-Mode check-drift`, `check-readme.ps1`, `dead_code.py` com 0 achados) e suíte em **71
  passed**, sem perda. Sem bump, sem tag e sem linha de `CHANGELOG.md` (escopo da `T8`). Nenhum
  achado fora de escopo. **Próxima tarefa:** **`RPC-T7c`** — mesmo dossiê
  (`docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T7`), últimos 5 clusters do kit
  executável: `.claude/skills/modelo-por-fase/SKILL.md:10` (ainda declara o hook "fora deste repo",
  o que a `T5` derrubou) e `:51`, `.claude/skills/handover/SKILL.md:8`,
  `.claude/skills/scrum-master/SKILL.md:18,309`; `.claude/agents/*.md` mediu 0 ocorrências.
  Consumo: ver `docs/telemetria.tsv`.
- **`RPC-T7c` — os ponteiros das três skills restantes do kit executável — 2026-08-18.** Terceira e
  última fatia da `T7`, que fecha a tarefa: com ela nenhuma superfície executável do kit trata
  `~/.claude` como residência de conteúdo do framework. Cinco write-clusters, todos textuais. O
  primeiro é o único com **fato derrubado**: `modelo-por-fase/SKILL.md:8-12` declarava o hook de
  enforcement como "fora deste repo, não versionado no kit", o que a `RPC-T5` desfez ao promover os
  quatro hooks globais a canônicos — passa a nomear
  `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` com `~/.claude/hooks/` citado como
  projeção. Os outros quatro (`modelo-por-fase:51`, `handover:8`, `scrum-master:18` e `:309`) trocam
  `~/.claude/CLAUDE.md` por `.claude/global/CLAUDE.md` na forma nua, seguindo a convenção que a
  `T7b` fixou e que foi conferida na fonte antes de editar: o ponto de carga só acompanha a
  **primeira** menção de cada arquivo, porque o texto de skill é pago em todo turno de quem a
  invoca. Nenhuma etapa de procedimento mudou. A varredura de fechamento do item 4 do `### T7`
  deixa **8 ocorrências vivas**, justificadas uma a uma: `modelo-por-fase:11` (a projeção que o
  cluster 1 produziu, resultado pretendido), `proximo-passo:27` (`<memory-dir>`, ponto de carga do
  harness sem canônico possível), `GOVERNANCA.md:116` (contraexemplo do argumento), `:197` (linha
  que define a classe), `:201` (enunciado do invariante), `:211`, `README.md:825` e
  `.claude/README.md:37` (as três já na forma canônico + projeção pela `T7a`, não reeditadas).
  Bateria do §3 item 6 inteira em exit 0 (`kit_check -Mode validate` — 8 agentes, 11 skills, 20
  entradas canônicas —, `-Mode check-drift`, `check-readme.ps1` com 16 guardrails × 14 seções,
  `dead_code.py` com 0 achados) e suíte em **71 passed**, piso mantido — a tarefa não cria teste,
  por ser edição textual de skill. Sem bump, sem tag e sem linha de `CHANGELOG.md` (escopo da `T8`).
  Nenhum achado fora de escopo. **Próxima tarefa:** **`RPC-T8`** — dossiê em
  `docs/plans/P-0735-residencia-e-ponto-de-carga.md` `### T8`.
  Consumo: ver `docs/telemetria.tsv`.

---
