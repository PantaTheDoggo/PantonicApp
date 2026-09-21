# RDO — P-0743 · DOM-T8a

**Plano:** `docs/plans/P-0743-modelo-de-dominio.md`
**Tarefa:** `DOM-T8a` — Os ponteiros que a forma nova deixou para trás
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** as quatro regiões da árvore que mandam o modelador devolver a linha `MD-<n>` — duas em `GOVERNANCA.md`, duas em `.claude/agents/pantonic-planner.md` — apontando para `### 1.4 Registro de versões`, que é onde o ato passa a ser registrado; e o preâmbulo da skill `diario-de-obras` nomeando a seção que de fato governa a gramática do modelo. Cinco ponteiros defasados, **nenhum deles mudando papel**.

**Arquivos-alvo:** - `GOVERNANCA.md` - **dois** pontos, medidos em 2026-09-20 e re-derivados no despacho (`I-5`): a linha `| **Modelagem** |` da matriz de responsabilidades da §3, 95 (bloco **R1**); e a linha `| modelador |` da tabela de papéis da `### 3.2`, 388 (bloco **R2**) - `.claude/agents/pantonic-planner.md` - **dois** pontos, medidos em 2026-09-20 e re-derivados no despacho (`I-5`): as quatro linhas do item `## 1. Modelo conceitual` do esqueleto da Fase 3, 165-168 (bloco **R3**); e o parágrafo `**O modelo antes das tarefas.**`, 180-191 (bloco **R4**) - `.claude/skills/diario-de-obras/SKILL.md` - **um** ponto, medido em 2026-09-21 e re-derivado no despacho (`I-5`): as duas linhas do preâmbulo de `## Gramática legível por máquina` que nomeiam a seção de origem da subseção do modelo, 135-136 (bloco **R5**). **A subseção `### Modelo de domínio (seção do plano)` não é tocada**: ela está correta desde a `DOM-T8`

**Verificação:** **Censo do token** (`D-50`), que percorre os dois arquivos inteiros: ``` grep -c 'MD-' GOVERNANCA.md ``` imprime `0` (hoje imprime `1`, medido 2026-09-20). ``` grep -c 'MD-' .claude/agents/pantonic-planner.md ``` imprime `0` (hoje imprime `2`, medido 2026-09-20). ``` grep -c 'carrega estado' .claude/agents/pantonic-planner.md ``` imprime `0` (hoje imprime `2`, medido 2026-09-20): as duas ocorrências falam de **andamento** e os blocos R3 e R4 as reescrevem com a palavra certa, agora que o modelo carrega estado inicial e final. ``` grep -c 'lista de mudanças' .claude/agents/pantonic-planner.md ``` imprime `0` (hoje imprime `1`, medido 2026-09-20). Literais que **entram**, cada um inteiro numa linha só do bloco: ``` grep -cF -e 'a linha do registro de versões que registra o ato' GOVERNANCA.md ``` imprime `1` (hoje imprime `0`) — bloco R1. ``` grep -cF -e 'a linha do ato em `### 1.4 Registro de versões`' GOVERNANCA.md ``` imprime `1` (hoje imprime `0`) — bloco R2. ``` grep -cF -e 'estado inicial e final, registro de versões' .claude/agents/pantonic-planner.md ``` imprime `1` (hoje imprime `0`) — bloco R3. ``` grep -cF -e 'Nenhum elemento da seção carrega andamento' .claude/agents/pantonic-planner.md ``` imprime `1` (hoje imprime `0`) — bloco R4. **Guardas — o que não pode mudar** (`D-48`, `AE-11`): ``` grep -cF -e 'resolver conflito entre o texto e a entrega' GOVERNANCA.md ``` imprime `1` (hoje imprime `1`, **inalterado**): o ato `conflito` segue com o modelador até o Marco 4. ``` sed -n '/^| papel | o que faz diante do modelo |/,/^$/p' GOVERNANCA.md | grep -c '^|' ``` imprime `9` (hoje imprime `9`, **inalterado**): cabeçalho, separador e **sete** papéis. ``` grep -c '^| \*\*' GOVERNANCA.md ``` imprime `15` (hoje imprime `15`, **inalterado**): a matriz de responsabilidades não ganha nem perde linha. **O ponteiro da skill** (bloco R5): ``` grep -cF -e '§5 e é' .claude/skills/diario-de-obras/SKILL.md ``` imprime `0` (hoje imprime `1`, na linha 135, medido 2026-09-21). ``` grep -cF -e '§5 e §15 — onde as duas divergem, governa a §15' .claude/skills/diario-de-obras/SKILL.md ``` imprime `1` (hoje imprime `0`, medido 2026-09-21). ``` grep -c 'transcreve' .claude/skills/diario-de-obras/SKILL.md ``` imprime `2` (hoje imprime `2`, **inalterado**): a outra ocorrência é o preâmbulo do `P-0739`, de outro plano, que este card não toca. ``` python .claude/tools/backlog.py check ``` imprime `check: OK — nenhuma violação.` e sai `0`.

