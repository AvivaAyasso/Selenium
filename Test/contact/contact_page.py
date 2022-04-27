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

def test_title_correctly():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-829"]').click()
    time.sleep(3)
    text = driver.find_element(By.XPATH,'//body/div[@id="page"]/div[@id="content"]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]').get_attribute("innerText")
    assert text == "You tell us. We listen."


def test_email_correctly():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-829"]').click()
    time.sleep(3)
    email = driver.find_element(By.XPATH,'//span[contains(text(),"hello@atid.store")]').get_attribute("innerText")
    assert email == "hello@atid.store"


def test_phone_number_correctly():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-829"]').click()
    time.sleep(3)
    phone = driver.find_element(By.XPATH,'// span[contains(text(), "972-52-1234567")]').get_attribute("innerText")
    assert phone == "972-52-1234567"


def test_time_one_correctly():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-829"]').click()
    time.sleep(3)
    time_one = driver.find_element(By.XPATH,'//span[contains(text(),"Sunday to Thursday - 9:00 am to 7:00 pm")]').get_attribute("innerText")
    assert time_one == "Sunday to Thursday - 9:00 am to 7:00 pm"


def test_time_tow_correctly():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-829"]').click()
    time.sleep(3)
    test_time_tow_correctly = driver.find_element(By.XPATH,'//span[contains(text(),"Friday - 8:00 am to 3:00 pm")]').get_attribute("innerText")
    assert test_time_tow_correctly == "Friday - 8:00 am to 3:00 pm"


def test_title_two_correctly():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-829"]').click()
    time.sleep(3)
    title_two = driver.find_element(By.XPATH,'//h4[contains(text(),"Need Help? Call Us.")]').get_attribute("innerText")
    assert title_two == "Need Help? Call Us."


def test_big_phone_number_correctly():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-829"]').click()
    time.sleep(3)
    big_phone = driver.find_element(By.XPATH,'//h3[contains(text(),"972-52-1234567")]').get_attribute("innerText")
    assert big_phone == "972-52-1234567"


def test_title_three_correctly():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-829"]').click()
    time.sleep(3)
    title_three = driver.find_element(By.XPATH,'//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[1]/div[1]/h3[1]').get_attribute("innerText")
    assert title_three == "Have any Queries? We're here to help."


###################################################################################################################################################################

def test_name_field_correctly():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-829"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//input[@id="wpforms-15-field_0"]').send_keys("Aviva")
    time.sleep(3)
    driver.find_element(By.XPATH,'//input[@id="wpforms-15-field_5"]').send_keys()
    time.sleep(3)
    driver.find_element(By.XPATH,'//input[@id="wpforms-15-field_4"]').send_keys()
    time.sleep(3)
    driver.find_element(By.XPATH,'//textarea[@id="wpforms-15-field_2"]').send_keys()
    time.sleep(3)
    driver.find_element(By.XPATH,'//button[@id="wpforms-submit-15"]').click()
    time.sleep(3)
    error_email = driver.find_element(By.XPATH,'//label[@id="wpforms-15-field_4-error"]').get_attribute("innerText")
    assert error_email == "This field is required."
    time.sleep(3)
    error_message = driver.find_element(By.XPATH,'//label[@id="wpforms-15-field_2-error"]').get_attribute("innerText")
    assert error_message == "This field is required."
    time.sleep(3)



def test_name_field_incorrectly():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-829"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//input[@id="wpforms-15-field_0"]').send_keys("@#%%156^^$")
    time.sleep(3)
    driver.find_element(By.XPATH,'//input[@id="wpforms-15-field_5"]').send_keys()
    time.sleep(3)
    driver.find_element(By.XPATH,'//input[@id="wpforms-15-field_4"]').send_keys("kkkkk")
    time.sleep(3)
    driver.find_element(By.XPATH,'//textarea[@id="wpforms-15-field_2"]').send_keys()
    time.sleep(3)
    driver.find_element(By.XPATH,'//button[@id="wpforms-submit-15"]').click()
    time.sleep(3)
    error_email = driver.find_element(By.XPATH,'//label[@id="wpforms-15-field_4-error"]').get_attribute("innerText")
    assert error_email == "This field is required."
    time.sleep(3)
    error_message = driver.find_element(By.XPATH,'//label[@id="wpforms-15-field_2-error"]').get_attribute("innerText")
    assert error_message == "This field is required."
    time.sleep(3)


