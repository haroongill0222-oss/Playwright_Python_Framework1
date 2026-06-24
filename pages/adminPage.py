from pages.basePage import BasePage

class AdminPage(BasePage):

    # locators
    admin_menu="//span[text()='Admin']"
    job_dropdown="//span[normalize-space()='Job']"
    job_titles_menu="//a[normalize-space()='Job Titles']"
    add_button="//button[normalize-space()='Add']"

    job_title_input="(//input[@class='oxd-input oxd-input--active'])[2]"
    description_input="//textarea[@placeholder='Type description here']"
    note_input="//textarea[@placeholder='Add note']"
    save_btn="//button[normalize-space()='Save']"

    def navigate_to_job_title(self):
        self.select_element(self.admin_menu)
        self.select_element(self.job_dropdown)
        self.select_element(self.job_titles_menu)

    def click_add_job_title(self):
        self.select_element(self.add_button)

    def add_job_title(self, title, description, note):
        self.enter_text(self.job_title_input, title)
        self.enter_text(self.description_input, description)
        self.enter_text(self.note_input, note)

    def click_save_btn(self):
        self.select_element(self.save_btn)