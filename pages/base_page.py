class BasePage:
    def __init__(self, page):
        self.page = page

    def url_contains(self, partial_url: str) -> bool:
        return partial_url in self.page.url