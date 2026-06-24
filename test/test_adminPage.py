import pytest
from playwright.sync_api import expect
from pages.adminPage import AdminPage
from testdata.testData1 import TestData1
from testdata.excel_reader import get_excel_data


@pytest.mark.parametrize("job_title,job_description,job_note",get_excel_data("Add_Jobs"))
def test_add_job_title(logged_in_page,job_title,job_description,job_note):

    admin = AdminPage(logged_in_page)

    # Navigate
    admin.navigate_to_job_title()

    # Click Add
    admin.click_add_job_title()

    # Fill Form
    admin.add_job_title(
        job_title,job_description,job_note
    )

    # Save
    admin.click_save_btn()

    # Verification
    expect(
        logged_in_page.locator("//h6[text()='Job Titles']")
    ).to_be_visible()