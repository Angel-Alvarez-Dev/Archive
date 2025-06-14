import reflex as rx
from archive.components.legal_page_template import (
    legal_page_template,
    text_section,
)


def refund_policy_page() -> rx.Component:
    return legal_page_template(
        "Refund Policy",
        text_section(
            "Digital Products",
            rx.el.p(
                "Due to the digital nature of our products (STL files and other assets), we generally do not offer refunds once a file has been downloaded."
            ),
        ),
        text_section(
            "Exceptions",
            rx.el.p(
                "A refund may be considered in cases where there is a technical error with the file that prevents its use, and we are unable to provide a corrected version in a timely manner. Please contact our support team with details of the issue."
            ),
        ),
    )