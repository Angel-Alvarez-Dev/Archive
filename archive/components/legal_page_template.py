import reflex as rx
from archive.components.navbar_component import navbar_component
from archive.components.footer_component import footer_component

BG_COLOR = "#121212"
PRIMARY_TEXT_COLOR = "#E0E0E0"
HEADING_COLOR = "#E0E0E0"
BODY_TEXT_COLOR = "#B0B0B0"
BORDER_COLOR = "#2C5F2D"
FONT_URBANSPLASH = "font-['Urbanist',_sans-serif]"
FONT_GEOGROTESK = "font-['Inter',_sans-serif]"


def legal_page_template(
    title: str, *children
) -> rx.Component:
    return rx.el.div(
        navbar_component(),
        rx.el.main(
            rx.el.div(
                rx.el.h1(
                    title,
                    class_name=f"text-[2.5rem] {FONT_URBANSPLASH} font-bold text-[{HEADING_COLOR}] text-center mb-4",
                ),
                rx.el.div(
                    class_name=f"w-1/4 mx-auto h-[1px] bg-[{BORDER_COLOR}] mb-12"
                ),
                rx.el.div(
                    *children,
                    class_name=f"max-w-4xl mx-auto {FONT_GEOGROTESK} text-[{BODY_TEXT_COLOR}] space-y-6",
                ),
                class_name="py-16 px-6",
            ),
            class_name="flex-grow",
        ),
        footer_component(),
        class_name=f"min-h-screen bg-[{BG_COLOR}] text-[{PRIMARY_TEXT_COLOR}] flex flex-col {FONT_GEOGROTESK}",
    )


def text_section(title: str, *content) -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            title,
            class_name=f"text-xl font-bold text-[{HEADING_COLOR}] mb-3 {FONT_GEOGROTESK}",
        ),
        rx.el.div(*content, class_name="space-y-4"),
        class_name="mb-6",
    )