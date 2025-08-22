# 🎓 QA.GURU Graduation Project

Автоматизация тестирования веб-приложений "Додо Пицца" с помощью Python, Pytest и Selene 🚀

## О проекте

Этот проект является дипломной работой по курсу QA.GURU и представляет собой фреймворк для автоматизации тестирования веб-приложения "Додо Пицца" (https://dodopizza.ru/). В реализации использованы инструменты и библиотеки:

<p  align="center">
  <code><img width="8%" title="Pycharm" src="resources/images/logo/pycharm.png" alt="pycharm"></code>
  <code><img width="8%" title="Python" src="resources/images/logo/python.png" alt="python"></code>
  <code><img width="8%" title="Pytest" src="resources/images/logo/pytest.png" alt="pytest"></code>
  <code><img width="8%" title="Selene" src="resources/images/logo/selene.png" alt="selene"></code>
  <code><img width="8%" title="Selenium" src="resources/images/logo/selenium.png" alt="selenium"></code>
  <code><img width="8%" title="GitHub" src="resources/images/logo/github.png" alt="github"></code>
  <code><img width="8%" title="Jenkins" src="resources/images/logo/jenkins.png" alt="jenkins"></code>
  <code><img width="8%" title="Allure Report" src="resources/images/logo/allure_report.png" alt="allure"></code>
  <code><img width="8%" title="Telegram" src="resources/images/logo/tg.png" alt="telegram"></code>
</p>

## Структура проекта

    📁helpers (все файлы в этом каталоге являются вспомогательными)
        📁application_manager
            application_manager.py (application manager - хранятся все страницы и компоненты)
        📁config
            links.py (содержит ссылки на сайт, которые используются в тестах)
        📁data
            user_info.py (содержит данные для тестовых пользователей, генерируемые с помощью Faker)
        📁pages[images](..%2Fqa_guru_graduation_project_mobile%2Fimages)
            📁components (общие компоненты которые используются во всех страницах)
                📁cart
                    cart.py (компонент корзины)
                📁header
                    header_menu.py (компонент верхнего меню)
            📁pages (страницы сайта)
                📁about_us_page
                    📁dodo_control_page
                        control_page.py (страница "Контроль Додо")
                    about_us_page.py (страница "О нас")
                📁contact_page
                    contacts_page.py (страница "Контакты")
                📁home_page
                    📁products (каталог продуктов доступный на главной странице)
                        📁pizza_group
                            home_page_pizza_group.py (группа "Пиццы" с каталогом пицц)
                        📁roman_pizza_group
                            home_page_roman_pizza_group.py (группа "Романская пицца" с каталогом романской пиццы)
                        📁combo_group
                            home_page_combo_group.py (группа "Комбо" с каталогом комбо продуктов)
                    home_page.py (главная страница с описанием общих функциональностей)
    📁resources (файлы, которые используются в тестах)
    📁tests (все файлы в этом каталоге являются тестами)
        📁tests_add_products (группа тестов, которые проверяют добавление продуктов в корзину)
            test_add_products_combo.py
            test_add_products_pizza.py
            test_add_products_roman_pizza.py
        📁tests_dodo_cart (группа тестов, которые проверяют корзину)
            test_dodo_cart_unauthorized.py
        📁tests_dodo_control_page (группа тестов, которые проверяют страницу "Контроль Додо")
            test_dodo_control_page.py
        📁tests_dodo_home_page (группа тестов, которые проверяют главную страницу)
            test_dodo_header_menu.py
            test_dodo_user_locations.py
    📁utils
        attach.py (файл с вспомогательными функциями для работы с видео, скриншотами и логами Allure)
    .gitignore
    conftest.py (фикстуры)
    pytest.ini (конфигурационный файл Pytest для Jenkins)
    README.md
    requirements.txt (файл с зависимостями)

## <img width="5%" title="pycharm" src="resources/images/logo/pycharm.png"> Запуск тестов локально

1) Клонировать репозиторий: git clone https://github.com/falinpavel/qa_guru_graduation_project.git
2) Установить зависимости: pip install -r requirements.txt
3) Запуск тестов с генерацией отчетов Allure: pytest --alluredir=reports/allure-results
4) Просмотр отчета Allure (если установлен Allure CLI): allure serve reports/allure-results

## <img width="5%" title="jenkins" src="resources/images/logo/jenkins.png"> Запуск тестов в Jenkins

1) Авторизоваться в Jenkins
2) Перейти в джобу falin_pavel_dodo_pizza_tests
3) Для запуска тестов в Jenkins нажать "Build with parameters"
4) Нажать "Build"

<p><img title="jenkins_build" src="resources/images/screenshot/jenkins_build_1.png"></p>
<p><img title="jenkins_build" src="resources/images/screenshot/jenkins_build_2.png"></p>

## <img width="5%" title="allure" src="resources/images/logo/allure_report.png"> Визуализация результатов (Allure Reports и Allure TestOps)

## Если тесты запускались локально, то результаты можно посмотреть командой: 

```bash
allure serve reports/allure-results
```
## Если тесты запускались в Jenkins, то результаты можно посмотреть кликнув по иконке Allure Report в Jenkins в завершенной сборке

<p><img title="allure" src="resources/images/screenshot/allure_report_in_jenkins_1.png"></p>
<p><img title="allure" src="resources/images/screenshot/allure_report_in_jenkins_2.png"></p>
<p><img title="allure" src="resources/images/screenshot/allure_report_in_jenkins_3.png"></p>

## Для просмотра результатов тестового прогона в Allure TestOps кликнув на соответствующую ему иконку в джобе Jenkins

<p><img title="allure_testops" src="resources/images/screenshot/allure_testops_in_jenkins_1.png"></p>
<p><img title="allure_testops" src="resources/images/screenshot/allure_testops_in_jenkins_2.png"></p>
<p><img title="allure_testops" src="resources/images/screenshot/allure_testops_in_jenkins_3.png"></p>

## <img width="5%" title="tg" src="resources/images/logo/tg.png"> Интеграция с Telegram в Jenkins для автоматической отправки результатов тестового прогона через бота

<p><img title="telegram" src="resources/images/screenshot/telegram_1.png"></p>
