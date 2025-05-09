import allure
from pages.home_page import HomePage
from pages.contact_us_page import ContactUsPage
from faker import Faker
import os
from playwright.sync_api import expect
from utils.take_screenshot import take_screenshot

fake = Faker()

@allure.title("Contact Us Form Test")
@allure.description("Test for submitting the contact us form with a message and file upload")
def test_contact_us_form(base_url, browser):
    page = browser.new_page()
    home = HomePage(page, base_url)
    contact = ContactUsPage(page)

    name = fake.name()
    email = fake.email()
    subject = "Test Subject"
    message = "This is a test message."
    file_path = os.path.abspath("data/test_file.txt")

    with allure.step("1-2. Navigate to the correct URL"):
        home.navigate()
        take_screenshot(page, "Navigated to Home Page")

    with allure.step("3. Verify that the home page is visible"):
        assert home.is_home_page_visible()
        take_screenshot(page, "Home Page Visible")

    with allure.step("4. Click 'Contact Us' button"):
        contact.click_contact_us()
        allure.attach(page.screenshot(), name="Click Contact Us", attachment_type=allure.attachment_type.PNG)

    with allure.step("5. Verify that 'GET IN TOUCH' is visible"):
        assert contact.url_contains("/contact_us")
        expect(contact.title).to_contain_text("Get In Touch")
        take_screenshot(page, "Contact Page Visible")

    with allure.step("6. Enter name, email, subject, and message"):
        contact.fill_form(name, email, subject, message)
        take_screenshot(page, "Filled Contact Form")

    with allure.step("7. Upload file"):
        contact.upload_file(file_path)
        take_screenshot(page, "File Uploaded")

    with allure.step("8-9. Click 'Submit' and accept the confirmation dialog"):
        contact.page.on("dialog", lambda dialog: dialog.accept())
        contact.submit_button.click()
        allure.attach(page.screenshot(), name="Submit Click", attachment_type=allure.attachment_type.PNG)

    with allure.step("10. Verify success message 'Success! Your details have been submitted successfully.' is visible"):
        expect(contact.success_msg).to_contain_text("Success! Your details have been submitted successfully")
        take_screenshot(page, "Form Submission Success")

    with allure.step("11. Click 'Home' button and verify navigation to home page"):
        contact.click_home_button()
        expect(contact.page).to_have_title("Automation Exercise")
        take_screenshot(page, "Navigated Back to Home Page")

    page.close()




# from pages.home_page import HomePage
# from pages.contact_us_page import ContactUsPage
# from faker import Faker
# import os
# from playwright.sync_api import expect
# from utils.take_screenshot import take_screenshot

# fake = Faker()

# def test_contact_us_form(base_url, browser):
#     page = browser.new_page()
#     home = HomePage(page, base_url)
#     contact = ContactUsPage(page)

#     name = fake.name()
#     email = fake.email()
#     subject = "Test Subject"
#     message = "This is a test message."
#     file_path = os.path.abspath("data/test_file.txt")

#     # 1-2. Navigate to correct url
#     home.navigate()

#     # 3. Verify that home page is visible successfully
#     assert home.is_home_page_visible()

#     # 4. Click on 'Contact Us' button
#     contact.click_contact_us()

#     # 5. Verify 'GET IN TOUCH' is visible
#     assert contact.url_contains("/contact_us")
#     expect(contact.title).to_contain_text("Get In Touch")

#     # 6. Enter name, email, subject and message
#     contact.fill_form(name, email, subject, message)

#     # 7. Upload file
#     contact.upload_file(file_path)

#     # 8-9. Click 'Submit' and OK buttons
#     contact.page.on("dialog", lambda dialog: dialog.accept())
#     contact.submit_button.click()

#     # 10. Verify success message 'Success! Your details have been submitted successfully.' is visible
#     expect(contact.success_msg).to_contain_text("Success! Your details have been submitted successfully")
#     take_screenshot(page, "Success! Your details have been submitted successfully")

#     # 11. Click 'Home' button and verify that landed to home page successfully
#     contact.click_home_button()
#     expect(contact.page).to_have_title("Automation Exercise")

#     page.close()