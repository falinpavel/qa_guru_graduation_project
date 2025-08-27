import allure

from helpers.application_manager.application_manager import dodo


@allure.epic('Оформление подарочных сертификатов')
@allure.feature('Проверка возможности оформления подарочного сертификата')
@allure.suite('Оформление подарочного сертификата пользователем')
class TestDodoBuyGiftCertificates:

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
            .is_opened() \
            .click_close_button_and_go_to_home()
        dodo.header_menu.click_gift_certificates_tab()
        dodo.gift_certificates_page \
            .popup_is_opened() \
            .select_and_click_the_recipient(a_gift_for='Для друзей и близких') \
            .click_accept_in_popup()

    @allure.story('Неавторизованный пользователь может просчитать сертификаты заполнив форму')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('Проверка возможности заполнения формы подсчета сертификатов группы '
                  '"Одна сумма" и корректности итоговых сумм')
    @allure.id('25')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-25')
    def test_choose_certificate_type_one_amount_and_fill_form(self):
        dodo.home_page.open_with(location='moscow')
        dodo.header_menu.click_gift_certificates_tab()
        dodo.gift_certificates_page \
            .popup_is_opened() \
            .select_and_click_the_recipient(a_gift_for='Для сотрудников') \
            .is_opened() \
            .click_order_button() \
            .choose_certificate_type(type_of='Одна сумма') \
            .filling_form_for_one_amount_certificate(amount=20000, total=10) \
            .click_back_button()

    @allure.story('Неавторизованный пользователь может просчитать сертификаты заполнив форму')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('Проверка возможности заполнения формы подсчета сертификатов группы "Разные суммы"')
    @allure.id('26')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-26')
    def test_choose_certificate_type_other_amount_and_fill_form(self):
        dodo.home_page.open_with(location='moscow')
        dodo.header_menu.click_gift_certificates_tab()
        dodo.gift_certificates_page \
            .popup_is_opened() \
            .select_and_click_the_recipient(a_gift_for='Для сотрудников') \
            .is_opened() \
            .click_order_button() \
            .choose_certificate_type(type_of='Разные суммы') \
            .filling_form_for_other_amount_certificate(first=('10', '2000'),
                                                       second=('15', '2500'),
                                                       third=('20', '5000'))

    @allure.story('Пользователь после заполнения формы и выборе "Отправим за вас" может скачать шаблон')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('Проверка, что после заполнения формы можно скачать шаблона при '
                  'если выбран способ получения "Отправим за вас"')
    @allure.id('27')
    @allure.label('owner', 'AQA Engineer: Falin Pavel')
    @allure.label('category', 'UI', 'WEB')
    @allure.link('https://jira.dodo.ru/tasks/DOOD-27')
    def test_download_template(self):
        dodo.home_page.open_with(location='moscow')
        dodo.header_menu.click_gift_certificates_tab()
        dodo.gift_certificates_page \
            .popup_is_opened() \
            .select_and_click_the_recipient(a_gift_for='Для сотрудников') \
            .is_opened() \
            .click_order_button() \
            .choose_certificate_type(type_of='Одна сумма') \
            .filling_form_for_one_amount_certificate(amount=20000, total=10) \
            .click_next_button()  # TODO! next steps
