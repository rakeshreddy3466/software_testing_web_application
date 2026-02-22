"""
Feature Requirement 01 (FR01): Core Interface - Homepage Initialization
Acceptance Criteria: The homepage must render completely, verified by the visibility of the main 'Features Items' section.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://automationexercise.com/"

def test_homepage_load(driver):
    # Step 1: Navigate to SUT
    driver.get(URL)
    
    # Step 2: Use Explicit Wait to ensure the main content container has loaded
    wait = WebDriverWait(driver, 10)
    featured_items = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.features_items")))
    
    # Step 3: Assert the core shopping UI is displayed to the user as per Acceptance Criteria
    assert featured_items.is_displayed(), "The 'Features Items' section did not load on the homepage."