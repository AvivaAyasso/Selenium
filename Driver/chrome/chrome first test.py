from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('..\Driver\chrome\chromedriver.exe')
driver.get("http://www.facebook.com")

driver.find_element(By.XPATH, '//a[contains(text(),"שכחת את הסיסמה?")]').click()
driver.find_element(By.XPATH,'//a[@id=''u_0_2_3O'']').click()


#-------------------------------------------------------------------------------



driver = webdriver.Chrome('..\Driver\chrome\chromedriver.exe')
driver.maximize_window()
driver.get("http://www.atid.store")

#home
driver.find_element(By.XPATH,'//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[1]/a[1]').click()

#store
driver.find_element(By.XPATH,'//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]').send_keys("test")
time.sleep(5)
driver.find_element(By.XPATH,'//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]').click()

#man
driver.find_element(By.XPATH,'//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]').send_keys("skirt")
time.sleep(3)
driver.find_element(By.XPATH,'//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]').click()

#woman
driver.find_element(By.XPATH,'//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[4]/a[1]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]').send_keys("skirt")
time.sleep(3)
driver.find_element(By.XPATH,'//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]').click()

def init():
    driver = webdriver.Chrome('../../../../../../PycharmProjects/contact/chrome/chromedriver.exe')
    driver.maximize_window()
    driver.get("http://www.atid.store")
    return driver

def test_search_product_in_store():
    driver = init()
    driver.find_element(By.XPATH,'//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]').click()
    time.sleep(3)
    driver.find_element(By.XPATH,'//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]').send_keys("test.'")
    time.sleep(3)
    driver.find_element(By.XPATH,'//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]').click()
    time.sleep(3)
    value = driver.find_element(By.XPATH,'//body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/p[1]').get_attribute("innerText")
    assert value == "No products were found matching your selection."
    return value

def test_search_product_in_man():
    driver = init()
    driver.find_element(By.XPATH,'//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]').click()
    time.sleep(3)
    driver.find_element(By.XPATH,'//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]').send_keys("skirt")
    time.sleep(3)
    driver.find_element(By.XPATH,'//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]').click()
    time.sleep(3)
    value = driver.find_element(By.XPATH, '//body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/p[1]').get_attribute("innerText")
    assert value == "No products were found matching your selection."


def test_search_product_in_woman():
    driver = init()
    driver.find_element(By.XPATH,'//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[4]/a[1]').click()
    time.sleep(3)
    driver.find_element(By.XPATH,'//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]').send_keys("skirt")
    time.sleep(3)
    driver.find_element(By.XPATH,'//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]').click()
    value = driver.find_element(By.XPATH, '//body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/p[1]').get_attribute("innerText")
    assert value == "No products were found matching your selection."


test_search_product_in_woman()