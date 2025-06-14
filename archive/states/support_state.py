import reflex as rx


class SupportState(rx.State):
    form_data: dict[str, str] = {}
    submitted: bool = False

    def handle_submit(self, form_data: dict):
        """Handle the contact form submission."""
        self.form_data = form_data
        self.submitted = True
        print(f"Contact form submitted: {self.form_data}")
        return rx.toast.success(
            "Your message has been sent successfully!"
        )