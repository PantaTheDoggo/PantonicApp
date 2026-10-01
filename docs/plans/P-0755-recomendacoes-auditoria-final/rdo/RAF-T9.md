# RDO — P-0755 · RAF-T9

# Humano

Tarefa "O curinga do alvo casa como na linha de comando" concluída em 2026-09-29.
O curinga dos arquivos-alvo passa a casar como na linha de comando: * não atravessa pasta e ** alcança subpastas.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 15/46 tarefas concluídas; próxima: "O caminho acentuado chega inteiro ao dossiê de evidência".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T9` — O curinga do alvo casa como na linha de comando
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o dossiê de evidência ler o curinga do alvo como a linha de comando o lê, com a estrela presa a uma pasta e a estrela dupla alcançando as subpastas.

**Arquivos-alvo:** - `.claude/tools/review_evidence.py` - `tests/test_review_evidence.py`

**Verificação:** 1. `python -m pytest tests/test_review_evidence.py -q -k glob_estrela` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - dossiê de evidência.curinga do alvo — a estrela fica numa pasta só, e a estrela dupla alcança as subpastas, como na linha de comando — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-31`; `F-1` (Python 3.12: `PurePath.full_match` só existe no 3.13), `F-17` (0 alvos com `*` nos planos vivos); relatório `R-30` (`AE-104` do `P-0754`).
- **Depende de:** `RAF-T8`
- **Operação do modelo:** `OP-9` - OP-9: Quem executa faz o dossiê de evidência ler o curinga do alvo como a linha de comando o lê, com a estrela presa a uma pasta e a estrela dupla alcançando as subpastas. - precisa de: dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; a tradução do curinga é própria, para regex (sem `fnmatch`, sem `glob`, sem `PurePath.full_match`); o curinga casa só contra os arquivos tocados, nunca contra a árvore inteira (`DAU-22` do `P-0754`, inalterada).
- **Contratos/classes:** duas funções novas, logo depois de `_eh_alvo_curinga`: 1. `_curinga_para_regex(padrao: str) -> str` — percorre o padrão da esquerda para a direita: `**/` vira `(?:[^/]*/)*` (zero ou mais pastas); `**` que não é seguido de `/` vira `.*`; `*` vira `[^/]*`; `?` vira `[^/]`; qualquer outro caractere entra com `re.escape`. 2. `_casa_curinga(caminho: str, padrao: str) -> bool` — `re.fullmatch(_curinga_para_regex(padrao), caminho) is not None`. As duas chamadas de `fnmatch.fnmatchcase` (em `confrontar_escopo`, função interna `coberto`, e em `montar_trechos`, no ramo do alvo com curinga) passam a `_casa_curinga`, com os mesmos argumentos, na mesma ordem (caminho normalizado, padrão normalizado); `import fnmatch` sai da lista de imports; o docstring de `_eh_alvo_curinga` troca `fnmatch` por `_casa_curinga`.
- **Passos:** 1. Acrescentar ao fim de `tests/test_review_evidence.py` os dois testes da seção `Testes`. 2. Rodar `python -m pytest tests/test_review_evidence.py -q -k glob_estrela` e conferir que os dois falham. 3. Aplicar `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 2 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A); os testes do curinga da `AUF-T3` (`test_tf_alvo_com_curinga_casa_os_tocados`, `test_tr_alvo_com_curinga_sem_tocado_diz_que_nada_casa`) seguem verdes sem mudança. - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Nenhuma linha que já existia em `tests/test_review_evidence.py` sai ou muda: o card só acrescenta ao fim do arquivo. - Os testes montam o próprio repositório em `tmp_path` com `_init_repo_com_baseline`; nenhum `git stash push`, `git add` sobre o índice real, `git reset --hard` nem `git clean`. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não expandir o curinga contra a árvore inteira; não mudar `_eh_alvo_curinga`, `_CAMINHO_RE` nem `_tarefa_dona`; não aceitar `[`, `]` ou `{` como curinga (entram como literal).
- **Contingências:** - se um teste que já existia em `tests/test_review_evidence.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_glob_estrela_nao_atravessa_pasta` — `relatorios/a.md` e `relatorios/sub/x.md` criados depois do `ref`, alvo `relatorios/*.md`: `confrontar_escopo(tocados, ["relatorios/*.md"], repo)["fora_dos_alvos"]` é `["relatorios/sub/x.md"]` e as chaves de `montar_trechos(repo, ["relatorios/*.md"], 4000, tocados, desde=ref)` são só `relatorios/a.md` (hoje o `fnmatch` casa os dois). TF `test_tf_glob_estrela_dupla_alcanca_subpastas` — os mesmos arquivos, alvo `relatorios/**/*.md`: `fora_dos_alvos` é `[]` e as chaves são `relatorios/a.md` e `relatorios/sub/x.md` (hoje o `fnmatch` deixa `relatorios/a.md` de fora, porque exige uma `/` depois de `relatorios/`). Suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** o curinga no alvo de outra tarefa do mesmo plano (`_tarefa_dona`, não pedido pela `R-30`); o caminho acentuado (`RAF-T10`).
- **Handover:** 2026-09-29 · para quem vier depois - **Entregue:** review_evidence.py: _curinga_para_regex e _casa_curinga substituem fnmatch.fnmatchcase em confrontar_escopo e montar_trechos (* não atravessa pasta, ** alcança subpastas); 2 testes novos, suíte 554 - **Contrato:** curinga de Arquivos-alvo casa como na linha de comando - **Não refazer:** _casa_curinga e os 2 testes - **Pendente:** nenhum

## Execução

**Consumo:** 28 tool uses, 71.9 k tokens, 294.5 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Exercicio ponta a ponta em montagem descartavel: main() com alvo relatorios/*.md, relatorios/**/*.md e relatorios\*.md da atribuicao na lista de Arquivos tocados, fato de escopo e chaves de trecho coerentes entre si; 22 casos de borda da traducao (**/ no inicio, ** no fim, ?, [ e { literais) casam como o card especifica, e divergem do fnmatch exatamente onde o R-30 apontava.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "A rubrica nomeia o rótulo do registro da orquestração" e vai pegar a tarefa "O curinga do alvo casa como na linha de comando".
Tarefa "O curinga do alvo casa como na linha de comando". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O curinga do alvo casa como na linha de comando" e vai executar: Quem executa faz o dossiê de evidência ler o curinga do alvo como a linha de comando o lê, com a estrela presa a uma pasta e a estrela dupla alcançando as subpastas.
Agente executor devolveu a tarefa "O curinga do alvo casa como na linha de comando": review — sem pendência.
Tarefa "O curinga do alvo casa como na linha de comando": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O curinga do alvo casa como na linha de comando" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O curinga do alvo casa como na linha de comando": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O curinga do alvo casa como na linha de comando" como done: registrar estado, RDO e telemetria.
