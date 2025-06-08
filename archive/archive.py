import reflex as rx
from archive.components.header_component import header_component
from archive.components.icon_bar_component import (
    icon_bar_component,
)
from archive.components.main_content_component import (
    main_content_component,
)
from archive.components.footer_component import footer_component
from archive.pages.subscribe_page import subscribe_page
from archive.pages.gallery_page import gallery_page

BG_COLOR = "#121212"
PRIMARY_TEXT_COLOR = "#2C5F2D"
FONT_GEOGROTESK = "font-['GeoGrotesk',_sans-serif]"


def index() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            header_component(),
            icon_bar_component(),
            main_content_component(),
            footer_component(),
            class_name=f"max-w-lg mx-auto px-4 {FONT_GEOGROTESK}",
        ),
        class_name=f"min-h-screen bg-[{BG_COLOR}] text-[{PRIMARY_TEXT_COLOR}]",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    stylesheets=["/custom_styles.css"],
    head_components=[
        rx.el.title("archive.co | 3D Models & Resources"),
        rx.el.meta(
            name="description",
            content="archive.co is a curated archive of 3D models and creative resources.",
        ),
        rx.el.meta(
            property="og:title",
            content="archive.co | 3D Models & Resources",
        ),
        rx.el.meta(
            property="og:description",
            content="Explore a curated archive of high-quality 3D models and creative assets at archive.co.",
        ),
        rx.el.meta(
            property="og:image",
            content="/archive-co-logo.svg",
        ),
        rx.el.link(
            rel="icon",
            href="/favicon.ico",
            type="image/x-icon",
        ),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.googleapis.com",
        ),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            crossorigin="",
        ),
    ],
)
app.add_page(index, route="/")
app.add_page(subscribe_page, route="/subscribe")
app.add_page(gallery_page, route="/gallery")