# Importaciones
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Funcion de validacion del login
def test_login_validation(login_in_driver):
    try:
        driver = login_in_driver

        # Validacion de login exitoso verificando que haya redirigido a la pagina del inventario
        assert "/inventory.html" in driver.current_url, "No se redirigio al inventario"

    except Exception as e:
        print(f"Error en test_login: {e}")
        raise
