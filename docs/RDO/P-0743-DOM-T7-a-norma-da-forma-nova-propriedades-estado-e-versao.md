# RDO — P-0743 · DOM-T7

**Plano:** `docs/plans/P-0743-modelo-de-dominio.md`
**Tarefa:** `DOM-T7` — A norma da forma nova: propriedades, estado e versão
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `GOVERNANCA.md` `### 3.2` descrevendo o modelo como objetos **com propriedades**, com o teste decidível de objeto e operação, o estado inicial e final como aceite do plano, o versionamento vigente/pendente/obsoleta e a distinção entre medição e drift.

**Arquivos-alvo:** - `GOVERNANCA.md` - **três** pontos da `### 3.2`, medidos em 2026-09-20 e re-derivados no despacho (`I-5`): o parágrafo `**O que é.**`, linhas 323-331 (bloco **P1**); a inserção imediatamente antes do parágrafo `**O contrato chega ao card.**`, linha 346 (bloco **P2**); o parágrafo `**Retroatividade.**`, linhas 370-373 (bloco **P3**)

**Verificação:** Os literais que **saem**, cada um inteiro numa linha só do destino (`AE-1`, `AE-13`): ``` grep -cF -e 'São três blocos, nesta ordem' GOVERNANCA.md ``` imprime `0` (hoje imprime `1`, na linha 325, medido 2026-09-20). ``` grep -cF -e '### 1.3 Mudanças do modelo' GOVERNANCA.md ``` imprime `0` (hoje imprime `1`, medido 2026-09-20). Os literais que **entram**, cada um inteiro numa linha só do bloco: ``` grep -cF -e 'objetos com propriedades' GOVERNANCA.md ``` imprime `1` (hoje imprime `0`) — bloco P1. ``` grep -cF -e 'Objeto é o que possui' GOVERNANCA.md ``` imprime `1` (hoje imprime `0`) — bloco P2, primeiro parágrafo. ``` grep -cF -e 'O aceite do plano é a confrontação dos dois' GOVERNANCA.md ``` imprime `1` (hoje imprime `0`) — bloco P2, segundo parágrafo. ``` grep -cF -e 'Medição e drift não são a mesma coisa' GOVERNANCA.md ``` imprime `1` (hoje imprime `0`) — bloco P2, quarto parágrafo. ``` grep -cF -e 'plano sem estado inicial e final' GOVERNANCA.md ``` imprime `0` (hoje imprime `0`, **inalterado**): o literal de exit é do instrumento (`DOM-T9`) e **não** entra na norma. A cadeia interna da `### 3.2` (`I-14`): nenhuma linha dela pode afirmar que o modelador resolve conflito e, ao mesmo tempo, que não resolve. ``` grep -cF -e 'resolução de conflito entre o texto e a entrega' GOVERNANCA.md ``` imprime `1` (hoje imprime `1`, **inalterado**): a mudança de papéis é Marco 4. ``` pwsh -NoProfile -File .claude/checks/check-readme.ps1 ``` sai `0` — o guarda confere as linhas `Fonte da verdade` das seções, e este card não mexe em nenhuma (hoje sai `0`, medido 2026-09-20).

