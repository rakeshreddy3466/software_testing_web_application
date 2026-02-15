from selenium.webdriver.common.by import By
URL = "https://automationexercise.com/"

def test_contact_us(driver):
    driver.get(URL)
    contact_btn = driver.find_element(By.CSS_SELECTOR, "a[href='/contact_us']")
    driver.execute_script("arguments[0].click();", contact_btn)
    
    header = driver.find_element(By.CSS_SELECTOR, ".contact-form h2").text
    assert "GET IN TOUCH" in header