# RDO — P-0753 · AF-T12

# Humano

Tarefa "O veredito do marco é um comando" concluída em 2026-09-27.
O veredito do dono num marco passa a ser gravado por um comando, nos três lugares do plano; ficou uma ressalva sobre dois caminhos de borda.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Auditoria de encerramento do estágio 1: as dezoito recomendações e os dois tíquetes do consultor": 12/21 tarefas concluídas; próxima: "O esqueleto do relatório de operações sai por comando".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0753-auditoria-estagio-1/plano.md`
**Tarefa:** `AF-T12` — O veredito do marco é um comando
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem conduz passa a gravar o veredito do dono no marco por um comando único, que o escreve em todos os lugares onde o marco aparece.

**Arquivos-alvo:** - `.claude/tools/encerrar.py` - `tests/test_encerrar.py`

**Verificação:** 1. `python .claude/tools/encerrar.py marco --help` → `exit 0` — antes `exit 2`, depois `exit 0` (esperado, não ensaiado) 2. `python -m pytest tests/test_encerrar.py -q -k "marco"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado) 3. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava) 4. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)

**Pronto quando:** - marco de validação.registro do veredito — um comando grava o resultado dado pelo dono em todos os lugares do marco, sem interpretar a frase dele — Verificações 1 e 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAF-14`, `DAF-27`, `F-12`.
- **Depende de:** `AF-T6`
- **Operação do modelo:** `OP-12` - OP-12: Quem conduz passa a gravar o veredito do dono no marco por um comando único, que o escreve em todos os lugares onde o marco aparece. - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; fechamento de tarefa — Quem implementa faz o fechamento copiar cada achado de processo do laudo para os achados do plano, com a rota, sem repetir achado igual.
- **Camada e fronteira:** instrumento do kit `.claude/tools/encerrar.py`; carrega `backlog.py` por caminho, como hoje; não importa de `tests/`. A máquina não interpreta a frase do dono: o resultado entra por argumento.
- **Domínio:** *lugares do marco* (`DAF-27`) — (1) a célula `veredito` (última) da linha `| **Marco <n>** |` da tabela *Marcos de validação* do cabeçalho do plano; (2) o fim da seção `## 0.` do plano; (3) o status do plano no Marco 1. O cenário do consultor não é lugar do marco.
- **Contratos/classes:** subcomando `marco`, com `parents=[comuns]` (o analisador comum de hoje, que já traz `--plano`, `--repo` e `--data`) e mais: `--marco <n>` (inteiro), `--resultado {go,no-go}`, `--veredito "<frase>"` e, exclusivos entre si e opcionais, `--aceita-versao <k>` ou `--recusa-versao <k>`. Recusa com `marco: <razão>` no stderr, exit `1` e nada escrito, quando: o plano não existe; a linha `| **Marco <n>** |` não existe (`linha do Marco <n> ausente na tabela de marcos`); a seção `## 0.` não existe (`seção ## 0 ausente`); veio `--aceita-versao` ou `--recusa-versao` e o plano não tem a linha `## 1A. Modelo conceitual — versão pendente de validação` (`plano sem versão pendente (## 1A)`). Escritas, nesta ordem: (1) a última célula da linha do marco vira `<resultado> · <data> — "<frase>"`, com `|` da frase escrito `\|`; (2) antes do primeiro heading `## ` que vem depois de `## 0.`, entram as linhas `**Marco <n>, <data> — veredito do dono (<resultado>):**`, uma linha vazia, `> <frase>` e uma linha vazia; (3) com `--marco 1`, `--resultado go` e o plano em `blocked`, `_backlog.transacionar_status(repo, modelo, <id do plano>, "ready", nota="Marco 1 go em <data>")`. Com versão, imprime no stdout o dossiê abaixo; sempre imprime por último `marco: Marco <n> gravado — <resultado>`.
- **Passos:** 1. Escrever a função `gravar_marco(...)` e o subcomando `marco` no `main`, pela regra de `Contratos/classes`. 2. Com `--aceita-versao <k>` ou `--recusa-versao <k>`, imprimir o dossiê com as seis linhas abaixo (as quebras são as do bloco; o recuo de dois espaços não entra na saída; `<frase>`, `<n>`, `<k>` e `<plano>` se substituem): ```text Plano: <plano> Ato: emenda Motivo: Marco <n>, veredito do dono: "<frase>" Fato novo: o dono aceitou a versão <k> do modelo no Marco <n>. Restrição: a versão <k> passa a vigente e a anterior a obsoleta; o conteúdo da obsoleta sai do plano e o registro de versões guarda a linha (GOVERNANCA.md §3.2). Devolver: a seção ## 1 depois do ato e a linha nova do registro de versões. ``` Com `--recusa-versao`, a linha `Fato novo` é `Fato novo: o dono recusou a versão <k> do modelo no Marco <n>.` e a `Restrição` é `Restrição: a versão <k> é eliminada e a vigente permanece, sem marca; o que foi entregue sob a versão recusada se refaz por card corretivo da operação afetada (GOVERNANCA.md §3.2).` 3. Escrever os quatro testes da seção `Testes`, sobre plano temporário legado no molde de `PLANO` de `tests/test_encerrar.py`, com a linha `**Status:** `` `blocked` ``, a tabela de marcos `| marco | o que o dono lê | veredito |` com `| **Marco 1** | a seção 1 | pendente |` e uma seção `## 0. O problema, verbatim` antes de `## 5. Tarefas`.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 4 testes novos (referência datada: `452 passed`, 2026-09-27). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Nenhuma verificação de recusa escreve arquivo; todas as checagens rodam antes da primeira escrita.
- **Não fazer:** não escrever na `## 1` nem na `## 1A` (o ato de versão é do modelador); não tirar o resultado da frase do dono (ele vem só de `--resultado`); não mudar os verbos `tarefa`, `handover` e `plano`.
- **Contingências:** - se um teste existente de `tests/test_encerrar.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_marco_go_grava_celula_zero_e_tira_de_blocked` — `marco --marco 1 --resultado go --veredito "Pode seguir"`: a célula vira `go · 2026-09-26 — "Pode seguir"`, a `## 0` ganha a linha `> Pode seguir` e o plano sai de `blocked` para `ready`. TR `test_tr_marco_no_go_nao_muda_status` — o mesmo com `--resultado no-go`: células e `## 0` gravadas, plano segue `blocked` (a regra concorrente, "todo marco 1 libera o plano", o tiraria). TF `test_tf_marco_recusa_versao_imprime_dossie_de_emenda` — plano com a linha `## 1A. Modelo conceitual — versão pendente de validação` e `--recusa-versao 2 --veredito "Não aceito"`: o stdout tem `Ato: emenda` e `Motivo: Marco 1, veredito do dono: "Não aceito"`. TR `test_tr_marco_recusa_sem_linha_do_marco_sem_escrever` — `--marco 2` num plano só com o Marco 1: exit 1, stderr com `linha do Marco 2 ausente`, plano igual byte a byte.
- **Fora do escopo desta tarefa:** o esqueleto do relatório de operações (`AF-T13`, que também edita `encerrar.py`); a promoção ou a eliminação da versão pendente (ato do modelador, com o dossiê que este verbo imprime).
- **Handover:** 2026-09-27 · para quem vier depois - **Entregue:** subcomando 'encerrar.py marco' (gravar_marco) grava a célula do marco, o ato na ## 0 e, no Marco 1 go com plano blocked, a transição para ready; com --aceita/--recusa-versao imprime o dossiê de emenda; 4 testes em tests/test_encerrar.py - **Contrato:** o veredito do marco se grava por um comando; dois caminhos de borda com defeito (ressalva do laudo, com o consultor) - **Não refazer:** nada a declarar - **Pendente:** (a) regravar marco com frase que tinha pipe escapado deixa resto na célula; (b) Marco 1 go com transição recusada grava o plano antes de sair exit 1 (ressalva do laudo)

## Execução

**Consumo:** 57 tool uses, 164.7 k tokens, 855.5 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master vai fechar a tarefa "O veredito do marco é um comando" como done: registrar estado, RDO e telemetria.
