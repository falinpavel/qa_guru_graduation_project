import allure
from selene import browser, have


class HomePageComboGroup:

    @allure.step('Перейти в группу "Пицца" кликнув на кнопку "Пицца" на главной странице')
    def click_combo_group(self) -> 'HomePageComboGroup':
        with allure.step('Клик на кнопку "Комбо"'):
            browser.element('//a[contains(text(),"Комбо")]').should(have.text('Комбо')).click()
        return self

    @allure.step('Кликнуть на конкретное комбо в группе "Комбо" и перейти в попап')
    def click_combo_and_open_popup(self, combo_name: str) -> 'HomePageComboGroup':
        with allure.step(f'Кликнуть на комбо {combo_name}'):
            browser.element(f'//span[contains(text(),"{combo_name}")]').click()
        return self

    @allure.step('Закрыть попап')
    def close_popup(self) -> 'HomePageComboGroup':
        with allure.step('Закрыть попап'):
            browser.element('.popup-close-button').click()
        return self

    @allure.step('Нажать на кнопку "Заменить" пиццу в комбо')
    def replace_pizza_in_combo(self, old_pizza: str, new_pizza: str) -> 'HomePageComboGroup':
        with allure.step('Заменить пиццу в комбо на другую можно нажав на кнопку "Заменить"'):
            browser.element('(//div[@class="name"])[1]').should(have.text(old_pizza))
            browser.element('(//button[contains(text(),"Заменить")])[1]').click()
        with allure.step(f'Выбрать пиццу {new_pizza}'):
            browser.element(f'//div[@class="sc-rtif5y-2 ceuSI" and text()="{new_pizza}"]').click()
            browser.element('(//div[@class="name"])[1]').should(have.text(new_pizza))
        return self
