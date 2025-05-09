import allure
from pages.home_page import HomePage
from playwright.sync_api import expect
from faker import Faker
from utils.take_screenshot import take_screenshot

@allure.title("Verify Subscription on Home Page")
@allure.description("Test to verify subscription functionality on the home page")
def test_verify_subscription_home_page(base_url, browser):
    fake = Faker()
    page = browser.new_page()
    home = HomePage(page, base_url)

    with allure.step("1-2. Navigate to the home page"):
        home.navigate()
        take_screenshot(page, "Navigated to Home Page")

    with allure.step("3. Verify that the home page is visible"):
        assert home.is_home_page_visible()
        take_screenshot(page, "Home Page Visible")

    with allure.step("4. Scroll down to footer"):
        home.subscription_title.scroll_into_view_if_needed()
        take_screenshot(page, "Scrolled to Footer")

    with allure.step("5. Verify text 'SUBSCRIPTION' is visible"):
        expect(home.subscription_title).to_contain_text("Subscription")
        take_screenshot(page, "Subscription Title Verified")

    with allure.step("6. Enter email address and click subscription button"):
        test_email = fake.email()
        home.email_input_field.fill(test_email)
        home.subscribe_button.click()
        take_screenshot(page, "Entered Email and Clicked Subscribe")

    with allure.step("7. Verify success message 'You have been successfully subscribed!' is visible"):
        expect(home.subscription_success_message).to_contain_text("You have been successfully subscribed!")
        take_screenshot(page, "Subscription Success Message")

    page.close()