**Pronto quando:** os dois literais de saída imprimem `0`, os quatro de entrada imprimem `1`, o literal de papéis segue **inalterado** em `1`, `check-readme.ps1` sai `0`, e nenhuma linha da `### 3.2` descreve o modelo como tendo lista de mudanças. Nenhum item se apoia em frase escrita pelo executor sobre a própria entrega (`I-11`, `D-22`).

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20
- **Depende de:** `DOM-T5b`
- **Nota de fila:** dependência corrigida de `DOM-T6` para `DOM-T5b` pela orquestração em 2026-09-20; a `DOM-T6` pertence ao Marco 5 e nada do terceiro estágio depende dela (§13.5). Ver `AE-16`
- **Fundamento:** `D-24`, `D-25`, `D-26`, `D-28`, `D-29`, `D-33`, `D-34`, `D-35`, `D-36`, `D-37`, `D-38`, `D-39`, `D-44`; invariantes `I-3`, `I-10`, `I-11`, `I-13`. O card transcreve a **§14** deste plano, residência única do texto. **O que muda nos papéis não está aqui** (`D-40`, `D-41`): é Marco 4, e depende da `Q-11`, aberta.
- **Oração do modelo:** `M-1` — a forma vigente do campo enquanto o modelo deste plano estiver na forma anterior; é a `DOM-T10` que converte o campo de todos os cards (`D-31`). - M-1: O modelo de um plano passa a descrever o que o plano entrega como objetos e operações encadeadas: cada objeto com o contrato que a implementação precisa, e cada operação nomeando quem age, o que faz e de que objetos precisa.
- **Camada e fronteira:** doutrina publicada, na raiz. Nenhum código, nenhum teste.
- **Contratos/classes:** nenhum.
- **Passos:** 1. Substituir as linhas 323-331 pelo **bloco P1** da §14, verbatim (`I-3`). 2. Inserir o **bloco P2** da §14 imediatamente antes da linha do parágrafo `**O contrato chega ao card.**`, separado dele por uma linha em branco. 3. Substituir as linhas 370-373 pelo **bloco P3** da §14, verbatim. 4. Imprimir as três regiões entregues e devolver, na linha de retorno, o **sinal** `fidelidade conferida: P1, P2, P3` — sinal, não prova (`I-11`). 5. Rodar as verificações abaixo.
- **Restrições desta tarefa:** - **Um bloco literal por ponto** (`I-13`): três pontos, três blocos. Nenhum passo manda redigir. Ponto que precise mudar e não tenha bloco → `blocked` razão `premissa`, nunca redação. - **Não tocar a tabela de papéis nem o parágrafo `Nenhum agente aciona outro agente`**: o ato `conflito` do modelador e a autoridade do consultor são Marco 4 e dependem da `Q-11`. Publicar metade da mudança de papéis é o defeito `AE-11`, que este plano já pagou duas vezes. - Não tocar `docs/RUBRICA_DE_REVISAO.md`, `.claude/tools/*`, `.claude/agents/*` nem `.claude/skills/*`. - Nenhuma contingência deste card cria arquivo (`I-10`). - Não commitar (`I-6`).
- **Não fazer:** - Não alterar os parágrafos `**Para quem é.**`, `**Estágio, não status.**`, `**O contrato chega ao card.**` e `**Quem escreve.**`: os quatro seguem verdadeiros. - Não renumerar nada da `### 3.2` nem de `## 3`.
- **Contingências:** 1. Se alguma das três faixas não casar com o conteúdo descrito → localizar por conteúdo, com os literais de saída da `Verificação`. Se um literal de saída imprimir mais de `1` → parar e sinalizar `blocked` razão `premissa`, com as linhas encontradas.
- **Testes:** nenhum teste automatizado — a entrega é doutrina publicada.
- **Fora do escopo desta tarefa:** a gramática (`DOM-T8`), o instrumento (`DOM-T9`), o modelo deste plano (`DOM-T10`), e tudo que muda papel (Marco 4).

## Execução

**Consumo:** 10 tool uses, 55.6 k tokens, 50.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: fidelidade conferida: P1, P2, P3
laudo: P-0743: nenhum card possui as duas linhas que exigem MD-<n> (GOVERNANCA.md 388 e o item (f) do modelador), e a DOM-T8 remove a residencia do token - definir o dono antes de despachar a DOM-T8, sem esperar a Q-11.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

A fidelidade verbatim deste card foi conferida por medida, nao pelo sinal do executor (I-11): diff dos blocos P1, P2 e P3 recortados da secao 14 do plano contra as regioes entregues de GOVERNANCA.md - tres blocos identicos, zero diferencas. E barato e deveria ser o padrao em todo card de transcricao, no lugar da leitura comparativa a olho. Segunda observacao, sobre a forma do card: esta tarefa publica a norma antes da gramatica (DOM-T8) e do instrumento (DOM-T9), entao a arvore fica, de proposito, num estado em que a 3.2 enumera quatro blocos (1.1 a 1.4) e o modelo.py ainda exige "### 1.3 Mudancas do modelo". O estado transitorio e declarado e coberto pelo bloco P3 (Retroatividade, exit 2), mas e ele que produz os dois achados acima: a janela entre norma e gramatica e onde token orfao nasce, e o plano precisa de dono explicito para os tokens que ela abandona.

## Fechamento

**Desdobramento:** aprovado
