from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_IS_EMPTY_MESSAGE = (By.XPATH, "//*[text()='Your cart is empty']")
ADD_TO_CART_UNDER_BTN = (By.ID, "addToCartButtonOrTextIdFor79962218")
ADD_TO_CART_RIGHT_SIDE_BTN = (By.CSS_SELECTOR, 'button[data-test="shippingButton"]')
DECLINE_BTN = (By.CSS_SELECTOR, 'button[data-test="espDrawerContent-declineCoverageButton"]')
TOTAL_PRISE_SHOWN = (By.XPATH, "//*[text()='$171.64 total']")


@then('Verify "Your cart is empty" message is shown')
def verify_text_is_empty_shown(context):
    actual_text = context.driver.find_element(*CART_IS_EMPTY_MESSAGE).text
    assert 'Your cart is empty' in actual_text, f"Expected text not in {actual_text}"
    print("Test Case Passed")


@when('Click at Add to cart button under the image of product')
def click_at_add_to_cart_under_image(context):
    context.driver.find_element(*ADD_TO_CART_UNDER_BTN).click()
    sleep(6)


@when('Click at Add to cart button from right side navigation menu')
def click_at_add_to_cart_from_right_menu(context):
    context.driver.find_element(*ADD_TO_CART_RIGHT_SIDE_BTN).click()
    sleep(6)


@when('Click at Decline coverage button')
def click_at_decline_coverage_button(context):
    context.driver.find_element(*DECLINE_BTN).click()
    sleep(6)


@then('Verify total price is shown')
def verify_total_price_is_shown(context):
    actual_text = context.driver.find_element(*TOTAL_PRISE_SHOWN).text
    assert '$171.64 total' in actual_text, f'Expected text "$171.64 total" not in {actual_text}'
    print("Test Case Passed")