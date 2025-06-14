import reflex as rx
from archive.components.navbar_component import navbar_component
from archive.components.footer_component import footer_component
from archive.states.state import DownloadState

BG_COLOR = "#121212"
PRIMARY_TEXT_COLOR = "#E0E0E0"
HEADING_COLOR = "#E0E0E0"
BODY_TEXT_COLOR = "#B0B0B0"
ACCENT_COLOR = "#2C5F2D"
BORDER_COLOR = "#2C5F2D"
BORDER_HOVER_COLOR = "#3A7F3D"
FONT_URBANSPLASH = "font-['Urbanist',_sans-serif]"
FONT_GEOGROTESK = "font-['Inter',_sans-serif]"


def download_success_page() -> rx.Component:
    download_button_class = f"w-full max-w-xs {FONT_GEOGROTESK} text-black border-2 border-[{ACCENT_COLOR}] bg-[{ACCENT_COLOR}] py-3 px-6 rounded-2xl hover:bg-[{BORDER_HOVER_COLOR}] hover:border-[{BORDER_HOVER_COLOR}] focus:outline-none focus:ring-2 focus:ring-[{ACCENT_COLOR}] focus:ring-offset-2 focus:ring-offset-black transition-all duration-300 transform hover:-translate-y-0.5 active:scale-95 text-[1rem] font-semibold"
    return rx.el.div(
        navbar_component(),
        rx.el.main(
            rx.el.div(
                rx.el.h1(
                    "Download Ready",
                    class_name=f"text-[2.5rem] {FONT_URBANSPLASH} font-bold text-[{HEADING_COLOR}] text-center mb-4",
                ),
                rx.el.p(
                    "Thank you for your purchase.",
                    class_name=f"text-lg text-[{BODY_TEXT_COLOR}] text-center mb-8 {FONT_GEOGROTESK}",
                ),
                rx.cond(
                    DownloadState.has_file,
                    rx.el.a(
                        "Download File",
                        href=DownloadState.download_url,
                        download=DownloadState.file_name_with_extension,
                        class_name=download_button_class,
                    ),
                    rx.el.p(
                        "No file specified for download. Please contact support.",
                        class_name=f"text-center text-red-500 {FONT_GEOGROTESK}",
                    ),
                ),
                class_name="flex flex-col items-center justify-center text-center p-8 rounded-2xl bg-[#1E1E1E] border border-[#2C5F2D] shadow-lg max-w-2xl mx-auto",
            ),
            class_name="flex-grow flex items-center justify-center",
        ),
        footer_component(),
        class_name=f"min-h-screen bg-[{BG_COLOR}] text-[{PRIMARY_TEXT_COLOR}] flex flex-col {FONT_GEOGROTESK}",
        on_mount=DownloadState.on_load,
    )