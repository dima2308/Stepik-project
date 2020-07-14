from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_on_the_btn_add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET).click()

    def get_book_title(self):
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE)
        return book_title.text

    def get_book_title_from_message(self):
        book_title_from_message = self.browser.find_element(*ProductPageLocators.MESSAGE_TITLE_BOOK)
        return book_title_from_message.text

    @staticmethod
    def should_be_equal_book_titles(title1, title2):
        assert title1 == title2

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def message_should_be_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), "Message isn't disappeared after adding product to basket"
