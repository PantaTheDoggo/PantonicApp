# P-0725 — Governança Pantonic* em três camadas condicionais

> ## ⛔ SUPERSEDED (2026-07-25, mesmo dia) — não executar
>
> Substituído por **`P-0725-governanca-hub-unico.md`**. O dono abortou o
> `PantonicContainerForAWS` (a medição de §1.1 mostrou que ele não tinha conteúdo próprio) e
> congelou o `PantonicContainer` como legado — o modelo de três camadas ficou sem as camadas 2 e 3.
>
> **Preservado por causa das medições**, que seguem válidas e são citadas pelo plano vivo:
> §1.1 (a camada 3 era um clone com ruído de formatação), §1.2 (o `ARQUITETURA_PANTONICA.md` do
> Container é especialização legítima, não deriva — fecha `TK-SGSS-ARQUETIPO`), §1.3 (o
> `pantonic-auditor-container.md` está na camada errada) e §1.4 (a premissa do P-0721 §1 era falsa).

**Origem:** decisão do dono (2026-07-25), reagindo ao desdobramento do SGSS sobre os filhos
existentes. Redefine QUEM é governança e QUEM é projeto final:

> "PantonicApp sempre é o documento base de todos os projetos Pantonic. PantonicContainer é
> invocado apenas se a aplicação é baseada em containers. E o PantonicContainerForAWS apenas se o
> container é usado na nuvem da AWS. Os demais virarão parte de repositórios específicos, e não
> devem entrar neste planejamento."

**Meta desta rodada:** deixar os **três** projetos locais de governança aptos a subir ao GitHub,
como camadas ordenadas e condicionais.

**Planejador:** Opus (Regra 7). **Executor:** Sonnet por fase, exceto a Fase C (curadoria de
conteúdo doutrinário → Opus).

**Estado:** **NOVO — não iniciado.** Rebaseia `P-0721-governanca-single-source` (ver §5): o
mecanismo (DP-1=D, DP-7=D1) é herdado sem mudança; o **conjunto governado** muda por completo.
**DP-9 é o único bloqueio real** e depende do dono.

---

## 0. Escopo

| Papel | Projetos | Nesta rodada |
|---|---|---|
| **Camada 1 — base** | `PantonicApp` | ✅ já é repo git publicado (`github.com/PantaTheDoggo/PantonicApp`) |
| **Camada 2 — condicional (container)** | `PantonicContainer` | ⬜ regularizar + publicar |
| **Camada 3 — condicional (container na AWS)** | `PantonicContainerForAWS` | ⬜ regularizar + publicar |
| **Consumidores (projetos finais)** | `PantonicVideo`, `PantonicScanlator`, `PantonicMonitor`, `PantonicPatom` | ❌ **fora deste planejamento** por decisão do dono |

A distinção é de natureza, não de tamanho: as três primeiras **definem** regras; as quatro últimas
**consomem** regras. Um consumidor nunca é fonte.

---

## 1. Diagnóstico medido (2026-07-25)

Comparação de hash MD5 dos 17 artefatos comuns nas três pastas (`A`=App, `C`=Container,
`W`=ForAWS):

| Artefato | A=C? | C=W? |
|---|---|---|
| `ARQUITETURA_PANTONICA.md` | ≠ | **=** |
| `GOVERNANCA.md` | ≠ | ≠ |
| `.claude/README.md` | ≠ | **=** |
| `agents/pantonic-auditor-arch.md` | ≠ | **=** |
| `agents/pantonic-auditor-cleancode.md` | **=** | **=** |
| `agents/pantonic-auditor-container.md` | **=** | **=** |
| `agents/pantonic-auditor-pyside6.md` | só no App | — |
| `agents/pantonic-executor.md` | ≠ | ≠ |
| `agents/pantonic-fora-da-caixa.md` | ≠ | **=** |
| `agents/pantonic-planner.md` | **=** | **=** |
| `agents/pantonic-scout.md` | ≠ | **=** |
| `skills/audit-sweep` | **=** | **=** |
| `skills/bootstrap-pantonic` | ≠ | ≠ |
| `skills/diario-de-obras` | ≠ | **=** |
| `skills/guardrails-check` | ≠ | **=** |
| `skills/handover` | ≠ | **=** |
| `skills/integrar-poc` | ≠ | **=** |
| `skills/proximo-passo` | ≠ | ≠ |

### 1.1. Achado dominante — a camada 3 está vazia de conteúdo AWS

**13 dos 17 artefatos do `ForAWS` são byte-idênticos aos do `Container`.** Os 4 que diferem foram
diffados linha a linha: `GOVERNANCA.md` (4 linhas), `bootstrap-pantonic` (4 linhas),
`pantonic-executor.md` (15) e `proximo-passo` (17). **Nenhuma dessas diferenças é uma regra de
AWS** — são rebordo de linha (`rewrap`) e texto desatualizado de uma cópia feita em momento
diferente. Exemplo real do diff de `GOVERNANCA.md`: a mesma frase quebrada em colunas distintas.

