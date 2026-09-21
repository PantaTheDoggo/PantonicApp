# RDO — P-0743 · DOM-T1

**Plano:** `docs/plans/P-0743-modelo-de-dominio.md`
**Tarefa:** `DOM-T1` — A norma do modelo de domínio, e o papel que a executa
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `GOVERNANCA.md` §3.2 substituída pela norma do modelo de domínio, a matriz de responsabilidades com a linha `**Modelagem**` e as três linhas de papel corrigidas, e a rubrica de revisão com a linha de alvo e o parágrafo de fronteira novos.

**Arquivos-alvo:** - `GOVERNANCA.md:320` (`### 3.2 O modelo conceitual do plano`, até a linha 356 inclusive) - `GOVERNANCA.md:94` (linha `| **Revisão** |` da matriz de responsabilidades) - `GOVERNANCA.md:91` (linha `| **Planejamento** |`) - `GOVERNANCA.md:92` (linha `| **Orquestração** |`) - `docs/RUBRICA_DE_REVISAO.md:246` (`## 6. Achado de processo`, linha da tabela cujo primeiro campo é `modelo`) - `docs/RUBRICA_DE_REVISAO.md:278` (`## 7. Fronteira do papel`, parágrafo único)

**Verificação:** ``` grep -c '^| \*\*' GOVERNANCA.md ``` imprime `15` (hoje imprime `14`, medido 2026-09-20 — a matriz de §3 ganha uma linha). ``` grep -n '### 3.2 O modelo de domínio do plano' GOVERNANCA.md ``` imprime uma linha (hoje não imprime nada). ``` grep -c 'confirma e emenda o modelo conceitual' GOVERNANCA.md ``` imprime `0` (hoje imprime `1`). ``` grep -c 'O reviewer não escreve fora do caminho do laudo' docs/RUBRICA_DE_REVISAO.md ``` imprime `1` (hoje imprime `0`). `python .claude/tools/backlog.py check` imprime `check: OK — nenhuma violação.` e sai `0` (mesma saída medida em 2026-09-20).

**Pronto quando:** `GOVERNANCA.md` §3.2 é o texto da §4 deste plano palavra por palavra, a matriz de §3 tem dez linhas de papel com a linha `**Modelagem**` logo depois de `**Revisão**`, as três linhas de papel citadas carregam o trecho novo, e os dois blocos da rubrica estão substituídos.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20
- **Fundamento:** `D-1`, `D-2`, `D-5`, `D-6`, `D-8`, `D-9`; fatos `F-9`, `F-14`. O card transcreve os blocos cercados da §4 deste plano, que é a residência única deles até a transcrição.
- **Oração do modelo:** `M-1`, `M-2`, `M-3`, `M-11` - M-1: O modelo de um plano passa a descrever o que o plano entrega como objetos e operações encadeadas: cada objeto com o contrato que a implementação precisa, e cada operação nomeando quem age, o que faz e de que objetos precisa. - M-2: O estado do modelo deixa de ser um status por frase e passa a ser uma posição no fluxo: o dono lê qual é o estágio atual, o que já ficou para trás e o que ainda vem. - M-3: A posição no fluxo é derivada do andamento das tarefas e nenhum papel a grava: o estágio atual é a primeira operação cujas tarefas ainda não fecharam. - M-11: O ensinamento de como se escreve um modelo mora na definição do modelador, separado da norma que diz o que um modelo é e da gramática que a máquina lê.
- **Camada e fronteira:** documentação de doutrina. Nenhum código, nenhum teste. A regra de dependência `infracore ← contracts ← services ← plugins` não é tocada.
- **Passos:** 1. Substituir as linhas 320..356 de `GOVERNANCA.md` pelo bloco cercado de `### 3.2 O modelo de domínio do plano` da §4 deste plano, verbatim. 2. Inserir, imediatamente depois da linha `| **Revisão** |` da matriz de §3, a linha `| **Modelagem** | …` da §4 deste plano, verbatim. 3. Trocar, na linha `| **Planejamento** |`, o trecho vigente pelo trecho novo da tabela de substituições da §4. 4. Repetir a troca na linha `| **Revisão** |` e na linha `| **Orquestração** |`, com os trechos correspondentes da mesma tabela. 5. Substituir integralmente a linha de alvo `modelo` da tabela da §6 de `docs/RUBRICA_DE_REVISAO.md` pelo bloco cercado correspondente da §4. 6. Substituir integralmente o parágrafo da §7 de `docs/RUBRICA_DE_REVISAO.md` pelo bloco cercado correspondente da §4. 7. Rodar as verificações abaixo.
- **Restrições desta tarefa:** - Texto normativo entra **verbatim** dos blocos cercados da §4. Não parafrasear, não resumir, não reordenar tabela (`I-3`). - Card que publica norma que altera contagem ou enumeração fecha, no mesmo card, as frases da mesma seção que contam o conjunto (`I-4`). A matriz passa de 9 para 10 linhas de papel. - Não commitar (`I-6`).
- **Não fazer:** - Não tocar `.claude/agents/*`, `.claude/skills/*`, `.claude/tools/*`, `README.md` nem `.claude/README.md` — cada um tem card próprio. - Não criar o agente `pantonic-model-designer` aqui: a norma o nomeia, a `DOM-T4` o cria. - Não editar `GOVERNANCA.md` §9, que enumera três agentes de um total de nove: a enumeração já está defasada antes deste plano e está declarada fora de escopo (§11).
- **Contingências:** 1. Se `Select-String -Path GOVERNANCA.md -SimpleMatch -Pattern 'nove papéis','oito papéis'` imprimir alguma linha → editar cada linha impressa para o numeral `dez`, no mesmo ato. 2. Se as linhas 320..356 de `GOVERNANCA.md` não começarem exatamente por `### 3.2 O modelo conceitual do plano` → parar e sinalizar `blocked` razão `premissa`. 3. Se a tabela da §6 de `docs/RUBRICA_DE_REVISAO.md` não tiver linha cujo primeiro campo seja `modelo` → parar e sinalizar `blocked` razão `premissa`.
- **Testes:** nenhum teste automatizado — a entrega é texto normativo. A aferição é a verificação abaixo.
- **Fora do escopo desta tarefa:** a gramática que a máquina lê (`DOM-T2`), o instrumento (`DOM-T3`), o agente (`DOM-T4`), as definições de conduta dos papéis (`DOM-T5`) e a documentação pública (`DOM-T6`).

## Execução

**Consumo:** 22 tool uses, 74.0 k tokens, 195.6 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: quebra de linha do bloco cercado da §7 (plano, §4, linhas 231-328) reempacotada para que o literal de aceite ficasse contíguo, sem alterar palavra, pontuação ou ordem do texto normativo

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

A transcrição de bloco cercado é classe barata desde que o literal de aceite seja publicado na mesma quebra de linha que o arquivo-alvo carrega; o único ponto de juízo exigido do executor nasceu da colisão entre a restrição verbatim (I-3) e um literal de aceite que o próprio plano publica quebrado.

## Fechamento

**Desdobramento:** aprovado
