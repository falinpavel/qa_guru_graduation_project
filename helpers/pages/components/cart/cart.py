import allure
from selene import browser, be, have
from selene.core.condition import Condition


class ComponentCart:

    @allure.step('Проверить что корзина пустая')
    def check_cart_is_empty(self) -> 'ComponentCart':
        with allure.step('Нажать на иконку корзины'):
            browser.element('[data-testid="navigation__cart"]').should(be.visible).click()
        with allure.step('Проверить отображения текста "Пока тут пусто"'):
            browser.element('.empty h2').should(be.visible).should(have.text('Пока тут пусто'))
        with allure.step('Проверить отображения текстов "Добавьте пиццу. Или две!"'
                         ' и "А мы доставим ваш заказ от 649 ₽"'):
            browser.element('.empty div').should(be.visible).should(Condition.by_and(
                have.text('Добавьте пиццу. Или две!'), have.text('А мы доставим ваш заказ от 649 ₽')
            ))
        with allure.step('Нажать на крестик для закрытия корзины и проверить что она закрылась'):
            browser.element('.button-close').click()
            browser.element('.gwOFSm').should(be.not_.visible)
        return self
