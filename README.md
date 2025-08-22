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
