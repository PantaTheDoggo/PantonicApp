# RDO — DIARIO_DE_OBRAS · TK-85a

# Humano

Tarefa "`rdo.py laudo --motivo` e o alvo `dossiê`" concluída em 2026-09-27.
O laudo do revisor ganhou lugar para o motivo de cada dimensão fora de conforme, e o alvo 'dossiê' passou a ser aceito com acento.
Revisão: aprovada com ressalva (94%).
Pendência para o dono: nenhuma.
Tíquete "O `rdo.py laudo` não tem onde pôr o motivo da dimensão, e recusa o alvo `dossiê`": 1/1 tarefas concluídas; nenhuma tarefa pronta na fila dele.
Achado registrado no plano, com rota: 1 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-85a` — `rdo.py laudo --motivo` e o alvo `dossiê`
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** em `.claude/tools/rdo.py`, subcomando `laudo`: 1. flag nova `--motivo DIMENSAO LINHA`, repetível (`nargs=2`, `action="append"`), com recusa (`RdoValidationError`, exit diferente de `0`, nenhum laudo escrito) quando a dimensão não é uma das sete, quando o nível dela é `conforme`, ou quando a linha é vazia, tem `|` ou quebra de linha; 2. o documento do laudo ganha, entre a tabela de níveis e `## Achado de processo`, a seção `## Motivo das dimensões fora de conforme`, com a tabela `| dimensão | nível | motivo |` (uma linha por `--motivo`, na ordem dada) ou o corpo `nenhum` sem a flag — a seção existe sempre, como a de achado; 3. `--achado-processo` aceita `dossiê` como sinônimo de `dossie` (normalizado antes da validação; a tabela segue imprimindo `dossiê`). Em `.claude/agents/pantonic-reviewer.md`, a frase que começa por `O motivo de cada dimensão fora de` passa a nomear a flag `--motivo` do `rdo.py laudo` como o lugar do motivo, e diz que ele não vai ao card *Lições aprendidas na tarefa*.

**Arquivos-alvo:** - `.claude/tools/rdo.py` - `tests/test_rdo.py` - `.claude/agents/pantonic-reviewer.md`

**Verificação:** 1. `python -m pytest tests/test_rdo.py -q -k "laudo_motivo or laudo_achado_dossie_acentuado"` → os testes novos verdes — antes `exit 5`, depois `exit 0` (antes nenhum teste selecionado). 2. `python -c "from pathlib import Path;print(Path('.claude/agents/pantonic-reviewer.md').read_text(encoding='utf-8').count('--motivo')>=1)"` → `True` — antes `False`, depois `True`. 3. `python -m pytest tests/test_rdo.py -q` → verde — antes `exit 0`, depois `exit 0`. 4. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`.

**Pronto quando:** o motivo de dimensão tem campo e seção própria no laudo, com recusa para dimensão `conforme`; `dossiê` é aceito como alvo; a definição do reviewer nomeia a flag.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-27
- **Caso medido que motivou:** ver `## TK-85`.
- **Reparo medido (protótipo do consultor, 2026-09-26, cópia da árvore já apagada):** os três itens acima em `cmd_laudo` e no `laudo_parser`; com eles, `tests/test_rdo.py` inteiro verde (nenhuma asserção existente depende da ordem das seções do laudo) e suíte sem falha; os dois testes abaixo falham sobre o `rdo.py` de hoje. Âncora no agente medida: a frase aparece uma vez no arquivo.
- **Testes (novos, em `tests/test_rdo.py`, com `_argv_laudo` e `rdo.main`; os do item 1 com nome começado por `test_laudo_motivo_`, o do item 2 `test_laudo_achado_dossie_acentuado`):** 1. TF: `_argv_laudo(d, **{"criterio-de-pronto": "parcial"})` mais `--motivo criterio-de-pronto "falta o modo validate"` → exit `0` e o laudo contém `## Motivo das dimensões fora de conforme` e `| criterio-de-pronto | parcial | falta o modo validate |`; TR: `--motivo escopo "x"` com `escopo` `conforme` → exit diferente de `0`; sem `--motivo`, o laudo contém a seção com o corpo `nenhum`. 2. TF: `--achado-processo dossiê "linha do achado"` → exit `0` e o laudo contém `| dossiê | linha do achado |`.
- **Não fazer:** não mudar `calcular_laudo` nem o `close`; não tornar `--motivo` obrigatório; não mudar a tabela de níveis nem o card *Lições aprendidas na tarefa*.
- **Notas de execução:** - 2026-09-26 `review` — rdo.py laudo --motivo + alvo dossiê + reviewer nomeia a flag; 5 testes novos; test_rdo 66 verdes; suíte 426 verdes - 2026-09-27 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-85a-rdo-py-laudo-motivo-e-o-alvo-dossie.md`, veredito ressalva 94%

## Execução

**Consumo:** não medido — executada na sessão principal, fora do loop: sem SubagentStop nem bloco de uso

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 94%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Exercicio ponta a ponta coerente: --motivo e --achado-processo compartilham a mesma forma de recusa (RdoValidationError, exit 1, nenhum laudo escrito) e a mesma guarda de linha; --motivo aceita nao-se-aplica e repeticao da mesma dimensao (duas linhas), o que o card nao proibe. Alvo acentuado so normaliza a forma minuscula exata (Dossie maiusculo e recusado).

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "Com `--desde`, o não rastreado anterior ao ref sai dos tocados" e vai pegar a tarefa "`rdo.py laudo --motivo` e o alvo `dossiê`".
Tarefa "`rdo.py laudo --motivo` e o alvo `dossiê`". Passo: conferir os gates e preparar o despacho.
Tarefa "`rdo.py laudo --motivo` e o alvo `dossiê`". Passo: conferir os gates e preparar o despacho.
Tarefa "`rdo.py laudo --motivo` e o alvo `dossiê`": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "`rdo.py laudo --motivo` e o alvo `dossiê`" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "`rdo.py laudo --motivo` e o alvo `dossiê`": ressalva 94%, bloqueante nenhuma.
Scrum master vai fechar a tarefa "`rdo.py laudo --motivo` e o alvo `dossiê`" como done: registrar estado, RDO e telemetria.
