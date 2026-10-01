# Cenário do consultor — P-0754

Handover entre acionamentos do consultor deste plano (`pantonic-consultant`). Plano:
`docs/plans/P-0754-auditoria-final/plano.md`; estado: `estado.tsv` nesta pasta. Tem autoridade
sobre o plano para o que cobre.

## Estado da janela (2026-09-28)

- Marco 1: `go` do dono em 2026-09-28. `AUF-T16` (auditoria nova) `blocked` por dependência:
  executada pela sessão principal no Marco 2 (`DAU-3`).
- `AUF-T1` `done` 100% (`AE-96`: arquivo novo vazio sai como bloco em branco, fecha com a marca de
  arquivo novo da `AUF-T3`). `AUF-T2` em `review`, laudo ressalva 91%, ressalva sanada pelo consultor
  (`DAU-32`, `AE-97`): pode fechar. `AUF-T3`..`AUF-T15` `ready`. Nenhum commit (commit só no marco).
- Diretiva do dono (2026-09-26), `DAU-20`: nenhum card corretivo nem tíquete por ajuste; achado novo
  vai a `## 9` do plano como `AE-<n>` com rota à `AUF-T16`. Erro inequívoco que mora fora do plano e
  é pequeno o consultor corrige no ato, declarado como `DAU-<n>` (precedente: `DAU-32`).
- Suíte medida em 2026-09-28 depois do `DAU-32`: `508 passed` (505 de HEAD `2513964` + 2 da
  `AUF-T1` + 1 da `AUF-T2`).

## Decisões vivas deste consultor

- **DAU-32** (acionamento 1, `AUF-T2`, `rota=resolve`): a entrega apagou
  `assert "+linha-1" not in texto` do TR `test_tr_arquivo_novo_sem_desde_segue_com_conteudo_integral`
  (`tests/test_review_evidence.py`, logo depois de `assert "linha-1\nlinha-2\n" in texto`). Reposta
  pelo consultor (arquivo em CRLF, preservado). Medido: `git diff 3be2450 --numstat` do arquivo =
  `20 0`; os dois testes exit 0; suíte `508 passed`.
- **DAU-33** (acionamento 2, `AUF-T16`, `rota=resolve`): laudo ressalva 90% (`criterio-de-pronto`
  parcial). O consultor corrigiu no ato o relatório `docs/audits/AUDITORIA_FINAL_KIT.md` (307 linhas):
  `R-26`..`R-31` (reg. 13, 14, 17, 18, 27, 28); `K-39`..`K-43` e reg. 49..54 (checks, skills
  `guardrails-check`, `diario-de-obras`, `passagem-de-bastao`, `checar-versao-kit`; `K-22`, `K-33`);
  reg. 41 e `R-16` pela causa medida (`P-0754-planejador` 45,2k e 69,5k na série);
  reg. 27 → `AE-104`; 19 aprovadas + 1 ressalva. `AE-111`..`AE-113` (processo) e `AE-114`..`AE-116`
  (contingência 2, reg. 23, 24, 36) na §9, rota plano sucessor. Medido: Verificações 1-6 iguais ao
  laudo; 0 registro sem `Origem:`, 0 `K` sem registro, 0 item do corpus sem `K`; `backlog.py check` OK.
  A `AUF-T16` fecha com a ressalva sanada, sem redespacho.

## Vigília para os próximos acionamentos

- `AUF-T3`..`AUF-T6` também acrescentam a `tests/test_review_evidence.py`: a mesma remoção de
  linha vizinha passaria verde por `-k` e pelo piso de contagem (`AE-98`). Na triagem de laudo dessas
  tarefas, conferir `git diff <ref do despacho> --numstat -- tests/test_review_evidence.py` (deleções
  esperadas 0, salvo a asserção que a `DAU-27` manda trocar, e ela é da `AUF-T8`, em outro arquivo).
- `AE-99` (caminho octal chega a `montar_trechos` como ausente) e `AE-98` vão à `AUF-T16`; não
  viram card. Fechados no relatório pela `R-31` e pela `R-12`.
- Os fatos novos da `DAU-33` (reg. 49..54) saíram de artefatos em
  `%TEMP%\claude\auditoria\p0754_artefatos\` e de `.claude/estado/progresso.txt`, fora do repositório.

## Matéria inconclusiva

- `AE-98`: se o remédio (Verificação de deleções = 0 no arquivo de teste) entra como regra do
  planejador ou como checagem do `review_evidence` — decisão da auditoria nova, não deste consultor.
  Fechado: a `R-12` do relatório o põe no `review_evidence.py`.
