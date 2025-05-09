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
    page = browser.new_page()
    user = create_test_user(page, base_url)

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