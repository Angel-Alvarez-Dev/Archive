import reflex as rx

CAPTION_TEXT_COLOR = "#888888"
BORDER_COLOR = "#2C5F2D"
FONT_GEOGROTESK = "font-['Inter',_sans-serif]"


def footer_component() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            class_name="w-full h-[1px] bg-gray-700 mb-8"
        ),
        rx.el.div(
            rx.el.a(
                "Privacy Policy",
                href="/privacy",
                class_name="hover:text-white transition-colors",
            ),
            rx.el.a(
                "Terms",
                href="/terms",
                class_name="hover:text-white transition-colors",
            ),
            rx.el.a(
                "Refund Policy",
                href="/refund",
                class_name="hover:text-white transition-colors",
            ),
            rx.el.a(
                "Copyright",
                href="/copyright",
                class_name="hover:text-white transition-colors",
            ),
            rx.el.a(
                "Support",
                href="/support",
                class_name="hover:text-white transition-colors",
            ),
            class_name=f"flex flex-wrap justify-center items-center gap-x-4 gap-y-2 text-center {FONT_GEOGROTESK} text-[{CAPTION_TEXT_COLOR}] text-sm mb-8",
        ),
        rx.el.p(
            "© 2025 archive.co. All rights reserved.",
            class_name=f"text-center {FONT_GEOGROTESK} text-[{CAPTION_TEXT_COLOR}] text-xs",
        ),
        class_name="px-4 py-8",
    )