from playwright.sync_api import Page


class FlightSearchPage:

    def __init__(self, page: Page):
        self.page = page

        # Search fields
        self.from_city = page.get_by_test_id("flight-from")
        self.to_city = page.get_by_test_id("flight-to")
        self.departure_date = page.get_by_test_id("flight-departure-date")
        self.return_date = page.get_by_test_id("flight-return-date")
        self.passengers = page.get_by_test_id("flight-passengers")
        self.travel_class = page.get_by_test_id("flight-class")
        self.one_way = page.get_by_test_id("flight-one-way")

        # Search button
        self.search_button = page.get_by_test_id("flight-search")

        # Validation messages
        self.from_error = page.get_by_text(
            "Please select a departure city."
        )

        self.to_error = page.get_by_text(
            "Please select a destination city."
        )

        self.same_city_error = page.get_by_text(
            "Departure and destination cities cannot be the same."
        )

    def select_from_city(self, city):
        self.from_city.select_option(city)

    def select_to_city(self, city):
        self.to_city.select_option(city)

    def select_departure_date(self, date):
        self.departure_date.fill(date)

    def select_return_date(self, date):
        self.return_date.fill(date)

    def set_passengers(self, count):
        self.passengers.fill(str(count))

    def select_travel_class(self, travel_class):
        self.travel_class.select_option(travel_class)

    def select_one_way(self):
        if not self.one_way.is_checked():
            self.one_way.check()

    def search_flights(self):
        self.search_button.click()

    def is_return_date_visible(self):
        return self.return_date.is_visible()