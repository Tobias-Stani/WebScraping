from selenium import webdriver
import pickle

# Inicializar el WebDriver
driver = webdriver.Chrome()

# Ir al sitio web
driver.get("#")

# Cargar las cookies guardadas
cookies = pickle.load(open("cookies.pkl", "rb"))

# Añadir las cookies al navegador de Selenium
for cookie in cookies:
    driver.add_cookie(cookie)

# Refrescar la página para que el navegador use las cookies
driver.refresh()

# Ahora deberías estar logueado sin necesidad de pasar por el formulario de login.
