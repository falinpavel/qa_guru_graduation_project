from selene import browser, by, be, have


class HomePage:

    def __init__(self):
        self.url = 'https://dodopizza.ru/'

    def open(self) -> 'HomePage':
        browser.open(self.url)
        return self

    def choose_location(self) -> 'HomePage':
        browser.element('//a[@class="locality-selector-popup__big-city"][contains(text(),"Москва")]').click()
        return self

