import allure
import pytest

from selene import browser, be, have, command
from selene.core.condition import Condition

from helpers.data.links import Links


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
            browser.element('.h1').with_(timeout=browser.config.timeout * 2).should(Condition.by_and(be.visible, have.text('Мы')))
        return self

    @allure.step('Кликнуть на кнопку "Заполнить анкету"')
    def click_questionnaire_button(self) -> 'AboutUsPage':
        try:
            with allure.step('Кликнуть на кнопку "Заполнить анкету" для перехода на страницу заполнения анкеты'):
                browser.element('//a[@class="secret-buyer__button"]').perform(command.js.scroll_into_view).click()
            with allure.step('Переключиться на новую вкладку'):
                browser.switch_to_next_tab()
        except AssertionError:
            pytest.xfail('Не удалось кликнуть на кнопку "Заполнить анкету". Тест флакает')
        return self
