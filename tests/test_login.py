import pytest
from pages.login_page import LoginPage
from tests.conftest import get_data_from_json
import time
from locators.locators_login import LoginPageLocators


class TestLogin:

    """
                FUNCIONA
    @pytest.mark.parametrize("user_data", get_data_from_json("data_login.json"))
    def test_navegacion(self, driver, user_data):
        # Instanciamos la pagina

        login_pg = LoginPage(driver) #instanciamos LoginPage que es donde están todos las acciones de la page

        # Aca navegamos usando la url del json

        url_destino = user_data["url"] # Creo la variable url_destino y le paso 
        login_pg.navegar(url_destino) # el objeto url del archivo user_data, que contiene el json
        assert "Home Banking" in driver.title, f"Error: la pagina en {url_destino} no cargó correctamente"""

    @pytest.mark.parametrize("user_data",get_data_from_json("data_login.json"))
    def test_login(self,driver,user_data):
        login_pg = LoginPage(driver)

        # CP-AUTH- 01 & 02

        print(f"\nEjecutando: {user_data['escenario']}")
        login_pg.navegar(user_data["url"])
        login_pg.ingresar_login(user_data["user"],user_data["password"])
        if user_data["escenario"] == "exitoso":
            assert login_pg.elemento_visible(LoginPageLocators.LOGOUT_BTN), \
                "No se muestra el boton salir luego del login"
            
        else:
            assert login_pg.elemento_visible(LoginPageLocators.ERROR_MESSAGE), \
                "No se muestra el mensaje de login erroneo"

        



    




