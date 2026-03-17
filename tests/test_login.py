import pytest
from pages.login_page import LoginPage
from tests.conftest import get_data_from_json
import time


class TestLogin:

    @pytest.mark.parametrize("user_data", get_data_from_json("data_login.json"))
    def test_navegacion_homebanking(self, driver, user_data):
        # Instanciamos la pagina

        login_pg = LoginPage(driver) #instanciamos LoginPage que es donde están todos las acciones de la page

        # Aca navegamos usando la url del json

        url_destino = user_data["url"] # Creo la variable url_destino y le paso 
        login_pg.navegar(url_destino) # el objeto url del archivo user_data, que contiene el json
        assert "Home Banking" in driver.title, f"Error: la pagina en {url_destino} no cargó correctamente"
        # time.sleep(10)
        





