# Corpus de benchmarking — 21 confirmados (V2B-T3)

**Data da coleta:** 2026-07-29 (janela de cota GitHub API não-autenticada, reset 05:31 local).
**Requisições gastas:** 50 (25 metadados + 0 reconfirmações + 20 árvores de arquivos = 45 no lote
principal; + 4 metadados de candidatos F novos + 1 árvore na ampliação para 21). Teto: 55.
**Método:** dois scripts PowerShell em lote (não requisição-a-requisição), `GET /repos/{o}/{r}`
e `GET /repos/{o}/{r}/git/trees/HEAD?recursive=1`, sem autenticação. Nenhum 404/403/429
recebido — nenhuma reconfirmação via WebSearch foi necessária.

**Numeração BM-01..BM-21** (usada por `V2B-T4..T7` para mapear relatórios): ver coluna `#BM`
abaixo, atribuída apenas às linhas `confirmado`, na ordem original da tabela de 25 candidatos —
`BM-21` é o acréscimo da ampliação (ver abaixo) e entra num lote extra do `V2B-T7`.

**Desvio resolvido — trilha F abaixo do piso de 3 → corpus ampliado para 21:** a lista de 25
candidatos do plano (`docs/plans/P-0729-v2-benchmarking.md` §2) só continha **2** candidatos para
a trilha F (gestão de projeto com IA) desde a origem, tornando o piso de 3 da `DV-3`
estruturalmente inatingível. **Decisão do dono, 2026-07-29:** ampliar o corpus para **21
repositórios** em vez de cortar um confirmado de outra trilha — as trilhas A–E ficam intactas e F
sobe a 3. A `DV-3` fica emendada nesse ponto (20 → 21; o piso de ≥3 por trilha permanece e agora é
cumprido em todas). Resolvido antes do `V2B-T4` de propósito: a numeração `BM-*` congela quando os
relatórios começam a ser emitidos.

**Escolha do 3º candidato de trilha F** (4 candidatos sondados na API em 2026-07-29):
`snarktank/ai-dev-tasks` (7786 stars, `pushed_at` 2025-11-05, Apache-2.0). Descartados:
`pabg92/Claude-Code-agentic-project-management` (25 stars — adaptação derivada do `BM-19`, geraria
relatório redundante), `danielrosehill/Agent-Handover-Demo` (6 stars, ativo, mas é demo mínima —
superfície insuficiente para 16 dimensões), `andyrewlee/awesome-agent-orchestrators` (1151 stars,
ativo, mas é lista de ecossistema — perfil de trilha D, não gestão de projeto).
**Tensão declarada:** o escolhido está parado desde nov/2025 (~9 meses), a mesma condição que
cortou `humanlayer/12-factor-agents` da trilha D. Aceito aqui porque a alternativa era deixar o
piso descumprido, e porque o repositório *é* a prática de trilha F com maior adoção pública
(PRD → lista de tarefas → uma sub-tarefa por vez com aprovação humana). A estagnação não é
escondida: aparece em `D2 — Vitalidade` do `BM-21` e deve ser pesada no confronto do Estágio 2.

**Renomeações/transferências de owner detectadas pela API** (a resposta HTTP 200 veio via
redirecionamento, não é correção de 404): `openai/agents.md` → `agentsmd/agents.md` (candidato
cortado, motivo abaixo, independente da renomeação); `davidkimai/Context-Engineering` →
`jasontang-ai/Context-Engineering` (cortado); `NVIDIA/NeMo-Guardrails` → `NVIDIA-NeMo/Guardrails`
(confirmado, `#BM-17`); `Wirasm/PRPs-agentic-eng` → `Wirasm/prp` (confirmado, `#BM-20`). As
árvores em `docs/benchmark/_trees/` usam o `full_name` atual (pós-redirecionamento).

