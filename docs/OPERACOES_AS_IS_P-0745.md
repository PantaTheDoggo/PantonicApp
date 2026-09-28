# Operações as-is — o que o `P-0745` deixou no lugar

Documento de encerramento do plano `docs/plans/P-0745-planejador-modelo-operacao.md`, redigido em
2026-09-22 na branch `plan/planner-modelo-escopo`. Descreve **as operações que existem hoje**, não a
execução que as produziu. Todo número abaixo foi re-derivado por comando nesta data; o registro da
execução mora no plano (`## Achados da execução`) e nos dez arquivos `docs/RDO/P-0745-*.md`.

---

## O problema

Quem planeja um trabalho neste repositório recortava as tarefas por **dois números**: um percentual
de ocupação da janela de contexto (50%, tolerância até 60%) e uma tabela de tetos de turnos por
classe de tarefa (≤15, ≤40, ≤60, ≤30, ≤50). Os dois foram calibrados em 2026-08-01 sobre uma janela
de 200 mil tokens. A janela real medida em 2026-09-18 é de **um milhão** — cinco vezes maior —, e
em 2026-09-19 o dono fixou que o critério de admissão de matéria num card é **coesão, não custo**.
Os números continuavam escritos, em **cinco residências** de doutrina, dimensionando uma coisa que
eles já não dimensionavam.

Ao lado disso, a unidade que esses números mediam — a *tarefa atômica* — sobrevivia em **vinte e uma
linhas** de doutrina viva (medido em 2026-09-21), enquanto o lado do executor já falava de módulo
coeso desde o plano anterior. E o protocolo de quem planeja mandava, na Fase 3, que cada card citasse
uma operação do modelo de domínio do plano — mas previa **uma única parada**, com o plano já
completo. Na prática, quem planejava escrevia os cards **antes de as operações existirem**, e depois
alguém escrevia o modelo por cima.

## A solução, em uma frase

O que era recorte por juízo e por número vira **leitura do modelo**: a quantidade de cards de um
plano passa a ser a contagem de operações dele, e o aceite de cada card passa a ser o estado final
das propriedades que a sua operação altera.

## Vocabulário mínimo

| termo | o que é |
|---|---|
| **modelo de domínio** | a seção `## 1` de um plano: os objetos que o plano transforma, as propriedades de cada objeto, e as operações que levam essas propriedades de um estado inicial a um estado final |
| **operação** (`OP-<n>`) | uma linha do modelo — um ato que altera propriedades nomeadas de objetos nomeados; declara de que objetos precisa e que propriedades altera |
| **card** | a unidade despachada a um agente executor: uma seção `### <ID> — <título>` da `## 8. Tarefas` do plano |
| **lastro** | a lista `tarefas:` que cada operação carrega, dizendo **quais cards a materializam**; é sobre quem entrega, não sobre o que se entrega |
| **censo** | o inventário, dentro do plano, de cada linha do repositório que carrega a forma que o plano aposenta, cada uma com o card que a reescreve |
| **residência** | o arquivo e a seção onde uma regra mora. A mesma regra em duas residências diverge no primeiro ajuste, e por isso cada regra tem uma só |
| **guarda executável** | função de teste que falha se a forma aposentada voltar ao texto de doutrina |
| **régua de dimensionamento** | o critério com que quem planeja decide o que cabe num card |

---

## O arco — os estratos

O modelo do plano tem **seis operações**, e elas são o esqueleto: um card por operação na autoria,
mais três cards corretivos que se somaram às operações que reparam. Os seis se agrupam em três
estratos, e cada estrato é inútil sem o anterior — não se muda a conduta de quem planeja (B) antes
de a norma que ele cita dizer outra coisa (A), e não se descreve a figura nova (C) antes de ela
existir.

| estrato | operação | pergunta que responde | cards |
|---|---|---|---|
| **A — a doutrina** | `OP-1` | com que régua se dimensiona um card, agora que os números caíram? | `PLN-T2` |
| | `OP-2` | que forma o card passa a ter? | `PLN-T3` |
| **B — a conduta** | `OP-3` | como corre uma sessão de planejamento quando o modelo ainda não existe? | `PLN-T4`, `PLN-T4a` |
| | `OP-4` | de quem é a lista de cards de cada operação? | `PLN-T5`, `PLN-T5a` |
| **C — a figura publicada** | `OP-5` | onde a figura de quem planeja se descreve? | `PLN-T1`, `PLN-T6` |
| | `OP-6` | como quem chega ao repositório encontra a unidade nova? | `PLN-T7`, `PLN-T7a` |

Duas observações sobre a tabela. A `OP-5` é a única que se materializa em **dois** cards de autoria,
e não por partição: a `PLN-T1` mede o retrato do **antes** e a `PLN-T6` escreve a descrição, que
consome esse retrato como insumo — por isso a `PLN-T1` roda primeiro de toda a fila, ainda que
pertença ao último estrato. E os três cards com sufixo `a` (`PLN-T4a`, `PLN-T5a`, `PLN-T7a`)
**nasceram durante a execução**: cada um repara um resíduo do card irmão e se soma à operação dele,
em vez de abrir operação nova. O plano nasceu com sete cards e fechou com dez.

Nenhum card ficou fora de estrato, e nenhum foi `cancelled`.

---

## `PLN-T1` — O retrato medido de quem planeja, antes da mudança

