import pytest
import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



def get_data_from_json(filename):
    # Esto obtiene la ruta de la raiz del proyecto
    base_path = os.path.dirname(os.path.dirname(__file__))

    # Construye la ruta final: raiz > data > data_login.json
    data_path = os.path.join(base_path, 'data', filename)
    
    with open(data_path, "r") as file:
        return json.load(file)


@pytest.fixture

# En esta clase se inicializa y se cierra el driver
# Además configura el chrome

def driver():
    # Setup
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    # Teardown
    driver.quit()