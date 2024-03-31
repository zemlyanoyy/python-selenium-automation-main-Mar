from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')
search_word = 'lamp'

# input search word
driver.find_element(By.ID, 'search').send_keys(search_word)

# Click on search button
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(6)

# Verify search working
actual_text = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
assert search_word in actual_text, f"Expected word {search_word} not found in actual text {actual_text}"

print("Test Case Passed")
driver.quit()
