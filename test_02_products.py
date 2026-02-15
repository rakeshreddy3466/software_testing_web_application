from selenium.webdriver.common.by import By
URL = "https://automationexercise.com/"

def test_view_products(driver):
    driver.get(URL)
    
    # Fix: Use JavaScript to click because Ads cover the button
    products_btn = driver.find_element(By.CSS_SELECTOR, "a[href='/products']")
    driver.execute_script("arguments[0].click();", products_btn)
    
    header = driver.find_element(By.CSS_SELECTOR, ".title.text-center").text
    assert "ALL PRODUCTS" in header