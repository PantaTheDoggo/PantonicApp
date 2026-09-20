# RDO — P-0739 · BKL-T11a

**Plano:** `docs/plans/P-0739-backlog-instrumento.md`
**Tarefa:** `BKL-T11a` — O hook fala no ponto de carga real: `stdin` em UTF-8 explícito e gatilho normalizado
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `python .claude/tools/backlog_hook.py`, rodado como **executável** com o payload de `UserPromptSubmit` em UTF-8 na entrada padrão, devolve `additionalContext` — hoje devolve **0 bytes** —, e um teste passa a exercer **o processo**, não só o módulo importado. Um ato, uma proposição.

**Arquivos-alvo:** - `.claude/tools/backlog_hook.py` - `tests/test_backlog.py`

**Verificação:** 1. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/tools/backlog_hook.py -Pattern 'sys.stdin.buffer' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. Mede a metade 1 — a que carrega o peso — pelo literal recortado da fonte. 2. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/tools/backlog_hook.py -Pattern 'unicodedata' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. Mede a metade 2. 3. ``` python -m pytest tests/test_backlog.py -q -k hook_executavel ``` → **2** selecionados e **verdes**. **Medido antes: 0 selecionados** — referência datada de 2026-09-20, fora do literal: 70 testes no módulo, todos desselecionados. É o item que prova que o **executável** passou a ser exercido, e não só o módulo. 4. ``` python -m pytest tests/ -q ``` → **verde**, com total **não menor** que o total re-medido no início deste despacho, e igual a ele **mais os dois** testes do campo `Testes`. Referência datada de 2026-09-20, fora do literal: suíte inteira com 222.

