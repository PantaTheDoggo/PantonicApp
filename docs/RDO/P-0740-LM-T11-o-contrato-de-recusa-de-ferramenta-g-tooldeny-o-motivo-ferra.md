# RDO — P-0740 · LM-T11

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T11` — O contrato de recusa de ferramenta: `G-TOOLDENY`, o motivo `ferramenta` e o fim da exceção do `AE-44`
**Modelo:** Opus · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — fechar o **contrato de recusa de ferramenta**: ferramenta negada ao executor deixa de ser improviso ou silêncio e passa a ser um desfecho **nomeado, devolvido e roteado**. Com ele, a exceção do `AE-44` fecha e a `GOVERNANCA.md` §3 volta a valer sem ressalva.

**Arquivos-alvo:** - `GOVERNANCA.md` - `README.md` - `.claude/skills/scrum-master/SKILL.md` - `.claude/agents/pantonic-executor.md` - `CHANGELOG.md`

**Verificação:** (forma normativa publicada pela `LM-T5`; todo valor abaixo foi rodado na autoria, 2026-09-19 — `DM-12`, `DM-24`) 1. ``` pwsh -NoProfile -Command ".claude/checks/check-readme.ps1" ``` → **exit 0**, anunciando **20 guardrail(s)**. **Medido antes: 19 guardrail(s)**. É o invariante de contagem do `AE-12`: a checagem 4 confronta a lista de `GOVERNANCA.md` §7 com a tabela do `README.md`, e sai vermelha se só uma das duas receber a guarda nova. 2. ``` pwsh -NoProfile -Command "(Select-String -Path GOVERNANCA.md -Pattern '^20\. \*\*G-TOOLDENY' | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. (A guarda existe na doutrina, no número que a sucede.) 3. ``` pwsh -NoProfile -Command "(Select-String -Path README.md -Pattern '^\| 20 \| .G-TOOLDENY.' | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. (E na tabela que o instrumento conta.) 4. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md,.claude/agents/pantonic-executor.md -Pattern '<dependencia|premissa>' -SimpleMatch | Measure-Object).Count" ``` → **0**. **Medido antes: 1**. (O domínio de dois termos some das superfícies — aceite de coerência do módulo.) 5. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md,.claude/agents/pantonic-executor.md -Pattern '<dependencia|premissa|ferramenta>' -SimpleMatch | Measure-Object).Count" ``` → **2**. **Medido antes: 0**. (E o de três entra nas **duas** superfícies. Sai **2**, e não 1, porque cada superfície enuncia o domínio por conta própria e fechar só uma deixaria o executor e o loop falando línguas diferentes.) 6. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern '^\| .A3c. \|' | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. (A regra de roteamento existe: sem ela o motivo novo chega ao loop e cai em *retorno inválido*.) 7. ``` pwsh -NoProfile -Command "(Select-String -Path CHANGELOG.md -Pattern 'recusa de ferramenta ao executor deixa de ser improviso' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. 8. ``` python -m pytest tests/ -q ``` → verde, **sem reduzir** o total re-medido no despacho (`DM-23`): esta tarefa não acrescenta teste, e é a suíte de conformance que tranca doutrina. **Medido antes: exit 0** — veredito **invariante** ao que outros cards entregam, que é o que os critérios (x)/(xiii) pedem e o que o `card_check` sabe conferir. Referência **datada**, e não aceite: `197 passed` em 2026-09-19 (`ESC-28`); a mesma baseline, publicada como constante, envelheceu três vezes nesta janela (187, 191, 197).

