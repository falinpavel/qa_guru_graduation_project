import allure
from selene import browser, have


class HomePagePizzaGroup:

    @allure.step('Перейти в группу "Пицца" кликнув на кнопку "Пицца" на главной странице')
    def click_pizza_group(self) -> 'HomePagePizzaGroup':
        with allure.step('Клик на кнопку "Пиццы"'):
            browser.element('//a[contains(text(),"Пиццы")]').should(have.text('Пиццы')).click()
        return self

    @allure.step('Кликнуть на конкретную пиццу в группе "Пицца" и перейти в попап')
    def click_pizza_and_open_popup(self, pizza_name) -> 'HomePagePizzaGroup':
        with allure.step(f'Кликнуть на пиццу {pizza_name}'):
            browser.element(f'//section[@id="guzhy"]//span[contains(text(),"{pizza_name}")]').click()
        return self

    @allure.step('Выбрать размер пиццы')
    def select_pizza_size(self, pizza_size) -> 'HomePagePizzaGroup':
        with allure.step(f'Выбрать размер пиццы {pizza_size}'):
            browser.element(f'[data-testid="menu__pizza_size_{pizza_size}"]').click()
        return self

    @allure.step('Выбрать тесто пиццы')
    def choose_dough_of_pizza(self, pizza_dough) -> 'HomePagePizzaGroup':
        with allure.step(f'Выбрать тесто пиццы {pizza_dough}'):
            browser.element(f'//label[contains(text(), "{pizza_dough}")]').click()
        return self

    @allure.step('Закрыть попапэ')
    def close_popup(self) -> 'HomePagePizzaGroup':
        with allure.step('Закрыть попап'):
            browser.element('.popup-close-button').click()
        return self
