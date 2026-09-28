---
name: redacao-doc
description: Redação de documento publicado — elimina narrativa de proveniência ("historinhas"), citação de interlocutor e ID de processo do corpo de qualquer doc lido por quem não participou da conversa que o gerou. Usar ao autorar, reescrever ou revisar README, doc de arquitetura, doc de governança ou qualquer artefato destinado a leitor externo.
---

# redacao-doc — o documento descreve o objeto, não a sua própria gestação

## Gatilho

Toda autoria, reescrita ou revisão de documento da classe **publicado** (ver §5). Obrigatória antes
de dar qualquer doc dessa classe como pronto. Não se aplica a registro de obra (§5, classe
**registro**), onde narrar é a função. Mensagem de conversa ao dono não é documento publicado:
segue *Mensagem legível ao dono* (`GOVERNANCA.md` §4.2) e a skill `mensagem-ao-dono`.

## 1. A regra

Um documento publicado responde **o que é**, **como se usa** e **quais são os limites**. A própria
gestação do documento mora no registro (§4).

O teste, aplicável frase a frase:

> **Teste do leitor externo** — o leitor nunca participou de nenhuma conversa sobre este projeto,
> não sabe quem são os interlocutores e não vai procurar nenhum artefato interno. A frase entrega a
> ele algo que muda o que ele entende ou faz? Se ela só entrega *proveniência* — quem pediu, quando
> foi decidido, que episódio motivou, qual tarefa mediu —, ela **sai**.

Frase que não passa no teste não é encurtada: é removida. Reescrever uma historinha em menos
palavras continua sendo historinha.

## 2. Os vícios nomeados

| # | Vício | Marca | Ação |
|---|---|---|---|
| V1 | **Proveniência** | "o caso que motivou", "nasceu de", "a evidência é do próprio repositório", "foi identificado quando" | remover |
| V2 | **Interlocutor** | pessoa como **narrador ou testemunha de um episódio**: "o dono detectou", "o usuário pediu", "por pedido do cliente", "foi decidido em" | remover; se a regra é real, enuncie a regra |
| V3 | **ID de processo** | `T3`, `V2I-T7`, `Estágio 5`, `SPRINT-*`, `P-0730`, `TK-04`, "a tarefa que mediu" | remover do corpo publicado |
| V4 | **Anúncio de estrutura** | "nesta seção veremos", "cada seção responde três coisas", "a seguir será explicado" | remover; a estrutura se mostra sozinha |
| V5 | **Autojustificação** | o documento argumentando a própria importância, ou defendendo a sua existência | remover; entregar conteúdo é o argumento |
| V6 | **Anedota** | caso concreto com personagem e data, usado para ilustrar | trocar por exemplo genérico e reproduzível, ou remover |
| V7 | **Datação viva** | "desde 2026-08-05", "recentemente", "até então", "passou a ser", "deixou de" | reescrever no presente do estado atual |
| V8 | **Dívida de processo** | "dívida registrada", "colisão ainda aberta", "pendente de ratificação" | mover para o tracker; no doc fica só a limitação, sem o processo |
| V9 | **Negar-afirmar** | a frase nega para depois afirmar: "não é X, é Y", "não basta X; o que vale é Y", "X, não Y", "mais do que X, é Y", "em vez de X, faz Y", "não se trata de X, e sim de Y" | manter só a afirmação |
| V10 | **Pessoa gramatical** | primeira ou segunda pessoa: "nós", "nosso", "no nosso caso", "você", "o seu projeto", "veja", "repare" | terceira pessoa; imperativo impessoal quando a frase é instrução |

### Antes → depois

**V1 + V2 + V3**

- ✗ *"Cada seção declara a sua fonte da verdade, e o caso que motivou essa forma está registrado: ao
  descrever de memória o procedimento, o dono o definiu como uma pilha FIFO, quando a implementação
  real é outra. O conceito estava certo e a prática, irreconhecível."*
- ✓ *"Cada seção declara a sua fonte da verdade. O acordo vale na forma que tomou no repositório."*

**V4**

- ✗ *"Por isso cada procedimento aqui responde três coisas na mesma seção: o que é, por que foi
  adotado (a evidência ou o episódio que o produziu) e onde o gerente intervém."*
- ✓ (nada — as seções já fazem isso; anunciar o formato consome a atenção que o conteúdo precisa)

**V7**

- ✗ *"O guarda de conformance deixou de rodar em cada commit e passou a rodar só no fechamento
  da tarefa."*
- ✓ *"O guarda de conformance roda no fechamento da tarefa."*

