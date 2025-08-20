import allure
from selene import browser, be, have, command
from selene.core.condition import Condition

from helpers.config.links import Links


class AboutUsPage:

    def __init__(self):
        self.url = Links.BASE_URL

    def open_with(self, location: str):
        with allure.step(f'Открыть страницу "О нас"'):
            browser.open(f'{self.url}/{location}{Links.ABOUT_US_PAGE_URL}')
        return self

    @allure.step('Проверить что открыта страница "О нас"')
    def is_opened(self):
        with allure.step(f'Проверить что открыта страница "О нас" и проверить контент (тайтлы)'):
            browser.element('.h1').should(Condition.by_and(have.text('Мы')))
            browser.element('//h2[text()="Идеальные ингредиенты"]').perform(
                command.js.scroll_into_view).should(Condition.by_and(have.text('Идеальные ингредиенты')))
            browser.element('//h2[text()="Одинаково вкусно в Москве и Сыктывкаре"]').perform(
                command.js.scroll_into_view).should(
                Condition.by_and(have.text('Одинаково вкусно в Москве и Сыктывкаре'))
            )
            browser.element('//h2[text()="Заморочились на цифрах"]').perform(
                command.js.scroll_into_view).should(Condition.by_and(have.text('Заморочились на цифрах')))
            browser.element('.refresh').should(be.visible).should(be.clickable).click()
            browser.element('//h2[text()="Единые стандарты"]').perform(
                command.js.scroll_into_view).should(Condition.by_and(have.text('Единые стандарты')))
            browser.element('//h2[text()="Открытость во всём"]').perform(
                command.js.scroll_into_view).should(Condition.by_and(have.text('Открытость во всём')))
            browser.element('//h2[text()="Открытость во всём"]').perform(
                command.js.scroll_into_view).should(Condition.by_and(have.text('Открытость во всём')))
            browser.element('//h2[text()="Почему Додо"]').perform(
                command.js.scroll_into_view).should(Condition.by_and(have.text('Почему Додо')))
        return self

    @allure.step('Клинкуть на кнопку "Заполнить анкету"')
    def click_questionnaire_button(self):
        with allure.step('Клинкуть на кнопку "Заполнить анкету" для перехода на страницу заполнения анкеты'):
            browser.element('.secret-buyer__button').perform(command.js.scroll_into_view).click()
            browser.switch_to_next_tab()
        return self
