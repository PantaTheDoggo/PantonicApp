# RDO — P-0745 · PLN-T1

**Plano:** `docs/plans/P-0745-planejador-modelo-operacao.md`
**Tarefa:** `PLN-T1` — O agregado medido da atuação do planejador
**Modelo:** Sonnet · **Classe:** investigacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** a seção `## 12. Agregado medido` deste plano preenchida com uma tabela por dimensão da §4, dentro de 120 linhas, sem nenhum dado bruto — o retrato do planejador **antes** deste plano.

**Arquivos-alvo:** - `docs/plans/P-0745-planejador-modelo-operacao.md` — só este arquivo, e nele só a seção nova `## 12. Agregado medido`, inserida entre `## 11. Riscos` e `## Achados da execução`. As oito fontes do corpus (`Método de sondagem`) são **lidas, nunca escritas**, e por isso não são arquivo-alvo.

**Verificação:** 1. ``` grep -c '^## 12. Agregado medido' docs/plans/P-0745-planejador-modelo-operacao.md ``` → **1**. **Medido antes: 0**. 2. ``` grep -c '^### [0-9]*\. ' docs/plans/P-0745-planejador-modelo-operacao.md ``` → **10** — as dez subseções do agregado, numeradas. **Medido antes: 0**. 3. ``` python -c "import re,pathlib;t=pathlib.Path('docs/plans/P-0745-planejador-modelo-operacao.md').read_text(encoding='utf-8');m=re.search(r'^## 12\. Agregado medido\n.*?(?=^## )', t, re.M|re.S);print(len(m.group(0).splitlines()) if m else 0)" ``` → um número **maior que 0 e menor ou igual a 120** — a seção inteira, do heading até a linha anterior ao próximo `## `. **Medido antes: 0** — a seção não existe. > **Reparo do consultor, 2026-09-22, com a tarefa já em `review` (`AE-2`).** O comando > publicado originalmente partia o arquivo pelo literal `## 12. Agregado medido`, que ocorre > **primeiro dentro do próprio card** (`Objetivo` e `Formato do agregado`): media prosa do > card, nunca a seção. Medido: devolve **6** no arquivo entregue e **73** no arquivo de > `d75e7a6` — nunca o `IndexError` que o card deduzia, porque o literal já existia no card > antes da entrega. O **critério não mudou** (≤ 120); mudou só o instrumento que o afere, > agora ancorado no heading em início de linha. Medições deste reparo, rodadas: **106** no > arquivo entregue, **0** no arquivo de `d75e7a6`. O número que o executor reportou na linha > de retorno (6) é o da forma antiga. 4. ``` python .claude/tools/backlog.py check ``` → `check: OK — nenhuma violação.`, exit **0**. **Medido antes: o mesmo** (`I-3`).

