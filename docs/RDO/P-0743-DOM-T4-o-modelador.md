# RDO — P-0743 · DOM-T4

**Plano:** `docs/plans/P-0743-modelo-de-dominio.md`
**Tarefa:** `DOM-T4` — O modelador
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** o agente `pantonic-model-designer` existindo como décimo agente do kit, com o ensinamento de como se escreve um modelo de domínio, e as duas portas de inventário do kit fechadas sobre dez agentes.

**Arquivos-alvo:** - `.claude/agents/pantonic-model-designer.md` - arquivo novo - `README.md` - a frase de contagem da §11 — linha 802 em 2026-09-20 - a tabela **Agentes** da §11: a linha nova entra **depois** da última linha da tabela, que é a de `pantonic-benchmarker` — linha 819 em 2026-09-20. O 816 previsto no planejamento estava defasado, medido no `ESC-1`; os dois números se re-derivam no despacho (`I-5`) - `.claude/README.md` - só a região entre os marcadores `kit:agents` de início e fim, e só por instrumento (`I-7`)

**Verificação:** ``` pwsh -NoProfile -File .claude/checks/check-readme.ps1 ``` sai `0` e a saída começa por `check-readme: OK - 10 agente(s), 11 skill(s), 20 guardrail(s)` (hoje: `check-readme: OK - 9 agente(s), 11 skill(s), 20 guardrail(s)`, medido 2026-09-20). ``` pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift ``` sai `0` e a saída começa por `kit_check: check-drift OK - .claude/README.md == regenerado (10 agente(s), 11 skill(s))` (hoje: `(9 agente(s), 11 skill(s))`, medido 2026-09-20). ``` grep -c '^| `pantonic-' README.md ``` imprime `10` (hoje imprime `9`). ``` grep -c '^| `pantonic-' .claude/README.md ``` imprime `10` (hoje imprime `9`). ``` grep -c 'O kit são dez agentes' README.md ``` imprime `1` (hoje imprime `0`). ``` grep -c -e 'nove agentes' -e '9 agente' README.md .claude/README.md ``` imprime `0` para os dois arquivos (hoje `README.md` imprime `1`, na linha 802, e `.claude/README.md` imprime `0`, medido 2026-09-20). É o aceite de coerência do inventário inteiro (`I-10`). ``` sed -n '1,6p' .claude/agents/pantonic-model-designer.md ``` sai idêntico, linha a linha, ao bloco cercado do front matter deste card; e a linha nova da tabela **Agentes** e a frase de contagem entregues conferem palavra por palavra com os blocos cercados correspondentes. Devolver na linha de retorno a declaração de fidelidade do `I-11`: `fidelidade conferida: <bloco> — <n> linhas idênticas ao bloco cercado do card`, uma por bloco literal deste card. **Divergência de um único token é defeito de transcrição (`I-3`), ainda que a semântica não mude** — foi assim que o `AE-8` passou por 11/11 greps verdes.

