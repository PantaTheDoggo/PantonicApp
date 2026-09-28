# RDO — P-0746 · LST-T3

**Plano:** `docs/plans/P-0746-lastro-do-modelo.md`
**Tarefa:** `LST-T3` — A residência do requisito secundário
**Modelo:** Opus · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** a gramática publicada do plano ganha a seção **Requisitos secundários** — onde o elemento sem lastro fica visível ao dono sem participar do contrato, com a responsabilidade declarada como inteira do agente.

**Arquivos-alvo:** - `.claude/skills/diario-de-obras/SKILL.md` — subseção da gramática do plano

**Verificação:** 1. ``` grep -cF 'Requisitos secundários' .claude/skills/diario-de-obras/SKILL.md ``` → **≥ 1**. **Medido antes: 0** (2026-09-21; `F-9` mediu 0 para a família da palavra). 2. ``` grep -cF 'não entra no modelo e não é aferido por lastro' .claude/skills/diario-de-obras/SKILL.md ``` → **≥ 1**. **Medido antes: 0** (2026-09-21). É o literal que separa a seção nova do modelo: sem ele, a gramática nomearia a seção sem dizer que ela fica fora do contrato. 3. Par presença-ausência sobre a forma: a seção é declarada **fora** da `## 1` — a gramática diz, por literal, que elemento da seção de requisitos secundários não entra no modelo e não é aferido por lastro. 4. ``` python -m pytest tests -q ``` → **≥ 262 passed** (`I-3`).

**Pronto quando:** as quatro verificações saem nos valores declarados. Por propriedade: - `restrições do modelo conceitual.decomposição de requisitos funcionais e não funcionais` — o elemento com lastro é funcional e entra no modelo; o sem lastro reside em seção nomeada fora do modelo, transparente ao dono e sob responsabilidade inteira do agente — Verificação 1 e 2.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-22
- **Depende de:** `LST-T7`
- **Fundamento:** `DLS-2`; fatos `F-1`, `F-9`. Precedente de forma: a `## 2` **deste** plano, que já é a primeira aplicação da residência.
- **Operação do modelo:** `OP-4` - OP-4: O redator da gramática constrói a restrição de decomposição de requisitos funcionais e não funcionais: o elemento com lastro é funcional e entra no modelo como contrato; o elemento sem lastro é não fundamental, reside em seção nomeada do plano fora do modelo, fica transparente para o dono e tem responsabilidade inteira do agente. - precisa de: restrições do modelo conceitual — norma em `GOVERNANCA.md` §3.2; forma publicada na subseção *Modelo de domínio (seção do plano)* da skill `diario-de-obras`; aferição em `.claude/tools/modelo.py` (`check`), com `tests/test_modelo.py` e fixtures; autoria em `.claude/agents/pantonic-model-designer.md`
- **Camada e fronteira:** gramática publicada. Nenhum instrumento — a `LST-T5` não afere esta seção, só a ausência de elemento sem lastro **dentro** do modelo.
- **Domínio:** *requisito secundário* — entrega que o agente julga necessária e que o enunciado não pediu. *Transparente* — visível ao dono e declarada, **não** submetida a aprovação dele.
- **Literais obrigatórios (verbatim, não parafrasear):** na skill, `Requisitos secundários` (o nome da seção, como a gramática o publica) e `não entra no modelo e não é aferido por lastro` (`DLS-14`).
- **Nota de aceite (`F-16`):** `grep -cF`, nunca `grep -ciF` (aborta, exit `134`).
- **Fora do escopo desta tarefa:** `GOVERNANCA.md` (fechado nas `LST-T1` e `LST-T7`), o instrumento (`LST-T5`), e a residência da declaração de lastro na tabela de gramática (`LST-T8`, a tarefa seguinte, que edita a mesma subseção) — as duas não se misturam no mesmo card.

## Execução

**Consumo:** 6 tool uses, 42.0 k tokens, 55.6 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

Tres observacoes. (1) Exercicio ponta a ponta do modulo: com a secao 2 nova no P-0746, modelo.py check saiu 0 e show/--pendente seguiram corretos - a delimitacao da 1A pelo proximo heading de nivel 2 continua valida com a secao de requisitos secundarios ocupando o numero 2. Nenhuma divergencia interna entre os tres paragrafos que LST-T1, LST-T7 e LST-T3 acumularam na mesma subsecao. (2) O aceite por literal verbatim discriminou bem o que a tarefa tinha de pousar, mas nao alcanca o que o texto afirma alem do literal: a fixacao do numero de secao passou pelas quatro verificacoes verdes e so aparece confrontando a gramatica com o corpus de planos. Para doutrina de kit, aceite por literal pede par com confronto do corpus que a regra nova passa a reger. (3) Tarefa de redacao de baixo custo (6 tool uses) sobre subsecao ja aquecida por duas tarefas anteriores da mesma janela - o encadeamento rendeu texto coerente sem custo de releitura.

## Fechamento

**Desdobramento:** aprovado
