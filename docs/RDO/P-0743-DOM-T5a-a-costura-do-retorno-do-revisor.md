# RDO — P-0743 · DOM-T5a

**Plano:** `docs/plans/P-0743-modelo-de-dominio.md`
**Tarefa:** `DOM-T5a` — A costura do retorno do revisor
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** o passo 7 de `.claude/agents/pantonic-reviewer.md` deixando de proibir o que o passo `5a` e o bullet de fronteira do mesmo arquivo mandam fazer — o dossiê `Ato de modelo` de `conflito` volta a caber na linha de retorno, que é de onde o bloco B do `scrum-master` o lê.

**Arquivos-alvo:** - `.claude/agents/pantonic-reviewer.md` - **um** ponto: o item 7 da lista de passos, `**Retorno ao chamador**`, linhas 127-135 em 2026-09-20, do `7. **Retorno ao chamador**` até `pendência ao dono ficam no laudo, que é onde eles têm leitor.` — nove linhas, re-derivadas no despacho (`I-5`)

**Verificação:** ``` grep -c 'duas linhas, nada além' .claude/agents/pantonic-reviewer.md ``` imprime `0` (hoje imprime `1`, na linha 127, medido 2026-09-20). É a frase que contradizia o passo `5a`. ``` grep -c 'as duas linhas fixas e, quando houver, o dossiê' .claude/agents/pantonic-reviewer.md ``` imprime `1` (hoje imprime `0`) — **primeira** linha do bloco J. ``` grep -c 'pendência ao dono ficam no laudo, que é onde eles têm leitor.' .claude/agents/pantonic-reviewer.md ``` imprime `1` (hoje imprime `1`, **inalterado**) — **última** linha do bloco J: o fim da região não se perde na substituição. ``` grep -c 'devolve o dossiê e para.' .claude/agents/pantonic-reviewer.md ``` imprime `1` (hoje imprime `0`). ``` grep -c 'Ato de modelo' .claude/agents/pantonic-reviewer.md ``` imprime `2` (hoje imprime `1`, na linha 107, medido 2026-09-20): o passo `5a` e o passo 7. ``` sed -n '127,142p' .claude/agents/pantonic-reviewer.md ``` sai idêntico, linha a linha, ao conteúdo do bloco J deste card — **é este comando, e não a declaração do executor, que prova a fidelidade** (`I-11`). Quem revisa confronta a saída contra o bloco; contagem de linhas autodeclarada não é evidência (`AE-12`). ``` grep -c 'Edit' .claude/agents/pantonic-reviewer.md ``` imprime `0` (hoje imprime `0`, **inalterado**): o card não devolve ferramenta de escrita ao revisor. ``` pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift ``` sai `0` e anuncia `(10 agente(s), 11 skill(s))` — **inalterado** (hoje idem, medido 2026-09-20): sem mudança de front matter não há drift.

