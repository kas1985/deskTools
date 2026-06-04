from __future__ import annotations

import os
import platform
import socket
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path

import psutil

from app.services.formatting import bytes_to_human, seconds_to_human


@dataclass(frozen=True)
class ProcessInfo:
    pid: int
    name: str
    cpu: float
    memory: float
    status: str


def resource_snapshot() -> dict[str, object]:
    cpu = psutil.cpu_percent(interval=0.15)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage(Path.home().anchor or os.getcwd())
    net = psutil.net_io_counters()
    uptime = time.time() - psutil.boot_time()
    return {
        "cpu": cpu,
        "memory_percent": memory.percent,
        "memory_used": bytes_to_human(memory.used),
        "memory_total": bytes_to_human(memory.total),
        "disk_percent": disk.percent,
        "disk_used": bytes_to_human(disk.used),
        "disk_total": bytes_to_human(disk.total),
        "net_sent": bytes_to_human(net.bytes_sent),
        "net_recv": bytes_to_human(net.bytes_recv),
        "uptime": seconds_to_human(uptime),
        "host": socket.gethostname(),
        "system": f"{platform.system()} {platform.release()}",
    }


def top_processes(limit: int = 12) -> list[ProcessInfo]:
    items: list[ProcessInfo] = []
    for proc in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent", "status"]):
        try:
            info = proc.info
            items.append(
                ProcessInfo(
                    pid=int(info["pid"]),
                    name=str(info.get("name") or "Sin nombre"),
                    cpu=float(info.get("cpu_percent") or 0),
                    memory=float(info.get("memory_percent") or 0),
                    status=str(info.get("status") or ""),
                )
            )
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return sorted(items, key=lambda item: (item.cpu, item.memory), reverse=True)[:limit]


def terminate_process(pid: int) -> str:
    proc = psutil.Process(pid)
    name = proc.name()
    proc.terminate()
    return f"Solicitud de cierre enviada a {name} ({pid})."


def run_command(args: list[str], timeout: int = 12) -> tuple[bool, str]:
    try:
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
            creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0,
        )
    except FileNotFoundError:
        return False, f"No se encontro el comando: {args[0]}"
    except subprocess.TimeoutExpired:
        return False, "El comando tardo demasiado y fue cancelado."

    output = (result.stdout or result.stderr or "").strip()
    return result.returncode == 0, output or "Comando ejecutado."
