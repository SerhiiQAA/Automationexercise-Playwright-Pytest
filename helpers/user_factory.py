from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from faker import Faker

fake = Faker()

def create_test_user(page, base_url):
    name = fake.first_name()
    email = fake.email()
    password = fake.password()

    home = HomePage(page, base_url)
    login = LoginPage(page)
    register = RegisterPage(page)

    home.navigate()
    home.click_signup_login()
    login.fill_signup_form(name, email)
    login.signup_button.click()
    register.fill_account_info(password, 1, 1, 2000)
    register.fill_address(name, fake.last_name(), fake.company(), fake.street_address(), fake.secondary_address(),
                          "Canada", fake.state(), fake.city(), fake.zipcode(), fake.phone_number())
    register.create_account_btn.click()
    register.continue_btn.click()

    return {
        "name": name,
        "email": email,
        "password": password,
        "page": page
    }
