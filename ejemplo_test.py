import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

def test_parabank():
    # Esta línea descarga y configura automáticamente el driver correcto
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    driver.get("https://para.testar.org/parabank/about.htm")
    assert "ParaBank | About Us" in driver.title
    driver.maximize_window()
    time.sleep(10)
    driver.quit()