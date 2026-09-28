"""TLG-T3 (`docs/plans/P-0748-tela-do-gerente.md` `### TLG-T3b`) — TFs de
`.claude/tools/progresso_hook.py`: ganchos `PreToolUse`/`PostToolUse`/`UserPromptSubmit`/`Stop`
que geram, a cada evento de transição do loop, a frase do repertório `FRASES` e a gravam em
`.claude/estado/progresso.txt`, uma por linha, na ordem em que o loop as atravessa.

Padrão de carga do módulo idêntico a `tests/test_modelo.py:35,53-54` (`.claude/` não é pacote
importável).
"""
from __future__ import annotations

import importlib.util
import json
import os
import sys
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
_PROGRESSO_HOOK_PATH = _ROOT / ".claude" / "tools" / "progresso_hook.py"


def _load_progresso_hook():
    spec = importlib.util.spec_from_file_location("progresso_hook", _PROGRESSO_HOOK_PATH)
    modulo = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = modulo
    spec.loader.exec_module(modulo)
    return modulo


progresso_hook = _load_progresso_hook()


def P(**k):
    return {
        "session_id": "s1",
        "transcript_path": str(Path("t.jsonl")),
        **k,
    }


@pytest.fixture
def raiz(tmp_path):
    plans = tmp_path / "docs" / "plans"
    plans.mkdir(parents=True)
    (plans / "P-9999-teste.md").write_text(
        "# P-9999 — Plano de teste\n"
        "\n"
        "### TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
        "### TLG-T10 — Outro título [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer y.\n",
        encoding="utf-8",
    )
    (tmp_path / "docs" / "DIARIO_DE_OBRAS.md").write_text(
        "# Diário de Obras — Teste\n"
        "## TK-99 — Tíquete de teste\n"
        "### TK-99a — Card do tíquete [Sonnet · classe mecanica]\n"
        "- **Objetivo:** Fazer z.\n",
        encoding="utf-8",
    )
    return tmp_path


@pytest.fixture
def estado(tmp_path):
    return tmp_path / "estado"


def progresso(estado):
    arq = estado / "progresso.txt"
    if not arq.exists():
        return []
    return arq.read_text(encoding="utf-8").splitlines()


def payload_next(resp_texto, session_id="s1", transcript_path=None):
    p = P(
        hook_event_name="PostToolUse",
        tool_name="Bash",
        tool_input={"command": "python .claude/tools/backlog.py next"},
        tool_response={"stdout": resp_texto},
        session_id=session_id,
    )
    if transcript_path is not None:
        p["transcript_path"] = transcript_path
    return p


def rodar(payload, estado, raiz):
    return progresso_hook.main(entrada=json.dumps(payload), estado=estado, raiz=raiz)


# --- TF-GER-1 -----------------------------------------------------------------------


def test_tf_ger_1_texto_da_resposta():
    f = progresso_hook.texto_da_resposta
    assert f("a\nb") == "a\nb"
    assert f({"stdout": "a\nb"}) == "a\nb"
    assert f({"content": [{"type": "text", "text": "a"}, {"type": "text", "text": "b"}]}) == "a\nb"
    assert f([{"type": "text", "text": "a"}, {"type": "text", "text": "b"}]) == "a\nb"
    assert f(None) == ""
    assert f({"x": 1}) == '{"x": 1}'
    assert f({"content": []}) == ""
    assert f([]) == ""
    assert f({"content": [{"type": "image"}]}) == ""


# --- TF-GER-2 -------------------------------------------------------------------------


def test_tf_ger_2_tarefa_escolhida_primeira_da_sessao(estado, raiz):
    payload = payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    )
    assert rodar(payload, estado, raiz) == 0
    assert progresso(estado) == [
        'Abrindo a janela do plano "Plano de teste".',
        'Tarefa "Um título de teste". Passo: conferir os gates e preparar o despacho.',
    ]
    estado_loop = json.loads((estado / progresso_hook.ESTADO_ARQ).read_text(encoding="utf-8"))
    assert estado_loop["tarefa"] == "TLG-T9"
    assert estado_loop["titulo"] == "Um título de teste"
    assert estado_loop["objetivo"] == "Fazer x."
    assert estado_loop["aberta"] is True
    assert "encerrada" not in estado_loop

    assert rodar(payload, estado, raiz) == 0
    linhas = progresso(estado)
    assert len(linhas) == 3
    assert linhas[2] == 'Tarefa "Um título de teste". Passo: conferir os gates e preparar o despacho.'


# --- TF-GER-3 -------------------------------------------------------------------------


def test_tf_ger_3_fila_vazia(estado, raiz, tmp_path):
    payload = payload_next("nada delegável\n")
    assert rodar(payload, estado, raiz) == 0
    assert progresso(estado) == [
        "Scrum master não encontrou tarefa delegável na fila. Encerrando a janela com o relatório."
    ]

    e2 = tmp_path / "estado2"
    e2.mkdir(parents=True)
    (e2 / progresso_hook.ESTADO_ARQ).write_text(
        json.dumps({
            "sessao": "s1",
            "aberta": True,
            "tarefa_fechada": "TLG-T9",
            "titulo_fechada": "Um título de teste",
        }),
        encoding="utf-8",
    )
    assert rodar(payload, e2, raiz) == 0
    assert progresso(e2) == [
        'Scrum master concluiu a tarefa "Um título de teste"; nada delegável na fila. '
        "Encerrando a janela com o relatório."
    ]
    estado_loop = json.loads((e2 / progresso_hook.ESTADO_ARQ).read_text(encoding="utf-8"))
    assert "tarefa_fechada" not in estado_loop


# --- TF-GER-4 -------------------------------------------------------------------------


def test_tf_ger_4_estado_mudado(estado, raiz):
    rodar(payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    ), estado, raiz)

    p_in_progress = P(
        hook_event_name="PreToolUse", tool_name="Bash",
        tool_input={"command": "python .claude/tools/backlog.py status TLG-T9 in-progress"},
    )
    assert rodar(p_in_progress, estado, raiz) == 0
    assert progresso(estado)[-1] == (
        'Tarefa "Um título de teste": gates aprovados; vou materializar in-progress '
        "e gravar o ponto de partida."
    )

    antes = len(progresso(estado))
    p_review = P(
        hook_event_name="PreToolUse", tool_name="Bash",
        tool_input={"command": "python .claude/tools/backlog.py status TLG-T9 review"},
    )
    assert rodar(p_review, estado, raiz) == 0
    assert len(progresso(estado)) == antes

    p_done = P(
        hook_event_name="PreToolUse", tool_name="Bash",
        tool_input={"command": "python .claude/tools/backlog.py status TLG-T9 done"},
    )
    assert rodar(p_done, estado, raiz) == 0
    assert progresso(estado)[-1] == (
        'Scrum master vai fechar a tarefa "Um título de teste" como done: registrar '
        "estado, RDO e telemetria."
    )
    estado_loop = json.loads((estado / progresso_hook.ESTADO_ARQ).read_text(encoding="utf-8"))
    assert estado_loop["tarefa_fechada"] == "TLG-T9"

    antes = len(progresso(estado))
    p_done_post = P(
        hook_event_name="PostToolUse", tool_name="Bash",
        tool_input={"command": "python .claude/tools/backlog.py status TLG-T9 done"},
    )
    assert rodar(p_done_post, estado, raiz) == 0
    assert len(progresso(estado)) == antes


