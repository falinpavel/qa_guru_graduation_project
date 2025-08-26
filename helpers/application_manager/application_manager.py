from helpers.pages.pages.about_us_page.about_us_page import AboutUsPage
from helpers.pages.components.cart.cart import ComponentCart
from helpers.pages.components.header.header_menu import HeaderMenu
from helpers.pages.pages.about_us_page.dodo_control_page.control_page import DodoControlPage
from helpers.pages.pages.contacts_page.contacts_page import ContactsPage
from helpers.pages.pages.corporate_orders_page.corporate_orders_page import CorporateOrdersPage
from helpers.pages.pages.gift_certificates_page.gift_certificates_page import GiftCertificatesPage
from helpers.pages.pages.home_page.home_page import HomePage
from helpers.pages.pages.home_page.products.combo_group.home_page_combo_group import HomePageComboGroup
from helpers.pages.pages.home_page.products.pizza_group.home_page_pizza_group import HomePagePizzaGroup
from helpers.pages.pages.home_page.products.roman_pizza_group.home_page_roman_pizza_group import HomePageRomanPizzaGroup
from helpers.pages.pages.home_page.products.snacks_group.home_page_snacks_group import HomePageSnacksGroup


class DodoApplicationManager:

    def __init__(self):

        self.home_page = HomePage()

        self.cart = ComponentCart()
        self.header_menu = HeaderMenu()

        self.home_page_pizza_group = HomePagePizzaGroup()
        self.home_page_roman_pizza_group = HomePageRomanPizzaGroup()
        self.home_page_combo_group = HomePageComboGroup()
        self.home_page_snacks_group = HomePageSnacksGroup()

        self.about_us_page = AboutUsPage()
        self.dodo_control_page = DodoControlPage()

        self.contacts_page = ContactsPage()

        self.corporate_orders_page = CorporateOrdersPage()

        self.gift_certificates_page = GiftCertificatesPage()


dodo = DodoApplicationManager()
