from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.language_dropdown  = By.XPATH, "//*[@data-testid='language-dropdown']"
        self.language_option    = None
        self.login_account_type = None
        self.username_field     = By.XPATH, "//*[@data-testid='login-user-id']"
        self.password_field     = By.XPATH, "//*[@data-testid='login-password']"
        self.login_button       = By.XPATH, "//*[@data-testid='login-submit']"
        self.dashboard          = By.XPATH, "//*[@id='root']//div[@class='sc-j0b7z7-0 jnzLKP']"
    
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
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.dashboard))
        dashboard = self.driver.find_element(*self.dashboard)
        assert dashboard.is_displayed(), "Login failed: Dashboard not found"
