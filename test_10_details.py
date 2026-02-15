import pytest
from selenium.webdriver.common.by import By
URL = "https://automationexercise.com/"

def test_product_details_page(driver):
    driver.get(URL)
    
    # Use JS Click to avoid ads blocking the click
    view_btn = driver.find_element(By.CSS_SELECTOR, "a[href='/product_details/1']")
    driver.execute_script("arguments[0].click();", view_btn)
    
    assert "product_details" in driver.current_url