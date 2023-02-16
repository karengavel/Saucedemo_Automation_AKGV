import pytest
from appium.webdriver.common.appiumby import AppiumBy
from Test.fixtures import driver


def testLogin(driver):
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="open menu").click()
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="menu item log in").click()
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Username input field").send_keys("bob@example.com")
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Password input field").send_keys("10203040")
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Login button").click()
    pantallaProducto = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="products screen")
    assert pantallaProducto


def testLoginConCredencialesIncorrectas(driver):
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="open menu").click()
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="menu item log in").click()
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Username input field").send_keys("bob@example")
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Password input field").send_keys("10203040")
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Login button").click()
    mensajeCredencialesIncorrectas = driver.find_elements(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                          value=".text(\"Provided credentials do not match any user in "
                                                                "this service.\")")
    assert mensajeCredencialesIncorrectas
