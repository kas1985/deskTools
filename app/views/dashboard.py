import flet as ft

from app.components import activity_item, info_row, metric_card, panel, progress_line, section_title
from app.services.system import resource_snapshot, top_processes
from app.theme import ACCENT, MUTED, SOFT_AMBER, SOFT_BLUE, SOFT_GREEN, SOFT_PINK


def dashboard_view(page: ft.Page) -> ft.Column:
    snapshot = resource_snapshot()
    processes = top_processes(5)
    return ft.Column(
        expand=True,
        spacing=18,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            section_title("Resumen del sistema", "Estado general del equipo en tiempo real."),
            ft.Row(
                spacing=14,
                controls=[
                    metric_card("CPU", f"{snapshot['cpu']:.0f}%", ft.Icons.MEMORY, SOFT_BLUE),
                    metric_card("Memoria", f"{snapshot['memory_percent']:.0f}%", ft.Icons.SPEED, SOFT_GREEN),
                    metric_card("Disco", f"{snapshot['disk_percent']:.0f}%", ft.Icons.STORAGE, SOFT_AMBER),
                    metric_card("Uptime", str(snapshot["uptime"]), ft.Icons.TIMER_OUTLINED, SOFT_PINK),
                ],
            ),
            ft.Row(
                spacing=18,
                vertical_alignment=ft.CrossAxisAlignment.START,
                controls=[
                    panel(
                        "Recursos",
                        [
                            progress_line("CPU", float(snapshot["cpu"]) / 100, ACCENT),
                            progress_line("Memoria", float(snapshot["memory_percent"]) / 100, "#27AE60"),
                            progress_line("Disco", float(snapshot["disk_percent"]) / 100, "#F2A541"),
                            info_row("Memoria usada", f"{snapshot['memory_used']} / {snapshot['memory_total']}"),
                            info_row("Disco usado", f"{snapshot['disk_used']} / {snapshot['disk_total']}"),
                        ],
                        expand=True,
                    ),
                    panel(
                        "Procesos con mas actividad",
                        [
                            activity_item(
                                item.name,
                                f"PID {item.pid} - CPU {item.cpu:.1f}% - RAM {item.memory:.1f}%",
                                item.status or "activo",
                                "#2F80ED",
                            )
                            for item in processes
                        ],
                        expand=True,
                    ),
                ],
            ),
            panel(
                "Equipo",
                [
                    info_row("Host", str(snapshot["host"]), ft.Icons.COMPUTER),
                    info_row("Sistema", str(snapshot["system"]), ft.Icons.WINDOW),
                    info_row("Datos enviados", str(snapshot["net_sent"]), ft.Icons.UPLOAD),
                    info_row("Datos recibidos", str(snapshot["net_recv"]), ft.Icons.DOWNLOAD),
                ],
            ),
        ],
    )
