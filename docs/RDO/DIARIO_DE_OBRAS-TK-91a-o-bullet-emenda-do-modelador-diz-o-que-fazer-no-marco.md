# RDO — DIARIO_DE_OBRAS · TK-91a

# Humano

Tarefa "O bullet Emenda do modelador diz o que fazer no marco" concluída em 2026-09-26.
O modelador passa a ter escrito o que fazer com a versão pendente do modelo quando o dono a aceita ou recusa.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Tíquete "O modelador não tem o ato que promove ou elimina a versão pendente no marco": 1/1 tarefas concluídas; nenhuma tarefa pronta na fila dele.
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achado registrado no plano, com rota: 1 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-91a` — O bullet Emenda do modelador diz o que fazer no marco
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** o arquivo do modelador descreve o desfecho da versão pendente no marco, aceita ou recusada, na forma da `GOVERNANCA.md` §3.2, dentro do ato `emenda`.

**Arquivos-alvo:** - `.claude/agents/pantonic-model-designer.md:88` — `toca**: quem decide entre as duas é o marco, nunca você.`

**Verificação:** 1. `python -c "from pathlib import Path;t=Path('.claude/agents/pantonic-model-designer.md').read_text(encoding='utf-8');print('Caiu pelo aceite da versão' in t)"` → `True` — antes `False`, depois `True`. 2. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate` → `kit_check: OK` — antes `exit 0`, depois `exit 0`. 3. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `kit_check: check-drift OK` — antes `exit 0`, depois `exit 0`.

**Pronto quando:** o bullet **Emenda** do modelador diz o desfecho da pendente no marco, aceita e recusada, e os dois modos do `kit_check` seguem exit 0 (medido em protótipo sobre a árvore, revertido, em 2026-09-26).

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Passos:** 1. Logo depois da linha 88 de `.claude/agents/pantonic-model-designer.md`, dentro do bullet **Emenda**, inserir as seis linhas do bloco abaixo, cada uma com dois espaços de recuo no arquivo, como as linhas vizinhas do bullet, sem mudar outra linha do arquivo: ```text **No marco**, o desfecho da pendente chega em novo dossiê `Ato: emenda`, com a validação do consultor e o ato do dono em `Motivo`. Aceita: o conteúdo da `## 1A` passa à `## 1`, com o cabeçalho em `situação: vigente`; a `## 1A` sai do plano; no registro de versões a pendente passa a `vigente` e a anterior a `obsoleta`, com a frase `Caiu pelo aceite da versão <N> em <data>` — a linha fica, o conteúdo da obsoleta não. Recusada: a `## 1A` e a linha dela saem, e a vigente fica sem marca (`GOVERNANCA.md` §3.2, *Versão vigente, pendente e obsoleta*). ```
- **Não fazer:** não criar ato novo nem valor novo no campo `Ato` (a gramática de seis campos é da `GOVERNANCA.md` §3.2); não tocar a `GOVERNANCA.md`; não mudar o título `## Os quatro atos`.
- **Contingências:** - se a linha 88 não trouxer o literal ancorado (o gate de âncora acusa) → inserir as seis linhas logo depois da linha que termina o bullet **Emenda** com `quem decide entre as duas é o marco, nunca você.`, e registrar a linha em `pendencia=`.
- **Handover:** 2026-09-26 · para `pantonic-model-designer` - **Entregue:** .claude/agents/pantonic-model-designer.md: bullet Emenda (apos a linha 88) descreve o desfecho da pendente no marco, aceita e recusada; secao 'A forma da devolucao' itens 1 e 2 cobrem o marco (corrigido pelo condutor no ato, achado do revisor) - **Contrato:** o modelador promove ou elimina a versao pendente no marco pelo ato emenda; kit_check validate e check-drift OK - **Não refazer:** nada a declarar - **Pendente:** nenhum
- **Notas de execução:** - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-91a-o-bullet-emenda-do-modelador-diz-o-que-fazer-no-marco.md`, veredito aprovado 100%

## Execução

**Consumo:** 9 tool uses, 52.1 k tokens, 72.8 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

No card de redação que insere texto literal num arquivo de agente, o 'Não fazer: sem mudar outra linha' tranca a execução no bloco ditado, e a coerência com as outras seções do mesmo arquivo (aqui, a forma da devolução) fica a cargo apenas de quem escreve o card. Para cada ato novo ou desfecho novo, quem escreve o card precisa confrontar o texto com as seções que descrevem a entrada (gramática), a saída (devolução) e as proibições do mesmo agente.

## Fechamento

**Desdobramento:** aprovado

# Histórico

Tarefa "O bullet Emenda do modelador diz o que fazer no marco": gates aprovados; vou materializar in-progress e gravar o ponto de partida.
Agente executor recebe a tarefa "O bullet Emenda do modelador diz o que fazer no marco" e vai executar: o arquivo do modelador descreve o desfecho da versão pendente no marco, aceita ou recusada, na forma da `GOVERNANCA.md` §3.2, dentro do ato `emenda`.
Agente executor devolveu a tarefa "O bullet Emenda do modelador diz o que fazer no marco": review — sem pendência.
Tarefa "O bullet Emenda do modelador diz o que fazer no marco": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "O bullet Emenda do modelador diz o que fazer no marco" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "O bullet Emenda do modelador diz o que fazer no marco": aprovado 100%, bloqueante nenhuma.
