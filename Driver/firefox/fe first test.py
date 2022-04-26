from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
driver.get("http://www.facebook.com")

# driver.find_element(By.XPATH, '//a[contains(text(),"שכחת את הסיסמה?")]').click()
driver.find_element(By.XPATH,'//a[@id=''u_0_2_3O'']').click()