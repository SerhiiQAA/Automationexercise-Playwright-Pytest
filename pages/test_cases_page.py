from pages.base_page import BasePage

class TCPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.title = page.locator("h2.title.text-center b")
