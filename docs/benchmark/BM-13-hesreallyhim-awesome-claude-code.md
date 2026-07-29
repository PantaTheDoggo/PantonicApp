# BM-13: hesreallyhim/awesome-claude-code

Trilha D | 51.192 stars | 2026-07-29T06:57:05Z | NOASSERTION

## D1 — Identidade e escopo
Curated awesome list de recursos/extensions para Claude Code. Problema: maximizar capacidades do agente através de skills, guardrails, monitors, tooling. Público: iniciantes e veteranos, ênfase em qualidade, segurança, originalidade.
https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/HEAD/README.md

## D2 — Vitalidade
Stars: 51.192 | Push: 2026-07-29T06:57:05Z | Contribuidores: NÃO ENCONTRADO | Licença: NOASSERTION
**Fonte:** `docs/benchmark/_CORPUS.md` linha 61

## D3 — Ciclo de vida do trabalho
Fases: (1) Descoberta → (2) Issue + formulário → (3) Validação automática (labels) → (4) Revisão manual → (5) Aceitação discricionária. Artefatos: issue template YAML, labels (validation-passed/failed), comentário automático. Gates: CoC, descrição 1 linha, licença válida, features únicas Claude Code.
https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/HEAD/CONTRIBUTING.md

## D4 — Papéis e modelo por fase
Papéis: mantenedor (decisão final), comunidade (recomendações). Sem modelo explícito por fase — todas usam issue + review humana.
https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/HEAD/CONTRIBUTING.md

## D5 — Unidade de trabalho e rastreabilidade
Tarefa: issue com formulário (link, nome, autor, descrição, categoria, licença). Rastreabilidade: issue → label → comentário → PR → CSV. Sem rastro requisito-código-teste.
https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/HEAD/.github/workflows/validate-new-issue.yml

## D6 — Contexto e custo
NÃO ENCONTRADO. Nenhum limite explícito.

## D7 — Memória e estado persistente
Single source-of-truth: `THE_RESOURCES_TABLE_NEW.csv` (12 colunas). README gerado de CSV + config + template. Estado de validação em issues do GitHub.
https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/HEAD/Makefile; https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/HEAD/config.yaml

## D8 — Qualidade e testes
Suite pytest: parsing, validação, CSV, segurança (XSS/injeção), operações. Sem TDD. Piso: não quantificado; cobertura funcional (happy path + erros), sem métrica mínima.
https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/HEAD/tests/test_resources.py

## D9 — Guardrails e enforcement
100% código executável: script Python `parse_issue_form --validate`. Workflow GitHub Actions (validate-new-issue.yml) on issue.opened/edited + label "resource-submission". Validação → labels automáticos (validation-passed/failed). Re-executa a cada edição.
https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/HEAD/.github/workflows/validate-new-issue.yml; https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/HEAD/Makefile

## D10 — Distribuição e versionamento do próprio framework
Instalação: clone ou consulta em browser (não pacote). Atualizações: sem versioning semântico. Versionamento: NÃO ENCONTRADO (sem releases, tags, changelog).
https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/HEAD/Makefile

## D11 — Extensibilidade
Categorias/subcategorias dinâmicas em config.yaml; novas subcategorias renderizadas automaticamente. Extensão sem fork: contributor submete → mantenedor aprova → entra no CSV (sem código customizado).
https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/HEAD/config.yaml

## D12 — Observabilidade e métricas
Ticker SVG + Recently-Added SVG (repo-ticker.csv, generate_recently_added_svg.py). Série histórica: ticker-previous.csv vs. ticker.csv. Sem observabilidade de consumo humano (tempo review, taxa rejeição).
https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/HEAD/Makefile

## D13 — Segurança e permissões
Sem sandbox; repositório é Markdown. Sem allowlist. `make ticker` requer GITHUB_TOKEN. Deletar recurso requer acesso direto CSV + push. Divulgação: private security advisory; superfície limitada às credenciais do mantenedor.
https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/HEAD/SECURITY.md

## D14 — Onboarding humano e documentação
README ~2k palavras; CODE_OF_CONDUCT; CONTRIBUTING.md (informal). Makefile documenta comandos. Sem "getting started" estruturado; nenhum passo a passo para novos mantenedores.
https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/HEAD/README.md; https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/HEAD/CONTRIBUTING.md

## D15 — Multi-projeto, multi-repo e equipe
Projeto singular. Coleta metadados de outros repos (ticker). Sem vínculo de doutrina a outros repositórios.

## D16 — Interação com o humano
Aprovação: mantenedor decide manualmente. Consultoria: comentários automáticos orientam correções (validation-failed). Automático: parsing, validação, README, SVG. Nunca automático: aprovação (curadoria com humano).
https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/HEAD/.github/workflows/validate-new-issue.yml

---

## Práticas transplantáveis

1. **Validação automática via GitHub Actions + labels dinâmicas.** Custo: baixo (~40h). Reutilizável em qualquer curation workflow.

2. **CSV como single source-of-truth com gerador idempotente.** Custo: médio (~80h). Desacopla dados de apresentação; multi-formato.

3. **Categorias/subcategorias dinâmicas sem refatoração.** Custo: baixo (~20h). Config YAML permite expansão; renderização automática.

---

## Anti-práticas

1. **Ciclo de vida informal sem SLA/timeline.** Risco: submissores esperam indefinidamente; inviabiliza projetos com deadline.

2. **Licença "NOASSERTION" em repositório público.** Risco: ambiguidade legal; consumidores não sabem direitos.

3. **Sem versionamento semântico apesar de ser doutrina/referência.** Risco: consumidores não rastreiam versão de "best practices"; quebra confiança em updates.

---

## Dimensões fora da grade

**Curadoria humana vs. automação trade-off:** Subjetividade do mantenedor é feature, não bug. Critérios "awesome" implícitos (CoC e exemplos, não documentado). Reduz complexidade; cria single point-of-failure.

**Documentação implícita de padrões:** "O que torna recurso awesome" transmitido via CoC/exemplos. Novo mantenedor enfrentaria curva de aprendizado alta.
