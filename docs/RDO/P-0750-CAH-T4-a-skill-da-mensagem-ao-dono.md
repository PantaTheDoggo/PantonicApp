# RDO — P-0750 · CAH-T4

**Plano:** `docs/plans/P-0750-comunicacao-agente-humano.md`
**Tarefa:** `CAH-T4` — A skill da mensagem ao dono
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** O autor de skill cria a skill da mensagem ao dono: a checagem antes de enviar, onde achar o título de cada sigla, o formato do pedido de decisão e o registro da falha; e a inscreve na anatomia do kit.

**Arquivos-alvo:** - `.claude/skills/mensagem-ao-dono/SKILL.md` (novo) - `README.md` (tabela *Skills* e frase de contagem da seção *Anatomia do kit* — `K1`, `K2`) - `.claude/README.md` (regenerado, não editado à mão)

**Verificação:** 1. ``` pwsh -NoProfile -Command '"skills=" + @(Get-ChildItem .claude/skills -Directory).Count + " linha=" + @(Select-String -LiteralPath README.md -SimpleMatch -Pattern "| ``mensagem-ao-dono`` |").Count' ``` → **skills=12 linha=1**. **Medido antes: skills=11 linha=0**. 2. ``` pwsh -NoProfile -File .claude/checks/check-readme.ps1 ``` → **exit 0**. **Medido pelo consultor** numa cópia (`-Root`, apagada) com `K1` e `K2` aplicados: exit 0, `12 skill(s)`; sem `K2`, exit 1 (`declara 11 vs 12`). 3. ``` pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift ``` → **exit 0**. 4. ``` python -m pytest tests -q ``` → **nenhuma falha**, total igual ao da véspera.

