# RDO — P-0754 · AUF-T7

# Humano

Tarefa "O painel mostra o título do tíquete em curso" concluída em 2026-09-28.
O painel de acompanhamento agora mostra o título do tíquete em curso, e não só o número dele.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria final do kit: os herdados e o relatório de auditoria nova": 7/16 tarefas concluídas; próxima: "A frase final do fechamento serve a todos os comandos".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0754-auditoria-final/plano.md`
**Tarefa:** `AUF-T7` — O painel mostra o título do tíquete em curso
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o painel do gerente mostrar o título do tíquete em curso, e não só o identificador dele.

**Arquivos-alvo:** - `.claude/tools/progresso_hook.py` - `tests/test_progresso_hook.py`

**Verificação:** 1. `python -m pytest tests/test_progresso_hook.py -q -k "tiquete"` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - painel do gerente.título do tíquete — o painel mostra o título do tíquete, como já faz com o card — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAU-15`, `DAU-26`; `H-14` (§2.1); `F-13`, `F-16`.
- **Operação do modelo:** `OP-7` - OP-7: Quem executa faz o painel do gerente mostrar o título do tíquete em curso, e não só o identificador dele. - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.
- **Camada e fronteira:** gancho do kit em `.claude/tools/progresso_hook.py` (roda em `PreToolUse`, `PostToolUse` e `Stop`); falha aberta, sem bloquear a chamada; não importa de `tests/`.
- **Contratos/classes:** `localizar_card(id_tarefa: str, raiz: Path) -> tuple[str, str, str]` — assinatura inalterada. Padrão novo, ao lado do de card (`^### <id> — (.+?) \[`): o de tíquete, `^## <id> — (.+?)\s*$`, com o id escapado por `re.escape`. Na varredura linha a linha, a linha que casa o padrão de tíquete devolve na hora `(título, "", "")` — título com `strip()`, objetivo vazio e título de plano vazio, porque o tíquete não mora dentro de um plano. O card (`### <id> — … [`), inclusive o card de tíquete, segue como hoje, e o fallback `(id_tarefa, "", "")` também.
- **Passos:** 1. Acrescentar ao fim de `tests/test_progresso_hook.py` os dois testes da seção `Testes`, no molde de `test_tf_san_18_titulo_do_plano_em_pasta` (`tmp_path` como raiz, diário em `docs/DIARIO_DE_OBRAS.md`). 2. Rodar `python -m pytest tests/test_progresso_hook.py -q -k "tiquete"` e conferir que o TF falha. 3. Acrescentar o padrão de tíquete a `localizar_card`, pela regra de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `505 passed`, 2026-09-28, HEAD `2513964`). - `python .claude/checks/dead_code.py` sai 0 e `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - O gancho segue em falha aberta: exceção dentro dele nunca bloqueia a chamada. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `FRASES` nem as frases do painel; não mudar `.claude/skills/scrum-master/SKILL.md`, `.claude/settings.json` nem `.claude/projecoes.json`.
- **Contingências:** - se um teste que já existia em `tests/test_progresso_hook.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_titulo_do_tiquete_em_curso` — diário com as linhas `# Diário`, vazia, `## TK-9 — Um tíquete de teste`, vazia e `Corpo do tíquete.`: `localizar_card("TK-9", tmp_path)` devolve `("Um tíquete de teste", "", "")` (a regra antiga devolve `("TK-9", "", "")`). TR `test_tr_card_de_tiquete_segue_com_o_titulo_do_card` — diário com `## TK-9 — Um tíquete de teste`, vazia, `### TK-9a — O card do tíquete [Sonnet · classe implementacao]` e `- **Objetivo:** fixture.`: `localizar_card("TK-9a", tmp_path)` devolve `("O card do tíquete", "fixture.", "Um tíquete de teste")`. Suíte `tests/test_progresso_hook.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** a frase final do fechamento (`AUF-T8`).
- **Handover:** 2026-09-28 · para `AUF-T15` - **Entregue:** localizar_card em .claude/tools/progresso_hook.py:143 casa também o cabeçalho de tíquete '## <id> — <título>' e devolve (título, '', ''); TF/TR no fim de tests/test_progresso_hook.py - **Contrato:** o painel mostra o título do tíquete em curso; card de tíquete e fallback inalterados - **Não refazer:** o padrão de tíquete em localizar_card - **Pendente:** nenhum

## Execução

**Consumo:** 14 tool uses, 56.1 k tokens, 133.5 s (fonte: `<usage>` do encerramento)

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

Scrum master concluiu a tarefa "O arquivo novo que não é texto se julga pelo conteúdo bruto" e vai pegar a tarefa "O painel mostra o título do tíquete em curso".
Tarefa "O painel mostra o título do tíquete em curso". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O painel mostra o título do tíquete em curso" e vai executar: Quem executa faz o painel do gerente mostrar o título do tíquete em curso, e não só o identificador dele.
Agente executor devolveu a tarefa "O painel mostra o título do tíquete em curso": review — sem pendência.
Tarefa "O painel mostra o título do tíquete em curso": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O painel mostra o título do tíquete em curso" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O painel mostra o título do tíquete em curso": aprovado 100%, bloqueante nenhuma, recomendação seguir.
Scrum master vai fechar a tarefa "O painel mostra o título do tíquete em curso" como done: registrar estado, RDO e telemetria.