# --- TF-GER-5 -------------------------------------------------------------------------


def test_tf_ger_5_agente_despachado(estado, raiz):
    rodar(payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    ), estado, raiz)

    def despachar(sub, prompt="…"):
        p = P(hook_event_name="PreToolUse", tool_name="Agent",
              tool_input={"subagent_type": sub, "prompt": prompt})
        rodar(p, estado, raiz)
        return progresso(estado)[-1]

    antes = len(progresso(estado))
    assert despachar("pantonic-executor") == (
        'Agente executor recebe a tarefa "Um título de teste" e vai executar: Fazer x.'
    )
    assert despachar("pantonic-reviewer") == (
        'Agente revisor recebe a tarefa "Um título de teste" e vai confrontar a entrega com o card.'
    )
    assert despachar("pantonic-consultant") == (
        'Agente consultor recebe a tarefa "Um título de teste" e vai triar.'
    )
    assert despachar("pantonic-model-designer", "Ato: emenda") == (
        'Agente modelador recebe a tarefa "Um título de teste" e vai fazer emenda no modelo.'
    )
    assert despachar("pantonic-model-designer", "sem ato aqui") == (
        'Agente modelador recebe a tarefa "Um título de teste" e vai atualizar o modelo.'
    )
    assert despachar("pantonic-planner") == (
        'Agente planejador recebe a tarefa "Um título de teste" e vai replanejar.'
    )
    depois = len(progresso(estado))
    rodar(P(hook_event_name="PreToolUse", tool_name="Agent",
            tool_input={"subagent_type": "pantonic-scout", "prompt": "…"}), estado, raiz)
    assert len(progresso(estado)) == depois


# --- TF-GER-6 -------------------------------------------------------------------------


def _volta_executor(estado, raiz, texto):
    rodar(payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    ), estado, raiz)
    p = P(hook_event_name="PostToolUse", tool_name="Agent",
          tool_input={"subagent_type": "pantonic-executor"},
          tool_response={"content": [{"type": "text", "text": texto}]})
    rodar(p, estado, raiz)
    return progresso(estado)[-1]


def test_tf_ger_6_agente_de_volta_executor(estado, raiz, tmp_path):
    e2 = tmp_path / "estado2"
    e3 = tmp_path / "estado3"
    assert _volta_executor(estado, raiz, "TLG-T9 review pendencia=uma coisa\nresto") == (
        'Agente executor devolveu a tarefa "Um título de teste": review — uma coisa.'
    )
    assert _volta_executor(e2, raiz, "TLG-T9 review") == (
        'Agente executor devolveu a tarefa "Um título de teste": review — sem pendência.'
    )
    assert _volta_executor(e3, raiz, "TLG-T9 blocked motivo=premissa falta y") == (
        'Agente executor devolveu a tarefa "Um título de teste": blocked — motivo premissa: falta y.'
    )
    assert _volta_executor(tmp_path / "estado4", raiz, "TLG-T9 review [pendencia=uma coisa]") == (
        'Agente executor devolveu a tarefa "Um título de teste": review — uma coisa.'
    )


# --- TF-GER-7 -------------------------------------------------------------------------


def test_tf_ger_7_agente_de_volta_revisor(estado, raiz):
    rodar(payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    ), estado, raiz)
    p = P(hook_event_name="PostToolUse", tool_name="Agent",
          tool_input={"subagent_type": "pantonic-reviewer"},
          tool_response={"content": [{"type": "text", "text": "TLG-T9 aprovado 100 bloqueante=nenhuma"}]})
    rodar(p, estado, raiz)
    assert progresso(estado)[-1] == (
        'Agente revisor devolveu a tarefa "Um título de teste": aprovado 100%, bloqueante nenhuma, recomendação não informada.'
    )
    rodar(P(hook_event_name="PostToolUse", tool_name="Agent",
            tool_input={"subagent_type": "pantonic-reviewer"},
            tool_response={"content": [{"type": "text", "text": "TLG-T9 aprovado 100% bloqueante=nenhuma"}]}),
          estado, raiz)
    assert progresso(estado)[-2:] == [
        'Agente revisor devolveu a tarefa "Um título de teste": aprovado 100%, bloqueante nenhuma, recomendação não informada.'
    ] * 2


def test_tf_m7_revisor_com_recomendacao(estado, raiz):
    rodar(payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    ), estado, raiz)
    p = P(hook_event_name="PostToolUse", tool_name="Agent",
          tool_input={"subagent_type": "pantonic-reviewer"},
          tool_response={"content": [{"type": "text",
                                       "text": "TLG-T9 ressalva 91 bloqueante=nenhuma recomendacao=seguir com ressalva"}]})
    rodar(p, estado, raiz)
    assert progresso(estado)[-1] == (
        'Agente revisor devolveu a tarefa "Um título de teste": ressalva 91%, bloqueante nenhuma, '
        'recomendação seguir com ressalva.'
    )


def test_tr_m7_revisor_sem_recomendacao_diz_nao_informada(estado, raiz):
    rodar(payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    ), estado, raiz)
    p = P(hook_event_name="PostToolUse", tool_name="Agent",
          tool_input={"subagent_type": "pantonic-reviewer"},
          tool_response={"content": [{"type": "text", "text": "TLG-T9 aprovado 100 bloqueante=nenhuma"}]})
    rodar(p, estado, raiz)
    assert progresso(estado)[-1] == (
        'Agente revisor devolveu a tarefa "Um título de teste": aprovado 100%, bloqueante nenhuma, '
        'recomendação não informada.'
    )


# --- TF-GER-8 -------------------------------------------------------------------------


def _volta_consultor(estado, raiz, texto):
    rodar(payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    ), estado, raiz)
    p = P(hook_event_name="PostToolUse", tool_name="Agent",
          tool_input={"subagent_type": "pantonic-consultant"},
          tool_response={"content": [{"type": "text", "text": texto}]})
    rodar(p, estado, raiz)
    return progresso(estado)[-1]


def test_tf_ger_8_agente_de_volta_consultor(estado, raiz, tmp_path):
    e2 = tmp_path / "estado2"
    assert _volta_consultor(estado, raiz, "rota=resolve\nreparo…") == (
        'Agente consultor devolveu a tarefa "Um título de teste": rota resolve.'
    )
    assert _volta_consultor(e2, raiz, "rota=planejador\nestrategico=muda o escopo") == (
        'Agente consultor devolveu a tarefa "Um título de teste": rota planejador; '
        "estratégico: muda o escopo."
    )


# --- TF-GER-9 -------------------------------------------------------------------------


def test_tf_ger_9_forma_generica(estado, raiz, tmp_path):
    assert _volta_executor(estado, raiz, "texto livre sem forma") == (
        'Agente executor devolveu a tarefa "Um título de teste": texto livre sem forma.'
    )

    e2 = tmp_path / "estado2"
    rodar(payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    ), e2, raiz)
    p = P(hook_event_name="PostToolUse", tool_name="Agent",
          tool_input={"subagent_type": "pantonic-model-designer"},
          tool_response={"content": [{"type": "text", "text": "Plano: docs/plans/x.md\nAto: emenda"}]})
    rodar(p, e2, raiz)
    assert progresso(e2)[-1] == (
        'Agente modelador devolveu a tarefa "Um título de teste": Plano: docs/plans/x.md.'
    )

    e3 = tmp_path / "estado3"
    _volta_executor(e3, raiz, "a" * 200)
    linha3 = progresso(e3)[-1]
    prefixo = 'Agente executor devolveu a tarefa "Um título de teste": '
    assert linha3 == prefixo + "a" * 160 + "…."

    e4 = tmp_path / "estado4"
    assert _volta_executor(e4, raiz, "") == (
        'Agente executor devolveu a tarefa "Um título de teste": (sem texto).'
    )

    e5 = tmp_path / "estado5"
    rodar(payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    ), e5, raiz)
    p5 = P(hook_event_name="PostToolUse", tool_name="Agent",
           tool_input={"subagent_type": "pantonic-executor"},
           tool_response={"content": []})
    rodar(p5, e5, raiz)
    assert progresso(e5)[-1] == (
        'Agente executor devolveu a tarefa "Um título de teste": (sem texto).'
    )


