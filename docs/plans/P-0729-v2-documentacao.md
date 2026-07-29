# P-0729 — V2 / Estágio 4: README espelho e fechamento da versão 2.0.0

**Iniciativa:** `PANTONIC-V2` — Estágio 4 de 4 (fechamento).
**Origem:** pedido do dono (2026-07-29): *"É necessário um README que seja um espelho dos documentos
atuais, de modo que um humano consiga ler um único arquivo, entender as premissas, filosofias e
escolhas do PantonicApp, e, principalmente, conseguir decidir sobre esse framework sem precisar ler
os demais artefatos."*

**Planejador:** Opus (2026-07-29). **Executor por tarefa:** T2 (redação do README) em **Opus** — é
síntese de doutrina, a fase mais intelectual da iniciativa; as demais em Sonnet; T5 com o dono.

**Estado:** `blocked` — razão: *depende do Estágio 3 inteiro `done`* (`P-0729-v2-melhoria` = parte A,
doutrina herdada; `P-0729-v2-melhoria-candidatos` = parte B, autorada pelo Estágio 2 T6). Espelhar um
framework que ainda está mudando produz um espelho que nasce errado.

**Este plano também fecha a iniciativa:** T4 acumula a **distribuição aos consumidores** — a Fase 4
do `P-0722`, mapeada para cá em `P-0729-v2-melhoria` §1. A propagação acontece **uma vez**, no
fechamento, e não a cada estágio (DM-6).

**Idioma:** **PT-BR** (decisão do dono, 2026-07-29). Todo o corpus — doutrina, planos, skills,
agentes — é PT-BR; um README em inglês seria o único artefato traduzido e um canal permanente de
drift.

---

## 0. O problema real deste estágio

Um README "espelho" tem um modo de falha conhecido: nasce fiel e envelhece mentindo. E ele mente
com autoridade, porque é o **único** arquivo que o leitor vai ler — é essa a exigência do dono. Este
plano trata o espelho como um artefato com **fonte da verdade declarada por seção** e um **guarda
executável de drift**, não como um documento de boa vontade. Sem o guarda, o README é o pior
artefato do repositório em vez do melhor.

Segunda exigência, igualmente literal: o leitor precisa **decidir** sobre o framework. Decidir exige
saber onde ele **não** serve, o que ele custa e o que ele deliberadamente recusa a fazer — não só o
que ele promete. Um README que só descreve virtudes falha no teste de aceitação de §4, por desenho.

## 1. Esqueleto obrigatório do README (13 seções)

Ordem e conteúdo fixados aqui para que o T2 execute redação, não arquitetura. Meta de tamanho:
**400-550 linhas** — abaixo disso não cabe a decisão; acima, o leitor volta a precisar de um índice,
e o espelho falhou.

| § | Seção | O que precisa responder | Fonte da verdade |
|---|---|---|---|
| 1 | **O que é** | Framework de governança + arquitetura para aplicações desktop Python/PySide6 construídas por agentes de IA. Em 3 parágrafos, sem jargão interno | `GOVERNANCA.md` §1 |
| 2 | **Para quem é / para quem não é** | Perfil de projeto e de dono onde compensa; e os casos em que **não** compensa (projeto pequeno, web, equipe grande com CI própria, quem não paga por contexto) | Este plano + §1 |
| 3 | **As cinco premissas** | Desktop-first; Python+PySide6+MVVM; obsessão por clean architecture; core comum reusável; extensão só por plugin | `GOVERNANCA.md` §1 |
| 4 | **A filosofia em seis escolhas** | Cada escolha no formato **escolha → alternativa rejeitada → por quê → o que custa**: (a) custo governado por fase de modelo; (b) uma tarefa por contexto; (c) guardrail executável acima de convenção; (d) plugins acima de configuração; (e) TDD com piso de regressão; (f) hub único distribuído por git em vez de cópia | `GOVERNANCA.md` §3, §4, §5, §7, §9 |
| 5 | **O modelo econômico** | Por que o framework existe: contexto reenviado × peso do modelo. Modelo por fase, orçamento de turnos, e o fato contraintuitivo de que **delegar a subagente é higiene de contexto, não economia de tokens** | `~/.claude/CLAUDE.md` Regra 7; `GOVERNANCA.md` §3 |
| 6 | **O ciclo de vida** | 4 artefatos → diário de obras → tarefa atômica → executor em contexto limpo → guardrails-check → handover → `execute o próximo passo`. Um diagrama `mermaid` e um exemplo concreto de tarefa atômica real | `GOVERNANCA.md` §4, §6 |
| 7 | **Anatomia do kit** | Tabela dos agentes e das skills, uma linha cada: nome, modelo, quando dispara | `.claude/README.md` |
| 8 | **Os guardrails** | Tabela: regra → como é enforceada (**teste executável** \| **gate de review** \| **instrução de agente**). A coluna do meio é o ponto alto do framework e precisa ser honesta sobre o que ainda é só texto | `GOVERNANCA.md` §7 |
| 9 | **Como adotar em 10 minutos** | Sequência exata de comandos (`git subtree add`, `sync-kit.ps1`, `kit-exclude.txt`) + o que o consumidor deve ajustar (os "fatos estáveis" dos agentes) e o que nunca deve tocar (o subtree) | `GOVERNANCA.md` §9, §10 |
| 10 | **O que este framework não resolve** | Limites honestos: não é CI/CD, não gerencia equipe, não substitui revisão humana, não impede custo alto se o dono ignorar os gates, não foi validado fora do stack desktop Python | Este plano |
| 11 | **Decisões e o que as motivou** | ADR compacto — cada decisão com a **evidência medida** que a produziu (o executor em Opus com 71 turnos; as ~300 linhas de código morto testado; as três premissas de plataforma que caíram por sonda curta; o symlink que exigia privilégio no Windows). É o que separa este framework de uma lista de boas intenções | `GOVERNANCA.md` §3; `docs/plans/*.md` fechados |
| 12 | **Versão, changelog e mapa dos documentos** | Versão vigente, o que mudou na 2.0.0, e a tabela "quer saber X? leia Y" apontando os documentos-fonte | `VERSION`, `CHANGELOG.md`, `docs/DOC_MAP.md` |
| 13 | **Devo adotar? (FAQ de decisão)** | 6 perguntas fechadas com resposta direta — incluindo pelo menos duas cuja resposta honesta é "não adote" | Todas as acima |

