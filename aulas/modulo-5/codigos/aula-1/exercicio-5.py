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

# informa a senha
password = driver.find_element(By.NAME, "password")
password.send_keys("secret_sauce")

# clica no botao de login
botao_login = driver.find_element(By.CLASS_NAME, "submit-button")
botao_login.click()

driver.implicitly_wait(5)

# primeiro item a ser inserido no carrinho
link_item = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
link_item.click()

# clica no botao add to cart
# botao_add_to_cart = driver.find_element(By.NAME, "add-to-cart")
# botao_add_to_cart.click()

# clicando no carrinho para verificar se o item foi adicionado
botao_carrinho = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
botao_carrinho.click()

botao_remove = driver.find_element(By.NAME, "remove-sauce-labs-backpack")
botao_remove.click()

botao_continue = driver.find_element(By.ID, "continue-shopping")
botao_continue.click()

time.sleep(10)

driver.quit()