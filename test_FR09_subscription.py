"""
Feature Requirement 09 (FR09): Engagement - Footer Subscription
Acceptance Criteria: The footer widget must contain the visible text 'SUBSCRIPTION'.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://automationexercise.com/"

def test_footer_subscription(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 10)
    
    # Step 1: Scroll down to trigger lazy loading if any
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Step 2: Wait for the footer header to become visibly rendered
    # We use .text instead of .textContent to ensure it's actually visible to a human
    footer_header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer-widget h2")))
    
    assert "SUBSCRIPTION" in footer_header.text.upper(), f"Expected visible 'SUBSCRIPTION' text, got '{footer_header.text}'"