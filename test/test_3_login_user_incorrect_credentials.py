import allure
from pages.home_page import HomePage
from pages.login_page import LoginPage
from playwright.sync_api import expect
from faker import Faker
from utils.take_screenshot import take_screenshot

fake = Faker()

@allure.title("Login Test with Incorrect Credentials")
@allure.description("Test for logging in with incorrect credentials and verifying error messages")
def test_login_with_incorrect_credentials(base_url, browser):
    page = browser.new_page()
    home = HomePage(page, base_url)
    login = LoginPage(page)

    wrong_email = fake.email()
    wrong_password = fake.password()

    with allure.step("1-2. Navigate to the home page"):
        home.navigate()
        take_screenshot(page, "Navigated to Home Page")

    with allure.step("3. Verify that the home page is visible"):
        assert home.is_home_page_visible()
        take_screenshot(page, "Home Page Visible")

    with allure.step("4. Click 'Signup / Login' button"):
        home.click_signup_login()
        allure.attach(page.screenshot(), name="Click Signup/Login", attachment_type=allure.attachment_type.PNG)

    with allure.step("5. Verify that 'Login to your account' is visible"):
        expect(login.login_form_title).to_contain_text("Login to your account")
        take_screenshot(page, "Login Form Visible")

    with allure.step("6. Enter incorrect email address and password"):
        login.fill_login_form(wrong_email, wrong_password)
        take_screenshot(page, "Filled Incorrect Login Form")

    with allure.step("7. Click 'Login' button"):
        login.login_button.click()
        allure.attach(page.screenshot(), name="Login Click", attachment_type=allure.attachment_type.PNG)

    with allure.step("8. Verify error 'Your email or password is incorrect!' is visible"):
        expect(login.login_form_msg).to_be_visible()
        expect(login.login_form_msg).to_have_text("Your email or password is incorrect!")
        take_screenshot(page, "Login Error Message")

    page.close()








# from pages.home_page import HomePage
# from pages.login_page import LoginPage
# from playwright.sync_api import expect
# from faker import Faker
# from utils.take_screenshot import take_screenshot

# fake = Faker()

# def test_login_with_incorrect_credentials(base_url, browser):
#     page = browser.new_page()
#     home = HomePage(page, base_url)
#     login = LoginPage(page)

#     wrong_email = fake.email()
#     wrong_password = fake.password()

#     # 1-2. Navigate to correct url
#     home.navigate()

#     # 3. Verify that home page is visible successfully
#     assert home.is_home_page_visible()

#     # 4. Click on 'Signup / Login' button
#     home.click_signup_login()

#     # 5. Verify 'Login to your account' is visible
#     expect(login.login_form_title).to_contain_text("Login to your account")

#     # 6. Enter incorrect email address and password
#     login.fill_login_form(wrong_email, wrong_password)

#     # 7. Click 'login' button
#     login.login_button.click()

#     # 8. Verify error 'Your email or password is incorrect!' is visible
#     expect(login.login_form_msg).to_be_visible()
#     expect(login.login_form_msg).to_have_text("Your email or password is incorrect!")
#     take_screenshot(page, "Your email or password is incorrect!")  

#     page.close()