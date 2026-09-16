from playwright.sync_api import expect

from pages.flight_search_page import FlightSearchPage
from pages.flight_selection_page import FlightSelectionPage
from pages.passenger_page import PassengerPage
from pages.payment_page import PaymentPage
from pages.confirmation_page import ConfirmationPage

from test_data.flight_data import FLIGHT_DATA, ROUND_TRIP_DATA


def test_one_way_flight_booking(page):

    # Open application
    page.goto("/flight-booking-scenarios")

    # Step 1 - Search
    search_page = FlightSearchPage(page)

    search_page.select_from_city(FLIGHT_DATA["from_city"])
    search_page.select_to_city(FLIGHT_DATA["to_city"])
    search_page.select_departure_date(
        FLIGHT_DATA["departure_date"]
    )
    search_page.set_passengers(
        FLIGHT_DATA["passengers"]
    )
    search_page.select_travel_class(
        FLIGHT_DATA["travel_class"]
    )
    search_page.select_one_way()
    search_page.search_flights()

    # Step 2 - Select flight
    selection_page = FlightSelectionPage(page)

    selection_page.sort_by_price_low_to_high()
    selection_page.select_flight(
        FLIGHT_DATA["flight_number"]
    )
    selection_page.continue_to_passengers()

    # Step 3 - Passenger details
    passenger_page = PassengerPage(page)

    passenger_page.enter_passenger_details(
        FLIGHT_DATA["passenger_name"],
        FLIGHT_DATA["passenger_email"],
        FLIGHT_DATA["passenger_phone"]
    )

    passenger_page.continue_to_payment()

    # Step 4 - Payment
    payment_page = PaymentPage(page)

    payment_page.enter_payment_details(
        FLIGHT_DATA["card_number"],
        FLIGHT_DATA["expiry"],
        FLIGHT_DATA["cvv"]
    )

    payment_page.book_flight()

    # Step 5 - Confirmation
    confirmation_page = ConfirmationPage(page)

    expect(
        confirmation_page.booking_success
    ).to_contain_text("Booking Confirmed")

    assert confirmation_page.is_booking_confirmed()

    pnr = confirmation_page.get_booking_reference()

    assert pnr

def test_round_trip_flight_booking(page):
    # Open application
    page.goto("/flight-booking-scenarios")
    # Step 1 - Search
    search_page = FlightSearchPage(page)
    search_page.select_from_city(ROUND_TRIP_DATA["from_city"])
    search_page.select_to_city(
        ROUND_TRIP_DATA["to_city"]
    )
    search_page.select_departure_date(
        ROUND_TRIP_DATA["departure_date"]
    )
    search_page.select_return_date(
        ROUND_TRIP_DATA["return_date"]
    )
    search_page.set_passengers(
        ROUND_TRIP_DATA["passengers"]
    )
    search_page.select_travel_class(
        ROUND_TRIP_DATA["travel_class"]
    )

    search_page.search_flights()

    # Step 2 - Select flights
    selection_page = FlightSelectionPage(page)
    selection_page.sort_by_price_low_to_high()

    # Select outbound flight
    selection_page.select_flight(
        ROUND_TRIP_DATA["departure_flight_number"]
    )
    #   Select return flight
    selection_page.select_flight(
        ROUND_TRIP_DATA["return_flight_number"]
    )
    selection_page.continue_to_passengers()

    # Step 3 - Passenger details
    passenger_page = PassengerPage(page)

    passenger_page.enter_passenger_details(
        ROUND_TRIP_DATA["passenger_name"],
        ROUND_TRIP_DATA["passenger_email"],
        ROUND_TRIP_DATA["passenger_phone"]
    )
    passenger_page.continue_to_payment()

    # Step 4 - Payment
    payment_page = PaymentPage(page)

    payment_page.enter_payment_details(
        ROUND_TRIP_DATA["card_number"],
        ROUND_TRIP_DATA["expiry"],
        ROUND_TRIP_DATA["cvv"]
    )

    payment_page.book_flight()

    # Step 5 - Confirmation
    confirmation_page = ConfirmationPage(page)
    expect(
        confirmation_page.booking_success
    ).to_contain_text("Booking Confirmed")

    assert confirmation_page.is_booking_confirmed()
    pnr = confirmation_page.get_booking_reference()
    assert pnr