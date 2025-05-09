import allure
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage
from playwright.sync_api import expect
from utils.take_screenshot import take_screenshot

@allure.title("Verify All Products and Product Detail Page")
@allure.description("Test to verify navigation to the products page and detailed product view")
def test_verify_all_products_and_product_detail_page(base_url, browser):
    page = browser.new_page()
    home = HomePage(page, base_url)
    products = ProductsPage(page)
    product_detail = ProductDetailPage(page)

    with allure.step("1-2. Navigate to the home page"):
        home.navigate()
        take_screenshot(page, "Navigated to Home Page")

    with allure.step("3. Verify that the home page is visible"):
        assert home.is_home_page_visible()
        take_screenshot(page, "Home Page Visible")

    with allure.step("4. Click 'Products' button"):
        home.products_button.click()
        allure.attach(page.screenshot(), name="Click Products", attachment_type=allure.attachment_type.PNG)

    with allure.step("5. Verify user is navigated to ALL PRODUCTS page successfully"):
        assert products.url_contains("/products")
        take_screenshot(page, "All Products Page Visible")

    with allure.step("6. Verify that the products list is visible"):
        expect(products.products_list).to_be_visible()
        assert products.product_card.count() > 1
        take_screenshot(page, "Products List Visible")

    with allure.step("7. Click 'View Product' of the first product"):
        products.view_first_product_button.click()
        allure.attach(page.screenshot(), name="View First Product Click", attachment_type=allure.attachment_type.PNG)

    with allure.step("8. Verify user is navigated to the product detail page"):
        assert products.url_contains("/product_details")
        take_screenshot(page, "Product Detail Page Visible")

    with allure.step("9. Verify product details are visible: name, category, price, availability, condition, brand"):
        product_detail.check_elements_visible([
            product_detail.product_name,
            product_detail.category,
            product_detail.price,
            product_detail.availability,
            product_detail.condition,
            product_detail.brand
        ])
        take_screenshot(page, "Product Details Verified")

    page.close()





# from pages.home_page import HomePage
# from pages.products_page import ProductsPage
# from pages.product_detail_page import ProductDetailPage
# from playwright.sync_api import expect
# from utils.take_screenshot import take_screenshot

# def test_verify_all_products_and_product_detail_page(base_url, browser):
#     page = browser.new_page()
#     home = HomePage(page, base_url)
#     products = ProductsPage(page)
#     product_detail = ProductDetailPage(page)

#     # 1-2. Navigate to correct url
#     home.navigate()

#     # 3. Verify that home page is visible successfully
#     assert home.is_home_page_visible()

#     # 4. Click on 'Products' button
#     home.products_button.click()

#     # 5. Verify user is navigated to ALL PRODUCTS page successfully
#     assert products.url_contains("/products")

#     # 6. The products list is visible
#     expect(products.products_list).to_be_visible()
#     assert products.product_card.count() > 1

#     # 7. Click on 'View Product' of first product
#     products.view_first_product_button.click()

#     # 8. User is landed to product detail page
#     assert products.url_contains("/product_details")
    
#     # 9. Verify that detail detail is visible: product name, category, price, availability, condition, brand
#     product_detail.check_elements_visible([
#         product_detail.product_name,
#         product_detail.category,
#         product_detail.price,
#         product_detail.availability,
#         product_detail.condition,
#         product_detail.brand
#     ])
#     take_screenshot(page, "Verify that detail detail is visible")

#     page.close()