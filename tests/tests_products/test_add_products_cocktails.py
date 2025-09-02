import allure
import pytest

from helpers.application_manager.application_manager import dodo


@allure.epic('Добавление продуктов в корзину')
@allure.feature('Проверка реализации функционала добавления продуктов в корзину')
@allure.suite('Корзина неавторизованного пользователя')
class TestDodoAddProductsCocktails:

    @allure.story('Дефолтным объемом коктейля 0,3 л')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('При выборе коктейля пользователю по умолчанию выбран самый маленький объем')
    @allure.id('21')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-21')
    @pytest.mark.parametrize(
        'cocktail_name',
        ['Персиковый молочный коктейль', 'Молочный коктейль Фисташка', 'Молочный коктейль с печеньем Орео',
         'Классический молочный коктейль', 'Клубничный молочный коктейль', 'Шоколадный молочный коктейль'],
        ids=
        ['Peach Milkshake', 'Milkshake Pistachio', 'Oreo Cookie Milkshake',
         'Classic milkshake', 'Strawberry Milkshake', 'Chocolate Milkshake']
    )
    def test_that_default_volume_is_small(self, cocktail_name):
        dodo.home_page.open_with(location='moscow')
        dodo.home_page_cocktails_group.click_cocktails_group() \
            .click_cocktail_and_open_popup(cocktail_name=cocktail_name) \
            .check_default_volume() \
            .close_popup()

    @allure.story('Пользователь может выбрать объем коктейля')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('При выборе коктейля пользователь может изменить '
                  'его объем, если это предусмотрено позицией')
    @allure.id('22')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-22')
    @pytest.mark.parametrize(
        'cocktail_name',
        ['Персиковый молочный коктейль', 'Молочный коктейль Фисташка', 'Молочный коктейль с печеньем Орео',
         'Классический молочный коктейль', 'Клубничный молочный коктейль', 'Шоколадный молочный коктейль'],
        ids=
        ['Peach Milkshake', 'Milkshake Pistachio', 'Oreo Cookie Milkshake',
         'Classic milkshake', 'Strawberry Milkshake', 'Chocolate Milkshake']
    )
    def test_that_user_can_choose_volume_of_cocktail(self, cocktail_name):
        dodo.home_page.open_with(location='moscow')
        dodo.home_page_cocktails_group.click_cocktails_group() \
            .click_cocktail_and_open_popup(cocktail_name=cocktail_name) \
            .change_volume_of_cocktail(new_volume='0,6 л') \
            .change_volume_of_cocktail(new_volume='0,3 л') \
            .close_popup()

    @allure.story('Любая позиция в группу "Коктейли" имеет цену')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('При просмотре группы "Коктейли" все позиции имеют заполненный элемент с ценой позиции,'
                  'и она не равна 0')
    @allure.id('24')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-24')
    def test_that_all_cocktails_has_price(self):
        dodo.home_page.open_with(location='moscow')
        dodo.home_page_cocktails_group.click_cocktails_group()
        dodo.home_page_cocktails_group.check_all_cocktails_prices()
