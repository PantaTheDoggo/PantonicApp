# RDO — P-0751 · EBK-T2

**Plano:** `docs/plans/P-0751-esgotar-backlog.md`
**Tarefa:** `EBK-T2` — O `check` confronta o card com o `rdo.py` e o piso com o corpus
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `python .claude/tools/backlog.py check` passa a emitir `C-16` para toda tarefa de plano e toda subtarefa de tíquete com status `ready`, `in-progress` ou `review` que a leitura de dossiê do `rdo.py` recusa, com a mensagem dessa leitura no texto da violação; e `C-17` para toda entrada de `_PISO_C11` que não casa nenhuma ocorrência de citação quebrada no corpus corrente.

**Arquivos-alvo:** - `.claude/tools/backlog.py` - `tests/test_backlog.py` - `.claude/skills/diario-de-obras/SKILL.md`

**Verificação:** 1. `python -m pytest tests/test_backlog.py -q` → verde, com os testes acima. 2. `python .claude/tools/backlog.py check` na árvore → `check: OK — nenhuma violação.` 3. `(Select-String -Path .claude/skills/diario-de-obras/SKILL.md -SimpleMatch 'Card vivo que o').Count` — antes `0`, depois `1`. 4. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho mais os testes novos (referência medida na autoria: `360 passed`, 2026-09-25).

**Pronto quando:** o `check` acusa card vivo que o `rdo.py` recusa e entrada de piso órfã, cada um com par em teste, e sai `OK` sobre a árvore.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Origem:** card `TK-55a` do diário de obras, seção `## TK-55`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-2` - OP-2: O card que faz a conferência do diário recusar o card que o fechamento não lê sai de pronto para concluído, sobre o backlog que a operação anterior deixou. - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Propriedades:** 1. A leitura que decide `C-16` é a mesma que `rdo.py close` usa para o dossiê — um card que o `close` recusaria sai acusado, e um que ele aceita não sai. A gramática não é reimplementada no `backlog.py`. 2. Card `done`, `cancelled` ou `blocked` não é lido para `C-16`. 3. `C-17` nomeia a entrada órfã; entrada órfã no corpus vivo sai de `_PISO_C11` neste card. 4. As menções do intervalo de códigos no módulo e na skill (`C-1..C-15`, depois do `EBK-T1`) passam a `C-1..C-17`. 5. (DEB-7) `C-16` e `C-17` julgam o corpus deste repositório, não todo `repo` passado a `check`, e entram por parâmetro que só o chamador de produção liga. `check` ganha `piso_c11: set[tuple[str, str]] | None = None` — ele, não a constante, decide o silêncio do `C-11` e o `C-17`; `None` = sem piso (nenhuma citação silenciada, nenhum `C-17`) — e `dossie: bool = False` — só com `True` (e `repo` dado) a leitura do `rdo.py` corre e sai `C-16`. O único chamador de produção (`main`, subcomando `check`; nenhum outro ponto do kit chama `check()`, medido por grep) passa `piso_c11=_PISO_C11, dossie=True`. Os testes que hoje chamam `check(...)` ficam intactos: medido (consultor, acionamento 2), a leitura estrita do `rdo.py` recusa todo card vivo das fixturas (`verde`, `pasta`, `vermelho`, `corpus`, `next_tk90`, …, nenhuma traz `Objetivo`/`Verificação`), e ligada por padrão derrubaria as asserções de `check` sobre elas. Leitura estrita = `extrair_dossie(..., esquema_legado=False, modelo_legado=None, classe_legado=None)`: card vivo de cabeçalho sem colchete sai `C-16` com a mensagem do `rdo.py` (na árvore, medido: 21 cards vivos, nenhum recusado).
- **Casos medidos que motivaram (2026-09-20 e 2026-09-25):** seis cards de tíquete sem `Arquivos-alvo`, `Verificação` e `Pronto quando` passaram no `check` e só falharam no `rdo.py close`; o `TK-68a` passou no `check` e o `review_evidence.py` recusou com `campo obrigatório ausente em 'TK-68a': 'verificacao'`, porque o literal do card tinha uma linha `### Controle 1.1 — …` na coluna 0.
- **Testes (novos, em `tests/test_backlog.py`):** - TF par sobre cópia da fixture `verde`: card `ready` íntegro → nenhum `C-16`; o mesmo card sem a linha `- **Verificação:**` → um `C-16` com o id; o mesmo card com uma linha `### X` na coluna 0 antes da `Verificação` → um `C-16` com o id. - TF: o mesmo card defeituoso com status `done` → nenhum `C-16`. - Montagem medida (consultor, acionamento 2): o card é o `TK-1a` da cópia da `verde`, que nasce sem campos; logo abaixo da linha `Status` dele entram `Objetivo`, `Arquivos-alvo` (um item), `Verificação` (um item) e `Pronto quando`. Com `check(carregar(repo), repo=repo, dossie=True)`: íntegro → `[]`; sem `Verificação` → só `C-16` `campo obrigatório ausente em 'TK-1a': 'verificacao'`; `### X` antes da `Verificação` → o mesmo `C-16`; sem `Verificação` e status `done` → `[]`. - TF par para `C-17`: piso com uma entrada que casa ocorrência da fixture → nenhum `C-17`; acrescida uma entrada que não casa nada → um `C-17` que a nomeia. Nenhuma fixture traz citação de seção; a cópia da `verde` recebe o arquivo `.claude/skills/diario-de-obras/SKILL.fixture.md` (`# X`, `## 1. Um`, prosa com `2.5`, sem heading `2.5`) e, apensa ao `docs/DIARIO_DE_OBRAS.md`, uma linha `Ver ` + esse caminho entre crases + um espaço + o sinal de seção e `2.5.` (a forma que o `C-11` colhe; não se escreve literal aqui porque o plano é corpus do `check`) — medido (consultor, acionamento 2): `check(carregar(repo), repo=repo)` sobre ela devolve exatamente um `C-11`, e nada mais. O piso do par é `{(".claude/skills/diario-de-obras/SKILL.fixture.md", "2.5")}`, passado por `piso_c11=` (propriedade 5).
- **Não fazer:** não mudar a gramática aceita pelo `rdo.py`; não corrigir card de plano fechado; não tocar `rdo.py`.
- **Contingências:** - se o Verificação 2 acusar `C-16` em card vivo da árvore → parar e sinalizar `blocked` razão `premissa`, colando as violações (o card acusado é defeito de autoria, de outro dono). - se `C-17` acusar entrada órfã no corpus vivo → remover a entrada de `_PISO_C11` e seguir (propriedade 3). Medido (consultor, acionamento 2, cópia da árvore com a propriedade 5 e `C-17` mínimo): a árvore acusa um `C-17`, `('GOVERNANCA.md', '3.2')`; removida a entrada, `check: OK — nenhuma violação.` exit 0, e a suíte inteira `362 passed` antes dos testes novos.
- **Notas de execução:** - 2026-09-25 `ready` — consultor acionamento 2: onde vale o piso fechado em DEB-7 (propriedade 5), par C-17 medido; defeito do card, nao improcedencia

## Execução

**Consumo:** 67 tool uses, 156.0 k tokens, 727.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