**Contexto que a motivou:** a descrição pública da figura de quem planeja não existia — não havia
arquivo, enquanto a figura do consultor já tinha o seu (`docs/consultant-spec.md`) e entrada no
índice de documentos. Escrever a descrição sem medir antes produziria adivinhação, e a regra do
projeto é que só se afirma o que foi medido.

**O que é o artefato:** a seção `## 12. Agregado medido` do próprio plano — dez subseções, uma por
dimensão da especificação prevista, cada uma com uma tabela de métricas (ocorrências, mais antiga,
mais recente, classe dominante, exemplo). Nenhum dado bruto: só o agregado.

**Como funciona na prática:** a seção é lida, não executada. O que se afere nela é o tamanho e a
forma, e o comando que o faz recorta o arquivo do heading até a seção seguinte:

```
python -c "import re,pathlib;t=pathlib.Path('docs/plans/P-0745-planejador-modelo-operacao.md').read_text(encoding='utf-8');m=re.search(r'^## 12\. Agregado medido\n.*?(?=^## )', t, re.M|re.S);print(len(m.group(0).splitlines()) if m else 0)"
```

Saída hoje: `106` — dentro do limite de 120 linhas que o card fixou. O conteúdo que essas 106 linhas
carregam é, por exemplo, a dimensão 7: `linhas de planejamento | 1`, `consumo mediano | 183k tk`,
`consumo máximo | 183k tk (mesma linha)`. Mediana e máximo coincidem porque há **uma** observação na
série, e o agregado a publica assim em vez de arredondar a ausência de dados.

**Protege contra:** especificação escrita de impressão. Toda afirmação da descrição publicada
(`PLN-T6`) tem de apontar para uma linha deste agregado ou para uma decisão do plano; sem o
agregado, não haveria a que apontar, e a alternativa seria descrever a figura por memória.

---

## `PLN-T2` — A régua sem número

**Contexto que a motivou:** os dois números do dimensionamento — 50% de ocupação e a tabela de tetos
de turnos por classe — viviam em cinco residências de doutrina, calibrados em 2026-08-01 sobre uma
janela cinco vezes menor que a real. Vinte e uma linhas de doutrina viva chamavam a unidade de
trabalho de *tarefa atômica*.

**O que é o artefato:** três documentos de norma reescritos — `GOVERNANCA.md` (nove sítios,
incluindo a *Diretriz de dimensionamento de tarefa* e a tabela de tetos, que saiu),
`.claude/global/CLAUDE.md` e `docs/RESIDENCIA_DOUTRINA.md` — mais a cópia das regras globais que o
dono carrega fora do repositório, e um arquivo novo: `tests/test_doutrina_unidade.py`.

**Como funciona na prática:** a régua é lida por quem planeja e diz, em `GOVERNANCA.md` §3, que a
tarefa se delimita por três critérios: *(a)* materializar uma operação inteira do modelo, *(b)* caber
num contexto coerente e coeso, *(c)* ser autossuficiente em contexto para a execução. A mesma seção
acrescenta a frase que fecha a porta: *"Nenhum percentual de ocupação e nenhum número de turnos
entram no dimensionamento"*. A guarda executável é o que impede a volta:

```
$ python -m pytest tests/test_doutrina_unidade.py -q
........                                                                 [100%]
8 passed in 0.02s
```

A primeira das oito funções é literal ao ponto de não admitir paráfrase:

```python
def test_governanca_dimensiona_pela_operacao_sem_percentual():
    t = _texto("GOVERNANCA.md")
    assert "50% de ocupação" not in t
    assert "Orçamento de turnos por tarefa atômica" not in t
    assert "materialização de uma operação do modelo" in t
```

**Protege contra:** a régua fantasma — número que ninguém mais usa para decidir nada e que todo
agente continua lendo como se decidisse. E contra *meia mudança publicada*: a mesma edição foi
aplicada, byte a byte, às duas cópias das regras globais, porque editar só a do repositório deixaria
a cópia que carrega em toda sessão contradizendo a doutrina.

**O procedimento que ela instalou:** **a classe do card é natureza, não teto.** A classe do
cabeçalho (`mecanica|implementacao|comportamental|investigacao|redacao`) continua declarando a
natureza do trabalho e calibrando a profundidade de quem executa — os instrumentos a leem —, e não
carrega nenhum número.

---

## `PLN-T3` — O formato do card passa a exigir a operação que ele materializa

**Contexto que a motivou:** o bloco de formato que quem planeja preenche abria por *"Formato de uma
tarefa atômica"* e pedia um objetivo em uma frase mais um critério objetivo solto. Nada no formato
ligava o card ao objeto que ele transforma, e o campo que nomeia a operação não constava dele.

**O que é o artefato:** a seção `## Formato de uma tarefa` da skill `diario-de-obras`
(`.claude/skills/diario-de-obras/SKILL.md:245`), mais três residências menores que deixaram de
nomear a unidade antiga: as skills `modelo-por-fase` e `bootstrap-pantonic` e o agente
`pantonic-fora-da-caixa`.

**Como funciona na prática:** a skill é carregada por quem registra ou despacha uma tarefa no diário
de obras, e o texto que ela apresenta agora abre assim:

> Uma tarefa é a **materialização de uma operação do modelo** (`GOVERNANCA.md` §3.2): o `Objetivo`
> copia o texto da operação, o campo `Operação do modelo` traz o texto e os contratos copiados
> (…), e o `Pronto quando` deriva do estado final das propriedades que a operação altera. Um card
> por operação; card corretivo (`T<n>a`) soma-se à operação do card que corrige.

