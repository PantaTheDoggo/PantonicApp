# RDO — P-0752 · FPU-T2

# Humano

Tarefa "O gate do card roda no ensaio do planejador e no despacho do loop" concluída em 2026-09-26.
O verificador de cards voltou a ser obrigatório: o loop não despacha card que ele reprova, e o planejador o roda antes de gravar cada card.
Revisão: aprovada com ressalva (88%); pendência do laudo: O gate do card religado por esta tarefa recusa os cards restantes do P-0752 no despacho (card_check exit 1, medido na revisao: FPU-T5a itens 3 e 4 'sem valor antes' e ancora .claude/skills/scrum-master/SKILL.md:105 'Passo 5 - Recepcao do retorno do executor' deslocada para :109 pelas 4 linhas que esta entrega inseriu no Passo 3; FPU-T4 itens 1, 3, 4; FPU-T6 itens 2, 4): o proximo despacho cai em B3. Causa: forma 'antes exit <crase>0<crase>', 'antes:' em prosa e 'antes' sem 'depois' ficam fora do regex do par da DFP-14; decidir entre reparar os cards do plano ou estender o regex antes de seguir a fila..
Pendência para o dono: O gate religado recusa os cards restantes do P-0752 no despacho (FPU-T5a itens 3-4 e ancora scrum-master/SKILL.md:105 deslocada para :109; FPU-T4 itens 1, 3, 4; FPU-T6 itens 2, 4): formas 'antes exit <crase>0<crase>', 'antes:' em prosa e 'antes' sem 'depois' ficam fora do regex do par da DFP-14.
Plano "Fato no ponto de uso: os mecanismos contra o esquecimento e a assunção": 4/11 tarefas concluídas; próxima: "O executor, o revisor e o loop falam do arquivo de medida".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achados registrados no plano, com rota: 4 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/plans/P-0752-fato-no-ponto-de-uso.md`
**Tarefa:** `FPU-T2` — O gate do card roda no ensaio do planejador e no despacho do loop
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** o `card_check` volta a ser gate obrigatório de despacho (scrum-master Passo 3 e gate de delegação) e passo final da autoria (planejador Fase 4 item 14 e Fase 5); a nota de suspensão da rubrica sai e a `### 8.1` publica as duas formas.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md:65` — `  Terceiro gate, mecânico: \`python .claude/tools/modelo.py check --plano <plano>\`` - `.claude/skills/passagem-de-bastao/SKILL.md:133` — `Recusa de qualquer item do gate: **não delega**, e o que falta fechar volta ao planejamento.` - `.claude/agents/pantonic-planner.md:411` — `14. **Ensaio dos cards em árvore temporária** — antes de gravar, aplique os cards em sequência` - `docs/RUBRICA_DE_REVISAO.md:328` — `**Nota (2026-09-19):** o gate está **suspenso em efeito** desde 2026-09-19, por decisão do loop` - `.claude/README.md` (projeção regenerada, se o gerador do kit a reescrever)

**Verificação:** 1. `python -c "from pathlib import Path;print(Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8').count('card_check'))"` → `2` — antes `0`, depois `2`. 2. `python -c "from pathlib import Path;print(Path('.claude/skills/passagem-de-bastao/SKILL.md').read_text(encoding='utf-8').count('card_check'))"` → `1` — antes `0`, depois `1`. 3. `python -c "from pathlib import Path;print(Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8').count('card_check'))"` → `2` — antes `0`, depois `2`. 4. `python -c "from pathlib import Path;print(Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8').count('suspenso em efeito'))"` → `0` — antes `1`, depois `0`. 5. `pwsh .claude/checks/check-readme.ps1` → exit 0 — antes exit `0`, depois exit `0` (trava).

