import allure
from selene import browser, have, be
from selene.core.condition import Condition

from helpers.data.links import Links


class CorporateOrdersPage:

    def __init__(self):
        self.url = Links.BASE_URL

    @allure.step('Открыть страницу "Корпоративные заказы"')
    def open_with(self, location: str) -> 'CorporateOrdersPage':
        with allure.step(f'Открыть страницу "Корпоративные заказы"'):
            browser.open(f'{self.url}/{location}{Links.CORPORATE_ORDERS_PAGE_URL}')
        return self

    @allure.step('Проверить что открылся попап')
    def popup_is_opened(self) -> 'CorporateOrdersPage':
        with allure.step(f'Проверить что открылся попап'):
            browser.element('//h3[contains(text(),"Закажите в Додо на команду!")]').should(
                Condition.by_and(be.visible))
        return self

    @allure.step('Закрыть попап')
    def close_popup(self) -> 'CorporateOrdersPage':
        with allure.step(f'Закрыть попап'):
            browser.element('.popup-close-button').click()
        return self

    @allure.step('Проверить что открыта страница "Корпоративные заказы"')
    def is_opened(self, location: str) -> 'CorporateOrdersPage':
        with allure.step(f'Проверить что открыта страница "Корпоративные заказы"'):
            browser.should(have.url(f'{self.url}/{location}{Links.CORPORATE_ORDERS_PAGE_URL}'))
        return self
