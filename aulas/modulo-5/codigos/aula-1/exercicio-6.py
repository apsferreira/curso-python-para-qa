
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# abrir o browser
driver = webdriver.Chrome()

# acessa o site 
driver.get("https://www.saucedemo.com/")

# informa o usuario
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

# clica no botao de login
botao_login = driver.find_element(By.CLASS_NAME, "submit-button")
botao_login.click()

mensagem = driver.find_element(By.CLASS_NAME, "error-message-container")
print(mensagem.text)


botao_cancelar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "asdasdasd"))
)
botao_cancelar.click()

time.sleep(4)
driver.quit()