# Governança de memórias e artefatos .claude (agnóstica a projeto)

Referenciado pela **Regra 6** do `~/.claude/CLAUDE.md`. Vale para todos os projetos.
Última revisão: 2026-07-07 (criado junto com a auditoria de memórias dos workspaces).

## 1. Princípio: cada informação tem um lar canônico único

Antes de gravar qualquer coisa, percorra a cadeia (o primeiro "sim" decide o lar):

1. **É derivável do repositório** (código, docs, git, diário de obras)? → **não grave em lugar nenhum**.
2. **É estado de trabalho** (sprint, pendência, próximo passo, contagem de testes)? → tracker
   canônico do projeto (diário de obras / PLANNING_ACTIVE / ESCALATIONS), nunca memória.
3. **Muda o comportamento do agente em toda sessão?** → CLAUDE.md (global se agnóstico,
   do projeto se citar caminhos/artefatos do projeto).
4. **É procedimento reexecutável sob demanda, com gatilho claro?** → skill.
5. **É papel delegável com ferramentas próprias?** → agente.
6. **É fato durável, não derivável, que custou caro descobrir?** → memória.

Gravar a mesma informação em dois lares é defeito (risco de drift); o segundo lar recebe no
máximo um ponteiro.

## 2. Memórias de projeto (`~/.claude/projects/<slug>/memory/`)

**Pode:**
- `user` — identidade/preferências duráveis do usuário observadas no contexto do projeto.
- `feedback` — correção/orientação do usuário com **Why** e **How to apply**, *ainda não
  promovida* a regra de CLAUDE.md.
- `project` — fato durável não derivável do repo: decisão verbal do usuário, constraint
  externa, invariante de design com racional, pegadinha custosa de redescobrir (perda de
  dados, limite hardcoded, "source of truth" não óbvio).
- `reference` — ponteiro para recurso externo (URL, dashboard, tíquete).

**Não pode:**
- **Changelog/status**: "sprint X completa, N testes verdes, versão Y" é história do repo.
- **Pendências/próximos passos**: memória vira stale no dia seguinte; no máximo um arquivo
  ponteiro para o tracker canônico (padrão `project-pending.md` → "tracked in docs/…").
- **Conteúdo derivável**: estrutura de pastas, lista de arquivos, assinaturas de API.
- **Tombstone de promoção**: quando um feedback vira regra de CLAUDE.md, a memória é
  **apagada** na mesma ação — não fica com nota "elevado a regra global em …".
- **Fato de escopo global em memória de projeto**: se vale para todos os projetos, promova a
  `~/.claude/CLAUDE.md` (não existe "memória global"; o CLAUDE.md global é esse lar).
- **Lista volátil duplicada** (ex.: roster de projetos sincronizados): uma única memória dona;
  as demais dizem "lista canônica em <memória dona de tal projeto>" sem repetir a lista.

**Formato:** 1 fato por arquivo; corpo ≤ ~30 linhas; `description` ≤ 120 chars (é o critério
de recall — escreva-a como gancho de decisão, não como título); frontmatter canônico com
`metadata: type:`. Todo arquivo indexado em `MEMORY.md`; todo item do índice aponta para
arquivo existente.

**Memória com valor medido** (ex.: linha `Consumo:`, contagem de tokens/duração): declara o
escopo da calibração ("medido no artefato X; pode variar por instância") e o método de
recalibração. Diagnóstico cuja conclusão depende desse valor recalibra no artefato-alvo antes
de reportar negativo — "nenhum achado" derivado de um registro estático é hipótese, não
conclusão (achado 15, `TK-KITCONSUMO-R2`).

**Higiene (na skill `memory-diet` e em auditorias):**
- Índice > ~40 linhas → rodar `memory-diet`.
- **Arquivo não indexado é limbo proibido**: memórias fora do índice continuam elegíveis a
  recall e poluem o contexto sem supervisão — indexar ou apagar.
- Ponteiro quebrado no índice (arquivo citado não existe) → remover na hora.
- Fato que virou obsoleto → apagar o arquivo (não "corrigir por cima" o que perdeu relevância).

## 3. `.claude` global (`~/.claude/`)

- `CLAUDE.md` global: só regras agnósticas de comportamento, ≤ 200 linhas. Conhecimento de
  domínio ou procedimento longo → doc em `~/.claude/docs/` referenciado pela regra, ou skill.
- Skills/agentes globais: só o que é reutilizável em ≥ 2 projetos. Se o texto cita caminhos,
  artefatos ou domínios de um projeto específico, pertence ao `.claude/` daquele projeto.
