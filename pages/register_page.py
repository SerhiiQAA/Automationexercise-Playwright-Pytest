from pages.base_page import BasePage

class RegisterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.signup_login_btn = page.locator("a[href='/login']")
        self.signup_name_input = page.locator("input[name='name']")
        self.signup_email_input = page.locator("input[data-qa='signup-email']")
        self.signup_button = page.locator("button[data-qa='signup-button']")
        self.title_radio = page.locator("#id_gender1")
        self.password_input = page.locator("#password")
        self.days_select = page.locator("#days")
        self.months_select = page.locator("#months")
        self.years_select = page.locator("#years")
        self.newsletter_checkbox = page.locator("#newsletter")
        self.offers_checkbox = page.locator("#optin")
        self.first_name_input = page.locator("#first_name")
        self.last_name_input = page.locator("#last_name")
        self.company_input = page.locator("#company")
        self.address1_input = page.locator("#address1")
        self.address2_input = page.locator("#address2")
        self.country_select = page.locator("#country")
        self.state_input = page.locator("#state")
        self.city_input = page.locator("#city")
        self.zipcode_input = page.locator("#zipcode")
        self.mobile_number_input = page.locator("#mobile_number")
        self.create_account_btn = page.locator("button[data-qa='create-account']")
        self.continue_btn = page.locator("a[data-qa='continue-button']")
        self.logged_in_as = page.locator("a:has-text('Logged in as')")
        self.delete_account_btn = page.locator("a[href='/delete_account']")
        self.account_msg = page.locator("h2")
        self.title = page.locator("h2.title")
        self.enter_account_info_msg = page.locator("b")
        self.email_exists_error = page.locator("p:has-text('Email Address already exist!')")
        self.logout_btn = page.locator("a[href='/logout']")

    # def open_home_page(self, url):
    #     self.page.goto(url)

    def click_signup(self):
        self.signup_button.click()

    def fill_account_info(self, password, day, month, year):
        self.title_radio.check()
        self.password_input.fill(password)
        self.days_select.select_option(str(day))
        self.months_select.select_option(str(month))
        self.years_select.select_option(str(year))

    def fill_address(self, first_name, last_name, company, addr1, addr2, country, state, city, zip_code, mobile):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.company_input.fill(company)
        self.address1_input.fill(addr1)
        self.address2_input.fill(addr2)
        self.country_select.select_option(country)
        self.state_input.fill(state)
        self.city_input.fill(city)
        self.zipcode_input.fill(zip_code)
        self.mobile_number_input.fill(mobile)