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
driver.get('https://www.amazon.com/')

# By CSS Selectors, ID
driver.find_elements(By.CSS_SELECTOR, "input#twotabsearchtextbox")
driver.find_elements(By.CSS_SELECTOR, "#twotabsearchtextbox")

# By CSS Selectors, classes
driver.find_elements(By.CSS_SELECTOR, "input.nav-progressive-attribute")
driver.find_elements(By.CSS_SELECTOR, "input.nav-input.nav-progressive-attribute")
driver.find_elements(By.CSS_SELECTOR, ".nav-input.nav-progressive-attribute")
driver.find_elements(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input")   # ID + Class

# By CSS Selectors, attributes
driver.find_elements(By.CSS_SELECTOR, "input[placeholder='Search Amazon']")
driver.find_elements(By.CSS_SELECTOR, "[placeholder='Search Amazon']")
driver.find_elements(By.CSS_SELECTOR, "input#twotabsearchtextbox.input[placeholder='Search Amazon']")

# By CSS Selectors, multiple attributes
driver.find_elements(By.CSS_SELECTOR, ".input[placeholder='Search Amazon'][type='text']")

# Contains: *=
driver.find_elements(By.CSS_SELECTOR, "a[href*='topnav_lang']")

# Contains from the Target Website as an Example
driver.find_elements(By.CSS_SELECTOR, "h1[class*='styles__StyledHeading']")

# Note: CSS does NOT support text, for text we use XPATH!!!