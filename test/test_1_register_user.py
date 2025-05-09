import allure
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from playwright.sync_api import expect
from faker import Faker
from utils.take_screenshot import take_screenshot

fake = Faker()

@allure.title("User Registration Test")
@allure.description("Test for registering a new user with step validations and screenshots")
def test_register_user(base_url, browser):
    page = browser.new_page()
    home = HomePage(page, base_url)
    login = LoginPage(page)
    register = RegisterPage(page)

    name = fake.first_name()
    email = fake.email()
    password = fake.password()
    first_name = fake.first_name()
    last_name = fake.last_name()
    company = fake.company()
    address1 = fake.street_address()
    address2 = fake.secondary_address()
    country = "Canada"
    state = fake.state()
    city = fake.city()
    zip_code = fake.zipcode()
    mobile = fake.phone_number()

    with allure.step("1-2. Navigate to the home page"):
        home.navigate()
        assert home.is_home_page_visible()
        take_screenshot(page, "Home Page")

    with allure.step("3. Click 'Signup/Login' button"):
        home.click_signup_login()
        allure.attach(page.screenshot(), name="Click Signup/Login", attachment_type=allure.attachment_type.PNG)

    with allure.step("4. Verify that 'New User Signup!' is visible"):
        expect(login.signup_form_title).to_contain_text("New User Signup!")
        take_screenshot(page, "Signup Form")

    with allure.step("5. Fill in 'Name' and 'Email' fields"):
        login.fill_signup_form(name, email)
        take_screenshot(page, "Filled Signup Form")

    with allure.step("6. Click 'Signup' button"):
        login.signup_button.click()
        allure.attach(page.screenshot(), name="Signup Click", attachment_type=allure.attachment_type.PNG)

    with allure.step("7. Verify 'Enter Account Information' is visible"):
        expect(register.title.nth(0)).to_contain_text("Enter Account Information")
        take_screenshot(page, "Enter Account Information")

    with allure.step("8. Fill in account information"):
        register.fill_account_info(password, 1, 1, 2000)
        take_screenshot(page, "Filled Account Info")

    with allure.step("9. Select checkbox 'Sign up for our newsletter!'"):
        register.newsletter_checkbox.check()
        take_screenshot(page, "Newsletter Checkbox Selected")

    with allure.step("10. Select checkbox 'Receive special offers from our partners!'"):
        register.offers_checkbox.check()
        take_screenshot(page, "Offers Checkbox Selected")

    with allure.step("11. Fill in address information"):
        register.fill_address(first_name, last_name, company, address1, address2, country, state, city, zip_code, mobile)
        allure.attach(page.screenshot(), name="Address Info", attachment_type=allure.attachment_type.PNG)

    with allure.step("12. Click 'Create Account' button"):
        register.create_account_btn.click()
        allure.attach(page.screenshot(), name="Create Account Click", attachment_type=allure.attachment_type.PNG)

    with allure.step("13. Verify 'Account Created!' is visible"):
        expect(register.account_msg.nth(0)).to_contain_text("Account Created!")
        take_screenshot(page, "Account Created")

    with allure.step("14. Click 'Continue' button"):
        register.continue_btn.click()
        allure.attach(page.screenshot(), name="Continue Click", attachment_type=allure.attachment_type.PNG)

    with allure.step("15. Verify 'Logged in as username' is visible"):
        expect(register.logged_in_as).to_contain_text(name)
        take_screenshot(page, "Logged in as User")

    with allure.step("16. Click 'Delete Account' button"):
        expect(register.delete_account_btn).to_be_visible()
        register.delete_account_btn.click()
        take_screenshot(page, "Account Deletion Initiated")

    with allure.step("17. Verify 'Account Deleted!' is visible"):
        expect(register.account_msg.nth(0)).to_contain_text("Account Deleted!")
        take_screenshot(page, "Account Deleted")

    with allure.step("18. Click 'Continue' after deletion"):
        register.continue_btn.click()

    page.close()




# from pages.home_page import HomePage
# from pages.login_page import LoginPage
# from pages.register_page import RegisterPage
# from playwright.sync_api import expect
# from faker import Faker
# from utils.take_screenshot import take_screenshot


# fake = Faker()

# def test_register_user(base_url, browser):
#     page = browser.new_page()
#     home = HomePage(page, base_url)
#     login = LoginPage(page)
#     register = RegisterPage(page)

#     name = fake.first_name()
#     email = fake.email()
#     password = fake.password()
#     first_name = fake.first_name()
#     last_name = fake.last_name()
#     company = fake.company()
#     address1 = fake.street_address()
#     address2 = fake.secondary_address()
#     country = "Canada"
#     state = fake.state()
#     city = fake.city()
#     zip_code = fake.zipcode()
#     mobile = fake.phone_number()

#     # 1-2. Navigate to correct url
#     home.navigate()

#     # 3. Verify that home page is visible successfully
#     assert home.is_home_page_visible()

#     # 4. Click on 'Test Cases' button
#     home.click_signup_login()

#     # 5. Verify 'New User Signup!' is visible
#     expect(login.signup_form_title).to_contain_text("New User Signup!")

#     # 6. Enter name and email
#     login.fill_signup_form(name, email)

#     # 7. Click 'Signup' button
#     login.signup_button.click()

#     # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
#     expect(register.title.nth(0)).to_contain_text("Enter Account Information")
#     take_screenshot(page, "Enter Account Information")

#     # 9. Fill details: Title, Name, Email, Password, Date of birth
#     register.fill_account_info(password, 1, 1, 2000)
#     take_screenshot(page, "Fill details")

#     # 10. Select checkbox 'Sign up for our newsletter!'
#     register.newsletter_checkbox.check()
#     take_screenshot(page, "Select checkbox 'Sign up for our newsletter!'")

#     # 11. Select checkbox 'Receive special offers from our partners!'
#     register.offers_checkbox.check()
#     take_screenshot(page, "Select checkbox 'Receive special offers from our partners!'")

#     # 12. Fill address info
#     register.fill_address(first_name, last_name, company, address1, address2, country, state, city, zip_code, mobile)
#     take_screenshot(page, "Fill address info: first_name, last_name, company, address1, address2, country, state, city, zip_code, mobile")

#     # 13. Click 'Create Account' button
#     register.create_account_btn.click()

#     # 14. Verify 'ACCOUNT CREATED!' is visible
#     expect(register.account_msg.nth(0)).to_contain_text("Account Created!")
#     take_screenshot(page, "Account Created!")

#     # 15. Click 'Continue' button
#     register.continue_btn.click()

#     # 16. Verify 'Logged in as username' is visible
#     expect(register.logged_in_as).to_contain_text(name)
#     take_screenshot(page, "'Logged in as username' and 'Delete Account' button is visible")

#     # 17. Click 'Delete Account' button
#     expect(register.delete_account_btn).to_be_visible()
#     register.delete_account_btn.click()

#     # 18. Verify 'ACCOUNT DELETED!' is visible and click 'Continue'
#     expect(register.account_msg.nth(0)).to_contain_text("Account Deleted!")
#     take_screenshot(page, "Account Deleted!")

#     register.continue_btn.click()

#     page.close()