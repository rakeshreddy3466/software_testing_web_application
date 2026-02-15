import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    print("\n[Setup] Starting Browser...")
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--ignore-certificate-errors")
    # This helps avoid some rendering issues
    options.add_argument("--disable-popup-blocking")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    yield driver
    print("\n[Teardown] Closing Browser...")
    driver.quit()