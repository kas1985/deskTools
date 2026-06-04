import flet as ft

from app.components import nav_destination
from app.config import APP_VERSION_LABEL
from app.data import NAV_ITEMS
from app.theme import ACCENT, BG, INK, MUTED, PANEL, SOFT_BLUE
from app.views import VIEWS, dashboard_view


def build_sidebar(rail: ft.NavigationRail) -> ft.Container:
    return ft.Container(
        width=240,
        bgcolor=PANEL,
        padding=ft.Padding.only(top=24, bottom=24),
        content=ft.Column(
            expand=True,
            spacing=20,
            controls=[
                ft.Container(
                    padding=ft.Padding.symmetric(horizontal=24),
                    content=ft.Row(
                        spacing=12,
                        controls=[
                            ft.Container(
                                width=38,
                                height=38,
                                border_radius=8,
                                bgcolor=ACCENT,
                                alignment=ft.Alignment.CENTER,
                                content=ft.Icon(ft.Icons.AUTO_AWESOME, color="#FFFFFF", size=22),
                            ),
                            ft.Column(
                                spacing=0,
                                controls=[
                                    ft.Text("VisualDesk", size=18, weight=ft.FontWeight.W_700, color=INK),
                                    ft.Text("Workspace", size=11, color=MUTED),
                                ],
                            ),
                        ],
                    ),
                ),
                ft.Container(expand=True, content=rail),
                ft.Container(
                    margin=ft.Margin.symmetric(horizontal=18),
                    padding=14,
                    border_radius=8,
                    bgcolor="#F7FAFF",
                    content=ft.Row(
                        spacing=10,
                        controls=[
                            ft.CircleAvatar(content=ft.Text("CD"), bgcolor=SOFT_BLUE, color=ACCENT),
                            ft.Column(
                                spacing=2,
                                controls=[
                                    ft.Text("Demo User", size=13, weight=ft.FontWeight.W_600, color=INK),
                                    ft.Text("Cuenta local", size=11, color=MUTED),
                                ],
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    padding=ft.Padding.symmetric(horizontal=18),
                    content=ft.Text(
                        APP_VERSION_LABEL,
                        size=11,
                        color=MUTED,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ),
            ],
        ),
    )


def main(page: ft.Page) -> None:
    page.title = APP_VERSION_LABEL
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = BG
    page.padding = 0
    page.window.width = 1180
    page.window.height = 760
    page.window.min_width = 980
    page.window.min_height = 680

    if not hasattr(page, "services"):
        page.services = []

    content = ft.Container(expand=True, padding=28, content=dashboard_view(page))

    def change_view(event: ft.ControlEvent) -> None:
        content.content = VIEWS[event.control.selected_index](page)
        page.update()

    rail = ft.NavigationRail(
        expand=True,
        selected_index=0,
        min_width=92,
        min_extended_width=220,
        label_type=ft.NavigationRailLabelType.ALL,
        bgcolor=PANEL,
        indicator_color=SOFT_BLUE,
        selected_label_text_style=ft.TextStyle(color=ACCENT, weight=ft.FontWeight.W_600),
        unselected_label_text_style=ft.TextStyle(color=MUTED),
        use_indicator=True,
        on_change=change_view,
        destinations=[nav_destination(*item) for item in NAV_ITEMS],
    )

    sidebar = build_sidebar(rail)
    page.add(ft.Row(expand=True, spacing=0, controls=[sidebar, content]))
