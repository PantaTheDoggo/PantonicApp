# Rubrica de revisão de tarefa

> Fonte da verdade: este documento é a régua canônica da revisão de uma tarefa executada. Os
> guardrails que ele mede moram em `GOVERNANCA.md` §7; a bateria de comandos que produz a evidência
> mecânica mora em `GOVERNANCA.md` §3.

A revisão de uma tarefa produz três valores: um **veredito**, uma **dimensão bloqueante** e um
**percentual**. O reviewer marca sete dimensões discretas; os três valores saem de uma função sobre
essas marcações.

## 1. Domínio de saída

| campo | valores |
|---|---|
| `veredito` | `aprovado` \| `ressalva` \| `reprovado` |
| `bloqueante` | nome de uma dimensão \| `nenhuma` |
| `percentual` | inteiro de 0 a 100 |

Este domínio é fechado. A rubrica produz valores dele e não o amplia.

O percentual é **calculado, nunca autorado**. O gerador do laudo recusa percentual e veredito
passados como argumento: o que ele aceita é a marcação das dimensões.

## 2. Os quatro níveis

| nível | significado | valor no cálculo |
|---|---|---|
| `conforme` | a dimensão está satisfeita como escrita | 1 |
| `parcial` | satisfeita em parte, com o resto identificado e roteado | 0,5 |
| `não conforme` | violada | 0 |
| `não se aplica` | a dimensão não tem objeto nesta tarefa | fora do cálculo |

`não se aplica` remove a dimensão do numerador **e** do denominador. Cada dimensão declara se admite
esse nível; quatro delas nunca admitem, o que mantém o denominador sempre maior que zero.

## 3. Autoridade da evidência

Cada dimensão declara a fonte da sua evidência: **mecânica** (comando com exit code) ou **de juízo**
(leitura do reviewer contra o dossiê da tarefa).

A camada mecânica é autoridade sobre o que ela mede. Onde o comando deu vermelho, a dimensão
correspondente não pode ser marcada `conforme` — a marcação é recusada com erro pelo gerador do
laudo, e nenhuma justificativa em prosa a libera. O juízo do reviewer opera apenas nas dimensões
cuja fonte é de juízo, e nas faixas que a evidência mecânica deixa em aberto.

Dimensão de fonte mista tem a parte mecânica travada e a parte de juízo livre.

A seção `## Arquivos tocados` do dossiê de evidência (`.claude/tools/review_evidence.py`) carrega
essa mesma autoridade por arquivo: cada arquivo tocado sai marcado `da entrega` (coberto pelos
`Arquivos-alvo` da tarefa) ou `alheio` (fora deles), com o estado `git` que comprova a marcação —
atribuição derivada da mesma `confrontar_escopo` que resolve a dimensão `escopo` abaixo, nunca uma
segunda classificação. O reviewer lê a atribuição já calculada; não a julga de memória nem depende
de injeção manual de contexto do orquestrador (`AE-13`).

**Nota (2026-09-19):** a atribuição do dossiê é **por arquivo** e segue dispensando injeção manual
para a pergunta de **escopo**; enquanto o commit for por marco (diretiva de execução do dono,
2026-09-18, item 3), o recorte `--desde <commit>` acumula as entregas do marco e um mesmo
arquivo-alvo carrega autoria de várias tarefas — neste regime a injeção manual de contexto **é
obrigatória** e faz parte do despacho do reviewer, não é desvio de quem orquestra; o que suspende
essa obrigação é **capacidade**, não card: atribuição por **hunk**.

## 4. As sete dimensões

### `criterio-de-pronto`

- **Pergunta:** a entrega satisfaz o campo "Pronto quando" do dossiê da tarefa?
- **Fonte da evidência:** juízo, sobre o dossiê de evidência e o diff dos arquivos-alvo confrontados
  com o dossiê da tarefa. Sem trava mecânica.
- **Bloqueante:** sim.
- **`conforme`:** cada item do critério de pronto tem contrapartida localizável na entrega.
- **`parcial`:** parte dos itens entregue e o restante identificado; ou o critério de pronto é
  inverificável como escrito, caso em que a marcação vem acompanhada de achado de processo com alvo
  `dossiê` (§6).
