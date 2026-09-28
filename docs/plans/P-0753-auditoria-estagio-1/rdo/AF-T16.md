# RDO — P-0753 · AF-T16

# Humano

Tarefa "Os verificadores em PowerShell escrevem UTF-8 no console" concluída em 2026-09-27.
Os verificadores em PowerShell passam a escrever UTF-8 no console, sem acentos corrompidos.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria de encerramento do estágio 1: as dezoito recomendações e os dois tíquetes do consultor": 16/21 tarefas concluídas; próxima: "O pré-voo do pedido confere o que o dono cita antes da campanha".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0753-auditoria-estagio-1/plano.md`
**Tarefa:** `AF-T16` — Os verificadores em PowerShell escrevem UTF-8 no console
**Modelo:** Sonnet · **Classe:** mecanica
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Os verificadores do kit passam a escrever os acentos corretamente no console do Windows.

**Arquivos-alvo:** - `.claude/checks/check-readme.ps1` - `.claude/checks/kit_check.ps1`

**Verificação:** 1. `python -c "import subprocess;r=subprocess.run(['pwsh','-NoProfile','-File','.claude/checks/check-readme.ps1'],capture_output=True);print(r.stdout.decode('utf-8','replace').count(chr(65533))>0)"` → `False` — antes `True`, depois `False` (esperado, não ensaiado) 2. `python -c "from pathlib import Path;s='[Console]::OutputEncoding = [Text.Encoding]::UTF8';print(Path('.claude/checks/kit_check.ps1').read_text(encoding='utf-8').count(s),Path('.claude/checks/check-readme.ps1').read_text(encoding='utf-8').count(s))"` → `1 1` — antes `0 0`, depois `1 1` (esperado, não ensaiado) 3. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava) 4. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)

**Pronto quando:** - verificadores do console.acentos na saída — letra acentuada sai correta — Verificações 1 e 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAF-23`, `F-23`, `F-34`.
- **Operação do modelo:** `OP-16` - OP-16: Os verificadores do kit passam a escrever os acentos corretamente no console do Windows. - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.
- **Camada e fronteira:** verificadores do kit em `.claude/checks/` (PowerShell 7); o texto das mensagens não muda.
- **Passos:** 1. Em cada um dos dois arquivos, inserir logo depois da linha `$ErrorActionPreference = 'Stop'` a linha abaixo (uma linha só; `param(...)` segue sendo a primeira instrução do script): ```text [Console]::OutputEncoding = [Text.Encoding]::UTF8 ```
- **Restrições desta tarefa:** - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0 e `pwsh -NoProfile -File .claude/checks/check-readme.ps1` sai 0. - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho). - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
- **Não fazer:** não mudar o texto de mensagem nenhuma; não trocar acento por ASCII; não mexer no bloco `param(...)`.
- **Contingências:** - se `tests/test_kit_check.py` cair por causa da saída em UTF-8 → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** nenhum teste novo; `tests/test_kit_check.py` e a suíte inteira como trava.
- **Fora do escopo desta tarefa:** os demais `.ps1` de `.claude/checks/` (a recomendação e a decisão nomeiam os dois).
- **Handover:** 2026-09-27 · para quem vier depois - **Entregue:** [Console]::OutputEncoding = [Text.Encoding]::UTF8 logo depois de $ErrorActionPreference em .claude/checks/check-readme.ps1:45 e .claude/checks/kit_check.ps1:35 - **Contrato:** os dois verificadores em PowerShell escrevem UTF-8 no console, sem caractere de substituição para quem lê a saída - **Não refazer:** nada a declarar - **Pendente:** nenhum

## Execução

**Consumo:** 11 tool uses, 48.8 k tokens, 148.7 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

O check-drift e o validate do kit_check no caminho verde não têm letra acentuada ('materializacao'); a correção de codificação só se observa no caminho de falha, que nenhum teste nem linha de aceite toca.

## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master vai fechar a tarefa "Os verificadores em PowerShell escrevem UTF-8 no console" como done: registrar estado, RDO e telemetria.
