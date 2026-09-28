# Campanha de insumos do P-0748 — respostas Q-1..Q-5

Respostas do scout às perguntas fechadas da §2.1 de `docs/plans/P-0748-tela-do-gerente.md`,
coletadas em 2026-09-23. Insumo da Fase 3b do planejador. `Q-6` é a sonda com o dono (matéria
da operação de viabilidade) e não consta aqui.

## Q-1 — chamadas de ferramenta do orquestrador no topo, por passo

| Passo | Ferramenta | Comando | Fonte |
|---|---|---|---|
| 2 | Bash | `python .claude/tools/backlog.py next` | scrum-master/SKILL.md:45 |
| 3 | Bash | `python .claude/tools/modelo.py check --plano <plano>` | scrum-master/SKILL.md:60 |
| 6 | Bash | `python .claude/tools/review_evidence.py --plano <plano> --tarefa <ID> --desde <ref> --out docs/RDO/evidencia/<plano>-<ID>.md` | scrum-master/SKILL.md:122-124 |
| 9 (antes) | Bash | `python .claude/tools/modelo.py check --plano <plano>` | scrum-master/SKILL.md:194 |
| 9 (status) | Bash | `python .claude/tools/backlog.py status <ID> <estado>` | scrum-master/SKILL.md:168 |
| 9 (close) | Bash | `python .claude/tools/rdo.py close --plano <plano> --tarefa <ID> --tool-uses <N> --tokens-k <k> --duracao-s <N> --veredito <aprovado\|ressalva> --percentual <0..100> --bloqueante <dim\|nenhuma> --recomendacao "…" --pendencia-laudo "…"` | scrum-master/SKILL.md:171-175 |
| 9 (telemetria) | Bash | `python .claude/tools/telemetria.py append --fonte usage/nao_medido` | scrum-master/SKILL.md:181 |
| 10/B0 | Bash | `python .claude/tools/review_evidence.py --plano <plano> --tarefa <ID> --desde <ref> --atribuir` | scrum-master/SKILL.md:251 |

## Q-2 — texto que as skills mandam escrever ao dono entre passos

Não encontrado. A `scrum-master` não prescreve texto ao dono entre passos. A `passagem-de-bastao`
se declara "transparente para o gerente do projeto — ele não a invoca, não a lê e não a
acompanha" (passagem-de-bastao/SKILL.md:10). O único texto ao dono é o "Relatório de
encerramento" (scrum-master/SKILL.md:276-304), no fim da janela.

## Q-3 — hooks e chaves de renderização

Global (`C:\Users\panta\.claude\settings.json`):
- `PreToolUse` matcher `Bash|PowerShell` → `pytest_pretooluse.py`, `verbose_cmd_pretooluse.py` (250-264)
- `PreToolUse` matcher `Read` → `read_cap_pretooluse.py` (267-275)
- `UserPromptSubmit` → `modelo_por_fase_userpromptsubmit.py` (277-287)
- `statusLine` → `statusline.py` (291-295) — única chave que afeta renderização
- outras chaves: `disableWorkflows` (289), `enableArtifact` (290)

Projeto (`.claude/settings.json`):
- `PreToolUse` matcher `.*` → `ocupacao.py` (23-32)
- `SubagentStop` → `telemetria_hook.py` (34-42)
- `UserPromptSubmit` → `backlog_hook.py` (44-53)

Nenhuma chave `verbose`, `collapse`, `hide` ou `outputStyle` encontrada.

## Q-4 — hook global de pytest

`C:\Users\panta\.claude\hooks\pytest_pretooluse.py` (1-65). Lê `tool_name` (35; aceita `Bash`
ou `PowerShell`) e `tool_input.command` (38). Sem reescrita devolve `{}` (25); com reescrita
devolve `hookSpecificOutput.updatedInput` com o comando encadeado a `pytest_filter.py` (50-60).

## Q-5 — linhas de retorno dos subagentes

- Executor (pantonic-executor.md:87-88): `<tarefa> review [pendencia=<uma linha>]` ou
  `<tarefa> blocked motivo=<dependencia|premissa|ferramenta> <uma linha de razão>`
- Reviewer (pantonic-reviewer.md:128-139): `<tarefa> <veredito> <percentual> bloqueante=<dimensão|nenhuma>`
  + `laudo=<caminho>`; opcionalmente o dossiê `Ato de modelo` de `conflito` anexo.
- Consultor (pantonic-consultant.md:24-25): `rota=<resolve|modelador|planejador>`
  [+ `estrategico=<uma frase>`], seguidas da decisão e do reparo.