O gabarito que vem logo abaixo ganhou duas linhas que antes não existiam — o campo
`- **Operação do modelo:**` e a forma do `Pronto quando` *por propriedade que a operação altera*.

**Protege contra:** card que descreve trabalho sem dizer que objeto ele transforma. Sem o campo da
operação, não há como aferir se a verificação do card mede as propriedades que ele alterou — e
`Pronto quando` volta a ser uma frase de intenção.

---

## `PLN-T4` — A sessão de planejamento ganha uma saída que termina sem plano

**Contexto que a motivou:** o protocolo de quem planeja mandava que o modelo precedesse a
decomposição, mas previa **uma única parada** — o plano já gravado, cards inclusive. As duas
instruções não coexistem: quem planeja escrevia cards citando operações que ainda não existiam, e a
definição pública da figura anunciava decomposição em *"tarefas atômicas fechadas"*.

**O que é o artefato:** `.claude/agents/pantonic-planner.md`, reescrito em dez regiões — a
`description` do frontmatter, os fatos estáveis, a tese do papel, a abertura do protocolo, a Fase 3
partida em **3a** e **3b**, a Fase 4, a Fase 5, a anatomia do card, a rodada de replanejamento e a
lista do que o papel nunca faz —, mais a região gerada `kit:agents` de `.claude/README.md`,
regenerada por script a partir do frontmatter.

**Como funciona na prática**, em quatro tempos:

1. **O que dispara** — um pedido de plano novo chega a quem planeja.
2. **A entrada** — o enunciado do pedido e os fatos que a sondagem levantou.
3. **O processamento** — na **Fase 3a** ele grava `docs/plans/P-NNNN-<slug>.md` com o esqueleto
   fixo e **sem** duas seções: a `## 1. Modelo conceitual` e a `## 5. Tarefas`. Então **para**.
4. **A saída** — `SAÍDA 3`: o dossiê `Ato de modelo` de `autoria`, com seis campos fechados
   (`Plano`, `Ato`, `Motivo`, `Fato novo`, `Restrição`, `Devolver`), devolvido na linha de retorno.
   Quem conduz a sessão despacha o modelador; nenhum agente aciona outro. Com a seção do modelo na
   árvore, a **Fase 3b** escreve um card por operação, na ordem delas, com o id derivado do número
   da operação.

A presença das duas fases é aferida por literal:

```
$ grep -c 'SAÍDA 3' .claude/agents/pantonic-planner.md
1
$ grep -c 'Fase 3b' .claude/agents/pantonic-planner.md
2
```

O resultado chega à porta de entrada pela `description` regenerada, que hoje anuncia *"decompor o
modelo de domínio de um plano em cards fechados — um por operação do modelo"*.

**Protege contra:** a operação inventada. Sem a parada obrigatória, quem planeja escreve `OP-1`,
`OP-2`, `OP-3` como rótulos de conveniência e alguém escreve o modelo depois para caber nos cards —
o que inverte a ordem entre a coisa e a medida dela.

**O procedimento que ela instalou:** **a partição é do modelo, não de quem planeja.** Um card por
operação, uma operação por card; card corretivo de replanejamento **soma-se** à operação do card que
corrige; e operação que não cabe num card coeso **não se parte** — é defeito do modelo, e volta a
quem o escreve por dossiê.

---

## `PLN-T4a` — O ponteiro que sobreviveu à tabela aposentada

**Contexto que a motivou:** onze horas depois de a tabela de tetos por classe ser removida de
`GOVERNANCA.md`, uma linha de `.claude/agents/pantonic-planner.md` continuava dizendo *"a régua
numérica é a tabela de classes de `GOVERNANCA.md` §3, interna a este papel"*. A tabela não existia
mais; o ponteiro para ela, sim. O censo do plano não podia tê-la apanhado: a varredura de 2026-09-21
buscou `atômic|atomic` e `50%|60%|~80 linhas|fatias verticais`, e a frase diz *"tabela de classes"*,
que não casa nenhum dos dois padrões.

**O que é o artefato:** a segunda metade de uma frase, em `.claude/agents/pantonic-planner.md`, mais
uma sétima função de teste em `tests/test_doutrina_unidade.py`. A primeira metade da frase —
*"Nenhum teto se escreve no card"* — sobreviveu intacta, porque continua verdadeira.

**Como funciona na prática:** a frase hoje remete à régua vigente em vez de à aposentada, e a guarda
tranca a remissão pelos dois lados — ausência do ponteiro morto, presença da negação viva:

```python
def test_conduta_do_planejador_nao_remete_a_tabela_aposentada():
    t = _texto(".claude/agents/pantonic-planner.md")
    assert "tabela de classes" not in t
    assert "tabela de tetos" not in t
    assert "Nenhum teto se escreve no" in t
```

Medido hoje: `grep -c 'tabela de classes' .claude/agents/pantonic-planner.md` devolve `0`.

**Protege contra:** *meia mudança publicada* — a regra cai numa residência e o ponteiro para ela
sobrevive noutra, de modo que um agente frio lendo só a segunda continua obedecendo a primeira.

---

## `PLN-T5` — De quem é a lista de cards de cada operação

