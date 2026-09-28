# RDO — P-0752 · FPU-T8

# Humano

Tarefa "As armadilhas de ferramenta medidas ganham um arquivo só" concluída em 2026-09-26.
As armadilhas de ferramenta já medidas passam a morar num arquivo só, com a forma segura de cada uma, e a doutrina e o planejador apontam para ele.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Fato no ponto de uso: os mecanismos contra o esquecimento e a assunção": 12/15 tarefas concluídas; próxima: "A skill de fatos frescos".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achado registrado no plano, com rota: 1 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/plans/P-0752-fato-no-ponto-de-uso.md`
**Tarefa:** `FPU-T8` — As armadilhas de ferramenta medidas ganham um arquivo só
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `docs/ARMADILHAS_DE_FERRAMENTA.md` existe com a tabela `| ferramenta | armadilha | caso medido | forma segura |` e as oito linhas de F-11; `GOVERNANCA.md` §3 (bullet *Disciplina de coleta*, linha 214) e `pantonic-planner.md` (campo `Verificação`, linha 450) apontam para ele, e o planejador passa a preferir `python -c` a shell em linha de Verificação.

**Arquivos-alvo:** - `docs/ARMADILHAS_DE_FERRAMENTA.md` (novo) - `GOVERNANCA.md:214` — `- **Disciplina de coleta** — \`git status --short\`/\`git log --oneline\` no lugar dos completos;` - `.claude/agents/pantonic-planner.md:450` — `- **Verificação:** comandos exatos, executáveis como estão; para tarefa sem artefato executável,` - `docs/DOC_MAP.md` (entrada do arquivo novo, logo depois do bloco `## docs/ACIONAMENTOS_CONSULTOR.tsv`; DFP-20)

**Verificação:** 1. `python -c "from pathlib import Path;p=Path('docs/ARMADILHAS_DE_FERRAMENTA.md');print(p.exists() and p.read_text(encoding='utf-8').count('|')>=40)"` → `True` (oito linhas de quatro colunas mais cabeçalho) — antes `False`, depois `True`. 2. `python -c "from pathlib import Path;print(Path('GOVERNANCA.md').read_text(encoding='utf-8').count('ARMADILHAS_DE_FERRAMENTA'))"` → `1` — antes `0`, depois `1`. 3. `python -c "from pathlib import Path;print(Path('.claude/agents/pantonic-planner.md').read_text(encoding='utf-8').count('ARMADILHAS_DE_FERRAMENTA'))"` → `1` — antes `0`, depois `1`. 4. `pwsh .claude/checks/kit_check.ps1` → exit 0 — antes `exit 0`, depois `exit 0` (trava). 5. `python -c "from pathlib import Path;p=Path('docs/ARMADILHAS_DE_FERRAMENTA.md');print(p.exists() and '| forma segura |' in p.read_text(encoding='utf-8') and 'git ls-files --others' in p.read_text(encoding='utf-8'))"` → `True` — antes `False`, depois `True`. 6. `python -c "from pathlib import Path;print(Path('docs/DOC_MAP.md').read_text(encoding='utf-8').count('## docs/ARMADILHAS_DE_FERRAMENTA.md'))"` → `1` — antes `0`, depois `1`.