**Pronto quando:** os sete greps devolvem os números declarados, `sed -n '127,142p'` sai idêntico ao bloco J, `check-drift` sai `0`, e **nenhuma linha de `pantonic-reviewer.md` proíbe o que outra linha dele manda** — a cadeia revisor → loop → modelador fecha. O `Pronto quando` **não** se apoia em nenhuma frase escrita pelo executor sobre a própria entrega (`I-11`, `AE-12`).

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20
- **Depende de:** `DOM-T5`
- **Fundamento:** `D-5`, `D-6`, `D-8`, `D-21`; invariantes `I-3`, `I-11`, `I-13`; achado `AE-11`. Card corretivo criado no escalonamento `ESC-4` (consultor de plano, 2026-09-20): a `DOM-T5` nomeou **quatro** pontos no reviewer e não deu bloco literal para o **quinto**; a execução acertou em não redigir (`I-13`) e o laudo saiu `aprovado 100%` com recomendação `escalar`.
- **Oração do modelo:** `M-9`, `M-10` - M-9: Nenhum outro papel escreve no modelo, e nenhum agente aciona outro agente: quem precisa de um ato de modelo devolve um dossiê fechado na própria linha de retorno, e quem conduz a sessão despacha o modelador. - M-10: O revisor volta a não ter ferramenta de escrita fora do laudo: divergência entre a entrega e o texto da operação vira achado, e o texto fica como está.
- **Camada e fronteira:** definição de agente, em `.claude/agents/`. Nenhum código, nenhum teste, nenhuma mudança de front matter — portanto **nenhum drift** em `.claude/README.md`.
- **Contratos/classes:** nenhum.
- **Passos:** 1. Imprimir a região vigente com `sed -n '127,135p' .claude/agents/pantonic-reviewer.md` e confrontá-la com o bloco J, para confirmar as âncoras antes de editar. 2. Substituir as linhas 127-135 pelo conteúdo do bloco J, verbatim (`I-3`), preservando a indentação de três espaços das linhas de continuação do item 7, que é a do arquivo. 3. Imprimir a região entregue e devolver, na linha de retorno, o **sinal** `fidelidade conferida: bloco J` — sinal, não prova: a prova são os comandos da `Verificação` (`I-11`). 4. Rodar as verificações abaixo.
- **Restrições desta tarefa:** - **Um bloco literal por ponto** (`I-13`): este card muda **um** ponto e traz **um** bloco. Se a execução concluir que algum outro ponto do arquivo precisa mudar, **não redija** — sinalize `blocked` razão `premissa`, nomeando a linha (`D-20`). - Nada de front matter: `name`, `model`, `description` e `tools` do reviewer ficam como a `DOM-T5` os deixou. `tools` continua **sem** `Edit` (`D-8`). - Não tocar `.claude/README.md`: sem mudança de front matter não há região gerada a regenerar (`I-7`, `I-9`). - Texto entra verbatim do bloco J (`I-3`); a prova de fidelidade é comando, não declaração (`I-11`). - Nenhuma contingência deste card cria arquivo (`I-10`). - Não commitar (`I-6`).
- **Não fazer:** - Não tocar os passos `5a` (linha 107) nem o bullet de fronteira (linha 150): eles já estão corretos, são entrega aprovada da `DOM-T5`, e é o passo 7 que os contradizia. - Não tocar `.claude/skills/scrum-master/SKILL.md`: o bloco B já lê o dossiê e está aprovado. - Não tocar `.claude/agents/pantonic-planner.md`, `pantonic-consultant.md`, `README.md`, `GOVERNANCA.md` nem `docs/RUBRICA_DE_REVISAO.md`. - Não acrescentar ao reviewer nenhuma instrução de despachar agente: quem despacha é quem conduz a sessão (`D-6`).
- **Contingências:** 1. Se as linhas 127-135 não casarem com o conteúdo descrito → localizar o item 7 por `grep -n 'Retorno ao chamador' .claude/agents/pantonic-reviewer.md`, que em 2026-09-20 imprime **uma** linha, a 127, e seguir a partir dela até a linha anterior a `## Proibições` (137 em 2026-09-20). Mais de uma ocorrência → parar e sinalizar `blocked` razão `premissa`.
- **Testes:** nenhum teste automatizado — a entrega é definição de conduta.
- **Fora do escopo desta tarefa:** a documentação pública e o `README.md` (`DOM-T6`), qualquer outra linha de `pantonic-reviewer.md`, e qualquer ato de modelo sobre plano real.

## Execução

**Consumo:** 14 tool uses, 58.8 k tokens, 79.1 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: fidelidade conferida: bloco J; precedente AE-1 aplicado, reempacotamento do soft-wrap conferido pelo revisor byte a byte
laudo: A costura revisor para loop para modelador ainda nao fecha: o despacho do scrum-master (SKILL.md 128/129/134) segue mandando o revisor devolver so as duas linhas, anulando na pratica a excecao que esta entrega abriu no passo 7 e que o bloco B (150) consome

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

Segunda vez que o precedente AE-1 é exercido, e segunda vez que ele funciona: reempacotar só o ponto de soft-wrap, conferido byte a byte, fecha sem violar a I-3. O que não funcionou foi a lição escrita — o AE-1 estava registrado desde a DOM-T1 e o bloco J repetiu o defeito onze achados depois, porque nem o autor do bloco nem o despacho o consultaram. Lição que depende de ser lembrada falha; a que vira regra verificável (I-10, I-11, I-13) pega.

## Fechamento

**Desdobramento:** aprovado
