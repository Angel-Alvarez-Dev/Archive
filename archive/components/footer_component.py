import reflex as rx

CAPTION_TEXT_COLOR = "#4A7A54"
BORDER_COLOR = "#2C5F2D"
FONT_GEOGROTESK = "font-['Inter',_sans-serif]"


def footer_component() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            class_name=f"w-full h-[1px] bg-[{BORDER_COLOR}] mb-4"
        ),
        rx.el.div(
            rx.el.a(
                "Email: alvarezvillegazangel@gmail.com",
                href="mailto:alvarezvillegazangel@gmail.com",
                class_name="hover:text-white",
            ),
            rx.el.span(" | ", class_name="mx-2"),
            rx.el.a(
                "Contact Page",
                href="mailto:alvarezvillegazangel@gmail.com",
                class_name="hover:text-white",
            ),
            class_name=f"text-center {FONT_GEOGROTESK} text-[{CAPTION_TEXT_COLOR}] text-sm mb-8 flex justify-center items-center",
        ),
        rx.el.p(
            "© 2025 archive.co. All rights reserved.",
            class_name=f"text-center {FONT_GEOGROTESK} text-[{CAPTION_TEXT_COLOR}] text-xs",
        ),
        class_name="px-4 py-8",
    )