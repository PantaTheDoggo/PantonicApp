# RDO — P-0745 · PLN-T4a

**Plano:** `docs/plans/P-0745-planejador-modelo-operacao.md`
**Tarefa:** `PLN-T4a` — O ponteiro sobrevivente da tabela aposentada, nos Fatos estáveis do planejador
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** `.claude/agents/pantonic-planner.md:36-37` deixa de remeter à *tabela de classes* de `GOVERNANCA.md` §3, aposentada pela `PLN-T2` (`DPN-3`), e passa a dizer o que a régua é hoje; a primeira metade da frase — `Nenhum teto se escreve no card` — sobrevive intacta, porque continua verdadeira. Uma guarda executável tranca o retorno da remissão.

**Arquivos-alvo:** - `.claude/agents/pantonic-planner.md:36-37` (`## Fatos estáveis`, fim do bullet do cabeçalho de tarefa) - `tests/test_doutrina_unidade.py` (acréscimo de uma função de teste; as duas existentes não se tocam)

**Verificação:** 1. ``` grep -c 'tabela de classes' .claude/agents/pantonic-planner.md ``` → **0**. **Medido antes: 1** (2026-09-22). 2. ``` grep -c 'Nenhum teto se escreve no' .claude/agents/pantonic-planner.md ``` → **1** — a metade verdadeira sobreviveu. **Medido antes: 1** (2026-09-22). 3. ``` grep -c 'Classe do card — natureza, não teto' .claude/agents/pantonic-planner.md ``` → **1**. **Medido antes: 0** (2026-09-22). O alvo da remissão existe: o mesmo `grep -c` sobre `GOVERNANCA.md` devolve **1**, medido na mesma data. 4. ``` python -m pytest tests -q ``` → termina em `<N> passed`, com `<N>` igual ao total re-medido no despacho **mais 1**. **Medido antes: `271 passed`** (2026-09-22). 5. ``` pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift ``` → exit **0**, primeira linha `kit_check: check-drift OK - .claude/README.md == regenerado (10 agente(s), 11 skill(s)); materializacao do alvo 'projeto' == canonico.` **Medido antes: o mesmo** (2026-09-22). 6. ``` python .claude/tools/backlog.py check ``` → `check: OK — nenhuma violação.`, exit **0**. **Medido antes: o mesmo**.

