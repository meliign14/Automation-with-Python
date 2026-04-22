from selenium.webdriver.common.by import By

class LoginPageLocators:

    """
    En esta clase se centralizan todos los localizadores de la pagina de Login
    """

    USERNAME_INPUT = (By.ID, "username")
    PASS_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-btn")
    REMINDME_BOX = (By.ID, "remember-me")

    ERROR_MESSAGE = (By.ID,"login-error")

    SUCCESS_LOGIN = (By.CLASS_NAME,"toast-message")
    BTN_YES = (By.CLASS_NAME,"btn btn-primary")
    SESSION_CLOSE = (By.CLASS_NAME,"toast info")

    PANEL_FLOTANTE = (By.CLASS_NAME, "docs-floating-panel")

    BTN1_HOVER = (By.CSS_SELECTOR, "div > a:nth-of-type(1)")
    BTN2_HOVER = (By.CSS_SELECTOR, "div > a:nth-of-type(2)")