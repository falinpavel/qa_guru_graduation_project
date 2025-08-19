import allure

from helpers.application_manager.application_manager import dodo


@allure.epic('Корзина неавторизованного пользователя')
@allure.feature('Проверка корзины неавторизованного пользователя на главной странице')
class TestDodoCart:

    @allure.story('У неавторизованного пользователя при первом посещении сайта корзина должна быть пустой')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Проверка пустой корзины при первом посещении сайта')
    @allure.id('7')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-7')
    def test_that_cart_is_empty(self):
        dodo.home_page.open_with(location='moscow')
        dodo.cart.check_cart_is_empty()