Consequência: hoje `PantonicContainerForAWS` **não é uma camada de AWS — é um clone de
`PantonicContainer` com ruído de formatação**. Isso é DP-9.

### 1.2. `ARQUITETURA_PANTONICA.md` é override de arquivo inteiro, e isso está correto

O Container não *acrescenta* seções à arquitetura do App: ele a **substitui**. §1-9 mantêm os
mesmos títulos, e a partir de §10 divergem por natureza —

| # | App (desktop) | Container |
|---|---|---|
| 10 | MVVM e PySide6 | Transporte e concorrência |
| 11 | Operações de OS e IN/OUT | Operações de OS, config e observabilidade |
| 12 | Contenção de falhas | **Empacotamento do artefato** (inserida) |
| 15 / 16 | Checklist de bootstrap | Checklist de bootstrap (deslocado +1) |

O ticket `TK-SGSS-ARQUETIPO` registrava esse "§15×§16" como deriva a investigar. **Não é deriva —
é especialização legítima**, e o deslocamento de numeração é só o efeito da inserção do §12. O
residual do ticket pode ser fechado com este registro.

### 1.3. Um artefato está na camada errada

`agents/pantonic-auditor-container.md` é **byte-idêntico nas três pastas**, incluindo o `App`. Um
auditor de container morando na camada base contradiz a regra que o dono acabou de declarar
("Container é invocado **apenas se** a aplicação é baseada em containers"). Ele desce para a
camada 2 na Fase C.

### 1.4. Premissa do P-0721 §1 corrigida

O P-0721 afirma: *"`GOVERNANCA.md` + `ARQUITETURA_PANTONICA.md` existem **só** em `PantonicApp/`;
nenhum filho tem cópia — confirmado"*. **Medido hoje: falso.** Os dois arquivos existem também em
`Container` e `ForAWS`. Datas: os três `GOVERNANCA.md` foram criados no mesmo minuto
(2026-07-21 09:05); os `ARQUITETURA_PANTONICA.md` dos filhos são de 2026-07-07 — **anteriores** ao
próprio plano, logo já estavam lá quando a sondagem os declarou inexistentes.

Terceira premissa a cair nesta iniciativa pelo mesmo motivo (sondagem de escopo insuficiente).
Reforça a lição já agendada para promoção ao `GOVERNANCA.md`.

---

## 2. Decisões

### Herdadas de P-0721 — fechadas, **não reabrir**
- **DP-1 = D** — distribuição por git a partir do hub remoto (não symlink/junção).
- **DP-7 = D1** — `git subtree` em `.claude/kit/` + materialização nos namespaces planos
  `.claude/skills/` e `.claude/agents/`, com exclusão declarada em `.claude/kit-exclude.txt`.

### Novas — desta rodada

| ID | Questão | Opções | Recomendação |
|---|---|---|---|
| **DP-9** | A camada 3 (`ForAWS`) não tem conteúdo próprio (§1.1). O que publicar? | **(a)** publicar como camada **declarada e vazia** (só `KIT.md` + regra de aplicabilidade; conteúdo AWS entra depois); **(b)** escrever o delta de AWS antes de publicar; **(c)** dobrar o ForAWS numa seção condicional do Container e não ter terceiro repo | **(a)**. O dono declarou o modelo de três camadas; a *regra de aplicabilidade* já tem valor sozinha, e (b) trava a publicação por tempo indeterminado. Mas é preciso saber, com todas as letras, que se está publicando um repositório sem conteúdo próprio. |
| **DP-10** | Granularidade do override entre camadas | **(a)** arquivo inteiro (a camada superior substitui o arquivo de mesmo nome); **(b)** fragmento/merge de seções | **(a)**. É o que já existe de fato (§1.2) e o que a materialização D1 faz naturalmente. (b) exige motor de merge — exatamente a complexidade que o dono recusou na rodada anterior. |
| **DP-11** | Ordem: publicar o estado atual ou reconciliar antes? | **(a)** snapshot fiel primeiro, reconciliar em commit seguinte; **(b)** reconciliar e publicar já limpo | **(a)**. O snapshot é o ponto de recuperação: qualquer erro da Fase C vira `git diff` contra uma baseline publicada. Foi o que se fez no hub, e funcionou. |

**DP-9 é o único que bloqueia** — trava a Fase A do `ForAWS`. DP-10/DP-11 têm recomendação de
baixo risco e seguem por omissão se o dono não se opuser.

---

