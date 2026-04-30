from socket import timeout

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.id_ventana_original = None

    def navegar(self,url):
        self.driver.get(url)


    def _esperar_por_elemento(self, by_locator,timeout = 10):# Pasamos locator y que el timeout sea igual a 10s
        try:
            WebDriverWait(self.driver, timeout).until(      
                EC.element_to_be_clickable(by_locator) # Espera a que el elemento sea clickeable
            ) 
            return self.driver.find_element(*by_locator) # Devuelve el elemento
        except TimeoutException:
            print("The element was not found") # Si no lo encuentra, muestra este msj
            return None                        # Y devuelve None

    def clickear(self, by_locator):
        user = self._esperar_por_elemento(by_locator) # Llama a la funcion _wait... y almacena el resultado en la variable user
        if user:                         
            user.click()                 # le hace click
        else:
            raise Exception("No puedo hacerle click")

    def typear(self, by_locator, otro_dato):
        user = self._esperar_por_elemento(by_locator)
        if user:
            user.clear() # Limpia el campo antes de escribir
            user.send_keys(otro_dato)
        else:
            raise Exception("Can't find the element")
        
    def limpiar_sesion(self):
        #Limpia cookies y localStorage para asegurar un test limpio
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def obtener_texto(self, by_locator):
        #Retorna el texto de un elemento, muy útil para mensajes de error
        return self._esperar_por_elemento(by_locator).text
    
    def elemento_visible(self, by_locator):
        #Verifica si un elemento está en pantalla (para aserciones)
        try:
            return self._esperar_por_elemento(by_locator).is_displayed()
        except:
            return False
        
    def esperar_a_que_desaparezca(self, by_locator, timeout=10):

        try:
            #Verifica que un elemento no esté en pantalla (para aserciones)
            return WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(by_locator)
            )
        
        except TimeoutException:
            print("El elemento es visible despues del timeout")


    def verificar_link_nueva_pestania(self, by_locator):
        # Verifica que un link abra en una nueva pestaña
        link = self._esperar_por_elemento(by_locator)
        if link:
            href = link.get_attribute("href")
            target = link.get_attribute("target")
            return target == "_blank" and href is not None
        else:
            raise Exception("No puedo encontrar el link para verificar")
        

    def click_y_cambiar_a_nueva_pestania(self, localizador):
        """
        Hace clic en un elemento, verifica que se abra una pestaña,
        cambia el foco a la nueva y devuelve True si tuvo éxito.
        """
        self.id_ventana_original = self.driver.current_window_handle
        conteo_antes = len(self.driver.window_handles)

        # Hacemos clic en el localizador que recibimos
        self.driver.find_element(*localizador).click()

        try:
            # Esperamos a que el conteo suba
            WebDriverWait(self.driver, 5).until(
                EC.number_of_windows_to_be(conteo_antes + 1)
            )
            
            # Cambiamos a la ventana que no sea la original
            for ventana in self.driver.window_handles:
                if ventana != self.id_ventana_original:
                    self.driver.switch_to.window(ventana)
                    #assert "Plan_de_Pruebas_HomeBanking_V3" in self.driver.title
                    break
            return True
        except:
            return False

    def volver_a_pestania_inicial(self):
        """Cierra la actual y regresa a la original."""
        self.driver.close()
        self.driver.switch_to.window(self.id_ventana_original)