import allure
from selene import browser, have, command, be
from selene.core.condition import Condition


class HomePageCocktailsGroup:

    @allure.step('Перейти в группу "Коктейли" кликнув на кнопку "Коктейли" на главной странице')
    def click_cocktails_group(self) -> 'HomePageCocktailsGroup':
        with allure.step('Клик на кнопку "Коктейли"'):
            browser.element('//a[contains(text(),"Коктейли")]').with_(timeout=browser.config.timeout * 2).should(
                Condition.by_and(be.clickable, have.text('Коктейли'))
            ).click()
        return self

    @allure.step('Кликнуть на конкретную позицию в группе "Коктейли" и перейти в попап')
    def click_cocktail_and_open_popup(self, cocktail_name: str) -> 'HomePageCocktailsGroup':
        with allure.step(f'Кликнуть на наименование коктейля: {cocktail_name}'):
            browser.element('//h2[contains(text(),"Коктейли")]').should(Condition.by_and(be.visible))
            browser.element(f'//section[@id="mrwqq"]//span[contains(text(),"{cocktail_name}")]').should(
                Condition.by_and(be.visible, be.clickable)
            ).click()
        return self

    @allure.step('Проверить дефолтный обьем коктейля')
    def check_default_volume(self, default_volume: str = '0,3 л') -> 'HomePageCocktailsGroup':
        with allure.step('Проверить что дефолтным обьемом коктейля является самый маленький (0,3 л)'):
            browser.element('//span[@class="sc-1r4m23d-15 fFeXIk"]').should(
                Condition.by_and(be.visible, have.text(default_volume)))
            return self

    @allure.step('Изменить объем коктейля')
    def change_volume_of_cocktail(self, new_volume: str) -> 'HomePageCocktailsGroup':
        with allure.step('Изменить дефолтный объем коктейля на новое значение'):
            browser.element(f'//label[contains(text(),"{new_volume}")]').click()
            browser.element('//span[@class="sc-1r4m23d-15 fFeXIk"]').should(
                Condition.by_and(be.visible, have.text(new_volume)))
            return self

    @allure.step('Закрыть попап')
    def close_popup(self) -> 'HomePageCocktailsGroup':
        with allure.step('Закрыть попап'):
            browser.element('.popup-close-button').click()
        return self

    @allure.step('Проверить что абсолютно у всех коктейлей есть цена')
    def check_all_cocktails_prices(self) -> 'HomePageCocktailsGroup':
        with allure.step('Перейти в группу "Коктейли" и проверить что у всех позиций есть цена и она не равна нулю'):
            all_products_carts = browser.all('//section[@id="mrwqq"]//div[@class="product-control-price"]')
            for product in all_products_carts:
                product.perform(command.js.scroll_into_view).should(Condition.by_and(be.visible, be.not_.blank))
        return self

