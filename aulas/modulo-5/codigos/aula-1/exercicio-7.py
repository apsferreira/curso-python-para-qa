from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# espera explicita
wait = WebDriverWait(driver, 10)

driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

botao_start = driver.find_element(By.CSS_SELECTOR, "#start button")
botao_start.click()

# espera implicita
texto_carregado = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#finish h4"))
)

print(f"o texto carregado foi: {texto_carregado.text}")

driver.quit()
