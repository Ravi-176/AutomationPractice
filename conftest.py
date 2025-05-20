import pytest
from dotenv import load_dotenv
from selenium import webdriver
import os
load_dotenv()
@pytest.fixture(scope="class")
def setup(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    base_url=os.getenv("BASE_URL")
    username=os.getenv("USER_NAME")
    password=os.getenv("PASSWORD")
    driver.get(base_url)
    request.cls.driver=driver
    request.cls.base_url=base_url
    request.cls.username=username
    request.cls.password=password
    return driver
