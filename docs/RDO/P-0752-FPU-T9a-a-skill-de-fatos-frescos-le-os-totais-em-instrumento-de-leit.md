# RDO — P-0752 · FPU-T9a

# Humano

Tarefa "A skill de fatos frescos lê os totais em instrumento de leitura e se declara medida em prosa" concluída em 2026-09-26.
A skill de fatos frescos passa a apontar só instrumentos que leem números, e deixa de mandar fechar o plano para contar tarefas.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Fato no ponto de uso: os mecanismos contra o esquecimento e a assunção": 15/17 tarefas concluídas; nenhuma tarefa pronta na fila dele.
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achado registrado no plano, com rota: 1 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/plans/P-0752-fato-no-ponto-de-uso.md`
**Tarefa:** `FPU-T9a` — A skill de fatos frescos lê os totais em instrumento de leitura e se declara medida em prosa
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** a skill `fatos-frescos` deixa de mandar rodar `encerrar.py plano` (que fecha o plano) e `telemetria.py` (que só apensa) para obter números, e aponta os instrumentos de leitura da DFP-21 — tarefas fechadas na projeção do índice de `docs/DIARIO_DE_OBRAS.md`, consumo na série `docs/telemetria.tsv` (`AE-47`); o exemplo cita uma linha real da série; a skill se declara a medida em prosa da DFP-12, sem o rótulo "régua executável" (`AE-48`); o *Relatório de encerramento* do `scrum-master` troca `encerrar.py plano` pelo índice do diário e pela série.

**Arquivos-alvo:** - `.claude/skills/fatos-frescos/SKILL.md:10` — `skill é a régua executável dessa medida — não substitui o instrumento onde ele existe (DFP-12).` - `.claude/skills/fatos-frescos/SKILL.md:35` — `Onde existe instrumento para o número, o instrumento é obrigatório — a tabela de origem cobre o` - `.claude/skills/fatos-frescos/SKILL.md:49` — `- antes: \`Fechamos 3 tarefas nesta janela, consumo de ~40k tokens.\`` - `.claude/skills/scrum-master/SKILL.md:316` — `totais vêm de \`encerrar.py plano\` ou da série, nunca de soma à mão.`

**Verificação:** 1. `python -c "from pathlib import Path;s=Path('.claude/skills/fatos-frescos/SKILL.md').read_text(encoding='utf-8');print('encerrar.py plano --plano' in s,'é a régua executável' in s,'medida em prosa' in s)"` → `False False True` — antes `True True False`, depois `False False True`. 2. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');q=chr(96);print(t.count('totais vêm de '+q+'encerrar.py plano'),t.count('totais vêm do índice do diário e da série'))"` → `0 1` — antes `1 0`, depois `0 1`. 3. `python -c "from pathlib import Path;s=Path('.claude/skills/fatos-frescos/SKILL.md').read_text(encoding='utf-8');c=Path('docs/telemetria.tsv').read_text(encoding='utf-8').splitlines()[893].split(chr(9));print('docs/telemetria.tsv:894' in s and '91.5k tokens e 31 tool_uses' in s and c[2]=='FPU-T9' and c[4]=='31' and c[5]=='91.5')"` → `True` — antes `False`, depois `True` (o exemplo confere com a linha que ele cita). 4. `python .claude/checks/frontmatter_yaml.py` → exit 0 — antes `exit 0`, depois `exit 0` (trava). 5. `pwsh .claude/checks/check-readme.ps1` → exit 0 — antes `exit 0`, depois `exit 0` (trava: a `description` não muda).

