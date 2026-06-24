from pages.basePage import BasePage

class PIMPage (BasePage):
    #   locators

    pim_menu = "//span[text()='PIM']"
    add_employee="//a[normalize-space()='Add Employee']"

    first_name="//input[@placeholder='First Name']"
    middle_name="//input[@placeholder='Middle Name']"
    last_name="//input[@placeholder='Last Name']"

    save_btn="//button[normalize-space()='Save']"

    def click_pim_menu (self):

        self.select_element(self.pim_menu)

    def click_add_btn (self):
        self.page.wait_for_selector(self.add_employee)
        self.select_element(self.add_employee)

    def add_employee_detail (self,first,middle,last):
        self.enter_text(self.first_name,first)
        self.enter_text(self.middle_name,middle)
        self.enter_text(self.last_name,last)

        self.select_element(self.save_btn)

