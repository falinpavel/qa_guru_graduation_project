import allure
from selene import browser, be, have

from helpers.config.links import Links


class HomePage:

    def __init__(self):
        self.url = Links.DODO_CONTROL_URL

    def open(self):
        with allure.step(f'Открыть главную страницу'):
            browser.open(self.url)
        return self

    def filling_questionnaire_form(self, country, city, address,
                                   name, birth_day, birth_month,
                                   birth_year, number, vk_link):
        with allure.step(f'Заполнить анкету'):
            browser.element('#select2-countries-container').click().type(country)
            browser.element('#select2-cities-container').click().type(city)
            browser.element('.select2-search__field').click().element(have.text(address)).click()
            browser.element('#name').click().type(name)
            browser.element('#birthDay').click().type(f'{birth_day}{birth_month}{birth_year}')
            browser.element('#phoneNumber').click().type(number)
            browser.element('#socialNetworkLink').click().type(vk_link)
            browser.element('[class=horizontal-radio] [for="3"]').click()
            browser.element('[class=horizontal-radio] [for="2"]').click()
            browser.element('[class=horizontal-radio] [for="1"]').click()
            browser.element('[for="pdn"]').click()
            return self