**Pronto quando:** armadilhas de ferramenta.residência — um arquivo, apontado pela doutrina e pela régua do card — Verificações 1 a 3, 5 e 6.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-26
- **Operação do modelo:** `OP-8` - OP-8: As armadilhas de ferramenta medidas ganham um arquivo só, apontado pela doutrina e pela régua do card. - precisa de: régua executável — Quem implementa acrescenta a conferência como código que falha ruidosamente no ato; nenhuma conferência nova entra como frase de skill.
- **Fundamento:** F-11, causa 5 de F-10, DFP-20.
- **Passos:** 1. Escrever o arquivo: cabeçalho de uma frase (o que é, quem apensa: quem mede uma armadilha nova apensa uma linha), a tabela com as oito linhas de F-11 (uma por armadilha, com o caso medido e o ponteiro), e a regra `linha de Verificação prefere python -c a shell; PowerShell só com pwsh -Command e aspas simples`. Linhas na ordem de F-11; `caso medido` é o ponteiro entre parênteses de F-11, salvo na linha 4, cujo ponteiro vira `card_check.py`, função `_rodar_comando` (o de F-11 derivou); `armadilha` é o texto de F-11, salvo na linha 1; `ferramenta` e `forma segura` são os textos abaixo, transcritos (DFP-20: cada forma medida pelo consultor); barra vertical dentro de célula vai escapada, `\|`: - linha 1 — ferramenta `PowerShell`; armadilha (re-medida, DFP-20): em aspas duplas o PowerShell expande `` `t `` e `$nome`, e `\t` fica como está; quem converte `\t` em tabulação é o literal Python dentro de `python -c "…"` — forma segura: aspas simples no PowerShell, onde nada se expande; em `python -c`, o `\t` que é texto vai em literal cru `r'…'`. - linha 2 — ferramenta `PowerShell` — forma segura: `-CaseSensitive` explícito, ou a contagem em `python -c` com `str.count`, que distingue caixa. - linha 3 — ferramenta `PowerShell` — forma segura: `(Get-Content f).Count`, ou `len(Path(f).read_text(encoding='utf-8').splitlines())` em `python -c`. - linha 4 — ferramenta `Python` — forma segura: linha de Verificação é um processo só, sem `;`, `\|` nem `>`; o filtro e a contagem vão dentro do próprio `python -c`. - linha 5 — ferramenta `git` — forma segura: listar os não rastreados à parte, com `git ls-files --others --exclude-standard`. - linha 6 — ferramenta `YAML` — forma segura: valor de `description` sem dois-pontos-espaço (trocar por ` - `) ou entre aspas duplas; conferir com `python .claude/checks/frontmatter_yaml.py <arquivo>`. - linha 7 — ferramenta `markdown` — forma segura: o literal de aceite se copia da linha física do arquivo, nunca do texto renderizado nem através de quebra de linha, e se confirma antes de publicar com `python -c` que imprime a contagem dele no arquivo. - linha 8 — ferramenta `Python` — forma segura: `python -X utf8`, ou `sys.stdout.reconfigure(encoding='utf-8')` antes do primeiro `print`. 2. `GOVERNANCA.md:214`: o bullet termina em `GOVERNANCA.md:217` — `não-teste redireciona a saída para arquivo e lê só o fim.`; trocar esse ponto final pela frase `; armadilhas de ferramenta medidas: \`docs/ARMADILHAS_DE_FERRAMENTA.md\` — consultar antes de escrever linha de Verificação` seguida de ponto final. 3. `.claude/agents/pantonic-planner.md:450` (bullet de duas linhas, 450-451): depois do ponto final da linha 451, acrescentar a frase `Prefira \`python -c\` a shell; as armadilhas medidas estão em \`docs/ARMADILHAS_DE_FERRAMENTA.md\`.` 4. `docs/DOC_MAP.md`: logo depois do bloco `## docs/ACIONAMENTOS_CONSULTOR.tsv` (quatro linhas, título e três campos), acrescentar uma linha vazia e o bloco `## docs/ARMADILHAS_DE_FERRAMENTA.md`, com as três linhas `**Propósito:** armadilhas de ferramenta medidas — a semântica que já enganou um agente, o caso medido e a forma segura, uma linha por armadilha; quem mede uma armadilha nova apensa uma linha.`, `**Quando consultar:** antes de escrever linha de Verificação ou comando de medida.` e `**Acesso:** Read integral.`
- **Não fazer:** não apagar a memória `powershell-contagem-de-linhas` (fora do repositório, I-1); não reescrever linhas de Verificação de card vivo (I-3); não reescrever as formas seguras do Passo 1 (medidas na DFP-20).
- **Contingências:** - se o bloco `## docs/ACIONAMENTOS_CONSULTOR.tsv` não estiver mais em `docs/DOC_MAP.md` → acrescentar o bloco do Passo 4 no fim do arquivo.
- **Handover:** 2026-09-26 · para `FPU-T9` - **Entregue:** docs/ARMADILHAS_DE_FERRAMENTA.md (tabela | ferramenta | armadilha | caso medido | forma segura |, oito linhas de F-11 com a forma segura medida pela DFP-20); ponteiros em GOVERNANCA.md:217 (Disciplina de coleta), .claude/agents/pantonic-planner.md:450-451 (campo Verificacao) e docs/DOC_MAP.md - **Contrato:** quem mede armadilha nova apensa uma linha ao arquivo; linha de Verificacao prefere python -c a shell - **Não refazer:** arquivo de armadilhas e ponteiros ja pagos - **Pendente:** docs/RUBRICA_DE_REVISAO.md secao 8 (regua de autoria do card) sem ponteiro para o arquivo; armadilha do heredoc Bash (\ vira \) medida pelo consultor e fora da tabela
- **Notas de execução:** - 2026-09-26 `done` — fechada por `encerrar.py`: RDO `docs/RDO/P-0752-FPU-T8-as-armadilhas-de-ferramenta-medidas-ganham-um-arquivo-so.md`, veredito aprovado 100%

## Execução