# --- TF-GER-10 ------------------------------------------------------------------------


def test_tf_ger_10_evidencia(estado, raiz):
    rodar(payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    ), estado, raiz)
    cmd = ("python .claude/tools/review_evidence.py --plano docs/plans/P-9999-teste.md "
           "--tarefa TLG-T9 --desde abc --out x.md")
    p = P(hook_event_name="PreToolUse", tool_name="Bash", tool_input={"command": cmd})
    rodar(p, estado, raiz)
    assert progresso(estado)[-1] == (
        'Tarefa "Um título de teste": vou reunir para o revisor o que mudou desde o despacho, '
        "os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit."
    )

    p2 = P(hook_event_name="PreToolUse", tool_name="Bash", tool_input={"command": cmd + " --atribuir"})
    rodar(p2, estado, raiz)
    assert progresso(estado)[-1] == (
        'Tarefa "Um título de teste": vou medir a que arquivo a pendência é atribuível.'
    )


# --- TF-GER-11 ------------------------------------------------------------------------


def test_tf_ger_11_tarefa_escolhida_depois_de_fechada(estado, raiz):
    estado.mkdir(parents=True)
    (estado / progresso_hook.ESTADO_ARQ).write_text(
        json.dumps({
            "sessao": "s1",
            "aberta": True,
            "tarefa_fechada": "TLG-T9",
            "titulo_fechada": "Um título de teste",
        }),
        encoding="utf-8",
    )
    payload = payload_next(
        "=== PRÓXIMA TAREFA: TLG-T10 — Outro título [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer y.\n"
    )
    rodar(payload, estado, raiz)
    assert progresso(estado) == [
        'Scrum master concluiu a tarefa "Um título de teste" e vai pegar a tarefa "Outro título".',
        'Tarefa "Outro título". Passo: conferir os gates e preparar o despacho.',
    ]


# --- TF-GER-12 ------------------------------------------------------------------------


def test_tf_ger_12_stop(estado, raiz):
    estado.mkdir(parents=True)
    (estado / progresso_hook.ESTADO_ARQ).write_text(
        json.dumps({"sessao": "s1", "aberta": True}), encoding="utf-8"
    )
    p = P(hook_event_name="Stop")
    rodar(p, estado, raiz)
    assert progresso(estado) == []

    p_show = P(hook_event_name="PreToolUse", tool_name="Bash",
               tool_input={"command": "python .claude/tools/modelo.py show --plano docs/plans/P-9999-teste.md"})
    rodar(p_show, estado, raiz)
    assert progresso(estado) == []

    rodar(p, estado, raiz)
    assert progresso(estado) == ["Scrum master mostrou o modelo do plano e aguarda; a resposta dele está na extensão."]
    estado_loop = json.loads((estado / progresso_hook.ESTADO_ARQ).read_text(encoding="utf-8"))
    assert estado_loop["aberta"] is True
    assert "relatorio" not in estado_loop

    rodar(p, estado, raiz)
    assert len(progresso(estado)) == 1

    e2 = estado.parent / "estado2"
    p_sem_loop = P(hook_event_name="Stop")
    rodar(p_sem_loop, e2, raiz)
    assert not (e2 / "progresso.txt").exists()

    e3 = estado.parent / "estado3"
    rodar(p_show, e3, raiz)
    rodar(p_sem_loop, e3, raiz)
    assert not (e3 / "progresso.txt").exists()


# --- TF-GER-13 ------------------------------------------------------------------------


def test_tf_ger_13_barreiras_e_falha_aberta(estado, raiz, capsys, tmp_path):
    payload = payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    )
    e1 = tmp_path / "e1"
    payload["agent_type"] = "pantonic-executor"
    assert progresso_hook.main(entrada=json.dumps(payload), estado=e1, raiz=raiz) == 0
    assert not (e1 / "progresso.txt").exists()

    e2 = tmp_path / "e2"
    assert progresso_hook.main(entrada="isto não é json", estado=e2, raiz=raiz) == 0
    assert not (e2 / "progresso.txt").exists()

    e3 = tmp_path / "e3"
    p3 = P(hook_event_name="PostToolUse", tool_name="Read", tool_input={})
    assert progresso_hook.main(entrada=json.dumps(p3), estado=e3, raiz=raiz) == 0
    assert not (e3 / "progresso.txt").exists()

    e4 = tmp_path / "e4"
    p4 = P(hook_event_name="PreToolUse", tool_name="Bash", tool_input={"command": "git status"})
    assert progresso_hook.main(entrada=json.dumps(p4), estado=e4, raiz=raiz) == 0
    assert not (e4 / "progresso.txt").exists()

    saida = capsys.readouterr()
    assert saida.out == ""
    assert saida.err == ""


# --- TF-GER-14 ------------------------------------------------------------------------


def test_tf_ger_14_agregacao(estado, raiz):
    p = P(hook_event_name="PreToolUse", tool_name="Bash",
          tool_input={"command": "python .claude/tools/backlog.py status TLG-T77 in-progress"})
    rodar(p, estado, raiz)
    assert progresso(estado) == [
        'Tarefa "TLG-T77": gates aprovados; vou materializar in-progress e gravar o ponto de partida.'
    ]

    e2 = raiz / "estado2"
    e2.mkdir(parents=True)
    (e2 / "tarefa-corrente.json").write_text(json.dumps({"tarefa": "TLG-T9"}), encoding="utf-8")
    p2 = P(hook_event_name="PreToolUse", tool_name="Agent",
           tool_input={"subagent_type": "pantonic-executor", "prompt": "…"})
    rodar(p2, e2, raiz)
    assert progresso(e2) == [
        'Agente executor recebe a tarefa "Um título de teste" e vai executar: Fazer x.'
    ]

    e3 = raiz / "estado3"
    p3 = payload_next(
        "=== PRÓXIMA TAREFA: TK-99a — Card do tíquete [Sonnet · classe mecanica]\n"
        "- **Objetivo:** Fazer z.\n"
    )
    rodar(p3, e3, raiz)
    assert progresso(e3) == [
        'Abrindo a janela do plano "Tíquete de teste".',
        'Tarefa "Card do tíquete". Passo: conferir os gates e preparar o despacho.',
    ]

    plano = raiz / "docs" / "plans" / "P-9999-teste.md"
    conteudo = plano.read_text(encoding="utf-8")
    conteudo += "### TLG-T11 — Objetivo longo [Sonnet · classe redacao]\n"
    conteudo += "- **Objetivo:** " + ("x" * 300) + "\n"
    plano.write_text(conteudo, encoding="utf-8")
    e4 = raiz / "estado4"
    p4 = payload_next(
        "=== PRÓXIMA TAREFA: TLG-T11 — Objetivo longo [Sonnet · classe redacao]\n"
        "- **Objetivo:** " + ("x" * 300) + "\n"
    )
    rodar(p4, e4, raiz)
    estado_loop = json.loads((e4 / progresso_hook.ESTADO_ARQ).read_text(encoding="utf-8"))
    assert len(estado_loop["objetivo"]) == 240
    assert estado_loop["objetivo"].endswith("…")


