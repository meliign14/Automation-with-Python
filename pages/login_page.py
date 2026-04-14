from pages.base_page import BasePage
from locators.locators_login import LoginPageLocators


class LoginPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    # Abrir la pagina

    def navegar(self, url):
        return super().navegar(url)


    def ingresar_login(self, user, password):
        """Completa el formulario de login y hace click en el boton de ingresar"""
        self.typear(LoginPageLocators.USERNAME_INPUT,user)
        self.typear(LoginPageLocators.PASS_INPUT,password)
        self.clickear(LoginPageLocators.LOGIN_BTN)


        from pages.dashboard_page import DashboardPage
        return DashboardPage(self.driver)

    

    def mostrar_error_login(self):
        """Valida que se muestra error de login"""
        return self.elemento_visible(LoginPageLocators.ERROR_MESSAGE)

    def obtener_mensaje_error(self):
        """Obtiene el mensaje de error"""
        return self.obtener_texto(LoginPageLocators.ERROR_MESSAGE)
    
    def logout_exitoso(self):
        """Valida que el logout fue exitoso"""
        return self.elemento_visible(LoginPageLocators.LOGIN_BTN)