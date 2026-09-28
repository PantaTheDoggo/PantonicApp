# RDO — DIARIO_DE_OBRAS · TK-77a

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-77a` — O `validate` recusa frontmatter de agente ou skill que o YAML estrito recusa
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** o `kit_check.ps1 -Mode validate` passa a falhar, nomeando o arquivo, quando o frontmatter de um `.claude/agents/*.md` ou de um `.claude/skills/*/SKILL.md` não é YAML válido para `yaml.safe_load` ou não carrega um mapeamento. A classe é a mesma nas duas famílias (o harness lê as duas pelo frontmatter), e o leitor de frontmatter do script já é um só (`Get-Frontmatter`).

**Arquivos-alvo:** - `.claude/checks/frontmatter_yaml.py` (novo) - `.claude/checks/kit_check.ps1` - `tests/test_frontmatter_yaml.py` (novo)

**Verificação:** 1. `python -m pytest tests/test_frontmatter_yaml.py -q` → verde, com os três testes acima. 2. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode validate` na árvore → exit `0` (os 22 frontmatters atuais passam). 3. `python -m pytest tests -q` → nenhuma falha; total = o da referência do despacho mais os testes novos (referência medida na autoria: `353 passed`, re-derivada no despacho).

**Pronto quando:** o `validate` recusa, com o nome do arquivo na saída, o frontmatter de agente ou skill que o `yaml.safe_load` recusa, e aceita o mesmo arquivo com ` - ` no lugar de `: `; o par está em teste ponta a ponta sobre cópia do kit, falhando sobre o `kit_check.ps1` anterior e passando sobre o novo.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-25
- **Desenho:** 1. `frontmatter_yaml.py` — função pura `problemas(caminhos: list[Path]) -> list[str]`: para cada arquivo, lê em UTF-8, recorta o bloco entre a primeira linha `---` e a seguinte `---` (arquivo sem o bloco não é problema deste script: o `validate` já o acusa), aplica `yaml.safe_load` e devolve `"<caminho>: <primeira linha da mensagem do erro YAML>"` quando o parser levanta, ou `"<caminho>: frontmatter não é mapeamento"` quando o resultado não é `dict`. CLI: `python .claude/checks/frontmatter_yaml.py <arquivo>...` imprime um problema por linha e sai `1` se houver algum, `0` se nenhum; sem PyYAML importável imprime `frontmatter_yaml: PyYAML ausente` e sai `2`. Força UTF-8 em `stdout`/`stderr` antes de imprimir (mesma forma do `_forcar_utf8` de `.claude/tools/review_evidence.py`). 2. `kit_check.ps1`, bloco `validate` — logo antes da linha `# --- 3. Paridade de versão: VERSION (raiz) == .claude/KIT_VERSION --------`, uma seção `# --- 2b. Frontmatter é YAML válido` que chama o script com os caminhos de `$agentFiles` e dos `SKILL.md` existentes de `$skillDirs`, no mesmo padrão da chamada do `materializar.py` (seção 4): exit `1` → cada linha vira `$errors.Add("frontmatter YAML: $line")`; exit diferente de `0` e `1` → `$errors.Add("frontmatter YAML: saida nao interpretavel (exit N): ...")`.
- **Caso medido que motivou (2026-09-25, re-medido no ato da autoria):** cópia de `.claude/` + `VERSION` num diretório temporário, com `Efêmero - cada acionamento` trocado por `Efêmero: cada acionamento` na `description` de `agents/pantonic-consultant.md` → `kit_check.ps1 -Mode validate -KitRoot <cópia>/.claude` sai `kit_check: OK - 10 agente(s), 12 skill(s) …` exit `0`. `yaml.safe_load('description: Efêmero: cada acionamento')` levanta `ScannerError`; com ` - ` devolve o mapeamento. Hoje os 10 agentes e as 12 skills da árvore passam no `safe_load`.
- **Testes (novos, em `tests/test_frontmatter_yaml.py`):** - TF par presença-ausência sobre a função: arquivo com `description: A: b` → 1 problema com o nome do arquivo; o mesmo com `description: A - b` → 0 problemas. - TF: frontmatter que carrega lista ou escalar (não mapeamento) → 1 problema. - TF par presença-ausência ponta a ponta: cópia de `.claude/` + `VERSION` sob `tmp_path` (`shutil.copytree`, ignorando `__pycache__`), `pwsh -NoProfile -File <cópia>/.claude/checks/kit_check.ps1 -Mode validate -KitRoot <cópia>/.claude` → exit `0`; com a troca acima no `pantonic-consultant.md` da cópia → exit diferente de `0` e a saída contém `pantonic-consultant.md`. Pular (`pytest.skip`) se `pwsh` não estiver no `PATH`.
- **Não fazer:** não reescrever `Get-Frontmatter`/`Get-FieldValue` nem as checagens de campo existentes; não tocar os agentes e skills da árvore (todos passam); não acrescentar PyYAML a arquivo de dependências.
- **Contingências:** 1. se algum frontmatter da árvore falhar no `safe_load` no ato da execução → parar e sinalizar `blocked motivo=premissa` com o arquivo e a mensagem do parser, sem consertá-lo.

## Execução

**Consumo:** 27 tool uses, 72.7 k tokens, 383.6 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado
