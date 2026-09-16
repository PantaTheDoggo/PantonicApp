# Laudo — DIARIO · TK-51

**Percentual:** 92%
**Veredito:** ressalva
**Dimensão bloqueante:** nenhuma
**Recomendação:** escalar
**Pendência:** A conclusao 'dentro da dispersao' repousa num teste de intervalo [min,max] que nao distingue ruido de deslocamento: a Tabela A mostra o grupo 'depois' (n=6) com mediana 46.070 contra 34.347 do grupo 'antes' (n=233) - antes de decidir causa/proxima rota, o dono precisa saber que o alto custo se repetiu em todas as 6 janelas pos-corte, e nao apenas na janela tratada.

| dimensão | nível |
|---|---|
| criterio-de-pronto | conforme |
| escopo | conforme |
| testes | nao-se-aplica |
| guardas | conforme |
| rota | conforme |
| residuo | nao-se-aplica |
| registro | parcial |

## Lições aprendidas na tarefa

Tarefa de classe investigacao com sonda de desenho fechado: o gate de calibracao passou na primeira formula candidata (custo zero de tentativa e erro), mas o desenho fixado no card apoiava-se num fato de corpus nao verificado pelo planejamento - o campo 'agentType' nao existe como top-level nos .jsonl, so no sidecar subagents/agent-*.meta.json. O executor achou fonte equivalente e nao gastou round-trip 'blocked'; o custo real dessa classe de tarefa esta em verificar o corpus ANTES de fechar o desenho da sonda, nao em rodar a sonda.

## Evidência mecânica desta revisão

O dossiê de evidência de `review_evidence.py` **não existe** para esta tarefa (ver Achado 1). A
camada mecânica foi reproduzida pelo reviewer, em leitura, e todos os comandos fecharam verdes:

- `python -m pytest -q` -> **exit 0**, 85 passed.
- `pwsh .claude/checks/kit_check.ps1 -Mode validate` -> **exit 0** (8 agentes, 11 skills, 21 entradas).
- `pwsh .claude/checks/kit_check.ps1 -Mode check-drift` -> **exit 0** (README do kit == regenerado).
- `python .claude/checks/ratchet_piso.py` -> **exit 0** (nenhum piso declarado).
- `pwsh .claude/checks/check-readme.ps1` -> **exit 0** (16 guardrails, 14 seções com fonte válida).
- `(Get-Content docs/CUSTO_DO_PICKUP.md).Count` -> **351**, igual ao `(~351 linhas)` gravado no
  `DOC_MAP.md`; a `## 11` ocupa as linhas 308-351 = **44 linhas** (teto do dossiê: 55).
- Escopo: os três alvos declarados (`docs/CUSTO_DO_PICKUP.md`, `docs/DOC_MAP.md`,
  `docs/DIARIO_DE_OBRAS.md`) têm mtime 11:05 de 2026-08-24; todo o resto da árvore suja é anterior
  (`.claude/tools/uow.py` 10:41, `README.md` 09:52, `docs/telemetria.tsv` 10:26) e idêntico ao
  estado pré-despacho. **Nenhum arquivo sob `.claude/` tocado**, nenhum arquivo novo versionado --
  a sonda e os TSVs ficaram fora do repo, como o dossiê exigia.
- `README.md` corretamente **não** tocado: a única ocorrência de `CUSTO_DO_PICKUP` no espelho
  (linha 339) nomeia o arquivo e não enumera seções -- a condicional do dossiê não disparou.

Nenhuma dimensão chegou vermelha da camada mecânica; nenhum `--vermelho-mecanico` aplicado.

## Motivo das dimensões fora de `conforme`

### `testes` -- `nao-se-aplica`

Dossiê de classe investigação/redação: o campo **Verificação** não exige teste funcional nem de
regressão, e a entrega é de três arquivos de documentação. A suíte segue medida por `guardas`
(85 passed, exit 0).

### `residuo` -- `nao-se-aplica`

Entrega sem artefato executável: nenhum símbolo, módulo ou arquivo de produção novo. O único
artefato executável da tarefa -- `sonda_dx5.py` -- era descartável por desenho (decisão 5 do
escopamento) e foi confirmado **fora do repositório**; nenhum artefato de rota abandonada
sobreviveu ao commit.

### `registro` -- `parcial`

Dois defeitos, ambos no bloco **Resultado** do `docs/DIARIO_DE_OBRAS.md` (linhas 838-849):

1. **Achado sem rota.** A execução descobriu que o campo `agentType` **não existe** como campo
   top-level nos `.jsonl` -- contradizendo a definição de corpus do próprio dossiê -- e resolveu a
   classificação pelo sidecar `<sessão>/subagents/agent-*.meta.json`. O fato está registrado em
   prosa dentro da `## 11` (linha 310) e **em lugar nenhum mais**: sem tíquete, sem `sem ação`, sem
   linha no índice do diário. O agravante é que o dossiê afirma que a `CTX-T3`/`CTX-T4` agregou
   `pantonic-executor` **n=149** por esse campo, enquanto a `TK-51` mediu **n=161** pelo sidecar --
   divergência entre duas medidas registradas que ficou sem rota.
2. **Verificação parafraseada.** O bloco **Resultado** narra os resultados (M1/M2/M3, veredito) mas
   não registra a aferição que o campo **Verificação** do dossiê pediu: a contagem de linhas antes x
   depois e o `git status --short`. Quem não executou não consegue reconferir o teto de 55 linhas
   nem o escopo pelo registro -- só refazendo a medida, como este laudo teve de fazer.

