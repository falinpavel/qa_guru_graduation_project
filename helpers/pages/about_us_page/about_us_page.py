import allure
from selene import browser, be, have, command

from helpers.config.links import Links


class AboutUsPage:

    def __init__(self):
        self.url = Links.BASE_URL

    def open_with(self, location: str):
        with allure.step(f'Открыть страницу "О нас"'):
            browser.open(f'{self.url}/{location}{Links.ABOUT_US_PAGE_URL}')
        return self

    def is_opened(self):
        with allure.step(f'Проверить что открыта страница "О нас"'):
            browser.element('.h1').should(have.text('Мы'))
            browser.element('//h2[text()="Идеальные ингредиенты"]').perform(
                command.js.scroll_into_view).should(be.visible)
            browser.element('//h2[text()="Одинаково вкусно в Москве и Сыктывкаре"]').perform(
                command.js.scroll_into_view).should(be.visible)
            browser.element('//h2[text()="Заморочились на цифрах"]').perform(
                command.js.scroll_into_view).should(be.visible)
            browser.element('.refresh').click()
            browser.element('//h2[text()="Единые стандарты"]').perform(
                command.js.scroll_into_view).should(be.visible)
            browser.element('//h2[text()="Открытость во всём"]').perform(
                command.js.scroll_into_view).should(be.visible)
            browser.element('//h2[text()="Открытость во всём"]').perform(
                command.js.scroll_into_view).should(be.visible)
            browser.element('//h2[text()="Почему Додо"]').perform(
                command.js.scroll_into_view).should(be.visible)
        return self
