import allure
from selene import browser, by, be, have
from selene.core.condition import Condition

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

    def change_location(self, new_location: str) -> 'HomePage':
        browser.element('[data-testid="header__about-slogan-text_link"]').click()
        browser.element('[data-testid="locality-selector-popup__search-input"]').click().type(
            new_location).press_enter()
        browser.element('[data-testid="header__about-slogan-text_link"]').should(have.text(new_location))
        return self

    def check_cart_is_empty(self) -> 'HomePage':
        browser.element('[data-testid="navigation__cart"]').click()
        browser.element('.empty h2').should(be.visible).should(have.text('Пока тут пусто'))
        browser.element('.empty div').should(be.visible).should(Condition.by_and(
            have.text('Добавьте пиццу. Или две!'), have.text('А мы доставим ваш заказ от 649 ₽')
        ))
        browser.element('.button-close').click()
        browser.element('.gwOFSm').should(be.not_.visible)
        return self
