# RDO — DIARIO_DE_OBRAS · TK-84a

# Humano

Tarefa "Com `--desde`, o não rastreado anterior ao ref sai dos tocados" concluída em 2026-09-26.
A evidência do revisor deixa de listar arquivo não rastreado mais antigo que o ponto de partida.
Revisão: aprovada com ressalva (94%).
Pendência para o dono: nenhuma.
Tíquete "`review_evidence.py --desde` lista não rastreado anterior ao despacho": 1/1 tarefas concluídas; nenhuma tarefa pronta na fila dele.
Achados registrados no plano, com rota: 2 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-84a` — Com `--desde`, o não rastreado anterior ao ref sai dos tocados
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** em `coletar_arquivos_tocados` de `.claude/tools/review_evidence.py`, com `desde` informado, cada entrada `??` do `git status` cujo arquivo tem data de modificação (`st_mtime`) menor que a data de commit de `desde` (`git show -s --format=%ct <desde>`, em segundos) deixa de entrar na lista; a de data igual ou maior entra como hoje. Caminho que não existe no disco como veio do `git status` (nome entre aspas com escape octal, por exemplo) entra como hoje, sem erro. Sem `desde`, nada muda. A docstring da função deixa de dizer que o não rastreado "entra sempre".

**Arquivos-alvo:** - `.claude/tools/review_evidence.py` - `tests/test_review_evidence.py`

**Verificação:** 1. `python -m pytest tests/test_review_evidence.py -q -k nao_rastreado_anterior_ao_desde` → o teste novo verde — antes `exit 5`, depois `exit 0` (antes nenhum teste selecionado). 2. `python -m pytest tests/test_review_evidence.py -q` → verde — antes `exit 0`, depois `exit 0`. 3. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`.

**Pronto quando:** com `desde`, não rastreado anterior ao commit de `desde` não aparece entre os tocados, provado pelo par, e sem `desde` a lista não muda.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Caso medido que motivou:** ver `## TK-84`.
- **Reparo medido (protótipo do consultor, 2026-09-26, cópia da árvore já apagada):** ler `%ct` de `desde` uma vez com o `_git` do módulo e, no laço das entradas `??`, pular a que tem `(root / caminho).stat().st_mtime < corte`. Com ele, `tests/test_review_evidence.py` inteiro verde e suíte sem falha; o teste abaixo falha sobre o `review_evidence.py` de hoje.
- **Testes (novo, em `tests/test_review_evidence.py`, nome começado por `test_coletar_nao_rastreado_anterior_ao_desde`):** TF par sobre `_init_repo_com_baseline`: `ref` = `HEAD`, `ct` = `%ct` de `ref`; `src/velho.py` criado com `os.utime` em `ct - 60` e `src/novo.py` com `os.utime` em `ct + 60` → `coletar_arquivos_tocados(repo, desde=ref)` contém `src/novo.py` e não contém `src/velho.py`; `coletar_arquivos_tocados(repo)` (sem `desde`) contém `src/velho.py`.
- **Não fazer:** não mudar `coletar_estado_git` nem os baldes de `confrontar_escopo`; não trocar a data de commit pela data de autor; não ler data de modificação de arquivo rastreado.
- **Contingências:** - se um teste existente de `desde` cair com o reparo → parar e sinalizar `blocked` razão `premissa`, nomeando o teste (medido no protótipo: nenhum cai).
- **Notas de execução:** - 2026-09-26 `review` — corte por %ct de desde no laço ?? de coletar_arquivos_tocados; TF novo verde (vermelho sem o reparo); test_review_evidence 55 passed; suíte 421 passed - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-84a-com-desde-o-nao-rastreado-anterior-ao-ref-sai-dos-tocados.md`, veredito ressalva 94%

## Execução

**Consumo:** não medido — executada inline pelo condutor na sessão principal, fora do loop: sem SubagentStop nem bloco de uso

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 94%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Card pedia Sonnet esforco low e foi executado inline em Opus pelo condutor: a entrega bate verbatim com o reparo medido do consultor (corte por %ct lido uma vez, skip no laco ?? com exists() antes do stat), o que indica tarefa inteiramente fechada pelo card e sem juizo residual - candidata natural ao modelo barato; o custo extra veio do caminho de execucao, nao da materia.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "TK-91" e vai pegar a tarefa "Com `--desde`, o não rastreado anterior ao ref sai dos tocados".
Tarefa "Com `--desde`, o não rastreado anterior ao ref sai dos tocados". Passo: conferir os gates e preparar o despacho.
Tarefa "Com `--desde`, o não rastreado anterior ao ref sai dos tocados". Passo: conferir os gates e preparar o despacho.
Scrum master vai fechar a tarefa "Com `--desde`, o não rastreado anterior ao ref sai dos tocados" como done: registrar estado, RDO e telemetria.
Scrum master concluiu a tarefa "Com `--desde`, o não rastreado anterior ao ref sai dos tocados" e vai pegar a tarefa "Com `--desde`, o não rastreado anterior ao ref sai dos tocados".
Tarefa "Com `--desde`, o não rastreado anterior ao ref sai dos tocados". Passo: conferir os gates e preparar o despacho.
Tarefa "Com `--desde`, o não rastreado anterior ao ref sai dos tocados": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Tarefa "Com `--desde`, o não rastreado anterior ao ref sai dos tocados": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "Com `--desde`, o não rastreado anterior ao ref sai dos tocados" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "Com `--desde`, o não rastreado anterior ao ref sai dos tocados": {"isAsync": true, "status": "async_launched", "agentId": "a9f9b45dbe9a25d83", "description": "Revisar entrega TK-84a", "resolvedModel": "claude-opus-5-5", "prom….
Scrum master vai fechar a tarefa "Com `--desde`, o não rastreado anterior ao ref sai dos tocados" como done: registrar estado, RDO e telemetria.
Scrum master concluiu a tarefa "Com `--desde`, o não rastreado anterior ao ref sai dos tocados" e vai pegar a tarefa "`rdo.py laudo --motivo` e o alvo `dossiê`".
Scrum master vai fechar a tarefa "Com `--desde`, o não rastreado anterior ao ref sai dos tocados" como done: registrar estado, RDO e telemetria.
