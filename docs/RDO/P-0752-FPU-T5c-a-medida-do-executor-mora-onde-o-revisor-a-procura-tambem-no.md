# RDO — P-0752 · FPU-T5c

# Humano

Tarefa "A medida do executor mora onde o revisor a procura, também no plano em pasta" concluída em 2026-09-26.
As instruções do executor e do loop passam a apontar o arquivo de medida no mesmo lugar onde o revisor o procura, também nos planos organizados em pasta.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Fato no ponto de uso: os mecanismos contra o esquecimento e a assunção": 10/15 tarefas concluídas; próxima: "O aviso de crença conta uma vez o literal que casa dois padrões".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achado registrado no plano, com rota: 1 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/plans/P-0752-fato-no-ponto-de-uso.md`
**Tarefa:** `FPU-T5c` — A medida do executor mora onde o revisor a procura, também no plano em pasta
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** o item 5a do executor e a Saída do Passo 5 do scrum-master deixam de fixar `docs/RDO/evidencia/<plano>-<ID>-medida.json` e passam a derivar o destino como `review_evidence.py` o procura (`AE-42`): `<evidencia>/<P-n>-<ID>-medida.json`, com `<P-n>` o id do plano (`P-0752`, nunca o caminho do `--plano`) e `<evidencia>` = `docs/RDO/evidencia` no plano legado ou `<pasta>/evidencia` no plano em pasta. O `pantonic-reviewer.md` não cita o caminho (só nomeia a seção `## Medida do executor`) e não muda.

**Arquivos-alvo:** - `.claude/agents/pantonic-executor.md:127` — `5a. **Medida gravada**: rode` - `.claude/skills/scrum-master/SKILL.md:119` — `cuja ausência vai ao laudo como verificação não` - `.claude/README.md` (projeção regenerada, se o gerador do kit a reescrever)

**Verificação:** 1. `python -c "from pathlib import Path;fs=['.claude/agents/pantonic-executor.md','.claude/skills/scrum-master/SKILL.md'];print(sum(Path(f).read_text(encoding='utf-8').count('<plano>-<ID>-medida.json') for f in fs))"` → `0` — antes `2`, depois `0`. 2. `python -c "from pathlib import Path;fs=['.claude/agents/pantonic-executor.md','.claude/skills/scrum-master/SKILL.md'];print(all('<pasta>/evidencia' in Path(f).read_text(encoding='utf-8') and '<P-n>-<ID>-medida.json' in Path(f).read_text(encoding='utf-8') for f in fs))"` → `True` — antes `False`, depois `True`. 3. `pwsh .claude/checks/kit_check.ps1` → exit 0 — antes `exit 0`, depois `exit 0` (trava; inclui o frontmatter dos agentes).

**Pronto quando:** retorno do executor.evidência de verificação — o executor grava a medida onde o revisor a lê, no plano legado e no plano em pasta — Verificações 1 e 2.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Depende de:** `FPU-T5a`
- **Operação do modelo:** `OP-5` - OP-5: O executor devolve a verificação como arquivo de medida gerado por comando, e o revisor e o loop leem o arquivo. - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; retorno do executor — Quem implementa faz o loop e o revisor lerem o arquivo de medida; prosa não conta como verde.
- **Fundamento:** DFP-6, DFP-17, DFP-19, `AE-42`.
- **Passos:** 1. Executor, item 5a: o trecho `` --gravar docs/RDO/evidencia/<plano>-<ID>-medida.json`; exit 1 `` passa a `` --gravar <evidencia>/<P-n>-<ID>-medida.json`, com `<P-n>` o id do plano (`P-0752`, nunca o caminho) e `<evidencia>` = `docs/RDO/evidencia` no plano legado ou `<pasta>/evidencia` no plano em pasta — a pasta em que `review_evidence.py` procura a medida; exit 1 ``. 2. Scrum-master, Passo 5, Saída: o trecho `` `docs/RDO/evidencia/<plano>-<ID>-medida.json`, cuja ausência `` passa a `` `<evidencia>/<P-n>-<ID>-medida.json` (`<P-n>` o id do plano; `<evidencia>` = `docs/RDO/evidencia` no legado, `<pasta>/evidencia` no plano em pasta), cuja ausência ``, inteiro na mesma linha, sem reflow do parágrafo. 3. Regenerar `.claude/README.md` pelo gerador do kit se ele projetar os arquivos tocados; rodar `pwsh .claude/checks/kit_check.ps1`. Medido pelo consultor em protótipo (acionamento 7): com os dois textos acima, Verificações 1 a 3 no valor `depois`, `kit_check` validate e `check-readme.ps1` exit 0.
- **Não fazer:** não tocar `review_evidence.py` nem `pantonic-reviewer.md`; não mexer nas linhas `--out docs/RDO/evidencia/<plano>-<ID>.md` (outra convenção, fora do `AE-42`); não acrescentar nem remover linha em `scrum-master/SKILL.md` (a âncora `SKILL.md:305` da `FPU-T9` conta linhas); não tocar o frontmatter dos agentes nem o bloco A do scrum-master.
- **Contingências:** - se `kit_check.ps1` acusar contagem no `README.md` por causa da regeneração → a frase de contagem não muda nesta tarefa (nenhum agente ou skill criado): parar e sinalizar `blocked` razão `premissa`, colando a saída.
- **Handover:** 2026-09-26 · para `FPU-T4a` - **Entregue:** .claude/agents/pantonic-executor.md:127 (item 5a) e .claude/skills/scrum-master/SKILL.md:119 (Passo 5, Saida) nomeiam <evidencia>/<P-n>-<ID>-medida.json, <P-n> = id do plano, <evidencia> = docs/RDO/evidencia (legado) ou <pasta>/evidencia (plano em pasta); contagem de linhas do scrum-master inalterada - **Contrato:** a medida do executor mora onde review_evidence a procura, nos dois layouts; kit_check exit 0 - **Não refazer:** caminho da medida ja pago - **Pendente:** docs/RDO/evidencia sem crase em pantonic-executor.md:127 (cosmetico)
- **Notas de execução:** - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T5c-a-medida-do-executor-mora-onde-o-revisor-a-procura-tambem-no.md`, veredito aprovado 100%

## Execução

**Consumo:** 12 tool uses, 58.0 k tokens, 95.4 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master concluiu a tarefa "O dossiê de despacho carrega os achados roteados ao card" e vai pegar a tarefa "A medida do executor mora onde o revisor a procura, também no plano em pasta".
Tarefa "A medida do executor mora onde o revisor a procura, também no plano em pasta". Passo: conferir os gates e preparar o despacho.
Tarefa "A medida do executor mora onde o revisor a procura, também no plano em pasta": gates aprovados; vou materializar in-progress e gravar o ponto de partida.
Agente executor recebe a tarefa "A medida do executor mora onde o revisor a procura, também no plano em pasta" e vai executar: o item 5a do executor e a Saída do Passo 5 do scrum-master deixam de fixar `docs/RDO/evidencia/<plano>-<ID>-medida.json` e passam a derivar o destino como `review_evidence.py` o procura (`AE-42`): `<evidencia>/<P-n>-<ID>-medida.json`, com …
Agente executor devolveu a tarefa "A medida do executor mora onde o revisor a procura, também no plano em pasta": review — sem pendência.
Tarefa "A medida do executor mora onde o revisor a procura, também no plano em pasta": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A medida do executor mora onde o revisor a procura, também no plano em pasta" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A medida do executor mora onde o revisor a procura, também no plano em pasta": aprovado 100%, bloqueante nenhuma.