**Contexto que a motivou:** a `PLN-T4` instituiu que quem planeja grava o esqueleto do plano **sem
cards** e devolve o pedido de autoria do modelo. Mas o portão do papel que escreve o modelo tratava
duas violações do instrumento como defeito da seção: `V1` (operação sem tarefa) e `V3` (tarefa
inexistente). Sobre um plano ainda sem cards, as duas disparam **por construção** — e quem escreve o
modelo nunca conseguiria fechar o portão. A conduta nova era inexequível pela conduta antiga.

**O que é o artefato:** dois parágrafos novos em `GOVERNANCA.md` §3.2 — *Lastro* e *Rascunho antes
do Marco 1* —, a linha `planejador` da tabela *Quem escreve* da mesma seção, e o bloco de fatos
estáveis de `.claude/agents/pantonic-model-designer.md`. As duas pontas dizem o mesmo, no mesmo card.

**Como funciona na prática:** `GOVERNANCA.md:435` fixa a atribuição — *"É lastro, não modelo: não
descreve o que o plano entrega, descreve quem o entrega. Por isso é a única linha da seção que não é
do modelador depois da autoria"*. E o portão, do outro lado, passou a devolver em vez de travar:

> Só cinco violações **não são suas**: `V2`, `V4` e `V14`, que moram no card, e `V1` e `V3`, que
> moram no **lastro** (…). Havendo **apenas** essas, devolva o ato com a **saída literal** do
> `check`, nomeando as violações que ficaram.

A saída literal de que o texto fala é esta, exercitada contra uma fixture do repositório:

```
$ python .claude/tools/modelo.py check --plano tests/fixtures/modelo/plano-invalido.md
V13 secao — cabeçalho, objetos, estado ou registro de versões ausente
V5 OP-1 — objeto inexistente objeto fantasma
V1 OP-2 — operação sem tarefa
V3 OP-3 — tarefa inexistente EX-T99
...
modelo: FALHOU — 10 violação(ões)
```

As linhas `V1` e `V3` são as que voltam nomeadas a quem decompõe o plano, em vez de bloquearem o ato
de quem escreve o modelo.

**Protege contra:** o impasse entre dois papéis — um que não pode escrever cards antes do modelo e
outro que não pode fechar o modelo antes dos cards. E, no sentido inverso, contra a versão do modelo
criada só porque um id de card mudou: antes da validação do dono, a seção é rascunho e se substitui
no lugar.

---

## `PLN-T5a` — A frase que governava o portão

**Contexto que a motivou:** a `PLN-T5` publicou, nas duas pontas, que `V1` e `V3` são do lastro de
quem planeja. Mas a frase **antecedente** do mesmo arquivo — que o card não podia editar, por estar
fora dos alvos declarados — continuava dizendo que *"é da seção toda violação que o instrumento não
indexa pelo `<ID>` de uma tarefa: as de `secao`, as de `OP-<n>` e as de `objeto`"*. O instrumento
indexa `V1` e `V3` **por `OP-<n>`**. As duas leituras coexistiam no mesmo arquivo, e a que governava
era a antiga. No mesmo exame ficou medido um segundo defeito: a frase enumerava as violações de
objeto como `(V6, V7, V15, V17)` — quatro de cinco, porque `V21` existe e não era citada.

**O que é o artefato:** a frase antecedente de `.claude/agents/pantonic-model-designer.md`,
reescrita em dois pontos, e uma oitava função de teste.

**Como funciona na prática:** o critério antigo não foi substituído — ele está correto para oito dos
dez códigos indexados por operação. O que o texto passou a fazer é **nomear a exceção onde o
critério é enunciado**, e trocar a lista fechada por uma regra:

> (…) **exceto `V1` e `V3`**: o instrumento as indexa por `OP-<n>`, mas elas moram no lastro e não
> são suas (…). A classe se lê pelo **rótulo com que o instrumento indexa** a violação, nunca por
> lista de códigos: o vocabulário `V1`..`V21` cresce, e lista fechada envelhece.

A guarda prende as três coisas ao mesmo tempo — a exceção presente, a lista fechada ausente, a
contagem certa:

```python
def test_gate_do_modelador_nao_classifica_lastro_como_secao():
    t = _texto(".claude/agents/pantonic-model-designer.md")
    assert "exceto `V1` e `V3`" in t
    assert "(`V6`, `V7`, `V15`, `V17`)" not in t
    assert "Só cinco violações" in t
```

**Protege contra:** duas leituras concorrentes da mesma regra no mesmo arquivo, com a mais antiga
governando por estar antes. E contra a lista de códigos que envelhece a cada código novo — o
vocabulário do instrumento cresceu de 20 para 21 durante esta mesma execução.

---

## `PLN-T6` — A figura ganha documento próprio

**Contexto que a motivou:** a figura de quem planeja existia só na definição de conduta do agente —
um arquivo que diz **como** agir, não **o que a figura é**. Quem precisasse decidir quando acionar
o planejamento, o que esperar dele e quanto custa não tinha onde ler.

**O que é o artefato:** `docs/planner-spec.md` — arquivo novo, **217 linhas**, **11 seções `##`**:
uma por dimensão prevista, mais a `## 0. O que esta especificação não é`, que declara o que o
documento **não** hospeda (o escopo do papel e o protocolo de conduta, ambos com residência própria
e citados, nunca reenunciados).

**Como funciona na prática:** cada afirmação do documento carrega uma âncora — no agregado medido
(o antes) ou numa decisão do plano (o depois) —, e cada seção fecha com um bloco `> **Âncoras:**`
que as lista. O documento se recusa a afirmar o que não mediu, e diz isso explicitamente. Na
dimensão do custo:

