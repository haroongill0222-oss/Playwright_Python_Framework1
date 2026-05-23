import time


def test_login(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    assert "OrangeHRM" in page.title()
    time.sleep(3)