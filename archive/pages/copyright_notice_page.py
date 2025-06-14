import reflex as rx
from archive.components.legal_page_template import (
    legal_page_template,
    text_section,
)


def copyright_notice_page() -> rx.Component:
    return legal_page_template(
        "Copyright Notice",
        text_section(
            "Ownership of Models",
            rx.el.p(
                "All models published on archive.co are the intellectual property of their respective creators. Unauthorized copying, sharing, or commercial use is strictly prohibited."
            ),
        ),
        text_section(
            "Fan Art",
            rx.el.p(
                "Some models may be inspired by existing characters and are considered fan art. This content is unofficial and is not affiliated with, or endorsed by, the original brand owners."
            ),
        ),
    )