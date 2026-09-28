# RDO — P-0747 · CON-T7

**Plano:** `docs/plans/P-0747-consultor-de-plano.md`
**Tarefa:** `CON-T7` — A medida do piloto da forma efêmera
**Modelo:** Sonnet · **Classe:** investigacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O medidor confronta o piloto da forma efêmera com a forma anterior: apura o custo de cada acionamento da janela pelo método já medido, conta as reprovações por perda de cenário e grava, na seção de custo da especificação, o veredito de adotar, recusar ou declarar a amostra insuficiente.

**Arquivos-alvo:** - `docs/consultant-spec.md`

**Verificação:** no PowerShell, na raiz do repositório. **Antes** e **depois** foram medidos em 2026-09-22 numa cópia da árvore com os cards anteriores aplicados em ensaio; o executor mede o **antes** antes da primeira edição. 1. antes `0` · depois `1` ~~~~ (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern '### Veredito do piloto da forma efêmera').Count ~~~~ 2. antes `0` · depois `1` ~~~~ (Select-String -Path 'docs/consultant-spec.md' -SimpleMatch -CaseSensitive -Pattern '| acionamentos | $/acionamento, média |').Count ~~~~ 3. A linha de agregado devolvida traz `acionamentos=`, `retentativas=` e o veredito, e a linha de tabela da subseção tem os mesmos números.

