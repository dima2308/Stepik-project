from selenium.webdriver.common.by import By


class BasePageLocators: 
  LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
  LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
  CART_BUTTON = (By.CSS_SELECTOR, ".btn-group > a:nth-child(1)")
  USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
  CART_ITEMS = (By.CLASS_NAME, "basket-items")
  CART_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner P")

class MainPageLocators:
  pass

class LoginPageLocators:
  LOGIN_FORM = (By.ID, "login_form")
  REGISTER_FORM = (By.ID, "register_form")
  EMAIL = (By.ID, "id_registration-email")
  PASSWORD = (By.ID, "id_registration-password1")
  PASWWORD_CONFIRM = (By.ID, "id_registration-password2")
  REGISTER_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators:
  BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-add-to-basket")
  BOOK_TITLE = (By.CSS_SELECTOR, ".page_inner h1")
  BOOK_PRICE = (By.CSS_SELECTOR, ".page_inner.price_color")
  MESSAGE_TITLE_BOOK = (By.CSS_SELECTOR, "div.alert:nth-child(1) > div:nth-child(2) > strong")
  SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1)")