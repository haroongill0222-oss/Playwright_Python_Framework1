from pages.pimPage import PIMPage
from pages.dashboardPage import DashboardPage
from testdata.testdata import Testdata


def test_add_employee(logged_in_page):

    dashboard = DashboardPage(logged_in_page)
    pim = PIMPage(logged_in_page)

    dashboard.navigate_to_pim()

    pim.click_add_btn()

    pim.add_employee_detail(
        Testdata.First_name,
        Testdata.Middle_name,
        Testdata.Last_name
    )

    logged_in_page.wait_for_url("**/viewPersonalDetails**")