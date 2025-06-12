import reflex as rx
import json
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
from archive.db import init_db


BG_COLOR = "#121212"
PRIMARY_TEXT_COLOR = "#2C5F2D"
FONT_GEOGROTESK = "font-['Inter',_sans-serif]"
structured_data = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "archive.co",
    "url": "https://archive.co",
    "logo": "https://archive.co/archive-co-logo.svg",
    "sameAs": [
        "https://github.com/Angel-Alvarez-Dev",
        "https://mx.pinterest.com/Archivo_co/",
        "patreon.com/Archive_co",
        "https://cults3d.com/@Archive_co",
    ],
}


def index() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            header_component(),
            icon_bar_component(),
            main_content_component(),
            footer_component(),
            class_name=f"max-w-[480px] mx-auto px-4 {FONT_GEOGROTESK}",
        ),
        class_name=f"min-h-screen bg-[{BG_COLOR}] text-[{PRIMARY_TEXT_COLOR}]",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.script(
            json.dumps(structured_data),
            type="application/ld+json",
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
        rx.el.link(
            rel="stylesheet",
            href="https://fonts.googleapis.com/css2?family=Urbanist:wght@400;700&family=Inter:wght@400;500;600;700&display=swap",
        ),
        rx.el.link(
            rel="icon",
            href="/archive-icon.svg",
            type="image/svg+xml",
        ),
    ],
)
app.add_page(
    index,
    route="/",
    title="archive.co – Curated 3D Archive & Community",
    description="The official hub for archive.co. Explore a curated archive of high-quality 3D models, creative assets, and join a community of artists and developers.",
    meta=[
        {
            "property": "og:title",
            "content": "archive.co – Curated 3D Archive & Community",
        },
        {
            "property": "og:description",
            "content": "The official hub for archive.co. Explore a curated archive of high-quality 3D models, creative assets, and join a community of artists and developers.",
        },
        {
            "property": "og:image",
            "content": "/archive-co-logo.svg",
        },
    ],
)
app.add_page(
    subscribe_page,
    route="/subscribe",
    title="Join archive.co – Free & Premium 3D Models",
    description="Subscribe to archive.co for exclusive access to free and premium 3D models, regular content updates, and direct support.",
    meta=[
        {
            "property": "og:title",
            "content": "Join archive.co – Free & Premium 3D Models",
        },
        {
            "property": "og:description",
            "content": "Subscribe to archive.co for exclusive access to free and premium 3D models, regular content updates, and direct support.",
        },
        {
            "property": "og:image",
            "content": "/archive-co-logo.svg",
        },
    ],
)
app.add_page(
    gallery_page,
    route="/gallery",
    title="archive.co Gallery – Graffiti & 3D Renders",
    description="Browse the project gallery of archive.co, featuring graffiti-inspired art, detailed 3D renders, and unique digital creations.",
    meta=[
        {
            "property": "og:title",
            "content": "archive.co Gallery – Graffiti & 3D Renders",
        },
        {
            "property": "og:description",
            "content": "Browse the project gallery of archive.co, featuring graffiti-inspired art, detailed 3D renders, and unique digital creations.",
        },
        {
            "property": "og:image",
            "content": "/archive-co-logo.svg",
        },
    ],
)