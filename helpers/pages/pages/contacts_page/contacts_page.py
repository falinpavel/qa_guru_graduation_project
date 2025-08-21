import allure
from selene import browser, have

from helpers.config.links import Links


class ContactsPage:

    def __init__(self):
        self.url = Links.BASE_URL

    def open_with(self, location: str) -> 'ContactsPage':
        with allure.step(f'Открыть страницу "Контакты"'):
            browser.open(f'{self.url}/{location}{Links.CONTACTS_PAGE_URL}')
        return self

    def is_opened(self, location: str) -> 'ContactsPage':
        with allure.step(f'Проверить что открыта страница "Контакты"'):
            browser.should(have.url(f'{self.url}/{location}{Links.CONTACTS_PAGE_URL}'))
        return self
