---
name: fatos-frescos
description: Antes de escrever despacho, relatório de janela, encerramento, handover ou mensagem ao dono que leve número, caminho com linha, hash ou contagem — tabula cada valor com a origem e proíbe enviar valor de origem memória. Usar sempre que o texto for carregar um número, um caminho com linha, um hash ou uma contagem.
---

# fatos-frescos — a origem de todo número é o ponto de uso

Amostra de 2026-09-26 (`P-0752-fato-no-ponto-de-uso.md` F-10): valor reutilizado em vez de medido
é a maior causa isolada de acionamento do consultor (~35% de 156 trechos classificados). Esta
skill é a medida em prosa da DFP-12, e não conferência executável — não substitui o instrumento onde ele existe (DFP-12, emendada pela DFP-21).

## Gatilho

Antes de escrever despacho, relatório de janela, encerramento, handover ou mensagem ao dono que
leve número, caminho com linha, hash ou contagem.

## Tabela de origem

Todo valor do texto entra numa das três classes:

| origem | o que significa |
|---|---|
| `rodado neste turno (comando)` | o comando que produziu o valor rodou nesta janela; o comando e o resultado ficam citados junto do valor. |
| `copiado de <arquivo:linha>` | o valor já estava em disco; a citação aponta o arquivo e a linha exata onde ele mora. |
| `memória` | o valor veio de recall, contexto de outra janela ou suposição — **origem proibida**. |

## Proibição

Nenhum número, caminho com linha, hash ou contagem sai com origem `memória`. Valor sem origem
`rodado neste turno` ou `copiado de <arquivo:linha>` não é enviado — é medido de novo, no turno,
antes do envio.

## Instrumentos por tipo de número

Onde existe instrumento de leitura para o número, ele é obrigatório — a tabela de origem cobre o
que não tem um (DFP-12, emendada pela DFP-21). Instrumento que escreve não é origem: `encerrar.py
plano` fecha o plano (exige o veredito do dono e recusa plano com tarefa aberta) e `telemetria.py`
só apensa linha à série.

- **Tarefas fechadas do plano** → a projeção `(<status>, <fechadas>/<total>)` do plano no índice
  de `docs/DIARIO_DE_OBRAS.md`, que `backlog.py status` reescreve a cada transição, lida no turno
  e citada como `copiado de docs/DIARIO_DE_OBRAS.md:<linha>`; as fechadas na janela são as que o
  próprio relatório lista com o RDO; nunca contagem de cabeça.
- **Consumo** (tool_uses, tokens, duração) → a série `docs/telemetria.tsv`: de uma tarefa, a linha
  dela, citada como `copiado de docs/telemetria.tsv:<linha>`; acumulado da janela, a soma rodada
  no turno, `python -c "import csv;r=[l for l in
  csv.DictReader(open('docs/telemetria.tsv',encoding='utf-8'),delimiter='\t') if
  l['tarefa'].startswith('<prefixo>')];print(len(r),round(sum(float(l['tokens_k']) for l in
  r),1))"`; nunca soma à mão.
- **Evidência de card** (itens de verificação, bate/não bate) → `python
  .claude/tools/card_check.py --plano <plano> --tarefa <ID> --mundo <antes|depois> --gravar
  <caminho>`.

## Exemplo

- antes:

  ~~~~
  A FPU-T9 custou uns 90k tokens.
  ~~~~

- depois:

  ~~~~
  A FPU-T9 custou 91.5k tokens e 31 tool_uses (copiado de `docs/telemetria.tsv:894`).
  ~~~~
