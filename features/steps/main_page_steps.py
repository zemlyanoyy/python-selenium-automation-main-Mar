from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when
from time import sleep



# SEARCH_INPUT = (By.ID, 'search')
# SEARCH_BTN = (.........)
CART_ICON = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")
SIGN_IN = (By.XPATH, "//span[contains(@class, 'styles__LinkText')]")

@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get("https://www.target.com/")


@when('Click on the Cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(6)
    # context.wait.until(
    #     EC.invisibility_of_element_located(CART_ICON),
    #     message="The cart icon did not disappear"
    # )


@when('Click Sign In')
def click_on_signin(context):
    context.driver.find_element(*SIGN_IN).click()
