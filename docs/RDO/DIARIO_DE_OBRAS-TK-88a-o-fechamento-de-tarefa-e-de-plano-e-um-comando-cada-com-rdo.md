# RDO — DIARIO_DE_OBRAS · TK-88a

# Humano

Tarefa "O fechamento de tarefa e de plano é um comando cada, com RDO e entrega em três seções e handover no card" concluída em 2026-09-26.
Revisão: aprovada com ressalva (85%); pendência do laudo: Defeito desta entrega no painel do gerente, medido em uso real hoje: progresso_hook.py:291-299 pega o primeiro '--tarefa' da linha inteira e casa 'encerrar.py plano' em texto de argumento - 14 linhas M-10 com '<ID>-revisao' no lugar do titulo (telemetria.py append encadeado antes do encerrar), 13 M-11 herdando o id errado e copiadas para o '# Historico' de 12 RDO, e 2 M-18 'vai fechar o plano' do P-0752 sem fechamento; correcao imediata: card corretivo que amarra --tarefa/--plano a propria invocacao do encerrar.py, com TR dos dois casos, e que passa o '**Plano:**' do RDO pelo mesmo _rel do verbo plano (encerrar.py:454 grava barra invertida em 16 RDO). O fechamento desta propria tarefa sera recusado pelo encerrar.py: nao ha linha medida de TK-88a na serie (executada na sessao principal) - a triagem decide o desfecho do consumo antes..
Pendência para o dono: nenhuma.
Tíquete "O encerramento de tarefa e de plano vira um comando, com relatório em três seções e handover no card": 2/4 tarefas concluídas; próxima: "O painel lê cada argumento da própria invocação, e o RDO publicado diz o plano e a tarefa certos".
Achados registrados no plano, com rota: 3 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-88a` — O fechamento de tarefa e de plano é um comando cada, com RDO e entrega em três seções e handover no card
**Modelo:** Opus · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `python .claude/tools/encerrar.py tarefa --plano <plano> --tarefa <ID> [--resumo] [--pendencia] [--achado TEXTO ROTA]... [--tool-uses --tokens-k --duracao-s]` leva a tarefa de `review` a `done` num ato só — gate do modelo, `backlog.transacionar_status` com a nota de fechamento, `rdo.cmd_close` com o pacote **transcrito do laudo** e as seções `# Humano`/`# Histórico` preenchidas, linha de telemetria (da série ou do trio do `<usage>`), `AE-<n>` com `**Rota:**` por achado —, e `python .claude/tools/encerrar.py plano --plano <plano> --veredito "<frase do dono>"` leva o plano a `done` — só sem tarefa aberta, com RDO de toda tarefa `done`, achado sem rota nenhum e documento de validação presente —, escreve `entrega.md`/`docs/plans/_ENTREGA-<id>.md` nas três seções e uma linha no cabeçalho do diário. Ambos recusam sem escrever quando falta insumo. O terceiro verbo, `python .claude/tools/encerrar.py handover --plano <plano> --tarefa <ID> --entregue "…" --contrato "…" [--nao-refazer] [--pendente] [--para <ID>]...`, escreve ou substitui o campo `- **Handover:**` no card (status `in-progress`/`review`/`done`/`blocked`), e `backlog.py next` imprime, sob `=== HANDOVER DE <ID>`, o handover de todo irmão que nomeia a próxima tarefa em `para` ou, sem nenhum, o da antecessora imediata.

