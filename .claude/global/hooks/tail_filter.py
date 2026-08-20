"""Filtro de cauda para comandos verbosos (builds, instalacoes).

Le stdin integral, grava em %TEMP%\\claude\\<nome-do-log> e imprime apenas as
ultimas N linhas precedidas de um cabecalho com o caminho do log completo.
Uso (gerado pelo hook verbose_cmd_pretooluse.py):

    comando 2>&1 | python tail_filter.py [nome-do-log] [n-linhas]

Observacao: num pipeline o exit code visto pelo agente e o deste filtro (0);
o sucesso/falha do comando deve ser avaliado pelo texto da cauda. Para depurar,
Grep no log completo — nunca Read integral.
"""
import os
import sys


def main() -> None:
    log_name = sys.argv[1] if len(sys.argv) > 1 else "verbose_last_run.log"
    tail_n = int(sys.argv[2]) if len(sys.argv) > 2 else 40

    log_dir = os.path.join(
        os.environ.get("TEMP") or os.environ.get("TMP") or ".", "claude"
    )
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, log_name)

    data = sys.stdin.buffer.read()
    with open(log_path, "wb") as f:
        f.write(data)

    lines = data.decode("utf-8", errors="replace").splitlines()
    shown = lines[-tail_n:]
    print(
        f"[saida filtrada: ultimas {len(shown)} de {len(lines)} linhas; "
        f"log completo: {log_path}]"
    )
    for line in shown:
        print(line)


if __name__ == "__main__":
    main()