- **`não conforme`:** o item central do critério não tem contrapartida na entrega.
- **`não se aplica`:** inadmissível.

### `escopo`

- **Pergunta:** os arquivos tocados formam um subconjunto dos arquivos-alvo declarados?
- **Fonte da evidência:** mecânica — a lista de arquivos tocados do dossiê de evidência confrontada
  com o campo "Arquivos-alvo" e com a lista de fora de escopo.
- **Bloqueante:** sim.
- **`conforme`:** conjunto tocado contido no conjunto declarado, ou nele mais os artefatos cuja
  atualização a doutrina torna obrigatória como consequência mecânica de uma mudança nos alvos —
  entrada de índice para doc que cruzou o limiar de tamanho, inventário gerado, registro de
  encerramento da tarefa.
- **`parcial`:** outro arquivo fora dos alvos tocado, declarado nos desvios do dossiê de evidência e
  limitado a artefato de registro.
- **`não conforme`:** arquivo fora dos alvos tocado sem declaração, ou arquivo nomeado na lista de
  fora de escopo tocado por qualquer motivo.
- **`não se aplica`:** dossiê sem campo de arquivos-alvo, com achado de processo de alvo `dossiê`.

### `testes`

- **Pergunta:** os testes que o dossiê exige existem e passam?
- **Fonte da evidência:** mecânica — presença dos arquivos de teste declarados e exit code da suíte
  da área tocada.
- **Bloqueante:** sim.
- **`conforme`:** o teste funcional e o teste de regressão exigidos existem e a suíte fecha em
  exit 0.
- **`parcial`:** os testes presentes passam, com cobertura menor que a declarada — teste funcional
  sem o de regressão que tranca o comportamento, por exemplo.
- **`não conforme`:** teste exigido ausente, suíte em exit não-zero, ou teste cujo significado mudou
  removido em vez de reescrito.
- **`não se aplica`:** dossiê de classe de redação, sem exigência de teste de código. A suíte
  continua medida pela dimensão `guardas`.

### `guardas`

- **Pergunta:** conformance, guardas estruturais e piso de regressão seguem verdes?
- **Fonte da evidência:** mecânica — exit code colado de cada comando da bateria de `GOVERNANCA.md`
  §3, mais a comparação do piso de regressão. Autoridade integral: esta dimensão não tem faixa de
  juízo.
- **Bloqueante:** sim.
- **`conforme`:** todos os comandos em exit 0 e piso mantido ou elevado.
- **`parcial`:** um comando em vermelho por causa anterior à tarefa, com a mesma falha demonstrada
  no estado prévio ao diff.
- **`não conforme`:** qualquer comando em vermelho por efeito da tarefa, ou piso de regressão
  rebaixado.
- **`não se aplica`:** inadmissível.

### `rota`

- **Pergunta:** a execução seguiu a rota aprovada no plano (`G-PLANFIDELITY`)?
- **Fonte da evidência:** juízo, sobre os desvios do dossiê de evidência e o diff, tendo o dossiê da
  tarefa como referência.
- **Bloqueante:** sim.
- **`conforme`:** nenhum desvio de rota; desvio de detalhe declarado e reversível.
- **`parcial`:** desvio de rota declarado no campo de desvios, contido em um arquivo-alvo e sem
  decision record que o autorize.
- **`não conforme`:** arquitetura aprovada substituída por alternativa própria da execução; ou
  obstáculo à rota resolvido por decisão da execução em vez de escalada.
- **`não se aplica`:** inadmissível.

### `residuo`

- **Pergunta:** a entrega deixou símbolo, módulo ou arquivo sem consumidor de produção
  (`G-DEADCODE`)?
- **Fonte da evidência:** mista — o detector de código morto sobre o que ele alcança, e juízo sobre
  os símbolos novos declarados no dossiê de evidência.
