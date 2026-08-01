---
name: checar-versao-kit
description: Checa se a versão local do kit agêntico diverge da versão publicada no hub PantonicApp, sem nunca atualizar sozinho, e arma o gatilho de revisão da doutrina (GOVERNANCA.md §7.1) quando o MINOR avançou desde a última rodada. Resolve a versão local em três modos — consumidor (.claude/kit/KIT_VERSION), hub (.claude/KIT_VERSION sem .claude/kit/) e não-instalado. Usar no momento de criar/registrar um plano novo (chamada pela skill diario-de-obras, operação "Registrar plano").
---

# checar-versao-kit — checagem anti-drift do kit agêntico

Operacional de `GOVERNANCA.md` §10 no hub (`PantonicApp`) — a doutrina mora lá; esta skill é o
procedimento que a executa. Em caso de dúvida sobre a regra, §10 é a fonte, não este arquivo.

## Quando roda

Na criação/registro de todo plano novo (skill `diario-de-obras`, operação "1. Registrar plano").
Esse é o único gatilho de invocação — não roda a cada turno, nem a cada tarefa, só quando um plano
é criado. Uma vez invocada, executa **duas** checagens independentes: a de versão (passos 1-3
abaixo) e a de revisão da doutrina (última seção), que aproveita a mesma leitura de versão.

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

### 2. Checagem remota (só nos modos consumidor/hub — 1 chamada de rede, sem fetch, sem tocar a árvore de trabalho)

```
git ls-remote --tags https://github.com/PantaTheDoggo/PantonicApp.git "kit-v*"
```

### 3. Comparar

Comparar a tag mais alta retornada (`kit-v<versão>`) com a versão local resolvida no passo 1
(`.claude/kit/KIT_VERSION` no modo consumidor, `.claude/KIT_VERSION` no modo hub).

## Os três resultados possíveis

- **Versões iguais** → segue em silêncio, sem gastar turno do dono.
- **Divergentes** → reporta: versão local, versão remota, e a pergunta *"atualizar agora ou
  postergar?"*. Registra a resposta do dono no plano que está sendo criado. **Nunca atualiza
  sozinho.**
- **Sem rede / remote inacessível** → reporta "não verificado" e segue. Falha de rede não
  bloqueia o trabalho nem vira silêncio — a incerteza é reportada.

## Gatilho de revisão da doutrina (`GOVERNANCA.md` §7.1)

A porta de saída de um guardrail está pendurada no **fechamento de MINOR do kit** — e esta skill é
quem a arma, porque já leu a versão local no passo 1. A doutrina mora em §7.1; aqui está só o
procedimento.

Rodar **depois** da checagem de versão, em qualquer modo exceto "kit não instalado":

1. Ler o MINOR corrente da versão local resolvida no passo 1 (`X.Y.Z` → `Y`).
2. Ler a **última revisão registrada** na lista "Registro das rodadas" de `GOVERNANCA.md` §7.1
   (Grep por `Registro das rodadas`, sem ler a seção inteira).
3. **MINOR corrente > MINOR da última revisão** → a revisão está **pendente**. Reportar ao dono:
   versão da última rodada, versão corrente, e quantas guardrails de §7 entram em escopo
   (introduzidas em MINOR ≤ corrente − 2). **Não executar a revisão aqui** — ela é uma tarefa
   nomeada, com registro próprio no diário; esta skill só a torna visível no momento em que há
   material para julgar.
4. **MINOR igual** → segue em silêncio, como no caso "versões iguais" da checagem de versão.

Um MINOR pode fechar sem que nenhum plano novo seja criado logo depois; nesse caso o aviso aparece
na próxima criação de plano. O atraso é aceito por desenho — o gatilho troca pontualidade por
custo zero de cerimônia (§7.1, "nunca em calendário").

## Proibição

**Nunca auto-atualizar o kit, sob nenhuma circunstância — nem "se for só patch".** Atualização é
sempre por comando explícito do dono. Não existe exceção de severidade: um bump patch-level segue
exatamente a mesma regra que um bump major. Esta skill só detecta e reporta divergência; agir
sobre ela é decisão do dono, nunca do agente.
