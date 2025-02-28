import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def driver():
    """Inicializar o webdriver"""
    
    driver = webdriver.Chrome()
    
    yield driver
    
    driver.quit()

def test_pesquisa_google(driver):
    
    driver.get("https://the-internet.herokuapp.com/login")

    campo_username = driver.find_element(By.NAME, "username")
    campo_username.send_keys("tomsmith")
    
    campo_password = driver.find_element(By.NAME, "password")
    campo_password.send_keys("SuperSecretPassword!")

    campo_password.send_keys(Keys.RETURN)

    time.sleep(10)

    print("Teste efetuado com sucesso")