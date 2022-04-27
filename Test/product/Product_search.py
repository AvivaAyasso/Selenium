import select

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

def init():
    driver = webdriver.Chrome("../../Driver/chrome/chromedriver.exe")
    driver.maximize_window()
    driver.get("http://www.atid.store")
    return driver


def test_search_product_in_store():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-45"]').click()
    time.sleep(3)
    aviva = Select(driver.find_element(By.XPATH, '//main[1]/div[1]/form[1]/select[1]'))
    aviva.select_by_index(3)
    time.sleep(3)
    elem = driver.find_elements(By.XPATH,'//main[1]/div[1]/ul[1]/li')
    elem[5].click()
    time.sleep(3)
    driver.find_element(By.XPATH,'//button[contains(text(),"Add to cart")]').click()
    time.sleep(3)
    driver.close()
    driver.quit()


def test_search_product_in_store2():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-45"]').click()
    time.sleep(3)
    aviva = Select(driver.find_element(By.XPATH,'//main[1]/div[1]/form[1]/select[1]'))
    aviva.select_by_index(3)
    time.sleep(3)
    elem = driver.find_elements(By.XPATH,'//main[1]/div[1]/ul[1]/li')
    elem[4].click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//button[contains(text(),"Add to cart")]').click()
    time.sleep(3)
    driver.close()
    driver.quit()


def test_search_product_in_man():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-266"]').click()
    time.sleep(3)
    aviva = Select(driver.find_element(By.XPATH,'//main[1]/div[1]/form[1]/select[1]'))
    aviva.select_by_index(2)
    elem = driver.find_elements(By.XPATH,'//main[1]/div[1]/ul[1]/li')
    elem[7].click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//button[contains(text(),"Add to cart")]').click()
    time.sleep(3)
    driver.close()
    driver.quit()


def test_search_product_in_man2():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-266"]').click()
    time.sleep(3)
    aviva = Select(driver.find_element(By.XPATH,'//main[1]/div[1]/form[1]/select[1]'))
    aviva.select_by_index(2)
    time.sleep(3)
    elem = driver.find_elements(By.XPATH,'//main[1]/div[1]/ul[1]/li')
    elem[1].click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//button[contains(text(),"Add to cart")]').click()
    time.sleep(3)
    driver.close()
    driver.quit()


def test_search_product_in_woman():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-267"]').click()
    time.sleep(3)
    aviva = Select(driver.find_element(By.XPATH,'//main[1]/div[1]/form[1]/select[1]'))
    aviva.select_by_index(3)
    elem = driver.find_elements(By.XPATH,'//main[1]/div[1]/ul[1]/li')
    elem[7].click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//button[contains(text(),"Add to cart")]').click()
    time.sleep(3)
    driver.close()
    driver.quit()

def test_search_product_in_woman2():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-267"]').click()
    time.sleep(3)
    aviva = Select(driver.find_element(By.XPATH,'//main[1]/div[1]/form[1]/select[1]'))
    aviva.select_by_index(3)
    elem = driver.find_elements(By.XPATH,'//main[1]/div[1]/ul[1]/li')
    elem[9].click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//button[contains(text(),"Add to cart")]').click()
    time.sleep(3)
    driver.close()
    driver.quit()


def test_search_product_in_accessories():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-671"]').click()
    time.sleep(3)
    aviva = Select(driver.find_element(By.XPATH,'//main[1]/div[1]/form[1]/select[1]'))
    aviva.select_by_index(1)
    time.sleep(3)
    elem = driver.find_elements(By.XPATH,'//main[1]/div[1]/ul[1]/li')
    elem[1].click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//button[contains(text(),"Add to cart")]').click()
    time.sleep(3)
    driver.close()
    driver.quit()

def test_search_product_in_accessories2():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-671"]').click()
    time.sleep(3)
    aviva = Select(driver.find_element(By.XPATH,'//main[1]/div[1]/form[1]/select[1]'))
    aviva.select_by_index(1)
    time.sleep(3)
    elem = driver.find_elements(By.XPATH,'//main[1]/div[1]/ul[1]/li')
    elem[3].click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//button[contains(text(),"Add to cart")]').click()
    time.sleep(3)
    driver.close()
    driver.quit()

