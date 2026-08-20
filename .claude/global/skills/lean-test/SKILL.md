---
name: lean-test
description: Run pytest with context-lean filtered output (only failures + final summary reach the context; full log saved to a temp file). Use when the user asks to run tests economically, or whenever running a large pytest suite. Args are passed to pytest (e.g. "tests/plugins -x").
---

# lean-test — rodar pytest com saída filtrada (economia de contexto)

Executa a suíte pytest canalizando a saída pelo filtro global, para que só o essencial
(falhas + sumário final) entre no contexto do agente.

## Passos

1. Monte o comando com os argumentos recebidos (default: `tests/ -q` se nenhum argumento):

   ```
   python -m pytest <args> -q 2>&1 | python "C:/Users/panta/.claude/hooks/pytest_filter.py"
   ```

   A sintaxe funciona igual nas ferramentas Bash e PowerShell. Exit code: 0 = suíte verde;
   1 = houve falha/erro (detectado pelo sumário do pytest).

   Observação: se o hook PreToolUse global `pytest_pretooluse.py` estiver ativo, um comando
   `pytest` puro já é reescrito assim automaticamente — neste caso basta rodar
   `python -m pytest <args> -q`.

2. O log completo fica em `%TEMP%\claude\pytest_last_run.log`
   (tipicamente `C:\Users\panta\AppData\Local\Temp\claude\pytest_last_run.log`).

3. Se houver falhas e o traceback filtrado não bastar para diagnosticar:
   - Use **Grep** no log completo com o nome do teste que falhou (com `-C 20` para contexto).
   - **Nunca** leia o log inteiro com Read/cat — isso desfaz a economia de contexto.

4. Para depuração profunda em que a saída integral é realmente necessária (raro), rode o
   pytest com `#nofilter` no fim do comando para pular o hook — e mesmo assim prefira
   redirecionar para arquivo e ler só a parte relevante.

## Relato ao usuário

Reporte apenas: contagem final (ex.: "1432 passed"), lista dos testes que falharam com a
causa de cada um, e o caminho do log completo.
