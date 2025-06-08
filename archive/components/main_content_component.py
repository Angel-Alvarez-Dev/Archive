import reflex as rx

BG_COLOR = "#121212"
CARD_BG_COLOR = "#1E1E1E"
HEADING_COLOR = "#1B3A28"
BODY_TEXT_COLOR = "#2C5F2D"
CAPTION_TEXT_COLOR = "#4A7A54"
BORDER_COLOR = "#2C5F2D"
BORDER_HOVER_COLOR = "#3A7F3D"
FONT_URBANSPLASH = "font-['UrbanSplash',_cursive]"
FONT_GEOGROTESK = "font-['GeoGrotesk',_sans-serif]"
FONT_KOUGAPIXEL = "font-['KougaPixel',_monospace]"


def _contact_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "CONTACT",
                    class_name=f"{FONT_GEOGROTESK} font-semibold text-lg text-[{HEADING_COLOR}]",
                ),
                class_name="flex-grow pl-3",
            ),
            rx.el.div(
                rx.el.span(
                    class_name="h-3 w-3 bg-[#FF5F56] rounded-full"
                ),
                rx.el.span(
                    class_name="h-3 w-3 bg-[#FFBD2E] rounded-full"
                ),
                rx.el.span(
                    class_name="h-3 w-3 bg-[#27C93F] rounded-full"
                ),
                class_name="flex items-center space-x-1.5 pr-3",
            ),
            class_name=f"flex justify-between items-center py-3 border-b border-[{BORDER_COLOR}]",
        ),
        rx.el.div(
            rx.icon(
                "mail",
                size=48,
                class_name=f"mx-auto my-4 text-[{BODY_TEXT_COLOR}] pt-6",
            ),
            rx.el.p(
                "Do you have a question or a proposal? Let's talk!",
                class_name=f"{FONT_GEOGROTESK} text-center text-[0.875rem] text-[{CAPTION_TEXT_COLOR}] mb-6",
            ),
            rx.el.a(
                rx.el.button(
                    "Contact",
                    class_name=f"w-full {FONT_GEOGROTESK} text-[{BODY_TEXT_COLOR}] border-2 border-[{BORDER_COLOR}] bg-[{BG_COLOR}] py-2 px-4 rounded-lg hover:bg-[{BODY_TEXT_COLOR}] hover:text-black focus:outline-none focus:ring-2 focus:ring-[{BORDER_COLOR}] focus:ring-offset-2 focus:ring-offset-black transition-all duration-300 transform hover:-translate-y-0.5",
                ),
                href="mailto:contact@archive.co",
            ),
            class_name="p-6",
        ),
        class_name=f"bg-[{CARD_BG_COLOR}] rounded-lg border border-[{BORDER_COLOR}] w-full max-w-sm mx-auto green-noise relative overflow-hidden transition-all duration-300 hover:-translate-y-0.5 hover:shadow-[0_2px_4px_rgba(44,95,45,0.5)] hover:border-[{BORDER_HOVER_COLOR}]",
    )


