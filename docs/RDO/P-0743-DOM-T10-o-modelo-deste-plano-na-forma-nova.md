# RDO — P-0743 · DOM-T10

**Plano:** `docs/plans/P-0743-modelo-de-dominio.md`
**Tarefa:** `DOM-T10` — O modelo deste plano, na forma nova
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** a seção `## 1. Modelo conceitual` do `P-0743` reescrita na forma nova — objetos com propriedades, fluxo com `altera:`, estado inicial e estado final, registro de versões — de modo que o dono leia, em `modelo.py show`, o estado final que ele mesmo especificou. **É a entrega que o Marco 3 mede.**

**Arquivos-alvo:** - `docs/plans/P-0743-modelo-de-dominio.md` - **um** ponto, e só um: o campo `- **Oração do modelo:**` de **todos** os cards da §9, que vira `- **Operação do modelo:**`. **Medido no `ESC-10`, 2026-09-21: são 18 cards** — 14 na autoria, 16 depois do `ESC-6`, 17 com a `DOM-T9b` e 18 com a `DOM-T9c` —, e a `V2` exige o campo em cada um: sem esta conversão o `check` sai `1` dezoito vezes, e não `0` - **A seção `## 1. Modelo conceitual` NÃO é alvo deste card** (`D-52`). Quem a grava é o `pantonic-model-designer`, no despacho próprio dele, porque o gate do ato dele exige que ela já esteja no arquivo. Edição do executor nessa região é edição **fora de alvo**, e o laudo a trata como tal

**Verificação:** ``` python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md ``` sai `0` e imprime uma linha começando por `modelo: OK — ` (hoje sai `2` com `modelo: forma anterior — plano na forma de orações`, medido 2026-09-20). ``` python .claude/tools/modelo.py show --plano docs/plans/P-0743-modelo-de-dominio.md ``` sai `0` e a saída traz as seções `## Objetos`, `## Fluxo` e o estado final. **É esta saída que o dono lê no Marco 3.** ``` grep -c '^### 1.3 Estado inicial e estado final' docs/plans/P-0743-modelo-de-dominio.md ``` imprime `1`. Na árvore, antes do ato do modelador: `0` (medido 2026-09-21). **A âncora `^###` é obrigatória**: sem ela o comando imprime `9` hoje — o heading aparece citado dentro dos blocos literais deste plano —, o aceite passaria antes de a tarefa começar e não discriminaria os dois mundos (`D-54`, `AE-23`). Com a âncora, só a seção real casa, e é exatamente este heading que o instrumento exige (`.claude/tools/modelo.py:158`). ``` grep -c '^- \*\*Oração do modelo:\*\*' docs/plans/P-0743-modelo-de-dominio.md ``` imprime `0` (hoje imprime `18`, medido 2026-09-21 — um por card). O padrão é ancorado em `^- ` de propósito: conta **campo**, não citação. Contado sem a âncora, `Oração do modelo` aparece 37 vezes no plano, e as excedentes são texto de card fechado — `DOM-T5` publica o literal que remove o campo dos agentes — que **não se toca** (`I-3`). ``` grep -c '^- \*\*Operação do modelo:\*\*' docs/plans/P-0743-modelo-de-dominio.md ``` imprime `18` (hoje imprime `0`, medido 2026-09-21) — um campo por card, que é o que a `V2` exige. O número se re-deriva no despacho (`I-5`): é a contagem de `^### DOM-T` do plano. ``` python .claude/tools/backlog.py check ``` imprime `check: OK — nenhuma violação.` e sai `0`.

**Pronto quando:** `modelo.py check` sobre este plano sai `0`, `show` imprime a leitura do dono com estado final, `backlog.py check` sai `0`, **a linha de retorno traz a saída literal do estado de entrada do ato 2** — exit `1`, `18` violações, todas `V2` — e o **registro do loop** mostra o despacho do modelador entre os dois atos deste card. É essa dupla — saída de comando mais registro de quem despachou — que discrimina a mão certa, e **nenhuma das duas é frase do executor sobre a própria entrega** (`I-11`, `AE-12`, `D-50`, `D-52`). A seção `## 1` **não entra no aceite deste card**: ela é entrega do ato do modelador.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-21
- **Depende de:** `DOM-T9c`
- **Fundamento:** `D-31`, `D-33`, `D-34`, `D-35`, `D-37`, `D-43`, `D-52`, `D-53`; invariantes `I-3`, `I-11`, `I-15`, `I-16`. O dono nomeou este plano como o **teste do desenho**: *"nosso modelo seria o agente model designer e o modelo. Por meio da operação 'construir o modelo', receberiamos o 'modelo' no padrão esperado"*. O conteúdo do modelo é **ato do modelador** (`D-5`), e **também a gravação dele** (`D-52`): este card não redige a seção **e não a transcreve** — ele pede o ato, espera, e converte os campos dos cards depois que a seção já está no arquivo. **São dois despachos deste mesmo card, com o ato do modelador entre eles.**
- **Operação do modelo:** `OP-12` - OP-12: O modelador constrói o modelo deste plano na forma nova, e o executor converte o campo de cada card para a operação que ele materializa, com o texto e o contrato copiados. - precisa de: modelador — `.claude/agents/pantonic-model-designer.md`; front matter com nome, descrição e lista de ferramentas, e corpo com os atos, o ensinamento e o gate; as duas portas de inventário do kit contam os agentes e hoje fecham sobre dez; cadeia de papéis diante do modelo — `.claude/agents/pantonic-reviewer.md`, `pantonic-planner.md` e `pantonic-consultant.md`, mais a skill `scrum-master`; cada elo declara o que devolve e quem o lê, e nenhum elo manda fazer o que outro elo proíbe; gramática do modelo — residência única na skill `diario-de-obras`, subseção `Modelo de domínio (seção do plano)`; uma linha de tabela por elemento, com a forma à esquerda e a regra mais o código de violação à direita; instrumento do modelo — `.claude/tools/modelo.py`, verbos `check` e `show`, exits `0`, `1` e `2` com literais fixos; lê as tarefas do plano por `backlog._parse_plano` e não reescreve `backlog.py`; cada regra nova nasce com fixture e teste pelo caminho do usuário
- **Camada e fronteira:** o plano, em `docs/plans/`. Nenhum código, nenhum teste.
- **Contratos/classes:** nenhum.
- **Passos:** **Ato 1 — pedir, e parar.** 1. **Não redigir e não transcrever o modelo.** Devolver, na linha de retorno, o dossiê `Ato de modelo` de `autoria`, com os seis campos da norma, pedindo o modelo do `P-0743` na forma nova, e **sinalizar `blocked` razão `dependencia`**: o card volta à fila depois do ato do modelador. Quem conduz a sessão o despacha (`D-5`, `D-6`); nenhum agente aciona outro. Insumos a declarar no campo `Fato novo` do dossiê: a §14, a §15 e a §16 deste plano, e o ponto de partida que o dono deu — objetos `agente model designer` e `modelo`, operação `construir o modelo` (`D-31`). O campo `Restrição` do dossiê declara, literalmente, **três** coisas: (a) o ato é `autoria` e **substitui** a `## 1. Modelo conceitual` em forma anterior — **não** se cria `## 1A`, que é a forma da emenda; (b) nenhuma outra linha do plano é dele; e (c) o `check` vai acusar `V2` em toda tarefa enquanto os cards ainda citam `Oração do modelo`, e essas violações **não são dele** — devolve o ato com a saída literal (`D-53`, `DOM-T9b`). **Ato 2 — converter, depois que a outra mão agiu.** 2. **Antes de qualquer edição**, rodar `python .claude/tools/modelo.py check --plano docs/plans/P-0743-modelo-de-dominio.md` e **devolver a saída literal** na linha de retorno. O estado de entrada esperado é exit `1`, `modelo: FALHOU — 18 violação(ões)`, e **todas** as linhas começando por `V2 `. Qualquer outro estado cai nas contingências 1, 3 ou 4 — **nenhum deles se resolve editando** (`D-52`, `I-16`). 3. Conferir que a `### 1.4 Registro de versões` que o modelador gravou traz a linha da versão vigente. Se não trouxer, é ato dele incompleto: contingência 1. 4. Converter o campo de cada card da §9 de `- **Oração do modelo:**` para `- **Operação do modelo:**`, **derivando a lista do que o modelador devolveu**: cada operação do fluxo traz a própria lista `tarefas:`, e o campo de um card é o conjunto das operações que o citam. Por operação citada, os dois sub-bullets que a gramática exige (`V14`): o texto copiado e a linha `precisa de:` com o contrato de cada objeto. **É derivação mecânica da entrega do modelador, não escolha do executor.** 5. Card que nenhuma operação citar → **parar e sinalizar `blocked` razão `premissa`**, com a lista dos cards órfãos. Não inventar operação para cobri-lo, e não apagar o card: a `D-46` fechou a `Q-12` **sem afrouxar a `V2`**: card sem operação não passa no `check`, e resolver isso é replanejamento, nunca ato de executor (`D-49`). 6. Rodar as verificações abaixo.
- **Restrições desta tarefa:** - **O executor não escreve na `## 1. Modelo conceitual` — nem para corrigir.** A região não é alvo deste card (`D-52`): defeito nela é ato do modelador, e a rota é `blocked` razão `dependencia` com a saída literal do `check`. Redigir ou retocar o modelo aqui seria o executor decidindo domínio, que é o que a `D-5` concentra num agente só. - **O estado de entrada do ato 2 é evidência, não opinião**: vai na linha de retorno como saída literal do comando, nunca como frase sobre ela (`I-11`, `AE-12`). Quem confirma que o modelador agiu é o **registro do loop**, que o despachou — não o executor. - As demais seções do plano **não mudam** neste card: a fila, os achados e as decisões ficam. - Nenhuma contingência deste card cria arquivo (`I-10`). Não commitar (`I-6`).
- **Não fazer:** - Não apagar nem reescrever as orações `M-1`..`M-12` em outro lugar do plano: os cards vigentes as citam no campo `Oração do modelo`, e quebrar essas citações é defeito de coerência. - Não tocar plano nenhum do acervo (`D-3`).
- **Contingências:** 1. Se o `check` do ato 2 sair `1` com **alguma** violação que não seja `V2` — indexada por `OP-<n>`, por `secao` ou por `objeto` (`V6`, `V7`, `V15`, `V17`), ou ainda `V4`/`V14` —, a seção entregue tem defeito → devolver a saída literal e sinalizar `blocked` razão `dependencia`. A família `objeto` foi medida no `ESC-10` e é a mais provável numa autoria (`AE-22`). **Não corrigir o modelo**: corrigir é ato do modelador. 2. Se o `check` do ato 2 sair `2` (`modelo: forma anterior`) → a seção **não foi gravada**: `blocked` razão `dependencia`, com a saída literal. Não transcrever a seção você mesmo, mesmo que a tenha recebido no despacho — é a região que a `D-52` tira deste card. 3. Se o `check` do ato 2 sair `0` **antes** de qualquer edição sua → alguém já converteu os campos, e há **duas mãos** na mesma região: `blocked` razão `premissa`, com a saída literal. É exatamente o caso que o `AE-21` mediu, e ele não se resolve seguindo em frente. 4. Se um literal de aceite imprimir número diferente do declarado **e** o bloco estiver transcrito verbatim → **parar** e devolver `blocked` razão `premissa` com o comando, a contagem obtida e a linha do bloco de onde o literal sai (`I-16`, `AE-19`). Não ajustar o texto publicado, não relaxar o comando e não atribuir a falha a causa não medida.
- **Testes:** nenhum teste automatizado.
- **Fora do escopo desta tarefa:** o modelo de qualquer outro plano, e tudo que muda papel (Marco 4).

## Execução

**Consumo:** 62 tool uses, 159.2 k tokens, 306.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
