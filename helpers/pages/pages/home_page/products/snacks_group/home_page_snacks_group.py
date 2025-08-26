import allure
from selene import browser, have, be, command
from selene.core.condition import Condition


class HomePageSnacksGroup:

    @allure.step('Перейти в группу "Закуски" кликнув на кнопку "Закуски" на главной странице')
    def click_snacks_group(self) -> 'HomePageSnacksGroup':
        with allure.step('Клик на кнопку "Закуски"'):
            browser.element('//a[contains(text(),"Закуски")]').should(have.text('Закуски')).click()
        return self

    @allure.step('Кликнуть на позицию закуски и открыть попап')
    def click_snack_and_open_popup(self, snacks_name: str) -> 'HomePageSnacksGroup':
        with allure.step(f'Кликнуть на позицию закуски {snacks_name} и открыть попап'):
            browser.element(f'//section[@id="kxgls"]//span[contains(text(),"{snacks_name}")]').should(
                Condition.by_and(be.visible, be.clickable)).click()
        return self

    @allure.step('Закрыть попапэ')
    def close_popup(self) -> 'HomePageSnacksGroup':
        with allure.step('Закрыть попап'):
            browser.element('.popup-close-button').click()
        return self

    @allure.step('Проверить дефолтное количество закуски')
    def check_default_quantity_of_snack(self, default_quantity: str = '5 шт') -> 'HomePageSnacksGroup':
        with allure.step('Проверить дефолтное количество закуски'):
            browser.element('//span[@class="sc-1r4m23d-15 fFeXIk"]').should(
                Condition.by_and(be.visible, have.text(default_quantity)))
            return self

    @allure.step('Изменить количество закуски')
    def change_quantity_of_snack(self, new_quantity: str) -> 'HomePageSnacksGroup':
        with allure.step('Проверить дефолтное количество закуски и изменить значение на новое'):
            browser.element(f'//label[contains(text(),"{new_quantity}")]').click()
            browser.element('//span[@class="sc-1r4m23d-15 fFeXIk"]').should(
                Condition.by_and(be.visible, have.text(new_quantity)))
            return self

    @allure.step('Проверить что абсолютно у всех закусок есть цена')
    def check_all_snacks_prices(self):
        with allure.step('Перейти в группу "Закуски" и проверить что у всех позиций есть цена и она не равна нулю'):
            all_products_carts = browser.all('//section[@id="kxgls"]//div[@class="product-control-price"]')
            for product in all_products_carts:
                product.perform(command.js.scroll_into_view).should(Condition.by_and(be.visible, be.not_.blank))
        return self
