import pytest
import time
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.login_user
class TestUserAddToBasketFromProductPage:
  @pytest.fixture(scope="function", autouse=True)
  def setup(self, browser):
    page = LoginPage(browser, link)
    page.open()
    email = str(time.time()) + "@fakemail.org"
    password = 'Test123456'
    page.register_new_user(email, password)
    page.should_be_authorized_user()

  def test_user_cant_see_success_message(self, browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_not_be_success_message()

  @pytest.mark.need_review 
  def test_user_can_add_product_to_basket(self, browser):
    page = ProductPage(browser, product_link)
    page.open() 
    book_title = page.get_book_title()
    page.click_on_the_btn_add_to_basket()
    book_title_from_message = page.get_book_title_from_message()
    page.should_be_equal_book_titles(book_title, book_title_from_message)

@pytest.mark.need_review    
@pytest.mark.parametrize('promo_code', [0, 1, 2, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, promo_code):
  link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}'.format(promo_code)
  page = ProductPage(browser, link)
  page.open() 
  book_title = page.get_book_title()
  page.click_on_the_btn_add_to_basket()
  page.solve_quiz_and_get_code() 
  book_title_from_message = page.get_book_title_from_message()
  page.should_be_equal_book_titles(book_title, book_title_from_message)

@pytest.mark.need_review  
def test_guest_can_go_to_login_page_from_product_page(browser):
  page = ProductPage(browser, product_link)
  page.open()
  page.go_to_login_page()

@pytest.mark.need_review   
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
  page = ProductPage(browser, product_link)
  page.open()
  browser.delete_all_cookies()
  page.go_to_cart()
  page = BasketPage(browser, browser.current_url)
  page.check_basket_items()
  page.check_epmty_basket_message()


def test_guest_cant_see_success_message(browser):
  page = ProductPage(browser, product_link)
  page.open()
  page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
  page = ProductPage(browser, product_link)
  page.open()
  page.should_be_login_link()

@pytest.mark.xfail(reason='Need')   
def test_message_disappeared_after_adding_product_to_basket(browser):
  page = ProductPage(browser, product_link)
  page.open()
  page.click_on_the_btn_add_to_basket()
  page.message_should_be_disappeared_after_adding_product_to_basket() 

@pytest.mark.xfail(reason='Need')   
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
  page = ProductPage(browser, product_link)
  page.open()
  page.click_on_the_btn_add_to_basket()
  page.should_not_be_success_message()

@pytest.mark.xfail(reason='Need')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.click_on_the_btn_add_to_basket()
    page.should_not_be_success_message()
