import reflex as rx
import asyncio
from typing import TypedDict


class MagazinePost(TypedDict):
    title: str
    image_url: str
    date: str
    read_more_url: str


class Project(TypedDict):
    name: str
    image_url: str
    embed_url: str
    model_url: str
    download_url: str
    purchase_url: str
    is_new: bool
    file_name: str


class Plan(TypedDict):
    name: str
    price: str
    features: list[str]
    link: str


class ShopProduct(TypedDict):
    name: str
    image_url: str
    embed_url: str
    model_url: str
    download_url: str
    purchase_url: str
    price: str
    is_new: bool
    file_name: str


class DownloadState(rx.State):
    file_name: str = ""

    @rx.var
    def download_url(self) -> str:
        return (
            f"https://cdn.archive.co/files/{self.file_name}.zip"
            if self.file_name
            else "#"
        )

    @rx.var
    def file_name_with_extension(self) -> str:
        return (
            f"{self.file_name}.zip"
            if self.file_name
            else ""
        )

    @rx.var
    def has_file(self) -> bool:
        return self.file_name != ""

    def on_load(self):
        self.file_name = self.router.page.params.get(
            "file", ""
        )


class MagazineState(rx.State):
    posts: list[MagazinePost] = [
        {
            "title": "Top 3D Models of 2024",
            "image_url": "/placeholder.svg",
            "date": "July 10, 2024",
            "read_more_url": "/magazine/top-models-2024",
        },
        {
            "title": "How the RetroBox Station was Designed",
            "image_url": "/placeholder.svg",
            "date": "July 5, 2024",
            "read_more_url": "/magazine/retrobox-design",
        },
        {
            "title": "Tips on Monetizing Your 3D Prints",
            "image_url": "/placeholder.svg",
            "date": "July 1, 2024",
            "read_more_url": "/magazine/monetizing-3d-prints",
        },
    ]

    @rx.var
    def latest_post(self) -> MagazinePost | None:
        if self.posts:
            return self.posts[0]
        return None


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
        projects_data: list[Project] = [
            {
                "name": "Batarang",
                "image_url": "/placeholder.svg",
                "embed_url": "https://sketchfab.com/models/85493032471649e0a03002f23aa88267/embed",
                "model_url": "https://sketchfab.com/3d-models/batarang-85493032471649e0a03002f23aa88267",
                "download_url": "#",
                "purchase_url": "/download_success?file=batarang",
                "is_new": True,
                "file_name": "batarang",
            },
            {
                "name": "Graffiti Spray Can",
                "image_url": "/placeholder.svg",
                "embed_url": "https://sketchfab.com/models/a931083988f44148b814a8e635f73752/embed",
                "model_url": "https://sketchfab.com/3d-models/graffiti-spray-paint-can-a931083988f44148b814a8e635f73752",
                "download_url": "#",
                "purchase_url": "/download_success?file=spraycan",
                "is_new": False,
                "file_name": "spraycan",
            },
            {
                "name": "Old Camera",
                "image_url": "/placeholder.svg",
                "embed_url": "https://sketchfab.com/models/ef0119e7a83b4815a51c4a919313a372/embed",
                "model_url": "https://sketchfab.com/3d-models/old-camera-ef0119e7a83b4815a51c4a919313a372",
                "download_url": "#",
                "purchase_url": "/download_success?file=oldcamera",
                "is_new": False,
                "file_name": "oldcamera",
            },
            {
                "name": "Cyberpunk Car",
                "image_url": "/placeholder.svg",
                "embed_url": "https://sketchfab.com/models/79493b8314e34195a7c29b1b7a9563d4/embed",
                "model_url": "https://sketchfab.com/3d-models/quadra-turbo-r-v-tech-cyberpunk-2077-79493b8314e34195a7c29b1b7a9563d4",
                "download_url": "#",
                "purchase_url": "/download_success?file=cyberpunkcar",
                "is_new": False,
                "file_name": "cyberpunkcar",
            },
            {
                "name": "Pixel Art Room",
                "image_url": "/placeholder.svg",
                "embed_url": "https://sketchfab.com/models/c632b7193f0b4bceb03d34a475514b13/embed",
                "model_url": "https://sketchfab.com/3d-models/isometric-low-poly-living-room-c632b7193f0b4bceb03d34a475514b13",
                "download_url": "#",
                "purchase_url": "/download_success?file=pixelroom",
                "is_new": False,
                "file_name": "pixelroom",
            },
            {
                "name": "Stylized Planet",
                "image_url": "/placeholder.svg",
                "embed_url": "https://sketchfab.com/models/904a601cf31843a693630f4e72aa1b41/embed",
                "model_url": "https://sketchfab.com/3d-models/a-stylized-planet-904a601cf31843a693630f4e72aa1b41",
                "download_url": "#",
                "purchase_url": "/download_success?file=stylizedplanet",
                "is_new": False,
                "file_name": "stylizedplanet",
            },
        ]
        async with self:
            self.projects = projects_data
            self.is_loading = False


class ShopState(rx.State):
    products: list[ShopProduct] = []
    is_loading: bool = True

    @rx.event(background=True)
    async def fetch_products(self):
        async with self:
            self.is_loading = True
        await asyncio.sleep(1)
        products_data: list[ShopProduct] = [
            {
                "name": "Batarang - Pro",
                "price": "$9.99",
                "image_url": "/placeholder.svg",
                "embed_url": "https://sketchfab.com/models/85493032471649e0a03002f23aa88267/embed",
                "model_url": "https://sketchfab.com/3d-models/batarang-85493032471649e0a03002f23aa88267",
                "download_url": "#",
                "purchase_url": "https://payhip.com/b/U2P0G",
                "is_new": True,
                "file_name": "batarang-pro",
            },
            {
                "name": "Graffiti Can - Pro",
                "price": "$4.99",
                "image_url": "/placeholder.svg",
                "embed_url": "https://sketchfab.com/models/a931083988f44148b814a8e635f73752/embed",
                "model_url": "https://sketchfab.com/3d-models/graffiti-spray-paint-can-a931083988f44148b814a8e635f73752",
                "download_url": "#",
                "purchase_url": "/download_success?file=spraycan-pro",
                "is_new": False,
                "file_name": "spraycan-pro",
            },
            {
                "name": "Old Camera - Pro",
                "price": "$12.50",
                "image_url": "/placeholder.svg",
                "embed_url": "https://sketchfab.com/models/ef0119e7a83b4815a51c4a919313a372/embed",
                "model_url": "https://sketchfab.com/3d-models/old-camera-ef0119e7a83b4815a51c4a919313a372",
                "download_url": "#",
                "purchase_url": "/download_success?file=oldcamera-pro",
                "is_new": False,
                "file_name": "oldcamera-pro",
            },
        ]
        async with self:
            self.products = products_data
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