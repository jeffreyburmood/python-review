from selenium.webdriver.common.by import By


class LoginPage:

    login_name = (By.CSS_SELECTOR, '.login_name')

    def __int__(self, driver):
        self.driver = driver

    def get_login_name(self):
        return self.driver.find_element(*LoginPage.login_name)