import allure
from selene import browser, have, command
from selene.core.condition import Condition


class HomePageComboGroup:

    @allure.step('Перейти в группу "Пицца" кликнув на кнопку "Пицца" на главной странице')
    def click_combo_group(self) -> 'HomePageComboGroup':
        with allure.step('Клик на кнопку "Комбо"'):
            browser.element('//a[contains(text(),"Комбо")]').should(have.text('Комбо')).click()
        return self

    @allure.step('Кликнуть на конкретное комбо в группе "Комбо" и перейти в попап')
    def click_combo_and_open_popup(self, combo_name: str) -> 'HomePageComboGroup':
        with allure.step(f'Кликнуть на комбо {combo_name}'):
            browser.element('//h2[contains(text(),"Комбо")]').perform(command.js.scroll_into_view).should(
                Condition.by_and(have.text('Комбо'))
            )
            browser.element(f'//section[@id="combo"]//span[contains(text(),"{combo_name}")]').click()
            browser.element(f'//span[contains(text(),"{combo_name}")]').perform(command.js.scroll_into_view).click()
        return self

    @allure.step('Закрыть попап')
    def close_popup(self) -> 'HomePageComboGroup':
        with allure.step('Закрыть попап'):
            browser.element('.popup-close-button').click()
        return self

    @allure.step('Нажать на кнопку "Заменить" в комбо для первой позиции')
    def replace_first_position_in_combo(self, old: str, new: str) -> 'HomePageComboGroup':
        with allure.step('Заменить в комбо первый элемент на другую позицию можно нажав на кнопку "Заменить"'):
            browser.element('(//div[@class="name"])[1]').should(Condition.by_and(have.text(old)))
            browser.element('(//button[contains(text(),"Заменить")])[1]').click()
        with allure.step(f'Выбрать новую позицию {new}'):
            browser.element(f'//div[@class="sc-rtif5y-2 ceuSI" and text()="{new}"]').click()
            browser.element('(//div[@class="name"])[1]').should(Condition.by_and(have.text(new)))
        return self

    @allure.step('Нажать на кнопку "Заменить" в комбо для второй позиции')
    def replace_second_position_in_combo(self, old: str, new: str) -> 'HomePageComboGroup':
        with allure.step('Заменить в комбо второй элемент на другую позицию можно нажав на кнопку "Заменить"'):
            browser.element('(//div[@class="name"])[2]').should(Condition.by_and(have.text(old)))
            browser.element('(//button[contains(text(),"Заменить")])[2]').click()
        with allure.step(f'Выбрать новую позицию {new}'):
            browser.element(f'//div[@class="sc-rtif5y-2 ceuSI" and text()="{new}"]').click()
            browser.element('(//div[@class="name"])[2]').should(Condition.by_and(have.text(new)))
        return self
