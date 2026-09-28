# RDO — P-0752 · FPU-T9

# Humano

Tarefa "A skill de fatos frescos" concluída em 2026-09-26.
Uma skill nova obriga toda mensagem ao dono a dizer de onde veio cada número, e proíbe número tirado da memória.
Revisão: aprovada com ressalva (88%).
Pendência para o dono: nenhuma.
Plano "Fato no ponto de uso: os mecanismos contra o esquecimento e a assunção": 13/15 tarefas concluídas; nenhuma tarefa pronta na fila dele.
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achados registrados no plano, com rota: 2 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/plans/P-0752-fato-no-ponto-de-uso.md`
**Tarefa:** `FPU-T9` — A skill de fatos frescos
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `.claude/skills/fatos-frescos/SKILL.md` existe (gatilho: antes de escrever despacho, relatório de janela, encerramento, handover ou mensagem ao dono que leve número, caminho com linha, hash ou contagem); o corpo manda tabular cada valor com a origem em três classes — `rodado neste turno (comando)`, `copiado de <arquivo:linha>`, `memória` — e proíbe enviar valor de origem `memória`; onde há instrumento para o número (`encerrar.py plano`, `telemetria.py`, `card_check.py`), manda usá-lo (DFP-12). A skill é citada por `mensagem-ao-dono` §1, pelo `scrum-master` (seção *Relatório de encerramento*) e pela `passagem-de-bastao` (Parte 3); a frase de contagem do `README.md` passa de `doze skills` a `treze skills` e a tabela de skills ganha a linha.

**Arquivos-alvo:** - `.claude/skills/fatos-frescos/SKILL.md` (novo; frontmatter `name`, `description` sem `: ` no valor — F-11) - `.claude/skills/mensagem-ao-dono/SKILL.md:21` — `## 1. Checagem antes de enviar` - `.claude/skills/scrum-master/SKILL.md:305` — `## Relatório de encerramento` - `.claude/skills/passagem-de-bastao/SKILL.md` — Parte 3, item 2 (`**Materializar o status e registrar**`) - `README.md:851` — `O kit são dez agentes, doze skills, quatro verificadores executáveis e a declaração de projeções,` e a tabela de skills da mesma seção - `.claude/README.md` (projeção regenerada)

**Verificação:** 1. `python -c "from pathlib import Path;print(Path('.claude/skills/fatos-frescos/SKILL.md').exists())"` → `True` — antes `False`, depois `True`. 2. `python -c "from pathlib import Path;print(sum(Path(p).read_text(encoding='utf-8').count('fatos-frescos') for p in ['.claude/skills/mensagem-ao-dono/SKILL.md','.claude/skills/scrum-master/SKILL.md','.claude/skills/passagem-de-bastao/SKILL.md'])>=3)"` → `True` — antes `False`, depois `True`. 3. `python -c "from pathlib import Path;t=Path('README.md').read_text(encoding='utf-8');print(t.count('treze skills'),t.count('doze skills'))"` → `1 0` — antes `0 1`, depois `1 0`. 4. `pwsh .claude/checks/check-readme.ps1` → exit 0 — antes `exit 0`, depois `exit 0` (a frase e a tabela batem com o disco: 13). 5. `python .claude/checks/frontmatter_yaml.py` → exit 0 — antes `exit 0`, depois `exit 0`.

