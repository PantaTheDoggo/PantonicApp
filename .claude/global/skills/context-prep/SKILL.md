---
name: context-prep
description: Fragmenta a carga inicial de contexto de uma tarefa — delega greps/varreduras exploratórias ao subagente context-scout e entrega ao modelo principal só um dossiê compacto, protegendo o contexto dele. Usar no início de tarefas que exigem explorar o repositório antes da fase de análise/implementação, ou quando o usuário pedir "preparação de contexto barata".
---

# context-prep — exploração em subagente, inteligência no modelo principal

A saída de greps e leituras exploratórias entra no contexto do modelo que as executa e é
cobrada na tarifa dele (e recobrada via cache a cada turno seguinte). Esta skill move essa
fase para o subagente [[context-scout]], preservando o contexto do
modelo principal para a fase intelectual. Complementa [[onboard]] (que cobre docs/planejamento);
esta cobre a exploração de código específica da tarefa.

## Critério de corte — delegar ou fazer direto

**Delegar ao context-scout quando** (qualquer um):
- A exploração esperada passa de ~3 buscas ou ~5 arquivos.
- A pergunta é aberta ("onde/como X é feito?", "quais arquivos usam Y?", "mapeie Z").
- Só a conclusão importa — o texto bruto dos matches não será citado nem editado.

**Fazer direto no modelo principal quando** (qualquer um):
- 1–3 greps pontuais cujo resultado literal é necessário (ex.: achar a linha exata a editar).
- O arquivo será editado — quem edita precisa ler o original, sem intermediário.
- O custo fixo do spawn (subagente frio relê CLAUDE.md, memória etc.) supera a exploração.

## Como delegar

1. Formule **uma pergunta de exploração fechada** por spawn (não "explore o projeto"), incluindo
   o objetivo da tarefa para o scout priorizar.
2. Spawn: `Agent` com `subagent_type: context-scout` (o agente já fixa o modelo).
   Perguntas independentes → múltiplos spawns em paralelo na mesma mensagem.
   **Todo prompt de spawn deve repetir o cap e o formato do dossiê** — encerre o prompt com:
   "Responda com um dossiê de ≤ 40 linhas: resposta direta, arquivos relevantes
   (`caminho:linha` + papel), assinaturas mínimas, lacunas." A instrução no prompt da tarefa
   prevalece sobre o arquivo do agente e evita dossiês longos entrando no modelo principal.
3. Trabalhe a partir do dossiê retornado; use os `caminho:linha` para Reads dirigidos
   (`offset`/`limit`) apenas do que a fase de implementação de fato exigir.
4. Se o dossiê listar **lacunas** que bloqueiam a tarefa, faça 1–2 verificações dirigidas
   diretamente — não re-explore por inteiro no modelo principal.

## Aceitação

- Nenhuma varredura ampla (>3 buscas / >5 arquivos) executada diretamente pelo modelo principal.
- O modelo principal só leu integralmente arquivos que editou ou citou.
- Dossiês recebidos ≤ ~40 linhas cada; lacunas tratadas com verificações dirigidas, não re-varredura.
- 2+ dossiês de scouts paralelos divergindo FACTUALMENTE sobre o mesmo símbolo/arquivo =
  bloqueante: 1 Read direto do trecho em disputa antes de montar a delegação (dossiê de scout
  pode estar confiante e errado, não só incompleto).
- Pergunta de precedência/gating: exigir do dossiê a condição de seleção de candidatos (ver
  item 5 do formato do scout); sem ela, o "ponto de plugagem" sugerido descreve o
  processamento, não o gate.
