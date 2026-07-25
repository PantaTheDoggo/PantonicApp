---
name: audit-sweep
description: Pré-varredura mecânica das auditorias Pantonic* — executa a bateria determinística de greps (arch, pyside6, cleancode, fora-da-caixa) fora dos modelos caros e grava um dossiê compacto em docs/audits/SWEEP_<AAAA-MM-DD>.md. Usar SEMPRE antes de invocar qualquer pantonic-auditor-* ou o pantonic-fora-da-caixa.
---

# audit-sweep — fase mecânica das auditorias fora do modelo caro

Os auditores rodam em Opus/Sonnet e, como subagentes, não podem delegar a ninguém: cada match
de grep mecânico entraria no contexto do modelo caro. A detecção mecânica é determinística —
não precisa de inteligência. Esta skill roda a bateria no contexto principal (delegando ao
`pantonic-scout`, Haiku, pelos critérios da skill context-prep) e grava o resultado num dossiê
que os auditores consomem pronto, gastando o modelo caro só na leitura confirmatória e no
julgamento.

## Passos

1. **Delegar a bateria ao `pantonic-scout`** — um spawn por bloco da tabela abaixo, em
   paralelo na mesma mensagem. Todo prompt de spawn termina com: "Responda com um dossiê de
   ≤ 40 linhas: matches como `caminho:linha` (ou contagens por arquivo), sem colar código."
   Sem o scout disponível, rode Grep direto com `output_mode: files_with_matches` ou `count`
   (nunca `content` com contexto amplo).

2. **Bateria de verificações mecânicas** (excluir sempre `build/`, `dist/`, `.venv/`,
   `__pycache__/`, `node_modules/`, `plugins/*/adhoc/`):

   | Bloco | O que buscar |
   |---|---|
   | ARCH-reverse | `from services|from plugins|import services|import plugins` dentro de `infracore/` e `contracts/`; `from plugins` dentro de `services/` |
   | ARCH-acl | imports de libs externas (do requirements) fora de `services/` — uma lib por grep |
   | ARCH-mvvm | `QtWidgets` em `**/view_model*.py` e `**/model*.py`; `PySide6|Qt` em `contracts/` |
   | ARCH-mirror | `^class (\w+)` na codebase → nomes de classe duplicados entre camadas |
   | PYSIDE | `QtWidgets` fora de views/shell; `QThread|QRunnable|QThreadPool` fora do task_runner; `time.sleep` em código de UI; `setGeometry`; `lambda` em `.connect(`; `def eventFilter` |
   | CLEANCODE | módulos > 300 linhas (contagem por arquivo); nº de `def ` por módulo (top 15); `except Exception` |
   | FORA-DA-CAIXA | `_v2|_new|_fixed|legacy|old_|workaround|fallback|special`; comentários `hack|tempor|compatibilidade|não mexer|nao mexer`; flags booleanas em assinaturas (`: bool =`) |

3. **Gravar `docs/audits/SWEEP_<AAAA-MM-DD>.md`** — uma seção `## <Bloco>` por bloco, com os
   matches `caminho:linha` (agrupar por arquivo; sistêmico = listar contagem + 3 exemplos).
   Cabeçalho com data e, se houver git, o hash curto do HEAD. **Meta: ≤ 150 linhas.**

4. **Encerrar informando o usuário**: o sweep está pronto e qual auditor invocar. O auditor
   parte do sweep (não repete greps) e só lê os arquivos marcados.

## Validade

Um sweep vale enquanto a codebase não mudar de forma relevante (referência: ~7 dias ou o mesmo
HEAD). Auditoria com sweep velho → rodar a skill de novo antes.
