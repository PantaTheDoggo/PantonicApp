# RDO — P-0753 · AF-T4

# Humano

Tarefa "O fechamento transcreve o achado de processo do laudo para os achados do plano" concluída em 2026-09-27.
O fechamento de tarefa copia sozinho para os achados do plano cada achado de processo que o revisor registra no laudo, com a rota dele.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria de encerramento do estágio 1: as dezoito recomendações e os dois tíquetes do consultor": 4/21 tarefas concluídas; próxima: "O gancho de telemetria grava todo papel do kit, e a soma do plano os separa".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0753-auditoria-estagio-1/plano.md`
**Tarefa:** `AF-T4` — O fechamento transcreve o achado de processo do laudo para os achados do plano
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O fechamento de tarefa passa a copiar para os achados do plano cada achado de processo que o laudo traz, com a rota dele.

**Arquivos-alvo:** - `.claude/tools/encerrar.py` - `tests/test_encerrar.py` - `.claude/skills/scrum-master/SKILL.md`

**Verificação:** 1. `python -m pytest tests/test_encerrar.py -q -k "achado_do_laudo"` → `exit 0` — antes `exit 5`, depois `exit 0` (esperado, não ensaiado) 2. `python -c "from pathlib import Path;print(Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8').count('cada linha da tabela'))"` → `1` — antes `0`, depois `1` (esperado, não ensaiado) 3. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava) 4. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)

