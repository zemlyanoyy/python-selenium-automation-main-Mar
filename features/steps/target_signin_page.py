from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# @given('Open Target main page')
# def open_target_main_page(context):
#     context.driver.get("https://www.target.com/")


@when('Click Sign In')
def click_on_signin(context):
    context.driver.find_element(By.XPATH, "//span[contains(@class, 'styles__LinkText')]").click()


@when('From right side navigation menu, click Sign in')
def click_on_right_side_signin(context):
    context.driver.find_element(By.XPATH, "//span[contains(@class, 'styles__ListItemText')]").click()
    sleep(6)


@then('Verify Sign In form opened')
def verify_signin_form_opened(context):
    actual_text = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    assert 'Sign into your Target account' in actual_text, f'Expected text not in {actual_text}'
    print("Test Case Passed")