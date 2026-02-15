import time
from selenium.webdriver.common.by import By
URL = "https://automationexercise.com/"

def test_cart_items_exist(driver):
    driver.get(URL + "product_details/1")
    
    # Use JS Click to avoid "ElementClickIntercepted"
    add_btn = driver.find_element(By.CSS_SELECTOR, "button.cart")
    driver.execute_script("arguments[0].click();", add_btn)
    
    time.sleep(2)
    driver.get(URL + "view_cart")
    
    rows = driver.find_elements(By.CSS_SELECTOR, "#cart_info_table tbody tr")
    assert len(rows) > 0