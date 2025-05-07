from helpers.user_factory import create_test_user
from pages.home_page import HomePage
from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_login_user_and_logout(base_url, browser):
    page = browser.new_page()
    user = create_test_user(page, base_url)

    home = HomePage(page, base_url)
    login = LoginPage(page)

    # 1-2. Logout
    login.logout_btn.click()

    # 3. Verify that home page is visible successfully
    assert home.is_home_page_visible()

    # 4. Click on 'Signup / Login' button
    home.click_signup_login()

    # 5. Verify 'Login to your account' is visible
    expect(login.login_form_title).to_contain_text("Login to your account")

    # 6. Enter correct email address and password
    login.fill_login_form(user["email"], user["password"])

    # 7. Click 'login' button
    login.login_button.click()

    # 8. Verify that 'Logged in as username' is visible
    expect(login.logged_in_as).to_be_visible()
    expect(login.logged_in_as).to_contain_text(user["name"])

    # 9. Click 'Logout' button
    login.logout_btn.click()

    # 10. Verify that user is navigated to login page
    expect(login.login_form_title).to_contain_text("Login to your account")

    page.close()




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

#     # 5. Verify 'Login to your account' is visible
#     expect(login.login_form_title).to_contain_text("Login to your account")

#     # 6. Enter correct email address and password
#     login.fill_login_form(email, password)

#     # 7. Click 'login' button
#     login.login_button.click()

#     # 8. Verify that 'Logged in as username' is visible
#     expect(login.logged_in_as).to_be_visible()
#     expect(login.logged_in_as).to_contain_text(name)

#     # 9. Click 'Logout' button
#     login.logout_btn.click()  # Click on 'Logout' button

#     # 10. Verify that user is navigated to login page
#     expect(login.login_form_title).to_contain_text("Login to your account")

#     page.close()