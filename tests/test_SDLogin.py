import os

from appium.webdriver.common.appiumby import AppiumBy

from Screens.screenProduct import screenProduct
from Screens.screenMenu import screenMenu
from Screens.screenLogin import screenLogin

import secrets
import string


def base_login(driver, username, password):
    product = screenProduct(driver)
    product.abrirMenu()
    menu = screenMenu(driver)
    menu.opcionLogin()
    login = screenLogin(driver)
    login.login(username, password)


def test_login_exito(driver):
    username = os.getenv("USERNAMESUCCESS")
    password = os.getenv("PASSWORDSUCCESS")
    base_login(driver, username, password)
    product = screenProduct(driver)
    assert product.existe_el_elemento(*product.lbl_productos)


def test_login_sin_username(driver):
    username = os.getenv("USERNAMENONEXISTENT")
    password = os.getenv("PASSWORDSUCCESS")
    base_login(driver, username, password)
    login = screenLogin(driver)
    assert login.existe_el_elemento(*login.lbl_dismatch)


def test_login_no_username(driver):
    username = os.getenv("NODATA")
    password = os.getenv("PASSWORDSUCCESS")
    base_login(driver, username, password)
    login = screenLogin(driver)
    assert login.existe_el_elemento(*login.lbl_nousername)


def test_login_no_password(driver):
    username = os.getenv("USERNAMESUCCESS")
    password = os.getenv("NODATA")
    base_login(driver, username, password)
    login = screenLogin(driver)
    assert login.existe_el_elemento(*login.lbl_nousername)


def test_login_password_aleatorio(driver):
    username = os.getenv("USERNAMESUCCESS")
    letras = string.ascii_letters
    digitos = string.digits
    caracteres_especiales = string.punctuation
    alfabeto = letras+digitos+caracteres_especiales
    password_longitud = 12
    password = ''
    for i in range(password_longitud):
        password += ''.join(secrets.choice(alfabeto))
    base_login(driver, username, password)
    login = screenLogin(driver)
    assert login.existe_el_elemento(*login.lbl_dismatch)


