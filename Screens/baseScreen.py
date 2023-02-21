from selenium.common import NoSuchElementException


class BaseScreen:

    def __init__(self, driver):
        self.driver = driver

    def encuentra_elemento(self, *locator):
        return self.driver.find_element(*locator)

    def existe_el_elemento(self, *locator):
        try:
            self.get_element(*locator)
            return True
        except NoSuchElementException:
            return False
