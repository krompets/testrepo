import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("https://192.168.107.62:2087/")
    driver.find_element_by_name("user").send_keys("root")
    driver.find_element_by_name("pass").send_keys("$%rtFGvb^&")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_contains("WebHost Manager"))