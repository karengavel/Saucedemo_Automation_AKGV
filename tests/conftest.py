import pytest
import yaml
from appium import webdriver

DESIRED_CAPABILITIES = {
    "platformName": "Android",
    "appium:platformVersion": "11",
    "appium:deviceName": "PixelXL",
    "appium:automationName": "UiAutomator2",
    "appium:app": "/Users/agamav/Desktop/Training/Saucedemo_Automation_AKGV/App/saucedemo.apk"
}

DATA_PATH = "../utils/data.yml"

URL = "http://0.0.0.0:4723/wd/hub"


# Función que lee el archivo yaml.
def load_data(path):
    with open(path) as data:
        return yaml.safe_load(data)


# Fixture. Carga el archivo con los datos.
@pytest.fixture(params=load_data(DATA_PATH))
def data(request):
    return request.param


@pytest.fixture
def driver():
    wait_seconds = 5
    driver = webdriver.Remote(URL, DESIRED_CAPABILITIES)
    driver.implicitly_wait(wait_seconds)
    yield driver
    driver.quit()
