from selenium.webdriver.common.by import By

class LoginPageLocators:

    """
    En esta clase se centralizan todos los localizadores de la pagina de Login
    """

    USERNAME_INPUT = (By.ID, "username")
    PASS_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-btn")
    REMINDME_BOX = (By.ID, "remember-me")
