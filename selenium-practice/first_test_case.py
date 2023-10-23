""" This is the first practice test case using Selenium in Python """

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()

driver.get('https://selenium.dev/')

driver.quit()