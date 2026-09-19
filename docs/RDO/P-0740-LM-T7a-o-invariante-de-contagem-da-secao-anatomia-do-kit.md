# RDO — P-0740 · LM-T7a

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T7a` — O invariante de contagem da seção *Anatomia do kit*
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — a prosa que **conta** a tabela de *Anatomia do kit* passa a ser conferida pelo mesmo guarda que confere a tabela. Enquanto o invariante não estiver no instrumento, o verde dele é falso conforto: hoje o script **anuncia** `9 agente(s)` e sai exit 0 com o README dizendo "oito agentes" duas linhas acima da tabela de nove.

**Arquivos-alvo:** - `README.md` - `.claude/checks/check-readme.ps1`

**Verificação:** (o "antes" de cada linha foi **rodado** no `ESC-2`; o item 2 é a saída que o passo 2 desta tarefa produz — `DM-12`) 1. `pwsh -NoProfile -Command "& .claude/checks/check-readme.ps1 | Out-Null; exit $LASTEXITCODE"` → exit 0. **Antes (medido):** exit 0 **também** — o exit code, sozinho, não discrimina nada aqui; quem discrimina é o item 2. 2. A saída do passo 2 (guarda pronto, prosa velha) foi **exit 1** com `Divergência na contagem de agentes: a frase de 'Anatomia do kit' declara 8 vs 9 agente(s) em .claude/agents/.` Se esse passo sair exit 0, a checagem **não** está discriminando: contingência 2. 3. `pwsh -NoProfile -Command ".claude/checks/kit_check.ps1 -Mode check-drift | Out-Null; exit $LASTEXITCODE"` → exit 0, regressão (medido no `ESC-2`, depois da `LM-T7`: exit 0). 4. `python -m pytest tests/ -q` → verde, piso ≥ **145** (medido: `145 passed`). Esta tarefa não acrescenta teste `pytest`: não há harness de `pytest` para os `.ps1` do kit (medido: nenhum arquivo de `tests/` invoca `pwsh`), e inventar um é outro tema. 5. `pwsh -NoProfile -Command "Select-String -Path README.md -Pattern 'O kit são' -SimpleMatch"` → uma linha, com `nove agentes`. **Antes (medido):** `README.md:760:O kit são oito agentes, onze skills, quatro verificadores executáveis e a declaração de projeções,`.

**Pronto quando:** `check-readme.ps1` tem a checagem 5 com as três mensagens literais; a saída do passo 2 (exit 1, `declara 8 vs 9`) está registrada na linha de retorno; `README.md:760` declara `nove agentes`; e as cinco linhas de `Verificação` saem como escritas.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` — despachada em 2026-09-18 pelo `scrum-master`. Aberta pelo `ESC-2` (2026-09-18) sobre o `AE-12`; residência única do reparo. A `LM-T7` **não** se refaz: ela entregou o que o card mandava, e o card é que não mandou fechar a frase que conta a tabela.
- **Esforço:** low
- **Depende de:** `DM-18`; a `LM-T7` fechada (a nona linha da tabela é entrega dela). Nenhuma outra tarefa, e nenhuma outra depende desta.
- **Produto do módulo:** (a) `check-readme.ps1` ganha a **checagem 5** — a frase de contagem da seção *Anatomia do kit* tem de declarar o mesmo número de **agentes** e de **skills** que o script já conta do disco; (b) a frase corrigida em `README.md`.
- **Fatos medidos no `ESC-2` (2026-09-18), que são a baseline desta tarefa:** - `README.md:760`, literal, ocorrência **única** de `O kit são` no arquivo: `O kit são oito agentes, onze skills, quatro verificadores executáveis e a declaração de projeções,` - disco: **9** arquivos em `.claude/agents/*.md`, **11** diretórios em `.claude/skills/`, **4** executáveis em `.claude/checks/`; - `check-readme.ps1` → **exit 0**, com `check-readme: OK - 9 agente(s), 11 skill(s), 18 guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade válida.` — isto é, o script **já calcula** `$agentCount` e `$skillCount` (`:230`) e não os confronta com a prosa. Nenhuma contagem nova se inventa nesta tarefa; - `README.md` **não** tem região marcada (`<!-- kit:agents:begin -->` só existe em `.claude/README.md`): a linha 760 é escrita à mão e **não** é regenerada por `kit_check`. `## <N>. Anatomia do kit`, a **primeira** linha que começa com `O kit são ` é a frase de contagem; dela se extraem o token imediatamente anterior a ` agentes` e o imediatamente anterior a ` skills`. Cada token vale como número se for **dígito** ou se estiver no mapa por extenso de `zero` a `vinte`; token fora disso é erro nomeado, nunca silêncio. disco tem): ``` Divergência na contagem de agentes: a frase de 'Anatomia do kit' declara <N> vs <M> agente(s) em .claude/agents/. Divergência na contagem de skills: a frase de 'Anatomia do kit' declara <N> vs <M> skill(s) em .claude/skills/. Frase de contagem de 'Anatomia do kit' ausente ou com numeral fora do vocabulário (dígito ou por extenso até vinte): '<token>'. ```
- **Passos — a ordem é o que produz a evidência, e não se inverte:** 1. Implementar a checagem 5 em `.claude/checks/check-readme.ps1`, no mesmo idioma das quatro existentes (acumular em `$errors`, nunca `exit` no meio), com o mapa de numerais e as três mensagens literais acima. 2. Rodar o guarda **com a prosa ainda velha**: `pwsh -NoProfile -Command "& .claude/checks/check-readme.ps1; exit $LASTEXITCODE"` → tem de sair **exit 1** com a primeira mensagem, na forma `declara 8 vs 9 agente(s)`. Registrar a saída na linha de retorno da entrega. **É este passo que prova que a checagem discrimina** — e ele só existe porque a correção da prosa vem depois. 3. Só então corrigir `README.md:760`, trocando **uma** palavra: ``` O kit são nove agentes, onze skills, quatro verificadores executáveis e a declaração de projeções, ```
- **Restrições desta tarefa:** a checagem 5 acumula em `$errors` como as outras quatro — o script tem de continuar reportando **todos** os problemas numa passada. A frase corrigida muda **uma** palavra: `oito` → `nove`; nada mais da linha se reescreve. `README.md` não é gerado — não rodar `kit_check -Mode generate` aqui.
- **Não fazer:** não estender a checagem a "verificadores executáveis" nem à "declaração de projeções" — o script **não conta** nenhum dos dois hoje, e autorar a contagem sem fato medido é o defeito que a `RP-1` já pagou; fica fora do escopo, nominalmente (`DM-18` (v)). Não tocar `.claude/agents/` (`DM-17`), `.claude/README.md` (é gerado, e a `LM-T7` já o regenerou), `GOVERNANCA.md` (a contagem de guardrails já tem a checagem 4) nem instrumento de `.claude/tools/`. Não commitar.
- **Contingências:** 1. se `README.md:760` não for o literal transcrito acima → parar e sinalizar `blocked` razão `premissa`, citando a linha encontrada; 2. se o passo 2 sair **exit 0** → a checagem não discrimina; corrigir a implementação e repetir o passo 2 antes de tocar a prosa. Se persistir depois de uma correção, parar e devolver `blocked` razão `premissa` com a saída obtida; 3. se `python -m pytest tests/ -q` ficar vermelho em qualquer teste → seguir com a entrega e devolver `contingência 3 acionada: <arquivo::teste> vermelho fora dos alvos` (esta tarefa não toca Python nenhum).

## Execução

**Consumo:** 13 tool uses, 75.3 k tokens, 268.8 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: passo2 registrado: check-readme FALHOU (1 problema) com 'declara 8 vs 9 agente(s)', exit 1 — prova de discriminacao exigida pelo Pronto quando

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
