# Importaciones
import pytest
from selenium import webdriver
from utils.LoginPage import login
from selenium.webdriver.common.by import By


# Configuracion del navegador
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options = options)

    yield driver # yield inserta el codigo de las instrucciones
                 # En este caso entrega el objeto driver al test para que pueda usarlo
                 
    driver.quit()

# Configuracion del login
@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver
