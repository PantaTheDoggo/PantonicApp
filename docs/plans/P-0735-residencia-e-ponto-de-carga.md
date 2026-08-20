# P-0735 — Residência e ponto de carga: o pacote materializa o que a doutrina invoca

**Data:** 2026-08-15 · **Origem:** `TK-45` (owner-gated, decidido no mesmo dia) · **Status:** `ready`
· **Prefixo das tarefas no diário:** `RPC-T<n>` · **Checagem de versão do kit:** modo hub —
**congelada em `0.0.0`** (`DE-7`), comparação local × remoto suspensa, nada a comparar.

## 0. O problema

O framework depende de artefatos que não viajam nele. **Treze** artefatos de conteúdo do framework
vivem só em `~/.claude/`, medidos em 2026-08-15:

| Grupo | Itens | Onde vivem hoje |
|---|---|---|
| Hooks registrados | `pytest_pretooluse.py`, `verbose_cmd_pretooluse.py`, `read_cap_pretooluse.py`, `modelo_por_fase_userpromptsubmit.py` | `~/.claude/hooks/` + registro em `~/.claude/settings.json` |
| Skills | `context-prep`, `doc-map`, `lean-test`, `memory-diet`, `onboard`, `test-tiers` | `~/.claude/skills/<nome>/SKILL.md` |
| Agente | `context-scout` | `~/.claude/agents/context-scout.md` |
| Docs de doutrina | `GOVERNANCA_MEMORIAS.md` (161 l), `RECOMENDACOES_CONSUMO_GLOBAL.md` (94 l) | `~/.claude/docs/` |

Mais o `~/.claude/CLAUDE.md` (156 linhas, 8 Regras, 7 delas apontando para o framework), que é a
doutrina sempre-ativa fora de projeto Pantonic.

Nenhum deles chega a consumidor algum, e a doutrina versionada **os invoca**: a skill `proximo-passo`
do kit prescreve `context-prep`/`context-scout`, e o hook global é o enforcement da disciplina de
coleta do `GOVERNANCA.md` §3. Pelo critério que a própria doutrina publicava — *"regra que só existe
no `~/.claude` do dono não é doutrina do framework"* — esses artefatos não são doutrina, e a doutrina
depende deles.

É a **5ª ocorrência medida da mesma classe**: `TK-01` (skill apontada para o global), `DR-B` de
`docs/RESIDENCIA_DOUTRINA.md` §5 (6 skills globais citadas pela doutrina, promoção adiada e nunca
aberta), `TK-21` (ratchet sem alvo), `TK-43` (hook num `settings.json` ignorado pelo git) e o
`permissions.deny` do guardrail 13 (`P-0734` `DP-R` §22.5).

**Raiz.** O teste de residência respondia *onde mora* com uma resposta só, fundindo dois eixos
independentes — **autoridade** (conteúdo do framework × da máquina do dono) e **ponto de carga**
(de onde o harness lê). Enquanto o ponto de carga é versionado, os eixos coincidem; quando o harness
impõe ponto de carga global ou não-versionado, a régua obrigava a escolher entre residência correta
e funcionar.

**Decisão do dono, ratificada em 2026-08-15 e fora de reabertura:** o pacote passa a materializar
também o `~/.claude`. Doutrina global, skills e agentes globais viram **projeção** de canônico
versionado. A régua nova já está publicada em `GOVERNANCA.md` §3.1 e conciliada em
`docs/RESIDENCIA_DOUTRINA.md` §8; este plano constrói o mecanismo e move os artefatos.

## 1. Decisões (fechadas no ato do planejamento)

Todas de planejamento. Nenhuma questão owner-gated pendente; nenhuma tarefa tem ponto de parada.

| Id | Decisão | Conteúdo |
|---|---|---|
| **`DL-1`** | Residência canônica por classe | Manifesto único em `.claude/projecoes.json`; materializador em `.claude/tools/materializar.py`; canônico do ponto de carga do usuário em `.claude/global/` (`CLAUDE.md`, `docs/`, `skills/`, `agents/`, `hooks/`). O canônico do ponto de carga do projeto já vive onde está (`.claude/tools/ocupacao.py` e as demais ferramentas do kit) |
| **`DL-2`** | Um materializador, dois alvos | O `hooks_sync.py` prescrito pela `T53` do `P-0734` **não nasce**: aquele desenho é o caso particular `--alvo projeto` deste. Nem `.claude/hooks/hooks.json` nasce — a declaração de hook é uma chave do manifesto único. Generalizar, não duplicar |
| **`DL-3`** | Local de máquina, declarado por exaustão | São locais de máquina, e a materialização os preserva intactos: `permissions.allow`, `additionalDirectories`, `model`, `effortLevel`, `switchModelsOnFlag`, `statusLine` e o script `statusline.py` que ela invoca. Tudo o mais que hoje está em `~/.claude/` e é conteúdo do framework passa a ser canônico |
| **`DL-4`** | Alcance do guarda | `kit_check.ps1 -Mode validate` valida o **canônico dos dois alvos** (leitura pura, segura em qualquer máquina); `-Mode check-drift` cobra a materialização **do alvo `projeto`**. O alvo `usuario` tem comando próprio (`materializar.py drift --alvo usuario`), fora da bateria de fechamento — cobrar no guarda a projeção de uma máquina alheia quebraria consumidor que não optou por ela |
| **`DL-5`** | O `~/.claude/CLAUDE.md` muda de residência, não de conteúdo | O texto vigente entra byte a byte em `.claude/global/CLAUDE.md`. Revisão do conteúdo item a item é matéria de `docs/RESIDENCIA_DOUTRINA.md` e não desta rodada; misturar as duas tornaria a mudança de residência irrevisável |
| **`DL-6`** | As skills e o agente globais ficam em `.claude/global/`, fora do load point de projeto | Promovê-los a `.claude/skills/`/`.claude/agents/` os ativaria em **todo** projeto Pantonic e duplicaria o nome com a projeção do usuário na mesma máquina. Efeito colateral desejado: a contagem do espelho (8 agentes, 11 skills) não muda, e `kit_check`/`check-readme.ps1`, que varrem `.claude/agents/*.md` e `.claude/skills/*/SKILL.md`, seguem íntegros sem alteração |
| **`DL-7`** | `permissions.deny` é canônico | O guardrail 13 é regra publicada, e a lista de subcomandos negados é o enforcement dela — cai na mesma invariante que o hook. Vira chave declarada do alvo `projeto`; `permissions.allow` e qualquer outra subchave de `permissions` ficam intocadas. Fecha a questão adjacente escalada em `P-0734` §22.5 |
| **`DL-8`** | Propagação: `DA-3` mantida | Hub primeiro, medir, depois propagar. `docs/CONSUMIDORES.md` registra **0/6** consumidores com `.claude/kit/`, então nenhuma exigência nova muda o estado de consumidor algum hoje. O alvo `usuario` é **opt-in**: só se materializa por comando explícito, nunca por efeito de sync. `sync-kit.ps1` não muda |
| **`DL-9`** | Rebase do `P-0734` | Classificação **(A)** da convenção de planos derivados: fato novo que muda o passo subsequente sem substituir a rota da iniciativa `EXECUCAO-AUTONOMA`. O `P-0734` vai para **`blocked`**, com `T53` e `T54` **canceladas por absorção**; destrava quando este plano fechar |
| **`DL-10`** *(2026-08-17 — decidida pelo dono sobre o `TK-47`, achado da `RPC-T4`)* | `apply` é byte-idempotente sob equivalência semântica | O primeiro `apply --alvo usuario` real reescreveu `~/.claude/settings.json` sem mudança semântica alguma, porque `write_settings` compara **texto** contra o `_dump` canônico e o arquivo do destino estava noutra formatação. **`apply` passa a não escrever quando o resultado é semanticamente igual ao que já está no destino** — preservar a formatação alheia é o comportamento correto de uma ferramenta opt-in que projeta na máquina de outro. Recusada a alternativa (aceitar a normalização e afrouxar o critério da `T5` para comparação semântica): manteria `apply` mexendo em arquivo que não precisava mudar e tiraria da `T5` o único sinal barato de que dispõe. **Fronteira explícita:** havendo mudança semântica real, a escrita continua reemitindo o arquivo inteiro no formato do `_dump`; escritor de JSON que preserva formatação alheia numa mudança real é outro problema e não entra aqui. Materializada pela `T10`, que precede a `T5` |