**V6**

- ✗ *"Em julho o espelho divergiu do disco por três versões seguidas, o que levou à criação do
  guarda."*
- ✓ *"O guarda falha quando o documento diverge do disco. O alcance dele é estrutural."*

### Forma da frase (V9, V10)

Toda frase é **afirmativa, no presente do indicativo**; instrução vai no **imperativo impessoal**. A
negação tem um uso só: **enunciar proibição ou limite**.

Negação que fica — proibição e limite carregam informação própria:

- *"O executor não decide, não pergunta ao dono e não muda a rota."*
- *"Nenhuma tarefa fecha sem aceite do dono."*
- *"O piso nunca desce sem ato registrado do dono."*

Negação que sai — o "não X" existe só para dar contraste ao "Y" que vem depois:

| ✗ | ✓ |
|---|---|
| *"Ser contrato não o torna autoridade. Cada seção declara a sua fonte da verdade."* | *"A autoridade de cada seção é a fonte da verdade declarada na primeira linha."* |
| *"Custo é o terceiro eixo, e é restrição de projeto, não razão de ser."* | *"Custo é o terceiro eixo: restrição de projeto."* |
| *"Fundamentos pares, não alternativas."* | *"Fundamentos pares."* |
| *"O teto é alarme, não controle."* | *"O teto é alarme."* |
| *"Herdado em vez de recriado."* | *"Herdado."* |

**Teste do apagamento:** apague a parte negada e leia o que sobrou. Frase que perde informação
enunciava um limite e fica. Frase que sobrevive idêntica, só mais curta, era V9 — a versão curta
substitui a original.

Pessoa gramatical (V10): o texto descreve o objeto em terceira pessoa. O autor nunca aparece
("nós", "nosso", "aqui optamos") e o leitor nunca é interpelado ("você", "o seu projeto", "veja").
Instrução direta usa imperativo impessoal — *"consulte o índice antes de abrir o plano"* —, sem
pronome de tratamento.

## 3. Razão legítima × história

Nem toda justificativa é vício. O corte é **na forma**, não no fato de haver um porquê:

| Entra | Não entra |
|---|---|
| A razão enunciada como **fato ou restrição atemporal**: *"o guarda cobre estrutura, não sentido"* | A razão enunciada como **acontecimento**: *"o guarda cobre estrutura porque em julho..."* |
| Trade-off que muda a decisão do leitor: *"conformance roda em toda tarefa; a suíte completa só no fechamento, porque custa N minutos"* | Quem propôs o trade-off, quando, em que reunião ou tarefa |
| Limitação honesta do estado atual: *"o grau em que os plugins realizam DDD não foi auditado"* | O ticket, o plano ou a fase em que essa auditoria está agendada |
| Exemplo genérico que o leitor pode reproduzir | Episódio datado com personagens |

Critério de uma linha: **razão que sobreviveria em um projeto que nunca teve esta conversa, entra.**

### Papel ≠ interlocutor (a distinção que mais erra)

Quando o processo descrito **tem** um humano no circuito, nomear esse humano é definir um papel, e
papel é conteúdo. O vício V2 é a pessoa aparecendo como **narrador ou testemunha**, não a pessoa
aparecendo como **agente de uma regra no presente**.

| Entra (papel) | Não entra (interlocutor) |
|---|---|
| *"A decisão de publicar é do dono, nunca do agente."* | *"O dono decidiu publicar."* |
| *"Nenhuma tarefa fecha sem aceite do dono."* | *"O dono aceitou a versão anterior em agosto."* |
| *"O gerente intervém aqui: aprovar o plano."* | *"Foi o gerente quem apontou esse problema."* |

Teste: troque o nome do papel por *"qualquer pessoa nesse papel"*. Se a frase continua verdadeira, é
papel e fica. Se vira falsa ou vazia, era episódio e sai.

## 4. Residência do que foi cortado

Nada se perde — muda de arquivo. Antes de remover, confirme que o conteúdo já vive no destino; se
não vive, registre lá **primeiro**.

| Conteúdo cortado | Destino |
|---|---|
| Como se decidiu, quem decidiu, alternativas descartadas | plano `docs/plans/P-*.md` (decisões `DR-`/`DP-`) |
| O que mudou entre versões | `CHANGELOG.md` |
| Episódio, medição, veredito de tarefa | `docs/DIARIO_DE_OBRAS.md` / `docs/DIARIO_HISTORICO.md` |
| Dívida, pendência, colisão aberta | tíquete `TK-*` no índice do diário |
| Regra de fato nova, descoberta ao escrever | a fonte da verdade dela (`GOVERNANCA.md`, `ARQUITETURA_PANTONICA.md`), nunca o doc publicado |

