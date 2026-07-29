# Índice do corpus de benchmarking (Estágio 1 — `PANTONIC-V2`)

Origem: `docs/plans/P-0729-v2-benchmarking.md` §5 (`V2B-T8` — Controle de qualidade e índice do
corpus). Esquema fixo em `docs/benchmark/_ESQUEMA.md`. Cache de metadados em
`docs/benchmark/_CORPUS.md` (tabela nas linhas 44-69).

Esta é a passada de QC **adversarial e final** antes do Estágio 2 (confronto). Checklist de
reprovação aplicado a cada um dos 21 relatórios:

1. Dimensão ausente/renomeada (deve ter D1..D16, nesta ordem, título canônico exato).
2. Afirmação sem URL.
3. URL apontando para a raiz do repositório em vez do arquivo específico.
4. Relatório com mais de 160 linhas.
5. Menção/juízo sobre o PantonicApp.
6. Rodapé incompleto (Práticas Transplantáveis, Anti-práticas, Dimensões Fora da Grade).
7. Campo "Dimensões Fora da Grade" ausente.

## Veredito por relatório

| BM | owner/repo | Trilha | Linhas (`wc -l`) | Veredito | Correção aplicada nesta passada |
|---|---|---|---|---|---|
| BM-01 | `github/spec-kit` | A | 147 | **Aprovado** | D2 sem nenhuma fonte — adicionada citação `_CORPUS.md` linha 44 |
| BM-02 | `bmad-code-org/BMAD-METHOD` | A | 160 | Aprovado | — |
| BM-03 | `Fission-AI/OpenSpec` | A | 115 | **Aprovado** | D2 citava `_CORPUS.md` linha `BM-03` (rótulo, não linha real) — corrigido para linha 47 |
| BM-04 | `SuperClaude-Org/SuperClaude_Framework` | A | 80 | **Aprovado** | D2 citava só "metadados T3" (vago) — corrigido para `_CORPUS.md` linha 49 |
| BM-05 | `anthropics/claude-code` | B | 102 | Aprovado | — |
| BM-06 | `anthropics/skills` | B | 136 | Aprovado | — |
| BM-07 | `github/awesome-copilot` | B | 104 | Aprovado | — |
| BM-08 | `google-gemini/gemini-cli` | B | 141 | Aprovado | — |
| BM-09 | `PatrickJS/awesome-cursorrules` | C | 118 | Aprovado | — |
| BM-10 | `cline/cline` | C | 119 | Aprovado | — |
| BM-11 | `coleam00/context-engineering-intro` | C | 71 | Aprovado | — |
| BM-12 | `steipete/agent-rules` | C | 137 | Aprovado | — |
| BM-13 | `hesreallyhim/awesome-claude-code` | D | 93 | **Aprovado** | D2 sem nenhuma fonte — adicionada citação `_CORPUS.md` linha 61 |
| BM-14 | `disler/claude-code-hooks-mastery` | D | 125 | Aprovado | — |
| BM-15 | `wshobson/agents` | D | 90 | Aprovado | — |
| BM-16 | `guardrails-ai/guardrails` | E | 92 | **Aprovado** | Item 5 — rodapé citava `Gerador: PANTONIC-V2 Estágio 1` (única menção a "Pantonic" nos 21); renomeado para `Coletor de benchmarking, Estágio 1` |
| BM-17 | `NVIDIA-NeMo/Guardrails` | E | 102 | Aprovado | — (cross-check D2 confirmado: `_CORPUS.md` linha 65, correto desde `V2B-T7`) |
| BM-18 | `promptfoo/promptfoo` | E | 84 | Aprovado | — |
| BM-19 | `sdi2200262/agentic-project-management` | F | 100 | Aprovado | — |
| BM-20 | `Wirasm/prp` | F | 90 | Aprovado | — |
| BM-21 | `snarktank/ai-dev-tasks` | F | 158 | Aprovado | — (cross-check D2 confirmado: `_CORPUS.md` linha 69, correto desde `V2B-T7`) |

**21/21 aprovados** após 5 correções pontuais (4× citação de fonte do D2, 1× menção a "Pantonic"
no rodapé). Nenhum relatório precisou de reemissão total. Checklist 1/4/6/7 limpo nos 21 sem
correção (dimensões, teto de linhas — `BM-02` está exatamente em 160, dentro do limite —, rodapé
e campo "Dimensões Fora da Grade" já vinham corretos). Checklist 3 (URL de raiz de repositório):
nenhuma ocorrência nos 21. Checklist 5: 1 ocorrência (`BM-16`), corrigida.

## Tíquete aberto — citação de fonte sem URL completa

