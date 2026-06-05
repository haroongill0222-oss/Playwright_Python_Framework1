from pages.basePage import BasePage

class LoginPage(BasePage):

    # locators
    username_input = "input[name='username']"
    password_input = "input[name='password']"
    login_button = "button[type='submit']"

    def login(self, username, password):
        self.page.locator(self.username_input).wait_for(state="visible")
        self.enter_text(self.username_input, username)
        self.enter_text(self.password_input, password)
        self.select_element(self.login_button)