**Pronto quando:** os cinco censos imprimem `0`, os cinco literais de entrada imprimem `1`, os quatro guardas imprimem os mesmos números de hoje, `backlog.py check` sai `0` e o sinal de fidelidade das cinco regiões foi devolvido. **Nenhum item deste `Pronto quando` se apoia em frase escrita pelo executor sobre a própria entrega** (`I-11`, `D-50`): a fidelidade do literal é conferida pelo revisor, por diff contra a §17.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-21
- **Depende de:** `DOM-T8`
- **Fundamento:** `D-24`, `D-28`, `D-29`, `D-48`, `D-49`, `D-50`, `D-51`; invariantes `I-3`, `I-4`, `I-5`, `I-11`, `I-13`. O card transcreve a **§17** deste plano. Nasceu do `AE-17`, no escalonamento `ESC-6`: a `DOM-T8` remove a última residência do token `MD-<n>` e quatro regiões continuavam exigindo-o, sem card que as re-declarasse. O quinto ponto entrou no `ESC-7` (`AE-18`): o preâmbulo da skill manda ler a §5 deste plano, que a §15 substituiu em quatro das seis linhas — **é ponteiro, não texto**, e por isso cabe aqui e não numa reabertura da `DOM-T8`, que fechou `aprovado 100%` e cujo aceite está satisfeito.
- **Oração do modelo:** `M-1`, `M-8` - M-1: O modelo de um plano passa a descrever o que o plano entrega como objetos e operações encadeadas: cada objeto com o contrato que a implementação precisa, e cada operação nomeando quem age, o que faz e de que objetos precisa. - M-8: Um agente único é dono de todas as operações do modelo: escreve o modelo de todo plano, emenda quando uma decisão muda o que o plano entrega, resolve conflito entre o texto e a entrega e explica o contexto a quem pergunta.
- **Camada e fronteira:** doutrina (`GOVERNANCA.md`) e agente do kit (`.claude/agents/`). Nenhum código, nenhum teste.
- **Contratos/classes:** nenhum.
- **Passos:** 1. Substituir a linha 95 de `GOVERNANCA.md` pelo **bloco R1** da §17, verbatim (`I-3`). 2. Substituir a linha 388 de `GOVERNANCA.md` pelo **bloco R2**. 3. Substituir as linhas 165-168 de `pantonic-planner.md` pelas quatro linhas do **bloco R3**, preservando os **34** espaços de indentação das linhas de continuação. 4. Substituir o parágrafo das linhas 180-191 de `pantonic-planner.md` pelo **bloco R4**. 5. Substituir as linhas 135-136 de `.claude/skills/diario-de-obras/SKILL.md` pelas duas linhas do **bloco R5**. 6. Imprimir as cinco regiões e devolver o **sinal** `fidelidade conferida: R1, R2, R3, R4, R5`. 7. Rodar as verificações abaixo.
- **Restrições desta tarefa:** - **Um bloco literal por ponto** (`I-13`): cinco pontos, cinco blocos. - **Nenhuma atribuição de papel muda** (`D-48`). O ato `conflito` **permanece** na linha 95 e na tabela de papéis; nenhuma linha entra na tabela de papéis e nenhuma sai; nenhuma outra célula da linha 95 é tocada. O que muda é só a forma do que o modelador devolve, e a `Verificação` publica os dois guardas que o afirmam. - As demais linhas da tabela de papéis (`planejador`, `consultor`, `revisor`, `executor`, `orquestração`, `dono`) **não mudam**: são Marco 4 (`D-49`), e a régua da `D-43` as tranca. - Não tocar `.claude/agents/pantonic-model-designer.md`: é a `DOM-T9a`, e a ordem é proposital. - Na skill, **só** as duas linhas do preâmbulo mudam. A subseção `### Modelo de domínio (seção do plano)` é entrega fechada da `DOM-T8` e **não se reabre** (`I-3`); as quatro linhas do preâmbulo que falam do `P-0739` e do `backlog.py` são de outro plano e **não se tocam**. - Nenhuma contingência deste card cria arquivo (`I-10`). Não commitar (`I-6`).
- **Não fazer:** - Não tocar a `### 3.2` fora da linha 388: os blocos `P1`, `P2` e `P3` que a `DOM-T7` publicou são fidelidade conferida e **não se reabrem** (`I-3`). - Não tocar `GOVERNANCA.md` §9, cuja enumeração de agentes já está defasada e está fora de escopo (§11). - Não alterar a anatomia do card nem o item `4a` da Fase 4 de `pantonic-planner.md`: a `DOM-T5` os fechou e eles não citam o token.
- **Contingências:** 1. Se alguma das quatro faixas não casar com o conteúdo descrito → localizar por conteúdo, com os literais de saída da `Verificação`. Literal de saída com contagem maior que a declarada → `blocked` razão `premissa`.
- **Testes:** nenhum teste automatizado — a entrega é doutrina publicada. Quem a afere são os censos da `Verificação`.
- **Fora do escopo desta tarefa:** o modelador (`DOM-T9a`), o instrumento (`DOM-T9`), o modelo deste plano (`DOM-T10`), e tudo que muda papel (Marco 4, trancado pela régua da `D-43`).

