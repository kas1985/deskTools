from __future__ import annotations

from pathlib import Path
from urllib.parse import urlparse

import yt_dlp


def validate_video_request(url: str, output_dir: str) -> tuple[bool, str]:
    parsed = urlparse(url.strip())
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return False, "Introduce una URL http o https valida."
    folder = Path(output_dir).expanduser()
    if not folder.exists() or not folder.is_dir():
        return False, "La carpeta de destino no existe."
    return True, ""


def download_video(url: str, output_dir: str) -> str:
    ok, message = validate_video_request(url, output_dir)
    if not ok:
        return message

    target = Path(output_dir).expanduser()
    options = {
        "outtmpl": str(target / "%(title).180s.%(ext)s"),
        "format": "best",
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
    }
    with yt_dlp.YoutubeDL(options) as downloader:
        info = downloader.extract_info(url.strip(), download=True)

    title = info.get("title", "video") if isinstance(info, dict) else "video"
    return f"Descarga completada: {title}"
