from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then


RIGHT_SIDE_SIGN_IN = (By.XPATH, "//span[contains(@class, 'styles__ListItemText')]")
SIGN_IN_FORM_HEADER = (By.XPATH, "//span[text()='Sign into your Target account']")


@when('From right side navigation menu, click Sign in')
def click_on_right_side_signin(context):
    context.driver.find_element(*RIGHT_SIDE_SIGN_IN).click()
    context.wait.until(
        EC.invisibility_of_element_located(RIGHT_SIDE_SIGN_IN),
        message="Sign in button from right side nav menu did not disappear"
    )


@then('Verify Sign In form opened')
def verify_signin_form_opened(context):
    actual_text = context.driver.find_element(*SIGN_IN_FORM_HEADER).text
    assert 'Sign into your Target account' in actual_text, f'Expected text not in {actual_text}'
    print("Test Case Passed")