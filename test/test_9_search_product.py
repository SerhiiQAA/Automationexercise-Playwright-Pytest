import allure
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from playwright.sync_api import expect
from utils.take_screenshot import take_screenshot

@allure.title("Search Product Test")
@allure.description("Test for searching a product and verifying the results")
def test_search_product(base_url, browser):
    page = browser.new_page()
    home = HomePage(page, base_url)
    products = ProductsPage(page)

    with allure.step("1-2. Navigate to the home page"):
        home.navigate()
        take_screenshot(page, "Navigated to Home Page")

    with allure.step("3. Verify that the home page is visible"):
        assert home.is_home_page_visible()
        take_screenshot(page, "Home Page Visible")

    with allure.step("4. Click 'Products' button"):
        home.click_products()
        allure.attach(page.screenshot(), name="Click Products", attachment_type=allure.attachment_type.PNG)

    with allure.step("5. Verify user is navigated to ALL PRODUCTS page"):
        assert products.url_contains("/products")
        expect(products.searched_products_title).to_contain_text("All Products")
        take_screenshot(page, "All Products Page Visible")

    with allure.step("6. Enter product name 'jeans' in search input and click search button"):
        products.search_input.fill("jeans")
        products.search_button.click()
        take_screenshot(page, "Product Search Input")

    with allure.step("7. Verify 'SEARCHED PRODUCTS' title is visible"):
        expect(products.searched_products_title).to_contain_text("Searched Products")
        take_screenshot(page, "Search Results Visible")

    with allure.step("8. Verify all products related to the search term 'jeans' are visible"):
        search_term = "jeans"
        items = products.searched_product_items.all_text_contents()
        assert all("jeans" in item.lower() for item in items)
        take_screenshot(page, "Search Results Verified")

    page.close()




# from pages.home_page import HomePage
# from pages.products_page import ProductsPage
# from playwright.sync_api import expect
# from utils.take_screenshot import take_screenshot

# def test_search_product(base_url, browser):
#     page = browser.new_page()
#     home = HomePage(page, base_url)
#     products = ProductsPage(page)

#     # 1-2. Navigate to correct url
#     home.navigate()

#     # 3. Verify that home page is visible successfully
#     assert home.is_home_page_visible() 
    
#     # 4. Click on 'Products' button
#     home.click_products()

#     # 5. Verify user is navigated to ALL PRODUCTS page successfully
#     assert products.url_contains("/products")
#     expect(products.searched_products_title).to_contain_text("All Products")

#     # 6. Enter product name in search input and click search button
#     products.search_input.fill("jeans")
#     products.search_button.click()

#     # 7. Verify 'SEARCHED PRODUCTS' is visible
#     expect(products.searched_products_title).to_contain_text("Searched Products")

#     # 8. Verify all the products related to search are visible
#     search_term = "jeans"
#     items = products.searched_product_items.all_text_contents()
#     assert all("jeans" in item.lower() for item in products.searched_product_items.all_text_contents())
#     take_screenshot(page, "Before Creating Account")
    
#     page.close()