**Pronto quando:** a seção `## 12. Agregado medido` existe com as dez subseções na ordem da §4, cada uma com a tabela ou com a linha `sem ocorrência no corpus medido`, e a seção inteira tem no máximo 120 linhas — o número que tem de existir ao final é, por dimensão, a contagem de ocorrências e a data da mais antiga e da mais recente. Por propriedade que a operação altera (`DPN-6`): - `agente de planejamento.descrição pública da figura` — a parcela desta tarefa: o retrato medido do antes, de que a descrição depende; a propriedade só alcança o estado final na `PLN-T6` — Verificação 1, 2 e 3. - As demais entregas desta tarefa são **requisito secundário** (`## Requisitos secundários`), não propriedade do modelo: a seção `## 12. Agregado medido` e o corpus fechado de onde ela sai.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-22
- **Fundamento:** `DPN-1`, `DPN-8`; fatos `F-2`, `F-9`. Herda o método da `PLS-T1` do `P-0744` com o corpus ampliado; o corpus é fechado e não se amplia.
- **Operação do modelo:** `OP-5` - OP-5: O redator da especificação descreve a figura de quem planeja depois de medir como ela se comportou até aqui: uma seção por dimensão, cada afirmação ancorada no retrato medido ou na decisão que instituiu o depois, e a última nomeando o que o corpus ainda não permite dizer. - precisa de: agente de planejamento — residências da conduta: `.claude/agents/pantonic-planner.md` (descrição, tese do papel, abertura do protocolo, Fases 3a e 3b, Fase 4, Fase 5, anatomia do card e rodada de replanejamento) e a região gerada `kit:agents` de `.claude/README.md` — produzida por `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` e nunca editada à mão. Residências da régua e da unidade: `GOVERNANCA.md` §3 (matriz de responsabilidades, *A unidade de trabalho é o módulo coeso*, *Diretriz de dimensionamento de tarefa*, tabela da §4, §4.1, §4.3, G-PLANREADY e G-MODULO), `.claude/global/CLAUDE.md` (Regras 2 e 7) e a cópia do dono (`DPN-12`), `docs/RESIDENCIA_DOUTRINA.md`, as skills `diario-de-obras` (*Formato de uma tarefa*), `modelo-por-fase` e `bootstrap-pantonic`, `.claude/agents/pantonic-fora-da-caixa.md` e `README.md`. Residência da responsabilidade pelo lastro: `GOVERNANCA.md` §3.2 e `.claude/agents/pantonic-model-designer.md`, nas duas pontas no mesmo card. Residência da descrição: `docs/planner-spec.md` (novo), uma seção por dimensão da §4, na ordem dela e aberta por `## 0. O que esta especificação não é`. O censo linha a linha, com destino, é a §7; a classe do cabeçalho do card permanece como natureza do trabalho, porque os parsers a leem; ocorrência de outro sentido — escrita atômica em disco, passo atômico de migração — fica intacta; as entradas `RP-1`..`RP-7` e os itens de verificação que não citam ocupação permanecem, são a memória medida do papel; o escopo do papel continua na matriz de `GOVERNANCA.md` §3 (G-SCOPE), e a especificação não é residência nem do escopo nem do protocolo de conduta; agente model designer — não se transforma neste plano: a seção `## 1. Modelo conceitual` escrita por ele e o vocabulário de violações `V1`..`V21` de `.claude/tools/modelo.py` são o insumo que quem planeja consome, e permanecem como estão. `.claude/tools/modelo.py`, `tests/test_modelo.py` e as fixtures **não se tocam**. O que os cards deste plano publicam em `GOVERNANCA.md` §3.2 e em `.claude/agents/pantonic-model-designer.md` é a responsabilidade de **quem planeja** pelo lastro das operações, e nada além disso: o portão com que o modelador aceita ou recusa escrever a seção sobre um plano ainda sem cards não é objeto deste plano — alterá-lo é colateral e se escala
- **Camada e fronteira:** nenhuma camada de produto é tocada. A tarefa lê o corpus e escreve **só** neste arquivo de plano.
- **Método de sondagem:** - **Corpus fechado, nesta ordem e só ele:** (1) `.claude/agents/pantonic-planner.md`, as entradas `RP-1`..`RP-7` e os casos `AE-*` e `DM-*` que elas citam; (2) `docs/plans/P-0739-backlog-instrumento.md`, seção `## Achados da execução`; (3) `docs/plans/P-0740-loop-de-modulos.md`, seção `## Achados da execução`; (4) `docs/plans/P-0741-modelo-conceitual.md`, seção `## Achados da execução`; (5) `docs/plans/P-0743-modelo-de-dominio.md`, seção `## Achados da execução` (`AE-1`..`AE-25`); (6) `docs/Entregas Aceitas/Entregas - P-0743.md`, inteiro; (7) `docs/consultant-spec.md`, §1 e §4, para a fronteira; (8) `docs/telemetria.tsv`, filtrado pelas linhas cujo campo `tarefa` contenha `planej` ou `planner`. - **Acesso barato:** cada seção `## Achados da execução` se alcança por `grep -n '^## Achados da execução' <plano>` seguido de leitura com `offset` e `limit` a partir da linha devolvida. Nenhum plano é lido inteiro. - **Métricas, por dimensão da §4:** número de ocorrências encontradas; a ocorrência mais antiga e a mais recente, com data; a classe de erro dominante, quando houver; e **uma** ocorrência de exemplo, citada por identificador e data, nunca transcrita. - **Métricas de custo (dimensão 7):** de `docs/telemetria.tsv`, o número de linhas de planejamento, o consumo mediano e o máximo, e a data da primeira e da última — com uma linha só (`F-9`), mediana e máximo coincidem e a tabela diz isso. - **Métricas de acionamento (dimensão 9):** número de rodadas de replanejamento ocorridas; quantas fecharam como decisão técnica ou tática no próprio contexto; quantas subiram ao dono; quantas terminaram com o plano `superseded`. - **Formato do agregado que volta:** a seção `## 12. Agregado medido` deste arquivo, inserida imediatamente antes de `## Achados da execução` e depois de `## 11. Riscos`, com **dez** subseções `### <n>. <dimensão>` na ordem da §4, cada uma com uma tabela de no máximo oito linhas. **Teto: 120 linhas** para a seção inteira. - **Nenhum dado bruto entra no agregado:** nenhuma citação literal de achado, nenhum trecho de plano, nenhuma linha de telemetria copiada. Só contagem, data, identificador e classe.
- **Restrições desta tarefa:** - Não ampliar o corpus. Fonte fora da lista de oito itens acima não entra. - Não editar nenhum arquivo além de `docs/plans/P-0745-planejador-modelo-operacao.md`. - Não escrever prosa de recomendação: a tarefa mede, não conclui. - Não commitar (`I-1`).
- **Não fazer:** - Não abrir `docs/DIARIO_DE_OBRAS.md` nem `docs/DIARIO_HISTORICO.md`: estão fora do corpus por tamanho. - Não criar `docs/planner-spec.md`: é a `PLN-T6`. - Não tocar a `## 1. Modelo conceitual` nem nenhum card deste plano.
- **Contingências:** 1. Se uma dimensão da §4 não tiver nenhuma ocorrência no corpus → a subseção dela existe com a tabela vazia e a linha literal `sem ocorrência no corpus medido`. Dimensão sem ocorrência é insumo da dimensão 10, não motivo de parada. 2. Se o agregado passar de 120 linhas → cortar pela cauda das tabelas, mantendo a ocorrência mais antiga e a mais recente de cada dimensão, e registrar na linha de retorno `contingência 2 acionada: <dimensão> cortada de <n> para 8 linhas`. 3. Se alguma das oito fontes do corpus não existir no caminho declarado → parar e sinalizar `blocked` razão `premissa`, com o caminho na linha de retorno.
- **Testes:** nenhum — a entrega é agregado em texto.
- **Fora do escopo desta tarefa:** a redação da especificação (`PLN-T6`) e o índice de documentos (`PLN-T7`).

## Execução

**Consumo:** 28 tool uses, 156.8 k tokens, 631.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: Verificação 3 do card media prosa do próprio card, não a seção entregue (devolvia 6, e o 'Medido antes: IndexError' era dedução falsa); reparada pelo consultor em :461-475, forma nova ancorada em ^## 12 com re.M devolve 106 no entregue e 0 sem a seção
laudo: Duas pendencias sem rota interna: (1) a citacao errada da dimensao 6 da secao 12 precisa ser corrigida antes de a PLN-T6 consumir o agregado como insumo, senao a especificacao herda a ancora quebrada; (2) AE-3 - enquanto houver trabalho nao commitado de outro plano na arvore, nenhum recorte --desde de review_evidence.py isola a entrega, e o reviewer recebe ruido maior que a entrega; o reparo e no instrumento ou na cadencia de commit, ambos fora do escopo do P-0745.

## Laudo

**Veredito:** ressalva

**Percentual:** 88%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar — duas pendências sem rota interna vão ao consultor de plano (B1): a âncora errada da dimensão 6 do agregado, a corrigir antes de a PLN-T6 consumi-lo como insumo; e o AE-3, que é do instrumento e da cadência de commit, fora do escopo do P-0745

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
