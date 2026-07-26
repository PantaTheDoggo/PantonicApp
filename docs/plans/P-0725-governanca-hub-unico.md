# P-0725 — Hub único de governança: PantonicApp canônico, PantonicVideo como prova de aceitação

**Origem:** decisão do dono (2026-07-25), simplificando o escopo pela segunda vez no mesmo dia.

> "Vamos abortar o PantonicContainerForAWS. Para simplificar, vamos restringir o plano apenas ao
> PantonicApp, e quando surgir a necessidade de revisão do PantonicContainer, farei um esforço
> direcionado neste. Por ora, vou deixá-lo como legado. O plano então vai se restringir a levar o
> PantonicApp para o Github, e usar o PantonicVideo como prova de aceitação."

**Substitui** `P-0725-governanca-tres-camadas.md` (mesmo dia, nunca executado): o modelo de três
camadas condicionais morreu com a medição de que a camada 3 não tinha conteúdo próprio.

**Planejador:** Opus. **Executor:** Sonnet, exceto a Fase 1 (curadoria de doutrina → Opus).

**Estado:** **PRONTO PARA EXECUÇÃO — não iniciado.** **Nenhuma decisão do dono em aberto**:
DP-12 fechada em 2026-07-25 conforme a recomendação. Próxima tarefa = **Fase 1** (reconciliar
hub × PantonicVideo), em **Opus** por ser curadoria de doutrina.

---

## 0. Escopo

| Papel | Projeto | Nesta rodada |
|---|---|---|
| **Hub canônico** | `PantonicApp` | ✅ já é repo git publicado; falta ficar **canônico** antes de valer como fonte |
| **Prova de aceitação** | `PantonicVideo` | o projeto Pantonic\* mais maduro — se a transição não quebrar nem causar perda nele, a governança nova está aceita |
| **Legado congelado** | `PantonicContainer` | ❌ fora de escopo; revisão dirigida quando o dono quiser |
| **Abortado** | `PantonicContainerForAWS` | ❌ não tinha conteúdo próprio (13/17 artefatos byte-idênticos ao Container) |
| **Fora** | `PantonicScanlator`, `PantonicMonitor`, `PantonicPatom` | consumidores futuros, não entram agora |

**Critério de aceitação da iniciativa inteira:** o `PantonicVideo` recebe o kit do hub sem quebrar
(suíte verde) e sem perder nada (nenhum artefato local sacrificado). Aceito isso, o modelo vale
para os demais.

---

## 1. Diagnóstico medido — `PantonicApp` × `PantonicVideo` (2026-07-25)

### 1.1. Só **5** artefatos são compartilhados, e a deriva é pequena

| Artefato | Linhas App | Linhas Video | Só no App | Só no Video | Leitura |
|---|---|---|---|---|---|
| `skills/proximo-passo` | 150 | 153 | 6 | 9 | **quase sincronizado** |
| `skills/diario-de-obras` | 149 | 150 | 7 | 8 | **quase sincronizado** |
| `skills/handover` | 92 | 93 | 9 | 10 | **quase sincronizado** |
| `skills/guardrails-check` | 79 | 105 | 15 | 41 | **override legítimo** — o título de cada um já declara: `Pantonic*` (hub) × `PantonicVideo` (local) |
| `agents/pantonic-executor` | 52 | 82 | 28 | 58 | **override legítimo** — as 58 linhas extras são os "fatos estáveis" do projeto |

Ou seja: **3 skills a reconciliar de verdade** (~15 linhas de cada lado, somadas) e **2 artefatos
que já são override por desenho** e devem continuar sendo. A regularização é pequena.

### 1.2. Cada lado tem artefatos que o outro não tem — e está certo assim

**Só no `PantonicVideo` (9 agentes)** — `architect-auditor`, `clean-code`, `domain-expert`,
`integration-auditor`, `integration-executor`, `integration-expert`, `integration-planer`,
`poc-inspector`, `service-inspector`. Pipeline de absorção de POC, específico do projeto.
**Nunca sobem para o hub. Nunca podem ser apagados pela materialização.**

**Só no `PantonicApp` (11 artefatos)** — `README.md`, agentes `pantonic-auditor-arch`,
`pantonic-auditor-cleancode`, `pantonic-auditor-container`, `pantonic-auditor-pyside6`,
`pantonic-fora-da-caixa`, `pantonic-planner`, `pantonic-scout`, e skills `audit-sweep`,
`bootstrap-pantonic`, `integrar-poc`. **Vão aterrissar no `PantonicVideo` na materialização** —
é isso que DP-12 pergunta.

