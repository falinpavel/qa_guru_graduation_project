from helpers.pages.components.cart import ComponentCart
from helpers.pages.components.header_menu import HeaderMenu
from helpers.pages.home_page.home_page import HomePage


class DodoApplicationManager:

    def __init__(self):
        self.home_page = HomePage()
        self.cart = ComponentCart()
        self.header_menu = HeaderMenu()


dodo = DodoApplicationManager()
