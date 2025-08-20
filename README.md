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

    📁helpers
        📁application_manager
            application_manager.py
        📁config
            links.py
        📁data
            user_info.py
        📁pages
            📁components
                📁cart
                    cart.py
                📁header
                    header_menu.py
            📁pages
                📁about_us_page
                    📁dodo_control_page
                        control_page.py
                    about_us_page.py
                📁contact_page
                    contacts_page.py
                📁home_page
                    📁products
                        📁pizza_group
                            home_page_pizza_group.py
                        📁roman_pizza_group
                            home_page_roman_pizza_group.py
                    home_page.py
    📁resources
    📁tests
        📁tests_add_products
            test_add_products_pizza.py
            test_add_products_roman_pizza.py
        📁tests_dodo_cart
            test_dodo_cart_unauthorized.py
        📁tests_dodo_control_page
            test_dodo_control_page.py
        📁tests_dodo_home_page
            test_dodo_header_menu.py
            test_dodo_user_locations.py
    📁utils
        attach.py
    .gitignore
    conftest.py
    pytest.ini
    README.md
    requirements.txt

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
