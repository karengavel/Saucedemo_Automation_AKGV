from Test.fixtures import driver
from Screens.screenLogin import screenLogin


class TestLogin:

    def testLoginScreen(self, driver):
        login = screenLogin(driver)
        login.loginExitoso()

    def testCredencialesIncorrectas(self, driver):
        login = screenLogin(driver)
        login.loginConCredencialesIncorrectas()

    def testSinUsuario(self, driver):
        login = screenLogin(driver)
        login.loginConCredencialesIncorrectas()

    def testSinContresena(self, driver):
        login = screenLogin(driver)
        login.loginSinPassword()
