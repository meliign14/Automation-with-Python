# Automation-with-Python
# 🏦 Homebanking framework
Scalable Web Automation Framework built with Python. Features: Pytest fixtures, Selenium WebDriver, Page Object Model, and custom HTML reports.
## 🚀 Tech Stack
*   **Language:** Python 3.14.0
*   **Test Framework:** Pytest 9.0.2
*   **Automation Tool:** Selenium WebDriver 4.40.0
*   **Driver Management:** Webdriver Manager (Chrome) 4.0.2
*   **CI/CD Ready:** Headless mode configured for GitHub Actions
*   **Reports:** Pytest html 4.2.0
## 🏗️ Architecture (Page Object Model)
The project is structured as follows:
- `pages/`: Page classes (BasePage, LoginPage, etc.) containing interaction logic.
- `locators/`: Centralized selectors (By.ID, By.XPATH) for easy maintenance.
- `tests/`: Test cases organized by feature.
- `data/`: JSON files for test data driven testing (Parameterized tests).
- `conftest.py`: Global fixtures, driver setup, and session management.
## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com
   cd your-repo
2. Create and activate a virtual enviroment:
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
