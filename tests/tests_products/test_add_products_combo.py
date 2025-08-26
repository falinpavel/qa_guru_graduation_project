import allure

from helpers.application_manager.application_manager import dodo


@allure.epic('Добавление продуктов в корзину')
@allure.feature('Проверка реализации функционала добавления продуктов в корзину')
@allure.suite('Корзина неавторизованного пользователя')
class TestDodoAddProductsCombo:

    @allure.story('Пользователь может изменить первую позицию в комбо на другую')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('При выборе комбо пользователь может изменить первую позицию в комбо на другую желаемую')
    @allure.id('12')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-12')
    def test_that_user_can_replace_first_position_in_combo(self):
        dodo.home_page.open_with(location='moscow')
        dodo.home_page_combo_group \
            .click_combo_group() \
            .click_combo_and_open_popup(combo_name='Пицца и напиток') \
            .replace_first_position_in_combo(old='Пепперони фреш', new='Сырная') \
            .close_popup() \
            .click_combo_group() \
            .click_combo_and_open_popup(combo_name='2 напитка') \
            .replace_first_position_in_combo(old='Добрый Кола', new='Добрый Киви-Виноград') \
            .close_popup()

    @allure.story('Пользователь может изменить вторую позицию в комбо на другую')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('При выборе комбо пользователь может изменить вторую позицию в комбо на двугую желаемую')
    @allure.id('13')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-13')
    def test_that_user_can_replace_second_position_in_combo(self):
        dodo.home_page.open_with(location='moscow')
        dodo.home_page_combo_group \
            .click_combo_group() \
            .click_combo_and_open_popup(combo_name='Салат и закуска') \
            .replace_second_position_in_combo(old='Додстер', new='Острый Додстер') \
            .close_popup() \
            .click_combo_group() \
            .click_combo_and_open_popup(combo_name='Пицца и напиток') \
            .replace_second_position_in_combo(old='Лимонад Арбузный лайм', new='Добрый Апельсин') \
            .close_popup()

    @allure.story('Любая позиция в группу "Комбо" имеет цену')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('При просмотре группы "Комбо" все позиции имеют заполненный элемент с ценой позиции,'
                  'и она не равна 0')
    @allure.id('17')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-17')
    def test_that_all_combo_has_price(self):
        dodo.home_page.open_with(location='moscow')
        dodo.home_page_combo_group.click_combo_group()
        dodo.home_page_combo_group.check_all_combo_prices()
