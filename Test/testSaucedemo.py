from appium.webdriver.common.appiumby import AppiumBy

from Test.fixtures import driver
from Screens.screenProduct import screenProduct
from Screens.screenMenu import screenMenu
from Screens.screenLogin import screenLogin


class TestLogin:

    def testLoginExitoso(self, driver):
        product = screenProduct(driver)
        menu = screenMenu(driver)
        login = screenLogin(driver)
        product.abrirMenu()
        menu.opcionLogin()
        login.ingresarUsuario("bob@example.com")
        login.ingresarContrasena("10203040")
        login.botonLogin()
        exito = login.loginExitoso()
        assert exito

    def testCredencialesIncorrectas(self, driver):
        product = screenProduct(driver)
        menu = screenMenu(driver)
        login = screenLogin(driver)
        product.abrirMenu()
        menu.opcionLogin()
        login.ingresarUsuario("bob1@example.com")
        login.ingresarContrasena("10203040")
        login.botonLogin()
        validacion = login.loginConCredencialesIncorrectas()
        assert validacion

    def testSinUsuario(self, driver):
        product = screenProduct(driver)
        menu = screenMenu(driver)
        login = screenLogin(driver)
        product.abrirMenu()
        menu.opcionLogin()
        login.ingresarUsuario("")
        login.ingresarContrasena("10203040")
        login.botonLogin()
        validacion = login.loginSinUsuario()
        assert validacion

    def testSinContresena(self, driver):
        product = screenProduct(driver)
        menu = screenMenu(driver)
        login = screenLogin(driver)
        product.abrirMenu()
        menu.opcionLogin()
        login.ingresarUsuario("bob1@example.com")
        login.ingresarContrasena("")
        login.botonLogin()
        validacion = login.loginSinPassword()
        assert validacion
