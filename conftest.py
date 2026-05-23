import pytest
from playwright.sync_api import sync_playwright



@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session",params=["chromium","firefox","webkit"])
def browser(request,playwright_instance):
    browser_name=request.param
    browser=getattr(playwright_instance,browser_name).launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="session")
def page(browser):
    page=browser.new_page()
    yield page
    page.close()