# --- TF-GER-15 ------------------------------------------------------------------------


def test_tf_ger_15_amostra_real_handback(estado, raiz):
    rodar(payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    ), estado, raiz)

    p_post = P(
        hook_event_name="PostToolUse", tool_name="Agent",
        tool_input={"subagent_type": "pantonic-executor", "prompt": "…"},
        tool_response={
            "status": "completed",
            "agentId": "ab2f2cd682dae49db",
            "agentType": "pantonic-executor",
            "handback": "send",
            "content": [{
                "type": "text",
                "text": (
                    'This agent\'s report was delivered to you as a message from '
                    '"ab2f2cd682dae49db" (its SubagentHandback call). Read it there; '
                    "it is not repeated here.\n"
                ),
            }],
        },
    )
    antes = len(progresso(estado))
    rodar(p_post, estado, raiz)
    assert len(progresso(estado)) == antes
    estado_loop = json.loads((estado / progresso_hook.ESTADO_ARQ).read_text(encoding="utf-8"))
    assert estado_loop["pendentes"] == {"ab2f2cd682dae49db": "pantonic-executor"}

    prompt = (
        '<agent-message from="ab2f2cd682dae49db">\n'
        "[Subagent hand-back] The text below is the final report of a subagent this "
        "session delegated to. The report follows:\n"
        "  TLG-T9 blocked motivo=premissa falta y\n"
        "  segunda linha\n"
        "</agent-message>"
    )
    p_ups = P(hook_event_name="UserPromptSubmit", prompt=prompt)
    rodar(p_ups, estado, raiz)
    assert progresso(estado)[-1] == (
        'Agente executor devolveu a tarefa "Um título de teste": blocked — motivo premissa: falta y.'
    )
    estado_loop = json.loads((estado / progresso_hook.ESTADO_ARQ).read_text(encoding="utf-8"))
    assert estado_loop["pendentes"] == {}

    antes = len(progresso(estado))
    rodar(p_ups, estado, raiz)
    assert len(progresso(estado)) == antes


# --- TF-GER-16 ------------------------------------------------------------------------


def test_tf_ger_16_sessao_nova(estado, raiz):
    estado.mkdir(parents=True)
    (estado / progresso_hook.ESTADO_ARQ).write_text(
        json.dumps({"sessao": "s0", "aberta": True, "tarefa": "TLG-T9"}), encoding="utf-8"
    )
    payload = payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n",
        session_id="s1",
    )
    rodar(payload, estado, raiz)
    linhas = progresso(estado)
    assert linhas[0] == 'Abrindo a janela do plano "Plano de teste".'
    estado_loop = json.loads((estado / progresso_hook.ESTADO_ARQ).read_text(encoding="utf-8"))
    assert estado_loop["sessao"] == "s1"


# --- TF-GER-17 ------------------------------------------------------------------------


