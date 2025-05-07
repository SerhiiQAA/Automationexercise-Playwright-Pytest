from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.signup_login_btn = page.locator("a[href='/login']")
        self.login_email_input = page.locator("input[data-qa='login-email']")
        self.login_password_input = page.locator("input[data-qa='login-password']")
        self.login_button = page.locator("button[data-qa='login-button']")
        self.signup_name_input = page.locator("input[name='name']")
        self.signup_email_input = page.locator("input[data-qa='signup-email']")
        self.signup_button = page.locator("button[data-qa='signup-button']")
        self.logged_in_as = page.locator("a:has-text('Logged in as')")
        self.delete_account_btn = page.locator("a[href='/delete_account']")
        self.logout_btn = page.locator("a[href='/logout']")
        self.signup_form_title = page.locator(".signup-form h2")
        self.signup_form_msg = page.locator(".signup-form p")
        self.login_form_title = page.locator(".login-form h2")
        self.login_form_msg = page.locator(".login-form p")

    def fill_signup_form(self, name, email):
        self.signup_name_input.fill(name)
        self.signup_email_input.fill(email)

    def fill_login_form(self, email, password):
        self.login_email_input.fill(email)
        self.login_password_input.fill(password)