---
name: checar-versao-kit
description: Checa se a versão local do kit agêntico diverge da versão publicada no hub PantonicApp, sem nunca atualizar sozinho. Resolve a versão local em três modos — consumidor (.claude/kit/KIT_VERSION), hub (.claude/KIT_VERSION sem .claude/kit/) e não-instalado. Usar no momento de criar/registrar um plano novo (chamada pela skill diario-de-obras, operação "Registrar plano").
---

# checar-versao-kit — checagem anti-drift do kit agêntico

Operacional de `GOVERNANCA.md` §10 no hub (`PantonicApp`) — a doutrina mora lá; esta skill é o
procedimento que a executa. Em caso de dúvida sobre a regra, §10 é a fonte, não este arquivo.

## Quando roda

Na criação/registro de todo plano novo (skill `diario-de-obras`, operação "1. Registrar plano").
Esse é o único gatilho — não roda a cada turno, nem a cada tarefa, só quando um plano é criado.

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

## Proibição

**Nunca auto-atualizar o kit, sob nenhuma circunstância — nem "se for só patch".** Atualização é
sempre por comando explícito do dono. Não existe exceção de severidade: um bump patch-level segue
exatamente a mesma regra que um bump major. Esta skill só detecta e reporta divergência; agir
sobre ela é decisão do dono, nunca do agente.
