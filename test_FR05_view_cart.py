"""
Feature Requirement 05 (FR05): Navigation - Accessing the Cart
Acceptance Criteria: The system must navigate to the cart URL successfully upon clicking the link.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://automationexercise.com/"

def test_view_cart_page(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 10)
    
    # Step 1: Wait for the cart button to be present in the DOM
    cart_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/view_cart']")))
    
    # Step 2: Force click using Javascript to bypass site-wide ad overlays
    driver.execute_script("arguments[0].click();", cart_btn)
    
    # Step 3: Wait explicitly for the URL to change to the cart endpoint
    wait.until(EC.url_contains("view_cart"))
    
    # Step 4: Verify the current URL
    assert "view_cart" in driver.current_url, f"Failed to navigate to cart. Current URL is: {driver.current_url}"