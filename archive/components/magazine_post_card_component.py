import reflex as rx

CARD_BG_COLOR = "#1E1E1E"
HEADING_COLOR = "#E0E0E0"
BODY_TEXT_COLOR = "#B0B0B0"
ACCENT_COLOR = "#2C5F2D"
BORDER_COLOR = "#2C5F2D"
BORDER_HOVER_COLOR = "#3A7F3D"
FONT_GEOGROTESK = "font-['Inter',_sans-serif]"


def magazine_post_card_component(
    post: dict,
) -> rx.Component:
    button_class = f"w-full text-center bg-transparent border-2 border-[{ACCENT_COLOR}] text-white {FONT_GEOGROTESK} font-semibold py-2 px-4 rounded-2xl hover:bg-[{ACCENT_COLOR}] hover:text-black focus:outline-none focus:ring-2 focus:ring-[{ACCENT_COLOR}] focus:ring-offset-2 transition-all duration-200 text-sm"
    return rx.el.div(
        rx.el.a(
            rx.el.img(
                src=post["image_url"],
                alt=post["title"],
                class_name="w-full h-48 object-cover rounded-t-2xl transition-transform duration-300 group-hover:scale-105",
                loading="lazy",
            ),
            href=post["read_more_url"],
        ),
        rx.el.div(
            rx.el.h3(
                post["title"],
                class_name=f"text-lg font-bold text-[{HEADING_COLOR}] mb-2 {FONT_GEOGROTESK}",
            ),
            rx.el.p(
                post["date"],
                class_name=f"text-sm text-[{BODY_TEXT_COLOR}] mb-4 {FONT_GEOGROTESK}",
            ),
            rx.el.a(
                "Read more",
                href=post["read_more_url"],
                class_name=button_class,
            ),
            class_name="p-4 flex flex-col flex-grow",
        ),
        class_name=f"bg-[{CARD_BG_COLOR}] rounded-2xl border border-[{BORDER_COLOR}] w-full overflow-hidden flex flex-col transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_8px_25px_rgba(44,95,45,0.3)] hover:border-[{BORDER_HOVER_COLOR}] group",
        style={"--tw-ring-offset-color": CARD_BG_COLOR},
    )