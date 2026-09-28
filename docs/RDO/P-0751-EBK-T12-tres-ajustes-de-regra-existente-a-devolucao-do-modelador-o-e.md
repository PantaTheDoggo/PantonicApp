# RDO — P-0751 · EBK-T12

**Plano:** `docs/plans/P-0751-esgotar-backlog.md`
**Tarefa:** `EBK-T12` — Três ajustes de regra existente: a devolução do modelador, o enunciado composto e o aviso de modelo
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** o `pantonic-model-designer` passa a devolver ponteiro, cabeçalho, linha da versão, saída do `check` e o campo `Achados fora da seção` — em vez de recopiar a seção —, com `GOVERNANCA.md` §3 e §3.2 dizendo o mesmo; §3.2 reconhece o enunciado composto de atos do dono registrados; e o aviso da fase intelectual do hook de modelo deixa de mandar parar quem está em Fable.

**Arquivos-alvo:** - `.claude/agents/pantonic-model-designer.md` - `GOVERNANCA.md` - `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` - `tests/test_materializar.py` (só o bloco 6, `DEB-10`)

**Verificação:** no PowerShell, na raiz; **antes** medido em 2026-09-25 (itens 1-7) e 2026-09-26 (item 8). 1. `(Select-String -Path .claude/agents/pantonic-model-designer.md -SimpleMatch 'Achados fora da seção:').Count` — antes `0`, depois `1` 2. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'devolve a seção literal').Count` — antes `2`, depois `0` 3. `(Select-String -Path GOVERNANCA.md -SimpleMatch 'O enunciado pode ser composto').Count` — antes `0`, depois `1` 4. `(Select-String -Path .claude/global/hooks/modelo_por_fase_userpromptsubmit.py -SimpleMatch 'Em Opus ou Fable, ignore').Count` — antes `0`, depois `1` 5. `python -m py_compile .claude/global/hooks/modelo_por_fase_userpromptsubmit.py` → exit `0` 6. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate` e `-Mode check-drift` → exit `0` 7. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho (medido pelo consultor numa cópia com os seis blocos: `376 passed`). 8. `(Select-String -Path tests/test_materializar.py -SimpleMatch '== 470').Count` — antes `1`, depois `0`

**Pronto quando:** as quatro contagens saem nos valores de depois, o hook compila e o kit segue sem drift interno.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Origem:** card `TK-67b` do diário de obras, seção `## TK-67`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-12` - OP-12: O card dos três ajustes de regra existente sai de pronto para concluído, sobre o backlog que a operação anterior deixou. - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Fundamento:** itens 1, 2 e 3 do insumo do veredito dos procedimentos, na seção `## TK-67` do diário de obras, com os casos medidos no `P-0747`.
- **Passos:** substituir cada **Texto atual** pelo **Texto novo** de mesmo número, no arquivo indicado; rodar `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate`; rodar as Verificações.
- **Texto novo 2:** ~~~~ devolve o ponteiro da seção, a linha do registro de versões que registra o ato, a saída do `check` e os achados fora da seção (`pantonic-model-designer`) ~~~~
- **Texto novo 3:** ~~~~ devolve o ponteiro da seção, a linha do ato em `### 1.4 Registro de versões`, a saída do `check` e os achados fora da seção; ~~~~
- **Texto novo 4:** ~~~~ o que o modelador imaginou. O enunciado pode ser composto — uma frase do dono mais atos dele registrados em datas diferentes, transcritos na `## 0`, cada ato com a data e o ponteiro ao registro —, e o lastro vale igual para cada parte. E o ~~~~
- **Texto novo 5:** ~~~~ "Se o modelo ativo for Sonnet ou Haiku, PARE e peca ao dono `/model opus` antes de " "prosseguir (anuncie a troca — Regra 5). Em Opus ou Fable, ignore: o modelo " "da sessao e escolha do dono.", ~~~~
- **Não fazer:** não rodar `materializar.py apply` nem escrever em `C:\Users\panta\.claude\` — a cópia do hook no ponto de carga é do condutor, no fechamento deste card (invariante I-1); não tocar o aviso da fase de execução nem o `systemMessage` da fase intelectual.
- **Contingências:** - se um **Texto atual** não for encontrado exatamente uma vez → parar e sinalizar `blocked` razão `premissa`, citando o número do bloco.
- **Notas de execução:** - 2026-09-26 `ready` — consultor acionamento 5: DEB-10, bloco 6 no test_materializar; edicoes da arvore revertidas

## Execução

**Consumo:** 28 tool uses, 64.7 k tokens, 206.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