def test_tf_ger_17_trava(estado, raiz):
    payload = payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    )
    estado.mkdir(parents=True)
    trava = estado / "progresso.lock"
    fd = os.open(trava, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    os.close(fd)

    assert progresso_hook.main(entrada=json.dumps(payload), estado=estado, raiz=raiz, espera=0.2) == 0
    assert not (estado / "progresso.txt").exists()

    mtime_antigo = os.stat(trava).st_mtime - 60
    os.utime(trava, (mtime_antigo, mtime_antigo))

    assert progresso_hook.main(entrada=json.dumps(payload), estado=estado, raiz=raiz, espera=0.2) == 0
    assert len(progresso(estado)) == 2
    assert not trava.exists()


# --- TF-GER-18 ------------------------------------------------------------------------


def test_tf_ger_18_residencia():
    import re

    assert len(progresso_hook.FRASES) == 25
    assert not any("<ID>" in v for v in progresso_hook.FRASES.values())

    skill = (_ROOT / ".claude" / "skills" / "scrum-master" / "SKILL.md").read_text(encoding="utf-8")
    padrao = re.compile(r"^\| `(M-\d+b?)` \| [^|]* \| `([^`]*)` \|", re.M)
    achados = padrao.findall(skill)
    assert len(achados) == 25
    for id_frase, frase_skill in achados:
        assert progresso_hook.FRASES[id_frase] == frase_skill


# --- TF-GER-19 ------------------------------------------------------------------------


def test_tf_ger_19_userpromptsubmit_sem_volta_pendente(estado, raiz):
    p1 = P(hook_event_name="UserPromptSubmit", prompt="rode o próximo passo")
    rodar(p1, estado, raiz)
    assert progresso(estado) == []

    p2 = P(hook_event_name="UserPromptSubmit", prompt=(
        '<agent-message from="xyz">\n'
        "[Subagent hand-back] The text below is the final report of a subagent this "
        "session delegated to. The report follows:\n"
        "  TLG-T9 review\n"
        "</agent-message>"
    ))
    rodar(p2, estado, raiz)
    assert progresso(estado) == []

    estado.mkdir(parents=True, exist_ok=True)
    (estado / progresso_hook.ESTADO_ARQ).write_text(
        json.dumps({"sessao": "s1", "tarefa": "TLG-T9", "titulo": "Um título de teste",
                    "pendentes": {"r1": "pantonic-reviewer"}}),
        encoding="utf-8",
    )
    p3 = P(hook_event_name="UserPromptSubmit", prompt=(
        '<agent-message from="r1">\n'
        "[Subagent hand-back] The text below is the final report of a subagent this "
        "session delegated to. The report follows:\n"
        "  TLG-T9 aprovado 100 bloqueante=nenhuma\n"
        "</agent-message>"
    ))
    rodar(p3, estado, raiz)
    assert progresso(estado) == [
        'Agente revisor devolveu a tarefa "Um título de teste": aprovado 100%, bloqueante nenhuma, recomendação não informada.'
    ]

    e2 = raiz / "estado_consultor"
    e2.mkdir(parents=True)
    (e2 / progresso_hook.ESTADO_ARQ).write_text(
        json.dumps({"sessao": "s1", "tarefa": "TLG-T9", "titulo": "Um título de teste",
                    "pendentes": {"c1": "pantonic-consultant"}}),
        encoding="utf-8",
    )
    p4 = P(hook_event_name="UserPromptSubmit", prompt=(
        '<agent-message from="c1">\n'
        "[Subagent hand-back] The text below is the final report of a subagent this "
        "session delegated to. The report follows:\n"
        "  rota=planejador\n"
        "  estrategico=muda o escopo\n"
        "</agent-message>"
    ))
    rodar(p4, e2, raiz)
    assert progresso(e2) == [
        'Agente consultor devolveu a tarefa "Um título de teste": rota planejador; '
        "estratégico: muda o escopo."
    ]


# --- TF-GER-20 ------------------------------------------------------------------------


def test_tf_ger_20_titulo_sobrevive_ao_subagentstop(estado, raiz):
    estado.mkdir(parents=True)
    (estado / "tarefa-corrente.json").write_text(json.dumps({"tarefa": "TLG-T9"}), encoding="utf-8")

    p1 = P(hook_event_name="PreToolUse", tool_name="Agent",
           tool_input={"subagent_type": "pantonic-executor", "prompt": "…"})
    rodar(p1, estado, raiz)

    (estado / "tarefa-corrente.json").unlink()

    p2 = P(hook_event_name="PostToolUse", tool_name="Agent",
           tool_input={"subagent_type": "pantonic-executor", "prompt": "…"},
           tool_response={
               "status": "completed",
               "agentId": "a1",
               "agentType": "pantonic-executor",
               "handback": "send",
               "content": [{"type": "text", "text": "ptr"}],
           })
    rodar(p2, estado, raiz)

    p3 = P(hook_event_name="UserPromptSubmit", prompt=(
        '<agent-message from="a1">\n'
        "x The report follows:\n"
        "  TLG-T9 review\n"
        "</agent-message>"
    ))
    rodar(p3, estado, raiz)

    p4 = P(hook_event_name="PreToolUse", tool_name="Agent",
           tool_input={"subagent_type": "pantonic-reviewer", "prompt": "…"})
    rodar(p4, estado, raiz)

    assert progresso(estado) == [
        'Agente executor recebe a tarefa "Um título de teste" e vai executar: Fazer x.',
        'Agente executor devolveu a tarefa "Um título de teste": review — sem pendência.',
        'Agente revisor recebe a tarefa "Um título de teste" e vai confrontar a entrega com o card.',
    ]
    estado_loop = json.loads((estado / progresso_hook.ESTADO_ARQ).read_text(encoding="utf-8"))
    assert estado_loop["tarefa"] == "TLG-T9"


# --- TF-GER-21 ------------------------------------------------------------------------


def test_tf_ger_21_evidencia_e_in_progress_alimentam_o_estado(estado, raiz):
    p1 = P(hook_event_name="PreToolUse", tool_name="Bash", tool_input={"command": (
        "python .claude/tools/review_evidence.py --plano docs/plans/P-9999-teste.md "
        "--tarefa TLG-T9 --desde abc --out x.md"
    )})
    rodar(p1, estado, raiz)

    p2 = P(hook_event_name="PreToolUse", tool_name="Agent",
           tool_input={"subagent_type": "pantonic-reviewer", "prompt": "…"})
    rodar(p2, estado, raiz)

    p3 = P(hook_event_name="PreToolUse", tool_name="Bash",
           tool_input={"command": "python .claude/tools/backlog.py status TLG-T10 in-progress"})
    rodar(p3, estado, raiz)

    p4 = P(hook_event_name="PreToolUse", tool_name="Agent",
           tool_input={"subagent_type": "pantonic-executor", "prompt": "…"})
    rodar(p4, estado, raiz)

    assert progresso(estado) == [
        'Tarefa "Um título de teste": vou reunir para o revisor o que mudou desde o despacho, '
        "os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.",
        'Agente revisor recebe a tarefa "Um título de teste" e vai confrontar a entrega com o card.',
        'Tarefa "Outro título": gates aprovados; vou materializar in-progress e gravar o ponto de partida.',
        'Agente executor recebe a tarefa "Outro título" e vai executar: Fazer y.',
    ]


# --- TF-GER-22 ------------------------------------------------------------------------


def test_tf_ger_22_comando_encadeado(estado, raiz):
    rodar(payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    ), estado, raiz)

    antes = len(progresso(estado))
    p1 = P(hook_event_name="PreToolUse", tool_name="Bash", tool_input={"command": (
        "python .claude/tools/backlog.py status TLG-T9 review && "
        "python .claude/tools/review_evidence.py --plano docs/plans/P-9999-teste.md "
        "--tarefa TLG-T9 --desde abc --out x.md"
    )})
    rodar(p1, estado, raiz)
    novas = progresso(estado)[antes:]
    assert novas == [
        'Tarefa "Um título de teste": vou reunir para o revisor o que mudou desde o despacho, '
        "os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit."
    ]

    antes2 = len(progresso(estado))
    p2 = P(hook_event_name="PreToolUse", tool_name="Bash", tool_input={"command": (
        "python .claude/tools/backlog.py status TLG-T9 in-progress; "
        "python .claude/tools/review_evidence.py --plano x --tarefa TLG-T9 --desde abc --atribuir"
    )})
    rodar(p2, estado, raiz)
    novas2 = progresso(estado)[antes2:]
    assert novas2 == [
        'Tarefa "Um título de teste": gates aprovados; vou materializar in-progress '
        "e gravar o ponto de partida.",
        'Tarefa "Um título de teste": vou medir a que arquivo a pendência é atribuível.',
    ]


# --- TF-GER-23 ------------------------------------------------------------------------


def test_tf_ger_23_janela_no_painel(estado, raiz):
    rodar(payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    ), estado, raiz)

    rodar(P(hook_event_name="Stop"), estado, raiz)

    rodar(P(hook_event_name="PreToolUse", tool_name="Bash",
            tool_input={"command": "python .claude/tools/backlog.py status TLG-T9 done"}), estado, raiz)

    rodar(P(hook_event_name="PreToolUse", tool_name="Bash",
            tool_input={"command": "python .claude/tools/modelo.py show --plano docs/plans/P-9999-teste.md"}),
          estado, raiz)

    rodar(P(hook_event_name="Stop"), estado, raiz)
    rodar(P(hook_event_name="Stop"), estado, raiz)

    rodar(payload_next(
        "=== PRÓXIMA TAREFA: TLG-T10 — Outro título [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer y.\n"
    ), estado, raiz)

    assert progresso(estado) == [
        'Abrindo a janela do plano "Plano de teste".',
        'Tarefa "Um título de teste". Passo: conferir os gates e preparar o despacho.',
        'Scrum master vai fechar a tarefa "Um título de teste" como done: registrar estado, '
        "RDO e telemetria.",
        "Scrum master mostrou o modelo do plano e aguarda; a resposta dele está na extensão.",
        'Scrum master concluiu a tarefa "Um título de teste" e vai pegar a tarefa "Outro título".',
        'Tarefa "Outro título". Passo: conferir os gates e preparar o despacho.',
    ]


# --- TF-GER-24 ------------------------------------------------------------------------


def test_tf_ger_24_estrategico_em_prosa_nao_e_estrategico(estado, raiz):
    assert _volta_consultor(
        estado, raiz,
        "rota=resolve\nDecisão: sem `estrategico=`, o impedimento é tático."
    ) == 'Agente consultor devolveu a tarefa "Um título de teste": rota resolve.'

    e2 = raiz / "estado_consultor2"
    e2.mkdir(parents=True)
    (e2 / progresso_hook.ESTADO_ARQ).write_text(
        json.dumps({"sessao": "s1", "tarefa": "TLG-T9", "titulo": "Um título de teste",
                    "pendentes": {"c1": "pantonic-consultant"}}),
        encoding="utf-8",
    )
    p = P(hook_event_name="UserPromptSubmit", prompt=(
        '<agent-message from="c1">\n'
        "[Subagent hand-back] The text below is the final report of a subagent this "
        "session delegated to. The report follows:\n"
        "  rota=resolve\n"
        "  - Decisão: sem `estrategico=`, o impedimento é tático.\n"
        "</agent-message>"
    ))
    rodar(p, e2, raiz)
    assert progresso(e2) == [
        'Agente consultor devolveu a tarefa "Um título de teste": rota resolve.'
    ]


