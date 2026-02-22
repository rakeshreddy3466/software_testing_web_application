"""
Feature Requirement 04 (FR04): Shopping Flow - Add to Cart
Acceptance Criteria: The 'Add to Cart' button must trigger a confirmation modal to the user.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://automationexercise.com/"

def test_add_to_cart(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 10)
    
    # Step 1: Wait for the product container and scroll it into view so buttons render as 'displayed'
    container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.features_items")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", container)
    
    buttons = driver.find_elements(By.CSS_SELECTOR, "a.add-to-cart")
    
    # Step 2: Iterate and click the first interactable/visible button using JS
    clicked = False
    for btn in buttons:
        if btn.is_displayed():
            driver.execute_script("arguments[0].click();", btn)
            clicked = True
            break
            
    assert clicked, "Could not find any visible 'Add to cart' button on the page."
    
    # Step 3: Wait explicitly for the success modal to appear
    success_modal = wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[contains(text(),'Added!')]")))
    
    # Step 4: Verify the modal is displayed
    assert success_modal.is_displayed(), "The 'Added!' confirmation modal was not displayed."