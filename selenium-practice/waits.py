
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.safari.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def main():
    safari_service = Service()  # this uses the selenium manager behind the scenes to manage browser drivers
    driver = webdriver.Safari(service=safari_service)
    driver.maximize_window()

    driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

    # implicit wait
    driver.implicitly_wait(5)  # number of seconds - max timeout

    driver.find_element(By.CSS_SELECTOR, '.search-keyword').send_keys('ber')

    # explicit wait

    cart_items = driver.find_elements(By.XPATH, '//div[@class="products"]/div')
    print(len(cart_items))
    assert len(cart_items) > 0

    for cart_item in cart_items:
        cart_item.find_element(By.XPATH, '//button[text()="ADD TO CART"]').click()

    driver.find_element(By.CSS_SELECTOR, 'img[alt="Cart"]').click()
    driver.find_element(By.XPATH, '//button[text()="PROCEED TO CHECKOUT"]').click()

    # need a wait for the promo code
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.promoInfo')))
    driver.find_element(By.CLASS_NAME, 'promoCode').send_keys('rahulshettyacademy')
    driver.find_element(By.CLASS_NAME, 'promoBtn').click()


    driver.close()


if __name__ == '__main__':
    main()