**Pronto quando:** - fechamento de tarefa.achado de processo do laudo — cada achado de processo do laudo chega aos achados do plano com a rota, uma vez só — Verificações 1 e 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAF-13`, `DAF-32`, `F-11`.
- **Operação do modelo:** `OP-4` - OP-4: O fechamento de tarefa passa a copiar para os achados do plano cada achado de processo que o laudo traz, com a rota dele. - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/encerrar.py`; carrega `backlog.py`, `rdo.py` e `telemetria.py` por caminho, como hoje; não importa de `tests/`.
- **Domínio:** *achado de processo* — linha da seção `## Achado de processo` do laudo que `rdo.py laudo` grava, na tabela `| alvo | achado |` (`alvo` ∈ `dossiê`, `doutrina`, `rubrica`, `modelo`), ou o corpo `nenhum` quando não há achado. Invariante: todo `AE-<n>` de `## Achados da execução` traz `**Rota:**` (o fechamento do plano recusa achado sem rota).
- **Contratos/classes:** função nova `achados_do_laudo(texto_laudo: str) -> list[tuple[str, str]]` — `(texto, rota)` por linha da tabela; `texto` = `achado de processo (<alvo>): ` + o trecho do achado antes da primeira ocorrência de `Rota:`, com `strip()`; `rota` = o trecho depois de `Rota:`, com `strip()`, ou `não declarada no laudo` quando o achado não traz `Rota:` ou o trecho sai vazio. `fechar_tarefa` grava, depois dos `--achado` de hoje, um `AE-<n>` por par de `achados_do_laudo`, pela `apensar_achado` existente, **pulando** o par cujo `texto` já ocorre em alguma entrada de `achados_do_plano(plano_path)` ou foi gravado antes no mesmo fechamento. `--achado` continua como está.
- **Passos:** 1. Escrever `achados_do_laudo` e chamá-la em `fechar_tarefa` sobre o texto do mesmo arquivo de laudo que o fechamento já passa a `ler_laudo` (lido com `encoding="utf-8"`); gravar os pares depois do laço dos `--achado`, pela `apensar_achado`, com a regra de não repetir de `Contratos/classes`; somar os ids gravados à linha `Achados:` do texto humano. 2. Em `.claude/skills/scrum-master/SKILL.md`, Passo 9, a linha abaixo depois de `antigo:` vira as duas linhas depois de `novo:` (as quebras são as do bloco; os rótulos não entram no arquivo): ```text antigo: (5) cada `--achado` vira `AE-<n>` com `**Rota:**` em `## Achados da execução` do plano. O novo: (5) cada linha da tabela `## Achado de processo` do laudo e cada `--achado` viram `AE-<n>` com `**Rota:**` em `## Achados da execução` do plano, sem repetir achado do laudo já registrado. O ``` 3. Escrever os três testes da seção `Testes`, com laudo de fixture igual à constante `LAUDO` de `tests/test_encerrar.py` acrescida, antes de `## Lições aprendidas na tarefa`, da seção `## Achado de processo` com a tabela `| alvo | achado |`.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 3 testes novos (referência datada: `452 passed`, 2026-09-27). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - O fechamento continua recusando sem escrever quando falta insumo; a leitura do achado do laudo nunca é motivo de recusa.
- **Não fazer:** não mudar `rdo.py` nem a forma da tabela que `rdo.py laudo` grava; não mudar `apensar_achado` nem a forma da entrada `AE-<n>`; não remover `--achado`.
- **Contingências:** - se o laudo não tiver a seção `## Achado de processo`, ou ela trouxer `nenhum` → nenhum achado do laudo; seguir. - se um teste existente de `tests/test_encerrar.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_achado_do_laudo_vira_ae_com_rota` — laudo com a linha `| dossiê | o card não citava o arquivo de teste. Rota: card corretivo ALF-T1a |`: o plano ganha `- **AE-2** (`ALF-T1`, fechamento, 2026-09-26) — achado de processo (dossiê): o card não citava o arquivo de teste. **Rota:** card corretivo ALF-T1a` (a regra de hoje não grava nada). TR `test_tr_achado_do_laudo_repetido_nao_duplica` — plano que já tem uma entrada com `achado de processo (dossiê): o card não citava o arquivo de teste.`: nenhum `AE-<n>` novo (a regra concorrente, "grava toda linha do laudo", duplicaria). TF `test_tf_achado_do_laudo_sem_rota_declarada` — linha `| doutrina | a skill não nomeia o gate. |`: o `AE-<n>` traz `**Rota:** não declarada no laudo`.
- **Fora do escopo desta tarefa:** a soma do consumo do plano por papel (`AF-T5`, que também edita `encerrar.py`).
- **Handover:** 2026-09-27 · para quem vier depois - **Entregue:** achados_do_laudo em .claude/tools/encerrar.py:238, chamada no fechamento (:555) apos os --achado, sem repetir texto ja registrado; Passo 9 item (5) do scrum-master (.claude/skills/scrum-master/SKILL.md:228); testes em tests/test_encerrar.py:188, :208, :231 - **Contrato:** encerrar.py tarefa transcreve cada linha de '## Achado de processo' do laudo como AE-<n> com Rota (ou 'nao declarada no laudo'); o condutor nao precisa repassar esses achados por --achado - **Não refazer:** a transcricao do achado do laudo - **Pendente:** nenhum

## Execução

**Consumo:** 27 tool uses, 94.0 k tokens, 387.7 s (fonte: `<usage>` do encerramento)

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

Scrum master concluiu a tarefa "O painel do gerente reconhece o programa depois das opções do interpretador" e vai pegar a tarefa "O fechamento transcreve o achado de processo do laudo para os achados do plano".
Tarefa "O fechamento transcreve o achado de processo do laudo para os achados do plano". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O fechamento transcreve o achado de processo do laudo para os achados do plano" e vai executar: O fechamento de tarefa passa a copiar para os achados do plano cada achado de processo que o laudo traz, com a rota dele.
Agente executor devolveu a tarefa "O fechamento transcreve o achado de processo do laudo para os achados do plano": review — sem pendência.
Agente revisor recebe a tarefa "O fechamento transcreve o achado de processo do laudo para os achados do plano" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O fechamento transcreve o achado de processo do laudo para os achados do plano": aprovado 100%, bloqueante nenhuma.
Scrum master vai fechar a tarefa "O fechamento transcreve o achado de processo do laudo para os achados do plano" como done: registrar estado, RDO e telemetria.