### 1.3. Três edições de doutrina estão **não commitadas** no PantonicVideo

`git status` marca como modificados `skills/diario-de-obras`, `skills/handover` e
`skills/proximo-passo`. São o trabalho de doutrina mais recente que existe — e é *deles* que sai a
deriva medida em §1.1. A Fase 1 lê a árvore de trabalho, não o `HEAD`; ignorá-las seria
canonizar uma versão já superada.

### 1.4. Dois riscos mecânicos medidos

- **Terminadores de linha:** o `PantonicVideo` é **CRLF** e não tem `.gitattributes`; o hub é
  **LF**. Materializar o kit LF num repo CRLF marca todo arquivo sincronizado como reescrito de
  ponta a ponta — o `git diff` da prova de aceitação vira ilegível justamente quando ele é a
  evidência.
- **258 arquivos sujos** no `PantonicVideo`, espalhados por `tests/`, `docs/`, `contracts/`,
  `services/`. `git subtree add` exige árvore limpa.

Nenhum dos dois vira decisão do dono — os dois têm solução mecânica na Fase 4 (§4).

---

## 2. Decisões

### Herdadas — fechadas, não reabrir
- **DP-1 = D** — distribuição por git a partir do hub remoto.
- **DP-7 = D1** — `git subtree` em `.claude/kit/` + materialização nos namespaces planos, com
  exclusão declarada em `.claude/kit-exclude.txt`.
- **DP-9** — resolvido pelo abort do `ForAWS`.
- **DP-10 = (a)** — override é de arquivo inteiro.
- **DP-11 = (a)** — snapshot fiel antes de reconciliar.

### Fechada nesta rodada

**DP-12 ✅ FECHADA 2026-07-25 = aceitar todos os artefatos só-do-hub, exceto
`skills/integrar-poc`.**

Racional: `integrar-poc` colide de frente com os 9 agentes `integration-*`/`poc-inspector`/
`service-inspector` que o `PantonicVideo` já tem e usa — duas doutrinas de absorção de POC no
mesmo projeto é ambiguidade, não enriquecimento. Os demais (4 auditores `pantonic-*`,
`pantonic-fora-da-caixa`, `pantonic-planner`, `pantonic-scout`, `README`, `audit-sweep`,
`bootstrap-pantonic`) são **aditivos**: aparecem como opção nova e não substituem nada que já
exista no projeto.

**Consequência operacional:** `.claude/kit-exclude.txt` do `PantonicVideo` passa a ter **3
entradas**, não 2 — os 2 overrides legítimos (§1.1) **mais** `integrar-poc`. A exclusão de
`integrar-poc` é de natureza diferente das outras duas: as duas primeiras protegem conteúdo local
de ser sobrescrito; esta impede a **chegada** de um artefato indesejado. Ambas as naturezas cabem
no mesmo arquivo, mas o `kit-exclude.txt` deve dizer qual é qual em comentário — senão, na
primeira revisão futura, alguém remove a linha do `integrar-poc` achando que protege algo que não
existe.

---

## 3. Regra nova de governança — versionamento e atualização sob comando

Pedido literal do dono. Duas metades:

**(a) Atualização é sempre iniciada pelo usuário.** Nenhum agente sincroniza kit por conta
própria, em nenhuma circunstância. Detectar divergência e agir sobre ela são atos separados; o
agente só faz o primeiro.

**(b) Checagem de versão na criação de todo plano.** Gatilho escolhido pelo dono: criação de
plano — o momento em que se decide trabalho futuro é o momento certo de saber se a doutrina base
está velha.

### Mecanismo

```
hub  PantonicApp/KIT_VERSION         "1.0.0"  — bump obrigatório em toda mudança canônica do kit
     tag git  kit-v1.0.0             na branch `kit`

consumidor  .claude/kit/KIT_VERSION  versão materializada (vem no subtree)

checagem    git ls-remote --tags <url> "kit-v*"     1 chamada de rede, sem fetch,
                                                     sem tocar a árvore de trabalho
```

**Resultado da checagem:**
- Versões iguais → segue em silêncio, sem gastar turno do dono.
- Divergentes → **reporta**: versão local, versão remota, e a pergunta *"atualizar agora ou
  postergar?"*. Registra a resposta no plano que está sendo criado. **Nunca atualiza sozinho.**
- Sem rede / remote inacessível → reporta "não verificado" e segue. Falha de rede não bloqueia
  trabalho nem vira silêncio.

