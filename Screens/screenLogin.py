from appium.webdriver.common.appiumby import AppiumBy
from Screens.baseScreen import BaseScreen


class screenLogin(BaseScreen):

    def __init__(self, driver):
        super().__init__(driver)

    user = "bob@example.com"
    password = "10203040"

    def Login(self, user, password):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="open menu").click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="menu item log in").click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Username input field").send_keys(user)
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Password input field").send_keys(password)
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Login button").click()

    def loginExitoso(self):
        self.Login(self.user, self.password)
        pantallaProducto = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="products screen")
        assert pantallaProducto

    def loginConCredencialesIncorrectas(self):
        self.Login("jnujimi", self.password)
        mensajeCredencialesIncorrectas = self.driver.find_elements(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                                   value=".text(\"Provided credentials do not match "
                                                                         "any user in "
                                                                         "this service.\")")
        assert mensajeCredencialesIncorrectas

    def loginSinUsuario(self):
        self.Login("", self.password)
        mensajeErrorUsername = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Username-error-message")
        assert mensajeErrorUsername

    def loginSinPassword(self):
        self.Login(self.user, "")
        mensajeErrorPassword = self.driver.find_elements(by=AppiumBy.ANDROID_UIAUTOMATOR, value=".text(\"Password is "
                                                                                                "required\")")
        assert mensajeErrorPassword
