from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

botao_add = driver.find_element(By.XPATH, "//button[text()='Add Element']")
botao_add.click()

botao_delete = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "added-manually"))
)
botao_delete.click()

print("Botao 'Add Element' clicado com sucesso")

driver.quit()