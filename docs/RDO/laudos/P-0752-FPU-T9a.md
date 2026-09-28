# Laudo — P-0752 · FPU-T9a

**Percentual:** 100%
**Veredito:** aprovado
**Dimensão bloqueante:** nenhuma
**Recomendação:** seguir
**Pendência:** nenhuma

| dimensão | nível |
|---|---|
| criterio-de-pronto | conforme |
| escopo | conforme |
| testes | nao-se-aplica |
| guardas | conforme |
| rota | conforme |
| residuo | nao-se-aplica |
| registro | conforme |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Decisão que o card não fechou (G-NOASK): o Passo 3 publicou a linha nova do Exemplo em crase simples com as crases internas escapadas por barra invertida, contra o critério (xi) da RUBRICA §8 (literal com crase vai em bloco cercado); a entrega decidiu manter as barras e envolver a linha em crase simples, e .claude/skills/fatos-frescos/SKILL.md:57 ficou com duas sequências barra-crase literais - o trecho de código fecha em "copiado de \" e a barra aparece no exemplo que modela a mensagem ao dono. A Verificação 3 confere só substrings e não discrimina a forma. Rota: item de replanejamento do P-0752 via consultor - card corretivo da OP-9 que reescreve a linha 57 com o literal em bloco cercado e uma Verificação que conta chr(92)+chr(96) no arquivo (antes 2, depois 0). |
| dossiê | A evidência atribui .claude/skills/scrum-master/SKILL.md à FPU-T2 (alvo ancorado com literal) e lista arquivos ?? fora dos alvos sem atribuição; reconciliado por mtime (depois do laudo da FPU-T9 só mudaram os dois alvos, o JSON de medida e registro da orquestração) e por git diff (a linha 316 do scrum-master traz o texto do Passo 4, arquivo com 409 linhas, bloco "encerrar.py plano --plano" intacto na linha 339). Rota: já roteada - TK-84a (AE-35) e TK-89a (AE-38); sem ação nova. |

## Lições aprendidas na tarefa

Card corretivo transcrito pelo consultor com os valores medidos em protótipo fechou sem parada; o único resíduo nasceu onde o próprio card deixou um literal com crase fora de bloco cercado - o critério (xi) da régua de autoria, que o card_check ainda não confere.