**Pronto quando:** mensagem ao dono.origem dos números — declarada por número: rodado neste turno ou copiado de arquivo e linha — Verificações 1 e 2.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Depende de:** `FPU-T8`
- **Operação do modelo:** `OP-9` - OP-9: A skill de fatos frescos faz toda mensagem ao dono declarar a origem de cada número, e memória deixa de ser origem admitida. - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; mensagem ao dono — Quem implementa faz a origem de cada número ser declarada antes de enviar; memória não é origem.
- **Fundamento:** DFP-12, F-8, causas 1 e 3 de F-10 (total de janela inflado, `AE-26` do `P-0745`; hash copiado de registro antigo).
- **Passos:** 1. Escrever a skill: gatilho, a tabela de origem (três classes), a proibição, a lista de instrumentos por tipo de número, e um exemplo antes/depois de duas linhas. 2. `mensagem-ao-dono` §1: acrescentar o item `- [ ] Todo número, caminho com linha, hash ou contagem passou pela skill \`fatos-frescos\` (origem declarada; memória não é origem).` 3. Scrum-master, *Relatório de encerramento*: acrescentar, depois de `Contadores finais`, a frase `— pela skill \`fatos-frescos\`: totais vêm de \`encerrar.py plano\` ou da série, nunca de soma à mão`. 4. Passagem-de-bastão, Parte 3 item 2: acrescentar `handover passa pela skill \`fatos-frescos\` antes de gravar`. 5. `README.md:851`: `doze skills` → `treze skills`; tabela de skills: linha nova na forma das vizinhas. 6. Regenerar `.claude/README.md` pelo gerador do kit; `pwsh .claude/checks/check-readme.ps1` exit 0.
- **Não fazer:** não criar gancho nem instrumento nesta tarefa; não tocar o bloco A do scrum-master; não tocar `GOVERNANCA.md`.
- **Contingências:** - se `check-readme.ps1` acusar outra contagem por extenso além da linha 851 (`AE-6` do `P-0750`) → trocar também a ocorrência acusada, só ela, e registrar em `pendencia=` a linha.
- **Handover:** 2026-09-26 · para `FPU-T10` - **Entregue:** .claude/skills/fatos-frescos/SKILL.md (nova; origem por valor em tres classes, memoria proibida); citada em mensagem-ao-dono secao 1, scrum-master Relatorio de encerramento (Contadores finais) e passagem-de-bastao Parte 3 item 2; README.md 'treze skills' + linha na tabela; .claude/README.md regenerado por kit_check -Mode generate - **Contrato:** toda mensagem ao dono com numero, caminho:linha, hash ou contagem passa pela skill; check-readme e kit_check check-drift OK com 13 skills - **Não refazer:** nada a declarar - **Pendente:** a secao Instrumentos da skill manda rodar encerrar.py plano (que FECHA o plano) para totais de janela e telemetria.py (so tem append) para consumo; a skill se diz 'regua executavel' contra a OP-9 - card corretivo da OP-9 via consultor
- **Notas de execução:** - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T9-a-skill-de-fatos-frescos.md`, veredito ressalva 88%

## Execução

**Consumo:** 31 tool uses, 91.5 k tokens, 186.7 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 88%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

Motivo do parcial em criterio-de-pronto: a skill que obriga declarar a origem de cada número abre com um número cuja origem declarada não o sustenta - "~35% de 156 trechos classificados... a maior causa isolada de acionamento do consultor" cita F-10, que dá ~35% sobre a amostra inteira (156 trechos, 40 acionamentos, ~60 lições, 118 AE) e não atribui a classe a acionamento do consultor (dos 40, 25 são defeito de autoria ou blocked premissa); e o exemplo "depois" declara consumo "copiado de docs/telemetria.tsv:212", linha que é o TK-51 de 2026-08-24. Gatilho, tabela das três classes, proibição de memória, instrumentos e as três citações (mensagem-ao-dono §1, scrum-master Relatório de encerramento, passagem-de-bastão Parte 3 item 2) e a contagem treze skills estão entregues e verdes (V1-V5, card_check --mundo depois exit 0, check-readme, check-drift 13 skills, frontmatter_yaml exit 0). Lição: card de redação cuja Verificação só conta ocorrência deixa passar o texto que desmente a própria regra - o exemplo de uma norma de proveniência precisa de linha de aceite que confira o ponteiro.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "As armadilhas de ferramenta medidas ganham um arquivo só" e vai pegar a tarefa "A skill de fatos frescos".
Tarefa "A skill de fatos frescos". Passo: conferir os gates e preparar o despacho.
Tarefa "A skill de fatos frescos": gates aprovados; vou materializar in-progress e gravar o ponto de partida.
Agente executor recebe a tarefa "A skill de fatos frescos" e vai executar: `.claude/skills/fatos-frescos/SKILL.md` existe (gatilho: antes de escrever despacho, relatório de janela, encerramento, handover ou mensagem ao dono que leve número, caminho com linha, hash ou contagem); o corpo manda tabular cada valor co…
Agente executor devolveu a tarefa "A skill de fatos frescos": review — sem pendência.
Tarefa "A skill de fatos frescos": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A skill de fatos frescos" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A skill de fatos frescos": ressalva 88%, bloqueante nenhuma.