| # | #BM | Trilha | owner/repo (candidato original) | full_name resolvido | Stars | pushed_at (UTC) | Licença | Status | Motivo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | BM-01 | A | `github/spec-kit` | `github/spec-kit` | 124381 | 2026-07-28T22:29:28Z | MIT | confirmado | maior atividade recente do grupo A |
| 2 | BM-02 | A | `bmad-code-org/BMAD-METHOD` | `bmad-code-org/BMAD-METHOD` | 51221 | 2026-07-29T06:57:18Z | NOASSERTION | confirmado | atividade mais recente da trilha A |
| 3 | — | A | `buildermethods/agent-os` | `buildermethods/agent-os` | 5136 | 2026-05-05T05:07:51Z | MIT | cortado | trilha A com 6 candidatos, corte para respeitar 25→20; `pushed_at` mais antigo do grupo A (empatado por antiguidade com #5) — critério do plano prioriza atividade recente sobre stars |
| 4 | BM-03 | A | `Fission-AI/OpenSpec` | `Fission-AI/OpenSpec` | 62995 | 2026-07-29T01:31:26Z | MIT | confirmado | atividade recente alta |
| 5 | — | A | `eyaltoledano/claude-task-master` | `eyaltoledano/claude-task-master` | 27919 | 2026-04-28T13:27:12Z | NOASSERTION | cortado | `pushed_at` mais antigo do grupo A — sem atividade desde abril/2026, prática mais estagnada da trilha |
| 6 | BM-04 | A | `SuperClaude-Org/SuperClaude_Framework` | `SuperClaude-Org/SuperClaude_Framework` | 23613 | 2026-07-22T06:02:09Z | MIT | confirmado | trilha A fecha com 4 (≥3 respeitado) |
| 7 | BM-05 | B | `anthropics/claude-code` | `anthropics/claude-code` | 139455 | 2026-07-25T01:35:55Z | (sem license.spdx_id) | confirmado | doutrina de plataforma, alta atividade |
| 8 | BM-06 | B | `anthropics/skills` | `anthropics/skills` | 164915 | 2026-07-24T20:12:36Z | (sem license.spdx_id) | confirmado | doutrina de plataforma, alta atividade |
| 9 | — | B | `openai/agents.md` | `agentsmd/agents.md` (renomeado/transferido) | 23286 | 2026-03-12T14:26:14Z | MIT | cortado | `pushed_at` mais antigo do grupo B (12/03 vs 24-29/07 dos demais) — trilha B com 5 candidatos, corte para respeitar 25→20 |
| 10 | BM-07 | B | `github/awesome-copilot` | `github/awesome-copilot` | 37168 | 2026-07-29T05:28:56Z | MIT | confirmado | atividade recente alta |
| 11 | BM-08 | B | `google-gemini/gemini-cli` | `google-gemini/gemini-cli` | 106231 | 2026-07-29T01:29:18Z | Apache-2.0 | confirmado | trilha B fecha com 4 (≥3 respeitado) |
| 12 | BM-09 | C | `PatrickJS/awesome-cursorrules` | `PatrickJS/awesome-cursorrules` | 40455 | 2026-05-30T18:01:29Z | CC0-1.0 | confirmado | volume/padrões de regra por stack |
| 13 | BM-10 | C | `cline/cline` | `cline/cline` | 65159 | 2026-07-29T07:23:35Z | Apache-2.0 | confirmado | atividade recente alta |
| 14 | BM-11 | C | `coleam00/context-engineering-intro` | `coleam00/context-engineering-intro` | 13750 | 2026-03-16T12:13:59Z | MIT | confirmado | PRP autocontido — mantido mesmo com atividade mais antiga que #16, dimensão sem substituto direto no grupo restante |
| 15 | — | C | `davidkimai/Context-Engineering` | `jasontang-ai/Context-Engineering` (renomeado/transferido) | 9179 | 2026-02-27T05:04:18Z | MIT | cortado | `pushed_at` mais antigo do grupo C — trilha C com 5 candidatos, corte para respeitar 25→20 |
| 16 | BM-12 | C | `steipete/agent-rules` | `steipete/agent-rules` | 5692 | 2026-05-03T17:06:19Z | MIT | confirmado | trilha C fecha com 4 (≥3 respeitado) |
| 17 | — | D | `humanlayer/12-factor-agents` | `humanlayer/12-factor-agents` | 24929 | 2025-09-21T14:37:40Z | NOASSERTION | cortado | `pushed_at` claramente o mais antigo de todo o corpus (set/2025, ~10 meses sem push) — framework parado, critério do plano é explícito sobre esse caso |
| 18 | BM-13 | D | `hesreallyhim/awesome-claude-code` | `hesreallyhim/awesome-claude-code` | 51192 | 2026-07-29T06:57:05Z | NOASSERTION | confirmado | atividade recente alta |
| 19 | BM-14 | D | `disler/claude-code-hooks-mastery` | `disler/claude-code-hooks-mastery` | 3855 | 2026-03-04T18:16:25Z | (sem license.spdx_id) | confirmado | trilha D fecha com 3 (piso mínimo) |
| 20 | BM-15 | D | `wshobson/agents` | `wshobson/agents` | 38344 | 2026-07-22T15:32:23Z | MIT | confirmado | atividade recente alta |
| 21 | BM-16 | E | `guardrails-ai/guardrails` | `guardrails-ai/guardrails` | 7221 | 2026-07-29T01:16:51Z | Apache-2.0 | confirmado | trilha E já no piso mínimo (3 candidatos no total) — nenhum corte possível |
| 22 | BM-17 | E | `NVIDIA/NeMo-Guardrails` | `NVIDIA-NeMo/Guardrails` (renomeado/transferido) | 6824 | 2026-07-29T07:29:11Z | NOASSERTION | confirmado | trilha E já no piso mínimo |
| 23 | BM-18 | E | `promptfoo/promptfoo` | `promptfoo/promptfoo` | 23715 | 2026-07-29T01:30:49Z | MIT | confirmado | trilha E já no piso mínimo |
| 24 | BM-19 | F | `sdi2200262/agentic-project-management` | `sdi2200262/agentic-project-management` | 2368 | 2026-06-08T13:30:29Z | NOASSERTION | confirmado | trilha F só tinha 2 candidatos na origem — ambos mantidos (ver desvio registrado acima) |
| 25 | BM-20 | F | `Wirasm/PRPs-agentic-eng` | `Wirasm/prp` (renomeado/transferido) | 2226 | 2026-07-27T13:48:33Z | MIT | confirmado | trilha F só tinha 2 candidatos na origem — ambos mantidos (ver desvio registrado acima) |
| 26 | BM-21 | F | *(fora da lista de origem — ampliação)* | `snarktank/ai-dev-tasks` | 7786 | 2025-11-05T19:42:09Z | Apache-2.0 | confirmado | 3º candidato de trilha F descoberto na ampliação para 21 (decisão do dono); repositório parado desde nov/2025 — tensão declarada acima |

**Resumo por trilha (confirmados):** A=4, B=4, C=4, D=3, E=3, F=3 (total 21). Piso de ≥3 por trilha
respeitado em todas, após a ampliação de 20 para 21.

**Árvores cacheadas:** `docs/benchmark/_trees/<slug>.txt`, um arquivo por confirmado, `slug` =
`full_name` resolvido em minúsculas com `/` → `-`. Nenhuma árvore veio truncada
(`truncated: true`) nesta coleta.
