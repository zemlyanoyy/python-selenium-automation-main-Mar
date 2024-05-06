from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
SEARCH_RESULT_SHOWN = (By.XPATH, "//div[@data-test='resultsHeading']")

@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(*SEARCH_INPUT).send_keys(product)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(10)   # we will kip this one


@then('Search results for {expected_product} are shown')
def verify_search_results_correct(context, expected_product):
    actual_text = context.driver.find_element(*SEARCH_RESULT_SHOWN).text
    assert expected_product in actual_text, f"Expected word {expected_product} not in {actual_text}"
    print("Test Case Passed")

