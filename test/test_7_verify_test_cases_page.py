from pages.home_page import HomePage
from pages.test_cases_page import TCPage
from playwright.sync_api import expect
from utils.take_screenshot import take_screenshot

def test_verify_test_cases_page(base_url, browser):
    page = browser.new_page()
    home = HomePage(page, base_url)
    test_cases = TCPage(page)

    # 1-2. Navigate to correct url
    home.navigate()

    # 3. Verify that home page is visible successfully
    assert home.is_home_page_visible()

    # 4. Click on 'Test Cases' button
    home.click_test_cases()

    # 5. Verify user is navigated to test cases page successfully
    assert test_cases.url_contains("/test_cases")
    expect(test_cases.title).to_contain_text("Test Cases")
    take_screenshot(page, "Test Cases")

    page.close()