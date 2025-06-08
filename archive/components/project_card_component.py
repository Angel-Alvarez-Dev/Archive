import reflex as rx

HEADING_COLOR = "#1B3A28"
BODY_TEXT_COLOR = "#2C5F2D"
CARD_BG_COLOR = "#1E1E1E"
BORDER_COLOR = "#2C5F2D"
BORDER_HOVER_COLOR = "#3A7F3D"
FONT_GEOGROTESK = "font-['GeoGrotesk',_sans-serif]"
FONT_KOUGAPIXEL = "font-['KougaPixel',_monospace]"


def project_card_component(
    project_name: str,
    image_url: str,
    design_link: str,
    is_new: bool = False,
) -> rx.Component:
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
        rx.el.img(
            src=image_url,
            alt=project_name,
            class_name="w-full h-56 object-cover aspect-video",
            loading="lazy",
        ),
        rx.el.div(
            rx.el.a(
                rx.el.button(
                    "Go to design",
                    class_name=f"w-full bg-[{BODY_TEXT_COLOR}] text-black {FONT_GEOGROTESK} font-medium py-2 px-4 rounded-lg hover:bg-[{BORDER_HOVER_COLOR}] focus:outline-none focus:ring-2 focus:ring-[{BORDER_COLOR}] focus:ring-offset-2 transition-all duration-200",
                    style={
                        "--tw-ring-offset-color": CARD_BG_COLOR
                    },
                ),
                href=design_link,
                is_external=True,
            ),
            class_name="p-6",
        ),
        class_name=f"bg-[{CARD_BG_COLOR}] rounded-lg border border-[{BORDER_COLOR}] w-full overflow-hidden green-noise relative transition-all duration-300 hover:-translate-y-0.5 hover:shadow-[0_2px_4px_rgba(44,95,45,0.5)] hover:border-[{BORDER_HOVER_COLOR}]",
    )