import time
from selenium.webdriver.common.by import By
URL = "https://automationexercise.com/"

def test_add_to_cart(driver):
    driver.get(URL)
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(1) # Short wait for scroll
    
    # Strategy: Get ALL 'Add to cart' buttons
    buttons = driver.find_elements(By.CSS_SELECTOR, "a.add-to-cart")
    
    # Loop through them and click the first one that is actually visible
    clicked = False
    for btn in buttons:
        if btn.is_displayed():
            driver.execute_script("arguments[0].click();", btn)
            clicked = True
            break
            
    assert clicked, "Could not find any visible 'Add to cart' button!"
    
    time.sleep(2)
    success_msg = driver.find_element(By.XPATH, "//h4[contains(text(),'Added!')]")
    assert success_msg.is_displayed()