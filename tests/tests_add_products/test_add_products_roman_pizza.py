import allure

from helpers.application_manager.application_manager import dodo


@allure.epic('Добавление продуктов в корзину')
@allure.feature('Проверка реализации функционала добавления продуктов в корзину')
@allure.suite('Корзина неавторизованного пользователя')
class TestDodoAddProductsRomanPizza:

    @allure.story('Пользователь не может выбрать размер римской пиццы')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('При выборе римской пиццы пользователь не может выбрать ее размер,'
                  ' она представлена одним размером в 25 см')
    @allure.id('10')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-10')
    def test_that_roman_pizza_presented_only_one_size(self):
        dodo.home_page.open_with(location='moscow')
        dodo.home_page_roman_pizza_group.click_roman_pizza_group() \
            .click_roman_pizza_and_open_popup('Римская Аррива!') \
            .check_roman_pizza_only_one_size() \
            .close_popup() \
            .click_roman_pizza_and_open_popup('Римская Жюльен') \
            .check_roman_pizza_only_one_size() \
            .close_popup() \
            .click_roman_pizza_and_open_popup('Римская Карбонара') \
            .check_roman_pizza_only_one_size() \
            .close_popup()

    @allure.story('Пользователь не может выбрать тесто римской пиццы')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('При выборе римской пиццы пользователь не может выбрать ее тесто,'
                  ' она делается только на римском тесте')
    @allure.id('11')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-11')
    def test_that_roman_pizza_presented_only_one_dough(self):
        dodo.home_page.open_with(location='moscow')
        dodo.home_page_roman_pizza_group.click_roman_pizza_group() \
            .click_roman_pizza_and_open_popup('Римская Аррива!') \
            .check_roman_pizza_only_roman_dough() \
            .close_popup() \
            .click_roman_pizza_and_open_popup('Римская Жюльен') \
            .check_roman_pizza_only_roman_dough() \
            .close_popup() \
            .click_roman_pizza_and_open_popup('Римская Карбонара') \
            .check_roman_pizza_only_roman_dough() \
            .close_popup()

    @allure.story('Любая позиция в группу "Римские пиццы" имеет цену')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('При просмотре группы "Римские пиццы" все позиции имеют заполненный элемент с ценой позиции,'
                  'и она не равна 0')
    @allure.id('18')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-18')
    def test_that_all_roman_pizza_has_price(self):
        dodo.home_page.open_with(location='moscow')
        dodo.home_page_roman_pizza_group.click_roman_pizza_group()
        dodo.home_page_roman_pizza_group.check_all_roman_pizza_prices()
