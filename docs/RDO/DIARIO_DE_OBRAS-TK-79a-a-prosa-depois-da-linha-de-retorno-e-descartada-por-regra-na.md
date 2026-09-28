# RDO — DIARIO_DE_OBRAS · TK-79a

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-79a` — A prosa depois da linha de retorno é descartada por regra, não por sorte
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** o retorno do executor com a linha válida seguida de prosa passa a ter tratamento escrito nas duas pontas: a definição do `pantonic-executor` diz que a última mensagem é só a linha, e que o que precisa chegar ao loop vai em `pendencia=`; a `scrum-master` tipifica, no passo 5 e na `A2`, que a linha válida seguida de prosa vale pela primeira linha não vazia (a mesma que o gancho do painel lê), com a prosa descartada sem reenvio e o descarte anotado no relatório — o resto deixa de se perder calado.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md` - `.claude/agents/pantonic-executor.md`

**Verificação:** 1. ``` pwsh -NoProfile -Command '$s = ".claude/skills/scrum-master/SKILL.md"; $e = ".claude/agents/pantonic-executor.md"; "S1=" + @(Select-String -LiteralPath $s -SimpleMatch -Pattern "Linha válida seguida de prosa").Count + " S2=" + @(Select-String -LiteralPath $s -SimpleMatch -Pattern "prosa **depois** de linha válida").Count + " E1=" + @(Select-String -LiteralPath $e -SimpleMatch -Pattern "**só** a linha de retorno").Count' ``` → **S1=1 S2=1 E1=1**. **Medido na autoria: S1=0 S2=0 E1=0**. 2. `python -m pytest tests -q` → nenhuma falha, total igual ao da referência do despacho.

**Pronto quando:** o passo 5 e a `A2` da `scrum-master` distinguem prosa **no lugar** da linha (inválido, reenvio) de prosa **depois** dela (descarte declarado), e a definição do executor fecha a última mensagem na linha — Verificação 1.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Caso medido que motivou (2026-09-24 e 2026-09-25):** os retornos de `TLG-T5`, `TLG-T3e` e `TLG-T3f` do `P-0748`, e o da `CAH-T2` do `P-0750` (`AE-4`, anexo), trouxeram a linha válida seguida de parágrafos; o de `TLG-T3f` com a proibição escrita no despacho.
- **Passos:** 1. Rodar a Verificação 1 e conferir os valores "antes". 2. Aplicar `S1`, `S2`, `E1` com `Edit`. 3. Rodar a Verificação 1 e 2.
- **Não fazer:** não tocar as demais linhas das tabelas dos blocos A e B, a gramática do passo 4, o `progresso_hook.py` nem o repertório `M-*`.
- **Contingências:** 1. se algum texto antigo não aparecer exatamente uma vez no arquivo → parar e sinalizar `blocked motivo=dependencia`, devolvendo o código da troca.
- **Testes:** nenhum novo (redação); a suíte inteira roda como TR.

## Execução

**Consumo:** 14 tool uses, 50.9 k tokens, 105.3 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
