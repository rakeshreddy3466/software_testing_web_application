from selenium.webdriver.common.by import By
URL = "https://automationexercise.com/"

def test_view_cart_page(driver):
    driver.get(URL)
    # Force click using Javascript (bypasses ads/overlays)
    cart_btn = driver.find_element(By.CSS_SELECTOR, "a[href='/view_cart']")
    driver.execute_script("arguments[0].click();", cart_btn)
    
    assert "view_cart" in driver.current_url