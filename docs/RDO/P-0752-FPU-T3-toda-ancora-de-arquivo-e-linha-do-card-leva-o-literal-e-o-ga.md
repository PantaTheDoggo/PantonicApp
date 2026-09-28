# RDO — P-0752 · FPU-T3

# Humano

Tarefa "Toda âncora de arquivo e linha do card leva o literal, e o gate confere a linha hoje" concluída em 2026-09-26.
O verificador de cards agora confere que cada referência a arquivo e linha nos alvos e nos passos traz o texto citado, e que esse texto está hoje naquela linha.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Fato no ponto de uso: os mecanismos contra o esquecimento e a assunção": 2/11 tarefas concluídas; próxima: "O executor devolve a medida como arquivo, e a evidência a incorpora".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achado registrado no plano, com rota: 1 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/plans/P-0752-fato-no-ponto-de-uso.md`
**Tarefa:** `FPU-T3` — Toda âncora de arquivo e linha do card leva o literal, e o gate confere a linha hoje
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `card_check.py` acusa `âncora sem literal` para toda ocorrência `` `<caminho>:<linha>` `` sem literal (DFP-4) e `literal fora da linha` quando o literal não está na linha citada da árvore de `--root`; card sem âncora não é afetado.

**Arquivos-alvo:** - `.claude/tools/card_check.py` — nova função `conferir_ancoras(dossie, root) -> list[str]` chamada em `verificar_tarefa` depois dos itens de Verificação - `tests/test_card_check.py` - `tests/fixtures/card_check/plano-ancoras.md` (novo) e `tests/fixtures/card_check/alvo.txt` (novo, três linhas: `um`, `dois`, `tres`)

**Verificação:** 1. `python -m pytest tests/test_card_check.py -q` → verde — antes `12 passed` (após `FPU-T1`), depois `16 passed`. 2. `python .claude/tools/card_check.py --plano tests/fixtures/card_check/plano-ancoras.md --tarefa AN-T2` → exit 1 com `âncora sem literal` — antes: arquivo inexistente, exit `1` por `plano inexistente`; depois exit `1` com `âncora sem literal`. 3. `python -m pytest -q` → nenhuma falha; `passed` ≥ 402 + 4 — antes `402 passed`.

