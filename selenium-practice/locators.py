""" this file contains a number of examples of using Selenium selectors as locators
    here is some documentation:  https://selenium-python.readthedocs.io/getting-started.html
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.safari.service import Service
from selenium.webdriver.support.select import Select


def main():
    safari_service = Service()  # this uses the selenium manager behind the scenes to manage browser drivers
    driver = webdriver.Safari(service=safari_service)
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

    # working with selections / dropdowns
    #
    # static dropdowns
    driver.get('https://rahulshettyacademy.com/angularpractice')

    dropdown = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
    dropdown.select_by_visible_text('Female')
    dropdown.select_by_index(0)
    #dropdown.select_by_value()

    # dynamic dropdowns
    driver.get('https://rahulshettyacademy.com/dropdownsPractise')

    driver.find_element(By.ID, 'autosuggest').send_keys('Ind')
    time.sleep(2)
    countries = driver.find_elements(By.CSS_SELECTOR, 'li[class="ui-menu-item"] a')

    for country in countries:
        if country.text == 'India':
            country.click()
            break

    #print(driver.find_element(By.ID, 'autosuggest').text)
    # because this is a dynamic field that is filled in by the automation script, can't use .text
    assert driver.find_element(By.ID, 'autosuggest').get_attribute('value') == 'India'

    time.sleep(3)

    # UI controls based locators
    driver.get('https://rahulshettyacademy.com/AutomationPractice')

    checkboxes = driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
    print(len(checkboxes))

    for checkbox in checkboxes:
        if checkbox.get_attribute('value') == 'option2':
            checkbox.click()
            assert checkbox.is_selected()
            break

    radio_buttons = driver.find_elements(By.CSS_SELECTOR, 'input[type="radio"]')
    for radio_button in radio_buttons:
        if radio_button.get_attribute('value') == 'radio2':
            radio_button.click()
            assert radio_button.is_selected()
            break

    time.sleep(3)

    driver.close()


if __name__ == '__main__':
    main()