**Pronto quando:** mensagem ao dono.origem dos números — declarada por número: rodado neste turno ou copiado de arquivo e linha — Verificações 1 a 3.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Depende de:** `FPU-T9`
- **Operação do modelo:** `OP-9` - OP-9: A skill de fatos frescos faz toda mensagem ao dono declarar a origem de cada número, e memória deixa de ser origem admitida. - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.; mensagem ao dono — Quem implementa faz a origem de cada número ser declarada antes de enviar; memória não é origem.
- **Fundamento:** DFP-12, DFP-21, `AE-47`, `AE-48`.
- **Passos:** 1. Skill, linha 10: o trecho `skill é a régua executável dessa medida — não substitui o instrumento onde ele existe (DFP-12).` passa a `skill é a medida em prosa da DFP-12, e não conferência executável — não substitui o instrumento onde ele existe (DFP-12, emendada pela DFP-21).` 2. Skill, `Instrumentos por tipo de número`: o título fica; o corpo (linhas 35 a 45, do parágrafo `Onde existe instrumento…` ao fim do bullet **Evidência de card**) passa a ser o parágrafo e os três bullets abaixo, transcritos, com quebra de linha livre até 100 colunas: - parágrafo: `Onde existe instrumento de leitura para o número, ele é obrigatório — a tabela de origem cobre o que não tem um (DFP-12, emendada pela DFP-21). Instrumento que escreve não é origem: \`encerrar.py plano\` fecha o plano (exige o veredito do dono e recusa plano com tarefa aberta) e \`telemetria.py\` só apensa linha à série.` - bullet 1: `- **Tarefas fechadas do plano** → a projeção \`(<status>, <fechadas>/<total>)\` do plano no índice de \`docs/DIARIO_DE_OBRAS.md\`, que \`backlog.py status\` reescreve a cada transição, lida no turno e citada como \`copiado de docs/DIARIO_DE_OBRAS.md:<linha>\`; as fechadas na janela são as que o próprio relatório lista com o RDO; nunca contagem de cabeça.` - bullet 2: `- **Consumo** (tool_uses, tokens, duração) → a série \`docs/telemetria.tsv\`: de uma tarefa, a linha dela, citada como \`copiado de docs/telemetria.tsv:<linha>\`; acumulado da janela, a soma rodada no turno, \`python -c "import csv;r=[l for l in csv.DictReader(open('docs/telemetria.tsv',encoding='utf-8'),delimiter='\t') if l['tarefa'].startswith('<prefixo>')];print(len(r),round(sum(float(l['tokens_k']) for l in r),1))"\`; nunca soma à mão.` O comando foi rodado pelo consultor (acionamento 9) com o prefixo `FPU-T`: exit 0, dois números. - bullet 3: o bullet **Evidência de card** de hoje, sem mudança. 3. Skill, `Exemplo`: as linhas de hoje (antes e depois, linhas 49 a 52) passam a duas, `- antes: A FPU-T9 custou uns 90k tokens.` e `- depois: A FPU-T9 custou 91.5k tokens e 31 tool_uses (copiado de \`docs/telemetria.tsv:894\`).` — a linha 894 da série é a da `FPU-T9`, medida pelo consultor. 4. Scrum-master, linha 316: o trecho `totais vêm de \`encerrar.py plano\` ou da série, nunca de soma à mão.` passa a `totais vêm do índice do diário e da série \`docs/telemetria.tsv\`, nunca de soma à mão.`, na mesma linha, sem reflow. Medido pelo consultor em protótipo (acionamento 9): com os Passos 1 a 4, Verificações 1 a 3 no valor `depois`.
- **Não fazer:** não tocar o frontmatter da skill (a `description` alimenta `.claude/README.md`); não tocar `mensagem-ao-dono` nem `passagem-de-bastao` (o item do checklist é o ponto de uso da skill, não conferência da régua — DFP-21); não tocar `encerrar.py` (I-4) nem `telemetria.py` (`FPU-T7`); não tocar o bloco de fechamento do plano no `scrum-master` (`encerrar.py plano --plano`); não acrescentar nem remover linha em `scrum-master/SKILL.md`.
- **Contingências:** - se a linha 894 de `docs/telemetria.tsv` não for mais a da `FPU-T9` → parar e sinalizar `blocked` razão `premissa`, colando a linha (a série nunca se reescreve, DFP-8).
- **Handover:** 2026-09-26 · para `FPU-T10` - **Entregue:** .claude/skills/fatos-frescos/SKILL.md: linha 10 declara a skill 'medida em prosa da DFP-12'; secao Instrumentos le totais no indice do diario e consumo na serie docs/telemetria.tsv; exemplo cita docs/telemetria.tsv:894 (FPU-T9); .claude/skills/scrum-master/SKILL.md:316 idem - **Contrato:** nenhum instrumento de escrita (encerrar.py plano, telemetria.py) e origem de numero na skill; frontmatter e check-readme OK - **Não refazer:** instrumentos de leitura ja pagos - **Pendente:** fatos-frescos/SKILL.md:57 tem duas sequencias barra-crase (literal com crase fora de bloco cercado, contra o criterio xi da rubrica 8)
- **Notas de execução:** - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T9a-a-skill-de-fatos-frescos-le-os-totais-em-instrumento-de-leit.md`, veredito aprovado 100%

## Execução

**Consumo:** 12 tool uses, 55.1 k tokens, 61.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

Card corretivo transcrito pelo consultor com os valores medidos em protótipo fechou sem parada; o único resíduo nasceu onde o próprio card deixou um literal com crase fora de bloco cercado - o critério (xi) da régua de autoria, que o card_check ainda não confere.

## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master concluiu a tarefa "A régua de autoria do card aponta as armadilhas de ferramenta" e vai pegar a tarefa "A skill de fatos frescos lê os totais em instrumento de leitura e se declara medida em prosa".
Tarefa "A skill de fatos frescos lê os totais em instrumento de leitura e se declara medida em prosa". Passo: conferir os gates e preparar o despacho.
Tarefa "A skill de fatos frescos lê os totais em instrumento de leitura e se declara medida em prosa": gates aprovados; vou materializar in-progress e gravar o ponto de partida.
Agente executor recebe a tarefa "A skill de fatos frescos lê os totais em instrumento de leitura e se declara medida em prosa" e vai executar: a skill `fatos-frescos` deixa de mandar rodar `encerrar.py plano` (que fecha o plano) e `telemetria.py` (que só apensa) para obter números, e aponta os instrumentos de leitura da DFP-21 — tarefas fechadas na projeção do índice de `docs/DIA…
Agente executor devolveu a tarefa "A skill de fatos frescos lê os totais em instrumento de leitura e se declara medida em prosa": review — sem pendência.
Tarefa "A skill de fatos frescos lê os totais em instrumento de leitura e se declara medida em prosa": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A skill de fatos frescos lê os totais em instrumento de leitura e se declara medida em prosa" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A skill de fatos frescos lê os totais em instrumento de leitura e se declara medida em prosa": aprovado 100%, bloqueante nenhuma.
