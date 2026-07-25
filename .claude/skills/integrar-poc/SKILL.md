---
name: integrar-poc
description: Integra uma POC validada pelo cliente como plugin de uma aplicação Pantonic*, dissecando-a nas camadas da clean architecture (pipeline de 5 passos do agente integrador). Usar quando uma POC standalone foi aprovada e deve virar plugin.
---

# integrar-poc — de POC validada a plugin

Pré-condições (GOVERNANCA.md §5): a POC funciona standalone, foi estressada e **validada pelo
cliente**. Sem validação, não integrar. Restrições de elegibilidade: sem network, GPU, daemons
ou estado persistido fora do user-data; determinística (ou seed exposta); licença compatível;
dependências explícitas em `requirements.txt`.

## Pipeline (5 passos, na ordem)

### 1. Inventário de dependências externas
Listar toda lib, API de OS e I/O que a POC usa (o `pantonic-scout` faz a varredura). Saída:
tabela dependência → uso.

### 2. Mapeamento para serviços
Para cada dependência: existe serviço ACL que a cobre? Usar. Não existe? Propor serviço novo
(Protocol em `contracts/`, implementação em `services/<nome>/`) — isso é uma tarefa própria no
diário de obras, anterior à do plugin. Filesystem SEMPRE via `FilesystemService` (G6); paths
via `PathsService`; trabalho pesado via `TaskRunner`.

### 3. Dissecação e geração do plugin
Dissecar a POC nas camadas:
- **Lógica validada** → `plugins/<nome>/adhoc/` — preservada, **não refatorar, não reescrever**.
- **Entidades/VOs que cruzam camadas** → `contracts/domain/` (mirror discipline).
- **UI** → View no plugin + `view_model.py` (ViewModel QtCore-only; egress de I/O pelo
  ViewModel → serviços).
- **`plugin.py`** → orquestrador fino com `on_load / on_enable / on_disable / on_unload`,
  roteando entre adhoc e plataforma via sinais/estado. Estado só em `plugins.<nome>.*`;
  comunicação com outros plugins só via state keys.

### 4. Manifest
Gerar `manifest.json`: `name` (snake_case), `version`, `contracts_min_version`, `author`,
`description` (≤500 chars), `entry_point` (`modulo:Classe`), `required_services`
(`[{name, min_version}]`), `inputs`, `outputs`, `permissions`. Imports do plugin restritos à
allowlist (`contracts.*`, `PySide6.*`, `pathlib`, `typing`) — validado por AST no load.

### 5. Conformance e teste do conjunto
TF do plugin + suíte de conformance completa + piso de regressão (skill `guardrails-check`).
Plugin que falhe validação no load fica `failed` sem derrubar a aplicação — mas falha de
conformance bloqueia o `done` da tarefa.

## Saída

Plugin em `plugins/<nome>/` (manifest.json, plugin.py, view_model.py, adhoc/), serviços novos
registrados, testes verdes, entrada do diário de obras atualizada.
