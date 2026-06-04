from __future__ import annotations


def bytes_to_human(value: int | float) -> str:
    size = float(value)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024 or unit == "TB":
            return f"{size:.1f} {unit}" if unit != "B" else f"{int(size)} B"
        size /= 1024
    return f"{size:.1f} TB"


def seconds_to_human(seconds: int | float) -> str:
    total = int(seconds)
    hours, remainder = divmod(total, 3600)
    minutes, _ = divmod(remainder, 60)
    if hours:
        return f"{hours} h {minutes} min"
    return f"{minutes} min"