**Arquivos-alvo:** - `.claude/tools/encerrar.py` (novo) - `.claude/tools/rdo.py` — `cmd_close` ganha `HUMANO`/`HISTORICO` (`--humano`, `--historico`) - `.claude/tools/rdo_template.md` — as três seções `# Humano` / `# Máquina` / `# Histórico` - `.claude/tools/backlog.py` — `transacionar_status`: plano → `done` com toda tarefa terminal; `extrair_handover`/`handovers_para` e o bloco `=== HANDOVER DE` em `renderizar_next` - `.claude/tools/caminhos.py` — `destino_operacoes`, `destino_entrega` - `.claude/tools/progresso_hook.py` — detecção de `encerrar.py tarefa` (`M-10`) e `M-18` - `GOVERNANCA.md` §4.2 (*Fronteira de registro*, *Fechamento enxuto*); `README.md` §9 e §11 - `.claude/skills/diario-de-obras/SKILL.md` (transição de plano, operação 7); `.claude/skills/passagem-de-bastao/SKILL.md` (Parte 3, itens 2-3); `.claude/skills/scrum-master/SKILL.md` (Passo 9, fechamento do plano, repertório `M-10`/`M-18`) - `tests/test_encerrar.py` (novo); `tests/test_rdo.py`, `tests/test_backlog.py`, `tests/test_progresso_hook.py`

**Verificação:** 1. `python -m pytest tests/test_encerrar.py tests/test_rdo.py tests/test_backlog.py tests/test_progresso_hook.py tests/test_caminhos.py -q` → verde. 2. `python .claude/tools/backlog.py check` → `check: OK — nenhuma violação.`, exit `0`. 3. `python -m pytest -q` → nenhuma falha; `passed` ≥ 376 + os testes novos.

