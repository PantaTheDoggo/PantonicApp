# RDO — P-0740 · LM-T2d

**Plano:** `docs/plans/P-0740-loop-de-modulos.md`
**Tarefa:** `LM-T2d` — A partição do bloco A por veredito: `A6a` e o domínio de `A8a`
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** um só — o bloco A passa a ser uma **partição**: todo par (`veredito`, `recomendacao`) tem exatamente uma regra, e nenhuma regra manda fazer o que o instrumento de fechamento recusa.

**Arquivos-alvo:** - `.claude/skills/scrum-master/SKILL.md`

**Verificação:** (`DM-24`: bloco cercado, `-SimpleMatch`, os **dois** valores rodados; as baselines abaixo foram medidas no `ESC-8` com estes mesmos comandos, extraídos deste card) 1. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern '| `A6a` |' -SimpleMatch | Measure-Object).Count" ``` → **1**. **Medido antes: 0**. 2. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'A6a' -SimpleMatch | Measure-Object).Count" ``` → **≥ 5** (a célula mais as quatro enumerações). **Medido antes: 0**. É esta linha que discrimina a entrega completa da que só acrescenta a linha da tabela. 3. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern '`recomendacao=escalar` (com `bloqueante=nenhuma`)' -SimpleMatch | Measure-Object).Count" ``` → **0** (a condição velha da `A8a` desapareceu). **Medido antes: 1**. 4. ``` pwsh -NoProfile -Command "(Select-String -Path .claude/skills/scrum-master/SKILL.md -Pattern 'nunca por `A8a`, `A8` ou `A9`' -SimpleMatch | Measure-Object).Count" ``` → **1** (a frase de partição). **Medido antes: 0**. 5. `python -m pytest tests/ -q` → verde, **sem número fixo de piso** (`DM-23`): o piso é o total que a árvore tiver **no despacho**, re-medido por quem despacha; esta tarefa não acrescenta teste e **não pode reduzir** esse total. Referência histórica, não aceite: `165 passed` em 2026-09-19.