**Pronto quando:** as oito linhas de `Verificação` saem nos valores declarados; a guarda existe nas duas superfícies que a contam; o domínio de três termos é o único enunciado; a `A3c` roteia o motivo novo; a linha do `CHANGELOG.md` está lá; e o literal do executor foi aplicado **pelo instrumento**, não por edição direta.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` · 2026-09-19 — segunda tarefa da fila da próxima janela (`DM-50`).
- **Esforço:** medium
- **Depende de:** `LM-T10` — **duas** vezes, e as duas são estruturais: (1) esta tarefa edita `.claude/agents/pantonic-executor.md`, que é a superfície recusada, e o único caminho decidido para editá-la é o instrumento que a `LM-T10` entrega; (2) se a `LM-T10` fechar `blocked` pela contingência 1 dela, a rota da `DM-50` caiu e **este card não se despacha como está** — volta ao consultor com o dado da recusa.
- **Produto do módulo:** (a) `G-TOOLDENY` publicada como item **20** de `GOVERNANCA.md` §7, com a linha correspondente na tabela *Os guardrails* do `README.md` **no mesmo ato** — a lista e a frase que a conta fecham juntas (`DM-18` (i)), e é o `check-readme.ps1` que reprova se divergirem; (b) o motivo **`ferramenta`** no domínio fechado do retorno do executor, nas duas superfícies que o enunciam; (c) a regra de roteamento **`A3c`** na tabela do `scrum-master`; (d) o encerramento explícito da exceção do `AE-44`; (e) a linha em `CHANGELOG.md`.
- **Coerência do módulo (aceite de `DM-3`):** depois desta tarefa, **nenhuma** das quatro superfícies enuncia o domínio antigo de dois termos. A varredura é parte da entrega, e a `Verificação` 4 a mede.
- **Restrições desta tarefa:** o literal 6 é aplicado **rodando o instrumento da `LM-T10`**, nunca por `Edit` ou `Write` — é a segunda prova da rota da `DM-50`, agora em produção e não em fixture. A exceção do `AE-44` **não** se reescreve no achado: ela fica onde está, como registro do que foi feito, e o que esta tarefa publica é o seu **encerramento**.
- **Não fazer:** não mexer em `.claude/tools/agentdef.py` nem nos testes dele (são da `LM-T10`); não estender `rdo.py`, `backlog.py`, `review_evidence.py` nem `card_check.py` — **medido na autoria: nenhum deles lê o domínio de `motivo`**, que vive só em prosa nas duas superfícies, e o `--razao` do `backlog.py` é texto livre; não alterar `description`, `model` ou `name` de agente nenhum; não regenerar `.claude/README.md` (a `description` não muda aqui); não commitar.
- **Contingências:** 1. se o instrumento da `LM-T10` recusar o literal 6 por não-unicidade ou ausência → parar e sinalizar `blocked` razão `premissa`, colando a saída do instrumento: o arquivo mudou entre a autoria e o despacho, e quem reconcilia o literal é o consultor; 2. se a `Verificação` 1 sair com número de guardas diferente de **20** → parar e sinalizar `blocked` razão `premissa`: a lista e a tabela divergiram, e é exatamente o invariante que esta linha existe para pegar; 3. se o `Bash` que roda o instrumento for recusado ao executor → devolver `blocked motivo=premissa` com a linha literal da recusa — o motivo `ferramenta` ainda **não** existe no domínio quando esta tarefa começa, e é ela que o cria.

## Execução

**Consumo:** 13 tool uses, 60.7 k tokens, 174.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: a frase de contagem do README ('Sete regras falham como teste executavel, doze dependem de gate de review ou de instrucao de agente') nao foi tocada - o card nao a prescreve e o check-readme.ps1 nao a le -, e com a guarda 20 ela passa a contar 12 onde ha 13
laudo: Regularizar, em um card, as duas frases de contagem do README §Os guardrails (726 e 753), estender o check-readme.ps1 para le-las, e citar a A3c nas tres enumeracoes de regras do scrum-master/SKILL.md (linhas 134, 252 e a secao de parada) - nenhuma prescrita por este card, nenhuma coberta pelas oito linhas de Verificacao.

## Laudo

**Veredito:** ressalva

**Percentual:** 88%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

A tarefa saiu por 13 tool-uses / 60.7k / 174s, a mais barata da janela, e a causa e metodologica, nao de tamanho: o executor nao redigitou literal nenhum. Fatiou os sete blocos do card por NUMERO DE LINHA num unico heredoc Python (lit(4575,4584), lit(4589,4589), ...), com dedent de 2 e um assert de que nenhuma cerca de codigo entrou na fatia, e so entao escreveu. Isso compra duas coisas de uma vez: a transcricao fica literal POR CONSTRUCAO, nao por conferencia, e as quatro escritas cabem num turno so. Vale como tecnica canonica de card de classe redacao com bloco de Texto literal. Segundo registro: o achado (i) do AE-48 - instrumento e Edit deixam o repositorio byte a byte identico - foi resolvido aqui pelo par registro-de-chamadas + mtime, e o par funcionou com folga: a sessao do executor tem 13 tool-uses, TODOS Read ou Bash, nenhum Edit/Write em lugar nenhum, e o mtime de pantonic-executor.md (18:50:28.815) casa com a chamada do agentdef.py (18:50:27) e fica 16s depois dos outros quatro alvos (18:50:12.74x). E uma prova barata e repetivel; o que ela custa e o transcript estar acessivel ao reviewer.

## Fechamento

**Desdobramento:** aprovado com ressalva