# --- TF-GER-25 ------------------------------------------------------------------------


def test_tf_ger_25_show_no_meio_da_janela_nao_encerra(estado, raiz):
    n9 = (
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    )
    show = "python .claude/tools/modelo.py show --plano docs/plans/P-9999-teste.md"

    rodar(payload_next(n9), estado, raiz)

    rodar(P(hook_event_name="PreToolUse", tool_name="Bash",
            tool_input={"command": show + " --drift"}), estado, raiz)
    rodar(P(hook_event_name="Stop"), estado, raiz)

    rodar(P(hook_event_name="PreToolUse", tool_name="Agent",
            tool_input={"subagent_type": "pantonic-executor", "prompt": "…"}), estado, raiz)
    rodar(P(hook_event_name="PostToolUse", tool_name="Agent",
            tool_input={"subagent_type": "pantonic-executor"},
            tool_response={"status": "completed", "agentId": "a1", "agentType": "pantonic-executor",
                            "handback": "send", "content": [{"type": "text", "text": "ptr"}]}),
          estado, raiz)

    rodar(P(hook_event_name="UserPromptSubmit", prompt="mostre o modelo"), estado, raiz)
    rodar(P(hook_event_name="PreToolUse", tool_name="Bash",
            tool_input={"command": show}), estado, raiz)
    rodar(P(hook_event_name="Stop"), estado, raiz)

    rodar(P(hook_event_name="UserPromptSubmit", prompt=(
        '<agent-message from="a1">\n'
        "x The report follows:\n"
        "  TLG-T9 review\n"
        "</agent-message>"
    )), estado, raiz)

    rodar(P(hook_event_name="PreToolUse", tool_name="Agent",
            tool_input={"subagent_type": "pantonic-reviewer", "prompt": "…"}), estado, raiz)
    rodar(P(hook_event_name="PostToolUse", tool_name="Agent",
            tool_input={"subagent_type": "pantonic-reviewer"},
            tool_response={"status": "completed", "agentId": "r1", "agentType": "pantonic-reviewer",
                            "handback": "send", "content": [{"type": "text", "text": "ptr"}]}),
          estado, raiz)
    rodar(P(hook_event_name="Stop"), estado, raiz)

    rodar(P(hook_event_name="UserPromptSubmit", prompt=(
        '<agent-message from="r1">\n'
        "x The report follows:\n"
        "  TLG-T9 aprovado 100 bloqueante=nenhuma\n"
        "</agent-message>"
    )), estado, raiz)
    rodar(P(hook_event_name="Stop"), estado, raiz)

    rodar(P(hook_event_name="PreToolUse", tool_name="Bash",
            tool_input={"command": "python .claude/tools/backlog.py status TLG-T9 done"}), estado, raiz)

    rodar(payload_next("nada delegável"), estado, raiz)
    rodar(P(hook_event_name="PreToolUse", tool_name="Bash",
            tool_input={"command": show}), estado, raiz)
    rodar(P(hook_event_name="Stop"), estado, raiz)

    n17 = "Scrum master mostrou o modelo do plano e aguarda; a resposta dele está na extensão."
    assert progresso(estado) == [
        'Abrindo a janela do plano "Plano de teste".',
        'Tarefa "Um título de teste". Passo: conferir os gates e preparar o despacho.',
        'Agente executor recebe a tarefa "Um título de teste" e vai executar: Fazer x.',
        n17,
        'Agente executor devolveu a tarefa "Um título de teste": review — sem pendência.',
        'Agente revisor recebe a tarefa "Um título de teste" e vai confrontar a entrega com o card.',
        'Agente revisor devolveu a tarefa "Um título de teste": aprovado 100%, bloqueante nenhuma, recomendação não informada.',
        'Scrum master vai fechar a tarefa "Um título de teste" como done: registrar estado, '
        "RDO e telemetria.",
        'Scrum master concluiu a tarefa "Um título de teste"; nada delegável na fila. '
        "Encerrando a janela com o relatório.",
        n17,
    ]


# --- TF-GER-26 ------------------------------------------------------------------------


def test_tf_ger_26_entrada_orfa_nao_apaga_a_m17_real(estado, raiz):
    show = "python .claude/tools/modelo.py show --plano docs/plans/P-9999-teste.md"
    estado.mkdir(parents=True)
    (estado / progresso_hook.ESTADO_ARQ).write_text(
        json.dumps({
            "sessao": "s1",
            "aberta": True,
            "tarefa": "TLG-T9",
            "titulo": "Um título de teste",
            "pendentes": {"x1": "pantonic-consultant"},
        }),
        encoding="utf-8",
    )

    rodar(payload_next("nada delegável"), estado, raiz)
    rodar(P(hook_event_name="PreToolUse", tool_name="Bash",
            tool_input={"command": show}), estado, raiz)
    rodar(P(hook_event_name="Stop"), estado, raiz)

    assert progresso(estado) == [
        'Scrum master não encontrou tarefa delegável na fila. Encerrando a janela com o relatório.',
        'Scrum master mostrou o modelo do plano e aguarda; a resposta dele está na extensão.',
    ]


# --- TF-GER-27 ------------------------------------------------------------------------


def test_tf_ger_27_show_puro_no_meio_da_janela(estado, raiz):
    n9 = (
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    )
    show = "python .claude/tools/modelo.py show --plano docs/plans/P-9999-teste.md"
    n17 = "Scrum master mostrou o modelo do plano e aguarda; a resposta dele está na extensão."

    rodar(payload_next(n9), estado, raiz)

    rodar(P(hook_event_name="PreToolUse", tool_name="Bash",
            tool_input={"command": show}), estado, raiz)
    rodar(P(hook_event_name="Stop"), estado, raiz)

    rodar(P(hook_event_name="PreToolUse", tool_name="Agent",
            tool_input={"subagent_type": "pantonic-executor", "prompt": "…"}), estado, raiz)
    rodar(P(hook_event_name="PostToolUse", tool_name="Agent",
            tool_input={"subagent_type": "pantonic-executor"},
            tool_response={"status": "completed", "agentId": "a1", "agentType": "pantonic-executor",
                            "handback": "send", "content": [{"type": "text", "text": "ptr"}]}),
          estado, raiz)
    rodar(P(hook_event_name="Stop"), estado, raiz)

    rodar(P(hook_event_name="UserPromptSubmit", prompt=(
        '<agent-message from="a1">\n'
        "x The report follows:\n"
        "  TLG-T9 review\n"
        "</agent-message>"
    )), estado, raiz)

    rodar(P(hook_event_name="PreToolUse", tool_name="Bash",
            tool_input={"command": "python .claude/tools/backlog.py status TLG-T9 done"}), estado, raiz)

    rodar(payload_next("nada delegável"), estado, raiz)
    rodar(P(hook_event_name="PreToolUse", tool_name="Bash",
            tool_input={"command": show}), estado, raiz)
    rodar(P(hook_event_name="Stop"), estado, raiz)

    assert progresso(estado) == [
        'Abrindo a janela do plano "Plano de teste".',
        'Tarefa "Um título de teste". Passo: conferir os gates e preparar o despacho.',
        n17,
        'Agente executor recebe a tarefa "Um título de teste" e vai executar: Fazer x.',
        'Agente executor devolveu a tarefa "Um título de teste": review — sem pendência.',
        'Scrum master vai fechar a tarefa "Um título de teste" como done: registrar estado, '
        "RDO e telemetria.",
        'Scrum master concluiu a tarefa "Um título de teste"; nada delegável na fila. '
        "Encerrando a janela com o relatório.",
        n17,
    ]
    estado_loop = json.loads((estado / progresso_hook.ESTADO_ARQ).read_text(encoding="utf-8"))
    assert estado_loop["aberta"] is True


