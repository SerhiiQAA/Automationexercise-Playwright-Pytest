from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page)
        self.page = page
        self.base_url = base_url
        
        self.test_cases_button = page.locator("li a[href='/test_cases']")
        self.contact_us_button = page.locator("li a[href='/contact_us']")
        self.products_button = page.locator("li a[href='/products']")
        self.signup_login_button = page.locator("a[href='/login']")
        self.subscription_title = page.locator("#footer h2") 
        self.email_input_field = page.locator("#susbscribe_email")
        self.subscribe_button = page.locator("#subscribe") 
        self.subscription_success_message = page.locator("div#success-subscribe") 
        # self.home_url = "http://automationexercise.com"

    def navigate(self):
        self.page.goto(self.base_url)

    def is_home_page_visible(self):
        return "Automation Exercise" in self.page.title()

    def click_test_cases(self):
        self.test_cases_button.click()

    def click_contact_us(self):
        self.contact_us_button.click()

    def click_products(self):
        self.products_button.click()

    def click_signup_login(self):
        self.signup_login_button.click()