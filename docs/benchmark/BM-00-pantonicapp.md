# BM-00: PantonicApp — Auto-retrato no esquema do corpus

**Sujeito:** PantonicApp (hub de governança Pantonic*), `D:\workspaces\PantonicApp`.
**Metadados:** repositório git local, sem hospedagem pública (ver D2) | versão do framework:
`1.2.0` (`VERSION:1`, `.claude/KIT_VERSION:1`).

---

## D1 — Identidade e escopo
Hub de doutrina + kit agêntico da família Pantonic* (desktop, Python+PySide6, MVVM). Não é ele
mesmo uma aplicação: sem `infracore/`, `contracts/` nem `tests/` (busca `tests/**` vazia).
**Fonte:** `GOVERNANCA.md:1-6`, `ARQUITETURA_PANTONICA.md:1-11`.

---

## D2 — Vitalidade
NÃO ENCONTRADO (stars/licença/contribuidores) — sem publicação pública, sem `LICENSE` na raiz.
Proxy do framework: `CHANGELOG.md` registra 3 versões em 2026-07-29.
**Fonte:** `VERSION:1`, `CHANGELOG.md:11,17`.

---

## D3 — Ciclo de vida do trabalho
PRD → Architecture → Spec → Sprint Plan → diário de obras → execução → `guardrails-check` →
`handover`. Gate de conformance é doutrina para consumidores; o hub não instancia essa suíte.
**Fonte:** `GOVERNANCA.md:158-178,196-197`.

---

## D4 — Papéis e modelo por fase
9 agentes em `.claude/agents/*.md`, `model:` explícito por papel (opus/sonnet/haiku por fase).
**Drift:** `.claude/README.md:8-19` lista só 8 — falta `pantonic-auditor-container` na tabela.
**Fonte:** `GOVERNANCA.md:43-47`, `.claude/agents/*.md:2-5`, `.claude/README.md:8-19`.

---

## D5 — Unidade de trabalho e rastreabilidade
Tarefa atômica do diário (objetivo, arquivos-alvo, testes, critério de pronto). Cada entrada fecha
com `Resultado`+`Veredito`+`Consumo`; ex.: `V2B-T2` expõe autoestimativa (13) vs medido (20).
**Fonte:** `GOVERNANCA.md:92-93`, `docs/DIARIO_DE_OBRAS.md:59-61,113-146`.

---

## D6 — Contexto e custo
Orçamento vinculante de ~≤40 tool uses/tarefa, batching, sem re-leitura de verificação. Doutrina
dividida entre o repo e o CLAUDE.md global do usuário (cruza com D15).
**Fonte:** `GOVERNANCA.md:67-69`, `C:\Users\panta\.claude\CLAUDE.md:30,107`.

---

## D7 — Memória e estado persistente
Três camadas: diário de obras (repo), `MEMORY.md` por projeto (fora do repo), CLAUDE.md global do
usuário (regras de todos os projetos, fora de qualquer repo).
**Fonte:** `GOVERNANCA.md:95-107`, `C:\Users\panta\.claude\CLAUDE.md:1`.

---

## D8 — Qualidade e testes
TDD é golden rule + TF/TR obrigatórios — doutrina **para consumidores**. O hub não tem suíte de
testes própria (`tests/**` vazio): nada aqui pratica o TDD que prescreve.
**Fonte:** `ARQUITETURA_PANTONICA.md:18`, `GOVERNANCA.md:130-138`.

---

## D9 — Guardrails e enforcement
8 guardrails textuais (`GOVERNANCA.md` §7); enforcement "código executável" é 0% dentro do hub
(sem camadas a testar) — aqui o enforcement real é `tools:` restrito por agente.
**PARCIAL — decidido, não escrito:** G-DEADCODE, G-PLANFIDELITY, G-PREMISE, G-PLANREADY,
G-EXECREADY (decididas 2026-07-22, `P-0722`, mescladas ao Estágio 3A).
**Fonte:** `GOVERNANCA.md:183-201`, `docs/DIARIO_DE_OBRAS.md:208-212`.

---

