# RDO — P-0740 · LM-T4a

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T4a` — A gramática de três campos nos dois parsers de cabeçalho
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — o cabeçalho de tarefa como **gramática lida por máquina**. Ensina os dois parsers do kit a aceitar o campo `esforço` de `DM-5` **antes** de qualquer card voltar a escrevê-lo (`DM-13` (ii)). Não publica doutrina (é a `LM-T4`), não mexe no conteúdo do dossiê (é a `LM-T3`) e não reescreve cabeçalho de card nenhum (é a `LM-T5`, no `P-0739`).

**Arquivos-alvo:** - `.claude/tools/rdo.py` - `.claude/tools/backlog.py` - `tests/test_rdo.py` - `tests/test_backlog.py` reenuncia): `### <ID> — <título> [<modelo>[ + dono][ · esforço <esforço>] · classe <classe>[ · teto <n>]]`, com `<modelo>` ∈ `Opus|Sonnet|Haiku`, `<esforço>` ∈ `low|medium|high|xhigh|max`, `<classe>` ∈ `mecanica|implementacao|comportamental|investigacao|redacao`. O campo `esforço` é **opcional** e fica **entre** modelo e classe; ausente, o cabeçalho continua válido exatamente como é hoje. Forma fora dessa gramática **não** bloqueia: cai no tratamento que cada instrumento já tem para cabeçalho inválido (ramo legado no `rdo.py`, `header_valido=False` no `backlog.py`).

**Verificação:** 1. `python -m pytest tests/test_rdo.py tests/test_backlog.py -q` → verde. As duas suítes são alvo desta tarefa e os cinco testes novos são dela. 2. `python -m pytest tests/ -q` → verde, piso ≥ **153** + os cinco testes novos (piso re-medido no `ESC-3`: `153 passed`; o de 145 venceu com a `LM-T1a`). Vermelho **fora** dos dois arquivos de teste alvo cai na contingência 2. 3. Efeito no arquivo-alvo, com baseline **medida** (`F-7`: zero ocorrências de `esforço` em toda a árvore `.claude/`, 2026-09-18): `Select-String -Path .claude/tools/rdo.py,.claude/tools/backlog.py -Pattern 'esforço' -SimpleMatch` → ao menos **1** linha de `.claude/tools/rdo.py` e ao menos **3** de `.claude/tools/backlog.py` (as duas do docstring e a do `_BRACKET`). Antes da entrega: nenhuma linha de nenhum dos dois.

