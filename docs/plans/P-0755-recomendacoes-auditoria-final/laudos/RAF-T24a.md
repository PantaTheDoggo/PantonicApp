# Laudo — P-0755 · RAF-T24a

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
| guardas | parcial | dead_code sai 1 com um achado so, docs/audits/sonda-2026-09-28/passos.py:13 (DRF-44), fora dos Arquivos-alvo e nao tocado pela entrega (blob 8ee3de5 igual no ref baa08f5 e na arvore), admitido na nota do despacho; reconciliado no ato: pytest re-rodado 602 passed = piso 602 do despacho, kit_check check-drift re-rodado exit 0, dead_code re-rodado com o mesmo achado unico; ratchet_piso, validate e check_readme em exit 0 na evidencia |
| testes | nao-se-aplica | nao-se-aplica: classe redacao, card declara nenhum teste novo; a suite inteira (que le a skill via tests/test_progresso_hook.py) medida em guardas: 602 passed |
| residuo | nao-se-aplica | nao-se-aplica: entrega sem artefato executavel, so prosa acrescida numa linha da skill scrum-master (numstat 1/1) |

## Achado de processo

| alvo | achado |
|---|---|
| dossiê | Reincidencia da DRF-44: o dossie de evidencia trava guardas em nao conforme pelo achado pre-existente do dead_code (docs/audits/sonda-2026-09-28/passos.py, blob 8ee3de5) sem carregar a linha de base admitida no despacho; a revisao reconcilia a mao a cada tarefa. Rota: DRF-44 ja aberta na secao 9 do P-0755; somar a reincidencia ao AE-<n> que aponta para ela. |

## Lições aprendidas na tarefa

Troca verbatim conferida por reconstrucao: o arquivo do ref com o trecho antigo substituido pelo novo e byte a byte igual a arvore (445 linhas nos dois, trecho antigo 1 ocorrencia, CR 0). Exercicio ponta a ponta da regra contra os instrumentos que ela cita: backlog.py admite a transicao blocked->ready; encerrar.py marco tem --aceita-versao e --recusa-versao; o validar do modelo.py emite V4 para operacao fora da vigente e da pendente sem olhar status do card - as tres afirmacoes da doutrina casam com o codigo. O ramo de recusa manda o consultor tirar a linha do estado.tsv sem verbo de instrumento para isso (backlog.py nao tem remocao); decisao do card (DRF-63), fora do julgamento desta entrega.
