from __future__ import annotations

import os
import tempfile
from pathlib import Path

import psutil

from app.services.formatting import bytes_to_human


def folder_size(path: Path, limit: int = 20000) -> int:
    total = 0
    count = 0
    for root, _, files in os.walk(path):
        for filename in files:
            try:
                total += (Path(root) / filename).stat().st_size
            except OSError:
                pass
            count += 1
            if count >= limit:
                return total
    return total


def storage_snapshot() -> dict[str, str]:
    home = Path.home()
    disk = psutil.disk_usage(home.anchor or home)
    temp_path = Path(tempfile.gettempdir())
    downloads = home / "Downloads"
    return {
        "disk": f"{bytes_to_human(disk.used)} / {bytes_to_human(disk.total)}",
        "disk_percent": f"{disk.percent:.0f}%",
        "temp_path": str(temp_path),
        "temp_size": bytes_to_human(folder_size(temp_path)),
        "downloads_size": bytes_to_human(folder_size(downloads)) if downloads.exists() else "No encontrado",
    }


def clean_user_temp() -> str:
    temp_path = Path(tempfile.gettempdir())
    removed = 0
    freed = 0
    for item in temp_path.iterdir():
        try:
            if item.is_file() or item.is_symlink():
                size = item.stat().st_size
                item.unlink()
                freed += size
                removed += 1
        except OSError:
            continue
    return f"Eliminados {removed} archivos temporales. Liberado: {bytes_to_human(freed)}."
