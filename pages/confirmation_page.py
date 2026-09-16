from playwright.sync_api import Page


class ConfirmationPage:

    def __init__(self, page: Page):
        self.page = page

        self.booking_success = page.get_by_test_id(
            "flight-booking-success"
        )

        self.pnr = page.get_by_test_id("flight-pnr")

    def is_booking_confirmed(self):
        return self.booking_success.is_visible()

    def get_booking_reference(self):
        return self.pnr.inner_text()