- **Bloqueante:** não.
- **`conforme`:** cada símbolo novo tem chamador de produção declarado, e nenhum artefato de rota
  abandonada sobreviveu ao commit.
- **`parcial`:** símbolo novo sem chamador de produção, com tíquete de consumo registrado.
- **`não conforme`:** artefato de rota abandonada sobrevivendo ao commit, ou símbolo novo sem
  chamador e sem rota.
- **`não se aplica`:** entrega sem artefato executável.

### `registro`

- **Pergunta:** o registro da tarefa é auditável por quem não a executou?
- **Fonte da evidência:** mista — presença e teto dos campos obrigatórios do dossiê de evidência
  verificados mecanicamente; juízo sobre a rota de cada achado.
- **Bloqueante:** não.
- **`conforme`:** todos os campos obrigatórios presentes dentro do teto; cada achado fora de escopo
  com rota nomeada (tíquete ou `sem ação`); verificação com exit code colado; consumo registrado por
  ponteiro para a série de telemetria.
- **`parcial`:** campos presentes, com um achado sem rota ou com verificação parafraseada em vez de
  exit code colado.
- **`não conforme`:** campo obrigatório ausente; achado citado em prosa e em lugar nenhum mais;
  número de consumo autorado pela própria execução.
- **`não se aplica`:** inadmissível.

O que esta dimensão mede no consumo é a **existência e a procedência** do registro, nunca a sua
**grandeza**. O número medido não pontua dimensão nenhuma, não reprova entrega, não abre
desdobramento e não é fundamento de achado: custo e consumo são informativos e só rendem insight no
agregado da série medida. O registro **qualitativo** daquela tarefa — o que o número sozinho não diz
— mora no card **"Lições aprendidas na tarefa"** do laudo, preenchido a critério do reviewer quando
houver o que observar; sem observação, o número isolado se desconsidera. O `teto` citado acima é o
limite de tamanho dos campos do dossiê de evidência, e nada tem com consumo.

## 5. Cálculo

### Pesos

Ordem canônica das dimensões, usada também para escolher a bloqueante quando há mais de uma
vermelha:

| # | dimensão | peso | bloqueante | admite `não se aplica` |
|---|---|---|---|---|
| 1 | `criterio-de-pronto` | 3 | sim | não |
| 2 | `escopo` | 2 | sim | sim |
| 3 | `testes` | 3 | sim | sim |
| 4 | `guardas` | 3 | sim | não |
| 5 | `rota` | 2 | sim | não |
| 6 | `residuo` | 2 | não | sim |
| 7 | `registro` | 2 | não | não |

Peso total com as sete aplicáveis: **17**. Denominador mínimo, com as três dimensões dispensáveis
fora: **10**.

### Fórmula

```
aplicáveis     = dimensões cujo nível difere de "não se aplica"
valor(conforme) = 1 ;  valor(parcial) = 0,5 ;  valor(não conforme) = 0

percentual = arredonda( 100 × Σ(peso(d) × valor(d)) / Σ(peso(d)) ),  d ∈ aplicáveis
```

Arredondamento de metade para cima, resultado inteiro.

### Dominância e veredito

```
vermelhas = [ d ∈ aplicáveis : bloqueante(d) e nível(d) = "não conforme" ], em ordem canônica

se vermelhas ≠ ∅:
    bloqueante = nome(vermelhas[0])
    veredito   = reprovado
senão:
    bloqueante = nenhuma
    veredito   = aprovado   se percentual ≥ 95
                 ressalva   se 70 ≤ percentual < 95
                 reprovado  se percentual < 70
```

A dominância vale qualquer que seja o percentual: vermelho em dimensão bloqueante reprova a 96% do
mesmo jeito que a 40%. A combinação `aprovado` com `bloqueante` preenchida é inalcançável por
construção.

O caminho inverso é aberto: uma tarefa pode ser `reprovado` com `bloqueante = nenhuma`, quando o
acúmulo de `parcial` e de vermelho não bloqueante derruba o percentual abaixo de 70.

### Propriedades que caem dos pesos

