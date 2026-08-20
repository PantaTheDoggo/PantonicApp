# Consumidores do kit agêntico

Registro dos projetos que consomem o kit publicado por este hub (`git subtree`
de `.claude/` para `<consumidor>/.claude/kit/`). As três colunas derivadas
(`Versão instalada`, `Último sync`, `Modo`) são escritas por máquina a partir
do `SYNC_STATE` que `sync-kit.ps1` grava em `<consumidor>/.claude/kit/` a cada
sync efetivo (`kit_check.ps1 -Mode consumers`, `V2K-T12b`) — editá-las à mão
recria o defeito do `.claude/README.md` (registro que mente em silêncio). A
coluna `Consumidor` é a única entrada mantida à mão.

Com a versão congelada em `0.0.0` (`GOVERNANCA.md` §10), a coluna `Versão instalada` carrega o
mesmo `0.0.0` para todos os consumidores e **não distingue deriva** — a deriva entre hub e
consumidor passa a ser detectada por `kit_check.ps1 -Mode check-drift` rodado no consumidor.

Hoje, **0/6 consumidores têm `.claude/kit/`** — nenhum foi instalado por
subtree ainda, então todas as 6 linhas abaixo permanecerem semeadas é o
resultado esperado, não falha.

| Consumidor | Versão instalada | Último sync | Modo |
|---|---|---|---|
| D:\workspaces\PantonicContainerForAWS | semeada — não verificada por sync | — | — |
| D:\workspaces\PantonicContainer | semeada — não verificada por sync | — | — |
| D:\workspaces\PantonicScanlator | semeada — não verificada por sync | — | — |
| D:\workspaces\PantonicPatom | semeada — não verificada por sync | — | — |
| D:\workspaces\PantonicMonitor | semeada — não verificada por sync | — | — |
| D:\workspaces\PantonicVideo | semeada — não verificada por sync | — | — |
