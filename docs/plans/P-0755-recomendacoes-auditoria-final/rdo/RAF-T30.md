# RDO — P-0755 · RAF-T30

# Humano

Tarefa "O fechamento de tarefa registra o achado pela linha de origem e avisa a falha de instrumento" concluída em 2026-09-29.
O fechamento de tarefa passou a registrar cada achado pela linha de origem e a avisar quando um achado aponta falha de instrumento.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 48/59 tarefas concluídas; próxima: "O laudo aceita o alvo instrumento que o aviso do fechamento lê".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T30` — O fechamento de tarefa registra o achado pela linha de origem e avisa a falha de instrumento
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz o fechamento de tarefa tratar cada achado do laudo pela linha de origem, pulando o já registrado e avisando a falha de instrumento.

**Arquivos-alvo:** - `.claude/tools/encerrar.py` - `tests/test_encerrar.py`

**Verificação:** 1. `python -m pytest tests/test_encerrar.py -q -k origem_do_achado` → `exit 0` — antes `exit 0`, depois `exit 0` 2. `python -m pytest tests/test_encerrar.py -q -k falha_de_instrumento` → `exit 0` — antes `exit 0`, depois `exit 0` 3. `python -c "from pathlib import Path;t=Path('tests/test_encerrar.py').read_text(encoding='utf-8');a=chr(34)+'linha nova do registro'+chr(34)+' not in saida';m=t.split('def test_tf_origem_do_achado_gravada_na_linha')[0];print('marco=%d total=%d'%(m.count(a),t.count(a)))"` → `marco=2 total=2` — antes `marco=1 total=2`, depois `marco=2 total=2`

**Pronto quando:** - fechamento.origem do achado registrado — cada achado registrado cita a linha do laudo de onde veio, e o fechamento pula o que já foi registrado com essa origem — Verificação 1 - fechamento.aviso de falha de instrumento — o fechamento avisa, numa linha própria, cada achado de instrumento que relata queda ou erro — Verificação 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-21`, `DRF-22`; `F-25` (`achados_do_laudo` lê a tabela `| alvo | achado |` de `## Achado de processo`; `apensar_achado` grava a `AE-` sem origem; a dedupe é por substring do texto; a regra `B1` mora só na skill `scrum-master`, e o código não lê `escalar`); relatório `R-19` (auditoria reg. 39: o achado que o consultor reescreveu entrou de novo, em duplicata) e `R-20` (reg. 47: falha de instrumento num laudo `seguir` não chegou ao consultor).
- **Depende de:** `RAF-T27`, `RAF-T23a`
- **Operação do modelo:** `OP-30` - OP-30: Quem executa faz o fechamento de tarefa tratar cada achado do laudo pela linha de origem, pulando o já registrado e avisando a falha de instrumento. - precisa de: fechamento — Quem implementa recebe o comando que hoje só grava o veredito do marco e confere achados por semelhança de texto, e acrescenta o que a operação pede.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/encerrar.py`, verbo `tarefa` (`fechar_tarefa` e `apensar_achado`); só biblioteca padrão. A forma da origem, `laudo:<TAREFA>#<n>` entre crases, é a mesma que o consultor passa a citar quando registra ou reescreve achado a partir de laudo (`RAF-T35`); a linha `encerrar: B1 — …` é a que a skill `scrum-master` passa a ler como pendência substantiva (`RAF-T34`). O verbo `marco` (`RAF-T23`) não muda. O contrato do objeto é: "Quem implementa recebe o comando que hoje só grava o veredito do marco e confere achados por semelhança de texto, e acrescenta o que a operação pede."
- **Contratos/classes:** `apensar_achado(plano_path: Path, tarefa_id: str, texto: str, rota: str, data: str, tiquete_id: str | None = None, origem: str | None = None) -> str` (parâmetro novo `origem`); `fechar_tarefa` — assinatura inalterada. Três regras: 1. `apensar_achado`: com `origem`, a entrada ganha no fim ` **Origem:** ` seguido de `origem` entre crases, depois de `**Rota:** <rota>`; sem `origem`, a entrada de hoje. Comentário cita `R-19` e `DRF-21` do `P-0755`. O `--achado` do comando segue sem origem. 2. `fechar_tarefa`, laço dos achados do laudo: numera os achados de `achados_do_laudo(texto_laudo)` a partir de 1, na ordem da tabela; a origem do achado `n` é `laudo:<tarefa_id>#<n>`; o achado é pulado quando a origem entre crases (`` `laudo:<tarefa_id>#<n>` ``) já está no texto das `AE-` do plano (`entradas_existentes`), ou, como hoje, quando o texto está nelas ou em `textos_gravados`; senão, `apensar_achado(..., origem=<origem>)`. A comparação com as crases impede que `laudo:ALF-T1#1` case dentro de `laudo:ALF-T1#11`. 3. `fechar_tarefa`, aviso `B1`: constantes novas, logo depois de `ACHADO_PROCESSO_HEADING`, `_ACHADO_INSTRUMENTO_RE` (casa `achado de processo (instrumento): <resto>`, sem distinção de caixa, capturando `resto`) e `_TERMOS_DE_FALHA = ("queda", "traceback", "exceção", "excecao", "exception", "error")`; depois da linha `Detalhe:` do texto devolvido, para cada achado do laudo, na ordem, que casa `_ACHADO_INSTRUMENTO_RE` e cujo `resto` em minúsculas contém um dos termos, o texto devolvido ganha a linha `encerrar: B1 — achado de instrumento com falha: <resto>` — registrado ou pulado, o aviso sai do mesmo jeito. O `main` imprime esse texto antes da linha final `encerrar: OK - comando 'tarefa' concluído; …`, como hoje.
- **Passos:** 0. Redespacho (`DRF-68`, `AE-186`): a primeira execução deixou na árvore as três regras de `Contratos/classes` e os cinco testes, e deslocou a última linha do teste do marco, `    assert "linha nova do registro" not in saida`, para o fim de `test_tr_falha_de_instrumento_sem_termo_ou_de_outro_alvo_cala`. Tirar essa linha do fim do TR e pô-la de volta como última linha de `test_tf_marco_recusa_devolver_sem_linha_nova_do_registro`, logo depois do `)` que fecha a asserção do `Devolver`, com os mesmos quatro espaços; nada mais muda no arquivo, e o TR passa a terminar em `    assert "encerrar: B1" not in saida`. Os Passos 1 a 3 já estão feitos e não se refazem (o Passo 2 não se reproduz: os testes novos já passam); seguir ao Passo 4 e rodar também a Verificação 3. 1. Acrescentar ao fim de `tests/test_encerrar.py` os cinco testes da seção `Testes`, com `_montar_repo`, `_laudo_com_achado` e `_argv_tarefa`, que já existem no arquivo. 2. Rodar `python -m pytest tests/test_encerrar.py -q -k "origem_do_achado or falha_de_instrumento"` e conferir que os três TF falham e os dois TR passam. 3. Aplicar as três regras de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 5 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). Os testes de achado que já existem (`test_tf_achado_do_laudo_vira_ae_com_rota`, `test_tr_achado_do_laudo_repetido_nao_duplica`, `test_tf_achado_do_laudo_sem_rota_declarada`) continuam passando sem mudança: afirmam o começo da linha, que não muda. - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Nenhuma linha que já existia em `tests/test_encerrar.py` sai ou muda: o card só acrescenta ao fim do arquivo. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit nem comando `git` que escreve no índice, na árvore ou nas referências (`stash`, `reset`, `checkout`, `restore`, `clean`, `add`), §4 invariante 14. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar `achados_do_laudo` nem a forma de `texto` e `rota` que ele devolve; não mudar o exit do fechamento por causa do aviso `B1`; não gravar o aviso no RDO; não reescrever `AE-` já registradas para acrescentar origem; não mexer no verbo `marco`.
- **Contingências:** - se um teste que já existia em `tests/test_encerrar.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** TF `test_tf_origem_do_achado_gravada_na_linha` — laudo com as linhas `dossiê` e `doutrina`: o plano tem `` - **AE-3** (`ALF-T1`, fechamento, 2026-09-26) — achado de processo (doutrina): a skill não nomeia o gate. **Rota:** tíquete **Origem:** `laudo:ALF-T1#2` `` (hoje sem a origem). TF `test_tf_origem_do_achado_ja_registrada_pula` — o plano já tem `AE-2` com outro texto e `` **Origem:** `laudo:ALF-T1#1` ``; o laudo tem a linha 1 `dossiê`: o plano não ganha `AE-3` (hoje ganha, porque o texto difere). TR `test_tr_origem_do_achado_de_outra_linha_nao_pula` — a `AE-2` existente tem `` `laudo:ALF-T1#11` ``: a linha 1 vira `AE-3` (a regra concorrente, casar `laudo:ALF-T1#1` como substring sem as crases, a pularia). TF `test_tf_falha_de_instrumento_avisa_b1` — linha `| instrumento | o card_check caiu com Traceback no item 2. Rota: tíquete |`: o stdout tem `encerrar: B1 — achado de instrumento com falha: o card_check caiu com Traceback no item 2.` antes de `encerrar: OK - comando 'tarefa' concluído` (hoje nenhum aviso). TR `test_tr_falha_de_instrumento_sem_termo_ou_de_outro_alvo_cala` — linhas `| instrumento | a saída do card_check é longa. |` e `| dossiê | o teste deu error no ramo vazio. |`: o stdout não tem `encerrar: B1` (a regra concorrente, qualquer achado de instrumento ou qualquer termo em qualquer alvo, avisaria). Suíte `tests/test_encerrar.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** a leitura da linha `B1` pela skill e a entrega do card ao consultor (`RAF-T34`); a origem citada pelo consultor (`RAF-T35`).
- **Handover:** 2026-09-29 · para `RAF-T30a` - **Entregue:** .claude/tools/encerrar.py: achado registrado pela linha de origem e o aviso 'encerrar: B1 — achado de instrumento com falha' (:588) lido do alvo instrumento; tests/test_encerrar.py com os cinco testes, e a asserção do TF do marco de volta ao lugar - **Contrato:** o aviso B1 só dispara com o alvo instrumento e termo de falha; outro alvo cala - **Não refazer:** nada a declarar - **Pendente:** o alvo instrumento ainda não é aceito pelo rdo.py nem pela rubrica: é a RAF-T30a (DRF-68)

