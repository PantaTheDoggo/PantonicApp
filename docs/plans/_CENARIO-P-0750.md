# Cenário do P-0750 — consultor

Plano: `docs/plans/P-0750-comunicacao-agente-humano.md` (legado, não rastreado). Modelo `## 1` versão 1, vigente, 5 operações; nenhum dossiê de emenda pendente.

## Decisões vivas (do consultor)

- Nenhuma decisão `DCH-` nova. Os reparos dos acionamentos 1 e 2 são trocas literais (`K2` no card da `CAH-T4`; corretivo `CAH-T4a`), sem mudar objeto, operação nem estado final da `## 1`.

## Fila

`CAH-T1`..`CAH-T4` `done` → `CAH-T5` `ready` (next) → `CAH-T4a` `ready`, corretivo da `CAH-T4` (`AE-7`, `OP-4`, listado em `tarefas:`), depende só de `CAH-T4`, posto depois para não reordenar. Medido no acionamento 2: `backlog.py check` exit 0, `next` = `CAH-T5`, `modelo.py check --plano` OK (5 operações, 6 tarefas).
`CAH-T4a`: troca `T1` de uma célula da §2 da skill; medida numa cópia (`novo=1 antigo=0`). `check-drift` numa cópia de `.claude/` falha sempre pela materialização (caminho absoluto, 13 problemas, com e sem `T1`) — não usar cópia para medir `check-drift`; na árvore, exit 0.

## Achados

- `AE-1`, `AE-2`, `AE-4` — régua de autoria (`TK-72`), sem corretivo (loop).
- `AE-3`, `AE-5` — ruído dos não rastreados de antes do despacho (`TK-55`); espere o mesmo no laudo da `CAH-T4` (agora com `SKILL.md` da execução anterior também não rastreado, sem diff).
- `AE-6` — absorvido (acionamento 1): `F-6` omitia que `check-readme.ps1` confere o numeral da frase de contagem; `K2` no card, `F-6` complementado. Régua de autoria `TK-72`: card que cria/apaga skill ou agente troca o numeral.
- `AE-7` — absorvido (acionamento 2): a §2 da skill tomava por título a etiqueta `[modelo · esforço · classe]` do cabeçalho de tarefa; corretivo `CAH-T4a`. Régua `TK-72`: literal que descreve saída de instrumento se confere contra a saída medida.

## Inconclusivo

- `CAH-T5` não cria nem apaga skill/agente: sem risco de contagem. Não conferido se `.claude/README.md` gerado repete alguma contagem por extenso (check-drift exit 0 hoje).

## Acionamentos

1. 2026-09-25 · `CAH-T4` · gatilho 1 (`blocked` premissa, Verificação 2) · `rota=resolve` · `K2` + contingência 3; redespacho normal (defeito do card, não improcedência).
2. 2026-09-25 · `CAH-T4` (laudo aprovado 100, `AE-7`) · gatilho 2 · `rota=resolve` · corretivo `CAH-T4a` depois da `CAH-T5`.
