# RDO — P-0755 · RAF-T12a

# Humano

Tarefa "A dimensão testes declara a fonte mista e o instrumento cita a rubrica pela seção" concluída em 2026-09-29.
A dimensão testes da rubrica passa a declarar a fonte mista, e o instrumento cita a rubrica pela seção e não pela linha.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Plano "Aplicação das recomendações da auditoria final do kit": 22/50 tarefas concluídas; próxima: "A conferência do card compara o depois com o esperado e lê o literal com pontuação".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0755-recomendacoes-auditoria-final/plano.md`
**Tarefa:** `RAF-T12a` — A dimensão testes declara a fonte mista e o instrumento cita a rubrica pela seção
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa faz a rubrica de revisão declarar a dimensão `testes` de fonte mista — presença dos testes e exit da suíte mecânicos e travados, juízo sobre as linhas removidas dos testes — e faz o instrumento do dossiê e o seu teste citarem a rubrica pela seção, sem número de linha.

**Arquivos-alvo:** - `docs/RUBRICA_DE_REVISAO.md` - `.claude/tools/review_evidence.py` - `tests/test_review_evidence.py`

**Verificação:** 1. `python -c "from pathlib import Path;r=Path('docs/RUBRICA_DE_REVISAO.md').read_text(encoding='utf-8');e=Path('.claude/tools/review_evidence.py').read_text(encoding='utf-8');t=Path('tests/test_review_evidence.py').read_text(encoding='utf-8');a=lambda s:sum(s.count('.md:'+n) for n in ('63-77','79-92','94-106'));print('testes=%d-%d ancoras=%d-%d docstring=%d'%(r.count('da área tocada e a seção'),r.count('da área tocada, mecânicos e travados'),a(e),a(t),e.count('Veredito travado da parte mecânica')))"` → `testes=0-1 ancoras=0-1 docstring=1` — antes `testes=1-0 ancoras=7-4 docstring=0`, depois `testes=0-1 ancoras=0-1 docstring=1`

**Pronto quando:** - rubrica de revisão.critério da asserção removida — a dimensão `testes` declara a fonte mista, com a parte mecânica travada e o juízo sobre as linhas removidas, e o instrumento cita a rubrica pela seção — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DRF-54`; `AE-151` (laudo da `RAF-T12`, ressalva 88); `docs/RUBRICA_DE_REVISAO.md` §3 ("Dimensão de fonte mista tem a parte mecânica travada e a parte de juízo livre"); relatório `R-12`.
- **Depende de:** `RAF-T12`
- **Operação do modelo:** `OP-12` - OP-12: Quem executa acrescenta à rubrica de revisão o critério que reprova a asserção de teste removida sem que o card mande removê-la. - precisa de: relatório da auditoria final — Ninguém altera: é a fonte do que cada operação faz e de como ela se prova.; dossiê de evidência — Quem implementa corrige um caso por vez do que a evidência mostra errado ou deixa de mostrar, cada caso com o teste que o reproduz numa montagem descartável.
- **Camada e fronteira:** doutrina do kit — a régua do revisor, `docs/RUBRICA_DE_REVISAO.md`, dimensão `testes` — e o texto que cita essa régua em `.claude/tools/review_evidence.py` (docstrings e uma linha de saída) e nos docstrings de `tests/test_review_evidence.py`; nenhum comportamento muda. A trava segue a de hoje: `veredito_testes` lê o exit do `pytest`, e o `rdo.py laudo` só recusa `conforme` contra vermelho mecânico (`DA-7`); o juízo sobre as linhas removidas fica livre, como a §3 da rubrica manda para a fonte mista. As citações da rubrica por número de linha nos dois arquivos de código apontam hoje para a dimensão errada (a rubrica cresceu desde a `EXA-T9b`) e passam a citar a seção, que não envelhece.
- **Passos:** 1. Na seção da dimensão `testes` de `docs/RUBRICA_DE_REVISAO.md` (o cabeçalho de nível 3 que abre a dimensão), trocar as duas linhas do bullet `- **Fonte da evidência:**` pelas três do texto novo (as quebras são as do bloco; cada linha perde o recuo deste card). Texto antigo: ```text - **Fonte da evidência:** mecânica — presença dos arquivos de teste declarados, exit code da suíte da área tocada e a seção `## Linhas removidas dos testes` da evidência. ``` Texto novo: ```text - **Fonte da evidência:** mista — presença dos arquivos de teste declarados e exit code da suíte da área tocada, mecânicos e travados; juízo sobre cada linha da seção `## Linhas removidas dos testes` da evidência, confrontada com o que o card manda remover. ``` 2. Em `.claude/tools/review_evidence.py`, na primeira linha do docstring de `veredito_testes`, trocar `Veredito mecânico travado da dimensão` por `Veredito travado da parte mecânica da dimensão` (sem quebra nova e sem refluxo). 3. Em `.claude/tools/review_evidence.py` (sete ocorrências: seis em docstring, uma na linha de saída do veredito aberto de `escopo`) e nos docstrings de `tests/test_review_evidence.py` (três ocorrências), toda citação de `RUBRICA_DE_REVISAO.md` com sufixo de linha (`:63-77`, `:79-92` ou `:94-106`) perde o sufixo e ganha ` §4` logo depois do caminho — depois da crase que fecha o caminho, quando ele está entre crases (sem quebra nova e sem refluxo). 4. Rodar a Verificação e a suíte inteira.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim (nenhum teste novo; o piso é o total re-medido no despacho; referência datada: `566 passed`, 2026-09-29, revisão da `RAF-T12`). - `python .claude/checks/dead_code.py` não ganha achado novo: o único achado admitido é o pré-existente de `docs/audits/sonda-2026-09-28/passos.py` (`1 achado(s)`, §8 risco 5). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Em `.claude/tools/review_evidence.py` e `tests/test_review_evidence.py` só mudam as linhas das citações e a primeira linha do docstring de `veredito_testes`: nenhum código, nome, asserção nem teste muda. - Só os `Arquivos-alvo` se editam; nada fora deles se toca, se reverte ou se commita; nenhum commit. - Fora do alcance: `docs/audits/`, `docs/plans/P-0753-auditoria-estagio-1/`, `docs/plans/P-0754-auditoria-final/`, `docs/telemetria.tsv`, a pasta do usuário `~/.claude/` e `.claude/KIT_VERSION`. - Achado fora deste card não vira edição: vai na linha de retorno da entrega como achado, e a condução o registra como `AE-<n>` na §9 do plano.
- **Não fazer:** não tocar o dado de entrada de `test_tr_extrair_arquivos_alvo_ignora_texto_sem_barra_e_referencia_de_linha` (a citação com sufixo de linha ali é o que o teste prova que o extrator descarta; é a única que fica); não mudar `veredito_testes` além do docstring nem o `rdo.py`; não mudar os bullets de nível da dimensão `testes` nem a §3 da rubrica; não editar `.claude/agents/pantonic-reviewer.md` (a régua mora na rubrica).
- **Contingências:** - se o texto antigo do passo 1 ou o trecho do passo 2 não existir verbatim → parar e sinalizar `blocked` razão `premissa`, nomeando o passo. - se as citações com sufixo de linha não forem sete em `.claude/tools/review_evidence.py` e quatro em `tests/test_review_evidence.py` (as três dos docstrings e a do dado de entrada) → parar e sinalizar `blocked` razão `premissa`, com a contagem medida. - se o sistema de permissão negar a edição de um arquivo-alvo → não refazer a mesma mudança por outra ferramenta nem por outro canal; fazer as demais edições do card, parar e sinalizar `blocked` razão `ferramenta`, com o caminho e o texto exato da edição negada na linha de retorno (§4 invariante 13).
- **Testes:** nenhum teste novo; `tests/test_review_evidence.py` e a suíte inteira.
- **Fora do escopo desta tarefa:** a trava do laudo (`rdo.py`, `DA-7`), que já só recusa `conforme` contra vermelho; citações da rubrica por número de linha em registro histórico (diário).
- **Handover:** 2026-09-29 · para quem vier depois - **Entregue:** rubrica: dimensão testes declara fonte mista (parte mecânica travada, juízo livre sobre as linhas removidas); review_evidence.py e test_review_evidence.py citam a rubrica por §4 no lugar do número de linha - **Contrato:** nenhuma citação da rubrica por número de linha no instrumento, exceto o dado de entrada do teste do extrator - **Não refazer:** o bullet de fonte mista e as dez citações - **Pendente:** nenhum

