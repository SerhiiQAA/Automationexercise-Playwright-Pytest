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