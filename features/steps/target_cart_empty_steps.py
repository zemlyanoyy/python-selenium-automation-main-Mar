from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get("https://www.target.com/")


@when('Click on the Cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/CartLink']").click()
    sleep(6)


@then('Verify "Your cart is empty" message is shown')
def verify_text_empty_shown(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    assert 'Your cart is empty' in actual_text, f"Expected text not in {actual_text}"
    print('Test Case Passed')


