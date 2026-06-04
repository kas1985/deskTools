import flet as ft

from app.theme import ACCENT, INK, MUTED, PANEL


def section_title(title: str, subtitle: str) -> ft.Column:
    return ft.Column(
        spacing=4,
        controls=[
            ft.Text(title, size=24, weight=ft.FontWeight.W_700, color=INK),
            ft.Text(subtitle, size=13, color=MUTED),
        ],
    )


def nav_destination(label: str, icon: str, selected_icon: str) -> ft.NavigationRailDestination:
    return ft.NavigationRailDestination(
        icon=ft.Icon(icon, color=MUTED),
        selected_icon=ft.Icon(selected_icon, color=ACCENT),
        label=label,
    )


def metric_card(label: str, value: str, icon: str, color: str) -> ft.Container:
    return ft.Container(
        expand=True,
        padding=18,
        border_radius=8,
        bgcolor=PANEL,
        shadow=ft.BoxShadow(
            blur_radius=18,
            color="#14000000",
            offset=ft.Offset(0, 8),
        ),
        content=ft.Column(
            spacing=14,
            controls=[
                ft.Container(
                    width=44,
                    height=44,
                    border_radius=8,
                    bgcolor=color,
                    alignment=ft.Alignment.CENTER,
                    content=ft.Icon(icon, color=ACCENT, size=24),
                ),
                ft.Column(
                    spacing=3,
                    controls=[
                        ft.Text(value, size=24, weight=ft.FontWeight.W_700, color=INK),
                        ft.Text(label, size=12, color=MUTED),
                    ],
                ),
            ],
        ),
    )


def action_button(label: str, icon: str, on_click, filled: bool = False) -> ft.Control:
    if filled:
        return ft.ElevatedButton(
            label,
            icon=icon,
            bgcolor=ACCENT,
            color="#FFFFFF",
            on_click=on_click,
        )
    return ft.OutlinedButton(label, icon=icon, on_click=on_click)


def activity_item(title: str, detail: str, tag: str, color: str) -> ft.Container:
    return ft.Container(
        padding=14,
        border=ft.Border.only(bottom=ft.BorderSide(1, "#EEF1F6")),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row(
                    spacing=12,
                    controls=[
                        ft.Container(width=10, height=10, border_radius=5, bgcolor=color),
                        ft.Column(
                            spacing=2,
                            controls=[
                                ft.Text(title, size=14, weight=ft.FontWeight.W_600, color=INK),
                                ft.Text(detail, size=12, color=MUTED),
                            ],
                        ),
                    ],
                ),
                ft.Container(
                    padding=ft.Padding.symmetric(horizontal=10, vertical=5),
                    border_radius=6,
                    bgcolor="#F2F5FA",
                    content=ft.Text(tag, size=11, color=MUTED),
                ),
            ],
        ),
    )


def info_row(label: str, value: str, icon: str | None = None) -> ft.Container:
    leading = []
    if icon:
        leading.append(ft.Icon(icon, color=ACCENT, size=20))

    return ft.Container(
        padding=ft.Padding.symmetric(horizontal=4, vertical=6),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row(
                    spacing=10,
                    controls=[
                        *leading,
                        ft.Text(label, size=13, color=MUTED),
                    ],
                ),
                ft.Text(value, size=13, weight=ft.FontWeight.W_600, color=INK),
            ],
        ),
    )


def panel(title: str, controls: list[ft.Control], expand: bool = False) -> ft.Container:
    return ft.Container(
        expand=expand,
        padding=18,
        border_radius=8,
        bgcolor=PANEL,
        shadow=ft.BoxShadow(
            blur_radius=18,
            color="#12000000",
            offset=ft.Offset(0, 8),
        ),
        content=ft.Column(
            spacing=14,
            controls=[
                ft.Text(title, size=16, weight=ft.FontWeight.W_700, color=INK),
                *controls,
            ],
        ),
    )


def progress_line(label: str, value: float, color: str) -> ft.Column:
    normalized = max(0, min(value, 1))
    return ft.Column(
        spacing=6,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text(label, size=12, color=MUTED),
                    ft.Text(
                        f"{int(normalized * 100)}%",
                        size=12,
                        weight=ft.FontWeight.W_600,
                        color=INK,
                    ),
                ],
            ),
            ft.ProgressBar(value=normalized, color=color, bgcolor="#EDF1F7", height=7),
        ],
    )