**Pronto quando:** - kit.procedimento da mensagem — skill com checagem, busca do título, pedido de decisão e registro de falha — Verificação 1, 2, 3

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Fundamento:** DCH-1, DCH-2, DCH-4, DCH-9, DCH-10; F-2, F-6; I-2, I-3.
- **Depende de:** `CAH-T1`, `CAH-T2`, `CAH-T3`
- **Operação do modelo:** `OP-4` - OP-4: O autor de skill cria a skill da mensagem ao dono: a checagem antes de enviar, onde achar o título de cada sigla, o formato do pedido de decisão e o registro da falha; e a inscreve na anatomia do kit. - precisa de: kit — Quem implementa recebe esses textos. O que esta entrega não toca continua valendo como hoje.
- **Camada e fronteira:** skill do kit (`.claude/skills/`), propagada a derivados pelo `sync-kit.ps1` fora deste plano; a regra não se copia, só se aponta (I-2).
- **Conteúdo literal de `.claude/skills/mensagem-ao-dono/SKILL.md`:** ````text --- name: mensagem-ao-dono description: Checagem de toda mensagem escrita para o dono humano — conversa, handover, relatório de janela, rodada de decisões. Troca a sigla sozinha pelo título entre aspas, traz para o corpo o que o dono precisa para decidir e registra a falha quando o dono teve de perguntar. Usar antes de enviar ao dono mensagem que cite sigla do kit ou aponte arquivo, e ao receber dele pergunta de esclarecimento. --- # mensagem-ao-dono — a mensagem se entende sozinha A regra mora em `GOVERNANCA.md` §4.2 (*Mensagem legível ao dono*); esta skill é o procedimento. ## Gatilho 1. Antes de enviar ao dono mensagem que cite sigla do kit (tarefa, tíquete, plano, decisão, achado, regra de roteamento, guardrail) ou aponte arquivo. 2. Ao receber do dono pergunta do tipo "o que é", "o que significa" ou "onde está" sobre algo que um agente escreveu — é falha medida (§4). Fora do alcance: a superfície agente↔agente (dossiê, retorno do executor, laudo, `passagem-de-bastao`), onde a sigla crua é o contrato; documento publicado (`redacao-doc`); documento de encerramento de plano (`entrega-de-encerramento`), que já define todo termo no texto. ## 1. Checagem antes de enviar - [ ] Toda sigla foi trocada pelo título entre aspas duplas (§2). A sigla só acompanha, entre parênteses, quando o dono precisa digitá-la para agir. - [ ] O dono decide ou valida sem abrir arquivo: o fato que sustenta cada pedido está no corpo, e o caminho é complemento. - [ ] Termo interno (laudo, evidência, janela, marco) tem glosa curta na primeira ocorrência. - [ ] Pedido de decisão no formato do §3. - [ ] Escrita no idioma em que o dono conversa. Exemplo — antes: `Próximo: TK-38.` · depois: `Próximo: o tíquete "Comunicação entre agente e humano — skill própria e requisitos mínimos" (TK-38).` (a sigla fica porque o dono a digita para mandar executar). ## 2. Onde achar o título | sigla | onde está o título | como buscar | |---|---|---| | tarefa `<PFX>-T<n>`, tíquete `TK-<n>`, plano `P-NNNN` | o cabeçalho do item | `python .claude/tools/backlog.py show <ID>` — o título é o texto depois de ` — ` na primeira linha | | decisão, fato, invariante, achado (`D…-<n>`, `F-<n>`, `I-<n>`, `AE-<n>`) | a linha que a define no plano de origem | busca de texto por `**<ID>**` ou `\| <ID> \|` no plano; o título é a primeira oração | | regra de roteamento `A<n>` ou `B<n>` | a coluna *condição* das tabelas dos blocos A e B da skill `scrum-master` | a condição, em palavras | | guardrail `G-<NOME>` | a lista de `GOVERNANCA.md` §7 | o nome da regra | | família de sigla | o glossário do `README.md`, bullet *Identificadores de trabalho* | — | Sem título achado, a sigla vai com uma frase que diga o que ela nomeia — nunca sozinha. ## 3. Pedido de decisão Uma mensagem, todas as questões juntas. Cada questão traz: o fato medido que a originou, as opções com o que cada uma implica, o que fica bloqueado sem resposta, a recomendação com o motivo e, quando existir, a opção "registrar e não agir". É o mesmo formato do relatório de encerramento da skill `scrum-master` e da rodada de decisões do `pantonic-planner`; esta seção não o redefine. ## 4. Registro de falha O dono perguntou o que algo significa, onde algo está, ou teve de abrir arquivo para decidir: quem recebeu a pergunta apensa **uma** linha a `docs/FALHAS_COMUNICACAO.tsv` antes de responder, sem reescrever linha anterior. Colunas separadas por TAB: | coluna | conteúdo | |---|---| | `data` | `AAAA-MM-DD` | | `superficie` | conversa, handover, relatório de janela, rodada de decisões, painel ou documento | | `o_que_faltou` | a sigla ou o termo sem glosa, ou o dado que só estava fora da mensagem | | `custo_prompts` | prompts do dono gastos no esclarecimento | | `correcao` | o que muda na regra ou nesta skill para não repetir, ou `-` | | `fonte` | caminho do registro do caso, ou `-` | A tabela se lê em conjunto na revisão da doutrina (`GOVERNANCA.md` §7.1); uma linha isolada não muda esta skill. ````
- **Passos:** 1. Rodar a Verificação 1 e conferir os valores "antes". 2. Criar `.claude/skills/mensagem-ao-dono/SKILL.md` com `Write`, conteúdo literal acima. 3. Aplicar `K1` e `K2` com `Edit`. 4. Rodar `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode generate` para regenerar `.claude/README.md`. 5. Rodar a Verificação 1 a 4.
- **Restrições desta tarefa:** I-2 — a skill aponta para a regra, não a reescreve; I-3 — nada na skill impõe requisito à superfície agente↔agente.
- **Não fazer:** não editar `.claude/README.md` à mão; não tocar `passagem-de-bastao`, `scrum-master` nem `pantonic-planner` (`CAH-T5`); não criar script; não rodar `sync-kit.ps1`.
- **Contingências:** 1. se o texto antigo de `K1` não aparecer exatamente uma vez → parar e sinalizar `blocked` razão `dependencia`. 2. se `kit_check.ps1 -Mode generate` falhar → parar e sinalizar `blocked` razão `ferramenta`, devolvendo o stderr. 3. **Redespacho de 2026-09-25 (AE-6):** a execução anterior deixou na árvore os passos 2, 3 (só `K1`) e 4 — medido pelo consultor: Verificação 1 dá `skills=12 linha=1`, Verificação 3 exit 0, Verificação 2 exit 1 só pela frase de contagem. Então: se `.claude/skills/mensagem-ao-dono/SKILL.md` já existe, conferir que é idêntico ao literal acima e, se diferir, sobrescrever com `Write`; se a linha `` | `mensagem-ao-dono` | `` já aparece uma vez no `README.md`, não reaplicar `K1` (a contingência 1 não vale para ela); aplicar `K2`, rodar o passo 4 e as Verificações 1 a 4. O "Medido antes" da Verificação 1 é, neste redespacho, `skills=12 linha=1`.
- **Testes:** nenhum novo (redação); a suíte inteira roda como TR — se algum teste contar skills e falhar pelo número 11 → 12, é `blocked` razão `premissa`, não edição de teste.
- **Fora do escopo desta tarefa:** propagação aos projetos derivados (`TK-81`); resolvedor sigla→título por função (DCH-10).
- **Notas de execução:** - 2026-09-25 `ready` — consultor: K2 (onze->doze skills) e contingencia 3 do redespacho, AE-6

## Execução

**Consumo:** 27 tool uses, 115.8 k tokens, 155.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
