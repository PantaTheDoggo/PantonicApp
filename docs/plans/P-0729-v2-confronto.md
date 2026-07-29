# P-0729 — V2 / Estágio 2: confronto dos relatórios e diagnóstico do PantonicApp

**Iniciativa:** `PANTONIC-V2` — Estágio 2 de 4.
**Origem:** pedido do dono (2026-07-29): *"De posse dos relatórios, use o modelo mais inteligente
para confrontar os relatórios emitidos e crie um relatório consolidado de pontos fracos e fortes do
PantonicApp comparado com outras práticas registradas publicamente."*

**Planejador:** Opus (2026-07-29). **Executor por tarefa:** T1/T2 em Sonnet (mecânica de extração e
tabulação — barato e verificável), T3/T4 em **Opus** (é o juízo comparativo que o dono pediu), T5
com o dono.

**Estado:** `blocked` — razão: *depende de `P-0729-v2-benchmarking` `done`* (sem os 20 relatórios
não há o que confrontar). Não escolhível pela `proximo-passo` até lá. Decisões fechadas (§6).

**Relação com os demais planos:** consome os artefatos do Estágio 1 e **produz o Estágio 3B** — a
última tarefa deste plano (T6) autora `P-0729-v2-melhoria-candidatos.md` **já fechado**, a partir do
`CANDIDATOS.md` ratificado pelo dono. É a aplicação do **gate de publicação** (G-PLANREADY item 5,
decisão do dono 2026-07-29): plano que depende de insumo futuro não se publica com um vão — ele
nasce como tarefa nomeada do plano que produz o insumo. O Estágio 3A
(`P-0729-v2-melhoria.md`, doutrina herdada do `P-0722`) já está fechado e independe deste.

---

## 0. Escopo

**Em escopo:** o auto-retrato do PantonicApp no mesmo esquema do corpus; a matriz de cobertura; o
relatório consolidado de forças/fraquezas/lacunas; o backlog priorizado de mudanças candidatas; a
ratificação do dono.

**Fora de escopo:** editar `GOVERNANCA.md`, `ARQUITETURA_PANTONICA.md`, `.claude/` ou qualquer
skill/agente. Este estágio **só escreve em `docs/benchmark/`**. A tentação de "já corrigir enquanto
analisa" é o modo de falha clássico aqui, e ela tem um plano próprio: o Estágio 3.

## 1. A regra que governa este estágio

**Nenhuma afirmação sobre um framework externo entra em qualquer artefato deste estágio sem citar
um `BM-NN` específico.** O modelo mais caro é também o mais fluente em inventar doutrina plausível
sobre projetos famosos que ele "conhece" do treino — e no Estágio 3 essa invenção viraria mudança
real na governança. O corpus de 20 relatórios com URL por linha existe para ser a **única** fonte
admissível. Afirmação sobre o próprio PantonicApp cita `arquivo:linha` do repositório.

## 2. Tarefas

### T1 — Auto-retrato do PantonicApp no esquema do corpus [Sonnet]
- **Objetivo:** descrever o PantonicApp nas mesmas 16 dimensões (D1..D16), com o mesmo rigor de
  evidência, para que ele seja a 21ª coluna da matriz — e não um caso especial descrito em prosa.
- **Arquivos-alvo:** `docs/benchmark/BM-00-pantonicapp.md` (novo).
- **Fontes admissíveis (todas locais):** `GOVERNANCA.md`, `ARQUITETURA_PANTONICA.md`,
  `.claude/README.md`, `.claude/agents/*.md`, `.claude/skills/*/SKILL.md`, `.claude/sync-kit.ps1`,
  `VERSION`/`.claude/KIT_VERSION`/`CHANGELOG.md`, `docs/plans/*.md` (planos fechados = evidência de
  processo real, não de intenção) e `~/.claude/CLAUDE.md` (Regras 1-7, que são doutrina de fato do
  framework, ainda que morem fora do repo — registrar essa localização como achado de D15).
