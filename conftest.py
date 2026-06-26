import os
import pytest
import allure
from playwright.sync_api import sync_playwright

from pages.loginPage import LoginPage
from utilities.configReader import ConfigReader

from utilities.logger import setup_logger

logger = setup_logger()

# Authentication state file
AUTH_STATE_PATH = ".auth/user_state.json"


# ---------------------------------------------------------
# PLAYWRIGHT INSTANCE
# ---------------------------------------------------------
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


# ---------------------------------------------------------
# BROWSER SETUP
# ---------------------------------------------------------
@pytest.fixture(scope="session", params=["chromium"])
def browser(request, playwright_instance):

    browser_name = request.param

    browser = getattr(playwright_instance, browser_name).launch(
        headless=False,
        slow_mo=1000
    )

    yield browser

    browser.close()


# ---------------------------------------------------------
# LOGIN ONCE AND SAVE SESSION
# ---------------------------------------------------------
@pytest.fixture(scope="session", autouse=True)
def create_auth_state(browser):

    os.makedirs(".auth", exist_ok=True)

    logger.info("Login process started")
    page = browser.new_page()

    page.goto(ConfigReader.QA_URL)

    login = LoginPage(page)

    login.login(
        ConfigReader.username,
        ConfigReader.PASSWORD
    )

    page.wait_for_url("**/dashboard/**")

    page.context.storage_state(path=AUTH_STATE_PATH)

    print("\n Login executed only once")

    page.close()

    yield

    # Cleanup after execution
    if os.path.exists(AUTH_STATE_PATH):
        os.remove(AUTH_STATE_PATH)
        print("\n Session file deleted")


# ---------------------------------------------------------
# LOGGED-IN PAGE FIXTURE
# ---------------------------------------------------------
@pytest.fixture()
def logged_in_page(browser, create_auth_state):

    context = browser.new_context(
        storage_state=AUTH_STATE_PATH
    )

    page = context.new_page()

    page.goto(ConfigReader.QA_URL)

    page.wait_for_url("**/dashboard/**")

    print(f"\nCurrent URL: {page.url}")

    yield page

    page.close()
    context.close()


# ---------------------------------------------------------
# NORMAL PAGE FIXTURE
# ---------------------------------------------------------
@pytest.fixture()
def page(browser):

    page = browser.new_page()

    yield page

    page.close()


# ---------------------------------------------------------
# 🔥 ALLURE SCREENSHOT ON FAILURE HOOK (ADDED)
# ---------------------------------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    # Only capture screenshot when test fails in execution phase
    if report.when == "call" and report.failed:

        page = item.funcargs.get("logged_in_page") or item.funcargs.get("page")

        if page:

            try:
                allure.attach(
                    page.screenshot(full_page=True),
                    name=f"Failure Screenshot - {item.name}",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"Failed to capture screenshot: {e}")