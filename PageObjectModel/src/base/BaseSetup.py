import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import expected_conditions as EC

def setup_driver(browser="chrome"):
    if browser.lower() == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser.lower() == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        raise ValueError("Unsupported browser. Please choose 'chrome', 'firefox', or 'edge'.")
    return driver

def wait_until_visible(driver, wait_seconds, locator):
    try:
        WebDriverWait(driver, wait_seconds).until(EC.presence_of_element_located(locator))
    except Exception as e:
        raise RuntimeError(f"Element not visible after {wait_seconds} seconds: {e}")

logging.basicConfig(
    level=logging.DEBUG,  # This sets the log level (e.g., DEBUG, INFO)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Format of the log message
    handlers=[
        logging.FileHandler('selenium_logs.log'),  # Save logs to a file
        logging.StreamHandler()  # Also print to the console
    ]
)