from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjectModel.src.base.BaseSetup import wait_until_visible

class LoginPage:
    def __init__(self, driver):
        """
        Initializes the LoginPage object with the driver and locators.
        
        Args:
            driver (WebDriver): The Selenium WebDriver instance.
        """
        self.driver = driver
        self.language_dropdown  = By.XPATH, "//*[@data-testid='language-dropdown']"
        self.language_option    = None
        self.login_account_type = None
        self.username_field     = By.XPATH, "//*[@data-testid='login-user-id']"
        self.password_field     = By.XPATH, "//*[@data-testid='login-password']"
        self.login_button       = By.XPATH, "//*[@data-testid='login-submit']"
        self.dashboard_iframe   = By.XPATH, "//iframe[@class='sc-ue54fd-1 kjwoRv']"
        self.dashboard          = By.XPATH, "//*[@id='chart-root']"

    def set_language(self, language):
        self.language_option = By.XPATH, f"//*[@data-testid='language-option' and text()='{language}']"

    def set_login_account_type(self, acc_type):
        self.login_account_type = By.XPATH, f"//*[@data-testid='login-account-type']//div[text()='{acc_type}']"

    def navigate_to_login_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def select_language(self, language):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.language_dropdown))
        self.driver.find_element(*self.language_dropdown).click()
        self.set_language(language)
        self.driver.find_element(*self.language_option).click()

    def select_login_type(self, account_type):
        self.set_login_account_type(account_type)
        self.driver.find_element(*self.login_account_type).click()

    def input_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def input_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def verify_dashboard(self):
        #Verifies that the dashboard is displayed after login.
        wait_until_visible(self.driver, 20, self.dashboard_iframe)
        iframe = self.driver.find_element(*self.dashboard_iframe)
        self.driver.switch_to.frame(iframe)
        wait_until_visible(self.driver, 10, self.dashboard)
        dashboard = self.driver.find_element(*self.dashboard)
        
        if not dashboard.is_displayed():
            raise RuntimeError("Login failed: Dashboard not found")
        
        # Switch back to the main document
        self.driver.switch_to.default_content()



    def login(self, language, login_type, username, password):
        #Performs the login process with the given credentials.
        try:
            # Perform login steps
            self.select_language(language)
            self.select_login_type(login_type)
            self.input_username(username)
            self.input_password(password)
            self.click_login()
            self.verify_dashboard()
            print("Login successful")
        except Exception as e:
            raise RuntimeError(f"Login failed: {e}")
