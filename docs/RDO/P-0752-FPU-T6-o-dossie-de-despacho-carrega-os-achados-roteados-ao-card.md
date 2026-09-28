# RDO — P-0752 · FPU-T6

# Humano

Tarefa "O dossiê de despacho carrega os achados roteados ao card" concluída em 2026-09-26.
O dossiê que o loop entrega a cada executor passa a trazer os achados já registrados que apontam para aquele card.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Fato no ponto de uso: os mecanismos contra o esquecimento e a assunção": 9/15 tarefas concluídas; próxima: "A medida do executor mora onde o revisor a procura, também no plano em pasta".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0752-fato-no-ponto-de-uso.md`
**Tarefa:** `FPU-T6` — O dossiê de despacho carrega os achados roteados ao card
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `backlog.py show <ID>` e `backlog.py next` imprimem, depois do texto do card de plano, o bloco `**Achados roteados a este card:**` com cada entrada `AE-<n>` da seção de achados do plano cujo texto depois de `**Rota:**` cita `<ID>` como palavra inteira (DFP-7), nas duas formas de entrada do corpus (id entre crases, a do consultor, e id sem crase, a do `encerrar.py tarefa --achado`); card sem achado roteado imprime `**Achados roteados a este card:** nenhum`. Plano inteiro, tíquete e subtarefa de tíquete saem como hoje.

**Arquivos-alvo:** - `.claude/tools/backlog.py:1008` — `def show(modelo: Modelo, id_: str) -> str:` - `.claude/tools/backlog.py:1431` — `linhas_saida.append(_truncar(item.texto, item.arquivo, item.linha_header, item.linha_fim))` - `tests/test_backlog.py`

