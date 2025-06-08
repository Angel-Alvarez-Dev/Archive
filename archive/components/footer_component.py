import reflex as rx

CAPTION_TEXT_COLOR = "#4A7A54"
FONT_GEOGROTESK = "font-['GeoGrotesk',_sans-serif]"


def footer_component() -> rx.Component:
    return rx.el.footer(
        rx.el.p(
            "© 2025 archive.co. All rights reserved.",
            class_name=f"text-center {FONT_GEOGROTESK} text-[{CAPTION_TEXT_COLOR}] text-xs py-8",
        )
    )