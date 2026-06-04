from __future__ import annotations

import os

from app.services.system import run_command

if os.name == "nt":
    import winreg
else:
    winreg = None


def current_power_plan() -> str:
    ok, output = run_command(["powercfg", "/GETACTIVESCHEME"])
    return output if ok else f"No disponible: {output}"


def set_power_plan(plan_alias: str) -> str:
    ok, output = run_command(["powercfg", "/SETACTIVE", plan_alias])
    if ok:
        return "Plan de energia actualizado."
    return f"No se pudo cambiar el plan: {output}"


def game_mode_enabled() -> bool:
    if winreg is None:
        return False
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\GameBar") as key:
            value, _ = winreg.QueryValueEx(key, "AllowAutoGameMode")
            return int(value) == 1
    except OSError:
        return False


def set_game_mode(enabled: bool) -> str:
    if winreg is None:
        return "Modo juego solo esta disponible en Windows."
    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\GameBar") as key:
        winreg.SetValueEx(key, "AllowAutoGameMode", 0, winreg.REG_DWORD, 1 if enabled else 0)
    return "Modo juego habilitado." if enabled else "Modo juego deshabilitado."


def performance_checks() -> list[tuple[str, str]]:
    return [
        ("Plan activo", current_power_plan()),
        ("Modo juego", "Activado" if game_mode_enabled() else "Desactivado"),
        ("Plataforma", os.name),
    ]
