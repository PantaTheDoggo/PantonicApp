---
name: mensagem-ao-dono
description: Checagem de toda mensagem escrita para o dono humano — conversa, handover, relatório de janela, rodada de decisões. Troca a sigla sozinha pelo título entre aspas, traz para o corpo o que o dono precisa para decidir e registra a falha quando o dono teve de perguntar. Usar antes de enviar ao dono mensagem que cite sigla do kit ou aponte arquivo, e ao receber dele pergunta de esclarecimento.
---

# mensagem-ao-dono — a mensagem se entende sozinha

A regra mora em `GOVERNANCA.md` §4.2 (*Mensagem legível ao dono*); esta skill é o procedimento.

## Gatilho

1. Antes de enviar ao dono mensagem que cite sigla do kit (tarefa, tíquete, plano, decisão,
   achado, regra de roteamento, guardrail) ou aponte arquivo.
2. Ao receber do dono pergunta do tipo "o que é", "o que significa" ou "onde está" sobre algo que
   um agente escreveu — é falha medida (§4).

Fora do alcance: a superfície agente↔agente (dossiê, retorno do executor, laudo,
`passagem-de-bastao`), onde a sigla crua é o contrato; documento publicado (`redacao-doc`);
documento de encerramento de plano (`entrega-de-encerramento`), que já define todo termo no texto.

## 1. Checagem antes de enviar

- [ ] Toda sigla foi trocada pelo título entre aspas duplas (§2). A sigla só acompanha, entre
      parênteses, quando o dono precisa digitá-la para agir.
- [ ] O dono decide ou valida sem abrir arquivo: o fato que sustenta cada pedido está no corpo, e
      o caminho é complemento.
- [ ] Termo interno (laudo, evidência, janela, marco) tem glosa curta na primeira ocorrência.
- [ ] Pedido de decisão no formato do §3.
- [ ] Escrita no idioma em que o dono conversa.
- [ ] Todo número, caminho com linha, hash ou contagem passou pela skill `fatos-frescos` (origem
      declarada; memória não é origem).

Exemplo — antes: `Próximo: TK-38.` · depois: `Próximo: o tíquete "Comunicação entre agente e
humano — skill própria e requisitos mínimos" (TK-38).` (a sigla fica porque o dono a digita para
mandar executar).

## 2. Onde achar o título

| sigla | onde está o título | como buscar |
|---|---|---|
| tarefa `<PFX>-T<n>`, tíquete `TK-<n>`, plano `P-NNNN` | o cabeçalho do item | `python .claude/tools/backlog.py show <ID>` — o título é o texto da primeira linha entre ` — ` e ` [`; sem ` [` na linha, vai até o fim dela |
| decisão, fato, invariante, achado (`D…-<n>`, `F-<n>`, `I-<n>`, `AE-<n>`) | a linha que a define no plano de origem | busca de texto por `**<ID>**` ou `\| <ID> \|` no plano; o título é a primeira oração |
| regra de roteamento `A<n>` ou `B<n>` | a coluna *condição* das tabelas dos blocos A e B da skill `scrum-master` | a condição, em palavras |
| guardrail `G-<NOME>` | a lista de `GOVERNANCA.md` §7 | o nome da regra |
| família de sigla | o glossário do `README.md`, bullet *Identificadores de trabalho* | — |

Sem título achado, a sigla vai com uma frase que diga o que ela nomeia — nunca sozinha.

## 3. Pedido de decisão

Uma mensagem, todas as questões juntas. Cada questão traz: o fato medido que a originou, as
opções com o que cada uma implica, o que fica bloqueado sem resposta, a recomendação com o motivo
e, quando existir, a opção "registrar e não agir". É o mesmo formato do relatório de encerramento
da skill `scrum-master` e da rodada de decisões do `pantonic-planner`; esta seção não o redefine.

## 4. Registro de falha

O dono perguntou o que algo significa, onde algo está, ou teve de abrir arquivo para decidir:
quem recebeu a pergunta apensa **uma** linha a `docs/FALHAS_COMUNICACAO.tsv` antes de responder,
sem reescrever linha anterior. Colunas separadas por TAB:

| coluna | conteúdo |
|---|---|
| `data` | `AAAA-MM-DD` |
| `superficie` | conversa, handover, relatório de janela, rodada de decisões, painel ou documento |
| `o_que_faltou` | a sigla ou o termo sem glosa, ou o dado que só estava fora da mensagem |
| `custo_prompts` | prompts do dono gastos no esclarecimento |
| `correcao` | o que muda na regra ou nesta skill para não repetir, ou `-` |
| `fonte` | caminho do registro do caso, ou `-` |

A tabela se lê em conjunto na revisão da doutrina (`GOVERNANCA.md` §7.1); uma linha isolada não
muda esta skill.
