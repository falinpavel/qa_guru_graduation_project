from helpers.application_manager.application_manager import dodo


class TestDodoHomePage:

    def test_change_location(self):
        dodo.home_page.open_with(location='moscow')
        dodo.home_page.change_location(new_location='Краснодар')

    def test_open_live_stream(self):
        dodo.home_page.open_with(location='moscow').check_live_stream()

    def test_that_cart_is_empty(self):
        dodo.home_page.open_with(location='moscow').check_cart_is_empty()
