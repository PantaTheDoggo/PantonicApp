# RDO — P-0753 · AF-T17

# Humano

Tarefa "O pré-voo do pedido confere o que o dono cita antes da campanha" concluída em 2026-09-27.
O planejador ganha um pré-voo que confere se o que o dono cita existe na árvore antes da campanha; ficou uma ressalva sobre a leitura de citações em crase.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Auditoria de encerramento do estágio 1: as dezoito recomendações e os dois tíquetes do consultor": 17/21 tarefas concluídas; próxima: "O guia de entrada descreve o kit como ele fica".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achados registrados no plano, com rota: 2 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/plans/P-0753-auditoria-estagio-1/plano.md`
**Tarefa:** `AF-T17` — O pré-voo do pedido confere o que o dono cita antes da campanha
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O planejador passa a conferir, antes de abrir a campanha, a existência de cada caminho, nome e opção que o pedido do dono cita.

**Arquivos-alvo:** - `.claude/tools/prevoo.py` (novo) - `tests/test_prevoo.py` (novo) - `.claude/agents/pantonic-planner.md`

**Verificação:** 1. `python .claude/tools/prevoo.py "reutilizando a função ler_texto_utf8 de .claude/tools/caminhos.py"` → `ler_texto_utf8 | não | —` — antes `exit 2`, depois `ler_texto_utf8 | não | —` (esperado, não ensaiado) 2. `python -m pytest tests/test_prevoo.py -q` → `exit 0` — antes `exit 4`, depois `exit 0` (esperado, não ensaiado) 3. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8');print(t.count('sem ferramenta, 1 turno'),t.count('prevoo.py'))"` → `0 1` — antes `1 0`, depois `0 1` (esperado, não ensaiado) 4. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava) 5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)

