# RDO — P-0754 · AUF-T2

# Humano

Tarefa "Um teste exercita o caminho com acento que o versionador devolve em código" concluída em 2026-09-28.
Um teste agora cobre o caminho com acento que o git devolve codificado; uma linha apagada por engano de outro teste foi reposta.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Auditoria final do kit: os herdados e o relatório de auditoria nova": 2/16 tarefas concluídas; próxima: "O alvo com curinga casa, e o alvo que não existia chega marcado como novo".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0754-auditoria-final/plano.md`
**Tarefa:** `AUF-T2` — Um teste exercita o caminho com acento que o versionador devolve em código
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa cobre com teste o trecho do instrumento de evidência que lê o caminho com acento devolvido em código pelo versionador.

**Arquivos-alvo:** - `tests/test_review_evidence.py`

**Verificação:** 1. `python -m pytest tests/test_review_evidence.py -q -k "caminho_acentuado"` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - dossiê de evidência.caminho com acento — um teste exercita o trecho com um caminho acentuado de verdade — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAU-13`; `H-12` (§2.1); `F-13`.
- **Depende de:** `AUF-T1`
- **Operação do modelo:** `OP-2` - OP-2: Quem executa cobre com teste o trecho do instrumento de evidência que lê o caminho com acento devolvido em código pelo versionador. - precisa de: levantamento dos herdados — Ninguém altera: é a fonte de cada item que o plano fecha e da prova com que ele fecha.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ao revisor, cada caso com o teste que o prova, sempre numa cópia descartável do repositório.
- **Camada e fronteira:** suíte do kit (`tests/`); o instrumento `.claude/tools/review_evidence.py` não muda nesta tarefa.
- **Contratos/classes:** o trecho coberto é o de `coletar_arquivos_tocados(root: Path, desde: str | None = None) -> list[str]`, com `desde`: a linha `??` do `git status` cujo caminho, lido por `_extrair_caminho_status` (que tira as aspas e não decodifica o escape octal), não existe no disco entra nos tocados, porque o salto `if arquivo.exists() and arquivo.stat().st_mtime < corte: continue` não dispara. Com `core.quotepath` ligado, o `git status` devolve `ação.txt` como `"a\303\247\303\243o.txt"`; o caminho que entra nos tocados é `a\303\247\303\243o.txt` — em Python, a string `"a\\303\\247\\303\\243o.txt"`.
- **Passos:** 1. Acrescentar ao fim de `tests/test_review_evidence.py` o teste da seção `Testes`: repositório de `_init_repo_com_baseline`, `_run_git(["config", "core.quotepath", "true"], repo)`, `ref = review_evidence.capturar_ref(repo)`, depois `(repo / "ação.txt")` criado com uma linha de texto. 2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma o 1 teste novo (referência datada: `505 passed`, 2026-09-28, HEAD `2513964`). - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`; o teste cria o próprio repositório em `tmp_path` com `_init_repo_com_baseline`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `.claude/tools/review_evidence.py` — nem para decodificar o escape octal: o card cobre o comportamento de hoje; não depender da configuração global do `git` (o teste liga `core.quotepath` no próprio repositório).
- **Contingências:** - se, com `core.quotepath` ligado no repositório do teste, a lista devolvida não for exatamente `["a\\303\\247\\303\\243o.txt"]` → parar e sinalizar `blocked` razão `premissa`, colando a lista devolvida e a saída de `git status --porcelain=v1 --untracked-files=all` do repositório do teste.
- **Testes:** TF `test_tf_caminho_acentuado_do_status_entra_nos_tocados_pelo_ramo_de_caminho_ausente` — `review_evidence.coletar_arquivos_tocados(repo, desde=ref)` devolve exatamente `["a\\303\\247\\303\\243o.txt"]` (a regra concorrente, que pulasse o caminho ausente do disco, devolveria `[]`). Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** decodificar o escape octal do `git status` (não pedido pela operação; se a revisão o julgar defeito, vira `AE-<n>` na §9).
- **Handover:** 2026-09-28 · para `AUF-T3` - **Entregue:** TF test_tf_caminho_acentuado_do_status_entra_nos_tocados_pelo_ramo_de_caminho_ausente em tests/test_review_evidence.py (fim do arquivo); assert '+linha-1' do TR da AUF-T1 reposto pelo consultor (DAU-32) - **Contrato:** coletar_arquivos_tocados com core.quotepath devolve o caminho com escape octal cru; comportamento de hoje coberto, instrumento intocado - **Não refazer:** nada a declarar - **Pendente:** caminho com escape octal chega a montar_trechos como arquivo ausente (AE-99, à AUF-T16)

## Execução

**Consumo:** 17 tool uses, 62.6 k tokens, 154.8 s (fonte: `<usage>` do encerramento)

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

Scrum master concluiu a tarefa "O arquivo criado depois do recorte chega ao revisor como diferença" e vai pegar a tarefa "Um teste exercita o caminho com acento que o versionador devolve em código".
Tarefa "Um teste exercita o caminho com acento que o versionador devolve em código". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "Um teste exercita o caminho com acento que o versionador devolve em código" e vai executar: Quem executa cobre com teste o trecho do instrumento de evidência que lê o caminho com acento devolvido em código pelo versionador.
Agente executor devolveu a tarefa "Um teste exercita o caminho com acento que o versionador devolve em código": review — sem pendência.
Tarefa "Um teste exercita o caminho com acento que o versionador devolve em código": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "Um teste exercita o caminho com acento que o versionador devolve em código" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "Um teste exercita o caminho com acento que o versionador devolve em código": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Agente consultor recebe a tarefa "Um teste exercita o caminho com acento que o versionador devolve em código" e vai triar.
Agente consultor devolveu a tarefa "Um teste exercita o caminho com acento que o versionador devolve em código": rota resolve.
Scrum master vai fechar a tarefa "Um teste exercita o caminho com acento que o versionador devolve em código" como done: registrar estado, RDO e telemetria.