- **Regra específica de honestidade:** dimensão onde o Pantonic tem **intenção mas não
  materialização** é marcada `PARCIAL — decidido, não escrito`, com ponteiro para o plano que a
  decidiu. Aplica-se em especial às 5 guardrails do `P-0722` (G-DEADCODE, G-PLANFIDELITY,
  G-PREMISE, G-PLANREADY, G-EXECREADY) e à skill `modelo-por-fase`: decididas em 2026-07-22, ainda
  não redigidas na doutrina — mescladas ao Estágio 3. Marcá-las como existentes falsearia o
  diagnóstico; ignorá-las produziria recomendações redundantes.
- **Pronto quando:** D1..D16 preenchidas com `arquivo:linha` em cada linha; rodapé com as 3
  práticas transplantáveis substituído por "N/A — sujeito da comparação"; toda dimensão `PARCIAL`
  com ponteiro para o plano de origem.

### T2 — Matriz de cobertura dimensão × framework [Sonnet]
- **Objetivo:** produzir o instrumento mecânico que permite ao Opus (T3) enxergar o padrão sem
  reler 21 relatórios — onde todo mundo faz algo que o Pantonic não faz, e onde o Pantonic está
  sozinho.
- **Arquivos-alvo:** `docs/benchmark/MATRIZ_DIMENSOES.md` (novo).
- **Formato:** 16 linhas (D1..D16) × 21 colunas (BM-00..BM-20). Célula ∈ {`—` ausente, `~` parcial,
  `+` pleno} seguida do ponteiro `BM-NN§Dx`. Abaixo da matriz, três listas derivadas mecanicamente:
  (a) **dimensões em que o Pantonic é `—` e ≥5 frameworks são `+`** (lacuna de consenso);
  (b) **dimensões em que o Pantonic é `+` e ≤2 frameworks são `+`** (diferencial ou excentricidade —
  o T3 decide qual); (c) **preocupações listadas em "Dimensões fora da grade"** por ≥2 relatórios
  (candidatas a D17+).
- **Regra:** classificar é mecânico e verificável; **interpretar não é tarefa desta T**. Nenhuma
  frase de opinião no arquivo.
- **Pronto quando:** nenhuma célula vazia; as três listas derivadas presentes; cada célula com
  ponteiro.

