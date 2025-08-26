import allure
from selene import browser, have, be
from selene.core.condition import Condition

from helpers.data.links import Links


class GiftCertificatesPage:

    def __init__(self):
        self.url = Links.BASE_URL

    @allure.step('Открыть страницу "Подарочные сертификаты"')
    def open_with(self, location: str) -> 'GiftCertificatesPage':
        with allure.step(f'Открыть страницу "Корпоративные заказы"'):
            browser.open(f'{self.url}/{location}{Links.GIFT_CERTIFICATES_PAGE_URL}')
        return self

    @allure.step('Проверить что открылся попап')
    def popup_is_opened(self) -> 'GiftCertificatesPage':
        with allure.step(f'Проверить что открылся попап'):
            browser.element('//h2[@class="title"]').should(Condition.by_and(have.text('Для кого сертификаты?')))
        return self

    @allure.step('Закрыть попап')
    def close_popup(self) -> 'GiftCertificatesPage':
        with allure.step(f'Закрыть попап'):
            browser.element('.popup-close-button').click()
        return self

    @allure.step('Проверить что открыта страница "Подарочные сертификаты"')
    def is_opened(self, location: str) -> 'GiftCertificatesPage':
        with allure.step(f'Проверить что открыта страница "Подарочные сертификаты"'):
            browser.should(have.url(f'{self.url}/{location}{Links.GIFT_CERTIFICATES_PAGE_URL}'))
        return self
