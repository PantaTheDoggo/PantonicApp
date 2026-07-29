# Relatório consolidado — confronto PantonicApp × 21 frameworks públicos

Origem: `docs/plans/P-0729-v2-confronto.md` §2 `T3` (Estágio 2 da iniciativa `PANTONIC-V2`).

**Corpus:** `docs/benchmark/BM-00-pantonicapp.md` (auto-retrato) + `BM-01`..`BM-21` (21 frameworks
externos), grade fixa de 16 dimensões (`docs/benchmark/_ESQUEMA.md` linhas 10-27), matriz de
cobertura em `docs/benchmark/MATRIZ_DIMENSOES.md` (352 células: `+` 182, `~` 114, `—` 56).

**Regra de evidência deste relatório (herdada do `_ESQUEMA.md` linhas 39-43):** nenhuma afirmação
sobre framework externo sem citar o `BM-NN` de onde saiu — conhecimento de treino sobre projetos
famosos não é fonte admissível aqui. Nenhuma afirmação sobre o PantonicApp sem `arquivo:linha`,
sempre mediada pelo `BM-00`.

**Convenção de ponteiro:** `BM-NN§Dx` = dimensão `Dx` dentro de `docs/benchmark/BM-NN-<slug>.md`.

---

## 1. Veredito em uma página

### Onde o PantonicApp está à frente da prática pública

**Custo do processo agêntico é a única frente em que o Pantonic lidera sem empate.** A dimensão
D6 (contexto e custo) é `—` em 15 dos 21 frameworks e `+` em apenas 2 — `BM-04§D6` (orçamento
graduado 200/1.000/2.500 tokens por complexidade) e `BM-12§D6` (teto de 200k tokens com ordem de
priorização de leitura). O Pantonic tem orçamento vinculante por tarefa, batching obrigatório e
proibição de releitura de verificação (`BM-00§D6`, `GOVERNANCA.md:67-69`). Seis relatórios
independentes cobram essa ausência dos próprios frameworks que descrevem: `BM-01` (anti-prática 1),
`BM-03` (anti-prática 2), `BM-05` (fora da grade), `BM-07` (anti-prática 3), `BM-10`
(anti-prática 3) e `BM-20` (fora da grade). O corpus concorda que o problema existe; quase ninguém
o resolve.

**A telemetria de consumo é medida, não autorrelatada.** Todo fechamento de tarefa registra
`Consumo: N tool uses, ~Xk tokens, modelo, duração` lido do bloco `<usage>` da notificação, com 5
casos de estouro de teto já registrados em série (`BM-00§D12`,
`docs/DIARIO_DE_OBRAS.md:141-146,190-195`). Os 3 externos com D12 `+` instrumentam consumo —
`BM-04§D12` (JSONL append-only, 150+ campos), `BM-08§D12` (OpenTelemetry com tokens, latência,
sessões), `BM-17§D12` (OTel + Jaeger) — mas nenhum distingue medição de autorrelato, e `BM-08§D12`
declara explicitamente que a retenção histórica fica a cargo do backend, isto é, fora do framework.

**Modelo por fase escolhido por custo.** D4 é `+` em 5 dos 21. Só `BM-15§D3` amarra modelo a fase
por economia (Planning/Sonnet → Execution/Haiku → Review/Sonnet). O Pantonic declara `model:` por
papel nos 9 agentes (`BM-00§D4`, `.claude/agents/*.md:2-5`) e trata a troca para um modelo mais
caro como decisão que exige OK do dono (`BM-00§D16`, `GOVERNANCA.md:57-62`). `BM-02` (anti-prática
3) e `BM-05` (anti-prática 2) nomeiam a ausência disso como defeito — "impossível otimizar custo
vs. qualidade".

**Atualização do framework nunca é automática.** `BM-00§D10` (`GOVERNANCA.md:233-277`) exige
paridade `VERSION` ↔ `.claude/KIT_VERSION` e checagem por skill, jamais update automático.
`BM-12` (anti-prática 2) documenta o resultado oposto num framework de doutrina real: referência
dinâmica `@$(pwd)/path` sem versionamento semântico produz atualização silenciosa e consumidor que
não sabe o que mudou.

### Onde o PantonicApp está atrás

