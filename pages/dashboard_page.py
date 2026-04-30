from pages.base_page import BasePage
from locators.locators_dashboard import DashboardLocators


class DashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def login_exitoso(self):
        """Valida que el login fue exitoso"""
        return self.elemento_visible(DashboardLocators.LOGOUT_BTN)

    def cerrar_sesion(self):
        """Hace click en el boton de logout"""
        self.esperar_a_que_desaparezca(DashboardLocators.TOAST_BTN) # Espera a que desaparezca el mensaje de éxito antes de hacer logout
        self.elemento_visible(DashboardLocators.LOGOUT_BTN)
        self.clickear(DashboardLocators.LOGOUT_BTN)
        self.clickear(DashboardLocators.MODAL_BTN)

        from pages.login_page import LoginPage

        return LoginPage(self.driver)
    
    def verifico_cta_corriente(self):
        return self.elemento_visible(DashboardLocators.CTA_CORRIENTE)

    def verifico_caja_ahorro(self):
        return self.elemento_visible(DashboardLocators.CAJA_AHORRO)

    def verifico_tarjeta_credito(self):
        return self.elemento_visible(DashboardLocators.TARJETA_CREDITO)