**Pronto quando:** card.premissas conferidas — conferidas por comando no ensaio da autoria e em todo despacho; card que não fecha não se despacha — Verificações 1 a 4.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Depende de:** `FPU-T1`, `FPU-T3`, `FPU-T5`
- **Operação do modelo:** `OP-2` - OP-2: O gate do card roda no ensaio do planejador e no despacho do loop, e card que não fecha não se despacha. - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; card — Quem implementa faz o instrumento ler a forma que o corpus vivo usa; card vivo não se reescreve para caber no instrumento.
- **Fundamento:** DFP-2, DFP-10, F-5; `docs/RUBRICA_DE_REVISAO.md:326-335`.
- **Passos:** 1. Scrum-master, Passo 3: depois do parágrafo do terceiro gate, inserir o quarto: `python .claude/tools/card_check.py --plano <plano> --tarefa <ID>` — exit `1`: **não delega**, o stderr vai à razão e a tarefa cai em `B3`, com a nota `gate do card`. Trocar `Aprovados os três` por `Aprovados os quatro`. 2. Passagem-de-bastão, gate de delegação: acrescentar o item 8, `card_check` exit 0 sobre o card, antes da linha `Recusa de qualquer item do gate`. 3. Planejador, Fase 4 item 14: nomear o instrumento — o ensaio roda `card_check.py --mundo antes` sobre cada card antes de gravar e `--mundo depois` sobre a cópia depois de aplicar o card; valor publicado é o medido. Fase 5: acrescentar `card_check` exit 0 para todo card como condição de registro, ao lado de `modelo.py check`. 4. Rubrica `### 8.1`: apagar o parágrafo da nota de suspensão (linhas 328-335, dois parágrafos, do `**Nota (2026-09-19):**` até `item a item, por quem despacha.`) e publicar a **forma B** (inline) ao lado da forma A (bloco cercado), com o par `antes`/`depois` e a regra de mundo por status (DFP-2, emendada por DFP-14: `→` e par opcionais, esperado comparado pela primeira crase), e a âncora com literal (DFP-4, emendada por DFP-16). 5. Regenerar `.claude/README.md` pelo gerador do kit se ele projetar as skills tocadas; rodar `pwsh .claude/checks/check-readme.ps1`.
- **Não fazer:** não tocar o bloco A nem o bloco B do scrum-master; não tocar `GOVERNANCA.md`; não reescrever cards vivos (I-3).
- **Contingências:** - se `pantonic-planner.md` tiver frontmatter que `yaml.safe_load` recuse depois da edição → a edição não tocou o frontmatter: parar e sinalizar `blocked` razão `premissa`, colando o erro.
- **Handover:** 2026-09-26 · para `FPU-T5a`, `FPU-T4` - **Entregue:** card_check e gate de despacho: .claude/skills/scrum-master/SKILL.md Passo 3 (quarto gate, exit 1 -> B3 com nota 'gate do card'; 'Aprovados os quatro'); .claude/skills/passagem-de-bastao/SKILL.md gate de delegacao item 8; .claude/agents/pantonic-planner.md Fase 4 item 14 (--mundo antes/depois no ensaio) e Fase 5 (card_check exit 0 por card); docs/RUBRICA_DE_REVISAO.md 8.1 sem a nota de suspensao, com Forma A e Forma B (inline) - **Contrato:** todo despacho roda card_check --plano <plano> --tarefa <ID>; exit 1 nao delega. Os cards restantes do P-0752 hoje saem exit 1 (FPU-T5a, FPU-T4, FPU-T6) - o reparo passa pelo consultor - **Não refazer:** nada a declarar - **Pendente:** scrum-master:62 diz 'sete itens' (agora oito) e a linha B3 do bloco B nao cita card_check; rubrica 8.1 diz literal 'comparado por strip() contra a linha citada' mas o instrumento confere contido em alguma linha da faixa
- **Notas de execução:** - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T2-o-gate-do-card-roda-no-ensaio-do-planejador-e-no-despacho-do.md`, veredito ressalva 88%

## Execução

**Consumo:** 27 tool uses, 107.2 k tokens, 313.1 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: O gate religado recusa os cards restantes do P-0752 no despacho (FPU-T5a itens 3-4 e ancora scrum-master/SKILL.md:105 deslocada para :109; FPU-T4 itens 1, 3, 4; FPU-T6 itens 2, 4): formas 'antes exit <crase>0<crase>', 'antes:' em prosa e 'antes' sem 'depois' ficam fora do regex do par da DFP-14
laudo: O gate do card religado por esta tarefa recusa os cards restantes do P-0752 no despacho (card_check exit 1, medido na revisao: FPU-T5a itens 3 e 4 'sem valor antes' e ancora .claude/skills/scrum-master/SKILL.md:105 'Passo 5 - Recepcao do retorno do executor' deslocada para :109 pelas 4 linhas que esta entrega inseriu no Passo 3; FPU-T4 itens 1, 3, 4; FPU-T6 itens 2, 4): o proximo despacho cai em B3. Causa: forma 'antes exit <crase>0<crase>', 'antes:' em prosa e 'antes' sem 'depois' ficam fora do regex do par da DFP-14; decidir entre reparar os cards do plano ou estender o regex antes de seguir a fila.

## Laudo

**Veredito:** ressalva

**Percentual:** 88%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

Motivo do parcial em criterio-de-pronto: Verificacoes 1 a 4 fecham (2, 1, 2, 0, re-medidas na revisao) e a 5 fecha a mao (check-readme exit 0), mas o objetivo manda a 8.1 publicar a ancora com literal pela DFP-16, e o texto publicado troca 'contido em alguma linha da faixa' por 'comparado contra a linha citada' (achado doutrina acima). O resto entregue: quarto gate no Passo 3 do scrum-master com 'Aprovados os quatro', item 8 no gate de delegacao, instrumento nomeado no item 14 e na Fase 5 do planejador, nota de suspensao apagada e forma B publicada. Observacao: o gate religado pegou, no primeiro uso, a ancora da FPU-T5a que esta mesma entrega envelheceu - o mecanismo funciona e o custo dele cai sobre a fila do proprio plano, que foi autorada antes de o gate valer.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "O executor devolve a medida como arquivo, e a evidência a incorpora" e vai pegar a tarefa "O gate do card roda no ensaio do planejador e no despacho do loop".
Tarefa "O gate do card roda no ensaio do planejador e no despacho do loop". Passo: conferir os gates e preparar o despacho.
Tarefa "O gate do card roda no ensaio do planejador e no despacho do loop": gates aprovados; vou materializar in-progress e gravar o ponto de partida.
Agente executor recebe a tarefa "O gate do card roda no ensaio do planejador e no despacho do loop" e vai executar: o `card_check` volta a ser gate obrigatório de despacho (scrum-master Passo 3 e gate de delegação) e passo final da autoria (planejador Fase 4 item 14 e Fase 5); a nota de suspensão da rubrica sai e a `### 8.1` publica as duas formas.
Agente executor devolveu a tarefa "O gate do card roda no ensaio do planejador e no despacho do loop": review — sem pendência.
Tarefa "O gate do card roda no ensaio do planejador e no despacho do loop": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O gate do card roda no ensaio do planejador e no despacho do loop" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O gate do card roda no ensaio do planejador e no despacho do loop": ressalva 88%, bloqueante nenhuma.
