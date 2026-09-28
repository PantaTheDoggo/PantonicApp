# RDO — P-0753 · AF-T6

# Humano

Tarefa "A recomendação do laudo viaja na primeira linha do revisor" concluída em 2026-09-27.
A recomendação do revisor passa a chegar na primeira linha do retorno dele, e o painel do gerente a mostra.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria de encerramento do estágio 1: as dezoito recomendações e os dois tíquetes do consultor": 6/21 tarefas concluídas; próxima: "A conferência do card lê a situação da tarefa no estado do plano em pasta".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achado registrado no plano, com rota: 1 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/plans/P-0753-auditoria-estagio-1/plano.md`
**Tarefa:** `AF-T6` — A recomendação do laudo viaja na primeira linha do revisor
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O revisor passa a devolver a recomendação do laudo na primeira linha, na forma que o painel, o fechamento e as instruções do gerente leem no mesmo ato.

**Arquivos-alvo:** - `.claude/agents/pantonic-reviewer.md` - `.claude/skills/scrum-master/SKILL.md` - `.claude/tools/progresso_hook.py` - `tests/test_progresso_hook.py`

**Verificação:** 1. `python -m pytest tests/test_progresso_hook.py -q -k "recomendacao"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado) 2. `python -c "from pathlib import Path;print(sum(Path(p).read_text(encoding='utf-8').count('recomendacao=<') for p in ['.claude/agents/pantonic-reviewer.md','.claude/skills/scrum-master/SKILL.md']))"` → `2` — antes `0`, depois `2` (esperado, não ensaiado) 3. `python -c "from pathlib import Path;t=sum(Path(p).read_text(encoding='utf-8').count('recomendação <recomendação>') for p in ['.claude/tools/progresso_hook.py','.claude/skills/scrum-master/SKILL.md']);print(t)"` → `2` — antes `0`, depois `2` (esperado, não ensaiado) 4. `python -m pytest tests/test_encerrar.py -q -k "tarefa_fecha_num_ato"` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava: o fechamento já transcreve `**Recomendação:**` do laudo) 5. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava) 6. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)

**Pronto quando:** - linha de retorno do revisor.recomendação do laudo — presente na primeira linha e lida, na mesma forma, pelo painel, pelo fechamento e pelas instruções do gerente — Verificações 1 a 4

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAF-19`, `DAF-26`, `DAF-38`, `F-18`, `F-28`.
- **Depende de:** `AF-T3`, `AF-T5`
- **Operação do modelo:** `OP-6` - OP-6: O revisor passa a devolver a recomendação do laudo na primeira linha, na forma que o painel, o fechamento e as instruções do gerente leem no mesmo ato. - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; painel do gerente — Quem implementa faz o painel reconhecer o programa chamado mesmo quando a chamada traz opções do interpretador antes dele.; fechamento de tarefa — Quem implementa faz o fechamento copiar cada achado de processo do laudo para os achados do plano, com a rota, sem repetir achado igual.
- **Camada e fronteira:** texto do agente revisor, instruções do gerente (skill `scrum-master`) e gancho do painel (`.claude/tools/progresso_hook.py`, falha aberta). O fechamento (`encerrar.py`) já lê a recomendação do laudo (`**Recomendação:**`) e não muda (`F-28`): os literais `bloqueante=` em `encerrar.py` e `rdo.py` são argumentos nomeados de função, não a linha do revisor.
- **Contratos/classes:** linha nova do revisor: `<tarefa> <veredito> <percentual> bloqueante=<dimensão|nenhuma> recomendacao=<seguir|seguir com ressalva|refazer|escalar>`. Regex da volta do revisor no painel: `^(\S+) (\S+) (\d+)%? bloqueante=(\S+)(?: recomendacao=(.+))?$`. Frase `M-7`: `Agente revisor devolveu a tarefa "<título>": <veredito> <percentual>%, bloqueante <bloqueante>, recomendação <recomendação>.`, com `<recomendação>` ← grupo 5, e `não informada` quando a linha vem sem o campo. `test_tf_ger_18_residencia` confere `FRASES` contra a tabela de frases da skill: as duas mudam juntas.
- **Passos:** 1. Em `.claude/agents/pantonic-reviewer.md`, passo 7 (*Retorno ao chamador*), a primeira linha do bloco das duas linhas fixas vira a linha nova de `Contratos/classes` (mesmo recuo de três espaços). 2. Em `.claude/skills/scrum-master/SKILL.md`, Passo 7: a linha de entrada `` `<tarefa> <veredito> <percentual> bloqueante=<dimensão|nenhuma>` `` vira a linha nova de `Contratos/classes`, entre crases; e as três linhas depois de `antigo:` viram as quatro depois de `novo:` (as quebras são as do bloco; os rótulos não entram no arquivo): ```text antigo: - **Ação:** ler `veredito` ∈ {`aprovado`, `ressalva`, `reprovado`}, `bloqueante` e o caminho do laudo — calculados pelo gerador, não recalculados pelo loop. Colher a `recomendação` **do laudo**, campo fechado (`seguir`, `seguir com ressalva`, `refazer`, `escalar`), lido por `A6`, novo: - **Ação:** ler `veredito` ∈ {`aprovado`, `ressalva`, `reprovado`}, `bloqueante`, `recomendacao` e o caminho do laudo — calculados pelo gerador e transcritos pelo revisor, não recalculados pelo loop. A `recomendação` vem **da primeira linha**, campo fechado (`seguir`, `seguir com ressalva`, `refazer`, `escalar`), lido por `A6`, ``` 3. Na tabela de frases da skill, linha `M-7`: o regex vira o de `Contratos/classes`, a frase vira a de `Contratos/classes` e a última célula passa a `` `<veredito>` ← grupo 2; `<percentual>` ← grupo 3; `<bloqueante>` ← grupo 4; `<recomendação>` ← grupo 5, ou `não informada` sem o campo ``. 4. Em `progresso_hook.py`: `FRASES['M-7']` vira a frase nova; o `re.match` da volta do `pantonic-reviewer` vira o regex novo, e o dicionário da frase ganha `"<recomendação>"`. 5. Escrever os dois testes da seção `Testes`.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 2 testes novos (referência datada: `452 passed`, 2026-09-27). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0 (o texto do agente muda no corpo, não no frontmatter). - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
- **Não fazer:** não tocar `encerrar.py` nem `rdo.py`; não mudar o frontmatter do agente; não mudar outra frase do painel; não renomear o campo para `recomendação` com acento na linha (a linha é de máquina, ASCII).
- **Contingências:** - se `test_tf_ger_7_agente_de_volta_revisor` cair só porque a frase ganhou `, recomendação não informada` → atualizar as duas asserções dele para a frase nova com `não informada` e seguir. - se `test_tf_ger_19_userpromptsubmit_sem_volta_pendente` e `test_tf_ger_25_show_no_meio_da_janela_nao_encerra` caírem pelo mesmo motivo (`DAF-38`) → em `tests/test_progresso_hook.py`, o literal `aprovado 100%, bloqueante nenhuma.'` (2 ocorrências no arquivo, uma em cada teste) passa a `aprovado 100%, bloqueante nenhuma, recomendação não informada.'` e seguir. - se outro teste existente cair, fora desses três → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_m7_revisor_com_recomendacao` — volta `TLG-T9 ressalva 91 bloqueante=nenhuma recomendacao=seguir com ressalva` gera `Agente revisor devolveu a tarefa "Um título de teste": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.` (com o regex antigo o grupo 4 engoliria `nenhuma recomendacao=seguir com ressalva`). TR `test_tr_m7_revisor_sem_recomendacao_diz_nao_informada` — volta `TLG-T9 aprovado 100 bloqueante=nenhuma` gera a frase com `recomendação não informada`.
- **Fora do escopo desta tarefa:** o verbo que despacha a tarefa (`AF-T10`).
- **Handover:** 2026-09-27 · para quem vier depois - **Entregue:** linha do revisor com recomendacao= (.claude/agents/pantonic-reviewer.md passo 7); scrum-master Passo 7 le a recomendacao da primeira linha e a linha M-7 da tabela; progresso_hook.py:224 casa o campo e a frase M-7 o mostra ('nao informada' sem ele); testes em tests/test_progresso_hook.py:310 e :326 - **Contrato:** o revisor devolve '<tarefa> <veredito> <percentual> bloqueante=<...> recomendacao=<...>'; o loop le a recomendacao dali, sem abrir o laudo - **Não refazer:** o campo recomendacao na primeira linha do revisor e no painel - **Pendente:** nenhum

## Execução

**Consumo:** 33 tool uses, 74.5 k tokens, 340.1 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

O primeiro despacho parou blocked/premissa porque a contingencia do card contou as ocorrencias da frase antiga do M-7 num teste so, e havia mais dois (ger_19, ger_25); o reparo DAF-38 fechou a contagem e o redespacho seguiu sem decisao nova. Contingencia que troca um literal em testes rende mais quando o autor do card conta as ocorrencias do literal antigo na suite inteira, com grep, no ato da autoria.

## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master vai marcar a tarefa "A recomendação do laudo viaja na primeira linha do revisor" como blocked, sem RDO.
Scrum master vai fechar a tarefa "A recomendação do laudo viaja na primeira linha do revisor" como done: registrar estado, RDO e telemetria.