# --- TF-GER-28 ------------------------------------------------------------------------


def test_tf_ger_28_agente_caido_e_parada_sem_next(estado, raiz):
    n9 = (
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    )
    show = "python .claude/tools/modelo.py show --plano docs/plans/P-9999-teste.md"
    n17 = "Scrum master mostrou o modelo do plano e aguarda; a resposta dele está na extensão."

    def despachar(sub, agent_id):
        rodar(P(hook_event_name="PreToolUse", tool_name="Agent",
                tool_input={"subagent_type": sub, "prompt": "…"}), estado, raiz)
        rodar(P(hook_event_name="PostToolUse", tool_name="Agent",
                tool_input={"subagent_type": sub},
                tool_response={"status": "completed", "agentId": agent_id, "agentType": sub,
                                "handback": "send", "content": [{"type": "text", "text": "ptr"}]}),
              estado, raiz)

    def hand_back(agent_id, corpo):
        rodar(P(hook_event_name="UserPromptSubmit", prompt=(
            f'<agent-message from="{agent_id}">\n'
            "x The report follows:\n"
            f"  {corpo}\n"
            "</agent-message>"
        )), estado, raiz)

    rodar(payload_next(n9), estado, raiz)

    despachar("pantonic-executor", "a1")
    rodar(P(hook_event_name="Stop"), estado, raiz)

    despachar("pantonic-executor", "a2")
    rodar(P(hook_event_name="Stop"), estado, raiz)

    hand_back("a2", "TLG-T9 review")

    despachar("pantonic-reviewer", "r1")
    rodar(P(hook_event_name="Stop"), estado, raiz)

    hand_back("r1", "TLG-T9 aprovado 100 bloqueante=nenhuma")

    rodar(P(hook_event_name="PreToolUse", tool_name="Bash",
            tool_input={"command": "python .claude/tools/backlog.py status TLG-T9 done"}), estado, raiz)
    rodar(P(hook_event_name="PreToolUse", tool_name="Bash",
            tool_input={"command": show}), estado, raiz)
    rodar(P(hook_event_name="Stop"), estado, raiz)

    linhas = progresso(estado)
    assert len(linhas) == 9
    assert linhas[-1] == n17
    estado_loop = json.loads((estado / progresso_hook.ESTADO_ARQ).read_text(encoding="utf-8"))
    assert estado_loop["pendentes"] == {"a1": "pantonic-executor"}


# --- TF-GER-29 ------------------------------------------------------------------------


def test_tf_ger_29_tarefa_parada_nao_e_tarefa_concluida(estado, raiz):
    n9 = (
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    )
    n10t = (
        "=== PRÓXIMA TAREFA: TLG-T10 — Outro título [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer y.\n"
    )

    rodar(payload_next(n9), estado, raiz)
    rodar(P(hook_event_name="PreToolUse", tool_name="Bash",
            tool_input={"command": "python .claude/tools/backlog.py status TLG-T9 blocked"}), estado, raiz)
    rodar(payload_next(n10t), estado, raiz)
    rodar(P(hook_event_name="PreToolUse", tool_name="Bash",
            tool_input={"command": "python .claude/tools/backlog.py status TLG-T10 cancelled"}), estado, raiz)
    rodar(payload_next("nada delegável"), estado, raiz)

    assert progresso(estado) == [
        'Abrindo a janela do plano "Plano de teste".',
        'Tarefa "Um título de teste". Passo: conferir os gates e preparar o despacho.',
        'Scrum master vai marcar a tarefa "Um título de teste" como blocked, sem RDO.',
        'Tarefa "Outro título". Passo: conferir os gates e preparar o despacho.',
        'Scrum master vai marcar a tarefa "Outro título" como cancelled, sem RDO.',
        'Scrum master não encontrou tarefa delegável na fila. Encerrando a janela com o relatório.',
    ]
    estado_loop = json.loads((estado / progresso_hook.ESTADO_ARQ).read_text(encoding="utf-8"))
    assert "tarefa_fechada" not in estado_loop


# --- TF-CAP-1..3 (de TLG-T3a, mantidos) ------------------------------------------------


def test_tf_cap_1_flag_ligado(tmp_path):
    estado = tmp_path / "estado"
    estado.mkdir(parents=True)
    (estado / "progresso-captura.on").touch()
    payload = {
        "hook_event_name": "PostToolUse",
        "tool_name": "Bash",
        "tool_input": {"command": "python x.py"},
        "tool_response": {"stdout": "x"},
        "transcript_path": str(tmp_path / "t.jsonl"),
        "session_id": "s1",
    }

    assert progresso_hook.main(entrada=json.dumps(payload), estado=estado) == 0

    captura = estado / "progresso-captura.jsonl"
    assert captura.exists()
    linhas = captura.read_text(encoding="utf-8").splitlines()
    assert len(linhas) == 1
    registro = json.loads(linhas[0])
    assert registro["evento"] == "PostToolUse"
    assert registro["tool"] == "Bash"
    assert registro["input_chaves"] == ["command"]
    assert registro["command"] == "python x.py"
    assert registro["response_tipo"] == "dict"
    assert registro["response_chaves"] == ["stdout"]
    assert registro["response"] == '{"stdout": "x"}'


def test_tf_cap_2_flag_desligado(tmp_path):
    estado = tmp_path / "estado"
    payload = {
        "hook_event_name": "PostToolUse",
        "tool_name": "Bash",
        "tool_input": {"command": "python x.py"},
        "tool_response": {"stdout": "x"},
        "transcript_path": str(tmp_path / "t.jsonl"),
        "session_id": "s1",
    }

    assert progresso_hook.main(entrada=json.dumps(payload), estado=estado) == 0

    assert not (estado / "progresso-captura.jsonl").exists()


# --- TF-GER-30 ----------------------------------------------------------------------


def test_tf_ger_30_dois_status_no_mesmo_comando(estado, raiz):
    rodar(payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    ), estado, raiz)

    antes = len(progresso(estado))
    p1 = P(hook_event_name="PreToolUse", tool_name="Bash", tool_input={"command": (
        "python .claude/tools/backlog.py status TLG-T9 done && "
        "python .claude/tools/backlog.py status TLG-T10 in-progress"
    )})
    rodar(p1, estado, raiz)
    assert progresso(estado)[antes:] == [
        'Scrum master vai fechar a tarefa "Um título de teste" como done: registrar estado, RDO e telemetria.',
        'Tarefa "Outro título": gates aprovados; vou materializar in-progress e gravar o ponto de partida.',
    ]


def test_tf_san_18_titulo_do_plano_em_pasta(tmp_path):
    pasta = tmp_path / "docs" / "plans" / "P-0-gama"
    pasta.mkdir(parents=True)
    (pasta / "plano.md").write_text(
        "# P-0 — Plano gama\n"
        "\n"
        "## 5. Tarefas\n"
        "\n"
        "### GAM-T1 — Primeira [Sonnet · classe implementacao]\n"
        "- **Objetivo:** fixture.\n",
        encoding="utf-8",
    )

    assert progresso_hook.localizar_card("GAM-T1", tmp_path) == ("Primeira", "fixture.", "Plano gama")


