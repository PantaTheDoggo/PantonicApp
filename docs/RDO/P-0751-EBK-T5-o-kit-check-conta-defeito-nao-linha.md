# RDO — P-0751 · EBK-T5

**Plano:** `docs/plans/P-0751-esgotar-backlog.md`
**Tarefa:** `EBK-T5` — O `kit_check` conta defeito, não linha
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** o número em `kit_check: check-drift FALHOU (<n> problema(s))` e em `kit_check: FALHOU (<n> problema(s))` passa a ser o número de defeitos: uma divergência de README conta `1`, e as linhas `[regenerado]`/`[versionado]` que a detalham continuam impressas sem entrar na contagem.

**Arquivos-alvo:** - `.claude/checks/kit_check.ps1` - `tests/test_kit_check.py` (novo, ou o arquivo de teste do `kit_check` que já existir)

**Verificação:** 1. `python -m pytest <arquivo de teste do kit_check> -q` → verde, com o teste acima. 2. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` na árvore → exit `0`. 3. `python -m pytest -q` → nenhuma falha; `passed` ≥ o do despacho mais os testes novos.

**Pronto quando:** uma divergência conta um problema, provado pelo teste, e o check segue verde na árvore.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Origem:** card `TK-55d` do diário de obras, seção `## TK-55`, transcrito sem mudança além dos identificadores.
- **Operação do modelo:** `OP-5` - OP-5: O card que faz a conferência do kit contar um defeito por vez sai de pronto para concluído, sobre o backlog que a operação anterior deixou. - precisa de: card — Quem implementa executa o card como está escrito, com o aceite que ele mesmo traz.; backlog — Quem implementa fecha um card por operação, sem acrescentar card ao plano.
- **Caso medido (2026-09-25):** cópia de `.claude/` em diretório temporário, com uma frase acrescentada a uma linha da região gerada de `.claude/README.md` → a saída listou `README.md diverge do regenerado (2 linha(s) diferente(s)):` mais as duas linhas de detalhe como três itens `- ` da mesma lista, todos contados.
- **Testes:** TF sobre cópia do kit sob `tmp_path` (pular se `pwsh` não estiver no `PATH`): uma divergência de README com duas linhas diferentes → a contagem de problemas atribuída ao README é `1` e as duas linhas de detalhe aparecem na saída.
- **Não fazer:** não mudar o que o `kit_check` considera divergência; não mexer na codificação do console (já correta).

## Execução

**Consumo:** 33 tool uses, 97.8 k tokens, 358.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
