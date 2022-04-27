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
    #call the driver function
    driver = init()

    #go to store page
    driver.find_element(By.XPATH,'//li[@id="menu-item-45"]').click()

    #go to list and choose category
    category = Select(driver.find_element(By.XPATH, '//main[1]/div[1]/form[1]/select[1]'))
    category.select_by_index(3)

    #choose product
    product = driver.find_elements(By.XPATH,'//main[1]/div[1]/ul[1]/li')
    product[5].click()

    # adding to cart
    driver.find_element(By.XPATH,'//button[contains(text(),"Add to cart")]').click()

    #going back to the store page
    driver.find_element(By.XPATH,'//li[@id="menu-item-45"]').click()

    #go to list and choose category
    category1 = Select(driver.find_element(By.XPATH,'//main[1]/div[1]/form[1]/select[1]'))
    category1.select_by_index(3)

    # choose Another product
    product1 = driver.find_elements(By.XPATH,'//main[1]/div[1]/ul[1]/li')
    product1[4].click()

    # adding to cart
    driver.find_element(By.XPATH, '//button[contains(text(),"Add to cart")]').click()

    #go to cart
    driver.find_element(By.XPATH,'//header/div[@id="ast-desktop-header"]/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]/a[1]').click()

    #verify that the registered name is the same as the defined name
    denim_jeans = driver.find_element(By.XPATH,'//a[contains(text(),"Dark Blue Denim Jeans")]').get_attribute("innerText")
    assert denim_jeans == "Dark Blue Denim Jeans"

    # verify that the registered price is the same as the defined price
    denim_jeans_price = driver.find_element(By.XPATH,'//tbody/tr[2]/td[6]/span[1]').get_attribute("innerText").split(".")
    assert denim_jeans_price[0] == "150"

    # verify that the registered name is the same as the defined name
    brown_jeans= driver.find_element(By.XPATH,'//a[contains(text(),"Dark Brown Jeans")]').get_attribute("innerText")
    assert brown_jeans == "Dark Brown Jeans"

    # verify that the registered price is the same as the defined price
    brown_jeans_price = driver.find_element(By.XPATH,'//tbody/tr[1]/td[6]/span[1]').get_attribute("innerText").split(".")
    assert brown_jeans_price[0] == "150"

    #Calculating the price of the products and comparing them to the final price
    sum = int(denim_jeans_price[0])+int(brown_jeans_price[0])
    total = driver.find_element(By.XPATH,'//tbody/tr[1]/td[1]/span[1]').get_attribute("innerText").split(".")
    assert int(total[0]) == sum

    #Closing and leaving the site
    driver.close()
    driver.quit()



def test_search_product_in_man():
    # call the driver function
    driver = init()

    # go to man page
    driver.find_element(By.XPATH,'//li[@id="menu-item-266"]').click()

    # go to list and choose category
    category = Select(driver.find_element(By.XPATH,'//main[1]/div[1]/form[1]/select[1]'))
    category.select_by_index(2)

    # choose product
    product = driver.find_elements(By.XPATH,'//main[1]/div[1]/ul[1]/li')
    product[3].click()

    # adding to cart
    driver.find_element(By.XPATH, '//button[contains(text(),"Add to cart")]').click()

    # going back to the man page
    driver.find_element(By.XPATH,'//li[@id="menu-item-266"]').click()

    # go to list and choose category
    category1 = Select(driver.find_element(By.XPATH,'//main[1]/div[1]/form[1]/select[1]'))
    category1.select_by_index(2)

    # choose Another product
    product1 = driver.find_elements(By.XPATH,'//main[1]/div[1]/ul[1]/li')
    product1[1].click()

    # adding to cart
    driver.find_element(By.XPATH, '//button[contains(text(),"Add to cart")]').click()

    #go to cart
    driver.find_element(By.XPATH,'//header/div[@id="ast-desktop-header"]/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]/a[1]').click()

    # verify that the registered name is the same as the defined name
    blue_shoes = driver.find_element(By.XPATH,'//a[contains(text(),"ATID Blue Shoes")]').get_attribute("innerText")
    assert blue_shoes == "ATID Blue Shoes"

    # verify that the registered price is the same as the defined price
    blue_shoes_price = driver.find_element(By.XPATH,'//tbody/tr[1]/td[6]/span[1]').get_attribute("innerText").split(".")
    assert blue_shoes_price[0] == "80"

    # verify that the registered name is the same as the defined name
    yellow_shoes = driver.find_element(By.XPATH,'//a[contains(text(),"ATID Yellow Shoes")]').get_attribute("innerText")
    assert yellow_shoes == "ATID Yellow Shoes"

    # verify that the registered price is the same as the defined price
    yellow_shoes_price = driver.find_element(By.XPATH,'//tbody/tr[2]/td[6]/span[1]').get_attribute("innerText").split(".")
    assert yellow_shoes_price[0] == "120"

    #Calculating the price of the products and comparing them to the final price
    sum = int(blue_shoes_price[0])+int(yellow_shoes_price[0])
    total = driver.find_element(By.XPATH,'//tbody/tr[1]/td[1]/span[1]').get_attribute("innerText").split(".")
    assert int(total[0]) == sum

    #Closing and leaving the site
    driver.close()
    driver.quit()