def test_tf_cap_3_barreira_agent_type(tmp_path):
    estado = tmp_path / "estado"
    payload = {
        "hook_event_name": "PostToolUse",
        "tool_name": "Bash",
        "tool_input": {"command": "python x.py"},
        "tool_response": {"stdout": "x"},
        "transcript_path": str(tmp_path / "t.jsonl"),
        "session_id": "s1",
        "agent_type": "pantonic-executor",
    }

    assert progresso_hook.main(entrada=json.dumps(payload), estado=estado) == 0

    assert not (estado / "progresso-captura.jsonl").exists()
    assert not estado.exists()


# --- TK-88 — o fechamento por instrumento chega ao painel --------------------------------------


def test_tf_tk88_encerrar_tarefa_gera_m10_e_encerrar_plano_gera_m18(estado, raiz):
    """TF do `TK-88`: `encerrar.py tarefa --tarefa <ID>` materializa o `done` em processo, sem
    `backlog.py status` na linha — a `M-10` sai da detecção do instrumento, com `tarefa_fechada`
    no estado; `encerrar.py plano --plano <caminho>` gera a `M-18` com o título do plano."""
    rodar(payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    ), estado, raiz)

    p_tarefa = P(
        hook_event_name="PreToolUse", tool_name="Bash",
        tool_input={"command": "python .claude/tools/encerrar.py tarefa --plano docs/plans/P-9999-teste.md --tarefa TLG-T9 --resumo 'x'"},
    )
    assert rodar(p_tarefa, estado, raiz) == 0
    assert progresso(estado)[-1] == (
        'Scrum master vai fechar a tarefa "Um título de teste" como done: registrar '
        "estado, RDO e telemetria."
    )
    assert json.loads((estado / progresso_hook.ESTADO_ARQ).read_text(encoding="utf-8"))["tarefa_fechada"] == "TLG-T9"

    p_plano = P(
        hook_event_name="PreToolUse", tool_name="Bash",
        tool_input={"command": 'python .claude/tools/encerrar.py plano --plano docs/plans/P-9999-teste.md --veredito "pode fechar"'},
    )
    assert rodar(p_plano, estado, raiz) == 0
    assert progresso(estado)[-1] == (
        'Scrum master vai fechar o plano "Plano de teste": registrar estado, relatório de entrega e a linha do diário.'
    )


# --- TK-88c: leitura por invocação, não por substring no comando inteiro ----------------


def test_tf_m10_da_propria_invocacao_em_comando_encadeado(estado, raiz):
    """TF do `TK-88c`: num comando encadeado, o `--tarefa` de uma invocação anterior
    (`telemetria.py append --tarefa X-revisao`) não vaza para a `M-10` de
    `encerrar.py tarefa` — o título e o `tarefa_fechada` saem do `--tarefa` da própria
    invocação de `encerrar.py tarefa` (`X`), não do `-revisao` de outro comando da linha
    (defeito reproduzido pelo revisor com `FPU-T8`)."""
    rodar(payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    ), estado, raiz)

    p = P(hook_event_name="PreToolUse", tool_name="Bash", tool_input={"command": (
        "python .claude/tools/telemetria.py append --tarefa TLG-T9-revisao --resumo x; "
        "python .claude/tools/encerrar.py tarefa --plano docs/plans/P-9999-teste.md --tarefa TLG-T9"
    )})
    assert rodar(p, estado, raiz) == 0
    assert progresso(estado)[-1] == (
        'Scrum master vai fechar a tarefa "Um título de teste" como done: registrar '
        "estado, RDO e telemetria."
    )
    assert json.loads((estado / progresso_hook.ESTADO_ARQ).read_text(encoding="utf-8"))["tarefa_fechada"] == "TLG-T9"


def test_tr_literal_em_argumento_nao_e_propria_invocacao(estado, raiz):
    """TR do `TK-88c`: o script citado dentro de um argumento — mensagem de commit,
    `--resumo` — não é a própria invocação, e não gera frase."""
    rodar(payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    ), estado, raiz)

    antes = len(progresso(estado))
    p1 = P(hook_event_name="PreToolUse", tool_name="Bash", tool_input={"command": (
        'git commit -m "ajusta o encerrar.py plano --plano docs/plans/P-9999-teste.md"'
    )})
    assert rodar(p1, estado, raiz) == 0
    assert progresso(estado)[antes:] == []

    p2 = P(hook_event_name="PreToolUse", tool_name="Bash", tool_input={"command": (
        'python .claude/tools/telemetria.py append --resumo "encerrar.py tarefa --tarefa TLG-T10"'
    )})
    assert rodar(p2, estado, raiz) == 0
    assert progresso(estado)[antes:] == []


def test_tf_review_evidence_da_propria_invocacao(estado, raiz):
    """TF do `TK-88c`: o `--tarefa` de um comando anterior na linha não muda o título da
    `M-5` — quem manda é o `--tarefa` da própria invocação de `review_evidence.py`."""
    rodar(payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    ), estado, raiz)

    antes = len(progresso(estado))
    p = P(hook_event_name="PreToolUse", tool_name="Bash", tool_input={"command": (
        "python .claude/tools/backlog.py status TLG-T10 in-progress; "
        "python .claude/tools/review_evidence.py --plano docs/plans/P-9999-teste.md "
        "--tarefa TLG-T9 --desde abc --out x.md"
    )})
    assert rodar(p, estado, raiz) == 0
    novas = progresso(estado)[antes:]
    assert novas == [
        'Tarefa "Outro título": gates aprovados; vou materializar in-progress e gravar o ponto de partida.',
        'Tarefa "Um título de teste": vou reunir para o revisor o que mudou desde o despacho, '
        "os arquivos tocados fora do previsto e o resultado dos testes e guardas do kit.",
    ]


# --- AF-T3: o painel reconhece o programa depois das opções do interpretador -----------


def test_tf_opcao_do_interpretador_com_valor_gera_m2(estado, raiz):
    rodar(payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    ), estado, raiz)

    p_in_progress = P(
        hook_event_name="PreToolUse", tool_name="Bash",
        tool_input={"command": "python -X utf8 .claude/tools/backlog.py status TLG-T9 in-progress"},
    )
    assert rodar(p_in_progress, estado, raiz) == 0
    assert progresso(estado)[-1] == (
        'Tarefa "Um título de teste": gates aprovados; vou materializar in-progress '
        "e gravar o ponto de partida."
    )


def test_tr_opcao_do_interpretador_sem_valor_segue_gerando_m2(estado, raiz):
    rodar(payload_next(
        "=== PRÓXIMA TAREFA: TLG-T9 — Um título de teste [Sonnet · classe redacao]\n"
        "- **Objetivo:** Fazer x.\n"
    ), estado, raiz)

    p_in_progress = P(
        hook_event_name="PreToolUse", tool_name="Bash",
        tool_input={"command": "python -u .claude/tools/backlog.py status TLG-T9 in-progress"},
    )
    assert rodar(p_in_progress, estado, raiz) == 0
    assert progresso(estado)[-1] == (
        'Tarefa "Um título de teste": gates aprovados; vou materializar in-progress '
        "e gravar o ponto de partida."
    )


def test_tf_opcao_do_interpretador_m_e_c():
    assert progresso_hook._programa(["python", "-m", "pytest", "-q"]) == ("pytest", ["-q"])
    assert progresso_hook._programa(["python", "-c", "print(1)"]) is None
