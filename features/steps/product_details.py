from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, '[aria-label="Carousel"] ul li')
SELECTED_COLOR = (By.CSS_SELECTOR, 'div[data-test="@web/VariationComponent"] div[class*="styles__StyledHeaderWrapperDiv"]')


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(10)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Green', 'Red', 'Black - Out of Stock', 'Dark Blue - Out of Stock', 'Light Blue - Out of Stock', 'Lime - Out of Stock', 'Orange - Out of Stock', 'Pink - Out of Stock', 'Purple - Out of Stock', 'Rose GOld - Out of Stock', 'Teal - Out of Stock', 'White - Out of Stock', 'Yellow - Out of Stock']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'

