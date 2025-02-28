from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/hovers")

time.sleep(2)

imagem_hover = driver.find_element(By.XPATH, "//div[@class='figure'][1]")

acao = ActionChains(driver)
acao.move_to_element(imagem_hover).perform()

tootip_text = driver.find_element(By.XPATH, "//div[@class='figure'][1]//h5").text

assert "name: user1" in tootip_text.lower(), "erro no tooltip"

print("Mouse hover realizado com sucesso")

time.sleep(2)

driver.quit()