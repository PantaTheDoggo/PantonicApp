# BM-09 — PatrickJS/awesome-cursorrules

**Corpus:** Trilha C (IA generativa e prompt/context engineering)

## D1 — Identidade e escopo

Coleção curada de >200 regras (arquivos `.mdc`) para personalizar o editor Cursor AI. Resolve inconsistência de assistência IA em projetos heterogêneos e reduz retrabalho em padrões repetidos. Público: desenvolvedores e equipes que usam Cursor AI em stacks diversos (frontend, backend, mobile, DevOps, games).

**Fonte:** `https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/HEAD/README.md`

## D2 — Vitalidade

Stars: 40455 | Último push: 2026-05-30T18:01:29Z | Licença: CC0-1.0 | Nº de contribuidores: **NÃO ENCONTRADO**

**Fonte:** `docs/benchmark/_CORPUS.md` (linha 55)

## D3 — Ciclo de vida do trabalho

**Fases:** Preparação (fork/clone) → Edição (arquivo `.mdc` com frontmatter) → Proposta (PR descritiva) → Revisão (maintainer valida conteúdo) → Aceitação/Rejeição. **Artefato por fase:** arquivo `.mdc` com campos `description`, `globs`, `alwaysApply`. **Gates:** CI checks (README, rule hygiene, awesome-lint, age-of-account >30 dias em `pull_request_target`).

**Fonte:** `https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/HEAD/contributing.md`, `.github/workflows/main.yml`

## D4 — Papéis e modelo por fase

Proprietário único (@PatrickJS) autorizado para workflows e scripts. Não há escolha explícita de modelo por fase — é repositório de curadoria, não ferramenta de orquestração. Comunidade rege-se por Contributor Covenant (respeito, inclusão, banimento de assédio).

**Fonte:** https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/HEAD/.github/CODEOWNERS, https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/HEAD/code-of-conduct.md

## D5 — Unidade de trabalho e rastreabilidade

Uma tarefa = arquivo `.mdc` novo ou atualização de regra existente. PR template obriga: `Summary`, `Contribution Type` (new rule/update/docs), `Value To Cursor Users`, `Added Or Changed Files`, checklist de qualidade (originalidade, nomes em kebab-case, ausência de rastreamento/tokens/promo). **Rastreabilidade:** PR traceia regra para repositório, mas não há rastro explícito requisito → código → teste.

**Fonte:** https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/HEAD/.github/pull_request_template.md

## D6 — Contexto e custo

**NÃO ENCONTRADO**

## D7 — Memória e estado persistente

Regras (arquivos `.mdc`) armazenadas em `/rules/` do repositório GitHub. Persistem via git entre sessões. Cada regra leva `description`, `globs` (padrões de arquivo), `alwaysApply` (booleano) em frontmatter YAML.

**Fonte:** docs/benchmark/_trees/patrickjs-awesome-cursorrules.txt (277 arquivos em /rules/), https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/HEAD/rules/react.mdc (exemplo)

## D8 — Qualidade e testes

Testes via `pnpm test` (Jest/Vitest). CI executa: `awesome-lint` v2.3.0, `check-awesome-list.mjs` (conformidade README), `check-rule-hygiene.mjs` (frontmatter), `check-repo-hygiene.mjs` (links, segurança). Não há TDD mencionado. Regressão: verificações automáticas em cada PR.

**Fonte:** https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/HEAD/package.json, https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/HEAD/.github/workflows/main.yml

## D9 — Guardrails e enforcement

**100% código executável.** Scripts Node.js validam automaticamente: (1) README (proíbe seções genéricas, valida links locais); (2) Conformidade de Regras (obriga `description`, `globs`, `alwaysApply`; detecta vazias/erros de IA); (3) Segurança de Prompts (12+ padrões perigosos: exfiltração de credenciais, leitura de arquivos sensíveis, bootstraps remotos, TLS bypass, hooks de persistência, Unicode injection); (4) Política de Templates (obriga `blank_issues_enabled: false`).

**Fonte:** https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/HEAD/scripts/check-repo-hygiene.mjs, https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/HEAD/scripts/check-awesome-list.mjs, https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/HEAD/.github/workflows/main.yml