O último item é a regra anti-duplicata: um doc publicado **nunca é a única fonte de uma regra**
(`docs/RESIDENCIA_DOUTRINA.md`).

## 5. Classes de documento

| Classe | Exemplos | Rigor |
|---|---|---|
| **Publicado** | `README.md`, `ARQUITETURA_PANTONICA.md`, `GOVERNANCA.md`, `docs/DOC_MAP.md`, doc de API | V1–V8 todos proibidos |
| **Seção histórica declarada** | uma seção do publicado cujo assunto *é* a mudança entre versões (ex.: "O que a versão X mudou"), e o `CHANGELOG.md` | V7 liberado (datar é o assunto); V1, V2, V3, V4, V5 continuam proibidos |
| **Registro** | diário de obras, planos, achados de execução, decision records | isento — narrar é a função |

Documento publicado **não cita** artefato da classe registro como fundamento no corpo. Ponteiro para
a fonte da verdade (doutrina, arquitetura) é obrigatório; ponteiro para o diário, para um plano ou
para uma tarefa é vício V3.

## 6. Varredura mecânica

Roda no doc antes de dá-lo por pronto. Match não é veredito automático — é linha a inspecionar.

```
Grep -i "o dono|o usuário|o cliente pediu|decisão do dono|por pedido|foi decidido"     # V2
Grep    "\bT[0-9]+[a-z]?\b|V2[A-Z]-T|Estágio [0-9]|SPRINT-|P-0[0-9]{3}|TK-[0-9]"       # V3
Grep    "[0-9]{4}-[0-9]{2}-[0-9]{2}"                                                    # V3/V7
Grep -i "nesta seção|neste documento|a seguir|como veremos|vamos ver|responde três"     # V4
Grep -i "o caso que|o episódio|a evidência é|nasceu de|surgiu quando|motivou a|levou à" # V1/V6
Grep -i "recentemente|até então|passou a |deixou de |antes disso|desde então|hoje o "   # V7
Grep -i "dívida|pendente de|ainda aberta|colisão|a ratificar"                           # V8
Grep -i "não é |não são |não basta|não se trata|, não |; não | e não |em vez de|mas sim|e sim|o que vale|mais do que"  # V9
Grep -i "\bnós\b|\bnoss[ao]|\bvocê|\bseu projeto|\bvamos |\bveja |\brepare "            # V10
```

**Piso de aceite:** zero ocorrências de V2, V3, V4 e V10 no corpo publicado. V9 sobrevive só onde a
negação enuncia proibição ou limite — toda outra ocorrência cai no teste do apagamento (§2). V1, V5,
V6, V7 e V8 admitem exceção só quando a linha passa no teste do §3, e a exceção é justificada no
fechamento da tarefa, fora do documento.

## 7. Procedimento

**Reescrita de documento existente** (o caso comum, e o mais perigoso: editar frase a frase preserva
o vício porque preserva a estrutura que ele criou):

1. Rode a varredura do §6 e conte as ocorrências por vício. Esse número é o baseline do aceite.
2. **Descarte o preâmbulo inteiro** e reescreva-o do zero. Preâmbulo é onde a narrativa se instala:
   saneá-lo por edição quase sempre falha.
3. Seção a seção: leia a seção completa, identifique **a afirmação que ela existe para fazer**,
   reescreva a partir dela. Não parta do texto antigo — parta da afirmação.
4. Corte antes de polir. Um documento sem historinha fica visivelmente menor; se o tamanho não caiu,
   o vício foi reescrito, não removido.
5. Passe o teste do apagamento (§2) em cada negação sobrevivente. V9 é vício de frase, e sobrevive a
   uma reescrita de seção inteira: ele se remove uma frase por vez, depois do corte estrutural.
6. Rode a varredura de novo. Toda ocorrência restante ou é exceção justificada pelo §3, ou fica.
7. Rode o guarda estrutural do doc, se houver (`.claude/checks/*.ps1`).

**Autoria nova:** escreva o corpo primeiro e o preâmbulo por último — preâmbulo escrito antes do
corpo vira declaração de intenções, que é V4 e V5 juntos.

## 8. Fechamento

O registro da tarefa (diário) reporta: contagem por vício antes → depois, variação de tamanho do
documento, e a lista de exceções mantidas com a justificativa do §3. O texto removido que ainda não
tinha residência (§4) é reportado como movido, com o destino nomeado.
