# Playwright-Pytest Automation Exercise

This project uses Playwright and Pytest for automating tests on the web application **automationexercise.com**.

## Description

This project automates testing for a web application using **Playwright** to control the browser and **Pytest** to execute tests. Tests can be run in headless mode using Python and Playwright, and results can be generated in both **HTML** format (for local viewing) and **Allure Report** (for more detailed insights).

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/playwright-pytest-automationexercise.git
   cd playwright-pytest-automationexercise

2. Create a virtual environment (recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # for MacOS/Linux
    venv\Scripts\activate     # for Windows

3. Install dependencies::
    ```bash
    pip install -r requirements.txt

## Running Tests
- Running tests in headless mode:
    ```bash
    npm run test

- Running tests with Allure Report:
    ```bash
    npm run test_allure

- Generating Allure Report:
    ```bash
    npm run report_allure

- Serving Allure Report Locally:
    ```bash
    npm run serve_allure

- Running tests in headless mode with report (running tests in headless mode with a simple HTML report locally):
    ```bash
    npm run test_report

## License

This project is licensed under the ISC License.