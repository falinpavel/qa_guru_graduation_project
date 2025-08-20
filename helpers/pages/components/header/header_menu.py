import allure
from selene import browser, be


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
