# RDO — DIARIO_DE_OBRAS · TK-54b

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-54b` — A fonte da bimodalidade
**Modelo:** Sonnet · **Classe:** investigacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** identificar **qual fonte liga e desliga** entre os dois regimes que a `## 12` mediu — `cache_read` exatamente 18.084 vs 26.695 (Δ **8.611 tok**), `cache_creation` ~16,5k vs ~19,4k, **preâmbulo visível idêntico** (~11.684 chars) nos dois.

**Arquivos-alvo:** `docs/CUSTO_DO_PICKUP.md` (a seção nova, ao fim do portador), `docs/DOC_MAP.md` (contagem de linhas do portador + bullet da seção nova) e `docs/DIARIO_DE_OBRAS.md` (este card: `Status` e bullet de fechamento). A sonda é de scratchpad, descartável e **fora do repo** — decisão 4 de `## TK-54`, não mexer no que se mede.

**Verificação:** `Select-String -Path docs\CUSTO_DO_PICKUP.md -Pattern '^## 16 ' -List` imprime uma linha (a seção começa em 520) · `(Get-Content docs\CUSTO_DO_PICKUP.md).Count` imprime 631, igual à contagem que o `DOC_MAP` publica para o portador · `Select-String -Path docs\CUSTO_DO_PICKUP.md -Pattern 'As quatro can','Veredito: não identificada'` imprime duas linhas (527, o gate das quatro canônicas da `## 12`; 620, o veredito) · `Select-String -Path docs\DOC_MAP.md -Pattern '^## docs/CUSTO_DO_PICKUP.md','## 16 A fonte'` imprime duas linhas (104 e 137). Os quatro rodam a partir de `D:\workspaces\PantonicApp` e foram medidos nesta forma em 2026-09-21.

**Pronto quando:** a seção do `docs/CUSTO_DO_PICKUP.md` nomeia a fonte com evidência, ou publica `não identificada` com a lista do que foi descartado e por quê; e `docs/DOC_MAP.md` registra a seção com a contagem de linhas do portador atualizada.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-21
- **Candidato nomeado, a confirmar ou descartar por sonda (não por argumento):** o mecanismo de *deferred tools* — em algumas janelas um conjunto de ferramentas chega só como nome, em outras com o schema completo, e a ordem de grandeza bate. Descartado o candidato, publica-se o que foi descartado e como.
- **Reparo de forma (2026-09-21, `AE-3`):** o card nasceu em 2026-08-31, antes do `rdo.py` atual, e não declarava `Verificação`, `Pronto quando` nem `Arquivos-alvo` — o gerador de evidência recusava a tarefa **depois** de ela estar entregue. Os três campos acima são **transcrição** do que foi despachado e medido, não escopo novo: `Pronto quando` é o texto literal do antigo *Critério de pronto*, com o número da seção substituído por *a seção do portador* — `## 14` e `## 15` foram ocupadas em 2026-09-20 por outra frente, depois de este card ser escrito, e a entrega saiu na `## 16`; o portador é único (`DX-3`), então a identidade do entregável não mudou.
- **Fecha apontando para:** `## 16` publicada em `docs/CUSTO_DO_PICKUP.md:520-631`.

## Execução

**Consumo:** 56 tool uses, 150.0 k tokens, 628.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: backlog.py check drenou a linha P-0745 do _INBOX.md para _INBOX_HISTORICO.md e regenerou o bloco fila:gerada como efeito colateral do proprio comando de verificacao, nao de edicao do executor
laudo: A fonte da bimodalidade de 8.611 tok e NAO OBSERVAVEL pelo corpus de transcripts em qualquer versao do formato (confirmado por enumeracao exaustiva de chaves na revisao): prosseguir sondando transcript nao pode responder a pergunta do TK-54. Decisao de rota pendente: financiar instrumento fora de banda (proxy/OTEL sobre o request) ou experimento pareado controlado, ou encerrar a pergunta como nao observavel e fechar o TK-54 com o extrato que ja tem.

## Laudo

**Veredito:** ressalva

**Percentual:** 92%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
