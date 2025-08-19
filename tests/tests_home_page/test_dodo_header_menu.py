import allure

from helpers.application_manager.application_manager import dodo


@allure.epic('Верхнее меню на главной странице')
@allure.feature('Проверка работы верхнего меню, переключение табов и проверка их активности')
class TestDodoHeaderMenu:

    @allure.story('У неавторизованного пользователя при клике на таб "Прямой эфир" открывается окно прямого эфира')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Проверка отображения/скрытия окна прямого эфира при клике на таб "Прямой эфир"')
    @allure.id('1')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-1')
    def test_opening_live_stream(self):
        dodo.home_page.open_with(location='moscow')
        dodo.header_menu.click_live_stream_tab().check_live_stream_is_active()
        dodo.header_menu.click_live_stream_tab().check_live_stream_is_inactive()
