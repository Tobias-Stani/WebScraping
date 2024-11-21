from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.by import By

import time

USER = "standard_user"
PASS = "secret_sauce" 

def main():

    #configuracion para abrir la web.
    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()

    option.add_argument("--window-size=1250,850")
    driver = Chrome(service=service, options=option)

    #Paso 1 abrir la pagina.
    driver.get("https://www.saucedemo.com/") #link completo de la web.

    #Paso 2 registro.
    userInput = driver.find_element(By.ID, "user-name")
    userInput.send_keys(USER)

    driver.find_element(By.ID, "password").send_keys(PASS)

    #Paso 3 clck en el boton de login.
    driver.find_element(By.ID, "login-button").click()

    #Paso 4 agregar productos al carrito
    driver.find_element(By.NAME, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()

    #Paso 5 ir al carrito.
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    #Paso 6 checkout.
    driver.find_element(By.NAME, "checkout").click()

    #Paso 7 datos de la compra.
    driver.find_element(By.NAME, "firstName").send_keys("Tobias")

    driver.find_element(By.NAME, "lastName").send_keys("Stani")
    
    driver.find_element(By.NAME, "postalCode").send_keys("8988")

    driver.find_element(By.NAME, "continue").click()

    #Paso 8 finalizar la compra.
    driver.find_element(By.NAME, "finish").click()

    time.sleep(3)
    driver.quit()

if __name__=="__main__":
    main()