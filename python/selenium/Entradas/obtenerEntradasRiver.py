from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup_driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    
    # Añadir la opción para iniciar el navegador en modo minimizado
    options.add_argument("--window-size=1250,850")
    options.add_argument("headless")  # Ejecuta el navegador en modo headless (sin UI)
    
    return Chrome(service=service, options=options)

def login(driver):
    driver.get("https://serviclub.com.ar/4633-espectaculos-")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h5')))

def findMatch(driver):
    products = driver.find_elements(By.CLASS_NAME, "product-title-item")
    
    matching_count = 0 
    
    for product in products:
        product_name = product.text
        if "RIVER" in product_name.upper(): 
            matching_count += 1
            print(f"Coincidencia encontrada: {product_name}")
    
    if matching_count > 0:
        print(f"\nSe encontraron {matching_count} productos con la palabra 'RIVER'.")
    else:
        print("\nNo se encontraron productos con la palabra 'RIVER'.")

def main():
    driver = setup_driver()  
    login(driver)  
    findMatch(driver)  

    time.sleep(5)  
    driver.quit()  

if __name__ == "__main__":
    main()