## 2. A régua nova (insumo, já publicada)

`GOVERNANCA.md` §3.1 — três classes (**canônico**, **ponto de carga**, **local de máquina**), a
**pergunta zero** antes das quatro (*isto é conteúdo ou ponto de carga?*), o `Prec-2` promovido a
**invariante** (*nada canônico mora só num ponto de carga*) e a precedência 2 passando a **canônico
vence projeção**. A afirmação de que hook não viaja saiu.

## 3. Invariante de execução (vale para todas as tarefas)

1. **Nenhum conteúdo é reescrito ao mudar de residência.** Promoção é cópia byte a byte do que está
   no ponto de carga para o canônico. Tarefa que precisar editar o texto promovido está fora do
   escopo dela.
2. **Nada fora do declarado é escrito ou removido.** Em `~/.claude/` vivem `projects/`,
   `file-history/`, `ide/`, `todos/` e memórias do dono: o materializador nunca toca caminho que o
   manifesto não declare, e **nunca remove arquivo** no destino.
3. **Fixture antes da máquina.** Todo comportamento novo é provado contra `tmp_path` com
   `--kit-root`/`--home` antes de qualquer execução contra o repositório ou o `~/.claude` reais.
4. **Sem bump e sem tag** (`DE-7`). A mudança canônica escreve linha no `CHANGELOG.md` sob
   `## [Não lançado]`.
5. **Nenhum guardrail novo.** O espelho permanece em **16 guardrails × 14 seções**.
6. **Bateria de fechamento:** `pwsh .claude/checks/kit_check.ps1 -Mode validate`,
   `pwsh .claude/checks/kit_check.ps1 -Mode check-drift`, `pwsh .claude/checks/check-readme.ps1`,
   `python .claude/checks/dead_code.py`, e `pytest` — os quatro primeiros em exit 0.
7. `.claude/skills/redacao-doc/SKILL.md` é normativa para todo texto publicado tocado aqui.

## 4. Tarefas

### T1 — Espelho: o `README.md` fala a régua das três classes [Opus · classe redacao · teto 30]
- **Objetivo:** o espelho deixa de afirmar o contrário da fonte da verdade. Executa **imediatamente**
  depois da publicação da régua nova: enquanto ele não roda, o `README.md` ensina o erro que o
  `TK-45` documenta.
