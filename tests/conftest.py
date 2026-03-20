import pytest
import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.base_page import BasePage



def get_data_from_json(filename):
    # Esto obtiene la ruta de la raiz del proyecto
    base_path = os.path.dirname(os.path.dirname(__file__))

    # Construye la ruta final: raiz > data > data_login.json
    data_path = os.path.join(base_path, 'data', filename)
    
    with open(data_path, "r") as file:
        return json.load(file)

# En esta funcion se inicializa y se cierra el driver
# Además configura el chrome
@pytest.fixture(scope="session")
def driver():
    # Setup: se ejecuta una sola vez al inicio
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver #Aquí corren todos los test

    #Teardown: se ejecuta al final de toda la suite
    driver.quit()


@pytest.fixture(autouse=True) #Limpia la sesion antes de cada test automáticamente
def preparar_test(driver):
    base_pg = BasePage(driver)
    base_pg.limpiar_sesion()


    