- `aprovado` equivale a todas as dimensões aplicáveis em `conforme`: o menor peso é 2 e o maior
  denominador é 17, logo um único `parcial` custa ao menos 5,9 pontos e leva o percentual a 94 ou
  menos.
- Um único `não conforme` não bloqueante deixa o percentual entre 70 e 94, isto é, `ressalva`.
- Quatro dimensões pesadas em `parcial` derrubam o percentual abaixo de 70 sem nenhuma vermelha:
  entrega difusa reprova sem depender de dominância.

### Exemplo

Tarefa de implementação com as sete dimensões aplicáveis: `criterio-de-pronto` conforme,
`escopo` conforme, `testes` parcial, `guardas` conforme, `rota` conforme, `residuo` parcial,
`registro` conforme.

Numerador: 3 + 2 + 1,5 + 3 + 2 + 1 + 2 = 14,5. Denominador: 17. Percentual: 85. Nenhuma vermelha
bloqueante, logo `bloqueante = nenhuma` e `veredito = ressalva`.

Mesma tarefa com `guardas` em `não conforme`: numerador 11,5, percentual 68, e a dominância fixa
`bloqueante = guardas`, `veredito = reprovado`.

## 6. Achado de processo

Parte do que uma revisão encontra acusa o **dossiê**. Tarefa mal decomposta,
critério de pronto inverificável, dossiê que empurra a execução contra a arquitetura, verificação
exigida que não discrimina nada: corrigir o sintoma na entrega deixa a causa de pé, e a tarefa
seguinte reincide.

O laudo carrega um campo próprio para esse achado, com quatro alvos possíveis:

| alvo | o que o achado denuncia |
|---|---|
| `dossiê` | decomposição errada, critério de pronto inverificável, arquivos-alvo incompletos, verificação sem poder discriminante |
| `doutrina` | guardrail ausente, ambíguo ou em conflito com outro |
| `rubrica` | dimensão mal formulada, nível sem fronteira clara, peso desalinhado com o dano real |
| `modelo` | operação do modelo de domínio do plano que a entrega tornou falsa ou ambígua (`GOVERNANCA.md` §3.2); rota: dossiê `Ato de modelo` de conflito, devolvido junto com o laudo e despachado ao `pantonic-model-designer` por quem conduz a sessão — nunca corrigido pelo reviewer |

Três invariantes governam a via:

1. **Achado de processo nunca rebaixa dimensão de entrega.** Uma execução que entregou fielmente o
   que um dossiê defeituoso pediu recebe as dimensões que merece pela entrega, com o achado anexado
   à parte. Punir a execução pelo defeito do dossiê ensina o loop a esconder o defeito.
2. **Achado de processo exige rota.** Ele fecha como tíquete indexado, como item de replanejamento
   do plano vigente, ou como emenda a este documento. Achado registrado apenas em prosa é registro
   incompleto, e cai na dimensão `registro`.
3. **Defeito do dossiê que impede a verificação marca `parcial`, nunca `conforme`.** Critério de
   pronto inverificável leva `criterio-de-pronto` a `parcial` e produz achado de alvo `dossiê`. O
   reviewer não completa o critério por conta própria.

Achado cujo alvo é `dossiê` e que **invalida a rota** do plano é decisão de arquitetura ou de
requisito: sobe ao dono pelo `--escalar` do laudo, e a revisão o registra sem resolvê-lo.
A decisão de mudar rota é do dono.

## 7. Fronteira do papel

O reviewer marca dimensões, anexa achados e emite o laudo pelo gerador. O reviewer não corrige o que
aponta, não replaneja, não edita os arquivos da tarefa e não escreve percentual nem veredito. A
correção do que o laudo aponta pertence a uma execução seguinte, com o laudo em mãos. **O reviewer não escreve fora do caminho do laudo**, e isso inclui o modelo de domínio do plano
(`GOVERNANCA.md` §3.2): divergência entre a entrega e o texto de uma operação vira achado de
processo de alvo `modelo`, e o texto fica como está até o modelador agir.

## 8. Rubrica de criação de tarefa

> Fonte da verdade: régua de **autoria** do card, aplicada **antes** do despacho — a §1..§7 julga a entrega, esta julga o dossiê que a pediu. Armadilhas de ferramenta medidas: `docs/ARMADILHAS_DE_FERRAMENTA.md` — consultar antes de escrever linha de Verificação.
> Medida que a originou (`P-0740`, `ESC-9`..`ESC-14`): oito defeitos de autoria numa janela, três cards seguidos parados por linha de aceite
> quebrada, e 867k tk em cinco passagens de consultor contra quatro tarefas fechadas.

| # | o card passa quando | caso medido |
|---|---|---|
| (i) | não exige do executor **avaliar**, **decidir** ou **tratar ambiguidade** | `AE-1` |
| (ii) | é um tema só, fechado, sem matéria transversal, e despachável **inteiro** num ato (`DM-2`/`DM-4`) | — |
| (iii) | o cabeçalho segue a gramática que os **parsers** aceitam **na data do card**, nunca a que só a doutrina conhece | `AE-5` |
| (iv) | declara o aceite de coerência do módulo (`DM-3`) | — |
| (v) | os números de aceite são re-deriváveis por comando, não copiados | `AE-21` |
| (vi) | todo entregável que cria, versiona ou apaga arquivo foi confrontado com o `.gitignore` e com o filtro do instrumento que o julga, e a `Verificação` discrimina o mundo com a mudança do mundo sem ela | `AE-2` |
| (vii) | toda linha de `Verificação` publica saída **observada**: comando com os argumentos exatos, pergunta binária pela flag binária e pelo exit code, e nenhum aceite exigindo verde que a tarefa não pode produzir | `AE-4` |
| (viii) | card que mexe em item de lista ou de tabela enumerada fecha, no mesmo ato, a frase da **mesma seção** que a conta, e estende o instrumento que julga a seção | `AE-12` |
| (ix) | exigência **estrutural** não é prometida como teste comportamental: ou vem com o caso em que a implementação certa e a reimplementação plausível divergem, ou vira inspeção mecânica, ou é `Restrição` sem teste | `AE-16` |
| (x) | nenhum total de suíte entra como constante de aceite: o piso é relação (*não reduz o total re-medido no despacho, e soma os `<N>` testes novos*), e o literal é referência **datada** | `AE-18` |
| (xi) | linha por efeito em arquivo publica **os dois** valores rodados; padrão que devolve o mesmo valor nos dois mundos é inválido por construção; literal com crase, asterisco ou barra invertida vai em **bloco cercado**, e padrão textual leva `-SimpleMatch` | `AE-19` |
| (xii) | o comando de aceite é **medida, não afirmação**: (a) recorte do literal da fonte, nunca palavra reescrita de memória; (b) rodado nos dois mundos, com os dois valores no card; (c) com as opções que o tornam discriminante (`-SimpleMatch`, `-CaseSensitive`); (d) com **alvo alcançável dentro do escopo declarado do card** — *executando só o que este card manda executar, este comando pode sair como o card diz?* | `AE-23`, `AE-19`, `AE-25`, `AE-26`/`AE-27`/`AE-28` |
| (xiii) | nenhum número de corpus — total de suíte, contagem de cards, de ocorrências ou de linhas — entra como constante de aceite: entra como **relação**, com o literal citado só como referência datada | `AE-21` |
| (xiv) | card **reescrito** re-declara as rotas de achado que apontam para ele | `AE-9` |
| (xv) | regra nova de tabela declara o efeito sobre **cada** valor do domínio que toca, e confronta a ação com o domínio que o instrumento de fechamento aceita | `AE-20`, `AE-22` |
| (xvi) | **rótulo de campo termina na mesma linha em que começa.** Decoração no rótulo (data, `ESC-n`, `DM-n`, ressalva) é permitida enquanto o `:**` couber na primeira linha; o parser de campos do kit lê **linha a linha**, de modo que rótulo quebrado faz o campo **desaparecer**, não apenas ficar feio | `AE-34` |
| (xvii) | **o aceite cobre o mundo que o próprio produto cria.** Quando o módulo **emite** uma forma, a `Verificação` exercita **essa** forma, e não só a que ele consome: produto que escreve num formato e é aferido noutro deixa o ramo que ele mesmo produz sem nenhuma linha que o discrimine | `AE-35` |
| (xviii) | **o valor publicado no literal `Medido antes` é invariante ao que outras entregas movem.** Ele mede o que **este** card possui — exit code do comando, veredito binário, recorte do arquivo-alvo —, nunca um total de corpus que qualquer outra entrega desloca (total de suíte, contagem de módulo compartilhado, contagem de cards ou de insumos do próprio plano); quando a pergunta é sobre corpus, o comando publica o **veredito** (`exit 0`, `iguais`, `1`) e o número absoluto desce para a prosa como referência **datada**, fora do literal | `AE-49` |

