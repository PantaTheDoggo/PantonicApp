# RDO — P-0740 · LM-T17

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T17` — Um referente, um rótulo: o censo fecha por token, não por frase
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — o mesmo evento deixa de ter dois rótulos no mesmo documento. Hoje a spec diz `três instanciações` (`:7`) e `As quatro instâncias medidas` (`:28`), e chama o grupo `ESC-27`..`ESC-36` ora de `3ª instância` (`:63-64`) ora de `instância do recorte` (`:134-135`).

**Arquivos-alvo:** - `docs/consultant-spec.md`

**Verificação:** (todas por **regex sobre o texto inteiro**, nunca por casamento linha a linha — é a lição do `AE-73` posta no instrumento do próprio aceite) 1. ``` python -c "import re;from pathlib import Path;print(len(re.findall(r'3ª',Path('docs/consultant-spec.md').read_text(encoding='utf-8'))))" ``` → **1**: sobra **só** a célula da tabela. Uma linha cobre **toda** forma em prosa — quebrada, abreviada, com ou sem substantivo. **Medido antes: 3**. 2. ``` python -c "import re;from pathlib import Path;print(len(re.findall(r'três instanciações',Path('docs/consultant-spec.md').read_text(encoding='utf-8'))))" ``` → **0**. **Medido antes: 1**. 3. ``` python -c "import re;from pathlib import Path;print(len(re.findall(r'quatro instanciações',Path('docs/consultant-spec.md').read_text(encoding='utf-8'))))" ``` → **1**. **Medido antes: 0**. 4. ``` python -c "import re;from pathlib import Path;print(len(re.findall(r'instância do recorte',Path('docs/consultant-spec.md').read_text(encoding='utf-8'))))" ``` → **9**: as sete de antes mais as duas novas. **Medido antes: 7**. 5. ``` python -c "import re;from pathlib import Path;print(len(re.findall(r'33\s+entregas até o',Path('docs/consultant-spec.md').read_text(encoding='utf-8'))))" ``` → **1**: o número da série ganha recorte nomeado. **Medido antes: 0**. 6. ``` python -c "import re;from pathlib import Path;print(len(re.findall(r'4ª',Path('docs/consultant-spec.md').read_text(encoding='utf-8'))))" ``` → **1**, **inalterado**: a prosa **não** troca um ordinal por outro — o rótulo ordinal vive só na tabela, onde um recenseamento futuro o corrige na mesma célula do recorte. **Medido antes: 1**. 7. ``` python -m pytest tests/ -q ``` → verde, **sem reduzir** o total re-medido no despacho (`DM-23`): esta tarefa não toca código. **Medido antes: exit 0** — veredito invariante; referência **datada**: `201 passed`.

**Pronto quando:** `3ª` aparece **uma** vez e só na tabela, `quatro instanciações` substituiu `três`, as duas referências novas nomeiam o recorte, a frase dos cards autorados carrega o corte `até o` `ESC-36`, nenhum juízo mudou — e as **sete** linhas de `Verificação` saem nos valores declarados.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` · 2026-09-19 — card novo do `ESC-40` (2026-09-19), pendência do laudo da `LM-T16`. **É a última rodada de correção sobre `docs/consultant-spec.md` neste plano** (teto declarado em `## 6`): achado novo depois dela vai ao plano que o dono declarou sobre a figura, não a outro card.
- **Esforço:** low
- **Depende de:** nada. Nada depende desta.
- **Causa medida, e é do aceite anterior, não da entrega:** a `Verificação` 11 da `LM-T16` usou `Select-String -SimpleMatch`, que casa **linha a linha** e não enxerga texto quebrado por soft-wrap. A população real de ocorrências era **8**, não 7: `grep -c '3ª instância'` devolve **0**, e a regex multilinha `3ª\s+instância` devolve **1**, em `:63-64`. Some-se `:144` (*"quatro na 3ª"*), que é referência **sem o substantivo** e escapa de qualquer busca pelo literal composto. **Por isso este card afere por token, com regex sobre o texto inteiro** — o rótulo `3ª` só pode sobrar **uma** vez, na célula da tabela, e qualquer forma em prosa (quebrada, abreviada, com ou sem substantivo) cai na mesma contagem.
- **Produto do módulo:** três substituições, todas com o literal prescrito e medidas no `ESC-40`. - **(a) `:7`** — `três instanciações` vira `quatro instanciações`. É a linha do **Método**, e é a que contradiz o título da tabela. - **(b) `:63-64`** — `Medido no primeiro acionamento da 3ª instância:` (quebrada entre as duas linhas) vira `Medido no primeiro acionamento da instância do recorte` seguido de `ESC-27`..`ESC-36` entre crases. - **(c) `:143-145`** — a frase dos cards autorados fecha **por inteiro** (`ESC-34`), porque carrega **três** números e um deles é série que o próprio ato de escrever incrementa: `quatro na 3ª` vira `quatro na instância do recorte` + o corte, e `que levou o plano de 29 a 33 entregas` ganha o recorte — `de 29 a 33 entregas até o` + `ESC-36` entre crases. Sem o recorte, o número morre no escalonamento seguinte, que é o `AE-70` de novo; `quatro na 1ª` e `as partições de dois cards em três` ficam **literais**, porque são verdadeiros e fechados.
- **Restrições desta tarefa:** **nenhum juízo da spec se reabre** — respostas, estrutura e conclusões ficam literais; muda rótulo e recorte. **Nenhum ordinal novo entra na prosa**: o substituto é sempre o recorte. A tabela de `§1` **não** se toca: ela já está correta desde a `LM-T16`, e a `Verificação` 6 tranca isso. Nenhum outro arquivo é tocado.
- **Não fazer:** não renumerar o bloco `Verificação` da `LM-T16` no plano (card fechado é registro, `DM-33` (iii) — a ordem `1..9, 11, 12, 13, 10` fica como está, com o defeito registrado no `AE-73`); não reabrir a fronteira com o `pantonic-planner`; não commitar.
- **Contingências:** 1. se a contagem de `3ª` no despacho não for **3** → **usar o medido no ato** e reportar: o aceite é *sobrar exatamente a célula da tabela*, não o número de partida; 2. se alguma das três substituições exigir mexer em juízo para não ficar contraditória → **parar** e sinalizar `blocked` razão `premissa`, nomeando a passagem.

