import allure
from helpers.user_factory import create_test_user
from pages.home_page import HomePage
from pages.login_page import LoginPage
from playwright.sync_api import expect
from faker import Faker
from utils.take_screenshot import take_screenshot

fake = Faker()

@allure.title("Signup with Existing Email Test")
@allure.description("Test to verify that trying to sign up with an already registered email shows an error message")
def test_signup_with_existing_email_shows_error(base_url, browser):
    # Create a valid user first
    page = browser.new_page()
    user = create_test_user(page, base_url)

    # Initialize page objects
    home = HomePage(page, base_url)
    login = LoginPage(page)

    with allure.step("1. Preparing user data"):
        login.logout_btn.click()

    with allure.step("2. Navigate to the home page"):
        page.goto(base_url)
        take_screenshot(page, "Home Page Navigation")

    with allure.step("3. Verify that the home page is visible"):
        assert home.is_home_page_visible()
        take_screenshot(page, "Home Page Visible")

    with allure.step("4. Click 'Signup / Login' button"):
        home.click_signup_login()
        allure.attach(page.screenshot(), name="Click Signup/Login", attachment_type=allure.attachment_type.PNG)

    with allure.step("5. Verify that 'New User Signup!' is visible"):
        expect(login.signup_form_title).to_contain_text("New User Signup!")
        take_screenshot(page, "Signup Form Visible")

    with allure.step("6. Enter a different name but use the already registered email"):
        login.fill_signup_form(fake.first_name(), user["email"])
        take_screenshot(page, "Signup Form with Existing Email")

    with allure.step("7. Click the 'Signup' button"):
        login.signup_button.click()
        allure.attach(page.screenshot(), name="Signup Click", attachment_type=allure.attachment_type.PNG)

    with allure.step("8. Verify that the error message 'Email Address already exist!' is visible"):
        expect(login.signup_form_msg).to_contain_text("Email Address already exist!")
        take_screenshot(page, "Error Message for Existing Email")

    page.close()





# from helpers.user_factory import create_test_user
# from pages.home_page import HomePage
# from pages.login_page import LoginPage
# from playwright.sync_api import expect
# from faker import Faker
# from utils.take_screenshot import take_screenshot

# fake = Faker()

# def test_signup_with_existing_email_shows_error(base_url, browser):
#     # Create a valid user first
#     page = browser.new_page()
#     user = create_test_user(page, base_url)

#     # Initialize page objects
#     home = HomePage(page, base_url)
#     login = LoginPage(page)

#     # 1-2. Log out and go back to the home page
#     login.logout_btn.click()
#     page.goto(base_url)

#     # 3. Verify that the home page is visible
#     assert home.is_home_page_visible()

#     # 4. Click on 'Signup / Login' button
#     home.click_signup_login()

#     # 5. Verify that 'New User Signup!' is visible
#     expect(login.signup_form_title).to_contain_text("New User Signup!")

#     # 6. Enter a different name but use the already registered email
#     login.fill_signup_form(fake.first_name(), user["email"])

#     # 7. Click the 'Signup' button
#     login.signup_button.click()

#     # 8. Verify that the error message 'Email Address already exist!' is visible
#     expect(login.signup_form_msg).to_contain_text("Email Address already exist!")
#     take_screenshot(page, "Email Address already exist!")  

#     # Close the page
#     page.close()





# from pages.home_page import HomePage
# from pages.login_page import LoginPage
# from pages.register_page import RegisterPage
# from playwright.sync_api import expect
# from faker import Faker

# fake = Faker()

# def test_login_user_with_correct_credentials(base_url, browser):
#     page = browser.new_page()
#     home = HomePage(page, base_url)
#     login = LoginPage(page)
#     register = RegisterPage(page)

#     name = fake.first_name()
#     email = fake.email()
#     password = fake.password()

#     home.navigate()
#     home.click_signup_login()
#     login.fill_signup_form(name, email)
#     login.signup_button.click()
#     register.fill_account_info(password, 1, 1, 2000)
#     register.fill_address(name, fake.last_name(), fake.company(), fake.street_address(), fake.secondary_address(),
#                           "Canada", fake.state(), fake.city(), fake.zipcode(), fake.phone_number())
#     register.create_account_btn.click()
#     register.continue_btn.click()

#     # 1-2. Navigate to correct url
#     login.logout_btn.click()

#     # 3. Verify that home page is visible successfully
#     assert home.is_home_page_visible()

#     # 4. Click on 'Signup / Login' button
#     home.click_signup_login()

#     # 5. Verify 'New User Signup!' is visible
#     expect(login.signup_form_title).to_contain_text("New User Signup!")

#     # 6. Enter name and already registered email address
#     login.fill_signup_form(fake.first_name(), email)

#     # 7. Click 'Signup' button
#     login.signup_button.click()

#     # 8. Verify error 'Email Address already exist!' is visible
#     expect(login.signup_form_msg).to_contain_text("Email Address already exist!")

#     page.close()