### Onde a regra mora
- **Doutrina:** `GOVERNANCA.md` §10 (nova) — "Versionamento e atualização do kit".
- **Operacional:** skill `checar-versao-kit` no kit, chamada pela `diario-de-obras` na operação de
  criação/registro de plano.

O bump de `KIT_VERSION` entra como **critério de pronto** de qualquer tarefa que edite `.claude/`
do hub — versão que não sobe quando o conteúdo muda transforma o guarda em teatro.

---

## 4. Fases

### Fase 1 — Reconciliar `PantonicApp` × `PantonicVideo`
**Modelo: Opus** (curadoria de doutrina). Não depende de DP-12.

**Entrada:** as versões da **árvore de trabalho** do `PantonicVideo` (§1.3), não do `HEAD`.

1. **3 skills compartilhadas** (`proximo-passo`, `diario-de-obras`, `handover`): para cada linha
   divergente, decidir de que lado está a regra mais nova e por quê. Resultado: **uma** versão
   canônica no hub que contém o melhor dos dois. Critério: a diferença carrega uma **regra**? Se
   for reformatação, o hub vence por já estar em LF; se for regra, vence quem tem a regra.
2. **Escrever `.claude/kit-exclude.txt` no `PantonicVideo` com as 3 entradas** — antes de qualquer
   sync. Essa é a linha de defesa contra a perda que a prova de aceitação quer excluir:

   ```
   # PROTEGE conteúdo local de ser sobrescrito pela materializacao:
   guardrails-check      # perfil PantonicVideo, decidido em 2026-07-25 (P-0721 Fase 1a)
   pantonic-executor     # carrega os "fatos estaveis" da arquitetura do projeto

   # IMPEDE a chegada de artefato indesejado (DP-12):
   integrar-poc          # colide com os 9 agentes integration-*/poc-inspector locais
   ```
3. Espelhar de volta ao `PantonicVideo` o que foi decidido a favor do hub, para os dois ficarem
   idênticos nos 3 arquivos compartilhados. **É isto que "quando eles forem sincronizados"
   significa** — a partir daqui o hub é fonte, e a cópia do Video é derivada.

**Critério de pronto:** `proximo-passo`, `diario-de-obras` e `handover` byte-idênticos entre hub e
`PantonicVideo` (a menos de terminador de linha); `kit-exclude.txt` escrito com as 3 entradas
acima, cada uma com o comentário que diz de que natureza ela é.

---

### Fase 2 — Versionamento + regra anti-drift
**Modelo: Sonnet. Teto: 20 tool uses.** Implementa o §3 inteiro.

1. `KIT_VERSION` = `1.0.0` na raiz do hub.
2. `GOVERNANCA.md` §10 nova, com as duas metades (a) e (b) do §3.
3. Skill `checar-versao-kit` (`.claude/skills/checar-versao-kit/SKILL.md`) — procedimento,
   comando de checagem, os três resultados possíveis, e a proibição explícita de auto-atualizar.
4. Ganchar a chamada na skill `diario-de-obras`, operação de criação de plano.

**Proibição:** não inventar auto-update, nem "atualizar se for só patch". A regra é comando do
usuário, sem exceção de severidade.

---

### Fase 3 — Publicar o hub canônico
**Modelo: Sonnet. Teto: 10 tool uses.**

1. Commit + push das Fases 1 e 2 para `origin/main`.
2. `git subtree split --prefix=.claude -b kit` → `git push origin kit`.
3. `git tag kit-v1.0.0 kit` → `git push origin kit-v1.0.0`.

**Critério de pronto:** `git ls-remote --tags origin "kit-v*"` devolve `kit-v1.0.0` — isto é, o
mecanismo de checagem do §3 já tem o que checar.

---

### Fase 4 — Prova de aceitação no `PantonicVideo`
**Modelo: Sonnet. Teto: 35 tool uses.** Depende da Fase 3. Sem decisão do dono pendente.

**Resolve os dois riscos mecânicos do §1.4 sem tocar no trabalho em curso do dono:**

- **Os 258 arquivos sujos:** a prova roda num **`git worktree` limpo** criado a partir do `HEAD`
  (`PantonicVideo` já usa `.claude/worktrees/`). A árvore suja não é commitada, stashada nem
  tocada. Só se exige que as 3 edições de kit do §1.3 estejam commitadas — elas são insumo da
  Fase 1 e precisam existir no `HEAD` para a prova ser reproduzível.
- **CRLF × LF:** `.gitattributes` no `PantonicVideo` **escopado só ao kit** —
  `.claude/** text=auto eol=lf`. Normaliza o caminho sincronizado e **não** renormaliza os ~1500
  arquivos do resto do repo. Commit próprio, antes do subtree.

