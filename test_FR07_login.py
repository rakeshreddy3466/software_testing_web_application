"""
Feature Requirement 07 (FR07): Security - User Login
Acceptance Criteria: Using valid credentials must result in a successful login, confirmed by the 'Logout' link appearing.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://automationexercise.com/"

def test_real_login(driver):
    driver.get(URL + "login")
    wait = WebDriverWait(driver, 10)
    
    # Step 1: Wait for elements, then use JS injection to set values, bypassing ad overlays
    email_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='login-email']")))
    driver.execute_script("arguments[0].value='testuser1@test.com';", email_box)
    
    pass_box = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']")
    driver.execute_script("arguments[0].value='password123';", pass_box)
    
    # Step 2: Click Login button via JS
    login_btn = driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']")
    driver.execute_script("arguments[0].click();", login_btn)
    
    # Step 3: Strict Assertion - Wait explicitly for the Logout button
    logout_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/logout']")))
    
    assert logout_btn.is_displayed(), "Login failed: Logout button is not visible."