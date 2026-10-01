# Laudo — P-0754 · AUF-T5

**Percentual:** 100%
**Veredito:** aprovado
**Dimensão bloqueante:** nenhuma
**Recomendação:** seguir
**Pendência:** nenhuma

| dimensão | nível |
|---|---|
| criterio-de-pronto | conforme |
| escopo | conforme |
| testes | conforme |
| guardas | conforme |
| rota | conforme |
| residuo | conforme |
| registro | conforme |

## Motivo das dimensões fora de conforme

nenhum

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Exercicio ponta a ponta (passo 3b) achou defeito anterior a esta entrega e fora de todo card do P-0754: 'review_evidence.py --atribuir' sem .claude/tools/rdo.py na raiz sai com traceback cru (exit 1), enquanto o caminho do dossie sai 'review_evidence: FALHOU - rdo.py: modulo nao encontrado' - contrato de erro divergente entre verbos do mesmo instrumento; rota: AE-<n> na secao 9 do plano, candidato a card de contrato de erro do instrumento |

## Lições aprendidas na tarefa

Reconciliacao sem divergencia: suite re-rodada 516 passed (514 no despacho + 2), Verificacoes 1 e 2 reproduzidas ([1-2-1]). Poder discriminante conferido fora do card: o review_evidence.py de 2ab46ca, num repositorio descartavel com versionado.log rastreado e ignorado, da git show rc 128, tocados ['versionado.log'] com o arquivo intocado e resumo de diferencas vazio com ele alterado - exatamente o que os dois testes novos negam. Ponta a ponta em repositorio descartavel: --capturar-ref com e sem HEAD, indice real (hash de ls-files -s) e lista de stash identicos antes e depois, com mudanca staged, rm --cached e nao rastreado presentes; --atribuir e o dossie completo (--out) coerentes entre si sobre o versionado ignorado (intocado fora, alterado dentro, estado git ' M'). commit-tree em capturar_ref deixou de receber o env do indice temporario - consequencia do recorte, sem efeito (commit-tree nao le indice).