**Regras de redação:** cada seção abre com a linha `> Fonte da verdade: <arquivo> §<seção>`; nada de
"veja o documento X para entender" no corpo (isso é exatamente o que o dono pediu para eliminar);
zero referência a decisão interna sem explicar o que ela significa para quem chega de fora.

## 2. Tarefas

### T1 — `docs/DOC_MAP.md` do hub [Sonnet]
- **Objetivo:** o hub tem quatro documentos acima de 500 linhas (`P-0721` 619, `P-0725-hub-unico`
  834, e os planos desta iniciativa) e nunca teve DOC_MAP — a Regra 4 do CLAUDE.md global o exige, e
  o §12 do README vai apontar para ele.
- **Arquivos-alvo:** `docs/DOC_MAP.md` (novo), via skill `doc-map`.
- **Pronto quando:** todo documento > 500 linhas do hub tem entrada com âncoras de seção e padrão de
  Grep de acesso; o mapa cabe em uma tela.

### T2 — Redigir o README espelho [**Opus**]
- **Objetivo:** o entregável central da iniciativa.
- **Arquivos-alvo:** `README.md` (raiz — hoje inexistente).
- **Método:** seguir §1 seção a seção. Fontes lidas por Grep/âncora, não integralmente (o próprio
  framework proíbe leitura integral de doc grande). Onde a doutrina for ambígua ou tiver envelhecido,
  **não inventar consenso**: registrar como achado da execução no fim deste plano e escrever o que é
  verdade hoje.
- **Pronto quando:** as 13 seções existem, cada uma com a linha de fonte da verdade; 400-550 linhas;
  §10 e §13 contêm afirmações desfavoráveis reais (um README sem elas reprova em §4); nenhuma
  remissão do tipo "leia o documento X para entender".

### T3 — Guarda de drift do espelho [Sonnet]
- **Objetivo:** impedir que o README envelheça mentindo — o risco declarado em §0.
- **Arquivos-alvo:** `.claude/checks/check-readme.ps1` (novo); integração como modo do
  `.claude/sync-kit.ps1 -Check` ou entrada na skill `guardrails-check` (o que for menos intrusivo,
  decidido na execução com uma sonda de 1 comando); `VERSION`/`KIT_VERSION`/`CHANGELOG.md`.
- **O que o guarda verifica** (tudo mecânico, zero julgamento):
  1. Todo agente em `.claude/agents/*.md` aparece na tabela do §7; todo item da tabela existe.
  2. Toda skill em `.claude/skills/*/SKILL.md` aparece no §7; e vice-versa.
  3. A versão citada no §12 é igual a `VERSION` e a `.claude/KIT_VERSION`, e os dois coincidem.
  4. O número de guardrails do §8 é igual ao de `GOVERNANCA.md` §7.
  5. Toda seção do README tem a linha `> Fonte da verdade:` e o arquivo citado existe.
- **Verificação:** o guarda falha ao se adicionar um agente sem atualizar o README, e passa no
  estado corrente.
- **Pronto quando:** as duas verificações acima passam; sai `exit 1` em divergência e `0` limpo.

### T4 — Fechar a versão 2.0.0 e distribuir [Sonnet] — *acumula `P-0722` Fase 4*
- **Objetivo:** entregar o V2 que o dono pediu, com o significado correto de MAJOR, e **avisar o
  consumidor** — a distribuição da iniciativa inteira acontece aqui, uma vez só.
