from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

botao_login = driver.find_element(By.NAME, "login-button")

botao_login.click()



