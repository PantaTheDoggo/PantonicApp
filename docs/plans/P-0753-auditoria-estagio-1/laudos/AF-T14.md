# Laudo — P-0753 · AF-T14

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
| dossiê | Restrição do AF-T14 justifica 'modelo.py check sobre o P-0753 sai 0' com '(o plano não tem ## 1A)', fato falso desde a versão 2 pendente gravada pelo modelador após a AF-T7 (plano.md:173); a restrição segue verdadeira (exit 0 re-medido, agora exercitando o caminho pendente sobre plano real). Rota: sem ação sobre a entrega; item de replanejamento do P-0753 — card cuja restrição cita estado do plano re-confere o parêntese quando o modelador grava versão pendente. |
| dossiê | O dossiê de evidência truncou o diff de modelo.py em 4000 caracteres antes da linha que materializa o Passo 2 (_diff_objetos, contrato); a leitura exigiu abrir o repositório. Rota: sem ação — teto conhecido do instrumento; registrado para o agregado. |

## Lições aprendidas na tarefa

Discriminação confirmada nos dois mundos: o modelo.py de f824f75 sobre a fixture nova dá check exit 0 e show 'sem drift'; o atual dá exit 1 com '1A: V5 OP-3 — objeto inexistente objeto fantasma' e a linha de contrato. Ponta a ponta: fluxo-pendente.md segue exit 1 (agora com '1A: V17 ...' somado), P-0753 real com ## 1A segue exit 0; validar tem um único chamador de produção (verbo_check).