**Enforcement (D9) é a lacuna maior — e é a raiz das outras duas.** O Pantonic tem 8 guardrails
textuais e enforcement executável de 0% dentro do hub; o que realmente barra algo é o campo
`tools:` no frontmatter dos agentes (`BM-00§D9`, `GOVERNANCA.md:183-201`). No corpus, D9 é `+` em
13 dos 21, e três frameworks chegam a 100% executável: `BM-09§D9` (scripts Node validando 12+
padrões perigosos), `BM-13§D9` (validador Python disparado por GitHub Actions em cada edição de
issue), `BM-16§D9` (Makefile + pre-commit + CI). Quatro relatórios distintos classificam guardrail
puramente textual como anti-prática, com o mesmo argumento: `BM-04` (anti-prática 1: "impossível
auditar; enforcement interpretativo"), `BM-05` (anti-prática 3: "conformidade silenciosa"),
`BM-11` (anti-prática 2: "CLAUDE.md pode ser ignorado"), `BM-21` (anti-prática 2: "checklist em
Markdown é frágil contra erros humanos").

**Qualidade e testes (D8): o hub prescreve o que não pratica.** TDD com TF+TR é golden rule para
consumidores, mas o hub não tem suíte própria — `tests/**` vazio (`BM-00§D8`,
`ARQUITETURA_PANTONICA.md:18`, `GOVERNANCA.md:130-138`), fato que o próprio auto-retrato registra
como anti-prática 2. D8 é `+` em 10 dos 21, com pisos que são comandos e não prosa: `BM-18§D8`
(`test:coverage:ratchet` como gate de CI que não permite regressão), `BM-15§D8` (intervalos de
confiança por bootstrap, exit 1 abaixo do threshold), `BM-08§D8` (deflaking obrigatório: teste novo
passa em ≥5 execuções antes do merge).

**Segurança e permissões (D13): allowlist de comandos destrutivos é literalmente
`NÃO ENCONTRADO`.** O sandbox documentado cobre os auditores, restritos a `Read,Glob,Grep,Write`
(`BM-00§D13`, `.claude/agents/pantonic-auditor-arch.md:5`); segredos e allowlist de ações
destrutivas não existem no auto-retrato. D13 é `+` em 7 dos 21, e o padrão mais barato do corpus é
`BM-15§D13`: allowlist de subcomandos de `git`/`gh`, sem `push --force`, `reset --hard`,
`branch -D`.

### A única coisa que o PantonicApp deveria mudar primeiro

**Converter a forma do enforcement de texto para código — não acrescentar mais regras.**

O `P-0722` já decidiu cinco guardrails novas (G-DEADCODE, G-PLANFIDELITY, G-PREMISE, G-PLANREADY,
G-EXECREADY) cuja redação está mesclada ao Estágio 3A (`BM-00§D9`,
`docs/DIARIO_DE_OBRAS.md:208-212`; plano em `docs/plans/P-0729-v2-melhoria.md` §1). Elas nascem
textuais, sobre um enforcement que já é textual. Isso tem um custo composto que o corpus enxerga
melhor que o próprio framework: cada regra nova aumenta o volume que todo agente lê em toda sessão
— hoje ~600 linhas entre `GOVERNANCA.md` e `ARQUITETURA_PANTONICA.md` (`BM-00§D14`) — sem aumentar
a garantia. É D9 comendo D6 e D14 ao mesmo tempo.

O primeiro passo é pequeno e já tem alvo comprovado: um checador executável do próprio kit. Ele
pegaria hoje, sem nenhuma regra nova, o defeito que o auto-retrato admite na anti-prática 1 —
`.claude/README.md:8-19` lista 8 agentes enquanto `pantonic-auditor-container` existe em disco
(`BM-00§D4`). É exatamente o *artifact drift check* de `BM-15§D9` (regenera, falha se diferente) e
o `npm run skill:validate` de `BM-07§D8`. O segundo passo é a allowlist de `BM-15§D13`. Os dois
somados custam menos que qualquer uma das cinco guardrails textuais já decididas — e são a
condição para que elas valham alguma coisa.

**Nota sobre a régua mecânica.** A lista (a) do `MATRIZ_DIMENSOES.md` (lacuna de consenso) saiu
vazia: a única dimensão em que o `BM-00` é `—` é D2, e nenhum externo é `+` em D2. Isso significa
"nenhuma lacuna detectável pelo critério mecânico", não "o Pantonic não tem lacunas". As lacunas
reais deste corpus estão nas três células `~` do `BM-00` — D8, D9, D13 — confrontadas com os `+`
externos, que é o juízo que o `T2` deliberadamente não fez.

---

## 2. Dimensão por dimensão (D1..D16)

### D1 — Identidade e escopo — **MANTER**

**Pantonic hoje:** hub de doutrina + kit agêntico da família Pantonic* (desktop, Python+PySide6,
MVVM); não é ele mesmo uma aplicação — sem `infracore/`, `contracts/` nem `tests/` (`BM-00§D1`,
`GOVERNANCA.md:1-6`, `ARQUITETURA_PANTONICA.md:1-11`).

**Corpus:** D1 é `+` nos 22 — todo framework do corpus sabe dizer o que é. O eixo que separa é a
largura do escopo: `BM-01§D1` é explicitamente agnóstico de linguagem e stack; `BM-02§D1` cobre
"desde bugs até sistemas empresariais"; `BM-10§D1` é assistente de IDE para qualquer projeto;
`BM-20§D1` é toolkit de feature dev end-to-end. Nenhum dos 21 é desktop-first, e nenhum trata de
UI, Qt ou empacotamento de binário.

**Veredito — MANTER.** O escopo estreito é o que torna possíveis os guardrails de camada que
`BM-01§D9` não pode ter: uma constituição agnóstica de stack só consegue enunciar princípios
("Simplicity", "Anti-Abstraction", `BM-01§D3`), enquanto uma doutrina que sabe que a stack é
PySide6/MVVM pode enunciar regra verificável. Alargar o escopo compraria irrelevância.

---

### D2 — Vitalidade — **REJEITAR**

**Pantonic hoje:** `NÃO ENCONTRADO` para stars, licença e contribuidores — sem publicação pública,
sem `LICENSE` na raiz; o proxy de vitalidade é o `CHANGELOG.md` com 3 versões em 2026-07-29
(`BM-00§D2`, `VERSION:1`, `CHANGELOG.md:11,17`).

**Corpus:** os 21 são `~` — todos têm stars e push recente, nenhum informa contribuidores. A faixa
vai de 2.226 (`BM-20§D2`) a 164.915 (`BM-06§D2`). Três declaram licença ambígua `NOASSERTION`
(`BM-02§D2`, `BM-13§D2`, `BM-17§D2`) e `BM-13` (anti-prática 2) trata isso como risco legal real.

**Veredito — REJEITAR.** *Motivo escrito:* publicar o hub para adquirir as métricas desta dimensão
importaria um custo que o corpus documenta e não compensaria nenhum benefício de doutrina.
`BM-09` (anti-prática 2) mede o custo num repositório de 40 mil stars com mantenedor único:
"revisão manual não escala, bus factor = 1". `BM-13` (anti-prática 1) mede o outro lado: ciclo de
contribuição informal sem SLA deixa submissores esperando indefinidamente. O PantonicApp é bus
factor 1 por desenho (`BM-00§D16` — diretiva de priorização, publicação de plano e troca de modelo
exigem o dono), de modo que abrir a fila comunitária importaria o defeito sem o benefício. Stars e
contribuidores não medem qualidade de doutrina, e nada no corpus liga uma coisa à outra.

*Resíduo barato, deliberadamente não promovido a item de backlog:* declarar licença e propriedade
na raiz custa um arquivo e remove a ambiguidade que `BM-13` (anti-prática 2) descreve — mas isso é
higiene de repositório, não adoção da dimensão.

---

### D3 — Ciclo de vida do trabalho — **MANTER**

**Pantonic hoje:** PRD → Architecture → Spec → Sprint Plan → diário de obras → execução →
`guardrails-check` → `handover`, com gate de conformance como doutrina para consumidores
(`BM-00§D3`, `GOVERNANCA.md:158-178,196-197`).

**Corpus:** D3 é `+` em 19 dos 21. Os ciclos com gate nomeado são os mais próximos:
`BM-02§D3` tem `bmad-check-implementation-readiness` com veredito PASS/CONCERNS/FAIL antes da fase
de implementação; `BM-19§D3` separa Planning de Implementation e exige aprovação dos 3 documentos
de planejamento antes de prosseguir (`BM-19§D16`); `BM-05§D3` tem 7 fases com três gates
posicionais (3→4, 4→5, 6→7); `BM-20§D3` define gates por condição de erro (ambiguidade, padrão não
encontrado, versão divergente, conflito de arquitetura). No extremo oposto, `BM-03§D3` declara
artefatos como "enablers, not gates" e `BM-21§D9` é 100% texto sem verificação.

**Veredito — MANTER.** O ciclo do Pantonic já tem a forma que o corpus valida. O único delta —
gate de prontidão explícito entre planejamento e execução — **já está decidido**: G-PLANREADY e
G-EXECREADY (`P-0722`), com redação mesclada ao Estágio 3A (`docs/plans/P-0729-v2-melhoria.md` §1).
`BM-02§D3` e `BM-19§D16` são confirmação empírica externa dessa decisão, não recomendação nova.

---

### D4 — Papéis e modelo por fase — **MANTER**

**Pantonic hoje:** 9 agentes em `.claude/agents/*.md`, `model:` explícito por papel
(`BM-00§D4`, `GOVERNANCA.md:43-47`, `.claude/agents/*.md:2-5`); drift conhecido:
`.claude/README.md:8-19` lista 8.

**Corpus:** D4 é `+` em 5 dos 21 (`BM-04`, `BM-11`, `BM-15`, `BM-19`, `BM-20`). Papéis nomeados são
comuns — 6 agentes nomeados em `BM-02§D4`, 20 em `BM-04§D4`, 3 papéis fixos em `BM-19§D4`, 203
agentes em `BM-15§D1` — mas amarrar **modelo** a **fase** aparece uma única vez:
`BM-15§D3` (Sonnet planeja, Haiku executa, Sonnet revisa). `BM-20§D4` chega perto com uma distinção
diferente: agentes consultivos são *report-only*, agentes de workflow rodam em laço até ficar
verde.

**Veredito — MANTER.** A escolha do Pantonic diverge deliberadamente de `BM-15§D3` no ponto que
importa: execução roda em Sonnet, não em Haiku, porque execução escreve código e barato demais
converte economia de modelo em retrabalho de turnos — que é a métrica que o Pantonic mede
(`BM-00§D12`). A skill `modelo-por-fase` está decidida e não escrita (Estágio 3A); `BM-15§D3`
reforça a decisão. A distinção *advisory vs. workflow* de `BM-20§D4` já existe de fato no Pantonic
via `tools:` (auditores sem `Edit`/`Bash`, `BM-00§D13`).

---

### D5 — Unidade de trabalho e rastreabilidade — **ADAPTAR**

**Pantonic hoje:** a unidade é a tarefa atômica do diário (objetivo, arquivos-alvo, testes,
critério de pronto), fechada com `Resultado` + `Veredito` + `Consumo` (`BM-00§D5`,
`GOVERNANCA.md:92-93`, `docs/DIARIO_DE_OBRAS.md:59-61,113-146`).

**Corpus:** D5 é `+` em 3 dos 21. `BM-01§D5` afirma rastreabilidade bidirecional requisito↔código
via decisões técnicas e código↔teste via TDD obrigatório. `BM-11§D5` faz o rastro pelo artefato:
seção "What"/"Success Criteria" → `examples/` → Validation Loop com pytest. `BM-20§D5` é o mais
operacional: cada passo do plano carrega `file:line`, descrição, **comando de validação** e
artefato esperado. Os outros 18 não têm rastro — e três relatórios tratam isso como defeito grave
(`BM-05` fora da grade, `BM-08` anti-prática 3, `BM-09` anti-prática 3).

**Veredito — ADAPTAR.** O Pantonic tem os dois extremos do rastro (requisito no dossiê da tarefa,
comportamento trancado por TF+TR) e nada no meio: nenhum ponteiro verificável liga um ao outro.
Adaptar significa importar apenas o formato de `BM-20§D5` — `file:line` + comando de validação
dentro do dossiê da tarefa, campos que já existem em prosa como "arquivos-alvo" e "testes". Custo:
alteração de template, sem código. Deliberadamente **não** se adota a matriz formal de
rastreabilidade (ver §4, descarte 1).

---

### D6 — Contexto e custo — **ADAPTAR**

**Pantonic hoje:** orçamento vinculante de ~≤40 tool uses por tarefa, batching de chamadas
independentes, proibição de releitura de verificação; doutrina dividida entre o repo e o CLAUDE.md
global do usuário (`BM-00§D6`, `GOVERNANCA.md:67-69`, `C:\Users\panta\.claude\CLAUDE.md:30,107`).

**Corpus:** o diferencial confirmado pela lista (b) do `MATRIZ_DIMENSOES.md` — `BM-00` é `+` e só
2 externos acompanham. `BM-04§D6` gradua o orçamento por complexidade da tarefa (200 / 1.000 /
2.500 tokens) e declara o ROI que justifica gastar em confiança antes de executar. `BM-12§D6` fixa
teto de 200k tokens e prescreve ordem de leitura (README → CLAUDE.md → árvore) para reduzir
consultas. Os outros 19 vão de `NÃO ENCONTRADO` a menção implícita — `BM-21§D6` chega a admitir
que a única estratégia é "fragmentar em tarefas menores".

**Veredito — ADAPTAR.** O núcleo se mantém: teto vinculante e medido. O que falta é granularidade
— o teto do Pantonic é um número único (~40) independentemente de a tarefa ser uma correção de
uma linha ou um relatório de confronto, e a série histórica registra 5 estouros
(`BM-00§D12`), o que sugere que o número único ora sobra ora falta. `BM-04§D6` mostra a forma
barata de corrigir: classes de tarefa com teto próprio. Custo: uma tabela na doutrina, zero código.

---

### D7 — Memória e estado persistente — **ADAPTAR**

**Pantonic hoje:** três camadas — diário de obras (no repo), `MEMORY.md` por projeto (fora do
repo), CLAUDE.md global do usuário (fora de qualquer repo) (`BM-00§D7`, `GOVERNANCA.md:95-107`).

**Corpus:** D7 é `+` em 16 dos 21 — persistir estado em arquivo versionado é consenso
(`BM-01§D7` markdown em git, `BM-03§D7` specs como source of truth, `BM-19§D7` message bus em
arquivo com `handoff.md` por agente, `BM-21§D7` checkboxes em markdown). O que destoa é
`BM-08§D7`: um processo de fundo analisa transcrições passadas, extrai candidatos duráveis
(fatos, skills, contexto de projeto) e os deposita numa *inbox*; nada é aplicado sem revisão
explícita via `/memory inbox` (`BM-08§D16`, e prática transplantável 1 do mesmo relatório).

**Veredito — ADAPTAR.** O Pantonic já tem governança de memória escrita (lar canônico único, 1
fato por arquivo, índice obrigatório) mas a decisão de gravar é do agente no momento em que ele
está gravando — não há separação entre *descobrir* e *aprovar*. `BM-08§D7` é a única prática do
corpus que ataca isso, e ela é adaptável a custo baixo: candidato vai para uma fila, o dono
promove. Não se adota o resto do mecanismo (análise automática de transcrições), que exigiria
infraestrutura fora do escopo do hub.

---

### D8 — Qualidade e testes — **ADOTAR**

**Pantonic hoje:** TDD é golden rule com TF/TR obrigatórios — **para consumidores**. O hub não tem
suíte de testes própria (`tests/**` vazio): nada aqui pratica o TDD que prescreve (`BM-00§D8`,
`ARQUITETURA_PANTONICA.md:18`, `GOVERNANCA.md:130-138`; anti-prática 2 do próprio auto-retrato).

**Corpus:** D8 é `+` em 10 dos 21. Três padrões relevantes, todos executáveis:
- **Ratchet de cobertura** — `BM-18§D8`: `test:coverage:ratchet` é gate de CI que simplesmente não
  deixa a métrica cair (prática transplantável 2 do mesmo relatório, custo estimado ~2 dias).
- **Piso com significância estatística** — `BM-15§D8`: três camadas (análise estática ~2s, LLM
  judge ~30s, Monte Carlo 50-100 execuções), regressão detectada por intervalos de confiança com
  1.000 reamostragens, exit 1 abaixo do threshold.
- **Deflaking obrigatório** — `BM-08§D8`: teste novo só entra depois de passar em ≥5 execuções, em
  múltiplos ambientes (nenhum, Docker, Podman).

No outro extremo, `BM-04§D8` descreve um framework com 0% de cobertura que promete testes "para as
semanas 2-3" e é chamado de anti-prática pelo próprio relatório ("ferramenta aumenta
confiabilidade do dev, mas ela própria não tem testes").

**Veredito — ADOTAR.** O "piso de regressão nunca desce" do Pantonic é hoje verificado por leitura
e disciplina; `BM-18§D8` mostra a mesma ideia como um comando que falha o build. A adoção é nos
consumidores (o hub não tem código a testar, `BM-00§D1`), e é justamente por isso que ela precisa
descer pela doutrina em vez de continuar como prosa. `BM-04§D8` é o retrato do risco de não fazer:
um framework de qualidade sem qualidade própria.

---

### D9 — Guardrails e enforcement — **ADOTAR**

**Pantonic hoje:** 8 guardrails textuais (`GOVERNANCA.md` §7); enforcement por código executável é
0% dentro do hub — o enforcement real é o campo `tools:` restrito por agente. Mais 5 guardrails
decididas e não escritas (G-DEADCODE, G-PLANFIDELITY, G-PREMISE, G-PLANREADY, G-EXECREADY,
decididas em 2026-07-22) (`BM-00§D9`, `GOVERNANCA.md:183-201`,
`docs/DIARIO_DE_OBRAS.md:208-212`).

**Corpus:** D9 é `+` em 13 dos 21 — é a dimensão em que a prática pública está mais adiante.
- **100% executável:** `BM-09§D9` (scripts Node validando README, frontmatter obrigatório e 12+
  padrões perigosos de prompt), `BM-13§D9` (validador Python disparado por GitHub Actions a cada
  edição de issue, com rotulagem automática), `BM-16§D9` (Makefile + pre-commit + CI + paranoia de
  licenças).
- **Bloqueio em tempo de execução:** `BM-14§D9` — hook `PreToolUse` em Python, `exit 2` cancela a
  chamada de ferramenta, com log JSON para auditoria. O próprio `BM-14` (anti-prática 1) alerta que
  a implementação por casamento de string é frágil (contornável por `\rm`, alias, quebra do
  comando) e recomenda allowlist.
- **Detecção de deriva de artefato:** `BM-15§D9` — o CI regenera os artefatos e falha se o
  resultado diferir do que está versionado, mais detecção de colisão de nomes e validação de
  estrutura JSON.
- **Misto texto+código com análise semântica:** `BM-01§D9` — constituição de cinco princípios, CI
  (pytest, ruff, CodeQL) e `/speckit.analyze` tratando violação de "MUST" como CRITICAL.

Quatro relatórios classificam guardrail textual como anti-prática, com argumentos convergentes:
`BM-04` (anti-prática 1: ~60% texto e ~10% código, "impossível auditar"), `BM-05` (anti-prática 3:
"conformidade silenciosa"), `BM-11` (anti-prática 2: "CLAUDE.md pode ser ignorado; melhor hook
pré-execução validado em código"), `BM-21` (anti-prática 2: "100% texto, 0% código; frágil contra
erros humanos").

**Veredito — ADOTAR.** É o item nº 1 do relatório. **O que se adota é a forma, não o conteúdo:**
as 5 guardrails do `P-0722` já estão decididas e planejadas para o Estágio 3A
(`docs/plans/P-0729-v2-melhoria.md` §1) — recomendá-las de novo seria inflar o backlog. A
recomendação é converter enforcement de texto para código, seguindo `BM-15§D9` (drift check e
validação de estrutura) e não `BM-14§D9` (bloqueio por casamento de string), pelo motivo que o
próprio `BM-14` documenta. O alvo inicial já falha hoje: o drift do `.claude/README.md`
(`BM-00§D4`).

---

### D10 — Distribuição e versionamento do próprio framework — **MANTER**

**Pantonic hoje:** `VERSION` / `.claude/KIT_VERSION` em paridade obrigatória, Semver com
significado declarado, distribuição por `git subtree` (branch `kit`), `sync-kit.ps1` respeitando
`kit-exclude.txt`, checagem por skill `checar-versao-kit`, **nunca update automático**
(`BM-00§D10`, `GOVERNANCA.md:233-277`, `.claude/sync-kit.ps1:1-14`).

**Corpus:** D10 é `+` em 13 dos 21. Os mecanismos mais elaborados: `BM-02§D10` versiona em dois
eixos (módulo e instalador) com `manifest.yaml` guardando versão exata e hash de commit por
módulo; `BM-19§D10` casa compatibilidade por major (CLI v1.x só busca templates v1.x.x) e registra
o estado do consumidor em `.apm/metadata.json`; `BM-01§D10` faz o CLI detectar e avisar novas
versões. O contra-exemplo é `BM-12§D10`: instalação por referência dinâmica, sem semver e sem
changelog — que o mesmo relatório denuncia (anti-prática 2) como atualização silenciosa, e agrava
(anti-prática 3) com a ausência de registro de consumidores.

**Veredito — MANTER.** O mecanismo do Pantonic é comparável aos melhores do corpus e supera todos
num ponto: nenhum externo trata o update como decisão humana obrigatória. A auto-detecção de
`BM-01§D10` seria um retrocesso à luz de `BM-12` (anti-prática 2). O único delta com valor —
compatibilidade por major do `BM-19§D10` — é barato mas não urgente enquanto o kit não tiver
quebrado compatibilidade. O inventário de consumidores levantado por `BM-12` (anti-prática 3) não
cabe aqui: é dimensão nova (ver §3, D18).

---

### D11 — Extensibilidade — **ADOTAR**

**Pantonic hoje:** 8 skills (`.claude/skills/*/SKILL.md`) + 9 agentes; extensão do kit por
`git subtree` + `kit-exclude.txt` local, sem fork (`BM-00§D11`, `.claude/skills/*/SKILL.md:2-3`,
`.claude/README.md:35-44`).

**Corpus:** D11 é `+` em 14 dos 21 — extensão sem fork é consenso, por catálogo (`BM-01§D11`),
override declarativo (`BM-02§D11`), plugins com descoberta automática (`BM-05§D11`), registro de
decorador (`BM-16§D11`) ou hooks em pontos fixos (`BM-18§D11`). O que diferencia os melhores não é
o mecanismo, é a **validação do artefato de extensão**: `BM-07§D8` roda `npm run skill:validate` e
`npm run plugin:validate` como gate de contribuição; `BM-15§D11` exige
`plugin-eval score --depth quick` e `make generate-all` antes do commit, com o CI recusando
divergência (`BM-15§D9`); `BM-09§D9` valida que todo arquivo de regra tem `description`, `globs` e
`alwaysApply`, e detecta arquivos vazios ou gerados com erro.

**Veredito — ADOTAR.** O Pantonic tem 17 artefatos de extensão (8 skills + 9 agentes) e nenhum
validador de estrutura — e já paga por isso: o auto-retrato registra que o README do kit diverge
do disco (`BM-00§D4`, anti-prática 1). É o mesmo item de trabalho do D9 (um checador, dois
checadores dentro dele), motivo pelo qual as duas linhas de backlog devem ser consolidadas em uma
no `T4`. Custo baixo: um script que lê `.claude/agents/*.md` e `.claude/skills/*/SKILL.md` e
confere frontmatter e paridade com o README.

---

### D12 — Observabilidade e métricas — **ADAPTAR**

**Pantonic hoje:** série histórica real — todo fechamento registra
`Consumo: N tool uses, ~Xk tokens, modelo, duração`, medido no bloco `<usage>` da notificação e
nunca por autorrelato; 5 casos de estouro de teto registrados (`BM-00§D12`,
`C:\Users\panta\.claude\CLAUDE.md:107`, `docs/DIARIO_DE_OBRAS.md:141-146,190-195`).

**Corpus:** D12 é a segunda dimensão mais fraca do corpus — `+` em apenas 3 dos 21, `—` em 9.
`BM-04§D12` mantém `workflow_metrics.jsonl` append-only com 150+ campos (consumo, qualidade,
eficiência), rotação mensal, análise semanal e testes A/B. `BM-08§D12` instrumenta com
OpenTelemetry (sessões, latência por ferramenta, tokens de entrada/saída/cache, operações de
arquivo) exportando para backends externos — e declara que a retenção histórica é responsabilidade
do backend. `BM-17§D12` repete o padrão OTel + Jaeger. Cinco relatórios listam a ausência de série
histórica como anti-prática (`BM-02`, `BM-10`, `BM-11`, `BM-18`, `BM-20`), sendo o argumento de
`BM-20` (anti-prática 3) o mais próximo da doutrina Pantonic: sem série, "cada run recomeça do
zero; sucessos prévios não criam piso anti-regressão".

**Veredito — ADAPTAR.** A **fonte** do Pantonic é melhor que a de qualquer externo — dado medido,
não autorrelatado, com o desvio do autorrelato já quantificado no próprio diário (`BM-00§D5`
registra autoestimativa 13 contra 20 medido). O **formato** é pior: a série vive em prosa dentro do
diário, o que significa que detectar tendência exige reler o diário. `BM-04§D12` mostra a forma
barata: linha append-only estruturada, agregável sem leitura humana. Adaptar é manter a fonte e
mudar o suporte. Isso também endereça a anti-prática 3 do próprio `BM-00` — cinco estouros viraram
prosa repetida em vez de sinal.

---

### D13 — Segurança e permissões — **ADOTAR**

**Pantonic hoje:** sandbox por agente via `tools:` no frontmatter — auditores restritos a
`Read,Glob,Grep,Write`, sem `Edit`/`Bash`, enforçado pelo harness. Segredos e allowlist de comandos
destrutivos: `NÃO ENCONTRADO` (`BM-00§D13`, `.claude/agents/pantonic-auditor-arch.md:5`,
`.claude/agents/pantonic-scout.md:5`).

**Corpus:** D13 é `+` em 7 dos 21. Três famílias de solução:
- **Allowlist de subcomandos** — `BM-15§D13`: `git` e `gh` restritos a subcomandos seguros, sem
  `push --force`, `reset --hard`, `branch -D`; mais gate de `author_association`.
- **Avaliação por comando** — `BM-10§D13`: não há lista fixa; cada comando carrega
  `requires_approval`, com modificação de dependências, `rm -rf`, `mv` e `sed -i` sinalizados;
  `CLINE_COMMAND_PERMISSIONS` permite padrões allow/deny.
- **Detecção de padrão perigoso em conteúdo** — `BM-09§D13`: 12+ regras cobrindo exfiltração de
  credenciais, chaves SSH, tokens AWS, bootstraps remotos, bypass de TLS, hooks de persistência e
  injeção Unicode. `BM-18§D12` complementa com sanitização de segredos em log (`[REDACTED]`).

O corpus também traz o único incidente real: `BM-16§D13` documenta o comprometimento de maio/2026
— PAT roubado, propagação a 30 repositórios, tokens de deploy expostos, resposta com rotação
org-wide e PATs de escopo fino com expiração. `BM-19§D13` descreve o risco análogo sem incidente:
templates podem injetar instruções maliciosas em agentes, e o framework admite não ter assinatura
criptográfica nem varredura de conteúdo.

**Veredito — ADOTAR.** O padrão de `BM-15§D13` é o mais barato e o menos frágil do corpus:
allowlist de subcomandos, declarativa, sem código de parsing — evitando explicitamente o problema
que `BM-14` (anti-prática 1) documenta no bloqueio por string. O Pantonic já usa o mecanismo certo
(`tools:` no frontmatter) numa parte dos agentes; falta estendê-lo à granularidade de comando para
os agentes que têm `Bash`. Custo: configuração, não código.

---

### D14 — Onboarding humano e documentação — **ADOTAR**

**Pantonic hoje:** `GOVERNANCA.md` (277 linhas) + `ARQUITETURA_PANTONICA.md` (276 linhas), ambos
abaixo do limiar de 500 linhas que exigiria `DOC_MAP.md`; `.claude/README.md` (50 linhas) onboarda
o kit; ~600 linhas ao todo (`BM-00§D14`, `GOVERNANCA.md:1-8,214`,
`ARQUITETURA_PANTONICA.md:1-11`).

**Corpus:** D14 é `+` em 19 dos 21 — é a dimensão mais bem coberta do corpus. Os tempos declarados
são comparáveis ao Pantonic: `BM-03§D14` (2 min de setup, 20 min para a primeira mudança, 30 min
para conhecimento funcional), `BM-20§D14` (2 min para decidir), `BM-21§D14` (~5 min para decidir,
~10 min para começar), `BM-04§D14` (5 min, com quatro níveis progressivos). O padrão que interessa
não é o volume, é a **origem**: `BM-13§D7` gera o README a partir de um CSV que é a única fonte de
verdade, com gerador idempotente (prática transplantável 2 do mesmo relatório); `BM-07§D7`
regenera as tabelas do README a partir da estrutura de diretórios via `npm start`.

**Veredito — ADOTAR.** O volume do Pantonic está bom; a **manutenção manual** é o defeito, e ele já
se manifestou: `.claude/README.md:8-19` lista 8 agentes enquanto existem 9 em disco (`BM-00§D4`,
anti-prática 1), ou seja, o documento de onboarding do kit já mente. `BM-13§D7` e `BM-07§D7` dão a
correção estrutural: o README do kit passa a ser derivado de `.claude/agents/*.md` e
`.claude/skills/*/SKILL.md`, não escrito à mão. É a mesma peça de trabalho do D11 — um gerador e um
validador são o mesmo script rodando em dois modos.

---

### D15 — Multi-projeto, multi-repo e equipe — **ADAPTAR**

**Pantonic hoje:** doutrina compartilhada por `git subtree`, provada em `PantonicVideo`; o CLAUDE.md
global do usuário vale para todos os projetos, não só os Pantonic* — parte da doutrina mora fora de
todo repo (`BM-00§D15`, `GOVERNANCA.md:220-231`,
`C:\Users\panta\.claude\CLAUDE.md:1,3,17,30,51,69,84,107`).

**Corpus:** D15 é `+` em 5 dos 21 e `—` em 6 — é a segunda dimensão mais fraca. O padrão mais
diretamente aplicável é `BM-02§D15`: overrides de **time** (`.toml`, versionados, herdados por
todos) separados de overrides **pessoais** (`.*.user.toml`, gitignored). `BM-10§D15` usa a mesma
divisão em outra forma (config global em `~/.cline/`, config de projeto em `.cline/` versionada e
sem segredos). `BM-20§D15` compartilha artefatos entre projetos por um store fora do repo
(`~/.prp/<key>/`). `BM-01§D15` admite que, em monorepo, o compartilhamento de doutrina é manual —
e o próprio relatório chama isso de anti-prática 2 ("duplicação = divergência").

**Veredito — ADAPTAR.** Há um achado concreto aqui: dois dos diferenciais do Pantonic dependem de
linhas que não estão em nenhum repositório. O orçamento de contexto (`BM-00§D6` cita
`C:\Users\panta\.claude\CLAUDE.md:30,107`) e a telemetria de consumo (`BM-00§D12` cita
`C:\Users\panta\.claude\CLAUDE.md:107`) vivem no CLAUDE.md global do usuário. Isso significa que um
consumidor que receba o kit por `git subtree` **não recebe** o que o `BM-00` apresenta como
diferencial do framework. A divisão de `BM-02§D15` resolve: o que é regra de todos os projetos do
dono fica global; o que é doutrina Pantonic desce para o repo versionado e viaja no kit. Custo:
mover texto e ajustar ponteiros — mas exige decisão do dono, porque mexe em arquivo fora do repo.

---

### D16 — Interação com o humano — **MANTER**

**Pantonic hoje:** nunca automáticos — atualização do kit, diretiva de priorização, publicação de
plano do Estágio 3B e troca de modelo de execução para um mais caro; todos exigem escrita ou OK
explícito do dono (`BM-00§D16`, `GOVERNANCA.md:238-242,108-112,57-62`,
`docs/DIARIO_DE_OBRAS.md:49-52`).

**Corpus:** D16 é `+` em 20 dos 21 — o consenso público é que o humano aprova. As formas variam:
aprovação por ação (`BM-10§D16`, com modo YOLO explicitamente opt-in), aprovação de artefato antes
da fase seguinte (`BM-19§D16`, três documentos de planejamento), confirmação verbal bloqueante
(`BM-21§D16`, o "Go" antes de expandir as subtarefas), revisão de inbox antes de persistir memória
(`BM-08§D16`), e o mais elaborado: `BM-20§D16` com *Standing Decisions* — o que já foi decidido o
agente resolve sozinho e registra como `auto`; o que está fora do escopo decidido ele escala em 2-3
linhas.

**Veredito — MANTER.** A lista de "nunca automático" do Pantonic é mais restritiva que a média do
corpus e contém um item que nenhum externo tem: **a troca de modelo para um mais caro**
(`BM-00§D16`, `GOVERNANCA.md:57-62`) — governança de custo tratada como decisão humana, não como
otimização. Os *Standing Decisions* de `BM-20§D16` são um refinamento interessante, mas o Pantonic
já tem o equivalente funcional (a lista fechada de itens não-automáticos) e importá-los agora
acrescentaria um artefato de estado a manter sem fechar nenhuma lacuna. Deliberadamente não
adotado: o modo sem aprovação (ver §4, descarte 8).

---

### Resumo dos 16 vereditos

| Veredito | Dimensões | Total |
|---|---|---|
| **MANTER** | D1, D3, D4, D10, D16 | 5 |
| **ADOTAR** | D8, D9, D11, D13, D14 | 5 |
| **ADAPTAR** | D5, D6, D7, D12, D15 | 5 |
| **REJEITAR** | D2 | 1 |

Os 5 `ADOTAR` consolidam em **3 peças de trabalho**, não 5: (i) um checador/gerador executável do
kit — cobre D9 (forma do enforcement), D11 (validação de artefato de extensão) e D14 (README
derivado do disco); (ii) allowlist de comandos destrutivos por agente — D13; (iii) piso de
regressão como comando na doutrina dos consumidores — D8.

---

## 3. Dimensões novas propostas (D17+)

Critério: preocupação pertinente a um framework desktop Python/PySide6 movido a agentes que **não
cabe** em nenhuma das 16 dimensões e que o Pantonic nunca considerou. Origem declarada em cada
caso: lista (c) do `MATRIZ_DIMENSOES.md` (linhas 62-78) ou leitura direta do corpus.

### D17 — Precedência e escopo entre mecanismos de doutrina coexistentes

*(lista (c) nº 3)*

**O que é.** Quando um framework oferece vários mecanismos para dizer a mesma coisa — regra global,
regra de projeto, skill, agente, hook — falta a regra que diz **qual vence** quando dois colidem e
**onde** cada tipo de conteúdo deve morar.

**Quem pratica (ou sofre).** `BM-10` (fora da grade) enuncia o problema com precisão: `.clinerules/`,
`hooks/`, `skills/` e `plugins/` são todos executáveis, mas não há guia de escopo dizendo "use
regra para X, hook para Y". `BM-14` (fora da grade) tem a variante de ordem: a precedência de
múltiplos hooks no mesmo evento não é clara. `BM-02§D15` é o único que resolve parcialmente, com a
hierarquia declarada time → usuário.

**Por que é pertinente ao Pantonic.** O framework tem quatro superfícies de doutrina — CLAUDE.md
global do usuário, `GOVERNANCA.md`, skills e agentes — e a fronteira entre elas é ela própria uma
regra que vive na superfície mais volátil, fora de todo repositório (`BM-00§D15`,
`C:\Users\panta\.claude\CLAUDE.md:1,3,17,30,51,69,84,107`). Isso não é D11 (como se estende) nem
D15 (quem compartilha): é a topologia interna da doutrina.

**Custo.** Baixo — uma tabela de precedência no `GOVERNANCA.md` mais a decisão de residência de
cada tipo de conteúdo. Nenhum código.

---

### D18 — Registro de consumidores e inventário de versões instaladas

*(lista (c) nº 2, generalizada)*

**O que é.** Saber, do lado do produtor da doutrina, **quem** consome, **qual versão** cada um tem
e **quando** foi o último sync — em vez de descobrir por inspeção manual repositório a repositório.

**Quem pratica.** `BM-07` (fora da grade) trata o `marketplace.json` como fonte canônica de
descoberta, desacoplada do repositório. `BM-15` (fora da grade) federa plugins por git-subdir e
admite a lacuna correspondente: não há governança de versionamento nem SLA entre contribuições
locais e remotas, de modo que quebra de compatibilidade cruzada não é detectada. `BM-19§D10`
resolve pelo lado do consumidor, com `.apm/metadata.json` guardando versão instalada, assistentes e
timestamps. `BM-12` (anti-prática 3) enuncia a falta no lado do produtor e propõe exatamente o
artefato: um documento de adoção com lista, versão e último sync.

**Por que é pertinente ao Pantonic.** A doutrina se propaga por `git subtree` para consumidores
(provado em `PantonicVideo`, `BM-00§D15`, `GOVERNANCA.md:220-231`), e o hub não tem nenhum registro
de quem está em qual versão. Consequência prática: é impossível responder "quais consumidores ainda
não receberam a guardrail X" sem abrir cada repositório. Não é D10 (como o consumidor instala e
atualiza) nem D15 (quem compartilha a doutrina): é o inventário do parque instalado.

**Custo.** Baixo — um arquivo no hub, atualizado pelo mesmo passo que já aplica a versão
(`.claude/sync-kit.ps1:1-14`, `BM-00§D10`).

---

### D19 — Recuperação de sessão e continuidade após perda de contexto **não planejada**

**O que é.** O que acontece quando o contexto acaba **no meio** de uma tarefa, e não no fim — como
o trabalho parcial é reconstituído sem refazer a descoberta.

**Quem pratica.** `BM-19` (fora da grade) é o caso mais explícito: além do estado persistente, o
framework tem `apm-9-recover` e `summarize-session` como **orquestração de reconexão**, e o
relatório argumenta que isso não cabe em D7 porque vai além de armazenamento. `BM-08§D3` persiste
transcrições de sessão localmente e oferece `/rewind` para versionamento intra-sessão.
`BM-10§D7` implementa checkpoints em um repositório git paralelo, com restauração seletiva
(só arquivos, só tarefa, ou tudo). `BM-20§D7` mantém `state.json` que preserva o estado quando o
laço atinge o máximo de iterações, e reconcilia contra git/gh no `--resume`.

**Por que é pertinente ao Pantonic.** A doutrina cobre muito bem a troca **planejada** de contexto
— uma tarefa por contexto, skill `handover`, diário como estado (`BM-00§D3`, `BM-00§D5`). Não cobre
a troca **não planejada**, e a série histórica mostra que ela acontece: 5 casos medidos de estouro
de teto (`BM-00§D12`, `docs/DIARIO_DE_OBRAS.md:141-146,190-195`). Hoje o custo desse evento é
reexecutar a descoberta inteira no contexto seguinte — que é o oposto exato do que D6 protege.

**Custo.** Baixo a médio — um procedimento de checkpoint intermediário no diário quando o consumo
cruza uma fração do teto, sem infraestrutura nova.

---

### D20 — Reversibilidade do trabalho do agente

**O que é.** Desfazer o que o agente escreveu **sem** contaminar o histórico de trabalho — separar
o snapshot de segurança do commit com significado.

**Quem pratica.** `BM-10§D7` é o desenho de referência: repositório *shadow* separado, snapshot
automático após cada ação de ferramenta, comparação de diff e restauração seletiva, sem tocar no
`.git` principal e desativável em repositórios grandes (prática transplantável 1 do mesmo
relatório, ~40h estimadas). `BM-08` (fora da grade) menciona checkpointing integrado a git
worktrees, e o relatório observa que isso não cabe bem em D7 porque é estado de código, não
memória. `BM-14` (fora da grade) enuncia a falta pelo negativo: não há mecanismo de rollback para
hooks que bloquearam ações.

**Por que é pertinente ao Pantonic.** As aplicações da família escrevem no disco do usuário
(`BM-00§D1`, `ARQUITETURA_PANTONICA.md:1-11`) e a doutrina de execução é editar direto na árvore de
trabalho, com o git do próprio trabalho como única rede de segurança — o que empurra o executor a
commitar cedo para se proteger, poluindo o histórico, ou a não se proteger. Não é D7 (memória de
doutrina) nem D13 (permissão para agir): é o que sobra depois de agir.

**Custo.** Médio — é a dimensão mais cara desta lista, e a única em que a recomendação honesta é
"considerar", não "adotar".

---

### D21 — Vida útil e deprecação da própria doutrina

**O que é.** O procedimento pelo qual uma regra **sai** do framework: revisão periódica, marcação
de obsolescência, período de transição.

**Quem pratica.** `BM-12` (fora da grade) enuncia a falta e propõe a política: regra depreciada
permanece por N versões menores antes de ser removida, porque mudança de sintaxe sem transição
"causa choque em bases grandes". `BM-17` (fora da grade) exibe a versão bem resolvida: duas versões
da linguagem de domínio (Colang v1.0 e v2.x) coexistem sem breaking change, com adoção gradual.
`BM-07§D3` tem o gatilho barato: re-review cíclico a cada 6 meses dos artefatos já aprovados —
segurança de longo prazo contra artefato envelhecido (prática transplantável 3 do mesmo relatório).

**Por que é pertinente ao Pantonic.** O framework tem 8 guardrails escritas mais 5 decididas
(`BM-00§D9`) e ~600 linhas de doutrina lida por todo agente em toda sessão (`BM-00§D14`). Nenhuma
regra jamais saiu. Como cada linha de doutrina é reenviada em cada turno, uma doutrina que só
cresce é um imposto crescente sobre exatamente a dimensão em que o framework lidera (D6). Não é
D10 (versionar o kit) nem D14 (quanto se lê para começar): é a taxa de saída, não a de entrada.

**Custo.** Baixo — um gatilho de revisão periódica com pergunta única: "esta regra mudou algum
comportamento nos últimos N meses?".

---

### D22 — Integridade da cadeia de suprimentos da própria doutrina

**O que é.** Garantir que o artefato de doutrina que chega ao consumidor é o que o produtor
escreveu — considerando que esse artefato **são instruções que um agente executa**.

**Quem pratica (e quem sofreu).** `BM-16§D13` é o único incidente real do corpus: um PAT roubado
propagou-se a 30 repositórios e a tokens de deploy, com uma versão comprometida publicada no
índice de pacotes; a resposta foi rotação org-wide, contas resetadas, infraestrutura offline e
PATs de escopo fino com expiração. `BM-19§D13` descreve o risco estrutural sem incidente: templates
podem injetar instruções maliciosas direcionando agentes, e o framework admite não ter assinatura
criptográfica nem varredura de conteúdo (anti-prática 1 do mesmo relatório: "não copiar sem antes
estabelecer verificação de assinatura ou allowlist"). `BM-10§D13` adota a mitigação mínima: regras,
hooks, skills e plugins devem vir de fonte confiável porque executam código.

**Por que é pertinente ao Pantonic.** O kit se propaga automaticamente para os consumidores no
próximo sync (`BM-00§D10`, `.claude/sync-kit.ps1:1-14`), e o conteúdo propagado são agentes e
skills — instruções que rodam com as ferramentas que o frontmatter concede (`BM-00§D13`). Um
artefato adulterado no hub vira execução em todos os consumidores sem nenhuma verificação
intermediária. O fato de o hub ser local e privado reduz a exposição, mas não elimina o vetor:
`BM-16§D13` mostra que o comprometimento veio de credencial, não de repositório público.

**Custo.** Baixo, na versão mínima — commits assinados no branch de distribuição e verificação no
sync. Alto, na versão completa (assinatura e varredura de conteúdo por artefato), que o corpus
inteiro deixa em aberto.

---

## 4. Descartes justificados

Práticas presentes e populares no corpus, deliberadamente **não** recomendadas, com o motivo do
conflito com as premissas Pantonic (desktop-first, custo por turno, uma tarefa por contexto,
clean architecture, decisão do dono).

**1. Matriz formal de rastreabilidade requisito → código → teste.**
Praticada por `BM-01§D5` (bidirecional) e cobrada como falta por três relatórios (`BM-05` fora da
grade, `BM-08` anti-prática 3, `BM-09` anti-prática 3). *Motivo do descarte:* o custo de
manutenção cresce com o número de requisitos e é pago em leitura, a cada turno de cada tarefa. O
Pantonic já tranca comportamento onde importa — TF por tarefa e TR de regressão (`BM-00§D8`) — e a
matriz duplicaria o rastro sem trancar nada a mais. Adota-se apenas o ponteiro barato (`file:line`
+ comando de validação, `BM-20§D5`), que é o veredito ADAPTAR de D5.

**2. Portabilidade multi-harness (adapter para N plataformas).**
`BM-15§D4` mantém uma arquitetura canônica e adapta automaticamente para 5 plataformas; `BM-01§D4`
suporta 30+ agentes de IA; `BM-12` (fora da grade) cobra de si mesmo a falta de um compilador
automático entre IDEs. *Motivo do descarte:* o adapter é um segundo sistema a manter, e o próprio
`BM-15` (fora da grade) documenta o preço — sem fallback manual, uma capacidade nova que o alvo não
suporta degrada em silêncio. Um framework de um dono em um harness paga o custo integral e não
recebe o benefício.

**3. Marketplace público e curadoria comunitária.**
`BM-07§D1`, `BM-09§D1` e `BM-13§D1` são exatamente isso. *Motivo do descarte:* os dois relatórios
de curadoria comunitária medem o custo em seus próprios termos — `BM-09` (anti-prática 2): "revisão
manual em repositório de 40 mil stars não escala, bus factor = 1"; `BM-13` (anti-prática 1): ciclo
informal sem SLA deixa submissores esperando. O Pantonic é bus factor 1 por desenho (`BM-00§D16`),
então abrir a fila importaria o gargalo sem ganhar nada. É o mesmo motivo do REJEITAR de D2.

**4. Avaliação estatística de agentes como gate de todo commit.**
`BM-15§D8` roda Monte Carlo com 50-100 execuções e bootstrap de 1.000 reamostragens. *Motivo do
descarte:* o próprio `BM-15` (anti-prática 1) mede o custo — ~5 min por PR — e recomenda reservar a
camada cara para releases. Custo por turno é a premissa que o Pantonic protege (`BM-00§D6`);
avaliação estatística de agente pode ter lugar em fechamento de versão do kit, nunca no ciclo de
uma tarefa.

**5. Meta de percentual de cobertura de testes.**
`BM-11§D8` exige ≥80% nos casos de uso. *Motivo do descarte:* percentual premia teste barato e
pune código difícil de instrumentar; o piso do Pantonic é comportamental ("nunca desce", teste com
significado alterado é reescrito e não deletado). O ratchet de `BM-18§D8` entrega o efeito
antirregressão sem fixar meta — e é isso, não o percentual, que o veredito ADOTAR de D8 recomenda.

**6. Multi-agente concorrente com message bus ou coordinated teams.**
`BM-19§D7` (fila em arquivo com diretório por agente), `BM-10§D15` (coordinator-specialist com
mailbox e mission log), `BM-20§D15` (multi-workstream em worktrees isolados, até 3 concorrentes).
*Motivo do descarte:* colide frontalmente com "uma tarefa por contexto" e com o custo por turno —
cada agente parte frio e repaga a doutrina inteira. `BM-10` (anti-prática 2) ainda documenta o
limite prático: o estado do time fica no disco de uma máquina, sem sincronização. No Pantonic,
delegar a subagente é higiene de contexto, não paralelismo, e essa distinção deve permanecer
explícita.

**7. Atualização automática do framework no consumidor.**
`BM-05§D10` faz auto-update em streaming; `BM-01§D10` detecta e avisa; `BM-12§D10` usa referência
dinâmica que atualiza sem passo nenhum. *Motivo do descarte:* `BM-12` (anti-prática 2) descreve o
resultado — "refs dinâmicas = atualizações silenciosas", consumidor sem noção de breaking change.
O Pantonic torna o update decisão do dono (`BM-00§D10`, `BM-00§D16`); adotar auto-update trocaria
uma garantia por conveniência.

**8. Modo sem aprovação (YOLO / `--non-interactive`).**
`BM-10§D13` oferece YOLO desativando todas as verificações; `BM-02§D16` oferece
`--non-interactive` executando "até a conclusão natural". *Motivo do descarte:* enquanto o
enforcement do Pantonic for textual (`BM-00§D9`), a lista de "nunca automático" (`BM-00§D16`) é a
única barreira que existe de fato — remover o humano remove tudo. A ordem correta é inversa à do
corpus: primeiro o enforcement vira código (ADOTAR de D9), só então discutir automação sem
supervisão.

---

## 5. Vieses do corpus — o que 21 repositórios públicos não conseguem informar

**1. Viés de sobrevivência.** O corpus só contém frameworks que existem. Os que morreram sem deixar
repositório são invisíveis, e mesmo os moribundos aparecem vivos: `BM-12§D1` só se revela
descontinuado porque o README redireciona para outro repositório, e `BM-21§D2` está parado desde
2025-11-05 (~9 meses) sem que nada além da data indique isso. Nenhuma conclusão do tipo "esta
prática funciona" pode ser tirada daqui — só "esta prática está escrita em um repositório ativo".

**2. Documentação não é prática.** A regra de evidência do corpus (`_ESQUEMA.md` linhas 39-43) mede
o que está escrito no repositório, não o que acontece em uso. Um framework com D9 "100% executável"
(`BM-16§D9`) pode ter regras triviais executadas com rigor; um com guardrail textual pode ser
seguido à risca por um time disciplinado. A matriz mede **forma de enforcement**, não
**conformidade obtida** — e essa distinção é decisiva para o item nº 1 deste relatório.

**3. Popularidade não é qualidade.** A faixa vai de 2.226 estrelas (`BM-20§D2`) a 164.915
(`BM-06§D2`), e nada no corpus liga estrelas a resultado. O framework com a arquitetura de
avaliação mais rigorosa (`BM-15§D8`) tem 38.344 estrelas (`BM-15§D2`); um com 0% de cobertura de
testes (`BM-04§D8`) tem 23.613 (`BM-04§D2`).

**4. Nenhum dado longitudinal — o que falha depois de 6 meses é desconhecido.** D12 é `+` em apenas
3 dos 21, e mesmo esses não retêm série: `BM-08§D12` declara explicitamente que a retenção
histórica é responsabilidade do backend de destino, isto é, fora do framework. Nenhum dos 21
publica "esta prática foi adotada e depois abandonada porque X". O corpus é uma fotografia de
2026-07-29, não um filme.

**5. Custo real é o maior buraco.** D6 é `—` em 15 dos 21. Os dois `+` **declaram** orçamento
(`BM-04§D6`, `BM-12§D6`) mas nenhum publica gasto medido. Consequência direta para este relatório:
os números de consumo do diário do Pantonic (`BM-00§D12`) não têm benchmark externo — quando uma
tarefa custa 45 tool uses, não existe nenhum dado público que diga se isso é bom ou ruim para uma
tarefa daquele tipo. A liderança do Pantonic em D6/D12 é, ao mesmo tempo, um isolamento: ele mede
sozinho e se compara consigo mesmo.

**6. Viés de domínio — nenhum framework desktop no corpus.** Zero dos 21 trata de UI, Qt/PySide6,
empacotamento de binário ou ciclo de vida de aplicação de desktop; os escopos declarados em D1 são
CLI, IDE, biblioteca ou metodologia. As dimensões em que a doutrina Pantonic é mais específica —
MVVM, regra de camadas, thread de UI — não têm **nenhum** comparável. A única aproximação em todo o
corpus é `BM-18` (fora da grade): 11 camadas com grafo de dependência acíclico verificável por
`npm run architecture:check` — que é TypeScript e serve como **forma** (verificação executável de
camada), nunca como conteúdo. Onde o Pantonic mais precisaria de espelho, o corpus é cego.

**7. Viés do coletor — parte dos `—` é orçamento de coleta, não ausência real.** Os 21 relatórios
saíram de um mesmo esquema, com teto de 160 linhas e ~10-12 buscas de conteúdo por repositório
(`BM-05` declara 10 buscas; `BM-20` declara 12; `BM-01` declara 12). `BM-08§D6` admite
literalmente que `docs/cli/token-caching.md` "existe (não buscado no orçamento)" — ou seja, ao
menos um `NÃO ENCONTRADO` do corpus é limite de coleta, não do framework. A matriz conta esse caso
como ausência. Onde uma conclusão deste relatório dependeu de uma célula `—` isolada, ela foi
formulada como "o corpus não registra", não como "o framework não tem".

**8. Autoavaliação no `BM-00`.** O auto-retrato foi escrito pelo mesmo sistema que este relatório
julga, com acesso privilegiado ao repositório que os 21 externos não tiveram (`arquivo:linha` local
contra URL pública). Isso corta nos dois sentidos: o `BM-00` enxerga defeitos que um coletor
externo jamais veria (as três anti-práticas que ele lista contra si mesmo), e pode ter sido
generoso em dimensões que ninguém auditou de fora. As três células `~` do `BM-00` (D8, D9, D13)
são autoconfessadas; não há garantia de que sejam as únicas.

---

**Relatório `V2C-T3` — Estágio 2 de `PANTONIC-V2`. Corpus: `BM-00` + 21 externos, 16 dimensões,
352 células. Nenhuma afirmação sobre framework externo sem `BM-NN`; nenhuma afirmação sobre o
PantonicApp sem `arquivo:linha` via `BM-00`. Este estágio não altera nenhum artefato fora de
`docs/benchmark/` — a conversão dos vereditos em backlog é o `T4`.**
