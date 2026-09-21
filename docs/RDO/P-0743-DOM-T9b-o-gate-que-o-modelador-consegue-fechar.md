# RDO — P-0743 · DOM-T9b

**Plano:** `docs/plans/P-0743-modelo-de-dominio.md`
**Tarefa:** `DOM-T9b` — O gate que o modelador consegue fechar
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** o bullet do gate em `.claude/agents/pantonic-model-designer.md` distinguindo a violação que é do modelador da que mora no card, para que o ato dele possa terminar num plano em conversão.

**Arquivos-alvo:** - `.claude/agents/pantonic-model-designer.md` - **um** ponto, medido em 2026-09-21 e re-derivado no despacho (`I-5`): o bullet do gate em `## Fatos estáveis`, linhas 22-24 (bloco **T1**)

**Verificação:** Literal que **sai**, inteiro numa linha só: ``` grep -cF -e 'o ato com exit `0`. Exit diferente de `0` é ato não concluído' .claude/agents/pantonic-model-designer.md ``` imprime `0` (hoje imprime `1`, na linha 23, medido 2026-09-21). Literais que **entram**, cada um inteiro numa linha só do bloco (`I-15`): ``` grep -cF -e 'Violação indexada pelo **`<ID>` de uma tarefa** (`V2`, `V4`, `V14`) **não é sua**' .claude/agents/pantonic-model-designer.md ``` imprime `1` (hoje imprime `0`, medido 2026-09-21). ``` grep -cF -e 'do `check`, nomeando as violações que ficaram' .claude/agents/pantonic-model-designer.md ``` imprime `1` (hoje imprime `0`, medido 2026-09-21). **Guardas — o que não pode mudar:** ``` grep -c '^## ' .claude/agents/pantonic-model-designer.md ``` imprime `6` (hoje imprime `6`, **inalterado**). ``` grep -cF -e '## Os quatro atos' .claude/agents/pantonic-model-designer.md ``` imprime `1` (hoje imprime `1`, **inalterado**). ``` grep -c '^- ' .claude/agents/pantonic-model-designer.md ``` imprime `19` (hoje imprime `19`, **inalterado**, medido 2026-09-21): o bloco T1 é **um** bullet, como o que ele substitui — o total de bullets de primeiro nível do arquivo não muda. ``` python .claude/tools/backlog.py check ``` imprime `check: OK — nenhuma violação.` e sai `0`.

**Pronto quando:** o literal de saída imprime `0`, os dois de entrada imprimem `1`, os três guardas imprimem os mesmos números de hoje, `backlog.py check` sai `0` e o sinal de fidelidade foi devolvido. A fidelidade do literal é conferida pelo revisor, por diff contra a §19 (`I-11`).

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-21
- **Depende de:** `DOM-T9a`
- **Fundamento:** `D-5`, `D-52`, `D-53`; invariantes `I-3`, `I-11`, `I-13`, `I-15`, `I-16`. O card transcreve a **§19** deste plano. Nasceu do `ESC-9`: com o gate vigente, a `DOM-T10` trava no primeiro despacho do modelador — gravada a seção, o `check` acusa `V2` em toda tarefa que ainda cita `Oração do modelo`, e essas linhas moram nos cards, que ele é **proibido** de tocar (`M-9`). Gate que só se fecha corrigindo o que não é seu é aceite inalcançável por construção, a mesma família do `AE-19`.
- **Oração do modelo:** `M-8`, `M-9` - M-8: Um agente único é dono de todas as operações do modelo: escreve o modelo de todo plano, emenda quando uma decisão muda o que o plano entrega, resolve conflito entre o texto e a entrega e explica o contexto a quem pergunta. - M-9: Nenhum outro papel escreve no modelo, e nenhum agente aciona outro agente: quem precisa de um ato de modelo devolve um dossiê fechado na própria linha de retorno, e quem conduz a sessão despacha o modelador.
- **Camada e fronteira:** agente do kit, em `.claude/agents/`. Nenhum código, nenhum teste.
- **Contratos/classes:** nenhum.
- **Passos:** 1. Substituir as linhas 22-24 pelo **bloco T1** da §19, verbatim (`I-3`). 2. Imprimir a região e devolver o **sinal** `fidelidade conferida: T1`. 3. Rodar as verificações abaixo.
- **Restrições desta tarefa:** - **Um bloco literal por ponto** (`I-13`): um ponto, um bloco. - Os outros três bullets de `## Fatos estáveis` **não mudam**, e nenhuma outra seção do arquivo é tocada: a `DOM-T9a` fechou seis pontos dele e eles **não se reabrem** (`I-3`). - Nenhum ato do modelador nasce, morre ou muda de dono: o gate muda de **leitura**, não de dono. - Nenhuma contingência deste card cria arquivo (`I-10`). Não commitar (`I-6`).
- **Não fazer:** - Não tocar `.claude/tools/modelo.py`: nenhuma violação muda de código, de literal ou de classe — a fronteira que o bloco usa (`violacoes_id` × `violacoes_op`) **já existe** no instrumento. - Não tocar `GOVERNANCA.md` §3.2: a norma não fala do gate, fala de quem escreve.
- **Contingências:** 1. Se a faixa 22-24 não casar com o conteúdo descrito → localizar por conteúdo, com o literal de saída da `Verificação`. Literal de saída com contagem maior que a declarada → `blocked` razão `premissa`. 2. Se um literal de aceite imprimir número diferente do declarado **e** o bloco estiver transcrito verbatim → **parar** e devolver `blocked` razão `premissa` com o comando, a contagem obtida e a linha do bloco de onde o literal sai (`I-16`, `AE-19`). Não ajustar o texto publicado, não relaxar o comando e não atribuir a falha a causa não medida.
- **Testes:** nenhum teste automatizado — a entrega é a definição de um agente.
- **Fora do escopo desta tarefa:** o modelo deste plano (`DOM-T10`), o instrumento, e tudo que muda papel (Marco 4).

## Execução

**Consumo:** 5 tool uses, 47.4 k tokens, 27.6 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: fidelidade conferida: T1
laudo: Antes do despacho da DOM-T10: o gate do modelador nao classifica as violacoes indexadas por "objeto" (V6, V7, V15, V17) - nem secao, nem card - e a DOM-T10 e a primeira autoria dele neste plano, o ato em que V15 e V17 sao as faltas mais provaveis; sem emenda a §19 e as linhas 22-29, o deadlock que o ESC-9 fechou pelo ramo <ID> reabre por um ramo que o texto nao nomeia.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

O defeito desta rodada era invisivel a todo o aceite do card: os sete literais medem FIDELIDADE DA TRANSCRICAO (o bloco chegou byte a byte) e o diff verbatim contra a §19 fecha em zero - nenhum deles mede a VERDADE do texto transcrito contra o codigo que ele descreve. O gap so apareceu ao exercitar o modulo ponta a ponta: rodar check sobre uma fixture invalida e censar as familias de indice que validar() de fato emite. Licao para os cards de transcricao literal que restam neste plano (DOM-T6, DOM-T10): quando o bloco literal DESCREVE um instrumento, o aceite por grep prova que o texto chegou, nunca que ele e verdadeiro - a conferencia contra o codigo e do revisor e tem de ser feita pelo caminho do usuario. Segunda observacao: a premissa errada nao nasceu no card, nasceu na medicao do consultor no ESC-9, e atravessou intacta D-52, D-53, §19 e o "Nao fazer" do card - quatro residencias repetindo a mesma frase sem que nenhuma a re-medisse.

## Fechamento

**Desdobramento:** aprovado
