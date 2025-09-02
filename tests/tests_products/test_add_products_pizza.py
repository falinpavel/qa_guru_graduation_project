import allure
import pytest

from helpers.application_manager.application_manager import dodo


@allure.epic('Добавление продуктов в корзину')
@allure.feature('Проверка реализации функционала добавления продуктов в корзину')
@allure.suite('Корзина неавторизованного пользователя')
class TestDodoAddProductsPizza:

    @allure.story('Пользователь может выбрать размер пиццы')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('При выборе пиццы пользователь может выбрать ее размер')
    @allure.id('1')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-1')
    @pytest.mark.parametrize(
        'pizza_name',
        ['Терияки', 'Чесночный цыпленок', 'Пикантные колбаски', 'Пепперони фреш', 'Четыре сыра', 'Сырная'],
        ids=
        ['Teriyaki', 'Garlic Chicken', 'Spicy sausages', 'Pepperoni fresh', 'Four cheeses', 'Cheese']
    )
    def test_that_user_can_choose_size_of_pizza(self, pizza_name):
        dodo.home_page.open_with(location='moscow')
        dodo.home_page_pizza_group.click_pizza_group()
        dodo.home_page_pizza_group \
            .click_pizza_and_open_popup(pizza_name=pizza_name) \
            .select_pizza_size(pizza_size='20 см') \
            .select_pizza_size(pizza_size='25 см') \
            .select_pizza_size(pizza_size='30 см') \
            .select_pizza_size(pizza_size='35 см') \
            .close_popup()

    @allure.story('Пользователь может выбрать тесто для пиццы')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('При выборе пиццы пользователь может выбрать тесто, на котором будет готовится пицца')
    @allure.id('2')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-2')
    @pytest.mark.parametrize(
        'pizza_name',
        ['Терияки', 'Чесночный цыпленок', 'Пикантные колбаски', 'Пепперони фреш', 'Четыре сыра', 'Сырная'],
        ids=
        ['Teriyaki', 'Garlic Chicken', 'Spicy sausages', 'Pepperoni fresh', 'Four cheeses', 'Cheese']
    )
    def test_that_user_can_choose_dough_of_pizza(self, pizza_name):
        dodo.home_page.open_with(location='moscow')
        dodo.home_page_pizza_group.click_pizza_group()
        dodo.home_page_pizza_group \
            .click_pizza_and_open_popup(pizza_name=pizza_name) \
            .choose_dough_of_pizza(pizza_dough='Тонкое') \
            .choose_dough_of_pizza(pizza_dough='Традиционное') \
            .close_popup()

    @allure.story('Любая позиция в группу "Пиццы" имеет цену')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('При просмотре группы "Пиццы" все позиции имеют заполненный элемент с ценой позиции,'
                  'и она не равна 0')
    @allure.id('16')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-16')
    def test_that_all_pizza_has_price(self):
        dodo.home_page.open_with(location='moscow')
        dodo.home_page_pizza_group.click_pizza_group()
        dodo.home_page_pizza_group.check_all_pizza_prices()
