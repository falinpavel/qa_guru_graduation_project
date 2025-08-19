import allure
from selene import browser, be, have

from helpers.config.links import Links


class HomePage:

    def __init__(self):
        self.url = Links.BASE_URL

    @allure.step(f'Открыть главную страницу')
    def open_with(self, location: str) -> 'HomePage':
        with allure.step(f'Открыть главную страницу для города {location}'):
            browser.open(f'{self.url}/{location}')
        with allure.step(f'Проверить что открыта главная страница для города {location}'):
            browser.should(have.url(f'{self.url}/{location}'))
        return self

    @allure.step('Изменить город из главной страницы')
    def change_location(self, new_location: str) -> 'HomePage':
        with allure.step('Кликнуть кнопку-ссылку уже выбранного города'):
            browser.element('[data-testid="header__about-slogan-text_link"]').should(be.visible).click()
        with allure.step('Ввести в поле поиска новый город'):
            browser.element('[data-testid="locality-selector-popup__search-input"]').should(be.visible).click().type(
                new_location).press_enter()
        with allure.step('Проверить что открылась страница с новым городом'):
            browser.element('[data-testid="header__about-slogan-text_link"]').should(have.text(new_location))
        return self