**Pronto quando:** - planejador.conferência do pedido — antes da campanha, cada caminho, nome e opção citados no pedido é conferido, e o que não existe volta ao dono — Verificações 1 a 3

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAF-16`, `DAF-31`, `F-14`.
- **Depende de:** `AF-T8`
- **Operação do modelo:** `OP-17` - OP-17: O planejador passa a conferir, antes de abrir a campanha, a existência de cada caminho, nome e opção que o pedido do dono cita. - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.; planejador — Quem implementa recebe o roteiro de fases do agente e muda só a fase que a recomendação aponta, deixando as demais como estão.
- **Camada e fronteira:** instrumento novo do kit `.claude/tools/prevoo.py` (somente leitura; não importa de `tests/` nem de irmão) e a Fase 0 do arquivo do agente planejador (corpo, não o frontmatter).
- **Contratos/classes:** `python .claude/tools/prevoo.py "<texto>" [--root <caminho>]` (raiz padrão: a do repositório, três níveis acima do arquivo). Força `sys.stdout.reconfigure(encoding="utf-8")` antes do primeiro `print`. Extrai do texto, na ordem da primeira aparição e sem repetir: **caminhos** — token terminado em `.py`, `.md`, `.ps1`, `.json`, `.tsv`, `.txt`, `.yml`, `.yaml` ou `.toml`, ou terminado em `/`; existe quando `(<root> / <token>)` existe; `onde` = o próprio caminho. **Símbolos** — nome seguido de `(`, ou identificador com `_` que não é parte de caminho nem de flag; existe quando algum `.py` sob `<root>` (fora de `.git` e `__pycache__`) tem a linha `def <nome>(` ou `class <nome>`; `onde` = `<arquivo>:<linha>` da primeira, com `/`. **Flags** — token que começa por `-` seguido de letra; existe quando algum `.py` sob `<root>/.claude` contém a flag entre aspas (`"<flag>"` ou `'<flag>'`); `onde` = `<arquivo>:<linha>` da primeira. Imprime a linha `citado | existe | onde` e uma linha `<citado> | <sim ou não> | <onde ou —>` por item. Exit `0` quando todo item existe (ou não há item), `1` quando algum não existe, `2` sem argumento (argparse).
- **Passos:** 1. Escrever `.claude/tools/prevoo.py` pela regra de `Contratos/classes`, com `main(argv=None) -> int` e `if __name__ == "__main__": sys.exit(main())`. 2. Escrever `tests/test_prevoo.py` com os testes da seção `Testes`, sobre árvore temporária (`--root <tmp_path>`), carregando o módulo por `importlib.util.spec_from_file_location`. 3. Em `.claude/agents/pantonic-planner.md`: o título `### Fase 0 — Intake (sem ferramenta, 1 turno)` vira `### Fase 0 — Intake (uma ferramenta, o pré-voo; 1 turno)`; e, depois da linha do item `1. Transcreva o pedido do dono **verbatim**`, entra o parágrafo abaixo, recuado três espaços, como continuação do item 1 (as quebras são as do bloco; o recuo de dois espaços do bloco não entra no arquivo): ```text **Pré-voo do pedido.** A `## 0` recebe a tabela `citado | existe | onde` que `python .claude/tools/prevoo.py "<pedido>"` imprime para todo caminho, símbolo e flag do texto do dono, colada por quem conduz a sessão; sem ela, rode o instrumento como primeiro ato e cole a tabela. Linha com `não` volta ao dono antes da campanha, pela SAÍDA 2, com o citado e o `onde` vazio: premissa do pedido que não existe na árvore não vira pergunta ao scout (caso medido, 2026-09-27: um nome de função citado no pedido e ausente da árvore custou uma instância inteira do planejador, 41,4k tokens). ```
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os testes novos (referência datada: `452 passed`, 2026-09-27). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0 (o frontmatter do agente não muda). - `python .claude/checks/dead_code.py` sai 0 (toda função nova é chamada a partir de `main`). - Só os `Arquivos-alvo` se editam ou se criam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
- **Não fazer:** não escrever em arquivo nenhum a partir do `prevoo.py`; não chamar rede; não mudar outra fase do arquivo do planejador; não registrar o instrumento em `.claude/settings.json` nem em `.claude/projecoes.json`.
- **Contingências:** - se `python .claude/checks/dead_code.py` acusar função do `prevoo.py` → a função não é chamada por `main`: ligá-la a `main` ou apagá-la, e seguir. - se `tests/piso_comportamental.txt` existir (entregue pela `AF-T15`) → acrescentar ao fim dele uma linha por TR novo desta tarefa, na forma `<nodeid> — <frase>` da `AF-T15`.
- **Testes:** TF `test_tf_prevoo_simbolo_ausente_diz_nao` — árvore temporária com `.claude/tools/caminhos.py` sem `ler_texto_utf8`: o texto `reutilizando a função ler_texto_utf8 de .claude/tools/caminhos.py` dá as linhas `.claude/tools/caminhos.py | sim | .claude/tools/caminhos.py` e `ler_texto_utf8 | não | —`, exit 1. TR `test_tr_prevoo_simbolo_definido_diz_onde` — com `def ler_texto_utf8(` na linha 3 do mesmo arquivo: `ler_texto_utf8 | sim | .claude/tools/caminhos.py:3`, exit 0 (a regra concorrente, "existe se aparece em qualquer lugar", aceitaria menção em `.md`; a fixture põe a menção num `.md` e a função ausente, e o TF acima tem de dar `não`). TF `test_tf_prevoo_flag_existente` — `.claude/tools/x.py` com `"--desde"`: o texto `rode com --desde` dá `--desde | sim | .claude/tools/x.py:<linha>`.
- **Fora do escopo desta tarefa:** a separação da campanha em blocos de leitura e de comando (`AF-T19`).
- **Handover:** 2026-09-27 · para quem vier depois - **Entregue:** instrumento novo .claude/tools/prevoo.py (citado | existe | onde; exit 0/1/2), tests/test_prevoo.py com 3 testes, Fase 0 do pantonic-planner.md (:79-89) manda rodar o pré-voo; linha do TR em tests/piso_comportamental.txt - **Contrato:** o planejador confere caminhos, símbolos e flags citados pelo dono antes da campanha; a leitura de token ainda não normaliza crase e pontuação (ressalva do laudo, com o consultor) - **Não refazer:** nada a declarar - **Pendente:** prevoo.py usa str.split() sem tirar crase, vírgula, ponto, ponto-e-vírgula nem parênteses: citação em crase e 'nome()' saem sem item (ressalva do laudo)

## Execução

**Consumo:** 40 tool uses, 104.5 k tokens, 689.8 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Os tres testes do card fixam o comportamento sobre texto ja limpo (tokens separados por espaco, sem crase); o defeito so aparece quando o instrumento recebe um pedido escrito como o dono escreve. Instrumento que le prosa pede, no card, um caso de aceite com a prosa real.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master vai fechar a tarefa "O pré-voo do pedido confere o que o dono cita antes da campanha" como done: registrar estado, RDO e telemetria.
