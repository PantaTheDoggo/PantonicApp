# Laudo — DIARIO_DE_OBRAS · TK-91a

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
| dossiê | Erro inequívoco, rota imediata: o card fechou o texto do marco no bullet Emenda e proibiu mudar outra linha, mas deixou a seção '## A forma da devolução' do mesmo arquivo (.claude/agents/pantonic-model-designer.md:117-124) sem o caso do marco: o item 1 manda devolver o ponteiro para a '## 1A' 'em todo ato que versiona', e no aceite a '## 1A' sai do plano (a seção escrita é a '## 1'); o item 2 manda devolver 'a linha da versão do ato', e o marco não cria linha, muda a situação de duas linhas já existentes (pendente->vigente, anterior->obsoleta; na recusa, remove a da pendente). Um modelador que parte do zero e executa o desfecho do marco recebe uma forma de devolução que não cabe no ato — a mesma classe de defeito que abriu o TK-91. A entrega inseriu o bloco do card literalmente e não se rebaixa por isso. Rota: card corretivo TK-91b no tíquete TK-91, aberto agora e antes de fechar o TK-91, que acrescenta aos itens 1 e 2 da '## A forma da devolução' o desfecho do marco (aceita: ponteiro para a '## 1' e as duas linhas com a situação alterada; recusada: ponteiro para a '## 1' intacta e a linha removida). |
| dossiê | Evidência sem o contexto da árvore (reconciliado, sem efeito na entrega): o dossiê de evidência lista 26 arquivos fora dos alvos e sem atribuição. São todos '??' anteriores ao despacho: o mtime do mais novo (docs/ACIONAMENTOS_CONSULTOR.tsv, 19:16:11Z) é anterior ao stash de despacho 8c8b6fb (19:17:33Z), e o stash não guarda arquivo não rastreado. O 'git diff 8c8b6fb' só mostra três arquivos: o alvo (+6 linhas, iguais ao bloco do card, recuo de dois espaços, LF), docs/DIARIO_DE_OBRAS.md (só o status in-progress->review, da orquestração) e docs/telemetria.tsv (linha de consumo medida, da orquestração). O literal da âncora aparece como 'não reconhecido como caminho'. Rota: tíquete TK-89 já existente (AE-38; conhecido também como AE-35 / TK-84a), sem tíquete novo. |

## Lições aprendidas na tarefa

No card de redação que insere texto literal num arquivo de agente, o 'Não fazer: sem mudar outra linha' tranca a execução no bloco ditado, e a coerência com as outras seções do mesmo arquivo (aqui, a forma da devolução) fica a cargo apenas de quem escreve o card. Para cada ato novo ou desfecho novo, quem escreve o card precisa confrontar o texto com as seções que descrevem a entrada (gramática), a saída (devolução) e as proibições do mesmo agente.