**Pronto quando:** `A6a` está entre `A6` e `A7` com o texto literal acima; a condição de `A8a` fala de **veredito**; a frase de partição está no parágrafo do bloco A; as quatro enumerações citam `A6a`; e as cinco linhas de `Verificação` saem como escritas.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `in-progress` (despachada em 2026-09-19) — card novo do `ESC-8` (2026-09-19), residência única do `AE-20`. A `LM-T2c` está `done` aprovada 100% e **não se refaz**: o que ela entregou continua de pé, e esta tarefa fecha as duas lacunas que a regra nova deixou no bloco A.
- **Esforço:** low
- **Depende de:** `LM-T2c` (fechada — é a `A8a` dela que esta tarefa completa) e `DM-26`. **Precede a `LM-T4`**, pela mesma razão da `LM-T2c`: mesmo arquivo em `Arquivos-alvo` (exclusão mútua) e doutrina não se publica sobre tabela de roteamento incompleta.
- **Produto do módulo:** (a) a linha `A6a`, entre `A6` e `A7`; (b) a condição de `A8a` reescrita em torno do **veredito**, não do bloqueante; (c) a frase de partição no parágrafo do bloco A; (d) as quatro enumerações do mesmo arquivo postas em dia, como na `LM-T2c`.
- **As duas lacunas, medidas no `ESC-8` (2026-09-19):** 1. **Regra que manda fazer o que o instrumento recusa.** A tripla (`reprovado`, `bloqueante=nenhuma`, `escalar`) casa `A8a`, que manda fechar o RDO **pelo veredito**; mas `python .claude/tools/rdo.py close --veredito reprovado` sai **exit 2** com `argument --veredito: invalid choice: 'reprovado' (choose from 'aprovado', 'ressalva')` — o `close` fecha `aprovado` ou `ressalva`, e `reprovado` é desfecho de **outra** natureza. 2. **Combinação sem regra nenhuma.** `escalar` com `bloqueante` diferente de `nenhuma` e retentativas = 0 não casa nada: `A7` exige retentativas = 1, `A8a` exige `bloqueante=nenhuma`, `A6` exige `recomendacao=refazer`. As duas são **o mesmo buraco** visto de dois lados: *entrega reprovada cujo laudo recomenda escalar, antes de a retentativa ser gasta*. Baselines dos comandos publicados abaixo: `A6a` no arquivo → **0**; a condição velha de `A8a` → **1**; a frase de partição → **0**. 1. Inserir na tabela do bloco A, **entre** a linha `A6` e a linha `A7`, a linha nova: ``` | `A6a` | `veredito=reprovado` e `recomendacao=escalar` (qualquer `bloqueante`, qualquer contador de retentativas) | **não** fecha RDO e **não** gasta retentativa: materializa a tarefa como `blocked` razão `premissa`, com a pendência do laudo transcrita na razão, registra o achado como `AE-<n>` em `## Achados da execução` do plano e escala ao **consultor de plano**, que decide entre refazer com diretivas novas, emendar o card ou mudar a rota; a janela **segue** com o que ele devolver (Diretiva de execução do `P-0740`, item 2). Refazer antes de escalar gastaria a retentativa numa rota que o laudo já pediu para rever. Precedência: `A6` vence esta regra — lá o próprio laudo mandou refazer —, e esta vence `A7` e `A8a` | ``` 2. Na linha `A8a`, substituir a condição ``` `recomendacao=escalar` (com `bloqueante=nenhuma`) ``` por ``` `recomendacao=escalar` e `veredito` ∈ {`aprovado`, `ressalva`} ``` — nada mais da linha muda. A condição nova **subsume** a antiga (`bloqueante` diferente de `nenhuma` implica `veredito=reprovado`, o que o arquivo já afirma) e, ao mesmo tempo, impede que a regra mande fechar o que o `close` recusa. 3. Acrescentar ao parágrafo que fecha o bloco A, depois da frase da `A8a`, a frase nova: ``` O bloco A parte **primeiro por veredito, depois por recomendação**: `veredito=reprovado` é decidido por `A6`, `A6a` ou `A7` e **nunca por `A8a`, `A8` ou `A9`**, que só são alcançadas com veredito `aprovado` ou `ressalva`. É essa partição que impede entrega reprovada de ser fechada como aprovada por uma recomendação `seguir`, e é ela que garante que nenhuma regra mande fechar o que o instrumento recusa — medido: `rdo.py close --veredito reprovado` sai exit 2, `invalid choice`. ``` 4. No Passo 7, trocar a enumeração `` `A8a`, `A8`, `A9` e `B1`. `` por: ``` `A6a`, `A8a`, `A8`, `A9` e `B1`. ``` 5. No gatilho do Passo 8, trocar `` (`A6`..`A9`, inclusive `A8a`) `` por: ``` (`A6`..`A9`, inclusive `A6a` e `A8a`) ``` 6. No parágrafo do consumo do laudo, trocar `` `A6`, `A7`..`A9` (inclusive `A8a`) e `B1` `` por: ``` `A6`, `A6a`, `A7`..`A9` (inclusive `A8a`) e `B1` ``` 7. No relatório de encerramento, trocar `` (`A1`..`A9`, inclusive `A8a`, ou `B0`..`B4`, pelo identificador) `` por: ``` (`A1`..`A9`, inclusive `A6a` e `A8a`, ou `B0`..`B4`, pelo identificador) ```
- **Testes:** **nenhum `pytest`** — declaração, não omissão, pela mesma razão da `LM-T2` e da `LM-T2c` (`AE-14`): tabela de roteamento é prosa lida pelo `scrum-master`. E **nenhuma linha de código**: a lacuna 1 se fecha **restringindo a regra ao domínio que o instrumento já aceita**, não alargando o instrumento — `--veredito` continua com dois valores, porque `reprovado` não é fechamento de RDO, é `A7`.
- **Restrições desta tarefa:** `A1`..`A3b`, `A6`, `A7`, `A8` e `A9` ficam **literais** — só a `A8a` tem a **condição** reescrita, e nada da ação dela muda. O bloco B fica **intocado**. Nenhuma renumeração: `A6a` é sufixo, pelo mesmo motivo da `A8a` (`DM-25` (iii)). Nenhum instrumento é tocado — em particular, **não** se alarga `--veredito` do `rdo.py close`.
- **Não fazer:** não tocar `.claude/tools/` (a lacuna se fecha na prosa, `DM-26` (iii)); não tocar `GOVERNANCA.md` (é a `LM-T4`); não tocar `.claude/agents/` (`DM-17`); não escrever teste `pytest` para regra de prosa; não commitar.
- **Contingências:** 1. se qualquer um dos sete literais a substituir não existir no arquivo exatamente como transcrito → parar e sinalizar `blocked` razão `premissa`, citando a linha encontrada; 2. se `python -m pytest tests/ -q` ficar vermelho → seguir com a entrega e devolver `contingência 2 acionada: <arquivo::teste> vermelho fora dos alvos`.

## Execução

**Consumo:** 17 tool uses, 50.6 k tokens, 65.3 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: A7 manda fechar RDO como reprovado e o rdo.py close recusa: a particao do bloco A so fecha de fato quando a acao de A7 for decidida pelo planejamento (reescrever a regra ou alargar a via de materializacao); a LM-T2d entregou o que o card contratou e nao podia tocar A7.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa

Tarefa de redacao por transcricao literal: os sete literais conferiram byte a byte e as cinco verificacoes bateram (1, 6, 0, 1, 171 passed), mas a contagem de Select-String nao discrimina coerencia do modulo. O residuo em A7 so apareceu no exercicio ponta a ponta da tabela contra o instrumento de fechamento - confronto que vale repetir em toda tarefa que altera tabela de roteamento.

## Fechamento

**Desdobramento:** aprovado
