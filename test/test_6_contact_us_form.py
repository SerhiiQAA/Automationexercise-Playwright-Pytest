from pages.home_page import HomePage
from pages.contact_us_page import ContactUsPage
from faker import Faker
import os
from playwright.sync_api import expect
from utils.take_screenshot import take_screenshot

fake = Faker()

def test_contact_us_form(base_url, browser):
    page = browser.new_page()
    home = HomePage(page, base_url)
    contact = ContactUsPage(page)

    name = fake.name()
    email = fake.email()
    subject = "Test Subject"
    message = "This is a test message."
    file_path = os.path.abspath("data/test_file.txt")

    # 1-2. Navigate to correct url
    home.navigate()

    # 3. Verify that home page is visible successfully
    assert home.is_home_page_visible()

    # 4. Click on 'Contact Us' button
    contact.click_contact_us()

    # 5. Verify 'GET IN TOUCH' is visible
    assert contact.url_contains("/contact_us")
    expect(contact.title).to_contain_text("Get In Touch")

    # 6. Enter name, email, subject and message
    contact.fill_form(name, email, subject, message)

    # 7. Upload file
    contact.upload_file(file_path)

    # 8-9. Click 'Submit' and OK buttons
    contact.page.on("dialog", lambda dialog: dialog.accept())
    contact.submit_button.click()

    # 10. Verify success message 'Success! Your details have been submitted successfully.' is visible
    expect(contact.success_msg).to_contain_text("Success! Your details have been submitted successfully")
    take_screenshot(page, "Success! Your details have been submitted successfully")

    # 11. Click 'Home' button and verify that landed to home page successfully
    contact.click_home_button()
    expect(contact.page).to_have_title("Automation Exercise")

    page.close()