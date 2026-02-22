"""
Feature Requirement 02 (FR02): Browsing - Product Catalog
Acceptance Criteria: Clicking the navigation link must display the 'All Products' header.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://automationexercise.com/"

def test_view_products(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 10)
    
    # Step 1: Locate the Products button
    products_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/products']")))
    
    # Step 2: Bypassing dynamic Google Ads overlays using JavaScript Execution
    # Standard Selenium click() often fails here due to ElementClickInterceptedException.
    driver.execute_script("arguments[0].click();", products_btn)
    
    # Step 3: Wait for the header to load on the new page and verify text
    header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".title.text-center")))
    
    assert "ALL PRODUCTS" in header.text, f"Expected 'ALL PRODUCTS', but got '{header.text}'"