**Pronto quando:** card.âncoras — toda âncora leva o literal, e o gate acusa literal fora da linha — Verificações 1 e 2; régua executável.conferências — a conferência de âncora roda no `card_check` — Verificação 1.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Depende de:** `FPU-T1`
- **Operação do modelo:** `OP-3` - OP-3: Toda âncora de arquivo e linha num card leva o literal citado, e o gate confere que o literal está naquela linha hoje. - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; card — Quem implementa faz o instrumento ler a forma que o corpus vivo usa; card vivo não se reescreve para caber no instrumento.
- **Fundamento:** DFP-4, F-2, causa 1 de F-10.
- **Contratos/classes:** `conferir_ancoras(dossie: DossieTarefa, root: Path) -> list[str]` (DFP-16, emenda DFP-4) — varre dois textos: as linhas brutas de `dossie.campos_linhas.get("arquivos-alvo", [])` e o conteúdo (achatado) de cada par de `dossie.extras` cujo rótulo, por `rdo._normalizar_rotulo`, é `passos` — `passos` não é campo canônico e `rdo.py` não se toca; `Texto atual <n>` não se varre e bloco cercado não é literal. Âncora e literal, regex exatas (medidas pelo consultor em protótipo): ~~~~ _ANCORA_RE = re.compile(r"`(?P<caminho>[^`:\s]+\.[A-Za-z0-9]+):(?P<linha>\d+)(?:-(?P<fim>\d+))?`") _LITERAL_APOS_ANCORA_RE = re.compile(r"\s*(?:—|:)\s*`(?P<lit>(?:\\`|[^`\\])+)`") ~~~~ literal = `_LITERAL_APOS_ANCORA_RE.match(texto, m.end())`, com `\`` trocado por `` ` `` e `strip()` (forma do corpus: `P-0752` linhas do `FPU-T2`, `FPU-T5a`, `FPU-T8`, `FPU-T10`); confere quando está **contido** em alguma linha (`strip()`) da faixa `linha..fim` de `root / caminho`. Âncora sem literal passa quando o mesmo texto de âncora (`m.group(0)`) tem literal em outra ocorrência do card (Passo que remete a alvo já ancorado).
- **Passos:** 1. Escrever `conferir_ancoras` com as três falhas nomeadas: `âncora sem literal`, `alvo inexistente`, `literal fora da linha` (mensagem traz o literal esperado e a linha real com `strip()`). 2. Chamar em `verificar_tarefa` só quando o mundo comparado é `antes` (card não `done`: a entrega desloca as linhas que o card ancorou; DFP-16), apensando as falhas à lista; `main` não muda. 3. Fixtures: `alvo.txt` com as linhas `um`, `dois`, ``tres `x` ``; `plano-ancoras.md` com quatro cards `ready` cuja Verificação é `` 1. `python -c "print('a')"` → `a` — antes `a`, depois `a` `` (fecha em `antes`). `AN-T1`: Arquivos-alvo `` `tests/fixtures/card_check/alvo.txt:2` — `dois` `` e `` `tests/fixtures/card_check/alvo.txt:3` — `tres \`x\`` ``, e Passo que repete a âncora da linha 2 sem literal (fecha); `AN-T2`: a âncora da linha 2 sem literal, só no Passo (falha `âncora sem literal`); `AN-T3`: Arquivos-alvo `` `tests/fixtures/card_check/alvo.txt:2` — `tres` `` (falha `literal fora da linha`); `AN-T4` sem âncora (fecha).
- **Testes (novos):** TF `test_tf_ancora_com_literal_fecha`, TF `test_tf_ancora_sem_literal_falha`, TF `test_tf_literal_fora_da_linha_falha`, TR `test_tr_card_sem_ancora_nao_muda` (`AN-T4` exit 0).
- **Não fazer:** não varrer `Verificação`, `Objetivo` nem `Contratos` por âncora (só `Arquivos-alvo` e `Passos`, DFP-16); não tocar `rdo.py`; não reescrever card vivo (I-3).
- **Contingências:** - se `conferir_ancoras` acusar algo nos cards `ready` deste plano (`FPU-T5`..`FPU-T10`) → não é da entrega; medido no acionamento 4 do consultor, com o protótipo acima: zero falhas depois do reparo das âncoras de `FPU-T2`, `FPU-T6` e `FPU-T8`; registrar em `pendencia=`. - Medido em protótipo sobre cópia da árvore (acionamento 4): Verificação 1 `16 passed`; Verificação 2 exit 1 com `âncora sem literal`; suíte `406 passed`; `dead_code.py`, `ratchet_piso.py`, `kit_check.ps1 -Mode validate`, `check-readme.ps1` exit 0.
- **Handover:** 2026-09-26 · para `FPU-T5`, `FPU-T2` - **Entregue:** conferir_ancoras(dossie, root) em .claude/tools/card_check.py:256, com _ANCORA_RE (:252) e _LITERAL_APOS_ANCORA_RE (:253); chamada em verificar_tarefa (:449) so com mundo antes; varre linhas brutas de Arquivos-alvo e o extra Passos (DFP-16); falhas nomeadas: ancora sem literal, alvo inexistente, literal fora da linha; fixtures tests/fixtures/card_check/plano-ancoras.md (AN-T1..AN-T4) e alvo.txt - **Contrato:** card_check acusa ancora sem literal e literal fora da linha em card nao done; ancora repetida sem literal passa se o mesmo texto de ancora tem literal em outra ocorrencia do card; Objetivo, Verificacao e Contratos nao sao varridos; card done nao confere ancora; test_card_check 16 passed; suite >= 406 - **Não refazer:** conferencia de ancora ja paga; rdo.py intocado de proposito (Passos lido do extra achatado) - **Pendente:** versao 2 do modelo (OP-3 e card.ancoras com o alcance da DFP-16) pendente de validacao do dono no marco; ancoras para arquivos que o proprio card cria saem alvo inexistente no mundo antes - FPU-T2 precisa isenta-las
- **Notas de execução:** - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T3-toda-ancora-de-arquivo-e-linha-do-card-leva-o-literal-e-o-ga.md`, veredito aprovado 100%

## Execução

**Consumo:** 25 tool uses, 102.9 k tokens, 349.9 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

Com a conferência apensada à mesma lista de falhas e main intocado (Passo 2), a linha-resumo conta falha de âncora como item: 'FALHOU - 2 item(ns)' quando as duas são 'alvo inexistente' e 'literal fora da linha', e elas saem sem o prefixo 'item N:' das falhas de Verificação. Foi o card que mandou; não é defeito da entrega, mas quem ler a saída do gate no FPU-T2 (despacho) deve saber que 'item(ns)' passou a significar 'falhas'. Exercício ponta a ponta sobre plano temporário fora do repo: faixa 'caminho:1-3' com separador ': ' fecha; crase escapada na 3ª linha confere e acusa quando diverge; 'alvo inexistente' dispara; FPU-T2 e FPU-T4..FPU-T10 do P-0752 não produzem nenhuma falha de âncora (contingência do card confirmada).

## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master concluiu a tarefa "O gate do card lê a forma do corpus e deixa de produzir item fantasma" e vai pegar a tarefa "Toda âncora de arquivo e linha do card leva o literal, e o gate confere a linha hoje".
Tarefa "Toda âncora de arquivo e linha do card leva o literal, e o gate confere a linha hoje". Passo: conferir os gates e preparar o despacho.
Agente consultor recebe a tarefa "Toda âncora de arquivo e linha do card leva o literal, e o gate confere a linha hoje" e vai triar.
Agente consultor devolveu a tarefa "Toda âncora de arquivo e linha do card leva o literal, e o gate confere a linha hoje": rota resolve.
Tarefa "Toda âncora de arquivo e linha do card leva o literal, e o gate confere a linha hoje": gates aprovados; vou materializar in-progress e gravar o ponto de partida.
Agente executor recebe a tarefa "Toda âncora de arquivo e linha do card leva o literal, e o gate confere a linha hoje" e vai executar: `card_check.py` acusa `âncora sem literal` para toda ocorrência `` `<caminho>:<linha>` `` sem literal (DFP-4) e `literal fora da linha` quando o literal não está na linha citada da árvore de `--root`; card sem âncora não é afetado.
Agente executor devolveu a tarefa "Toda âncora de arquivo e linha do card leva o literal, e o gate confere a linha hoje": review — sem pendência.
Tarefa "Toda âncora de arquivo e linha do card leva o literal, e o gate confere a linha hoje": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "Toda âncora de arquivo e linha do card leva o literal, e o gate confere a linha hoje" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "Toda âncora de arquivo e linha do card leva o literal, e o gate confere a linha hoje": aprovado 100%, bloqueante nenhuma.
Agente modelador recebe a tarefa "Toda âncora de arquivo e linha do card leva o literal, e o gate confere a linha hoje" e vai atualizar o modelo.
Agente modelador devolveu a tarefa "Toda âncora de arquivo e linha do card leva o literal, e o gate confere a linha hoje": Gravei a versão 2 do modelo como **pendente**, seguindo a forma de emenda. A `## 1` vigente (versão 1) ficou como estava. O `check` sai com exit 0, sem nenhuma ….
Scrum master vai fechar a tarefa "Toda âncora de arquivo e linha do card leva o literal, e o gate confere a linha hoje" como done: registrar estado, RDO e telemetria.
