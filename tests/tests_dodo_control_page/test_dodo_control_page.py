import allure

from helpers.application_manager.application_manager import dodo
from helpers.data.user_info import user


@allure.epic('Страница регистрации инспектора (тайного покупателя)')
@allure.feature('Проверка работы верхнего меню, переключение табов и проверка их активности')
@allure.suite('Верхнее меню на главной странице')
class TestDodoControlPage:

    @allure.story('Неавторизованный пользователь на странице "О нас" может заполнить анкету и стать инспектором')
    @allure.severity(allure.severity_level.MINOR)
    @allure.title('Проверка перехода на отдельную страницу для заполнения анкеты инспектора')
    @allure.id('4')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-4')
    def test_transition_questionnaire_form(self):
        dodo.home_page.open_with(location='moscow')
        dodo.header_menu.click_about_us_tab()
        dodo.about_us_page.click_questionnaire_button()
        dodo.dodo_control_page.is_opened()

    @allure.story('Пользователь может заполнить анкету и стать инспектором')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Проверка заполнения формы для анкеты инспектора')
    @allure.id('5')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-5')
    def test_successful_filling_questionnaire_form(self):
        dodo.about_us_page \
            .open_with(location='moscow') \
            .is_opened(location='moscow') \
            .click_questionnaire_button()
        dodo.dodo_control_page \
            .is_opened() \
            .filling_questionnaire_form(country=user.country, city=user.city,
                                        address=user.address_pizza, name=user.name,
                                        birth_day=user.birth_day, birth_month=user.birth_month,
                                        birth_year=user.birth_year, number=user.number, vk_link=user.vk_link)
