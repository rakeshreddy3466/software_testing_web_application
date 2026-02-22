"""
Feature Requirement 06 (FR06): Data Integrity - Cart Persistence
Acceptance Criteria: The cart table must not be empty and must display at least one product row.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://automationexercise.com/"

def test_cart_items_exist(driver):
    driver.get(URL + "product_details/1")
    wait = WebDriverWait(driver, 10)
    
    # Step 1: Wait for Add to Cart button and click it via JS
    add_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.cart")))
    driver.execute_script("arguments[0].click();", add_btn)
    
    # Step 2: Explicitly wait for the success modal before navigating away (replaces sleep)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[contains(text(),'Added!')]")))
    
    # Step 3: Navigate to cart
    driver.get(URL + "view_cart")
    
    # Step 4: Wait for the cart table to load and count the rows
    wait.until(EC.presence_of_element_located((By.ID, "cart_info_table")))
    rows = driver.find_elements(By.CSS_SELECTOR, "#cart_info_table tbody tr")
    
    assert len(rows) > 0, "The cart is empty; expected at least one product row."