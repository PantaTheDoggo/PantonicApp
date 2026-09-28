# RDO — P-0745 · PLN-T3

**Plano:** `docs/plans/P-0745-planejador-modelo-operacao.md`
**Tarefa:** `PLN-T3` — A gramática do card: a tarefa é a materialização de uma operação
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** a skill `diario-de-obras` apresenta o formato de uma tarefa como a materialização de uma operação do modelo, com o campo `Operação do modelo` no bloco de formato; as skills `modelo-por-fase` e `bootstrap-pantonic` e o agente `pantonic-fora-da-caixa` deixam de nomear a tarefa atômica.

**Arquivos-alvo:** - `.claude/skills/diario-de-obras/SKILL.md:206-225` (heading `## Formato de uma tarefa atômica` e o bloco de formato) - `.claude/skills/modelo-por-fase/SKILL.md:24` (linha `| Execução (implementar/editar/testar/corrigir) |`) - `.claude/skills/bootstrap-pantonic/SKILL.md:34` (`checklists de tarefas atômicas`) - `.claude/agents/pantonic-fora-da-caixa.md:54` (`cada passo virando tarefa atômica candidata`) - `tests/test_doutrina_unidade.py` (criado pela `PLN-T2`; soma um teste)

**Verificação:** 1. ``` grep -c '^## Formato de uma tarefa atômica' .claude/skills/diario-de-obras/SKILL.md ``` → **0**. **Medido antes: 1**. 2. ``` grep -c '^## Formato de uma tarefa$' .claude/skills/diario-de-obras/SKILL.md ``` → **1**. **Medido antes: 0**. 3. ``` grep -c 'Operação do modelo' .claude/skills/diario-de-obras/SKILL.md ``` → **um número maior em 2 que o medido no despacho** (o parágrafo novo e a linha do bloco de formato). **Medido antes: 1** (2026-09-21). 4. ``` grep -c 'tarefa atômica\|tarefas atômicas' .claude/skills/modelo-por-fase/SKILL.md .claude/skills/bootstrap-pantonic/SKILL.md .claude/agents/pantonic-fora-da-caixa.md ``` → três linhas, todas terminando em `:0`. **Medido antes: `:1`, `:1`, `:1`**. 5. ``` python -m pytest tests -q ``` → `<N> passed`, com `<N>` igual ao total re-medido no despacho **mais 1**. **Medido antes: `262 passed`** (2026-09-21, antes da `PLN-T2`). 6. ``` python .claude/tools/backlog.py check ``` → `check: OK — nenhuma violação.`, exit **0**. **Medido antes: o mesmo**.

