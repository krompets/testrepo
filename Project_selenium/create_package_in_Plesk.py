import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("https://95.164.68.118:8443/")
    driver.find_element_by_name("login_name").send_keys("root")
    driver.find_element_by_name("passwd").send_keys("$%rtFGvb^&")
    driver.find_element_by_name("send").click()
    WebDriverWait(driver, 10).until(EC.title_contains("Home"))
    driver.find_element_by_class_name("icon-nav-service-plans").click()
    driver.find_element_by_class_name("sb-add-new-plan").click()
    driver.find_element_by_id("general-name").send_keys("pack2")
    driver.find_element_by_id("btn-send").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"msg-info")))
