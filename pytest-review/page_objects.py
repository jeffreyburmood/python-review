""" work on some examples using POM technique """
from selenium import webdriver
from selenium.webdriver.safari.service import Service
from page_objects.login_page import LoginPage

class TestWithPOM:

    def test_useLoginPage(self):
        safari_service = Service()  # this uses the selenium manager behind the scenes to manage browser drivers
        driver = webdriver.Safari(service=safari_service)

        # use login PO
        login_page = LoginPage(driver)
        driver.get('https://rahulshettyacademy.com')
