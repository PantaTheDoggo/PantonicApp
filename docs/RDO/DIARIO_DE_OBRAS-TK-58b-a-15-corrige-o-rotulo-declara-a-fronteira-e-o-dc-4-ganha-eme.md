# RDO — DIARIO_DE_OBRAS · TK-58b

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-58b` — A `## 15` corrige o rótulo, declara a fronteira e o `DC-4` ganha emenda
**Modelo:** Sonnet · **Classe:** redacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** a `## 15` de `docs/CUSTO_DO_PICKUP.md` deixa de sustentar *"o pickup custa 39.650 tk"* e passa a sustentar *"abrir janela com pickup custou 39.650 tk, dentro da faixa de abertura sem pickup do mesmo dia"*; o método `DC-4` ganha as três cláusulas que o caso mediu; e a `## 14` recebe um `a apurar` na composição dela.

**Arquivos-alvo:** - `docs/CUSTO_DO_PICKUP.md`

**Verificação:** - A `## 15` **não** contém mais a frase `o additionalContext do hook (**16.459 bytes**)`. - A `## 15` contém os literais `7.867` e `Fronteira do que esta medida sustenta`. - A `## 14` contém o literal `a apurar`. - `python -m pytest` verde, coletando **238** — não pode cair.

**Pronto quando:** os três fatos medidos no transcript da sessão `8760907f` estão publicados, e cada um com o objeto corretamente nomeado: 1. **Correção de rótulo.** `16.458` é o comprimento da **linha JSONL** do registro do hook, com envelope e escapes. O texto efetivamente injetado é **7.867 chars** (`rendered[0].content`), contra **7.079** na `## 14`: os dois pickups diferem **~11%**, não em ordem de grandeza. O recálculo de 36.140 que a pendência propunha era aritmética sobre o rótulo errado e **não** se publica. 2. **Fronteira declarada.** Os 39.650 tk **não isolam o pickup**: o registro do pickup é ~16% dos ~48,5 mil chars renderizados que precedem o primeiro `usage` — o resto é listagem de agentes (6.141), listagem de skills (11.948), arquivos anexados (13.605), `session_context` (3.377), MCP (2.053) e ambiente (1.718). E 39.650 cai **dentro** da linha de base sem pickup do mesmo dia (36.023 · 36.262 · 48.171 · 49.533): o efeito buscado é menor que a dispersão do controle. A seção publica o custo de **abertura de janela que fez pickup**, comparável aos regimes da `## 12` e da `## 13`, e **não** o custo do pickup. Isolar o pickup exige **controle pareado** (sessão gêmea, mesmo dia e mesma árvore, sem o gatilho); enquanto não houver, o par do `DC-4` fica **aberto por declaração**, não fechado por medida. 3. **A sessão nomeia o dossiê que o pickup projetou:** `MC-T1`, do plano `P-0741`. Medida de pickup sem a tarefa declarada não é interpretável. 4. **Emenda ao `DC-4`, três cláusulas:** (i) o pickup é **função da tarefa**, não constante, e toda medida nomeia o dossiê que projetou — duas medidas de tarefas diferentes **não formam par**; (ii) a metade `usage_1` só vale se **isolar** o pickup, e sem controle pareado a metade se declara aberta; (iii) **todo número publicado nomeia o objeto medido** — comprimento de registro, de texto renderizado e de texto-fonte são três objetos distintos. 5. **`a apurar` na `## 14`.** Recomposta para a sessão `8760907f` pelo mesmo método, a metade em chars dá **20.996** (`CLAUDE.md` 12.313 + `MEMORY.md` 816 + hook 7.867). A divergência contra os 26.760 não é só de dossiê: a `## 14` publica `CLAUDE.md` em **10.376** (medido **12.313** nesta data) e soma **8.488** chars de memórias indexadas que **não aparecem** entre os anexos da primeira requisição daquela sessão. Isso se registra como **`a apurar`**, não como defeito, e é pré-requisito de qualquer republicação da `## 14`.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20 — pendência do laudo do `TK-58a` (ressalva 88%), roteada pelo `A8a` e resolvida pelo consultor no escalonamento 7. **Nada aqui é remedição:** tudo o que corrige já está no transcript em disco.
- **Não fazer:** não republicar os 26.760 nem os 36.140; não alterar a metade em chars nem a redução de **−65,5%**, que nunca dependeu do `usage_1` e segue de pé; não abrir `docs/plans/P-0741-modelo-conceitual.md`; não tocar `GOVERNANCA.md`, `docs/RUBRICA_DE_REVISAO.md` nem `.claude/skills/diario-de-obras/SKILL.md` — a outra janela de orquestração está editando os três **agora**.

## Execução

**Consumo:** 12 tool uses, 59.2 k tokens, 129.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: Titulo e lead da secao 15 ainda sustentam o par fechado que o corpo da secao declara aberto. Roteado ao TK-58c.

## Laudo

**Veredito:** ressalva

**Percentual:** 88%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