**Pronto quando:** `.claude/agents/pantonic-model-designer.md` existe com os sete blocos, os dois guardas saem `0` anunciando dez agentes, as duas tabelas de inventário têm dez linhas de agente e **nenhuma frase dos dois READMEs conta nove agentes** (`I-10`).

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20
- **Depende de:** `DOM-T3`
- **Fundamento:** `D-5`, `D-6`, `D-9`, `D-12`; fatos `F-2`, `F-7`, `F-8`; invariantes `I-4`, `I-7`, `I-9`. A norma que este agente executa foi gravada pela `DOM-T1`; a gramática que ele escreve, pela `DOM-T2`; o instrumento que o confere, pela `DOM-T3`.
- **Oração do modelo:** `M-8`, `M-9`, `M-11` - M-8: Um agente único é dono de todas as operações do modelo: escreve o modelo de todo plano, emenda quando uma decisão muda o que o plano entrega, resolve conflito entre o texto e a entrega e explica o contexto a quem pergunta. - M-9: Nenhum outro papel escreve no modelo, e nenhum agente aciona outro agente: quem precisa de um ato de modelo devolve um dossiê fechado na própria linha de retorno, e quem conduz a sessão despacha o modelador. - M-11: O ensinamento de como se escreve um modelo mora na definição do modelador, separado da norma que diz o que um modelo é e da gramática que a máquina lê.
- **Camada e fronteira:** definição de agente, em `.claude/agents/`. O arquivo novo tem front matter com `name`, `description`, `model` e `tools`, na mesma forma dos nove vigentes.
- **Texto novo, literal — front matter de `.claude/agents/pantonic-model-designer.md`:** ```markdown --- name: pantonic-model-designer description: Modelador de domínio de plano Pantonic*. Dono único de todo ato sobre a seção Modelo conceitual de um plano - escreve na autoria, emenda quando uma decisão muda o que o plano entrega, resolve conflito entre o texto e a entrega e explica o contexto do modelo. Não planeja, não executa, não julga entrega e não escreve nenhuma outra linha do plano. model: opus tools: Read, Glob, Grep, Bash, Edit --- ```
- **Texto novo, literal — linha a acrescentar ao fim da tabela **Agentes** de `README.md` §11:** ```markdown | `pantonic-model-designer` | Opus | Todo ato sobre o modelo de domínio de um plano: escrever na autoria, emendar por decisão, resolver conflito entre o texto e a entrega e explicar o contexto. Não planeja, não executa e não julga. | ```
- **Texto novo, literal — frase de contagem de `README.md` §11:** ```markdown O kit são dez agentes, onze skills, quatro verificadores executáveis e a declaração de projeções, ```
- **Passos:** 1. Criar `.claude/agents/pantonic-model-designer.md` com o front matter literal acima e o corpo descrito no passo 2. 2. Escrever o corpo do agente com sete blocos, nesta ordem: (a) o papel, apontando para a matriz de `GOVERNANCA.md` §3 como residência única dele; (b) os fatos estáveis — a norma em `GOVERNANCA.md` §3.2, a gramática na skill `diario-de-obras`, o instrumento `.claude/tools/modelo.py`; (c) **o ensinamento**: como se escreve um modelo de domínio — começar pelos objetos que o plano manipula, dar a cada um o contrato que quem implementa precisa, encadear as operações na ordem em que o produto as executa, escrever cada operação nomeando quem age, e conferir que a primeira operação é a única que só depende de objeto externo; (d) os quatro atos — `autoria`, `emenda`, `conflito`, `leitura` —, com o que cada um recebe e o que devolve; (e) a gramática do dossiê `Ato de modelo` de seis campos, copiada da norma; (f) a forma da devolução: a seção `## 1. Modelo conceitual` inteira e literal, mais a linha `MD-<n>` do ato, e nada mais; (g) o que o modelador nunca faz — não planeja, não executa, não julga entrega, não escreve fora da seção `## 1. Modelo conceitual` e não aciona outro agente. 3. Acrescentar, no bloco (b), a linha de auto-conferência: todo ato termina com `python .claude/tools/modelo.py check --plano <plano>` e só devolve com exit `0`. 4. Acrescentar a linha literal da tabela **Agentes** ao fim dela em `README.md` §11, depois da linha de `pantonic-benchmarker`. 5. Trocar a frase de contagem de `README.md` §11 pela frase literal acima. 6. Regenerar `.claude/README.md` com `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate`. 7. Rodar as verificações abaixo.
- **Restrições desta tarefa:** - `README.md` (a raiz) e `.claude/README.md` são arquivos diferentes com donos diferentes (`I-9`): o primeiro é editado à mão nos passos 4 e 5; o segundo **só** pelo instrumento do passo 6 (`I-7`). - A frase de contagem e a tabela são a mesma seção: quem acrescenta a linha fecha a frase no mesmo ato (`I-4`). O aceite é de coerência do **inventário inteiro**, não das duas linhas editadas (`I-10`): depois do passo 6, nenhuma frase do `README.md` nem de `.claude/README.md` pode contar nove agentes. - Nenhuma contingência deste card cria arquivo além de `.claude/agents/pantonic-model-designer.md`, que já está nos `Arquivos-alvo`. Se alguma só puder ser cumprida criando outro arquivo, o card está incompleto: sinalizar `blocked` razão `premissa` (`I-10`). O numeral vai **por extenso**, como o vigente, porque é assim que `check-readme.ps1` o lê. - `tools:` do agente novo não inclui `Write`: o modelador edita a seção de um plano que já existe, nunca cria arquivo. - Não commitar (`I-6`).
- **Não fazer:** - Não editar a região gerada de `.claude/README.md` à mão, em nenhuma circunstância. - Não tocar `GOVERNANCA.md` §9, cuja enumeração de agentes já está defasada e está fora de escopo (§11). - Não mudar o front matter de nenhum dos nove agentes existentes. - Não escrever no corpo do agente a norma nem a gramática: elas têm residência própria e o corpo aponta para elas (`D-9`).
- **Contingências:** 1. Se `kit_check.ps1 -Mode generate` sair diferente de `0` → parar e sinalizar `blocked` razão `ferramenta`, com a saída literal na linha de retorno. 2. Se `check-readme.ps1` acusar divergência de contagem depois do passo 5 → a frase ficou com numeral errado; corrigir a frase e repetir, sem tocar a tabela.
- **Testes:** nenhum teste automatizado — a entrega é definição de agente e inventário. A aferição são os dois guardas abaixo, que já discriminam a contagem.
- **Fora do escopo desta tarefa:** as cláusulas dos outros papéis (`DOM-T5`), a seção pública §8.1 (`DOM-T6`) e qualquer ato de modelo sobre plano real.

## Execução

**Consumo:** 26 tool uses, 99.5 k tokens, 168.7 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: fidelidade conferida nos três blocos literais (front matter 6 linhas, linha da tabela Agentes 1, frase de contagem 1); conferida pelo revisor byte a byte em Python, não por diff de shell, porque árvore com CRLF misto mascara divergência de terminador

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

A fidelidade foi conferida byte a byte em Python e não por diff de shell — em árvore com CRLF misto o diff mascara divergência de terminador. O README.md carrega, no mesmo recorte, dois hunks da MC-T5 do P-0741 (linha 417 e a seção 8.1 nova) além dos dois desta entrega (802 e 819): arquivo compartilhado entre janelas exige separação por hunk, não por arquivo — e isso vale para a DOM-T6, que revisa o README inteiro.

## Fechamento

**Desdobramento:** aprovado
