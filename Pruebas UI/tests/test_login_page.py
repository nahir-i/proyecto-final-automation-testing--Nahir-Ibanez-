import pytest
from pages.login_page import LoginPage
from data.data_login import CASOS_LOGIN
from utils.example_csv import get_login_csv
from utils.faker import get_login_faker

@pytest.mark.parametrize("username,password,login_bool",CASOS_LOGIN)
def test_login( driver, username , password , login_bool ):
    # Se crea el objeto (instanciarlo)
    loginPage = LoginPage(driver) 
    # Se abre la web y se ingresan credenciales
    loginPage.open()
    loginPage.login(username , password)

    if login_bool:
        # Caso de exito
        assert "inventory.html" in driver.current_url
    else:
        # Caso de fallo
        assert "inventory.html" not in driver.current_url

        