## D10 — Distribuição e versionamento do próprio framework

Marcado `"private": true` em `package.json` — não publicado em npm. Distribuição: clone direto de GitHub. **Versão:** não declarada no `package.json`. Sem CHANGELOG. Sem releases formais.

**Fonte:** https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/HEAD/package.json, Glob para CHANGELOG (não encontrado)

## D11 — Extensibilidade

Modelo aberto de contribuição. Qualquer pessoa pode submeter nova regra via PR seguindo template `.mdc`. Não há sistema de plugins, hooks ou extensões formais — é lista, não engine.

**Fonte:** https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/HEAD/contributing.md

## D12 — Observabilidade e métricas

**NÃO ENCONTRADO**

## D13 — Segurança e permissões

**Sandbox:** verificação de idade da conta (GitHub >30 dias) em `pull_request_target`. **Allowlist:** @PatrickJS, dependabot, Copilot bypassam age check. **Detecção de padrões sensíveis:** 12+ regras em `check-repo-security.mjs` (credenciais, SSH keys, AWS tokens, shell bootstraps, TLS bypass, cron/shell/git hooks, Unicode controle). **Separação:** `pull_request_target` (código confiável valida) vs `pull_request` (PR code em sandbox).

**Fonte:** https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/HEAD/.github/workflows/main.yml, https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/HEAD/scripts/check-repo-hygiene.mjs

## D14 — Onboarding humano e documentação

README detalhado (escopo, stacks cobertos). `contributing.md` com diretrizes passo-a-passo. `code-of-conduct.md` (Contributor Covenant). PR template guia novo contribuidor (checklist, exemplos). Bom onboarding: ~10 min para decidir, ~5 min para submeter primeira regra.

**Fonte:** https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/HEAD/README.md, https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/HEAD/contributing.md, https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/HEAD/code-of-conduct.md, https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/HEAD/.github/pull_request_template.md

## D15 — Multi-projeto, multi-repo e equipe

Coleção compartilhada para uso em múltiplos projetos/pessoas. Governa-se por Contributor Covenant (comunidade comunitária, não corporativa). Sem governança formal entre múltiplos repositórios — é um único hub centralizado.

**Fonte:** https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/HEAD/README.md, https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/HEAD/code-of-conduct.md

## D16 — Interação com o humano

PRs revisadas manualmente por maintainer (@PatrickJS). Humano decide aceitação (julga originalidade, utilidade, conformidade). Issue templates guiam relatores. Nenhuma aceitação automática de regras.

**Fonte:** https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/HEAD/.github/pull_request_template.md, docs/benchmark/_trees/patrickjs-awesome-cursorrules.txt (.github/ISSUE_TEMPLATE/, .github/workflows/)

---

## Práticas transplantáveis

1. **Validação de segurança em prompts (12+ padrões detectados):** Custo: ~1 sprint. Aplicável a qualquer framework que ingira texto de usuário (regras, skills, instruções).

2. **Frontmatter YAML obrigatório + CI checks:** Custo: ~2 dias. Reduz "lixo" no repositório; transplantável para galeria de qualquer linguagem.

3. **Verificação de idade da conta + allowlist em CI:** Custo: ~1 dia. Sandbox eficaz contra spam/vandalism; aplica-se a repos comunitários.

## Anti-práticas

1. **Versão não declarada, sem CHANGELOG, distribuição apenas via clone:** Deixa consumidores sem forma de rastrear atualizações ou decidir se upgrade trás breaking changes. Propriedade `"private": true` sem npm publishing reduz adoção.

2. **Proprietário único (@PatrickJS) para toda automação:** Single point of failure (bus factor = 1). Revisão manual em 40k-star repo não escala.

3. **Sem rastreamento requisito → código → teste:** PRs traciam regra, mas não há série histórica, métricas de adoção ou piso de qualidade (ex.: test coverage, integração com algum CI externo).

## Dimensões fora da grade

- **Curvetura da comunidade:** Awesome list sem publicação formal perde feedback loop entre autores de regras e consumidores. Não há issue/discussion sobre "qual regra não funcionou" ou "regra X precisa update pra React 19".

