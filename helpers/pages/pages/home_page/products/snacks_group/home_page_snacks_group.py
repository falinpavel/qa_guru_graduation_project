import allure
from selene import browser, have


class HomePageSnacksGroup:

    @allure.step('Перейти в группу "Пицца" кликнув на кнопку "Пицца" на главной странице')
    def click_roman_pizza_group(self) -> 'HomePageSnacksGroup':
        with allure.step('Клик на кнопку "Пиццы"'):
            browser.element('//a[contains(text(),"Закуски")]').should(have.text('Закуски')).click()
        return self
