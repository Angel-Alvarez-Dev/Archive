import reflex as rx

ICON_COLOR = "#2C5F2D"
ICON_HOVER_COLOR = "#5EA96E"
FOCUS_RING_COLOR = "#3A7F3D"
BG_COLOR = "#121212"


def icon_bar_component() -> rx.Component:
    icon_link_base_class = f"group p-2 rounded-lg flex items-center justify-center transition-all duration-300 transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-[{FOCUS_RING_COLOR}] focus:ring-offset-2 focus:ring-offset-[{BG_COLOR}]"
    icon_svg_class = f"stroke-[{ICON_COLOR}] group-hover:stroke-[{ICON_HOVER_COLOR}] group-focus:stroke-[{ICON_HOVER_COLOR}] transition-all duration-300"
    return rx.el.div(
        rx.el.a(
            rx.icon(
                "home", size=24, class_name=icon_svg_class
            ),
            href="/",
            aria_label="Go to archive.co Home",
            class_name=icon_link_base_class,
        ),
        rx.el.a(
            rx.icon(
                "bell", size=24, class_name=icon_svg_class
            ),
            href="/subscribe",
            aria_label="Subscribe to archive.co",
            class_name=icon_link_base_class,
        ),
        rx.el.a(
            rx.icon(
                "camera", size=24, class_name=icon_svg_class
            ),
            href="/gallery",
            aria_label="Go to archive.co Gallery",
            class_name=icon_link_base_class,
        ),
        class_name="flex items-center w-full justify-center gap-4 py-4 mb-4",
    )