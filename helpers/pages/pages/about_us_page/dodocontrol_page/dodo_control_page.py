import allure
from selene import browser, be, have, by, command
from selene.core.condition import Condition

from helpers.config.links import Links


class DodoControlPage:

    def __init__(self):
        self.url = Links.DODO_CONTROL_URL

    def open(self) -> 'DodoControlPage':
        with allure.step(f'Открыть главную страницу'):
            browser.open(self.url)
        return self

    def is_opened(self) -> 'DodoControlPage':
        browser.should(have.url(self.url))
        return self

    def filling_questionnaire_form(self, country, city, address,
                                   name, birth_day, birth_month,
                                   birth_year, number, vk_link) -> 'DodoControlPage':
        with allure.step(f'Заполнить анкету'):
            browser.element('.tab-right').should(Condition.by_and(have.text('ВОЙТИ')))

            browser.element('#select2-countries-container').click()
            browser.element('#select2-countries-results').should(Condition.by_and(be.visible)).element(
                by.text(country)).should(Condition.by_and(be.clickable)).click()
            # TODO: приоритет низкий, доделать потом

            # browser.element('#select2-cities-container').click()
            # browser.element('#select2-cities-results').should(Condition.by_and(be.visible)).element(
            #     by.text(city)).should(Condition.by_and(be.clickable)).click()
            #
            # browser.element('.select2-selection--multiple').click()
            # browser.element('#select2-pizzerias-results').should(Condition.by_and(be.visible)).element(
            #     by.text(address)).should(Condition.by_and(be.clickable)).click()

            # browser.element('#name').click().clear().type(name)
            # browser.element('#birthDay').click().clear().type(f'{birth_day}{birth_month}{birth_year}')
            # browser.element('#phoneNumber').click().clear().type(number)
            # browser.element('#socialNetworkLink').click().clear().type(vk_link)
            # browser.element('[class=horizontal-radio] [for="3"]').click()
            # browser.element('[class=horizontal-radio] [for="2"]').click()
            # browser.element('[class=horizontal-radio] [for="1"]').click()
            # browser.element('[for="pdn"]').click()
            return self
