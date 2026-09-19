# RDO — P-0740 · LM-T3

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T3` — A evidência que basta ao reviewer
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** o dossiê de evidência, de ponta a ponta. Cobre o defeito 6 e absorve a `AUT-T5c`.

**Arquivos-alvo:** `.claude/tools/review_evidence.py` · `tests/test_review_evidence.py` · `docs/RUBRICA_DE_REVISAO.md` (seção da camada mecânica)

**Verificação:** `python -m pytest tests/test_review_evidence.py -q` verde — baseline medida no `ESC-3`: `25 passed` · `python -m pytest tests/ -q` verde, piso ≥ **153** (medido no `ESC-3`: `153 passed`; o piso de 145 venceu com a `LM-T1a`). O piso é mínimo e a `LM-T2a`, se rodar antes, acrescenta três testes.

**Pronto quando:** o dossiê gerado por `.claude/tools/review_evidence.py` traz, por arquivo vermelho, a atribuição "da entrega" ou "alheio" com o estado git que a comprova; os três testes nomeados em `Testes` existem em `tests/test_review_evidence.py`; `docs/RUBRICA_DE_REVISAO.md` descreve a atribuição na seção da camada mecânica; e as duas linhas de `Verificação` saem verdes com o piso ≥ **153**.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` — despachada em 2026-09-18 pelo `scrum-master`.
- **Esforço:** medium
- **Produto do módulo:** o dossiê passa a trazer, por arquivo vermelho, a **atribuição**: tocado por esta tarefa (dentro dos `Arquivos-alvo`) ou alheio (fora deles, com o estado git que o comprova). O reviewer deixa de precisar de injeção manual de contexto para não reprovar entrega correta.
- **Coerência do módulo (aceite de `DM-3`):** a atribuição usa a **mesma** função que já existe no módulo — `confrontar_escopo` (`:282-333`), com os cinco baldes da `DB-25`/`DB-32`. Uma pergunta, uma implementação, três consumidores: o dossiê (esta tarefa), o verbo `--atribuir` (`LM-T2a`) e a prosa `B0`/`B1` do loop (`LM-T2`). **Nenhuma** classificação nova se escreve aqui (`DM-19`).
- **Testes:** TF arquivo vermelho dentro dos alvos sai marcado como da entrega; TF arquivo vermelho fora dos alvos sai marcado como alheio com o estado git; TR a seção nova chama `confrontar_escopo` e **não** reimplementa a classificação (nenhum segundo laço de cobertura no módulo).
- **Depende de:** nada — **a dependência da `LM-T2` caiu no `ESC-3`** (`DM-19` (iv)): a função de atribuição já existe neste mesmo módulo e não nasce em tarefa nenhuma. Fica a **exclusão mútua** com a `LM-T2a` sobre `.claude/tools/review_evidence.py`: as duas editam o arquivo em regiões diferentes e não podem estar abertas ao mesmo tempo; qualquer ordem serve. **Esta tarefa fecha o `AE-13`**, que já custou duas injeções manuais de contexto na revisão.

## Execução

**Consumo:** 30 tool uses, 93.9 k tokens, 289.4 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: coletar_estado_git(root) ignora o --desde: arquivo ja commitado entre <ref> e HEAD sai 'alheio (sem entrada em git status)' — atribuicao sem a evidencia git que o card prometeu; rotear correcao (git diff <ref> --name-status) como tarefa do P-0740.

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
