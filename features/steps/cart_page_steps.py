from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify "Your cart is empty" message is shown')
def verify_text_is_empty_shown(context):
    actual_text = context.driver.find_element(By.XPATH, "//*[text()='Your cart is empty']").text
    assert 'Your cart is empty' in actual_text, f"Expected text not in {actual_text}"
    print("Test Case Passed")