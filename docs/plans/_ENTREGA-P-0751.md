# Entrega — P-0751 · Esgotar o backlog antes da publicação do kit

# Humano

Plano "Esgotar o backlog antes da publicação do kit" fechado em 2026-09-26, pelo aceite do dono: "Rode o revisor, considere o veredito do 0751 aceito e encerre.".
O backlog de cards prontos antes da publicação do kit foi esgotado: as 16 tarefas do plano estão concluídas.
Tarefas: 16 concluídas de 16; aprovadas sem ressalva: 15; com ressalva: 1.
Achados da execução: 4, todos com rota.
Documento de validação: `docs/OPERACOES_AS_IS_P-0751.md`.
Instrumentos no fechamento: modelo conferido sem violação; gramática do diário: sem violação.
Consumo do plano na série de telemetria: 3797.3 mil tokens em 46 linha(s).

# Máquina

**Plano:** `docs/plans/P-0751-esgotar-backlog.md` · **Id:** `P-0751` · **Fechado em:** 2026-09-26
**Veredito do dono (verbatim):** Rode o revisor, considere o veredito do 0751 aceito e encerre.
**Documento de validação:** `docs/OPERACOES_AS_IS_P-0751.md`
**Gate do modelo:** `modelo.py check` exit 0 — modelo: OK — 14 operações, 2 objetos, 2 propriedades, 16 tarefas, versão 1
**Gramática do backlog:** `backlog.py check` — sem violação

## Tarefas

| tarefa | título | status | veredito | percentual | desdobramento | RDO |
|---|---|---|---|---|---|---|
| `EBK-T1` | O `check` acusa tíquete vivo sem card | done | aprovado | 100% | aprovado | `docs/RDO/P-0751-EBK-T1-o-check-acusa-tiquete-vivo-sem-card.md` |
| `EBK-T2` | O `check` confronta o card com o `rdo.py` e o piso com o corpus | done | aprovado | 100% | aprovado | `docs/RDO/P-0751-EBK-T2-o-check-confronta-o-card-com-o-rdo-py-e-o-piso-com-o-corpus.md` |
| `EBK-T3` | O `next` projeta o colchete do cabeçalho inteiro | done | aprovado | 100% | aprovado | `docs/RDO/P-0751-EBK-T3-o-next-projeta-o-colchete-do-cabecalho-inteiro.md` |
| `EBK-T4` | `rdo.py close` recusa tarefa que não está `done` | done | aprovado | 100% | aprovado | `docs/RDO/P-0751-EBK-T4-rdo-py-close-recusa-tarefa-que-nao-esta-done.md` |
| `EBK-T5` | O `kit_check` conta defeito, não linha | done | ressalva | 91% | aprovado com ressalva | `docs/RDO/P-0751-EBK-T5-o-kit-check-conta-defeito-nao-linha.md` |
| `EBK-T5a` | O `kit_check` não conta o sumário do `materializar` e detalha sob o problema | done | aprovado | 100% | aprovado | `docs/RDO/P-0751-EBK-T5a-o-kit-check-nao-conta-o-sumario-do-materializar-e-detalha-so.md` |
| `EBK-T6` | Nenhuma fixture carrega nome que o harness descobre | done | aprovado | 100% | aprovado | `docs/RDO/P-0751-EBK-T6-nenhuma-fixture-carrega-nome-que-o-harness-descobre.md` |
| `EBK-T7` | A doutrina do teste que discrimina e da medida publicada | done | aprovado | 100% | aprovado | `docs/RDO/P-0751-EBK-T7-a-doutrina-do-teste-que-discrimina-e-da-medida-publicada.md` |
| `EBK-T8` | A vigência do modelo, o desfecho do drift recusado e o lastro na descrição pública | done | aprovado | 100% | aprovado | `docs/RDO/P-0751-EBK-T8-a-vigencia-do-modelo-o-desfecho-do-drift-recusado-e-o-lastro.md` |
| `EBK-T9` | Uma operação, uma oração | done | aprovado | 100% | aprovado | `docs/RDO/P-0751-EBK-T9-uma-operacao-uma-oracao.md` |
| `EBK-T10` | A régua de autoria do card, segunda leva | done | aprovado | 100% | aprovado | `docs/RDO/P-0751-EBK-T10-a-regua-de-autoria-do-card-segunda-leva.md` |
| `EBK-T11` | O planejador publica o grep da superfície e ensaia os cards antes de gravar | done | aprovado | 100% | aprovado | `docs/RDO/P-0751-EBK-T11-o-planejador-publica-o-grep-da-superficie-e-ensaia-os-cards.md` |
| `EBK-T12` | Três ajustes de regra existente: a devolução do modelador, o enunciado composto e o aviso de modelo | done | aprovado | 100% | aprovado | `docs/RDO/P-0751-EBK-T12-tres-ajustes-de-regra-existente-a-devolucao-do-modelador-o-e.md` |
| `EBK-T13` | Quanto custa retomar o planejador por mensagem | done | aprovado | 100% | aprovado | `docs/RDO/P-0751-EBK-T13-quanto-custa-retomar-o-planejador-por-mensagem.md` |
| `EBK-T13a` | A razão da regra da retomada sai do custo de partida, não da média | done | aprovado | 100% | aprovado | `docs/RDO/P-0751-EBK-T13a-a-razao-da-regra-da-retomada-sai-do-custo-de-partida-nao-da.md` |
| `EBK-T14` | A rodada de revisão de guardrails pendente desde 2026-08-08 | done | aprovado | 100% | aprovado | `docs/RDO/P-0751-EBK-T14-a-rodada-de-revisao-de-guardrails-pendente-desde-2026-08-08.md` |

