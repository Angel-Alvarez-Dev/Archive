import reflex as rx

BG_COLOR = "#121212"
CARD_BG_COLOR = "#1E1E1E"
HEADING_COLOR = "#1B3A28"
BODY_TEXT_COLOR = "#2C5F2D"
CAPTION_TEXT_COLOR = "#4A7A54"
BORDER_COLOR = "#2C5F2D"
BORDER_HOVER_COLOR = "#3A7F3D"
FONT_GEOGROTESK = "font-['GeoGrotesk',_sans-serif]"


def subscription_card_component(
    plan_name: str,
    price: str,
    features: list[str],
    subscribe_link: str,
) -> rx.Component:
    subscribe_button_classes = f"w-full {FONT_GEOGROTESK} text-[{BODY_TEXT_COLOR}] border-2 border-[{BORDER_COLOR}] bg-[{BG_COLOR}] font-medium py-2 px-4 rounded-lg hover:bg-[{BODY_TEXT_COLOR}] hover:text-black focus:outline-none focus:ring-2 focus:ring-[{BORDER_COLOR}] focus:ring-offset-2 transition-all duration-300 transform hover:-translate-y-0.5"
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    plan_name,
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
            rx.el.p(
                price,
                class_name=f"{FONT_GEOGROTESK} font-bold text-3xl text-[{HEADING_COLOR}] mb-6 text-center pt-6",
            ),
            rx.el.ul(
                rx.foreach(
                    features,
                    lambda feature: rx.el.li(
                        rx.icon(
                            "check",
                            size=20,
                            class_name=f"text-[{BODY_TEXT_COLOR}] mr-3 flex-shrink-0",
                        ),
                        rx.el.span(
                            feature,
                            class_name=f"{FONT_GEOGROTESK} text-[0.875rem] text-[{BODY_TEXT_COLOR}]",
                        ),
                        class_name="flex items-center mb-2",
                    ),
                ),
                class_name="space-y-2 mb-auto",
            ),
            rx.el.a(
                rx.el.button(
                    "Subscribe",
                    class_name=subscribe_button_classes,
                    style={
                        "--tw-ring-offset-color": CARD_BG_COLOR
                    },
                ),
                href=subscribe_link,
                is_external=True,
                class_name="mt-8",
            ),
            class_name="p-6 flex flex-col h-full",
        ),
        class_name=f"bg-[{CARD_BG_COLOR}] rounded-lg border border-[{BORDER_COLOR}] w-full green-noise relative overflow-hidden transition-all duration-300 flex flex-col hover:-translate-y-0.5 hover:border-[{BORDER_HOVER_COLOR}] hover:shadow-[0_2px_4px_rgba(44,95,45,0.5)]",
    )