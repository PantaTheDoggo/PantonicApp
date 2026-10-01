# RDO — P-0755 · RAF-T11a

# Humano

Tarefa "A seção das linhas removidas cobre o teste sob curinga ou diretório e a linha que começa por dois hífens" concluída em 2026-09-29.
A seção das linhas removidas dos testes passa a cobrir teste sob curinga ou diretório e a linha que começa por dois hífens.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 20/49 tarefas concluídas; próxima: "A rubrica reprova a asserção de teste removida sem ordem do card".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T11a` — A seção das linhas removidas cobre o teste sob curinga ou diretório e a linha que começa por dois hífens
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz a seção `## Linhas removidas dos testes` do dossiê de evidência mostrar também o arquivo de teste que um alvo curinga ou diretório cobre e a linha removida cujo conteúdo começa por `--`.

**Arquivos-alvo:** - `.claude/tools/review_evidence.py` - `tests/test_review_evidence.py`

**Verificação:** 1. `python -m pytest tests/test_review_evidence.py -q -k "removidas_de_teste and (curinga or hifens or diretorio)"` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - dossiê de evidência.linhas removidas dos testes — o arquivo de teste coberto por alvo curinga ou diretório e a linha removida que começa por `--` aparecem na seção — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-53`; `AE-149` (laudo da `RAF-T11`, ressalva 91); `DRF-33`; `F-17`; relatório `R-12`.
- **Depende de:** `RAF-T11`
- **Operação do modelo:** `OP-11` - OP-11: Quem executa faz o dossiê de evidência mostrar, para cada arquivo de teste entre os alvos do card, as linhas que a entrega removeu. - precisa de: dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; roda `git` por subprocesso sem escrever no índice real, na lista de stash nem na árvore de trabalho. A forma da seção (`_renderizar_removidas_de_teste`) não muda; muda quais arquivos entram nela e quais linhas contam como removidas. A seção informa, não julga.
- **Contratos/classes:** três regras em `.claude/tools/review_evidence.py`: 1. `_linhas_removidas_do_diff(texto: str) -> list[str]`, nova, logo antes de `def linhas_removidas_de_teste(` — as linhas do texto que começam por `-` e vêm depois da primeira linha que começa por `@@`, na ordem; texto sem linha `@@` dá lista vazia. O cabeçalho (`--- a/...`) fica antes do primeiro `@@` e sai; a linha removida cujo conteúdo começa por `--` fica. 2. `linhas_removidas_de_teste(root: Path, arquivos_alvo: list[str], desde: str | None = None, tocados: list[str] | None = None) -> dict[str, list[str]]` — para cada alvo, na ordem, os caminhos que ele cobre, pela mesma expansão de `montar_trechos`: alvo curinga (`_eh_alvo_curinga`) cobre os `tocados` que casam por `_casa_curinga` (separador normalizado nos dois lados); alvo diretório (`tocados` não vazio e `_eh_alvo_diretorio`) cobre os `tocados` sob o prefixo `<alvo>/` normalizado; outro alvo cobre a si mesmo, como veio. Cada caminho coberto que é de teste (`_eh_alvo_de_teste`) e cuja forma normalizada (`_normalizar_separador`) ainda não tem chave ganha a chave do caminho como veio e o valor `_linhas_removidas_do_diff(_diff_para_arquivo(root, caminho, desde))`. O docstring deixa de dizer que o curinga fica de fora e que o filtro é o de `---`. 3. `montar_documento` passa os tocados que já coleta: `removidas_teste=linhas_removidas_de_teste(root, arquivos_alvo, desde, tocados)`.
- **Passos:** 1. Acrescentar ao fim de `tests/test_review_evidence.py` o helper `_secao_removidas(documento: str) -> str` (o trecho do documento depois de `## Linhas removidas dos testes` e antes de `## Medida do executor`) e os quatro testes da seção `Testes`. 2. Rodar a Verificação 1 e conferir `3 failed, 1 passed` (o TR passa antes). 3. Aplicar as três regras de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 4 testes novos (referência datada: `562 passed`, 2026-09-29, revisão da `RAF-T11`). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Nenhuma linha que já existia em `tests/test_review_evidence.py` sai ou muda: o card só acrescenta ao fim do arquivo. - Os testes montam o próprio repositório em `tmp_path` com `_repo_com_teste_versionado`; o `add` e o `commit` do TF dos dois hífens rodam por `_run_git` só nesse repositório; nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `montar_trechos`, `_renderizar_removidas_de_teste` nem os textos da seção; não julgar a remoção (nenhum veredito novo); não editar `docs/RUBRICA_DE_REVISAO.md` (o critério é da `RAF-T12`).
- **Contingências:** - se um teste que já existia em `tests/test_review_evidence.py` cair por causa da mudança → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_removidas_de_teste_curinga_cobre_teste_tocado` — repositório de `_repo_com_teste_versionado`, `ref` capturado, depois a linha `    assert 2 == 2` sai; plano com alvo `tests/test_*.py`; a seção (`_secao_removidas`) tem `` ### `tests/test_a.py` — 1 linha(s) removida(s) `` e `-    assert 2 == 2`, e não tem `- nenhum arquivo de teste entre os alvos` (hoje o curinga é pulado e a seção diz isso). TF `test_tf_removidas_de_teste_diretorio_cobre_teste_tocado` — o mesmo, com alvo `tests/` (hoje o diretório não é arquivo de teste e é pulado). TF `test_tf_removidas_de_teste_linha_que_comeca_por_dois_hifens` — `tests/test_a.py` ganha a quarta linha `--sep--`, commitada no repositório de `tmp_path`; `ref` capturado; a linha `--sep--` sai; alvo `tests/test_a.py`; a seção tem `` ### `tests/test_a.py` — 1 linha(s) removida(s) `` e, entre as suas linhas, `---sep--` (hoje o filtro de `---` a apaga com o cabeçalho e a seção diz `nenhuma linha removida`). TR `test_tr_removidas_de_teste_alvo_e_curinga_uma_entrada` — alvos `tests/test_a.py` e `tests/test_*.py`, a linha `    assert 2 == 2` sai: a seção tem uma só ocorrência de `` ### `tests/test_a.py` `` (a regra concorrente que expandisse o curinga sem conferir as chaves já postas daria duas). Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** a linha `- nenhum arquivo de teste entre os alvos`, que passa a ler os alvos expandidos (nenhum tocado de teste coberto, nenhuma remoção a mostrar); o critério da rubrica (`RAF-T12`).
- **Handover:** 2026-09-29 · para `RAF-T12` - **Entregue:** review_evidence.py: linhas_removidas_de_teste(…, tocados) expande alvo curinga ou diretório contra os tocados (uma chave por arquivo); _linhas_removidas_do_diff conta só linhas '-' depois do primeiro @@; 4 testes novos, suíte 566 - **Contrato:** a seção '## Linhas removidas dos testes' cobre teste sob curinga ou diretório e não perde linha que começa por '--' - **Não refazer:** a expansão dos alvos e o parser do diff - **Pendente:** nenhum

## Execução

**Consumo:** 28 tool uses, 91.3 k tokens, 336.4 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Exercicio ponta a ponta em repositorio descartavel (alvos tests\test_*.py com barra invertida, tests/**/test_*.py, alvo exato com barra invertida mais curinga, src/*.py, arquivo de teste apagado, nao rastreado presente no ref, nao rastreado novo cujo conteudo tem linha '@@' e linha '-'): cobertura, dedupe por forma normalizada e a linha '---sep--' saem como o card fixa; o arquivo novo com '@@' no conteudo sai 'nenhuma linha removida', porque a regra ancora no primeiro '@@' do diff e nao no conteudo. Alvo diretorio sem barra final ('tests') nao chega a expandir: o parser do plano o descarta como literal nao reconhecido, fato pre-existente e visivel no proprio dossie (Literais nao reconhecidos) - o card usa 'tests/'. A propria secao nova confirma a restricao de so acrescentar: tests/test_review_evidence.py saiu 'nenhuma linha removida'.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "A evidência mostra as linhas que a entrega tirou dos testes" e vai pegar a tarefa "A seção das linhas removidas cobre o teste sob curinga ou diretório e a linha que começa por dois hífens".
Tarefa "A seção das linhas removidas cobre o teste sob curinga ou diretório e a linha que começa por dois hífens". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "A seção das linhas removidas cobre o teste sob curinga ou diretório e a linha que começa por dois hífens" e vai executar: Quem executa faz a seção `## Linhas removidas dos testes` do dossiê de evidência mostrar também o arquivo de teste que um alvo curinga ou diretório cobre e a linha removida cujo conteúdo começa por `--`.
Agente executor devolveu a tarefa "A seção das linhas removidas cobre o teste sob curinga ou diretório e a linha que começa por dois hífens": review — sem pendência.
Tarefa "A seção das linhas removidas cobre o teste sob curinga ou diretório e a linha que começa por dois hífens": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A seção das linhas removidas cobre o teste sob curinga ou diretório e a linha que começa por dois hífens" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A seção das linhas removidas cobre o teste sob curinga ou diretório e a linha que começa por dois hífens": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "A seção das linhas removidas cobre o teste sob curinga ou diretório e a linha que começa por dois hífens" como done: registrar estado, RDO e telemetria.
