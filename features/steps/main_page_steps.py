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


@when('Click Sign In')
def click_on_signin(context):
    context.driver.find_element(By.XPATH, "//span[contains(@class, 'styles__LinkText')]").click()