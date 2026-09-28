# Armadilhas de ferramenta medidas

Armadilhas de ferramenta medidas — a semântica que já enganou um agente, o caso medido e a forma segura, uma linha por armadilha; quem mede uma armadilha nova apensa uma linha.

| ferramenta | armadilha | caso medido | forma segura |
|---|---|---|---|
| `PowerShell` | em aspas duplas o PowerShell expande `` `t `` e `$nome`, e `\t` fica como está; quem converte `\t` em tabulação é o literal Python dentro de `python -c "…"` | (`P-0740`, 2026-09-19) | aspas simples no PowerShell, onde nada se expande; em `python -c`, o `\t` que é texto vai em literal cru `r'…'`. |
| `PowerShell` | `Select-String` é case-insensitive por padrão | (`LM-T5a`) | `-CaseSensitive` explícito, ou a contagem em `python -c` com `str.count`, que distingue caixa. |
| `PowerShell` | `Measure-Object -Line` ignora linha vazia | (memória `powershell-contagem-de-linhas`, 2026-08-08) | `(Get-Content f).Count`, ou `len(Path(f).read_text(encoding='utf-8').splitlines())` em `python -c`. |
| `Python` | `subprocess.run` sem `shell=True` trata `;` e `\|` como texto | `card_check.py`, função `_rodar_comando` | linha de Verificação é um processo só, sem `;`, `\|` nem `>`; o filtro e a contagem vão dentro do próprio `python -c`. |
| `git` | `git stash create` não carrega não rastreado | (`AE-3` do `P-0750`) | listar os não rastreados à parte, com `git ls-files --others --exclude-standard`. |
| `YAML` | `description` de frontmatter com `: ` derruba `yaml.safe_load` | (`AE-20` do `P-0747`) | valor de `description` sem dois-pontos-espaço (trocar por ` - `) ou entre aspas duplas; conferir com `python .claude/checks/frontmatter_yaml.py <arquivo>`. |
| `markdown` | escape de markdown (`\*`) e soft-wrap vazando para literal de aceite | (`AE-19`, `AE-23` do `P-0740`) | o literal de aceite se copia da linha física do arquivo, nunca do texto renderizado nem através de quebra de linha, e se confirma antes de publicar com `python -c` que imprime a contagem dele no arquivo. |
| `Python` | console cp1252 estoura `UnicodeEncodeError` ao imprimir `→` | (`TK-65b`, e de novo na autoria deste plano, 2026-09-26) | `python -X utf8`, ou `sys.stdout.reconfigure(encoding='utf-8')` antes do primeiro `print`. |
| `Bash` (ferramenta do agente) | a ferramenta Bash reduz `\\` a `\` antes de o bash ler o comando — entre aspas simples, entre aspas duplas e em heredoc, com ou sem aspas no delimitador | (`P-0752`, 2026-09-26: `python -c "import sys;print(repr(sys.argv[1]))" 'a\\tb'` imprime `'a\\tb'` pela ferramenta Bash e `'a\\\\tb'` pela ferramenta PowerShell) | arquivo que leva barra invertida se grava com Write/Edit, nunca por heredoc; comando com `\\` literal vai pela ferramenta PowerShell com aspas simples, ou a barra entra por `chr(92)` dentro do `python -c`. |
| `Python` (linha de comando) | opção do interpretador antes do script (`-X utf8`, `-W`, `-m`, `-c`) desloca o nome do programa: quem lê a linha pulando só o token iniciado por `-` toma o valor da opção (`utf8`) pelo script | (`R-06` da auditoria de encerramento do estágio 1, 2026-09-27: com `python -X utf8`, o painel do gerente calou `M-2`, `M-5`, `M-10`, `M-13` e `M-18`) | quem lê a linha de comando pula a opção junto com o valor dela (`-X`, `-W`), toma o módulo depois de `-m` como programa e não procura script depois de `-c` — é o que `progresso_hook._programa` faz. |

Regra: linha de Verificação prefere `python -c` a shell; PowerShell só com `pwsh -Command` e aspas simples.
