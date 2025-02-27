from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")

campo_pesquisa = driver.find_element(By.NAME, "q")
print("campo de pesquisa encontrado")
driver.quit()