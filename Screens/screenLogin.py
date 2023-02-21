from appium.webdriver.common.appiumby import AppiumBy
from Screens.baseScreen import BaseScreen


class screenLogin(BaseScreen):

    def __init__(self, driver):
        super().__init__(driver)
        self.txtbox_username = (AppiumBy.ACCESSIBILITY_ID, "Username input field")
        self.txtbox_password = (AppiumBy.ACCESSIBILITY_ID, "Password input field")
        self.btn_login = (AppiumBy.ACCESSIBILITY_ID, "Login button")

    def login(self, username, password):
        self.driver.find_element(*self.txtbox_username).send_keys(username)
        self.driver.find_element(*self.txtbox_password).send_keys(password)
        self.driver.find_element(*self.btn_login).click()