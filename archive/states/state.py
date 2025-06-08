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
                "name": "Batarang",
                "image_url": "/placeholder.svg",
                "design_link": "https://sketchfab.com/archive.co/models",
                "is_new": True,
            },
            {
                "name": "Batarang (Graffiti)",
                "image_url": "/placeholder.svg",
                "design_link": "https://sketchfab.com/archive.co/models",
                "is_new": False,
            },
            {
                "name": "Papel Picado",
                "image_url": "/placeholder.svg",
                "design_link": "https://sketchfab.com/archive.co/models",
                "is_new": False,
            },
            {
                "name": "Project Alpha",
                "image_url": "/placeholder.svg",
                "design_link": "https://sketchfab.com/archive.co/models",
                "is_new": False,
            },
            {
                "name": "Project Beta",
                "image_url": "/placeholder.svg",
                "design_link": "https://sketchfab.com/archive.co/models",
                "is_new": False,
            },
            {
                "name": "Project Gamma",
                "image_url": "/placeholder.svg",
                "design_link": "https://sketchfab.com/archive.co/models",
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
            "link": "https://www.patreon.com/archive.co",
        },
        {
            "name": "Hobbyist",
            "price": "$5/month",
            "features": [
                "Access to the magazine",
                "Catalog of paid 3D files",
                "Regular catalog updates",
            ],
            "link": "https://www.patreon.com/archive.co",
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
            "link": "https://www.patreon.com/archive.co",
        },
    ]