- **Arquivos-alvo e a edição exata de cada um:**
  1. **`README.md` §12 "Memória e telemetria"**, parágrafo do teste de residência (começa em
     *"**Memória.** Só vira memória o fato durável não derivável"*, ~`:813-819`): o teste passa a ter
     a **pergunta zero** antes das quatro, na forma da fonte (*é ponto de carga ou configuração de
     quem opera a máquina? então não mora: recebe*). O destino da pergunta 1 deixa de ser "doutrina
     global do dono" solta e passa a ser **doutrina global canônica no kit, projetada em
     `~/.claude/CLAUDE.md`**.
  2. **`README.md` §12**, parágrafo *"A governança das memórias do harness… **não viaja** para o
     consumidor"* (~`:827-830`): a afirmação de não-viagem **cai**. O texto novo diz que a governança
     das memórias é doutrina global, canônica no kit e projetada no ponto de carga do usuário.
  3. **`README.md` §12**, parágrafo de precedência (~`:832-837`): a segunda regra deixa de ser
     "versionado vence não-versionado" e passa a **canônico vence projeção**, com a nota de que
     projeção não se edita no destino.
  4. **`README.md` §11 "Anatomia do kit"**, frase de abertura (`:741`): (a) o número de skills passa
     de "dez" para **onze** — o disco e a tabela da própria seção têm onze, e o guarda compara tabela
     × disco sem ler o número em prosa; (b) a frase passa a nomear, entre o que viaja, a **declaração
     de projeções** além de agentes, skills e verificadores.
  5. **`README.md` §11**, parágrafo novo logo depois da lista de verificadores (que termina em
     `:786`): nomeia `.claude/projecoes.json` como a declaração canônica das projeções,
     `.claude/tools/materializar.py` como o comando que as aplica e verifica, e `.claude/global/`
     como a residência canônica do que se projeta no ponto de carga do usuário.
  6. **`README.md` §11**, último parágrafo (`:800-805`), frase *"Skills instaladas fora do
     repositório, de uso pessoal, não fazem parte do kit e não viajam"*: reescrita para a régua nova
     — o que não faz parte do kit é **configuração de quem opera a máquina**; skill de conteúdo do
     framework é canônica no kit e se projeta no ponto de carga.
  7. **`README.md` §2**, frase de `:212` (*"fora do kit, porque o que não viaja no pacote distribuído
     não chega a consumidor nenhum"*): conciliar com a invariante — o que não chega a consumidor é o
     que fica **só** num ponto de carga, e a resposta é projetar, não excluir do pacote.
- **Cuidado.** As tabelas de agentes e de skills do §11 **não mudam**: as seis skills e o agente
  globais nascem em `.claude/global/` e não entram na contagem do espelho (`DL-6`). Nenhuma seção
  numerada nova; nenhuma linha de `> Fonte da verdade:` alterada.
- **Verificação:** `pwsh .claude/checks/check-readme.ps1` em exit 0; `Grep "não viaja"` em
  `README.md` → nenhuma ocorrência que afirme que conteúdo do framework não viaja.
- **Pronto quando:** um leitor que só tenha o `README.md` aplica a régua das três classes e chega à
  mesma resposta que o `GOVERNANCA.md` §3.1 daria.

### T2 — Manifesto de projeções, materializador e o ponto de carga do projeto [Sonnet · classe implementação padrão · teto 40]
- **Objetivo:** existe um canônico declarado para o que o harness lê, e um comando idempotente que o
  projeta. Nesta tarefa o alvo é só o **projeto** — a máquina do dono não é tocada.
- **Arquivos-alvo:**
  - `.claude/projecoes.json` — **novo**, a declaração canônica.
  - `.claude/tools/materializar.py` — **novo**, o materializador/verificador.
  - `tests/test_materializar.py` — **novo**.
  - `.claude/settings.json` — **não se edita à mão**: passa a ser produto de
    `python .claude/tools/materializar.py apply`.
- **Insumo a transcrever, não a inventar.** O `.claude/settings.json` do repositório é ignorado pelo
  git (`.gitignore:3`) e já existe nesta máquina com duas chaves de topo: `permissions.deny` (as 6
  entradas que o guardrail 13 exige) e `hooks` (o `PreToolUse` do proxy de ocupação, comando
  `python .claude/tools/ocupacao.py`). **Ler o arquivo e transcrever as duas para o manifesto sem
  alterar nenhum valor.** Nenhum hook novo e nenhuma entrada de deny nova nascem aqui.
- **Esquema do manifesto.** JSON, uma única chave de topo `alvos`, com um objeto por alvo:
  ```json
  {
    "alvos": {
      "projeto": {
        "settings": "settings.json",
        "raiz": null,
        "chaves": { "hooks": { }, "permissions.deny": [] },
        "arquivos": []
      },
      "usuario": {
        "settings": "{HOME_CLAUDE}/settings.json",
        "raiz": "{HOME_CLAUDE}",
        "chaves": { "hooks": { } },
        "arquivos": []
      }
    }
  }
  ```
  `chaves.hooks` usa o mesmo esquema que o harness lê dentro de `settings.json` (evento → lista de
  `{matcher?, hooks:[{type, command, timeout?, statusMessage?}]}`). Caminho de comando escrito por
  placeholder: **`{KIT_ROOT}`** (raiz do kit resolvida) e **`{HOME_CLAUDE}`** (o `~/.claude` do
  usuário corrente). O alvo `usuario` nasce **declarado e vazio** nesta tarefa — as `T3`..`T6` o
  preenchem.
- **Ancoragem — as duas topologias, resolvidas sem pergunta.** O script resolve a raiz do kit a
  partir do próprio caminho: no **hub** a raiz é `<repo>/.claude` e o destino do alvo `projeto` é
  `<raiz>/settings.json`; no **consumidor** a raiz é `<repo>/.claude/kit` e o destino é o
  `settings.json` do **pai**. Regra única que decide: se o diretório-raiz do kit se chama `kit`, o
  destino é o pai; senão, é ele mesmo. `{KIT_ROOT}` resolve para `.claude` ou `.claude/kit`,
  com separador POSIX em qualquer plataforma. `--kit-root <caminho>` e `--home <caminho>` sobrepõem
  a resolução — mesmo desenho de `-KitRoot` (`kit_check.ps1`) e `--root` (`dead_code.py`).
- **CLI — três subcomandos, nenhum interativo.** `apply`, `check` (valida o canônico, não olha a
  máquina) e `drift` (compara destino × canônico). Todos aceitam
  `--alvo projeto|usuario|todos` (**default `projeto`**), `--kit-root` e `--home`; todos saem 0 em
  sucesso e 1 em falha, imprimindo **uma linha por problema**, e toda mensagem de falha traz o
  comando de remédio.
- **Semântica do `apply` — o que ela nunca pode destruir.**
  - Chave de topo do `settings.json` que o manifesto **não declara**: preservada com o valor intacto.
  - Dentro de `hooks`, por evento: as entradas canônicas entram primeiro, na ordem declarada, com o
    comando já resolvido; as entradas locais **não-kit** são preservadas depois, na ordem original;
    as entradas locais **de kit** ausentes do canônico são removidas (são resíduo).
  - `permissions.deny`: substituída pela lista declarada. `permissions.allow` e qualquer outra
    subchave de `permissions` ficam intocadas.
  - `arquivos`: só caminho declarado é escrito, com o conteúdo copiado byte a byte; **nada é
    removido** no destino.
  - `settings.json` ausente ⇒ cria o arquivo só com as chaves declaradas. Escrita com indentação de
    2 espaços, newline final, UTF-8 sem BOM, e **idempotente**: conteúdo igual ao do disco não gera
    escrita.
- **O que é "entrada de kit".** Aquela cujo `command` referencia caminho sob a raiz do kit resolvida
  (`<KIT_ROOT>/tools/`, `<KIT_ROOT>/checks/`, `<KIT_ROOT>/global/hooks/`) ou, no alvo `usuario`, sob
  `<HOME_CLAUDE>/hooks/`. Todo o resto é configuração de quem opera a máquina e é **intocável**.
- **O que o `check` exige do canônico:** o manifesto existe e parseia; `alvos` é objeto; todo caminho
  em `arquivos.de` existe sob a raiz do kit; cada entrada de hook tem lista `hooks` não vazia, com
  `type: "command"` e `command` não vazio; e todo `command` que use um placeholder aponta para
  arquivo **existente** no canônico correspondente.
- **O que o `drift` acusa (exit 1):** (a) destino inexistente; (b) entrada canônica ausente do
  destino, ou presente com comando diferente do resolvido; (c) entrada **de kit** no destino que não
  está declarada no canônico — a guarda de regressão que impede alguém de voltar a registrar hook
  direto no arquivo de máquina; (d) `permissions.deny` do destino diferente da declarada; (e) arquivo
  declarado ausente do destino ou com conteúdo diferente.
- **Testes (mínimo 12, fixtures sintéticas em `tmp_path`, nunca escrevendo no repositório real nem
  no `~/.claude` real):**
  1. `apply` no layout hub materializa o hook do canônico;
  2. `apply` devolve `permissions.deny` igual à declarada e **não toca** `permissions.allow`;
  3. `apply` no layout consumidor (`<repo>/.claude/kit`) grava o comando com prefixo `.claude/kit/`
     e escreve no `settings.json` do pai;
  4. `apply` é idempotente — segunda execução não altera o conteúdo nem reescreve o arquivo;
  5. `apply` preserva hook local não-kit e remove entrada de kit obsoleta;
  6. `apply` preserva chave de topo não declarada (`model`, `statusLine`);
  7. `apply` sobre `settings.json` ausente cria o arquivo só com as chaves declaradas;
  8. `apply --alvo usuario` com `--home <tmp>` copia arquivo declarado e **não remove** arquivo
     não declarado presente no destino;
  9. `check` falha quando o canônico aponta comando para arquivo inexistente;
  10. `drift` falha com destino ausente, e a mensagem contém o comando de remédio;
  11. `drift` falha com hook de kit presente no destino e ausente do canônico;
  12. `drift --alvo projeto` sai 0 contra o repositório real depois do `apply` (leitura pura).
- **Invariantes.** Nenhum hook novo e nenhuma entrada de deny nova nascem aqui. Nenhum repositório
  derivado é tocado (`DA-3`). `sync-kit.ps1` não muda. O alvo `usuario` é declarado e vazio: nenhuma
  escrita em `~/.claude` acontece nesta tarefa.
- **Verificação:** bateria do §3 item 6; e, especificamente, `drift` vermelho quando a materialização
  é desfeita à mão, provado uma vez durante a tarefa.
- **Pronto quando:** o canônico do ponto de carga do projeto existe versionado, o
  `.claude/settings.json` local é produto de comando idempotente com `permissions.allow` intacto, e
  `drift` fica vermelho tanto se alguém desfizer a materialização quanto se alguém registrar hook de
  kit direto no arquivo local.

### T3 — `kit_check` cobra o canônico e a materialização [Sonnet · classe implementação padrão · teto 40]
- **Objetivo:** a régua deixa de depender de disciplina e passa a ter guarda. Estado inconsistente
  falha ruidosamente na bateria de fechamento.
- **Arquivos-alvo:** `.claude/checks/kit_check.ps1` — dois blocos novos; `tests/` não muda.
- **A edição exata.** O `-Mode validate` tem hoje três blocos (`1. Agentes`, `2. Skills`,
  `3. Paridade de versão`), agrega problemas em `$errors` e imprime a linha
  `kit_check: OK - N agente(s) e M skill(s) validados; VERSION == KIT_VERSION (...)`:
  - **Bloco 4, depois da paridade de versão:** chama
    `python <kitRoot>/tools/materializar.py check --alvo todos --kit-root <kitRoot>` e agrega **cada
    linha da saída** a `$errors`. A linha de OK do modo passa a citar também a contagem de entradas
    canônicas declaradas.
  - **`-Mode check-drift`:** ganha bloco equivalente com
    `materializar.py drift --alvo projeto --kit-root <kitRoot>`, agregado ao mesmo relatório de falha
    do modo — o modo continua checando `.claude/README.md` contra o regenerado, e agora falha também
    por materialização ausente ou divergente do alvo `projeto`.
  - **O alvo `usuario` fica fora do `check-drift`** (`DL-4`): cobrar no guarda a projeção da máquina
    de quem executa quebraria consumidor que não optou por ela.
  - `python` indisponível ou saída não interpretável **falha ruidosamente**; nenhum dos dois modos
    passa em silêncio por não conseguir checar.
- **Verificação:** bateria do §3 item 6; `kit_check -Mode validate` e `-Mode check-drift` em exit 0;
  e, provado uma vez na tarefa, `-Mode check-drift` vermelho com a materialização desfeita à mão.
- **Pronto quando:** desfazer a materialização, ou declarar no canônico um comando que aponta para
  arquivo inexistente, reprova a bateria de fechamento.

### T4 — `.claude/global/`: a doutrina global vira canônica projetada [Sonnet · classe implementação padrão · teto 40]
- **Objetivo:** a doutrina sempre-ativa fora de projeto Pantonic passa a viajar no pacote. Primeiro
  uso real do alvo `usuario`, com o conteúdo mais simples de provar: arquivos, sem hook.
- **Arquivos-alvo:**
  - `.claude/global/CLAUDE.md` — **novo**, cópia byte a byte de `~/.claude/CLAUDE.md` (156 linhas).
  - `.claude/global/docs/GOVERNANCA_MEMORIAS.md` — **novo**, cópia byte a byte (161 linhas).
  - `.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md` — **novo**, cópia byte a byte (94 linhas).
  - `.claude/projecoes.json` — **editado**: o bloco `arquivos` do alvo `usuario` passa a declarar os
    três pares `de`/`para` (`global/CLAUDE.md` → `CLAUDE.md`;
    `global/docs/GOVERNANCA_MEMORIAS.md` → `docs/GOVERNANCA_MEMORIAS.md`;
    `global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md` → `docs/RECOMENDACOES_CONSUMO_GLOBAL.md`).
  - `tests/test_materializar.py` — **editado**: um teste que prova que `drift --alvo usuario --home
    <tmp>` acusa arquivo ausente e sai 0 depois do `apply` correspondente.
- **Ordem obrigatória do ato.** Copiar **primeiro** o ponto de carga para o canônico, declarar
  depois, e só então rodar `apply --alvo usuario`. Feito nessa ordem, a materialização é **no-op**:
  o `~/.claude` do dono não muda um byte, e o `drift` verde é a prova de que a promoção foi fiel.
  Qualquer diferença detectada é erro de cópia, e a tarefa para.
- **Proibido:** editar o texto promovido (`DL-5`), reordenar Regras, mexer em qualquer arquivo de
  `~/.claude/` que não esteja nos três declarados.
- **Verificação:** bateria do §3 item 6; `python .claude/tools/materializar.py drift --alvo usuario`
  em exit 0 **sem** que nenhum arquivo do `~/.claude` tenha data de modificação alterada pelo
  `apply`.
- **Pronto quando:** os três documentos existem versionados no kit, o manifesto os declara, e o
  ponto de carga do usuário é reproduzível a partir do repositório.

### T10 — `apply` não reescreve o que não mudou [Sonnet · classe implementação padrão · teto 25]
- **Precede a `T5`** (`DL-10`). Aberta em 2026-08-17 pelo `TK-47`, achado da `T4`.
- **Objetivo:** `materializar.py apply` deixa de reescrever o `settings.json` do destino quando o
  resultado é semanticamente igual ao que já está lá. Sem isso, a `T5` — que manda parar em
  **qualquer** diferença fora do caminho resolvido pelo placeholder — para por um efeito que não é
  do escopo dela.
- **Fato medido (`RPC-T4`, 2026-08-17):** `write_settings`
  (`.claude/tools/materializar.py:220-231`) só evita a escrita quando o **texto** do destino é igual
  ao `_dump` canônico (`:216-217`, `indent=2`, `ensure_ascii=False`, `\n` final). Formatação
  divergente no destino ⇒ reescrita do arquivo inteiro, mtime alterado, conteúdo semanticamente
  intacto.
- **Arquivos-alvo:**
  - `.claude/tools/materializar.py` — **editado**, só `write_settings`: mantida a comparação de
    texto como caminho rápido, entra a comparação **semântica** contra o JSON já existente no
    destino (`json.loads` do arquivo × `obj`); iguais ⇒ retorna `False` **sem abrir o arquivo para
    escrita**. Destino ausente ou com JSON ilegível ⇒ comportamento atual (escreve).
  - `tests/test_materializar.py` — **editado**, dois testes: (1) TF — destino com o mesmo conteúdo
    semântico em formatação divergente (`indent=4` e ordem de chaves trocada) não é tocado pelo
    `apply` (bytes idênticos antes e depois); (2) regressão — destino a que falta uma entrada de
    hook canônica **continua** sendo escrito pelo `apply`, e o resultado sai no formato do `_dump`.
- **Proibido:** mudar `_dump` (o formato de escrita quando há mudança real não está em questão);
  mexer em `check` ou `drift` — ambos já comparam semanticamente (`:348`, `:358`, `:374`), e é por
  isso que esta mudança não cria drift perpétuo; tocar `~/.claude` real fora de fixture (`§3` item
  3: `--kit-root`/`--home` em `tmp_path`).
- **Fora de escopo, por `DL-10`:** preservar a formatação alheia quando há mudança semântica real.
- **Verificação:** bateria do `§3` item 6, com a suíte saindo de **65** para **67** testes; e, em
  fixture, `apply` rodado duas vezes seguidas sobre destino já materializado sem alterar um byte.
- **Pronto quando:** `apply` é byte-idempotente sob equivalência semântica, e a `T5` pode tratar
  qualquer diferença byte a byte no `settings.json` como sinal.

### T5 — Os hooks globais e seus módulos viram canônicos [Sonnet · classe implementação padrão · teto 40]
- **Objetivo:** os quatro hooks que hoje só existem na máquina do dono passam a ser declaração
  versionada com script versionado. É o caso que fecha o `TK-43` na sua forma geral.
- **Arquivos-alvo:**
  - `.claude/global/hooks/` — **novo**, com os scripts referenciados pelos quatro hooks registrados
    em `~/.claude/settings.json` mais os módulos que eles importam. Copiar byte a byte:
    `pytest_pretooluse.py`, `verbose_cmd_pretooluse.py`, `read_cap_pretooluse.py`,
    `modelo_por_fase_userpromptsubmit.py`, e — **confirmando por `Grep "^(import|from)"` nos quatro**
    — os helpers `pytest_filter.py` e `tail_filter.py`.
  - `.claude/projecoes.json` — **editado**: `arquivos` do alvo `usuario` ganha um par por script
    (`global/hooks/<x>.py` → `hooks/<x>.py`), e `chaves.hooks` passa a declarar os quatro registros,
    transcritos do estado vigente com o comando reescrito por `{HOME_CLAUDE}`:

    | Evento | `matcher` | Comandos, na ordem |
    |---|---|---|
    | `PreToolUse` | `Bash\|PowerShell` | `pytest_pretooluse.py`, `verbose_cmd_pretooluse.py` |
    | `PreToolUse` | `Read` | `read_cap_pretooluse.py` |
    | `UserPromptSubmit` | *(sem matcher)* | `modelo_por_fase_userpromptsubmit.py` |

    `timeout: 15` e o `statusMessage` de cada entrada são transcritos como estão.
  - `tests/test_materializar.py` — **editado**: um teste que prova, com `--home <tmp>`, que
    `apply --alvo usuario` preserva `model`, `effortLevel`, `switchModelsOnFlag`, `statusLine` e
    `permissions.allow` do `settings.json` do usuário.
- **Fica de fora, por `DL-3`:** `statusline.py` e a chave `statusLine`. Linha de status é
  configuração de quem opera a máquina; promovê-la faria o pacote decidir a aparência do terminal
  alheio.
- **Ordem obrigatória do ato:** copiar → declarar → `apply --alvo usuario` → conferir que o
  `~/.claude/settings.json` resultante difere do anterior **apenas** no caminho dos comandos
  resolvido pelo placeholder. Qualquer outra diferença para a tarefa.
- **Verificação:** bateria do §3 item 6; `materializar.py drift --alvo usuario` em exit 0; e uma
  invocação real de cada um dos quatro hooks continuando a funcionar (um `pytest` filtrado, um Read
  em arquivo grande, um comando verboso, um prompt novo).
- **Pronto quando:** os quatro hooks e a sua declaração existem versionados, o `~/.claude` do dono
  é reproduzível a partir do repositório, e o que sobra de exclusivo na máquina é só o que a `DL-3`
  declara.

### T11 — `{KIT_ROOT}` resolve para caminho absoluto [Sonnet · classe implementação padrão · teto 30]
- **Sucede a `T5`.** Aberta em 2026-08-17 pelo `TK-49`, achado da `T5`, com a rota decidida pelo dono
  no mesmo dia: corrigir na origem, para que nenhum consumidor herde o defeito. Recusada a
  alternativa de tratar como limitação operacional ("não mude o cwd").
- **Objetivo:** o `command` de hook gravado no `settings.json` do alvo `projeto` deixa de depender do
  cwd da chamada de ferramenta. `{KIT_ROOT}` passa a resolver para o caminho **absoluto** (POSIX) da
  raiz do kit, como `{HOME_CLAUDE}` já faz.
- **Fato medido (`RPC-T5`, 2026-08-17):** `kit_root_placeholder`
  (`.claude/tools/materializar.py:70-74`) devolve o texto relativo `.claude` (hub) ou `.claude/kit`
  (consumidor), de modo que `.claude/settings.json` registra `python .claude/tools/ocupacao.py`.
  Basta o cwd sair da raiz do repositório para o hook falhar — e hook `PreToolUse` que falha bloqueia
  **toda** ferramenta da sessão, inclusive a que restauraria o cwd. Medido ao vivo.
- **Premissa que sustenta a mudança, verificada em 2026-08-17:** `.claude/settings.json` é
  **gitignorado** (`.gitignore:3`) — artefato materializado por máquina, nunca versionado. A
  portabilidade que o desenho original perseguia (comando idêntico em qualquer clone) não tinha
  objeto: o arquivo nunca viaja entre clones.
- **Arquivos-alvo:**
  - `.claude/tools/materializar.py` — **editado**, três regiões:
    1. `kit_root_placeholder` (`:70-74`) devolve `kit_root.as_posix()` (já absoluto: `resolve_kit_root`
       faz `.resolve()` nos dois caminhos, `:58-61`). Nome da função **preservado**; docstring
       reescrita — o texto que hoje afirma "nunca o caminho físico absoluto" passa a afirmar o
       oposto, com a razão (o destino é local de máquina, e o cwd da chamada não é garantido).
    2. Entra `_kit_marker_prefix(kit_root) -> str`, privada, devolvendo o marcador **relativo**
       (`.claude/kit` se `kit_root.name == "kit"`, senão `.claude`) — a regra de topologia que hoje
       vive em `kit_root_placeholder`. `is_kit_command` (`:90-98`) passa a usá-la no lugar de
       `kit_root_placeholder`. **Isto é obrigatório, não estético:** a classificação é por substring,
       e o marcador relativo casa as duas formas — a absoluta gravada de agora em diante (que o
       contém) e a relativa gravada pelas versões anteriores. Sem isso, o `apply` da primeira
       execução classificaria a entrada relativa já instalada como hook **não-kit**, a preservaria ao
       lado da nova e deixaria o hook defeituoso vivo exatamente onde ele já está.
    3. Docstring de módulo (`:12-17`), o parágrafo que declara o texto portátil e a sua razão.
  - `tests/test_materializar.py` — **editado**. Seis asserções passam a esperar o caminho absoluto
    derivado da fixture `tmp_path` (nunca literal): `:95` (`python .claude/tools/ocupacao.py`), `:131`
    (`python .claude/kit/tools/ocupacao.py`, layout consumidor), `:200`, `:216`
    (`.../hook_antigo.py`, entrada de kit obsoleta), `:234` e `:437` (`.../obsoleto.py`). Mais **dois
    testes novos**: (1) TF — o `command` gravado pelo `apply` é caminho absoluto e o arquivo referido
    existe em disco; (2) TR — destino que já traz a entrada de kit na forma **relativa** antiga sai do
    `apply` com **uma** entrada só, a absoluta (regressão do `TK-49`).
- **Ordem obrigatória do ato:** editar → suíte verde em fixture → só então `apply --alvo projeto`
  real. O hook editado é `PreToolUse` com matcher `.*` e governa as chamadas de ferramenta da própria
  sessão: `settings.json` real inválido derruba a sessão. Antes do `apply` real, provar à mão que
  `python <abs>/.claude/tools/ocupacao.py` roda a partir de um cwd fora da raiz.
- **Proibido:** tocar o alvo `usuario` — `{HOME_CLAUDE}` já resolve absoluto (`:86`) e nada nele muda;
  tocar `~/.claude` real (§3 item 3); mudar `_referenced_file` (`:101-112`), que já opera sobre
  `kit_root` físico; alterar `check`/`drift`, que consomem o mesmo resolvedor e acompanham sozinhos.
- **Fora de escopo:** a prosa de `docs/plans/P-0734-execucao-autonoma.md` (`:2196-2198`, `:4474-4475`)
  e a da `### T2` deste plano (`:170`) — dossiê de tarefa já executada narra o ocorrido e não se
  reescreve (`DP-H`); o registro do que mudou é o bullet de fechamento desta tarefa.
- **Verificação:** bateria do §3 item 6 (`kit_check.ps1 -Mode validate`, `kit_check.ps1 -Mode
  check-drift`, `check-readme.ps1`, `dead_code.py`), com a suíte saindo de **68** para **70** testes;
  `materializar.py drift --alvo projeto` em exit 0 **depois** do `apply` real; e o `settings.json`
  resultante diferindo do anterior **apenas** no caminho do comando.
- **Pronto quando:** o hook do alvo `projeto` roda de qualquer cwd, a forma relativa antiga é
  substituída (não duplicada) na primeira materialização, e o `TK-49` fecha.

### T6 — As seis skills e o agente `context-scout` [Sonnet · classe implementação padrão · teto 40]
- **Objetivo:** os artefatos executáveis que a doutrina versionada invoca passam a existir no pacote.
  Fecha o `DR-B`, aberto desde 2026-08-03.
- **Arquivos-alvo:**
  - `.claude/global/skills/<nome>/SKILL.md` — **novos**, cópia byte a byte de
    `~/.claude/skills/<nome>/SKILL.md` para os seis: `context-prep`, `doc-map`, `lean-test`,
    `memory-diet`, `onboard`, `test-tiers`. Copiar também qualquer arquivo auxiliar existente dentro
    de cada diretório de skill.
  - `.claude/global/agents/context-scout.md` — **novo**, cópia byte a byte.
  - `.claude/projecoes.json` — **editado**: um par `de`/`para` por arquivo copiado.
  - `tests/test_materializar.py` — **editado**: um teste que prova que `apply --alvo usuario` cria
    diretório intermediário inexistente no destino (`skills/<nome>/`) sem tocar irmão não declarado.
- **Cuidado (`DL-6`).** Os sete artefatos **não** vão para `.claude/skills/` nem `.claude/agents/`:
  ali eles se tornariam skills de projeto ativas em todo Pantonic e colidiriam por nome com a própria
  projeção. Consequência verificável: as tabelas do `README.md` §11 e o `.claude/README.md` **não
  mudam**, e `kit_check`/`check-readme.ps1` continuam contando 8 agentes e 11 skills.
- **Ordem obrigatória do ato:** copiar → declarar → `apply --alvo usuario` (no-op) → `drift` verde.
- **Verificação:** bateria do §3 item 6; `kit_check -Mode check-drift` em exit 0 (prova de que o
  índice derivado do kit não se moveu); `materializar.py drift --alvo usuario` em exit 0.
- **Pronto quando:** as seis skills e o agente existem versionados no kit, e a doutrina que os cita
  aponta para artefato que viaja.

### T7 — Os ponteiros da doutrina para artefato global [Opus · classe redacao · teto 30]
- **Objetivo:** todo texto vivo que aponta para `~/.claude/<algo>` como se fosse residência passa a
  apontar para o canônico, com o ponto de carga citado como projeção. Sem isso a promoção existe e
  ninguém a encontra.
- **Arquivos-alvo e a edição exata:**
  1. **`GOVERNANCA.md` §3**, bullet do modelo por fase (`:111-113`): o ponteiro
     `~/.claude/docs/RECOMENDACOES_CONSUMO_GLOBAL.md` passa a
     `.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md`.
  2. **`GOVERNANCA.md` §3.1**, último parágrafo: confirmar que o ponteiro da governança das memórias
     nomeia o canônico (`.claude/global/docs/GOVERNANCA_MEMORIAS.md`) com o ponto de carga como
     projeção. Editar só se a redação vigente ainda citar o ponto de carga como residência.
  3. **`.claude/skills/proximo-passo/SKILL.md`**: as invocações de `context-prep` e `context-scout`
     passam a citar o caminho canônico do kit; nenhuma etapa do procedimento muda.
  4. **Varredura fechada**, com `Grep -n "~/\.claude"` restrito a `GOVERNANCA.md`,
     `ARQUITETURA_PANTONICA.md`, `README.md`, `.claude/skills/**/SKILL.md`, `.claude/agents/*.md` e
     `.claude/README.md`: cada ocorrência viva ou vira ponteiro canônico, ou é declarada como ponto
     de carga na própria frase. Ocorrência em `docs/plans/**`, `docs/DIARIO_*.md`, `docs/RDO/**`,
     `CHANGELOG.md` e `docs/audits/**` **não é tocada** — narra o ocorrido.
- **Proibido:** mudar o comportamento de qualquer skill ou agente; criar guardrail; reescrever
  registro do ocorrido.
- **Verificação:** bateria do §3 item 6; a varredura do item 4 repetida ao fim, com cada ocorrência
  restante justificada em uma linha no fechamento.
- **Pronto quando:** nenhuma superfície publicada ou executável do kit trata `~/.claude` como
  residência de conteúdo do framework.

### T8 — `.gitignore`, `CHANGELOG.md` e o fechamento dos tíquetes [Sonnet · classe mecanica · teto 15]
- **Objetivo:** o registro fecha junto com a mudança, e quem ler o `.gitignore` não repete o erro por
  leitura correta do documento errado.
- **Arquivos-alvo:**
  1. **`.gitignore`, comentário do bloco das linhas 1-3.** As duas entradas ignoradas **permanecem**
     e o comentário continua verdadeiro; acrescentar o ponteiro: a declaração canônica do que o
     harness lê mora em `.claude/projecoes.json`, versionada, e este arquivo é a materialização local
     produzida por `python .claude/tools/materializar.py apply`.
  2. **`CHANGELOG.md`, sob `## [Não lançado]`.** Uma entrada, na forma das vizinhas, cobrindo: a
     régua das três classes no §3.1, a residência canônica das projeções, o materializador, a
     exigência nova do `kit_check` e a promoção dos treze artefatos globais. Marcada `(RPC-T1..T7)`.
  3. **`docs/DIARIO_DE_OBRAS.md`, índice de tíquetes.** Status final de `TK-45` e `TK-43` (`done`,
     apontando para este plano) e a linha do `permissions.deny` escalado em `P-0734` §22.5 registrada
     como fechada pela `DL-7`.
- **Proibido:** número de versão novo, tag, seção numerada nova (`DE-7`); reescrever seção histórica
  do `CHANGELOG.md`; tocar a diretiva de priorização do topo do diário.
- **Verificação:** bateria do §3 item 6; `Grep -E "3\.0\.0|kit-v|bump"` dentro da seção
  `[Não lançado]` → vazio.
- **Pronto quando:** o `CHANGELOG.md` registra a mudança canônica, o `.gitignore` aponta para o
  canônico, e nenhum tíquete quitado por este plano continua aberto no índice.

### T9 — Revisão do `README.md` da raiz [Opus + dono · classe redacao · teto 25]
- **Objetivo:** fechar a sprint pelo contrato entre o framework e o cliente (`G-README` dever 2). O
  guarda executável é instrumento da atividade; o **único teste de sentido é o veredito do dono**.
- **Arquivos-alvo:** `README.md` (raiz) — leitura integral e correção do que a rodada tenha
  dessincronizado; `.claude/README.md` só se `kit_check -Mode check-drift` acusar.
- **Roteiro:**
  1. Rodar `pwsh .claude/checks/check-readme.ps1` e resolver toda falha estrutural (paridade de
     agentes, skills, versão, contagem de guardrails, fonte da verdade de cada seção).
  2. Ler o `README.md` inteiro procurando o que o guarda **não** vê: prosa que ainda descreva o
     estado anterior, número escrito por extenso divergente da tabela, seção que prometa artefato
     inexistente.
  3. Aplicar a `redacao-doc` ao que for reescrito.
  4. Apresentar ao dono, em uma mensagem, o que mudou no espelho nesta sprint e **pedir o veredito**.
     Aprovado, a sprint fecha; reprovado, o veredito vira o insumo da rodada seguinte e a tarefa
     devolve ao planejamento.
- **Proibido:** fechar a tarefa sem o veredito do dono; tratar o exit 0 do guarda como aceite.
- **Verificação:** `pwsh .claude/checks/check-readme.ps1` em exit 0 **e** veredito do dono
  registrado.
- **Pronto quando:** o dono aceita o espelho.

## 5. Ordem de execução

Linear, sem ramo: `T1 → T2 → T3 → T4 → T10 → T5 → T11 → T6 → T7 → T8 → T9`.

A `T10` entra em 2026-08-17, entre a `T4` e a `T5`, pela `DL-10`: ela conserta no materializador o
efeito que faria a `T5` parar por causa alheia.

A `T11` entra em 2026-08-17, logo depois da `T5`, pelo `TK-49`: o defeito que ela corrige foi medido
ao vivo na verificação da `T5` e viaja para todo consumidor que materializar o alvo `projeto`, então
precede a promoção dos artefatos executáveis restantes.

O corte é por valor validável cedo. `T1` fecha, no ato, a contradição que a régua nova abriu no
espelho. `T2` entrega o primeiro artefato executável e provável — materializar e verificar o ponto de
carga do projeto —, e `T3` o transforma em guarda. `T4`, `T5` e `T6` são a mesma operação repetida em
três conteúdos de risco crescente (documento, hook, artefato executável), cada uma provada por um
`drift` verde que não altera um byte da máquina. `T7` e `T8` fecham a superfície e o registro, e `T9`
é o aceite.

Dependências duras: `T3` exige o CLI da `T2`; `T4`..`T6` exigem o alvo `usuario` declarado pela `T2`;
`T7` exige os caminhos que `T4`..`T6` criam.

## 6. Rebase e absorção

### 6.1 `P-0734-execucao-autonoma` — classificação (A)

A premissa da iniciativa `EXECUCAO-AUTONOMA` continua de pé: nada aqui muda o loop, os papéis ou os
instrumentos dela. O que muda é o passo subsequente — duas tarefas dela resolviam, em forma
particular, a matéria que este plano resolve em forma geral.

- **`P-0734` → `blocked`**, razão: matéria de residência e distribuição centralizada no `P-0735`;
  destrava no fechamento dele. O plano fica suspenso em **49/60**, como a diretiva do dono já
  registrou.
- **`### T53` — cancelada por absorção.** O desenho dela (residência versionada de hook,
  materializador idempotente `apply`/`check`/`drift`, preservação de `permissions.deny` e de hook
  não-kit, ancoragem hub × consumidor, `kit_check` cobrando canônico e materialização) é **insumo
  integral** da `T2` e da `T3` deste plano, e sobrevive inteiro. Some apenas a residência particular
  que ela prescrevia: `.claude/hooks/hooks.json` **não nasce**, porque uma segunda declaração ao lado
  do manifesto único seria a duplicata que a régua proíbe (`DL-2`).
- **`### T54` — cancelada por absorção.** A superfície publicada que ela regularizava está coberta:
  `GOVERNANCA.md` §3.1 nesta rodada de planejamento, `README.md` §11/§13 na `T1`, `.gitignore` e
  `CHANGELOG.md` na `T8`. Um item dela é **revogado**: a `T54` mandava manter como está o bullet do
  hook global do `modelo-por-fase` (`GOVERNANCA.md` §3), pelo critério de que hook de kit é o que
  executa comando do kit. A régua nova não distingue por quem executa, e sim por de quem é o conteúdo
  — aquele hook é enforcement de regra publicada e já foi conciliado.
- **`### T14`** (telemetria sem turno de agente) declarava dependência da `T53`. A dependência passa
  para a **`T2`** deste plano; nenhuma outra linha do dossiê dela muda.

### 6.2 Rota de cada tíquete

| Tíquete | Rota |
|---|---|
| **`TK-45`** | **Absorvido** — é a origem deste plano. Fecha em `done` quando o plano fechar |
| **`TK-43`** | **Absorvido** — o caso particular do hook é o alvo da `T2`/`T3` (declaração e guarda) e da `T5` (os hooks globais). Fecha em `done` junto com a `T5` |
| **`permissions.deny` do guardrail 13** (`P-0734` `DP-R` §22.5, escalado e não decidido) | **Absorvido pela `DL-7`** — vira chave canônica declarada do alvo `projeto` na `T2`. A questão escalada deixa de estar aberta: a decisão do dono sobre alcance do pacote a cobre, e a invariante do §3.1 a decide |
| **`DR-B`** (`docs/RESIDENCIA_DOUTRINA.md` §5) | **Destravado e executado** na `T6`. A restrição derivada dele ("a descida não cita skill global") cai na `T7` |
| **`TK-21`** (ratchet sem alvo, 0/6 consumidores) | **Não absorvido.** A rota dele já está decidida (`DH-4`) e executável (`P-0733` `### T10`): o ratchet sai da bateria do hub e ganha residência na skill `guardrails-check`, que roda onde há código de produção. A régua nova não altera essa conclusão — o defeito ali é **verificador sem objeto**, e este plano não faz consumidor nenhum instalar o kit (`DL-8`). Permanece no `P-0733` |

## Achados da execução

- **2026-08-17** — achado durante a escolha da `RPC-T5` pela `proximo-passo`: `~/.claude/settings.json`
  perdeu a chave `hooks` inteira (os 4 hooks registrados, premissa da `T5`), sem ação intencional do
  dono, causa não investigada por decisão dele (foco em proteção, não em achar culpado). A `T5`
  restaura o registro normalmente, usando a tabela Evento/matcher/Comandos já transcrita em `### T5`
  (não depende do estado atual do settings.json). Vulnerabilidade a considerar (settings.json global
  pode perder chave inteira silenciosamente) registrada como tíquete avulso pendente de abertura no
  diário (`TK` a alocar) — rota: decisão do dono.
| **`TK-01`** | Já fechado; citado como precedente da classe, sem ação |

## 7. Fora de escopo (explícito)

- **O conteúdo do `~/.claude/CLAUDE.md`** — a promoção é de residência, não de texto (`DL-5`). Revisar
  as 8 Regras item a item é matéria de `docs/RESIDENCIA_DOUTRINA.md`, e reabri-la aqui tornaria a
  mudança de residência irrevisável.
- **Propagação aos consumidores** — `DA-3` mantida: hub primeiro, medir, depois propagar. Gatilho:
  quando o primeiro consumidor materializar `.claude/kit/`, a decisão de projetar o alvo `usuario`
  naquela máquina é de quem a opera, e o plano de propagação nasce ali.
- **`sync-kit.ps1`** — o contrato dele é espelhar `skills/` e `agents/` no namespace plano do
  consumidor; `global/`, `tools/` e `checks/` viajam dentro de `.claude/kit/` pelo caminho que já
  existe. Estender um script provado ponta a ponta, sem medida que o justifique, fica para o gatilho
  de propagação.
- **`statusline.py` e a chave `statusLine`** — locais de máquina por `DL-3`.
- **`TK-36`** (unificação `handover` + `proximo-passo`) e **`TK-38`** (comunicação agente↔humano) —
  matérias disjuntas, com tíquete próprio.

## 8. Riscos

| Risco | Mitigação |
|---|---|
| Escrita destrutiva no `~/.claude` do dono | Invariante 2 do §3 (nada fora do declarado é escrito, nada é removido), `--home` obrigatório nos testes, e a **ordem copiar → declarar → aplicar**, que torna todo `apply` de promoção um no-op verificável |
| Promoção infiel (o canônico diverge do que estava rodando) | Cópia byte a byte, e o `drift` verde imediatamente depois do `apply` é a prova. Diferença detectada **para a tarefa** em vez de virar correção de passagem |
| Colisão de nome entre skill do kit e skill projetada na mesma máquina | `DL-6`: o canônico do ponto de carga do usuário vive em `.claude/global/`, que não é caminho de descoberta de skill de projeto |
| Consumidor reprovado por guarda que cobra projeção de máquina alheia | `DL-4`: `check-drift` cobre só o alvo `projeto`; o alvo `usuario` tem comando próprio, fora da bateria |
| A régua publicada nomear caminho que ainda não existe | Janela fechada pela ordem do §5: a `T1` regulariza o espelho e a `T2` cria o mecanismo antes de qualquer ponteiro novo entrar em skill ou agente (`T7`) |