## Execução

**Consumo:** 17 tool uses, 64.4 k tokens, 233.3 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Redespacho fechou o defeito do primeiro laudo: tests/test_encerrar.py so ganhou linhas depois da 1211 (git diff contra 9e5bf2e sem linha removida), a assercao 'linha nova do registro' voltou ao TF do marco e a Verificacao 3 sai marco=2 total=2. Exercicio ponta a ponta numa copia temporaria: tres achados numerados #1..#3 na ordem da tabela, B1 com EXCECAO em caixa alta sai antes da linha OK, e o --achado do comando segue sem Origem. O caminho real rdo.py laudo -> alvo instrumento -> B1 segue fechado ate a RAF-T30a (DRF-68), fora deste card.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Tarefa "O fechamento de tarefa registra o achado pela linha de origem e avisa a falha de instrumento": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O fechamento de tarefa registra o achado pela linha de origem e avisa a falha de instrumento" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O fechamento de tarefa registra o achado pela linha de origem e avisa a falha de instrumento": reprovado 74%, bloqueante testes, recomendação escalar.
Scrum master vai marcar a tarefa "O fechamento de tarefa registra o achado pela linha de origem e avisa a falha de instrumento" como blocked, sem RDO.
Agente consultor recebe a tarefa "O fechamento de tarefa registra o achado pela linha de origem e avisa a falha de instrumento" e vai triar.
Agente consultor devolveu a tarefa "O fechamento de tarefa registra o achado pela linha de origem e avisa a falha de instrumento": rota modelador.
Agente modelador recebe a tarefa "O fechamento de tarefa registra o achado pela linha de origem e avisa a falha de instrumento" e vai fazer emenda no modelo.
Agente modelador devolveu a tarefa "O fechamento de tarefa registra o achado pela linha de origem e avisa a falha de instrumento": Emenda feita. A versão 4 fica pendente na `## 1A`, e o `check` sai com exit 0..
Agente executor recebe a tarefa "O fechamento de tarefa registra o achado pela linha de origem e avisa a falha de instrumento" e vai executar: Quem executa faz o fechamento de tarefa tratar cada achado do laudo pela linha de origem, pulando o já registrado e avisando a falha de instrumento.
Agente executor devolveu a tarefa "O fechamento de tarefa registra o achado pela linha de origem e avisa a falha de instrumento": review — sem pendência.
Tarefa "O fechamento de tarefa registra o achado pela linha de origem e avisa a falha de instrumento": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O fechamento de tarefa registra o achado pela linha de origem e avisa a falha de instrumento" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O fechamento de tarefa registra o achado pela linha de origem e avisa a falha de instrumento": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O fechamento de tarefa registra o achado pela linha de origem e avisa a falha de instrumento" como done: registrar estado, RDO e telemetria.
