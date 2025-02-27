from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# abre o chrome
driver = webdriver.Chrome()

# acessa o google.com
driver.get("https://google.com")

# encontro o elemento de pesquisa da pagina
campo_pesquisa = driver.find_element(By.NAME, "q")

# informando o texto Selenium Webdriver
campo_pesquisa.send_keys("Selenium Webdriver")

campo_pesquisa.send_keys(Keys.RETURN)

time.sleep(3)
driver.quit()