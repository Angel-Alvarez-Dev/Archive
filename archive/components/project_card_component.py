import reflex as rx

HEADING_COLOR = "#E0E0E0"
BODY_TEXT_COLOR = "#B0B0B0"
CARD_BG_COLOR = "#1E1E1E"
BORDER_COLOR = "#2C5F2D"
BORDER_HOVER_COLOR = "#3A7F3D"
ACCENT_COLOR = "#2C5F2D"
FONT_GEOGROTESK = "font-['Inter',_sans-serif]"
FONT_KOUGAPIXEL = "font-['KougaPixel',_monospace]"


def project_card_component(
    project_name: str,
    embed_url: str,
    model_url: str,
    image_url: str,
    download_url: str,
    purchase_url: str,
    price: str | None = None,
    is_new: bool = False,
    file_name: str = "",
) -> rx.Component:
    action_button_class = f"w-full text-center bg-transparent border-2 border-[{ACCENT_COLOR}] text-white {FONT_GEOGROTESK} font-semibold py-2 px-4 rounded-2xl hover:bg-[{ACCENT_COLOR}] hover:text-black focus:outline-none focus:ring-2 focus:ring-[{ACCENT_COLOR}] focus:ring-offset-2 transition-all duration-200 text-sm"
    buy_button_class = f"w-full text-center bg-[{ACCENT_COLOR}] border-2 border-[{ACCENT_COLOR}] text-black {FONT_GEOGROTESK} font-semibold py-2 px-4 rounded-2xl hover:bg-[{BORDER_HOVER_COLOR}] hover:border-[{BORDER_HOVER_COLOR}] focus:outline-none focus:ring-2 focus:ring-[{ACCENT_COLOR}] focus:ring-offset-2 transition-all duration-200 text-sm"
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    project_name,
                    class_name=f"{FONT_GEOGROTESK} font-semibold text-lg text-[{HEADING_COLOR}]",
                ),
                rx.cond(
                    is_new,
                    rx.el.span(
                        "NEW",
                        class_name=f"ml-2 {FONT_KOUGAPIXEL} bg-[{BORDER_COLOR}] text-black px-2 py-0.5 rounded-md text-xs font-semibold",
                    ),
                    None,
                ),
                class_name="flex-grow flex items-center pl-3",
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
            rx.el.iframe(
                src=f"{embed_url}?autostart=0&ui_controls=1&ui_infos=0&ui_watermark=0",
                class_name="w-full aspect-video border-0",
                loading="lazy",
                allow="autoplay; fullscreen; xr-spatial-tracking",
                allow_fullscreen=True,
            ),
            rx.el.noscript(
                rx.el.img(
                    src=image_url,
                    alt=f"Static preview for {project_name}",
                    class_name="w-full aspect-video object-cover",
                )
            ),
            class_name="relative overflow-hidden bg-black",
        ),
        rx.el.div(
            rx.cond(
                price,
                rx.el.div(
                    rx.el.p(
                        price,
                        class_name=f"text-xl font-bold text-[{HEADING_COLOR}]",
                    ),
                    rx.el.a(
                        "Buy",
                        href=purchase_url,
                        is_external=True,
                        target="_blank",
                        class_name=buy_button_class,
                        style={"width": "120px"},
                    ),
                    class_name="flex justify-between items-center w-full",
                ),
                rx.el.div(
                    rx.el.a(
                        "View More",
                        href=model_url,
                        is_external=True,
                        class_name=action_button_class,
                    ),
                    rx.el.a(
                        "Download",
                        href=download_url,
                        is_external=True,
                        class_name=action_button_class,
                    ),
                    rx.el.a(
                        "Buy",
                        href=purchase_url,
                        is_external=True,
                        target="_blank",
                        class_name=buy_button_class,
                    ),
                    class_name="flex flex-col sm:flex-row gap-2",
                ),
            ),
            class_name="p-4",
            style={"--tw-ring-offset-color": CARD_BG_COLOR},
        ),
        class_name=f"bg-[{CARD_BG_COLOR}] rounded-2xl border border-[{BORDER_COLOR}] w-full overflow-hidden green-noise relative transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_8px_25px_rgba(44,95,45,0.3)] hover:border-[{BORDER_HOVER_COLOR}] group",
    )