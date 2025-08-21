import allure

from selene import browser, be, have, command
from selene.core.condition import Condition

from helpers.config.links import Links


class AboutUsPage:

    def __init__(self):
        self.url = Links.BASE_URL

    def open_with(self, location: str) -> 'AboutUsPage':
        with allure.step(f'Открыть страницу "О нас"'):
            browser.open(f'{self.url}/{location}{Links.ABOUT_US_PAGE_URL}')
        return self

    @allure.step('Проверить что открыта страница "О нас"')
    def is_opened(self, location: str) -> 'AboutUsPage':
        with allure.step(f'Проверить что открыта страница с правильной ссылкой'):
            browser.should(have.url(f'{self.url}/{location}{Links.ABOUT_US_PAGE_URL}'))
        with allure.step(f'Проверить что открыта страница и на ней отображается h1 "Мы"'):
            browser.element('.h1').should(Condition.by_and(have.text('Мы')))
        with allure.step(f'Проверить что открыта страница и на ней отображается текст "Идеальные ингредиенты"'):
            browser.element('//h2[text()="Идеальные ингредиенты"]').perform(
                command.js.scroll_into_view).should(Condition.by_and(have.text('Идеальные ингредиенты')))
        with allure.step(f'Проверить что открыта страница и на ней отображается текст "Одинаково вкусно в... '):
            browser.element('//h2[text()="Одинаково вкусно в Москве и Сыктывкаре"]').perform(
                command.js.scroll_into_view).should(
                Condition.by_and(have.text('Одинаково вкусно в Москве и Сыктывкаре'))
            )
        with allure.step(f'Проверить что открыта страница и на ней отображается текст "Заморочились на цифрах"'):
            browser.element('//h2[text()="Заморочились на цифрах"]').perform(
                command.js.scroll_into_view).should(Condition.by_and(have.text('Заморочились на цифрах')))
        with allure.step(f'Проверить что Кнопка "Обновить" функциональна'):
            browser.element('.refresh').should(be.visible).should(be.clickable).click()
        with allure.step(f'Проверить что открыта страница и на ней отображается текст "Единые стандарты"'):
            browser.element('//h2[text()="Единые стандарты"]').perform(
                command.js.scroll_into_view).should(Condition.by_and(have.text('Единые стандарты')))
        with allure.step(f'Проверить что открыта страница и на ней отображается текст "Открытость во всём"'):
            browser.element('//h2[text()="Открытость во всём"]').perform(
                command.js.scroll_into_view).should(Condition.by_and(have.text('Открытость во всём')))
        with allure.step(f'Проверить что открыта страница и на ней отображается текст "Почему Додо"'):
            browser.element('//h2[text()="Открытость во всём"]').perform(
                command.js.scroll_into_view).should(Condition.by_and(have.text('Открытость во всём')))
        with allure.step(f'Проверить что открыта страница и на ней отображается текст "Почему Додо"'):
            browser.element('//h2[text()="Почему Додо"]').perform(
                command.js.scroll_into_view).should(Condition.by_and(have.text('Почему Додо')))
        return self

    @allure.step('Кликнуть на кнопку "Заполнить анкету"')
    def click_questionnaire_button(self) -> 'AboutUsPage':
        with allure.step('Кликнуть на кнопку "Заполнить анкету" для перехода на страницу заполнения анкеты'):
            browser.element('.secret-buyer__button').perform(command.js.scroll_into_view).click()
        with allure.step('Переключиться на новую вкладку'):
            browser.switch_to_next_tab()
        return self