## Execução

**Consumo:** 16 tool uses, 57.9 k tokens, 111.7 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: docs/consultant-spec.md secao 10 publica 'o emprestimo e fato medido nove vezes' sem recorte e a arvore mede 11 - a figura autorou LM-T16 (ESC-37) e LM-T17 (ESC-40) depois do ESC-36: o artefato que o dono le para decidir carrega um numero que o proprio ato de escalonar falsificou, fora do escopo desta entrega e vedado a card novo pelo teto do ESC-40, logo a rota e o plano que o dono declarou sobre a figura.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

Aceite por token fechou o que o aceite por frase deixara passar: len(re.findall(r'3a')) cai de 3 para 1 e alcanca a forma quebrada por soft-wrap que Select-String -SimpleMatch nao enxerga (AE-73); as seis linhas de regex sairam exatamente nos valores declarados (1, 0, 1, 9, 1, 1) e a bateria inteira da LM-T16, re-rodada sobre a arvore de hoje, sai verde nas nove linhas - prova de que a terceira rodada nao desfez a segunda (pytest: 201 passed, igual a referencia datada). O que o token nao cobre e REFERENTE: os dois primeiros achados sairam da leitura ponta a ponta do documento, nao de contagem nenhuma - aceite completo por construcao para a pergunta que faz nao e aceite completo para a coerencia do artefato. Consumo medido (57,9k tk, 16 tool uses): o card trouxe o literal ja medido no ESC-40 e nao deixou nada para o executor decidir - e isso que o numero mostra.

## Fechamento

**Desdobramento:** aprovado