> Mediana e máximo coincidem porque há uma única observação. Primeira e última data coincidem pela
> mesma razão. Com `n = 1` não há dispersão, não há tendência e não há valor típico: **183k tokens
> é uma observação, não uma expectativa**, e esta seção não a converte em previsão.

E a `## 10. O que esta especificação não fecha` é uma tabela de **nove** perguntas em aberto — as
cinco que o agregado já trazia e quatro que a redação acrescentou —, cada uma com a coluna *o que
seria preciso medir para respondê-la*. Uma delas é o caso em que o executor **recusou** cumprir a
rota que lhe deram, e a recusa foi julgada correta: o agregado fixa os extremos e a contagem `3` de
uma dimensão sem permitir reconstruir a terceira ocorrência, de modo que nomeá-la seria escolher.

**Protege contra:** a especificação que preenche lacuna com o plausível. A alternativa a nomear a
pergunta é respondê-la por adivinhação, e um número inventado num documento de decisão é publicado
como fato.

---

## `PLN-T7` — A porta de entrada passa a falar da unidade nova

**Contexto que a motivou:** o `README.md` é o que um leitor novo abre primeiro, e ele definia a
unidade de execução como *tarefa atômica* em nove linhas, publicava a tabela de tetos por classe
como régua viva e não tinha entrada de índice nem para a especificação nova nem para este plano.
`GOVERNANCA.md:78,80` — no parágrafo de abertura da mesma seção de onde a tabela de tetos saiu —
ainda nomeava o *orçamento de turnos* como alavanca de qualidade.

**O que é o artefato:** `README.md` (glossário e cinco seções), duas entradas novas em
`docs/DOC_MAP.md` — `docs/DOC_MAP.md:232` para a especificação e `:255` para o plano, ambas com
propósito, quando consultar e o padrão `Grep` de acesso — e o parágrafo de abertura de
`GOVERNANCA.md` §3.

**Como funciona na prática:** a entrada de glossário do `README.md` passou a definir a unidade assim:

> **Card** — a unidade de execução: a materialização de **uma operação do modelo** do plano,
> executável por um agente que não conhece o projeto, em contexto limpo, sem busca transversal —
> uma operação inteira, coesa e autossuficiente em contexto, sem percentual e sem teto.

O índice de documentos é como um agente frio alcança o que o plano publicou; hoje ele tem 13 blocos
`Acesso:`, dois deles deste plano. E a estrutura do `README.md` continua conferida por script:

```
$ pwsh -NoProfile -File .claude/checks/check-readme.ps1
check-readme: OK - 10 agente(s), 11 skill(s), 20 guardrail(s), versão '0.0.0', 14 seção(ões) com
Fonte da verdade válida; frases de contagem de 'Os guardrails' conferidas: (…) =True, (…) =True.
```

**Protege contra:** a documentação de entrada que ensina a forma que o repositório aposentou. Um
agente ou uma pessoa que comece pelo `README.md` aprenderia a régua errada e a aplicaria com toda a
confiança de quem leu a fonte oficial.

---

## `PLN-T7a` — O README deixa de defender o teto que ele mesmo declara aposentado

**Contexto que a motivou:** a `PLN-T7` instalou em `README.md` o parágrafo que **declara** a tabela
de tetos aposentada. Mas **oito sítios** do mesmo documento continuavam definindo, defendendo ou
pressupondo esse teto: a entrada de glossário *Orçamento de turnos*; o parágrafo do `≤30`; o *"Por
quê"* que argumenta a favor do teto graduado; a premissa de estouro de teto em *"Onde o gerente
intervém"*; a calibração de tetos como finalidade da série, em dois pontos; e a linha da tabela de
trade-offs. O documento de entrada contradizia a si mesmo. Nada apanhou: o único aferidor do card
anterior era o script de estrutura, que confere contagens e **não discrimina órfão semântico**.

**O que é o artefato:** oito regiões de `README.md` reescritas, e a oitava função de
`tests/test_doutrina_unidade.py`.

**Como funciona na prática:** a doutrina viva do documento foi reescrita e as **duas medidas
históricas datadas** foram preservadas — medida do passado é registro, não regra, e reescrevê-la
apagaria a evidência que justifica a troca. A guarda afere as duas direções no mesmo teste:

```python
def test_readme_nao_defende_a_regua_aposentada():
    t = _texto("README.md")
    assert "Orçamento de turnos" not in t
    assert "Teto de turnos graduado por classe" not in t
    assert "não cabe em ≤30" not in t
    assert "71 turnos e ~189 mil tokens" in t
```

Medido hoje: a soma das três formas revogadas devolve `0` ocorrências, e a medida histórica devolve
`2` — ambas intactas.

**Protege contra:** guarda que só afere ausência, e que por isso autorizaria apagar demais. O
documento tem de perder a regra revogada **e** manter a evidência datada que motivou revogá-la; um
teste que só checasse a primeira metade aprovaria a deleção da segunda.

---

## O que vale além deste plano

