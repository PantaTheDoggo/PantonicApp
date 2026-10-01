# Laudo — P-0755 · RAF-T1

**Percentual:** 88%
**Veredito:** ressalva
**Dimensão bloqueante:** nenhuma
**Recomendação:** seguir com ressalva
**Pendência:** nenhuma

| dimensão | nível |
|---|---|
| criterio-de-pronto | conforme |
| escopo | conforme |
| testes | nao-se-aplica |
| guardas | parcial |
| rota | conforme |
| residuo | nao-se-aplica |
| registro | conforme |

## Motivo das dimensões fora de conforme

| dimensão | nível | motivo |
|---|---|---|
| guardas | parcial | dead_code sai 1 por docs/audits/sonda-2026-09-28/passos.py:13, arquivo untracked de 2026-09-28 16:23 (antes do ref 14f0161 de 22:03), fora dos Arquivos-alvo e na lista Fora do alcance; a entrega so tocou SKILL.md (sem Python), logo a falha e anterior a tarefa; pytest 521 passed e check-drift 0 re-rodados na revisao |
| testes | nao-se-aplica | classe redacao sem teste de codigo exigido; a suite (521 passed, piso mantido) e medida em guardas |
| residuo | nao-se-aplica | entrega sem artefato executavel: so prosa na skill |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | dossie de evidencia do P-0755 herda vermelho de dead_code causado pela sonda untracked docs/audits/sonda-2026-09-28/passos.py (fora do alcance de toda tarefa do plano): toda revisao da janela vai reconciliar o mesmo vermelho. Rota: AE-<n> na §9 do P-0755 - excluir docs/audits/ da varredura do dead_code ou versionar/remover a sonda por decisao da conducao |
| dossiê | Passo 1 do RAF-T1 manda 'cada linha perde os dois espacos do recuo deste card' sobre um bloco recuado 5 espacos: o resultado literal (3 espacos) fez '- **Janela:**' virar sub-item aninhado do bullet '- **Ação:**' no Markdown, e nao campo irmao de Gatilho/Entrada/Acao/Saida. A execucao seguiu o card a letra; a Verificacao 1 (count do literal) nao discrimina o recuo. Rota: AE-<n> na §9 do P-0755 - decidir se o campo sobe a coluna 0 (card de reparo) e fixar no planejador a forma 'perde o recuo deste card' usada em RAF-T3/RAF-T4 |

## Lições aprendidas na tarefa

Instrucao de recuo relativa ('perde N espacos') e fragil quando o bloco vive dentro de item numerado; a forma absoluta ('perde o recuo deste card', usada no item 4 da RAF-T3) nao deixa margem. A Verificacao por count de substring e cega a recuo.
