# RDO — P-0755 · RAF-T9a

# Humano

Tarefa "O teste do curinga da AUF-T3 nomeia o mecanismo que casa o alvo" concluída em 2026-09-29.
O teste do curinga passa a nomear o mecanismo que de fato casa o alvo.
Revisão: aprovada com ressalva (88%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 16/47 tarefas concluídas; próxima: "O caminho acentuado chega inteiro ao dossiê de evidência".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T9a` — O teste do curinga da AUF-T3 nomeia o mecanismo que casa o alvo
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o docstring de `test_tf_alvo_com_curinga_casa_os_tocados`, em `tests/test_review_evidence.py`, nomear `_casa_curinga`, que a `RAF-T9` pôs no lugar do `fnmatch`, em vez de dizer que o curinga casa por `fnmatch`.

**Arquivos-alvo:** - `tests/test_review_evidence.py`

**Verificação:** 1. `python -c "import pathlib,sys; t=pathlib.Path('tests/test_review_evidence.py').read_text(encoding='utf-8'); q=chr(96); a=t.count('por '+q+'fnmatch'+q); d=t.count('por '+q+'_casa_curinga'+q+' (RAF-T9)'); print('docstring=%d-%d'%(a,d)); sys.exit(0 if (a,d)==(0,1) else 1)"` → `exit 0` — antes `exit 1`, depois `exit 0` (imprime `docstring=1-0` antes e `docstring=0-1` depois)

**Pronto quando:** - dossiê de evidência.curinga do alvo — o teste do curinga da `AUF-T3` nomeia o mecanismo que casa o alvo, `_casa_curinga` — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-51`; `AE-140` (laudo da `RAF-T9`, ressalva 91); `DRF-31`; relatório `R-30`.
- **Depende de:** `RAF-T9`
- **Operação do modelo:** `OP-9` - OP-9: Quem executa faz o dossiê de evidência ler o curinga do alvo como a linha de comando o lê, com a estrela presa a uma pasta e a estrela dupla alcançando as subpastas. - precisa de: dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** teste do instrumento do kit, `tests/test_review_evidence.py`, só o docstring do teste da `AUF-T3`; nenhum código nem asserção muda. A `RAF-T9` congelou as linhas que já existiam no arquivo e mandou trocar só o docstring de `_eh_alvo_curinga`; este é o outro texto que a entrega dela tornou falso.
- **Passos:** 1. No teste `test_tf_alvo_com_curinga_casa_os_tocados`, trocar as três linhas do docstring pelas três do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card e guarda os quatro espaços do corpo da função; o resto do teste não muda). Texto antigo: ```text """AUF-T3: alvo com curinga (`relatorios/*.md`) casa, por `fnmatch`, cada tocado que bate com o padrão — não a regra antiga, que descartava o literal e dava os dois arquivos como fora dos alvos com uma entrada só sob a chave do padrão.""" ``` Texto novo: ```text """AUF-T3: alvo com curinga (`relatorios/*.md`) casa, por `_casa_curinga` (RAF-T9), cada tocado que bate com o padrão — não a regra antiga, que descartava o literal e dava os dois arquivos como fora dos alvos com uma entrada só sob a chave do padrão.""" ``` 2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `88 passed` em `tests/test_review_evidence.py`, 2026-09-29, depois da `RAF-T9`). - `test_tf_alvo_com_curinga_casa_os_tocados` e `test_tr_alvo_com_curinga_sem_tocado_diz_que_nada_casa` seguem verdes. - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Em `tests/test_review_evidence.py`, as únicas linhas que mudam são as três do docstring do passo 1. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não editar `.claude/tools/review_evidence.py`; não mudar os docstrings dos dois testes `glob_estrela` da `RAF-T9` (o "hoje" deles nomeia a regra concorrente na data da autoria, convenção dos docstrings de teste do kit).
- **Contingências:** - se o texto antigo do passo 1 não existir verbatim em `tests/test_review_evidence.py` → parar e sinalizar `blocked` razão `premissa`. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo: a mudança é de redação e a prova é o recorte do literal na Verificação 1. Regressão: o teste da `AUF-T3`, a suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** o caminho acentuado (`RAF-T10`); o fim de linha do arquivo (medido 2026-09-29: `w/crlf` contra `eol=lf`, fora do P-0755).
- **Handover:** 2026-09-29 · para `RAF-T10` - **Entregue:** docstring de test_tf_alvo_com_curinga_casa_os_tocados (tests/test_review_evidence.py:1459-1461) cita _casa_curinga (RAF-T9) no lugar de fnmatch - **Contrato:** nenhum docstring de teste-alvo nomeia o fnmatch como mecanismo vigente - **Não refazer:** a troca do docstring - **Pendente:** nenhum

## Execução

**Consumo:** 13 tool uses, 65.3 k tokens, 157.8 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 88%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "O curinga do alvo casa como na linha de comando" e vai pegar a tarefa "O teste do curinga da AUF-T3 nomeia o mecanismo que casa o alvo".
Tarefa "O teste do curinga da AUF-T3 nomeia o mecanismo que casa o alvo". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O teste do curinga da AUF-T3 nomeia o mecanismo que casa o alvo" e vai executar: Quem executa faz o docstring de `test_tf_alvo_com_curinga_casa_os_tocados`, em `tests/test_review_evidence.py`, nomear `_casa_curinga`, que a `RAF-T9` pôs no lugar do `fnmatch`, em vez de dizer que o curinga casa por `fnmatch`.
Agente executor devolveu a tarefa "O teste do curinga da AUF-T3 nomeia o mecanismo que casa o alvo": review — sem pendência.
Tarefa "O teste do curinga da AUF-T3 nomeia o mecanismo que casa o alvo": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O teste do curinga da AUF-T3 nomeia o mecanismo que casa o alvo" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O teste do curinga da AUF-T3 nomeia o mecanismo que casa o alvo": ressalva 88%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O teste do curinga da AUF-T3 nomeia o mecanismo que casa o alvo" como done: registrar estado, RDO e telemetria.
