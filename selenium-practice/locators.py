""" this file contains a number of examples of using Selenium selectors as locators """

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def main():

    driver = webdriver.Safari()
    driver.maximize_window()

    driver.implicitly_wait(10) # seconds

    driver.get('https://rahulshettyacademy.com/locatorspractice/')

    time.sleep(5)

    driver.close()


if __name__ == '__main__':
    main()