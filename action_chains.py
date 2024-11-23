from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

# Inicializando o navegador
driver = webdriver.Firefox()        # Navegador
driver.get('https://google.com')    # Recuperando a URL

message_field = driver.find_element(By.NAME, 'q')   # Campo de texto
button = driver.find_element(By.NAME, 'btnK')       # Botão de pesquisa

# Usando ActionChains para clicar e enviar texto
action = ActionChains(driver)
action.click(on_element=message_field)
action.send_keys("Hello World")
action.click(on_element=button)
action.perform()

# Fechando o navegador
sleep(3)  # Espera 3 segundos
driver.quit()  # Fechando o navegador
print("Navegador finalizado")