## 3. Arquitetura das três camadas

```
  camada 1  PantonicApp            aplica-se SEMPRE
              │  base: golden rules, MVVM/PySide6, kit agêntico comum
              ▼
  camada 2  PantonicContainer      aplica-se SE a aplicação é containerizada
              │  substitui: ARQUITETURA (transporte/empacotamento/observabilidade)
              │  acrescenta: pantonic-auditor-container
              ▼
  camada 3  PantonicContainerForAWS  aplica-se SE o container roda na AWS
                 (hoje vazia — DP-9)

  projeto consumidor  .claude/kit-layers.txt   →  declara a lista ordenada
                      .claude/kit-exclude.txt  →  o que NÃO materializar
                      .claude/kit/<camada>/    →  subtree por camada
                      .claude/{skills,agents}/ →  materializado, camadas em ordem
```

**Regra de composição:** as camadas são aplicadas na ordem declarada; a última que declara um
artefato de dado nome vence (DP-10). Uma camada só pode ser declarada se sua predecessora também
estiver — `ForAWS` sem `Container` é composição inválida e o sync deve recusá-la.

**O que cada camada guarda depois da Fase C:** apenas o que **possui**. Nada de triplicata — foi
a triplicata que produziu a deriva medida em §1.

---

## 4. Fases

### Fase A — Regularizar `Container` e `ForAWS` como repositórios git
**Modelo: Sonnet. Teto: 25 tool uses.** Bloqueada por DP-9 (só para o `ForAWS`; o `Container`
pode andar sozinho).

Decisões já fechadas, não reabrir: DP-1=D, DP-7=D1, DP-10, DP-11.

**Proibições (raio de explosão):**
- Não tocar em `PantonicVideo`, `PantonicScanlator`, `PantonicMonitor`, `PantonicPatom`.
- **Não editar conteúdo de doutrina nesta fase.** O commit inicial é snapshot fiel (DP-11);
  qualquer correção de texto é Fase C.
- Não criar remote nem dar push — o dono cria os repositórios no GitHub (Fase E).

**A1. Varredura de credenciais — ANTES de qualquer `git add`.** Precedente do hub, e aqui vale
dobrado porque um dos repos é temático de AWS. Grep nos dois diretórios por:
`AKIA`, `ASIA`, `aws_secret_access_key`, `arn:aws`, `\b\d{12}\b` (account id),
`BEGIN [A-Z ]*PRIVATE KEY`, `password\s*[:=]`, `secret\s*[:=]`, `token\s*[:=]`.
Qualquer achado **para a fase** e vira relatório ao dono — nunca "limpar e seguir" por conta
própria.

**A2.** Copiar `.gitignore` e `.gitattributes` do hub para as duas raízes, conteúdo idêntico
(mesmo racional: LF canônico, sem o qual o drift-guard compara terminador em vez de regra).

**A3.** Em cada repo: `git init -b main` → `git add -A` → commit
`chore: snapshot canônico as-is (pré-reconciliação P-0725)`.

**A4.** Commit **separado** de normalização: `git add --renormalize .` →
`chore: normalizar terminadores para LF`. Separado de propósito — misturar EOL com conteúdo no
mesmo commit é o que torna o histórico ilegível.

**A5.** Verificar: `git status --short` limpo, `git log --oneline` com 2 commits em cada.

**Critério de pronto:** dois repositórios git locais, tree limpo, 2 commits, sem remote.

---

### Fase B — Declaração de aplicabilidade (`KIT.md` em cada raiz)
**Modelo: Sonnet. Teto: 10 tool uses.** É o artefato que responde literalmente ao pedido do dono
("subir com diretrizes específicas de uso"). Conteúdo já redigido — a execução é mecânica.

Cada raiz recebe um `KIT.md` com o mesmo esqueleto:

```markdown
# KIT — <nome> (camada <N> da governança Pantonic*)

**Aplica-se quando:** <condição>
**Requer:** <camada anterior, ou "nenhuma">
**Fornece:** <lista dos artefatos que esta camada possui/substitui>

Esta camada é aplicada por composição ordenada (ver P-0725 §3). Um artefato aqui SUBSTITUI o de
mesmo nome da camada anterior. Não copie este repositório para dentro de um projeto — declare-o
em `.claude/kit-layers.txt` e deixe o sync materializar.
```

Preenchimento por camada:

| Camada | Aplica-se quando | Requer |
|---|---|---|
| 1 — `PantonicApp` | **sempre** — todo projeto Pantonic* | nenhuma |
| 2 — `PantonicContainer` | a aplicação é baseada em containers | `PantonicApp` |
| 3 — `PantonicContainerForAWS` | o container roda na nuvem AWS | `PantonicContainer` |

