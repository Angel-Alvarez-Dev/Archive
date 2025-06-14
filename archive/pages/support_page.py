import reflex as rx
from archive.components.navbar_component import navbar_component
from archive.components.footer_component import footer_component
from archive.states.support_state import SupportState

BG_COLOR = "#121212"
PRIMARY_TEXT_COLOR = "#E0E0E0"
HEADING_COLOR = "#E0E0E0"
BODY_TEXT_COLOR = "#B0B0B0"
CAPTION_TEXT_COLOR = "#888888"
BORDER_COLOR = "#2C5F2D"
ACCENT_COLOR = "#2C5F2D"
BORDER_HOVER_COLOR = "#3A7F3D"
FONT_URBANSPLASH = "font-['Urbanist',_sans-serif]"
FONT_GEOGROTESK = "font-['Inter',_sans-serif]"


def contact_form() -> rx.Component:
    input_class = f"w-full {FONT_GEOGROTESK} text-base bg-black border-2 border-[{BORDER_COLOR}] text-white placeholder:text-[{CAPTION_TEXT_COLOR}] rounded-2xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-[{BORDER_HOVER_COLOR}] focus:border-[{BORDER_HOVER_COLOR}] transition-all"
    button_class = f"w-full {FONT_GEOGROTESK} text-black border-2 border-[{ACCENT_COLOR}] bg-[{ACCENT_COLOR}] py-3 px-6 rounded-2xl hover:bg-[{BORDER_HOVER_COLOR}] hover:border-[{BORDER_HOVER_COLOR}] focus:outline-none focus:ring-2 focus:ring-[{ACCENT_COLOR}] focus:ring-offset-2 focus:ring-offset-black transition-all duration-300 transform hover:-translate-y-0.5 active:scale-95 text-[1rem] font-semibold"
    return rx.el.div(
        rx.cond(
            SupportState.submitted,
            rx.el.div(
                "Thank you for your message! We'll get back to you soon.",
                class_name=f"p-6 text-center text-lg font-semibold bg-[#1E1E1E] border-2 border-[{BORDER_HOVER_COLOR}] rounded-2xl text-white",
            ),
            rx.el.form(
                rx.el.div(
                    rx.el.label(
                        "Name",
                        html_for="name",
                        class_name=f"mb-1 text-sm font-medium {FONT_GEOGROTESK}",
                    ),
                    rx.el.input(
                        id="name",
                        name="name",
                        type="text",
                        required=True,
                        class_name=input_class,
                    ),
                    class_name="flex flex-col gap-1 w-full",
                ),
                rx.el.div(
                    rx.el.label(
                        "Email",
                        html_for="email",
                        class_name=f"mb-1 text-sm font-medium {FONT_GEOGROTESK}",
                    ),
                    rx.el.input(
                        id="email",
                        name="email",
                        type="email",
                        required=True,
                        class_name=input_class,
                    ),
                    class_name="flex flex-col gap-1 w-full",
                ),
                rx.el.div(
                    rx.el.label(
                        "Subject",
                        html_for="subject",
                        class_name=f"mb-1 text-sm font-medium {FONT_GEOGROTESK}",
                    ),
                    rx.el.input(
                        id="subject",
                        name="subject",
                        type="text",
                        required=True,
                        class_name=input_class,
                    ),
                    class_name="flex flex-col gap-1 w-full",
                ),
                rx.el.div(
                    rx.el.label(
                        "Message",
                        html_for="message",
                        class_name=f"mb-1 text-sm font-medium {FONT_GEOGROTESK}",
                    ),
                    rx.el.textarea(
                        id="message",
                        name="message",
                        required=True,
                        class_name=f"{input_class} min-h-[120px]",
                    ),
                    class_name="flex flex-col gap-1 w-full",
                ),
                rx.el.button(
                    "Send Message",
                    type="submit",
                    class_name=button_class,
                ),
                on_submit=SupportState.handle_submit,
                reset_on_submit=True,
                class_name="flex flex-col gap-4 items-center w-full",
            ),
        ),
        class_name="w-full max-w-2xl mx-auto",
    )


def faq_item(question: str, answer: str) -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            question,
            class_name=f"font-semibold text-lg text-[{HEADING_COLOR}]",
        ),
        rx.el.p(
            answer,
            class_name=f"mt-1 text-[{BODY_TEXT_COLOR}]",
        ),
        class_name="py-4 border-b border-gray-800",
    )


def support_page() -> rx.Component:
    return rx.el.div(
        navbar_component(),
        rx.el.main(
            rx.el.div(
                rx.el.h1(
                    "Support",
                    class_name=f"text-[2.5rem] {FONT_URBANSPLASH} font-bold text-[{HEADING_COLOR}] text-center mb-4",
                ),
                rx.el.div(
                    class_name=f"w-1/4 mx-auto h-[1px] bg-[{BORDER_COLOR}] mb-12"
                ),
                rx.el.h2(
                    "Frequently Asked Questions",
                    class_name=f"text-2xl {FONT_URBANSPLASH} font-bold text-[{HEADING_COLOR}] text-center mb-8",
                ),
                faq_item(
                    "How do I download my files after purchase?",
                    "After a successful purchase, you will be redirected to a download page. You will also receive an email with a download link.",
                ),
                faq_item(
                    "What file formats are included?",
                    "Most models are provided in STL format, which is compatible with most 3D printers. Some may include other formats like OBJ or FBX.",
                ),
                faq_item(
                    "Can I use the models for commercial projects?",
                    "By default, all models are for personal use only. If you need a commercial license, please contact us through the form below to discuss terms.",
                ),
                rx.el.h2(
                    "Contact Us",
                    class_name=f"text-2xl {FONT_URBANSPLASH} font-bold text-[{HEADING_COLOR}] text-center mt-16 mb-8",
                ),
                contact_form(),
                class_name="py-16 px-6 max-w-4xl mx-auto",
            ),
            class_name="flex-grow",
        ),
        footer_component(),
        class_name=f"min-h-screen bg-[{BG_COLOR}] text-[{PRIMARY_TEXT_COLOR}] flex flex-col {FONT_GEOGROTESK}",
    )