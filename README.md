# 🎓 QA.GURU Graduation Project

Автоматизация тестирования веб-приложений "Додо Пицца" с помощью Python, Pytest и Selene 🚀

## 📖 О проекте

Этот фреймворк предназначен для автоматизации тестирования веб-приложения "Додо Пицца" (https://dodopizza.ru/) и написан с использованием инструментов:

<p  align="center">
  <code><img width="5%" title="Pycharm" src="resources/images/logo/pycharm.png" alt="pycharm"></code>
  <code><img width="5%" title="Python" src="resources/images/logo/python.png" alt="python"></code>
  <code><img width="5%" title="Pytest" src="resources/images/logo/pytest.png" alt="pytest"></code>
  <code><img width="5%" title="Selene" src="resources/images/logo/selene.png" alt="selene"></code>
  <code><img width="5%" title="Selenium" src="resources/images/logo/selenium.png" alt="selenium"></code>
  <code><img width="5%" title="GitHub" src="resources/images/logo/github.png" alt="github"></code>
  <code><img width="5%" title="Jenkins" src="resources/images/logo/jenkins.png" alt="jenkins"></code>
  <code><img width="5%" title="Allure Report" src="resources/images/logo/allure_report.png" alt="allure"></code>
  <code><img width="5%" title="Telegram" src="resources/images/logo/tg.png" alt="telegram"></code>
</p>

# Структура проекта

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

## Запуск тестов локально

1) Клонировать репозиторий: git clone https://github.com/falinpavel/qa_guru_graduation_project.git
2) Установить зависимости: pip install -r requirements.txt
3) Запуск тестов с генерацией отчетов Allure: pytest --alluredir=reports/allure-results
4) Просмотр отчета Allure (если установлен Allure CLI): allure serve reports/allure-results

## Запуск тестов в Jenkins

1) Авторизоваться в Jenkins
2) Перейти в джобу falin_pavel_dodo_pizza_tests
3) Для запуска тестов в Jenkins нажать "Build with parameters"
4) Нажать "Build"

# Визуализация результатов

### Если тесты запускались локально, то результаты можно посмотреть командой: 
```bash
allure serve reports/allure-results
```
### Если тесты запускались в Jenkins, то результаты можно посмотреть кликнув по иконке Allure в Jenkins в завершенной сборке

<p><img title="Jenkins_Allure" src="resources/images/screenshot/allure_report_in_jenkins_1.png"></p>
<p><img title="Jenkins_Allure" src="resources/images/screenshot/allure_report_in_jenkins_2.png"></p>
<p><img title="Jenkins_Allure" src="resources/images/screenshot/allure_report_in_jenkins_3.png"></p>

# Интеграция с Telegram для отправки результатов тестов (на уровне Jenkins)

<p><img title="Telegram" src="resources/images/screenshot/telegram_1.png"></p>
