from playwright.sync_api import expect

from pages.flight_search_page import FlightSearchPage
from pages.flight_selection_page import FlightSelectionPage
from pages.passenger_page import PassengerPage
from constants.flight_constants import DEPARTURE_DATE, TRAVEL_CLASS, FROM_CITY, TO_CITY, DEFAULT_PASSENGERS


def test_invalid_passenger_email(page):

    # Open application
    page.goto("/flight-booking-scenarios")

    # Step 1 - Search
    search_page = FlightSearchPage(page)

    search_page.select_from_city(FROM_CITY)
    search_page.select_to_city(TO_CITY)
    search_page.select_departure_date(DEPARTURE_DATE)
    search_page.set_passengers(DEFAULT_PASSENGERS)
    search_page.select_travel_class(TRAVEL_CLASS)
    search_page.select_one_way()
    search_page.search_flights()

    # Step 2 - Select flight
    selection_page = FlightSelectionPage(page)

    selection_page.select_flight("GW100")
    selection_page.continue_to_passengers()

    # Step 3 - Passenger details
    passenger_page = PassengerPage(page)

    passenger_page.enter_passenger_details(
        "Aman Sharma",
        "amansharma",
        "679845132"
    )

    passenger_page.continue_to_payment()

    # Verify email validation
    expect(
        passenger_page.email_error
    ).to_have_text(
        "Enter a valid email address."
    )

    expect(
        passenger_page.email_error
    ).to_be_visible()