from pages.home_page import HomePage
from pages.login_page import LoginPage
from playwright.sync_api import expect
from faker import Faker

fake = Faker()

def test_login_with_incorrect_credentials(base_url, browser):
    page = browser.new_page()
    home = HomePage(page, base_url)
    login = LoginPage(page)

    wrong_email = fake.email()
    wrong_password = fake.password()

    # 1-2. Navigate to correct url
    home.navigate()

    # 3. Verify that home page is visible successfully
    assert home.is_home_page_visible()

    # 4. Click on 'Signup / Login' button
    home.click_signup_login()

    # 5. Verify 'Login to your account' is visible
    expect(login.login_form_title).to_contain_text("Login to your account")

    # 6. Enter incorrect email address and password
    login.fill_login_form(wrong_email, wrong_password)

    # 7. Click 'login' button
    login.login_button.click()

    # 8. Verify error 'Your email or password is incorrect!' is visible
    expect(login.login_form_msg).to_be_visible()
    expect(login.login_form_msg).to_have_text("Your email or password is incorrect!")

    page.close()