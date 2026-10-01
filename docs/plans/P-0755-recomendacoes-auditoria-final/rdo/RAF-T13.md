# RDO — P-0755 · RAF-T13

# Humano

Tarefa "A conferência do card compara o depois com o esperado e lê o literal com pontuação" concluída em 2026-09-29.
A conferência do card passa a comparar o mundo depois com o esperado declarado e a ler o literal com pontuação.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 23/50 tarefas concluídas; próxima: "A conferência do card roda o git de leitura contra o recorte do despacho".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T13` — A conferência do card compara o depois com o esperado e lê o literal com pontuação
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz a conferência de verificação do card comparar com o resultado que o card escreve, também no bloco cercado medido depois da entrega e no literal com pontuação.

**Arquivos-alvo:** - `.claude/tools/card_check.py` - `tests/test_card_check.py`

**Verificação:** 1. `python -m pytest tests/test_card_check.py -q -k bloco_cercado_mundo` → `exit 0` — antes `exit 5`, depois `exit 0` 2. `python -m pytest tests/test_card_check.py -q -k par_com_crase` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - conferência de verificação do card.resultado esperado no bloco cercado — é comparada com o resultado que o card escreve para depois da entrega — Verificação 1 - conferência de verificação do card.literal com pontuação — o valor entre crases é lido inteiro, só depois do comando; o card antigo continua lido como antes — Verificação 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-13` (i) e (ii); `F-14`, `F-16` (um único par real com pontuação no literal, `docs/plans/P-0753-auditoria-estagio-1/plano.md` linha 434); relatório `R-09`, `R-10`.
- **Depende de:** `RAF-T7`
- **Operação do modelo:** `OP-13` - OP-13: Quem executa faz a conferência de verificação do card comparar com o resultado que o card escreve, também no bloco cercado medido depois da entrega e no literal com pontuação. - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/card_check.py`, só biblioteca padrão; carrega `rdo.py` e `caminhos.py` por caminho; roda o comando publicado por `subprocess.run` sem `shell=True`, como hoje. O card cobre as duas recomendações da operação (`R-09` e `R-10`) no mesmo arquivo. A forma normativa do bloco `Verificação` (`docs/RUBRICA_DE_REVISAO.md` §8.1, Formas A e B) não muda de texto; o card antigo continua lido como antes. O contrato do objeto é: "Quem implementa amplia o que a conferência aceita sem deixar de ler os cards já escritos na forma antiga."
- **Contratos/classes:** `verificar_tarefa(plano: Path, tarefa_id: str, root: Path, mundo: str | None = None) -> tuple[bool, list[str], dict]` e `main` — assinaturas inalteradas. Três regras: 1. Forma de bloco cercado (`forma="8.1"`), `R-09`: depois das checagens de presença de hoje (comando, `→`, `Medido antes`), com `mundo == "depois"` o valor comparado é o literal do esperado — função nova `_literal_do_esperado(esperado: str) -> str | None`: o primeiro negrito `**<valor>**` do esperado (regex nova `_NEGRITO_RE = re.compile(r"\*\*(?P<val>[^*]+?)\*\*")`, valor sem espaços nas pontas); sem negrito, o primeiro trecho entre crases (`_CRASE_RE`); sem nenhum, `None` → falha `item <n>: esperado sem literal` e o item não roda. A divergência no mundo `depois` sai `item <n>: divergencia - esperado (depois) declara '<valor>', execução mediu exit <x> saída '<saída>'`. Com `mundo == "antes"`, tudo como hoje: compara `Medido antes`, e a divergência segue `item <n>: divergencia - Medido antes declara '<valor>', ...`. A comparação segue `_bate_com_medido` (`exit N` compara o código; outro valor, substring de stdout mais stderr). 2. Forma inline, `R-10`: o par `antes`/`depois` é procurado só no trecho que começa no primeiro `→` depois do comando (sem `→`, no resto do item, como hoje), primeiro pela regex nova `_ANTES_DEPOIS_CRASE_RE = re.compile(r"antes\s+`(?P<antes>[^`]*)`\s*[,;]?\s*depois\s+`(?P<depois>[^`]*)`")`, que aceita `,`, `;` e `.` dentro do literal; sem par com crase, pela `_ANTES_DEPOIS_RE` de hoje (legado), no mesmo trecho. 3. O docstring de `verificar_tarefa` troca a frase que diz que o mundo só afeta a forma inline pela regra 1.
- **Passos:** 1. Acrescentar ao fim de `tests/test_card_check.py` os helpers `_plano_com_item(tmp_path: Path, item: str) -> Path` (plano sintético em `tmp_path/plano.md` com o card `RX-T1`, campos `Objetivo`, `Entregável`, `Verificação` com o item dado e `Pronto quando`), `_bloco(valor_impresso: str, esperado: str, medido_antes: str) -> str` (item de bloco cercado com `python -c "print('<valor_impresso>')"`, a linha `→ <esperado>. **Medido antes: <medido_antes>**`) e `_rodar(card_check, plano: Path, mundo: str) -> int` (`main` com `--tarefa RX-T1`, `--root` na raiz do repositório e `--mundo`), e os sete testes da seção `Testes`. 2. Rodar `python -m pytest tests/test_card_check.py -q -k "bloco_cercado_mundo or par_com_crase"` e conferir que os cinco TF falham e os dois TR passam. 3. Aplicar as três regras de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 7 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Nenhuma linha que já existia em `tests/test_card_check.py` sai ou muda: o card só acrescenta ao fim do arquivo; as fixtures de `tests/fixtures/card_check/` não mudam. - O `card_check` deste plano continua saindo 0 sobre os cards `RAF-T1`..`RAF-T18` com a regra nova: todos usam o par com crase depois do `→`. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `_ANTES_DEPOIS_RE` (legado), `_SETA_INLINE_RE`, `_SETA_RE` nem `_MEDIDO_ANTES_RE`; não mudar a lista de programas aceitos nem a troca de `<ref>` (é da `RAF-T14`); não mudar `--gravar` nem `caminhos.destino_medida` (é da `RAF-T15`); não editar `docs/RUBRICA_DE_REVISAO.md`.
- **Contingências:** - se um teste que já existia em `tests/test_card_check.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_bloco_cercado_mundo_depois_compara_com_o_esperado` — bloco que imprime `a`, esperado `imprime **b**`, `Medido antes: a`: `--mundo depois` sai 1 com `divergencia - esperado (depois) declara 'b'` no stderr (hoje sai 0, comparando `a`); o mesmo bloco imprimindo `b` sai 0 com `--mundo depois` (hoje sai 1). TR `test_tr_bloco_cercado_mundo_antes_segue_com_o_medido` — imprimindo `a`, `--mundo antes` sai 0; imprimindo `b`, sai 1 com `divergencia - Medido antes declara 'a'`. TF `test_tf_bloco_cercado_mundo_depois_sem_literal_falha` — esperado `imprime o valor`, sem negrito nem crase: `--mundo depois` sai 1 com `item 1: esperado sem literal`. TF `test_tf_par_com_crase_depois_aceita_ponto` — item inline `` `python -c "print('a.txt: 2')"` → `a.txt: 3` — antes `a.txt: 2`, depois `a.txt: 3` ``: `--mundo antes` sai 0; `--mundo depois` sai 1 com `declara 'a.txt: 3'` (hoje a regex corta o literal em `a` e sai 0). TF `test_tf_par_com_crase_antes_aceita_virgula` — antes `x, y` com o comando imprimindo `x; z`: `--mundo antes` sai 1 com `divergencia - valor do mundo (antes) declara 'x, y'` (hoje sai 1 com `sem valor antes`); imprimindo `x, y`, sai 0. TF `test_tf_par_com_crase_so_depois_da_seta` — item `` `python -c "print('a')"` (nota: antes `z`, depois `z`) → `a` — antes `a`, depois `a` ``: `--mundo antes` sai 0 (hoje lê o par da nota e sai 1). TR `test_tr_par_com_crase_legado_sem_crase_segue_lido` — item `` `python -c "print(2)"` → 3 — antes 2, depois 3 ``, sem crase no par: `--mundo antes` sai 0 e `--mundo depois` sai 1. Suíte `tests/test_card_check.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** o `git` de leitura, o `<ref>` no comando e a linha de invariância (`RAF-T14`); a pasta e o nome da medida gravada (`RAF-T15`); reescrever o par da linha 434 do plano `P-0753` (fora do alcance de todo card, §4 invariante 7).
- **Handover:** 2026-09-29 · para `RAF-T14` - **Entregue:** card_check.py: no mundo depois, bloco cercado compara com o literal do esperado (negrito ou crase; sem literal falha 'esperado sem literal'); par antes/depois com crase lido só depois da primeira →, aceita pontuação; 7 testes novos, suíte 573 - **Contrato:** RAF-T1..RAF-T18 seguem saindo 0 no card_check; mundo antes segue com o Medido antes - **Não refazer:** _literal_do_esperado, _NEGRITO_RE, _ANTES_DEPOIS_CRASE_RE e os testes - **Pendente:** nenhum

