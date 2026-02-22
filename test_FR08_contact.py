"""
Feature Requirement 08 (FR08): Support - Contact Form
Acceptance Criteria: The 'Contact Us' page must load and show the 'Get In Touch' header.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://automationexercise.com/"

def test_contact_us(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 10)
    
    contact_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/contact_us']")))
    driver.execute_script("arguments[0].click();", contact_btn)
    
    header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".contact-form h2")))
    assert "GET IN TOUCH" in header.text, "The 'GET IN TOUCH' header is missing."