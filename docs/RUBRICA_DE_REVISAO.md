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

O laudo carrega um campo próprio para esse achado, com três alvos possíveis:

| alvo | o que o achado denuncia |
|---|---|
| `dossiê` | decomposição errada, critério de pronto inverificável, arquivos-alvo incompletos, verificação sem poder discriminante |
| `doutrina` | guardrail ausente, ambíguo ou em conflito com outro |
| `rubrica` | dimensão mal formulada, nível sem fronteira clara, peso desalinhado com o dano real |

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
correção do que o laudo aponta pertence a uma execução seguinte, com o laudo em mãos.
