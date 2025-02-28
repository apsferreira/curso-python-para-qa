from selenium import webdriver

# inicializar o WebDriver do Chrome
driver = webdriver.Chrome()

# acessar um site de teste
driver.get("https://the-internet.herokuapp.com/")

print(f"titulo da pagina: {driver.title}")

driver.quit()