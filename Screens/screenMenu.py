from appium.webdriver.common.appiumby import AppiumBy

from Screens.baseScreen import BaseScreen


class screenMenu(BaseScreen):

    def __init__(self, driver):
        super().__init__(driver)

    def opcionLogin(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="menu item log in").click()