| regra | o que resolve | residência |
|---|---|---|
| A unidade de trabalho é a materialização de uma operação do modelo | recorte de card deixa de ser juízo de quem planeja e passa a ser consequência do modelo | `GOVERNANCA.md` §3, *A unidade de trabalho é o módulo coeso* |
| A régua de dimensionamento são três critérios sem número | nenhum percentual e nenhum teto dimensionam tarefa; o único limiar que resta governa a janela de orquestração | `GOVERNANCA.md` §3, *Diretriz de dimensionamento de tarefa* |
| A classe do card é natureza, não teto | a classe continua calibrando a profundidade de quem executa, sem carregar número | `GOVERNANCA.md` §3, *Classe do card — natureza, não teto* |
| Um card por operação; corretivo soma-se à operação que repara; operação não se parte | a contagem de cards de um plano deixa de ser arbitrária, e operação que não cabe num card vira achado de modelo | `GOVERNANCA.md` §3 e `.claude/agents/pantonic-planner.md`, Fase 3b e rodada de replanejamento |
| A sessão de planejamento pode terminar sem plano fechado (`SAÍDA 3`) | a decomposição só começa com o modelo na árvore | `.claude/agents/pantonic-planner.md`, Fase 3a |
| O lastro é de quem planeja; `V1` e `V3` voltam nomeadas em vez de travarem o ato | o portão de quem escreve o modelo fecha sobre plano ainda sem cards | `GOVERNANCA.md` §3.2, *Lastro*; `.claude/agents/pantonic-model-designer.md` |
| Antes da primeira validação do dono, a seção do modelo é rascunho substituível no lugar | evita versão de modelo criada por mudança que não altera o que o plano entrega | `GOVERNANCA.md` §3.2, *Rascunho antes do Marco 1* |
| A classe de uma violação se lê pelo rótulo com que o instrumento a indexa, nunca por lista de códigos | lista fechada de códigos envelhece a cada código novo | `.claude/agents/pantonic-model-designer.md` |

---

## Os ganhos, medidos

Tudo re-derivado em 2026-09-22, contra as referências datadas de 2026-09-21 que o plano registrou.

| medida | antes | depois |
|---|---|---|
| linhas de doutrina viva que chamam a unidade de *tarefa atômica* | 21 (2026-09-21) | 4 — e nenhuma é regra: duas são medidas datadas de 2026-07 preservadas, uma é a linha que **registra** a aposentadoria e uma é uma linha de tabela de trade-offs citando a mesma medida histórica |
| ocorrências de *tarefa atômica* na cópia das regras globais que o dono carrega | 2 | 0 |
| régua de dimensionamento em `GOVERNANCA.md` §3 | percentual de ocupação (50%, tolerância 60%) mais tabela de tetos por classe (≤15/≤40/≤60/≤30/≤50) | três critérios sem número |
| descrição pública da figura de quem planeja | não existia | `docs/planner-spec.md`, 217 linhas, 11 seções `##` |
| guardas executáveis sobre a doutrina da unidade de trabalho | 0 | 8 funções em `tests/test_doutrina_unidade.py`, todas verdes |
| total da suíte | `262 passed` (2026-09-21) | `277 passed` (2026-09-22) |
| blocos `Acesso:` em `docs/DOC_MAP.md` | 9 (2026-09-21) | 13 — dois deles deste plano (`:232` e `:255`); os demais vieram de outra frente na mesma árvore |
| conformidade do modelo do plano | versão 1 recusada pelo dono em 2026-09-21 | `modelo: OK — 6 operações, 3 objetos, 7 propriedades, 10 tarefas, versão 4`, exit `0`; `show` reporta `estágio atual: concluído` |
| vereditos de revisão | — | 10 cards julgados: 7 `aprovado` 100%, 3 `ressalva` (88%, 94%, 83%); **dimensão bloqueante em nenhum** |

**Custo da execução, medido, não estimado.** `docs/telemetria.tsv` registra, para as tarefas
`PLN-*` e `MARCO*` de 2026-09-22, **38 registros**, somando **852 tool uses** e **4.553,9k
tokens** — 3.959,3k em 31 registros de Opus e 594,6k em 7 de Sonnet. A leitura é direta: o recorte
não tem mais duplicata (`sort | uniq -d` devolve vazio).

Nove pares duplicados existiram no arquivo durante a execução e foram removidos no fechamento, com
a medição refeita. A causa é de condução do loop, não do instrumento: o gancho que grava ao fim de
cada subagente já registrava a linha da execução, e o loop apensou a mesma linha de novo em nove
das dez tarefas. A norma manda **conferir** a linha do gancho contra o consumo reportado e
corrigi-la quando divergir — não apensar uma segunda. Cada par diferia **só na duração**, em frações
de segundo: `tool_uses` e `tokens_k` eram idênticos, de modo que nenhum total publicado antes da
limpeza estava certo, mas nenhuma medida por tarefa estava errada. Registrado no plano.

---

## O padrão que a execução revelou

Os achados registrados no plano não são assuntos independentes. **Nove deles são uma raiz só, vista
em camadas** — e cada camada só ficou visível depois de a anterior ser corrigida. A progressão vale
mais que qualquer um dos casos isolados.

**A raiz, isolada no quinto degrau:** a régua de autoria de card do projeto prende a exigência
*"número re-derivável por comando, nunca copiado"* à **linha de aceite** do card. Cinco dos seis
primeiros defeitos moraram **fora** do bloco de verificação — em declaração de arquivos-alvo, em
restrições, em descrição de tamanho de bloco e em censo. A régua, como estava escrita, não alcançava
a classe.

**Dois fatos que dão a escala.** Os defeitos tiveram **seis autores distintos** — dois papéis de
planejamento, três execuções diferentes e o papel de consultoria. Não é descuido individual: é vão
de régua. E o defeito do quarto degrau foi apanhado num card que, se não fosse reparado, **teria
bloqueado a última tarefa do plano** — apanhado por varredura deliberada dos cards ainda abertos,
não por sorte.

