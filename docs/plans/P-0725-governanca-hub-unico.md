# P-0725 — Hub único de governança: PantonicApp canônico, PantonicVideo como prova de aceitação

**Origem:** decisão do dono (2026-07-25), simplificando o escopo pela segunda vez no mesmo dia.

> "Vamos abortar o PantonicContainerForAWS. Para simplificar, vamos restringir o plano apenas ao
> PantonicApp, e quando surgir a necessidade de revisão do PantonicContainer, farei um esforço
> direcionado neste. Por ora, vou deixá-lo como legado. O plano então vai se restringir a levar o
> PantonicApp para o Github, e usar o PantonicVideo como prova de aceitação."

**Substitui** `P-0725-governanca-tres-camadas.md` (mesmo dia, nunca executado): o modelo de três
camadas condicionais morreu com a medição de que a camada 3 não tinha conteúdo próprio.

**Planejador:** Opus. **Executor:** Sonnet, exceto a Fase 1 (curadoria de doutrina → Opus).

**Estado (2026-07-28):** **DONE — Fases 1 a 5 concluídas.** Fase 4: prova de aceitação do
mecanismo `git subtree` + `sync-kit.ps1` verde no `PantonicVideo` (worktree descartável, árvore
principal nunca tocada — ver Notas de execução). Fase 5: doutrina invertida em `GOVERNANCA.md`
§9 (kit distribuído via subtree/materialização, não cópia manual), `P-0721` fechado, e as duas
lições da iniciativa promovidas a `GOVERNANCA.md` §3. Nenhuma tarefa deste plano segue em aberto;
detalhe em "Notas de execução" → Fase 5.

> **Consumo do kit:** suportado a partir de **`kit-v1.0.1`**. A tag `kit-v1.0.0` ficou incompleta
> em dois pontos — sem `sync-kit.ps1` (o split foi feito antes de o script existir) e sem
> `KIT_VERSION` (que estava fora do prefixo do subtree). Ela **não** foi movida nem apagada;
> permanece publicada como está, marcada aqui como incompleta.

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

**DP-13 ✅ FECHADA 2026-07-26 = `KIT_VERSION` mora DENTRO de `.claude/`, no hub.**

Levantada pelo orquestrador no pickup da Fase 3b (ver Achados): o arquivo estava na raiz do hub,
fora do prefixo `--prefix=.claude` do subtree, então nunca chegaria ao consumidor e a checagem
anti-drift do §3 leria um arquivo inexistente. Decidido pelo arquiteto **sem custo para o dono** —
não era escolha de política, era defeito: a versão de um artefato distribuído tem que viajar
dentro do artefato. Executada na Fase 3b (§4). Rejeitada a rota alternativa de o `sync-kit.ps1`
copiar a versão — ver a resolução do achado para o motivo (a cópia teria de vir da rede, e uma
versão local lida do remoto é sempre igual ao remoto: o guarda nunca dispara).

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
hub  PantonicApp/.claude/KIT_VERSION  "1.0.1"  — DENTRO do kit (corrigido em 2026-07-26, DP-13);
                                                bump obrigatório em toda mudança canônica do kit
     tag git  kit-v1.0.1              na branch `kit` (raiz do branch = `.claude/` do hub,
                                      logo `KIT_VERSION` fica na raiz do branch)

consumidor  .claude/kit/KIT_VERSION   chega **pelo próprio subtree**, sem nenhum passo de cópia

checagem    git ls-remote --tags <url> "kit-v*"     1 chamada de rede, sem fetch,
                                                     sem tocar a árvore de trabalho
```

**Por que dentro do `.claude/` e não na raiz do hub (DP-13, 2026-07-26):** a versão é atributo do
artefato distribuído. Fora do prefixo do subtree ela não viaja, e o consumidor não tem como
responder *"que versão está instalada aqui?"* — que é exatamente a pergunta da metade (b). Ver o
achado de 2026-07-26 e sua resolução.

**Resultado da checagem:**
- Versões iguais → segue em silêncio, sem gastar turno do dono.
- Divergentes → **reporta**: versão local, versão remota, e a pergunta *"atualizar agora ou
  postergar?"*. Registra a resposta no plano que está sendo criado. **Nunca atualiza sozinho.**
- Sem rede / remote inacessível → reporta "não verificado" e segue. Falha de rede não bloqueia
  trabalho nem vira silêncio.

**Como a versão local é resolvida (DP-13):** a skill decide pelo que existe na árvore, nesta
ordem — (1) existe `.claude/kit/KIT_VERSION` → **modo consumidor**, é essa a versão local; (2) não
existe `.claude/kit/`, mas existe `.claude/KIT_VERSION` → **modo hub**: este repo *é* a fonte, não
há o que atualizar; a checagem reporta "hub canônico — nada a comparar" e, se a rede permitir,
avisa se a tag remota mais recente não corresponde ao `KIT_VERSION` local (sinal de que alguém
mudou o kit e não republicou); (3) nenhum dos dois → "kit não instalado", segue em silêncio. O
modo hub não é hipótese remota: o gatilho da regra é **criação de plano**, e os planos desta
iniciativa nascem no próprio `PantonicApp`.

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

1. `KIT_VERSION` = `1.0.0` na raiz do hub. *(Local corrigido em 2026-07-26 por **DP-13**: o
   arquivo passa para `.claude/KIT_VERSION`, dentro do prefixo do subtree. A Fase 3b faz o `git
   mv`; esta linha fica como registro do que a Fase 2 executou.)*
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

**Executada em 2026-07-26 — e incompleta**, por um motivo que só apareceu depois: o branch `kit`
foi splitado antes de o `sync-kit.ps1` existir, então `kit-v1.0.0` publica o conteúdo do kit sem o
script que o materializa. A Fase 3b corrige e republica; esta fase só fecha de verdade com
`kit-v1.0.1` no remote.

---

### Fase 3b — Autorar o `sync-kit.ps1`, mover o `KIT_VERSION` e republicar o kit *(aberta em 2026-07-26)*
**Modelo: Sonnet. Teto: 25 tool uses** (era 20; +5 pela DP-13). Depende das Fases 1–3 (todas
`done`). Sem decisão do dono pendente — **DP-13 fechada pelo arquiteto**, esta fase só executa.

**Por que existe:** o §5 declarou a Fase 3 do `P-0721` "absorvida pela Fase 4 daqui", mas aquela
fase tinha **quatro** tarefas — T2 virou a Fase 3 deste plano, T3/T4 viraram a Fase 4, e **T1
(autorar o materializador) caiu no vão da divisão**. A Fase 4 passo 5 manda "materializar via
`sync-kit.ps1`" e o script não existe em nenhum dos dois repos. Esta fase repõe o T1 no lugar em
vez de enfiá-lo no teto da Fase 4 — escrever um mecanismo que vale para **todo** consumidor futuro
como efeito colateral de uma prova de aceitação é como se fixa contrato sem revisão.

**O contrato não precisa ser desenhado — já está escrito.** `P-0721-governanca-single-source.md`,
Fase 3/T1, especifica as sete cláusulas do script (resolução por `$PSScriptRoot`; cópia de
`kit/skills/<nome>/` e `kit/agents/<nome>.md` para o namespace plano; leitura do `kit-exclude.txt`
com `#` de comentário; proibição de apagar artefato que não vem do kit; idempotência; `-Check` que
só compara e sai com exit 1 se divergir; resumo "N copiados, M pulados"). **Implementar aquele T1
verbatim** — divergir dele é replanejamento, não execução, e escala ao arquiteto.