### 8.1 A forma normativa do bloco `Verificação`

Todo item de `Verificação` tem **três** elementos, nesta ordem e legíveis por máquina:

1. o **comando**, em bloco cercado, exatamente como foi rodado;
2. o **valor esperado**, na linha iniciada por `→`;
3. o **valor medido antes**, no literal `**Medido antes: <valor>**` — os elementos 2 e 3 saem juntos, na forma `→ **1**. **Medido antes: 0**.`

O item começa em `N.` seguido **imediatamente** do bloco cercado — nenhuma prosa entre o número e a abertura do comando. Prosa explicativa, quando houver, vai **depois** do `**Medido antes: <valor>**`, nunca antes do comando.

Não é forma nova: 32 itens do `P-0740` já a usam, e o que a norma acrescenta é torná-la obrigatória e **parseável**. A razão de ser norma, e não um décimo sexto critério, está medida: dezoito critérios em vigor não impediram oito defeitos numa janela, e o `AE-30` nasceu no mesmo ato que escreveu o critério contra ele, três parágrafos acima da linha defeituosa.
Checklist lido pelo autor não fecha defeito de autoria; o que fecha é comando que falha ruidosamente no ato da autoria.

**Passo mecânico, e o ciclo:** `python .claude/tools/card_check.py --plano <plano> --tarefa <ID>`. **Card cujo `card_check` não sai 0 não se despacha.**

**Forma A (bloco cercado)** — a forma acima: comando em bloco cercado, esperado na linha `→`,
medido antes no literal `**Medido antes: <valor>**`.

**Forma B (inline)** — item cujo resto da linha do marcador, depois de `N.`, começa por crase
simples: `` N. `<comando>` → <esperado>[ — antes `<a>`, depois `<b>`] ``. `→ <esperado>` e o par
` — antes …, depois …` são opcionais, cada um; esperado é o texto entre `→` e ` — antes` (ou o fim
do item, quando não há par). O mundo comparado deriva do status do card: `done` compara `depois`
— ou, sem par, o conteúdo da primeira crase do esperado —; qualquer outro status compara `antes`
(ausente: `sem valor antes`; esperado sem `→`: `sem valor esperado`; esperado sem crase: `esperado
sem literal`) (DFP-2, emendada por DFP-14).

Toda ocorrência `` `<caminho>:<linha>` `` em `Arquivos-alvo` e `Passos` é âncora: o literal é o
texto entre crases logo após ` — ` ou `: ` na mesma linha, desescapado e com `strip()`, e confere
quando está contido em alguma linha (`strip()`) da faixa `linha..fim`; âncora sem literal e literal fora da linha são falhas nomeadas, e âncora
sem literal só passa se o mesmo texto de âncora tiver literal noutra ocorrência do card — a
conferência roda só com mundo `antes` (DFP-4, emendada por DFP-16).

### 8.2 Julgamento dos cards do `P-0740` (2026-09-19)

Vinte cards, re-contados no ato: 23 `LM-*` no plano, menos `LM-T5`, `LM-T5a` e `LM-T6` — contagem como relação, nunca constante, que é o critério (xiii) aplicado a esta própria linha.

