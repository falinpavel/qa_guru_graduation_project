# 🎓 QA Guru Graduation Project
Автоматизация тестирования веб-приложений с помощью Python, Pytest и Selene 🚀

### 📖 О проекте
Этот фреймворк предназначен для автоматизации тестирования веб-приложений и написан с использованием инструментов:

🐍 Python
✅ Pytest
🌐 Selene
🕷️ Selenium WebDriver

### Цель — писать поддерживаемые, читаемые и надежные тесты, используя лучшие практики автоматизации.

## ⚙️ Реализовано
📂 Чистая архитектура с использованием паттерна Page Object

🧪 Поддержка параметризации и фикстур Pytest

📊 Интеграция с Allure Report — красивые отчеты о тестах

🎭 Генерация уникальных тестовых данных с помощью Faker

## 🗂️ Структура проекта

    📁helpers (все файлы в этом каталоге являются вспомогательными)
        📁application_manager
            application_manager.py (application manager - хранятся все страницы и компоненты)
        📁config
            links.py (содержит ссылки на сайт, которые используются в тестах)
        📁data
            user_info.py (содержит данные для тестовых пользователей, генерируемые с помощью Faker)
        📁pages
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
                    home_page.py (главная страница с описанием общих функциональностей)
    📁resources (файлы, которые используются в тестах)
    📁tests (все файлы в этом каталоге являются тестами)
        📁tests_add_products (группа тестов, которые проверяют добавление продуктов в корзину)
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

## 🏃 Быстрый старт

| Запуск локально                                                                                |Запуск в Jenkins | 
|------------------------------------------------------------------------------------------------|---------------:|
| Клонировать репозиторий: git clone https://github.com/falinpavel/qa_guru_graduation_project.git |  |
| Установить зависимости: pip install -r requirements.txt                                        |  |
| Запуск тестов с генерацией отчетов Allure: pytest --alluredir=reports/allure-results           |  |
| Просмотр отчета Allure (если установлен Allure CLI): allure serve reports/allure-results                                          |  |
|                                                                                                |  |
|                                                                                                |  |

## 🖼️ Визуализация результатов
