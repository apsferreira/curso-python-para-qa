from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

time.sleep(2)

botao_alerta_simples = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
botao_alerta_simples.click()

alerta = Alert(driver)
print(f"Texto do Alerta: {alerta.text}")
alerta.accept()

time.sleep(2)

mensagem_confirmacao = driver.find_element(By.ID, "result").text
assert mensagem_confirmacao == "You successfully clicked an alert", f"Erro mensagem incorreta: {mensagem_confirmacao}"

print("Alerta Aceito com sucesso")

time.sleep(2)

botao_alerta_confirmacao = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
botao_alerta_confirmacao.click()

alerta = Alert(driver)
print(f"Texto do Alerta de confirmacao: {alerta.text}")
alerta.dismiss() # clicar no botao cancelar

mensagem_confirmacao = driver.find_element(By.ID, "result").text
assert mensagem_confirmacao == "You clicked: Cancel", "Mensagem incorreta"

print("Alerta de Confimaçao Cancelado")

time.sleep(2)

botao_alerta_prompt = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
botao_alerta_prompt.click()

alerta = Alert(driver)
print(f"Texto do Alerta de Prompt: {alerta.text}")
texto_teste = "Teste Selenium!"
alerta.send_keys(texto_teste)
alerta.accept() # Confirma

# Valida repsosta na pagina
mensagem_confirmacao = driver.find_element(By.ID, "result").text
assert mensagem_confirmacao == f"You entered: {texto_teste}", f"Erro: Mensagem Incorreta: {mensagem_confirmacao}"


print("Alerta de Prompt preenchido com sucesso")

time.sleep(2)

driver.quit()