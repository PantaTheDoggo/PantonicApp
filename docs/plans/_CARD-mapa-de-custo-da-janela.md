# Card de invocação — Mapa de custo da janela mais cara

> **Não é plano.** É o portador da diretiva do dono, escrito para atravessar um `/clear`. Nenhum
> ID de plano foi alocado: `P-0739` segue livre, e se esta matéria vira plano formal é decisão da
> rodada de planejamento que este card abre. Prefixo `_` pela mesma convenção de `_INBOX.md`.
>
> **Origem:** parada por poluição de contexto (Regra 2) em 2026-08-31 — a diretiva abaixo
> contradiz decisões fechadas que o contexto anterior tinha ingerido por inteiro, e por isso o
> desenho **não** foi autorado lá. Este card carrega a diretiva e os insumos; o método é da
> rodada nova.

## Como invocar

Abrir janela limpa (`/clear`), pôr o modelo em `/model opus` — é rodada de **planejamento**,
fase intelectual — e mandar:

> Leia `docs/plans/_CARD-mapa-de-custo-da-janela.md` e conduza a rodada de planejamento que ele
> descreve.

## Diretiva do dono (verbatim, 2026-08-31)

> "A análise não foi adequadamente feita, pois ela focou apenas no volume e não no conteúdo.
> Eu preciso do mapeamento completo dos custos da janela mais cara, para identificar os
> desperdícios reais. Essa análise numérica não traz valor nenhum para a discussão. Refazer e
> mapear exatamente cada porcentagem com seu objetivo, e avaliar economicamente cada extrato:
> gastos incontornáveis, gastos que podem ser contornados, ineficiências inerentes do framework
> mas que poderiam ser mitigados, ineficiências que inviabilizam o framework."

## O entregável

Um **mapa de composição** da janela mais cara: extrato a extrato, cada um com (a) o percentual do
custo de abertura que ocupa, (b) **o propósito que serve**, e (c) a classificação econômica em um
dos quatro baldes do dono:

1. **Incontornável** — custo que existe para a coisa funcionar; cortar quebra.
2. **Contornável** — custo que serve a um propósito real, mas que outra forma atenderia mais barato.
3. **Ineficiência inerente ao framework, mitigável** — o desenho cobra isso por construção, e dá
   para reduzir sem trocar o desenho.
4. **Ineficiência que inviabiliza o framework** — custo que, mantido, derruba a economia da
   operação. É o balde que muda rota, não parâmetro.

O que reprova esta rodada é repetir o erro anterior: entregar dispersão, mediana e delta de um
**total** sem dizer de que o total é feito nem se cada parte se justifica.

## O que NÃO herdar (ponto crítico)

Ao ler `docs/DIARIO_DE_OBRAS.md`, a rodada nova vai encontrar a doutrina do `TK-51`/`TK-53`, que
**esta diretiva derruba**. Ela está viva no arquivo e vai parecer vinculante:

- `TK-51`, decisão 1: *"a metade opaca se precifica por regressão, não por adivinhação de payload"*.
- `TK-53`, decisão 1: *"discriminar camada, não adivinhar payload"*; decisão 6: *"toda conclusão se
  apoia em `usage_1` e `chars_preambulo` brutos"*.

Essas decisões proibiam exatamente o que o dono está pedindo. **Elas não governam esta rodada.**

E a premissa que as sustentava — *"a metade opaca só se mede por diferença"* — é **provavelmente
falsa**, e é o que fazia a pergunta do dono parecer inviável. Boa parte da superfície opaca é
**enumerável**: os esquemas das ferramentas registradas e as skills anunciadas existem em arquivo
e no próprio anúncio da sessão. O que de fato não é legível é só o prompt de sistema do produto.
Confirmar até onde a enumeração chega é a primeira coisa a estabelecer — e é o que decide se o
mapa fecha em 100% ou fecha com um resíduo declarado.

## Insumos que já existem (verificar antes de confiar)

**Medidas anteriores** (respondem *quanto*, não *de quê* — servem de baseline e de ponto de partida
para escolher a janela):

- `docs/CUSTO_DO_PICKUP.md` — `Grep pattern:"^## 11 "` (composição visível × opaco, `TK-51`) e
  `Grep pattern:"^## 12 "` (os três eixos, `TK-53a`). Arquivo em 402 linhas, já **acima** do teto de
  320 da `DX-3` — ver decisão pendente 2 abaixo.
- `docs/DIARIO_DE_OBRAS.md` — `Grep pattern:"^## TK-51 "`, `"^## TK-53 "`, `"^### TK-53a "`.
  Ler **só** a faixa da âncora; nunca o diário inteiro.

**Sondagem já paga que sobreviveu ao `/clear`** — em
`C:\Users\panta\AppData\Local\Temp\claude\d--workspaces-PantonicApp\34e72d6b-061e-4ba0-8029-012047b5e9d9\scratchpad\`:

- `serie_dx6.tsv` (147 KB) — **uma linha por janela do corpus inteiro**, com `projeto`, `arquivo`,
  `ts_inicio`, `escopo` (`principal` / `subagente:<papel>`), os três componentes de token, `usage_1`,
  `chars_preambulo`, `version`, `gitBranch`. **Serve para eleger a janela mais cara sem re-rodar
  nada** — é ordenar por `usage_1`.
- `sonda_dx6.py` (12,6 KB) — a sonda que gerou o TSV; lê `.jsonl` linha a linha parando na 1ª
  entrada `assistant` com `usage`. Referência de como varrer o corpus sem estourar contexto.

É diretório temporário: **testar existência antes de planejar em cima**. Se sumiu, o desenho da
sonda está no card `### TK-53a` do diário e se reescreve — mas note que ela mede **volume**, que é
o que o dono recusou; o instrumento desta rodada é outro, e itemiza conteúdo por origem.

## Decisões do dono, pendentes (levantadas na parada, não resolvidas)

1. **O que acontece com o `TK-53`.** O `TK-53a` entregou e mediu `sem degrau (oscilação
   pré-existente)` — contradizendo a premissa com que o tíquete foi aberto. O `TK-53b` nunca rodou e
   **perdeu o objeto** (só existia para filtrar candidatos dentro de um intervalo de degrau que a
   medição diz não existir). O tíquete vira `superseded` por esta diretiva, ou segue vivo em
   paralelo? Enquanto não decidir, a `Fila corrente` do diário mantém o `TK-53b` travado.
2. **Teto de `docs/CUSTO_DO_PICKUP.md`.** 402 linhas contra as 320 da `DX-3`, e este mapa é maior
   que qualquer seção anterior. Partir o arquivo, arquivar seções antigas, ou o mapa nasce em
   artefato próprio? A `DX-3` proíbe renomear/duplicar, então isso é decisão sua, não do planejador.
3. **O `P-0737` (loop autônomo) continua `blocked`?** A razão registrada hoje é a premissa de custo
   fixo de abertura de janela. Esta rodada é que vai dizer se esse custo é justificável — então o
   destravamento provavelmente é **consequência** dela, não pré-requisito. Registrado para não se
   perder.

## Fronteiras

- Rodada de **planejamento**: produz desenho e decisões fechadas, não implementa sonda nem publica
  medida. Se a decomposição couber numa tarefa atômica, ela sai delegável sem round-trip
  (`G-PLANREADY`).
- Vale a decisão 10 do `TK-53`, que **não** é derrubada por esta diretiva: *medir não pode mexer no
  que se mede* — nenhuma alteração de prompt, agente, skill, memória, `settings` ou superfície de
  ferramenta durante a medição, sob pena de corromper a própria série.
