from pages.base_page import BasePage
from locators.locators_login import LoginPageLocators
from selenium.webdriver.common.action_chains import ActionChains


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
    
    def panel_flotante(self):
        """Valida que el panel flotante de documentación esté presente en la página de login"""
        return self.elemento_visible(LoginPageLocators.PANEL_FLOTANTE)

    def boton_con_hover(self):
        """Valida que los elementos del papel tengan el efecto hover"""
        if not self.elemento_visible(LoginPageLocators.BTN1_HOVER):
            return False
        boton = self.driver.find_element(*LoginPageLocators.BTN1_HOVER)
        # Obtener propiedades iniciales
        color_inicial = boton.value_of_css_property("background-color")

        # Aplicar hover
        actions = ActionChains(self.driver)
        actions.move_to_element(boton).perform()

        # Un pequeño delay para asegurar que el efecto hover se aplique

        import time
        time.sleep(0.5)
        
        # Obtener propiedades despues del hover
        color_hover = boton.value_of_css_property("background-color")
        return color_inicial != color_hover
        
    def verificar_pestanias(self):
        return self.click_y_cambiar_a_nueva_pestania(LoginPageLocators.BTN1_HOVER)





        

        
        
