# RDO — P-0743 · DOM-T8

**Plano:** `docs/plans/P-0743-modelo-de-dominio.md`
**Tarefa:** `DOM-T8` — A gramática da forma nova
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** a subseção `### Modelo de domínio (seção do plano)` da skill `diario-de-obras` lendo a forma nova: propriedades na tabela de objetos, `altera:` na operação, estado inicial e final no lugar da lista de mudanças, registro de versões e o bloco irmão `## 1A`.

**Arquivos-alvo:** - `.claude/skills/diario-de-obras/SKILL.md` - **cinco** pontos, medidos em 2026-09-20 e re-derivados no despacho (`I-5`): a linha `| cabeçalho |`, 182 (bloco **G1**); a linha `| objetos |`, 183 (bloco **G2**); a linha `| operações |`, 184 (bloco **G3**); a linha `| mudanças |`, 185, que vira **duas** linhas (bloco **G4**); e a inserção imediatamente antes do parágrafo `**Andamento, nunca gravado.**`, 188 (bloco **G5**)

**Verificação:** Literais que **saem**, cada um inteiro numa linha só: ``` grep -cF -e '| mudanças | `### 1.3 Mudanças do modelo`' .claude/skills/diario-de-obras/SKILL.md ``` imprime `0` (hoje imprime `1`, na linha 185, medido 2026-09-20). Literais que **entram**, cada um inteiro numa linha só do bloco: ``` grep -cF -e '| estado | `### 1.3 Estado inicial e estado final`' .claude/skills/diario-de-obras/SKILL.md ``` imprime `1` (hoje imprime `0`) — primeira linha do bloco G4. ``` grep -cF -e '| versões | `### 1.4 Registro de versões`' .claude/skills/diario-de-obras/SKILL.md ``` imprime `1` (hoje imprime `0`) — segunda linha do bloco G4. ``` grep -cF -e 'propriedades \| contrato \| origem' .claude/skills/diario-de-obras/SKILL.md ``` imprime `1` (hoje imprime `0`) — bloco G2, a coluna nova da tabela de objetos. ``` grep -cF -e '## 1A. Modelo conceitual' .claude/skills/diario-de-obras/SKILL.md ``` imprime `1` (hoje imprime `0`) — bloco G5. ``` grep -cF -e '<p> propriedades · situação:' .claude/skills/diario-de-obras/SKILL.md ``` imprime `1` (hoje imprime `0`) — bloco G1. ``` grep -cF -e '| campo do card |' .claude/skills/diario-de-obras/SKILL.md ``` imprime `1` (hoje imprime `1`, **inalterado**): a `V2` não é tocada. **Censo da subseção** (`D-50`), que é o que dá poder discriminante à cláusula do `Pronto quando` — o grep do heading sozinho não alcança a linha do cabeçalho: ``` grep -c 'MD-' .claude/skills/diario-de-obras/SKILL.md ``` imprime `0` (hoje imprime `2`, nas linhas 182 e 185, medido 2026-09-20). ``` python .claude/tools/backlog.py check ``` imprime `check: OK — nenhuma violação.` e sai `0`.

