import time
from selenium.webdriver.common.by import By
URL = "https://automationexercise.com/"

def test_real_login(driver):
    driver.get(URL + "login")
    time.sleep(2) 
    
    # Use official testing credentials guaranteed by the site
    email_box = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-email']")
    driver.execute_script("arguments[0].value='testuser1@test.com';", email_box)
    
    pass_box = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']")
    driver.execute_script("arguments[0].value='password123';", pass_box)
    
    # 2. Click Login
    login_btn = driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']")
    driver.execute_script("arguments[0].click();", login_btn)
    
    time.sleep(3) 
    
    # 3. Verification Strategy
    try:
        logout_btn = driver.find_element(By.CSS_SELECTOR, "a[href='/logout']")
        assert logout_btn.is_displayed()
        print("\nLogin Successful: Logout button found.")
    except:
        body_text = driver.find_element(By.TAG_NAME, "body").text
        # We check for the name 'testuser' which is associated with these credentials
        assert "Logged in as" in body_text