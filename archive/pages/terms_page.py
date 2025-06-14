import reflex as rx
from archive.components.legal_page_template import (
    legal_page_template,
    text_section,
)


def terms_page() -> rx.Component:
    return legal_page_template(
        "Terms and Conditions",
        text_section(
            "Usage Rights",
            rx.el.p(
                "All 3D models and digital assets purchased or downloaded from archive.co are for personal, non-commercial use only, unless explicitly stated otherwise in a separate license agreement."
            ),
            rx.el.p(
                "You may not resell, redistribute, or use the models for commercial purposes without prior written consent."
            ),
        ),
        text_section(
            "Access to Content",
            rx.el.p(
                "Upon purchase, you will be granted access to download the digital files. We are not responsible for any loss of data on your end. We recommend backing up your downloaded files."
            ),
        ),
    )