- O inverso também vale: preferência global descoberta dentro de um projeto (ex.: "sempre
  planeje com modelo caro e execute com barato") não fica na memória do projeto — sobe.

## 4. Skills — o que pode e o que não pode

**Pode:** procedimento reexecutável com gatilho explícito ("quando X, faça estes passos");
checklists de verificação; conhecimento volumoso carregado sob demanda (progressive
disclosure); convenções de formato de artefatos que o agente produz.

**Não pode:**
- Estado ou progresso de trabalho (→ tracker do projeto; se um pipeline precisa de ponteiro
  de progresso, ele vive no artefato produzido, não na skill).
- Preferências do usuário (→ memória `user`/`feedback` ou CLAUDE.md).
- Regra que precisa valer sempre, sem gatilho (→ CLAUDE.md; skill só é lida quando invocada).
- Fatos com data de validade curta (versões, contagens, URLs de sprint).

## 5. Agentes (`.claude/agents/*.md`)

**Pode:** papel, ferramentas, modelo, critérios de qualidade do output e um bloco curto de
**fatos estáveis** (regras de arquitetura, onde estão os testes, ponteiro para DOC_MAP).

**Não pode:**
- Backlog, estado de sprint ou qualquer fato volátil — agentes não são atualizados a cada
  tarefa; conteúdo volátil neles envelhece silenciosamente.
- Cópia extensa de docs do projeto (apontar, não duplicar).

**Kits propagados** (agentes replicados entre projetos): as divergências locais legítimas de
cada derivado ficam registradas numa única memória dona no projeto-matriz; quem propaga lê
essa memória antes e nunca recria arquivo removido de propósito.

## 6. Pastas `.claude` aninhadas, órfãs e raiz de sessão

- **Raiz de sessão canônica = raiz do repositório.** Abrir sessão em subpasta do projeto ou
  na pasta-mãe dos workspaces cria um slug paralelo em `~/.claude/projects/` com settings e
  memória órfãos — dois universos de memória para o mesmo trabalho.
- `.claude` legítima existe em exatamente dois níveis: a global (`~/.claude`) e a da raiz de
  cada projeto. `.claude` em subpasta é defeito: fundir o que for útil na da raiz e apagar.
- **Pasta-mãe de workspaces** (ex.: `d:\workspaces`): nunca deve ter `CLAUDE.md` — arquivos
  CLAUDE.md de diretórios ancestrais são carregados por todas as sessões descendentes (ruído
  multiplicado por N projetos). `.claude` ali só se existir um workflow deliberado operado da
  raiz; caso contrário, remover.
- **Projetos arquivados** (`OLD/` etc.): a `.claude` vira peça de arquivo; não abrir sessões lá
  nem propagar kits para lá.
- **Slug morto** (a pasta de disco correspondente ao slug em `~/.claude/projects/` não existe
  mais): memória valiosa ali está encalhada — nunca mais será recuperada. Fundir os fatos
  duráveis na memória do projeto canônico vivo e remover a `memory/` do slug morto.
- Sintomas a caçar em auditoria: slugs com sufixo de subpasta em `~/.claude/projects/`;
  `settings.json` auto-gerado fora de raiz de projeto; pasta `memory/` sem `MEMORY.md`;
  locks/artefatos de runtime soltos em `.claude` de projeto; slug sem pasta de disco.

## 7. Ciclo de vida (promoção e rebaixamento)

- Feedback que se repete ou o usuário declara permanente → promover a regra de CLAUDE.md
  **e apagar a memória**.
- Procedimento executado manualmente pela 2ª vez → candidato a skill.
- Memória `project` cujo fato foi absorvido pelos docs do projeto → apagar (o doc é o lar).
- Skill/agente que não é invocado há muito tempo e cujo conteúdo envelheceu → revisar ou
  remover; artefato morto também é ruído (aparece nas listas de skills/agentes de toda sessão).

## 8. Fila de candidatos a memória (`<memory-dir>/_INBOX.md`)

**Descobrir e aprovar são atos de donos diferentes.** O agente descobre; só o dono promove. Um
agente que grava memória direto decide sozinho o que toda sessão futura vai carregar, e o custo
do erro — recall poluído, fato errado repetido para sempre, tokens gastos em todo turno — recai
sobre quem não participou da decisão.

**Regra:** o agente **não escreve por conta própria** em `<memory-dir>/*.md` nem no `MEMORY.md`
(`<memory-dir>` = `~/.claude/projects/<slug>/memory/`). Candidato a memória vira **uma linha** em
`<memory-dir>/_INBOX.md` — append-only, mesma forma do `docs/plans/_INBOX.md`. Criar o arquivo de
memória e indexá-lo é **ato explícito do dono**, nunca inferido de "o dono pareceu querer que eu
lembrasse disso".

**Única exceção** — a que a Regra 6 do CLAUDE.md global já obriga: **remover** ponteiro quebrado
do `MEMORY.md` e apagar memória comprovadamente obsoleta, na hora. A exceção é de **remoção**:
apagar reduz o que o recall carrega, escrever aumenta. Não existe exceção de escrita.

**Forma da linha** (uma por candidato):

- `AAAA-MM-DD` — `<slug-kebab>` — *type* (`user`/`feedback`/`project`/`reference`) — gancho de uma
  linha (o que seria a `description`) — **origem:** o que aconteceu que sugeriu a memória.

**Ciclo:** o dono decide e a linha **permanece**, marcada no lugar — `[promovido]` (arquivo criado
e indexado no `MEMORY.md`) ou `[descartado — motivo]`; enquanto pendente, fica intocada. Linha
nunca é apagada: o inbox é o registro de que o agente propôs e de como o dono decidiu.

**Drenagem:** a fila é apresentada ao dono no mesmo ato em que a skill `scrum-master` drena o
inbox de planos (passo 1). Fila sem hábito de drenagem acumula e o agente volta a gravar direto —
esse é o risco real desta regra, e a drenagem acoplada é a mitigação.

**Residência:** esta seção é **global e não entra no kit** (decisão `DK-6` do plano
`P-0729-v2-melhoria-candidatos`, PantonicApp): memória de projeto existe também em projeto
não-Pantonic do dono, e o teste de residência manda para o global o que vale fora da família. Os
projetos Pantonic recebem só um ponteiro (`GOVERNANCA.md` §3.1).