| card | veredito | defeito nomeado |
|---|---|---|
| `LM-T1` | não passa | (x) piso de suíte como constante de aceite (`total ≥ 145`, `142 + 3`) |
| `LM-T1a` | não passa | (x) `piso ≥ 145` e a baseline de módulo `47 → 55` como constantes |
| `LM-T2` | não passa | (xiv) a reescrita do `ESC-3` proibiu tocar o bloco A e não re-declarou a rota do `AE-9`, que apontava para este card; o buraco só apareceu no laudo da tarefa seguinte |
| `LM-T2a` | não passa | (x) `piso ≥ 156` como constante |
| `LM-T2b` | não passa | (xiii) o `Pronto quando` fixa `175 passed` como aceite; e a `Verificação` 4 só ficou exequível depois do reparo do `AE-25` |
| `LM-T2c` | não passa | (xv) a `A8a` nova não partiu o domínio: dois pares (`veredito`, `recomendacao`) ficaram sem regra útil, um deles mandando fazer o que o instrumento recusa (`AE-20`) |
| `LM-T2d` | não passa | (xv) publicou a frase de partição sem confrontar a ação da `A7` com o domínio que o `rdo.py close` aceita (`AE-22`) |
| `LM-T2e` | **passa** | padrão por recorte da fonte, dois mundos por linha, invariante declarado com o casamento conferido, piso em relação |
| `LM-T2f` | não passa | (xiii) aceite absoluto (`9 passed`, `174 passed`) onde a relação é `−1`; hoje ainda casa (suíte re-medida neste ato: `175 passed`) e envelhece no primeiro card que somar teste |
| `LM-T3` | não passa | (x) `piso ≥ 153` como constante; e (vii) `Verificação` em prosa corrida, sem os dois valores rodados por linha |
| `LM-T3a` | **passa** | piso em relação com literal datado, quatro linhas medidas, regra concorrente por teste, guarda de borda com residência única |
| `LM-T3b` | **passa** | baselines re-medidas verdadeiras neste ato (`9`; `1, 2, 5, 1, 2`), concorrente nomeado, contingência que **para** se o invariante mudar |
| `LM-T4` | não passa | (i) o item (c) manda **decidir** o que permanece, o que migra e o que é aposentado, sem decisão fechada no plano; e (viii) publica na §7, lista que o `check-readme` conta contra a tabela de `README.md` — arquivo fora dos alvos e guarda fora do aceite |
| `LM-T4a` | não passa | (x) `piso ≥ 153 + os cinco testes novos` como constante |
| `LM-T4b` | não passa | (xii)(d) o `Pronto quando` exige transitar **card real**, que o próprio card declara inalcançável (`AE-29`); a emenda do `ESC-13` moveu a `Verificação` 2 para fixture e não reconferiu o critério de pronto que dependia dela — mesma causa do `AE-30` |
| `LM-T5b` | **passa** | três elementos em todo item, contingência que prevê o envelhecimento da própria baseline, lista fechada de comandos, piso em relação |
| `LM-T7` | não passa | (viii) fechou o **item** da tabela e não a frase da mesma seção que o conta, com as cinco verificações verdes (`AE-12`); e (x) `piso ≥ 145` |
| `LM-T7a` | não passa | (x) `piso ≥ 145` como constante — no resto, o card que melhor prova discriminação, ao rodar o guarda novo contra a prosa velha antes de corrigi-la |
| `LM-T8` | não passa | (ii)/(xii)(d) dois estados de executabilidade no mesmo card: o `Pronto quando` condiciona o item (b) à `LM-T4`, e despacho nenhum fecha o card inteiro |
| `LM-T9` | não passa | (i) exige juízo do executor — dizer se a autoria de cards é da figura ou empréstimo, e fixar a regra de quando **não** acionar o consultor |

Dezesseis dos vinte não passam, e nenhum por conteúdo: o defeito mora sempre na linha de aceite — piso ou baseline como constante em oito, alvo
inalcançável dentro do escopo em dois, juízo exigido do executor em dois, domínio de tabela não partido em dois, invariante de contagem em um, rota de achado órfã em um.
