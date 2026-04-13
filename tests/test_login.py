import pytest
from pages.login_page import LoginPage
from tests.conftest import get_data_from_json
import time


class TestLogin:

    @pytest.mark.parametrize("user_data", get_data_from_json("data_login.json"))
    def test_login(self, driver, user_data):
        login_pg = LoginPage(driver)

        print(f"\nEjecutando: {user_data['escenario']}")
        login_pg.navegar(user_data["url"])
        login_pg.ingresar_login(user_data["user"], user_data["password"])
        

        assert login_pg.login_exitoso() if user_data["escenario"] == "exitoso" \
            else login_pg.mostrar_error_login(), \
            f"Validación fallida para escenario: {user_data['escenario']}"

    def test_login_bloqueado(self, driver):
        login_pg = LoginPage(driver)
        datos = get_data_from_json("data_login.json")
        block_user = datos[2]
        
        login_pg.navegar(block_user["url"])
        
        for _ in range(3):
            login_pg.ingresar_login(block_user["user"], block_user["password"])

        assert login_pg.obtener_mensaje_error() == block_user["resultado esperado"], \
            "Mensaje de error bloqueado no coincide"