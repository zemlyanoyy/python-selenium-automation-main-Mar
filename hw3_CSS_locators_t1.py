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
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')


# Amazon Logo
driver.find_elements(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')

# Create account
driver.find_elements(By.CSS_SELECTOR, 'h1.a-spacing-small')

# Your name
driver.find_elements(By.CSS_SELECTOR, '#ap_customer_name')

# Email
driver.find_elements(By.CSS_SELECTOR, '#ap_email')

# Password
driver.find_elements(By.CSS_SELECTOR, '#ap_password')

# Password must be at least 6 characters
driver.find_element(By.XPATH, "//div[contains(text(),'at least 6 characters.')and@class='a-alert-content']")

# Re-enter password
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

# Create your Amazon account
driver.find_element(By.CSS_SELECTOR, '#continue')


# Conditions of Use
driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='condition']")

# Privacy Notice
driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='privacy']")


# Sign in
driver.find_element(By.XPATH, "//a[contains(text(),'Sign in')and@class='a-link-emphasis']")