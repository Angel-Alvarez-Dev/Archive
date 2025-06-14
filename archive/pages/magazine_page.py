import reflex as rx
from archive.components.header_component import header_component
from archive.components.footer_component import footer_component
from archive.components.magazine_post_card_component import (
    magazine_post_card_component,
)
from archive.components.navbar_component import navbar_component
from archive.states.state import MagazineState

BG_COLOR = "#121212"
HEADING_COLOR = "#E0E0E0"
BODY_TEXT_COLOR = "#B0B0B0"
BORDER_COLOR = "#2C5F2D"
FONT_URBANSPLASH = "font-['Urbanist',_sans-serif]"
FONT_GEOGROTESK = "font-['Inter',_sans-serif]"


def magazine_page() -> rx.Component:
    section_spacing = "my-16"
    return rx.el.div(
        navbar_component(),
        rx.el.div(
            header_component(),
            rx.el.div(
                rx.el.h1(
                    "Magazine",
                    class_name=f"text-[2rem] {FONT_URBANSPLASH} font-bold text-[{HEADING_COLOR}] text-center mb-1",
                ),
                rx.el.div(
                    class_name=f"w-1/2 mx-auto h-[1px] bg-[{BORDER_COLOR}] mb-8"
                ),
                class_name=f"{section_spacing} text-center",
            ),
            rx.el.div(
                rx.foreach(
                    MagazineState.posts,
                    magazine_post_card_component,
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-y-8 gap-x-8 px-4 md:px-8 max-w-7xl mx-auto items-stretch",
            ),
            footer_component(),
            class_name=f"max-w-7xl mx-auto px-4 {FONT_GEOGROTESK}",
        ),
        class_name=f"min-h-screen bg-[{BG_COLOR}] text-white py-8",
    )