# RDO — P-0755 · RAF-T7a

# Humano

Tarefa "O ramo que o conteúdo antigo não texto nunca alcança sai do dossiê de evidência" concluída em 2026-09-29.
O dossiê de evidência perde as duas comparações que nunca podiam dar verdadeiro.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 12/45 tarefas concluídas; próxima: "O binário novo leva a marca de novo e o registro da orquestração tem um nome só".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T7a` — O ramo que o conteúdo antigo não texto nunca alcança sai do dossiê de evidência
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa tira de `.claude/tools/review_evidence.py` as duas comparações de bytes que a `RAF-T7` pôs no ramo em que o conteúdo do `ref` não se lê como texto e o de hoje se lê: os bytes de hoje decodificam em UTF-8 e os do `ref` não, logo nunca são iguais; a comparação de `_diff_para_arquivo` guarda um retorno inalcançável e a de `_nao_rastreado_mudou_desde_ref` é sempre verdadeira.

**Arquivos-alvo:** - `.claude/tools/review_evidence.py`

**Verificação:** 1. `python -c "import pathlib,sys; t=pathlib.Path('.claude/tools/review_evidence.py').read_text(encoding='utf-8'); n=t.count('_bytes_do_ref('); print(n); sys.exit(0 if n==3 else 1)"` → `exit 0` — antes `exit 1`, depois `exit 0` (imprime `5` antes e `3` depois)

**Pronto quando:** - dossiê de evidência.casos em que hoje quebra — o conteúdo antigo que não se lê como texto sai como binário, sem a comparação de bytes que nunca iguala — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-49`; `AE-135` (laudo da `RAF-T7`, ressalva 91); `DRF-11`; relatório `R-13`.
- **Depende de:** `RAF-T7`
- **Operação do modelo:** `OP-7` - OP-7: Quem executa faz o dossiê de evidência chegar ao fim nos três casos em que hoje quebra: conteúdo antigo que não se lê como texto, módulo de apoio ausente e medida guardada em outra pasta. - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; despacho de tarefa — Quem implementa recebe o comando que hoje imprime tudo na tela de quem conduz e o faz gravar o pacote da tarefa num arquivo fora do versionamento, imprimindo só o recado ao executor.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/review_evidence.py`, só biblioteca padrão; roda `git` por subprocesso sem escrever no índice real, na lista de stash nem na árvore de trabalho. O comportamento observável não muda: em todo caso alcançável, os dois ramos já devolvem o que passam a devolver sem a comparação. O contrato do objeto é: "Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável."
- **Contratos/classes:** assinaturas inalteradas. Duas regras, as duas no ramo `if texto_ref is None:`, que só se alcança com o arquivo de hoje decodificado em UTF-8 (`_texto_do_disco` não devolveu `None`) e o conteúdo do `ref` não decodificável: 1. `_diff_para_arquivo`, bloco do `TK-93a`: o ramo devolve direto `(arquivo binário ou não-UTF-8 — trecho omitido)`; saem a linha `if _bytes_do_ref(root, desde, caminho_rel) == (root / caminho_rel).read_bytes():` e o `return` que ela guardava. 2. `_nao_rastreado_mudou_desde_ref`: o ramo devolve `True` no lugar de `return _bytes_do_ref(root, ref, caminho) != (root / caminho).read_bytes()`. `_bytes_do_ref` segue com dois chamadores: `_texto_do_ref_ou_none` e o ramo de `_nao_rastreado_mudou_desde_ref` em que o arquivo de hoje não se lê como texto.
- **Passos:** 1. Rodar a Verificação 1 e conferir que imprime `5` e sai 1. 2. Aplicar as duas regras de `Contratos/classes`. 3. Rodar a Verificação, `python -m pytest tests/test_review_evidence.py -q -k quebra` e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e não soma teste novo (referência datada: `83 passed` em `tests/test_review_evidence.py`, 2026-09-29, depois da `RAF-T7`). - Os cinco testes `quebra` da `RAF-T7` seguem verdes; `test_tf_quebra_ref_binario_hoje_texto_compara_bytes` passa pelos dois ramos. - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `_texto_do_ref_ou_none`, `_bytes_do_ref`, `_texto_do_disco` nem o ramo em que o arquivo de hoje não se lê como texto; não mexer na marca de arquivo novo nem nos rótulos da lista (é da `RAF-T8`); não acrescentar nem mudar teste.
- **Contingências:** - se um teste de `tests/test_review_evidence.py` cair depois do passo 2 → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo: o retorno que sai é inalcançável por construção e nenhum teste o exercita; a prova é a inspeção mecânica da Verificação 1 (item 12(ii) da Fase 4 do planejador). Regressão: os cinco testes `quebra` da `RAF-T7`, a suíte `tests/test_review_evidence.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** a marca do binário novo e o rótulo único (`RAF-T8`); o fim de linha da árvore de trabalho (medido em 2026-09-29: mais de cem arquivos rastreados `w/crlf` contra `eol=lf`, este entre eles).
- **Handover:** 2026-09-29 · para `RAF-T8` - **Entregue:** review_evidence.py: ramos texto_ref None de _diff_para_arquivo e _nao_rastreado_mudou_desde_ref sem a comparação de bytes inalcançável (_bytes_do_ref( conta 3); suíte 549 - **Contrato:** conteúdo antigo não texto: trecho omitido e arquivo tratado como mudado, sem git show a mais - **Não refazer:** a remoção dos dois ramos - **Pendente:** nenhum

## Execução

**Consumo:** 15 tool uses, 55.3 k tokens, 167.9 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Reconciliacao por construcao: com _texto_do_disco devolvendo texto (bytes de hoje decodificam em UTF-8) e _texto_do_ref_ou_none devolvendo None (bytes do ref nao decodificam), os bytes nunca igualam - as duas comparacoes removidas eram de fato constantes, e o comportamento observavel nao muda. Verificacao 1 rodada nos dois mundos: 5 no ref 0ac4f75, 3 na arvore, exit 0. Os 5 testes quebra (inclusive test_tf_quebra_ref_binario_hoje_texto_compara_bytes, que atravessa coletar_arquivos_tocados e montar_trechos, isto e, os dois ramos editados) seguem verdes; tests/test_review_evidence.py intocado.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "O dossiê de evidência chega ao fim nos três casos em que quebrava" e vai pegar a tarefa "O ramo que o conteúdo antigo não texto nunca alcança sai do dossiê de evidência".
Tarefa "O ramo que o conteúdo antigo não texto nunca alcança sai do dossiê de evidência". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O ramo que o conteúdo antigo não texto nunca alcança sai do dossiê de evidência" e vai executar: Quem executa tira de `.claude/tools/review_evidence.py` as duas comparações de bytes que a `RAF-T7` pôs no ramo em que o conteúdo do `ref` não se lê como texto e o de hoje se lê: os bytes de hoje decodificam em UTF-8 e os do `ref` não, log…
Agente executor devolveu a tarefa "O ramo que o conteúdo antigo não texto nunca alcança sai do dossiê de evidência": review — sem pendência.
Tarefa "O ramo que o conteúdo antigo não texto nunca alcança sai do dossiê de evidência": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O ramo que o conteúdo antigo não texto nunca alcança sai do dossiê de evidência" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O ramo que o conteúdo antigo não texto nunca alcança sai do dossiê de evidência": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O ramo que o conteúdo antigo não texto nunca alcança sai do dossiê de evidência" como done: registrar estado, RDO e telemetria.
