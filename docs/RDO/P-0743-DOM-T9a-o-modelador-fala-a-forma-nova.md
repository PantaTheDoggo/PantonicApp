# RDO — P-0743 · DOM-T9a

**Plano:** `docs/plans/P-0743-modelo-de-dominio.md`
**Tarefa:** `DOM-T9a` — O modelador fala a forma nova
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `.claude/agents/pantonic-model-designer.md` devolvendo o que a forma nova define — versão em `### 1.4 Registro de versões`, bloco irmão `## 1A` na emenda, propriedades como ponto de partida do ensinamento — com os **quatro atos** e todas as responsabilidades intactos.

**Arquivos-alvo:** - `.claude/agents/pantonic-model-designer.md` - **seis** pontos, medidos em 2026-09-20 e re-derivados no despacho (`I-5`): o bullet da norma em `## Fatos estáveis`, 15-17 (bloco **S1**); o item 1 de `## O ensinamento`, 28-30 (bloco **S2**); o bullet **Autoria**, 42-44 (bloco **S3**); o bullet **Emenda**, 45-48 (bloco **S4**); os bullets **Conflito** e **Leitura**, 49-55 (bloco **S5**); e a seção `## A forma da devolução` inteira, 69-77 (bloco **S6**)

**Verificação:** **Censo do arquivo inteiro** (`D-50`): ``` grep -c 'MD-' .claude/agents/pantonic-model-designer.md ``` imprime `0` (hoje imprime `5`, medido 2026-09-20). ``` grep -c 'Mudanças do modelo' .claude/agents/pantonic-model-designer.md ``` imprime `0` (hoje imprime `2`, medido 2026-09-20). ``` grep -c 'três blocos' .claude/agents/pantonic-model-designer.md ``` imprime `0` (hoje imprime `1`, medido 2026-09-20). Literais que **entram**, cada um inteiro numa linha só do bloco: ``` grep -cF -e 'os quatro blocos que a compõem' .claude/agents/pantonic-model-designer.md ``` imprime `1` (hoje imprime `0`) — bloco S1. ``` grep -cF -e 'Comece pelas **propriedades**' .claude/agents/pantonic-model-designer.md ``` imprime `1` (hoje imprime `0`) — bloco S2. ``` grep -cF -e 'linha da **versão 1** em `### 1.4 Registro de versões`' .claude/agents/pantonic-model-designer.md ``` imprime `1` (hoje imprime `0`) — bloco S3. ``` grep -cF -e '**Versiona, não reescreve.**' .claude/agents/pantonic-model-designer.md ``` imprime `1` (hoje imprime `0`) — bloco S4. ``` grep -cF -e 'nenhuma linha de versão é gerada' .claude/agents/pantonic-model-designer.md ``` imprime `1` (hoje imprime `0`) — bloco S5. ``` grep -cF -e '## 1A. Modelo conceitual' .claude/agents/pantonic-model-designer.md ``` imprime `2` (hoje imprime `0`) — uma no bloco S4, uma no bloco S6. **Guardas — o que não pode mudar** (`D-48`, `AE-11`): ``` grep -cF -e '## Os quatro atos' .claude/agents/pantonic-model-designer.md ``` imprime `1` (hoje imprime `1`, **inalterado**). ``` grep -cF -e '- **Conflito** —' .claude/agents/pantonic-model-designer.md ``` imprime `1` (hoje imprime `1`, **inalterado**): o ato segue existindo e segue sendo dele. ``` grep -c '^## ' .claude/agents/pantonic-model-designer.md ``` imprime `6` (hoje imprime `6`, **inalterado**): nenhuma seção nasce e nenhuma morre. ``` sed -n '1,6p' .claude/agents/pantonic-model-designer.md ``` imprime o front matter com `name: pantonic-model-designer`, `model: opus` e a linha `tools:` **inalterados**. ``` python .claude/tools/backlog.py check ``` imprime `check: OK — nenhuma violação.` e sai `0`.