## Execução

**Consumo:** 28 tool uses, 68.9 k tokens, 237.6 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master concluiu a tarefa "A rubrica reprova a asserção de teste removida sem ordem do card" e vai pegar a tarefa "A dimensão testes declara a fonte mista e o instrumento cita a rubrica pela seção".
Tarefa "A dimensão testes declara a fonte mista e o instrumento cita a rubrica pela seção". Passo: conferir os gates e preparar o despacho.
Agente executor recebe a tarefa "A dimensão testes declara a fonte mista e o instrumento cita a rubrica pela seção" e vai executar: Quem executa faz a rubrica de revisão declarar a dimensão `testes` de fonte mista — presença dos testes e exit da suíte mecânicos e travados, juízo sobre as linhas removidas dos testes — e faz o instrumento do dossiê e o seu teste citarem …
Agente executor devolveu a tarefa "A dimensão testes declara a fonte mista e o instrumento cita a rubrica pela seção": review — sem pendência.
Tarefa "A dimensão testes declara a fonte mista e o instrumento cita a rubrica pela seção": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "A dimensão testes declara a fonte mista e o instrumento cita a rubrica pela seção" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "A dimensão testes declara a fonte mista e o instrumento cita a rubrica pela seção": ressalva 91%, bloqueante nenhuma, recomendação seguir com ressalva.
Scrum master vai fechar a tarefa "A dimensão testes declara a fonte mista e o instrumento cita a rubrica pela seção" como done: registrar estado, RDO e telemetria.