### T3 — Relatório consolidado de forças, fraquezas e lacunas [**Opus**]
- **Objetivo:** o entregável central do estágio — o juízo comparativo que o dono pediu.
- **Arquivos-alvo:** `docs/benchmark/RELATORIO_CONSOLIDADO.md` (novo).
- **Estrutura obrigatória:**
  1. **Veredito em uma página** — onde o PantonicApp está à frente da prática pública, onde está
     atrás, e a única coisa que ele deveria mudar primeiro.
  2. **Uma seção por dimensão (D1..D16)**, cada uma com: como o Pantonic resolve hoje; como os
     frameworks públicos resolvem (citando os `BM-NN` relevantes); e um **veredito** ∈ {`MANTER`,
     `ADOTAR`, `ADAPTAR`, `REJEITAR`}. `REJEITAR` **exige motivo escrito** — uma prática popular
     recusada sem motivo é a mesma falha de rigor que adotá-la sem motivo.
  3. **Dimensões novas (D17+)** — preocupações pertinentes que o Pantonic nunca considerou,
     vindas da lista (c) do T2 e da leitura do Opus. É o pedido explícito do dono ("identificar
     outras dimensões que eu possa não ter considerado"). Cada uma com: o que é, quem a pratica,
     por que é pertinente a um framework desktop Python/PySide6 movido a agentes, e o que custaria.
  4. **Descartes justificados** — práticas populares deliberadamente recusadas por conflitarem com
     as premissas Pantonic (desktop-first, custo por turno, uma tarefa por contexto, clean
     architecture). Esta seção protege o framework de adotar por mimetismo; sua ausência seria o
     defeito mais provável de um relatório escrito por um modelo agradável.
  5. **Vieses do corpus** — o que 20 repositórios públicos **não** conseguem informar (ex.: o que
     falha em produção depois de 6 meses; custo real; projetos que morreram e não têm repo).
- **Guardrail:** zero afirmação sobre framework externo sem citar `BM-NN`; zero afirmação sobre o
  Pantonic sem `arquivo:linha` (via `BM-00`).
- **Pronto quando:** 16 dimensões com veredito; toda `REJEITAR` com motivo; seções 3, 4 e 5
  presentes e não-vazias (seção 3 vazia = a leitura foi rasa, reabre a tarefa).

### T4 — Backlog priorizado de candidatos a mudança [**Opus**]
- **Objetivo:** converter o consolidado em decisões apresentáveis ao dono — uma lista onde cada item
  é escolhível isoladamente, e não um ensaio.
- **Arquivos-alvo:** `docs/benchmark/CANDIDATOS.md` (novo).
- **Formato:** uma linha por candidato `C-NN`, com: dimensão de origem, mudança proposta em uma
  frase, artefato-alvo (`GOVERNANCA.md §X`, `.claude/skills/<x>`, check executável, …), **impacto**
  (qual dor real ataca — custo, qualidade, ou dimensão nova), **esforço** (tarefas atômicas
  estimadas), **risco**, **dependências**, e **sobreposição com o P-0722** (qual das 5 guardrails
  mescladas ele reforça, duplica ou contradiz — coluna obrigatória, dado que o P-0722 está mesclado
  ao Estágio 3). Ordenação sugerida por impacto ÷ esforço, explicitada.
- **Regra de rastreabilidade:** todo `C-NN` aponta para a seção do consolidado que o originou.
  Candidato sem origem no consolidado é ideia do executor — não entra.
- **Pronto quando:** todo candidato rastreável; a coluna de sobreposição com o P-0722 preenchida
  para todos; nenhuma linha sem esforço estimado.

### T5 — Ratificação do dono [dono, com o orquestrador em Opus]
- **Objetivo:** fechar todas as decisões **antes** do Estágio 3 existir como plano executável — é
  literalmente a regra G-PLANREADY que este mesmo estágio recomenda ratificar.
- **Arquivos-alvo:** `docs/benchmark/CANDIDATOS.md` (coluna `Decisão` ∈ {`adotar`, `adaptar`,
  `rejeitar`, `adiar`} + uma linha de motivo quando ≠ `adotar`).
- **Método:** apresentar os candidatos em blocos por dimensão (não um a um — 1 round-trip por
  bloco, não N); recomendação do planejador visível em cada linha; o dono decide.
- **Pronto quando:** nenhum `C-NN` sem decisão registrada.

### T6 — Autorar o plano do Estágio 3B, já fechado [**Opus**]
- **Objetivo:** converter os `C-NN` ratificados num plano executável **completo** — a aplicação do
  gate de publicação (G-PLANREADY item 5): o plano dependente do benchmarking nasce aqui, fechado,
  em vez de ter sido publicado com um vão no Estágio 3A.
- **Arquivos-alvo:** `docs/plans/P-0729-v2-melhoria-candidatos.md` (novo);
  `docs/plans/_INBOX.md` (uma linha, append-only); `docs/DIARIO_DE_OBRAS.md` (linha no índice +
  bullets na sprint `SPRINT-PANTONICV2`).
- **Formato de cada tarefa do plano novo:** objetivo em uma frase, arquivos-alvo com caminho exato,
  artefatos/contratos envolvidos, verificação, critério de pronto, modelo da fase, e o `C-NN` de
  origem. Ordenadas por dependência; sem dependência, por impacto ÷ esforço.
- **Regras de decomposição:** (a) tarefa que toque doutrina (`GOVERNANCA.md`,
  `ARQUITETURA_PANTONICA.md`) e mecânica (skill, agente, script) no mesmo passe é **dividida** — são
  fases de modelo diferentes; (b) todo `C-NN` `adotar`/`adaptar` gera exatamente uma tarefa; (c)
  nenhum `C-NN` `rejeitar`/`adiar` gera tarefa; (d) nenhuma tarefa sem `C-NN` de origem — ideia nova
  do executor não entra, vira candidato para uma rodada futura.
- **Gate de publicação (bloqueante):** o plano só é apensado ao `_INBOX.md` se passar nas 5
  condições de G-PLANREADY — nomenclatura, `T1..Tn` sequenciais, **todas as decisões tomadas**,
  linear sem referência para frente, e **nenhum bloco em aberto**. Se algum candidato ratificado não
  puder ser fechado em tarefa (falta informação que só a execução revelaria), ele **não entra no
  plano**: vira uma tarefa de investigação própria, com teto de sondagem e entregável de descoberta.
- **Pronto quando:** o plano existe, fechado pelas 5 condições; todo `C-NN` `adotar`/`adaptar` tem
  tarefa; a linha do inbox e as linhas do diário existem; este plano fecha e o Estágio 3B é
  destravado.

## 3. Verificação de aceitação do estágio

1. `MATRIZ_DIMENSOES.md` sem célula vazia e com as três listas derivadas.
2. Amostragem adversarial: sortear 5 afirmações do `RELATORIO_CONSOLIDADO.md` e confirmar que cada
   uma resolve para um `BM-NN` e daí para uma URL real. Uma falha reprova o relatório inteiro (a
   invenção não é local — indica o método).
3. `CANDIDATOS.md` com 100% das decisões preenchidas.
4. `P-0729-v2-melhoria-candidatos.md` passa nas 5 condições de G-PLANREADY — em especial a quinta:
   nenhum bloco em aberto, nenhuma tarefa cujo conteúdo dependa de artefato inexistente.

## 4. Riscos

- **Opus escrevendo do treino em vez do corpus** — risco dominante, e a mitigação é a verificação
  adversarial de §3.2, não a boa-fé.
- **Viés de novidade:** adotar prática popular porque é popular. Mitigação: a seção "Descartes
  justificados" é obrigatória e não-vazia; e `REJEITAR` exige motivo, o que força simetria.
- **Auto-retrato generoso** (T1 descrevendo a intenção do Pantonic como se fosse implementação).
  Mitigação: `PARCIAL — decidido, não escrito` é uma classificação de primeira classe, com ponteiro
  obrigatório para o plano de origem.
- **Matriz binária escondendo grau.** Mitigação: três níveis (`—`/`~`/`+`), não dois, e o ponteiro
  na célula permite auditar a classificação.

## 5. Onde termina a fronteira deste estágio

Este estágio **decide tudo** o que diz respeito às mudanças — o quê, por quê, e (em T6) como serão
decompostas em tarefas. O que ele não faz é **executar** qualquer uma delas: nenhuma linha de
`GOVERNANCA.md`, skill, agente ou check é tocada aqui.

A ordem interna importa e não é negociável: `CANDIDATOS.md` (T4) diz *o quê* e *por quê*; a
ratificação (T5) fecha as decisões; só então a decomposição em tarefas atômicas (T6) acontece. Isso
mantém a decisão na fase intelectual (Opus) em vez de deixá-la vazar para o executor no modelo
barato — a falha medida em `P-0722` §1 — e, ao mesmo tempo, satisfaz o gate de publicação: o plano
do Estágio 3B só existe depois que não sobrou nada a decidir nele.

## 6. Decisões (fechadas no planejamento)

| id | Decisão | Valor | Motivo |
|---|---|---|---|
| **DC-1** | O PantonicApp entra na comparação como par | `BM-00` no mesmo esquema D1..D16 | Comparar prosa contra tabela produz conclusão enviesada a favor de quem foi descrito em prosa |
| **DC-2** | Modelo do confronto | T1/T2 Sonnet, T3/T4 **Opus** | Extrair e tabular é mecânico; julgar e priorizar é a fase intelectual (Regra 7 / GOVERNANCA §3) |
| **DC-3** | Guardrails do P-0722 no auto-retrato | `PARCIAL — decidido, não escrito`, nunca `+` nem `—` | Elas existem como decisão ratificada e não como texto vigente; qualquer outra marcação falseia o diagnóstico |
| **DC-4** | Fronteira de escrita do estágio | Só `docs/benchmark/` | Analisar e corrigir no mesmo passe é como as rotas se bifurcam sem decision record (G-PLANFIDELITY) |
| **DC-5** | Ratificação antes do plano de melhoria | T5 fecha todas as decisões antes do Estágio 3B ser escrito | Decisão postergada acaba tomada pelo executor no modelo barato — a falha medida em `P-0722` §1 |
| **DC-6** | Quem autora o plano do Estágio 3B | **T6 deste plano**, já fechado, e não um bloco aberto no Estágio 3A | Gate de publicação (G-PLANREADY item 5, decisão do dono 2026-07-29): plano com vão é escolhível pela `proximo-passo` e para o executor no meio |