**Pronto quando:** o literal de saída imprime `0`, os cinco de entrada imprimem `1`, a linha do campo do card segue **inalterada**, `backlog.py check` sai `0`, e **o censo do token imprime `0`** — é ele, e não juízo do executor, que afirma que nenhuma linha da subseção descreve o modelo como tendo lista de mudanças (`D-50`, `I-11`).

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20
- **Depende de:** `DOM-T7`
- **Fundamento:** `D-24`, `D-25`, `D-28`, `D-29`, `D-33`, `D-34`, `D-35`, `D-37`; invariantes `I-3`, `I-10`, `I-11`, `I-13`. O card transcreve a **§15** deste plano. Depende da `DOM-T7` porque a gramática é a forma da norma: publicá-la antes abriria a janela em que as duas divergem, defeito medido na `MC-T1` e repetido no `AE-4`.
- **Oração do modelo:** `M-1` - M-1: O modelo de um plano passa a descrever o que o plano entrega como objetos e operações encadeadas: cada objeto com o contrato que a implementação precisa, e cada operação nomeando quem age, o que faz e de que objetos precisa.
- **Camada e fronteira:** skill do kit, em `.claude/skills/`. Nenhum código, nenhum teste.
- **Contratos/classes:** nenhum.
- **Passos:** 1. Substituir a linha 182 pelo **bloco G1** da §15, verbatim (`I-3`). 2. Substituir a linha 183 pelo **bloco G2**. 3. Substituir a linha 184 pelo **bloco G3**. 4. Substituir a linha 185 pelas **duas** linhas do **bloco G4**. 5. Inserir o **bloco G5** imediatamente antes do parágrafo `**Andamento, nunca gravado.**`, separado dele por uma linha em branco. 6. Imprimir as cinco regiões e devolver o **sinal** `fidelidade conferida: G1, G2, G3, G4, G5`. 7. Rodar as verificações abaixo.
- **Restrições desta tarefa:** - **Um bloco literal por ponto** (`I-13`): cinco pontos, cinco blocos. - A linha `| campo do card |` (186) **não muda**: a `V2` fica como está, e a `D-46` fechou a `Q-12` **mantendo-a intacta** — não é questão aberta que a protege, é decisão (`D-49`). - O preâmbulo da seção `## Gramática legível por máquina` **não muda**: ele já aponta para a §5 deste plano, e a §15 é continuação dela, não substituição — a `DOM-T3a` fechou aquele ponto. - Não tocar `.claude/tools/*`: o instrumento aprende a gramática na `DOM-T9`, e **nesta ordem** (`AE-5`, `AE-6`: gramática nova não se aplica antes de o parser aprender — aqui a ordem é a inversa e proposital, porque a gramática é a residência que o instrumento lê). - Nenhuma contingência deste card cria arquivo (`I-10`). Não commitar (`I-6`).
- **Não fazer:** - Não alterar o parágrafo `**Andamento, nunca gravado.**`: ele segue verdadeiro, e o estado de que a §15 fala é o das **propriedades**, não o andamento das operações. - Não alterar a subseção `### Item e residência` nem nenhuma outra seção da skill.
- **Contingências:** 1. Se alguma das cinco faixas não casar com o conteúdo descrito → localizar por conteúdo, com os literais de saída da `Verificação`. Literal de saída com mais de `1` → `blocked` razão `premissa`.
- **Testes:** nenhum teste automatizado — a entrega é gramática publicada. Quem a afere é a `DOM-T9`, que a implementa e traz os testes.
- **Fora do escopo desta tarefa:** o instrumento (`DOM-T9`), o modelo deste plano (`DOM-T10`), a `V2` e a `Q-12`, e tudo que muda papel (Marco 4).

## Execução

**Consumo:** 14 tool uses, 56.8 k tokens, 73.7 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: fidelidade conferida: G1, G2, G3, G4, G5
laudo: P-0743: o preambulo da skill diario-de-obras aponta para a §5 do plano como residencia do texto da subsecao Modelo de dominio, mas a subsecao passou a transcrever a §15 - §5 e §15 divergem na arvore e nenhum card reconcilia as duas nem corrige o ponteiro; fora do alcance da D-48/AE-17, precisa de card corretivo ou de emenda que declare qual das duas secoes governa.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

A fidelidade verbatim foi conferida por diff dos cinco blocos recortados da §15 (linhas 3357, 3364, 3371, 3378-3379, 3386-3392) contra as regioes entregues (SKILL.md 182, 183, 184, 185-186, 189-195): cinco diffs vazios e byte-count identico (263/474/821/714/636). A licao da DOM-T7 se confirma como metodo - leitura comparativa nao discrimina linha de tabela de 821 bytes com escape de pipe e crase, e o diff discrimina em um ato. O censo "grep -c MD-" foi o unico item do Pronto quando com poder discriminante real sobre a clausula de escopo de subsecao (D-50): os greps de literal nao alcancavam a linha do cabecalho, onde o token vivia. Ponto barato para o proximo card da mesma familia: a linha congelada da V2 (campo do card) foi conferida por diff contra a propria residencia (§5 linha 394), nao por contagem - a contagem prova que ela existe, o diff prova que ela nao mudou.

## Fechamento

**Desdobramento:** aprovado
