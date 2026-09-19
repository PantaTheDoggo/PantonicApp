# RDO — P-0740 · LM-T1

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T1` — O pacote de fechamento: estado, telemetria e contratos
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** tudo que o loop escreve ao fechar uma tarefa, num módulo só. Cobre os defeitos 1 e 3 e absorve a `AUT-T4`.

**Arquivos-alvo:** - `.gitignore` - `.claude/estado/.gitkeep` - `.claude/tools/rdo.py` - `.claude/skills/scrum-master/SKILL.md` - `tests/test_rdo.py` - `tests/test_telemetria.py`

**Verificação:** (as linhas 3, 4 e 5 trazem a saída **medida** com a entrega na árvore, `AE-4`; nenhuma delas é saída deduzida.) 1. `python -m pytest tests/test_rdo.py tests/test_telemetria.py -q` → verde. 2. `python -m pytest tests/ -q` → verde, total ≥ 145 (142 da baseline + os 3 TF deste card). 3. `git check-ignore -q .claude/estado/.gitkeep` → **exit code 1** (= o caminho **não** está ignorado, que é o efeito de `DM-10`). Em PowerShell, ler com `git check-ignore -q .claude/estado/.gitkeep; $LASTEXITCODE` → imprime `1`. **Não** usar `-v` como critério: com `-v` o git reporta o padrão decisivo inclusive quando é negação, imprime `.gitignore:12:!.claude/estado/.gitkeep` e sai `0`, e isso **não** significa ignorado. 4. `git check-ignore -v .claude/estado/tarefa-corrente.json` → imprime uma linha terminando em `.claude/estado/*` (medido: `.gitignore:11:.claude/estado/*`; o número da linha não é aceite, o padrão citado é). 5. `git status --porcelain -uall .claude/estado/` → imprime exatamente `?? .claude/estado/.gitkeep`. O `-uall` é obrigatório: sem ele o git colapsa o diretório não rastreado e imprime `?? .claude/estado/`.

**Pronto quando:** as cinco verificações acima saem como descrito, e `.gitignore` contém as duas linhas `.claude/estado/*` e `!.claude/estado/.gitkeep` nessa ordem, `rdo.py:772` diz `type=float` e o Passo 4 do `scrum-master` contém a palavra `garantir` antes de `gravar`.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `review` — a entrega material já está na árvore, completa e verde; a rodada `RP-2` (2026-09-18, `DM-12`) corrigiu as verificações 3 e 5 e a contingência 1, que eram insatisfazíveis como escritas (`AE-4`), e passou a tarefa de `blocked` a `review` sem redespacho. **Para quem revisa:** a entrega está **não commitada** na árvore, misturada a entregas não commitadas de outras tarefas; a atribuição é pelos `Arquivos-alvo` deste card — `.gitignore`, `.claude/estado/.gitkeep` (novo), `.claude/tools/rdo.py`, `.claude/skills/scrum-master/SKILL.md`, `tests/test_rdo.py`, `tests/test_telemetria.py`, e nada além disso é desta tarefa. O julgamento é contra as cinco verificações **abaixo, já corrigidas**. A rodada `RP-3` (`DM-13`) trocou o cabeçalho de três campos pela forma de dois campos que os instrumentos parseiam, para que o dossiê de evidência da revisão possa ser gerado; nenhuma linha da entrega é afetada.
- **Esforço:** medium
- **Depende de:** `DM-10` (forma do slot de estado), `DM-11` (tipo de `--tokens-k`), `DM-3` (coerência é aceite), e os fatos `F-1`..`F-4` da §3. Nenhuma tarefa anterior.
- **Produto do módulo:** (a) o **slot** `.claude/estado/` versionado — `.gitkeep` rastreável e conteúdo de sessão ainda ignorado, conforme `DM-10`, com o `.gitignore` reescrito no texto literal abaixo; (b) `rdo.py close --tokens-k` aceitando e gravando decimal de uma casa, conforme `DM-11`, de modo que o mesmo literal sirva a `telemetria.py append --tokens_k` sem conversão; (c) Passo 4 e Passo 9 do `scrum-master` reescritos nos dois textos literais abaixo — o Passo 4 garante o diretório antes de gravar (segunda trava), o Passo 9 fixa que o mesmo literal vai às duas chamadas. ``` # Estado de sessão do loop autônomo (ex.: tarefa-corrente.json, escrito pelo `scrum-master` no # despacho e consumido pelo hook `SubagentStop` — T55) — fato de uma sessão numa máquina, nunca # canônico do framework. .claude/estado/ ``` por **estas seis**, na mesma posição do arquivo: ``` # Slot de estado de sessão do loop autônomo. O diretório é canônico do framework e viaja # versionado (`.gitkeep`), para que o Passo 4 do `scrum-master` nunca grave em caminho # inexistente; o conteúdo (ex.: tarefa-corrente.json, escrito no despacho e consumido pelo hook # `SubagentStop` — T55) é fato de uma sessão numa máquina e nunca se versiona. .claude/estado/* !.claude/estado/.gitkeep ``` que começa com **`- **Ação:** gravar`** e segue com o caminho do arquivo de estado. Trocar o início dela, até o abre-parêntese de "objeto único", por: ``` - **Ação:** garantir o diretório `.claude/estado/` (ele viaja versionado com `.gitkeep`, `DM-10` do `P-0740`; recriá-lo se tiver sido apagado nesta máquina) e gravar `.claude/estado/tarefa-corrente.json` (objeto único: ``` O resto da frase (`tarefa`, `projeto`, `modelo`, `plano`, `despachado_em` ISO 8601 …) fica intacto. `--tool-uses <N> --tokens-k <N> --duracao-s <N> \` por `--tool-uses <N> --tokens-k <tokens_k> --duracao-s <N> \`; e apender, como parágrafo próprio logo depois do parágrafo que termina em "nunca copiado para o diário." (`:157`), esta frase: ``` O `<tokens_k>` é o mesmo literal nas duas chamadas — decimal de uma casa (ex.: `203.7`), a forma que o hook `SubagentStop` já produz. O loop não converte, não arredonda e não trunca o número entre uma chamada e outra (`DM-11` do `P-0740`). ```
- **Contratos/classes:** `.claude/tools/rdo.py:772` — `"--tokens-k", required=True, type=int, dest="tokens_k",` passa a `type=float`; `:675` — `"TOKENS_K": str(args.tokens_k),` passa a `"TOKENS_K": f"{args.tokens_k:.1f}",`. `.claude/tools/telemetria.py` **não se edita**: `--tokens_k` (`:150`) já aceita o literal decimal por `_validar_numero_nao_negativo` (`:106`).
- **Coerência do módulo (aceite de `DM-3`):** o literal `203.7` entra sem erro nos dois CLIs e sai gravado nos dois artefatos (RDO e `docs/telemetria.tsv`) com a mesma grafia, sem conversão intermediária.
- **Restrições desta tarefa:** o `.gitignore` é tocado **só** nas quatro linhas transcritas acima — `.claude/settings.local.json`, `.claude/settings.json`, `__pycache__/`, `*.pyc`, o bloco de ruído de SO/editor, `*.log`, `scratchpad/`, `PantonicForDesktop/` e `PantonicForContainer/` ficam como estão. A negação `!.claude/estado/.gitkeep` vem **depois** de `.claude/estado/*`, nesta ordem, e nenhuma linha com `.claude/estado/` terminando em barra sobra no arquivo. Nenhum comando de git que altere índice ou HEAD (`git add`, `git commit`, `git stash`, `git checkout`, `git restore`): a árvore já carrega entregas não commitadas de outras tarefas e a desta também fica não commitada. `rdo.py` não importa `telemetria.py` (`DM-11`).
- **Não fazer:** não tocar `.claude/tools/telemetria_hook.py` nem `tests/test_telemetria_hook.py` (são a `LM-T2`); não tocar `.claude/tools/backlog.py`; não tocar `.claude/tools/telemetria.py`; não mexer em `--tool-uses` nem em `--duracao-s`, que continuam `int`; não criar `.claude/estado/tarefa-corrente.json` (quem o escreve é o Passo 4, em tempo de despacho).
- **Contingências:** - se `git check-ignore -q .claude/estado/.gitkeep` sair com exit code **0** depois da edição (= o caminho **está** ignorado, o oposto do pretendido) → conferir no `.gitignore` que `!.claude/estado/.gitkeep` está depois de `.claude/estado/*` e que nenhuma linha `.claude/estado/` com barra final sobrou; corrigir e repetir o comando. Se ainda sair `0`, parar e sinalizar `blocked` razão `premissa`. **Exit code `1` é o resultado esperado e não é erro**; a saída de `git check-ignore -v` **não** é critério aqui, porque com `-v` o git imprime o padrão decisivo mesmo quando ele é a negação que desfaz o ignore (`DM-12`). - se a ferramenta de escrita recusar arquivo vazio → gravar em `.claude/estado/.gitkeep` a única linha `# slot versionado; o conteudo deste diretorio e ignorado (ver .gitignore)` e devolver `contingência 2 acionada: .gitkeep com uma linha de comentário`. - se algum teste pré-existente de `tests/test_rdo.py` ficar vermelho pela forma decimal → ajustar **só** a asserção do literal de tokens desse teste, nada mais, e devolver `contingência 3 acionada: <nome do teste> ajustado`. - se `python -m pytest tests/test_telemetria.py -q --collect-only` já listar um teste cujo nome contenha `decimal` → não criar teste novo em `tests/test_telemetria.py`; citar o nome dele na linha de retorno e implementar só o TR de coerência, em `tests/test_rdo.py`.
- **Testes:** TF em `tests/test_rdo.py` — `rdo.py close --tokens-k 203.7` sai exit 0 e o RDO gerado contém `203.7`; TR em `tests/test_rdo.py` — `--tokens-k 80` grava `80.0` (uma casa decimal sempre, o que a regra concorrente `str(int)` daria como `80` e por isso discrimina); TF em `tests/test_telemetria.py` — `telemetria.py append --tokens_k 203.7` sai exit 0 e a linha apensada traz `203.7` na coluna `tokens_k`.
- **Fora do escopo desta tarefa:** o hook `SubagentStop` e a fonte do número que ele grava são a `LM-T2` (`AE-3`); a atribuição de arquivo vermelho é a `LM-T3`.

## Execução

**Consumo:** 37 tool uses, 134.8 k tokens, 340 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: Domínio de --tokens-k em rdo.py close ficou sem guarda após type=float (aceita negativo, notação científica e nan), divergindo de telemetria.py, que valida.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar — abrir item de replanejamento no P-0740 para fechar o contrato de erro do módulo de fechamento

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