**Um ajuste obrigatório sobre o T1:** o `kit-exclude.txt` que a Fase 1 escreveu no `PantonicVideo`
usa **caminho relativo a `.claude/`** (`skills/guardrails-check`, `agents/pantonic-executor`,
`skills/integrar-poc`), não nome nu como o T1 supunha — desvio declarado e justificado na Fase 1
(nome nu é ambíguo entre os dois namespaces). O parser lê esse formato. Aceitar nome nu também,
por compatibilidade, é opcional; o formato com namespace é o normativo.

**Sequência:**
1. Escrever `.claude/sync-kit.ps1` no hub, conforme o T1 + o ajuste de formato acima.
2. Provar em sandbox descartável no scratchpad (é o T3 do `P-0721`, que a Fase 4 daqui não cobre —
   ela prova o caso real, não o mecanismo): `git init` num diretório limpo simulando um filho com
   **(a)** um agente local que não vem do kit, **(b)** um `kit-exclude.txt` excluindo 1 skill do
   kit e **(c)** uma versão local divergente dessa skill. Rodar `subtree add` + `sync-kit.ps1`.
   **Aceite:** kit materializado; (a) intocado; (c) **não** sobrescrito; `-Check` → exit 0; rodar
   2× seguidas não muda nada.
3. **DP-13 — pôr o `KIT_VERSION` dentro do kit.** Quatro edições, todas mecânicas:
   - `git mv KIT_VERSION .claude/KIT_VERSION` no hub.
   - Bumpar o conteúdo para `1.0.1` — é mudança canônica no `.claude/`, e o §3 torna o bump
     definition-of-done, não cortesia.
   - `GOVERNANCA.md` §10: corrigir o caminho canônico e o diagrama para `.claude/KIT_VERSION`,
     dizendo **por que** (a versão viaja dentro do artefato que ela versiona).
   - `checar-versao-kit/SKILL.md`: escrever a resolução da versão local em três modos —
     consumidor (`.claude/kit/KIT_VERSION`), **hub** (`.claude/KIT_VERSION` sem `.claude/kit/` →
     "hub canônico, nada a comparar") e não-instalado. Ver §3. Sem esse modo hub, a própria
     criação de plano **neste repo** cai no ramo de arquivo ausente.

   **Não** adicionar cláusula de cópia de `KIT_VERSION` ao `sync-kit.ps1`: com o arquivo dentro do
   prefixo, ele chega pelo subtree e o contrato T1 permanece com as sete cláusulas originais.
4. Commit + push em `origin/main`.
5. Re-splitar e republicar: `git subtree split --prefix=.claude -b kit -f` (ou apagar e recriar o
   branch local `kit`) → `git push origin kit` → `git tag kit-v1.0.1 kit` → `git push origin
   kit-v1.0.1`. **A tag `kit-v1.0.0` não é movida nem apagada** — retag de tag publicada é
   reescrita de história do ponto de vista de quem já buscou; ela fica como está, marcada no §
   Achados como incompleta.

**Critério de pronto — três checks, todos contra a tag publicada, não contra a árvore local:**
1. `git ls-remote --tags origin "kit-v*"` devolve **duas** tags.
2. `git ls-tree --name-only kit-v1.0.1` lista **`sync-kit.ps1`** na raiz.
3. `git show kit-v1.0.1:KIT_VERSION` devolve **`1.0.1`** — cobre a DP-13 e, de quebra, prova que
   tag e arquivo concordam.

Os checks 2 e 3 existem porque as duas falhas desta iniciativa foram do mesmo tipo: o conteúdo
publicado não tinha o que o consumidor precisa, e ninguém olhou o *publicado* — só o local. Check
que roda na árvore de trabalho não teria pego nenhuma das duas.

