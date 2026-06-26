import allure
import pytest

from pages.pimPage import PIMPage
from pages.dashboardPage import DashboardPage
from testdata.testdata import Testdata
from utilities.logger import setup_logger

logger=setup_logger()
@allure.title("verify pim page")
@allure.description("validate pim page")
@pytest.mark.order(2)
def test_add_employee(logged_in_page):

    dashboard = DashboardPage(logged_in_page)
    pim = PIMPage(logged_in_page)

    dashboard.navigate_to_pim()

    with allure.step("click add btn"):

        pim.click_add_btn()

    with allure.step("Add employee detail"):
        pim.add_employee_detail(
            Testdata.First_name,
            Testdata.Middle_name,
            Testdata.Last_name
        )

    with allure.step("Successful verify personal detail"):
        logged_in_page.wait_for_url("**/viewPersonalDetails**")
        logger.info("user landed on pim page successfully")