**Pronto quando:** os quatro itens de `Verificação` dão o resultado descrito; rodado à mão no ponto de carga — o executável com o payload UTF-8 na entrada padrão, **sem** `PYTHONUTF8` no ambiente —, o hook devolve `additionalContext` não vazio; e prompt sem gatilho continua devolvendo stdout vazio com exit 0.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` · 2026-09-20
- **Esforço:** low
- **Depende de:** `BKL-T11`
- **Razão da dependência e insumos (`DB-50`):** o hook nasceu na `BKL-T11`, e é o executável dela que esta tarefa conserta. Decisões: `DB-52` (as duas metades e a residência do reparo), `DB-8` (o hook), `DB-1` (o instrumento é stdlib). Fato: `AE-35`, e o precedente `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`, cujo `_norm` é a referência da segunda metade — **e cuja primeira metade não existe**, medido no `ESC-9`.
- **Passos:** 1. **Metade 1, e é ela que carrega o peso — ler `stdin` como bytes e decodificar UTF-8 explicitamente.** Em `main` (`.claude/tools/backlog_hook.py:72`), trocar `sys.stdin.read()` por leitura de `sys.stdin.buffer` com `.decode("utf-8", errors="replace")`, mantendo o `try/except` que já existe e o contrato de **exit 0 sempre**. Razão medida em 2026-09-20, fora do literal: num host sem `PYTHONUTF8`, `sys.stdin.read()` decodifica em `cp1252` e o payload UTF-8 chega como `execute o prÃ³ximo passo`; o mesmo payload com `PYTHONUTF8=1` devolve **6.997** bytes de `additionalContext`, e sem ele, **0**. 2. **Metade 2 — normalizar a comparação do gatilho, e escrever o literal sem acento.** `_casa_gatilho` (`.claude/tools/backlog_hook.py:32`) passa a comparar sobre texto normalizado — minúsculas e acentos removidos por `unicodedata.normalize("NFKD", …)` descartando os combinantes, o mesmo `_norm` do precedente —, e `_GATILHO` (`.claude/tools/backlog_hook.py:20`) passa a ser o literal **sem acento**, `proximo passo`. Isso faz casar tanto `próximo passo` quanto `proximo passo`, que é o que um dono digita sem pensar. **Esta metade sozinha não conserta o defeito** — medido no `ESC-9`: o texto mis-decodificado normaliza para `execute o pra3ximo passo`, que **não** contém `proximo passo`, porque o `³` do `cp1252` decompõe em `3` sob NFKD. Ela entra porque amplia o gatilho, não porque salva a metade 1. 3. **O teste que faltava — exercer o executável.** Escrever em `tests/test_backlog.py` os dois TF do campo `Testes`, que rodam `subprocess.run([sys.executable, ".claude/tools/backlog_hook.py"], input=<bytes UTF-8>, …)`, alimentando **bytes** pela entrada padrão e afirmando sobre os **bytes** da saída. É a distinção que deixou o defeito passar: os TF da `BKL-T11` alimentam `processar` por importação, com a string já decodificada em memória, e nunca tocam o `sys.stdin` de um processo. 4. **Não mudar mais nada do hook:** `processar`, `_texto_next`, `_carregar_backlog` e o contrato de exit 0 ficam como estão — o defeito é de I/O e de comparação, e o `next` que o hook invoca funciona.
- **Restrições desta tarefa (copiadas inline; nenhuma vale por ponteiro):** - **O hook nunca bloqueia o prompt:** qualquer falha — decodificação, exceção, exit 3 de `next` — vira texto em `additionalContext` ou stdout vazio, e o processo sai **0**. O reparo não introduz caminho novo de erro: `errors="replace"` nunca levanta. - **Sem subprocesso dentro do hook:** a seleção continua rodando por importação de `.claude/tools/backlog.py`. O subprocesso aparece **no teste**, que é quem precisa de um processo real para exercer `stdin`. - **Prompt sem gatilho continua em silêncio:** stdout vazio e exit 0. O par com o teste de gatilho é o que separa *injeta sempre* de *injeta quando casa*. - **Piso de regressão como relação:** a entrega soma os `<N>` testes novos e **não reduz** o total de `python -m pytest tests/ -q` re-medido no próprio despacho. Referência datada de 2026-09-20, fora do literal: `tests/test_backlog.py` com 70 testes e a suíte inteira com 222.
- **Não fazer:** - Não editar `.claude/tools/backlog.py` — o instrumento fechou no `BKL-T10`/`BKL-T10b`. - Não editar `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py` nem qualquer outro hook: o `ESC-9` mediu que ele tem a **mesma** lacuna, e consertá-lo é matéria de outro plano (`AE-36`). Aqui ele é **referência**, não alvo. - Não editar `.claude/tools/ocupacao.py` nem `.claude/tools/telemetria_hook.py`, que leem `stdin` pelo mesmo padrão — mesma razão. - Não editar `README.md`, `docs/DIARIO_DE_OBRAS.md` nem card nenhum deste plano. - Não mexer em `.claude/projecoes.json`: o registro do hook já entrou pela `BKL-T11` e `materializar.py drift` está em 0.
- **Contingências:** - se `sys.stdin.buffer` não existir no ambiente de teste (stdin substituído por objeto sem `buffer`) → cair para `sys.stdin.read()` no mesmo `try`, mantendo exit 0, e declarar na linha de retorno `contingência 1 acionada: fallback de stdin sem buffer`; - se o TF de subprocesso ficar acima de 5 s por carregar o repo real → apontá-lo para uma cópia de fixture em `tmp_path` via a variável de ambiente que `resolve_repo` já respeita, e declarar na linha de retorno; - se o payload de fixture precisar de campo além de `hook_event_name` e `prompt` → acrescentá-lo, porque a forma do evento é do harness e não desta tarefa.
- **Fora do escopo desta tarefa:** a aferição do pickup e a revisão do `README.md` — `BKL-T12`, que executa **depois** desta e cuja medida depende deste reparo. Ficam fora, nomeados no `AE-36` e sem card: a mesma lacuna em `.claude/global/hooks/modelo_por_fase_userpromptsubmit.py`, em `.claude/tools/ocupacao.py` e em `.claude/tools/telemetria_hook.py`.

## Execução

**Consumo:** 31 tool uses, 75.8 k tokens, 204.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: nenhuma declarada pelo executor
laudo: A regra que este card instala - teste que julga um executavel roda o executavel - entra incompleta: sem fixar o ambiente do subprocesso ela nao discrimina, e o AE-36 vai propaga-la a tres entrypoints; decidir no planejamento antes da propagacao.

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
