from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.products_list = page.locator(".features_items")
        self.product_card = page.locator(".single-products")
        self.view_first_product_button = page.locator('a[href="/product_details/1"]')
        self.search_input = page.locator("input#search_product")
        self.search_button = page.locator("button#submit_search")
        self.searched_products_title = page.locator("h2.title.text-center")
        self.searched_product_items = page.locator(".single-products .productinfo p")