def test_subject_field_correctly():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-829"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//input[@id="wpforms-15-field_0"]').send_keys()
    time.sleep(3)
    driver.find_element(By.XPATH,'//input[@id="wpforms-15-field_5"]').send_keys("Hello")
    time.sleep(3)
    driver.find_element(By.XPATH,'//input[@id="wpforms-15-field_4"]').send_keys()
    time.sleep(3)
    driver.find_element(By.XPATH,'//textarea[@id="wpforms-15-field_2"]').send_keys()
    time.sleep(3)
    driver.find_element(By.XPATH,'//button[@id="wpforms-submit-15"]').click()
    time.sleep(3)
    error_name = driver.find_element(By.XPATH,'//label[@id="wpforms-15-field_0-error"]').get_attribute("innerText")
    assert error_name == "This field is required."
    time.sleep(3)
    error_email = driver.find_element(By.XPATH,'//label[@id="wpforms-15-field_4-error"]').get_attribute("innerText")
    assert error_email == "This field is required."
    time.sleep(3)
    error_message = driver.find_element(By.XPATH,'//label[@id="wpforms-15-field_2-error"]').get_attribute("innerText")
    assert error_message == "This field is required."
    time.sleep(3)

def test_subject_field_incorrectly():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-829"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//input[@id="wpforms-15-field_0"]').send_keys()
    time.sleep(3)
    driver.find_element(By.XPATH,'//input[@id="wpforms-15-field_5"]').send_keys("@#$#@")
    time.sleep(3)
    driver.find_element(By.XPATH,'//input[@id="wpforms-15-field_4"]').send_keys()
    time.sleep(3)
    driver.find_element(By.XPATH,'//textarea[@id="wpforms-15-field_2"]').send_keys()
    time.sleep(3)
    driver.find_element(By.XPATH,'//button[@id="wpforms-submit-15"]').click()
    time.sleep(3)
    error_name = driver.find_element(By.XPATH,'//label[@id="wpforms-15-field_0-error"]').get_attribute("innerText")
    assert error_name == "This field is required."
    time.sleep(3)
    error_email = driver.find_element(By.XPATH,'//label[@id="wpforms-15-field_4-error"]').get_attribute("innerText")
    assert error_email == "This field is required."
    time.sleep(3)
    error_message = driver.find_element(By.XPATH,'//label[@id="wpforms-15-field_2-error"]').get_attribute("innerText")
    assert error_message == "This field is required."
    time.sleep(3)

def test_email_field_correctly():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-829"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//input[@id="wpforms-15-field_0"]').send_keys()
    time.sleep(3)
    driver.find_element(By.XPATH,'//input[@id="wpforms-15-field_5"]').send_keys()
    time.sleep(3)
    driver.find_element(By.XPATH,'//input[@id="wpforms-15-field_4"]').send_keys("avivaayasso0@gmail.com")
    time.sleep(3)
    driver.find_element(By.XPATH,'//textarea[@id="wpforms-15-field_2"]').send_keys()
    time.sleep(3)
    driver.find_element(By.XPATH,'//button[@id="wpforms-submit-15"]').click()
    time.sleep(3)
    error_name = driver.find_element(By.XPATH,'//label[@id="wpforms-15-field_0-error"]').get_attribute("innerText")
    assert error_name == "This field is required."
    time.sleep(3)
    error_message = driver.find_element(By.XPATH, '//label[@id="wpforms-15-field_2-error"]').get_attribute("innerText")
    assert error_message == "This field is required."
    time.sleep(3)


def test_email_field_incorrectly():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-829"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//input[@id="wpforms-15-field_0"]').send_keys()
    time.sleep(3)
    driver.find_element(By.XPATH,'//input[@id="wpforms-15-field_5"]').send_keys()
    time.sleep(3)
    driver.find_element(By.XPATH,'//input[@id="wpforms-15-field_4"]').send_keys("avivaayasso0@gmail")
    time.sleep(3)
    driver.find_element(By.XPATH,'//textarea[@id="wpforms-15-field_2"]').send_keys()
    time.sleep(3)
    driver.find_element(By.XPATH,'//button[@id="wpforms-submit-15"]').click()
    time.sleep(3)
    error_name = driver.find_element(By.XPATH,'//label[@id="wpforms-15-field_0-error"]').get_attribute("innerText")
    assert error_name == "This field is required."
    time.sleep(3)
    error_message = driver.find_element(By.XPATH, '//label[@id="wpforms-15-field_2-error"]').get_attribute("innerText")
    assert error_message == "This field is required."
    time.sleep(3)
    error_email = driver.find_element(By.XPATH,'//label[@id="wpforms-15-field_4-error"]').get_attribute("innerText")
    assert error_email == "Please enter a valid email address."


