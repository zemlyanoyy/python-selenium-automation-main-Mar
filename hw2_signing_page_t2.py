from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# Create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open the url
driver.get('https://www.target.com/')

# Click Signin button
driver.find_element(By.XPATH, "//span[contains(@class, 'styles__LinkText')]").click()

# Click Signin from side navigation
driver.find_element(By.XPATH, "//li[contains(@class, 'styles__ListItemLi')]").click()
sleep(6)

# "Sign into your Target account" text is shown
actual_text = driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
assert 'Sign into your Target account' in actual_text, f'Expected text "Sign into your Target account" not in {actual_text}'

# Sign in button is shown
driver.find_element(By.ID, 'login')

print('Test case passed')
driver.quit()
