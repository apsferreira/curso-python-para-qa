from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# acessa a pagina do formulario
driver.get("https://the-internet.herokuapp.com/inputs")

# aguarda ate que o campo numero esteja visivel
campo_numero = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "input"))
)

valor_teste = "100"
campo_numero.send_keys(valor_teste)

time.sleep(2)
valor_exibido = campo_numero.get_attribute("value")

assert valor_exibido == valor_teste, f"erro: Esperado {valor_teste}, mas foi {valor_exibido}"

print("Teste concluido com sucesso")