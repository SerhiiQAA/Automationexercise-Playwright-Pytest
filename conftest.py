import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://automationexercise.com"
HEADLESS = True

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        yield browser
        browser.close()


# import pytest
# from playwright.sync_api import sync_playwright

# # Значення за замовчуванням
# DEFAULT_BASE_URL = "https://automationexercise.com"
# DEFAULT_HEADLESS = True
# DEFAULT_BROWSER = "chromium"

# # Додаємо параметри командного рядка для вибору браузера та базової URL-адреси
# def pytest_addoption(parser):
#     parser.addoption(
#         "--test-browser", action="store", default=DEFAULT_BROWSER, help="Choose browser: chromium, firefox, webkit"
#     )
#     parser.addoption(
#         "--base-url", action="store", default=DEFAULT_BASE_URL, help="Base URL for tests"
#     )
#     parser.addoption(
#         "--headless", action="store_true", default=DEFAULT_HEADLESS, help="Run tests in headless mode"
#     )

# # Фікстура для базового URL
# @pytest.fixture(scope="session")
# def base_url(request):
#     return request.config.getoption("--base-url")

# # Фікстура для браузера
# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("--test-browser")
#     headless = request.config.getoption("--headless")
    
#     with sync_playwright() as p:
#         if browser_name == "firefox":
#             browser = p.firefox.launch(headless=headless)
#         elif browser_name == "webkit":
#             browser = p.webkit.launch(headless=headless)
#         else:
#             browser = p.chromium.launch(headless=headless)  # За замовчуванням Chromium
#         yield browser
#         browser.close()




