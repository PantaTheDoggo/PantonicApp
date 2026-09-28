# RDO — P-0749 · SAN-T6

**Plano:** `docs/plans/P-0749-saneamento-artefatos.md`
**Tarefa:** `SAN-T6` — A porta de entrada descreve a pasta, a tabela e o texto mínimo
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O mantenedor da porta de entrada do repositório reescreve a descrição pública do kit: pasta por plano, tabela de estado e artefato de humano mínimo.

**Arquivos-alvo:** - `README.md`

**Verificação:** 1. ``` pwsh -NoProfile -File .claude/checks/check-readme.ps1 ``` → **exit 0, com a linha que começa por `check-readme: OK - 10 agente(s), 11 skill(s), 20 guardrail(s)`**. **Medido antes: check-readme: OK - 10 agente(s), 11 skill(s), 20 guardrail(s)**. 2. ``` pwsh -NoProfile -Command '(@(foreach ($p in "P-NNNN","P-<n>-<slug>/","Artefato de humano mínimo") { @(Select-String -LiteralPath README.md -SimpleMatch -Pattern $p).Count })) -join " / "' ``` → **0 / 2 / 1**. **Medido antes: 3 / 0 / 0**. 3. ``` python -m pytest tests -q ``` → **o total do despacho, nenhuma falha**. **Medido antes: 339 passed** (2026-09-25, com a entrega de `AE-1`; 313 em 2026-09-24). 4. ``` veredito do dono sobre as trocas M1..M4 ``` → **go**. **Medido antes: sem veredito**. **Aferição: manual**.

**Pronto quando:** - kit.porta de entrada — descreve pasta por plano, tabela de estado e a regra do texto mínimo — Verificação 1, 2, 4

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Fundamento:** DSA-3, DSA-4, DSA-5, DSA-11; G-README (a revisão do `README.md` fecha a sprint).
- **Depende de:** `SAN-T5`
- **Operação do modelo:** `OP-6` - OP-6: O mantenedor da porta de entrada do repositório reescreve a descrição pública do kit: pasta por plano, tabela de estado e artefato de humano mínimo. - precisa de: kit — Quem implementa recebe essas ferramentas e esses textos. O que já está gravado continua sendo lido como hoje.; plano novo — Quem implementa não o escreve. A forma com que ele nasce mostra se o kit mudou.
- **Camada e fronteira:** só o `README.md`; ele aponta para a regra, não a copia (I-5).
- **Passos:** 1. Rodar a Verificação 1 e 2 e conferir os valores "antes". 2. Aplicar `M1`..`M4` com `Edit`. 3. Rodar a Verificação 1 a 3. 4. Devolver ao chamador as quatro trocas aplicadas, para o veredito do dono.
- **Restrições desta tarefa:** I-5 — o `README.md` aponta para a regra, não a copia; as contagens que o `README.md` anuncia (agentes, skills, guardrails) não mudam.
- **Não fazer:** não editar outra seção do `README.md`; não tocar `GOVERNANCA.md` nem a doutrina.
- **Contingências:** 1. se um texto antigo não aparecer exatamente uma vez → parar e sinalizar `blocked` razão `dependencia`, devolvendo o código da troca; 2. se `check-readme.ps1` sair diferente de 0 → corrigir a troca que o quebrou; persistindo → parar e sinalizar `blocked` razão `premissa`, devolvendo a saída.
- **Testes:** nenhum novo; guarda `check-readme.ps1`.
- **Fora do escopo desta tarefa:** qualquer outra seção do `README.md`.

## Execução

**Consumo:** 12 tool uses, 50.0 k tokens, 63.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: nenhuma; criterio-de-pronto parcial: Verificacao 4 (veredito do dono sobre M1..M4) vai ao dono no relatorio de encerramento; achados com rota em AE-5 do P-0749

## Laudo

**Veredito:** ressalva

**Percentual:** 88%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir com ressalva

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
