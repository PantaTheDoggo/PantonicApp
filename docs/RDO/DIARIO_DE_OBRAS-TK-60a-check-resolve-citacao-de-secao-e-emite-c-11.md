# RDO — DIARIO_DE_OBRAS · TK-60a

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-60a` — `check` resolve citação de seção e emite `C-11`
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `check` passa a resolver as citações de seção do corpus contra o arquivo citado e a emitir `C-11` quando a seção citada não existe nele. Fecha o terceiro resolvedor de referência do kit — caminho de arquivo tem `Test-Path`, identificador de tarefa tem `review_evidence`, citação de seção passa a ter este.

**Arquivos-alvo:** - `.claude/tools/backlog.py` - `tests/test_backlog.py` - `tests/fixtures/backlog/citacao_secao/`

**Verificação:** - `python .claude/checks/dead_code.py` sai **exit 0** — hoje sai `FALHOU - 1 achado(s)`, nomeando `.claude/tools/backlog.py:638: resolver_citacao_secao - sem chamador de producao alcancavel`. - `python .claude/tools/backlog.py check` sai **exit 0**. Se sair 1, o **piso do item 7 está errado** — não o corpus. - `python -m pytest tests/test_backlog.py` verde; `python -m pytest` verde, sem queda do piso de **234** (medido em 2026-09-20, com a entrega anterior na árvore).

**Pronto quando:** os oito itens abaixo valem, e cada um é conferível no arquivo entregue. 1. **Gramática de colheita — a observada, não a inventada.** A citação real do kit é `` `<arquivo>.md` §<N>[.<N>]* `` (literal entre crases, espaço, `§`). Medido em 2026-09-20: **1.017** ocorrências dessa forma contra **1** da forma `§X.Y publicada em <arquivo>` que o card anterior fixava — e essa 1 é o texto do próprio tíquete. A `_REF_SECAO_RE` entregue **sai**. 2. **Domínio — um nível e N níveis.** Medido: **772** citações de um nível (`§3`, `§7`, `§10`) contra **240** de dois ou mais. A gramática anterior exigia `\d+(?:\.\d+)+` e reprovava as 772. 3. **Casamento por heading numerado, nunca substring** — `^#{1,6}\s+<N>(\.<N>)*\b`. O núcleo entregue está **correto e fica**: é o que faz o caso motivador sair `C-11` apesar de o literal existir (`.claude/skills/diario-de-obras/SKILL.md` tem `2.5` em prosa na linha 42 e **zero** headings numerados nas suas 301 linhas). 4. **Resolução de caminho: raiz do repo, com queda para basename único no corpus.** Medido: **56** ocorrências / 20 distintas falhariam só por a citação omitir o prefixo — `` `RUBRICA_DE_REVISAO.md` §8 `` (9 ocorrências) com o arquivo em `docs/`. Sem essa queda o lint vira ruído. 5. **Fronteira declarada, e é silêncio nos dois casos:** arquivo que não existe nem por basename **não** é `C-11` — resolver caminho é do `Test-Path` (`DB-2`, uma residência por regra); e `§` seguido de **três ou mais** componentes numéricos é **versão**, não seção (medido: `` `CHANGELOG.md` §3.0.0 ``, 3 ocorrências). 6. **O chamador de produção é `check`.** Nenhum subcomando novo, nenhum segundo ponto de entrada. 7. **Piso, para o lint não nascer vermelho.** `check` não tem severidade: violação implica exit 1. O corpus vivo já carrega dívida — medido: **duas** seções citadas que não existem, `` `GOVERNANCA.md` §1.1 `` e `` §3.2 ``, em **13** ocorrências (`docs/DIARIO_HISTORICO.md` 5, `docs/plans/P-0741-modelo-conceitual.md` 6, `P-0730` 1, `P-0731` 1). `C-11` nasce com um piso dessas **duas** entradas, inline no módulo, cada uma com origem e data da medida — mesma trava do `.claude/checks/ratchet_piso.py`. O lint falha no **próximo** ponteiro quebrado, que é o defeito que o `TK-60` existe para pegar. Quitar o piso é tíquete próprio, não deste card. 8. **O mundo do teste é declarado.** A fixture `tests/fixtures/backlog/citacao_secao/` **fica** — é a convenção do módulo e blinda o teste das edições da outra janela —, e a folha `.claude/skills/diario-de-obras/SKILL.md` dentro dela é **renomeada para `SKILL.fixture.md`**, preservando o diretório-espelho. Razão medida: com o nome real, o harness passou a listar a fixture como **skill invocável** (`tests/fixtures/backlog/citacao_secao:diario-de-obras`). E o **par de regressão do domínio**, que é o defeito medido nesta rodada, entra como teste: `§3` contra `GOVERNANCA.md`, `§8` contra `docs/RUBRICA_DE_REVISAO.md` e `§9` contra `docs/consultant-spec.md` resolvem (`None`); hoje os três saem `C-11`.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20 — **reescrito** após reprovação 56% (bloqueante `guardas`). A reprovação foi de **autoria do card**, não de conduta do executor: a `Verificação` anterior exigia superfície de CLI e fixava uma gramática de citação que **não existe no corpus**. Retentativa não consumida.
- **Não fazer:** não editar `docs/plans/P-0741-modelo-conceitual.md` — é plano **vivo de outra janela de orquestração ativa neste mesmo repositório**; as 6 ocorrências dele entram no piso, são reportadas e **não** corrigidas. Não corrigir nenhuma das 13 ocorrências. Não criar subcomando de CLI. Não editar `GOVERNANCA.md`, `.claude/tools/rdo.py`, `review_evidence.py` nem `.claude/estado/tarefa-corrente.json`.

## Execução

**Consumo:** 50 tool uses, 134.9 k tokens, 704.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: Item 5 nao implementado: resolver_citacao_secao devolve C-11 quando _resolver_arquivo_citado da None, contra o proprio docstring; as 3 entradas extras do piso sao artefato desse defeito. Com o item 5 correto e o piso nas 2 entradas do card, check sai exit 0 com zero C-11 (medido na revisao).

## Laudo

**Veredito:** ressalva

**Percentual:** 76%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
