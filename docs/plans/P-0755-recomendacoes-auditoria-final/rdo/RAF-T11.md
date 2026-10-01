# RDO — P-0755 · RAF-T11

# Humano

Tarefa "A evidência mostra as linhas que a entrega tirou dos testes" concluída em 2026-09-29.
O dossiê de evidência passa a mostrar as linhas que a entrega tirou dos arquivos de teste.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 19/48 tarefas concluídas; próxima: "A rubrica reprova a asserção de teste removida sem ordem do card".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T11` — A evidência mostra as linhas que a entrega tirou dos testes
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o dossiê de evidência mostrar, para cada arquivo de teste entre os alvos do card, as linhas que a entrega removeu.

**Arquivos-alvo:** - `.claude/tools/review_evidence.py` - `tests/test_review_evidence.py`

**Verificação:** 1. `python -m pytest tests/test_review_evidence.py -q -k removidas_de_teste` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - dossiê de evidência.linhas removidas dos testes — para cada arquivo de teste entre os alvos, a evidência mostra as linhas que saíram — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-33`; `F-17` (nenhuma lógica reconhece arquivo de teste), `F-18`; relatório `R-12` (`AE-97` e `AE-98` do `P-0754`: a remoção de uma asserção vizinha passou verde).
- **Depende de:** `RAF-T10a`
- **Operação do modelo:** `OP-11` - OP-11: Quem executa faz o dossiê de evidência mostrar, para cada arquivo de teste entre os alvos do card, as linhas que a entrega removeu. - precisa de: dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; roda `git` por subprocesso sem escrever no índice real, na lista de stash nem na árvore de trabalho. A seção nova informa, não julga: o veredito sobre a asserção removida é do revisor pela rubrica (`RAF-T12`), e o dossiê não ganha veredito mecânico novo.
- **Contratos/classes:** quatro regras, com as funções novas logo antes de `def _renderizar(`: 1. `_eh_alvo_de_teste(alvo: str) -> bool` — com separador normalizado (`_normalizar_separador`), verdadeiro quando o caminho começa por `tests/` e o nome do arquivo começa por `test_` e termina em `.py`. 2. `linhas_removidas_de_teste(root: Path, arquivos_alvo: list[str], desde: str | None = None) -> dict[str, list[str]]` — para cada alvo, na ordem, que não é curinga (`_eh_alvo_curinga`) e é de teste: a chave é o alvo como veio, e o valor são as linhas do texto de `_diff_para_arquivo(root, alvo, desde)` que começam por `-` e não por `---`, na ordem. 3. `_renderizar_removidas_de_teste(removidas: dict[str, list[str]]) -> list[str]` — a seção, nesta forma exata: a linha `## Linhas removidas dos testes`; sem chave, a linha `- nenhum arquivo de teste entre os alvos`; por chave sem linha removida, `` ### `<caminho>` — nenhuma linha removida ``; por chave com linhas, `` ### `<caminho>` — <n> linha(s) removida(s) ``, uma linha com três crases, as linhas removidas como vieram e outra linha com três crases. 4. `_renderizar(...)` ganha o parâmetro de palavra-chave `removidas_teste: dict[str, list[str]] | None = None` e põe a seção logo depois dos trechos de diff (depois da linha vazia que fecha a seção de trechos), seguida de uma linha vazia, antes da `## Medida do executor`; `montar_documento` passa `removidas_teste=linhas_removidas_de_teste(root, arquivos_alvo, desde)`.
- **Passos:** 1. Acrescentar ao fim de `tests/test_review_evidence.py` o helper `_repo_com_teste_versionado(tmp_path: Path) -> Path` (repositório de `_init_repo_com_baseline` com `tests/test_a.py` versionado, de três linhas: `def test_a():`, `    assert 1 == 1` e `    assert 2 == 2`) e os três testes da seção `Testes`. 2. Rodar `python -m pytest tests/test_review_evidence.py -q -k removidas_de_teste` e conferir que os três falham. 3. Aplicar as quatro regras de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 3 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Nenhuma linha que já existia em `tests/test_review_evidence.py` sai ou muda: o card só acrescenta ao fim do arquivo. - Os testes montam o próprio repositório em `tmp_path` com `_init_repo_com_baseline`; nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `montar_trechos` nem o teto dos trechos; não julgar a remoção (nenhum veredito novo); não editar `docs/RUBRICA_DE_REVISAO.md` (o critério é da `RAF-T12`).
- **Contingências:** - se um teste que já existia em `tests/test_review_evidence.py` cair por causa da seção nova no documento → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_removidas_de_teste_aparecem_na_evidencia` — `tests/test_a.py` versionado, `ref` capturado, depois a linha `    assert 2 == 2` sai; plano com alvo `tests/test_a.py`; o documento de `montar_documento(..., desde=ref)` tem as linhas `## Linhas removidas dos testes`, `` ### `tests/test_a.py` — 1 linha(s) removida(s) `` e `-    assert 2 == 2` (hoje a seção não existe). TR `test_tr_removidas_de_teste_so_acrescimo_diz_nenhuma` — o arquivo só ganha a linha `    assert 3 == 3`; alvos `tests/test_a.py` e `src/b.py`: o documento tem a linha `` ### `tests/test_a.py` — nenhuma linha removida `` e, depois do título da seção, nenhuma entrada de `src/b.py` (a regra concorrente que listasse todo alvo daria uma entrada para ele). TR `test_tr_removidas_de_teste_sem_alvo_de_teste` — alvo só `src/b.py`: o documento tem a linha `- nenhum arquivo de teste entre os alvos`. Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** o critério da rubrica que reprova a asserção removida (`RAF-T12`); a leitura por `numstat` (o texto do diff já dá as linhas).
- **Handover:** 2026-09-29 · para `RAF-T12` - **Entregue:** review_evidence.py: o dossiê de evidência mostra, para cada arquivo de teste entre os alvos do card, as linhas que a entrega removeu (ver RDO RAF-T11) - **Contrato:** remoção de linha em arquivo de teste-alvo fica visível ao revisor no dossiê - **Não refazer:** a seção de linhas removidas e os testes - **Pendente:** nenhum

## Execução

**Consumo:** 30 tool uses, 81.7 k tokens, 295.8 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

A secao nova se provou no proprio dossie desta entrega: tests/test_review_evidence.py saiu 'nenhuma linha removida', o que confirma mecanicamente a restricao de so acrescentar ao fim do arquivo - a restricao que antes exigia leitura do diff agora se le numa linha.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "O arquivo acentuado já rastreado chega com um nome só ao dossiê de evidência" e vai pegar a tarefa "A evidência mostra as linhas que a entrega tirou dos testes".
Tarefa "A evidência mostra as linhas que a entrega tirou dos testes". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "A evidência mostra as linhas que a entrega tirou dos testes" e vai executar: Quem executa faz o dossiê de evidência mostrar, para cada arquivo de teste entre os alvos do card, as linhas que a entrega removeu.
Agente executor devolveu a tarefa "A evidência mostra as linhas que a entrega tirou dos testes": review — sem pendência.
Tarefa "A evidência mostra as linhas que a entrega tirou dos testes": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A evidência mostra as linhas que a entrega tirou dos testes" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A evidência mostra as linhas que a entrega tirou dos testes": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "A evidência mostra as linhas que a entrega tirou dos testes" como done: registrar estado, RDO e telemetria.