**Verificação:** 1. `python -m pytest tests/test_backlog.py -q` → verde — antes `108 passed`, depois `112 passed`. 2. `python -c "from pathlib import Path;print(Path('.claude/tools/backlog.py').read_text(encoding='utf-8').count('Achados roteados')>=1)"` → `True` — antes `False`, depois `True`. 3. `python .claude/tools/backlog.py check` → `check: OK — nenhuma violação.` — antes `OK`, depois `OK` (trava: o `check` da árvore real segue OK com o `backlog.py` alterado). 4. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`. 5. `python -c "import subprocess,sys;o=subprocess.run([sys.executable,'.claude/tools/backlog.py','show','FPU-T1'],capture_output=True,text=True,encoding='utf-8').stdout;b=o.split(chr(10)+'**Achados roteados a este card:**'+chr(10));print(len(b)==2 and b[1].count('**Rota:**')>=3)"` → `True` — antes `False`, depois `True` (no corpus real, `AE-1`..`AE-3` do §8 são roteados à `FPU-T1`).

**Pronto quando:** dossiê de despacho.precedentes — derivados das entradas de achado do plano roteadas ao card — Verificações 1, 2 e 5.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Operação do modelo:** `OP-6` - OP-6: O dossiê de despacho carrega os achados do plano roteados ao card, derivados das entradas de achado e não da memória de quem despacha. - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; dossiê de despacho — Quem implementa deriva o precedente dos achados do plano, sem depender de quem despacha lembrar.; achado de execução — Ninguém altera: o achado nasce do laudo e o dossiê o lê.
- **Fundamento:** DFP-7, DFP-19, F-4, causa 4 de F-10 (`AE-1` do `P-0743` registrado na `DOM-T1` e não colado no despacho da `DOM-T5`).
- **Contratos/classes:** (DFP-19) - `achados_roteados(texto_plano: str, tarefa_id: str) -> list[str]` em `backlog.py` — recebe `Plano.texto`, já carregado (`show` e `renderizar_next` não recebem `repo`, e `Item.arquivo` é relativo ao repo). Leitura duplicada de `encerrar.achados_do_plano`, sem import: seção = da linha que casa `^## .*Achados da execução` até a próxima que casa `^#{1,2} ` (exclusive) ou o fim; entrada = linha que começa com `- ` na coluna 0 mais as seguintes até a próxima `- ` na coluna 0 ou o fim da seção, sem as linhas em branco do fim; só vale entrada cuja primeira linha casa `\bAE-(\d+)\b` (as duas formas casam; numeração não contígua não importa). Rota = texto da entrada depois da primeira ocorrência de `**Rota:**`, até o fim da entrada (inclui linhas de continuação e anotações posteriores, como `**Destino (…)**`); entrada sem `**Rota:**` nunca é roteada. Filtro: `re.search(rf"(?<![\w-]){re.escape(tarefa_id)}(?![\w-])", rota)`. Devolve o texto verbatim de cada entrada (linhas unidas por `\n`), na ordem do arquivo. - `_bloco_achados(texto_plano: str, tarefa_id: str) -> str` — `**Achados roteados a este card:** nenhum` se a lista é vazia; senão a linha `**Achados roteados a este card:**` seguida das entradas, unidas por `\n`. - `show`: quando `alvo` é `Item` com `tipo == "tarefa"`, devolve `_truncar(...)` + `"\n\n"` + `_bloco_achados(plano.texto, alvo.id)`, com `plano` = o de `modelo.planos` cujo `id == alvo.pai`; qualquer outro alvo devolve exatamente o de hoje. O bloco fica fora do teto DB-7 (o teto é do texto do card). - `renderizar_next`: quando `tipo_pai == "plano"`, `linhas_saida.append(_bloco_achados(pai.texto, item.id))` logo depois da linha do dossiê truncado e antes de `--- pendências mecânicas ---` (o `next` não chama `show`).
- **Passos:** 1. Escrever `_ACHADOS_HEADING_RE`, `_AE_ID_RE`, `achados_roteados` e `_bloco_achados` logo acima de `show`, com o comentário de duplicação (`sem import cruzado com encerrar.py`, padrão `.claude/tools/rdo.py:137` — `duplicado aqui — sem import cruzado`). 2. Alterar `show` e `renderizar_next` como no Contratos. 3. Testes em `tests/test_backlog.py`, **sem alterar a fixture `verde` em disco**: helper `_verde_com_achados(tmp_path)` copia a `verde` com `_copiar_fixture` e apensa ao fim de `docs/plans/P-0001-alfa.md` uma linha em branco, `## Achados da execução`, outra linha em branco e quatro entradas — `AE-1` na forma do consultor (id entre crases) com `**Rota:**` citando `ALF-T1`; `AE-7` na forma do `encerrar.py` (`- **AE-7** (` + crase + `ALF-T1` + crase + `, fechamento, 2026-01-02) — …`) com a `**Rota:**` numa linha de continuação indentada de dois espaços citando `ALF-T1`; `AE-8` que cita `ALF-T1` no texto e não tem `**Rota:**`; `AE-9` com `**Rota:**` citando só `ALF-T1a`. A seção entra no texto do card `ALF-T1` (o `## Achados da execução` não é fronteira de item no `_scan_items`), por isso os asserts olham só o bloco. TF `test_tf_show_lista_achado_roteado` (bloco = o que vem depois de `"\n\n**Achados roteados a este card:**\n"` em `show(modelo, "ALF-T1")`: contém `AE-1`, `AE-7` e a linha de continuação; não contém `AE-8` nem `AE-9`); TF `test_tf_show_sem_achado_diz_nenhum` (`verde` intacta: `show(modelo, "BET-T1")` termina em `"\n\n**Achados roteados a este card:** nenhum"`); TR `test_tr_show_de_tiquete_nao_muda` (`verde` intacta: `show(modelo, "TK-1a") == _localizar(modelo, "TK-1a").texto`, e `renderizar_next` do vencedor `TK-1a` não contém `Achados roteados`); TF `test_tf_next_de_tarefa_de_plano_traz_o_bloco(tmp_path, capsys)` (`main(["next", "--repo", str(_verde_com_handover(tmp_path))])`, vencedor `ALF-T2`: a saída contém `**Achados roteados a este card:** nenhum` depois de `--- dossiê` e antes de `--- pendências mecânicas ---`). Medido pelo consultor em protótipo (acionamento 7): com o `backlog.py` de hoje os três TF falham e o TR passa; com o contrato, os quatro passam.
- **Não fazer:** não importar `encerrar.py` (DFP-7, I-4); não mudar o texto do card devolvido antes do bloco nem o `_truncar`; não alterar a fixture `verde` em disco (compartilhada por 20 testes; o vencedor do `next` nela é `TK-1a`); não mudar `_scan_items`; não tocar o índice do diário.
- **Contingências:** - se um teste existente de `show` ou `next` afirmar a saída inteira de tarefa de plano → o teste que fixa o comportamento antigo é alvo da tarefa (`DM-33` do `P-0740`): passa a admitir o bloco; registrar em `pendencia=`. Medido no protótipo do consultor: nenhum (suíte inteira verde).
- **Handover:** 2026-09-26 · para `FPU-T5c` - **Entregue:** achados_roteados(texto_plano, tarefa_id) em .claude/tools/backlog.py:1012 (le as duas formas de entrada AE, consultor e encerrar.py) e _bloco_achados (:1052); show (:1059) e renderizar_next (:1434) apensam o bloco '**Achados roteados a este card:**' a tarefa de plano; 4 testes novos em tests/test_backlog.py (helper _verde_com_achados) - **Contrato:** backlog.py show <ID> e next trazem, depois do dossie, cada AE do plano cuja Rota cita o ID como palavra inteira; sem achado: 'nenhum'; tiquete nao muda; test_backlog 112 passed; suite 419 passed - **Não refazer:** bloco de achados no dossie ja pago - **Pendente:** o show do ultimo card do plano traz as secoes 6 a 8 junto (_scan_items so corta em heading '## X — ...'), comportamento anterior fora do card
- **Notas de execução:** - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T6-o-dossie-de-despacho-carrega-os-achados-roteados-ao-card.md`, veredito aprovado 100%

## Execução

**Consumo:** 49 tool uses, 108.2 k tokens, 421.3 s (fonte: `<usage>` do encerramento)

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

Scrum master concluiu a tarefa "O aviso de crença no ato de gravar plano ou diário" e vai pegar a tarefa "O dossiê de despacho carrega os achados roteados ao card".
Tarefa "O dossiê de despacho carrega os achados roteados ao card". Passo: conferir os gates e preparar o despacho.
Agente consultor recebe a tarefa "O dossiê de despacho carrega os achados roteados ao card" e vai triar.
Agente consultor devolveu a tarefa "O dossiê de despacho carrega os achados roteados ao card": rota resolve.
Tarefa "O dossiê de despacho carrega os achados roteados ao card": gates aprovados; vou materializar in-progress e gravar o ponto de partida.
Tarefa "O dossiê de despacho carrega os achados roteados ao card". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O dossiê de despacho carrega os achados roteados ao card" e vai executar: `backlog.py show <ID>` e `backlog.py next` imprimem, depois do texto do card de plano, o bloco `**Achados roteados a este card:**` com cada entrada `AE-<n>` da seção de achados do plano cujo texto depois de `**Rota:**` cita `<ID>` como pal…
Agente executor devolveu a tarefa "O dossiê de despacho carrega os achados roteados ao card": review — sem pendência.
Tarefa "O dossiê de despacho carrega os achados roteados ao card": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O dossiê de despacho carrega os achados roteados ao card" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O dossiê de despacho carrega os achados roteados ao card": aprovado 100%, bloqueante nenhuma.
