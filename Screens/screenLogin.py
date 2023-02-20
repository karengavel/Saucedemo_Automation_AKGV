from appium.webdriver.common.appiumby import AppiumBy
from Screens.baseScreen import BaseScreen


class screenLogin(BaseScreen):

    def __init__(self, driver):
        super().__init__(driver)

    user = "bob@example.com"
    password = "10203040"

    def ingresarUsuario(self, user):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Username input field").send_keys(user)

    def ingresarContrasena(self, password):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Password input field").send_keys(password)

    def botonLogin(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Login button").click()

    def loginExitoso(self):
        exito = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="products screen")
        return exito

    def loginConCredencialesIncorrectas(self):
        mensajeValidacion = self.driver.find_elements(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                      value=".text(\"Provided credentials do not match "
                                                            "any user in "
                                                            "this service.\")")
        return mensajeValidacion

    def loginSinUsuario(self):
        sinUsuario = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Username-error-message")
        return sinUsuario

    def loginSinPassword(self):
        sinPassword = self.driver.find_elements(by=AppiumBy.ANDROID_UIAUTOMATOR, value=".text(\"Password is "
                                                                                       "required\")")
        return sinPassword
