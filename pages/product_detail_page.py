from pages.base_page import BasePage
from playwright.sync_api import expect

class ProductDetailPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.product_name = page.locator(".product-information h2")
        self.category = page.locator(".product-information > p:nth-child(3)")
        self.price = page.locator(".product-information > span:nth-child(5) > span")
        self.availability = page.locator(".product-information > p:nth-child(6)")
        self.condition = page.locator(".product-information > p:nth-child(7)")
        self.brand = page.locator(".product-information > p:nth-child(8)")

    def check_elements_visible(self, elements):
        for locator in elements:
            expect(locator).to_be_visible()