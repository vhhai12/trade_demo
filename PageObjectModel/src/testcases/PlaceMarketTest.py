import sys
sys.path.append(".")  # Add the project root to the system path
import unittest
import time

from PageObjectModel.src.pages.LoginPage import LoginPage
from PageObjectModel.src.pages.WebTraderPage import WebTraderPage
from PageObjectModel.src.base.BaseSetup import setup_driver

# Constants
LOGIN_URL = "https://aqxtrader.aquariux.com"
USERNAME = "2091000906"
PASSWORD = "dCz0qw$v0A$K"
LANGUAGE = "English"
ACCOUNT_TYPE = "Demo Account"

class PlaceMarketTest(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment before each test case.
        Initialize the driver and page objects and perform login.
        """
        self.driver = setup_driver(browser="edge")
        self.login_page = LoginPage(self.driver)
        self.web_trader_page = WebTraderPage(self.driver)
        
        # Navigate to login page and perform login
        self.login_page.navigate_to_login_page(LOGIN_URL)
        self.login_page.login(LANGUAGE, ACCOUNT_TYPE, USERNAME, PASSWORD)
    
    def tearDown(self):
        """
        Clean up after each test case by quitting the driver.
        """
        time.sleep(3)
        self.driver.quit()
    
    def test_trade_page(self):
        """
        Test Case 1: Test Trade page
        """
        MARKET_SECTION = "trade"
        MARKET_CATEGORY_UP_LEVEL = "All"
        MARKET_CATEGORY_LOW_LEVEL = "Crypto"
        COIN = "BTCUSD.std"
        TAB = "Trade"
        TRADE_ORDER = "buy"
        TRADE_ORDER_TYPE = "Market"
        
        try:
            # Select the trading option in the sidebar
            self.web_trader_page.select_option(MARKET_SECTION)
            
            # Select market category
            self.web_trader_page.select_market(MARKET_CATEGORY_UP_LEVEL)
            self.web_trader_page.select_market(MARKET_CATEGORY_LOW_LEVEL)
            
            # Select a specific coin
            self.web_trader_page.select_coin(COIN)
            
            # Place Market with Stop Loss and Take Profit
            self.web_trader_page.select_Trade_or_Specification_tab(TAB)
            self.web_trader_page.select_trade_order(TRADE_ORDER)
            self.web_trader_page.select_trade_order_type(TRADE_ORDER_TYPE)
            self.web_trader_page.input_trade_unit(10)
            LIVE_BUY_PRICE = self.web_trader_page.get_trade_live_buy_price()
            STOP_LOSS_PRICE = LIVE_BUY_PRICE*0.98
            TAKE_PROFIT_PRICE = LIVE_BUY_PRICE*1.02
            self.web_trader_page.input_stop_loss_price(STOP_LOSS_PRICE)
            self.web_trader_page.input_take_profit_price(TAKE_PROFIT_PRICE)
            self.web_trader_page.place_trade_order()
            
            # Validate the order placed details with compare to notifications and position table details
            #self.web_trader_page.validate_the_order_placed_details_with_compare_to_notifications_and_position_table_details("1")
            
            # Edit Open Positions
            self.web_trader_page.edit_open_positions(LIVE_BUY_PRICE - 1100, LIVE_BUY_PRICE + 1100)
            
            # Partial Close Open Positions
            self.web_trader_page.partial_close_open_positions(8)
            
            # Close Open Positions
            self.web_trader_page.close_open_positions()
            
            # Place Limit / Stop order with different types of Expiry
            self.web_trader_page.select_Trade_or_Specification_tab(TAB)
            self.web_trader_page.select_trade_order(TRADE_ORDER)
            self.web_trader_page.select_trade_order_type("Limit")
            self.web_trader_page.input_trade_unit(10)
            LIVE_BUY_PRICE = self.web_trader_page.get_trade_live_buy_price()
            self.web_trader_page.input_limit_price(LIVE_BUY_PRICE*0.99)
            self.web_trader_page.input_stop_loss_price(LIVE_BUY_PRICE*0.98)
            self.web_trader_page.input_take_profit_price(LIVE_BUY_PRICE*1.02)
            self.web_trader_page.select_expiry_type("Good Till Cancelled")
            self.web_trader_page.place_trade_order()
            
            # Able to edit Pending Orders for all values included
            self.web_trader_page.edit_pending_orders(LIVE_BUY_PRICE*0.998, LIVE_BUY_PRICE*0.988, LIVE_BUY_PRICE*1.021, "Good till day")
            
        except Exception as e:
            self.fail(f"Test Case Failed: {e}")
        print("Test Case 1: Test Trade page: passed")
    
if __name__ == "__main__":
    unittest.main()
