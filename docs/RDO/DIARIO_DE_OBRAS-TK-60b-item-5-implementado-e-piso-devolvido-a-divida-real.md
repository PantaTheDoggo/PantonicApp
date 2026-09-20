# RDO — DIARIO_DE_OBRAS · TK-60b

**Plano:** `docs/DIARIO_DE_OBRAS.md`
**Tarefa:** `TK-60b` — Item 5 implementado e piso devolvido à dívida real
**Modelo:** Sonnet · **Classe:** implementacao
**Esquema de leitura do plano:** padrao

## Dossiê

**Objetivo:** implementar o item 5 do `TK-60a` **como ele já está escrito** — arquivo citado que não resolve nem por basename devolve `None` em silêncio — e devolver `_PISO_C11` às duas entradas de dívida real. Hoje `resolver_citacao_secao` devolve `C-11` quando `_resolver_arquivo_citado` devolve `None`, **contra o próprio docstring**, e as 3 entradas extras do piso são artefato desse defeito. Nenhuma rota nova: o estado final está medido.

**Arquivos-alvo:** - `.claude/tools/backlog.py` - `tests/test_backlog.py`

**Verificação:** - `python .claude/tools/backlog.py check` sai **exit 0** com `check: OK` e nenhuma violação (medido em cópia patchada contra o repo real, 2026-09-20). - `python .claude/checks/dead_code.py` sai **exit 0**. - `python -m pytest` verde, sem queda do piso de **235**.

**Pronto quando:** 1. `resolver_citacao_secao` devolve `None` quando `_resolver_arquivo_citado` devolve `None` — um `if caminho is None: return None` antes do laço de headings. **Nenhuma outra** mudança de comportamento: gramática de colheita, domínio, casamento por heading, chamador em `check` e fixture estão aprovados e não se tocam. 2. `_PISO_C11` tem **exatamente duas** entradas, as de dívida real em `GOVERNANCA.md`. As três saem: duas citam doc de **outro repositório** (PantonicVideo) e uma é **nota de diff**, não citação. As três são falso positivo do colhedor, que o item 5 silencia sozinho. **O princípio que isso destila, e que vale para toda autoria desta família:** *piso absorve dívida real, nunca falso positivo do colhedor*. O teste é mecânico — com o colhedor correto, **remover** uma entrada do piso tem de fazer o lint **acusar**; a entrada que some sem acusar nunca foi dívida, era defeito de gramática escondido dentro do piso. 3. **Teste que tranca a regra** (é o que impede a reincidência): par presença-ausência sobre o ramo do item 5 — citação a arquivo que não existe, e a arquivo de basename ambíguo, saem `None`; citação a arquivo existente com seção ausente sai `C-11`. 4. **Número de dívida corrigido no comentário de origem do piso: 15 ocorrências, não 13.** Medido pelo próprio instrumento com `_PISO_C11` vazio, em cópia: 15 violações, todas das duas seções ausentes, nenhuma das três espúrias reaparecendo. O 13 do `TK-60a` era contagem de **linhas** (`grep -c`) e não contava a ocorrência que o próprio card criou.

**Dossiê fechado por:** nenhum

**Extras (rótulos livres do plano, verbatim):**

- **Status:** `done` · 2026-09-20
- **Não fazer:** não corrigir nenhuma das 15 ocorrências; não editar `docs/plans/P-0741-modelo-conceitual.md` — plano vivo de outra janela; não editar `GOVERNANCA.md`; não mexer em `_REF_SECAO_RE`, `_CITACAO_SECAO_HARVEST_RE`, `_HEADING_NUMERADO_RE`, na chamada dentro de `check` nem na fixture.

## Execução

**Consumo:** 20 tool uses, 67.6 k tokens, 158.0 s (fonte: `<usage>` do encerramento)

**Pendência para o dono:** laudo: Decomposicao por arquivo dentro do comentario de origem do _PISO_C11 ainda soma 13 e contradiz o 15 do proprio cabecalho. Roteada ao TK-60c.

## Laudo

**Veredito:** ressalva

**Percentual:** 91%

**Dimensão bloqueante:** nenhuma

**Recomendação:** escalar

## Lições aprendidas na tarefa



## Fechamento

**Desdobramento:** aprovado com ressalva