**Pronto quando:** as seis verificações imprimem os valores declarados e nenhum arquivo fora dos `Arquivos-alvo` foi editado. Por propriedade que a operação altera (`DPN-6`): - `agente de planejamento.régua com que ele dimensiona um card` — a parcela desta tarefa: a última residência da conduta que remetia à tabela aposentada deixa de remeter, e passa a apontar para a régua vigente; é o estado final que a versão 4 pendente do modelo exige e que o dono valida no Marco 2 — Verificação 1, 2 e 3. - As demais entregas desta tarefa são **requisito secundário** (`## Requisitos secundários`), não propriedade do modelo: a asserção nova de `tests/test_doutrina_unidade.py`, aferida pela Verificação 4.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-22
- **Depende de:** `PLN-T4`
- **Fundamento:** `DPN-3`; achado `AE-13`. **Card corretivo somado à `OP-3`**, na forma que a própria `PLN-T2` instituiu em `GOVERNANCA.md` §3 (*A unidade de trabalho é o módulo coeso*: card corretivo de replanejamento **somado à operação que repara**, nunca operação partida em dois). Resíduo de `OP-3` e não de `OP-1`: quem aposentou a tabela foi a `OP-1`, em `GOVERNANCA.md`, mas o ponteiro sobrevivente está em `.claude/agents/pantonic-planner.md` — residência da `OP-3`, a única operação que declara alterar a **régua** e agir naquele arquivo.
- **Operação do modelo:** `OP-3` - OP-3: O autor de papéis fecha o vão do protocolo de quem planeja: a sessão ganha uma terceira forma de terminar sem plano fechado, com o esqueleto gravado e o pedido de autoria do modelo devolvido na linha de retorno; a decomposição só começa depois de o modelo existir, um card por operação, e o recorte deixa de se medir por percentual. - precisa de: agente de planejamento — residências da conduta: `.claude/agents/pantonic-planner.md` (descrição, tese do papel, abertura do protocolo, Fases 3a e 3b, Fase 4, Fase 5, anatomia do card e rodada de replanejamento) e a região gerada `kit:agents` de `.claude/README.md` — produzida por `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` e nunca editada à mão. Residências da régua e da unidade: `GOVERNANCA.md` §3 (matriz de responsabilidades, *A unidade de trabalho é o módulo coeso*, *Diretriz de dimensionamento de tarefa*, tabela da §4, §4.1, §4.3, G-PLANREADY e G-MODULO), `.claude/global/CLAUDE.md` (Regras 2 e 7) e a cópia do dono (`DPN-12`), `docs/RESIDENCIA_DOUTRINA.md`, as skills `diario-de-obras` (*Formato de uma tarefa*), `modelo-por-fase` e `bootstrap-pantonic`, `.claude/agents/pantonic-fora-da-caixa.md` e `README.md`. Residência da responsabilidade pelo lastro: `GOVERNANCA.md` §3.2 e `.claude/agents/pantonic-model-designer.md`, nas duas pontas no mesmo card. Residência da descrição: `docs/planner-spec.md` (novo), uma seção por dimensão da §4, na ordem dela e aberta por `## 0. O que esta especificação não é`. O censo linha a linha, com destino, é a §7; a classe do cabeçalho do card permanece como natureza do trabalho, porque os parsers a leem; ocorrência de outro sentido — escrita atômica em disco, passo atômico de migração — fica intacta; as entradas `RP-1`..`RP-7` e os itens de verificação que não citam ocupação permanecem, são a memória medida do papel; o escopo do papel continua na matriz de `GOVERNANCA.md` §3 (G-SCOPE), e a especificação não é residência nem do escopo nem do protocolo de conduta; agente model designer — não se transforma neste plano: a seção `## 1. Modelo conceitual` escrita por ele e o vocabulário de violações `V1`..`V21` de `.claude/tools/modelo.py` são o insumo que quem planeja consome, e permanecem como estão. `.claude/tools/modelo.py`, `tests/test_modelo.py` e as fixtures **não se tocam**. O que os cards deste plano publicam em `GOVERNANCA.md` §3.2 e em `.claude/agents/pantonic-model-designer.md` é a responsabilidade de **quem planeja** pelo lastro das operações, e nada além disso: o portão com que o modelador aceita ou recusa escrever a seção sobre um plano ainda sem cards não é objeto deste plano — alterá-lo é colateral e se escala - **Contrato copiado da versão 3, vigente em 2026-09-22.** A versão 4 está **pendente** do veredito do dono no Marco 2 (`## 1A`), e a medição parte sempre do modelo **vigente** (`GOVERNANCA.md` §3.2). Este card executa antes do Marco 2, logo não há o que recopiar.
- **Camada e fronteira:** um agente do kit, uma frase, mais uma asserção na guarda executável que a `PLN-T2` criou. Nenhuma linha de `GOVERNANCA.md`, nenhuma skill, nenhum instrumento de `.claude/tools/`. A região gerada `kit:agents` de `.claude/README.md` **não** se regenera: o texto tocado está em `## Fatos estáveis`, não na `description` do frontmatter — a Verificação 5 afere que o drift continua ausente.
- **Domínio:** *tabela de classes* — a tabela de tetos de turnos por classe que vivia em `GOVERNANCA.md` §3 e foi aposentada em 2026-09-21 (`DPN-3`), substituída pelo bullet *Classe do card — natureza, não teto* (`GOVERNANCA.md:189`). *Fatos estáveis* — a região de `.claude/agents/pantonic-planner.md` que a versão 4 pendente do modelo acrescenta à enumeração fechada das residências da conduta.
- **Passos:** 1. Em `.claude/agents/pantonic-planner.md:37`, substituir o literal `card: a régua numérica é a tabela de classes de `GOVERNANCA.md` §3, interna a este papel.` pelo literal `card, e nenhum número o dimensiona: a classe é natureza do trabalho (`GOVERNANCA.md` §3, *Classe do card — natureza, não teto*) e a régua é a operação do modelo que o card materializa (`GOVERNANCA.md` §3.2).` O fim da linha 36 — `Nenhum teto se escreve no` — **não se toca**: é a metade verdadeira da frase, e a Verificação 2 afere que ela sobreviveu. Quebra de linha se reajusta a ~100 colunas; palavra não muda. 2. Acrescentar a `tests/test_doutrina_unidade.py`, **depois** das duas funções existentes e sem alterar nenhuma delas, a função literal: ```python def test_conduta_do_planejador_nao_remete_a_tabela_aposentada(): t = _texto(".claude/agents/pantonic-planner.md") assert "tabela de classes" not in t assert "tabela de tetos" not in t assert "Nenhum teto se escreve no" in t ``` 3. Rodar as verificações abaixo.
- **Restrições desta tarefa:** - Só a segunda metade da frase muda. Nenhuma outra linha de `.claude/agents/pantonic-planner.md` se toca — em especial as entradas `RP-1`..`RP-7` e os itens da Fase 4, que são a memória medida do papel (`I-9`). - As duas funções já existentes de `tests/test_doutrina_unidade.py` não se alteram: são entrega aceita da `PLN-T2`. - Não regenerar região alguma de `.claude/README.md`. - Não commitar (`I-1`).
- **Não fazer:** - Não "aproveitar" para revisar outras remissões do agente: a varredura da família `tabela de classes|tabela de tetos|teto por classe` foi feita em 2026-09-22 e este é o **único** sítio vivo (`AE-14`). `CHANGELOG.md:196,215` e `.claude/global/docs/RECOMENDACOES_CONSUMO_GLOBAL.md:71` são registro datado e **ficam** (`I-7`). - Não tocar `GOVERNANCA.md`: o sítio dele já é da `PLN-T7`, passo 4a.
- **Contingências:** 1. Se o literal do passo 1 não casar byte a byte → localizar por `grep -n 'tabela de classes' .claude/agents/pantonic-planner.md` e aplicar sobre a linha devolvida; se o literal não existir no arquivo → parar e sinalizar `blocked` razão `premissa`. 2. Se `python -m pytest tests -q` reprovar em teste que este card não criou → parar e sinalizar `blocked` razão `premissa`, colando a linha de falha.
- **Testes:** `TR-DU-3` (`test_conduta_do_planejador_nao_remete_a_tabela_aposentada`), em `tests/test_doutrina_unidade.py`; suíte: `python -m pytest tests -q`.
- **Fora do escopo desta tarefa:** o sítio de `GOVERNANCA.md` (`PLN-T7`, passo 4a); a recópia dos contratos da versão 4 nos cards abertos, que é condicionada ao veredito do dono no Marco 2 e mora na `PLN-T6` e na `PLN-T7`.

## Execução

**Consumo:** 16 tool uses, 55.4 k tokens, 117.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** executor: card afirmava duas funções já existentes em tests/test_doutrina_unidade.py quando havia quatro; o executor nomeou o erro na linha de retorno, não alterou nenhuma das quatro e a entrega não foi afetada
laudo: Sexta ocorrência medida da mesma raiz de autoria (número sobre a árvore envelhecido entre autoria e despacho): a §8 da rubrica cobre a linha de aceite e não a afirmação do card sobre a árvore - emenda à régua de autoria, ao planejamento.

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar: a régua de autoria da rubrica §8 prende o número re-derivável à linha de aceite, e as seis ocorrências desta janela moraram fora do bloco Verificação. Emenda à régua é matéria de kit, fora do escopo do P-0745; vai ao consultor por B1 para decidir a rota

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
