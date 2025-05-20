import time,allure,pytest
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


@pytest.mark.usefixtures("setup")
class TestLogin():
    @pytest.mark.negative
    def test_negative(self,setup):
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
    @pytest.mark.positive
    def test_positive(self,setup):
        driver=setup
        username = driver.find_element(By.ID, "login-username")
        username.send_keys(self.username)
        password=driver.find_element(By.ID,"login-password")
        password.send_keys(self.password)
        sign_in_btn = driver.find_element(By.XPATH, "//button/span[text()='Sign in']")
        sign_in_btn.click()
        time.sleep(5)
        dashboard=driver.find_element(By.XPATH,"//div/p/span[@data-qa='lufexuloga']")
        assert "Somesh" in dashboard.text
        driver.quit()