### Os degraus, com estado

| # | o que se descobriu | estado |
|---|---|---|
| 1 | **Âncora de linha não é invariante.** Um card declarava um alvo em `SKILL.md:206-225`; o heading real estava em **245**, deslocado +39 por trabalho não commitado de outra frente no mesmo arquivo. Pior que o deslocamento: o passo descrevia um bloco como tendo 18 linhas, e ele tinha 14 — e a contingência do card cobria a âncora que não casa, não a **contagem** errada. Reincidiu em mais três gerações de re-ancoragem, sempre resolvida pelo literal | 🟡 **Caso fechado, classe sem guarda** — os quatro casos foram resolvidos no despacho; nada impede o quinto |
| 2 | **Censo por enumeração não é censo.** Um inventário levantado comparando os trechos já conhecidos entre duas cópias de um documento prova que **esses trechos** são iguais, e não diz nada sobre o terceiro. O mesmo defeito apareceu em quatro residências diferentes: a cópia das regras globais fora do repositório, o documento de governança, a conduta de quem planeja e o portão de quem escreve o modelo | 🟡 — todos os sítios órfãos foram achados por varredura e atribuídos a cards; a régua que os evitaria não foi escrita na residência dela |
| 3 | **De quem é o número.** Das dez afirmações numéricas varridas nos cards ainda abertos, **seis constantes continuavam exatas**. Logo o defeito não é *ser constante*: o discriminante é a **autoria**. Número sobre o que o próprio card escreve não envelhece — o card é a causa dele; número sobre o resto da árvore envelhece entre a autoria e o despacho, e só sobrevive como **relação** (*"igual ao re-medido no despacho ± n"*) ou **invariância** | 🔴 **Regra escrita, aplicação pendente** — o texto da emenda está redigido verbatim no plano e roteado a um tíquete; a régua do projeto ainda não o incorporou |
| 4 | **O comando pode estar atualizado e responder à pergunta errada.** Uma execução parou com a entrega **correta** na árvore porque `grep -c` conta **linhas** e a verificação perguntava **ocorrências** — o literal exigido estava numa linha física só, e o comando devolveu `1` onde o aceite exigia `≥2`. A varredura dos cards abertos encontrou mais três da mesma espécie: contagem de identificadores distintos feita por contagem de linhas, e busca sensível à caixa sobre um corpus que mistura caixa (10 linhas contra 11) | 🔴 — os quatro aferidores foram reparados nos cards; a regra *"toda linha de verificação declara que pergunta o comando responde"* está redigida e pendente de aplicação |
| 5 | **Aposentar um conceito não é revogar o parágrafo que o instituía.** O documento de entrada declarava a régua aposentada num parágrafo e continuava a **defendê-la** em oito outros — glossário, argumento de defesa, premissa de intervenção, finalidade de uma série, linha de tabela. O alvo de uma revogação é todo enunciado que **define, defende, pressupõe ou invoca** o conceito, em toda residência, e a varredura se faz pelo conceito, nunca pelo literal do parágrafo revogado | 🟢 **Fechado com guarda** para o documento de entrada (`test_readme_nao_defende_a_regua_aposentada` prende seis literais revogados) · 🔴 para a régua geral, que continua fora da residência normativa |
| 6 | **Guarda de invariante com N residências afere contagem, não pertinência.** A guarda escrita para preservar as medidas históricas usa `assert "<literal>" in t`, que prova que **sobrou ao menos uma** — e a regra protege **duas**. Apagar uma delas passa no teste. Medido: `grep -c` devolve `2` hoje, ambas intactas, então não houve dano | 🔴 — a asserção continua como está; a regra que o caso fixa está redigida e roteada |

### Os demais achados, com estado

| achado | estado |
|---|---|
| Card publicado sem o campo que o gerador de dossiê lê, e verificação cujo comando media a prosa do próprio card em vez da seção entregue | 🟡 — os dois reparados no card, sem guarda contra a classe |
| A edição das duas cópias das regras globais: a do repositório tem guarda executável; **a do dono, fora do repositório, nenhuma** — medido hoje em `0` ocorrências da forma antiga, sem nada que o mantenha | 🟡 — a distinção mais concreta desta lista: metade do mesmo ato está trancada e metade depende de alguém lembrar |
| O portão de quem escreve o modelo, com as duas leituras concorrentes | 🟢 — fechado e trancado por `test_gate_do_modelador_nao_classifica_lastro_como_secao` |
| O ponteiro sobrevivente à tabela aposentada, na conduta de quem planeja | 🟢 — fechado e trancado por `test_conduta_do_planejador_nao_remete_a_tabela_aposentada` |
| O gerador de dossiê de evidência não isola a entrega quando a árvore carrega trabalho não commitado de outra frente — medido por arquivo, por hunk dentro de um arquivo-alvo e em arquivo não rastreado, que chega colado inteiro ao revisor | 🔴 — o remédio é conhecido (atribuição por hunk, ou cadência de commit que isole a entrega) e não foi feito |
| O instrumento do modelo confere operação → card, nunca card → operação: um card fora de toda lista `tarefas:` sai lastro órfão e o `check` continua verde | 🔴 — medido com prova durante a execução; o instrumento não foi tocado, por estar fora do escopo do plano |
| A transição `blocked` → `review` existe na doutrina e não no instrumento, que a recusa e obriga a alcançá-la por três chamadas | 🔴 — mesma natureza: doutrina andou, instrumento ficou |
| Uma frase da especificação publicada afirma primazia (*"é a primeira vez que…"*) sem âncora, contra a regra do próprio documento; e uma linha de âncoras omite a citação que as outras quatro trazem | 🔴 — as duas conhecidas, nenhuma bloqueante, nenhuma corrigida |

