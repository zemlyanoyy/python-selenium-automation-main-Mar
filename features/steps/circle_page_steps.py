from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

TEN_BENEFITS = (By.CSS_SELECTOR, 'div[class="cell-item-content"]')


@given('Open Target Circle page')
def open_circle_page(context):
    context.driver.get("https://www.target.com/l/target-circle/-/N-pzno9")


@when('Search the benefit boxes')
def search_benefit_boxes(context):
    context.driver.find_elements(*TEN_BENEFITS)


@then('Verify 10 benefit boxes are shown')
def verify_10_benefit_boxes(context):
    actual_result = context.driver.find_elements(*TEN_BENEFITS)
    assert len(actual_result) == 10, f'Expected amount of benefit boxes are not in {actual_result}'
    print("Test Case Passed")
