import allure
from pages.home_page import HomePage
from pages.test_cases_page import TCPage
from playwright.sync_api import expect
from utils.take_screenshot import take_screenshot

@allure.title("Verify Test Cases Page")
@allure.description("Test to verify navigation to the test cases page")
def test_verify_test_cases_page(base_url, browser):
    page = browser.new_page()
    home = HomePage(page, base_url)
    test_cases = TCPage(page)

    with allure.step("1-2. Navigate to the correct URL"):
        home.navigate()
        take_screenshot(page, "Navigated to Home Page")

    with allure.step("3. Verify that the home page is visible"):
        assert home.is_home_page_visible()
        take_screenshot(page, "Home Page Visible")

    with allure.step("4. Click 'Test Cases' button"):
        home.click_test_cases()
        allure.attach(page.screenshot(), name="Click Test Cases", attachment_type=allure.attachment_type.PNG)

    with allure.step("5. Verify user is navigated to the test cases page"):
        assert test_cases.url_contains("/test_cases")
        expect(test_cases.title).to_contain_text("Test Cases")
        take_screenshot(page, "Test Cases Page Visible")

    page.close()




# from pages.home_page import HomePage
# from pages.test_cases_page import TCPage
# from playwright.sync_api import expect
# from utils.take_screenshot import take_screenshot

# def test_verify_test_cases_page(base_url, browser):
#     page = browser.new_page()
#     home = HomePage(page, base_url)
#     test_cases = TCPage(page)

#     # 1-2. Navigate to correct url
#     home.navigate()

#     # 3. Verify that home page is visible successfully
#     assert home.is_home_page_visible()

#     # 4. Click on 'Test Cases' button
#     home.click_test_cases()

#     # 5. Verify user is navigated to test cases page successfully
#     assert test_cases.url_contains("/test_cases")
#     expect(test_cases.title).to_contain_text("Test Cases")
#     take_screenshot(page, "Test Cases")

#     page.close()