O campo **Fornece** do App e do Container só fica correto depois da Fase C; até lá escreve-se
`(provisório — ver P-0725 Fase C)`.

---

### Fase C — Reconciliação 3-vias e extração de delta
**Modelo: Opus** (curadoria de conteúdo doutrinário, não mecânica). Depende de A e B.

Para cada um dos 17 artefatos da tabela §1, classificar em **uma** das quatro:

1. **Base** — vive só no App; camadas superiores herdam. (Esperado: a maioria do kit.)
2. **Override legítimo** — a camada superior o substitui por especialização real.
   (Confirmado: `ARQUITETURA_PANTONICA.md` no Container.)
3. **Cópia velha** — a camada superior tem uma versão *atrás* do canônico, sem conteúdo próprio.
   → **apagar do filho**, herdar. (Esperado: quase tudo do `ForAWS`, §1.1.)
4. **Camada errada** — artefato específico morando na base. → **descer**.
   (Confirmado: `pantonic-auditor-container.md`, §1.3.)

**Método:** comparar sempre **depois** da normalização LF da Fase A4 — antes disso o diff mede
terminador, não regra. Onde o filho estiver atrás, a pergunta não é "qual texto é melhor" e sim
"esta diferença carrega uma regra que o canônico não tem?". Se não carrega, é classe 3.

**Critério de pronto:** nenhum arquivo byte-idêntico entre duas camadas. Um artefato idêntico em
duas camadas é, por definição, uma triplicata esperando para derivar.

---

### Fase D — Composição de N camadas no consumidor
Depende da **Fase 3 do P-0721** (o `sync-kit.ps1` provado em sandbox). Generaliza aquele
mecanismo de 1 camada para uma lista ordenada:

- `.claude/kit-layers.txt` — uma camada por linha, na ordem de aplicação, `#` comenta.
- Recusar composição inválida (camada sem sua predecessora, §3).
- Materializar camada a camada, a posterior sobrescrevendo a anterior (DP-10).
- `.claude/kit-exclude.txt` continua respeitado, aplicado **por último**.
- `-Check` continua sendo a semente do drift-guard (DP-5).

Nenhum consumidor é migrado nesta rodada — os projetos finais estão fora de escopo (§0). A Fase D
entrega a capacidade; o primeiro consumo é assunto de um plano posterior.

---

### Fase E — Publicação
Dono cria os dois repositórios vazios no GitHub; execução adiciona o remote e dá push das duas
branches `main`. Espelha o que já se fez com o hub.

---

## 5. Relação com o P-0721 (rebase explícito)

Para não violar o guardrail de convergência de iniciativa (skill `proximo-passo`: dois planos
vivos disputando a mesma rota não se desempatam por FIFO):

| P-0721 | Situação após este plano |
|---|---|
| Fases 0, 1a, 1b, 2 (`done`) | **Mantidas.** O congelamento canônico do hub e sua regularização git seguem válidos e são pré-requisito daqui. |
| Fase 3 (provar D1 em sandbox) | **Mantida e ainda é a próxima tarefa executável.** A Fase D deste plano a estende de 1 para N camadas — não a substitui. |
| Fase 4 (migrar os 6 filhos) | **Superseded.** O conjunto de filhos deixou de existir como bloco único: 2 viraram camadas de governança (este plano), 4 viraram consumidores fora de escopo. |
| **DP-8** (5 filhos não são repos git) | **Encerrado como estava.** Substituído pela Fase A, que cobre só os 2 que continuam em escopo. Os outros 3 não precisam ser repos git para nada agora. |
| Fases 5, 6 | Mantidas, com o conjunto reduzido. |
| `TK-SGSS-ARQUETIPO` (residual §15×§16) | **Fechável** com o registro de §1.2 — é especialização, não deriva. |

---

## 6. Riscos

| Risco | Mitigação |
|---|---|
| **Publicar segredo de AWS** num repo temático de AWS | A1 é bloqueante e roda antes do primeiro `git add`. Achado para a fase. |
| **Camada 3 vazia** vira repositório-fantasma que ninguém mantém | DP-9 força a escolha consciente; o `KIT.md` declara o estado como provisório em vez de fingir conteúdo. |
| Fase C confundir ruído de formatação com divergência de regra | A4 (normalização LF em commit próprio) é pré-requisito duro de C. Já mordeu duas vezes nesta iniciativa. |
| Reconciliação apagar uma regra que só existia no filho | DP-11: snapshot publicado antes; toda remoção é reversível por `git diff` contra a baseline. |
| Novo plano coexistir com o P-0721 e os dois serem escolhidos como "próximo" | §5 rebaseia explicitamente, com Fase 4 marcada `superseded` e DP-8 encerrado. |

---

## Achados da execução

_(vazio — plano não iniciado)_
