from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# Datos de usuario
USER = "standard_user"
PASS = "secret_sauce"

def setup_driver():
    """Configura y devuelve un controlador de Selenium listo para usar."""
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1250,850")
    return Chrome(service=service, options=options)

def login(driver, username, password):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

def add_to_cart(driver, items):
    for item in items:
        driver.find_element(By.NAME, f"add-to-cart-{item}").click()

def checkout(driver, first_name, last_name, postal_code):
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.NAME, "checkout").click()
    driver.find_element(By.NAME, "firstName").send_keys(first_name)
    driver.find_element(By.NAME, "lastName").send_keys(last_name)
    driver.find_element(By.NAME, "postalCode").send_keys(postal_code)
    driver.find_element(By.NAME, "continue").click()
    driver.find_element(By.NAME, "finish").click()

def main():
    # Configurar el driver
    driver = setup_driver()
    
    try:
        # Login
        login(driver, USER, PASS)
        
        # Agregar productos al carrito
        items = ["sauce-labs-bike-light", "sauce-labs-backpack"]
        add_to_cart(driver, items)
        
        # Realizar checkout
        checkout(driver, first_name="Tobias", last_name="Stani", postal_code="8988")
        
        # Esperar para verificar la compra
        time.sleep(3)
    finally:
        # Cerrar el driver
        driver.quit()

if __name__ == "__main__":
    main()
