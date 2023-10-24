""" this file contains a number of examples of using Selenium selectors as locators
    here is some documentation:  https://selenium-python.readthedocs.io/getting-started.html
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def main():
    driver = webdriver.Safari()
    driver.maximize_window()

    driver.implicitly_wait(10)  # seconds

    driver.get('https://rahulshettyacademy.com/locatorspractice/')

    # first try to login in using bad credentials
    driver.find_element_by_id('inputUsername').send_keys('tester')
    driver.find_element_by_name('inputPassword').send_keys('random passwd')
    driver.find_element_by_class_name('signInBtn').click()
    # verify incorrect name or password message
    print(driver.find_element_by_class_name('error').text)

    # click on Forgot Password and create a user login
    driver.find_element_by_link_text('Forgot your password?').click()

    time.sleep(3) # pause so we can see the website

    driver.find_element_by_css_selector('input[placeholder="Name"]').send_keys('john')
    driver.find_element_by_css_selector('input[placeholder="Email"]').send_keys('john@email.com')
    driver.find_element_by_css_selector('input[placeholder="Phone Number"]').send_keys('4804409982')

    driver.find_element_by_css_selector('.reset-pwd-btn').click()
    print(driver.find_element_by_css_selector('.infoMsg').text)

    driver.find_element_by_css_selector('.go-to-login-btn').click()

    time.sleep(3)

    driver.close()


if __name__ == '__main__':
    main()
