from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/checkboxes")

time.sleep(2)

checkboxes = driver.find_elements(By.TAG_NAME, "input")

for checkbox in checkboxes:
    # o checkbox está marcado?
    if not checkbox.is_selected():
        checkbox.click()

    assert checkbox.is_selected(), "Erro: O checkbox nao foi marcado corretamente"

checkboxes[1].click()

print("Checkbox selecionado com sucesso")

time.sleep(5)

driver.quit()