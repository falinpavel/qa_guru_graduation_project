import allure
import pytest

from helpers.application_manager.application_manager import dodo


@allure.epic('Изменение города пользователя')
@allure.feature('Проверка изменения города пользователя')
@allure.suite('Изменение города пользователя')
class TestDodoUserLocations:

    @allure.story('Неавторизованный пользователь может сменить город при клику на кнопку-ссылку')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Проверка изменения города пользователя при клике на кнопку-ссылку уже выбранного города')
    @allure.id('9')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-9')
    @pytest.mark.parametrize('new_location',
                             ['Краснодар', 'Абинск', 'Кисловодск'],
                             ids=['Krasnodar', 'Abinsk', 'Kislovodsk'])
    def test_change_location(self, new_location):
        dodo.home_page.open_with(location='moscow')
        dodo.home_page.change_location(new_location=new_location)
