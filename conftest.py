import os
import pytest
from playwright.sync_api import sync_playwright
from pages.loginPage import LoginPage
from utilities.configReader import ConfigReader

AUTH_STATE_PATH = ".auth/user_state.json"


# -------------------------------
# Playwright Instance
# -------------------------------

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


# -------------------------------
# Browser Fixture
# -------------------------------

@pytest.fixture(scope="session", params=["chromium"])
def browser(request, playwright_instance):

    browser_name = request.param

    browser = getattr(
        playwright_instance,
        browser_name
    ).launch(
        headless=False,
        slow_mo=1000
    )

    yield browser

    browser.close()


# -------------------------------
# Login Once & Save Session
# -------------------------------

@pytest.fixture(scope="session", autouse=True)
def create_auth_state(browser):

    os.makedirs(".auth", exist_ok=True)

    page = browser.new_page()

    page.goto(ConfigReader.QA_URL)

    login = LoginPage(page)

    login.login(
        ConfigReader.username,
        ConfigReader.PASSWORD
    )

    page.wait_for_url("**/dashboard/index")

    page.context.storage_state(
        path=AUTH_STATE_PATH
    )

    print("\nLogin executed only once")

    page.close()

    yield

    if os.path.exists(AUTH_STATE_PATH):
        os.remove(AUTH_STATE_PATH)
        print("\nSession file deleted")


# -------------------------------
# Logged In Page
# -------------------------------

@pytest.fixture()
def logged_in_page(browser, create_auth_state):

    context = browser.new_context(
        storage_state=AUTH_STATE_PATH
    )

    page = context.new_page()

    page.goto(ConfigReader.QA_URL)

    page.wait_for_url("**/dashboard/index")

    print(f"Current URL: {page.url}")

    yield page

    page.close()
    context.close()


# -------------------------------
# Normal Page
# -------------------------------

@pytest.fixture()
def page(browser):

    page = browser.new_page()

    yield page

    page.close()