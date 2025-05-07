from pages.base_page import BasePage

class ContactUsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.contact_us_btn = page.locator("a[href='/contact_us']")
        self.title = page.locator("h2:has-text('Get In Touch')")
        self.name_input = page.locator("input[name='name']")
        self.email_input = page.locator("input[name='email']")
        self.subject_input = page.locator("input[name='subject']")
        self.message_textarea = page.locator("textarea[name='message']")
        self.upload_file_input = page.locator("input[name='upload_file']")
        self.subscribe_email_input = page.locator("#susbscribe_email")
        self.submit_button = page.locator('input[type="submit"]')
        self.success_msg = page.locator("div.status.alert.alert-success")
        self.ad_container = page.locator("div.advertisement")
        self.ad_close_button = page.locator("ins > span > svg > g")
        self.home_button = page.locator("a.btn.btn-success")

    def click_contact_us(self):
        self.contact_us_btn.click()

    def fill_form(self, name, email, subject, message):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.subject_input.fill(subject)
        self.message_textarea.fill(message)
        self.message_textarea.blur()
        self.page.wait_for_timeout(300)

    def upload_file(self, file_path: str):
        self.upload_file_input.set_input_files(file_path)

    def click_submit_button(self):
        self.submit_button.click()

    def click_home_button(self):
        self.home_button.click()