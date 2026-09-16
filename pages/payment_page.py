from playwright.sync_api import Page


class PaymentPage:

    def __init__(self, page: Page):
        self.page = page

        self.total = page.get_by_test_id("flight-total")
        self.card_number = page.get_by_test_id("flight-card-number")
        self.expiry = page.get_by_test_id("flight-expiry")
        self.cvv = page.get_by_test_id("flight-cvv")

        self.book_button = page.get_by_test_id("flight-book")

    def enter_payment_details(self, card_number, expiry, cvv):
        self.card_number.fill(card_number)
        self.expiry.fill(expiry)
        self.cvv.fill(cvv)

    def book_flight(self):
        self.book_button.click()