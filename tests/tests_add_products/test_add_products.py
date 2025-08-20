import allure

from helpers.application_manager.application_manager import dodo


@allure.epic('Добавление продуктов в корзину')
@allure.feature('Проверка реализации функционала добавления продуктов в корзину')
@allure.suite('Корзина неавторизованного пользователя')
class TestDodoAddProducts:

    @allure.story('Пользователь может выбрать размер пиццы')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('При выборе пиццы пользователь может выбрать ее размер')
    @allure.id('11')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-11')
    def test_that_user_can_choose_size_of_pizza(self):
        dodo.home_page.open_with(location='moscow')
        dodo.home_page_pizza_group.click_pizza_group()
        dodo.home_page_pizza_group \
            .click_pizza_and_open_popup(pizza_name='Терияки') \
            .choose_size_of_pizza(pizza_size='20 см') \
            .choose_size_of_pizza(pizza_size='25 см') \
            .choose_size_of_pizza(pizza_size='30 см') \
            .choose_size_of_pizza(pizza_size='35 см') \
            .close_popup() \
            .click_pizza_and_open_popup(pizza_name='Чесночный цыпленок') \
            .choose_size_of_pizza(pizza_size='35 см') \
            .choose_size_of_pizza(pizza_size='30 см') \
            .choose_size_of_pizza(pizza_size='25 см') \
            .choose_size_of_pizza(pizza_size='20 см') \
            .close_popup()

    @allure.story('Пользователь может выбрать тесто для пиццы')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('При выборе пиццы пользователь может выбрать тесто, на котором будет готовится пицца')
    @allure.id('10')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-10')
    def test_that_user_can_choose_dough_of_pizza(self):
        dodo.home_page.open_with(location='moscow')
        dodo.home_page_pizza_group.click_pizza_group()
        dodo.home_page_pizza_group \
            .click_pizza_and_open_popup(pizza_name='Пикантные колбаски') \
            .choose_dough_of_pizza(pizza_dough='Тонкое') \
            .choose_dough_of_pizza(pizza_dough='Традиционное') \
            .close_popup() \
            .click_pizza_and_open_popup(pizza_name='Чоризо фреш') \
            .choose_dough_of_pizza(pizza_dough='Традиционное') \
            .choose_dough_of_pizza(pizza_dough='Тонкое') \
            .close_popup()
