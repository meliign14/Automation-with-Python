from pages.base_page import BasePage
from locators.locators_login import LoginPageLocators


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