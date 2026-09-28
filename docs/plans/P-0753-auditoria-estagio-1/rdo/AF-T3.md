# RDO — P-0753 · AF-T3

# Humano

Tarefa "O painel do gerente reconhece o programa depois das opções do interpretador" concluída em 2026-09-27.
O painel do gerente reconhece o programa chamado mesmo quando o Python recebe opções como -X utf8 antes dele.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria de encerramento do estágio 1: as dezoito recomendações e os dois tíquetes do consultor": 3/21 tarefas concluídas; próxima: "O fechamento transcreve o achado de processo do laudo para os achados do plano".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0753-auditoria-estagio-1/plano.md`
**Tarefa:** `AF-T3` — O painel do gerente reconhece o programa depois das opções do interpretador
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O painel do gerente passa a reconhecer o programa chamado quando a chamada traz opções do interpretador antes dele.

**Arquivos-alvo:** - `.claude/tools/progresso_hook.py` - `tests/test_progresso_hook.py` - `docs/ARMADILHAS_DE_FERRAMENTA.md`

**Verificação:** 1. `python -m pytest tests/test_progresso_hook.py -q -k "opcao_do_interpretador"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado) 2. `python -c "import importlib.util as u;from pathlib import Path;s=u.spec_from_file_location('p',Path('.claude/tools/progresso_hook.py'));m=u.module_from_spec(s);s.loader.exec_module(m);print(m._programa(['python','-X','utf8','.claude/tools/backlog.py','status'])[0])"` → `backlog.py` — antes `utf8`, depois `backlog.py` (esperado, não ensaiado) 3. `python -c "from pathlib import Path;print(Path('docs/ARMADILHAS_DE_FERRAMENTA.md').read_text(encoding='utf-8').count('progresso_hook._programa'))"` → `1` — antes `0`, depois `1` (esperado, não ensaiado) 4. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava) 5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)

**Pronto quando:** - painel do gerente.leitura de chamada com opção do interpretador — com qualquer opção do interpretador, o painel reconhece o programa e mostra as mesmas linhas da chamada sem opção — Verificações 1 e 2 (a armadilha registrada, Verificação 3)

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAF-12`, `F-10`, `F-32`.
- **Operação do modelo:** `OP-3` - OP-3: O painel do gerente passa a reconhecer o programa chamado quando a chamada traz opções do interpretador antes dele. - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.
- **Camada e fronteira:** gancho do kit em `.claude/tools/progresso_hook.py` (roda em `PreToolUse`, `PostToolUse` e `Stop`); falha aberta, sem bloquear a chamada; não importa de `tests/`.
- **Contratos/classes:** `_programa(tokens: list[str]) -> tuple[str, list[str]] | None` — assinatura inalterada. Regra nova, sobre os tokens depois do interpretador: `-X` e `-W` consomem também o token seguinte (o valor) — e, na forma colada (`-Xutf8`, `-Wignore`), só o próprio token; `-m <módulo>` devolve `(<módulo>, tokens depois do módulo)`; `-c` devolve `None` (não há script); qualquer outro token iniciado por `-` consome só a si mesmo, como hoje; o primeiro token que não começa por `-` é o script, como hoje.
- **Passos:** 1. Reescrever o laço de `_programa` com a regra de `Contratos/classes`. 2. Escrever os três testes da seção `Testes`, no molde de `test_tf_ger_4_estado_mudado` (fixture `estado`, `raiz`; `payload_next` com `=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]`). 3. Apensar ao fim da tabela de `docs/ARMADILHAS_DE_FERRAMENTA.md` a linha abaixo (as quebras são as do bloco: uma linha só): ```text | `Python` (linha de comando) | opção do interpretador antes do script (`-X utf8`, `-W`, `-m`, `-c`) desloca o nome do programa: quem lê a linha pulando só o token iniciado por `-` toma o valor da opção (`utf8`) pelo script | (`R-06` da auditoria de encerramento do estágio 1, 2026-09-27: com `python -X utf8`, o painel do gerente calou `M-2`, `M-5`, `M-10`, `M-13` e `M-18`) | quem lê a linha de comando pula a opção junto com o valor dela (`-X`, `-W`), toma o módulo depois de `-m` como programa e não procura script depois de `-c` — é o que `progresso_hook._programa` faz. | ```
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 3 testes novos (referência datada: `452 passed`, 2026-09-27). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - O gancho segue em falha aberta: exceção dentro dele nunca bloqueia a chamada.
- **Não fazer:** não mudar `FRASES` nem as frases do painel; não mudar a linha da armadilha do console cp1252 já existente na tabela; não mudar o `.claude/settings.json` nem o `.claude/projecoes.json`.
- **Contingências:** - se um teste existente de `tests/test_progresso_hook.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_opcao_do_interpretador_com_valor_gera_m2` — `python -X utf8 .claude/tools/backlog.py status TLG-T9 in-progress` gera a frase `M-2` (`Tarefa "Um título de teste": gates aprovados; vou materializar in-progress e gravar o ponto de partida.`); a regra antiga toma `utf8` pelo script e não gera. TR `test_tr_opcao_do_interpretador_sem_valor_segue_gerando_m2` — `python -u .claude/tools/backlog.py status TLG-T9 in-progress` gera `M-2` (a regra concorrente "toda opção consome o token seguinte" tomaria `status` pelo script e não geraria). TF `test_tf_opcao_do_interpretador_m_e_c` — `_programa(['python','-m','pytest','-q'])` devolve `('pytest', ['-q'])` e `_programa(['python','-c','print(1)'])` devolve `None`.
- **Fora do escopo desta tarefa:** a recomendação do laudo na linha do revisor (`AF-T6`, que também edita `progresso_hook.py`).
- **Handover:** 2026-09-27 · para quem vier depois - **Entregue:** _programa em .claude/tools/progresso_hook.py:293 pula -X/-W com valor (separado ou colado), devolve o modulo apos -m, None para -c; testes em tests/test_progresso_hook.py:1362, :1379, :1396; armadilha nova em docs/ARMADILHAS_DE_FERRAMENTA.md:16 - **Contrato:** o painel gera as mesmas linhas para 'python -X utf8 <script>' e 'python <script>'; assinatura de _programa inalterada - **Não refazer:** a leitura das opcoes do interpretador no painel - **Pendente:** nenhum

## Execução

**Consumo:** 23 tool uses, 75.9 k tokens, 354.3 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master vai fechar a tarefa "O painel do gerente reconhece o programa depois das opções do interpretador" como done: registrar estado, RDO e telemetria.
