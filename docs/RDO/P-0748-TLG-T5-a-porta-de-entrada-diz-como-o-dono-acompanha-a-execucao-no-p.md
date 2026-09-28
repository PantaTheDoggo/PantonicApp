# RDO — P-0748 · TLG-T5

**Plano:** `docs/plans/P-0748-tela-do-gerente.md`
**Tarefa:** `TLG-T5` — A porta de entrada diz como o dono acompanha a execução no painel
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O mantenedor da porta de entrada do repositório reescreve a descrição pública de como o dono acompanha a execução — o painel fora da extensão e como se lê a linha de cada passo —, e essa própria tarefa corre pelo loop já modificado, com o dono lendo nesse painel o fluxo em linguagem humana e dando o aceite final.

**Arquivos-alvo:** - `README.md:442` — a linha que contém ele lê um relatório no fim (única no arquivo, re-medida 2026-09-24) - `README.md:831` — a linha da tabela de skills da scrum-master, que contém roteia pelo veredito calculado e encerra a janela (única no arquivo, re-medida 2026-09-24)

**Verificação:** 1. `pwsh -NoProfile -File .claude/checks/check-readme.ps1; $LASTEXITCODE` → `check-readme: OK - 10 agente(s), 11 skill(s), 20 guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade válida; frases de contagem de 'Os guardrails' conferidas: 'regras mínimas obrigatórias'=True, 'regras falham como teste executável'=True.` e `0` (re-medido em 2026-09-24 nesta rodada; as contagens não mudam). 2. `(Select-String -SimpleMatch -Path README.md -Pattern "Repertório de mensagens ao gerente" | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `1`. 3. `(Select-String -SimpleMatch -Path README.md -Pattern "ele lê um relatório no fim" | Measure-Object).Count` → antes `1` (medido 2026-09-24), depois `0`. 4. `(Select-String -SimpleMatch -Path README.md -Pattern "gera a linha em linguagem humana" | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `1`. 5. `(Select-String -SimpleMatch -Path README.md -Pattern "Get-Content -Path .claude/estado/progresso.txt -Wait -Tail 30 -Encoding utf8" | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `1`. 6. `(Select-String -SimpleMatch -Path README.md -Pattern "progresso_hook.py" | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `1`.

**Pronto quando:** `stream de dados.descrição pública` — *a porta de entrada diz ao leitor que a execução se acompanha num painel fora da extensão, que mostra o arquivo de progresso com uma linha em linguagem humana a cada passo; diz como abrir esse painel e mostra como a linha se lê* — Verificação 2, 3, 4, 5 e 6. O veredito do dono sobre o painel **durante** esta tarefa é o Marco 3 (aceite de marco, `+ dono`, registrado na tabela de marcos do plano pela orquestração — `I-6`), e no mesmo ato ele valida a versão 3 da `## 1A`.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-24
- **Fundamento:** `DTG-6` (corpus real: esta tarefa é o Marco 3), `DTG-27` (o painel e o comando que o abre), `DTG-30` e `DTG-33` (linha gerada, com o título), `DTG-36` (`DTG-14` caída: nenhuma reabertura de sessão; o `README` cita a seção da skill e mostra duas linhas de exemplo, não recopia), `DTG-37` (última tarefa), `F-15` (saída do `check-readme.ps1`, re-medida em 2026-09-24), `F-28` (âncoras do `README`, re-medidas em 2026-09-24), `I-6`, `I-9`, `I-12`.
- **Depende de:** `TLG-T4a`
- **Operação do modelo:** `OP-5` - OP-5: O mantenedor da porta de entrada do repositório reescreve a descrição pública de como o dono acompanha a execução — o painel fora da extensão e como se lê a linha de cada passo —, e essa própria tarefa corre pelo loop já modificado, com o dono lendo nesse painel o fluxo em linguagem humana e dando o aceite final. - precisa de: stream de dados — Quem implementa recebe o loop do condutor — as transições que ele atravessa a cada tarefa e o que ele tem em mãos em cada uma —, a função do kit que gera a linha a partir do evento de cada transição, e o arquivo de progresso onde essa função grava. A ferramenta que roda os agentes e o painel que mostra o arquivo ficam como estão.; tela do monitor — Quem implementa não mexe nela: o dono abre o painel e só o observa, na validação do fim. A sonda do começo foi feita no painel da extensão, e foi o que ela viu que tirou a tela de lá.
- **Camada e fronteira:** documentação pública (`README.md`): um trecho do parágrafo **O que é.** da `## 6. O loop de execução` e um trecho da célula de descrição da linha `scrum-master` na tabela de skills. Nenhuma skill, agente, instrumento ou configuração. O dono abre o painel (`DTG-27`) **antes** do despacho deste card, na mesma sessão — nenhuma reabertura é necessária (`AE-6`, `DTG-36`).
- **Domínio:** *porta de entrada* = `README.md`; *descrição pública* = o que um leitor sem acesso às skills entende sobre como se acompanha a execução; *painel* = o terminal integrado do VS Code rodando `Get-Content -Path .claude/estado/progresso.txt -Wait -Tail 30 -Encoding utf8` na raiz do repositório (`DTG-27`); *linha gerada* = a frase que o gancho grava no evento da transição, com o título da tarefa entre aspas no lugar da sigla (`I-12`).
- **Contratos/classes:** nenhum código.
- **Texto novo, literal:** na linha `README.md:442`, substituir o trecho `o gerente não medeia tarefa a tarefa — ele lê um relatório no fim.` (o resto da linha, antes e depois do trecho, fica) por: ``` o gerente não medeia tarefa a tarefa: acompanha a execução num painel fora da extensão do editor, que mostra o arquivo de progresso `.claude/estado/progresso.txt` com uma linha em linguagem humana por transição — por exemplo `Tarefa "A porta de entrada diz como o dono acompanha a execução no painel". Passo: conferir os gates e preparar o despacho.` e `Agente revisor devolveu a tarefa "A porta de entrada diz como o dono acompanha a execução no painel": aprovado 100%, bloqueante nenhuma.` —, gerada por um gancho do kit (`.claude/tools/progresso_hook.py`) a partir do evento de cada transição do loop, com o título da tarefa no lugar da sigla e sem nenhuma saída de ferramenta entre duas linhas; as frases estão na seção *Repertório de mensagens ao gerente* da `scrum-master`. Para abrir o painel, no terminal integrado do VS Code, na raiz do repositório: `Get-Content -Path .claude/estado/progresso.txt -Wait -Tail 30 -Encoding utf8` (o arquivo nasce com a primeira linha gerada). No fim da janela, o gerente lê um relatório. ``` Na tabela de skills, na linha `README.md:831`, substituir o trecho `roteia pelo veredito calculado e encerra a janela` por `roteia pelo veredito calculado e encerra a janela; a cada transição, um gancho do kit gera a linha em linguagem humana que o gerente lê no painel do arquivo de progresso`.
- **Passos:** 1. Substituir o trecho da linha `README.md:442` pelo texto dado. 2. Substituir o trecho da linha `README.md:831` pelo texto dado. 3. Rodar a Verificação 1 a 6.
- **Restrições desta tarefa:** `I-9` — o `check-readme.ps1` sai `0`; `DTG-36` — o `README` cita a seção da skill e mostra duas linhas de exemplo, não recopia o repertório; nenhuma contagem do `README` muda (nenhum agente, skill ou guardrail do kit é acrescentado — `F-15`). Só estas duas edições.
- **Não fazer:** não acrescentar seção nova ao `README`; não reescrever o resto da `## 6`; não editar `README.md:100` (a `passagem-de-bastao` continua transparente ao gerente); não editar `.claude/README.md`; não tocar skill, agente, instrumento, `projecoes.json` ou `settings.json`; não quebrar o comando `Get-Content` em duas linhas; não escrever "reabrir a sessão".
- **Contingências:** 1. se `check-readme.ps1` sair diferente de `0` → parar e sinalizar `blocked` razão `premissa` com a linha impressa; 2. se o trecho `ele lê um relatório no fim` não aparece exatamente uma vez no `README.md` → parar e sinalizar `blocked` razão `premissa` com a saída de `grep -n "relatório no fim" README.md`; 3. se o trecho `roteia pelo veredito calculado e encerra a janela` não aparece exatamente uma vez no `README.md` → parar e sinalizar `blocked` razão `premissa` com a saída de `grep -n "roteia pelo veredito calculado" README.md`.
- **Testes:** nenhum TF; guarda: `pwsh -NoProfile -File .claude/checks/check-readme.ps1`.
- **Fora do escopo desta tarefa:** propagação aos kits derivados (`DTG-8`, tíquete próprio no fechamento do plano); qualquer retroação que o Marco 3 peça (rodada tática sobre `TLG-T3b`, `TLG-T2b` ou `TLG-T4a`, `R-4`, `R-6`).

## Execução

**Consumo:** 11 tool uses, 59.0 k tokens, 97.3 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: nenhuma; achados de processo registrados como AE-15 (README:831) e recorrencia do AE-11 (TK-55)

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
