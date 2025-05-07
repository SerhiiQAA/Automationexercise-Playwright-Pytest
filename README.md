# Playwright-Pytest Automation Exercise

This project uses Playwright and Pytest for automating tests on the web application **automationexercise.com**.

## 📄Description

This project automates testing for a web application using **Playwright** to control the browser and **Pytest** to execute tests.  
Tests can be run in headless mode using Python and Playwright, and results can be generated in both **HTML format** (for local viewing) and **Allure Report** (for more detailed insights).  
Additionally, this project includes integration with **Slack** to receive notifications about CI test results.


## ⚙️Installation

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

## 🚀Running Tests
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

## 🏃‍♂️Continuous Integration (CI) and Slack Notifications

This project uses GitHub Actions to run tests automatically on every push or pull request to the master branch.
After each CI run, a notification is sent to a configured Slack channel with the status of the run (success or failure) and a link to the published Allure report via GitHub Pages.

To configure Slack integration:

1. Create a Slack App and enable Incoming Webhooks.
2. Add a webhook URL to your Slack channel.
3. Save the webhook URL as a GitHub Actions Secret with the name ACTION_MONITORING_SLACK.

The Slack message includes:

- Repository name
- Workflow and job name
- Test status (✅ success / ❌ failure)
- Run number
- Link to the latest published Allure report

## 📝License

This project is licensed under the ISC License.