**Pronto quando:** as seis verificações imprimem os valores declarados. Por propriedade que a operação altera (`DPN-6`): - `agente de planejamento.unidade de trabalho que ele recorta` — a parcela desta tarefa: o bloco de formato que ele preenche abre por *Formato de uma tarefa*, declara o card como a materialização de uma operação, traz o campo `Operação do modelo` com o texto e os contratos copiados e faz o `Pronto quando` derivar do estado final de cada propriedade que a operação altera; e nenhuma das quatro definições de conduta nomeia a tarefa atômica como unidade, com as ocorrências de outro sentido, como passo atômico de migração, intactas — Verificação 1, 2, 3 e 4. - As demais entregas desta tarefa são **requisito secundário** (`## Requisitos secundários`), não propriedade do modelo: a extensão da guarda `tests/test_doutrina_unidade.py`, aferida pela Verificação 5.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-22
- **Depende de:** `PLN-T2`
- **Fundamento:** `DPN-2`, `DPN-6`, `DPN-9`; fatos `F-6`; censo da §7 (linhas das skills e do `pantonic-fora-da-caixa`).
- **Operação do modelo:** `OP-2` - OP-2: O redator da gramática reescreve a forma do card que quem planeja emite: ele passa a nascer como a materialização de uma operação, com o texto dela copiado e o contrato dos objetos de que ela precisa, e as demais definições de conduta deixam de chamar a unidade pelo nome antigo. - precisa de: agente de planejamento — residências da conduta: `.claude/agents/pantonic-planner.md` (descrição, tese do papel, abertura do protocolo, Fases 3a e 3b, Fase 4, Fase 5, anatomia do card e rodada de replanejamento) e a região gerada `kit:agents` de `.claude/README.md` — produzida por `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` e nunca editada à mão. Residências da régua e da unidade: `GOVERNANCA.md` §3 (matriz de responsabilidades, *A unidade de trabalho é o módulo coeso*, *Diretriz de dimensionamento de tarefa*, tabela da §4, §4.1, §4.3, G-PLANREADY e G-MODULO), `.claude/global/CLAUDE.md` (Regras 2 e 7) e a cópia do dono (`DPN-12`), `docs/RESIDENCIA_DOUTRINA.md`, as skills `diario-de-obras` (*Formato de uma tarefa*), `modelo-por-fase` e `bootstrap-pantonic`, `.claude/agents/pantonic-fora-da-caixa.md` e `README.md`. Residência da responsabilidade pelo lastro: `GOVERNANCA.md` §3.2 e `.claude/agents/pantonic-model-designer.md`, nas duas pontas no mesmo card. Residência da descrição: `docs/planner-spec.md` (novo), uma seção por dimensão da §4, na ordem dela e aberta por `## 0. O que esta especificação não é`. O censo linha a linha, com destino, é a §7; a classe do cabeçalho do card permanece como natureza do trabalho, porque os parsers a leem; ocorrência de outro sentido — escrita atômica em disco, passo atômico de migração — fica intacta; as entradas `RP-1`..`RP-7` e os itens de verificação que não citam ocupação permanecem, são a memória medida do papel; o escopo do papel continua na matriz de `GOVERNANCA.md` §3 (G-SCOPE), e a especificação não é residência nem do escopo nem do protocolo de conduta; tarefa — nenhum card deste plano altera uma tarefa. O que se observa nela, antes e depois, é o padrão sob o qual ela nasce: o nome da unidade no cabeçalho e na doutrina, a régua que definiu o recorte e a presença do campo `Operação do modelo` com o texto e os contratos copiados. Os sete cards deste plano, escritos sob o padrão antigo, são o retrato do antes; a aferição do depois é o primeiro plano decomposto depois da `PLN-T4`, lido por `python .claude/tools/modelo.py show`
- **Camada e fronteira:** skills e um agente do kit; um teste somado ao arquivo criado pela `PLN-T2`. A subseção "Modelo de domínio (seção do plano)" da skill `diario-de-obras` **não se toca** (fronteira com o `P-0743`, §6).
- **Passos:** 1. Em `.claude/skills/diario-de-obras/SKILL.md:206`, substituir o heading `## Formato de uma tarefa atômica` por `## Formato de uma tarefa` e inserir, logo abaixo dele e antes do bloco cercado, o parágrafo literal: `Uma tarefa é a **materialização de uma operação do modelo** (`GOVERNANCA.md` §3.2): o `Objetivo` copia o texto da operação, o campo `Operação do modelo` traz o texto e os contratos copiados (gramática em "Modelo de domínio (seção do plano)", acima), e o `Pronto quando` deriva do estado final das propriedades que a operação altera. Um card por operação; card corretivo (`T<n>a`) soma-se à operação do card que corrige.` 2. No bloco cercado de formato (linhas 209-226), inserir, imediatamente depois da linha `- **Objetivo:** <uma frase>`, a linha literal: `- **Operação do modelo:** `OP-<n>` + os dois sub-bullets copiados (texto da operação; `precisa de:` com contrato)` e substituir a linha `- **Pronto quando:** <critério objetivo>` por `- **Pronto quando:** <por propriedade que a operação altera, o estado final da ### 1.3 e a verificação que o mede>`. 3. Em `.claude/skills/modelo-por-fase/SKILL.md:24`, substituir `Uma tarefa atômica do diário de obras, TDD` por `Um card do diário de obras — a materialização de uma operação do modelo —, TDD`. 4. Em `.claude/skills/bootstrap-pantonic/SKILL.md:34`, substituir `checklists de tarefas atômicas` por `checklists de cards, um por operação do modelo`. 5. Em `.claude/agents/pantonic-fora-da-caixa.md:54`, substituir `cada passo virando tarefa atômica candidata` por `cada passo virando card candidato, a materializar por uma operação do modelo do plano que o adotar`. 6. Apensar a `tests/test_doutrina_unidade.py` a função literal: ```python def test_skill_diario_formato_de_tarefa_pela_operacao(): t = _texto(".claude/skills/diario-de-obras/SKILL.md") assert "## Formato de uma tarefa atômica" not in t assert "## Formato de uma tarefa\n" in t assert "materialização de uma operação do modelo" in t ``` 7. Rodar as verificações abaixo.
- **Restrições desta tarefa:** - A subseção `### Modelo de domínio (seção do plano)` (linhas 175-204) não se edita. - Os literais dos passos 1-6 entram como estão. - Não commitar (`I-1`).
- **Não fazer:** - Não editar `.claude/agents/pantonic-fora-da-caixa.md:67` ("passos atômicos, cada um testável"): é passo de migração, outro sentido (§7). - Não editar `pantonic-executor.md:140`: o heading é a negação da forma antiga (§7). - Não regenerar `.claude/README.md`: nenhuma `description` muda neste card.
- **Contingências:** 1. Se uma âncora de linha não casar com o texto declarado → localizar pelo literal (`grep -n`) e seguir; literal ausente → parar e sinalizar `blocked` razão `premissa`. 2. Se `tests/test_doutrina_unidade.py` não existir → parar e sinalizar `blocked` razão `dependencia` (`PLN-T2`).
- **Testes:** `TR-DU-3` (`test_skill_diario_formato_de_tarefa_pela_operacao`); suíte: `python -m pytest tests -q`.
- **Fora do escopo desta tarefa:** o protocolo do planejador (`PLN-T4`) e a `description` dele, que é o que a região gerada de `.claude/README.md` repete.

## Execução

**Consumo:** 17 tool uses, 56.9 k tokens, 107.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: dimensão registro marcada parcial: a linha de retorno citou o medido antes desatualizado em prosa, sem nomear a verificação nem dar rota, o que obrigou a revisão a re-derivar as seis baselines

## Laudo

**Veredito:** ressalva

**Percentual:** 94%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva: dois achados de alvo dossiê, ambos com rota. (1) âncoras do card desatualizadas sobre alvo compartilhado, rota AE-12 do P-0745; (2) Medido antes da Verificação 5 defasado em +9, rota sem ação — a forma do item é relativa ao total re-medido, então o aceite se sustenta em 272 = 271 + 1

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