## D10 — Distribuição e versionamento do próprio framework
`VERSION`/`.claude/KIT_VERSION` em paridade obrigatória, Semver com significado declarado.
Distribuição por `git subtree` (branch `kit`); `sync-kit.ps1` aplica versão respeitando
`kit-exclude.txt`; checagem via skill `checar-versao-kit`, nunca update automático.
**Fonte:** `GOVERNANCA.md:233-277`, `.claude/sync-kit.ps1:1-14`.

---

## D11 — Extensibilidade
8 skills (`.claude/skills/*/SKILL.md`) + 9 agentes (D4). Extensão do próprio kit é por
`git subtree` + `kit-exclude.txt` local — sem fork.
**Fonte:** `.claude/skills/*/SKILL.md:2-3`, `.claude/README.md:35-44`.

---

## D12 — Observabilidade e métricas
Série histórica real: todo fechamento registra `Consumo: N tool uses, ~Xk tokens, modelo, duração`
medido no `<usage>`, nunca autorrelato — 5 casos medidos de estouro de teto no diário.
**Fonte:** `C:\Users\panta\.claude\CLAUDE.md:107`, `docs/DIARIO_DE_OBRAS.md:141-146,190-195`.

---

## D13 — Segurança e permissões
Sandbox por agente via `tools:` no frontmatter (ex.: auditores só `Read,Glob,Grep,Write`, sem
`Edit`/`Bash`, enforçado pelo harness). Segredos/allowlist de comandos destrutivos: NÃO ENCONTRADO.
**Fonte:** `.claude/agents/pantonic-auditor-arch.md:5`, `.claude/agents/pantonic-scout.md:5`.

---

## D14 — Onboarding humano e documentação
`GOVERNANCA.md` (277 l.) + `ARQUITETURA_PANTONICA.md` (276 l.) — abaixo do limiar de `DOC_MAP.md`
(500 l., nenhum encontrado). `.claude/README.md` (50 l.) onboarda o kit. ~600 linhas ao todo.
**Fonte:** `GOVERNANCA.md:1-8,214`, `ARQUITETURA_PANTONICA.md:1-11`.

---

## D15 — Multi-projeto, multi-repo e equipe
Doutrina compartilhada por `git subtree`, provada em `PantonicVideo`. CLAUDE.md global do usuário
vale para todos os projetos, não só Pantonic* — parte da doutrina de fato mora fora de todo repo.
**Fonte:** `GOVERNANCA.md:220-231`, `C:\Users\panta\.claude\CLAUDE.md:1,3,17,30,51,69,84,107`.

---

## D16 — Interação com o humano
Nunca automáticos: atualização do kit, diretiva de priorização, publicação de plano do Estágio 3B,
troca de modelo de execução para um mais caro — todos exigem escrita/OK explícito do dono.
**Fonte:** `GOVERNANCA.md:238-242,108-112,57-62`, `docs/DIARIO_DE_OBRAS.md:49-52`.

---

## Práticas Transplantáveis

N/A — sujeito da comparação.

---

## Anti-práticas (autocrítica do próprio framework)

1. **README do kit desatualizado.** `.claude/README.md:8-19` lista 8 agentes;
   `pantonic-auditor-container` existe em disco e não está na tabela. Onboarding (D14) já diverge
   da fonte de verdade.

2. **Guardrails de conformance são doutrina que o hub não pratica.** `GOVERNANCA.md:183-201` exige
   AST executável para consumidores; o hub que escreve a regra não tem código de camadas para
   segui-la (D8/D9).

3. **Estouro de teto vira prosa repetida, não guardrail executável.**
   `docs/DIARIO_DE_OBRAS.md:141-146,190-195` é o quinto caso da mesma série, mesma causa (divisão
   prévia insuficiente), mesma lição reescrita em vez de virar checagem automática.

---

## Dimensões Fora da Grade

- **Mecanismo de distribuição `git subtree`+`sync-kit.ps1`+`kit-exclude.txt`:** é D10 e D11 ao
  mesmo tempo — propagação de doutrina entre repositórios, sem dimensão própria na grade.
- **Guardrail de custo do processo agêntico em si:** "modelo por fase vinculante"
  (`GOVERNANCA.md:57-62`) governa o custo de rodar os agentes, distinto de D6 (tarefa) e D12
  (produto).

---

**Relatório finalizado: 156 linhas | auto-retrato, sem WebFetch/API externa.**
