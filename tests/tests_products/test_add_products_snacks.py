import allure

from helpers.application_manager.application_manager import dodo


@allure.epic('Добавление продуктов в корзину')
@allure.feature('Проверка реализации функционала добавления продуктов в корзину')
@allure.suite('Корзина неавторизованного пользователя')
class TestDodoAddProductsSnacks:

    @allure.story('Пользователь может изменить количество закуски в позиции')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('При выборе закуски пользователь может изменить '
                  'дефолтное количество в позиции, если это предусмотрено')
    @allure.id('14')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-14')
    def test_that_user_can_choose_quantity_of_snacks(self):
        dodo.home_page.open_with(location='moscow')
        dodo.home_page_snacks_group.click_snacks_group() \
            .click_snack_and_open_popup(snacks_name='Креветки терияки') \
            .check_default_quantity_of_snack() \
            .change_quantity_of_snack(new_quantity='9 шт') \
            .close_popup() \
            .click_snack_and_open_popup(snacks_name='Хашбрауны') \
            .check_default_quantity_of_snack(default_quantity='4 шт') \
            .change_quantity_of_snack(new_quantity='3 шт') \
            .change_quantity_of_snack(new_quantity='2 шт') \
            .close_popup()

    @allure.story('Любая позиция в группу "Закуски" имеет цену')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('При просмотре группы закусок все позиции имеют заполненный элемент с ценой позиции,'
                  'и она не равна 0')
    @allure.id('15')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-15')
    def test_that_all_snacks_has_price(self):
        dodo.home_page.open_with(location='moscow')
        dodo.home_page_snacks_group.click_snacks_group()
        dodo.home_page_snacks_group.check_all_snacks_prices()
