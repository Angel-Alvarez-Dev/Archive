import reflex as rx
import asyncio
from typing import TypedDict

class Project(TypedDict):
    name: str
    image_url: str
    design_link: str
    is_new: bool


class Plan(TypedDict):
    name: str
    price: str
    features: list[str]
    link: str


class HomeState(rx.State):
    subscribed: bool = False

    def handle_subscribe(self, form_data: dict):
        email = form_data.get("email", "")
        if not email or "@" not in email:
            return rx.toast.error(
                "Please enter a valid email address."
            )
        print(f"Subscribing email: {email}")
        self.subscribed = True


class GalleryState(rx.State):
    projects: list[Project] = []
    is_loading: bool = True

    @rx.event(background=True)
    async def fetch_projects(self):
        async with self:
            self.is_loading = True
        await asyncio.sleep(1)
        projects_data = [
    {
        "name": "Kobe Bryant Deluxe",
        "image_url": "/img/Kobe-Bryant.webp",
        "design_link": "https://cults3d.com/:2577977",
        "is_new": True,
    },
    {
        "name": "LeBron James",
        "image_url": "/img/Lebron-James.webp",
        "design_link": "https://cults3d.com/:2570894",
        "is_new": True,
    },
    {
        "name": "Kyrie Irving",
        "image_url": "/img/Kyrie-Irving.webp",
        "design_link": "https://cults3d.com/:2571048",
        "is_new": True,
    },
    {
        "name": "Batarang Graffiti",
        "image_url": "/img/Batarang-Graffiti.webp",
        "design_link": "https://cults3d.com/:2205748",
        "is_new": True,
    },
    {
        "name": "Travis Scott",
        "image_url": "/img/Travis-Scott.webp",
        "design_link": "https://cults3d.com/:2568176",
        "is_new": True,
    },
    {
        "name": "Papel Picado",
        "image_url": "/img/Papel-Picado.webp",
        "design_link": "https://cults3d.com/:2323614",
        "is_new": False,
    },
    {
        "name": "Cartoon Bomb",
        "image_url": "/img/Cartoon-Bomb.webp",
        "design_link": "https://cults3d.com/:2198787",
        "is_new": False,
    },
    {
        "name": "Pixel Cherries",
        "image_url": "/img/Pixel-Cherrys.webp",
        "design_link": "https://cults3d.com/:2641869",
        "is_new": False,
    },
    {
        "name": "Pixel A",
        "image_url": "/img/Pixel-A.webp",
        "design_link": "https://cults3d.com/:2642125",
        "is_new": False,
    },
]



        async with self:
            self.projects = projects_data
            self.is_loading = False


class SubscribeState(rx.State):
    plans: list[Plan] = [
        {
            "name": "Free",
            "price": "Free",
            "features": [
                "Access to the magazine",
                "Free 3D files",
            ],
            "link": "patreon.com/Archive_co",
        },
        {
            "name": "Hobbyist",
            "price": "$5/month",
            "features": [
                "Access to the magazine",
                "Catalog of paid 3D files",
                "Regular catalog updates",
            ],
            "link": "patreon.com/Archive_co",
        },
        {
            "name": "Creator",
            "price": "$20/month",
            "features": [
                "Access to the magazine",
                "Complete catalog of paid 3D files",
                "Early access to files",
                "Custom 3D files",
                "Direct communication line",
            ],
            "link": "patreon.com/Archive_co",
        },
    ]