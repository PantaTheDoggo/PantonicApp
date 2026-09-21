# RDO — P-0743 · DOM-T5b

**Plano:** `docs/plans/P-0743-modelo-de-dominio.md`
**Tarefa:** `DOM-T5b` — A cadeia do retorno, do emissor ao consumidor
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** os cinco pontos que ainda proíbem, contam ou transportam a linha de retorno do revisor alinhados entre si, de ponta a ponta: a definição do papel, o **despacho** do passo 6, a **leitura** do passo 7 e o que o passo 7 entrega ao passo 8 — de modo que o dossiê `Ato de modelo` que o bloco B do passo 8 consome possa existir.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md` - **quatro** pontos, medidos em 2026-09-20 e re-derivados no despacho (`I-5`): passo 6 ação, linhas 127-128 (bloco K); passo 6 saída, linha 129 (bloco L); passo 7 entrada, linhas 134-136 (bloco M); passo 7 saída, linha 141 (bloco N) - `.claude/agents/pantonic-reviewer.md` - **um** ponto: o bullet `- Saída:` do domínio de saída, linhas 51-52 (bloco O)

**Verificação:** Os cinco literais que **saem** — todos medidos em 2026-09-20, cada um numa linha só do destino: ``` grep -cF -e 'instrução de devolver só as duas linhas de veredito.' .claude/skills/scrum-master/SKILL.md ``` imprime `0` (hoje imprime `1`, na linha 128). ``` grep -cF -e '- **Saída:** duas linhas do `reviewer`.' .claude/skills/scrum-master/SKILL.md ``` imprime `0` (hoje imprime `1`, na linha 129). ``` grep -cF -e '- **Entrada:** as duas linhas fixas:' .claude/skills/scrum-master/SKILL.md ``` imprime `0` (hoje imprime `1`, na linha 134). ``` grep -cF -e '- **Saída:** tripla (`veredito`, `bloqueante`, `recomendação`) para o roteamento.' .claude/skills/scrum-master/SKILL.md ``` imprime `0` (hoje imprime `1`, na linha 141). ``` grep -cF -e '- Saída: duas linhas de veredito ao chamador e o laudo em documento próprio' .claude/agents/pantonic-reviewer.md ``` imprime `0` (hoje imprime `1`, na linha 51). Os cinco literais que **entram** — a borda de cada bloco: ``` grep -cF -e '**Não limite o retorno dele às duas linhas.**' .claude/skills/scrum-master/SKILL.md ``` imprime `1` (hoje imprime `0`). ``` grep -cF -e '- **Saída:** as duas linhas do `reviewer` e, quando houver, o dossiê' .claude/skills/scrum-master/SKILL.md ``` imprime `1` (hoje imprime `0`). ``` grep -cF -e '- **Entrada:** as duas linhas fixas e, quando houver, o dossiê anexo abaixo delas:' .claude/skills/scrum-master/SKILL.md ``` imprime `1` (hoje imprime `0`). ``` grep -cF -e 'para o roteamento, mais o dossiê `Ato de modelo` quando ele veio no retorno.' .claude/skills/scrum-master/SKILL.md ``` imprime `1` (hoje imprime `0`). ``` grep -cF -e 'as duas linhas de veredito ao chamador, o dossiê' .claude/agents/pantonic-reviewer.md ``` imprime `1` (hoje imprime `0`). A cadeia inteira, de ponta a ponta (`I-14`): ``` grep -c -e 'só as duas linhas' -e 'somente as duas' -e 'só duas linhas' .claude/skills/scrum-master/SKILL.md .claude/agents/pantonic-reviewer.md ``` imprime `0` para os dois arquivos (hoje o `scrum-master` imprime `1` e o reviewer `0`, medido 2026-09-20). **Nenhuma linha de nenhum dos dois pode limitar o retorno do revisor a duas linhas.** ``` grep -c 'Ato de modelo' .claude/skills/scrum-master/SKILL.md .claude/agents/pantonic-reviewer.md ``` imprime `4` ou mais para o `scrum-master` (hoje `1`, o bloco B) e `3` ou mais para o reviewer (hoje `2`, o passo `5a` e o passo 7), medido 2026-09-20: os blocos K, M e N acrescentam três citações ao `scrum-master` e o bloco O uma ao reviewer. ``` grep -cF -e 'Edit' .claude/agents/pantonic-reviewer.md ``` imprime `0` (hoje imprime `0`, **inalterado**). As cinco regiões entregues, para confronto linha a linha com os blocos K, L, M, N e O (`I-11` item 1) — **é este comando, e não a declaração do executor, que prova a fidelidade**: ``` sed -n '125,150p' .claude/skills/scrum-master/SKILL.md sed -n '49,55p' .claude/agents/pantonic-reviewer.md ``` ``` pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift ``` sai `0` e anuncia `(10 agente(s), 11 skill(s))` — **inalterado** (hoje idem, medido 2026-09-20).

**Pronto quando:** os cinco literais de saída imprimem `0`, os cinco de entrada imprimem `1`, o comando de cadeia imprime `0` para os dois arquivos, as contagens de `Ato de modelo` subiram como declarado, `check-drift` sai `0`, e **nenhum elo da tabela da cadeia contradiz outro** — a rota revisor → despacho → leitura → roteamento → modelador fecha de ponta a ponta. Nenhum item deste `Pronto quando` se apoia em frase escrita pelo executor sobre a própria entrega (`I-11`, `D-22`).

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20
- **Depende de:** `DOM-T5a`
- **Fundamento:** `D-5`, `D-6`, `D-8`, `D-23`; invariantes `I-3`, `I-11`, `I-13`, `I-14`; achados `AE-11`, `AE-13`, `AE-14`. Card corretivo criado no escalonamento `ESC-5` (consultor de plano, 2026-09-20). A `DOM-T5a` fechou a contradição **dentro** de `pantonic-reviewer.md`; o `scrum-master` a reimpõe no ato do despacho, que é onde a instrução de fato vincula o revisor. **Este card fecha a cadeia inteira de uma vez**, e não o próximo elo.
- **Oração do modelo:** `M-9`, `M-10` - M-9: Nenhum outro papel escreve no modelo, e nenhum agente aciona outro agente: quem precisa de um ato de modelo devolve um dossiê fechado na própria linha de retorno, e quem conduz a sessão despacha o modelador. - M-10: O revisor volta a não ter ferramenta de escrita fora do laudo: divergência entre a entrega e o texto da operação vira achado, e o texto fica como está.
- **Camada e fronteira:** skill de orquestração e definição de agente. Nenhum código, nenhum teste, **nenhuma mudança de front matter** — portanto nenhum drift em `.claude/README.md`.
- **Contratos/classes:** nenhum. O contrato que muda é o **da linha de retorno do revisor**, e ele já está escrito em `GOVERNANCA.md` §3.2: duas linhas fixas e, quando houver, o dossiê `Ato de modelo` de seis campos anexo abaixo delas.
- **Passos:** 1. Substituir as linhas 127-128 de `.claude/skills/scrum-master/SKILL.md` pelo **bloco K**. 2. Substituir a linha 129 pelo **bloco L**. 3. Substituir as linhas 134-136 pelo **bloco M**. 4. Substituir a linha 141 pelo **bloco N**. 5. Substituir as linhas 51-52 de `.claude/agents/pantonic-reviewer.md` pelo **bloco O**. 6. Percorrer a cadeia inteira com o comando de residuo da `Verificação` e conferir que os elos marcados **correto** na tabela acima seguem intocados. 7. Imprimir cada região entregue e devolver, na linha de retorno, o **sinal** `fidelidade conferida: bloco K, L, M, N, O` — sinal, não prova (`I-11`). 8. Rodar as verificações abaixo.
- **Restrições desta tarefa:** - **Um bloco literal por ponto** (`I-13`): cinco pontos, cinco blocos. Nenhum passo manda redigir. - **Tripwire de replanejamento (`D-23`).** A tabela da cadeia acima é **exaustiva**, medida no `ESC-5`. Se a execução encontrar um **sexto** ponto da mesma família — frase que proíba, conte ou transporte a linha de retorno do revisor e que não esteja na tabela —, **não corrija e não redija**: pare, sinalize `blocked` razão `premissa` e devolva a linha encontrada. Um sexto ponto significa que a superfície não está delimitada, e a resposta é **replanejar**, não um sexto card corretivo. - Nada de front matter em nenhum dos dois arquivos; `tools` do reviewer continua **sem** `Edit` (`D-8`). Sem mudança de front matter não há região gerada a regenerar (`I-7`, `I-9`). - Texto entra verbatim dos cinco blocos (`I-3`); a prova de fidelidade é comando, não declaração (`I-11`). - Nenhuma contingência deste card cria arquivo (`I-10`). - Não commitar (`I-6`).
- **Não fazer:** - Não tocar `GOVERNANCA.md` §3.2 nem `docs/RUBRICA_DE_REVISAO.md` §6: os dois elos de norma da tabela foram conferidos no `ESC-5` e **estão corretos**. A linha do revisor na tabela de papéis da §3.2 descreve o que ele faz **diante do modelo**, e o parágrafo seguinte já manda devolver o dossiê na própria linha de retorno — não há omissão a fechar ali. - Não tocar os passos `5a` (107), 7 (127) e o bullet de fronteira (150) de `pantonic-reviewer.md`: entregas aprovadas da `DOM-T5` e da `DOM-T5a`. - Não tocar os blocos B (passo 8, linha 150) e C (passo 9) do `scrum-master`: entregas aprovadas. - Não tocar `.claude/agents/pantonic-planner.md`, `pantonic-consultant.md`, `pantonic-model-designer.md`, `README.md` nem `.claude/README.md`. - Não acrescentar a nenhum agente instrução de despachar outro agente (`D-6`).
- **Contingências:** 1. Se alguma das cinco faixas não casar com o conteúdo descrito → localizar o ponto por conteúdo, com os literais de saída da `Verificação`, e seguir. Se um literal de saída imprimir mais de `1` → parar e sinalizar `blocked` razão `premissa`, com as linhas encontradas.
- **Testes:** nenhum teste automatizado — a entrega é definição de conduta e de orquestração.
- **Fora do escopo desta tarefa:** a documentação pública e o `README.md` (`DOM-T6`), a norma e a rubrica (elos conferidos e corretos), e qualquer ato de modelo sobre plano real.

## Execução

**Consumo:** 10 tool uses, 57.7 k tokens, 50.2 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: fidelidade conferida: bloco K, L, M, N, O; conferida pelo revisor byte a byte em Python
laudo: A tabela dos doze elos nao e exaustiva: a linha Entrada do passo 8 do scrum-master omite o dossie Ato de modelo que o passo 7 lhe entrega e que a saida do mesmo passo consome; decimo terceiro elo, criado pela DOM-T5, fora dos cinco blocos desta entrega. D-23 manda replanejar, nao abrir sexto card

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

O tripwire do D-23 cumpriu a função para a qual foi escrito: em vez de um sexto card corretivo fechar mais um elo e descobrir o seguinte, a condição de parada estava decidida antes e a rota é replanejamento. O que a superfície medida do ESC-5 não alcançou foi um elo criado pela própria DOM-T5 — a linha Entrada do passo 8 —, o que mostra que varredura de cadeia precisa reincluir os pontos que as entregas anteriores da mesma janela criaram, não só os que existiam antes dela.

## Fechamento

**Desdobramento:** aprovado
