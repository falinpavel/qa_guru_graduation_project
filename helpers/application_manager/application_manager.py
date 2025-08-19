from helpers.pages.about_us_page.about_us_page import AboutUsPage
from helpers.pages.components.cart.cart import ComponentCart
from helpers.pages.components.header.header_menu import HeaderMenu
from helpers.pages.home_page.home_page import HomePage


class DodoApplicationManager:

    def __init__(self):
        self.home_page = HomePage()
        self.about_us_page = AboutUsPage()
        self.cart = ComponentCart()
        self.header_menu = HeaderMenu()


dodo = DodoApplicationManager()
