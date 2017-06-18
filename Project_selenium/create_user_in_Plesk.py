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
    driver.find_element_by_class_name("icon-nav-clients").click()
    driver.find_element_by_class_name("sb-add-new-customer").click()
    driver.find_element_by_id("contactInfoSection-contactInfo-contactName").send_keys("user1")
    driver.find_element_by_id("contactInfoSection-contactInfo-email").send_keys("user1@m.co")
    driver.find_element_by_id("accessToPanelSection-loginInfo-userName").send_keys("user1")
    driver.find_element_by_id("accessToPanelSection-loginInfo-password-generate-button").click()
    driver.find_element_by_id("subscription-domainInfo-domainName").send_keys("user1.com")
    driver.find_element_by_id("subscription-domainInfo-userName").send_keys("user1")
    driver.find_element_by_id("subscription-domainInfo-password-generate-button").click()
    driver.find_element_by_id("btn-send").click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"msg-info")))
