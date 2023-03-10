import pytest
from appium import webdriver

DESIRED_CAPABILITIES = {
    "platformName": "Android",
    "appium:platformVersion": "11",
    "appium:deviceName": "PixelXL",
    "appium:automationName": "UiAutomator2",
    "appium:app": "/Users/agamav/Desktop/Training/Saucedemo_Automation_AKGV/App/saucedemo.apk"
}

URL = "http://0.0.0.0:4723/wd/hub"


@pytest.fixture
def driver(request):
    wait_seconds = 5
    driver = webdriver.Remote(URL, DESIRED_CAPABILITIES)
    driver.implicitly_wait(wait_seconds)
    yield driver
    driver.quit()
