import time
from selenium.webdriver.common.by import By
URL = "https://automationexercise.com/"

def test_footer_subscription(driver):
    driver.get(URL)
    
    # Scroll all the way down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2) # Give it a moment to render
    
    # Strategy: Get the H2 element inside the footer widget
    # We use 'textContent' via JS to ensure we get the text even if hidden
    footer_header = driver.find_element(By.CSS_SELECTOR, ".footer-widget h2")
    text_content = driver.execute_script("return arguments[0].textContent;", footer_header)
    
    # Clean up whitespace and check
    assert "SUBSCRIPTION" in text_content.strip().upper()