**Pronto quando:** - `consultor.forma da figura` — efêmera com cenário persistido, instalada pela seção `## Acionamento do consultor` da skill do loop: o cenário do plano, com teto de 15k tokens, é o handover, e o reprovisionamento por limite deixa de existir; o corpo do agente e a regra do loop deixam de descrevê-lo instanciado uma vez (`F-4` itens 44 e 45); ao fim do plano a forma leva o veredito medido do piloto, gravado na §11 da spec (item 46) — adotada; ou recusada, com achado em `## 9` e rota para plano novo de standby com aquecimento; ou em amostra insuficiente, com linha nova na §11 da spec e o piloto seguindo na próxima execução — Verificação 1, 2, 3

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-23
- **Depende de:** `CON-T6a`
- **Fundamento:** `DCS-7`, `DCS-22`; fatos `F-7`, `F-4` item 46; spec §11 (i) e (ii).
- **Operação do modelo:** `OP-7` - OP-7: O medidor confronta o piloto da forma efêmera com a forma anterior: apura o custo de cada acionamento da janela pelo método já medido, conta as reprovações por perda de cenário e grava, na seção de custo da especificação, o veredito de adotar, recusar ou declarar a amostra insuficiente. - precisa de: consultor — residências: **a lista `F-4` da `## 2`, itens 1 a 47, residência única — o card a copia pelo número do item e nunca a reenuncia**. Partição, **cada item em exatamente uma operação**: `OP-1` itens 13 a 23; `OP-2` item 24; `OP-3` itens 1, 2 e 4 a 12; `OP-4` itens 3, 44 e 45; `OP-5` itens 25 a 38; `OP-6` itens 42 e 43; `OP-7` item 46; `OP-8` itens 39, 40, 41 e 47 (`DCS-20`). O corpo do agente se divide por item: a `OP-2` escreve o item 24 e não toca a `description` nem as linhas de forma; a `OP-4` escreve as linhas de forma (item 44); a `description` (item 47) só muda na `OP-8`. Residências novas, fora de `F-4`: o arquivo de estatística de `DCS-8`, criado pela `OP-2`; o arquivo de cenário de `DCS-6` e a seção nova `## Acionamento do consultor` da skill do loop, logo antes de `## Relatório de encerramento` e não como passo (`DCS-19`), ambos da `OP-4`; as entradas dos dois arquivos no índice de documentos são da `OP-6` (item 43). Fonte normativa das regras reescritas, nos dois cabeçalhos de fonte da skill do loop (itens 1 e 5): `P-0747` `DCS-3`..`DCS-6` ao lado do `P-0734`, com a cláusula de divergência valendo também para as seções do `P-0747` (`DCS-11`). A região gerada do item 41 só muda por instrumento (`I-4`) e se regenera uma vez, na `OP-8`, no mesmo ato que troca a `description` do item 47 pela forma que o veredito do piloto deixou: o check-drift da região é gate da checagem de guardrails (`F-16`), e trocar a `description` antes deixaria o gate de toda tarefa intermediária vermelho. Rota devolvida ∈ {`resolve`, `modelador`, `planejador`} (`DCS-3`). **Fora**: plano não-pronto no gate de delegação e contexto acabando dentro da tarefa não são parada de executor e continuam indo ao planejamento; as linhas que `F-4` declara fora por `DCS-18` não se tocam. Residência que roteie parada de executor ou cite o consultor e não esteja em `F-4` é achado para o modelador, não licença de autoria. Intocados: `GOVERNANCA.md` §4.5 e a vigência do modelo (`DCS-12`); o critério de não-acionamento na entrada (`DCS-10`); a cópia do dono e os derivados (`DCS-13`); as três contagens defasadas da spec (`DCS-2`); a frase *"O kit são dez agentes"* (`DCS-15`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`); acionamento do consultor — nenhuma operação altera um acionamento. O que se observa nele é o custo, apurado pelo método de `F-7`; a sonda é descartável e não vira artefato. Retrato do antes: as instâncias 1-4 da forma standby (`F-7`) e a série de `F-8`; o depois: os acionamentos da janela de execução deste plano a partir do aceite da `OP-4`
- **Camada e fronteira:** medição — leitura de transcripts fora do repositório e de `docs/telemetria.tsv`; escrita só no fim da §11 de `docs/consultant-spec.md`.
- **Domínio:** **acionamento** — uma instância efêmera do `pantonic-consultant` despachada com o caminho `docs/plans/_CENARIO-P-0747.md` na mensagem de entrada; **reprovação** — revisão repetida de uma mesma tarefa (`DCS-22`).
- **Contratos/classes:** nenhuma assinatura de código; a sonda é descartável e fica em `%TEMP%\claude\`.
- **Método de sondagem:** 1. Grave o bloco **Sonda** abaixo em `%TEMP%\claude\sonda_p0747.py` e rode `python $env:TEMP\claude\sonda_p0747.py`. A sonda lê só os transcripts `~/.claude/projects/d--workspaces-PantonicApp/*/subagents/agent-*.jsonl` cujo `agent-*.meta.json` tem `agentType` igual a `pantonic-consultant` e cuja primeira linha cita `_CENARIO-P-0747.md`; cada arquivo é um acionamento. Saída: `acionamentos=<n>` e, com `n` > 0, `media=$<x> min=$<a> max=$<b>`. Medido em 2026-09-22 antes da janela: `acionamentos=0`. 2. Grave o bloco **Contagem** abaixo em `%TEMP%\claude\retentativas_p0747.py` e rode `python $env:TEMP\claude\retentativas_p0747.py` na raiz do repositório. Saída: `retentativas=<r> reprovacoes=<p> tarefas=<t>`. Medido em 2026-09-22 antes da janela: `retentativas=0 reprovacoes=0 tarefas=0`. 3. Tome o veredito da `Contingências` deste card que casa os valores medidos: as quatro linhas cobrem todos os valores possíveis. 4. Apense ao fim de `docs/consultant-spec.md`, depois da última linha, uma linha em branco e o bloco **Subseção** abaixo, trocando `<acionamentos>`, `<media>`, `<min>`, `<max>`, `<reprovacoes>`, `<retentativas>` e `<veredito>` pelos valores medidos (custo com uma casa decimal e vírgula, como `$1,3`; com menos de 1 acionamento, `<media>` vira `—` e `<min>–<max>` vira `—`) e `<frase>` pela frase do veredito no bloco **Frases**. - **Agregado que volta** (≤ 4 linhas, na linha de retorno): as duas linhas de saída das sondas, o veredito e, quando acionada, a linha `contingência recusa acionada: veredito recusada`. Nenhum dado bruto de transcript entra no contexto nem no retorno.
- **Restrições desta tarefa:** - Toda edição é substituição literal: o **Texto novo** entra exatamente como está no bloco, sem reformular, sem quebrar linha e sem corrigir pontuação. - Não commitar (`DCS-16`). Não tocar `GOVERNANCA.md` §4.5 nem a vigência do modelo (`DCS-12`). - Nenhum agente aciona outro: todo despacho descrito no texto é ato do loop (`I-2`). O consultor nunca escreve a `## 1` de plano nenhum (`I-3`). - Piso de regressão é relação: o total de `passed` de `python -m pytest -q` medido no despacho não diminui (`I-6`).
- **Não fazer:** - Não versionar a sonda nem nenhum arquivo em `.claude/tools/`. - Não editar a §11 fora do fim do arquivo, nem as §§1-10.
- **Contingências:** - se a sonda imprimir `acionamentos=0`, `acionamentos=1` ou `acionamentos=2` → seguir com o veredito `amostra insuficiente` e a coluna de custo com `—` - se `acionamentos` for 3 ou mais, a média ficar abaixo de `$3.7` e `reprovacoes=0` → seguir com o veredito `adotada` - se `acionamentos` for 3 ou mais e a média for `$3.7` ou mais, ou `reprovacoes` for maior que 0 → seguir com o veredito `recusada`, e devolver na linha de retorno `contingência recusa acionada: veredito recusada` para a orquestração registrar o `AE-<n>` com rota "plano novo: standby + ping, spec §11 (ii)" - se o diretório `~/.claude/projects/d--workspaces-PantonicApp` não existir → parar e sinalizar `blocked` razão `premissa`
- **Testes:** nenhum — tarefa de medição; as sondas são descartáveis e não se versionam.
- **Fora do escopo desta tarefa:** a descrição pública da forma (`CON-T8`). if json.load(open(meta, encoding="utf-8")).get("agentType") != "pantonic-consultant": continue jl = meta[: -len(".meta.json")] + ".jsonl" linhas = open(jl, encoding="utf-8").read().splitlines() if not linhas or FILTRO not in linhas[0]: continue uso = {} for l in linhas: e = json.loads(l) m = e.get("message") or {} if e.get("type") == "assistant" and m.get("id") and m.get("usage"): uso[m["id"]] = m["usage"] s = lambda k: sum(u.get(k, 0) or 0 for u in uso.values()) custo = (s("input_tokens") * 5 + s("output_tokens") * 25 + s("cache_read_input_tokens") * 0.5 + s("cache_creation_input_tokens") * 6.25) / 1e6 custos.append(custo) print(f"media=${sum(custos)/n:.1f} min=${min(custos):.1f} max=${max(custos):.1f}") t = r["tarefa"] if re.fullmatch(r"CON-T[56][a-z]?", t): exe[t] += 1 m = re.fullmatch(r"(CON-T[56][a-z]?)-revisao", t) if m: rev[m.group(1)] += 1

## Execução

**Consumo:** 15 tool uses, 72.5 k tokens, 107.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: O veredito adotada repousa em 3 instancias do consultor em claude-fable-5-1, precificadas a Opus e comparadas ao piso standby de 3,7 dolares medido em Opus; a subsecao nao declara o modelo: decidir, antes da CON-T8, se vale como medida da forma ou se vira amostra de outro modelo

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
