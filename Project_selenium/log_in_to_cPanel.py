import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(capabilities={"acceptInsecureCerts": True,"marionette": False})
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    pass
    driver.get("https://192.168.107.62:2087/")
    driver.find_element_by_name("user").send_keys("root")
    driver.find_element_by_name("pass").send_keys("$%rtFGvb^&")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_contains("WebHost Manager"))