# RDO — P-0750 · CAH-T3

**Plano:** `docs/plans/P-0750-comunicacao-agente-humano.md`
**Tarefa:** `CAH-T3` — A tabela de falhas de comunicação, com as falhas já medidas
**Modelo:** Sonnet · **Classe:** mecanica
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O mantenedor do registro cria a tabela de falhas de comunicação e nela transcreve as três falhas já medidas.

**Arquivos-alvo:** - `docs/FALHAS_COMUNICACAO.tsv` (novo)

**Verificação:** 1. ``` python -c "import csv;r=list(csv.reader(open('docs/FALHAS_COMUNICACAO.tsv',encoding='utf-8',newline=''),delimiter='\t'));print(len(r),sorted({len(x) for x in r}),r[0][0],r[3][0])" ``` → **`4 [6] data 2026-09-24`**. **Medido antes: arquivo inexistente**.

**Pronto quando:** - kit.registro de falha — tabela de máquina de uma linha por falha, gravada por quem recebeu a pergunta — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Fundamento:** DCH-4; F-8.
- **Depende de:** `CAH-T1`
- **Operação do modelo:** `OP-3` - OP-3: O mantenedor do registro cria a tabela de falhas de comunicação e nela transcreve as três falhas já medidas. - precisa de: kit — Quem implementa recebe esses textos. O que esta entrega não toca continua valendo como hoje. - precisa de: falhas medidas — Quem implementa as transcreve, sem reinterpretar.
- **Camada e fronteira:** artefato de máquina do projeto, em `docs/`, ao lado de `docs/telemetria.tsv`.
- **Passos:** 1. Confirmar que `docs/FALHAS_COMUNICACAO.tsv` não existe. 2. Gravar o arquivo com `Write`, trocando cada `⇥` por TAB. 3. Rodar a Verificação 1.
- **Restrições desta tarefa:** nenhuma célula contém TAB ou quebra de linha; o texto das falhas é transcrito, não reescrito.
- **Não fazer:** não criar instrumento de gravação; não tocar `docs/telemetria.tsv`.
- **Contingências:** 1. se o arquivo já existir → parar e sinalizar `blocked` razão `premissa`.
- **Testes:** nenhum novo; a Verificação 1 confere a forma.
- **Fora do escopo desta tarefa:** o procedimento de quem grava a linha (`CAH-T4`, na skill).

## Execução

**Consumo:** 6 tool uses, 47.5 k tokens, 30.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
