# RDO — P-0752 · FPU-T8a

# Humano

Tarefa "A régua de autoria do card aponta as armadilhas de ferramenta" concluída em 2026-09-26.
A régua de revisão dos cards passa a apontar o arquivo de armadilhas de ferramenta.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Fato no ponto de uso: os mecanismos contra o esquecimento e a assunção": 14/17 tarefas concluídas; próxima: "A skill de fatos frescos lê os totais em instrumento de leitura e se declara medida em prosa".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0752-fato-no-ponto-de-uso.md`
**Tarefa:** `FPU-T8a` — A régua de autoria do card aponta as armadilhas de ferramenta
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** a `## 8` de `docs/RUBRICA_DE_REVISAO.md`, que se nomeia "régua de **autoria** do card", passa a apontar `docs/ARMADILHAS_DE_FERRAMENTA.md` (`AE-46`): a OP-8 manda o arquivo ser apontado pela doutrina e pela régua do card, e a `FPU-T8` só o apontou em `GOVERNANCA.md` e no campo `Verificação` do planejador.

**Arquivos-alvo:** - `docs/RUBRICA_DE_REVISAO.md:288` — `> Fonte da verdade: régua de **autoria** do card, aplicada **antes** do despacho`

**Verificação:** 1. `python -c "from pathlib import Path;print(Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8').count('ARMADILHAS_DE_FERRAMENTA'))"` → `1` — antes `0`, depois `1`. 2. `python -c "from pathlib import Path;l=Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8').splitlines();print([x.startswith('> Fonte da verdade') for x in l if 'ARMADILHAS_DE_FERRAMENTA' in x]==[True])"` → `True` — antes `False`, depois `True`.

**Pronto quando:** armadilhas de ferramenta.residência — um arquivo, apontado pela doutrina e pela régua do card — Verificações 1 e 2.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Depende de:** `FPU-T8`
- **Operação do modelo:** `OP-8` - OP-8: As armadilhas de ferramenta medidas ganham um arquivo só, apontado pela doutrina e pela régua do card. - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.
- **Fundamento:** DFP-20, DFP-21, `AE-46`.
- **Passos:** 1. Na linha 288, depois do ponto final de `esta julga o dossiê que a pediu.`, acrescentar, na mesma linha, um espaço e a frase `Armadilhas de ferramenta medidas: \`docs/ARMADILHAS_DE_FERRAMENTA.md\` — consultar antes de escrever linha de Verificação.` Medido pelo consultor em protótipo (acionamento 9): Verificações 1 e 2 no valor `depois`.
- **Não fazer:** não acrescentar nem remover linha em `docs/RUBRICA_DE_REVISAO.md` (a âncora das linhas 340-341 do `TK-89b` conta linhas); não tocar a `### 8.1` (matéria do `TK-89b`) nem a tabela de critérios; não tocar `docs/ARMADILHAS_DE_FERRAMENTA.md`.
- **Contingências:** - se a linha 288 não começar mais por `> Fonte da verdade` → acrescentar a frase ao fim da linha do blockquote que abre a `## 8`, onde ela estiver, e registrar a linha em `pendencia=`.
- **Handover:** 2026-09-26 · para `FPU-T9a` - **Entregue:** docs/RUBRICA_DE_REVISAO.md:288 (linha '> Fonte da verdade' da secao 8) ganhou o ponteiro para docs/ARMADILHAS_DE_FERRAMENTA.md na mesma linha; contagem do arquivo mantida em 373 - **Contrato:** a regua de autoria do card aponta as armadilhas medidas - **Não refazer:** ponteiro na rubrica ja pago - **Pendente:** nenhum
- **Notas de execução:** - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T8a-a-regua-de-autoria-do-card-aponta-as-armadilhas-de-ferrament.md`, veredito aprovado 100%

## Execução

**Consumo:** 8 tool uses, 48.9 k tokens, 39.6 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

Card corretivo da OP-8 aberto pelo achado de dossiê do laudo da FPU-T8 fechou num ato: frase transcrita, âncora com literal, duas Verificações com os dois mundos medidos pelo consultor em protótipo e restrição de contagem de linhas re-derivável (373 antes e depois) - nenhuma decisão restou ao executor.

## Fechamento

**Desdobramento:** aprovado

# Histórico

Tarefa "A régua de autoria do card aponta as armadilhas de ferramenta": gates aprovados; vou materializar in-progress e gravar o ponto de partida.
Scrum master concluiu a tarefa "A skill de fatos frescos" e vai pegar a tarefa "A régua de autoria do card aponta as armadilhas de ferramenta".
Tarefa "A régua de autoria do card aponta as armadilhas de ferramenta". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "A régua de autoria do card aponta as armadilhas de ferramenta" e vai executar: a `## 8` de `docs/RUBRICA_DE_REVISAO.md`, que se nomeia "régua de **autoria** do card", passa a apontar `docs/ARMADILHAS_DE_FERRAMENTA.md` (`AE-46`): a OP-8 manda o arquivo ser apontado pela doutrina e pela régua do card, e a `FPU-T8` só o…
Agente executor devolveu a tarefa "A régua de autoria do card aponta as armadilhas de ferramenta": review — sem pendência.
Tarefa "A régua de autoria do card aponta as armadilhas de ferramenta": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A régua de autoria do card aponta as armadilhas de ferramenta" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A régua de autoria do card aponta as armadilhas de ferramenta": aprovado 100%, bloqueante nenhuma.
