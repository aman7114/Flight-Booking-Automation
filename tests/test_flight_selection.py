from pages.flight_search_page import FlightSearchPage
from pages.flight_selection_page import FlightSelectionPage


def test_sort_flights_by_price_low_to_high(page):

    # Open application
    page.goto("/flight-booking-scenarios")

    # Step 1 - Search
    search_page = FlightSearchPage(page)

    search_page.select_from_city("New York")
    search_page.select_to_city("London")
    search_page.select_departure_date("2026-09-18")
    search_page.set_passengers(1)
    search_page.select_travel_class("Economy")
    search_page.select_one_way()
    search_page.search_flights()

    # Step 2 - Select flight
    selection_page = FlightSelectionPage(page)

    # Sort by price: Low to High
    selection_page.sort_by_price_low_to_high()

    # Get displayed flight prices
    prices = selection_page.get_flight_prices()

    # Verify prices are in ascending order
    assert prices == sorted(prices)

def test_filter_nonstop_flights(page):

    # Open application
    page.goto("/flight-booking-scenarios")

    # Step 1 - Search
    search_page = FlightSearchPage(page)

    search_page.select_from_city("New York")
    search_page.select_to_city("London")
    search_page.select_departure_date("2026-09-18")
    search_page.set_passengers(1)
    search_page.select_travel_class("Economy")
    search_page.select_one_way()
    search_page.search_flights()

    # Step 2 - Select flight
    selection_page = FlightSelectionPage(page)

    # Apply Non-stop filter
    selection_page.select_nonstop()

    # Verify filter is applied
    assert selection_page.nonstop_filter.is_checked()

    # Get visible flights
    flights = selection_page.get_visible_flight_results()

    # Verify every visible flight is Non-stop
    for flight in flights:
        assert "Non-stop" in flight

def test_continue_button_disabled_until_flight_selected(page):

    # Open application
    page.goto("/flight-booking-scenarios")

    # Step 1 - Search
    search_page = FlightSearchPage(page)

    search_page.select_from_city("New York")
    search_page.select_to_city("London")
    search_page.select_departure_date("2026-09-18")
    search_page.set_passengers(1)
    search_page.select_travel_class("Economy")
    search_page.select_one_way()
    search_page.search_flights()

    # Step 2 - Select flight
    selection_page = FlightSelectionPage(page)

    # Continue should be disabled initially
    assert not selection_page.is_continue_enabled()

    # Select a flight
    selection_page.select_flight("GW100")

    # Continue should now be enabled
    assert selection_page.is_continue_enabled()