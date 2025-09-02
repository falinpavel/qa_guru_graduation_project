import allure
from selene import browser, have, be
from selene.core.condition import Condition

from helpers.data.links import Links


class GiftCertificatesPage:

    def __init__(self):
        self.url = Links.GIFT_CERTIFICATES_PAGE_URL

    @allure.step('Открыть страницу "Сертификаты для бизнеса"')
    def open_with(self) -> 'GiftCertificatesPage':
        with allure.step(f'Открыть страницу "Сертификаты для бизнеса"'):
            browser.open(self.url)
        return self

    # @allure.step('Проверить что открылся попап')
    # def popup_is_opened(self) -> 'GiftCertificatesPage':
    #     with allure.step(f'Проверить что открылся попап'):
    #         browser.element('//h2[@class="title"]').should(Condition.by_and(have.text('Для кого сертификаты?')))
    #     return self
    #
    # @allure.step('Закрыть попап')
    # def close_popup(self) -> 'GiftCertificatesPage':
    #     with allure.step(f'Закрыть попап'):
    #         browser.element('.popup-close-button').click()
    #     return self

    @allure.step('Проверить что открыта страница "Сертификаты для бизнеса"')
    def is_opened(self) -> 'GiftCertificatesPage':
        with allure.step(f'Проверить что открыта страница "Сертификаты для бизнеса"'):
            browser.should(have.url(self.url))

            browser.element('[data-testid="order-button"]').should(
                Condition.by_and(be.clickable, have.text('Заказать')))
        return self

    # @allure.step('В попапе нажать на кнопку "Понятно"')
    # def click_accept_in_popup(self):
    #     with allure.step('Если выбран "Для друзей и близких" то в попапе нажать на кнопку "Понятно"'):
    #         browser.element('//button[contains(text(),"Понятно")]').should(Condition.by_and(be.clickable)).click()

    # @allure.step('Нажать на кнопку выбора "Для кого сертификаты?"')
    # def select_and_click_the_recipient(self, a_gift_for: str) -> 'GiftCertificatesPage':
    #     with allure.step(f'В попапе нажать на кнопку "{a_gift_for}"'):
    #         if a_gift_for == 'Для сотрудников':
    #             browser.element(f'//button[text()="{a_gift_for}"]').should(Condition.by_and(be.clickable)).click()
    #         else:
    #             with allure.step('Кликнуть на "Для друзей и близких" и проверить что в попапе отображается '
    #                              'подсказка о недоступности такой покупки'):
    #                 browser.element(f'//button[text()="{a_gift_for}"]').should(Condition.by_and(be.clickable)).click()
    #                 browser.element('//h2[@class="title"]').should(Condition.by_and(
    #                     have.text('Таких сертификатов нет, но мы учли ваш ответ')))
    #     return self

    @allure.step('Нажать на кнопку "Заказать"')
    def click_order_button(self) -> 'GiftCertificatesPage':
        with allure.step('Нажать на кнопку "Заказать" на странице'):
            browser.element('[data-testid="order-button"]').should(Condition.by_and(be.clickable)).click()
        return self

    @allure.step('Вернуться назад на главную')
    def click_close_button_and_go_to_home(self) -> 'GiftCertificatesPage':
        with allure.step('Нажать крестик на странице "Сертификаты для бизнеса" что бы вернуться на главную страницу'):
            browser.element('.header-right').should(Condition.by_and(be.visible, be.clickable)).click()
        return self

    @allure.step('Вернуться назад к кнопке "Заказать"')
    def click_back_button(self) -> 'GiftCertificatesPage':
        with allure.step('Нажать на кнопку назад и вернуться на предыдущий таб в /certificates'):
            browser.element('.header-left').should(Condition.by_and(be.visible, be.clickable)).click()
        return self

    @allure.step('Выбрать тип сертификата ("Одна сумма" или "Разные суммы")')
    def choose_certificate_type(self, type_of: str):
        with allure.step(f'Выбрать тип сертификата: {type_of}'):
            browser.element(f'//label[text()="{type_of}"]').should(Condition.by_and(be.clickable)).click()
        return self

    @allure.step('Заполнить форму для сертификата типа "Одна сумма"')
    def filling_form_for_one_amount_certificate(self, amount: int, total: int) -> 'GiftCertificatesPage':
        with allure.step(f'Заполнить бюджет на сумму: {amount} и для количества сотрудников: {total}'):
            browser.element('#certificates__single__budget').should(Condition.by_and(
                be.clickable)).clear().click().type(amount).press_enter().should(have.value(str(amount)))

        with allure.step(f'Заполнить количество сотрудников: {total}'):
            browser.element('#certificates__single__count').should(Condition.by_and(
                be.clickable)).clear().click().type(total).press_enter().should(have.value(str(total)))

        with allure.step(f'Проверить корректность расчета, что сумма сертификата равна: {amount // total}'):
            browser.element('#certificates__single__amount').should(Condition.by_and(
                have.value(f"{amount // total:,}".replace(",", "\u00A0") + "\u202F₽")))
        return self

    @allure.step('Заполнить форму для сертификата типа "Разные суммы"')
    def filling_form_for_other_amount_certificate(self,
                                                  first: tuple,
                                                  second: tuple,
                                                  third: tuple
                                                  ) -> 'GiftCertificatesPage':
        certificates = [first, second, third]

        for index, cert_data in enumerate(certificates):
            with allure.step(f'Заполнить значения для {index + 1}-го сертификата'):
                inputs = browser.all(f'.input-sub-container [data-index="{index}"]')

                inputs.first.should(be.clickable).click().type(cert_data[0]).press_enter()
                inputs.first.should(have.value(cert_data[0]))

                inputs.second.should(be.clickable).click().type(cert_data[1]).press_enter()
                inputs.second.should(have.value(cert_data[1]))

                if index < 2:
                    browser.element('//button[contains(text(),"Добавить ещё")]').click()
        return self

    @allure.step('Нажать на кнопку "Дальше"')
    def click_next_button(self) -> 'GiftCertificatesPage':
        with allure.step('После заполнения формы нажать на кнопку "Дальше"'):
            browser.element('[data-testid="next-button"]').should(Condition.by_and(be.clickable)).click()
        return self


