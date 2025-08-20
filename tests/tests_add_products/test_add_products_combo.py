import allure

from helpers.application_manager.application_manager import dodo


@allure.epic('Добавление продуктов в корзину')
@allure.feature('Проверка реализации функционала добавления продуктов в корзину')
@allure.suite('Корзина неавторизованного пользователя')
class TestDodoAddProductsCombo:

    @allure.story('Пользователь может изменить пиццу в комбо на другую')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('При выборе комбо пользователь может изменить пиццу в комбо на желаемую')
    @allure.id('1')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-1')
    def test_that_user_can_choose_size_of_pizza(self):
        dodo.home_page.open_with(location='moscow')
        dodo.home_page_combo_group \
            .click_combo_group() \
            .click_combo_and_open_popup(combo_name='Пицца и напиток') \
            .replace_pizza_in_combo(old_pizza='Пепперони фреш', new_pizza='Сырная') \
            .close_popup()
