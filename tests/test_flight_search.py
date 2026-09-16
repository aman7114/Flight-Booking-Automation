from pages.flight_search_page import FlightSearchPage


def test_return_date_hidden_for_one_way(page):

    page.goto("/flight-booking-scenarios")
    search_page = FlightSearchPage(page)
    search_page.select_one_way()
    assert not search_page.is_return_date_visible()