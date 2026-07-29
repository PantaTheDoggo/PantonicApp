# Esquema fixo de relatório de benchmarking (D1..D16)

Origem: `docs/plans/P-0729-v2-benchmarking.md` §3 (Estágio 1 da iniciativa `PANTONIC-V2`).
Todo relatório em `docs/benchmark/BM-<NN>-<slug>.md` usa **exatamente** estas 16 dimensões, nesta
ordem, com estes títulos — é o que torna 20 relatórios de Haiku confrontáveis em um único passe de
Opus no Estágio 2, e é a grade da matriz de cobertura (`P-0729-v2-confronto` T2).

**Dimensão sem evidência recebe literalmente `NÃO ENCONTRADO`, nunca inferência.**

| id | Dimensão | O que responder |
|---|---|---|
| D1 | Identidade e escopo | O que é, que problema resolve, para que tipo de projeto |
| D2 | Vitalidade | Stars, último push, nº de contribuidores, licença (do cache do T3) |
| D3 | Ciclo de vida do trabalho | Fases, artefatos produzidos em cada uma, gates entre elas |
| D4 | Papéis e modelo por fase | Que agentes/papéis existem; há escolha explícita de modelo por fase? |
| D5 | Unidade de trabalho e rastreabilidade | O que é "uma tarefa"; existe rastro requisito → código → teste? |
| D6 | Contexto e custo | Há orçamento/limite explícito de contexto, turnos ou dinheiro? Como? |
| D7 | Memória e estado persistente | O que sobrevive entre sessões e onde vive |
| D8 | Qualidade e testes | TDD? Gates de teste? Noção de regressão/piso? |
| D9 | Guardrails e enforcement | As regras são texto, checklist, ou **código executável**? Qual proporção? |
| D10 | Distribuição e versionamento do próprio framework | Como o consumidor instala, atualiza e sabe a versão que tem |
| D11 | Extensibilidade | Plugins, skills, comandos, hooks — como se estende sem forkar |
| D12 | Observabilidade e métricas | Telemetria de consumo/qualidade; existe série histórica? |
| D13 | Segurança e permissões | Sandbox, allowlist, segredos, ações destrutivas |
| D14 | Onboarding humano e documentação | Quanto um humano precisa ler para decidir e para começar |
| D15 | Multi-projeto, multi-repo e equipe | Vários projetos/pessoas compartilham a doutrina? Como? |
| D16 | Interação com o humano | Onde o humano aprova, decide, é consultado; o que nunca é automático |

## Rodapé obrigatório de todo relatório

Além das 16 dimensões, todo relatório fecha com:

- **3 práticas transplantáveis** — cada uma com o custo estimado de adoção.
- **3 anti-práticas** — o que este framework faz que seria um erro copiar, com o motivo.
- **Dimensões fora da grade** — qualquer preocupação relevante deste framework que **não** cabe em
  D1..D16. Este campo é o principal instrumento de descoberta pedido pelo dono; "nenhuma" é
  resposta válida, mas nunca é resposta automática.

## Regra de evidência

Toda afirmação carrega a URL exata (arquivo, não repositório) de onde saiu. Sem URL, a linha não
existe. Informação não confirmada nesta execução — mesmo para repositórios famosos — é
`NÃO ENCONTRADO`, nunca resposta de memória de treino.
