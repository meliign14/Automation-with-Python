import pytest
from pages.dashboard_page import DashboardPage
#from pages.login_page import LoginPage
from tests.conftest import get_data_from_json
import time


class TestLogin:

    def test_login(self, login_data, login_pg):
       """ login_pg = LoginPage(driver)
        datos = get_data_from_json("data_login.json")"""
       user_data = login_data[0]
        
       login_pg.navegar(user_data["url"])
       dashboard_pg = login_pg.ingresar_login(user_data["user"], user_data["password"])
        

       assert dashboard_pg.login_exitoso(),\
            f"Validación fallida para escenario: {user_data['escenario']}"
        
    def test_logout(self, driver, login_data, login_pg):
        user = login_data[0]
        
        login_pg.navegar(user["url"])
        login_pg.ingresar_login(user["user"], user["password"])

        dashboard_pg = DashboardPage(driver)
        dashboard_pg.cerrar_sesion()

        assert login_pg.logout_exitoso(), \
            "El logout no fue exitoso"


    def test_login_bloqueado(self, login_data, login_pg):
        block_user = login_data[2]
        
        login_pg.navegar(block_user["url"])
        
        for _ in range(3):
            login_pg.ingresar_login(block_user["user"], block_user["password"])

        assert login_pg.obtener_mensaje_error() == block_user["resultado esperado"], \
            "Mensaje de error bloqueado no coincide"

    def test_panel(self, login_data, login_pg):
        user = login_data[0]
        
        login_pg.navegar(user["url"])


        assert login_pg.panel_flotante(), \
            "El panel flotante de documentación no está presente en la página de login"
        
    def test_hover(self, login_data, login_pg):
        user = login_data[0]
        login_pg.navegar(user["url"])
        

        assert login_pg.boton_con_hover(), \
            "El botón no tiene efecto hover"
        

    def test_pestanias(self, login_data, login_pg):
        user = login_data[0]
        login_pg.navegar(user["url"])

        
        assert login_pg.verificar_pestanias(), \
            "Los links no abren en otra pestaña"

        login_pg.volver_a_pestania_inicial()