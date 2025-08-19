import pytest

from selene import browser
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    chrome_options = Options()
    prefs = {
        "profile.default_content_settings.popups": 0,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.geolocation": 2,  # 2 = Block
        "profile.managed_default_content_settings.geolocation": 2
    }
    chrome_options.add_experimental_option(name="prefs", value=prefs)
    chrome_options.page_load_strategy = 'eager'
    chrome_options.add_argument("--disable-geolocation")
    chrome_options.add_argument("--disable-features=Geolocation")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    browser.config.driver_options = chrome_options
    yield
    browser.quit()
