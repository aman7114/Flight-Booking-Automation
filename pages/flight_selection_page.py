from playwright.sync_api import Page


class FlightSelectionPage:

    def __init__(self, page: Page):
        self.page = page

        self.sort_dropdown = page.get_by_test_id("flight-sort")
        self.airline_filter = page.get_by_test_id("flight-filter-airline")
        self.nonstop_filter = page.get_by_test_id("flight-filter-nonstop")

        self.continue_button = page.get_by_test_id(
            "flight-continue-to-passengers"
        )

        self.flight_prices = page.locator(
            '[data-testid^="flight-result-"] h5.text-primary'
        )

        self.flight_results = page.locator(
            '[data-testid^="flight-result-"]:visible'
        )

    def sort_by_price_low_to_high(self):
        self.sort_dropdown.select_option("price-asc")

    def filter_by_airline(self, airline):
        self.airline_filter.select_option(airline)

    def select_nonstop(self):
        if not self.nonstop_filter.is_checked():
            self.nonstop_filter.check()

    def get_visible_flight_results(self):
        return self.flight_results.all_inner_texts()

    def select_flight(self, flight_number):
        self.page.get_by_test_id(
            f"flight-select-{flight_number}"
        ).click()

    def get_flight_prices(self):
        prices = self.flight_prices.all_inner_texts()

        return [
            int(price.replace("$", "").strip())
            for price in prices
        ]

    def is_continue_enabled(self):
        return self.continue_button.is_enabled()

    def continue_to_passengers(self):
        self.continue_button.click()