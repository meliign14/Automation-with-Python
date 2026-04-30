import pytest
import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from pages.base_page import BasePage



def get_data_from_json(filename):
    # Esto obtiene la ruta de la raiz del proyecto
    base_path = os.path.dirname(os.path.dirname(__file__))

    # Construye la ruta final: raiz > data > data_login.json
    data_path = os.path.join(base_path, 'data', filename)
    
    with open(data_path, "r") as file:
        return json.load(file)
    

@pytest.fixture
def login_data():
    """Fixture que carga los datos del JSON una sola vez"""
    return get_data_from_json("data_login.json")

@pytest.fixture
def login_pg(driver):
    """Fixture que instancia el LoginPage y te lo entrega listo"""
    from pages.login_page import LoginPage
    return LoginPage(driver)

@pytest.fixture
def logged_in_dashboard(driver, login_pg, login_data):
    """Realiza el login exitoso"""

    data = next(d for d in login_data if d["escenario"] == "exitoso")

    driver.get(data["url"])

    return login_pg.ingresar_login(data["user"], data["password"])


@pytest.fixture(scope="session")
def driver():
    """ Fixture que inicializa el driver de Chrome una sola vez por sesion de prueba"""
    # Configurar las opciones de Chrome
    chrome_options = Options()
    # Detectar si estamos en GitHub Actions (CI)
    # GitHub siempre define esta variable de entorno como 'true'
    if os.getenv('GITHUB_ACTIONS')== 'true':
        chrome_options.add_argument("--headless") # No abre ventana
        chrome_options.add_argument("--no-sandbox") # Necesario para entornos Linux/Docker
        chrome_options.add_argument("--disable-dev-shm-usage") # Evita problemas de memoria
        chrome_options.add_argument("--window-size=1920,1080") # Simula un monitor

    # Setup: se ejecuta una sola vez al inicio
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    driver.implicitly_wait(10)
    if os.getenv('GITHUB_ACTIONS')!= 'true':
        driver.maximize_window()
    yield driver #Aquí corren todos los test

    # Teardown: se ejecuta al final de toda la suite
    driver.quit()


@pytest.fixture(autouse=True) #Limpia la sesion antes de cada test automáticamente
def preparar_test(driver):
    base_pg = BasePage(driver)
    base_pg.limpiar_sesion()