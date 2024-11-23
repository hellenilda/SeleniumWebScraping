from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()        # Navegador
driver.get('https://google.com')    # Recuperando a URL
search = driver.find_element("name", 'q') # Acessando a barra de pesquisa
search.send_keys("Python Testing with Selenium")    # Valor na barra de pesquisa
search.submit()     # Enviar o valor/texto de pesquisa

sleep(5)        # Tempo de espera
driver.quit()   # Fechando o navegador
print("Navegador finalizado")