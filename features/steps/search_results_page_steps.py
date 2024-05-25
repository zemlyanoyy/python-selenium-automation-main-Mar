from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
SEARCH_RESULT_SHOWN = (By.XPATH, "//div[@data-test='resultsHeading']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")


@when('Search for {product}')
def search_product(context, product):

    context.app.header.search_product(product)   # context.driver.find_element(*SEARCH_INPUT).send_keys(product)
    # context.driver.find_element(*SEARCH_BTN).click()
    # sleep(10)   # we will kip this one

@then('Search results for {expected_product} are shown')
def verify_search_results_correct(context, expected_product):
    # actual_text = context.driver.find_element(*SEARCH_RESULT_SHOWN).text
    # assert expected_product in actual_text, f"Expected word {expected_product} not in {actual_text}"
    # print("Test Case Passed")
    context.app.search_reults_page.verify_search_results(expected_product)

@then('Verify that every product has a name and an image')
def verify_products_name_img(context):

    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_products = context.driver.find_elements(*LISTINGS)

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        print(title)
        assert title, 'Product title not shown'
        product.find_element(*PRODUCT_IMG)