---
name: checar-versao-kit
description: Resolve a versão local do kit agêntico e, enquanto o framework estiver com a versão congelada em 0.0.0 (GOVERNANCA.md §10), reporta "congelada — nada a comparar" sem tocar a rede. Fora do congelamento, compara com a versão publicada no hub PantonicApp sem nunca atualizar sozinho, em três modos de resolução (consumidor, hub, não-instalado). Nos dois regimes arma o gatilho de revisão da doutrina (GOVERNANCA.md §7.1), que fica pendente quando existe plano fechado como done no índice do diário sem rodada de revisão registrada. Usar no momento de criar/registrar um plano novo (chamada pela skill diario-de-obras, operação "Registrar plano").
---

# checar-versao-kit — checagem anti-drift do kit agêntico

Operacional de `GOVERNANCA.md` §10 no hub (`PantonicApp`) — a doutrina mora lá; esta skill é o
procedimento que a executa. Em caso de dúvida sobre a regra, §10 é a fonte, não este arquivo.

## Quando roda

Na criação/registro de todo plano novo (skill `diario-de-obras`, operação "1. Registrar plano").
Esse é o único gatilho de invocação — não roda a cada turno, nem a cada tarefa, só quando um plano
é criado. Uma vez invocada, executa **duas** checagens independentes: a de versão (passos 1-3
abaixo) e a de revisão da doutrina (última seção); as duas compartilham só o momento de invocação,
não mais a leitura de versão. Sob congelamento, a primeira para no passo 1 ("Congelamento
(curto-circuito)" abaixo) e a segunda roda assim mesmo.

## Procedimento

### 1. Resolver a versão local (três modos, nesta ordem)

A skill decide pelo que existe na árvore do repo onde o plano está sendo criado — nunca assume
que o repo é um consumidor:

1. **Existe `.claude/kit/KIT_VERSION`** → **modo consumidor**. É essa a versão local; segue para
   o passo 2.
2. **Não existe `.claude/kit/`, mas existe `.claude/KIT_VERSION`** → **modo hub**: este repo *é*
   a fonte do kit, não há o que atualizar. Reporta "hub canônico — nada a comparar" e, se a rede
   permitir, roda mesmo assim a checagem remota do passo 2 só para avisar se a tag mais recente
   publicada não corresponde ao `.claude/KIT_VERSION` local (sinal de que alguém mudou o kit e
   esqueceu de republicar). Esse aviso não é o fluxo "divergentes" do passo 3 — é um alerta de
   "republicação pendente", e mesmo com o aviso a skill não atualiza nada (não há para onde
   atualizar: este repo já é o hub).
   O modo hub não é hipótese remota: o gatilho da regra é a criação de um plano, e os planos desta
   iniciativa nascem no próprio `PantonicApp` — logo este modo é esperado, não excepcional.
3. **Nenhum dos dois existe** → **"kit não instalado"**, segue em silêncio (sem checagem remota,
   sem bloquear a criação do plano).

**Congelamento (curto-circuito).** Se a versão local resolvida for `0.0.0`, o framework está em
desenvolvimento pré-lançamento (`GOVERNANCA.md` §10, bloco "Congelamento pré-lançamento"): reportar
`versão congelada em 0.0.0 — nada a comparar`, **pular os passos 2 e 3** (nenhuma chamada de rede
acontece) e **seguir direto para o gatilho de revisão da doutrina**, que com a `DE-8` não depende de
versão e roda igual nos dois regimes. A skill **não** encerra aqui.

### 2. Checagem remota (só nos modos consumidor/hub — 1 chamada de rede, sem fetch, sem tocar a árvore de trabalho)

```
git ls-remote --tags https://github.com/PantaTheDoggo/PantonicApp.git "kit-v*"
```

### 3. Comparar

Comparar a tag mais alta retornada (`kit-v<versão>`) com a versão local resolvida no passo 1
(`.claude/kit/KIT_VERSION` no modo consumidor, `.claude/KIT_VERSION` no modo hub). Quando as duas
divergem, extrair o componente MAJOR de cada uma (`M.x.y` → `M`) — é o que decide entre os dois
ramos de divergência abaixo, padrão de `BM-19§D10` (CLI v1.x consome só templates v1.x.x):
consumidor com kit `M.x` consome doutrina `M.x`.

## Os resultados possíveis

- **Versão congelada (`0.0.0`)** → reporta "congelada — nada a comparar", sem rede e sem pergunta
  ao dono, e segue para o gatilho de revisão.
- **Versões iguais** → segue em silêncio, sem gastar turno do dono.
- **Divergentes em MINOR/PATCH** (mesmo MAJOR) → reporta: versão local, versão remota, e a
  pergunta *"atualizar agora ou postergar?"*. Registra a resposta do dono no plano que está sendo
  criado. **Nunca atualiza sozinho.**
- **Divergentes em MAJOR** → não é tratada como divergência comum: reporta como **incompatível**
  (versão local, versão remota, MAJOR local ≠ MAJOR remoto) e **para** — sem a pergunta de
  "atualizar agora ou postergar", porque não é uma atualização de rotina. A regra do §10(a) segue
  intacta: o agente **nunca atualiza sozinho**; decidir como prosseguir (inclusive migrar) é do
  dono.
- **Sem rede / remote inacessível** → reporta "não verificado" e segue. Falha de rede não
  bloqueia o trabalho nem vira silêncio — a incerteza é reportada.

## Gatilho de revisão da doutrina (`GOVERNANCA.md` §7.1)

A porta de saída de um guardrail está pendurada no **fechamento de um plano** (status `done` no
índice do diário) — e esta skill é quem a arma, porque roda no momento certo (criação de plano). A
doutrina mora em §7.1; aqui está só o procedimento. Roda **sempre**, congelada ou não.

1. Ler, em `GOVERNANCA.md` §7.1, a última rodada registrada e o plano que ela cobre (Grep por
   `Registro das rodadas`, sem ler a seção inteira).
2. Ler o índice de `docs/DIARIO_DE_OBRAS.md` e listar os planos com status `done` (Grep por
   `| done |` na tabela do índice).
3. **Existe plano `done` fechado a partir do marco zero (`2026-08-01`) que não conste de nenhuma
   rodada registrada** → a revisão está **pendente**. Reportar ao dono: o plano que disparou, a
   última rodada registrada e quantas guardrails de §7 entram em escopo (as que já constavam na
   penúltima rodada). **Não executar a revisão aqui** — ela é uma tarefa nomeada, com registro
   próprio no diário; esta skill só a torna visível no momento em que há material para julgar.
4. **Nenhum plano `done` fora das rodadas registradas** → segue em silêncio.

Um plano pode fechar sem que outro seja criado logo depois; nesse caso o aviso aparece na próxima
criação de plano. O atraso é aceito por desenho — o gatilho troca pontualidade por custo zero de
cerimônia (§7.1, "nunca em calendário").

## Proibição

**Nunca auto-atualizar o kit, sob nenhuma circunstância — nem "se for só patch".** Atualização é
sempre por comando explícito do dono. Não existe exceção de severidade: um bump patch-level segue
exatamente a mesma regra que um bump major. Esta skill só detecta e reporta divergência; agir
sobre ela é decisão do dono, nunca do agente.
