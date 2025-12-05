import pytest
from utils.helpers import  get_driver

@pytest.fixture
def driver():
    # Configuracion para consultar a selenium web driver
    driver = get_driver()
    yield driver
    driver.quit()