# Matriz de cobertura — dimensão × framework

Origem: `docs/plans/P-0729-v2-confronto.md` §2 `T2` (Estágio 2 da iniciativa `PANTONIC-V2`).

Instrumento mecânico de leitura da matriz D1..D16 × corpus de relatórios de benchmarking
(`docs/benchmark/BM-*.md`), para a tarefa `V2C-T3` (Opus) enxergar o padrão de cobertura sem
reler os 22 relatórios individualmente.

**NOTA sobre a contagem de colunas:** o corpus tem **22 relatórios, `BM-00`..`BM-21`**
(`BM-00` = auto-retrato do próprio PantonicApp, os demais 21 = frameworks externos). O texto do
plano `P-0729-v2-confronto.md` §2 fala em "21 colunas (BM-00..BM-20)" — está desatualizado: o
`BM-21` nasceu depois, no `V2B-T7`. Esta matriz usa as **22 colunas reais**.

## Legenda

- `—` ausente — `~` parcial — `+` pleno (ver rubrica de classificação no `V2C-T2`, não repetida
  aqui: dúvida entre dois níveis resolve-se pelo menor).
- **Convenção de ponteiro (declarada uma única vez, não repetida em cada célula):** a célula da
  linha `Dx`, coluna `BM-NN` cita exatamente `BM-NN§Dx` — ou seja, a dimensão `Dx` dentro do
  relatório `docs/benchmark/BM-NN-<slug>.md`. Essa identidade é posicional e derivável de
  qualquer célula da tabela; nenhuma célula individual repete o texto do ponteiro.
- Títulos curtos de dimensão seguem `docs/benchmark/_ESQUEMA.md` linhas 10-27, sem deriva.

## Matriz (16 dimensões × 22 relatórios)

| Dim | Título | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1 | Identidade e escopo | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
| D2 | Vitalidade | — | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ |
| D3 | Ciclo de vida do trabalho | + | + | + | + | + | + | + | + | + | + | + | + | ~ | + | + | + | + | + | ~ | + | + | + |
| D4 | Papéis e modelo por fase | + | ~ | ~ | ~ | + | ~ | ~ | ~ | ~ | ~ | ~ | + | ~ | ~ | ~ | + | ~ | ~ | ~ | + | + | ~ |
| D5 | Unidade de trabalho e rastreabilidade | + | + | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | + | ~ | ~ | ~ | ~ | ~ | ~ | — | ~ | + | ~ |
| D6 | Contexto e custo | + | — | — | — | + | — | — | — | — | — | — | — | + | — | — | — | — | — | — | — | — | — |
| D7 | Memória e estado persistente | + | + | + | + | + | ~ | ~ | ~ | + | + | + | — | + | + | + | + | + | + | — | + | + | + |
| D8 | Qualidade e testes | ~ | + | ~ | ~ | — | — | ~ | ~ | + | + | — | + | + | ~ | ~ | + | + | + | + | — | + | — |
| D9 | Guardrails e enforcement | ~ | + | + | + | ~ | ~ | ~ | + | + | + | + | + | ~ | + | + | + | + | + | — | ~ | + | ~ |
| D10 | Distribuição e versionamento do próprio framework | + | + | + | + | + | + | ~ | ~ | + | — | + | — | ~ | — | — | ~ | + | + | + | + | + | — |
| D11 | Extensibilidade | + | + | ~ | + | + | + | + | + | + | — | + | ~ | + | + | ~ | + | + | + | + | ~ | + | — |
| D12 | Observabilidade e métricas | + | — | — | — | + | — | ~ | — | + | — | ~ | ~ | ~ | ~ | ~ | — | ~ | + | ~ | — | ~ | — |
| D13 | Segurança e permissões | ~ | — | — | ~ | + | ~ | — | ~ | + | + | + | + | ~ | ~ | ~ | ~ | + | ~ | ~ | + | — | — |
| D14 | Onboarding humano e documentação | + | + | + | + | + | + | + | + | + | + | + | + | + | ~ | + | ~ | + | + | + | + | + | + |
| D15 | Multi-projeto, multi-repo e equipe | + | ~ | ~ | + | — | + | ~ | — | ~ | ~ | + | ~ | ~ | — | ~ | + | ~ | — | — | — | + | ~ |
| D16 | Interação com o humano | + | + | + | + | + | + | + | + | + | + | + | + | + | + | ~ | ~ | + | + | + | + | + | + |

**Totais medidos (contando as 352 células):** `+` = 182 | `~` = 114 | `—` = 56.

## Listas derivadas (contadas na própria matriz)

### (a) Lacuna de consenso
Critério: `BM-00` é `—` **e** ≥5 frameworks (`BM-01`..`BM-21`) são `+` na mesma dimensão.

`(vazia)` — a única dimensão em que `BM-00` é `—` é `D2` (Vitalidade), mas nenhum framework
(`BM-01`..`BM-21`) marca `+` em `D2` — todos os 21 são `~` (contribuidores tipicamente
`NÃO ENCONTRADO` dentro de uma dimensão majoritariamente respondida). 0 frameworks em `+` < 5
exigido pelo critério.

### (b) Diferencial ou excentricidade
Critério: `BM-00` é `+` **e** ≤2 frameworks (`BM-01`..`BM-21`) são `+` na mesma dimensão.

- **D6 — Contexto e custo** — `BM-00` = `+`; 2 frameworks em `+` (`BM-04`, `BM-12`).

### (c) Candidatas a D17+
Critério: preocupação do agregado "Dimensões Fora da Grade" (`INDICE.md` linhas 73-98) citada
por ≥2 relatórios, agrupando redações equivalentes da mesma preocupação. Preocupação citada por
1 só relatório não entra.

1. **Ausência de teto/orçamento de contexto-turnos-custo enforçado** — `BM-05` ("Custo por
   sessão/turno sem orçamento explícito"), `BM-20` ("Ausência de teto de contexto/turnos/custo
   enforçado"). Contagem: 2 (`BM-05`, `BM-20`).
2. **Marketplace/registro central como infraestrutura canônica de descoberta, com lacunas de
   governança** — `BM-07` ("Marketplace (JSON) como fonte canônica de descoberta; compilação de
   workflows markdown → lock.yml com risco de inconsistência fonte/compilado"), `BM-15`
   ("Marketplace federado via git-subdir sem governança de versionamento/SLA entre contribuições
   locais e remotas"). Contagem: 2 (`BM-07`, `BM-15`).
3. **Falta de guia de precedência/escopo entre múltiplos mecanismos de extensão coexistentes
   (hooks/rules/skills/plugins)** — `BM-10` ("falta de guia de escopo entre
   hooks/rules/skills/plugins"), `BM-14` ("Ordem/precedência de múltiplos hooks no mesmo evento
   não é clara"). Contagem: 2 (`BM-10`, `BM-14`).

---

**Instrumento gerado por `V2C-T2` — sem juízo interpretativo; classificação mecânica conforme
rubrica do dossiê da tarefa.**
