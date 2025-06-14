import reflex as rx

BG_COLOR = "#121212"
PRIMARY_TEXT_COLOR = "#E0E0E0"
ACCENT_COLOR = "#2C5F2D"
FONT_GEOGROTESK = "font-['Inter',_sans-serif]"


def nav_link(text: str, href: str) -> rx.Component:
    return rx.el.a(
        text,
        href=href,
        class_name=f"px-4 py-2 {FONT_GEOGROTESK} text-base font-medium text-[{PRIMARY_TEXT_COLOR}] hover:text-[{ACCENT_COLOR}] transition-colors duration-300 rounded-2xl",
    )


def navbar_component() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            nav_link("Home", "/"),
            nav_link("Gallery", "/gallery"),
            nav_link("Shop", "/shop"),
            nav_link("Magazine", "/magazine"),
            nav_link("Subscribe", "/subscribe"),
            nav_link("Support", "/support"),
            class_name="flex items-center justify-center flex-wrap",
        ),
        class_name=f"sticky top-0 z-50 w-full py-2 bg-[{BG_COLOR}]/80 backdrop-blur-md border-b border-gray-800",
    )