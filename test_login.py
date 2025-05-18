from selenium import webdriver
import time,allure,pytest
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
@pytest.fixture
def setup():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")
    return driver
def test_negative(setup):
    driver=setup
    username=driver.find_element(By.ID,"login-username")
    username.send_keys("admin@admin")
    password=driver.find_element(By.ID,"login-password")
    password.send_keys("admin")
    sign_in_btn=driver.find_element(By.XPATH,"//button/span[text()='Sign in']")
    sign_in_btn.click()
    time.sleep(5)
    js_notification_box_msg=driver.find_element(By.XPATH,"//div/div[@id='js-notification-box-msg']")
    assert js_notification_box_msg.text=="Your email, password, IP address or location did not match"
    driver.quit()
def test_positive(setup):
    driver=setup
    username = driver.find_element(By.ID, "login-username")
    username.send_keys("somesh065@gmail.com")
    password=driver.find_element(By.ID,"login-password")
    password.send_keys("1Somesh#16#")
    sign_in_btn = driver.find_element(By.XPATH, "//button/span[text()='Sign in']")
    sign_in_btn.click()
    time.sleep(5)
    dashboard=driver.find_element(By.XPATH,"//div/p/span[@data-qa='lufexuloga']")
    assert "Somesh" in dashboard.text
    driver.quit()