## Achados da execução (verbatim do plano)

- **AE-1** (`EBK-T1`, `blocked` premissa, 2026-09-25) — a contingência mandava a subtarefa da fixture herdar "o mesmo status do tíquete"; o `TK-2` da `vermelho` tem `backlog`, fora do vocabulário, e a herança duplicaria o `C-3`. Absorvido pelo consultor no card (contingência 1) e em `DEB-6`. Régua de autoria (`EBK-T10`): contingência que copia um valor de fixture confere se a fixture carrega aquele valor de propósito. **Rota:** resolve — absorvido pelo consultor no card da `EBK-T1` (`DEB-6`).
- **AE-2** (`EBK-T5`, laudo `ressalva` 91%, 2026-09-25) — quatro achados de processo. (1) O objetivo prometeu o número de defeitos em `kit_check: check-drift FALHOU` e em `kit_check: FALHOU`, e o card só prescreveu o README: os dois ramos do `materializar.py` seguem contando a linha de sumário dele (medido: 13 problemas para 12 defeitos no `check-drift` de uma cópia do kit; 2 para 1 no `validate` com uma entrada do manifesto apontando arquivo ausente). (2) As linhas de detalhe do README saem com o marcador de item, e a lista tem mais itens que o número do cabeçalho. (3) O `review_evidence.py` com `--desde` lista como "sem atribuição" os não rastreados anteriores ao commit do despacho (19 na `EBK-T5`). (4) O `rdo.py laudo` não tem campo para o motivo de dimensão fora de `conforme`, e o alvo `dossiê` que o `pantonic-reviewer` grafa é recusado pelo gerador, que só aceita `dossie`. Destino (`DEB-9`): (1) e (2) no corretivo `EBK-T5a`; (3) no `TK-84`; (4) no `TK-85`, os dois com card no diário. Régua de autoria (`EBK-T10`): objetivo que nomeia mais de um caso tem um caso prescrito e testado para cada um; card de instrumento que conta problema confere de onde vem cada linha contada. **Rota:** corretivo `EBK-T5a` para (1) e (2); tíquetes `TK-84` para (3) e `TK-85` para (4) (`DEB-9`).
- **AE-5** (`EBK-T13`, laudo `aprovado` 100% com recomendação `escalar`, 2026-09-26; regra `A8a`/`B1`) — A regra 'Rodada de replanejamento abre instância fria do planejador', que o EBK-T13 pôs na GOVERNANCA.md §3 como o card mandava, se apoia numa comparação de médias sem normalizar pelo volume. Normalizada por mensagem, a comparação se inverte em 5 das 6 retomadas. A triagem do consultor decide se a regra fica ou se abre tíquete para medir de novo. Destino (`DEB-12`): a regra fica, e a razão dela passa ao custo de partida no corretivo `EBK-T13a`. Régua de autoria (`EBK-T10`): função de desfecho que compara custo de segmentos normaliza pelo que as opções têm de diferente, e não pelo volume de trabalho da rodada. **Rota:** corretivo `EBK-T13a` (`DEB-12`).
- **AE-6** (fechamento do plano, condutor, 2026-09-26) — (1) `python .claude/tools/backlog.py check --repo <cópia da fixture verde>` sai exit 1 com `C-17 GOVERNANCA.md:1 — piso_c11 nomeia entrada órfã: `GOVERNANCA.md` §1.1`: o subcomando `check` liga `piso_c11=_PISO_C11` para qualquer `--repo`, e toda entrada do piso deste repositório sai órfã em outro corpus (efeito provável nos kits derivados). (2) `backlog.py next`/`show` do `EBK-T14`, último card antes da `## 6`, imprimiu como dossiê também as seções `## 6`, `## 7` e `## 8` do plano. Destino (`DEB-13`, consultor, acionamento 8): (1) no `TK-86`, (2) no `TK-87`, os dois com card `ready` no diário. Régua de autoria: dado medido num corpus (piso, lista de dívida) não mora em constante de instrumento que vai a outro corpus; e a fronteira de um card na leitura do instrumento é a mesma que o autor vê, o cabeçalho seguinte do plano. **Rota:** tíquetes `TK-86` para (1) e `TK-87` para (2) (`DEB-13`).

