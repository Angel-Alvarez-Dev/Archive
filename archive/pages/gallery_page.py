import reflex as rx
from archive.components.header_component import header_component
from archive.components.footer_component import footer_component
from archive.components.project_card_component import (
    project_card_component,
)
from archive.components.navbar_component import navbar_component
from archive.states.state import GalleryState

BG_COLOR = "#121212"
CARD_BG_COLOR = "#1E1E1E"
HEADING_COLOR = "#E0E0E0"
BODY_TEXT_COLOR = "#B0B0B0"
BORDER_COLOR = "#2C5F2D"
FONT_URBANSPLASH = "font-['Urbanist',_sans-serif]"
FONT_GEOGROTESK = "font-['Inter',_sans-serif]"


def skeleton_loader() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            class_name="h-[61px] bg-gray-700/50 rounded-t-2xl"
        ),
        rx.el.div(class_name="aspect-video bg-gray-700/50"),
        rx.el.div(class_name="p-4 h-[76px]"),
        class_name=f"bg-[{CARD_BG_COLOR}] rounded-2xl border border-[{BORDER_COLOR}] w-full overflow-hidden animate-pulse",
    )


def gallery_page() -> rx.Component:
    section_spacing = "my-16"
    return rx.el.div(
        navbar_component(),
        rx.el.div(
            header_component(),
            rx.el.div(
                rx.el.h1(
                    "Project Gallery",
                    class_name=f"text-[2rem] {FONT_URBANSPLASH} font-bold text-[{HEADING_COLOR}] text-center mb-1",
                ),
                rx.el.div(
                    class_name=f"w-1/2 mx-auto h-[1px] bg-[{BORDER_COLOR}] mb-8"
                ),
                class_name=f"{section_spacing} text-center",
            ),
            rx.el.div(
                rx.cond(
                    GalleryState.is_loading,
                    rx.fragment(
                        skeleton_loader(),
                        skeleton_loader(),
                        skeleton_loader(),
                        skeleton_loader(),
                        skeleton_loader(),
                        skeleton_loader(),
                    ),
                    rx.foreach(
                        GalleryState.projects,
                        lambda project: project_card_component(
                            project_name=project["name"],
                            image_url=project["image_url"],
                            model_url=project["model_url"],
                            embed_url=project["embed_url"],
                            download_url=project[
                                "download_url"
                            ],
                            purchase_url=project[
                                "purchase_url"
                            ],
                            is_new=project.get(
                                "is_new", False
                            ),
                            file_name=project.get(
                                "file_name", ""
                            ),
                        ),
                    ),
                ),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-2 gap-y-8 gap-x-8 px-4 md:px-8 max-w-6xl mx-auto",
            ),
            footer_component(),
            class_name=f"max-w-7xl mx-auto px-4 {FONT_GEOGROTESK}",
        ),
        class_name=f"min-h-screen bg-[{BG_COLOR}] text-white py-8",
        on_mount=GalleryState.fetch_projects,
    )