def test_message_field_correctly():
    driver = init()
    #contact us button
    driver.find_element(By.XPATH,'//li[@id="menu-item-829"]').click()
    time.sleep(3)
    #name field
    driver.find_element(By.XPATH, '//input[@id="wpforms-15-field_0"]').send_keys()
    time.sleep(3)
    #subject field
    driver.find_element(By.XPATH,'//input[@id="wpforms-15-field_5"]').send_keys()
    time.sleep(3)
    # email field
    driver.find_element(By.XPATH,'//input[@id="wpforms-15-field_4"]').send_keys()
    time.sleep(3)
    #message field
    driver.find_element(By.XPATH,'//textarea[@id="wpforms-15-field_2"]').send_keys("Thank you")
    time.sleep(3)
    #send message button
    driver.find_element(By.XPATH,'//button[@id="wpforms-submit-15"]').click()
    time.sleep(3)
    error_name = driver.find_element(By.XPATH,'//label[@id="wpforms-15-field_0-error"]').get_attribute("innerText")
    assert error_name == "This field is required."
    time.sleep(3)
    error_email = driver.find_element(By.XPATH,'//label[@id="wpforms-15-field_4-error"]').get_attribute("innerText")
    assert error_email == "This field is required."
    time.sleep(3)

def test_message_field_incorrectly():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-829"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//input[@id="wpforms-15-field_0"]').send_keys()
    time.sleep(3)
    driver.find_element(By.XPATH,'//input[@id="wpforms-15-field_5"]').send_keys()
    time.sleep(3)
    driver.find_element(By.XPATH,'//input[@id="wpforms-15-field_4"]').send_keys()
    time.sleep(3)
    driver.find_element(By.XPATH,'//textarea[@id="wpforms-15-field_2"]').send_keys()
    time.sleep(3)
    driver.find_element(By.XPATH,'//button[@id="wpforms-submit-15"]').click()
    time.sleep(3)
    error_name = driver.find_element(By.XPATH,'//label[@id="wpforms-15-field_0-error"]').get_attribute("innerText")
    assert error_name == "This field is required."
    time.sleep(3)
    error_email = driver.find_element(By.XPATH,'//label[@id="wpforms-15-field_4-error"]').get_attribute("innerText")
    assert error_email == "This field is required."
    time.sleep(3)
    error_message = driver.find_element(By.XPATH, '//label[@id="wpforms-15-field_2-error"]').get_attribute("innerText")
    assert error_message == "This field is required."
    time.sleep(3)

def test_end_to_end_correctly():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-829"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//input[@id="wpforms-15-field_0"]').send_keys("Aviva")
    time.sleep(3)
    driver.find_element(By.XPATH,'//input[@id="wpforms-15-field_5"]').send_keys("Thank you")
    time.sleep(3)
    driver.find_element(By.XPATH,'//input[@id="wpforms-15-field_4"]').send_keys("avivaayasso0@gmail.com")
    time.sleep(3)
    driver.find_element(By.XPATH,'//textarea[@id="wpforms-15-field_2"]').send_keys("Hello, thank you")
    time.sleep(3)
    driver.find_element(By.XPATH,'//button[@id="wpforms-submit-15"]').click()
    time.sleep(3)
    message = driver.find_element(By.XPATH,'//p[contains(text(),"Thanks for contacting us! We will be in touch with")]').get_attribute("innerText")
    assert message == "Thanks for contacting us! We will be in touch with you shortly."


def test_end_to_end_incorrectly():
    driver = init()
    driver.find_element(By.XPATH,'//li[@id="menu-item-829"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//input[@id="wpforms-15-field_0"]').send_keys("#@##$$$")
    time.sleep(3)
    driver.find_element(By.XPATH,'//input[@id="wpforms-15-field_5"]').send_keys("####$")
    time.sleep(3)
    driver.find_element(By.XPATH,'//input[@id="wpforms-15-field_4"]').send_keys("avivaayasso0@gmail.")
    time.sleep(3)
    driver.find_element(By.XPATH,'//textarea[@id="wpforms-15-field_2"]').send_keys("##@#@@$")
    time.sleep(3)
    driver.find_element(By.XPATH,'//button[@id="wpforms-submit-15"]').click()
    time.sleep(3)
    error = driver.find_element(By.XPATH,'//label[@id="wpforms-15-field_4-error"]').get_attribute("innerText")
    assert error == "Please enter a valid email address."

