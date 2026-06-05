import time

from pages.loginPage import LoginPage
from utilities.configReader import ConfigReader

def test_valid_login(page):
    page.goto(ConfigReader.QA_URL)

    login=LoginPage(page)

    login.login(
        ConfigReader.username,
        ConfigReader.PASSWORD)

    page.wait_for_url("**/dashboard/**")

    assert "dashboard" in page.url.lower()

    time.sleep(2)