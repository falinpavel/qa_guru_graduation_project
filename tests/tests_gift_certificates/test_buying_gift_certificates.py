import allure

from helpers.application_manager.application_manager import dodo


@allure.epic('Оформление подарочных сертификатов')
@allure.feature('Проверка возможности оформления подарочного сертификата')
@allure.suite('Оформление подарочного сертификата пользователем')
class TestDodoUserLocations:

    @allure.story('Неавторизованный пользователь может перейти на вкладку "Подарочные сертификаты" '
                  'и выбрать для кого хочет оформить сертификат')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Проверка возможности выбора для кого хочет оформить сертификат пользователь')
    @allure.description('На данный момент сертификаты можно оформить только "Для сотрудников", в тесте вторым '
                        'шагом проверяем что при клике на "Для друзей и близких" появилась подсказка '
                        'о невозможности покупки таких сертификатов')
    @allure.id('23')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-23')
    def test_choose_recipient_for_a_gift_certificates(self):
        dodo.home_page.open_with(location='moscow')
        dodo.header_menu.click_gift_certificates_tab()
        dodo.gift_certificates_page \
            .popup_is_opened() \
            .select_and_click_the_recipient(a_gift_for='Для сотрудников') \
            .page_is_opened() \
            .click_close_button_and_go_to_home()
        dodo.header_menu.click_gift_certificates_tab()
        dodo.gift_certificates_page \
            .popup_is_opened() \
            .select_and_click_the_recipient(a_gift_for='Для друзей и близких') \
            .click_accept_in_popup()
