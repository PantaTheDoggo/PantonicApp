# Global Agent Rules (all projects)

## Regra 1 — Nunca iniciar execução automaticamente após aprovação de um plano

Quando o modo de planejamento (Plan Mode) é usado e o usuário aprova o plano, **não inicie a
execução automaticamente**. Pare e aguarde uma instrução explícita do usuário para começar.

**Motivo:** o usuário usa um modelo mais caro (ex.: Opus) para planejar e o Sonnet para executar.
Se a execução começar sem uma parada explícita, o modelo caro usado no planejamento acaba sendo
reaproveitado para a execução — desperdiçando custo em tarefas que deveriam rodar em um modelo
mais barato.

**Como aplicar:** ao sair do Plan Mode com um plano aprovado, encerre o turno comunicando que o
plano foi aprovado e está pronto para execução, sem chamar ferramentas de edição/execução. Só
prossiga com a implementação em uma nova mensagem/turno iniciada pelo usuário.

## Regra 2 — Integridade do contexto

Um contexto sustenta **um cenário coerente**: ele segue enquanto tudo que entra pertence a esse
cenário. Entrando material de outro cenário, ou material que contradiz o que já está lá, o
contexto está **poluído** — e contexto poluído não se recupera, se substitui.

**Motivo:** só uma condição encerra um contexto — a **coesão**, e no instante em que cai. A
**capacidade** não encerra nada: é diretriz de dimensionamento, exercida antes de a tarefa
começar.

- **Coesão** — violação **fatal e imediata**. Pare ao primeiro sinal, de forma **não graciosa**:
  nada do que for produzido depois do sinal se aproveita, não existe "termino o que está aberto e
  limpo depois" nem fechamento cerimonioso. Retorne a quem orquestra demandando
  **contexto limpo para a reexecução**.
- **Capacidade** — mesmo coeso, o desempenho cai conforme o contexto enche. A capacidade não
  interrompe trabalho em curso: ela **dimensiona o trabalho antes de começar**. Quem planeja
  delimita cada tarefa para caber num contexto coerente e coeso, autossuficiente em contexto para
  a execução, dentro de uma estimativa de **50% de ocupação da janela, com tolerância até 60%**. O
  número não é constante mágica: vem da literatura sobre decaimento de desempenho de agentes em
  função do enchimento do contexto, e é revisto se a literatura indicar outro valor.

**Sinais de poluição** (checagem obrigatória, lista não exaustiva): material de outra tarefa,
outro plano ou outra iniciativa entrou no contexto; premissa que sustentava o trabalho foi
derrubada no meio dele; a rota bifurcou ou uma decisão do dono contradiz o que já foi ingerido;
duas fontes do mesmo fato divergem sem descarte imediato; entrou informação ambígua ou
controversa que muda o que já foi feito.

**O que não é poluição:** corrigir o próprio erro, sobrescrever valor errado, refinar detalhe. A
contradição é fatal quando atinge o **cenário** (premissa, rota, contrato), e não quando atinge
um **detalhe** que o próprio contexto já substituiu.

**Consequências práticas:** para quem executa, vale **uma tarefa por contexto**, inalterado. Para
quem orquestra, conduzir um plano **é** uma tarefa: o contexto atravessa várias tarefas atômicas
sem violar nada, porque o cenário é o mesmo, e encerra na **troca de plano ou iniciativa** (troca
de cenário) ou na capacidade, o que vier antes.

**Como aplicar:** a poluição é o **único** critério de parada de execução, e a parada é **não
graciosa**: nada se inicia depois do sinal, nada do produzido depois dele se aproveita e **não há
ponteiro de retomada**, porque não há retomada — devolve-se a quem orquestra a declaração de
poluição e a demanda de reexecução em contexto limpo. Capacidade **não** interrompe tarefa em
curso: é diretriz de dimensionamento de quem planeja.

## Regra 3 — Economia de contexto (minimizar ingestão de saída descartável)

**Motivo:** saída verbosa de ferramentas (logs de teste, listagens, builds) entra inteira no
contexto e degrada qualidade/custo. Filtre na origem, não depois.

**Como aplicar:**

- **Testes pytest:** um hook PreToolUse global já reescreve comandos `pytest` puros para filtrar a
  saída (só falhas + sumário; log completo em `%TEMP%\claude\pytest_last_run.log`). Não contorne o
  filtro com pipes próprios; para depurar uma falha, use Grep no log completo. Bypass explícito
  (raro): terminar o comando com `#nofilter`.
- **Disciplina de coleta** (git, listagens, arquivos grandes, comandos verbosos, varreduras
  amplas): em projeto Pantonic*, a lista completa vive em `GOVERNANCA.md` §3 do kit — bullets
  compactos que qualquer agente do framework precisa, mesmo sem este arquivo.

## Regra 4 — Onboarding econômico e bootstrap de projeto novo

**Motivo:** a coleta inicial de informações de um agente novo é o segundo maior consumidor de
contexto depois de saída de ferramentas; índices baratos com ponteiros vêm antes de leituras
integrais (progressive disclosure).

**Como aplicar:**
- Ao iniciar trabalho num projeto com documentação extensa, use a skill `onboard`;
  se existir `docs/DOC_MAP.md`, ele é a porta de entrada obrigatória para os docs.
- Índice de memória (MEMORY.md): linhas-hook de ≤120 chars, nunca conteúdo; ao passar de
  ~40 linhas, rodar a skill `memory-diet`.

## Regra 5 — Destacar troca de modelo no meio da conversa