**Pronto quando:** os dois verbos fecham tarefa e plano num comando cada, com as três seções, recusando sem escrever quando falta insumo, e as residências da doutrina (GOVERNANCA §4.2, as três skills, README) descrevem o instrumento como a forma canônica.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Testes:** TF `tests/test_encerrar.py` — fechamento de tarefa escreve status, RDO em três seções (humano com título e revisão em palavras; máquina com pacote do laudo e consumo da série; histórico só com as linhas do título) e achado com rota; consumo por argumento apensa a série; fechamento de plano escreve status, entrega em três seções e linha do diário. TR — cada checagem recusa sem escrever (status ≠ `review`, laudo ausente, `reprovado`, consumo ausente; tarefa aberta, sem documento de validação, achado sem rota, `done` sem RDO). TF handover em `test_encerrar.py` (campo no card antes de `Notas`, substituição, transcrição no RDO; recusa em `ready`) e em `test_backlog.py` (`next` devolve o da antecessora; o endereçado em `para` vence). TF/TR em `test_backlog.py` (plano `ready → done`), `test_rdo.py` (três seções e mínimo honesto), `test_progresso_hook.py` (`M-10` pelo instrumento, `M-18`).
- **Não fazer:** não reimplementar regra de `backlog.py`/`rdo.py`/`telemetria.py` dentro do `encerrar.py`; não inventar número de consumo; não apagar o laudo.
- **Notas de execução:** - 2026-09-26 `review` — entrega na árvore; o próprio card se fecha por `python .claude/tools/encerrar.py tarefa --plano docs/DIARIO_DE_OBRAS.md --tarefa TK-88a --laudo <laudo>` depois do laudo do revisor. - 2026-09-26 `review` — laudo `ressalva 85`, bloqueante nenhuma, recomendação `escalar` (`docs/RDO/laudos/DIARIO_DE_OBRAS-TK-88a.md`); triagem do consultor em `CT-1`..`CT-4` do `## TK-88`. **Não fechar antes do `done` da `TK-88b`:** a única linha medida desta tarefa na série é a rodada do revisor (`CT-2`), e o `encerrar.py` de hoje a tomaria como consumo do executor. Depois dela, o condutor fecha esta tarefa com o comando abaixo, sozinho na linha de comando (`CT-1`); o laudo é o padrão (`docs/RDO/laudos/DIARIO_DE_OBRAS-TK-88a.md`): - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-88a-o-fechamento-de-tarefa-e-de-plano-e-um-comando-cada-com-rdo.md`, veredito ressalva 85% ``` python .claude/tools/encerrar.py tarefa --plano docs/DIARIO_DE_OBRAS.md --tarefa TK-88a --nao-medido "executada na sessão principal, fora do loop: sem SubagentStop nem bloco de uso" --achado "painel do gerente: o gancho lê o argumento de tarefa e de plano na linha de comando inteira, e o RDO grava o caminho do plano com barra invertida" "TK-88c" --achado "tarefa executada fora do loop: evidência sem ponto de partida e fechamento sem medida" "TK-88b" --achado "pré-checagens de rdo e backlog copiadas no instrumento de fechamento" "TK-88d" ```

## Execução

**Consumo:** não medido — executada na sessão principal, fora do loop: sem SubagentStop nem bloco de uso

**Pendência para o dono:** laudo: Defeito desta entrega no painel do gerente, medido em uso real hoje: progresso_hook.py:291-299 pega o primeiro '--tarefa' da linha inteira e casa 'encerrar.py plano' em texto de argumento - 14 linhas M-10 com '<ID>-revisao' no lugar do titulo (telemetria.py append encadeado antes do encerrar), 13 M-11 herdando o id errado e copiadas para o '# Historico' de 12 RDO, e 2 M-18 'vai fechar o plano' do P-0752 sem fechamento; correcao imediata: card corretivo que amarra --tarefa/--plano a propria invocacao do encerrar.py, com TR dos dois casos, e que passa o '**Plano:**' do RDO pelo mesmo _rel do verbo plano (encerrar.py:454 grava barra invertida em 16 RDO). O fechamento desta propria tarefa sera recusado pelo encerrar.py: nao ha linha medida de TK-88a na serie (executada na sessao principal) - a triagem decide o desfecho do consumo antes.

## Laudo

**Veredito:** ressalva

**Percentual:** 85%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

Motivo do parcial em testes: o card declara TF/TR para test_progresso_hook.py (M-10 pelo instrumento, M-18) e so ha o TF (test_tf_tk88_encerrar_tarefa_gera_m10_e_encerrar_plano_gera_m18), com o comando isolado; o TR que discriminaria comando encadeado e literal em argumento nao existe, e e exatamente onde o defeito escalado vive (reproduzido com progresso_hook.evento sobre 'telemetria.py append --tarefa FPU-T8-revisao ...; encerrar.py tarefa --tarefa FPU-T8' -> titulo 'FPU-T8-revisao'). Motivo do parcial em registro: Medida do executor ausente (verificacao nao registrada pela execucao; as notas do card e do TK-88 parafraseiam a entrega sem exit code) e nenhuma linha de TK-88a em docs/telemetria.tsv. Re-medido na revisao: Verificacao 1 exit 0 (230 passed), 2 'check: OK' exit 0, 3 exit 0 (420 passed >= 376 + novos). Exercicio ponta a ponta: 16 fechamentos reais de hoje (15 RDO do P-0752 e o do TK-91a) com as tres secoes, handover no card e handovers_para devolvendo FPU-T9/FPU-T9a para FPU-T10 e FPU-T4a para FPU-T7; em copia de fixture de plano em pasta, handover -> tarefa -> plano fecharam (estado.tsv done, rdo/GAM-T1.md, entrega.md, linha FECHADO no diario) e o plano recusou sem operacoes.md. Divergencias menores do modulo, para o mesmo card corretivo: a linha FECHADO conta 1/2 com cancelada enquanto o indice logo abaixo diz done 1/1; stdout 'tarefa fechado'.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Tarefa "O fechamento de tarefa e de plano é um comando cada, com RDO e entrega em três seções e handover no card": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O fechamento de tarefa e de plano é um comando cada, com RDO e entrega em três seções e handover no card" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O fechamento de tarefa e de plano é um comando cada, com RDO e entrega em três seções e handover no card": ressalva 85%, bloqueante nenhuma.
Agente consultor recebe a tarefa "O fechamento de tarefa e de plano é um comando cada, com RDO e entrega em três seções e handover no card" e vai triar.
Agente consultor devolveu a tarefa "O fechamento de tarefa e de plano é um comando cada, com RDO e entrega em três seções e handover no card": rota resolve.
Scrum master vai fechar a tarefa "O fechamento de tarefa e de plano é um comando cada, com RDO e entrega em três seções e handover no card" como done: registrar estado, RDO e telemetria.
