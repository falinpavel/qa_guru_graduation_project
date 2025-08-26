import allure
from selene import browser, be, have
from selene.core.condition import Condition


class HeaderMenu:

    @allure.step('Кликнуть на таб "Прямой эфир"')
    def click_live_stream_tab(self) -> 'HeaderMenu':
        with allure.step('Кликнуть на таб "Прямой эфир"'):
            browser.element('.ieMmsb').click()
        return self

    @allure.step('Проверить активность таба "Прямой эфир"')
    def check_live_stream_is_active(self) -> 'HeaderMenu':
        browser.element('.bEPbwt').should(be.present)
        return self

    @allure.step('Проверить неактивность таба "Прямой эфир"')
    def check_live_stream_is_inactive(self) -> 'HeaderMenu':
        browser.element('.bEPbwt').should(be.not_.present)
        return self

    @allure.step('Кликнуть на таб "О нас"')
    def click_about_us_tab(self) -> 'HeaderMenu':
        with allure.step('Кликнуть на таб "О нас"'):
            browser.element('//a[text()="О нас"]').click()
        return self

    @allure.step('Кликнуть на таб "Контакты"')
    def click_contacts_tab(self) -> 'HeaderMenu':
        with allure.step('Кликнуть на таб "Контакты"'):
            browser.element('//a[text()="Контакты"]').click()
        return self

    @allure.step('Кликнуть на таб "Корпоративные заказы"')
    def click_corporate_orders_tab(self) -> 'HeaderMenu':
        with allure.step('Кликнуть на таб "Корпоративные заказы"'):
            browser.element('//a[text()="Корпоративные заказы"]').click()
        return self

    @allure.step('Кликнуть на таб "Подарочные сертификаты"')
    def click_gift_certificates_tab(self) -> 'HeaderMenu':
        with allure.step('Кликнуть на таб "Подарочные сертификаты"'):
            browser.element('//a[text()="Подарочные сертификаты"]').should(Condition.by_and(
                have.text('Подарочные сертификаты'), be.clickable)).click()
        return self

