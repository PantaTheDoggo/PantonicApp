# RDO — P-0750 · CAH-T1

**Plano:** `docs/plans/P-0750-comunicacao-agente-humano.md`
**Tarefa:** `CAH-T1` — A regra da mensagem legível ao dono, na doutrina e no regulamento global
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O redator da doutrina escreve, ao lado da regra do artefato de humano mínimo, a regra da mensagem ao dono: o dono decide sem abrir outro documento nem perguntar de volta, e nenhuma sigla chega sozinha, vai o título entre aspas como no painel; o regulamento global ganha o eco curto dessa regra.

**Arquivos-alvo:** - `GOVERNANCA.md` - `.claude/global/CLAUDE.md`

**Verificação:** 1. ``` pwsh -NoProfile -Command '(@(foreach ($p in @(@("GOVERNANCA.md","Mensagem legível ao dono"),@(".claude/global/CLAUDE.md","## Regra 9 — ")))) { @(Select-String -LiteralPath $p[0] -SimpleMatch -Pattern $p[1]).Count })) -join " / "' ``` → **1 / 1**. **Medido antes: 0 / 0**. 2. ``` pwsh -NoProfile -Command '"total=" + @(Select-String -Path "GOVERNANCA.md","README.md",".claude/agents/*.md",".claude/skills/*/SKILL.md" -SimpleMatch -Pattern "a sigla só o acompanha, entre parênteses").Count' ``` → **total=1** (a linha da regra em `GOVERNANCA.md`). **Medido antes: total=0**. 3. ``` python -m pytest tests -q ``` → **nenhuma falha**, total igual ao da véspera. **Medido antes: 313 passed** (F-9).

**Pronto quando:** - kit.regra da mensagem ao dono — uma regra única na doutrina, ao lado da regra do texto mínimo, com eco curto no regulamento global — Verificação 1, 2 - kit.nome das coisas na mensagem — em toda mensagem ao dono o título entre aspas substitui a sigla; a sigla só acompanha quando o dono precisa digitá-la — Verificação 1

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Fundamento:** DCH-1, DCH-2, DCH-3, DCH-4, DCH-8; F-2, F-4, F-5, F-7; I-2, I-4.
- **Depende de:** `SAN-T5`
- **Operação do modelo:** `OP-1` - OP-1: O redator da doutrina escreve, ao lado da regra do artefato de humano mínimo, a regra da mensagem ao dono: o dono decide sem abrir outro documento nem perguntar de volta, e nenhuma sigla chega sozinha, vai o título entre aspas como no painel; o regulamento global ganha o eco curto dessa regra. - precisa de: painel do gerente — Quem implementa não o toca. É o padrão copiado: o título entre aspas no lugar da sigla.
- **Camada e fronteira:** doutrina do kit (`GOVERNANCA.md` §4.2) e residência do regulamento global; nenhum código.
- **Passos:** 1. Rodar a Verificação 1 e conferir os valores "antes". 2. Aplicar `H1` e `H2` com `Edit`. 3. Rodar a Verificação 1 a 3.
- **Restrições desta tarefa:** I-2 — o texto da regra entra uma vez em `GOVERNANCA.md`; I-4 — não rodar `materializar.py apply`.
- **Não fazer:** não criar item novo em `GOVERNANCA.md` §7; não tocar o bullet *Artefato de humano mínimo*; não renumerar as regras 1–8 do regulamento global.
- **Contingências:** 1. se `  são aplicações desta regra.` não aparecer exatamente uma vez em `GOVERNANCA.md` (o `SAN-T5` não rodou ou mudou o texto) → parar e sinalizar `blocked` razão `dependencia`. 2. se `  codar a alternativa.` não for a última linha não vazia de `.claude/global/CLAUDE.md` → parar e sinalizar `blocked` razão `premissa`.
- **Testes:** nenhum novo (redação); a suíte inteira roda como TR.
- **Fora do escopo desta tarefa:** a skill (`CAH-T4`), a tabela de falhas (`CAH-T3`), o `apply` em `~/.claude/` (dono).

## Execução

**Consumo:** 13 tool uses, 53.5 k tokens, 95.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