**Consumo:** 18 tool uses, 71.9 k tokens, 136.3 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa

A 1a execução parou em blocked premissa (forma segura ausente em F-11) e custou um acionamento de consultor; a reexecução, com as oito formas seguras medidas e transcritas no Passo 1 (DFP-20), fechou sem nenhuma decisão do executor - card que carrega o valor medido fecha a classe G-NOASK na origem.

## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master concluiu a tarefa "O aviso de crença conta uma vez o literal que casa dois padrões" e vai pegar a tarefa "As armadilhas de ferramenta medidas ganham um arquivo só".
Tarefa "As armadilhas de ferramenta medidas ganham um arquivo só". Passo: conferir os gates e preparar o despacho.
Tarefa "As armadilhas de ferramenta medidas ganham um arquivo só": gates aprovados; vou materializar in-progress e gravar o ponto de partida.
Agente executor recebe a tarefa "As armadilhas de ferramenta medidas ganham um arquivo só" e vai executar: `docs/ARMADILHAS_DE_FERRAMENTA.md` existe com a tabela `| ferramenta | armadilha | caso medido | forma segura |` e as oito linhas de F-11; `GOVERNANCA.md` §3 (bullet *Disciplina de coleta*, linha 214) e `pantonic-planner.md` (campo `Verifi…
Agente executor devolveu a tarefa "As armadilhas de ferramenta medidas ganham um arquivo só": blocked — motivo premissa: defeito=ambiguidade: Objetivo (linha 629) e o objeto "armadilhas de ferramenta" do modelo (linha 36) exigem a tabela `| ferramenta | armadilha | caso medido | forma segura |` com as oito linhas de F-11; o Passo 1 (linha 637) só manda transcrever de F-11 "uma por armadilha, com o caso medido e o ponteiro" — omite de onde vem a coluna `forma segura`. F-11 (linha 159, fonte declarada da tabela) registra, para cada uma das oito armadilhas, só o texto da armadilha e o caso medido entre parênteses (ex.: "aspas duplas no PowerShell convertem `\t` em tabulação (`P-0740`, 2026-09-19)"; "`git stash create` não carrega não rastreado (`AE-3` do `P-0750`)"); nenhuma das oito cláusulas traz o texto da forma segura correspondente. Preencher essa coluna exigiria eu autorar/escolher o texto do reparo para cada armadilha (ex.: para `Measure-Object -Line` ignora linha vazia — usar `(Get-Content f).Count`, forma que só existe fora do plano, na memória `powershell-contagem-de-linhas`; para `git stash create` não carrega não rastreado, para `description` de frontmatter com `: ` derrubando `yaml.safe_load`, para `subprocess.run` sem `shell=True`, para escape de markdown/soft-wrap, para console cp1252 com `UnicodeEncodeError`, para `Select-String` case-insensitive, para aspas duplas convertendo `\t` — nenhuma tem forma segura literal no card nem em F-11). Não escolhi nenhum desses textos nem apliquei nenhuma edição (nenhum arquivo tocado). Referente ausente: o dado-fonte "forma segura" por armadilha, que o card cita F-11 como fonte da tabela sem ele conter..
Scrum master vai marcar a tarefa "As armadilhas de ferramenta medidas ganham um arquivo só" como blocked, sem RDO.
Agente consultor recebe a tarefa "As armadilhas de ferramenta medidas ganham um arquivo só" e vai triar.
Agente consultor devolveu a tarefa "As armadilhas de ferramenta medidas ganham um arquivo só": rota resolve.
Tarefa "As armadilhas de ferramenta medidas ganham um arquivo só": gates aprovados; vou materializar in-progress e gravar o ponto de partida.
Agente executor recebe a tarefa "As armadilhas de ferramenta medidas ganham um arquivo só" e vai executar: `docs/ARMADILHAS_DE_FERRAMENTA.md` existe com a tabela `| ferramenta | armadilha | caso medido | forma segura |` e as oito linhas de F-11; `GOVERNANCA.md` §3 (bullet *Disciplina de coleta*, linha 214) e `pantonic-planner.md` (campo `Verifi…
Agente executor devolveu a tarefa "As armadilhas de ferramenta medidas ganham um arquivo só": review — sem pendência.
Tarefa "As armadilhas de ferramenta medidas ganham um arquivo só": vou reunir para o revisor o que mudou desde o despacho, os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.
Agente revisor recebe a tarefa "As armadilhas de ferramenta medidas ganham um arquivo só" e vai confrontar a entrega com o card.
Agente revisor devolveu a tarefa "As armadilhas de ferramenta medidas ganham um arquivo só": aprovado 100%, bloqueante nenhuma.
