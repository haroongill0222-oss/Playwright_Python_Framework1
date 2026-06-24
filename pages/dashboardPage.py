from pages.basePage import BasePage


class DashboardPage(BasePage):
    pim_menu = "//span[normalize-space()='PIM']"

    def navigate_to_pim(self):
        self.page.locator(self.pim_menu).click()