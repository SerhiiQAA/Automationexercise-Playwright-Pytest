from pages.home_page import HomePage
from playwright.sync_api import expect
from faker import Faker
from utils.take_screenshot import take_screenshot

def test_verify_subscription_home_page(base_url, browser):
    fake = Faker()
    page = browser.new_page()
    home = HomePage(page, base_url)

    # 1-2. Navigate to correct url
    home.navigate()

    # 3. Verify that home page is visible successfully
    assert home.is_home_page_visible()

    # 4. Scroll down to footer
    home.subscription_title.scroll_into_view_if_needed()

    # 5. Verify text 'SUBSCRIPTION'
    expect(home.subscription_title).to_contain_text("Subscription")

    # 6. Enter email address in input and click arrow button
    test_email = fake.email()
    home.email_input_field.fill(test_email)
    home.subscribe_button.click()

    # 7. Verify success message 'You have been successfully subscribed!' is visible
    expect(home.subscription_success_message).to_contain_text("You have been successfully subscribed!")
    take_screenshot(page, "You have been successfully subscribed!")

    page.close()