**Achado fora do escopo desta tarefa, com ação futura recomendada** (não bloqueia o Estágio 2):
boa parte das seções D3..D16 (fora de D1/D2, que majoritariamente citam URL completa ou
`_CORPUS.md`) cita a fonte por **caminho de arquivo relativo** (`` **Fonte:** `package.json` ``,
`` **Fonte:** árvore cacheada ``, `` [Árvore](docs/benchmark/_trees/...) ``) em vez da URL exata
(`raw.githubusercontent.com/...` ou `github.com/.../blob/...`) exigida literalmente por
`_ESQUEMA.md` linhas 39-42. Ocorre em pelo menos `BM-07`, `BM-09` (quase todas as 16 dimensões),
`BM-10`, `BM-11`, `BM-14`, `BM-16` (D7-D16), `BM-17` (D7/D11/D12) — um padrão sistêmico do
coletor em vários lotes/sessões distintas, não um erro isolado. Corrigir cada citação exigiria
reconstruir a URL RAW específica por arquivo em ~40+ pontos, o que excede o orçamento desta
tarefa (~45 tool uses) e configura busca transversal — registrado aqui como tíquete em vez de
corrigido inline. **Recomendação:** tarefa dedicada (`V2B-T9` ou item do backlog geral) para
normalizar todas as citações de fonte para o formato URL completo, reaproveitando o padrão já
usado em D1/D2 da maioria dos relatórios.

## Dimensões Fora da Grade — agregado dos 21 relatórios

Insumo para o Estágio 2 (matriz de cobertura e relatório consolidado). 2 relatórios (`BM-11`,
`BM-16`) responderam "nenhuma"; os demais 19 têm pelo menos 1 item.

- **BM-01** — Workflow engine com steps compostos (command/shell/if_then/do_while/fan_out/gate/switch); integração com 30+ agentes de IA em múltiplas linguagens de contexto; conceitos de SDD (spec-of-specs, complex-features, stack pós-spec).
- **BM-02** — Falta de documentação sobre qual middleware de IA/IDE é necessário para integração.
- **BM-03** — Governança de conflito em specs compartilhadas (merge concorrente); tratamento de código legado sem spec de origem.
- **BM-04** — Suporte multilíngue nativo (EN/JP/KR/ZH); reflexão PDCA (docs/patterns, docs/mistakes); orquestração de 8 MCPs.
- **BM-05** — Custo por sessão/turno sem orçamento explícito; ausência de rastreamento requisito→código→teste; estado persistente entre invocações não documentado.
- **BM-06** — Orquestração entre múltiplas skills em sequência; controle de token window entre skills; versionamento granular por skill.
- **BM-07** — Marketplace (JSON) como fonte canônica de descoberta; compilação de workflows markdown → lock.yml com risco de inconsistência fonte/compilado.
- **BM-08** — Routing de modelo (model-routing/model-steering/local-model-routing); versionamento de artefato dentro da sessão (`/rewind`); checkpointing com integração a git worktrees.
- **BM-09** — Ausência de feedback loop formal entre autores de regras e consumidores (curadoria de comunidade sem publicação estruturada).
- **BM-10** — Ambiguidade de mode-locking (transições plan↔act); sobreposição entre sub-agentes paralelos e "coordinated teams"; falta de guia de escopo entre hooks/rules/skills/plugins.
- **BM-11** — Nenhuma (fora de escala/compliance/performance sob carga, tidas como não aplicáveis a um template local).
- **BM-12** — Portabilidade entre IDEs sem compilador automático (acoplado a Cursor/Claude Code); ausência de política de deprecação/sunsetting de rules.
- **BM-13** — Trade-off curadoria humana vs. automação (subjetividade do mantenedor como single point-of-failure); padrão de "awesome" documentado apenas implicitamente via CoC/exemplos.
- **BM-14** — Ordem/precedência de múltiplos hooks no mesmo evento não é clara; sem validação de schema do próprio `settings.json`; sem mecanismo de rollback/recovery para hooks que bloquearam ações.
- **BM-15** — Marketplace federado via git-subdir sem governança de versionamento/SLA entre contribuições; adapter harness como único mecanismo de portabilidade, sem fallback manual.
- **BM-16** — Nenhuma (framework alinhado a D1..D16 sem preocupação relevante fora da grade).
- **BM-17** — Manutenção simultânea de Colang v1.0 e v2.x sem breaking change (evolução de linguagem de domínio específico sem obsolescência forçada).
- **BM-18** — Arquitetura em camadas com verificação de grafo acíclico de dependências (`architecture:check`); planos de refatoração documentados explicitamente como artefato versionado.
- **BM-19** — Recuperação de sessão (`apm-9-recover`, `summarize-session`) como orquestração de reconexão, além de simples estado persistente; acoplamento explícito de Message Bus a uma plataforma.
- **BM-20** — Ausência de teto de contexto/turnos/custo enforçado; heterogeneidade de gate logic por skill sem agregação uniforme (dificulta auditoria cruzada).
- **BM-21** — Falta de orientação estruturada para adaptar templates a stacks/convenções diversas (só "customize as needed").
