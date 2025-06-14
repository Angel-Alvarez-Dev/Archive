import reflex as rx
import json
from archive.components.header_component import header_component
from archive.components.navbar_component import navbar_component
from archive.components.main_content_component import (
    main_content_component,
)
from archive.components.footer_component import footer_component
from archive.pages.subscribe_page import subscribe_page
from archive.pages.gallery_page import gallery_page
from archive.pages.magazine_page import magazine_page
from archive.pages.shop_page import shop_page
from archive.pages.download_success_page import (
    download_success_page,
)
from archive.pages.privacy_policy_page import (
    privacy_policy_page,
)
from archive.pages.terms_page import terms_page
from archive.pages.refund_policy_page import refund_policy_page
from archive.pages.copyright_notice_page import (
    copyright_notice_page,
)
from archive.pages.support_page import support_page

BG_COLOR = "#121212"
PRIMARY_TEXT_COLOR = "#E0E0E0"
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
        "https://patreon.com/Archive_co",
        "https://cults3d.com/@Archive_co",
    ],
}


def index() -> rx.Component:
    return rx.el.div(
        navbar_component(),
        rx.el.div(
            header_component(),
            main_content_component(),
            footer_component(),
            class_name=f"max-w-7xl mx-auto px-4 {FONT_GEOGROTESK}",
        ),
        class_name=f"min-h-screen bg-[{BG_COLOR}] text-[{PRIMARY_TEXT_COLOR}]",
    )


app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="green",
        radius="large",
    ),
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
app.add_page(
    shop_page,
    route="/shop",
    title="Shop - archive.co",
    description="Purchase high-quality 3D models and assets from the archive.co shop.",
    meta=[
        {
            "property": "og:title",
            "content": "Shop - archive.co",
        },
        {
            "property": "og:description",
            "content": "Purchase high-quality 3D models and assets from the archive.co shop.",
        },
        {
            "property": "og:image",
            "content": "/archive-co-logo.svg",
        },
    ],
)
app.add_page(
    magazine_page,
    route="/magazine",
    title="archive.co Magazine – 3D Printing Articles & News",
    description="Read the latest articles, tutorials, and news about 3D printing, modeling, and creative tech from archive.co.",
    meta=[
        {
            "property": "og:title",
            "content": "archive.co Magazine – 3D Printing Articles & News",
        },
        {
            "property": "og:description",
            "content": "Read the latest articles, tutorials, and news about 3D printing, modeling, and creative tech from archive.co.",
        },
        {
            "property": "og:image",
            "content": "/archive-co-logo.svg",
        },
    ],
)
app.add_page(
    download_success_page,
    route="/download_success",
    title="Download Your File - archive.co",
    description="Download your purchased file from archive.co.",
)
app.add_page(
    privacy_policy_page,
    route="/privacy",
    title="Privacy Policy - archive.co",
)
app.add_page(
    terms_page,
    route="/terms",
    title="Terms and Conditions - archive.co",
)
app.add_page(
    refund_policy_page,
    route="/refund",
    title="Refund Policy - archive.co",
)
app.add_page(
    copyright_notice_page,
    route="/copyright",
    title="Copyright Notice - archive.co",
)
app.add_page(
    support_page,
    route="/support",
    title="Support - archive.co",
)