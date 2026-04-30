import pytest
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
import time


class TestDashboard:
    
    def test_validacion(self, logged_in_dashboard):
        """Hace el login y Valida que los elementos del dashboard estén presentes"""

        # logged_in YA ES el objeto Dashboard Page por ende va sin paréntesis
       

        assert logged_in_dashboard.verifico_cta_corriente(), \
            "La cuenta corriente no está visible en el dashboard"
        
        assert logged_in_dashboard.verifico_caja_ahorro(), \
            "La caja de ahorro no está visible en el dashboard"
        
        assert logged_in_dashboard.verifico_tarjeta_credito(), \
            "La tarjeta de crédito no está visible en el dashboard"