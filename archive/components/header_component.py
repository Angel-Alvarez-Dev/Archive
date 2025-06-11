import reflex as rx

SUBTITLE_COLOR = "#4A7A54"
ACCENT_COLOR = "#1B3A28"
FONT_URBANSPLASH = "font-['Urbanist',_sans-serif]"
FONT_GEOGROTESK = "font-['Inter',_sans-serif]"


def header_component() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                "archive.co",
                class_name=f"text-center {FONT_URBANSPLASH} text-5xl md:text-6xl text-[{ACCENT_COLOR}] font-bold",
            ),
            rx.el.p(
                "CURATED 3D ARCHIVE",
                class_name=f"text-center {FONT_GEOGROTESK} text-[{SUBTITLE_COLOR}] text-[1.25rem] mt-2 tracking-wider",
            ),
            class_name="py-8 md:py-12",
        )
    )