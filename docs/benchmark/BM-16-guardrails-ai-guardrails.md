# BM-16: guardrails-ai/guardrails

## D1 — Identidade e escopo
Framework Python para validação LLM input/output e geração de dados estruturados. Resolve confiabilidade: detecção/mitigação de riscos, ecossistema modular via Hub. Para desenvolvedores de aplicações LLM que precisam conformidade, qualidade e segurança.
**Fonte:** README (https://raw.githubusercontent.com/guardrails-ai/guardrails/HEAD/README.md)

## D2 — Vitalidade
Stars: 7221 | Último push: 2026-07-29T01:16:51Z | Nº contribuidores: NÃO ENCONTRADO | Licença: Apache-2.0
**Fonte:** `docs/benchmark/_CORPUS.md` linha 64

## D3 — Ciclo de vida do trabalho
**Fases:** (1) Identificação (alertas Dependabot) → (2) Resolução (atualizar `pyproject.toml`/`poetry.lock`, fixes upstream-first) → (3) Validação (3 gates executáveis).
**Artefatos:** alertas, `pyproject.toml` (ranges), `poetry.lock` (pinned), passagem de gates lint/type/test.
**Fonte:** CLAUDE.md (https://raw.githubusercontent.com/guardrails-ai/guardrails/HEAD/CLAUDE.md)

## D4 — Papéis e modelo por fase
Dependabot (scanning) → Contributors (implementação) → Maintainers (review/release). Modelo único: PRs diretas para bugs, Discord para features. Sem escolha de modelo alternativo por fase.
**Fonte:** CLAUDE.md, CONTRIBUTING.md (https://raw.githubusercontent.com/guardrails-ai/guardrails/HEAD/CONTRIBUTING.md)

## D5 — Unidade de trabalho e rastreabilidade
Unidade: validator customizado ou atualização de dependência. Padrão: `@register_validator()` + classe `Validator` + `_validate()` → `PassResult`/`FailResult`. Interface contratual clara; sem rastro explícito requisito→teste automatizado.
**Fonte:** docs/how_to_guides/custom_validator.ipynb (https://raw.githubusercontent.com/guardrails-ai/guardrails/HEAD/docs/how_to_guides/custom_validator.ipynb)

## D6 — Contexto e custo
**NÃO ENCONTRADO** — nenhuma política de orçamento, limite de contexto, turnos ou dinheiro. Dependências opcionais (e.g., `anthropic`) indicam flexibilidade sem políticas explícitas de custo.
**Fonte:** pyproject.toml (https://raw.githubusercontent.com/guardrails-ai/guardrails/HEAD/pyproject.toml)

## D7 — Memória e estado persistente
`guard.history` (per-sessão), `guardrails/version.py`, `poetry.lock` (reproduzibilidade), logging estruturado, VectorDB opcional, SQLAlchemy opcional.
**Fonte:** guardrails_server.ipynb, pyproject.toml

## D8 — Qualidade e testes
**Três gates obrigatórios:** `make lint` (Ruff), `make type` (Pyright), `make test` (pytest). Todos passam pré-commit. Sem piso de regressão ou TDD puro explícitos.
**Fonte:** CLAUDE.md

## D9 — Guardrails e enforcement
**100% executável.** Regras: `CLAUDE.md` (two-file strategy), `Makefile` (gates), `.github/workflows/` (CI), `pyproject.toml` (paranoia licenças). Pré-commit hooks, CI automático.
**Fonte:** CLAUDE.md, CONTRIBUTING.md, pyproject.toml

## D10 — Distribuição e versionamento do próprio framework
**Versão 0.11.0 | Distribuição: PyPI | Versionamento: Semantic | Console: `guardrails` | Python ≥3.10 <3.14 | Gestor: Poetry**
Instalação: `pip install guardrails-ai` ou `pip install git+...@v0.10.0` (pós-0.10.1). Atualização: `pip --upgrade`. Versão: `guardrails/version.py` ou `pip show`.
**Fonte:** pyproject.toml, SECURITY_ADVISORY.md

## D11 — Extensibilidade
(1) Validators: herança de `Validator`, `@register_validator()`, `_validate()` → `PassResult`/`FailResult`, `ErrorSpan`. (2) Modo local/remoto: `_inference_local()` ou `_inference_remote()`. (3) Integração: `Guard.use(validator)`. (4) Hub: marketplace sem fork.
**Fonte:** docs/how_to_guides/custom_validator.ipynb

## D12 — Observabilidade e métricas
`opentelemetry-sdk` com exporters, logging estruturado. `guard.history` por-sessão; sem série histórica persistente. Métricas: taxa aprovação/reprovação, latência, erros/tipo.
**Fonte:** pyproject.toml, guardrails_server.ipynb

## D13 — Segurança e permissões
**Compromisso maio 2026:** v0.10.1 malware (PyPI) via GitHub PAT roubado → 30 repos → deploy tokens. **Resposta:** rotação tokens org-wide, reset accounts, infraestrutura offline, políticas GitHub (verified commits, fine-grained PATs com expiração). **Contact:** security@guardrailsai.com. Paranoia de licenças; sem sandbox explícito para validators locais.
**Fonte:** SECURITY_ADVISORY.md (https://raw.githubusercontent.com/guardrails-ai/guardrails/HEAD/SECURITY_ADVISORY.md)

## D14 — Onboarding humano e documentação
**Decidir:** README (~2 min), 20+ notebooks (código limpo, chatbot, PII, entidades, estruturado, integrações LLM).
**Começar:** CONTRIBUTING (`make dev`, `make test`), 6+ how-to guides, 8 API reference docs.
Volume extenso; prioriza exemplos interativos.
**Fonte:** README, CONTRIBUTING.md, docs/

## D15 — Multi-projeto, multi-repo e equipe
Hub centralizado para compartilhar validators sem fork. CLI: `guardrails create`, `install`, `uninstall`. Sem governança cross-repo ou sincronização de doutrina.
**Fonte:** pyproject.toml, guardrails/cli/hub/

## D16 — Interação com o humano
**Automático:** `guard.parse()`, validators (PassResult/FailResult).
**Humano consulta:** code review (PRs obrigatórias), alertas críticos (segurança), escolha de validators.
**Nunca automático:** mudanças cross-deps, releases (maintainer gate), deploy malicioso (pós-0.10.1: verify signatures).
Servidor: HTTP REST; sem aprovação manual explícita.
**Fonte:** guardrails_server.ipynb, CONTRIBUTING.md, SECURITY_ADVISORY.md

---

## Rodapé

### 3 Práticas Transplantáveis
1. **Two-file strategy** (ranges largos em pyproject.toml, pinned em poetry.lock) — reduz conflitos. **Custo:** ~2-4h (Poetry).
2. **Three-gate Makefile** (lint+type+test pré-commit) — evita merges quebrados. **Custo:** ~4-6h (ruff+pyright+pré-commit).
3. **Plugin registry com decorador** (@register_validator, interface contratual) — extensão sem fork. **Custo:** ~8-12h (design, docs, exemplos).

### 3 Anti-práticas
1. **Usar versão comprometida "por compatibilidade"** (0.10.1/malware) — sacrifica segurança. **Motivo:** credenciais roubadas, dados expostos, reputação.
2. **PATs sem expiração/verificação de signatures** — vetor primário. **Motivo:** roubo = acesso 30 repos, CI/CD comprometido, releases maliciosas.
3. **PyPI sem validação signature/checksum pré-release** — injeta malware. **Motivo:** milhões de downloads maliciosos.

### Dimensões Fora da Grade
Nenhuma. Framework alinhado D1..D16; sem preocupações relevantes fora da grade.

---
**Repositório:** guardrails-ai/guardrails | **BM:** 16 | **Coleta:** 2026-07-29 | **Buscas:** 10/12 | **Gerador:** PANTONIC-V2 Estágio 1
