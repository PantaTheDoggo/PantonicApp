# RDO — P-0753 · AF-T15

# Humano

Tarefa "O piso comportamental e o teste de camadas passam a existir no hub" concluída em 2026-09-27.
O hub passa a ter o piso comportamental trancado e um teste que proíbe os instrumentos do kit de importar de tests ou caminhos.
Revisão: aprovada sem ressalva (100%).
Pendência para o dono: nenhuma.
Plano "Auditoria de encerramento do estágio 1: as dezoito recomendações e os dois tíquetes do consultor": 15/21 tarefas concluídas; próxima: "Os verificadores em PowerShell escrevem UTF-8 no console".
Handover para quem vem depois: registrado no card; o `next` o entrega à sucessora.

# Máquina

**Plano:** `docs/plans/P-0753-auditoria-estagio-1/plano.md`
**Tarefa:** `AF-T15` — O piso comportamental e o teste de camadas passam a existir no hub
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** Quem executa cria o piso dos comportamentos trancados e o teste de camadas que a verificação obrigatória do kit exige.

**Arquivos-alvo:** - `tests/piso_comportamental.txt` - `tests/conformance/test_camadas_do_kit.py`

**Verificação:** 1. `python .claude/checks/ratchet_piso.py` → `piso intacto` — antes `nenhum piso declarado`, depois `piso intacto` (esperado, não ensaiado) 2. `python -m pytest tests/conformance -q` → `exit 0` — antes `exit 4`, depois `exit 0` (esperado, não ensaiado) 3. `python -c "import subprocess,sys;from pathlib import Path;p=Path('tests/piso_comportamental.txt');c=subprocess.run([sys.executable,'-m','pytest','--co','-q'],capture_output=True,text=True).stdout.splitlines();tr=sorted(x.strip() for x in c if '::test_tr_' in x);print('ausente' if not p.exists() else ('iguais' if sorted(l.split(' — ')[0].strip() for l in p.read_text(encoding='utf-8').splitlines() if l.strip() and not l.startswith('#'))==tr else 'diferentes'))"` → `iguais` — antes `ausente`, depois `iguais` (esperado, não ensaiado) 4. `python -m pytest -q` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava) 5. `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` → `exit 0` — antes `exit 0`, depois `exit 0` (esperado, não ensaiado; trava)

**Pronto quando:** - bateria de testes do kit.piso e conformidade — o piso lista os comportamentos trancados e o teste de camadas roda na suíte — Verificações 1 a 3

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Fundamento:** `DAF-9`, `DAF-35`, `F-4`, `F-35`.
- **Operação do modelo:** `OP-15` - OP-15: Quem executa cria o piso dos comportamentos trancados e o teste de camadas que a verificação obrigatória do kit exige. - precisa de: dossiê de evidência — Quem implementa faz o resumo de diferenças sair do mesmo recorte da lista de arquivos tocados, e o relatório de auditoria de quem conduz contar como registro da condução, nunca como entrega fora do alvo.
- **Camada e fronteira:** bateria de testes do hub (`tests/`); a regra de camadas do kit é: nenhum `.claude/tools/*.py` nem `.claude/checks/*.py` importa de `tests` e nenhum importa `caminhos` por `import` (carrega por `importlib.util.spec_from_file_location`). A skill `guardrails-check` não muda.
- **Contratos/classes:** `tests/piso_comportamental.txt` — lido por `.claude/checks/ratchet_piso.py`: uma linha por comportamento, `<pytest nodeid> — <frase>` (separador espaço, travessão, espaço); linhas vazias e iniciadas por `#` ignoradas. `tests/conformance/test_camadas_do_kit.py` — função `violacoes_de_camada(arquivos: list[Path]) -> list[str]`, que faz `ast.parse` de cada arquivo e devolve `<arquivo>:<linha> importa <módulo>` para todo `Import`/`ImportFrom` cujo primeiro componente do módulo é `tests` ou `caminhos`.
- **Passos:** 1. Escrever `tests/conformance/test_camadas_do_kit.py` com `violacoes_de_camada` e os dois testes da seção `Testes`. 2. Gerar `tests/piso_comportamental.txt` **depois** do passo 1: a primeira linha é `# Piso comportamental do hub — um comportamento trancado por linha (GOVERNANCA.md §4.4); gerado pela AF-T15 do P-0753.`; depois, uma linha por nodeid da saída de `python -m pytest --co -q` que contém `::test_tr_`, na ordem da coleta, na forma `<nodeid> — <frase>`, com `<frase>` = o nome da função sem o prefixo `test_tr_` e sem o sufixo de parâmetro entre colchetes, com `_` trocado por espaço.
- **Restrições desta tarefa:** - Suíte `python -m pytest -q` sem falha ao fim; o piso é o total re-medido no despacho mais os 2 testes novos (referência datada: `452 passed`, 2026-09-27; `107` nodeids `::test_tr_` coletados na mesma data). - `pwsh -NoProfile -File .claude/checks/kit_check.ps1 -Mode check-drift` sai 0. - Só os `Arquivos-alvo` se criam; nada fora deles se toca, se reverte ou se commita; nenhum commit.
- **Não fazer:** não mudar `.claude/skills/guardrails-check/SKILL.md`; não mudar `ratchet_piso.py`; não escrever frase à mão fora da regra do passo 2; não criar `conftest.py` nem `__init__.py`.
- **Contingências:** - se o teste de camadas acusar violação real num arquivo de `.claude/tools/` ou `.claude/checks/` → parar e sinalizar `blocked` razão `premissa`, colando a lista (medido na autoria: nenhuma). - se `python .claude/checks/ratchet_piso.py` sair diferente de 0 com o piso recém-gerado → a lista divergiu da coleta: gerar de novo pelo passo 2 e seguir; se persistir, parar e sinalizar `blocked` razão `premissa`, colando a saída.
- **Testes:** TF `test_tf_instrumentos_do_kit_nao_importam_tests_nem_caminhos` — `violacoes_de_camada` sobre todo `.claude/tools/*.py` e `.claude/checks/*.py` devolve lista vazia. TR `test_tr_camada_acusa_import_de_tests_e_de_caminhos` — arquivo temporário com `from tests import x` e `import caminhos` dá exatamente 2 violações (a regra concorrente, "só `tests`", daria 1).
- **Fora do escopo desta tarefa:** teste de TR acrescentado depois desta tarefa entra no piso por quem o cria, não por esta tarefa.
- **Handover:** 2026-09-27 · para quem vier depois - **Entregue:** tests/piso_comportamental.txt com 124 nodeids de TR gerados da coleta (ratchet_piso.py sai 0); tests/conformance/test_camadas_do_kit.py com violacoes_de_camada e o par TF/TR - **Contrato:** o hub tem piso comportamental trancado e teste de camadas: instrumento do kit que importe tests ou caminhos por import quebra a suíte - **Não refazer:** o piso e o teste de camadas - **Pendente:** nenhum

## Execução

**Consumo:** 20 tool uses, 62.4 k tokens, 275.2 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** nenhuma

## Laudo

**Veredito:** aprovado

**Percentual:** 100%

**Dimensão bloqueante:** nenhuma

**Recomendação:** seguir

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado

# Histórico

Scrum master vai fechar a tarefa "O piso comportamental e o teste de camadas passam a existir no hub" como done: registrar estado, RDO e telemetria.