**Motivo:** o usuário acompanha custo/desempenho por trecho da conversa e quer saber, sem
precisar rolar para cima, qual modelo gerou cada resposta. A extensão VS Code renderiza só
CommonMark/GFM puro — sem HTML, ANSI ou cor customizada — então não existe "amarelo" literal;
o substituto é uma convenção visual fixa (confirmado via pesquisa: blockquote + negrito + emoji
são os únicos destaques nativos disponíveis).

**Como aplicar:** ao detectar no histórico um bloco `<local-command-stdout>` de troca de modelo
("Set model to X"), abrir a **primeira resposta seguinte** com:

> 🟡 **Troca de modelo:** `modelo-anterior` → `modelo-novo`

Só uma vez por troca — não repetir a cada turno enquanto o modelo permanecer o mesmo.

## Regra 6 — Governança de memórias e artefatos .claude

**Motivo:** memória com dado fora de escopo (status de sprint, lista volátil, regra já
promovida) polui o recall e desperdiça tokens em toda sessão futura. Regramento completo em
`~/.claude/docs/GOVERNANCA_MEMORIAS.md` — consultar antes de gravar memória em caso de dúvida
e em qualquer auditoria de memórias.

**Como aplicar (essência):**
- Lar canônico da memória: só **fato durável não derivável** vira memória (as demais residências —
  regra, procedimento, papel, estado de trabalho — seguem o teste de residência de
  `GOVERNANCA.md` §3.1, kit Pantonic).
- **Descobrir ≠ aprovar:** o agente **não grava memória direto**. Candidato vira uma linha em
  `<memory-dir>/_INBOX.md` (append-only) e **só o dono promove**; a única exceção é a remoção
  (ponteiro quebrado, memória obsoleta). Fila, forma da linha e ciclo:
  `~/.claude/docs/GOVERNANCA_MEMORIAS.md` §8.
- Memória: 1 fato por arquivo, ≤ ~30 linhas, `description` ≤ 120 chars; todo arquivo indexado
  no MEMORY.md (arquivo não indexado = indexar ou apagar); ponteiro quebrado remove-se na hora.
- Ao promover feedback a regra de CLAUDE.md, **apagar a memória de origem** (sem tombstone).
- Fato de escopo global não fica em memória de projeto — sobe para o CLAUDE.md global.
- Listas voláteis (ex.: roster de projetos sincronizados) têm uma única memória dona; as
  demais apontam para ela sem repetir a lista.
- Raiz de sessão canônica = raiz do repo. Não abrir sessão em subpasta de projeto nem na
  pasta-mãe dos workspaces; `.claude` em subpasta é defeito (fundir na raiz e apagar).

## Regra 7 — Economia de turnos (não só de tamanho de contexto)

**Motivo:** custo total ≈ Σ por turno (tamanho do contexto reenviado × peso do modelo); número de
turnos e peso do modelo em subagentes são alavancas tão grandes quanto o tamanho do contexto —
reduzir o contexto por turno sem governar o número de turnos e o modelo deixa a maior alavanca de
custo solta (caso medido: `GOVERNANCA.md` §3, kit Pantonic).

**Como aplicar:**
- **Batching de chamadas independentes**: leituras/greps sem dependência entre si vão na mesma
  mensagem — N leituras em 1 turno custam 1 reenvio de contexto; em N turnos custam N reenvios.
- **Cadência de testes, não só tier**: Tier 1 no máximo 2× por tarefa (após implementar, após
  corrigir) — nunca a cada micro-edição; tier superior só no fechamento.
- **Sem re-leitura de verificação**: Edit/Write falham ruidosamente; reler o arquivo editado "para
  conferir" é um turno inteiro desperdiçado.
- **Orçamento por tarefa atômica**: há um teto por classe de tarefa, calibrado pela série medida —
  não um número único aqui; a tabela de tetos é autoridade do kit (`GOVERNANCA.md` §3, em projeto
  Pantonic*). Estourar não é punição — é sinal de tarefa mal decomposta (replanejar) ou de método
  ruim (thrashing editar-testar-editar sem plano interno); reportar no handover, não simplesmente
  continuar.
- **Plano interno antes da primeira edição** — esboçar a sequência de mudanças reduz turnos de
  retrabalho.
- **Fechamento enxuto**: um único registro canônico; relatório final ao orquestrador é ponteiro +
  deltas, nunca repetir o mesmo conteúdo já escrito no registro canônico.
- **Telemetria é medida, não auto-relatada**: consumo de uma tarefa vem da notificação de
  conclusão (dado medido), nunca do auto-relato do executor (em projeto Pantonic*, a doutrina
  completa — inclusive a linha `Consumo:` — mora em `GOVERNANCA.md` §4.2).

## Regra 8 — O executor não decide, não pergunta e não muda a rota do plano

**Motivo:** decidir é fase de planejamento (modelo caro), não de execução. Um executor que
pergunta ao dono ou substitui a arquitetura aprovada por uma alternativa própria sob pressão de
obstáculo técnico faz a fase intelectual vazar para a fase barata, sem o contexto de quem decidiu.

**Como aplicar:**
- **Plano não-pronto:** se para começar o executor precisaria perguntar ou decidir algo (questão
  pendente, bloco a preencher, ramo condicional não resolvido, insumo que ainda não existe), o
  plano está incompleto — devolve ao planejamento e **não performa**.
- **Rota é do dono:** ao bater num obstáculo que ameaça a rota aprovada, o executor **para**,
  registra o achado e escala para replanejamento — nunca substitui a arquitetura por uma
  alternativa própria na mesma execução. Bifurcar rota exige decision record aprovado **antes** de
  codar a alternativa.
