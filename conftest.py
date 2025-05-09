import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://automationexercise.com"
HEADLESS = True

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

def pytest_addoption(parser):
    """Додаємо CLI параметр для вибору браузера (playwright_browser)"""
    parser.addoption("--playwright_browser", action="store", default="chromium", help="Choose browser: chromium, firefox, webkit")

@pytest.fixture(scope="function")
def browser(pytestconfig):
    """Запускаємо обраний браузер на основі CLI аргументу"""
    browser_name = pytestconfig.getoption("playwright_browser")

    with sync_playwright() as p:
        browser = p[browser_name].launch(headless=HEADLESS)
        yield browser
        browser.close()







# import pytest
# from playwright.sync_api import sync_playwright

# BASE_URL = "https://automationexercise.com"
# HEADLESS = True

# @pytest.fixture(scope="session")
# def base_url():
#     return BASE_URL

# @pytest.fixture(scope="function")
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=HEADLESS)
#         yield browser
#         browser.close()