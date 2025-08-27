import allure
from selene import browser, have, be
from selene.core.condition import Condition

from helpers.data.links import Links


class GiftCertificatesPage:

    def __init__(self):
        self.url = f"{Links.BASE_URL}{Links.GIFT_CERTIFICATES_PAGE_URL}"

    @allure.step('Открыть страницу "Подарочные сертификаты"')
    def open_with(self) -> 'GiftCertificatesPage':
        with allure.step(f'Открыть страницу "Корпоративные заказы"'):
            browser.open(self.url)
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
    def page_is_opened(self) -> 'GiftCertificatesPage':
        with allure.step(f'Проверить что открыта страница "Подарочные сертификаты"'):
            browser.should(have.url(self.url))
            browser.element('[data-testid="order-button"]').should(
                Condition.by_and(be.clickable, have.text('Заказать')))
        return self

    @allure.step('В попапе нажать на кнопку "Понятно"')
    def click_accept_in_popup(self):
        with allure.step('Если выбран "Для друзей и близких" то в попапе нажать на кнопку "Понятно"'):
            browser.element('//button[contains(text(),"Понятно")]').should(Condition.by_and(be.clickable)).click()

    @allure.step('Нажать на кнопку выбора "Для кого сертификаты?"')
    def select_and_click_the_recipient(self, a_gift_for: str) -> 'GiftCertificatesPage':
        with allure.step(f'В попапе нажать на кнопку "{a_gift_for}"'):
            if a_gift_for == 'Для сотрудников':
                browser.element(f'//button[text()="{a_gift_for}"]').should(Condition.by_and(be.clickable)).click()
            else:
                with allure.step('Кликнуть на "Для другей и близких" и проверить что в попапе отображается '
                                 'подсказка о недоступности такой покупки'):
                    browser.element(f'//button[text()="{a_gift_for}"]').should(Condition.by_and(be.clickable)).click()
                    browser.element('//h2[@class="title"]').should(Condition.by_and(
                        have.text('Таких сертификатов нет, но мы учли ваш ответ')))
        return self

    @allure.step('Нажать на кнопку "Заказать"')
    def click_order_button(self) -> 'GiftCertificatesPage':
        with allure.step('Нажать на кнопку "Заказать" на странице'):
            browser.element('[data-testid="order-button"]').should(Condition.by_and(be.clickable)).click()
        return self

    @allure.step('Вернуться назад на главную')
    def click_close_button_and_go_to_home(self) -> 'GiftCertificatesPage':
        with allure.step('Нажать на крестик на странице "Сертификаты" что бы вернуться на главную страницу'):
            browser.element('.header-right').should(Condition.by_and(be.visible, be.clickable)).click()
        return self
