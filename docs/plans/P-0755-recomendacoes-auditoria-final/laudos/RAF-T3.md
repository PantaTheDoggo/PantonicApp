# Laudo — P-0755 · RAF-T3

**Percentual:** 91%
**Veredito:** ressalva
**Dimensão bloqueante:** nenhuma
**Recomendação:** seguir com ressalva
**Pendência:** nenhuma

| dimensão | nível |
|---|---|
| criterio-de-pronto | conforme |
| escopo | conforme |
| testes | conforme |
| guardas | parcial |
| rota | conforme |
| residuo | conforme |
| registro | conforme |

## Motivo das dimensões fora de conforme

| dimensão | nível | motivo |
|---|---|---|
| guardas | parcial | dead_code.py sai 1 com 1 achado, o pre-existente de docs/audits/sonda-2026-09-28/passos.py:13 (DRF-44), o mesmo medido no despacho; nenhum achado novo; pytest 530 passed = piso 525 + 5 novos; ratchet, kit_check validate/check-drift e check-readme em exit 0 |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | A regra fechada de conferir_ancoras_do_card (Contratos/classes item 2, DRF-8/DRF-35) toma todo trecho entre crases de Passos e Contratos/classes como ancora: exercitada em leitura sobre cards reais do P-0755, marca como ausente comando, molde e nome de campo (RAF-T30: 21 de 33 linhas 'ancora ausente'; RAF-T3: 'Testes', 'backlog.main([...])'), fatia os code spans de crase dupla em fragmentos (') dos campos', '(regex'), e o padrao (c) nao casa arquivo sem extensao apos o ponto ('.gitignore:12' cai em ausente) nem caminho nao relativo a raiz ('caminhos.py:119') - o pacote leva ruido de ancora ausente falsa ao executor, que a RAF-T4 manda nao reconferir. Entrega fiel ao card. Rota: AE na secao 9 do P-0755, item de replanejamento a triar pelo consultor antes da RAF-T4. |

## Lições aprendidas na tarefa

Os cinco testes da RAF-T3 so exercitam a fixture sintetica, cujo card cita ancoras limpas; o comportamento da regra sobre cards reais (ruido de ancora ausente) so apareceu ao rodar conferir_ancoras_do_card em leitura sobre o proprio plano. Card que fecha regra de parser sobre texto de card ganha em trazer um caso medido sobre card real no aceite.