## Execução

**Consumo:** 44 tool uses, 137.1 k tokens, 757.4 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

A prova de TDD reproduzida pelo reviewer numa copia fora do repositorio (card_check.py do ref e0043041 + os testes novos) deu 5 TF vermelhos e 2 TR verdes, exatamente como o Passo 2 pede: a prova nao precisa de git stash na arvore real. Exercicio ponta a ponta (plano sintetico fora do repo): forma 8.1 em --mundo depois com negrito 'exit 3' compara o codigo, crase com ponto/virgula/ponto-e-virgula casa inteiro, esperado sem literal falha nomeado, --gravar grava a medida; nenhum card real de docs/plans/ tem item 8.1 com esperado sem literal (327 itens, 0 reais), entao a regra nova nao quebra card ja escrito.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "A dimensão testes declara a fonte mista e o instrumento cita a rubrica pela seção" e vai pegar a tarefa "A conferência do card compara o depois com o esperado e lê o literal com pontuação".
Tarefa "A conferência do card compara o depois com o esperado e lê o literal com pontuação". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "A conferência do card compara o depois com o esperado e lê o literal com pontuação" e vai executar: Quem executa faz a conferência de verificação do card comparar com o resultado que o card escreve, também no bloco cercado medido depois da entrega e no literal com pontuação.
Agente executor devolveu a tarefa "A conferência do card compara o depois com o esperado e lê o literal com pontuação": review — sem pendência.
Tarefa "A conferência do card compara o depois com o esperado e lê o literal com pontuação": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A conferência do card compara o depois com o esperado e lê o literal com pontuação" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A conferência do card compara o depois com o esperado e lê o literal com pontuação": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "A conferência do card compara o depois com o esperado e lê o literal com pontuação" como done: registrar estado, RDO e telemetria.
