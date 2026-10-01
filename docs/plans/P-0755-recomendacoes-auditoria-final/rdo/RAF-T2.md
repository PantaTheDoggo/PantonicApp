# RDO — P-0755 · RAF-T2

# Humano

Tarefa "O medidor de custo da sessão vira comando do kit" concluída em 2026-09-28.
O kit ganha um comando que mede quanto contexto cada turno do loop reenvia, repartido por passo e por tarefa.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 3/41 tarefas concluídas; próxima: "O despacho grava o pacote da tarefa e imprime só o recado ao executor".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T2` — O medidor de custo da sessão vira comando do kit
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa cria o medidor de custo da sessão, que lê uma conversa gravada e reparte o contexto reenviado por turno, por passo do loop e por tarefa despachada.

**Arquivos-alvo:** - `.claude/tools/custo_sessao.py` - `tests/test_custo_sessao.py`

**Verificação:** 1. `python -m pytest tests/test_custo_sessao.py -q -k medir` → `exit 0` — antes `exit 4`, depois `exit 0` 2. `python -m pytest tests/test_custo_sessao.py -q -k passos` → `exit 0` — antes `exit 4`, depois `exit 0`

**Pronto quando:** - medidor de custo da sessão.medida por turno — um comando do kit, com teste, grava o contexto reenviado em cada turno de uma conversa gravada — Verificação 1 - medidor de custo da sessão.medida por passo e por tarefa — os turnos se repartem por passo do loop e por tarefa de qualquer plano ou tíquete; numa janela sem despacho o comando informa zero e termina bem — Verificação 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-6`; `F-6` (285,6k por turno no loop real), `F-13` (os rascunhos quebram e fixam `AUF-T`); relatório `R-01`.
- **Depende de:** `RAF-T1`
- **Operação do modelo:** `OP-2` - OP-2: Quem executa cria o medidor de custo da sessão, que lê uma conversa gravada e reparte o contexto reenviado por turno, por passo do loop e por tarefa despachada. - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; rascunhos de medição da auditoria — Ninguém altera: são o ponto de partida do medidor novo e ficam como estão.; gerente do loop — Quem implementa recebe os passos do loop como estão e muda só o trecho que a operação nomeia, com a regra escrita num lugar só.
- **Camada e fronteira:** instrumento do kit em `.claude/tools/`, só biblioteca padrão (Python 3.12); não importa de `tests/`, de outro módulo do kit nem de projeto consumidor; lê o transcript e escreve só o TSV que recebe por argumento. Os rascunhos `docs/audits/sonda-2026-09-28/medir.py` e `docs/audits/sonda-2026-09-28/passos.py` são o ponto de partida lido e ficam intocados (contrato do objeto: "Ninguém altera: são o ponto de partida do medidor novo e ficam como estão.").
- **Contratos/classes:** módulo novo `.claude/tools/custo_sessao.py`, com guarda `if __name__ == "__main__": sys.exit(main())` e toda função alcançável a partir de `main` (o `dead_code.py` julga alcançabilidade). Funções e saídas, exatas: 1. `medir(transcript: Path, saida: Path) -> int` — para cada linha do transcript que é JSON (linha que não é JSON se pula) com `type == "assistant"` e `message.usage` não vazio, grava no TSV uma linha com cinco campos separados por tabulação: `timestamp` do evento, `message.id`, o contexto reenviado `input_tokens + cache_read_input_tokens + cache_creation_input_tokens` (ausente conta 0), `output_tokens` e as ferramentas do turno unidas por ` | `; devolve o número de linhas. Ferramentas, por bloco de `message.content`, na ordem: `tool_use` de nome `Agent` → `Agent:<subagent_type>:<description>`; `tool_use` de nome `Bash` ou `PowerShell` → `Bash:` seguido do `command` com todo espaço em branco colapsado num espaço, cortado em 220 caracteres; outro `tool_use` → `<name>:` seguido de `file_path` (na falta, `pattern`), cortado em 120; bloco `text` com texto não vazio → `TEXT`. 2. `classificar_passo(ferramentas: str) -> str` — tira `TEXT | ` e ` | TEXT` do texto e devolve o primeiro que casa, nesta ordem: contém `pantonic-executor` → `P4`; `pantonic-reviewer` → `P6`; `pantonic-consultant` → `P8`; `encerrar.py` → `P9`; casa a regex `backlog\.py status \S+ review` → `P5`; contém `despachar` → `P3`; contém `backlog.py next` → `P2`; casa a regex `grep -n|--co -q|wc -l` e não contém `laudo` → `P3`; contém `laudos/` ou `Achado de processo` → `P7`; texto vazio ou só `TEXT` → `texto`; senão `outro`. 3. `passos(tsv: Path, regex_inicio: str, regex_fim: str) -> list[str]` — agrupa as linhas do TSV por `message.id` (a primeira linha do id dá `timestamp`, contexto e saída; as ferramentas de todas as linhas do id se juntam por ` | `); a janela vai da primeira mensagem cujas ferramentas casam `regex_inicio` (`re.search`) até a última que casa `regex_fim`. Sem mensagem que case uma das duas, ou com a última do fim antes da primeira do início, devolve exatamente `["janela: vazia", "por tarefa: n=0"]`. Com janela, devolve, nesta ordem: `janela: <ts0> -> <ts1> turnos <N> ctx_k <x> out_k <y>`; uma linha `<passo> turnos=<n> ctx_k=<x> out_k=<y>` por passo, em ordem alfabética do passo; e, se nenhuma mensagem da janela casou a regex de tarefa `despachar ([A-Z]+-T\d+[a-z]?|TK-\d+)`, a linha `por tarefa: n=0`; senão `por tarefa: n=<k> turnos medio=<m> ctx_k medio=<c> min_turnos=<a> max_turnos=<b>` e uma linha `<tarefa> turnos=<n> ctx_k=<x> out_k=<y>` por tarefa, na ordem do primeiro despacho. A tarefa corrente é a do último `despachar` casado até a mensagem (inclusive); mensagem anterior ao primeiro despacho não entra em tarefa nenhuma. Todo valor `_k` é o total dividido por 1000 com uma casa (`f"{v / 1000:.1f}"`); `turnos medio` também com uma casa. 4. `main(argv: list[str] | None = None) -> int` — `argparse` com subcomandos obrigatórios `medir <transcript> <saida>` e `passos <tsv> <regex_inicio> <regex_fim>`; reconfigura stdout e stderr para UTF-8; `medir` imprime `<n> linhas` e sai 0; `passos` imprime as linhas de `passos()` e sai 0. Os caminhos vêm como dados na linha de comando (relativos ao diretório corrente ou absolutos) e não se normalizam. Recusas fechadas, cada uma com stderr e exit 1, sem gravar nada: transcript que não é arquivo → `custo_sessao: FALHOU - transcript não encontrado '<caminho>'`; TSV que não é arquivo → `custo_sessao: FALHOU - tsv não encontrado '<caminho>'`; `regex_inicio` ou `regex_fim` que não compila → `custo_sessao: FALHOU - regex inválida '<padrão>': <erro do re>`. Sem subcomando, a recusa é a do `argparse` (exit 2).
- **Passos:** 1. Criar `tests/test_custo_sessao.py` com os quatro testes da seção `Testes`, carregando o módulo por `importlib.util.spec_from_file_location` a partir de `.claude/tools/custo_sessao.py`, com o transcript sintético escrito em `tmp_path` (uma linha `user`, os turnos `assistant` do teste e uma linha que não é JSON). 2. Rodar `python -m pytest tests/test_custo_sessao.py -q` e conferir que falha (o módulo não existe). 3. Criar `.claude/tools/custo_sessao.py` com o contrato de `Contratos/classes`. 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o total não cai abaixo do re-medido no despacho e soma os 4 testes novos (referência datada: `521 passed`, 2026-09-28, antes da etapa A). - Só biblioteca padrão; Python 3.12. - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Os testes usam só transcript sintético em `tmp_path`; nenhum teste lê `%TEMP%`, a pasta do usuário ou `docs/audits/`. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não editar nem apagar `docs/audits/sonda-2026-09-28/medir.py` e `docs/audits/sonda-2026-09-28/passos.py`; não localizar o transcript sozinho (o caminho vem por argumento); não registrar o comando em `.claude/projecoes.json` (não é hook); não citar o comando no `README.md` (é da `RAF-T40`).
- **Contingências:** - se `python .claude/checks/dead_code.py` acusar símbolo de `.claude/tools/custo_sessao.py` → seguir com a chamada do símbolo a partir de `main` ou com a remoção do símbolo, até o achado sumir, sem mudar a saída de `Contratos/classes`. - se um teste que já existia na suíte cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste.
- **Testes:** TF `test_tf_medir_grava_uma_linha_por_turno_com_contexto_reenviado` — transcript com dois turnos: `m1` (`input_tokens` 10, `cache_read_input_tokens` 1000, `cache_creation_input_tokens` 200, `output_tokens` 30, um `Bash` com `python .claude/tools/backlog.py next`) e `m2` (5, 2000, 0, 40, um bloco `text`); `main(["medir", ...])` sai 0, imprime `2 linhas`, e o TSV é exatamente `t1\tm1\t1210\t30\tBash:python .claude/tools/backlog.py next` e `t2\tm2\t2005\t40\tTEXT` (a regra concorrente que somasse só `cache_read_input_tokens` daria 1000). TF `test_tf_passos_reparte_por_passo_e_por_tarefa_de_qualquer_plano` — quatro turnos de contexto 1000, 2000, 3000 e 4000: `despachar RAF-T3`, `Agent` `pantonic-executor`, `despachar TK-12`, `Agent` `pantonic-reviewer`; `passos` com início `despachar` e fim `pantonic-reviewer` sai 0 e imprime `janela: t1 -> t4 turnos 4 ctx_k 10.0 out_k 0.0`, `P3 turnos=2 ctx_k=4.0 out_k=0.0`, `P4 turnos=1 ctx_k=2.0 out_k=0.0`, `P6 turnos=1 ctx_k=4.0 out_k=0.0`, `por tarefa: n=2 turnos medio=2.0 ctx_k medio=5.0 min_turnos=2 max_turnos=2`, `RAF-T3 turnos=2 ctx_k=3.0 out_k=0.0` e `TK-12 turnos=2 ctx_k=7.0 out_k=0.0` (o rascunho, preso a `AUF-T`, não conta tarefa nenhuma). TR `test_tr_passos_sem_despacho_informa_zero_e_sai_0` — janela sem `despachar`: a última linha é `por tarefa: n=0` e o exit é 0 (o rascunho sai 1 com `ZeroDivisionError`); regex de início que nada casa: saída exatamente `janela: vazia` e `por tarefa: n=0`, exit 0. TR `test_tr_medir_e_passos_recusam_com_mensagem` — `medir` com transcript inexistente sai 1 com `custo_sessao: FALHOU - transcript não encontrado` no stderr; `passos` com início `(` sai 1 com `custo_sessao: FALHOU - regex inválida '('` (a regra concorrente sem recusa sai com exceção do `re`). Suíte `tests/test_custo_sessao.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** a medida do ganho sobre o transcript real do loop (ato da condução no relatório do Marco 6, §7); a doutrina da janela nova (`RAF-T1`); a citação no `README.md` (`RAF-T40`).
- **Handover:** 2026-09-28 · para quem vier depois - **Entregue:** comando novo .claude/tools/custo_sessao.py (subcomandos medir <transcript> <saida> e passos <tsv> <regex_inicio> <regex_fim>) com 4 testes em tests/test_custo_sessao.py; suíte 525 passed - **Contrato:** medir grava TSV timestamp/message.id/contexto reenviado/output/ferramentas por turno; passos reparte por passo P2..P9 e por tarefa de qualquer plano ou tíquete (regex despachar <ID>); recusas fechadas com exit 1 - **Não refazer:** o medidor e os testes; os rascunhos de docs/audits/sonda-2026-09-28/ ficam intocados - **Pendente:** a medida do ganho sobre o transcript real do loop é da condução no relatório do Marco 6

## Execução

**Consumo:** 20 tool uses, 101.0 k tokens, 363.1 s (fonte: `<usage>` do encerramento)

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

Scrum master concluiu a tarefa "O campo Janela do Passo 1 fica irmão dos outros campos do passo" e vai pegar a tarefa "O medidor de custo da sessão vira comando do kit".
Tarefa "O medidor de custo da sessão vira comando do kit". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "O medidor de custo da sessão vira comando do kit" e vai executar: Quem executa cria o medidor de custo da sessão, que lê uma conversa gravada e reparte o contexto reenviado por turno, por passo do loop e por tarefa despachada.
Agente executor devolveu a tarefa "O medidor de custo da sessão vira comando do kit": review — sem pendência.
Tarefa "O medidor de custo da sessão vira comando do kit": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O medidor de custo da sessão vira comando do kit" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O medidor de custo da sessão vira comando do kit": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "O medidor de custo da sessão vira comando do kit" como done: registrar estado, RDO e telemetria.
