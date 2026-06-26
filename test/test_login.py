import time

from pages.loginPage import LoginPage
from utilities.configReader import ConfigReader
from utilities.logger import setup_logger

looger=setup_logger()
def test_valid_login(page):
    page.goto(ConfigReader.QA_URL)

    login=LoginPage(page)

    login.login(
        ConfigReader.username,
        ConfigReader.PASSWORD)

    page.wait_for_url("**/dashboard/**")

    assert "dashboard" in page.url.lower()

    time.sleep(2)
    looger.info("successful log in dashboard ")