#!/usr/bin/env python3
"""Convierte firebase-config.json en config.dat (JSON codificado en base64).

Uso:
    python3 config_a_base64.py                      # firebase-config.json -> config.dat
    python3 config_a_base64.py entrada.json salida.dat
    python3 config_a_base64.py --decode             # config.dat -> JSON por pantalla (para comprobar)

Nota: base64 es una codificación, no cifrado. Solo evita que las credenciales
se lean a simple vista o las indexen buscadores de texto.
"""
import base64
import json
import sys
from pathlib import Path


def main(argv):
    if argv and argv[0] == "--decode":
        src = Path(argv[1] if len(argv) > 1 else "config.dat")
        print(base64.b64decode(src.read_text().strip()).decode("utf-8"))
        return 0

    src = Path(argv[0] if argv else "firebase-config.json")
    dst = Path(argv[1] if len(argv) > 1 else "config.dat")

    if not src.exists():
        print(f"No existe {src}", file=sys.stderr)
        return 1
    try:
        cfg = json.loads(src.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"{src} no es un JSON válido: {e}", file=sys.stderr)
        return 1

    faltan = [k for k in ("apiKey", "databaseURL") if k not in cfg]
    if faltan:
        print(f"Aviso: faltan campos habituales: {', '.join(faltan)}", file=sys.stderr)

    compact = json.dumps(cfg, ensure_ascii=False, separators=(",", ":"))
    dst.write_text(base64.b64encode(compact.encode("utf-8")).decode("ascii") + "\n")
    print(f"{src} -> {dst} ({dst.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
