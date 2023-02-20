from appium.webdriver.common.appiumby import AppiumBy

from Screens.baseScreen import BaseScreen


class screenProduct(BaseScreen):

    def __init__(self, driver):
        super().__init__(driver)

    def abrirMenu(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="open menu").click()