- **Arquivos-alvo:** `VERSION` e `.claude/KIT_VERSION` → `2.0.0`; `CHANGELOG.md` (seção `2.0.0`
  consolidando toda a iniciativa: benchmarking, guardrails novos, mudanças adotadas, README);
  `GOVERNANCA.md` §9 (uma linha apontando o README como porta de entrada humana do framework);
  `git tag kit-v2.0.0`.
- **Justificativa do MAJOR a registrar no CHANGELOG:** a superfície que o consumidor consome mudou
  (guardrails novos vinculantes + artefatos novos no kit + README canônico). Se ao chegar aqui
  **nenhuma** mudança exigir ação do consumidor, registrar isso e sair em `1.x` — semver que mente
  sobre compatibilidade custa mais do que a satisfação de escrever "2.0.0".
- **Nota de migração (para o `PantonicVideo`, único consumidor real hoje):** o que muda ao rodar
  `sync-kit.ps1`, em especial se algum override declarado em `kit-exclude.txt` colidir com artefato
  novo do kit, e quais guardrails novas passam a valer para os agentes daquele projeto.
- **Limite inviolável (`GOVERNANCA.md` §10a):** a divergência de versão do consumidor é
  **reportada**, nunca aplicada por agente. Detectar e agir são atos distintos; não existe threshold
  de severidade que justifique pular a separação. Esta tarefa não toca o repositório do consumidor.
- **Pronto quando:** os dois arquivos em `2.0.0` (ou a justificativa contrária escrita); CHANGELOG
  consolidado com a nota de migração; tag criada; o guarda do T3 passa; a divergência de versão do
  `PantonicVideo` está reportada ao dono, com nenhuma alteração feita naquele repositório.

### T5 — Teste de aceitação do espelho [dono]
- **Objetivo:** verificar a exigência literal do dono — *decidir sobre o framework sem ler os demais
  artefatos*.
- **Método:** o dono (ou um leitor externo) lê **apenas** o `README.md` e responde, sem abrir
  nenhum outro arquivo:
  1. O que este framework faz por mim que eu não teria de graça?
  2. Em que tipo de projeto ele seria um erro?
  3. Quanto ele me custa — em disciplina e em dinheiro?
  4. Qual a primeira coisa que eu faço para adotá-lo, e a primeira que eu quebro se fizer errado?
  5. O que ele deliberadamente recusa a fazer, e por quê?
  6. Como eu descubro que a minha cópia está desatualizada?
- **Pronto quando:** as 6 respostas saem do README sozinho. Qualquer pergunta que exija abrir outro
  arquivo **reabre o T2** com a lacuna nomeada — e a reabertura é o resultado esperado na primeira
  rodada, não um fracasso.

## 3. Riscos

- **README bonito e falso** — o modo de falha central (§0). Mitigação: T3 (guarda mecânico) + T5
  (aceitação por leitura cega).
- **Espelho virar terceiro documento de doutrina**, divergindo de `GOVERNANCA.md` a cada edição.
  Mitigação: linha `> Fonte da verdade:` por seção; edição de doutrina acontece na fonte e desce
  para o README, nunca o contrário — regra a escrever no próprio §12.
- **Tamanho:** 13 seções tendem a 800+ linhas. Mitigação: teto declarado em §1; o que não couber é
  sinal de que pertence ao documento-fonte, não ao espelho.
- **Publicidade:** o repositório é público (`github.com/PantaTheDoggo/PantonicApp`) e o README passa
  a ser sua fachada. Mitigação: §11 cita evidências medidas do próprio projeto — nenhuma delas
  contém segredo, mas o T2 confere isso explicitamente antes de fechar.

## 4. Decisões (fechadas no planejamento)

| id | Decisão | Valor | Motivo |
|---|---|---|---|
| **DD-1** | Idioma | PT-BR | Decisão do dono; todo o corpus é PT-BR e um único artefato traduzido é canal permanente de drift |
| **DD-2** | Um arquivo, não um site | `README.md` na raiz | A exigência é "um humano lê um único arquivo"; qualquer split reintroduz o problema que o README resolve |
| **DD-3** | Espelho com fonte declarada | `> Fonte da verdade:` por seção + guarda executável | Espelho sem guarda envelhece mentindo, e mente com autoridade por ser o único arquivo lido |
| **DD-4** | Aceitação por leitura cega | 6 perguntas de decisão, T5 | Testa a exigência real (decidir) em vez da aparente (existir um README) |
| **DD-5** | MAJOR condicionado | `2.0.0` se houver mudança que exija ação do consumidor; caso contrário `1.x` com justificativa | Meta do dono é o V2, mas semver é contrato com o consumidor, não placar da iniciativa |
