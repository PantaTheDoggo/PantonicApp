# RDO — DIARIO_DE_OBRAS · TK-93a

# Humano

Tarefa "O `<ref>` do despacho carrega o não rastreado, e o redespacho reusa o do primeiro despacho" concluída em 2026-09-27.
O ponto de partida do despacho passou a carregar os arquivos não rastreados, e a evidência mostra só o que mudou neles desde então.
Revisão: aprovada com ressalva (91%).
Pendência para o dono: nenhuma.
Tíquete "A evidência não mostra o que mudou em arquivo não rastreado, e o redespacho perde a primeira execução": 1/1 tarefas concluídas; nenhuma tarefa pronta na fila dele.
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.
Achados registrados no plano, com rota: 2 (ver seção de achados da execução).

# Máquina

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-93a` — O `<ref>` do despacho carrega o não rastreado, e o redespacho reusa o do primeiro despacho
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** em `.claude/tools/review_evidence.py`: 1. `capturar_ref(root)` e a flag `--capturar-ref`, que imprime o `<ref>` e sai `0` sem exigir `--plano` nem `--tarefa` (sem a flag, os dois seguem obrigatórios): o `<ref>` é um commit cujo pai é `HEAD` (sem pai em repositório sem commit) e cuja árvore é a árvore de trabalho inteira — rastreados e não rastreados não ignorados —, gravado por índice temporário; árvore de trabalho, índice e lista de stash saem como entraram; 2. com `--desde <ref>`, o arquivo hoje não rastreado e presente no `<ref>` é julgado pelo conteúdo, comparado linha a linha com o fim de linha normalizado: entra nos tocados só se mudou, e o trecho dele é o diff unificado entre o conteúdo no `<ref>` e o atual, ou `(sem alteração desde <ref>)` quando igual; ele não entra nos tocados pela saída de `git diff <ref> --name-only` (que o dá como apagado) e o estado dele na evidência segue `??`. Com `<ref>` de `git stash create` (sem não rastreados), o resultado é o de hoje; 3. o Passo 4 do `scrum-master` manda capturar o `<ref>` pela flag e reusar o do primeiro despacho no redespacho (texto em `Passos`).

**Arquivos-alvo:** - `.claude/tools/review_evidence.py` - `tests/test_review_evidence.py` - `.claude/skills/scrum-master/SKILL.md`

**Verificação:** 1. `python .claude/tools/review_evidence.py --capturar-ref` → verde — antes `exit 2`, depois `exit 0`. 2. `python -m pytest tests/test_review_evidence.py -q -k "capturar_ref or nao_rastreado_no_ref"` → verde — antes `exit 5`, depois `exit 0`. 3. `python -c "from pathlib import Path;t=Path('.claude/skills/scrum-master/SKILL.md').read_text(encoding='utf-8');print(t.count('git stash create'),t.count('review_evidence.py --capturar-ref'),t.count('vale o do primeiro despacho'))"` → `0 1 1` — antes `1 0 0`, depois `0 1 1`. 4. `python -m pytest -q` → nenhuma falha — antes `exit 0`, depois `exit 0`. 5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `kit_check: check-drift OK` — antes `exit 0`, depois `exit 0`.

**Pronto quando:** a evidência de tarefa que edita arquivo não rastreado mostra o hunk da edição, e só o não rastreado que mudou entra nos tocados (Verificação 2); a captura existe e não mexe na árvore (Verificação 1 e 2); o Passo 4 manda capturar pela flag e reusar o primeiro `<ref>` (Verificação 3). Medido em protótipo do consultor sobre cópia da árvore com o `TK-92a` aplicado, apagada, em 2026-09-26: suíte `430 passed` → `432 passed`, `check-drift` OK.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-27
- **Depende de:** `TK-92a`
- **Passos:** 1. Em `.claude/skills/scrum-master/SKILL.md`, Passo 4, as quatro linhas depois de `antigo:` viram as seis depois de `novo:` (as quebras são as do bloco; os rótulos não entram no arquivo; cada linha leva no arquivo os dois espaços de recuo que tem no bloco): ```text antigo: `docs/telemetria.tsv`. Capturar como `<ref>` (schema `DP-S`) a saída de `git stash create` — instantâneo dos arquivos rastreados no despacho, que não altera árvore, índice nem a lista de stash —, ou `git rev-parse HEAD` quando ela vier vazia (árvore limpa); usada no passo 6 (`AUT-T5b`), onde o trecho de cada alvo passa a mostrar só o que mudou desde o despacho. novo: `docs/telemetria.tsv`. Capturar como `<ref>` (schema `DP-S`) a saída de `python .claude/tools/review_evidence.py --capturar-ref` — instantâneo da árvore de trabalho inteira no despacho, rastreados e não rastreados, que não altera árvore, índice nem a lista de stash; usada no passo 6 (`AUT-T5b`), onde o trecho de cada alvo passa a mostrar só o que mudou desde o despacho. No redespacho da mesma tarefa (retomada depois de `blocked`, ou retentativa), o `<ref>` não se recaptura: vale o do primeiro despacho, para a evidência cobrir as duas execuções. ```
- **Contratos/classes:** `capturar_ref(root: Path) -> str` (o SHA do commit); `--capturar-ref` é `store_true`, com `--root` opcional como hoje. As assinaturas de `coletar_arquivos_tocados`, `coletar_estado_git`, `montar_trechos` e `montar_documento` não mudam.
- **Caso medido que motivou:** ver `## TK-93`.
- **Testes (novos, em `tests/test_review_evidence.py`):** TF `test_tf_capturar_ref_carrega_nao_rastreado` — repositório temporário com um não rastreado: `git show <ref>:<arquivo>` devolve o conteúdo dele, e `git status --porcelain=v1 --untracked-files=all` e `git stash list` saem iguais aos de antes da captura. TF `test_tf_nao_rastreado_no_ref_mostra_so_o_hunk` — não rastreado de 400 linhas no `<ref>`, uma linha editada depois: o trecho traz a linha nova com `+` e não é truncado no teto de 4000, e `coletar_arquivos_tocados(repo, ref)` devolve só ele (outro não rastreado, sem mudança, fica de fora). Os TF da `TK-78c` (`<ref>` de `git stash create`) seguem verdes sem mudança.
- **Não fazer:** não mudar o teto de 4000 caracteres nem o recorte por data (`st_mtime`) do não rastreado ausente do `<ref>`; não tocar `_classificar_campo_alvos` (é do `TK-89a`) nem o destino da medida (é do `TK-92a`); não mudar `pantonic-reviewer.md`, que cita o `<ref>` do passo 4 e segue certo; não usar `git stash push` nem nada que mexa na árvore, no índice real ou na lista de stash.
- **Contingências:** - se um teste existente de `tests/test_review_evidence.py` cair → parar e sinalizar `blocked` razão `premissa`, nomeando o teste (no protótipo, nenhum caiu).
- **Handover:** 2026-09-27 · para quem vier depois - **Entregue:** review_evidence.py --capturar-ref (capturar_ref: índice temporário com a árvore de trabalho) e julgamento por conteúdo do não rastreado presente no <ref>; scrum-master Passo 4 manda capturar assim e reusar o <ref> no redespacho - **Contrato:** a evidência mostra só o hunk do não rastreado que mudou desde o despacho - **Não refazer:** nada a declarar - **Pendente:** rastreado-e-ignorado sai do <ref> (git add -A em índice vazio); binário ou não-UTF-8 intocado entra sempre em tocados — AE com rota auditoria final
- **Notas de execução:** - 2026-09-27 `done` — fechada por `encerrar.py`: RDO `docs/RDO/DIARIO_DE_OBRAS-TK-93a-o-ref-do-despacho-carrega-o-nao-rastreado-e-o-redespacho-reu.md`, veredito ressalva 91%

## Execução

**Consumo:** 42 tool uses, 115.2 k tokens, 698.8 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa

O instrumento que troca 'git stash create' por captura própria herda a obrigação de reproduzir o que o stash já fazia de graça: o stash parte do índice de HEAD, e um índice temporário vazio não parte. Exercício ponta a ponta em repositório com arquivo forçado ('add -f') e binário não rastreado revelou os dois furos que os TF de texto puro nunca tocam.

## Fechamento

**Desdobramento:** aprovado com ressalva

# Histórico

Scrum master vai fechar a tarefa "O `<ref>` do despacho carrega o não rastreado, e o redespacho reusa o do primeiro despacho" como done: registrar estado, RDO e telemetria.
