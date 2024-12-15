import time
from selenium.webdriver.common.by import By
from PageObjectModel.src.base.BaseSetup import *

class WebTraderPage:
    def __init__(self, driver):
        self.driver = driver
        self.option = None
        self.market = None
        self.coin = None
        self.tab = None
        self.trade_order = None
        self.notification_list_result_item = None
        self.trade_order_type_dropdown  = By.XPATH, "//*[@data-testid='trade-dropdown-order-type']"
        self.trade_order_type           = None
        self.trade_units_input          = By.XPATH, "//*[@data-testid='trade-input-volume']"
        self.trade_live_buy_price       = By.XPATH, "//*[@data-testid='trade-live-buy-price']"
        self.stop_loss_input            = By.XPATH, "//*[@data-testid='trade-input-stoploss-price']"
        self.take_profit_input          = By.XPATH, "//*[@data-testid='trade-input-takeprofit-price']"
        self.place_order_btn            = By.XPATH, "//*[@data-testid='trade-button-order']"
        
        self.trade_confirmation_modal   = By.XPATH, "//*[@data-testid='trade-confirmation-modal']"
        self.trade_confirmation_btn     = By.XPATH, "//*[@data-testid='trade-confirmation-button-confirm']"
        
        self.tab_asset_order_type_open_positions = By.XPATH, "//*[@data-testid='tab-asset-order-type-open-positions']"
        self.tab_asset_order_type_pending_orders = By.XPATH, "//*[@data-testid='tab-asset-order-type-pending-orders']"
        self.tab_asset_order_type_history        = By.XPATH, "//*[@data-testid='tab-asset-order-type-history']"
        
        self.asset_open_button_track     = By.XPATH, "//*[@data-testid='asset-open-button-track']"
        self.asset_open_button_edit      = By.XPATH, "//*[@data-testid='asset-open-button-edit']"
        self.edit_input_price            = By.XPATH, "//*[@data-testid='edit-input-price']"
        self.edit_input_stoploss_price   = By.XPATH, "//*[@data-testid='edit-input-stoploss-price']"
        self.edit_input_takeprofit_price = By.XPATH, "//*[@data-testid='edit-input-takeprofit-price']"
        self.edit_confirmation_modal     = By.XPATH, "//*[@data-testid='edit-confirmation-modal']"
        self.edit_button_order           = By.XPATH, "//*[@data-testid='edit-button-order']"
        
        self.asset_open_button_close            = By.XPATH, "(//*[@data-testid='asset-open-button-close'])[1]"
        self.confirm_close_order_modal          = By.XPATH, "//*[@class='sc-ur24yu-1 eqxJBS']"
        self.close_order_input_volume           = By.XPATH, "//*[@data-testid='close-order-input-volume']" 
        self.close_order_input_volume_decrease  = By.XPATH, "//*[@data-testid='close-order-input-volume-decrease']" 
        self.close_order_button_cancel          = By.XPATH, "//*[@data-testid='close-order-button-cancel']" 
        self.close_order_button_submit          = By.XPATH, "//*[@data-testid='close-order-button-submit']" 
        
        self.limit_trade_input_price         = By.XPATH, "//*[@data-testid='trade-input-price']" 
        self.limit_expiry_dropdown = By.XPATH, "//*[@data-testid='trade-dropdown-expiry']" 
        self.limit_expiry_good_till_cancelled = By.XPATH, "//*[@data-testid='trade-dropdown-expiry-good-till-cancelled']"
        self.limit_expiry_good_till_day = By.XPATH, "//*[@data-testid='trade-dropdown-expiry-good-till-day']"
        
        self.asset_pending_button_edit      = By.XPATH, "//*[@data-testid='asset-pending-button-edit']"
        self.tab_asset_order_type_open_positions = By.XPATH, "//*[@data-testid='tab-asset-order-type-open-positions']"
        self.tab_asset_order_type_pending_orders = By.XPATH, "//*[@data-testid='tab-asset-order-type-pending-orders']"
        
        
        #Notification
        self.notification_description       = By.XPATH, "//*[@data-testid='notification-description']"
        self.notification_close_btn         = By.XPATH, "//*[@data-testid='notification-close-button']"
        self.notification_selector          = By.XPATH, "//*[@data-testid='notification-selector']"
        self.notification_list_result       = By.XPATH, "//*[@data-testid='notification-list-result']"
        self.notification_list_result_item  = By.XPATH, "//*[@data-testid='notification-list-result-item']"
        
        #Order detail
        self.order_detail_modal         = By.XPATH, "//*[@data-testid='notification-order-details-modal']"
        self.order_detail_symbol        = By.XPATH, "(//*[@data-testid='notification-order-details-value'])[1]"
        self.order_detail_order_no      = By.XPATH, "(//*[@data-testid='notification-order-details-value'])[3]"
        self.order_detail_size          = By.XPATH, "(//*[@data-testid='notification-order-details-value'])[4]"
        self.order_detail_unit          = By.XPATH, "(//*[@data-testid='notification-order-details-value'])[5]"
        self.order_detail_entry_price   = By.XPATH, "(//*[@data-testid='notification-order-details-value'])[6]"
        self.order_detail_close_btn     = By.XPATH, "//*[@data-testid='notification-order-details-modal-close']"
        
    def set_option(self, _option):
        #Sets the locator for a specific sidebar option.
        self.option = By.XPATH, f"//*[@data-testid='side-bar-option-{_option}']"

    def set_market(self, _market):
        #Sets the locator for a specific market.
        self.market = By.XPATH, f"//*[contains(@class,'sc-1jd986s-0 iqiCBC') and text()='{_market}']"

    def set_coin(self, _coin):
        #Sets the locator for a specific coin.
        self.coin = By.XPATH, f"//*[@class='sc-iubs14-5 fFEJmt' and text()='{_coin}']"
    
    def set_tab(self, _tab_name):
        #Sets the locator for a specific coin.
        self.tab = By.XPATH, f"//*[contains(@class,'sc-1jd986s-0 iqiCBC') and text()='{_tab_name}']"

    def set_trade_order(self, _order):
        #Sets the locator for a specific coin.
        self.trade_order = By.XPATH, f"//*[@data-testid='trade-button-order-{_order}']"
        
    def set_trade_order_type(self, _order_type):
        #Sets the locator for a specific coin.
        self.trade_order_type = By.XPATH, f"//*[@data-testid='trade-dropdown-order-type-{_order_type}']"
    
    def set_notification_list_result_item(self, _num_order):
        #Sets the locator for a specific coin.
        self.notification_list_result_item = By.XPATH, f"(//*[@data-testid='notification-list-result-item'])[{_num_order}]"

    def select_option(self, option):
        #Selects the specified sidebar option.
        self.set_option(option.lower())
        try:
            wait_until_visible(self.driver, 10, self.option)
            self.driver.find_element(*self.option).click()
        except Exception as e:
            raise RuntimeError(f"Failed to select sidebar option '{option}': {e}")

    def select_market(self, market):
        #Selects the specified market.
        market = market.capitalize()
        self.set_market(market)
        try:
            wait_until_visible(self.driver, 10, self.market)
            self.driver.find_element(*self.market).click()
        except Exception as e:
            raise RuntimeError(f"Failed to select market '{market}': {e}")

    def select_coin(self, coin):
        #Selects the specified coin.
        self.set_coin(coin)
        try:
            wait_until_visible(self.driver, 10, self.coin)
            self.driver.find_element(*self.coin).click()
        except Exception as e:
            raise RuntimeError(f"Failed to select coin '{coin}': {e}")

    def select_Trade_or_Specification_tab(self, tab_name):
        tab_name = tab_name.capitalize()
        self.set_tab(tab_name)
        try:
            self.driver.find_element(*self.tab).click()
        except Exception as e:
            raise RuntimeError(f"Failed to select tab '{tab_name}': {e}")
    
    def select_trade_order(self, order):
        #Selects the specified trade order.
        order = order.lower()
        self.set_trade_order(order)
        try:
            self.driver.find_element(*self.trade_order).click()
        except Exception as e:
            raise RuntimeError(f"Failed to select trade order '{order}': {e}")
        
    def select_trade_order_type(self, order_type):
        #Selects the specified trade order type from dropdown.
        try:
            wait_until_visible(self.driver, 10, self.trade_order_type_dropdown)
            self.driver.find_element(*self.trade_order_type_dropdown).click()
            self.set_trade_order_type(order_type.lower())
            self.driver.find_element(*self.trade_order_type).click()
        except Exception as e:
            raise RuntimeError(f"Failed to select trade order type '{order_type}': {e}")
        
    def input_trade_unit(self, volume):
        try:
            input_field = self.driver.find_element(*self.trade_units_input)
            input_field.click()
            input_field.clear()
            input_field.send_keys(volume)
        except Exception as e:
            raise RuntimeError(f"Failed to input trade unit '{volume}': {e}")
        
    def get_trade_live_buy_price(self):
        try:
            print(self.driver.find_element(*self.trade_live_buy_price).text)
            return float(self.driver.find_element(*self.trade_live_buy_price).text.replace(",", ""))
        except Exception as e:
            raise RuntimeError(f"Failed to get trade live buy price: {e}")
        
    def input_stop_loss_price(self, price):
        try:
            self.driver.find_element(*self.stop_loss_input).click()
            self.driver.find_element(*self.stop_loss_input).send_keys(price)
        except Exception as e:
            raise RuntimeError(f"Failed to input '{price}': {e}")
        
    def input_take_profit_price(self, price):
        try:
            self.driver.find_element(*self.take_profit_input).click()
            self.driver.find_element(*self.take_profit_input).send_keys(price)
        except Exception as e:
            raise RuntimeError(f"Failed to input '{price}': {e}")
        
    def place_trade_order(self):
        try:
            button = self.driver.find_element(*self.place_order_btn)
            is_disabled = button.get_attribute("disabled")
            if is_disabled:
                logging.error("Button is disabled")
            else:
                logging.info("Button is enabled")
                button.click()
                assert self.driver.find_element(*self.trade_confirmation_modal).is_displayed(), "Modal is not visible"
                self.driver.find_element(*self.trade_confirmation_btn).click()
        except Exception as e:
            raise RuntimeError(f"Failed to place an order : {e}")
    
    def edit_trade_order(self):
        try:
            button = self.driver.find_element(*self.place_order_btn)
            is_disabled = button.get_attribute("disabled")
            if is_disabled:
                logging.error("Button is disabled")
            else:
                logging.info("Button is enabled")
                button.click()
                assert self.driver.find_element(*self.trade_confirmation_modal).is_displayed(), "Modal is not visible"
                self.driver.find_element(*self.trade_confirmation_btn).click()
        except Exception as e:
            raise RuntimeError(f"Failed to place an order : {e}")
    
    def edit_open_positions(self, stoploss_price, takeprofit_price):
        try:
            self.driver.find_element(*self.tab_asset_order_type_open_positions).click()
            wait_until_visible(self.driver, 10, self.asset_open_button_edit)
            button = self.driver.find_element(*self.asset_open_button_edit)
            is_disabled = button.get_attribute("disabled")
            if is_disabled:
                logging.error("Edit Open Positions button is disabled")
            else:
                logging.info("Edit Open Positions button is enabled")
                button.click()
                wait_until_visible(self.driver, 10, self.edit_confirmation_modal)
                assert self.driver.find_element(*self.edit_confirmation_modal).is_displayed(), "Modal is not visible"
                input_stoploss_price = self.driver.find_element(*self.edit_input_stoploss_price)
                input_takeprofit_price = self.driver.find_element(*self.edit_input_takeprofit_price)
                input_stoploss_price.click()
                input_stoploss_price.clear()
                input_stoploss_price.send_keys(stoploss_price)
                input_takeprofit_price.click()
                input_takeprofit_price.clear()
                input_takeprofit_price.send_keys(takeprofit_price)
                self.driver.find_element(*self.edit_button_order).click()
                
        except Exception as e:
            raise RuntimeError(f"Failed to edit open positions : {e}")
    
    def partial_close_open_positions(self, size):
        try:
            wait_until_visible(self.driver, 10, self.asset_open_button_close)
            button = self.driver.find_element(*self.asset_open_button_close)
            is_disabled = button.get_attribute("disabled")
            if is_disabled:
                logging.error("Close Open Positions button is disabled")
            else:
                logging.info("Close Open Positions button is enabled")
                button.click()
                wait_until_visible(self.driver, 10, self.confirm_close_order_modal)
                assert self.driver.find_element(*self.confirm_close_order_modal).is_displayed(), "Modal is not visible"
                input = self.driver.find_element(*self.close_order_input_volume)
                input.click()
                input.clear()
                input.send_keys(float(size))
                self.driver.find_element(*self.close_order_input_volume_decrease).click()
                self.driver.find_element(*self.close_order_button_submit).click()
                wait_until_visible(self.driver, 10, self.asset_open_button_close)
                time.sleep(5)
                
        except Exception as e:
            raise RuntimeError(f"Failed to partial close open positions : {e}")
        
    def close_open_positions(self):
        try:
            wait_until_visible(self.driver, 10, self.asset_open_button_close)
            button = self.driver.find_element(*self.asset_open_button_close)
            is_disabled = button.get_attribute("disabled")
            if is_disabled:
                logging.error("Close Open Positions button is disabled")
            else:
                logging.info("Close Open Positions button is enabled")
                button.click()
                wait_until_visible(self.driver, 10, self.confirm_close_order_modal)
                assert self.driver.find_element(*self.confirm_close_order_modal).is_displayed(), "Modal is not visible"
                self.driver.find_element(*self.close_order_button_submit).click()
                wait_until_visible(self.driver, 10, self.asset_open_button_close)
                time.sleep(5)
                
        except Exception as e:
            raise RuntimeError(f"Failed to Close open positions : {e}")
        
    def input_limit_price(self, price):
        try:
            input_field = self.driver.find_element(*self.limit_trade_input_price)
            input_field.click()
            input_field.clear()
            input_field.send_keys(price)
        except Exception as e:
            raise RuntimeError(f"Failed to input Limit price '{price}': {e}")
        
    def select_expiry_type(self, expiry_type):
        #Selects the specified Expiry type from dropdown.
        try:
            wait_until_visible(self.driver, 10, self.limit_expiry_dropdown)
            self.driver.find_element(*self.limit_expiry_dropdown).click()
            if expiry_type.lower() == "good till cancelled":
                self.driver.find_element(*self.limit_expiry_good_till_cancelled).click()
            elif expiry_type.lower() == "good till day":
                self.driver.find_element(*self.limit_expiry_good_till_day).click()
            else:
                logging.error("Expiry type is incorrect, please check again")
        except Exception as e:
            raise RuntimeError(f"Failed to select Expiry type '{expiry_type}': {e}")
    
    def edit_pending_orders(self, input_price=None, stoploss_price=None, takeprofit_price=None, expiry_type=None):
        try:
            self.driver.find_element(*self.tab_asset_order_type_pending_orders).click()
            wait_until_visible(self.driver, 10, self.asset_pending_button_edit)
            button = self.driver.find_element(*self.asset_pending_button_edit)
            is_disabled = button.get_attribute("disabled")
            if is_disabled:
                logging.error("Edit Open Positions button is disabled")
            else:
                logging.info("Edit Open Positions button is enabled")
                button.click()
                wait_until_visible(self.driver, 10, self.edit_confirmation_modal)
                assert self.driver.find_element(*self.edit_confirmation_modal).is_displayed(), "Modal is not visible"
                if input_price!=None:
                    input_price = self.driver.find_element(*self.edit_input_price)
                    input_price.click()
                    input_price.clear()
                    input_price.send_keys(stoploss_price)
                if stoploss_price!=None:
                    input_stoploss_price = self.driver.find_element(*self.edit_input_stoploss_price)
                    input_stoploss_price.click()
                    input_stoploss_price.clear()
                    input_stoploss_price.send_keys(stoploss_price)
                if takeprofit_price!=None:    
                    input_takeprofit_price = self.driver.find_element(*self.edit_input_takeprofit_price)
                    input_takeprofit_price.click()
                    input_takeprofit_price.clear()
                    input_takeprofit_price.send_keys(takeprofit_price)
                if expiry_type!=None:
                    self.select_expiry_type(self, expiry_type)
                self.driver.find_element(*self.edit_button_order).click()
                
        except Exception as e:
            raise RuntimeError(f"Failed to edit open positions : {e}")
    
    def split_the_result_and_extract_variables(self, result_string):
        order_no = result_string.split("#")[1].split(" ")[0]
        symbol      = result_string.split("#")[1].split(" ")[1].split(":")[0]
        size        = result_string.split("Size ")[1].split(" ")[0]
        units       = result_string.split("Units ")[1].split(" ")[0]
        entry_price = result_string.split("@ ")[1]
        return order_no, symbol, size, units, entry_price
    
    def validate_the_order_placed_details_with_compare_to_notifications_and_position_table_details(self, num_order):
        wait_until_invisible(self.driver, 10, self.notification_description)
        #self.driver.find_element(*self.notification_close_btn).click
        self.driver.find_element(*self.notification_selector).click()
        wait_until_visible(self.driver, 10, self.notification_list_result)
        self.set_notification_list_result_item(num_order)
        result_detail = self.driver.find_element(*self.notification_list_result_item).text
        self.driver.find_element(*self.notification_list_result_item).click()
        wait_until_visible(self.driver, 10, self.order_detail_modal)
        self.driver.find_element(By.XPATH, "//form[@class='sc-19cupja-3 iZHyXr']")
        order_no, symbol, size, units, entry_price = self.split_the_result_and_extract_variables(result_detail)
        assert symbol       == self.driver.find_element(*self.order_detail_symbol).click()
        assert order_no     == self.driver.find_element(*self.order_detail_order_no).text
        assert size         == self.driver.find_element(*self.order_detail_size).text
        assert units        == self.driver.find_element(*self.order_detail_unit).text
        assert entry_price  == self.driver.find_element(*self.order_detail_entry_price).text
        self.driver.find_element(*self.order_detail_close_btn).click()
        