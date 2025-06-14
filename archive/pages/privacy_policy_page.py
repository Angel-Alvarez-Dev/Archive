import reflex as rx
from archive.components.legal_page_template import (
    legal_page_template,
    text_section,
)


def privacy_policy_page() -> rx.Component:
    return legal_page_template(
        "Privacy Policy",
        text_section(
            "User Data Collection",
            rx.el.p(
                "We collect user data when you subscribe to our newsletter, make a purchase, or contact us. This data may include your name, email address, and transaction details."
            ),
            rx.el.p(
                "Email addresses collected for the newsletter are used exclusively for sending updates, free models, and articles."
            ),
        ),
        text_section(
            "Data Storage and Usage",
            rx.el.p(
                "Your data is stored securely. We use third-party services like Stripe and Payhip for payment processing. We do not store your full credit card information on our servers."
            ),
            rx.el.p(
                "We do not sell or rent your personal information to third parties."
            ),
        ),
    )