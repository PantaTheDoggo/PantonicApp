# RDO — DIARIO_DE_OBRAS · TK-89a

# Humano

Tarefa "O leitor de alvos da evidência corta o literal da âncora antes de varrer as crases" concluída em 2026-09-26.
A evidência do revisor passou a reconhecer como alvo a entrada com âncora seguida de literal, em vez de descartá-la.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Tíquete "O gate do card religado deixou atrás o leitor de alvos e a doutrina": 1/2 tarefas concluídas; próxima: "A doutrina do gate do card conta oito itens, cita o `card_check` no `B3` e confere o literal contido na faixa".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-89a` — O leitor de alvos da evidência corta o literal da âncora antes de varrer as crases
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** em `_classificar_campo_alvos` de `.claude/tools/review_evidence.py`, antes da varredura por `_BACKTICK_RE`, o texto do campo (`arquivos-alvo` ou `entregavel`) troca cada âncora seguida de literal pela âncora só; o resto da função não muda. Com isso a entrada `` `<caminho>:<linha>` — `<literal>` `` vira um alvo, com ou sem crase escapada no literal, e o literal não vai aos descartados.

**Arquivos-alvo:** - `.claude/tools/review_evidence.py` - `tests/test_review_evidence.py`

**Verificação:** 1. `python -c "import sys;sys.path.insert(0,'.claude/tools');import review_evidence as r,rdo;from pathlib import Path;d=rdo.extrair_dossie(Path('docs/plans/P-0752-fato-no-ponto-de-uso.md'),'FPU-T2',esquema_legado=False,modelo_legado=None,classe_legado=None);print(len(r.extrair_arquivos_alvo(d.campos)))"` → `5` — antes `1`, depois `5`. 2. `python -m pytest tests/test_review_evidence.py -q -k alvo_ancorado_com_literal` → verde — antes `exit 5`, depois `exit 0` (antes nenhum teste selecionado). 3. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`. 4. `python -m pytest tests/test_review_evidence.py -q -k literais_nao_caminho_lista` → verde — antes `exit 0`, depois `exit 0` (o teste de `CT89-1`, com a entrada trocada).

