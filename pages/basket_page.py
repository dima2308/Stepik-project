from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
  def check_basket_items(self):
    assert self.is_not_element_present(*BasketPageLocators.CART_ITEMS), "Basket not epmty"

  def check_epmty_basket_message(self):
    text_empty = self.browser.find_element(*BasketPageLocators.CART_EMPTY_MESSAGE).text
    assert 'Your basket is empty.' in text_empty