def test_search_product_in_woman():
    # call the driver function
    driver = init()

    # go to woman page
    driver.find_element(By.XPATH,'//li[@id="menu-item-267"]').click()

    # go to list and choose category
    category = Select(driver.find_element(By.XPATH,'//main[1]/div[1]/form[1]/select[1]'))
    category.select_by_index(3)

    # choose product
    product = driver.find_elements(By.XPATH,'//main[1]/div[1]/ul[1]/li')
    product[7].click()

    # adding to cart
    driver.find_element(By.XPATH, '//button[contains(text(),"Add to cart")]').click()

    # going back to the woman page
    driver.find_element(By.XPATH,'//li[@id="menu-item-267"]').click()

    # go to list and choose category
    category1 = Select(driver.find_element(By.XPATH,'//main[1]/div[1]/form[1]/select[1]'))
    category1.select_by_index(3)

    # choose Another product
    product1 = driver.find_elements(By.XPATH,'//main[1]/div[1]/ul[1]/li')
    product1[9].click()

    # adding to cart
    driver.find_element(By.XPATH, '//button[contains(text(),"Add to cart")]').click()

    #go to cart
    driver.find_element(By.XPATH,'//header/div[@id="ast-desktop-header"]/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]/a[1]').click()

    # verify that the registered name is the same as the defined name
    tshirt = driver.find_element(By.XPATH,'//a[contains(text(),"Flamingo Tshirt")]').get_attribute("innerText")
    assert tshirt == "Flamingo Tshirt"

    # verify that the registered price is the same as the defined price
    tshirt_price = driver.find_element(By.XPATH,'//tbody/tr[1]/td[6]/span[1]').get_attribute("innerText").split(".")
    assert tshirt_price[0] == "50"

    # verify that the registered name is the same as the defined name
    white_tshirt = driver.find_element(By.XPATH,'//a[contains(text(),"White Underground Tshirt")]').get_attribute("innerText")
    assert white_tshirt == "White Underground Tshirt"

    # verify that the registered price is the same as the defined price
    white_tshirt_price = driver.find_element(By.XPATH,'//tbody/tr[2]/td[6]/span[1]').get_attribute("innerText").split(".")
    assert white_tshirt_price[0] == "150"

    # Calculating the price of the products and comparing them to the final price
    sum = int(tshirt_price[0])+int(white_tshirt_price[0])
    total = driver.find_element(By.XPATH,'//tbody/tr[1]/td[1]/span[1]').get_attribute("innerText").split(".")
    assert int(total[0]) == sum

    # Closing and leaving the site
    driver.close()
    driver.quit()


def test_search_product_in_accessories():
    # call the driver function
    driver = init()

    # go to accessories page
    driver.find_element(By.XPATH,'//li[@id="menu-item-671"]').click()

    # go to list and choose category
    category = Select(driver.find_element(By.XPATH,'//main[1]/div[1]/form[1]/select[1]'))
    category.select_by_index(1)

    # choose product
    product = driver.find_elements(By.XPATH,'//main[1]/div[1]/ul[1]/li')
    product[1].click()

    # adding to cart
    driver.find_element(By.XPATH, '//button[contains(text(),"Add to cart")]').click()

    # going back to the accessories page
    driver.find_element(By.XPATH, '//li[@id="menu-item-671"]').click()

    # go to list and choose category
    category1 = Select(driver.find_element(By.XPATH,'//main[1]/div[1]/form[1]/select[1]'))
    category1.select_by_index(1)

    # choose Another product
    product1 = driver.find_elements(By.XPATH,'//main[1]/div[1]/ul[1]/li')
    product1[3].click()

    # adding to cart
    driver.find_element(By.XPATH, '//button[contains(text(),"Add to cart")]').click()

    #go to cart
    driver.find_element(By.XPATH,'//header/div[@id="ast-desktop-header"]/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]/a[1]').click()

    # verify that the registered name is the same as the defined name
    handbag = driver.find_element(By.XPATH,'//a[contains(text(),"Black Over-the-shoulder Handbag")]').get_attribute("innerText")
    assert handbag == "Black Over-the-shoulder Handbag"

    # verify that the registered price is the same as the defined price
    handbag_price = driver.find_element(By.XPATH, '//tbody/tr[2]/td[6]/span[1]').get_attribute("innerText").split(".")
    assert handbag_price[0] == "85"

    # verify that the registered name is the same as the defined name
    bag = driver.find_element(By.XPATH,'//a[contains(text(),"Bright Red Bag")]').get_attribute("innerText")
    assert bag == "Bright Red Bag"

    # verify that the registered price is the same as the defined price
    bag_price = driver.find_element(By.XPATH,'//tbody/tr[1]/td[6]/span[1]').get_attribute("innerText").split(".")
    assert bag_price[0] == "150"

    # Calculating the price of the products and comparing them to the final price
    sum = int(handbag_price[0]) + int(bag_price[0])
    total = driver.find_element(By.XPATH,'//tbody/tr[1]/td[1]/span[1]').get_attribute("innerText").split(".")
    assert int(total[0]) == sum

    # Closing and leaving the site
    driver.close()
    driver.quit()