**Não pesou na marcação:** a ausência de `Consumo:` no bloco Resultado e de linha `TK-51` em
`docs/telemetria.tsv`. Consumo é registro **medido** pela orquestração (`GOVERNANCA.md` §3), passo
posterior a esta revisão, e a rubrica só reprova consumo **autorado pela execução** -- não é o caso.
Nenhum número de consumo pontuou dimensão alguma neste laudo.

## Achados de processo

### Achado 1 -- alvo `doutrina`: tíquete residente no diário não tem dossiê de evidência possível

O protocolo de revisão exige o dossiê de `review_evidence.py` como uma das três entradas de
julgamento, e o instrumento recebe `--plano <caminho do .md do plano>`. A `TK-51` **não mora em
plano**: é tíquete do `docs/DIARIO_DE_OBRAS.md`. A chamada
`python .claude/tools/review_evidence.py --plano docs/DIARIO_DE_OBRAS.md --tarefa TK-51` falha com
**exit 1** (`tarefa: TK-51 não encontrada`), mesmo com o card `### TK-51` presente na linha 762.
Consequência medida: esta revisão julgou **sem** a metade mecânica travada e teve de reproduzi-la à
mão. Toda tarefa despachada a partir do diário, e não de um plano, cai no mesmo buraco.
**Rota:** tíquete no `docs/plans/_INBOX.md` -- *"`review_evidence.py` aceita tíquete residente no
diário de obras (`### TK-<n>`), ou a doutrina proíbe despachar tíquete de diário à revisão"*.

### Achado 2 -- alvo `dossiê`: o desenho fechado da sonda fixou um fato de corpus falso

O card fecha o corpus com *"janela principal = arquivo sem campo `agentType` nas entradas lidas;
janela de subagente = o valor do `agentType`"* e instrui *"o executor implementa, não projeta"*. O
campo não existe. A execução entregou fielmente o que o dossiê pediu, achando fonte equivalente sem
gastar round-trip `blocked` -- por isso **nenhuma dimensão de entrega foi rebaixada por este achado**
(`RUBRICA_DE_REVISAO.md` §6, invariante 1). O defeito é do planejamento: desenho de instrumento
fechado sobre estrutura de dados não verificada. **Rota:** item de replanejamento -- quando o card
fixa o desenho de uma sonda, o planejador verifica a estrutura do corpus antes de fechar, ou marca o
ponto como *a confirmar na calibração*.

### Achado 3 -- alvo `dossiê`: a linha de fecho obrigatória não discrimina o que a tarefa foi medir

A segunda linha de fecho é imposta no formato *"46.071 está dentro/fora do intervalo [mín, máx] da
baseline estendida"*. Pertinência ao intervalo `[mín, máx]` de n=233 é o teste menos discriminante
possível: qualquer valor abaixo do máximo histórico passa como "dentro", inclusive uma distribuição
inteiramente deslocada. Foi o que aconteceu -- a própria Tabela A mostra `depois` (n=6) com
**mediana 46.070** contra **34.347** do `antes`, isto é, as seis janelas pós-corte agrupadas no topo
da faixa histórica, e ainda assim a linha de fecho devolve "dentro". O executor publicou os dois
fatos, como mandado; o defeito é da verificação exigida, não da entrega. **Rota:** subiu ao dono
pelo `--escalar` deste laudo -- a linha de fecho lida isolada e a Tabela A lida inteira levam a
decisões opostas sobre causa/próxima rota, e a escolha do critério é dele.

## Observações que não rebaixam dimensão

- **Vocabulário do bloco Veredito.** O dossiê fecha quatro formas (`subiu <N> tok`, `desceu <N> tok`,
  `estável (|Δ| < 500 tok)`, `não isolado`), uma linha por componente. Três das quatro linhas
  obedecem; a quarta (dispersão M1) combina duas formas na mesma linha -- *"**subiu** frente à
  mediana, mas **estável** frente ao máximo histórico"* -- e usa `subiu` sem o `<N> tok`. O critério
  de pronto não carrega essa exigência, então não marcou; fica como nota de forma.
- **Tabela de blocos entregue em prosa.** O formato pedia a tabela de blocos por janela com Δ de
  cada bloco. Como os quatro preâmbulos armazenados não trazem nenhum marcador
  (`<system-reminder>`/`gitStatus:`/`<env>`) e tudo colapsou num único bloco `pedido`, a tabela teria
  uma linha só; o executor deu o Δ em uma frase (linha 330). Conteúdo satisfeito.
- **Conversão chars->tok da Tabela B.** O visível em tokens sai do câmbio 0,590 chars/tok da M3, cuja
  regressão tem **r²=0,030** -- o nível absoluto de visível e opaco é, portanto, frouxo. A
  **conclusão** não depende disso: os `chars_preâmbulo` das quatro janelas são praticamente idênticos
  (11.684 / 11.684 / 12.138 / 11.683), logo `Δ visível ~ 0` sob qualquer câmbio, e o Δ cai no opaco
  por construção. O método foi o que o dossiê fixou (decisão 2 / M2), e o executor o seguiu.
- **Proibições respeitadas.** A `## 11` não propõe, não recomenda e não executa corte algum; nenhum
  prompt, agente, skill ou superfície de ferramenta foi tocado; `docs/telemetria.tsv` não foi
  retificado; `docs/plans/P-0738-contexto-esgotado.md` não foi reaberto; o gate de calibração passou
  na primeira fórmula candidata e foi declarado na publicação.
