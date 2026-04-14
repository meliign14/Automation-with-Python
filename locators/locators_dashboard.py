from selenium.webdriver.common.by import By


class DashboardLocators:

    LOGOUT_BTN = (By.ID,"logout-btn")
    MODAL_BTN = (By.ID, "modal-confirm")
    TOAST_BTN = (By.ID,"toast-success")
    TOAST_MESSAGE = (By.CLASS_NAME,"toast-message")

    DASHBOARD_SECTION = (By.ID,"dashboard-section")