## Consumo (`docs/telemetria.tsv`)

| papel | linhas | tool uses | mil tokens |
|---|---|---|---|
| executor | 22 | 504 | 1771.3 |
| revisor | 16 | 289 | 1362.2 |
| consultor | 8 | 292 | 663.8 |
| outros | 0 | 0 | 0.0 |
| **total** | 46 | 1085 | 3797.3 |

## Violações do `check` no fechamento

(nenhuma)

# Histórico

Agente executor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai executar: `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo
Agente executor devolveu a tarefa "O `check` acusa tíquete vivo sem card": blocked — motivo premissa:: contingência do card ("se um teste existente ficar vermelho só por causa do C-15... acrescentar... subtarefa mínima... com o mesmo status do tíquete; se, com isso, outra asserção do mesmo teste mudar de resultado → parar") se confirma em test_tf_check_vermelho_dispara_cada_codigo_uma_vez — TK-2 da fixture vermelho tem status `backlog` (fora do vocabulário, já gera C-3); a subtarefa TK-2a prescrita herdando "o mesmo status do tíquete" duplicaria C-3 (agora em TK-2 e TK-2a), mudando o resultado da asserção `sorted(codigos) == sorted(esperados)` além do C-15 sozinho — nomeando o teste conforme a cláusula..
Agente consultor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai triar.
Agente consultor devolveu a tarefa "O `check` acusa tíquete vivo sem card": rota resolve.
Agente executor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai executar: `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo
Agente executor devolveu a tarefa "O `check` acusa tíquete vivo sem card": review — sem pendência.
Agente revisor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O `check` acusa tíquete vivo sem card": aprovado 100%, bloqueante nenhuma.
Agente executor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai executar: `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo
Agente executor devolveu a tarefa "O `check` acusa tíquete vivo sem card": blocked — motivo premissa: defeito=decisao: "C-17 para toda entrada de `_PISO_C11` que não casa nenhuma ocorrência de citação quebrada no corpus corrente" exige escolher se C-17 vale só para o repo real ou para todo `repo` passado a `check()` — escolha que o card não fecha; a leitura genérica (única compatível com o texto do card, já que `_PISO_C11` é constante de módulo aplicada uniformemente a qualquer `repo`) quebra `test_tf_san_7_pasta_check_verde` e `test_tf_san_20_c10_projeto_novo_sem_plano` em `tests/test_backlog.py` (fixture `pasta`: zero ocorrências de `§` ou `GOVERNANCA` em todo o diretório, confirmado por grep — logo toda entrada viva de `_PISO_C11` sairia órfã nesse corpus e ambos os testes, que hoje afirmam `violacoes == []` com `repo=repo`, passariam a falhar), violando o piso de regressão da Verificação 4 ("nenhuma falha; passed ≥ o do despacho mais os testes novos")..
Agente consultor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai triar.
Agente consultor devolveu a tarefa "O `check` acusa tíquete vivo sem card": rota resolve.
Agente executor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai executar: `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo
Agente executor devolveu a tarefa "O `check` acusa tíquete vivo sem card": review — sem pendência.
Agente revisor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O `check` acusa tíquete vivo sem card": aprovado 100%, bloqueante nenhuma.
Agente executor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai executar: `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo
Agente executor devolveu a tarefa "O `check` acusa tíquete vivo sem card": review — sem pendência.
Agente revisor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O `check` acusa tíquete vivo sem card": aprovado 100%, bloqueante nenhuma.
Agente executor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai executar: `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo
Agente executor devolveu a tarefa "O `check` acusa tíquete vivo sem card": blocked — motivo premissa: defeito=ambiguidade: contingência "se um teste existente de close falhar porque a tarefa da fixture não está `done` → mudar só a linha de status dessa tarefa na fixture para `done`" pressupõe uma linha de Status já existente na fixture, mas ~20 dos 23 testes de `close` usam `--tarefa T7`/`T8a` de `docs/plans/P-0734-execucao-autonoma.md` (`_PLANO_REAL`), plano sem nenhuma linha `- **Status:**` para tarefa alguma e fora do `Arquivos-alvo` do card (que só autoriza tocar `tests/fixtures/`) — exige de mim decidir entre adicionar Status a um plano fora de escopo, trocar a tarefa-fixture real por outra com conteúdo compatível às asserções (`"provar o padrão"`, `"cria \`.claude/tools/telemetria.py\`"` etc.) ou tratar status ausente como não-bloqueante, nenhuma delas resolvida pelo card..
Agente consultor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai triar.
Agente consultor devolveu a tarefa "O `check` acusa tíquete vivo sem card": rota resolve.
Agente executor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai executar: `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo
Agente executor devolveu a tarefa "O `check` acusa tíquete vivo sem card": review — sem pendência.
Agente revisor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O `check` acusa tíquete vivo sem card": aprovado 100%, bloqueante nenhuma.
Agente executor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai executar: `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo
Agente executor devolveu a tarefa "O `check` acusa tíquete vivo sem card": review — sem pendência.
Agente revisor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O `check` acusa tíquete vivo sem card": ressalva 91%, bloqueante nenhuma.
Agente consultor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai triar.
Agente consultor devolveu a tarefa "O `check` acusa tíquete vivo sem card": rota resolve.
Agente executor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai executar: `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo
Agente executor devolveu a tarefa "O `check` acusa tíquete vivo sem card": review — sem pendência.
Agente revisor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O `check` acusa tíquete vivo sem card": aprovado 100%, bloqueante nenhuma.
Agente executor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai executar: `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo
Agente executor devolveu a tarefa "O `check` acusa tíquete vivo sem card": review — sem pendência.
Agente revisor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O `check` acusa tíquete vivo sem card": aprovado 100%, bloqueante nenhuma.
Agente executor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai executar: `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo
Agente executor devolveu a tarefa "O `check` acusa tíquete vivo sem card": review — sem pendência.
Agente revisor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O `check` acusa tíquete vivo sem card": aprovado 100%, bloqueante nenhuma.
Agente executor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai executar: `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo
Agente executor devolveu a tarefa "O `check` acusa tíquete vivo sem card": review — sem pendência.
Agente revisor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O `check` acusa tíquete vivo sem card": aprovado 100%, bloqueante nenhuma.
Agente executor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai executar: `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo
Agente executor devolveu a tarefa "O `check` acusa tíquete vivo sem card": review — sem pendência.
Agente revisor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O `check` acusa tíquete vivo sem card": aprovado 100%, bloqueante nenhuma.
Agente executor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai executar: `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo
Agente executor devolveu a tarefa "O `check` acusa tíquete vivo sem card": review — sem pendência.
Agente revisor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O `check` acusa tíquete vivo sem card": aprovado 100%, bloqueante nenhuma.
Agente executor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai executar: `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo
Agente executor devolveu a tarefa "O `check` acusa tíquete vivo sem card": review — sem pendência.
Agente revisor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O `check` acusa tíquete vivo sem card": aprovado 100%, bloqueante nenhuma.
Agente executor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai executar: `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo
Agente executor devolveu a tarefa "O `check` acusa tíquete vivo sem card": blocked — motivo premissa: Verificação 7 falhou: Texto novo 5 (linha nova do hook) mudou o tamanho do systemMessage e quebrou tests/test_materializar.py:614 (assert len(...) == 470, obtido 510), teste não citado nem tratado pelo card..
Agente consultor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai triar.
Agente consultor devolveu a tarefa "O `check` acusa tíquete vivo sem card": rota resolve.
Agente executor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai executar: `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo
Agente executor devolveu a tarefa "O `check` acusa tíquete vivo sem card": review — sem pendência.
Agente revisor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O `check` acusa tíquete vivo sem card": aprovado 100%, bloqueante nenhuma.
Agente executor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai executar: `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo
Agente executor devolveu a tarefa "O `check` acusa tíquete vivo sem card": blocked — motivo premissa: defeito=ambiguidade: "cada trecho do .jsonl que começa numa mensagem do tipo user vinda de fora do agente (a invocação ou uma retomada por mensagem) e vai até a próxima" exige decidir, para os 2 agentes do corpus (passo 1: agentType=pantonic-planner + `P-0747` na 1ª linha do .jsonl irmão), o tratamento de entradas type=user/content-string com `isMeta=true` que aparecem logo após a real invocação (ex.: linhas 0 e 1 de `agent-a19e1fec74025c07a.jsonl` e de `agent-a332b22b3e70b5799.jsonl`) — campo que o método não menciona; tratá-las como início de segmento (retomada) ou como parte do segmento anterior (ignoradas) são as duas leituras não fechadas pelo card, e cada uma muda o agrupamento fria/retomada e portanto a média que decide entre Texto A e Texto B no passo 5 — na leitura literal (toda entrada conta), a "fria" fica com custo $0,00 nos dois agentes porque o `isMeta` consome sozinho o primeiro segmento.
Agente consultor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai triar.
Agente consultor devolveu a tarefa "O `check` acusa tíquete vivo sem card": rota resolve.
Agente executor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai executar: `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo
Agente executor devolveu a tarefa "O `check` acusa tíquete vivo sem card": review — sem pendência.
Agente revisor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O `check` acusa tíquete vivo sem card": aprovado 100%, bloqueante nenhuma.
Agente consultor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai triar.
Agente consultor devolveu a tarefa "O `check` acusa tíquete vivo sem card": rota resolve.
Agente executor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai executar: `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo
Agente executor devolveu a tarefa "O `check` acusa tíquete vivo sem card": review — sem pendência.
Agente revisor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O `check` acusa tíquete vivo sem card": aprovado 100%, bloqueante nenhuma.
Agente executor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai executar: `python .claude/tools/backlog.py check` passa a emitir a violação `C-15` para todo
Agente executor devolveu a tarefa "O `check` acusa tíquete vivo sem card": review — sem pendência.
Agente revisor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O `check` acusa tíquete vivo sem card": aprovado 100%, bloqueante nenhuma.
Agente consultor recebe a tarefa "O `check` acusa tíquete vivo sem card" e vai triar.
Agente consultor devolveu a tarefa "O `check` acusa tíquete vivo sem card": rota resolve.
