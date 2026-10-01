# RDO — P-0755 · RAF-T8a

# Humano

Tarefa "A rubrica nomeia o rótulo do registro da orquestração" concluída em 2026-09-29.
A rubrica de revisão passa a nomear o terceiro rótulo dos arquivos tocados, o do registro da orquestração.
Revisão: aprovada com ressalva (88%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 14/46 tarefas concluídas; próxima: "O curinga do alvo casa como na linha de comando".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T8a` — A rubrica nomeia o rótulo do registro da orquestração
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz a frase da rubrica de revisão que conta os rótulos da seção `## Arquivos tocados` do dossiê de evidência nomear também `registro da orquestração`, o rótulo que a `RAF-T8` criou.

**Arquivos-alvo:** - `docs/RUBRICA_DE_REVISAO.md`

**Verificação:** 1. `python -c "import sys;from pathlib import Path;t=Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8');a=t.count('(fora deles), com o estado');b=t.count('(arquivo que quem conduz escreve por ofício,');print('arquivos=%d-%d'%(a,b));sys.exit(0 if (a,b)==(0,1) else 1)"` → `exit 0` — antes `exit 1`, depois `exit 0` (imprime `arquivos=1-0` antes e `arquivos=0-1` depois)

**Pronto quando:** - dossiê de evidência.rótulo do registro da orquestração — a rubrica nomeia o rótulo que a lista do dossiê usa — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-50`; `AE-137` (laudo da `RAF-T8`, ressalva 91); `DRF-12`; relatório `R-14`.
- **Depende de:** `RAF-T8`
- **Operação do modelo:** `OP-8` - OP-8: Quem executa acerta duas marcas do dossiê de evidência: a de arquivo novo, que passa a valer também para o que não é texto, e a do registro da orquestração, que passa a ter o mesmo nome na lista e no resumo. - precisa de: dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável.; casos registrados pela auditoria — Ninguém altera: cada caso se monta de novo dentro do teste, e é a resposta do kit a ele que prova a mudança.
- **Camada e fronteira:** doutrina do kit — a régua do revisor, `docs/RUBRICA_DE_REVISAO.md`, o parágrafo que abre com a seção `## Arquivos tocados` do dossiê de evidência, antes da nota de 2026-09-19; nenhum código muda. A frase segue dizendo que a atribuição vem da `confrontar_escopo`, que é onde o balde do registro da orquestração nasce.
- **Passos:** 1. Trocar a linha do texto antigo pelas duas do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card; as linhas vizinhas não mudam e não refluem). Texto antigo: ```text `Arquivos-alvo` da tarefa) ou `alheio` (fora deles), com o estado `git` que comprova a marcação — ``` Texto novo: ```text `Arquivos-alvo` da tarefa), `registro da orquestração` (arquivo que quem conduz escreve por ofício, sem peso no veredito) ou `alheio` (os demais), com o estado `git` que comprova a marcação — ``` 2. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `552 passed`, 2026-09-29, depois da `RAF-T8`). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - O arquivo segue com fim de linha LF (medido 2026-09-29: nenhum CR). - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não mudar a nota de 2026-09-19 nem a dimensão `escopo`; não mexer na dimensão `testes` (é da `RAF-T12`); não editar `.claude/tools/review_evidence.py` nem `.claude/agents/pantonic-reviewer.md`.
- **Contingências:** - se o texto antigo do passo 1 não existir verbatim em `docs/RUBRICA_DE_REVISAO.md` → parar e sinalizar `blocked` razão `premissa`. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo: a mudança é de redação e a prova é o recorte do literal na Verificação 1. Regressão: a suíte inteira.
- **Fora do escopo desta tarefa:** o critério da asserção removida (`RAF-T12`); o curinga do alvo (`RAF-T9`).
- **Handover:** 2026-09-29 · para `RAF-T12` - **Entregue:** docs/RUBRICA_DE_REVISAO.md §3 nomeia os três rótulos de '## Arquivos tocados': da entrega, alheio e registro da orquestração (arquivo que quem conduz escreve por ofício, sem peso no veredito) - **Contrato:** a rubrica e o review_evidence.py usam o mesmo nome para o registro da orquestração - **Não refazer:** a troca da frase da rubrica - **Pendente:** nenhum

## Execução

**Consumo:** 9 tool uses, 49.4 k tokens, 125.8 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 88%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "O binário novo leva a marca de novo e o registro da orquestração tem um nome só" e vai pegar a tarefa "A rubrica nomeia o rótulo do registro da orquestração".
Tarefa "A rubrica nomeia o rótulo do registro da orquestração". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "A rubrica nomeia o rótulo do registro da orquestração" e vai executar: Quem executa faz a frase da rubrica de revisão que conta os rótulos da seção `## Arquivos tocados` do dossiê de evidência nomear também `registro da orquestração`, o rótulo que a `RAF-T8` criou.
Agente executor devolveu a tarefa "A rubrica nomeia o rótulo do registro da orquestração": review — sem pendência.
Tarefa "A rubrica nomeia o rótulo do registro da orquestração": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A rubrica nomeia o rótulo do registro da orquestração" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A rubrica nomeia o rótulo do registro da orquestração": ressalva 88%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "A rubrica nomeia o rótulo do registro da orquestração" como done: registrar estado, RDO e telemetria.
