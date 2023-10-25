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
    driver.find_element(By.ID,'inputUsername').send_keys('tester')
    driver.find_element(By.NAME,'inputPassword').send_keys('random passwd')
    driver.find_element(By.CLASS_NAME, 'signInBtn').click()
    # verify incorrect name or password message
    message = driver.find_element(By.CLASS_NAME,'error').text
    assert 'Incorrect' in message

    # click on Forgot Password and create a user login
    driver.find_element(By.LINK_TEXT,'Forgot your password?').click()

    time.sleep(3) # pause so we can see the website

    driver.find_element(By.CSS_SELECTOR,'input[placeholder="Name"]').send_keys('john')
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Email"]').send_keys('john@email.com')
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Phone Number"]').send_keys('4804409982')

    driver.find_element(By.CSS_SELECTOR,'.reset-pwd-btn').click()
    message = driver.find_element(By.CSS_SELECTOR,'.infoMsg').text
    assert 'temporary password' in message

    driver.find_element(By.CSS_SELECTOR,'.go-to-login-btn').click()

    time.sleep(3)

    driver.close()


if __name__ == '__main__':
    main()
