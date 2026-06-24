import os

import pytest

from playwright.sync_api import sync_playwright

from pages.loginPage import LoginPage

from utilities.configReader import ConfigReader

# Authentication state file

AUTH_STATE_PATH = ".auth/user_state.json"


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session", params=["chromium"])
# @pytest.fixture(scope="session", params=["chromium", "firefox"])

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

    page = browser.new_page()

    page.goto(ConfigReader.QA_URL)

    login = LoginPage(page)

    login.login(

        ConfigReader.username,   # FIXED
        ConfigReader.PASSWORD

    )

    page.wait_for_url("**/dashboard/**")

    page.context.storage_state(   # FIXED method call

        path=AUTH_STATE_PATH

    )

    print("\n Login executed only once")

    page.close()

    yield

    # Cleanup after execution

    if os.path.exists(AUTH_STATE_PATH):
        os.remove(AUTH_STATE_PATH)

        print("\n Session file deleted")


# ---------------------------------------------------------

# LOGGED-IN PAGE FOR TESTS

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

# NORMAL PAGE (WITHOUT LOGIN)

# ---------------------------------------------------------

@pytest.fixture()
def page(browser):
    page = browser.new_page()

    yield page

    page.close()