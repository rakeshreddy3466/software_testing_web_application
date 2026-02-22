"""
Feature Requirement 10 (FR10): Detail Discovery - Product Specifications
Acceptance Criteria: The detail page must load with 'Brand' and 'Availability' information visible.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://automationexercise.com/"

def test_product_details_page(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 10)
    
    # Step 1: Navigate to details page
    view_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/product_details/1']")))
    driver.execute_script("arguments[0].click();", view_btn)
    
    # Step 2: Ensure URL changed
    wait.until(EC.url_contains("product_details"))
    
    # Step 3: Strict Assertion - explicitly check for Brand and Availability visibility
    # The site uses <b> tags for these labels
    availability_label = wait.until(EC.visibility_of_element_located((By.XPATH, "//b[contains(text(), 'Availability:')]")))
    brand_label = wait.until(EC.visibility_of_element_located((By.XPATH, "//b[contains(text(), 'Brand:')]")))
    
    assert availability_label.is_displayed(), "'Availability' information is not visible on the details page."
    assert brand_label.is_displayed(), "'Brand' information is not visible on the details page."