## Execução

**Consumo:** 22 tool uses, 67.1 k tokens, 113.3 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: fidelidade conferida: R1, R2, R3, R4, R5
laudo: P-0743: antes de despachar a DOM-T9a, re-derivar as linhas de aceite dos seis literais da §18 - o aceite do R5 da DOM-T8a era inalcancavel por construcao (literal quebrado em duas linhas) e a mesma autoria produz os cards restantes.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

O discriminante foi o diff byte a byte dos cinco blocos da §17 (plano 3562, 3569, 3578-3581, 3589-3601, 3612-3613) contra a arvore: GOVERNANCA.md 95 e 388, pantonic-planner.md 165-168 (34 espacos de indentacao nas linhas de continuacao) e 180-192, SKILL.md 135-136; uma ocorrencia exata por bloco, zero divergencia. Os quatro guardas de "nao mudou" saem 1, 9, 15 e 2 e os cinco censos saem 0: nenhuma atribuicao de papel se moveu (D-48, AE-11). O token MD-<n> nao sobrou em residencia orfa do kit - o que resta esta em pantonic-model-designer.md (DOM-T9a) e modelo.py (DOM-T9), ambos com card. A linha de aceite vermelha do R5 nao era vermelho de entrega: o texto esta na arvore identico ao da residencia, quebrado nas mesmas duas linhas em que a residencia o publica.

## Fechamento

**Desdobramento:** aprovado
