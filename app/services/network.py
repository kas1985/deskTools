from __future__ import annotations

import socket

import psutil

from app.services.formatting import bytes_to_human
from app.services.system import run_command


def network_snapshot() -> dict[str, str]:
    counters = psutil.net_io_counters()
    addrs = psutil.net_if_addrs()
    active = []
    for name, values in addrs.items():
        for addr in values:
            if addr.family == socket.AF_INET and not addr.address.startswith("127."):
                active.append(f"{name}: {addr.address}")
    return {
        "sent": bytes_to_human(counters.bytes_sent),
        "received": bytes_to_human(counters.bytes_recv),
        "interfaces": "\n".join(active[:5]) or "Sin interfaces activas",
    }


def ping_host(host: str) -> str:
    target = host.strip()
    if not target:
        return "Introduce un host o IP."
    ok, output = run_command(["ping", "-n", "4", target], timeout=15)
    return output if ok else f"No se pudo completar el ping:\n{output}"
