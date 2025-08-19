from helpers.application_manager.application_manager import dodo


class TestDodoHomePage:

    def test_register_user(self):
        dodo.home_page.open()
        dodo.home_page.choose_location()
