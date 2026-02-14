import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"

# -----------------------------
# Test Case 1: Successful Login
# -----------------------------
def test_login_success():
    print("Opening browser.....")
    driver = webdriver.Chrome()
    driver.get(URL)
    time.sleep(2)  # tunggu 2 detik agar halaman terbuka sepenuhnya

    print("Entering valid credentials...")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(2)
    driver.find_element(By.ID, "login-button").click()

    print("Waiting for Products page...")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )
    time.sleep(1)

    # Verification
    assert "inventory" in driver.current_url, "URL does not contain inventory"
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products", "Title is not Products"
    print("Test Login Success: Passed")
    time.sleep(2)  # tunggu sebentar sebelum menutup browser
    driver.quit()


# -----------------------------
# Test Case 2: Failed Login
# -----------------------------
def test_login_failure():
    print("Opening browser...")
    driver = webdriver.Chrome()
    driver.get(URL)
    time.sleep(2)

    print("Entering invalid credentials...")
    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    time.sleep(1)
    driver.find_element(By.ID, "login-button").click()

    print("Waiting for error message...")
    error_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )
    time.sleep(1)

    # Verification
    assert "Username and password do not match" in error_element.text, "Error message not shown"
    print("Test Login Failure: Passed")
    time.sleep(2)
    driver.quit()


# -----------------------------
# Run Tests
# -----------------------------
if __name__ == "__main__":
    test_login_success()
    test_login_failure()
