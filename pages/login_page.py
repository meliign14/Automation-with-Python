from pages.base_page import BasePage
from locators.locators_login import LoginPageLocators
from pages.dashboard_page import DashboardPage


class LoginPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    # Abrir la pagina

    def navegar(self, url):
        return super().navegar(url)

    # Llamar al metodo para escribir email y contraseña

    def ingresar_login(self, user, password):
        self.typear(LoginPageLocators.USERNAME_INPUT,user)
        self.typear(LoginPageLocators.PASS_INPUT,password)
        self.clickear(LoginPageLocators.LOGIN_BTN)

        return DashboardPage(self.driver)

    def login_exitoso(self):
        """Valida que el login fue exitoso"""
        return self.elemento_visible(LoginPageLocators.LOGOUT_BTN)

    def mostrar_error_login(self):
        """Valida que se muestra error de login"""
        return self.elemento_visible(LoginPageLocators.ERROR_MESSAGE)

    def obtener_mensaje_error(self):
        """Obtiene el mensaje de error"""
        return self.obtener_texto(LoginPageLocators.ERROR_MESSAGE)