**Pronto quando:** a entrada de `Arquivos-alvo` com âncora e literal conta como um alvo na evidência, provado pelo TF e pela `FPU-T2` do `P-0752` (5 alvos).

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Contratos/classes:** constante de módulo `_LITERAL_APOS_ANCORA_RE = re.compile(r"(`[^`\s]+:\d+(?:-\d+)?`)\s*(?:—|:)\s*`(?:\\`|[^`\\])+`")`, aplicada com `.sub(r"\1", texto)`; mesma leitura de literal da `DFP-16` do `P-0752` (`card_check._LITERAL_APOS_ANCORA_RE`), duplicada aqui, sem import cruzado.
- **Caso medido que motivou:** ver `## TK-89`, item (1).
- **Testes (novos, em `tests/test_review_evidence.py`):** TF `test_tf_alvo_ancorado_com_literal_e_um_alvo` — o campo `- \`a/b.md:3\` — \`x \\\` y\` - \`c/d.py\`` (literal com crase escapada) → `_classificar_campo_alvos` devolve `(["a/b.md", "c/d.py"], [])`; hoje devolve `(["a/b.md"], [...])` (medido no protótipo). TR `test_tr_alvo_sem_ancora_nao_muda` — campo só com caminhos entre crases e um literal não caminho → mesmo resultado de hoje.
- **Teste existente que muda (um só, `CT89-1`):** em `test_tr_extrair_literais_nao_caminho_lista_o_descartado`, a entrada `` `.claude/tools/rdo.py:79` — `_ID_HEADER_RE = re.compile(x)` `` perde o `:79` e fica `` `.claude/tools/rdo.py` — `_ID_HEADER_RE = re.compile(x)` ``. Razão: com linha, o par é âncora da `DFP-16` e o literal é dela (conferido pelo `card_check`), não literal descartado — o corte o tira dos descartados por decisão (Objetivo); sem linha, o `re.compile` continua literal não caminho e o teste segue provando o que prova (a `DB-27` lista o descartado). Os dois `assert` ficam como estão. Medido pelo consultor (protótipo na árvore, revertido): com o corte e essa troca, `tests/test_review_evidence.py` 55 passed, suíte 442 passed, `FPU-T2` 5 alvos e 0 descartados, o campo do TF → `(['a/b.md', 'c/d.py'], [])`.
- **Não fazer:** não mudar `_eh_caminho`, `_LINHA_REF_RE` nem `_SECAO_REF_RE`; não importar `card_check`; não tocar `rdo.py`; não mudar os `assert` de `test_tr_extrair_literais_nao_caminho_lista_o_descartado` nem a entrada de `test_tf_extrair_arquivos_alvo_aceita_arquivo_de_raiz_e_recusa_literal_de_regex` (a mesma, que segue verde com `:79`); não aplicar o corte só aos alvos (descartados lidos do texto sem corte voltam a desalinhar na crase escapada).
- **Contingências:** - se cair um teste existente de `_classificar_campo_alvos` ou de `extrair_literais_nao_caminho` **outro que** `test_tr_extrair_literais_nao_caminho_lista_o_descartado` (tratado em `CT89-1`) → parar e sinalizar `blocked` razão `premissa`, nomeando o teste (no protótipo, o corte só muda cards do `P-0752` e só esse teste cai).
- **Handover:** 2026-09-26 · para `TK-89b` - **Entregue:** review_evidence.py: _LITERAL_APOS_ANCORA_RE corta o literal da âncora em _classificar_campo_alvos antes de _BACKTICK_RE; FPU-T2 do P-0752 conta 5 alvos - **Contrato:** entrada de Arquivos-alvo 'caminho:linha — literal' é um alvo, e o literal não vai aos descartados - **Não refazer:** nada a declarar - **Pendente:** nenhum
- **Notas de execução:** - 2026-09-26 `ready` — consultor TK-89 acionamento 1 (CT89-1): corte mantido nos alvos e nos descartados; test_tr_extrair_literais_nao_caminho_lista_o_descartado troca a entrada rdo.py:79 por rdo.py (asserts intactos); protótipo medido 442 passed - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-89a-o-leitor-de-alvos-da-evidencia-corta-o-literal-da-ancora-ant.md`, veredito aprovado 100%

## Execução

**Consumo:** 25 tool uses, 83.6 k tokens, 765.0 s (fonte: `<usage>` do encerramento)

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

Scrum master concluiu a tarefa "O fechamento pergunta ao `rdo.py` e ao `backlog.py` se pode escrever, em vez de copiar a regra deles" e vai pegar a tarefa "O leitor de alvos da evidência corta o literal da âncora antes de varrer as crases".
Tarefa "O leitor de alvos da evidência corta o literal da âncora antes de varrer as crases". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O leitor de alvos da evidência corta o literal da âncora antes de varrer as crases" e vai executar: em `_classificar_campo_alvos` de `.claude/tools/review_evidence.py`, antes da varredura por `_BACKTICK_RE`, o texto do campo (`arquivos-alvo` ou `entregavel`) troca cada âncora seguida de literal pela âncora só; o resto da função não muda.…
Agente executor devolveu a tarefa "O leitor de alvos da evidência corta o literal da âncora antes de varrer as crases": blocked — motivo premissa: contingência do próprio card: aplicar `_LITERAL_APOS_ANCORA_RE.sub(r"\1", texto)` antes de `_BACKTICK_RE` quebra `tests/test_review_evidence.py::test_tr_extrair_literais_nao_caminho_lista_o_descartado` (o par `` `.claude/tools/rdo.py:79` — `_ID_HEADER_RE = re.compile(x)` `` casa a regex do card e some do texto, então `re.compile` deixa de aparecer em `extrair_literais_nao_caminho`, contra o `assert any("re.compile" in item ...)` da linha 473) — confirmado isolando a regex do card num script `python` avulso (removido, nenhum arquivo do dossiê foi tocado) e rodando `.sub()`/`.finditer()` sobre o texto exato do teste existente..
Scrum master vai marcar a tarefa "O leitor de alvos da evidência corta o literal da âncora antes de varrer as crases" como blocked, sem RDO.
Agente consultor recebe a tarefa "O leitor de alvos da evidência corta o literal da âncora antes de varrer as crases" e vai triar.
Agente consultor devolveu a tarefa "O leitor de alvos da evidência corta o literal da âncora antes de varrer as crases": rota resolve.
Agente executor recebe a tarefa "O leitor de alvos da evidência corta o literal da âncora antes de varrer as crases" e vai executar: em `_classificar_campo_alvos` de `.claude/tools/review_evidence.py`, antes da varredura por `_BACKTICK_RE`, o texto do campo (`arquivos-alvo` ou `entregavel`) troca cada âncora seguida de literal pela âncora só; o resto da função não muda.…
Agente executor devolveu a tarefa "O leitor de alvos da evidência corta o literal da âncora antes de varrer as crases": review — sem pendência.
Agente revisor recebe a tarefa "O leitor de alvos da evidência corta o literal da âncora antes de varrer as crases" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O leitor de alvos da evidência corta o literal da âncora antes de varrer as crases": aprovado 100%, bloqueante nenhuma.
Scrum master vai fechar a tarefa "O leitor de alvos da evidência corta o literal da âncora antes de varrer as crases" como done: registrar estado, RDO e telemetria.
