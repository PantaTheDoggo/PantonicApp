# RDO — P-0740 · LM-T2

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T2` — `B0` e `B1`: a cadência da janela na prosa do `scrum-master`
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — o que faz a janela **continuar ou parar**, escrito na doutrina do loop. Cobre os defeitos 4 e 5 da §3 e absorve a `AUT-T3`. Nenhuma linha de código: esta tarefa edita **um** arquivo de prosa.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md`

**Verificação:** (tarefa de redação: verificação **por efeito no arquivo-alvo**. Os itens 1 e 3 foram **corrigidos pelo `ESC-6`** e re-rodados nos **dois** mundos, conforme `DM-24` (iii); os itens 2, 4 e 5 vieram do `ESC-3` e foram **reconferidos** aqui) 1. Comando em **bloco cercado**, não em code span — o literal contém crase (`DM-24` (i)): ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern '| `B0` |' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido no `ESC-6` nos dois mundos:** **0** antes da entrega (a linha não existia) e **1** depois. A forma anterior deste item usava crase **dupla**, artefato de escape do code span, e devolvia **0 nos dois mundos** — não discriminava nada, e é o `AE-19`. 2. `pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'pendência substantiva' -SimpleMatch | Measure-Object).Count"` → ≥ 1. Baseline medida: **0**. 3. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'roteada ao planejador' -SimpleMatch | Measure-Object).Count" ``` → **0** (a rota velha desapareceu). **Medido:** **1** antes da entrega, na linha `:216`, e **0** depois. O padrão anterior deste item procurava `planejador` **em negrito**, que nunca existiu no arquivo: dava **0 nos dois mundos** (`AE-19`). Foi corrigido à mão pelo `scrum-master` no despacho — e é por isso que este item passou, enquanto o item 1, não conferido, parou a entrega. 4. `pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern '--atribuir' -SimpleMatch | Measure-Object).Count"` → ≥ 1 (a prosa cita o comando que a `LM-T2a` expõe). Baseline medida: **0**. 5. `python -m pytest tests/ -q` → verde, **sem número fixo de piso** (`DM-23`): o piso é o total que a árvore tiver **no despacho**, re-medido por quem despacha e registrado no dossiê; esta tarefa **não acrescenta teste** e **não pode reduzir** esse total — é o que tranca a suíte de conformance contra edição de doutrina. Referência histórica, não aceite: `165 passed` em 2026-09-19 (`ESC-5`).

**Pronto quando:** a tabela do bloco B tem `B0` antes de `B1` com os dois textos literais acima; a lista *O que obriga parada*, o Passo 9, o Passo 10 e o relatório de encerramento estão em dia com eles; e as cinco linhas de `Verificação` saem como escritas.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `review` — posta em `review` pelo `ESC-6` em 2026-09-19, **sem redespacho**. A entrega existe na árvore, está completa e verde; o que falhou foram **duas linhas de `Verificação` do card**, corrigidas abaixo. Mesma disposição e mesmo fundamento da `LM-T1` na `RP-2` (`DM-12` (iii), `GOVERNANCA.md` §7 item 17, cláusula emendada por esta mesma execução): existe entrega que satisfaz o entregável sob as decisões vigentes → bloqueio **de aceite**, a rodada corrige a redação e a tarefa **não se refaz**. Quem julga a árvore contra o dossiê corrigido é o `pantonic-reviewer`. Medido no `ESC-6` com os comandos corrigidos: item 1 → **1**, item 2 → **1**, item 3 → **0**, item 4 → **1**, suíte **165 passed**. Antes disso era `ready` — **reescrita pelo `ESC-3` (2026-09-18)**. A versão anterior era anterior às lições das rodadas `RP-1`..`RP-5` e foi **recusada no `G-PLANREADY`** pelo loop, sem gastar executor (`AE-14`): mandava o executor decidir onde criar uma "função de atribuição" que não tinha residência, listava três testes sem sujeito executável e repetia um piso vencido. O módulo foi partido em três pela `DM-19`: **esta** carrega só a prosa do loop.
- **Esforço:** medium
- **Depende de:** `LM-T2a` — as duas regras novas **citam o comando** que ela expõe, e publicar prosa que manda rodar um comando inexistente é o `AE-5` de novo (doutrina antes do instrumento). Mais `DM-19` (residência da atribuição) e a *Diretiva de execução do `P-0740`*, item 2 (a janela vai até o marco validável; pendência substantiva vira escalonamento ao consultor).
- **Produto do módulo:** (a) regra **`B0`** nova, avaliada **antes** de `B1`; (b) `B1` reescrita em torno de **pendência substantiva** e roteada ao **consultor de plano**, com a janela seguindo; (c) as três superfícies do mesmo arquivo que citam `B1` postas em dia — a lista *O que obriga parada*, o Passo 10 e o relatório de encerramento —, mais a linha do Passo 9 sobre o número do hook, que o `AE-3` mediu errado cinco vezes nesta janela.
- **Âncoras medidas no `ESC-3` (2026-09-18; re-derivar no despacho, o arquivo é da orquestração):** `### Bloco B — continuar ou encerrar a janela` em `.claude/skills/scrum-master/SKILL.md:202`; cabeçalho da tabela em `:206-207`; linha `B1` em `:208`; `B2` `:209`; `B3` `:210`; `B4` `:211`; lista *O que obriga parada* em `:215-218`; Passo 9 em `:138-166`, com o parágrafo do `<usage>` em `:157-159`; Passo 10 em `:167-175`, com a linha `- **Ação:**` em `:173`; relatório de encerramento em `:237` (`- Plano conduzido e regra que encerrou a janela (\`A1\`..\`A9\` ou \`B1\`..\`B4\`, pelo identificador).`). 1. Inserir, **antes** da linha `B1` da tabela do bloco B, a linha nova: ``` | `B0` | vermelho de verificação, ou item de `pendencia=`, **atribuível a arquivo fora dos `Arquivos-alvo` da tarefa** — atribuição **medida** por `python .claude/tools/review_evidence.py --plano <plano> --tarefa <ID> --desde <ref> --atribuir`, nunca julgada de memória | não é pendência da tarefa: registra `AE-<n>` com a atribuição medida, **não rebaixa** a entrega, não refaz laudo e **segue** por `B4` | ``` 2. Substituir a linha `B1` inteira por: ``` | `B1` | **pendência substantiva**: `recomendacao=escalar` no laudo, **ou** `pendencia=` cujo texto **não** seja integralmente atribuível a arquivo fora dos alvos por `B0` | registra a pendência como `AE-<n>` em `## Achados da execução` do plano, descarta o laudo e escala ao **consultor de plano** (`pantonic-consultant`, instanciado uma vez por execução), que devolve decisão e reparo: a janela **segue** com o que ele devolver. **PARA** só se o consultor classificar o impedimento como **estratégico**; ao dono chega só isso (`G-NOASK`, `GOVERNANCA.md` §7 item 18) | ``` 3. Na linha 3 da seção (`Avaliado **depois** de \`A6\`..\`A9\`…`), acrescentar ao fim da frase: ``` A precedência dentro do bloco é `B0` → `B1` → `B2` → `B3` → `B4`: o que é atribuível a arquivo alheio sai em `B0` e nunca chega a `B1`. ``` 4. Na lista *O que obriga parada*, substituir o trecho `ou pela recomendação \`escalar\` do laudo (\`B1\`), roteada ao planejador —` por: ``` ou pela recomendação `escalar` do laudo (`B1`), roteada ao **consultor de plano** — ``` e acrescentar, ao fim do mesmo bullet, a frase: ``` Escalonamento ao consultor **não** encerra a janela: encerra-a só a classificação `estratégico` que ele devolver. ``` 5. No Passo 10, substituir a linha `- **Ação:** aplicar a tabela do bloco B, também por precedência.` pelo texto: ``` - **Ação:** aplicar a tabela do bloco B, também por precedência, começando por `B0` — a atribuição de arquivo é **medida** pelo comando do `B0`, não julgada de memória. ``` 6. No relatório de encerramento, trocar `(\`A1\`..\`A9\` ou \`B1\`..\`B4\`, pelo identificador)` por: ``` (`A1`..`A9` ou `B0`..`B4`, pelo identificador) ``` 7. No Passo 9, ao fim do parágrafo que manda apender a linha de `docs/telemetria.tsv`, acrescentar: ``` O número da linha é o do bloco `<usage>` da notificação, **conferido**: o hook `SubagentStop` grava sozinho e já gravou valor inflado (`AE-3`); linha do hook que divergir do `<usage>` é corrigida à mão pelo loop. E o hook **não dispara** quando o subagente é retomado por `SendMessage` — nesse caso a linha é apensada pelo loop, como todas as outras. ```
- **Testes:** **nenhum `pytest`** — e isto é declaração, não omissão. As regras `B0`/`B1` são prosa lida pelo `scrum-master`; não há sujeito executável nesta tarefa. A versão anterior do card listava três TFs sobre "o comportamento do loop", que nenhum runner executa (`AE-14`). O que é executável — a atribuição — vive na `LM-T2a` e é testada lá.
- **Restrições desta tarefa:** o bloco A fica **intocado** — `A1`..`A9` não mudam de condição nem de ação. `B2`, `B3` e `B4` ficam **literais**: só a precedência passa a nomear `B0`. Nenhuma regra nova além de `B0`. O arquivo é da orquestração e muda fora do ciclo de tarefa: re-derivar as âncoras no despacho (contingência 1).
- **Não fazer:** não tocar `.claude/tools/review_evidence.py` (é a `LM-T2a`) nem `.claude/tools/telemetria_hook.py` (é a `LM-T2b`); não tocar `GOVERNANCA.md` (a doutrina da unidade de trabalho é a `LM-T4`); não tocar `.claude/agents/` (`DM-17`); não escrever teste `pytest` para regra de prosa; não commitar.
- **Contingências:** 1. se qualquer um dos literais a substituir (passos 2, 4, 5, 6) não existir no arquivo exatamente como transcrito → parar e sinalizar `blocked` razão `premissa`, citando a linha encontrada; 2. se `python -m pytest tests/ -q` ficar vermelho → seguir com a entrega e devolver `contingência 2 acionada: <arquivo::teste> vermelho fora dos alvos` (esta tarefa não toca Python nenhum).

## Execução

**Consumo:** 14 tool uses, 78.4 k tokens, 275.3 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: Bloco A sem regra para recomendacao=escalar (AE-9) deixa o B1 recem-entregue inalcancavel pela sua primeira condicao, e o card que o plano elegeu dono da materia fechou sem resolve-la: precisa de card novo antes de a cadencia B0/B1 valer na pratica.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
