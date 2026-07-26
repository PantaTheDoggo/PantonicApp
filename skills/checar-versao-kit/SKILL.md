---
name: checar-versao-kit
description: Checa se a versão local do kit agêntico (.claude/kit/KIT_VERSION) diverge da versão publicada no hub PantonicApp, sem nunca atualizar sozinho. Usar no momento de criar/registrar um plano novo (chamada pela skill diario-de-obras, operação "Registrar plano").
---

# checar-versao-kit — checagem anti-drift do kit agêntico

Operacional de `GOVERNANCA.md` §10 no hub (`PantonicApp`) — a doutrina mora lá; esta skill é o
procedimento que a executa. Em caso de dúvida sobre a regra, §10 é a fonte, não este arquivo.

## Quando roda

Na criação/registro de todo plano novo (skill `diario-de-obras`, operação "1. Registrar plano").
Esse é o único gatilho — não roda a cada turno, nem a cada tarefa, só quando um plano é criado.

## Procedimento

1. Ler a versão local materializada em `.claude/kit/KIT_VERSION` do projeto consumidor.
2. Rodar a checagem remota (1 chamada de rede, sem fetch, sem tocar a árvore de trabalho):

   ```
   git ls-remote --tags https://github.com/PantaTheDoggo/PantonicApp.git "kit-v*"
   ```

3. Comparar a tag mais alta retornada (`kit-v<versão>`) com o conteúdo de
   `.claude/kit/KIT_VERSION`.

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
