from playwright.sync_api import expect

from pages.flight_search_page import FlightSearchPage


def test_search_validation_for_empty_cities(page):

    # Open application
    page.goto("/flight-booking-scenarios")

    # Step 1 - Search
    search_page = FlightSearchPage(page)
    # Leave From and To empty
    search_page.search_flights()
    # Verify validation messages
    expect(search_page.from_error).to_have_text("Please select a departure city.")

    expect(search_page.to_error).to_have_text("Please select a destination city.")

    # Verify validation messages are visible
    expect(search_page.from_error).to_be_visible()
    expect(search_page.to_error).to_be_visible()

def test_same_origin_and_destination_validation(page):

    # Open application
    page.goto("/flight-booking-scenarios")

    # Step 1 - Search
    search_page = FlightSearchPage(page)

    search_page.select_from_city("New York")
    search_page.select_to_city("London")

    search_page.search_flights()

    # Verify validation message
    expect(
        search_page.same_city_error
    ).to_have_text(
        "Departure and destination cities cannot be the same."
    )

    # Verify validation message is visible
    expect(
        search_page.same_city_error
    ).to_be_visible()