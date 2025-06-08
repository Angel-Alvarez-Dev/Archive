import reflex as rx
from archive.components.header_component import header_component
from archive.components.footer_component import footer_component
from archive.components.subscription_card_component import (
    subscription_card_component,
)
from archive.components.icon_bar_component import (
    icon_bar_component,
)
from archive.states.state import SubscribeState

BG_COLOR = "#121212"
BODY_TEXT_COLOR = "#2C5F2D"
HEADING_COLOR = "#1B3A28"
BORDER_COLOR = "#2C5F2D"
FONT_URBANSPLASH = "font-['UrbanSplash',_cursive]"
FONT_GEOGROTESK = "font-['GeoGrotesk',_sans-serif]"


def subscribe_page() -> rx.Component:
    section_spacing = "my-16"
    return rx.el.div(
        rx.el.div(
            header_component(),
            icon_bar_component(),
            rx.el.div(
                rx.el.h1(
                    "Subscription Plans",
                    class_name=f"text-[2rem] {FONT_URBANSPLASH} text-[{HEADING_COLOR}] text-center mb-1",
                ),
                rx.el.div(
                    class_name=f"w-1/2 mx-auto h-[1px] bg-[{BORDER_COLOR}] mb-8"
                ),
                class_name=f"{section_spacing} text-center",
            ),
            rx.el.div(
                rx.foreach(
                    SubscribeState.plans,
                    lambda plan: subscription_card_component(
                        plan_name=plan["name"],
                        price=plan["price"],
                        features=plan["features"],
                        subscribe_link=plan["link"],
                    ),
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-y-8 gap-x-8 px-4 md:px-8 max-w-6xl mx-auto items-stretch",
            ),
            footer_component(),
            class_name=f"max-w-7xl mx-auto px-4 {FONT_GEOGROTESK}",
        ),
        class_name=f"min-h-screen bg-[{BG_COLOR}] text-[{BODY_TEXT_COLOR}] py-8",
    )