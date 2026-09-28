# RDO — P-0748 · TLG-T5a

**Plano:** `docs/plans/P-0748-tela-do-gerente.md`
**Tarefa:** `TLG-T5a` — A célula da scrum-master na tabela de skills volta a dizer quando a janela encerra
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O mantenedor da porta de entrada do repositório reescreve a descrição pública de como o dono acompanha a execução — o painel fora da extensão e como se lê a linha de cada passo —, e essa própria tarefa corre pelo loop já modificado, com o dono lendo nesse painel o fluxo em linguagem humana e dando o aceite final.

**Arquivos-alvo:** - `README.md:841` — a linha da tabela de skills da scrum-master, que contém encerra a janela; a cada transição (única no arquivo, medida 2026-09-24; localizar pelo texto)

**Verificação:** 1. `pwsh -NoProfile -File .claude/checks/check-readme.ps1; $LASTEXITCODE` → `check-readme: OK - 10 agente(s), 11 skill(s), 20 guardrail(s), versão '0.0.0', 14 seção(ões) com Fonte da verdade válida; frases de contagem de 'Os guardrails' conferidas: 'regras mínimas obrigatórias'=True, 'regras falham como teste executável'=True.` e `0` (medido 2026-09-24 antes da edição; a edição não muda contagem). 2. `(Select-String -SimpleMatch -Path README.md -Pattern "progresso pelo fim do plano" | Measure-Object).Count` → antes `1` (medido 2026-09-24), depois `0`. 3. `(Select-String -SimpleMatch -Path README.md -Pattern "encerra a janela pelo fim do plano ou pela condição de contexto; a cada transição" | Measure-Object).Count` → antes `0` (medido 2026-09-24), depois `1`. 4. `(Select-String -SimpleMatch -Path README.md -Pattern "gera a linha em linguagem humana" | Measure-Object).Count` → antes `1` (medido 2026-09-24), depois `1`.

**Pronto quando:** `stream de dados.descrição pública` — *a porta de entrada diz ao leitor que a execução se acompanha num painel fora da extensão, que mostra o arquivo de progresso com uma linha em linguagem humana a cada passo; diz como abrir esse painel e mostra como a linha se lê* — Verificação 2, 3 e 4 (a célula deixa de dizer que o gerente lê o painel "pelo fim do plano").

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-24
- **Fundamento:** `DTG-41` (c), `DTG-44`, `DTG-48`, `AE-15`, `I-9`, `F-15`.
- **Depende de:** `TLG-T3f`
- **Operação do modelo:** `OP-5` - OP-5: O mantenedor da porta de entrada do repositório reescreve a descrição pública de como o dono acompanha a execução — o painel fora da extensão e como se lê a linha de cada passo —, e essa própria tarefa corre pelo loop já modificado, com o dono lendo nesse painel o fluxo em linguagem humana e dando o aceite final. - precisa de: stream de dados — Quem implementa recebe o loop do condutor — as transições que ele atravessa a cada tarefa e o que ele tem em mãos em cada uma —, a função do kit que gera a linha a partir do evento de cada transição, e o arquivo de progresso onde essa função grava. A ferramenta que roda os agentes e o painel que mostra o arquivo ficam como estão.; tela do monitor — Quem implementa não mexe nela: o dono abre o painel e só o observa, na validação do fim. A sonda do começo foi feita no painel da extensão, e foi o que ela viu que tirou a tela de lá.
- **Camada e fronteira:** documentação pública (`README.md`): um trecho da célula de descrição da linha `scrum-master` na tabela de skills. Nada mais.
- **Domínio:** *célula da `scrum-master`* = a linha da tabela de skills do `README.md` que começa por `` | `scrum-master` | Ponto de entrada da execução de backlog ``; o complemento `pelo fim do plano ou pela condição de contexto` rege `encerra a janela` (é o texto do `HEAD`), e a `TLG-T5` o deixou regendo `lê no painel` (`AE-15`).
- **Contratos/classes:** nenhum código.
- **Texto novo, literal:** na linha `README.md:841`, substituir o trecho `encerra a janela; a cada transição, um gancho do kit gera a linha em linguagem humana que o gerente lê no painel do arquivo de progresso pelo fim do plano ou pela condição de contexto.` por `encerra a janela pelo fim do plano ou pela condição de contexto; a cada transição, um gancho do kit gera a linha em linguagem humana que o gerente lê no painel do arquivo de progresso.` — o resto da linha, antes e depois do trecho, fica.
- **Passos:** 1. Substituir o trecho pelo texto dado. 2. Rodar a Verificação 1 a 4.
- **Restrições desta tarefa:** `I-9` — o `check-readme.ps1` sai `0` com as mesmas contagens; só esta edição.
- **Não fazer:** não editar outra linha do `README.md` nem outra célula da tabela; não reescrever a cláusula do gancho; não tocar skill, agente, instrumento ou configuração.
- **Contingências:** 1. se `(Select-String -SimpleMatch -Path README.md -Pattern "progresso pelo fim do plano" | Measure-Object).Count` não for `1` antes da edição → parar e sinalizar `blocked` razão `premissa` com a saída de `grep -n "pelo fim do plano" README.md`; 2. se `check-readme.ps1` sair diferente de `0` → parar e sinalizar `blocked` razão `premissa` com a linha impressa.
- **Testes:** nenhum TF; guarda: `pwsh -NoProfile -File .claude/checks/check-readme.ps1`.
- **Fora do escopo desta tarefa:** o parágrafo **O que é.** da `## 6` (entregue por `TLG-T5`); o gancho (`TLG-T3c`); propagação aos kits derivados (`DTG-8`).

## Execução

**Consumo:** 10 tool uses, 48.6 k tokens, 28.4 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: nenhuma; recorrencia do AE-11 (TK-55)

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
