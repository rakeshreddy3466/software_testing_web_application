from selenium.webdriver.common.by import By
URL = "https://automationexercise.com/"

def test_homepage_load(driver):
    driver.get(URL)
    logo = driver.find_element(By.CSS_SELECTOR, "img[alt='Website for automation practice']")
    assert logo.is_displayed()