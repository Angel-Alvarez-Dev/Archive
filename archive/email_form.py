import reflex as rx
import re
from archive.db import save_email

class HomeState(rx.State):
    subscribed: bool = False

    def handle_subscribe(self, form_data: dict):
        email = form_data.get("email", "").strip()

        if not email or "@" not in email:
            return rx.toast.error("Please enter a valid email address.")

        if save_email(email):
            self.subscribed = True
            return rx.toast.success("You're in! Welcome to archive.co.")
        else:
            return rx.toast.warning("This email is already registered.")

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

class EmailFormState(rx.State):
    email: str = ""
    message: str = ""

    def submit_email(self):
        if not EMAIL_REGEX.fullmatch(self.email):
            self.message = "Invalid email address."
            return
        if save_email(self.email):
            self.message = "You're in! 🎉"
            self.email = ""
        else:
            self.message = "Email already registered."
