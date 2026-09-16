from playwright.sync_api import Page


class PassengerPage:

    def __init__(self, page: Page):
        self.page = page

        self.name = page.get_by_test_id("flight-passenger-name")
        self.email = page.get_by_test_id("flight-passenger-email")
        self.phone = page.get_by_test_id("flight-passenger-phone")

        self.continue_button = page.get_by_test_id("flight-continue-to-payment")

        self.email_error = page.get_by_text("Enter a valid email address.")

    def enter_passenger_details(self, name, email, phone):
        self.name.fill(name)
        self.email.fill(email)
        self.phone.fill(phone)

    def continue_to_payment(self):
        self.continue_button.click()