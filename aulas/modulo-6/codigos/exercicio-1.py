from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/dropdown")

time.sleep(2)

# localizar o dropdown
dropdown = Select(driver.find_element(By.ID, "dropdown"))

dropdown.select_by_visible_text("Option 2")

time.sleep(1)

opcao_selecionada = dropdown.first_selected_option.text

assert opcao_selecionada == "Option 2", f"Erro na selecao do dropdown!"

print("Selecao do dropdown realizada com Sucesso")

driver.quit()