---

## Pendências abertas ao fim do plano

| # | pendência | por que ficou aberta | o que a fecha | bloqueia algo? |
|---|---|---|---|---|
| **1** | Três emendas à régua de autoria de card — *de quem é o número* (degrau 3), *que pergunta o comando responde* (degrau 4) e *varredura pelo conceito aposentado* (degrau 5) | a régua de autoria de card é artefato de kit, fora do objeto deste plano | aplicar os três critérios, no mesmo ato, ao tíquete `TK-72`. **O texto das três está redigido verbatim no plano** — custo de redação zero na abertura | não bloqueia este plano; a classe de defeito segue possível em todo plano futuro |
| **2** | A guarda de invariante que afere presença em vez de contagem (degrau 6) | o literal foi ditado pelo card, que proibia alterar palavra | trocar a asserção por contagem das N residências; entra no mesmo tíquete `TK-72` | não — as duas residências estão intactas hoje, medido |
| **3** | A família do instrumento de evidência e do instrumento do modelo: recorte que não isola a entrega, ausência da conferência card → operação, e a transição `blocked` → `review` que o instrumento recusa | `.claude/tools/*` está explicitamente fora do escopo deste plano | os tíquetes `TK-66`/`TK-74`, com o par de remédios já nomeado (atribuição por hunk ou cadência de commit) | não bloqueou nenhuma entrega; encareceu todas as revisões desta execução, que exigiram reconciliação manual por hunk e por data de modificação |
| **4** | A terceira ocorrência da sexta dimensão do agregado não se reconstrói: a tabela fixa os extremos e a contagem `3`, e há **quatro** candidatas no corpus | rotear a um card a correção de um dado que o corpus não permite reconstruir produz tarefa parcialmente impossível; a recusa do executor foi julgada correta | declarar o critério de inclusão usado na medição e reaplicá-lo às quatro candidatas — exige o corpus aberto | não. Está declarada como pergunta em aberto na `## 10` de `docs/planner-spec.md`, com o que seria preciso medir |
| **5** | Duas imperfeições de redação em `docs/planner-spec.md`: uma afirmação de primazia sem âncora e uma linha de âncoras incompleta | apareceram na revisão do card que escreveu o arquivo, sem custo de dimensão e sem claim dependendo delas | uma passagem de redação; a primeira é reversível por deleção | não |
| **6** | A cópia das regras globais que o dono carrega fora do repositório não tem guarda executável | nenhum teste do repositório pode ler um arquivo fora dele | um verificador com acesso ao caminho externo, ou a decisão de que essa cópia é sincronizada em vez de editada | não hoje — medido em `0` ocorrências da forma antiga; é a metade não trancada do ato |
| **7** | A série de custo de sessões de planejamento tem **uma** linha, e ela é anterior à régua nova | não havia o que medir | ao menos duas sessões posteriores registradas na telemetria, para a série ganhar dispersão | não. Está declarada em `docs/planner-spec.md` §7 e §10, sem número estimado |

---

## O estado, sem enfeite

O plano entregou **dez cards, todos `done`**, contra as seis operações do seu modelo — sete de
autoria e três corretivos nascidos durante a execução e somados às operações que reparam. Nenhum
card foi cancelado e nenhuma revisão apontou dimensão bloqueante: sete fecharam em 100% e três com
ressalva (88%, 94% e 83%), as três por defeito de **autoria de card**, nunca por defeito de entrega.
Os três instrumentos de fechamento saem limpos hoje: `backlog.py check` exit `0`, `modelo.py check`
exit `0` com `6 operações, 3 objetos, 7 propriedades, 10 tarefas, versão 4`, e `277 passed` na suíte.

O que o repositório ganhou de durável: a régua de dimensionamento perdeu os dois números e ganhou
três critérios; a unidade de trabalho passou a ser definida pelo modelo em todas as residências de
doutrina viva — as quatro ocorrências remanescentes da forma antiga são registro datado, preservado
de propósito; a sessão de planejamento ganhou uma saída que termina **sem plano**, de modo que a
decomposição só começa com o modelo na árvore; e a figura de quem planeja ganhou descrição pública
própria, de 217 linhas, que nomeia nove perguntas em aberto em vez de respondê-las.

Ficaram **sete pendências**. Quatro delas (as de nº 1, 2, 3 e 6) **têm efeito fora deste plano**:
as três emendas à régua de autoria de card e a correção da guarda de invariante valem para todo
plano futuro do framework e estão com o texto pronto, aguardando o tíquete; a defasagem entre a
doutrina e os instrumentos do loop encarece toda revisão enquanto durar; e a cópia das regras globais
que carrega em toda sessão de trabalho está correta hoje sem nada que a mantenha correta amanhã.
As outras três são locais a este plano e nenhuma bloqueia o veredito.

O mais caro que esta execução produziu não foi código: foi a demonstração, com seis autores
distintos e nove casos em cadeia, de que **a régua de autoria de card do projeto não alcança a classe
de defeito que mais apareceu**. Essa demonstração está no plano, e a emenda que a fecha está
redigida — falta aplicá-la onde a régua mora.
