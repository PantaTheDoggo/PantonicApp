# RDO — P-0755 · RAF-T21

# Humano

Tarefa "A conferência do modelo recusa o card que copia a operação com outro texto" concluída em 2026-09-29.
A conferência do modelo passa a recusar o card que copia a operação com outro texto.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 33/52 tarefas concluídas; próxima: "A diferença entre versões mostra a operação inserida, a renumerada e a propriedade nova".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T21` — A conferência do modelo recusa o card que copia a operação com outro texto
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz a conferência do modelo recusar o card cujo texto copiado da operação difere do texto da versão que ele cita.

**Arquivos-alvo:** - `.claude/tools/modelo.py` - `tests/test_modelo.py`

**Verificação:** 1. `python -m pytest tests/test_modelo.py -q -k texto_divergente` → `exit 0` — antes `exit 5`, depois `exit 0`

**Pronto quando:** - conferência do modelo.fidelidade do texto copiado no card — recusa o card cujo texto copiado diverge da versão que ele cita — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-15`, `DRF-37`, `DRF-61`; `F-19` (vocabulário `V1`..`V21`; `V4` e `V14` julgam o card; nenhum confere o texto copiado); relatório `R-06` (auditoria reg. 36 e 37: o `check` aprovou card com texto de operação divergente).
- **Depende de:** `RAF-T19`, `RAF-T19a`
- **Operação do modelo:** `OP-21` - OP-21: Quem executa faz a conferência do modelo recusar o card cujo texto copiado da operação difere do texto da versão que ele cita. - precisa de: conferência do modelo — Quem implementa acrescenta à conferência o que cada operação pede, sem mudar o que ela já julga quando chamada como hoje.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/modelo.py`, função `validar`; só biblioteca padrão. A violação nova julga o card contra a versão que ele cita: a operação citada pelo número na vigente e, com a `## 1A` presente, também na pendente — o card da operação nova (escrito na rodada que segue a emenda, `DRF-14`) e o card antigo de uma operação renumerada pela emenda copiam textos de versões diferentes, e os dois são válidos até o marco (`DRF-37`). A reescrita do texto nos cards, na promoção, é da `RAF-T23`. O contrato do objeto é: "Quem implementa acrescenta à conferência o que cada operação pede, sem mudar o que ela já julga quando chamada como hoje."
- **Contratos/classes:** três regras: 1. Função nova `_texto_copiado(item_texto: str, op_id: str) -> str | None`, logo antes de `validar`: o resto da primeira linha do card que começa por `  - <op_id>: ` (dois espaços, hífen, espaço, o id, dois-pontos, espaço), com os espaços colapsados (`" ".join(resto.split())`); `None` sem essa linha. 2. Em `validar`, no laço dos cards (o bloco `if not pendente:` que emite `V2`, `V4` e `V14`), logo depois da checagem de `V14`, para cada `op_id` citado cujo número existe em alguma versão: os textos da operação são todos os de mesmo número na vigente e, havendo `modelo_pendente`, na pendente, com espaços colapsados — número duplicado numa versão (o caso da `V11`) conta cada um dos textos, nunca só o último (`DRF-61`); quando o texto copiado não é `None` e não é nenhum deles, emite `V22 <ID> — texto de OP-<n> diverge da versão <v>`, com `<v>` = versão da vigente quando o número existe nela, senão versão da pendente. Número que não existe em versão nenhuma já sai `V4` e não ganha `V22`. Vale com e sem `--so-vigente`. 3. A descrição do `argparse` de `main` troca `contra o vocabulário de violações V1..V21 (### 16); show deriva` por `contra o vocabulário de violações V1..V22 (### 16; V22 do P-0755); show deriva`.
- **Passos:** 1. Acrescentar ao fim de `tests/test_modelo.py` os três testes da seção `Testes`, com o helper `_raiz_modelo_pendente` da `RAF-T19`. 2. Rodar `python -m pytest tests/test_modelo.py -q -k texto_divergente` e conferir que os dois TF falham e o TR passa. 3. Aplicar as três regras de `Contratos/classes` (redespacho, `DRF-61`: os três testes e as regras 1 e 3 já estão na árvore; a regra 2 se ajusta à forma de hoje, um conjunto de textos por número). 4. Rodar `python .claude/tools/modelo.py check --plano docs/plans/P-0754-auditoria-final/plano.md` e conferir exit 0 (o único plano vivo com modelo além deste; medido no ensaio: nenhum card dele diverge). 5. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 3 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Nenhuma linha que já existia em `tests/test_modelo.py` sai ou muda: o card só acrescenta ao fim do arquivo; as fixtures de `tests/fixtures/modelo/` não mudam. - Os testes gravam só em `tmp_path`. - O `check` passa a sair 1 sobre quatro planos encerrados, com a divergência que a `R-06` descreve (medido no ensaio, `F-31`): `docs/plans/P-0746-lastro-do-modelo.md` (1 linha `V22`, `LST-T5`), `docs/plans/P-0747-consultor-de-plano.md` (7, `CON-T3`..`CON-T5a`), `docs/plans/P-0748-tela-do-gerente.md` (5, `TLG-T2`..`TLG-T4`) e `docs/plans/P-0753-auditoria-estagio-1/plano.md` (1, `AF-T19`). Nenhum deles se edita: são registro histórico, e nenhum instrumento roda o `check` sobre plano encerrado (§7). - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não reescrever card de plano nenhum para acertar texto (a reescrita é da promoção, `RAF-T23`); não mexer em `_tem_subbullets` nem no `V14`; não mexer em `_diff_fluxo` nem em `_diff_estado` (`RAF-T22`); não renumerar nem reordenar as violações de hoje.
- **Contingências:** - se um teste que já existia em `tests/test_modelo.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o passo 4 der exit 1 → parar e sinalizar `blocked` razão `premissa`, colando as linhas `V22` do `P-0754`. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_texto_divergente_v22_da_vigente` — `tarefas_op2="EX-T2"`, `card_op2=True` e o `EX-T1` com o texto `Primeira operação da fixture, na redação antiga.`: `check` sai 1 com `V22 EX-T1 — texto de OP-1 diverge da versão 1` no stderr (hoje sai 0). TR `test_tr_texto_divergente_so_em_espacos_nao_e_v22` — o `EX-T1` com `Primeira  operação da fixture. ` (espaço duplo e espaço na ponta): `check` sai 0 (a regra concorrente, comparação literal, acusaria `V22`). TF `test_tf_texto_divergente_v22_da_pendente` — o `EX-T2` com o texto `Outra redação da segunda operação.`: `check --so-vigente` sai 1 com `V22 EX-T2 — texto de OP-2 diverge da versão 2` (hoje sai 0). O teste existente `test_tf_check_invalido_lista_catorze_violacoes_na_ordem` é o TR do número duplicado (`DRF-61`): o `EX2-T3` de `plano-invalido-2.md` copia o primeiro dos dois `OP-3`, e só a regra concorrente (um texto por número, o último vence) o acusa `V22`; ele passa sem linha mudada. Suíte `tests/test_modelo.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** a reescrita do texto da operação nos cards, na promoção da versão aceita (`RAF-T23`); a diferença entre versões (`RAF-T22`).
- **Handover:** 2026-09-29 · para `RAF-T22` - **Entregue:** modelo.py: V22 recusa card que copia a operação com texto diferente da versão citada, comparando com todos os textos de mesmo número (vigente e pendente; número duplicado conta cada um); 3 testes novos - **Contrato:** check sobre P-0754 e P-0755 sai 0; o teste das catorze violações segue intacto - **Não refazer:** a V22 e os testes texto_divergente - **Pendente:** nenhum

## Execução

**Consumo:** 25 tool uses, 76.4 k tokens, 245.7 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Exercicio ponta a ponta nesta revisao, em raiz temporaria fora do repositorio, com e sem --so-vigente: card que copia o texto novo da pendente para numero que existe na vigente sai 0 (DRF-37); card que copia texto da vigente com a pendente reescrita sai 0; texto que nao e nenhum sai V22 versao 1; OP-2 so-pendente com texto de OP-1 sai V22 versao 2; numero duplicado na vigente com copia do primeiro texto sai so V8/V11, sem V22 (DRF-61); tabulacao e espacos multiplos colapsam; OP-9 inexistente sai so V4. Forma da mensagem V22 casa com V4/V14 ('V<n> <ID> — ...'). Planos reais: P-0754 e P-0755 saem 0; os quatro encerrados saem 1 com exatamente 1/7/5/1 linhas V22, como o card mediu. show segue exit 0 e o --help publica V1..V22. OP-21 confere com a entrega: sem conflito de modelo. A parada do primeiro despacho custou um despacho inteiro mais uma passagem de consultor por um caso que o ensaio do card teria revelado rodando a regra contra a suite existente.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "O despacho pede à conferência do modelo só a versão vigente" e vai pegar a tarefa "A conferência do modelo recusa o card que copia a operação com outro texto".
Tarefa "A conferência do modelo recusa o card que copia a operação com outro texto". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "A conferência do modelo recusa o card que copia a operação com outro texto" e vai executar: Quem executa faz a conferência do modelo recusar o card cujo texto copiado da operação difere do texto da versão que ele cita.
Agente executor devolveu a tarefa "A conferência do modelo recusa o card que copia a operação com outro texto": blocked — motivo premissa: teste existente tests/test_modelo.py::test_tf_check_invalido_lista_catorze_violacoes_na_ordem caiu após aplicar a regra V22 (contingência do card): stderr ganhou `V22 EX2-T3 — texto de OP-3 diverge da versão 1` e a contagem virou `modelo: FALHOU — 5 violação(ões)` onde o teste esperava 4; nada revertido, as três regras de Contratos/classes e os 3 testes novos (TF/TF/TR de `texto_divergente`, todos verdes, `python -m pytest tests/test_modelo.py -q -k texto_divergente` → 3 passed) e o passo 4 (`check` sobre `docs/plans/P-0754-auditoria-final/plano.md` → exit 0) seguem no estado da entrega; suíte inteira não rodada até o fim (parou em 592 passed, 1 failed); dead_code.py e kit_check.ps1 não rodados (contingência manda parar antes); nenhum commit nem comando git que escreve foi executado..
Scrum master vai marcar a tarefa "A conferência do modelo recusa o card que copia a operação com outro texto" como blocked, sem RDO.
Scrum master vai marcar a tarefa "A conferência do modelo recusa o card que copia a operação com outro texto" como blocked, sem RDO.
Agente consultor recebe a tarefa "A conferência do modelo recusa o card que copia a operação com outro texto" e vai triar.
Agente consultor devolveu a tarefa "A conferência do modelo recusa o card que copia a operação com outro texto": rota resolve.
Tarefa "A conferência do modelo recusa o card que copia a operação com outro texto". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "A conferência do modelo recusa o card que copia a operação com outro texto" e vai executar: Quem executa faz a conferência do modelo recusar o card cujo texto copiado da operação difere do texto da versão que ele cita.
Agente executor devolveu a tarefa "A conferência do modelo recusa o card que copia a operação com outro texto": review — sem pendência.
Tarefa "A conferência do modelo recusa o card que copia a operação com outro texto": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A conferência do modelo recusa o card que copia a operação com outro texto" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A conferência do modelo recusa o card que copia a operação com outro texto": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "A conferência do modelo recusa o card que copia a operação com outro texto" como done: registrar estado, RDO e telemetria.