**Pronto quando:** os três censos imprimem `0`, os seis literais de entrada imprimem os números declarados, os quatro guardas imprimem os mesmos números de hoje, `backlog.py check` sai `0` e o sinal de fidelidade das seis regiões foi devolvido. **Nenhum item deste `Pronto quando` se apoia em frase escrita pelo executor sobre a própria entrega** (`I-11`, `D-50`): a fidelidade do literal é conferida pelo revisor, por diff contra a §18.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-21
- **Depende de:** `DOM-T9`
- **Fundamento:** `D-28`, `D-29`, `D-34`, `D-35`, `D-48`, `D-49`, `D-50`; invariantes `I-3`, `I-4`, `I-5`, `I-11`, `I-13`, `I-15`, `I-16`. O card transcreve a **§18** deste plano. É o segundo corretivo do `AE-17` (`ESC-6`): cinco pontos do agente exigem a linha `MD-<n>`, e um sexto manda começar pelos objetos, contra o parágrafo `**Objeto, operação e propriedade.**` que a `DOM-T7` publicou.
- **Oração do modelo:** `M-8`, `M-11` - M-8: Um agente único é dono de todas as operações do modelo: escreve o modelo de todo plano, emenda quando uma decisão muda o que o plano entrega, resolve conflito entre o texto e a entrega e explica o contexto a quem pergunta. - M-11: O ensinamento de como se escreve um modelo mora na definição do modelador, separado da norma que diz o que um modelo é e da gramática que a máquina lê.
- **Camada e fronteira:** agente do kit, em `.claude/agents/`. Nenhum código, nenhum teste.
- **Contratos/classes:** nenhum.
- **Passos:** 1. Substituir as linhas 15-17 pelo **bloco S1** da §18, verbatim (`I-3`). 2. Substituir as linhas 28-30 pelo **bloco S2**. 3. Substituir as linhas 42-44 pelo **bloco S3**. 4. Substituir as linhas 45-48 pelo **bloco S4**. 5. Substituir as linhas 49-55 pelo **bloco S5**. 6. Substituir as linhas 69-77 pelo **bloco S6**. 7. Imprimir as seis regiões e devolver o **sinal** `fidelidade conferida: S1, S2, S3, S4, S5, S6`. 8. Rodar as verificações abaixo.
- **Restrições desta tarefa:** - **Um bloco literal por ponto** (`I-13`): seis pontos, seis blocos. - **Nenhum ato nasce, morre ou muda de dono** (`D-48`). O heading `## Os quatro atos` e os quatro bullets permanecem, inclusive **Conflito** — a `D-47` o extingue no **Marco 4**, e publicar isso agora é o defeito `AE-11`, que este plano já pagou duas vezes. A `Verificação` publica os guardas que o afirmam. - O front matter (linhas 1-6) **não muda**: a `description` descreve papel, não forma, e a `DOM-T4` a fechou com aceite próprio. - A seção `## O que você nunca faz` e a seção `## A gramática do dossiê Ato de modelo` **não mudam**: a primeira é papel; a segunda é cópia da norma, cujos seis campos a §14 não tocou. - Não tocar `GOVERNANCA.md`, `pantonic-planner.md`, `.claude/tools/*` nem a skill `diario-de-obras`: cada um tem o seu card, e todos vêm antes deste. - Nenhuma contingência deste card cria arquivo (`I-10`). Não commitar (`I-6`).
- **Não fazer:** - Não acrescentar item novo ao `## O ensinamento`: são **quatro** itens antes e depois, e o estado inicial, o estado final e o versionamento moram na norma, que o próprio corpo manda ler e **não recopia** (`D-9`). - Não reescrever o bullet do instrumento nem o do gate `modelo.py check` exit `0`: a `DOM-T9` acabou de os tornar verdadeiros.
- **Contingências:** 1. Se alguma das seis faixas não casar com o conteúdo descrito → localizar por conteúdo, com os literais de saída da `Verificação`. Literal de saída com contagem maior que a declarada → `blocked` razão `premissa`. 2. Se um literal de aceite imprimir número diferente do declarado **e** o bloco estiver transcrito verbatim → **parar** e devolver `blocked` razão `premissa` com o comando, a contagem obtida e a linha do bloco de onde o literal sai (`I-16`, `AE-19`). Não ajustar o texto publicado, não relaxar o comando e não atribuir a falha a causa não medida.
- **Testes:** nenhum teste automatizado — a entrega é a definição de um agente. Quem a afere são os censos da `Verificação`.
- **Fora do escopo desta tarefa:** o modelo deste plano (`DOM-T10`), a `V2`, e tudo que muda papel — inclusive a extinção do ato `conflito` que a `D-47` já decidiu (Marco 4, trancado pela régua da `D-43`).

## Execução

**Consumo:** 12 tool uses, 57.8 k tokens, 60.9 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: fidelidade conferida: S1, S2, S3, S4, S5, S6
laudo: P-0743: antes de despachar a DOM-T10, fechar quem escreve a secao no arquivo - o modelador so devolve com modelo.py check --plano exit 0, o que exige que ele mesmo ja tenha gravado a ## 1. Modelo conceitual no plano, e o passo 2 da DOM-T10 manda o executor transcrever a secao recebida no mesmo lugar: duas maos sobre a mesma regiao, sem regra de precedencia no card.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

O discriminante foi o diff linha a linha dos seis blocos da §18 (plano 3665-3667, 3676-3681, 3688-3690, 3699-3705, 3714-3720, 3728-3738) contra a arvore (agente 15-17, 28-33, 45-47, 48-54, 55-61, 75-85): seis regioes, zero divergencia de byte. Os tres censos saem 0 e os quatro guardas saem 1, 1, 6 e front matter intacto - nenhum ato nasce, morre ou muda de dono. A coerencia ponta a ponta fecha: o S2 do agente agora diz o mesmo que GOVERNANCA.md 347-353, o "quatro blocos" do S1 casa com o "Sao quatro blocos" da norma em 326, e as formas que o S4 e o S6 prometem sao literalmente as que o instrumento le - "## 1A. Modelo conceitual - versao pendente de validacao" e "### 1.4 Registro de versoes" batem com _HEADING_PENDENTE e com a extracao da tabela em modelo.py, e "situacao: pendente" casa com _SITUACAO_RE. O censo de MD- no kit inteiro (.claude, GOVERNANCA.md, README.md, RUBRICA) sai 0: o AE-17 fecha aqui, no segundo corretivo, e nenhuma residencia viva do kit manda mais o modelador devolver o token extinto.

## Fechamento

**Desdobramento:** aprovado
