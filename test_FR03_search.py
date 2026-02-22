"""
Feature Requirement 03 (FR03): Utility - Search Functionality
Acceptance Criteria: Searching for a term like "Tshirt" must return results under a 'Searched Products' title.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://automationexercise.com/"

def test_search_product(driver):
    driver.get(URL + "products")
    wait = WebDriverWait(driver, 10)
    
    # Step 1: Wait for search input to be present in the DOM
    search_box = wait.until(EC.presence_of_element_located((By.ID, "search_product")))
    
    # Step 2: Use JS injection to bypass aggressive ad overlays blocking send_keys
    driver.execute_script("arguments[0].value='Tshirt';", search_box)
    
    # Step 3: Click the search submit button via JS
    submit_btn = driver.find_element(By.ID, "submit_search")
    driver.execute_script("arguments[0].click();", submit_btn)
    
    # Step 4: Wait for the results header to appear and verify
    header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".title.text-center")))
    
    assert "SEARCHED PRODUCTS" in header.text, "The 'SEARCHED PRODUCTS' header did not appear after searching."