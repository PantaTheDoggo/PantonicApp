# RDO — P-0749 · SAN-T2a

**Plano:** `docs/plans/P-0749-saneamento-artefatos.md`
**Tarefa:** `SAN-T2a` — Projeto novo com contador em P-0 e nenhum plano passa no check
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Corretivo da `SAN-T2` (`AE-4`): o estado de projeto novo que o bootstrap cria (`_INBOX.md` só com `**Próximo id de plano: P-0.**`, `docs/plans/` sem plano) deixa de acusar `C-10`; com plano presente, `C-10` segue como está.

**Arquivos-alvo:** - `.claude/tools/backlog.py` - `tests/test_backlog.py`

**Verificação:** 1. ``` python -m pytest tests/test_backlog.py -q -k tf_san ``` → **8 passed**. **Medido antes: 7 passed** (2026-09-25; conta TF de cards anteriores, `AE-2`). 2. ``` pwsh -NoProfile -Command '@(Select-String -LiteralPath .claude/tools/backlog.py -SimpleMatch -Pattern "if ids_planos and contador <= max(ids_planos):").Count' ``` → **1**. **Medido antes: 0**. 3. ``` pwsh -NoProfile -Command '$r = "$env:TEMP/san-t2a-ref/backlog.py"; $a = @(python $r check --repo . 2>$null) + @(python $r next --repo .); $b = @(python .claude/tools/backlog.py check --repo . 2>$null) + @(python .claude/tools/backlog.py next --repo .); if (($a -join "|") -ne ($b -join "|")) { "DIFERE"; exit 1 } else { "IGUAL" }' ``` → **IGUAL**. **Medido antes: IGUAL** (2026-09-25, reparo aplicado numa cópia; mede-se depois do passo 1). 4. ``` python -m pytest tests -q ``` → **o total anotado no passo 1 + 1, nenhuma falha**. **Medido antes: 352 passed** (2026-09-25; 353 com o reparo numa cópia da árvore). 5. ``` python .claude/checks/dead_code.py ``` → **exit 0**. **Medido antes: exit 0**.

**Pronto quando:** - kit.número do plano — projeto novo começa em zero e soma um; aqui a contagem segue de onde está — Verificação 1, 2, 3

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Fundamento:** DSA-22, DSA-3, DSA-14; I-2; `AE-4`.
- **Depende de:** `SAN-T2`
- **Operação do modelo:** `OP-2` - OP-2: O mantenedor do backlog faz o instrumento de backlog guardar o estado de plano e de tarefa numa tabela de máquina na pasta do plano, contar o próximo número a partir do zero em projeto novo e acusar plano novo com estado escrito no texto. - precisa de: kit — Quem implementa recebe essas ferramentas e esses textos. O que já está gravado continua sendo lido como hoje.; acervo existente — Quem implementa não o toca. Ele prova que nada do que existe se perdeu.
- **Camada e fronteira:** kit, `.claude/tools/backlog.py` (só o bloco `C-10` de `check`) e `tests/test_backlog.py`.
- **Passos:** 1. Antes de qualquer edição, copiar o código de referência para `$env:TEMP` (`DSA-20`) e anotar o total da suíte: ``` pwsh -NoProfile -Command 'New-Item -ItemType Directory -Force "$env:TEMP/san-t2a-ref" | Out-Null; Copy-Item .claude/tools/backlog.py,.claude/tools/caminhos.py "$env:TEMP/san-t2a-ref/"; "copiado"' python -m pytest tests -q ``` 2. Aplicar o bloco de `Texto novo, literal`. 3. Acrescentar ao fim de `tests/test_backlog.py` o TF de `Testes`. 4. Rodar a Verificação 1 a 5.
- **Restrições desta tarefa:** I-2 — com plano presente, `C-10` e a sua mensagem não mudam (`test_tf_san_12_c10_preserva_largura` e a fixture `contador_inbox` seguem verdes, inalterados).
- **Não fazer:** não tocar `transacionar_drain`, `caminhos.py`, a doutrina nem fixture existente; não criar fixture nova (o TF monta o estado em `tmp_path`).
- **Contingências:** 1. se o texto antigo não aparecer literal, ou aparecer mais de uma vez → parar e sinalizar `blocked` razão `premissa`, devolvendo a linha.
- **Fora do escopo desta tarefa:** a doutrina do bootstrap (`SAN-T4`, entregue); o `README.md` (`SAN-T6`).

## Execução

**Consumo:** 18 tool uses, 64.9 k tokens, 128.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
