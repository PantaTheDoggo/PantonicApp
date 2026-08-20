# RDO — P-0734 · T13

**Plano:** `docs/plans/P-0734-execucao-autonoma.md`
**Tarefa:** `T13` — Proxy de ocupação de contexto
**Modelo:** Sonnet · **Classe:** implementacao · **Teto:** 40
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** dar ao scrum-master um sinal de "a janela está acabando" que ele consiga enxergar — já que a ocupação real não lhe é observável (§2, item 3).

**Arquivos-alvo:** conforme o veredito da `T1` — hook em `settings.json` mais script de medição em `.claude/tools/`, ou, se o evento necessário não existir, o contador calibrado dentro da skill `scrum-master`, mais teste.

**Verificação:** bateria do §3; teste do cálculo do limiar.

**Pronto quando:** o loop tem um critério de encerramento de janela que ele próprio consegue avaliar, seja qual for o mecanismo.

**Dossiê fechado por:** `T1` sonda 3.

**Extras (rótulos livres do plano, verbatim):**

- **Conteúdo:** limiar declarado em número; aviso injetado no contexto do orquestrador quando cruzado; comportamento do scrum-master ao recebê-lo (encerrar a tarefa corrente, arquivar, preparar o handover de janela e parar).
- **Resultado negativo é resultado:** se a `T1` derrubar a viabilidade do hook, a tarefa entrega o contador calibrado pela série de `docs/telemetria.tsv` **e** registra a inviabilidade com a evidência — não fica em aberto nem finge que o proxy existe.

## Execução

**Consumo:** 35 tool uses contra o teto 40, 131 k tokens, 15599 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: TK-43 (achado de processo, alvo dossie): os dossies de T13 e T14 nomeiam .claude/settings.json como residencia do hook, e .gitignore:3 declara esse arquivo "nunca canonica" — o proxy entregue funciona so no hub e nao viaja para consumidor nenhum, nem kit_check o ve; decisao do dono sobre residencia versionada de hook e requisito de arquitetura de distribuicao, invalida a rota do dossie da T14 e precede a T14.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

Achado 1 (alvo doutrina/instrumento, rota: tiquete novo) — o dossie de evidencia mecanica desta revisao nasceu inoperante para escopo: leu "Arquivos-alvo declarados: .claude/tools/" como caminho literal ("sem diferenca coletavel — arquivo ausente na arvore de trabalho") e listou como "tocados" os 59 arquivos de toda a arvore nao commitada do P-0734, produzindo "59 arquivos fora dos alvos" que nada tem com esta tarefa. Com a iniciativa inteira sem commit, review_evidence.py nao consegue atribuir diff a tarefa, e a camada declarada autoridade sobre escopo fica sem poder discriminante; o conjunto real (ocupacao.py, test_ocupacao.py, settings.json, GOVERNANCA.md, scrum-master/SKILL.md, diario, telemetria) teve de ser reconstruido pelo reviewer fora do dossie. Achado 2 (alvo dossie, rota: item de replanejamento) — o campo Arquivos-alvo do "### T13" nao nomeia .claude/skills/scrum-master/SKILL.md nem GOVERNANCA.md 4.3, embora o campo Conteudo exija justamente o comportamento do scrum-master ao receber o aviso; a entrega tocou as duas superficies por consequencia obrigatoria (G-SURFACE) e nao por dispersao — marcacao de escopo julgada contra o Conteudo, sem punir a execucao pelo campo incompleto (RUBRICA 6, invariante 1). Observacao de metodo — o ramo A (hook PreToolUse com hookSpecificOutput.additionalContext) foi provado ao vivo com sonda descartavel e revertida antes de virar entrega, e o instrumento se validou em producao no mesmo dia ao encerrar a janela do proprio orquestrador; a limitacao que o executor registrou como inferida (agent_type ausente na sessao principal) ficou remediada por esse disparo. Consumo medido da serie: 35 turnos (informacao de agregado, nao nota).

## Fechamento

**Desdobramento:** aprovado