**Pronto quando:** os dois parsers aceitam o cabeçalho de três campos e continuam aceitando o de dois; os cinco testes acima existem e passam; a busca do item 3 devolve as linhas nos dois arquivos.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` — despachada em 2026-09-18 pelo `scrum-master`. Era `ready`
- **Esforço:** low
- **Depende de:** `DM-5` (a gramática), `DM-13` (a ordem), os fatos `F-5`, `F-6` e `F-7` da §3, e a `LM-T1` fechada — ela é a última tarefa a tocar `.claude/tools/rdo.py` antes desta, e as duas não podem estar abertas ao mesmo tempo sobre o mesmo arquivo.
- **Passos:** 1. Em `.claude/tools/rdo.py:85-89`, substituir o bloco inteiro do `_HEADER_BRACKET_RE` pelo **texto novo, literal**: ```python _HEADER_BRACKET_RE = re.compile( r"^### (?P<id>(?:[A-Z0-9]+-)?T[0-9]+[a-z]?) — (?P<titulo>.+?) " r"\[(?P<modelo>Opus|Sonnet|Haiku)(?: \+ dono)?" r"(?: · esforço (?:low|medium|high|xhigh|max))?" r" · classe (?P<classe>.+?)" r"(?: · teto (?:prescrito )?[0-9]+)?\](?P<sufixo>.*)$" ) ``` 2. Em `.claude/tools/backlog.py:51`, substituir a linha `_BRACKET = rf"\[({_MODELOS})(?: \+ dono)? · classe ({_CLASSES})(?: · teto \d+)?\]"` pelo **texto novo, literal**: ```python _ESFORCOS = "low|medium|high|xhigh|max" _BRACKET = ( rf"\[({_MODELOS})(?: \+ dono)?(?: · esforço (?:{_ESFORCOS}))?" rf" · classe ({_CLASSES})(?: · teto \d+)?\]" ) ``` 3. Em `.claude/tools/backlog.py:12`, trocar a linha ``- tarefa de plano: `### <ID> — <título> [<modelo>[ + dono] · classe <classe>[ · teto <n>]]`,`` por ``- tarefa de plano: `### <ID> — <título> [<modelo>[ + dono][ · esforço <esforço>] · classe <classe>[ · teto <n>]]`,`` 4. Em `.claude/tools/backlog.py:16`, trocar a linha ``- subtarefa de tíquete: `### TK-<n><letra> — <título> [<modelo> · classe <classe>]`, dentro da`` por ``- subtarefa de tíquete: `### TK-<n><letra> — <título> [<modelo>[ · esforço <esforço>] · classe <classe>]`, dentro da`` 5. Escrever os cinco testes da seção **Testes**: dois em `tests/test_rdo.py` e três em `tests/test_backlog.py`. Todos afirmam sobre a constante de regex do próprio módulo, com a linha de cabeçalho literal escrita dentro do teste — sem fixture em disco e sem invocar CLI. — é o que dá poder discriminante a cada uma): - `TF-rdo-3campos` — `_HEADER_BRACKET_RE.match("### XX-T1 — Título [Sonnet · esforço medium · classe implementacao]")` devolve match com `group("modelo") == "Sonnet"` e `group("classe") == "implementacao"`. *Concorrente:* com a gramática de hoje (`F-5`) o match é `None`, e é esse `None` que leva `extrair_dossie` ao ramo legado e produz o exit 1 do `AE-5`. - `TR-rdo-2campos` — `_HEADER_BRACKET_RE.match("### XX-T2 — Título [Opus + dono · classe investigacao]")` continua devolvendo match, com `group("modelo") == "Opus"` e `group("classe") == "investigacao"`. *Concorrente:* com o campo `esforço` implementado como **obrigatório**, esta linha passa a dar `None` — é o que o teste tranca. - `TF-bkl-3campos` — `TAREFA_HEADER_RE.match("### XX-T1 — Título [Sonnet · esforço medium · classe implementacao]")` devolve match com `group(1) == "XX-T1"`, `group(2) == "Título"`, `group(3) == "Sonnet"` e `group(4) == "implementacao"`. *Concorrente:* hoje o match é `None`, e é isso que faz o `Item` nascer `header_valido=False`, sem modelo e sem classe (`F-6`). - `TR-bkl-grupos-posicionais` — `TAREFA_HEADER_RE.match("### XX-T2 — Título [Opus + dono · classe investigacao · teto 3]")` devolve match com `group(3) == "Opus"` e `group(4) == "investigacao"`. *Concorrente:* com um grupo **capturante** no `_BRACKET`, `group(3)`/`group(4)` passam a devolver valores deslocados e o teste falha — é exatamente a leitura que `backlog.py:229` e `:232` fazem. - `TF-bkl-esforco-fora-do-vocabulario` — `TAREFA_HEADER_RE.match("### XX-T3 — Título [Sonnet · esforço enorme · classe implementacao]")` devolve `None`. *Concorrente:* com o campo escrito como `.+?` em vez do vocabulário fechado, casaria — a gramática é fechada.
- **Restrições desta tarefa:** o grupo novo é **não capturante** nos dois arquivos — em `backlog.py` porque `:229` e `:232` leem `mm.group(3)`/`mm.group(4)` por posição (`F-6`), e em `rdo.py` por simetria, já que ninguém consome o valor. O campo `esforço` é **opcional**: o corpus de planos vivos (`P-0739` e os históricos) está inteiro na forma de dois campos e não pode deixar de casar.
- **Não fazer:** não acrescentar campo `esforco` ao `DossieTarefa` nem à saída do dossiê, e não mexer na mensagem do ramo legado (`rdo.py:230-240`) — o grupo novo é tolerado e descartado; quem consome esforço é quem despacha, não o instrumento. Não tocar `.claude/tools/review_evidence.py`: ele consome `extrair_dossie` e herda a gramática sem edição (e é alvo da `LM-T3`). Não rodar `python .claude/tools/backlog.py check` nem tratá-lo como aceite — são 315 violações pré-existentes em arquivos que esta tarefa não toca (`AE-1`), e ele sai `1` de qualquer forma. Não reescrever cabeçalho de card em plano nenhum: os deste plano estão congelados na forma de dois campos por `DM-13` (iii), e os do `P-0739` são da `LM-T5`. Não publicar a gramática em `GOVERNANCA.md` nem em skill: é a `LM-T4`.
- **Contingências:** 1. se o literal citado no passo 1, 2, 3 ou 4 não existir no arquivo exatamente como transcrito (linha movida, texto diferente) → parar e sinalizar `blocked` razão `premissa`, citando a linha encontrada; 2. se `python -m pytest tests/ -q` ficar vermelho em teste **fora** de `tests/test_rdo.py` e `tests/test_backlog.py` → seguir com a entrega e devolver na linha de retorno `contingência 2 acionada: <arquivo::teste> vermelho fora dos alvos`.
- **Fora do escopo desta tarefa:** a publicação da gramática na doutrina (`LM-T4`); a migração dos cabeçalhos dos cards do `P-0739` (`LM-T5`); a atribuição de arquivo vermelho no dossiê (`LM-T3`).

## Execução

**Consumo:** 25 tool uses, 61.3 k tokens, 86.3 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
