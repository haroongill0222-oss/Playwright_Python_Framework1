import allure
import pytest

from pages.dashboardPage import DashboardPage

@allure.title("Open Desktop page")
@allure.description("Successful open desktop page")
@pytest.mark.order(1)
def test_dashboard(logged_in_page):
    dashboard = DashboardPage(logged_in_page)

    with allure.step("successful  navigate"):
        dashboard.navigate_to_pim()
