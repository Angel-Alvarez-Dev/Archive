import reflex as rx
from archive.states.state import HomeState, MagazineState
from archive.components.magazine_post_card_component import (
    magazine_post_card_component,
)

BG_COLOR = "#121212"
CARD_BG_COLOR = "#1E1E1E"
HEADING_COLOR = "#E0E0E0"
BODY_TEXT_COLOR = "#B0B0B0"
CAPTION_TEXT_COLOR = "#888888"
BORDER_COLOR = "#2C5F2D"
ACCENT_COLOR = "#2C5F2D"
BORDER_HOVER_COLOR = "#3A7F3D"
FONT_URBANSPLASH = "font-['Urbanist',_sans-serif]"
FONT_GEOGROTESK = "font-['Inter',_sans-serif]"
FONT_KOUGAPIXEL = "font-['KougaPixel',_monospace]"


def _hero_image_section() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.img(
                src="/archive_graffiti_transparent.png",
                alt="Pixelated graffiti style art for archive.co",
                class_name=f"w-36 h-36 md:w-44 md:h-44 mx-auto rounded-2xl border-2 border-[{BORDER_COLOR}] object-cover transition-all duration-700 hover:scale-105 hover:border-[{BORDER_HOVER_COLOR}] hover:shadow-[0_0_30px_rgba(44,95,45,0.4)] hover:rotate-1 block",
                loading="lazy",
            ),
            class_name="relative group transform transition-transform duration-500 hover:-translate-y-1",
        ),
        rx.el.div(
            rx.el.p(
                "archive.co",
                class_name=f"text-center {FONT_KOUGAPIXEL} text-[{CAPTION_TEXT_COLOR}] text-2xl md:text-3xl mt-4 transition-all duration-300 hover:text-[{BORDER_HOVER_COLOR}] hover:scale-105 hover:tracking-wider",
            ),
            class_name="group",
        ),
        class_name="mb-8",
    )


def _platform_buttons() -> rx.Component:
    platform_button_classes = f"w-full {FONT_GEOGROTESK} py-3 px-6 rounded-2xl text-lg focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-black transition-all duration-300 transform hover:-translate-y-0.5 active:scale-95 font-semibold text-[1rem] text-black bg-[{ACCENT_COLOR}] hover:bg-[{BORDER_HOVER_COLOR}] hover:shadow-[0_4px_15px_rgba(44,95,45,0.4)] tracking-wide"
    return rx.el.div(
        rx.el.a(
            rx.el.button(
                "PATREON",
                class_name=platform_button_classes,
            ),
            href="https://patreon.com/Archive_co?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=creatorshare_creator&utm_content=join_link",
            target="_blank",
            rel="noopener noreferrer",
            is_external=True,
            class_name="w-full md:w-auto",
        ),
        rx.el.a(
            rx.el.button(
                "CULTS3D",
                class_name=platform_button_classes,
            ),
            href="https://cults3d.com/@Archive_co",
            target="_blank",
            rel="noopener noreferrer",
            is_external=True,
            class_name="w-full md:w-auto",
        ),
        class_name="flex flex-col md:flex-row gap-4",
    )


def _social_links() -> rx.Component:
    social_links_data = [
        {
            "icon": "github",
            "href": "https://github.com/Angel-Alvarez-Dev",
            "label": "GitHub",
        },
        {
            "icon": "pinterest",
            "href": "https://mx.pinterest.com/Archivo_co/",
            "label": "Pinterest",
        },
        {
            "icon": "instagram",
            "href": "https://www.instagram.com/archivo.co/?utm_source=ig_web_button_share_sheet",
            "label": "Instagram",
        },
        {
            "icon": "package-open",
            "href": "https://cults3d.com/@Archive_co",
            "label": "Cults3D",
        },
        {
            "icon": "patreon",
            "href": "https://patreon.com/Archive_co?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=creatorshare_creator&utm_content=join_link",
            "label": "Patreon",
        },
    ]
    return rx.el.div(
        rx.foreach(
            social_links_data,
            lambda link: rx.el.a(
                rx.icon(
                    tag=link["icon"],
                    size=24,
                    class_name=f"stroke-white hover:stroke-[{BORDER_HOVER_COLOR}] hover:scale-110 transition-all duration-300 transform hover:rotate-6",
                ),
                href=link["href"],
                target="_blank",
                rel="noopener noreferrer",
                is_external=True,
                class_name="p-2 rounded-lg hover:bg-[rgba(44,95,45,0.1)] transition-all duration-200 group",
                title=link["label"],
            ),
        ),
        class_name="flex flex-wrap justify-center items-center gap-3 md:gap-4",
    )