def main_content_component() -> rx.Component:
    button_base_classes = f"w-full {FONT_GEOGROTESK} py-3 px-6 rounded-lg text-lg focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-black transition-all duration-300 transform hover:-translate-y-0.5"
    subscribe_button_classes = f"{button_base_classes} text-[{BODY_TEXT_COLOR}] border-2 border-[{BORDER_COLOR}] bg-black hover:bg-[{BODY_TEXT_COLOR}] hover:text-black hover:shadow-[0_2px_4px_rgba(44,95,45,0.5)]"
    platform_button_classes = f"{button_base_classes} text-black bg-[{BODY_TEXT_COLOR}] hover:bg-[{BORDER_HOVER_COLOR}] hover:shadow-[0_2px_4px_rgba(44,95,45,0.5)]"
    section_spacing = "my-16"
    return rx.el.main(
        rx.el.section(
            rx.el.div(
                rx.el.img(
                    src="/pixel_art_avatar.png",
                    alt="archive.co Pixel Art Avatar",
                    class_name=f"w-32 h-32 md:w-40 md:h-40 mx-auto rounded-lg border-2 border-[{BORDER_COLOR}] object-cover transition-opacity duration-500 opacity-0",
                    loading="lazy",
                    custom_attrs={
                        "onload": "this.style.opacity = 1;"
                    },
                ),
                rx.el.p(
                    "archive.co",
                    class_name=f"text-center {FONT_KOUGAPIXEL} text-[{CAPTION_TEXT_COLOR}] text-2xl md:text-3xl mt-4",
                ),
                class_name="mb-8",
            ),
            rx.el.h1(
                "3D MODELS & RESOURCES",
                class_name=f"text-center {FONT_URBANSPLASH} text-[{HEADING_COLOR}] text-[2rem] mb-2",
            ),
            rx.el.div(
                class_name=f"w-1/2 mx-auto h-[1px] bg-[{BORDER_COLOR}] mb-6"
            ),
            rx.el.a(
                rx.el.button(
                    "Subscribe to archive.co",
                    class_name=subscribe_button_classes,
                ),
                href="#subscribe",
                class_name="block mb-4",
            ),
            rx.el.div(
                rx.el.a(
                    rx.el.button(
                        "GUMROAD",
                        class_name=platform_button_classes,
                    ),
                    href="https://gumroad.com/archive.co",
                    is_external=True,
                    class_name="w-full md:w-auto",
                ),
                rx.el.a(
                    rx.el.button(
                        "SKETCHFAB",
                        class_name=platform_button_classes,
                    ),
                    href="https://sketchfab.com/archive.co",
                    is_external=True,
                    class_name="w-full md:w-auto",
                ),
                class_name="flex flex-col md:flex-row gap-4",
            ),
            class_name=f"flex flex-col items-center {section_spacing}",
        ),
        rx.el.section(
            rx.el.h2(
                "ABOUT",
                class_name=f"{FONT_URBANSPLASH} text-[{HEADING_COLOR}] text-[2rem] mb-1 text-center",
            ),
            rx.el.div(
                class_name=f"w-1/4 mx-auto h-[1px] bg-[{BORDER_COLOR}] mb-3"
            ),
            rx.el.p(
                "archive.co is a curated collection of high-quality 3D models and creative resources, designed for artists, developers, and enthusiasts.",
                class_name=f"{FONT_GEOGROTESK} text-[{BODY_TEXT_COLOR}] text-[0.875rem] leading-relaxed text-center",
            ),
            class_name=f"px-4 {section_spacing}",
        ),
        rx.el.section(
            _contact_card(),
            class_name=f"px-4 {section_spacing}",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.a(
                    rx.icon(
                        tag="twitter",
                        size=24,
                        class_name=f"stroke-[{BODY_TEXT_COLOR}] hover:stroke-[{BORDER_HOVER_COLOR}] hover:scale-105 transition-all duration-300",
                    ),
                    href="#",
                    is_external=True,
                ),
                rx.el.a(
                    rx.icon(
                        tag="instagram",
                        size=24,
                        class_name=f"stroke-[{BODY_TEXT_COLOR}] hover:stroke-[{BORDER_HOVER_COLOR}] hover:scale-105 transition-all duration-300",
                    ),
                    href="#",
                    is_external=True,
                ),
                rx.el.a(
                    rx.icon(
                        tag="youtube",
                        size=24,
                        class_name=f"stroke-[{BODY_TEXT_COLOR}] hover:stroke-[{BORDER_HOVER_COLOR}] hover:scale-105 transition-all duration-300",
                    ),
                    href="#",
                    is_external=True,
                ),
                rx.el.a(
                    rx.icon(
                        tag="github",
                        size=24,
                        class_name=f"stroke-[{BODY_TEXT_COLOR}] hover:stroke-[{BORDER_HOVER_COLOR}] hover:scale-105 transition-all duration-300",
                    ),
                    href="#",
                    is_external=True,
                ),
                class_name="flex flex-wrap justify-center items-center gap-6 md:gap-8",
            ),
            class_name=f"{section_spacing}",
        ),
    )