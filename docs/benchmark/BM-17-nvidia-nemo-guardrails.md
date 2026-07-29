# BM-17: NVIDIA NeMo-Guardrails

**Repo:** `NVIDIA-NeMo/Guardrails` | **Trilha:** E | **Stars:** 6824 | **Push:** 2026-07-29T07:29:11Z | **Versão:** 0.23.0 | **Licença:** NOASSERTION

---

## D1 — Identidade e escopo

Toolkit que adiciona guardrails programáveis a LLMs. Resolve vulnerabilidades (jailbreaks, injeção de prompt) e tema-boundedness. Público: desenvolvedores de aplicações LLM seguras e confiáveis.
[README](https://raw.githubusercontent.com/NVIDIA-NeMo/Guardrails/HEAD/README.md)

## D2 — Vitalidade

6824 stars | Último push: 2026-07-29T07:29:11Z | Contribuidores: NÃO ENCONTRADO | Licença: NOASSERTION | Versão: 0.23.0 (2026-07-01) | Releases ~1-2 meses.
**Fonte:** `docs/benchmark/_CORPUS.md` linha 65; [CHANGELOG](https://raw.githubusercontent.com/NVIDIA-NeMo/Guardrails/HEAD/CHANGELOG.md)

## D3 — Ciclo de vida do trabalho

Issue triada → Aprovação de plano → Implementação em `develop` → `make test` obrigatório → `make pre-commit` → Documentação → Review+merge. Artefatos: Issue → PR (linked, conventional commit) → Testes automatizados → Merge.
[AGENTS.md](https://raw.githubusercontent.com/NVIDIA-NeMo/Guardrails/HEAD/AGENTS.md) | [CONTRIBUTING.md](https://raw.githubusercontent.com/NVIDIA-NeMo/Guardrails/HEAD/CONTRIBUTING.md)

## D4 — Papéis e modelo por fase

**Papéis:** Devs comunitários (Code), Mantenedores NVIDIA (triagem/aprovação/merge), IA auxiliar sem submissão automática. Sem delegação de decisões críticas. Modelo por fase: não documentado.
[AGENTS.md](https://raw.githubusercontent.com/NVIDIA-NeMo/Guardrails/HEAD/AGENTS.md)

## D5 — Unidade de trabalho e rastreabilidade

Issue triada → PR (linked via "Closes #XYZ") → Testes obrigatórios (workflows automáticos) → Merge. Sem 1:1 teste por requisito.
[CONTRIBUTING.md](https://raw.githubusercontent.com/NVIDIA-NeMo/Guardrails/HEAD/CONTRIBUTING.md)

## D6 — Contexto e custo

NÃO ENCONTRADO

## D7 — Memória e estado persistente

Config guardrails: YAML (disco, versionado). Estado conversacional: memória (serializável). Histórico: app hospedeira. Versão: pyproject.toml. Persistência em: disco (exemplos/configs), Git (histórico).
[Árvore](docs/benchmark/_trees/nvidia-nemo-guardrails.txt)

## D8 — Qualidade e testes

Sem TDD explícito. Testes obrigatórios: `make test`, `make test-coverage`. Workflows automáticos (pr-tests.yml, full-tests.yml). Pre-commit verifica linting/formatação/headers. Piso: suite completa.
[CONTRIBUTING.md](https://raw.githubusercontent.com/NVIDIA-NeMo/Guardrails/HEAD/CONTRIBUTING.md)

## D9 — Guardrails e enforcement

~70% código executável (Makefile, GitHub Actions), ~30% texto. Pre-commit obrigatório, testes obrigatórios (workflows), label `status: triaged` bloqueia, signing obrigatório (GPG ou Signed-off-by).
[CONTRIBUTING.md](https://raw.githubusercontent.com/NVIDIA-NeMo/Guardrails/HEAD/CONTRIBUTING.md)

## D10 — Distribuição e versionamento do próprio framework

PyPI: `pip install nemoguardrails==0.23.0`. Sem auto-upgrade. Semantic versioning (MAJOR.MINOR.PATCH). Releases via `publish-wheel.yml` (input manual de versão).
[publish-wheel.yml](https://raw.githubusercontent.com/NVIDIA-NeMo/Guardrails/HEAD/.github/workflows/publish-wheel.yml)

## D11 — Extensibilidade

**Actions:** Criação (`creating-actions.mdx`), registrando (`registering-actions.mdx`). **Colang:** v1.0 e v2.x (linguagem própria). **LLM backends:** exemplos em `examples/configs/llm/`. Sem forking necessário.
[Árvore](docs/benchmark/_trees/nvidia-nemo-guardrails.txt)

## D12 — Observabilidade e métricas

Logging detalhado, OpenTelemetry (métricas, tracing), Jaeger. Span reference, content capture, adapter configs documentados. Série histórica: depende de exportador externo.
[Árvore](docs/benchmark/_trees/nvidia-nemo-guardrails.txt)

## D13 — Segurança e permissões

**Modelo:** Sem autenticação/autorização/TLS/rate-limiting nativo. Segurança via infraestrutura (gateway/proxy/load balancer). **Proteções:** Guardrails contra jailbreaks, llama_guard, nemoguards, sensitive-data-detection. Secrets via env vars (app responsável).
[SECURITY.md](https://raw.githubusercontent.com/NVIDIA-NeMo/Guardrails/HEAD/SECURITY.md)

## D14 — Onboarding humano e documentação

README (~200 linhas), CONTRIBUTING (~100 linhas), docs em https://docs.nvidia.com/nemo/guardrails. 50+ exemplos, 7+ tutoriais. Para decisor: ~30 min. Para começar: ~1-2h.
[README](https://raw.githubusercontent.com/NVIDIA-NeMo/Guardrails/HEAD/README.md)

## D15 — Multi-projeto, multi-repo e equipe

Único repo oficial, exemplos em subpastas. Sem framework de doutrina distribuída. Equipe: Mantenedores NVIDIA (triagem/merge) + comunidade aberta.
[AGENTS.md](https://raw.githubusercontent.com/NVIDIA-NeMo/Guardrails/HEAD/AGENTS.md)

## D16 — Interação com o humano

Decisões humanas obrigatórias: triagem, aprovação de plano, review, merge. Nunca automático: triagem, plano, merge, publicação (requer input de versão). IA auxiliar, nunca substitui.
[AGENTS.md](https://raw.githubusercontent.com/NVIDIA-NeMo/Guardrails/HEAD/AGENTS.md)

---

## Práticas transplantáveis

1. **Conventional Commit + Auto-Changelog:** Prefixos (`fix:`, `feat:`, `docs:`) com CHANGELOG automático evita overhead manual. Custo: ~1-2h setup.
2. **Duas versões de linguagem em paralelo:** Colang v1 e v2 coexistem, adoção gradual. Custo: 2-4 semanas arquitetura.
3. **Guardrails via código (Makefile + pre-commit):** Enforce de linting/formatação/headers. Custo: 4-8h config.

## Anti-práticas

1. **Segurança perimetral-only sem sandbox:** Reduz complexidade do framework mas aumenta risco em devlocal/deployments ad-hoc.
2. **Testes obrigatórios sem TDD explícito:** Gates funcionam mas perdem design-by-tests e descoberta de bugs antes da implementação.
3. **Publicação manual no PyPI:** Input humano de versão previne typos mas adiciona fricção e risco tag-vs-artefato.

## Dimensões fora da grade

**Colang v1.0 vs v2.x:** Mantém duas linguagens simultâneas sem breaking change — merecia dimensão própria sobre "evolução de domínio-específica sem obsolescência forçada".
