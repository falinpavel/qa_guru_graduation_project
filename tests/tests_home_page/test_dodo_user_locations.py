import allure

from helpers.application_manager.application_manager import dodo


@allure.epic('Изменение города пользователя')
@allure.feature('Проверка изменения города пользователя')
@allure.suite('Изменение города пользователя')
class TestDodoUserLocations:

    @allure.story('Неавторизованный пользователь может сменить город при клику на кнопку-ссылку')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Провкрка изменения города пользователя при клике на кнопку-ссылку уже выбранного города')
    @allure.id('6')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-6')
    def test_change_location(self):
        dodo.home_page.open_with(location='moscow')
        dodo.home_page.change_location(new_location='Краснодар')
