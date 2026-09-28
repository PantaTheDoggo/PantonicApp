# RDO — P-0749 · SAN-T6b

**Plano:** `docs/plans/P-0749-saneamento-artefatos.md`
**Tarefa:** `SAN-T6b` — As decisões estruturantes dizem o contador como a regra o diz
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Corretivo da `SAN-T6a` (`AE-6`): na tabela da §14 do `README.md` (*Decisões estruturantes*), a linha *Plano tem contador sequencial global no nome* deixa de chamar o contador de "global" e passa a dizê-lo como o glossário (`M5`) e `GOVERNANCA.md` §7 item 11: do repositório.

**Arquivos-alvo:** - `README.md`

**Verificação:** 1. ``` pwsh -NoProfile -File .claude/checks/check-readme.ps1 ``` → **exit 0, com a linha que começa por `check-readme: OK - 10 agente(s), 11 skill(s), 20 guardrail(s)`**. **Medido antes: exit 0, a mesma linha** (2026-09-25; e com `M6` aplicado numa cópia da árvore, `-Root` em `$env:TEMP`). 2. ``` pwsh -NoProfile -Command '(@(foreach ($p in "contador sequencial global","contador global","Plano tem contador sequencial do repositório no nome") { @(Select-String -LiteralPath README.md -SimpleMatch -Pattern $p).Count })) -join " / "' ``` → **0 / 0 / 1**. **Medido antes: 1 / 0 / 0** (2026-09-25; `0 / 0 / 1` com `M6` aplicado numa cópia). 3. ``` python -m pytest tests -q ``` → **o total do despacho, nenhuma falha**. **Medido antes: 353 passed** (2026-09-25).

**Pronto quando:** - kit.porta de entrada — descreve pasta por plano, tabela de estado e a regra do texto mínimo — Verificação 1, 2

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Fundamento:** DSA-24, DSA-23, DSA-3; I-5; `AE-6`.
- **Depende de:** `SAN-T6a`
- **Operação do modelo:** `OP-6` - OP-6: O mantenedor da porta de entrada do repositório reescreve a descrição pública do kit: pasta por plano, tabela de estado e artefato de humano mínimo. - precisa de: kit — Quem implementa recebe essas ferramentas e esses textos. O que já está gravado continua sendo lido como hoje.; plano novo — Quem implementa não o escreve. A forma com que ele nasce mostra se o kit mudou.
- **Camada e fronteira:** só o `README.md`, a primeira célula de uma linha da tabela da §14 (a linha 1045 em 2026-09-25).
- **Passos:** 1. Rodar a Verificação 1 e 2 e conferir os valores "antes". 2. Aplicar `M6` com `Edit`. 3. Rodar a Verificação 1 a 3. 4. Devolver ao chamador a troca aplicada: o veredito do dono sobre `M6` sobe com o de `M1`..`M5` no relatório de encerramento (DSA-24) e não é critério desta revisão.
- **Restrições desta tarefa:** I-5; as contagens que o `README.md` anuncia não mudam.
- **Não fazer:** não editar outra linha nem a segunda célula; não tocar `GOVERNANCA.md` nem a doutrina.
- **Contingências:** 1. se o texto antigo não aparecer exatamente uma vez → parar e sinalizar `blocked` razão `dependencia`, devolvendo a contagem.
- **Testes:** nenhum novo; guarda `check-readme.ps1`.
- **Fora do escopo desta tarefa:** qualquer outra linha do `README.md`; `contador sequencial` sem "global" (`README.md:624`, `GOVERNANCA.md:867`) fica — não contradiz a regra.

## Execução

**Consumo:** 12 tool uses, 47.6 k tokens, 65.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: nenhuma; achado de autoria (total de suite no literal Medido antes) registrado em AE-7, sem corretivo

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