def main_content_component() -> rx.Component:
    subscribe_button_classes = f"w-full sm:w-auto {FONT_GEOGROTESK} text-black border-2 border-[{ACCENT_COLOR}] bg-[{ACCENT_COLOR}] py-3 px-6 rounded-2xl hover:bg-[{BORDER_HOVER_COLOR}] hover:border-[{BORDER_HOVER_COLOR}] focus:outline-none focus:ring-2 focus:ring-[{ACCENT_COLOR}] focus:ring-offset-2 focus:ring-offset-black transition-all duration-300 transform hover:-translate-y-0.5 active:scale-95 text-[1rem] font-semibold"
    section_spacing = "py-16"
    return rx.el.main(
        rx.el.section(
            _hero_image_section(),
            rx.el.h1(
                "3D MODELS & RESOURCES",
                class_name=f"text-center {FONT_URBANSPLASH} text-[{HEADING_COLOR}] text-[2.5rem] md:text-[3rem] mb-4 tracking-wide font-bold",
            ),
            rx.el.div(
                class_name=f"w-1/2 mx-auto h-[2px] bg-[{BORDER_COLOR}] mb-8 rounded-full"
            ),
            _platform_buttons(),
            class_name=f"flex flex-col items-center {section_spacing} px-4",
        ),
        rx.el.section(
            rx.el.h2(
                "Latest from the Magazine",
                class_name=f"{FONT_URBANSPLASH} text-[{HEADING_COLOR}] text-[2rem] font-bold md:text-[2.2rem] mb-2 text-center tracking-wide",
            ),
            rx.el.div(
                class_name=f"w-1/4 mx-auto h-[2px] bg-[{BORDER_COLOR}] mb-6 rounded-full"
            ),
            rx.el.div(
                rx.cond(
                    MagazineState.latest_post,
                    magazine_post_card_component(
                        MagazineState.latest_post
                    ),
                    rx.el.p(
                        "No articles yet. Check back soon!",
                        class_name=f"text-center text-[{BODY_TEXT_COLOR}]",
                    ),
                ),
                class_name="max-w-2xl mx-auto",
            ),
            class_name=f"px-4 {section_spacing}",
        ),
        rx.el.section(
            rx.el.h2(
                "ABOUT",
                class_name=f"{FONT_URBANSPLASH} text-[{HEADING_COLOR}] text-[2rem] font-bold md:text-[2.2rem] mb-2 text-center tracking-wide",
            ),
            rx.el.div(
                class_name=f"w-1/4 mx-auto h-[2px] bg-[{BORDER_COLOR}] mb-6 rounded-full"
            ),
            rx.el.p(
                "archive.co is a curated collection of high-quality 3D models and creative resources, designed for artists, developers, and enthusiasts.",
                class_name=f"{FONT_GEOGROTESK} text-[{BODY_TEXT_COLOR}] text-[1rem] leading-relaxed text-center max-w-2xl mx-auto",
            ),
            class_name=f"px-4 {section_spacing}",
        ),
        rx.el.section(
            rx.cond(
                HomeState.subscribed,
                rx.el.div(
                    "Welcome to archive.co!",
                    class_name=f"w-full mb-6 {FONT_GEOGROTESK} text-lg text-white font-semibold p-4 text-center rounded-2xl bg-[{CARD_BG_COLOR}] border-2 border-[{BORDER_HOVER_COLOR}] shadow-[0_0_20px_rgba(58,127,61,0.5)]",
                ),
                rx.el.form(
                    rx.el.label(
                        "Get free models and exclusive articles in your inbox.",
                        html_for="email",
                        class_name=f"{FONT_GEOGROTESK} text-center w-full mb-2 text-[{CAPTION_TEXT_COLOR}] text-base font-medium",
                    ),
                    rx.el.div(
                        rx.el.input(
                            placeholder="your@mail.com",
                            name="email",
                            id="email",
                            type="email",
                            required=True,
                            class_name=f"w-full {FONT_GEOGROTESK} text-base bg-black border-2 border-[{BORDER_COLOR}] text-white placeholder:text-[{CAPTION_TEXT_COLOR}] rounded-2xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-[{BORDER_HOVER_COLOR}] focus:border-[{BORDER_HOVER_COLOR}] transition-all",
                        ),
                        rx.el.button(
                            "Join",
                            type="submit",
                            class_name=subscribe_button_classes,
                        ),
                        class_name="flex flex-col items-center gap-4 w-full sm:flex-row",
                    ),
                    on_submit=HomeState.handle_subscribe,
                    reset_on_submit=True,
                    class_name="w-full mb-6 flex flex-col items-center max-w-md mx-auto",
                ),
            ),
            class_name="px-4",
        ),
        rx.el.section(
            _social_links(), class_name=f"pb-16 pt-8"
        ),
    )