import allure
from selene import browser, have


class HomePageRomanPizzaGroup:

    @allure.step('Перейти в группу "Пицца" кликнув на кнопку "Пицца" на главной странице')
    def click_roman_pizza_group(self) -> 'HomePageRomanPizzaGroup':
        with allure.step('Клик на кнопку "Пиццы"'):
            browser.element('//a[contains(text(),"Римские пиццы")]').should(have.text('Римские пиццы')).click()
        return self

    @allure.step('Кликнуть на конкретную римскую пиццу в группе "Римские пиццы" и перейти в попап')
    def click_roman_pizza_and_open_popup(self, roman_pizza_name) -> 'HomePageRomanPizzaGroup':
        with allure.step(f'Кликнуть на пиццу {roman_pizza_name}'):
            browser.element(f'//span[contains(text(),"{roman_pizza_name}")]').click()
        return self

    @allure.step('Закрыть попапэ')
    def close_popup(self) -> 'HomePageRomanPizzaGroup':
        with allure.step('Закрыть попап'):
            browser.element('.popup-close-button').click()
        return self

    @allure.step('Проверить что римская пицца представлена только в одном размере')
    def check_roman_pizza_only_one_size(self) -> 'HomePageRomanPizzaGroup':
        with allure.step('Перейти в попап римской пиццы и проверить что римская пицца'
                         ' представлена только в одном размере'):
            browser.element('sc-1rpjq4r-0').should(have.text('25 см'))
        return self

    @allure.step('Проверить что римская пицца делается только из римского теста')
    def check_roman_pizza_only_roman_dough(self) -> 'HomePageRomanPizzaGroup':
        with allure.step('Перейти в попап римской пиццы и проверить что римская пицца'
                         ' делается только из римского теста'):
            browser.element('sc-1rpjq4r-0').should(have.text('Римское тесто'))
        return self