**Proibições:** não tocar em `D:\workspaces\PantonicVideo` nesta fase (a materialização real é a
Fase 4); o sandbox do passo 2 vive no scratchpad da sessão, nunca em `D:\workspaces\`.

---

### Fase 4 — Prova de aceitação no `PantonicVideo`
**Modelo: Sonnet. Teto: 35 tool uses.** Depende da **Fase 3b** (o passo 5 daqui usa o
`sync-kit.ps1` que ela autora) e consome `kit-v1.0.1`, não `kit-v1.0.0`. Sem decisão do dono
pendente.

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
4. `git subtree add --prefix=.claude/kit <URL> kit --squash` — o branch `kit` já na ponta
   `kit-v1.0.1` (Fase 3b). Conferir que `.claude/kit/sync-kit.ps1` chegou; se não chegou, a
   Fase 3b não fechou e esta para aqui.
5. Materializar: `pwsh .claude/kit/sync-kit.ps1`, respeitando `kit-exclude.txt`. Depois,
   `sync-kit.ps1 -Check` → exit 0.
6. **Verificar as duas metades da aceitação:**
   - **Não perdeu:** os 9 agentes locais e os 2 overrides declarados seguem presentes e com o
     conteúdo de antes. Conferir por hash contra a tag `pre-kit-migration`.
   - **Não chegou o que foi excluído:** `skills/integrar-poc` **não** existe em
     `.claude/skills/` depois da materialização (DP-12). Exclusão que não é verificada é
     exclusão que ninguém sabe se funcionou.
   - **Não quebrou:** Tier 3 verde, contagem ≥ baseline do passo 2; `tests/conformance/` verde.
   - **O kit publicado basta:** rodar `checar-versao-kit` no `PantonicVideo` e obter a comparação
     real (local `1.0.1` × remoto `1.0.1`), não "arquivo ausente". Esta verificação é a
     generalização das duas falhas de 2026-07-26 — *o que o consumidor precisa que o kit publicado
     não tem* só aparece quando alguém exercita o kit **como consumidor**, e o `PantonicVideo` é o
     primeiro a fazê-lo.
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

Promover junto a **quarta** lição, da mesma família e medida em 2026-07-26 (ver Achados): **rebase
que absorve uma fase de outro plano precisa mapear tarefa a tarefa**. "Fase X absorvida pela Fase
Y" é uma afirmação numa granularidade mais grossa que o objeto afirmado — aqui, uma fase de quatro
tarefas se espalhou por duas fases e a que sobrou (autorar o materializador) não caiu em nenhuma,
o que só apareceu quando a Fase 4 foi executar um passo cujo insumo não existia. Um plano que
absorve outro herda as tarefas, não o título da fase.

---

## 5. Relação com os planos anteriores

| Plano | Situação |
|---|---|
| `P-0725-governanca-tres-camadas` | **Superseded** no mesmo dia — o modelo de 3 camadas caiu com o abort do `ForAWS` e o congelamento do `Container`. |
| `P-0721` Fases 0/1a/1b/2 (`done`) | Mantidas — congelamento canônico do hub e regularização git seguem válidos. |
| `P-0721` Fase 3 (provar D1 em sandbox) | **Absorvida, agora com mapeamento tarefa a tarefa** — a redação anterior ("absorvida pela Fase 4") era grossa demais e perdeu o T1 (corrigido em 2026-07-26): **T1** (autorar `sync-kit.ps1`) → **Fase 3b** daqui; **T2** (publicar o branch `kit`) → Fase 3; **T3** (provar `add` + materialização em sandbox) → Fase 3b passo 2; **T4** (provar a tese: 1 linha no hub chega ao filho) → Fase 4. A prova do *caso real* substitui o sandbox artificial, mas a prova do *mecanismo* continua sendo em sandbox — são coisas diferentes, e confundi-las foi a origem do vão. |
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

## Notas de execução

### 2026-07-25 — Fase 1 (reconciliar `PantonicApp` × `PantonicVideo`) — **done**

Executada em Opus, conforme o plano. Entrada = árvore de trabalho do `PantonicVideo` (§1.3), não
o `HEAD`.

**Critério de curadoria aplicado, com um refinamento medido:** além de "quem tem a regra vence",
uma divergência foi decidida por **sobrevivência à materialização** — o canônico é materializado
em N projetos, logo não pode citar artefato que não viaja com ele nem caminho de máquina.

| # | Skill / linha | Vence | Razão |
|---|---|---|---|
| D1 | `proximo-passo` preâmbulo | **síntese** | Video acertou ao citar `CLAUDE.md` Regra 2 (resolve em todo consumidor); mas o trecho "cópia local do kit (`D:\workspaces\...`)" foi **descartado** — caminho de máquina + descreve a cópia manual que a Fase 4 substitui por subtree |
| D2 | `proximo-passo` §3 citação | síntese (idem D1) | — |
| D3 | `proximo-passo` §4 "Dieta do prompt" | **Video** | carrega REGRA: fraseado agnóstico de agente (DP-2 / `TK-SGSS-ARQUETIPO`) e remove jargão de um projeto só (camadas/MVVM/ACL); wrap também estava correto |
| D4 | `diario-de-obras` cabeçalho | **hub** | mesma razão de D1 (caminho absoluto + relação "adaptada") |
| D5 | `diario-de-obras` diretiva | **Video** | citação inline redundante com o cabeçalho |
| D6 | `diario-de-obras` §3 Condensar `(a)(b)(c)(d)` | **hub** | sem diferença de regra → reformatação; letras são referenciáveis |
| D7 | `handover` regra de ouro | síntese (idem D1) | — |
| D8 | `handover` §1 Gate | **hub** | REGRA: aponta para a skill `guardrails-check` (viaja no kit); o Video apontava para a tabela "Test execution tiers" do seu próprio `CLAUDE.md`, que não existe em outro consumidor |
| D9 | `handover` §2 achado fora de escopo | **Video** | proveniência da regra (decisão do dono 2026-07-16) |
| D10 | `handover` §2 gate de triagem | **hub** | **verificado**: `docs/plans/P-0714*` não existe mais no `PantonicVideo` → o "precedente" do Video era ponteiro morto |
| D11 | `handover` §4 | **Video** | linha do hub estourava o wrap; conteúdo idêntico (LF garantido na escrita) |

**Critério de pronto — verificado, 5 pontos:** (1) as 3 skills byte-idênticas hub × Video
(`diff --strip-trailing-cr` limpo nas 3); (2) zero caminho absoluto de máquina remanescente;
(3) zero ponteiro `P-0714`; (4) `kit-exclude.txt` com exatamente 3 entradas; (5) os 3 alvos de
exclusão existem no caminho que a entrada declara.

**Desvio declarado (formato do `kit-exclude.txt`):** o snippet do §4/Fase 1 usa nomes nus
(`guardrails-check`); foi escrito com **caminho relativo a `.claude/`**
(`skills/guardrails-check`, `agents/pantonic-executor`, `skills/integrar-poc`). Razão: nome nu é
ambíguo entre os namespaces `skills/` e `agents/`, e o `sync-kit.ps1` ainda não existe para
desambiguar — a ambiguidade viraria defeito na Fase 4. As 3 entradas e as duas naturezas
comentadas seguem exatamente como o plano exige.

**Não feito de propósito:** `KIT_VERSION` não foi bumpado — ele **ainda não existe**; a Fase 2 o
cria já em `1.0.0`, cobrindo o conteúdo desta fase. Commit também não foi feito: é o passo 1 da
Fase 3.

---

### 2026-07-26 — Fase 2 (versionamento + regra anti-drift) — **done**

Executada em Sonnet, conforme o plano. Implementado o §3 inteiro:

1. `KIT_VERSION` criado na raiz do hub com `1.0.0`.
2. `GOVERNANCA.md` §10 novo, com as duas metades (a)/(b), o bloco "Mecanismo" e os três
   resultados da checagem.
3. Skill nova `.claude/skills/checar-versao-kit/SKILL.md`, com o procedimento operacional
   completo (replicado, não reformulado) e a proibição explícita de auto-atualizar mesmo para
   patch.
4. `.claude/skills/diario-de-obras/SKILL.md`, operação "1. Registrar plano" — gancho adicionado
   chamando `checar-versao-kit` na criação de plano, com os três desfechos resumidos.

**Achado da Fase 1 (`GOVERNANCA.md` não viaja no subtree) triado aqui** — ver a marca "TRIADO na
Fase 2" na seção "Achados da execução": resolvido por replicação do texto normativo nos dois
lugares, decisão do orquestrador (não do dono).

**Não feito de propósito:** tag `kit-v1.0.0`, commit e push — todos são Fase 3.

Consumo: 15 tool uses, ~57k tokens, sonnet, ~5min.

---

### 2026-07-26 — Fase 3 (publicar o hub canônico) — **done**

Executada em Sonnet, conforme o plano, 3 passos:

1. `git status --short` reconferido antes do commit — idêntico ao estado reportado na delegação
   (6 modificados + `checar-versao-kit/` + `KIT_VERSION` novos, nada inesperado). Commit
   `724db5e` ("chore(governanca): reconciliar kit .claude PantonicApp x PantonicVideo +
   versionamento anti-drift"), 8 arquivos. Push `origin main`: `98444a1..724db5e`.
2. `git subtree split --prefix=.claude -b kit` → branch local `kit` na ponta
   `3c9817ca000580293dd0bde56b7ce82756bfa8c7`. Push `origin kit` (`new branch`).
3. `git tag kit-v1.0.0 kit` → push `origin kit-v1.0.0` (`new tag`).

**Critério de pronto verificado:** `git ls-remote --tags origin "kit-v*"` retorna
`3c9817ca000580293dd0bde56b7ce82756bfa8c7  refs/tags/kit-v1.0.0` — mecanismo de checagem do §3
já tem o que checar.

**Não feito de propósito:** nenhuma verificação de conteúdo do subtree (ex.: conferir se
`GOVERNANCA.md` ficou de fora, achado já documentado abaixo) — fora do escopo mecânico desta
fase; a prova de conteúdo é da Fase 4.

Consumo: 9 tool uses, ~54k tokens, sonnet, ~108s.

---

## Achados da execução

### 2026-07-25 — `GOVERNANCA.md` **não viaja** com o subtree (afeta a Fase 2)

**Evidência:** o subtree é `--prefix=.claude` (§4/Fase 3 passo 2), e `GOVERNANCA.md` está na
**raiz** do hub, fora desse prefixo. Consequência: toda citação a `GOVERNANCA.md §N` dentro de uma
skill do kit é um ponteiro que **dangla em qualquer consumidor** — foi por isso que a Fase 1
converteu as 3 citações para a forma dupla (`~/.claude/CLAUDE.md` Regra 2, resolvível em todo
projeto; `GOVERNANCA.md` §N "no hub do kit", explicitamente marcado como do hub).

**Por que é pertinente agora:** a **Fase 2** manda escrever a regra nova como `GOVERNANCA.md` §10
e "ganchar a chamada na skill `diario-de-obras`". Se a regra (a)/(b) do §3 viver **só** no
`GOVERNANCA.md`, o consumidor recebe a skill que manda checar versão e não recebe a regra que
explica o mecanismo.

**Rota sugerida (decisão do dono na Fase 2, não tomada aqui):** o texto normativo da regra vive na
skill `checar-versao-kit` (que viaja no kit) e o `GOVERNANCA.md` §10 fica como a versão do hub
apontando para ela — em vez do inverso. Não implementado nesta fase: está fora do escopo da
Fase 1 e a Fase 2 tem dono e teto próprios.

**TRIADO na Fase 2 (2026-07-26) — resolvido por replicação, não por ponteiro.** A rota efetivada
não foi a sugerida acima: em vez de o `GOVERNANCA.md` §10 apontar para a skill, **ambos carregam
o texto normativo completo** — §10 como doutrina do hub e `checar-versao-kit` como operacional que
viaja no kit. O consumidor recebe a regra inteira via `.claude/` mesmo sem `GOVERNANCA.md`, que era
o risco original. **Decisão tomada pelo orquestrador no dossiê de delegação, não pelo dono** — o
custo é duplicação de texto normativo em dois lugares (drift possível se um for editado sozinho).
Reverter para a rota "ponteiro" é barato enquanto o kit não foi publicado (Fase 3).

**Ressalva de 2026-07-26 — a janela acima fechou e reabriu.** A Fase 3 publicou o kit poucas horas
depois desta nota, então a condição "enquanto não foi publicado" expirou sem ninguém encerrá-la.
Mas a **Fase 3b** republica o kit como `1.0.1` de qualquer forma, o que devolve por uma rodada o
mesmo custo baixo de reversão. Como a decisão foi do orquestrador e nunca chegou ao dono, fica
**registrado como ponto opcional de revisão do dono na Fase 3b** — não bloqueante: sem
manifestação, a replicação permanece e esta nota se encerra em definitivo quando a `1.0.1` subir.

### 2026-07-26 — `sync-kit.ps1` não existe (bloqueia a Fase 4 passo 5)

**Evidência:** busca por `sync-kit*` na raiz de `PantonicApp` e de `PantonicVideo` (fora de
`.git/`) não encontra o arquivo em nenhum dos dois repos. A própria nota da Fase 1 (linha ~323
deste plano) já registrava "o `sync-kit.ps1` ainda não existe" — o gap é conhecido desde a Fase 1,
mas a Fase 4 §4 passo 5 ("Materializar via `sync-kit.ps1`, respeitando `kit-exclude.txt`") assume
que ele já existe e não tem passo próprio para autorá-lo.

**Por que não foi decidido aqui:** escrever o script exige desenhar o contrato de materialização
(flatten de `.claude/kit/{skills,agents}/*` → `.claude/{skills,agents}/*`, respeitando
`kit-exclude.txt`, idempotente) — decisão de mecanismo de plataforma que vale para **todo**
consumidor futuro do hub, não só a prova de aceitação do `PantonicVideo`. Escrevê-lo às pressas
dentro do teto de 35 tool uses da Fase 4 (que já cobre tag, baseline Tier 3, `.gitattributes`,
`subtree add`, verificação e `diff --stat`) arrisca fixar o contrato como efeito colateral de uma
prova, sem revisão própria — mesmo padrão do risco em §6 "checagem de versão virar auto-update por
iniciativa de agente", mas aplicado ao desenho do sync em vez do gatilho de update.

**Verificado antes de registrar (não é suposição):** `kit-exclude.txt` do `PantonicVideo` já tem
as 3 entradas corretas (formato `namespace/nome`, conforme desvio declarado na Fase 1); a tag
`kit-v1.0.0` está confirmada no remote (`git tag -l` + `git remote -v` em `PantonicApp`); não há
`.gitattributes` no `PantonicVideo` ainda (esperado, é passo 3 da própria Fase 4); `git status
--short` no `PantonicVideo` mostra 259 arquivos sujos (consistente com os "258 arquivos sujos" do
§1.4). Ou seja: tudo que a Fase 4 precisa **exceto** o script de materialização já está no lugar.

**Não decidido aqui — para o arquiteto reavaliar:** se `sync-kit.ps1` entra como pré-requisito
dentro da própria Fase 4 (teto ajustado), vira sub-tarefa separada antes da Fase 4 (ex.:
`Fase 3b`), ou existe uma rota alternativa de materialização que este levantamento não achou.
Fase 4 não foi delegada à execução enquanto este ponto não for resolvido.

#### RESOLVIDO pelo arquiteto — 2026-07-26 (avaliação da anotação, em Opus)

**Abriu-se a `Fase 3b`** (§4), fase própria antes da Fase 4, teto de 20 tool uses, em Sonnet. As
três perguntas da nota, respondidas:

1. **Não é decisão de mecanismo de plataforma — o contrato já existe.** O levantamento não achou a
   rota porque procurou o *arquivo*, não a *especificação*: `P-0721-governanca-single-source.md`,
   Fase 3/**T1**, define as sete cláusulas do script (`$PSScriptRoot`, flatten dos dois namespaces,
   `kit-exclude.txt` com `#`, nunca apagar o que não é do kit, idempotência, `-Check` com exit 1,
   resumo). A Fase 3b implementa aquilo verbatim, com um único ajuste declarado (formato
   `namespace/nome` no `kit-exclude.txt`, conforme a Fase 1). Executor não redesenha: divergir do
   T1 escala ao arquiteto.
2. **A causa-raiz não é "a Fase 4 assume que o script existe".** É o §5 deste plano ter absorvido a
   Fase 3 do `P-0721` **em bloco** ("absorvida pela Fase 4"), quando aquela fase tinha quatro
   tarefas que se espalharam por duas fases daqui — T2 para a Fase 3, T3/T4 para a Fase 4 — e o T1
   não coube em nenhuma. Absorção de fase multi-tarefa sem mapeamento tarefa a tarefa. É a mesma
   família das três premissas que já caíram nesta iniciativa (§4/Fase 5): **verificação numa
   granularidade mais grossa que a do objeto verificado**. O §5 foi reescrito com o mapeamento
   explícito; a lição entra no `GOVERNANCA.md` junto das outras três na Fase 5.
3. **Consequência que a nota não registrou: a Fase 3 `done` não era final.** O `P-0721` T2 exige
   que a raiz do branch `kit` contenha o `sync-kit.ps1`; o split foi feito antes de o script
   existir. Portanto **`kit-v1.0.0` é uma tag que ninguém consegue consumir** — traz skills e
   agentes sem o materializador. Não é lacuna de plano, é defeito no artefato publicado. Como o
   hub ainda não tem consumidor (a Fase 4 seria o primeiro), o dano é zero; corrigir agora custa
   uma republicação. A tag `kit-v1.0.0` **não é movida** — fica marcada aqui como incompleta e o
   suporte começa em `kit-v1.0.1`.

**O que a anotação fez certo, e vale manter como padrão:** o parágrafo "Verificado antes de
registrar" confere tudo o mais que a Fase 4 precisa e conclui "tudo exceto o script já está no
lugar". Nota de bloqueio que escopa o bloqueio é a diferença entre `blocked` e travado — quem
retoma sabe que falta uma peça, não uma investigação. E recusar autorar o script dentro do teto da
Fase 4 foi a decisão certa pelo motivo certo.

### 2026-07-26 — `KIT_VERSION` nunca materializa em `.claude/kit/KIT_VERSION` (mecanismo anti-drift quebrado)

**Encontrado no pickup da Fase 3b, antes de delegar** (orquestrador, revisão do dossiê de
delegação — nenhuma linha ainda escrita em `.claude/sync-kit.ps1`).

**Evidência:**
- `GOVERNANCA.md` §10 e este plano (linha ~138: `hub PantonicApp/KIT_VERSION "1.0.0"`) colocam o
  `KIT_VERSION` canônico na **raiz do repo hub**, fora de `.claude/`. Confirmado:
  `PantonicApp/KIT_VERSION` existe e contém `1.0.0`; `PantonicApp/.claude/KIT_VERSION` **não**
  existe.
- O branch `kit` é `git subtree split --prefix=.claude -b kit` (T2) — só o conteúdo de `.claude/`
  entra. `git ls-tree --name-only kit` confirma: `README.md`, `agents`, `skills` — sem
  `KIT_VERSION`. Um arquivo fora de `.claude/` **não pode** viajar por esse subtree, nunca vai
  chegar em `kit-v1.0.1` por mais que a Fase 3b republique.
- `checar-versao-kit/SKILL.md` (passo 1) lê `.claude/kit/KIT_VERSION` **do consumidor** como a
  versão local a comparar contra a tag remota. Esse arquivo só existiria se algo o materializasse
  ali — e nada o faz: T1 (`P-0721` Fase 3, as sete cláusulas que a Fase 3b implementa verbatim)
  só copia `kit/skills/<nome>/` e `kit/agents/<nome>.md`; não menciona `KIT_VERSION`.
- Consequência: mesmo depois de Fase 3b + Fase 4 completas como escritas, todo consumidor futuro
  roda `checar-versao-kit` contra um `.claude/kit/KIT_VERSION` que nunca existiu — a checagem
  anti-drift de `GOVERNANCA.md` §10 fica quebrada por desenho, silenciosamente (sem erro que chame
  atenção; o passo 1 da skill simplesmente lê um arquivo ausente).

**Por que não foi decidido aqui:** é o mesmo tipo de decisão que a nota anterior (`sync-kit.ps1`
não existe) já escalou — desenhar como `KIT_VERSION` viaja do hub ao consumidor é contrato de
plataforma para todo consumidor futuro, não só para a Fase 3b/4 vigentes. Duas rotas óbvias
concorrem sem que o plano ou o `GOVERNANCA.md` tenham decidido entre elas: (a) `sync-kit.ps1`
ganha uma 8ª cláusula que copia `KIT_VERSION` (lido de algum lugar — mas de onde, se o hub-side
`KIT_VERSION` fica **fora** do subtree que o script materializa?) para
`.claude/kit/KIT_VERSION`; (b) `KIT_VERSION` migra para dentro de `.claude/` no hub, passando a
viajar naturalmente pelo split — mas isso contradiz o diagrama vigente de `GOVERNANCA.md` §10 e
deste plano (linha ~138), que o colocam deliberadamente na raiz do hub, fora do kit. Escolher (a)
ou (b) sem revisão fixaria um contrato não revisado, mesmo risco já nomeado na nota anterior.

**Não decidido aqui — para o arquiteto reavaliar:** qual das duas rotas (ou uma terceira) resolve
a materialização de `KIT_VERSION` no consumidor, e em que fase ela entra — dentro da própria
Fase 3b (o script já está sendo autorado ali) ou como fase própria antes da Fase 4 (mesma lógica
que separou a Fase 3b do resto). Fase 3b segue com o passo 3 da sua sequência ("bumpar
`KIT_VERSION` para `1.0.1`") apontando para o arquivo na raiz do hub como está — mas **sem
resolver este ponto, a republicação de `kit-v1.0.1` reproduz o mesmo defeito da `kit-v1.0.0`**
(tag que ninguém consegue consumir por completo), agora para o mecanismo de versão em vez do
materializador. Fase 3b não foi delegada à execução enquanto este ponto não for resolvido.

#### RESOLVIDO pelo arquiteto — 2026-07-26 (**DP-13**, §2)

**Rota (b): `KIT_VERSION` migra para `.claude/KIT_VERSION` no hub.** A Fase 3b executa (passo 3),
teto ajustado de 20 para 25. Não sobe ao dono: isto não é escolha de política, é defeito de
localização de arquivo — a decisão de política que o dono tomou ("haverá controle de versão do
kit") continua intacta, só estava implementada num lugar onde não funciona.

**Por que (a) está descartada, e não é questão de gosto.** A pergunta que a própria nota faz entre
parênteses — *"lido de onde, se o hub-side `KIT_VERSION` fica fora do subtree?"* — já é a
refutação. O `sync-kit.ps1` roda **no consumidor**, e só enxerga o que o subtree trouxe; para
copiar uma versão que não veio, teria de ir à rede. E aí o mecanismo se autodestrói: a versão
"local" passaria a ser lida do remoto, os dois lados da comparação viriam da mesma fonte e a
checagem **nunca acusaria divergência**. Um guarda anti-drift que sempre diz "iguais" é pior que
nenhum, porque produz confiança. Some-se que (a) exigiria uma 8ª cláusula no contrato T1 — que a
Fase 3b implementa verbatim — e o custo aparece dos dois lados.

**Por que (b) não contradiz nada que valha a pena preservar.** O conflito apontado é com o
diagrama do §3 (linha ~138) e o `GOVERNANCA.md` §10 — mas o diagrama é justamente o artefato
errado. Ele foi escrito antes de existir o branch `kit`, quando "raiz do hub" e "raiz do kit"
ainda pareciam a mesma coisa; depois do split com `--prefix=.claude`, a raiz do kit **é** o
`.claude/`. Corrigir o diagrama é reconhecer o que o split já fez. Com (b) o arquivo chega ao
consumidor pelo próprio `subtree add/pull`, sem passo de cópia, sem cláusula nova e sem código: a
correção tem custo negativo em mecanismo.

**Rota (c) considerada e descartada:** dispensar o arquivo e derivar a versão instalada do SHA no
commit de squash do subtree (`Squashed '.claude/kit/' content from commit <sha>`), comparando com
o SHA que `ls-remote` devolve. É mais à prova de adulteração — SHA não se edita à mão — mas troca
uma leitura de arquivo por parsing de mensagem de commit, quebra se alguém usar `subtree add` sem
`--squash`, e devolve um SHA onde o dono precisa ler *"local 1.0.0, remoto 1.0.1"* para decidir.
Complexidade sem ganho para a pergunta que a regra faz.

**Um segundo defeito, achado ao decidir este:** a skill lê `.claude/kit/KIT_VERSION` e nada mais —
mas o gatilho da regra é **criação de plano**, e os planos desta iniciativa nascem no
`PantonicApp`, que não tem (nem terá) `.claude/kit/`. Rodando no hub, a skill cairia no ramo
"arquivo ausente" do mesmo jeito, mesmo depois da DP-13. Daí o **modo hub** especificado no §3 e no
passo 3 da Fase 3b. Vale a generalização: toda regra do kit precisa responder o que faz **quando
roda no próprio hub** — o hub é consumidor da sua própria doutrina, sem ser consumidor do seu
próprio subtree.

**O que a anotação fez certo:** achou por revisão do dossiê, **antes** de escrever uma linha do
script — o momento mais barato possível. E ligou os três pontos que ninguém tinha ligado (arquivo
na raiz + prefixo do split + o passo 1 da skill), que é o que transforma três fatos inertes num
defeito. Foi o segundo achado seguido do mesmo tipo, o que sugere que a varredura "o que o
consumidor precisa que o kit publicado não tem" deveria ser um passo explícito da Fase 4, não uma
sorte de pickup.

---

### Fase 3b — EXECUTADA 2026-07-26 (Sonnet) ✅

**Os três checks de pronto, verificados pelo orquestrador contra a tag publicada** (não contra a
árvore local — é o ponto da fase):

```
git ls-remote --tags origin "kit-v*"
  3c9817c…  refs/tags/kit-v1.0.0     (intacta, não movida)
  68e79c1…  refs/tags/kit-v1.0.1
git ls-tree --name-only kit-v1.0.1   → KIT_VERSION  README.md  agents  skills  sync-kit.ps1
git show kit-v1.0.1:KIT_VERSION      → 1.0.1
```

**Entregue:**
1. `.claude/sync-kit.ps1` — sete cláusulas do T1 verbatim. O parser de exclusão descarta tudo a
   partir do primeiro `#` (`IndexOf('#')` + substring + trim), então comentário inline e linha de
   continuação só-comentário colapsam corretamente; casa `<namespace>/<nome>` (normativo) e aceita
   nome nu por compatibilidade, documentado no cabeçalho.
2. **DP-13:** `git mv KIT_VERSION .claude/KIT_VERSION`, conteúdo `1.0.0`→`1.0.1`; `GOVERNANCA.md`
   §10 corrigido para o caminho novo com o racional ("a versão viaja dentro do artefato que ela
   versiona"); `checar-versao-kit/SKILL.md` reescrita com a resolução em três modos
   (consumidor / hub / não-instalado) + `description` do frontmatter.
3. Commit `ffd8b14` em `main`, pushed.

**Comandos exatos que funcionaram — a Fase 4 reusa estes, não os do plano:**
```
git branch -D kit                              # o -f de `subtree split -b` NÃO existe nesta
git subtree split --prefix=.claude -b kit      # versão do git: delete-then-recreate é a rota
git push origin kit
git subtree add --prefix=.claude/kit https://github.com/PantaTheDoggo/PantonicApp.git kit --squash
```

**Prova de mecanismo (sandbox descartável no scratchpad, T3 do `P-0721`):** filho simulado com
(a) agente local fora do kit, (b) `kit-exclude.txt` **na forma real** — comentário inline +
continuação indentada só-comentário — e (c) versão local divergente da skill excluída. Resultado:
`15 copiados, 1 pulado por exclusão` (bate com o inventário de 16); (a) intocado; (c) **não**
sobrescrito; `.claude/kit/KIT_VERSION` chegou com `1.0.1`; `-Check` → exit 0; idempotência provada
por **sha256 de cada arquivo** antes/depois da 2ª rodada, não só pelo texto do resumo.

**Desvio de ordenação (autorizado pelo orquestrador na delegação, registrado aqui):** a sequência
do §4/Fase 3b põe a prova de sandbox no passo 2, antes do move do `KIT_VERSION` e do push. É
mecanicamente impossível — o `subtree add` puxa do branch publicado, que naquele momento era o
`kit-v1.0.0`, sem `sync-kit.ps1` e sem `KIT_VERSION`; o sandbox rodaria um script inexistente. A
prova foi para **depois do push do branch e antes da tag**, mantendo a tag (o ato que declara
suporte) condicionada à prova verde. Nenhum passo removido, nenhum aceite alterado. **Lição, do
mesmo naipe das outras desta iniciativa:** um passo de verificação que consome um artefato
publicado tem de vir depois do passo que o publica — ordenar a prova antes da publicação é a mesma
família de erro que verificar numa granularidade mais grossa que a do objeto verificado.

**Teto estourado, com número:** teto do plano = 25; contagem do orquestrador no gate de delegação
= ~30-34 (o sandbox sozinho é ~10-12), teto operacional fixado em 35. O executor parou **em 35
exatamente**, com o trabalho funcional completo e verificado e o write-up desta seção pendente —
escrita pelo orquestrador. A causa não foi thrashing: o teto de 25 nunca foi re-orçado quando a
DP-13 acrescentou quatro edições à fase. Fase que ganha escopo por decisão de arquiteto precisa
ganhar teto no mesmo ato.

Consumo: 35 tool uses, ~83k tokens, Sonnet, ~8min.

### 2026-07-28 — Fase 4 executada e fechada: prova de aceitação verde no `PantonicVideo`

Executor Sonnet, no repo `PantonicVideo`, teto 35 tool uses. Sequência do §4/Fase 4 seguida à
risca: worktree isolada em `.claude/worktrees/kit-migration-proof` a partir do `HEAD` (a árvore
de trabalho principal, com 271 arquivos modificados, nunca foi tocada); tag `pre-kit-migration`
criada antes de qualquer mudança; baseline Tier 3 rodado primeiro.

**7a — não perdeu (evidência: sha256 idêntico antes/depois):** os dois overrides locais
declarados em `kit-exclude.txt` (`skills/guardrails-check`, `agents/pantonic-executor`)
produziram o **mesmo hash sha256** antes e depois de `sync-kit.ps1`. `kit-exclude.txt` em si é
um arquivo **não commitado** no `PantonicVideo` (parte dos 271 arquivos modificados/novos da
árvore principal) — copiado manualmente para dentro da worktree (não para a árvore principal)
para que o mecanismo de exclusão pudesse ser exercitado de verdade; sem essa cópia, a worktree
(criada a partir do `HEAD` committed) não teria o arquivo e 7b não seria testável.

**7b — não chegou o excluído:** `.claude/skills/integrar-poc` **ausente** após materialização
(`sync-kit: 13 copied, 3 skipped by exclusion` / `-Check: clean, 13 managed artifact(s) match the
kit (3 excluded)`, exit 0) — os 3 excluídos batem com as 3 entradas de `kit-exclude.txt`.

**7c — não quebrou:** Tier 3 baseline = **1873 passed** (76.69s); Tier 3 pós-materialização =
**1873 passed** (81.20s) — igual. `tests/conformance/` isolado = **61 passed** (13.50s), verde.

**Rollback (passo 9) testado com sucesso:** `git reset --hard pre-kit-migration` na worktree —
`HEAD` volta a bater exatamente com a tag (`8e8a872...`), `.claude/kit` e `.gitattributes`
desaparecem, `git status --short` fica vazio. Worktree removida ao final
(`git worktree remove --force`); nada foi aplicado na árvore principal do `PantonicVideo`.

**Achado fora de escopo, não bloqueante:** rodar a suíte completa a partir da raiz do repo grava
`pantonicvideo-project.json` e `script.json` soltos no cwd (efeito colateral de teste não
isolado, appareceu na 1ª e na 2ª rodada Tier 3 respectivamente) — não referenciado por nome
literal em `tests/`, então provável default de path quando um teste não passa location
explícita. Não é causado pelo escopo do `.gitattributes` (única causa que o §4 passo 8 previa
para "algo fora do esperado no diff"); removido manualmente da worktree antes do `git diff
--stat` de verificação para não confundir o escopo do kit com ruído de teste. Registrado como
`TK-PYTEST-CWD-ARTIFACTS` no diário do `PantonicVideo` (backlog, não bloqueia a Fase 4).

**Veredito:** Fase 4 **done** — mecanismo `git subtree` + `sync-kit.ps1` provado ponta a ponta
(não-perda, não-vazamento do excluído, não-quebra, rollback) num consumidor real. Próxima =
**Fase 5** (decisão do dono sobre aplicar a migração de verdade no `PantonicVideo` + inverter a
doutrina de `GOVERNANCA.md` §9), fora do escopo desta execução.

Consumo: 39 tool uses, ~81k tokens, Sonnet, ~26min. (Teto do dossiê = 35; estouro de 4, todo em
leitura/edição dos dois documentos de fechamento — o trabalho funcional coube no orçamento. O
autorrelato do executor dizia 38; o dado medido da notificação é 39 — a linha vale pelo medido.
Mesma classe de "teto sem reorçamento" já registrada na Fase 3b: o dossiê orçou a mecânica da
prova e não orçou a escrita dos registros em dois repos.)

### 2026-07-28 — Fase 5 (registrar a decisão) — **done**

Executado inline pelo orquestrador (`proximo-passo`), owner-gated: o dono aprovou explicitamente
"Fase 5 agora", com um esclarecimento de escopo prévio — Fase 5, como escrita no plano, é só
documentação/fechamento (doutrina + registro de DP + lições), **não** inclui reaplicar o
`git subtree add` de verdade na árvore principal (a nota de fechamento da Fase 4 tinha
paraphraseado "aplicar a migração de verdade", mas isso não é uma fase especificada em lugar
nenhum deste documento — a árvore principal do `PantonicVideo` segue intocada e continua com 271+
arquivos da sessão de trabalho do dono). O dono confirmou o escopo restrito antes de prosseguir.

**Feito:**
1. `GOVERNANCA.md` §9 invertido — de "todo projeto novo copia esse kit no bootstrap" para "cada
   consumidor materializa via `git subtree` + `sync-kit.ps1`, respeitando `kit-exclude.txt`";
   referência cruzada ao mecanismo já documentado em §10.
2. Duas lições promovidas a `GOVERNANCA.md` §3 ("Regras de operação"): (a) decisão de mecanismo
   de plataforma exige sonda de viabilidade antes da recomendação — as três premissas que caíram
   nesta iniciativa (symlink exige privilégio Windows; filhos não são repos git; filhos já tinham
   cópia manual da doutrina); (b) rebase que absorve fase de outro plano mapeia tarefa a tarefa,
   não fase a fase — a tarefa "autorar o materializador" que ficou sem dono entre a Fase 3 e a
   Fase 4 deste plano.
3. `P-0721-governanca-single-source.md` fechado — header substituído por nota de fechamento
   apontando para este plano §5, com o relacionamento Fase 3/Fase 4/DP-8 já registrado em §5 desta
   sprint.
4. **Registro final de DPs desta iniciativa:** DP-1..DP-6 e DP-8 em `P-0721` (todas fechadas,
   ver header de `P-0721`); DP-1=D, DP-7=D1, DP-9 (resolvido pelo abort do `ForAWS`), DP-10=(a),
   DP-11=(a), DP-12 ✅ (§2 acima), DP-13 ✅ (§2 acima) — neste plano. Nenhuma DP pendente.
5. Índice do diário do `PantonicVideo` (`docs/DIARIO_DE_OBRAS.md`, linha `SPRINT-GOV`) atualizado
   para `done`.

**Não feito (fora de escopo, por decisão do dono nesta mesma rodada):** aplicar o `git subtree
add` de verdade na árvore principal do `PantonicVideo`. Não há dossiê/procedimento escrito para
essa ação neste plano; se o dono quiser prosseguir, é um plano novo (a árvore suja atual e o
mecanismo de exclusão precisam de desenho próprio, fora do que a Fase 4 provou em worktree
descartável).

Consumo: ver notificação do orquestrador (`proximo-passo`) — tarefa executada inline, sem
subagente.