**Sequência:**
1. Tag de retorno: `git tag pre-kit-migration` — e o comando de rollback escrito no plano **antes**
   de começar, não depois.
2. Baseline: rodar a suíte **Tier 3** uma vez e **anotar a contagem** — sem número de antes não
   existe prova de "não quebrou".
3. `.gitattributes` escopado (acima), commit próprio.
4. `git subtree add --prefix=.claude/kit <URL> kit --squash`.
5. Materializar via `sync-kit.ps1`, respeitando `kit-exclude.txt`.
6. **Verificar as duas metades da aceitação:**
   - **Não perdeu:** os 9 agentes locais e os 2 overrides declarados seguem presentes e com o
     conteúdo de antes. Conferir por hash contra a tag `pre-kit-migration`.
   - **Não chegou o que foi excluído:** `skills/integrar-poc` **não** existe em
     `.claude/skills/` depois da materialização (DP-12). Exclusão que não é verificada é
     exclusão que ninguém sabe se funcionou.
   - **Não quebrou:** Tier 3 verde, contagem ≥ baseline do passo 2; `tests/conformance/` verde.
7. `git diff --stat` legível — se estourar em arquivos não relacionados ao kit, o passo 3 falhou e
   a prova para.

**Critério de pronto:** os dois lados do critério do dono demonstrados com número, e o rollback
testado ao menos uma vez (`git reset --hard pre-kit-migration` num worktree descartável).

---

### Fase 5 — Registrar a decisão
Se a Fase 4 passar: inverter a doutrina em `GOVERNANCA.md` §9, que hoje diz o **oposto** do modelo
novo — *"Todo projeto novo copia esse kit no bootstrap"*. Enquanto essa frase estiver publicada, o
hub canônico está mandando copiar o que ele existe para deixar de ser copiado.

Fechar `P-0721` e este plano com o registro de DP-1..DP-12, e promover ao `GOVERNANCA.md` a lição
das **três premissas que caíram nesta iniciativa** por sondagem curta demais (symlink de arquivo
exige privilégio; filhos não são repos git; os filhos *tinham* cópia dos docs de doutrina):
decisão que escolhe **mecanismo de plataforma** exige sonda de viabilidade junto da recomendação.

---

## 5. Relação com os planos anteriores

| Plano | Situação |
|---|---|
| `P-0725-governanca-tres-camadas` | **Superseded** no mesmo dia — o modelo de 3 camadas caiu com o abort do `ForAWS` e o congelamento do `Container`. |
| `P-0721` Fases 0/1a/1b/2 (`done`) | Mantidas — congelamento canônico do hub e regularização git seguem válidos. |
| `P-0721` Fase 3 (provar D1 em sandbox) | **Absorvida pela Fase 4 daqui.** A prova em sandbox descartável perdeu a razão de ser: agora existe um alvo real, com suíte de teste, e a rede de segurança é o `worktree` + tag em vez de um sandbox artificial. |
| `P-0721` Fase 4 (migrar 6 filhos) | **Superseded** — 1 vira prova de aceitação, 1 vira legado, 1 abortado, 3 adiados. |
| `P-0721` DP-8 | **Encerrado** — nenhum dos projetos que ele travava está mais em escopo. |
| `TK-SGSS-ARQUETIPO` | **Fechável** — o residual §15×§16 era especialização do Container, não deriva (medido em `P-0725-tres-camadas` §1.2). Com o Container congelado, some do radar. |

---

## 6. Riscos

| Risco | Mitigação |
|---|---|
| A prova de aceitação "passar" sem provar nada (suíte não rodada antes) | Fase 4 passo 2 exige contagem de baseline **antes** do subtree. Sem número de antes, não há prova. |
| Materialização apagar override local do `PantonicVideo` | `kit-exclude.txt` escrito na **Fase 1**, muito antes do primeiro sync — não como correção depois do estrago. |
| `git diff` da prova ilegível por flip de EOL | `.gitattributes` escopado a `.claude/**`, em commit próprio e anterior. |
| Mexer nos 258 arquivos sujos do dono para "limpar a árvore" | Proibido. A prova roda em `worktree` a partir do `HEAD`. |
| Checagem de versão virar auto-update por iniciativa de agente | §3 é explícito nos dois sentidos, e a skill declara a proibição. Vale inclusive para patch. |
| `GOVERNANCA.md` §9 continuar mandando copiar o kit depois da migração | Fase 5 é parte do plano, não follow-up opcional. |

---

## Achados da execução

_(vazio — plano não iniciado)_
