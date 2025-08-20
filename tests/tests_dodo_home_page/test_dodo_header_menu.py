import allure

from helpers.application_manager.application_manager import dodo


@allure.epic('Верхнее меню на главной странице')
@allure.feature('Проверка работы верхнего меню, переключение табов и проверка их активности')
@allure.suite('Верхнее меню на главной странице')
class TestDodoHeaderMenu:

    @allure.story('У неавторизованного пользователя при клике на таб "Прямой эфир" открывается окно прямого эфира')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Проверка отображения/скрытия окна прямого эфира при клике на таб "Прямой эфир"')
    @allure.id('6')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-6')
    def test_opening_live_stream(self):
        dodo.home_page.open_with(location='moscow')
        dodo.header_menu \
            .click_live_stream_tab() \
            .check_live_stream_is_active() \
            .click_live_stream_tab() \
            .check_live_stream_is_inactive()

    @allure.story('Неавторизованный пользователь может переходить на страницу "О нас"')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Проверка перехода на страницу "О нас" и ее контент')
    @allure.id('7')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-7')
    def test_opening_about_us(self):
        dodo.home_page.open_with(location='moscow')
        dodo.header_menu.click_about_us_tab()
        dodo.about_us_page.is_opened(location='moscow')

    @allure.story('Неавторизованный пользователь может переходить на страницу "Контакты"')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Проверка перехода на страницу "Контакты" и ее контент')
    @allure.id('8')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-8')
    def test_opening_contacts(self):
        dodo.home_page.open_with(location='moscow')
        dodo.header_menu.click_contacts_tab()
        dodo.contacts_page.is_opened(location='moscow')
