from appium.webdriver.common.appiumby import AppiumBy
from tests.conftest import driver, data
from Screens.screenProduct import screenProduct
from Screens.screenMenu import screenMenu
from Screens.screenLogin import screenLogin


def test_login(driver, data):
    product = screenProduct(driver)
    product.abrirMenu()
    menu = screenMenu(driver)
    menu.opcionLogin()
    username = data['user']
    password = data['password']
    login = screenLogin(driver)
    login.login(username, password)
    try:
        caso_exitoso = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=data['value'])
    except:
        caso_exitoso = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=data['value'])
    assert caso_exitoso
